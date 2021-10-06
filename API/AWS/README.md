- https://docs.aws.amazon.com/AmazonS3/latest/userguide/HostingWebsiteOnS3Setup.html
- https://docs.aws.amazon.com/AmazonS3/latest/userguide/how-to-page-redirect.html
- https://docs.aws.amazon.com/AmazonS3/latest/userguide/website-hosting-cloudfront-walkthrough.html

|Name|Description|
|:---:|:---|
| `RoutingRules` | Container for a collection of RoutingRule elements. |
| `RoutingRule` | A rule that identifies a condition and the redirect that is applied when the condition is met. **
| `Condition` | Container for describing a condition that must be met for the specified redirect to be applied. If the routing rule does not include a condition, the rule is applied to all requests. |
| `KeyPrefixEquals` | The prefix of the object key name from which requests are redirected. KeyPrefixEquals is required if HttpErrorCodeReturnedEquals is not specified. If both KeyPrefixEquals and HttpErrorCodeReturnedEquals are specified, both must be true for the condition to be met. |
| `HttpErrorCodeReturnedEquals` | The HTTP error code that must match for the redirect to apply. If an error occurs, and if the error code meets this value, then the specified redirect applies. |
| `HttpErrorCodeReturnedEquals` | is required if KeyPrefixEquals is not specified. If both KeyPrefixEquals and HttpErrorCodeReturnedEquals are specified, both must be true for the condition to be met. |
| `Redirect` | Container element that provides instructions for redirecting the request. You can redirect requests to another host or another page, or you can specify another protocol to use. A RoutingRule must have a Redirect element. A Redirect element must contain at least one of the following sibling elements: Protocol, HostName, ReplaceKeyPrefixWith, ReplaceKeyWith, or HttpRedirectCode. |
| `Protocol` | The protocol, http or https, to be used in the Location header that is returned in the response. If one of its siblings is supplied, Protocol is not required. |
| `HostName` | The hostname to be used in the Location header that is returned in the response. If one of its siblings is supplied, HostName is not required. |
| `ReplaceKeyPrefixWith` | The prefix of the object key name that replaces the value of KeyPrefixEquals in the redirect request. If one of its siblings is supplied, ReplaceKeyPrefixWith is not required. It can be supplied only if ReplaceKeyWith is not supplied. |
| `ReplaceKeyWith` | The object key to be used in the Location header that is returned in the response. If one of its siblings is supplied, ReplaceKeyWith is not required. It can be supplied only if ReplaceKeyPrefixWith is not supplied. |
| `HttpRedirectCode` | The HTTP redirect code to be used in the Location header that is returned in the response. If one of its siblings is supplied, HttpRedirectCode is not required. |

## Redirect requests for an object ##

You can redirect requests for an object to another object or URL by setting the website redirect location in the
metadata of the object. You set the redirect by adding the `x-amz-website-redirect-location` property to the object
metadata. On the Amazon S3 console, you set the Website Redirect Location in the metadata of the object. If you use
the [Amazon S3 API](https://docs.aws.amazon.com/AmazonS3/latest/userguide/how-to-page-redirect.html#page-redirect-using-rest-api)
, you set `x-amz-website-redirect-location`. The website then interprets the object as a 301 redirect.

To redirect a request to another object, you set the redirect location to the key of the target object. To redirect a
request to an external URL, you set the redirect location to the URL that you want. For more information about object
metadata, see [System-defined](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingMetadata.html#SysMetadata)
object metadata.

When you set a page redirect, you can either keep or delete the source object content. For example, if you have a
page1.html object in your bucket, you can redirect any requests for this page to another object, page2.html. You have
two options:

1. Keep the content of the `page1.html` object and redirect page requests.
2. Delete the content of page1.html and upload a zero-byte object named `page1.html`
   to replace the existing object and redirect page requests.

## Enabling Static Web-Hosting ##

- https://docs.aws.amazon.com/AmazonS3/latest/userguide/IndexDocumentSupport.html
- https://docs.aws.amazon.com/AmazonS3/latest/userguide/CustomErrorDocSupport.html
- https://docs.aws.amazon.com/AmazonS3/latest/userguide/how-to-page-redirect.html#advanced-conditional-redirects

After you create a bucket, you can enable static website hosting for your bucket. You can create a new bucket or use an
existing bucket.

To enable static website hosting

1. Sign in to the AWS Management Console and open the Amazon S3 console at https://console.aws.amazon.com/s3/.
2. In the Buckets list, choose the name of the bucket that you want to enable static website hosting for.
3. Choose Properties.
4. Under Static website hosting, choose Edit.
5. Choose Use this bucket to host a website.
6. Under Static website hosting, choose Enable.
7. In Index document, enter the file name of the index document, typically index.html.
8. The index document name is case sensitive and must exactly match the file name of the HTML index document that you
   plan to upload to your S3 bucket. When you configure a bucket for website hosting, you must specify an index
   document. Amazon S3 returns this index document when requests are made to the root domain or any of the subfolders.
   For more information, see Configuring an index document.
9. To provide your own custom error document for 4XX class errors, in Error document, enter the custom error document
   file name.
10. The error document name is case sensitive and must exactly match the file name of the HTML error document that you
    plan to upload to your S3 bucket. If you don't specify a custom error document and an error occurs, Amazon S3
    returns a default HTML error document. For more information, see Configuring a custom error document.
11. (Optional) If you want to specify advanced redirection rules, in Redirection rules, enter XML to describe the rules.
12. For example, you can conditionally route requests according to specific object key names or prefixes in the request.
    For more information, see Configure redirection rules to use advanced conditional redirects.
13. Choose Save changes.
14. Amazon S3 enables static website hosting for your bucket. At the bottom of the page, under Static website hosting,
    you see the website endpoint for your bucket.
15. Under Static website hosting, note the Endpoint.
16. The Endpoint is the Amazon S3 website endpoint for your bucket. After you finish configuring your bucket as a static
    website, you can use this endpoint to test your website.

## Security + Public Access Blocking ##

- https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html

### Bucket Policy ###

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::<your-bucket>/*"
        }
    ]
}