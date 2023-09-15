import webbrowser
import os
from saving_datas import  save_report_to_txt, save_report_to_docx, save_report_to_pdf
from fetching_datas import fetch_cve_cvss_info_nvd, fetch_references, fetch_exploit

def main():
    # Prompt the user to input a CVE ID
    cve_id = input("Enter the CVE ID: ")

    # Fetch data from different sources
    nvd_data = fetch_cve_cvss_info_nvd(cve_id)
    references = fetch_references(cve_id)
    exploit_script = fetch_exploit(cve_id)

    # Generate a report
    report = "CVE Information Report".center(150)
    report += f"\n\nCVE ID: {cve_id}\n"
    if nvd_data:
        report += "\nSummary\n\n"
        report += nvd_data['summary'] + "\n\n"
        report += "CVSS Information\n"
        report += "\nBase Score:" + nvd_data['cvss_score']
        report += nvd_data['cvss_vector'] + "\n"
    else:
        report += "\nNo CVE information found.\n"

    report += "\nReferences\n"
    if references:
        for i, reference in enumerate(references, start=1):
            report += f"\nReference {i}: {reference}"
    else:
        report += "\nNo references found.\n"
    report += "\n\nExploit Script:\n"
    if exploit_script:
        report += exploit_script
    else:
        report += "\nNo exploit script found.\n"

    print(report)

    # Prompt the user for the saving format
    while True:
        save_format = input("Choose a format to save the report (txt, pdf, docx): ").lower()
        if save_format in ['txt', 'pdf', 'docx']:
            break
        else:
            print("Invalid format. Please choose 'txt', 'pdf', or 'docx'.")

    # Prompt the user for the directory to save the report
    directory = os.getcwd()

    # Create the directory if it doesn't exist
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except Exception as e:
            print(f"Error creating directory {directory}: {str(e)}")

    # Save the report in the chosen format and directory
    if save_format == 'txt':
        save_report_to_txt(directory, cve_id, report)
    elif save_format == 'pdf':
        save_report_to_pdf(directory, cve_id, report)
    elif save_format == 'docx':
        save_report_to_docx(directory, cve_id, report)

    # Open the top references in a web browser
    for i, reference in enumerate(references[:5], start=1):
        try:
            webbrowser.open_new_tab(reference)
        except Exception as e:
            print(f"Error opening reference {i}: {str(e)}")

if __name__ == "__main__":
    main()
