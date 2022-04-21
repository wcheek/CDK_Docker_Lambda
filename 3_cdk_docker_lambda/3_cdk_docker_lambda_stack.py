from aws_cdk import Stack
from aws_cdk import aws_lambda as _lambda
from constructs import Construct


class CdkDockerLambdaStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

    def build_lambda_func(self):
        self.prediction_lambda = _lambda.DockerImageFunction(
            scope=self,
            id="ExampleDockerLambda",
            # Function name on AWS
            function_name="ExampleDockerLambda",
            # Use aws_cdk.aws_lambda.DockerImageCode.from_image_asset to build
            # a docker image on deployment
            code=_lambda.DockerImageCode.from_image_asset(
                # Directory relative to the stack which contains Dockerfile
                directory="ExampleDockerLambda"
            ),
        )
