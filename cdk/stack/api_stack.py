from aws_cdk import (core,
                     aws_apigateway as apigateway,
                     aws_lambda as lambda_)
import os.path
dirname = os.path.dirname(__file__)

class MyAPIService(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:

        super().__init__(scope, id, **kwargs)

        handler = lambda_.Function(self,'MyPyLambda',
            handler='lambda_handler.handler',
            runtime=lambda_.Runtime.PYTHON_3_7,
            code=lambda_.Code.asset('lambda'),
        )

        api = apigateway.RestApi(self, "MyPys-api",
                  rest_api_name="MyPy Service",
                  description="This service serves MyPys.")

        get_MyPys_integration = apigateway.LambdaIntegration(handler,
                request_templates={"application/json": '{ "statusCode": "200" }'})

        api.root.add_method("GET", get_MyPys_integration)   # GET /
