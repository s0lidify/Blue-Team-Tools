import os
import datetime

def get_input(prompt, default=None):
    """Helper function to get user input with a default value."""
    user_input = input(prompt).strip()
    return user_input if user_input else default

def create_soc_incident_report():
    print("\nSOC Incident Report Generator")
    print("="*40)

    # Collecting user inputs
    incident_id = get_input("Incident ID: ")
    incident_datetime = get_input("Incident Date & Time (Press Enter for current): ", 
                                  datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    reporter_name = get_input("Reporter Name: ")
    incident_type = get_input("Incident Type (e.g., Phishing, Malware, DDoS): ")
    severity = get_input("Severity (Low/Medium/High/Critical): ")
    affected_systems = get_input("Affected Systems (comma-separated): ")
    impact_assessment = get_input("Impact Assessment (e.g., Data loss, Downtime): ")
    attacker_ip_geo = get_input("Attacker IP & Geo-location: ")
    compromised_accounts = get_input("Compromised Accounts (if any): ")
    iocs = get_input("Indicators of Compromise (IOCs): ")
    logs_referred = get_input("Logs to Refer (e.g., SIEM, Firewall, Event Logs): ")
    response_actions = get_input("Response Actions Taken: ")
    mitigation_measures = get_input("Mitigation Measures Implemented: ")
    description = get_input("Incident Description: ")

    # Formatting report
    report_content = f"""
    ================================
        SOC INCIDENT REPORT
    ================================
    Incident ID: {incident_id}
    Incident Date & Time: {incident_datetime}
    Reporter Name: {reporter_name}
    Incident Type: {incident_type}
    Severity: {severity}
    ------------------------------
    Affected Systems: {affected_systems}
    Impact Assessment: {impact_assessment}
    Attacker IP & Geo: {attacker_ip_geo}
    Compromised Accounts: {compromised_accounts}
    Indicators of Compromise (IOCs): {iocs}
    Logs to Refer: {logs_referred}
    ------------------------------
    Response Actions Taken: {response_actions}
    Mitigation Measures: {mitigation_measures}
    ------------------------------
    Incident Description:
    {description}
    ================================
    """

    # Define report directory
    user_home = os.getenv("HOME")  # Gets /home/$USER
    report_dir = os.path.join(user_home, "IncidentReports")
    os.makedirs(report_dir, exist_ok=True)  # Create directory if it doesn't exist

    # Save report to file
    file_name = f"Incident_Report_{incident_id}.txt"
    file_path = os.path.join(report_dir, file_name)

    with open(file_path, "w") as file:
        file.write(report_content)

    print("\nIncident report successfully created!")
    print(f"File saved at: {file_path}")

if __name__ == "__main__":
    create_soc_incident_report()
