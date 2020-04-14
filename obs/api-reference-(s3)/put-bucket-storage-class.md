# PUT Bucket storage class<a name="EN-US_TOPIC_0125560403"></a>

You can use this operation to create a default storage class for a bucket or change the default storage class of a bucket.

Only users granted the  **s3:PutBucketStoragePolicy**  permission can perform this operation. By default, only the bucket owner can perform this operation. The bucket owner can allow other users to perform this operation by granting them the permission or setting a bucket policy.

When a bucket has a default storage class, if users do not specify the object storage class when uploading or copying an object or initializing a multipart upload task, the object will use the default bucket storage class.

When users do not manually set a default storage class for a bucket, the bucket will have the Standard storage class by default.

## Request Syntax<a name="section1693614596537"></a>

```
PUT /?storagePolicy HTTP/1.1
User-Agent: agent
Host: bucketname.obs.example.com
Date: date
Accept: */*
Date: date
Authorization: authorization
Content-Length: length

<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<StoragePolicy xmlns="http://obs.example.com/doc/2015-06-30/">
  <DefaultStorageClass>STANDARD</DefaultStorageClass>
</StoragePolicy>
```

## Request Parameters<a name="section931219237541"></a>

This request involves no parameters.

## Request Headers<a name="section1454013816540"></a>

This request uses common headers. For details about common request headers, see  [Common Request Headers](common-request-headers.md).

## Request Elements<a name="section1254181935510"></a>

This request uses elements to specify the default bucket storage class.  [Table 1](#table63485364)  describes the elements.

**Table  1**  Request elements

<a name="table63485364"></a>
<table><thead align="left"><tr id="row57640352"><th class="cellrowborder" valign="top" width="34.83%" id="mcps1.2.4.1.1"><p id="p334413554618"><a name="p334413554618"></a><a name="p334413554618"></a>Element</p>
</th>
<th class="cellrowborder" valign="top" width="41.93%" id="mcps1.2.4.1.2"><p id="p16344235134618"><a name="p16344235134618"></a><a name="p16344235134618"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="23.24%" id="mcps1.2.4.1.3"><p id="p03441835144619"><a name="p03441835144619"></a><a name="p03441835144619"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row9812033"><td class="cellrowborder" valign="top" width="34.83%" headers="mcps1.2.4.1.1 "><p id="p124693486466"><a name="p124693486466"></a><a name="p124693486466"></a>DefaultStorageClass</p>
</td>
<td class="cellrowborder" valign="top" width="41.93%" headers="mcps1.2.4.1.2 "><p id="p2469104884616"><a name="p2469104884616"></a><a name="p2469104884616"></a>Indicates the default bucket storage class.</p>
<p id="p1469184814615"><a name="p1469184814615"></a><a name="p1469184814615"></a>It is a character string and can be <strong id="b047020485465"><a name="b047020485465"></a><a name="b047020485465"></a>STANDARD</strong> (OBS Standard), <strong id="b6470164816464"><a name="b6470164816464"></a><a name="b6470164816464"></a>STANDARD_IA</strong> (OBS Warm), or <strong id="b10470104811465"><a name="b10470104811465"></a><a name="b10470104811465"></a>GLACIER</strong> (OBS Cold). Note that the three storage class values are case-sensitive.</p>
</td>
<td class="cellrowborder" valign="top" width="23.24%" headers="mcps1.2.4.1.3 "><p id="p17470194814463"><a name="p17470194814463"></a><a name="p17470194814463"></a>Mandatory</p>
</td>
</tr>
</tbody>
</table>

## Response Syntax<a name="section28885633224023"></a>

```
HTTP/1.1 status_code
Server: Server Name
x-amz-request-id: request id
x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc
x-amz-id-2: id
Date: date
Content-Length: 0
```

## Response Headers<a name="section52552049224023"></a>

This response uses common headers. For details about common response headers, see  [Common Response Headers](common-response-headers.md).

## Response Elements<a name="section55760466224023"></a>

This response involves no elements.

## Error Responses<a name="section48517371224023"></a>

No special error responses are returned. For details about error responses, see  [Table 1](error-codes.md#table30733758).

## Sample Request<a name="section31331064"></a>

```
PUT / HTTP/1.1
User-Agent: Jakarta Commons-HttpClient/3.1
Host: bucketname.obs.example.com
Accept: */*
Date: Sun, 26 Sep 2017 08:24:46 GMT
Authorization: AWS 04RZT432N80TGDF2Y2G2:ZyEGq367GyGGyItzr5egJOjaqiM=
Content-Length: 240
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<StoragePolicy xmlns="http://obs.example.com/doc/2015-06-30/">
  <DefaultStorageClass>STANDARD</DefaultStorageClass>
</StoragePolicy>
```

## Sample Response<a name="section35401528"></a>

```
HTTP/1.1 200 OK
Server: OBS
x-amz-request-id: 3CEF0000015D08E1CF94AE61EA0EA1BC
x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc
x-amz-id-2: 0Z9Og4sWbGljhJq/UYfv6oBCwQ3/ZidsCQYz4CYBU305KRQnMwJWNXk/3/vswTEx
Date: Sun, 26 Sep 2017 08:28:06 GMT
Content-Length: 0
```

