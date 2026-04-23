import requests
import sys
import os

# ENVs
DOJO_URL = os.getenv("DEFECTDOJO_URL", "http://localhost:8080")
API_KEY = os.getenv("DEFECTDOJO_API_KEY")
PRODUCT_ID = os.getenv("DEFECTDOJO_PRODUCT_ID")
ENGAGEMENT_ID = os.getenv("DEFECTDOJO_ENGAGEMENT_ID")

def upload_to_dojo(file_path, scan_type):
    if not API_KEY:
        print("[ERROR] DEFECTDOJO_API_KEY is not set")
        return

    import_url = f"{DOJO_URL.rstrip('/')}/api/v2/import-scan/"
    
    headers = {
        "Authorization": f"Token {API_KEY}"
    }
    
    # Параметры загрузки
    data = {
        "engagement": ENGAGEMENT_ID,
        "scan_type": scan_type,
        "active": True,
        "verified": True,
        "close_old_findings": True,
        "push_to_jira": False
    }
    
    try:
        with open(file_path, "rb") as f:
            files = {"file": f}
            response = requests.post(import_url, headers=headers, data=data, files=files)

        if response.status_code in [200, 201]:
            print(f"[SUCCESS] {scan_type} report uploaded successfully!")
        else:
            print(f"[ERROR] Failed to upload {scan_type}. Status: {response.status_code}")
            print(response.text)
    except FileNotFoundError:
        print(f"[ERROR] File not found: {file_path}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python dojo_upload.py <file_path> <scan_type>")
    else:
        upload_to_dojo(sys.argv[1], sys.argv[2])
