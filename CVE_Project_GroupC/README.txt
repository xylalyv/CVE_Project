Project Name: CVE_Project_GroupC

Description:

This Python script fetches information about a Common Vulnerabilities and Exposures (CVE) ID from various sources, including the National Vulnerability Database (NVD), Vulmon, and Exploit-DB. It generates a detailed report containing CVE details, CVSS scores, references, and, if available, an exploit script for the given CVE ID. The user can choose to save the report in TXT, PDF, or DOCX format.

Dependencies:

- Python 3.x
- The following Python libraries:
  - requests
  - BeautifulSoup (bs4)
  - docx
  - reportlab
  - webbrowser

Instructions for Running the Project:

1. Ensure you have Python 3.x installed on your system. You can download it from https://www.python.org/downloads/.

2. Install the required Python libraries using pip. Open your command prompt or terminal and run the following commands:

- pip install requests
- pip install beautifulsoup4
- pip install python-docx
- pip install reportlab
- pip install urllib3

3. Clone this repository to your local machine or download the project files.

4. Open a command prompt or terminal and navigate to the project directory.

5. Run the script by executing the following command:

python CVE_Project_GroupC.py

6. Follow the on-screen instructions:

- Enter a CVE ID when prompted.
- Choose the format (txt, pdf, or docx) in which you want to save the report.
- The report will be saved in the project directory and opened in your default application for that file type.
- The top references (up to 5) will be opened in your web browser.

7. Enjoy using the CVE_Project_GroupC!

Note: Make sure you have an active internet connection to fetch data from online sources.
