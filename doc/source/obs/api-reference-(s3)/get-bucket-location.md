# GET Bucket location<a name="EN-US_TOPIC_0125560404"></a>

Only the bucket owner or a user that is granted with the  **s3:GetBucketLocation**  permission in the bucket policy can obtain the bucket location information.

## Request Syntax<a name="section29779194"></a>

```
GET /?location HTTP/1.1 
 User-Agent: agent
 Host: bucketname.obs.example.com 
 Accept: */*
 Date: date 
 Authorization: authorization
```

## Request Parameters<a name="section66686155"></a>

This request involves no parameters.

## Request Headers<a name="section63304483"></a>

This request uses common headers. For details about common request headers, see section  [Common Request Headers](common-request-headers.md).

## Request Elements<a name="section32869435"></a>

This request involves no elements.

## Response Syntax<a name="section45329261"></a>

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
 <CreateBucketConfiguration xmlns="http://obs.example.com/doc/2015-06-30/"> 
 <LocationConstraint>Location</LocationConstraint> 
 </CreateBucketConfiguration>
```

## Response Headers<a name="section5310165"></a>

This response uses common headers. For details about common response headers, see section  [Common Response Headers](common-response-headers.md).

## Response Elements<a name="section47791486"></a>

This response contains an element to describe the bucket Region.  [Table 1](#table25305148)  describes this element.

**Table  1**  Response element

<a name="table25305148"></a>
<table><thead align="left"><tr id="row47009632"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p49683833"><a name="p49683833"></a><a name="p49683833"></a>Element</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p64967535"><a name="p64967535"></a><a name="p64967535"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row27878953"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p43602703"><a name="p43602703"></a><a name="p43602703"></a>LocationConstraint</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p42158091"><a name="p42158091"></a><a name="p42158091"></a>Indicates information about a bucket's Region.</p>
<p id="p43878499"><a name="p43878499"></a><a name="p43878499"></a>Type: String</p>
</td>
</tr>
</tbody>
</table>

## Error Responses<a name="section27470193"></a>

No special error responses are returned. For details about error responses, see  [Table 1](error-codes.md#table30733758).

## Sample Request<a name="section7915861"></a>

```
GET /?location HTTP/1.1 
 User-Agent: Jakarta Commons-HttpClient/3.1 
 Host: bucketname.obs.example.com
 Accept: */*
 Date: Sun, 26 Sep 2010 09:16:00 GMT  
 Authorization: AWS 04RZT432N80TGDF2Y2G2:JUtd9kkJFjbKbkP9f6T/tAxozYY= 
```

## Sample Response<a name="section4133890"></a>

```
HTTP/1.1 200 OK 
 Server: OBS 
 x-amz-request-id: 367CB63A2F283044981285492719060 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 x-amz-id-2: MzY3Q0I2M0EyRjI4MzA0NDk4MTI4NTQ5MjcxOTA2MEFBQUFBQUFBYmJiYmJiYmJD 
 Content-Type: application/xml 
 Date: Sun, 26 Sep 2010 09:18:36 GMT 
 Content-Length: 560 

 <?xml version="1.0" encoding="UTF-8" standalone="yes"?> 
 <CreateBucketConfiguration xmlns="http://obs.example.com/doc/2015-06-30/"> 
 <LocationConstraint>example</LocationConstraint> 
 </CreateBucketConfiguration>
```

