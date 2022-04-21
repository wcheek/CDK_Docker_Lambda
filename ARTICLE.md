# Deploy a Docker built Lambda function with AWS CDK

This project is a minimum working example of deploying an AWS Lambda function using Docker and AWS CDK.

Deploying Lambda functions using Docker has a number of benefits

- Package all necessary libraries into a single Docker image
- Bypass AWS Lambda's size constraint of 512 mb. Docker images stored on AWS ECR have a maximum size of 10 gb.
- It’s easy!

