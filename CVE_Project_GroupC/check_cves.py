import re
# Function to check if a CVE ID is valid for exploit_db
def is_valid_cve_for_exploit(cve_id):
    # Define a regular expression pattern for the CVE ID format
    pattern = R'^CVE-(20[0-2]\d|2023)-\d{4,5}$'
    
    # Use re.match to check if the provided CVE ID matches the pattern
    if re.match(pattern, cve_id):
        return True  # Valid CVE ID
    else:
        return False  # Invalid CVE ID

# Function to check if a CVE ID is valid for NVD
def is_valid_cve_for_nvd(cve_id):
    # Define a regular expression pattern for the CVE ID format
    pattern = R'^CVE-(198[8-9]|199\d|200\d|201[0-9]|202[0-3])-\d{4,5}$'
    
    # Use re.match to check if the provided CVE ID matches the pattern
    if re.match(pattern, cve_id):
        return True  # Valid CVE ID
    else:
        return False  # Invalid CVE ID
