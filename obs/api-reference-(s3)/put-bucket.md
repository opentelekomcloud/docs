# PUT Bucket<a name="EN-US_TOPIC_0125560305"></a>

You can send the  **PUT Bucket**  request to create a bucket with the specified name.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>You can create a maximum of 100 buckets.  

The name of a bucket must be unique in OBS. If a user repeatedly creates namesake buckets in the same region, status code  **200** is returned. If namesake buckets are repeatedly created in other cases, status code **409** is returned. You can set the ACL of a bucket by adding optional header **x-amz-acl**  to a request.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>In multiple regions scenarios, if user A creates a bucket, deletes the bucket later, and immediately creates a bucket with the same name in different regions, the system will respond  **409**. If user A creates a bucket with the same name in different regions 30 minutes later, the system will respond **200**.  
>If a 5_xx_  error is returned from the server or the request times out during bucket creation, the system takes about 10 minutes to make bucket information consistent. During the process, bucket information is inaccurate.  

## Storage Class<a name="section47363625202820"></a>

Users are allowed to create buckets of different storage classes. The  **x-default-storage-class**  header in a bucket creation request specifies the default storage class for a bucket. The storage class of the objects in a bucket is the same as that of the bucket. There are three storage classes: STANDARD \(OBS Standard\), STANDARD\_IA \(OBS Warm\), and GLACIER \(OBS Cold\). If this header is not in the request, the storage class of the bucket created is OBS Standard. When users upload an object to a bucket, if they do not set the storage class of the object \(see  [PUT Object](put-object.md)\), the object will use the default storage class of the bucket.

## Request Syntax<a name="section38116128"></a>

```
PUT / HTTP/1.1 
 User-Agent: agent
 Host: Host Server
 Accept: */*
 Date: date 
 Authorization: authorization
 Content-Length: 0 
 <Optional Additional Header> 

 <CreateBucketConfiguration xmlns="http://obs.example.com/doc/2015-06-30/"> 
 <LocationConstraint>location</LocationConstraint> 
 </CreateBucketConfiguration>
```

## Request Parameters<a name="section7500834"></a>

This request involves no parameters.

## Request Headers<a name="section398650"></a>

This request uses common headers. For details about common request headers, see section  [Common Request Headers](common-request-headers.md).

