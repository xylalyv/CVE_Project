import requests
from bs4 import BeautifulSoup
import webbrowser
from urllib.parse import urlparse
from check_cves import is_valid_cve_for_nvd, is_valid_cve_for_exploit

# Function to fetch CVE CVSS information from NVD
def fetch_cve_cvss_info_nvd(cve_id):
    url = f"https://nvd.nist.gov/vuln/detail/{cve_id}"
    try:
        if is_valid_cve_for_nvd(cve_id):
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for HTTP errors (4xx and 5xx)
            soup = BeautifulSoup(response.text, 'html.parser')
            # Extract summary and CVSS information from the NVD page
            summary = soup.find('p', {'data-testid': 'vuln-description'}).text
            cvss_score = soup.find('span', {'class': 'severityDetail'}).text
            cvss_vector = soup.find('span', {'data-testid' : 'vuln-cvss3-nist-vector'}).text
            return {'summary': summary, 'cvss_score': cvss_score, 'cvss_vector': cvss_vector}
    except requests.exceptions.RequestException as e:
        print(f"Request error while fetching CVE information from NVD for {cve_id}: {str(e)}")
    except Exception as e:
        print(f"An error occurred while fetching CVE information from NVD for {cve_id}: {str(e)}")
    
    return None

# Function to fetch references with technical information
def fetch_references(cve_id):
    references = []
    try:
        url = f"https://vulmon.com/vulnerabilitydetails?qid={cve_id}"
        response = requests.get(url)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find the section containing references
            reference_section = soup.find('div', {'class': 'ui list ex5'})
            
            if reference_section:
                # Extract links from the reference section
                reference_links = reference_section.find_all('a', href=True)
                for link in reference_links[:5]:
                    reference_url = link['href']
                    try:
                        # Try to parse the URL and check if it's valid
                        parsed_url = urlparse(reference_url)
                        if parsed_url.scheme and parsed_url.netloc:
                            # Attempt to fetch the content of the reference URL
                            reference_response = requests.get(reference_url)
                            if reference_response.status_code == 200:
                                references.append(reference_url)
                            else:
                                print(f"Skipping broken link: {reference_url}")
                        else:
                            print(f"Skipping invalid URL: {reference_url}")
                    except Exception as e:
                        print(f"An error occurred while processing URL: {reference_url} - {str(e)}")
                    
                if not references:
                    print(f"No valid references found for {cve_id}")
            else:
                print(f"No reference section found for {cve_id}")
        else:
            print(f"Error fetching references from vulmon.com for {cve_id}")
    except Exception as e:
        print(f"An error occurred while fetching references: {str(e)}")
    
    return references

# Function to check if an exploit is available on Exploit DB and fetch the script
def fetch_exploit(cve_id):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    }
    search_url = f"https://www.exploit-db.com/search?cve={cve_id}"
    try:
        response = requests.get(search_url, headers= headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return
    if response.status_code == 200 and is_valid_cve_for_exploit(cve_id):
        webbrowser.open(search_url)