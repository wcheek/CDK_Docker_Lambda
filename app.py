#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk_docker_lambda.cdk_docker_lambda_stack import CdkDockerLambdaStack

app = cdk.App()
CdkDockerLambdaStack(app, "3CdkDockerLambdaStack")

app.synth()
