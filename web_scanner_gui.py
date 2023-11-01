import requests
import tkinter as tk
from tkinter import scrolledtext, messagebox

def scan_url(base_url, text_area):
    paths = [
     "/admin",
        "/login",
        "/wp-admin",  # Wordpress admin panel
        "/.git",  # Exposed .git directory
        "/.env",  # Exposed environment variables
        "/.htaccess",  # Exposed server configuration
        "/wp-content/", #wordpress content
        "/wp-includes/", #wordpress core
         "/wp-includes/",  # WordPress core files
        "/administrator/",  # Joomla admin login
        "/user/login",  # Drupal login page
        "/phpmyadmin/",  # phpMyAdmin database manager
        "/phppgadmin/",  # phpPgAdmin database manager for PostgreSQL
        "/adminer.php",  # Adminer database management tool
        "/.svn/",  # Exposed Subversion directory
        "/.git/config",  # Exposed .git configuration
        "/robots.txt",  # Robots.txt file
        "/.htaccess",  # Apache server configuration
        "/.htpasswd",  # Apache password file
        "/.bash_history",  # Bash history file
        "/.DS_Store",  # macOS folder settings
        "/backup.tar.gz",  # Possible backup file
        "/backup.zip",  # Possible backup file
        "/database.sql",  # Possible backup file
        "/error.log",  # Server error logs
        "/install.php",  # CMS setup files
        "/setup.php",  # CMS setup files
        "/readme.html",  # Application readme
        "/README.md",  # Application readme
        "/cpanel/",  # cPanel login
        "/webmail/",  # Webmail login
        "/swag/",  # Swagger UI
        "/_profiler/",  # Symfony web debug toolbar
        "/info.php",  # File with phpinfo() output
        "/apidoc/",  # API documentation
        "/api/",  # Common API endpoint
        "/graphql",  # GraphQL endpoint
        "/api/debug",  # Possible debugging endpoint for APIs
        "/.git"  # Exposed .git directory
        "/phpinfo.php", # File with phpinfo() output
        "/info.php",
        "/.env",  # Exposed environment variables
        "/test.php",
        "/backup",
        "/db_backup",
        "/backup.sql",
        "/db_backup.sql",
        "/config.php",  # Common configuration file
        "/wp-config.php",  # WordPress configuration file
        "/sitemap.xml",  # May give a layout of all the URLs of the application
    ]

    for path in paths:
        url = base_url.rstrip('/') + path
        try:
            response = requests.get(url)
            if response.status_code == 200:
                text_area.insert(tk.END, f"[!] Potential Issue Found at: {url}\n")
        except Exception as e:
            text_area.insert(tk.END, f"[ERROR] Could not scan {url}. Reason: {str(e)}\n")
    messagebox.showinfo("Scan Complete", "The scan is complete.")

def clear_text_area(text_area):
    text_area.delete('1.0', tk.END)

def main():
    root = tk.Tk()
    root.title("Web Scanner")

    label = tk.Label(root, text="Enter the base URL (e.g., https://example.com):")
    label.pack(padx=20, pady=5)

    url_entry = tk.Entry(root, width=50)
    url_entry.pack(padx=20, pady=5)

    button_frame = tk.Frame(root)
    button_frame.pack(padx=20, pady=10)

    scan_button = tk.Button(button_frame, text="Scan URL", command=lambda: scan_url(url_entry.get(), text_area))
    scan_button.pack(side=tk.LEFT)

    clear_button = tk.Button(button_frame, text="Clear", command=lambda: clear_text_area(text_area))
    clear_button.pack(side=tk.LEFT)

    text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20)
    text_area.pack(padx=20, pady=10)

    root.mainloop()

if __name__ == '__main__':
    main()
