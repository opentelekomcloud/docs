# Complete Multipart Upload<a name="EN-US_TOPIC_0125560338"></a>

After uploading all parts for a multipart upload, you can use this operation to complete the multipart upload.

Upon receiving a Complete Multipart Upload request, OBS concatenates the specified parts to create a new object. All associated parts cannot be downloaded until the multipart upload is complete.

When starting to complete a multipart upload, OBS first copies the header information from the metadata of associated parts and then incorporates the header information into the metadata of the newly created object.

Before a multipart upload is completed, all associated parts occupy storage quota. After the multipart upload is completed, only parts included in the part list specified in the  **Complete Multipart Upload**  request are concatenated. These parts still occupy storage quota while other parts are deleted to release storage quota.

After a multipart upload is completed, you can send a  **GET**  request to obtain the newly created object or some parts comprising this object by specifying a range in the request. You can also send a **DELETE**  request to delete all parts uploaded for the multipart upload. The deleted parts cannot be restored.

The MD5 value recorded in the ETag of a newly created object is calculated using the MD5 values of the parts comprising this object. The object ETag is calculated as follows:

_MD5\(M<sub>1</sub>M<sub>2</sub>......M<sub>N</sub>\)-N_

where

**_M<sub>n</sub>_**  is the MD5 value of part N

**_N_**  is the total number of parts

## Versioning<a name="section2191769"></a>

If a bucket has versioning enabled, a unique version ID is generated for an object created from a multipart upload in this bucket and the version ID is returned in response header  **x-amz-version-id**. If the bucket has versioning suspended, the version ID of the object is **null**. For details about bucket versioning, see section  [PUT Bucket versioning](put-bucket-versioning.md).

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>If 10 parts are uploaded but only 9 parts are selected for combination, the part that is not combined will be automatically deleted. After the part is deleted, it cannot be restored. Before combining the parts, adopt the interface used to list the parts that have been uploaded to check all parts to ensure that no part is missed.  

## Request Syntax<a name="section4329874"></a>

```
POST /ObjectName?uploadId=uploadID HTTP/1.1 
 User-Agent: agent
 Host: bucketname.obs.example.com 
 Accept: */*
 Date: date 
 Content-Length: length 
 Authorization: auth
 Expect: expect
 <CompleteMultipartUpload> 
 <Part> 
 <PartNumber>partNum1</PartNumber> 
 <ETag>etag1</ETag> 
 </Part> 
 <Part> 
 <PartNumber>partNum2</PartNumber> 
 <ETag>etag2</ETag> 
 </Part> 
 <Part> 
 <PartNumber>partNum3</PartNumber> 
 <ETag>etag3</ETag> 
 </Part> 
 </CompleteMultipartUpload>
```

## Request Parameters<a name="section38968871"></a>

