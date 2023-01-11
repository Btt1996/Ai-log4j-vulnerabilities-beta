import json
import requests

def study_log4j():
    # Code to study log4j vulnerabilities
    vulnerabilities = ["Injection attack", "File inclusion attack", "File path traversal attack", "Log forging"]
    send_to_file2(vulnerabilities)

def send_to_file2(vulnerabilities):
    # Send the vulnerabilities to File 2 for further analysis
    data = {"vulnerabilities": vulnerabilities}
    requests.post("http://localhost:8000/analyze", json=data)

if __name__ == "__main__":
    study_log4j()
