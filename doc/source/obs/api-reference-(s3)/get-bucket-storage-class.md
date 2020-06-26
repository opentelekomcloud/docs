# GET Bucket storage class<a name="EN-US_TOPIC_0125560378"></a>

You can use this operation to obtain the default storage class of a bucket.

Only users granted the  **s3:GetBucketStoragePolicy**  permission can perform this operation. By default, only the bucket owner can perform this operation. The bucket owner can allow other users to perform this operation by granting them the permission or setting a bucket policy.

## Request Syntax<a name="section8474400"></a>

```
GET /?storagePolicy HTTP/1.1
User-Agent: agent
Host: bucketname.obs.example.com
Accept: */*
Date: date
Authorization: authorization
```

## Request Parameters<a name="section28412381"></a>

This request involves no parameters.

## Request Headers<a name="section49412770"></a>

This request uses common headers. For details about common request headers, see  [Common Request Headers](common-request-headers.md).

## Request Elements<a name="section16756923"></a>

This request involves no elements.

## Response Syntax<a name="section29441461"></a>

```
HTTP/1.1 status_code
Server: Server Name
x-amz-request-id: request id
x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc
x-amz-id-2: id
Content-Type: type
Date: date
Content-Length: length

<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<StoragePolicy xmlns="http://obs.example.com/doc/2015-06-30/">
  <DefaultStorageClass>STANDARD</DefaultStorageClass>
</StoragePolicy>
```

## Response Headers<a name="section12865091"></a>

This response uses common headers. For details about common response headers, see  [Common Response Headers](common-response-headers.md).

## Response Elements<a name="section7655917"></a>

This response contains elements to specify the default bucket storage class.  [Table 1](#table40100219)  describes the elements.

**Table  1**  Response elements

<a name="table40100219"></a>
<table><thead align="left"><tr id="row34562362"><th class="cellrowborder" valign="top" width="39.44%" id="mcps1.2.3.1.1"><p id="p93814525510"><a name="p93814525510"></a><a name="p93814525510"></a>Element</p>
</th>
<th class="cellrowborder" valign="top" width="60.56%" id="mcps1.2.3.1.2"><p id="p193815105519"><a name="p193815105519"></a><a name="p193815105519"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row16883390"><td class="cellrowborder" valign="top" width="39.44%" headers="mcps1.2.3.1.1 "><p id="p62034596165412"><a name="p62034596165412"></a><a name="p62034596165412"></a>StoragePolicy</p>
</td>
<td class="cellrowborder" valign="top" width="60.56%" headers="mcps1.2.3.1.2 "><p id="p143502104551"><a name="p143502104551"></a><a name="p143502104551"></a>Indicates the bucket storage specification, including the default bucket storage class.</p>
<p id="p635013103555"><a name="p635013103555"></a><a name="p635013103555"></a>Type: XML</p>
</td>
</tr>
<tr id="row35218150"><td class="cellrowborder" valign="top" width="39.44%" headers="mcps1.2.3.1.1 "><p id="p16334111"><a name="p16334111"></a><a name="p16334111"></a>DefaultStorageClass</p>
</td>
<td class="cellrowborder" valign="top" width="60.56%" headers="mcps1.2.3.1.2 "><p id="p10246132219559"><a name="p10246132219559"></a><a name="p10246132219559"></a>Indicates the default bucket storage class.</p>
<p id="p624692219554"><a name="p624692219554"></a><a name="p624692219554"></a>Type: It is a character string. <a href="put-bucket-storage-class.md#table63485364">Table 1</a> provides the possible values.</p>
</td>
</tr>
</tbody>
</table>

## Error Responses<a name="section59410009"></a>

No special error responses are returned. For details about error responses, see  [Table 1](error-codes.md#table30733758).

## Sample Request<a name="section22641308"></a>

```
GET /?storagePolicy HTTP/1.1
User-Agent: Jakarta Commons-HttpClient/3.1
Host: bucketname.obs.example.com
Accept: */*
Date: Sun, 26 Sep 2017 08:24:46 GMT
Authorization: AWS 08350B985315591007AD:UpIi7+loQpsAFUpKCYvmIuZyFP0=
```

## Sample Response<a name="section22735078"></a>

```
HTTP/1.1 200 OK
Server: OBS
x-amz-request-id: 3CEF0000015D0B5293440F668629A2C9
x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc
x-amz-id-2: Dbn8aLu3MP7QA692G1pQdYZTf3Xa7vVGikDMbX+VfLFhat/ML3I/YkW8fwvWQSNr
Content-Type: application/xml
Date: Sun, 26 Sep 2017 08:24:47 GMT
Content-Length: 187
 
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<StoragePolicy xmlns="http://obs.example.com/doc/2015-06-30/">
  <DefaultStorageClass>STANDARD</DefaultStorageClass>
</StoragePolicy>
```