This request uses one parameter to specify the ID of the multipart upload to be completed.  [Table 1](#table6473820)  describes the parameter.

**Table  1**  Request parameter

<a name="table6473820"></a>
<table><thead align="left"><tr id="row27116914"><th class="cellrowborder" valign="top" width="21.04210421042104%" id="mcps1.2.4.1.1"><p id="p48986392"><a name="p48986392"></a><a name="p48986392"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="52.705270527052704%" id="mcps1.2.4.1.2"><p id="p8474815"><a name="p8474815"></a><a name="p8474815"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="26.25262526252625%" id="mcps1.2.4.1.3"><p id="p15371406"><a name="p15371406"></a><a name="p15371406"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row37124398"><td class="cellrowborder" valign="top" width="21.04210421042104%" headers="mcps1.2.4.1.1 "><p id="p54286279"><a name="p54286279"></a><a name="p54286279"></a>uploadId</p>
</td>
<td class="cellrowborder" valign="top" width="52.705270527052704%" headers="mcps1.2.4.1.2 "><p id="p35112448"><a name="p35112448"></a><a name="p35112448"></a>Indicates the ID of the multipart upload to be completed.</p>
<p id="p47576576"><a name="p47576576"></a><a name="p47576576"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="26.25262526252625%" headers="mcps1.2.4.1.3 "><p id="p28497420"><a name="p28497420"></a><a name="p28497420"></a>Mandatory</p>
</td>
</tr>
</tbody>
</table>

## Request Headers<a name="section15175522"></a>

This request uses common headers. For details about common request headers, see section  [Common Request Headers](common-request-headers.md).

## Request Elements<a name="section2361972"></a>

This request contains elements to specify the part list for the multipart upload to be completed.  [Table 2](#table57330131)  describes the elements.

**Table  2**  Request elements

<a name="table57330131"></a>
<table><thead align="left"><tr id="row419316"><th class="cellrowborder" valign="top" width="23.212321232123212%" id="mcps1.2.4.1.1"><p id="p33964601"><a name="p33964601"></a><a name="p33964601"></a>Element</p>
</th>
<th class="cellrowborder" valign="top" width="51.035103510351036%" id="mcps1.2.4.1.2"><p id="p66778138"><a name="p66778138"></a><a name="p66778138"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="25.752575257525752%" id="mcps1.2.4.1.3"><p id="p40320129"><a name="p40320129"></a><a name="p40320129"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row44704979"><td class="cellrowborder" valign="top" width="23.212321232123212%" headers="mcps1.2.4.1.1 "><p id="p64333562"><a name="p64333562"></a><a name="p64333562"></a>CompleteMultipartUpload</p>
</td>
<td class="cellrowborder" valign="top" width="51.035103510351036%" headers="mcps1.2.4.1.2 "><p id="p43636062"><a name="p43636062"></a><a name="p43636062"></a>Indicates the container for the list of parts to be concatenated.</p>
<p id="p57180242"><a name="p57180242"></a><a name="p57180242"></a>Type: XML</p>
</td>
<td class="cellrowborder" valign="top" width="25.752575257525752%" headers="mcps1.2.4.1.3 "><p id="p1088027"><a name="p1088027"></a><a name="p1088027"></a>Mandatory</p>
</td>
</tr>
<tr id="row9792251"><td class="cellrowborder" valign="top" width="23.212321232123212%" headers="mcps1.2.4.1.1 "><p id="p54974852"><a name="p54974852"></a><a name="p54974852"></a>PartNumber</p>
</td>
<td class="cellrowborder" valign="top" width="51.035103510351036%" headers="mcps1.2.4.1.2 "><p id="p23778026"><a name="p23778026"></a><a name="p23778026"></a>Indicates the number that identifies a part.</p>
<p id="p12675643"><a name="p12675643"></a><a name="p12675643"></a>Type: Integer</p>
</td>
<td class="cellrowborder" valign="top" width="25.752575257525752%" headers="mcps1.2.4.1.3 "><p id="p20094134"><a name="p20094134"></a><a name="p20094134"></a>Mandatory</p>
</td>
</tr>
<tr id="row46629482"><td class="cellrowborder" valign="top" width="23.212321232123212%" headers="mcps1.2.4.1.1 "><p id="p18891734"><a name="p18891734"></a><a name="p18891734"></a>ETag</p>
</td>
<td class="cellrowborder" valign="top" width="51.035103510351036%" headers="mcps1.2.4.1.2 "><p id="p53835453"><a name="p53835453"></a><a name="p53835453"></a>Indicates the ETag returned after a part is uploaded.</p>
<p id="p14757035"><a name="p14757035"></a><a name="p14757035"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="25.752575257525752%" headers="mcps1.2.4.1.3 "><p id="p54469209"><a name="p54469209"></a><a name="p54469209"></a>Mandatory</p>
</td>
</tr>
</tbody>
</table>

## Response Syntax<a name="section6261685"></a>

```
HTTP/1.1 status_code 
 x-amz-id-2: id 
 x-amz-request-id: request id 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 x-reserved-indicator: indicator
 Content-Type: type
 Date: date 
 Connection: state 
 Server: server     
<?xml version="1.0" encoding="UTF-8" standalone="yes"?> 
 <CompleteMultipartUploadResult xmlns="http://obs.example.com/doc/2015-06-30/"> 
 <Location>http://example-Bucket.obs.example.com/example-Object</Location> 
 <Bucket>BucketName</Bucket> 
 <Key>ObjectName</Key> 
 <ETag>ETag</ETag> 
 </CompleteMultipartUploadResult>
```

## Response Headers<a name="section56355167"></a>

This response uses common headers. For details about common response headers, see section  [Common Response Headers](common-response-headers.md).

This response also uses one optional header, as described in  [Table 3](#table49929783).

**Table  3**  Optional response header

<a name="table49929783"></a>
<table><thead align="left"><tr id="row56148564"><th class="cellrowborder" valign="top" width="42.77%" id="mcps1.2.3.1.1"><p id="p51739874"><a name="p51739874"></a><a name="p51739874"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="57.230000000000004%" id="mcps1.2.3.1.2"><p id="p30180276"><a name="p30180276"></a><a name="p30180276"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row28683315"><td class="cellrowborder" valign="top" width="42.77%" headers="mcps1.2.3.1.1 "><p id="p41647174"><a name="p41647174"></a><a name="p41647174"></a>x-amz-version-id</p>
</td>
<td class="cellrowborder" valign="top" width="57.230000000000004%" headers="mcps1.2.3.1.2 "><p id="p17977942"><a name="p17977942"></a><a name="p17977942"></a>Indicates the version ID of the object created from a multipart upload.</p>
<p id="p27583752"><a name="p27583752"></a><a name="p27583752"></a>Type: String</p>
</td>
</tr>
<tr id="row47127628104355"><td class="cellrowborder" valign="top" width="42.77%" headers="mcps1.2.3.1.1 "><p id="p7599119171420"><a name="p7599119171420"></a><a name="p7599119171420"></a>x-amz-server-side-encryption</p>
</td>
<td class="cellrowborder" valign="top" width="57.230000000000004%" headers="mcps1.2.3.1.2 "><p id="p11548897171420"><a name="p11548897171420"></a><a name="p11548897171420"></a>This header is included in a response if SSE-KMS is used.</p>
<p id="p36831211171420"><a name="p36831211171420"></a><a name="p36831211171420"></a>Type: string</p>
<p id="p63045451171420"><a name="p63045451171420"></a><a name="p63045451171420"></a>Example: x-amz-server-side-encryption:aws:kms</p>
</td>
</tr>
<tr id="row2030036510440"><td class="cellrowborder" valign="top" width="42.77%" headers="mcps1.2.3.1.1 "><p id="p57671339171420"><a name="p57671339171420"></a><a name="p57671339171420"></a>x-amz-server-side-encryption-aws-kms-key-id</p>
</td>
<td class="cellrowborder" valign="top" width="57.230000000000004%" headers="mcps1.2.3.1.2 "><p id="p40866906171420"><a name="p40866906171420"></a><a name="p40866906171420"></a>Indicates the master key ID. This header is included in a response if SSE-KMS is used.</p>
<p id="p32257837171420"><a name="p32257837171420"></a><a name="p32257837171420"></a>Example: x-amz-server-side-encryption-aws-kms-key-id:arn:aws:kms:sichuan:domainiddomainiddomainiddoma0001:key/4f1cd4de-ab64-4807-920a-47fc42e7f0d0</p>
</td>
</tr>
<tr id="row6543377910443"><td class="cellrowborder" valign="top" width="42.77%" headers="mcps1.2.3.1.1 "><p id="p27861469171420"><a name="p27861469171420"></a><a name="p27861469171420"></a>x-amz-server-side-encryption-customer-algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="57.230000000000004%" headers="mcps1.2.3.1.2 "><p id="p42186497171420"><a name="p42186497171420"></a><a name="p42186497171420"></a>Indicates an encryption algorithm. This header is included in a response if SSE-C is used.</p>
<p id="p44134156171420"><a name="p44134156171420"></a><a name="p44134156171420"></a>Type: string</p>
<p id="p61663090171420"><a name="p61663090171420"></a><a name="p61663090171420"></a>Example: x-amz-server-side-encryption-customer-algorithm:AES256</p>
</td>
</tr>
</tbody>
</table>

## Response Elements<a name="section37434462"></a>

This response contains elements to indicate the results of completing a multipart upload.  [Table 4](#table32583578)  describes the elements.

**Table  4**  Response elements

<a name="table32583578"></a>
<table><thead align="left"><tr id="row51931690"><th class="cellrowborder" valign="top" width="29.01%" id="mcps1.2.3.1.1"><p id="p45717377"><a name="p45717377"></a><a name="p45717377"></a>Element</p>
</th>
<th class="cellrowborder" valign="top" width="70.99%" id="mcps1.2.3.1.2"><p id="p12120085"><a name="p12120085"></a><a name="p12120085"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row42202829"><td class="cellrowborder" valign="top" width="29.01%" headers="mcps1.2.3.1.1 "><p id="p62986002"><a name="p62986002"></a><a name="p62986002"></a>Location</p>
</td>
<td class="cellrowborder" valign="top" width="70.99%" headers="mcps1.2.3.1.2 "><p id="p1592523"><a name="p1592523"></a><a name="p1592523"></a>Indicates the URL of the newly created object.</p>
<p id="p14332711"><a name="p14332711"></a><a name="p14332711"></a>Type: String</p>
</td>
</tr>
<tr id="row61885537"><td class="cellrowborder" valign="top" width="29.01%" headers="mcps1.2.3.1.1 "><p id="p46672571"><a name="p46672571"></a><a name="p46672571"></a>Bucket</p>
</td>
<td class="cellrowborder" valign="top" width="70.99%" headers="mcps1.2.3.1.2 "><p id="p22381889"><a name="p22381889"></a><a name="p22381889"></a>Indicates the bucket that contains the newly created object.</p>
<p id="p110417"><a name="p110417"></a><a name="p110417"></a>Type: String</p>
</td>
</tr>
<tr id="row993757"><td class="cellrowborder" valign="top" width="29.01%" headers="mcps1.2.3.1.1 "><p id="p13385460"><a name="p13385460"></a><a name="p13385460"></a>Key</p>
</td>
<td class="cellrowborder" valign="top" width="70.99%" headers="mcps1.2.3.1.2 "><p id="p10480496"><a name="p10480496"></a><a name="p10480496"></a>Indicates the key of the newly created object.</p>
<p id="p27215608"><a name="p27215608"></a><a name="p27215608"></a>Type: String</p>
</td>
</tr>
<tr id="row43613881"><td class="cellrowborder" valign="top" width="29.01%" headers="mcps1.2.3.1.1 "><p id="p43063478"><a name="p43063478"></a><a name="p43063478"></a>ETag</p>
</td>
<td class="cellrowborder" valign="top" width="70.99%" headers="mcps1.2.3.1.2 "><p id="p65589712"><a name="p65589712"></a><a name="p65589712"></a>Indicates the ETag that identifies the metadata of the newly created object. This ETag is calculated using the MD5 values of parts comprising the newly created object.</p>
<p id="p53436499"><a name="p53436499"></a><a name="p53436499"></a>Type: String</p>
</td>
</tr>
</tbody>
</table>

## Error Responses<a name="section1365842"></a>

-   If the request contains no request body, OBS returns status code  **400 Bad Request**.
-   If the request contains a request body in incorrect syntax, OBS returns status code  **400 Bad Request**.
-   If parts are not listed in the request body in ascending order, OBS returns status code  **400 Bad Request** and error code **InvalidPartOrder**.
-   If an AK or signature is invalid, OBS returns status code  **403 Forbidden** and error code **AccessDenied**.
-   If the requested bucket does not exist, OBS returns status code  **404 Not Found** and error code **NoSuchBucket**.
-   If the requested multipart upload does not exist, OBS returns  **404 NotFound** and error code **NoSuchUpload**.
-   If the requester is not the initiator of the multipart upload, OBS returns status code  **403 Forbidden** and error code **AccessDenied**.
-   If the part list contains nonexistent parts, OBS returns status code  **400 Bad Request** and error code **InvalidPart**.
-   If the ETag of a part in the part list is incorrect, OBS returns status code  **400 Bad Request** and error code **InvalidPart**.
-   If the size of a part \(excluding the last part\) in the part list is smaller than 5 MB, OBS returns status code  **400 Bad Request**.
-   If the size of the newly created object is greater than 48.8 TB, OBS returns status code  **400 Bad Request**.

For details about other error responses, see  [Table 1](error-codes.md#table30733758).

## Sample Request<a name="section15624539"></a>

```
POST /example-object?uploadId=AAAsb2FkIElEIGZvciBlbHZpbmcncyWeeS1tb3ZpZS5tMnRzIRRwbG9hZA HTTP/1.1 
 User-Agent: Jakarta Commons-HttpClient/3.1
 Host: bucketname.obs.example.com 
 Accept: */*
 Date: Mon, 1 Nov 2010 20:34:56 GMT 
 Content-Length: 391 
 Authorization: AWS AKIAIOSFODNN7EXAMPLE:0RQf4/cRonhpaBX5sCYVf1bNRuU=
 Expect: 100-continue
 <CompleteMultipartUpload> 
 <Part> 
 <PartNumber>1</PartNumber> 
 <ETag>"a54357aff0632cce46d942af68356b38"</ETag> 
 </Part> 
 <Part> 
 <PartNumber>2</PartNumber> 
 <ETag>"0c78aef83f66abc1fa1e8477f296d394"</ETag> 
 </Part> 
 <Part> 
 <PartNumber>3</PartNumber> 
 <ETag>"acbd18db4cc2f85cedef654fccc4a4d8"</ETag> 
 </Part> 
 </CompleteMultipartUpload>
```

## Sample Response<a name="section6403130"></a>

```
HTTP/1.1 200 OK 
 x-amz-id-2: Uuag1LuByRx9e6j5Onimru9pO4ZVKnJ2Qz7/C1NPcfTWAtRPfTaOFg== 
 x-amz-request-id: 656c76696e6727732072657175657374 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 x-reserved-indicator: 3
 Content-Type: application/xml
 Date: Mon, 1 Nov 2010 20:34:56 GMT 
 Connection: close 
 Content-Length: 306
 Server: OBS     
<?xml version="1.0" encoding="UTF-8"?> 
 <CompleteMultipartUploadResult xmlns="http://obs.example.com/doc/2015-06-30/"> 
 <Location>http://example-Bucket.obs.example.com/example-Object</Location> 
 <Bucket>Example-Bucket</Bucket> 
 <Key>Example-Object</Key> 
 <ETag>"3858f62230ac3c915f300c664312c11f-9"</ETag> 
 </CompleteMultipartUploadResult>
```

## Sample Request \(Getting an Object Created from a Multipart Upload with Version ID Specified\)<a name="section48891485"></a>

```
 POST /object?uploadId=DCD2FC9CAB7800000143947AB58A5094 HTTP/1.1
 User-Agent: Jakarta Commons-HttpClient/3.1
 Host: bucketname.obs.example.com 
 Accept: */*
 Date: Wed, 15 Jan 2014 06:09:39 +0000 
 Authorization: AWS C9590CEB8EC051BDEC9D:xQ9EFib6cohqMu2bLLJ0soseeUI= 
 Content-Length: 155   
 Expect: 100-continue
 <CompleteMultipartUpload> 
 <Part> 
 <PartNumber>1</PartNumber> 
 <ETag>"9fd2e548507ceef1a2183a8328b5cf2c"</ETag> 
 </Part> 
 </CompleteMultipartUpload>
```

## Sample Response \(Getting an Object Created from a Multipart Upload with Version ID Specified\)<a name="section37370189"></a>

```
HTTP/1.1 200 OK 
 Server: OBS 
 x-amz-request-id: DCD2FC9CAB78000001439484FB045617 
 x-amz-id-2: xw5X6Y7YIpWnQgHNYG3ce4+lj8O1GjiGvFXSgdPV1x2tYn2iZXFnTJm0yh5X5XnV 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 x-reserved-indicator: 3
 Content-Type: application/xml 
 x-amz-version-id: AAABQ5R6tZ7c0vycq3gAAAAbVURTRkha 
 Date: Wed, 15 Jan 2014 06:09:39 GMT 
 Content-Length: 300 
 <?xml version="1.0" encoding="UTF-8" standalone="yes"?> 
 <CompleteMultipartUploadResult xmlns="http://obs.example.com/doc/2015-06-30/"> 
 <Location>/example/multi</Location> 
 <Bucket>example</Bucket> 
 <Key>multi</Key> 
 <ETag>"59297fcb0de64c706cbb46e382d9c625-1"</ETag> 
 </CompleteMultipartUploadResult>
```

