import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from fetching_datas import fetch_cve_cvss_info_nvd, fetch_references, fetch_exploit
from check_cves import is_valid_cve_for_nvd, is_valid_cve_for_exploit
from docx import Document
# Function to save the report to a text file
def save_report_to_txt(directory, cve_id, report):
    file_name = os.path.join(directory, f"{cve_id}_report.txt")
    try:
        if is_valid_cve_for_nvd(cve_id) and is_valid_cve_for_exploit(cve_id):
            with open(file_name, "w") as file:
                file.write(report)
            print(f"Report saved to {file_name}")
            os.startfile(file_name)
        else:
            print(f"Error saving the report to {file_name}: {str(e)}")
    except Exception as e:
        print(f"Error saving the report to {file_name}: {str(e)}")
# Function to save the report to a PDF file
def save_report_to_pdf(directory, cve_id, report):
    # Construct the file name for the PDF report
    file_name = os.path.join(directory, f"{cve_id}_report.pdf")

    try:
        # Check if the CVE ID is valid for both NVD and Exploit
        if is_valid_cve_for_nvd(cve_id) and is_valid_cve_for_exploit(cve_id):
            # Create a PDF document
            doc = SimpleDocTemplate(file_name, pagesize=letter)
            styles = getSampleStyleSheet()
            story = []

            # Add the title to the PDF
            story.append(Paragraph("CVE Information Report", styles["Title"]))
            story.append(Spacer(1, 12))

            # Add the CVE ID to the PDF
            story.append(Paragraph(f"CVE ID: {cve_id}", styles["Normal"]))

            # Add the CVE summary to the PDF
            nvd_data = fetch_cve_cvss_info_nvd(cve_id)
            if nvd_data:
                story.append(Spacer(1, 12))
                story.append(Paragraph(f"Summary: {nvd_data['summary']}", styles["Normal"]))

                # Add CVSS information to the PDF
                story.append(Spacer(1, 12))
                story.append(Paragraph(f"CVSS Base Score: {nvd_data['cvss_score']}", styles["Normal"]))
                story.append(Paragraph(f"CVSS Vector: {nvd_data['cvss_vector']}", styles["Normal"]))

            # Add references to the PDF
            story.append(Spacer(1, 12))
            story.append(Paragraph("References:", styles["Normal"]))
            references = fetch_references(cve_id)
            for i, reference in enumerate(references, start=1):
                story.append(Paragraph(f"Reference {i}: {reference}", styles["Normal"]))

            # Add exploit script information to the PDF
            story.append(Spacer(1, 12))
            story.append(Paragraph("Exploit Script:", styles["Normal"]))
            exploit_script = fetch_exploit(cve_id)
            story.append(Paragraph(f"{exploit_script}", styles["Normal"]))

            # Build and save the PDF
            doc.build(story)

            # Notify the user about the successful PDF generation
            print(f"Report saved to {file_name}")

            # Open the PDF file using the default system viewer
            os.startfile(file_name)
        else:
            print(f"Error saving the report to {file_name}: CVE ID is not valid for both NVD and Exploit.")
    except Exception as e:
        print(f"Error saving the report to {file_name}: {str(e)}")


# Function to save the report to a DOCX file
def save_report_to_docx(directory, cve_id, report):
    file_name = os.path.join(directory, f"{cve_id}_report.docx")
    try:
        if is_valid_cve_for_nvd(cve_id) and is_valid_cve_for_exploit(cve_id):
            doc = Document()
            doc.add_paragraph(report)
            doc.save(file_name)
            print(f"Report saved to {file_name}")
            os.startfile(file_name)
    except Exception as e:
        print(f"Error saving the report to {file_name}: {str(e)}")
