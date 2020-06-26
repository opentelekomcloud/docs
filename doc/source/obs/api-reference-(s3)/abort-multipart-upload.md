# Abort Multipart Upload<a name="EN-US_TOPIC_0125560402"></a>

You can use this operation to abort a multipart upload. After the request is sent, parts associated to the multipart upload cannot be uploaded or listed.

## Request Syntax<a name="section4482025"></a>

```
DELETE /ObjectName?uploadId=uplaodID HTTP/1.1 
 User-Agent: agent
 Host: bucketname.obs.example.com 
 Accept: */*
 Date: date 
 Authorization: auth
```

## Request Parameters<a name="section40338225"></a>

This request uses one parameter to specify the ID of the multipart upload to be completed.  [Table 1](#table46411854)  describes the parameter.

**Table  1**  Request parameter

<a name="table46411854"></a>
<table><thead align="left"><tr id="row54874371"><th class="cellrowborder" valign="top" width="26.552655265526553%" id="mcps1.2.4.1.1"><p id="p15639030"><a name="p15639030"></a><a name="p15639030"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="45.92459245924592%" id="mcps1.2.4.1.2"><p id="p58801955"><a name="p58801955"></a><a name="p58801955"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="27.522752275227525%" id="mcps1.2.4.1.3"><p id="p65337904"><a name="p65337904"></a><a name="p65337904"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row57878853"><td class="cellrowborder" valign="top" width="26.552655265526553%" headers="mcps1.2.4.1.1 "><p id="p57675531"><a name="p57675531"></a><a name="p57675531"></a>uploadId</p>
</td>
<td class="cellrowborder" valign="top" width="45.92459245924592%" headers="mcps1.2.4.1.2 "><p id="p41206441"><a name="p41206441"></a><a name="p41206441"></a>Indicates the ID of the multipart upload to be aborted.</p>
<p id="p35313657"><a name="p35313657"></a><a name="p35313657"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="27.522752275227525%" headers="mcps1.2.4.1.3 "><p id="p41834000"><a name="p41834000"></a><a name="p41834000"></a>Mandatory</p>
</td>
</tr>
</tbody>
</table>

## Request Headers<a name="section27499711"></a>

This request uses common headers. For details about common request headers, see section  [Common Request Headers](common-request-headers.md).

## Request Elements<a name="section46170811"></a>

This request involves no elements.

## Response Syntax<a name="section1451448"></a>

```
HTTP/1.1 status_code 
 x-amz-id-2: id 
 x-amz-request-id: request id 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Date: date 
 Server: server
```

## Response Headers<a name="section13063034"></a>

This response uses common headers. For details about common response headers, see section  [Common Response Headers](common-response-headers.md).

## Response Elements<a name="section50458444"></a>

This response involves no elements.

## Error Responses<a name="section51472815"></a>

-   If an AK or signature is invalid, OBS returns status code  **403 Forbidden** and error code **AccessDenied**.
-   If the requested bucket does not exist, OBS returns status code  **404 Not Found** and error code **NoSuchBucket**.
-   If the requester is neither the initiator of a multipart upload nor the bucket owner, OBS returns status code  **403 Forbidden** and error code **AccessDenied**.
-   If the operation succeeded, OBS returns status code  **204 No Content**.

For details about other error responses, see  [Table 1](error-codes.md#table30733758).

## Sample Request<a name="section8332925"></a>

```
DELETE /example-object?uploadId=VXBsb2FkIElEIGZvciBlbHZpbmcncyBteS1tb3ZpZS5tMnRzIHVwbG9hZ HTTP/1.1 
 User-Agent: Jakarta Commons-HttpClient/3.1
 Host: bucketname.obs.example.com
 Accept: */*
 Date: Mon, 1 Nov 2010 20:34:56 GMT 
 Authorization: AWS AKIAIOSFODNN7EXAMPLE:0RQf3/cRonhpaBX5sCYVf1bNRuU=
```

## Sample Response<a name="section7887465"></a>

```
HTTP/1.1 204 No Content 
 x-amz-id-2: Weag1LuByRx9e6j5Onimru9pO4ZVKnJ2Qz7/C1NPcfTWAtRPfTaOFg== 
 x-amz-request-id: 996c76696e6727732072657175657374 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Date: Mon, 1 Nov 2010 20:34:56 GMT
 Server: OBS
```

