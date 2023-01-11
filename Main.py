from Study_log4j import Study_log4j
from Scan_vulnerabilities import Scan_vulnerabilities
from Machine_learning import Machine_learning
from Vulnerability_report import Vulnerability_report

def main():
    # Input section for website URL
    url = input("Please enter the website URL: ")

    # Initialize the Study_log4j class
    log4j_study = Study_log4j()
    # Analyze the log4j system and identify vulnerabilities
    vulnerabilities = log4j_study.analyze(url)

    # Initialize the Scan_vulnerabilities class
    vulnerability_scan = Scan_vulnerabilities()
    # Process the vulnerabilities
    processed_vulnerabilities = vulnerability_scan.process(vulnerabilities)

    # Initialize the Machine_learning class
    machine_learning = Machine_learning()
    # Train the classifier
    machine_learning.train(processed_vulnerabilities)
    # Predict the labels for the vulnerabilities
    predictions = machine_learning.predict(processed_vulnerabilities)

    # Initialize the Vulnerability_report class
    report = Vulnerability_report()
    # Generate the report
    report.generate_report(processed_vulnerabilities, predictions)

if __name__ == '__main__':
    main()
