#!/bin/bash

# Build the Docker image
docker build -t log4j-vulnerabilities-beta .

# Run the Docker container
docker run -it --rm log4j-vulnerabilities-beta
