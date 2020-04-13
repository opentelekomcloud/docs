# GET Bucket tagging<a name="EN-US_TOPIC_0125560249"></a>

This implementation of the  **GET**  operation uses the **tagging**  subresource to return the tag set associated with the bucket. However, searching for buckets by tag is not  supported.

Only users granted the  **s3:GetBucketTagging**  permission can perform this operation. By default, the permission is granted to the bucket owner only. However, it can be granted to other users by configuring the bucket policy.

## Request Syntax<a name="section38789260145638"></a>

```
GET /?tagging HTTP/1.1
User-Agent: agent 
Host: bucketname.obs.example.com
Accept: */* 
Date: date 
Authorization: authorization string
```

## Request Parameters<a name="section24539173145638"></a>

This request contains no parameter.

## Request Headers<a name="section38099522145638"></a>

This request uses common headers. For details about common request headers, see section  [Common Request Headers](common-request-headers.md).

## Request Elements<a name="section58590878145638"></a>

This request contains no element.

## Response Syntax<a name="section5866353914519"></a>

```
HTTP/1.1 200 OK
Server: Server Name 
x-amz-request-id: request id 
x-amz-id-2: id 
x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
Content-Type: application/xml 
Content-Length: 0 
Date: date
<?xml version="1.0" encoding="UTF-8" standalone="yes"?> 
 
<Tagging xmlns="http://obs.example.com/doc/2015-06-30/"> 
    <TagSet> 
        <Tag> 
            <Key>TagNameJJ1</Key> 
            <Value>tytttasceettt</Value> 
        </Tag> 
</TagSet> 
</Tagging>
```

## Response Headers<a name="section1737390614519"></a>

This response uses common headers. For details about common response headers, see section  [Common Response Headers](common-response-headers.md).

## Response Elements<a name="section4911114514519"></a>

This response contains elements to detail bucket lifecycle configuration. The following table describes the elements.

**Table  1**  Elements to be configured for bucket tags

<a name="table55855374145027"></a>
<table><thead align="left"><tr id="row43394869145027"><th class="cellrowborder" valign="top" width="20.200000000000003%" id="mcps1.2.4.1.1"><p id="p25323481145027"><a name="p25323481145027"></a><a name="p25323481145027"></a>Element</p>
</th>
<th class="cellrowborder" valign="top" width="60.61%" id="mcps1.2.4.1.2"><p id="p37936074145027"><a name="p37936074145027"></a><a name="p37936074145027"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="19.189999999999998%" id="mcps1.2.4.1.3"><p id="p52923119145027"><a name="p52923119145027"></a><a name="p52923119145027"></a>Mandatory or Not</p>
</th>
</tr>
</thead>
<tbody><tr id="row58914224145027"><td class="cellrowborder" valign="top" width="20.200000000000003%" headers="mcps1.2.4.1.1 "><p id="p46789943103837"><a name="p46789943103837"></a><a name="p46789943103837"></a>Tagging</p>
</td>
<td class="cellrowborder" valign="top" width="60.61%" headers="mcps1.2.4.1.2 "><p id="p31889035103837"><a name="p31889035103837"></a><a name="p31889035103837"></a>Container for the <strong id="b18565866103837"><a name="b18565866103837"></a><a name="b18565866103837"></a>TagSet</strong>&nbsp;and&nbsp;<strong id="b32875072103837"><a name="b32875072103837"></a><a name="b32875072103837"></a>Tag</strong> elements</p>
<p id="p27440198103837"><a name="p27440198103837"></a><a name="p27440198103837"></a>Type:  Container</p>
<p id="p45635198103837"><a name="p45635198103837"></a><a name="p45635198103837"></a>Ancestor: None</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.3 "><p id="p5463532103837"><a name="p5463532103837"></a><a name="p5463532103837"></a>Yes</p>
</td>
</tr>
<tr id="row30825325103856"><td class="cellrowborder" valign="top" width="20.200000000000003%" headers="mcps1.2.4.1.1 "><p id="p63172917103947"><a name="p63172917103947"></a><a name="p63172917103947"></a>TagSet</p>
</td>
<td class="cellrowborder" valign="top" width="60.61%" headers="mcps1.2.4.1.2 "><p id="p16732614103947"><a name="p16732614103947"></a><a name="p16732614103947"></a>Container for a set of tags</p>
<p id="p16375801103947"><a name="p16375801103947"></a><a name="p16375801103947"></a>Type: Container</p>
<p id="p13164488103947"><a name="p13164488103947"></a><a name="p13164488103947"></a>Ancestor: Tagging</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.3 "><p id="p59690594103947"><a name="p59690594103947"></a><a name="p59690594103947"></a>Yes</p>
</td>
</tr>
<tr id="row2629709410396"><td class="cellrowborder" valign="top" width="20.200000000000003%" headers="mcps1.2.4.1.1 "><p id="p27899690103947"><a name="p27899690103947"></a><a name="p27899690103947"></a>Tag</p>
</td>
<td class="cellrowborder" valign="top" width="60.61%" headers="mcps1.2.4.1.2 "><p id="p45282441103947"><a name="p45282441103947"></a><a name="p45282441103947"></a>Container for tag information</p>
<p id="p4888788103947"><a name="p4888788103947"></a><a name="p4888788103947"></a>Type: Container. Each bucket supports a maximum of 10 tags.</p>
<p id="p43999100103947"><a name="p43999100103947"></a><a name="p43999100103947"></a>Ancestor:  TagSet</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.3 "><p id="p7157356103947"><a name="p7157356103947"></a><a name="p7157356103947"></a>Yes</p>
</td>
</tr>
<tr id="row19744018103911"><td class="cellrowborder" valign="top" width="20.200000000000003%" headers="mcps1.2.4.1.1 "><p id="p50330179103947"><a name="p50330179103947"></a><a name="p50330179103947"></a>Key</p>
</td>
<td class="cellrowborder" valign="top" width="60.61%" headers="mcps1.2.4.1.2 "><p id="p50212713103947"><a name="p50212713103947"></a><a name="p50212713103947"></a>Name of the tag</p>
<p id="p49261238103947"><a name="p49261238103947"></a><a name="p49261238103947"></a>Type: String. It can contain a maximum of 36 characters, including A to Z, a to z, 0 to 9, hyphens (-), underscores (_), and Unicode(\u4E00-\u9FFF). In the same bucket, the key of a tag must be unique.</p>
<p id="p40697959103947"><a name="p40697959103947"></a><a name="p40697959103947"></a>Ancestor: Tag</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.3 "><p id="p8200422103947"><a name="p8200422103947"></a><a name="p8200422103947"></a>Yes</p>
</td>
</tr>
<tr id="row9143931103933"><td class="cellrowborder" valign="top" width="20.200000000000003%" headers="mcps1.2.4.1.1 "><p id="p5419392103947"><a name="p5419392103947"></a><a name="p5419392103947"></a>Value</p>
</td>
<td class="cellrowborder" valign="top" width="60.61%" headers="mcps1.2.4.1.2 "><p id="p36317623103947"><a name="p36317623103947"></a><a name="p36317623103947"></a>Value of the tag</p>
<p id="p58423158103947"><a name="p58423158103947"></a><a name="p58423158103947"></a>Type: String. It can contain a maximum of 43 characters, including A to Z, a to z, 0 to 9, hyphens (-), underscores (_), periods (.), and Unicode(\u4E00-\u9FFF). Note that periods (.) can be used for this parameter.</p>
<p id="p56046379103947"><a name="p56046379103947"></a><a name="p56046379103947"></a>Ancestor: Tag</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.3 "><p id="p43462851103947"><a name="p43462851103947"></a><a name="p43462851103947"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Error Responses<a name="section3300087714519"></a>

