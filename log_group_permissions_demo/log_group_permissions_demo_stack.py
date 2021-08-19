"""Module for the main LogGroupPermissionsDemo Stack."""

# Standard library imports
# -

# Related third party imports
# -

# Local application/library specific imports
from aws_cdk import core


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

        # The code that defines your stack goes here
