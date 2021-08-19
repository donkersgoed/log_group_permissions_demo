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

        role.add_to_policy(
            iam.PolicyStatement(
                actions=["logs:PutLogEvents", "logs:CreateLogStream"],
                effect=iam.Effect.ALLOW,
                resources=["*"],
            )
        )

        function = lambda_.Function(
            scope=self,
            id="Function",
            code=lambda_.Code.from_inline("print('Hello World')"),
            runtime=lambda_.Runtime.PYTHON_3_8,
            handler="index.handler",
            role=role,
        )
