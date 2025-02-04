import os
import re
import subprocess

class RapidBot:
    def __init__(self):
        self.privacy_issues = []

    def scan_windows_settings(self):
        print("Scanning Windows settings for potential privacy leaks...")
        # Example: Check if location services are enabled
        location_services_cmd = 'powershell "Get-ItemProperty -Path HKLM:\\SYSTEM\\CurrentControlSet\\Services\\lfsvc\\Service\\Configuration | Select-Object -ExpandProperty Status"'
        status = subprocess.check_output(location_services_cmd, shell=True).decode().strip()
        
        if status != '0':
            self.privacy_issues.append("Location services are enabled.")
        else:
            print("Location services are disabled.")

    def scan_installed_applications(self):
        print("Scanning installed applications for potential privacy leaks...")
        # List of common applications known for privacy issues
        suspicious_apps = ['Skype', 'Zoom', 'Google Chrome']
        installed_apps_cmd = 'powershell "Get-ItemProperty HKLM:\\Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\* | Select-Object DisplayName"'
        installed_apps = subprocess.check_output(installed_apps_cmd, shell=True).decode()

        for app in suspicious_apps:
            if re.search(app, installed_apps, re.IGNORECASE):
                self.privacy_issues.append(f"Application '{app}' is installed, which might have privacy concerns.")

    def report_issues(self):
        if not self.privacy_issues:
            print("No potential privacy leaks found.")
        else:
            print("Potential privacy leaks identified:")
            for issue in self.privacy_issues:
                print(f"- {issue}")

    def run(self):
        self.scan_windows_settings()
        self.scan_installed_applications()
        self.report_issues()

if __name__ == "__main__":
    bot = RapidBot()
    bot.run()