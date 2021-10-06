# Lambda Layering #

- **The Serverless Application Model (SAM)**: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-application-model.pdf#building-layers

- **Lambda Application(s) Design Patterns**: https://docs.aws.amazon.com/lambda/latest/operatorguide/application-design.html
    - **Anti-Patterns**: https://docs.aws.amazon.com/lambda/latest/operatorguide/no-function.html
        - https://aws.amazon.com/blogs/compute/operating-lambda-anti-patterns-in-event-driven-architectures-part-3/
- **Deployments**: https://docs.aws.amazon.com/lambda/latest/dg/deploying-lambda-apps.html
- **Best Practices**: https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html#function-code
- **Lambda State-Machines**: https://docs.aws.amazon.com/lambda/latest/dg/lambda-stepfunctions.html
  - **The Step Function**: https://docs.aws.amazon.com/lambda/latest/dg/services-stepfunctions.html
- **Node-JS Promise vs. Callback Implementations**: https://docs.aws.amazon.com/lambda/latest/dg/nodejs-handler.html
  - **`*.zip` Archives**: https://docs.aws.amazon.com/lambda/latest/dg/nodejs-package.html

## Overview ##

If you deploy your function code using a .zip file archive, you can use Lambda layers as a distribution mechanism for
libraries, [custom runtimes](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-custom.html), and other function
dependencies. Layers enable you to manage your in-development function code independently from the unchanging code and
resources that it uses. You can configure your function to use layers that you create, layers that AWS provides, or
layers from other AWS customers (or Cross-Account).

## Creating and sharing Lambda layers ##

- https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html

### Creating a layer ###

A Lambda layer is a .zip file archive that can contain additional code or data. A layer can contain libraries, a custom
runtime, data, or configuration files. Layers promote code sharing and separation of responsibilities so that you can
iterate faster on writing business logic.

You can create layers using the Lambda console, the Lambda API, AWS CloudFormation, or the AWS Serverless Application
Model (AWS SAM).

#### API Usage ####

You build your layer code into a .zip file archive using the same procedure as you would for a function deployment
package. If your layer includes any native code libraries, you must compile and build these libraries using a Linux
development machine so that the binaries are compatible with [Amazon Linux](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html).

```bash
aws lambda publish-layer-version --layer-name "my-layer" --description "My layer"  \
    --license-info "MIT" --content "S3Bucket=example-1-lambda-layer,S3Key=layer.zip" \
        --compatible-runtimes "python3.6" "python3.7" "python3.8"

# >>> {
# >>>     "Content": {
# >>>         "Location": "https://awslambda-us-east-2-layers.s3.us-east-2.amazonaws.com/snapshots/123456789012/my-layer-4aaa2fbb-ff77-4b0a-ad92-5b78a716a96a?versionId=27iWyA73cCAYqyH...",
# >>>         "CodeSha256": "tv9jJO+rPbXUUXuRKi7CwHzKtLDkDRJLB3cC3Z/ouXo=",
# >>>         "CodeSize": 169
# >>>     },
# >>>     "LayerArn": "arn:aws:lambda:us-east-2:123456789012:layer:my-layer",
# >>>     "LayerVersionArn": "arn:aws:lambda:us-east-2:123456789012:layer:my-layer:1",
# >>>     "Description": "My layer",
# >>>     "CreatedDate": "2018-11-14T23:03:52.894+0000",
# >>>     "Version": 1,
# >>>     "LicenseInfo": "MIT",
# >>>     "CompatibleRuntimes": [
# >>>         "python3.6",
# >>>         "python3.7",
# >>>         "python3.8"
# >>>     ]
# >>> }

aws lambda publish-layer-version --layer-name "my-layer" --description "My layer"  \
    --license-info "MIT" --content "S3Bucket=example-1-lambda-layer,S3Key=layer.zip" \
        --compatible-runtimes "python3.6" "python3.7" "python3.8"

# >>>     "Content": "...",
# >>>     "LayerArn": "arn:aws:lambda:us-east-2:123456789012:layer:my-layer",
# >>>     "LayerVersionArn": "arn:aws:lambda:us-east-2:123456789012:layer:my-layer:2",
# >>>     "Description": "...",
# >>>     "CreatedDate": "...",
# >>>     "Version": 2,
# >>>     "LicenseInfo": "MIT",
# >>>     "CompatibleRuntimes": [
# >>>         "python3.6",
# >>>         "python3.7",
# >>>         "python3.8"
# >>>     ]
# >>> }
```

> Each time that you call publish-layer-version, you create a new version of the layer.
