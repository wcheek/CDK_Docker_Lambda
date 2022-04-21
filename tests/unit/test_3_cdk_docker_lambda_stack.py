import aws_cdk as core
import aws_cdk.assertions as assertions

from 3_cdk_docker_lambda.3_cdk_docker_lambda_stack import 3CdkDockerLambdaStack

# example tests. To run these tests, uncomment this file along with the example
# resource in 3_cdk_docker_lambda/3_cdk_docker_lambda_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = 3CdkDockerLambdaStack(app, "3-cdk-docker-lambda")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
