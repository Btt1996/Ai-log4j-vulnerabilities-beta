# Ai-log4j-vulnerabilities-beta
This repository contains a beta version of a project that studies log4j vulnerabilities and provides a report on the vulnerabilities found. The project uses a combination of automated testing, machine learning, and manual analysis to identify potential vulnerabilities in log4j-based systems. The report contains the likelihood of each vulnerability to be exploited and recommendations on how to fix them. The project is still in beta and has not been fully tested, contributions are welcomed.


## Files
1. `VulnerabilityScanner.java`: This class scans the website for vulnerabilities and logs the result. The scan is performed by connecting to the website and checking for known vulnerabilities.
2. `main.py`: This script coordinates the flow of data between the other files by reading the log file produced by `VulnerabilityScanner.java` and parsing the data.
3. `Study_log4j.py`: This script analyzes the log data and reports any vulnerabilities found.
4. `Scan_vulnerabilities.py`: This script scans the vulnerabilities reported by `Study_log4j.py` and processes the results.
5. `Machine_learning.py`: This script uses machine learning to predict the labels for the vulnerabilities.
6. `Vulnerability_report.py`: This script generates a report file that summarizes the vulnerabilities found and the machine learning predictions.
7. `requirements.txt`: This file contains a list of the libraries that your project depends on, one library per line.
8. `run.sh`: This script is responsible for running the `main.py` script and passing the website URL as an argument.
9. `Dockerfile`: This file contains the instructions for building a container and running the project inside it.

## Usage

### Prerequisites

- Java 8 or above 
- Python 3.x 
- pip
- Git
- Docker (if you want to use the provided Dockerfile)

### Installation

1. Clone the repository 
```sh
git clone https://github.com/<your-username>/Understanding-log4j-Security-Risks.git
2.Install the dependencies
"pip install -r requirements.txt"
### Runing the script
1.Compile the java code and run it:
"javac VulnerabilityScanner.java
java VulnerabilityScanner <url>"
2.Run the main script
"sh run.sh <url>"
3.The script will produce a report.txt file with the results
### Using Docker
You can use the provided Dockerfile to build a container and run the project inside it.
1.build the image
"docker build -t log4j-scan ."
2.Run the container
"docker run -it --rm log4j-scan <url>"
The container will run the scan and generate a report.txt file in the root directory.
## Contributing
This project welcomes contributions and suggestions. For details, see the CONTRIBUTING.md.
## Disclaimer
This tool is for educational purposes only and should not be used without proper knowledge and understanding of the risks and legal implications.

