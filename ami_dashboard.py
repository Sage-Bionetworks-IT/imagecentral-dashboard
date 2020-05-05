"""Create AMI dashboard by uses gh-pages.

Configuration:

Make sure you can assume the packer service role by configuring
~/.aws/config and ~/.aws/credentials.  Set up conda env:
```
conda create -n aws python=3.7
conda activate aws
pip install aws
pip install awsmfa
```

Usage:
```
awsmfa -i imagecentral -t imagecentral.admin -c ...
git clone -b gh-pages https://github.com/thomasyu888/imagecentral-infra.git
cd imagecentral-infra
python scripts/ami_dashboard.py
git diff
git commit -am "Update"
git push
```

"""
import argparse
from typing import List

import boto3


def get_aws_client(service: str, access_key: str,
                   secret_access_key: str,
                   role_arn: str) -> boto3.client:
    """Get AWS client

    Args:
        service: AWS service to use
        access_key: AWS Access key Id
        secret_access_key: AWS Secret access key
        role_arn: AWS role to assume

    Returns:
        boto3.client

    """
    # Must use sts client to assume role first
    sts_client = boto3.client(
        'sts',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_access_key
    )
    assume_role_object = sts_client.assume_role(RoleArn=role_arn,
                                                RoleSessionName="packer",
                                                DurationSeconds=3600)
    credentials = assume_role_object['Credentials']
    client = boto3.client(
        service,
        aws_access_key_id=credentials['AccessKeyId'],
        aws_secret_access_key=credentials['SecretAccessKey'],
        aws_session_token=credentials['SessionToken']
    )
    return client


def form_markdown_text(ami_dict: dict) -> List[str]:
    """Forms readme text to push to github

    Args:
        images: Dictionary of images

    Returns:
        markdown text with AMI table

    """
    text = []
    text.append("# AMI Dashboard")
    text.append("Here are a list of AMIs")
    text.append("")
    text.append("AMI Name | AMI Id")
    text.append("-------- | ------")
    # Sort values of AMI name to AMI Id
    for key, value in sorted(ami_dict.items(), reverse=True):
        text.append(f"{key} | `{value}`")

    return "\n".join(text)


def cli():
    """CLI"""
    parser = argparse.ArgumentParser(
        description='Challenge utility functions'
    )
    parser.add_argument("access_key_id", help="AWS access key id", type=str)
    parser.add_argument("secret_access_key", help="AWS secret access key",
                        type=str)
    parser.add_argument("role_arn", help="AWS Role ARN", type=str)
    parser.add_argument("--exclude_ami", nargs="+",
                        help="Exclude AMIs with these prefixes")
    args = parser.parse_args()
    return args


def main():
    """List available AMI's, form markdown table text with AMIs,
    push to github"""
    args = cli()
    ec2_client = get_aws_client("ec2", args.access_key_id,
                                args.secret_access_key,
                                args.role_arn)
    # Get AMI images
    images = ec2_client.describe_images(Owners=['self'])

    ami_dict = {image['Name']: image['ImageId']
                for image in images['Images']}

    markdown_text = form_markdown_text(ami_dict)
    with open("README.md", "w") as readme_f:
        readme_f.write(markdown_text)


if __name__ == "__main__":
    main()
