# Ai-log4j-vulnerabilities-beta
This repository contains a beta version of a project that studies log4j vulnerabilities and provides a report on the vulnerabilities found. The project uses a combination of automated testing, machine learning, and manual analysis to identify potential vulnerabilities in log4j-based systems. The report contains the likelihood of each vulnerability to be exploited and recommendations on how to fix them. The project is still in beta and has not been fully tested, contributions are welcomed


## File Explanation

- **File1: Study_log4j.py** 
- This script uses automated testing to identify known vulnerabilities in log4j systems and sends them to File2 for further analysis.


- **File2: VulnerabilityScanner.java** 
- This script receives the vulnerabilities from File1, performs further analysis, and sends the results to File3 for machine learning.


- **File3: Machine_learning.py** 
- This script receives the vulnerabilities from File2, learns from them using machine learning, and saves the learning to an external file.


- **File4: Generate_Report.py**
- This script receives the vulnerabilities from File3, loads the previously trained model, and uses it to generate a report on the vulnerabilities found.

## Getting started

- Make sure you have Docker installed on your system.
- Clone the repository by running `git clone https://github.com/btt1996/Ai-log4j-vulnerabilities-beta.git`

## Running with Docker

- Build the Docker image by running 
`docker build -t log4j-vulnerabilities-beta .`

- Run the Docker container by running 
`docker run -it --rm Ai-log4j-vulnerabilities-beta`

- Check the report generated in the output.

## Dependencies
- Docker
- Python 3.x
- Java 8
- Git
- json
- requests (for python)
- sklearn (for python)
- org.json (for java)
- apache http client (for java)

## Contributing

This project is still in beta, and contributions are more than welcome. If you find any bugs or have any suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