Except for common error responses, special error responses are also returned. The following table lists error responses and possible causes.

**Table  2**  Error responses and possible causes

<a name="table3266664814519"></a>
<table><thead align="left"><tr id="row4080837914519"><th class="cellrowborder" valign="top" width="22.45%" id="mcps1.2.4.1.1"><p id="p1714439414519"><a name="p1714439414519"></a><a name="p1714439414519"></a>Error Code</p>
</th>
<th class="cellrowborder" valign="top" width="59.18%" id="mcps1.2.4.1.2"><p id="p4651869814519"><a name="p4651869814519"></a><a name="p4651869814519"></a>Possible Cause</p>
</th>
<th class="cellrowborder" valign="top" width="18.37%" id="mcps1.2.4.1.3"><p id="p991821114519"><a name="p991821114519"></a><a name="p991821114519"></a>HTTP Status Code</p>
</th>
</tr>
</thead>
<tbody><tr id="row6517759614519"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.4.1.1 "><p id="p8664140105157"><a name="p8664140105157"></a><a name="p8664140105157"></a>NoSuchTagSet</p>
</td>
<td class="cellrowborder" valign="top" width="59.18%" headers="mcps1.2.4.1.2 "><p id="p30706709105157"><a name="p30706709105157"></a><a name="p30706709105157"></a>The specified bucket is not configured with a tag.</p>
</td>
<td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.3 "><p id="p4215462105157"><a name="p4215462105157"></a><a name="p4215462105157"></a>404 Not Found</p>
</td>
</tr>
</tbody>
</table>

## Sample Request<a name="section21401127145254"></a>

```
GET /?tagging HTTP/1.1 
User-Agent: curl/7.19.7 (x86_64-suse-linux-gnu) libcurl/7.19.7 OpenSSL/0.9.8j zlib/1.2.7 libidn/1.10 
Host: bucketname.obs.example.com 
Accept: */* 
Date: Tue, 09 May 2017 03:17:07 +0000 
Authorization: authorization string
```

## Sample Response<a name="section32165774145254"></a>

```
HTTP/1.1 200 OK
Server: OBS 
x-amz-request-id: 0002B7532E0000015BEB35330C5884X1 
x-amz-id-2: s12w20LYNQqSb7moq4ibgJwmQRSmVQV+rFBqplOGYkXUpXeS/nOmbkyD+E35K79j 
x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
Content-Type: application/xml 
Date: Tue, 09 May 2017 03:16:23 GMT 
Content-Length: 441 
<?xml version="1.0" encoding="UTF-8" standalone="yes"?> 
<Tagging xmlns="http://obs.example.com/doc/2015-06-30/"> 
    <TagSet> 
        <Tag> 
            <Key>TagNameJJ1</Key> 
            <Value>tytttasceettt</Value> 
        </Tag> 
</TagSet> 
</Tagging>
```

