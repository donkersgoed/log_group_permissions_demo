"""Config Module."""
# Standard library imports
import os

# Related third party imports
from aws_cdk import core
import stringcase

# Local application/library specific imports
# -


class Config:
    """Config class."""

    def __init__(self, **kwargs) -> None:
        """Initialize config class."""
        self.environment = os.getenv("ENVIRONMENT")
        stack_snake = stringcase.snakecase(os.getenv("STACK_NAME"))
        self.stack_name = stringcase.camelcase(stack_snake)

        self.env = core.Environment(
            account=os.getenv("AWS_ACCOUNT"), region=os.getenv("AWS_REGION")
        )

        self._default_config = {
            "account": self.env.account,
            "region": self.env.region,
            "environment": self.environment,
            "stack_name": self.stack_name,
        }

    def base(self):
        """Define the base configuration."""
        __config = {}
        return {**__config, **self._default_config}
