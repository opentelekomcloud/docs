# Error Response Syntax<a name="obs_03_0014"></a>

## Error Response Headers<a name="section49814798"></a>

When an error occurs, the header information contains:

Content-Type: application/\*, which may be in HTML or text format

HTTP status code 3xx, 4xx, or 5xx. For details, see  [Table 1](error-code-list.md#table30733758).

## Error Response Body<a name="section66197583"></a>

The response body also contains information about the error. The following example is an error response body in an authentication failure.

```
<html><h1>Unauthorized</h1><p>This server could not verify that you are authorized to access the document you requested.</p></html>
```

