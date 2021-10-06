https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-application-model.pdf#building-layers

Because AWS SAM integrates with other AWS services, creating serverless applications with AWS SAM provides the following
benefits:

- **Single-deployment configuration.**
  - AWS SAM makes it easy to organize related components and resources, and operate on a single
  stack. You can use AWS SAM to share configuration (such as memory and timeouts) between resources, and deploy all
  related resources together as a single, versioned entity.
- **Extension of AWS CloudFormation.**
  - Because AWS SAM is an extension of AWS CloudFormation, you get the reliable deployment capabilities
    of AWS CloudFormation. You can define resources by using AWS CloudFormation in your AWS SAM template. Also, you can use
    the full suite of resources, intrinsic functions, and other template features that are available in AWS CloudFormation.
- **Built-in best practices.**
  - You can use AWS SAM to define and deploy your infrastructure as a config. This makes it possible for you to
    use and enforce best practices such as code reviews.

- **Local debugging and testing.**
  - The AWS SAM CLI lets you locally build, test, and debug serverless applications that are
  defined by AWS SAM templates.
    - [JetBrains AWS Toolkit](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/)
      - [PyCharm](https://aws.amazon.com/pycharm/)
    - [VSCode AWS Toolkit](https://aws.amazon.com/visualstudiocode/)

## Installing AWS SAM CLI ##

Follow these steps to install and configure the prerequisites for using the AWS SAM command line interface (CLI) on your
macOS host:

1. Create an AWS account.
2. Configure AWS Identity and Access Management (IAM) permissions and AWS credentials.
3. Install Docker. Note: Docker is a prerequisite only for testing your application locally or using the `--use-container`
option
4. Install Homebrew.
    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
    ```
5. Install the AWS SAM CLI.
    ```bash
    brew tap aws/tap && brew install aws-sam-cli
    ```
Validate SAM CLI Installation.
    ```bash
    sam --version
    ```

