# Lambda `context` #

When Lambda runs your function, it passes a context object to the handler. This object provides methods and properties
that provide information about the invocation, function, and execution environment.

### Context Methods ###

`getRemainingTimeInMillis()` – Returns the number of milliseconds left before the execution times out. Context properties

### Context Properties ###

- `functionName` – The name of the Lambda function.
- `functionVersion` – The version of the function.
- `invokedFunctionArn` – The Amazon Resource Name (ARN) that's used to invoke the function. Indicates if the invoker
specified a version number or alias.
- `memoryLimitInMB` – The amount of memory that's allocated for the function. awsRequestId – The identifier of the
invocation request.
- `logGroupName` – The log group for the function. logStreamName – The log stream for the function
instance.
- `callbackWaitsForEmptyEventLoop` – Set to `false` to send the response right away when the callback runs, instead
of waiting for the Node.js event loop to be empty. If this is false, any outstanding events continue to run during the
next invocation.

### Logging ###

```javascript
exports.handler = async function(event, context) {
    console.log("ENVIRONMENT VARIABLES\n" + JSON.stringify(process.env, null, 4))
    console.info("EVENT\n" + JSON.stringify(event, null, 4))

    return context.logStreamName
}
```
---

## Example ##

```javascript
exports.handler = async function(event, context) {
    console.log('Remaining time: ', context.getRemainingTimeInMillis())
    console.log('Function name: ', context.functionName)
    return context.logStreamName
}
```