You can add optional headers to this request.  [Table 1](#table31170320)  describes the optional headers.

**Table  1**  Optional request headers

<a name="table31170320"></a>
<table><thead align="left"><tr id="row47912089"><th class="cellrowborder" valign="top" width="33.333333333333336%" id="mcps1.2.4.1.1"><p id="p55673999"><a name="p55673999"></a><a name="p55673999"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="33.333333333333336%" id="mcps1.2.4.1.2"><p id="p13300041"><a name="p13300041"></a><a name="p13300041"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="33.333333333333336%" id="mcps1.2.4.1.3"><p id="p3561519"><a name="p3561519"></a><a name="p3561519"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row20047659"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p13247650"><a name="p13247650"></a><a name="p13247650"></a>x-amz-acl</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p66426750"><a name="p66426750"></a><a name="p66426750"></a>Indicates the ACL of a bucket. Possible values are <strong id="b60969846"><a name="b60969846"></a><a name="b60969846"></a>private</strong>,&nbsp;<strong id="b11857703"><a name="b11857703"></a><a name="b11857703"></a>public-read</strong>,&nbsp;<strong id="b39610468"><a name="b39610468"></a><a name="b39610468"></a>public-read-write</strong>,&nbsp;<strong id="b20949892"><a name="b20949892"></a><a name="b20949892"></a>authenticated-read</strong>,&nbsp;<strong id="b54331306"><a name="b54331306"></a><a name="b54331306"></a>bucket-owner-read</strong>, and&nbsp;<strong id="b19219710"><a name="b19219710"></a><a name="b19219710"></a>bucket-owner-full-control</strong>. For details, see&nbsp;<a href="acl.md#table40200743">Table 4</a>.</p>
<p id="p13292668"><a name="p13292668"></a><a name="p13292668"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p2964327"><a name="p2964327"></a><a name="p2964327"></a>Optional</p>
</td>
</tr>
<tr id="row23889184203239"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p57471669203319"><a name="p57471669203319"></a><a name="p57471669203319"></a>x-default-storage-class</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p14900873203330"><a name="p14900873203330"></a><a name="p14900873203330"></a>When creating a bucket, you can add this header in the request to set the bucket's default storage class, which can be STANDARD (OBS Standard), STANDARD_IA (OBS Warm), and GLACIER (OBS Cold). If this header is not specified in the request, the storage class of the bucket created is OBS Standard.</p>
<p id="p66998998203330"><a name="p66998998203330"></a><a name="p66998998203330"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p34271861203337"><a name="p34271861203337"></a><a name="p34271861203337"></a>Optional</p>
</td>
</tr>
<tr id="row1772355541119"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p2636530171316"><a name="p2636530171316"></a><a name="p2636530171316"></a>x-amz-security-token</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p176361330141312"><a name="p176361330141312"></a><a name="p176361330141312"></a>Header field used to identify the request of a federated user. When the federal authentication function is enabled, users sending such requests are identified as federated users.</p>
<p id="p186362030201310"><a name="p186362030201310"></a><a name="p186362030201310"></a>Type: string</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p1063603061316"><a name="p1063603061316"></a><a name="p1063603061316"></a>Optional. This parameter must be carried in the request sent by federated users.</p>
</td>
</tr>
</tbody>
</table>

## Request Elements<a name="section5296112755414"></a>

This request contains one element, as described in  [Table 2](#table5512965)

**Table  2**  Request element

<a name="table5512965"></a>
<table><thead align="left"><tr id="row5892555"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p7534928"><a name="p7534928"></a><a name="p7534928"></a>Element</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p6349446"><a name="p6349446"></a><a name="p6349446"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p44543124"><a name="p44543124"></a><a name="p44543124"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row51223331"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p55449179"><a name="p55449179"></a><a name="p55449179"></a>LocationConstraint</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p62198499"><a name="p62198499"></a><a name="p62198499"></a>Indicates the Region where a bucket will be created. This element is contained in <strong id="b22915580"><a name="b22915580"></a><a name="b22915580"></a>CreateBucketConfiguration</strong>.</p>
<p id="p4913635"><a name="p4913635"></a><a name="p4913635"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p62460164"><a name="p62460164"></a><a name="p62460164"></a>Optional</p>
</td>
</tr>
</tbody>
</table>

## Response Syntax<a name="section61603605"></a>

```
HTTP/1.1 status_code 
 Server: Server Name 
 x-amz-request-id: request id 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Location: location 
 x-amz-id-2: id 
 Date: date 
 Content-Length: 0
```

## Response Headers<a name="section17561535"></a>

This response uses common headers. For details about common response headers, see section  [Common Response Headers](common-response-headers.md).

## Response Elements<a name="section23836090"></a>

This response involves no elements.

## Error Responses<a name="section13198224"></a>

No special error responses are returned. For details about error responses, see  [Table 1](error-codes.md#table30733758).

## Sample Request<a name="section12795575"></a>

```
PUT / HTTP/1.1 
 User-Agent: Jakarta Commons-HttpClient/3.1 
 Host: bucketname.obs.example.com
 Accept: */* 
 Date: Sat, 03 Dec 2011 06:31:58 +0000 
 Authorization: AWS BF6C09F302931425E9A7:QBaO+tS/76QYHVnUoxvf9EPH/3o= 
 Content-Length: 0
```

## Sample Response<a name="section48051319"></a>

```
HTTP/1.1 200 OK 
 Server: OBS 
 x-amz-request-id: 001B21A61C6C00000134029F41D1527F 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Location: /bucketname 
 x-amz-id-2: MDAxQjIxQTYxQzZDMDAwMDAxMzQwMjlGNDFEMTUyN0ZBQUFBQUFBQWJiYmJiYmJi 
 Date: Sat, 03 Dec 2011 06:31:58 GMT 
 Content-Length: 0
```

## Sample Request \(Example of Setting the Region of a Bucket\)<a name="section29808687"></a>

```
PUT / HTTP/1.1 
 User-Agent: Jakarta Commons-HttpClient/3.1 
 Host: bucketname.obs.example.com 
 Accept: */* 
 Date: Sat, 03 Dec 2011 06:31:58 +0000 
 Authorization: AWS BF6C09F302931425E9A7:QBaO+tS/76QYHVnUoxvf9EPH/3o= 
 Content-Length: 149

<CreateBucketConfiguration xmlns="http://obs.example.com/doc/2015-06-30/"> 
<LocationConstraint>EU</LocationConstraint>
</CreateBucketConfiguration>
```

## Sample Response \(Example of Setting the Region of a Bucket\)<a name="section66951593"></a>

```
HTTP/1.1 200 OK 
 Server: OBS 
 x-amz-request-id: 001B21A61C6C00000134029F41D1527F 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc  
 Location: /bucketname 
 x-amz-id-2: MDAxQjIxQTYxQzZDMDAwMDAxMzQwMjlGNDFEMTUyN0ZBQUFBQUFBQWJiYmJiYmJi 
 Date: Sat, 03 Dec 2011 06:31:58 GMT 
 Content-Length: 0
```

