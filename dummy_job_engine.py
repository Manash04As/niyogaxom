# dummy_job_engine.py
from datetime import datetime
import os

# Folder path where job pages will be saved
JOB_FOLDER = "jobs"

# Today's date for file naming
TODAY = datetime.now().strftime("%Y-%m-%d")

# Dummy job data (Assam + Central)
jobs_data = {
    "Assam": [
        {"title": "APSC Junior Engineer Recruitment 2025", "link": "https://assamcareer.com/apsc-je-2025"},
        {"title": "DHS Grade-III Posts - Apply Now", "link": "https://jobassam.in/dhs-2025"}
    ],
    "Central": [
        {"title": "SSC GD Constable Notification 2025", "link": "https://ssc.nic.in/notifications/2025"},
        {"title": "UPSC NDA-I 2025 Application Open", "link": "https://upsc.gov.in/nda1-2025"}
    ]
}

# Create jobs folder if it doesn't exist
os.makedirs(JOB_FOLDER, exist_ok=True)

# Build HTML content
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Job Updates – {TODAY}</title>
    <link rel='stylesheet' href='/static/style.css'>
</head>
<body>
    <h1>Job Updates – {TODAY}</h1>
"""

for category, jobs in jobs_data.items():
    html_content += f"<h2>{category} Government Jobs</h2><ul>"
    for job in jobs:
        html_content += f"<li><a href='{job['link']}' target='_blank'>{job['title']}</a></li>"
    html_content += "</ul>"

html_content += "</body></html>"

# Save to file
filename = os.path.join(JOB_FOLDER, f"{TODAY}.html")
with open(filename, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Dummy job page generated: {filename}")
