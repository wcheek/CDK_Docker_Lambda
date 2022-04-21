# Deploy a Docker built Lambda function with AWS CDK

This project is a minimum working example of deploying an AWS Lambda function using Docker and AWS CDK.

Deploying Lambda functions using Docker has a number of benefits

- Package all necessary libraries into a single Docker image
- Bypass AWS Lambda's size constraint of 512 mb. Docker images stored on AWS ECR have a maximum size of 10 gb.
- It’s easy!

[GitHub Repository](https://github.com/wcheek/CDK_Docker_Lambda)

## CDK init & deploy

I won’t cover setting up CDK and bootstrapping the environment. You can find that information [here.](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html)

Once you have set up CDK, we need to set up the project:

1. `mkdir cdk_docker_lambda && cd cdk_docker_lambda`

2. `cdk init --language python`

3. `source .venv/bin/activate`

4. `pip install -r requirements.txt && pip install -r requirements-dev.txt`

    Now deploy empty stack to AWS:

5. `cdk deploy`

## Stack design

Our stack will deploy only a lambda function. The lambda function will be built using `Docker`, so be sure to have `Docker` installed and the `Docker` daemon running.

```python
# cdk_docker_lambda/cdk_docker_lambda_stack.py

from aws_cdk import Stack
from aws_cdk import aws_lambda as _lambda
from constructs import Construct


class CdkDockerLambdaStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.build_lambda_func()

    def build_lambda_func(self):
        self.prediction_lambda = _lambda.DockerImageFunction(
            scope=self,
            id="ExampleDockerLambda",
            # Function name on AWS
            function_name="ExampleDockerLambda",
            # Use aws_cdk.aws_lambda.DockerImageCode.from_image_asset to build
            # a docker image on deployment
            code=_lambda.DockerImageCode.from_image_asset(
                # Directory relative to where you execute cdk deploy
                # contains a Dockerfile with build instructions
                directory="cdk_docker_lambda/ExampleDockerLambda"
            ),
        )

```

## Lambda function

Create a new directory in `cdk_docker_lambda` called `ExampleDockerLambda`. Here we are going to put a `Dockerfile`, `requirements.txt` which holds our function’s dependencies, and the lambda function itself, `example_docker_lambda.py`

### cdk_docker_lambda/ExampleDockerLambda/Dockerfile

```dockerfile
FROM amazon/aws-lambda-python:latest

LABEL maintainer="Wesley Cheek"
# Installs python, removes cache file to make things smaller
RUN yum update -y && \
    yum install -y python3 python3-dev python3-pip gcc && \
    rm -Rf /var/cache/yum
# Be sure to copy over the function itself!
COPY example_docker_lambda.py ./
# Copies requirements.txt file into the container
COPY requirements.txt ./
# Installs dependencies found in your requirements.txt file
RUN pip install -r requirements.txt

# Points to the handler function of your lambda function
CMD ["example_docker_lambda.handler"]
```

### cdk_docker_lambda/ExampleDockerLambda/requirements.txt

```
requests
```

### cdk_docker_lambda/ExampleDockerLambda/example_docker_lambda.py

```python
# Very simple

import requests

def handler(event, context):
    return "Hello Lambda!"

```

Now `cdk deploy`. `AWS CDK` will build your new Lambda function using `Docker` and then push it for you to the `ECR` repository that was originally created for you by running `cdk bootstrap` during the CDK setup. How convenient. 

After the image is built and pushed, CDK will deploy the necessary infrastructure. You can navigate to the `AWS CloudFormation` console to view the deployment. It should only take a couple minutes. 

Once finished, you will find your beautful `Docker` deployed Lambda function on the Lambda console

![lambda func](D:\Projects\Notes\My Articles\3_CDK_Docker_Lambda\Assets\lambda func.png)

### Test your Lambda function

We can use any kind of event since the function always just returns a string.

![image-20220421105909196](D:\Projects\Notes\My Articles\3_CDK_Docker_Lambda\Assets\image-20220421105909196.png)

Have fun easily deploying any sized Lambda you’d like using `AWS CDK` and `Docker`!
