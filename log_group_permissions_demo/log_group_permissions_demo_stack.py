"""Module for the main LogGroupPermissionsDemo Stack."""

# Standard library imports
# -

# Related third party imports
# -

# Local application/library specific imports
from aws_cdk import core, aws_lambda as lambda_, aws_iam as iam


class LogGroupPermissionsDemoStack(core.Stack):
    """The LogGroupPermissionsDemo Stack."""

    def __init__(
        self,
        scope: core.Construct,
        construct_id: str,
        config: dict,  # pylint: disable=unused-argument
        **kwargs,
    ) -> None:
        """Construct a new LogGroupPermissionsDemoStack."""
        super().__init__(scope, construct_id, **kwargs)

        role = iam.Role(
            scope=self,
            id="Role",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
        )

        function = lambda_.Function(
            scope=self,
            id="Function",
            code=lambda_.Code.from_inline("print('Hello World')"),
            runtime=lambda_.Runtime.PYTHON_3_8,
            handler="index.handler",
            role=role,
        )
        
        statement = iam.PolicyStatement(
                actions=["logs:PutLogEvents", "logs:CreateLogStream"],
                effect=iam.Effect.ALLOW,
                resources=[
                    f'arn:aws:logs:{self.region}:{self.account}:log-group:/aws/lambda/{function.function_name}:log-stream:*'],
        )
        
        log_policy = iam.Policy(
            scope=self, id='Policy',
            document=iam.PolicyDocument(statements=[statement])
        )
        log_policy.attach_to_role(role)
