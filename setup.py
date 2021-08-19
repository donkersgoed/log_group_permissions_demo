"""Project setup."""

import setuptools

with open("README.md") as fp:
    long_description = fp.read()

CDK_VERSION = None
with open(".env.aws", "r") as env_file:
    env_vars = env_file.read().split("\n")
    for env_var in env_vars:
        if env_var.startswith("CDK_VERSION"):
            CDK_VERSION = env_var.split("=")[1].replace('"', "")

if not CDK_VERSION:
    raise ValueError("The ENV VAR CDK_VERSION is required.")

setuptools.setup(
    name="LogGroupPermissionsDemo",
    version="0.0.1",
    description="LogGroupPermissionsDemo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Luc van Donkersgoed",
    package_dir={"": "log_group_permissions_demo"},
    packages=setuptools.find_packages(where="log_group_permissions_demo"),
    install_requires=[
        "python-dotenv==0.17.0",
        "stringcase==1.2.0",
        f"aws-cdk.aws-iam=={CDK_VERSION}",
        f"aws-cdk.aws-lambda=={CDK_VERSION}",
        f"aws-cdk.aws-logs=={CDK_VERSION}",
        f"aws-cdk.core=={CDK_VERSION}",
    ],
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
)
