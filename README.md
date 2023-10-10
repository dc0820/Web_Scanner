# **Web_Scanner**

## **About**
This web vulnerability scanner, `web_scanner.py`, is a Python-based tool created by Daniel Cook. It aims to help you identify common vulnerable endpoints and misconfigurations on your website by scanning for well-known paths. Remember always to test only on platforms you have permission to scan to avoid legal consequences.

## **Features**
- **Path Enumeration**: The tool tests a set of predefined paths that are commonly known to have vulnerabilities or expose sensitive information. These include but aren't limited to:
    - Admin panels like `/admin`, `/login`, and `/wp-admin`.
    - Exposed directories and files like `/.git`, `/.env`, and `/.htaccess`.
    - Backup files like `/backup.tar.gz`, `/backup.zip`, and `/database.sql`.
    - CMS specific paths, e.g., WordPress (`/wp-content/`, `/wp-includes/`), Joomla (`/administrator/`), and Drupal (`/user/login`).
    - Database management tools like `/phpmyadmin/` and `/adminer.php`.
    - And many more...

- **Status Code Checker**: For each path, the tool checks if it's accessible (HTTP 200 status code).
  
- **Exception Handling**: In cases where a particular URL can't be scanned, it provides the reason for the error, ensuring the tool doesn't crash midway.

## **How to Use**
1. **Run the script**: Execute the `python3 web_scanner.py` script.
2. **Enter the Base URL**: When prompted, input the base URL of the site you want to scan (e.g., `https://example.com`).
3. **View Results**: The script will then iterate over the predefined paths, providing output for potential issues and errors. Once completed, you'll see a "Scan Complete." message.

## **Pre-requisites**
To run this tool, ensure you have:
- Python installed on your machine.
- The `requests` library. Install it using:
  `pip install requests`


## **Caution**
Always ensure you have the appropriate permissions before scanning any web application. Unauthorized scanning and testing can lead to legal actions against you. This tool is intended for educational purposes and ethical use only.

## **Feedback & Contribution**
Your feedback is invaluable. If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request. If you have additional paths or vulnerabilities that should be checked, your contributions are always welcome!

---

Best,
**Daniel Cook**


