#!/usr/bin/env python3
"""The main app. Contains all the stacks."""

# Standard library imports
# -

# Related third party imports
# -

# Local application/library specific imports
from aws_cdk import core
from config import Config
from log_group_permissions_demo.log_group_permissions_demo_stack import LogGroupPermissionsDemoStack

config = Config()

app = core.App()
LogGroupPermissionsDemoStack(
    scope=app,
    construct_id="LogGroupPermissionsDemoStack",
    config=config.base(),
    env=config.env,
)

app.synth()
