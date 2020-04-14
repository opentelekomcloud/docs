# DELETE Multiple Objects<a name="EN-US_TOPIC_0125560366"></a>

You can use this operation to delete multiple objects from a bucket in batches.

Deleted objects cannot be restored or accessed using  **LIST**  or  **GET**. The OBS deletes multiple objects simultaneously and returns the deletion result of each object.

The  **DELETE Multiple Objects**  operation supports two modes for response: verbose and quiet.

In verbose mode, the returned response includes the deletion result of each requested object in an XML file.

In quiet mode, the returned response includes only results of objects failed to be deleted. The OBS uses verbose mode by default and you can specify quiet mode in the request body.

A  **DELETE Multiple Objects**  request must contain headers  **Content-MD5**  and  **Content-Length**  to detect network errors.

## Request Syntax<a name="section7589824"></a>

```
POST /?delete HTTP/1.1  
 User-Agent: agent
 Host: bucketname.obs.example.com 
 Accept: */*
 Date: date
 Authorization: Signature  
 Content-MD5: MD5 
 Content-Length: length 
 Expect: expect

 <?xml version="1.0" encoding="UTF-8"?> 
 <Delete> 
 <Quiet>true</Quiet>  
 <Object> 
 <Key>Key1</Key> 
 </Object>  
 <Object>  
 <Key>Key2</Key> 
 </Object> 
 </Delete>  
```

## Request Parameters<a name="section1199559"></a>

This request involves no parameters.

## Request Headers<a name="section10796036"></a>

This request uses common headers. For details about common request headers, see section  [Common Request Headers](common-request-headers.md).

## Request Elements<a name="section30055464"></a>

This request uses elements to specify the list of objects to be deleted in batches.  [Table 1](#table42836777)  describes the elements.

**Table  1**  Request elements

<a name="table42836777"></a>
<table><thead align="left"><tr id="row59230144"><th class="cellrowborder" valign="top" width="24.392439243924393%" id="mcps1.2.4.1.1"><p id="p32912398"><a name="p32912398"></a><a name="p32912398"></a>Element</p>
</th>
<th class="cellrowborder" valign="top" width="47.98479847984798%" id="mcps1.2.4.1.2"><p id="p48658592"><a name="p48658592"></a><a name="p48658592"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="27.622762276227625%" id="mcps1.2.4.1.3"><p id="p49031903"><a name="p49031903"></a><a name="p49031903"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row38633946"><td class="cellrowborder" valign="top" width="24.392439243924393%" headers="mcps1.2.4.1.1 "><p id="p42341959"><a name="p42341959"></a><a name="p42341959"></a>Quiet</p>
</td>
<td class="cellrowborder" valign="top" width="47.98479847984798%" headers="mcps1.2.4.1.2 "><p id="p1085814181877"><a name="p1085814181877"></a><a name="p1085814181877"></a>Indicates the element to enable quite mode for the request. If the element is specified, OBS returns only the list of objects that failed to be deleted.</p>
<p id="p7146644"><a name="p7146644"></a><a name="p7146644"></a>This element is only valid when its value is <strong id="b64319798"><a name="b64319798"></a><a name="b64319798"></a>true</strong>. Otherwise, OBS ignores it.</p>
<p id="p42007273"><a name="p42007273"></a><a name="p42007273"></a>Type: Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="27.622762276227625%" headers="mcps1.2.4.1.3 "><p id="p47145967"><a name="p47145967"></a><a name="p47145967"></a>Optional</p>
</td>
</tr>
<tr id="row21660524"><td class="cellrowborder" valign="top" width="24.392439243924393%" headers="mcps1.2.4.1.1 "><p id="p9671997"><a name="p9671997"></a><a name="p9671997"></a>Delete</p>
</td>
<td class="cellrowborder" valign="top" width="47.98479847984798%" headers="mcps1.2.4.1.2 "><p id="p45234324"><a name="p45234324"></a><a name="p45234324"></a>Indicates the list of objects to be deleted.</p>
<p id="p4455732"><a name="p4455732"></a><a name="p4455732"></a>Type: XML</p>
</td>
<td class="cellrowborder" valign="top" width="27.622762276227625%" headers="mcps1.2.4.1.3 "><p id="p25369996"><a name="p25369996"></a><a name="p25369996"></a>Mandatory</p>
</td>
</tr>
<tr id="row27003373"><td class="cellrowborder" valign="top" width="24.392439243924393%" headers="mcps1.2.4.1.1 "><p id="p39789633"><a name="p39789633"></a><a name="p39789633"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="47.98479847984798%" headers="mcps1.2.4.1.2 "><p id="p1734841"><a name="p1734841"></a><a name="p1734841"></a>Indicates an object to be deleted.</p>
<p id="p15613574"><a name="p15613574"></a><a name="p15613574"></a>Type: XML</p>
</td>
<td class="cellrowborder" valign="top" width="27.622762276227625%" headers="mcps1.2.4.1.3 "><p id="p56740016"><a name="p56740016"></a><a name="p56740016"></a>Mandatory</p>
</td>
</tr>
<tr id="row40898103"><td class="cellrowborder" valign="top" width="24.392439243924393%" headers="mcps1.2.4.1.1 "><p id="p24412045"><a name="p24412045"></a><a name="p24412045"></a>Key</p>
</td>
<td class="cellrowborder" valign="top" width="47.98479847984798%" headers="mcps1.2.4.1.2 "><p id="p31218599"><a name="p31218599"></a><a name="p31218599"></a>Indicates the key of an object to be deleted.</p>
<p id="p12531937"><a name="p12531937"></a><a name="p12531937"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="27.622762276227625%" headers="mcps1.2.4.1.3 "><p id="p8453981"><a name="p8453981"></a><a name="p8453981"></a>Mandatory</p>
</td>
</tr>
<tr id="row8976969"><td class="cellrowborder" valign="top" width="24.392439243924393%" headers="mcps1.2.4.1.1 "><p id="p56045856"><a name="p56045856"></a><a name="p56045856"></a>VersionId</p>
</td>
<td class="cellrowborder" valign="top" width="47.98479847984798%" headers="mcps1.2.4.1.2 "><p id="p43420508"><a name="p43420508"></a><a name="p43420508"></a>Indicates the version ID of an object to be deleted.</p>
<p id="p55240260"><a name="p55240260"></a><a name="p55240260"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="27.622762276227625%" headers="mcps1.2.4.1.3 "><p id="p45276050"><a name="p45276050"></a><a name="p45276050"></a>Optional</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>Request constraints:  
>This request can delete a maximum of 1000 objects at a time. If you send the request to delete more than 1000 objects, OBS returns an error response.  
>After receiving the request, OBS deletes objects simultaneously in a circular manner. During this process, OBS may encounter an internal error. For example, data inconsistency may occur because the metadata of an object still exists after the object's index data is deleted.  

## Response Syntax<a name="section65367744"></a>

```
HTTP/1.1 status_code 
 x-amz-id-2: id 
 x-amz-request-id: request id 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Date: date 
 Content-Type: type 
 Content-Length: length  
 Server: server  

 <?xml version="1.0" encoding="UTF-8" standalone="yes"?> 
 <DeleteResult xmlns="http://obs.example.com/doc/2015-06-30/"> 
 <Deleted> 
 <Key>Key1</Key> 
 </Deleted> 
 <Error> 
 <Key>Key2</Key> 
 <Code>InternalError</Code> 
 <Message>Internal Error</Message> 
 </Error> 
 </DeleteResult>
```

## Response Headers<a name="section51438785"></a>

This response uses common headers. For details about common response headers, see section  [Common Response Headers](common-response-headers.md).

## Response Elements<a name="section60295883"></a>

This response contains elements to return results of object deletion.  [Table 2](#table56991560)  describes the elements.

**Table  2**  Response elements

<a name="table56991560"></a>
<table><thead align="left"><tr id="row39761544"><th class="cellrowborder" valign="top" width="24.292429242924293%" id="mcps1.2.4.1.1"><p id="p66568510"><a name="p66568510"></a><a name="p66568510"></a>Element</p>
</th>
<th class="cellrowborder" valign="top" width="47.89478947894789%" id="mcps1.2.4.1.2"><p id="p23340236"><a name="p23340236"></a><a name="p23340236"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="27.81278127812781%" id="mcps1.2.4.1.3"><p id="p11511003"><a name="p11511003"></a><a name="p11511003"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row36490171"><td class="cellrowborder" valign="top" width="24.292429242924293%" headers="mcps1.2.4.1.1 "><p id="p2913837"><a name="p2913837"></a><a name="p2913837"></a>DeleteResult</p>
</td>
<td class="cellrowborder" valign="top" width="47.89478947894789%" headers="mcps1.2.4.1.2 "><p id="p34694260"><a name="p34694260"></a><a name="p34694260"></a>Indicates the container for the response.</p>
<p id="p43812891"><a name="p43812891"></a><a name="p43812891"></a>Type: Container</p>
</td>
<td class="cellrowborder" valign="top" width="27.81278127812781%" headers="mcps1.2.4.1.3 "><p id="p59183292"><a name="p59183292"></a><a name="p59183292"></a>Mandatory</p>
</td>
</tr>
<tr id="row62887584"><td class="cellrowborder" valign="top" width="24.292429242924293%" headers="mcps1.2.4.1.1 "><p id="p60729557"><a name="p60729557"></a><a name="p60729557"></a>Deleted</p>
</td>
<td class="cellrowborder" valign="top" width="47.89478947894789%" headers="mcps1.2.4.1.2 "><p id="p20147070"><a name="p20147070"></a><a name="p20147070"></a>Indicates the container element for a successful deletion.</p>
<p id="p47105906"><a name="p47105906"></a><a name="p47105906"></a>Type: Container</p>
</td>
<td class="cellrowborder" valign="top" width="27.81278127812781%" headers="mcps1.2.4.1.3 "><p id="p57482021"><a name="p57482021"></a><a name="p57482021"></a>Mandatory</p>
</td>
</tr>
<tr id="row47576142"><td class="cellrowborder" valign="top" width="24.292429242924293%" headers="mcps1.2.4.1.1 "><p id="p28462276"><a name="p28462276"></a><a name="p28462276"></a>Error</p>
</td>
<td class="cellrowborder" valign="top" width="47.89478947894789%" headers="mcps1.2.4.1.2 "><p id="p23743056"><a name="p23743056"></a><a name="p23743056"></a>Indicates the container for a failed deletion.</p>
<p id="p12360912"><a name="p12360912"></a><a name="p12360912"></a>Type: Container</p>
</td>
<td class="cellrowborder" valign="top" width="27.81278127812781%" headers="mcps1.2.4.1.3 "><p id="p61709845"><a name="p61709845"></a><a name="p61709845"></a>Mandatory</p>
</td>
</tr>
<tr id="row18517699"><td class="cellrowborder" valign="top" width="24.292429242924293%" headers="mcps1.2.4.1.1 "><p id="p23538684"><a name="p23538684"></a><a name="p23538684"></a>Key</p>
</td>
<td class="cellrowborder" valign="top" width="47.89478947894789%" headers="mcps1.2.4.1.2 "><p id="p27585257"><a name="p27585257"></a><a name="p27585257"></a>Indicates the key of a deleted object.</p>
<p id="p46940727"><a name="p46940727"></a><a name="p46940727"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="27.81278127812781%" headers="mcps1.2.4.1.3 "><p id="p44102542"><a name="p44102542"></a><a name="p44102542"></a>Mandatory</p>
</td>
</tr>
<tr id="row61378561"><td class="cellrowborder" valign="top" width="24.292429242924293%" headers="mcps1.2.4.1.1 "><p id="p5607548"><a name="p5607548"></a><a name="p5607548"></a>Code</p>
</td>
<td class="cellrowborder" valign="top" width="47.89478947894789%" headers="mcps1.2.4.1.2 "><p id="p51558219"><a name="p51558219"></a><a name="p51558219"></a>Indicates the status code for a failed deletion.</p>
<p id="p61370790"><a name="p61370790"></a><a name="p61370790"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="27.81278127812781%" headers="mcps1.2.4.1.3 "><p id="p4978063"><a name="p4978063"></a><a name="p4978063"></a>Mandatory</p>
</td>
</tr>
<tr id="row44802567"><td class="cellrowborder" valign="top" width="24.292429242924293%" headers="mcps1.2.4.1.1 "><p id="p5129283"><a name="p5129283"></a><a name="p5129283"></a>Message</p>
</td>
<td class="cellrowborder" valign="top" width="47.89478947894789%" headers="mcps1.2.4.1.2 "><p id="p12818804"><a name="p12818804"></a><a name="p12818804"></a>Indicates the error details about a failed deletion.</p>
<p id="p48260380"><a name="p48260380"></a><a name="p48260380"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="27.81278127812781%" headers="mcps1.2.4.1.3 "><p id="p16776727"><a name="p16776727"></a><a name="p16776727"></a>Mandatory</p>
</td>
</tr>
<tr id="row16772820"><td class="cellrowborder" valign="top" width="24.292429242924293%" headers="mcps1.2.4.1.1 "><p id="p16421203"><a name="p16421203"></a><a name="p16421203"></a>VersionId</p>
</td>
<td class="cellrowborder" valign="top" width="47.89478947894789%" headers="mcps1.2.4.1.2 "><p id="p55049062"><a name="p55049062"></a><a name="p55049062"></a>Indicates the version ID of an object to be deleted.</p>
<p id="p25679515"><a name="p25679515"></a><a name="p25679515"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="27.81278127812781%" headers="mcps1.2.4.1.3 "><p id="p66774824"><a name="p66774824"></a><a name="p66774824"></a>Optional</p>
</td>
</tr>
<tr id="row64102506"><td class="cellrowborder" valign="top" width="24.292429242924293%" headers="mcps1.2.4.1.1 "><p id="p24920491"><a name="p24920491"></a><a name="p24920491"></a>DeleteMarker</p>
</td>
<td class="cellrowborder" valign="top" width="47.89478947894789%" headers="mcps1.2.4.1.2 "><p id="p5293856"><a name="p5293856"></a><a name="p5293856"></a>If this element is specified, <strong id="b47644705"><a name="b47644705"></a><a name="b47644705"></a>true</strong> will be returned when you create or delete a deletion mark in the requested bucket with versioning enabled.</p>
<p id="p26149169"><a name="p26149169"></a><a name="p26149169"></a>Type: Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="27.81278127812781%" headers="mcps1.2.4.1.3 "><p id="p37707976"><a name="p37707976"></a><a name="p37707976"></a>Optional</p>
</td>
</tr>
<tr id="row3827464"><td class="cellrowborder" valign="top" width="24.292429242924293%" headers="mcps1.2.4.1.1 "><p id="p41589152"><a name="p41589152"></a><a name="p41589152"></a>DeleteMarkerVersionId</p>
</td>
<td class="cellrowborder" valign="top" width="47.89478947894789%" headers="mcps1.2.4.1.2 "><p id="p13278128"><a name="p13278128"></a><a name="p13278128"></a>Indicates the version ID of the deletion marker deleted or created by the request.</p>
<p id="p52394293"><a name="p52394293"></a><a name="p52394293"></a>If the <strong id="b8122131314152"><a name="b8122131314152"></a><a name="b8122131314152"></a>DELETE multiple objects</strong> request either creates or deletes a deletion marker, OBS returns this element in response with the version ID of the deletion marker. This element will be returned in either of the following cases:</p>
<a name="ul16079341"></a><a name="ul16079341"></a><ul id="ul16079341"><li>You send a non-version <strong id="b27358258"><a name="b27358258"></a><a name="b27358258"></a>DELETE multiple object</strong> request, that is, you specify only object key but not the version ID. In this case, OBS creates a deletion marker and returns its version ID in the response.</li><li>You send a version <strong id="b1426411"><a name="b1426411"></a><a name="b1426411"></a>DELETE multiple objects</strong> request, that is, you specify an object key and a version ID that identifies a deletion marker. In this case, OBS deletes a deletion marker and returns its version ID in the response.</li></ul>
<p id="p12837703"><a name="p12837703"></a><a name="p12837703"></a>Type: Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="27.81278127812781%" headers="mcps1.2.4.1.3 "><p id="p33221002"><a name="p33221002"></a><a name="p33221002"></a>Optional</p>
</td>
</tr>
</tbody>
</table>

## Error Responses<a name="section5792039"></a>

1.  If more than 1000 objects are requested, OBS returns status code  **400 Bad Request**.
2.  If an object key is invalid \(for example, the object key contains 1024 characters\), OBS returns status code  **400 Bad Request**.
3.  If the  **Content-MD5** header does not exist, OBS returns status code **400 Bad Request**.
4.  If bucket metadata does not exist, OBS returns status code  **404 Not Found** and error code **NoSuchBucket**.
5.  If the requester does not have  **WRITE**  permission for the requested bucket, OBS returns status code **403 Forbidden**  and prompt message **AccessDenied**.

For details about other error responses, see  [Table 1](error-codes.md#table30733758).

## Sample Request<a name="section46319263"></a>

```
POST /?delete HTTP/1.1  
 User-Agent: Jakarta Commons-HttpClient/3.1
 Host: bucketname.obs.example.com 
 Accept: */*
 Date: Tue, 14 Jan 2014 12:10:09 +0000
 Authorization: AWS BF6C09F302931425E9A7:wQ1Tp3rD7kaUCsYfPKxOIN7NoSA=  
 Content-MD5: 367CB63A2F283044981285491015079 
 Content-Length: 135 
 Expect: 100-continue

 <?xml version="1.0" encoding="UTF-8"?> 
 <Delete> 
 <Quiet>true</Quiet>  
 <Object> 
 <Key>Key1</Key> 
 </Object>  
 <Object>  
 <Key>Key2</Key> 
 </Object>  
 </Delete>  
```

## Sample Response<a name="section14220187"></a>

```
HTTP/1.1 200 OK 
 x-amz-id-2: Weag1LuByRx9e6j5Onimru9pO4ZVKnJ2Qz7/C1NPcfTWAtRPfTaOFg== 
 x-amz-request-id: 996c76696e6727732072657175657374  
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Date: Mon, 1 Nov 2010 20:34:56 GMT 
 Content-Type: application/xml 
 Content-Length: 10485760 
 Server: OBS  

 <?xml version="1.0" encoding="UTF-8"?> 
 <DeleteResult xmlns="http://obs.example.com/doc/2015-06-30/"> 
 <Deleted> 
 <Key>Key1</Key> 
 </Deleted> 
 <Error> 
 <Key>Key2</Key> 
 <Code>InternalError</Code> 
 <Message>Internal Error</Message> 
 </Error> 
 </DeleteResult>
```

## Sample Request \(Deleting an Object with No Version ID Specified form a Bucket with Versioning Enabled\)<a name="section10984535"></a>

```
POST /?delete HTTP/1.1  
 User-Agent: Jakarta Commons-HttpClient/3.1
 Host: bucketname.obs.example.com 
 Accept: */*
 Date: Tue, 14 Jan 2014 12:10:09 +0000 
 Authorization: AWS C9590CEB8EC051BDEC9D:HLq5AmI/Zlz1PPsXdk6pIHuNaCM= 
 Content-MD5: uj2BQLIgDcegTcWHwEGoiA== 
 Content-Length: 64 
 Expect: 100-continue

 <Delete> 
 <Object> 
 <Key>object</Key> 
 </Object> 
 </Delete> 
```

## Sample Response \(Deleting an Object with No Version ID Specified form a Bucket with Versioning Enabled\)<a name="section31751951"></a>

```
HTTP/1.1 200 OK 
 Server: OBS 
 x-amz-request-id: DCD2FC9CAB780000014390A8AA7D4763 
 x-amz-id-2: iFIiPx4egtz5ToRcIIkVZ5Nz8F+zUCis6JKhuQysA4gxLIt+EgPMTMuO08beG7sd 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Content-Type: application/xml 
 Date: Tue, 14 Jan 2014 12:10:09 GMT 
 Content-Length: 280  

 <DeleteResult xmlns="http://obs.example.com/doc/2015-06-30/"> 
 <Deleted> 
 <Key>object</Key> 
 <DeleteMarker>true</DeleteMarker> 
 <DeleteMarkerVersionId>AAABQ5Coqqzc0vycq3gAAAAZVURTRkha</DeleteMarkerVersionId> 
 </Deleted> 
 </DeleteResult>
```

## Sample Request \(Deleting an Object with Version ID Specified from a Bucket\)<a name="section21771268"></a>

```
POST /example?delete HTTP/1.1  
 User-Agent: Jakarta Commons-HttpClient/3.1
 Host: bucketname.obs.example.com 
 Accept: */*
 Date: Tue, 14 Jan 2014 12:19:57 +0000 
 Authorization: AWS C9590CEB8EC051BDEC9D:eTmW0xEkSYrfqOSjZUV7zS+Ap5Y= 
 Content-MD5: YDYt+eVo7S5tnBHaHOylGA== 
 Content-Length: 124 
 Expect: 100-continue

 <Delete> 
 <Object> 
 <Key>object</Key> 
 <VersionId>AAABQ4-glIvc0vycq3gAAAAVVURTRkha</VersionId> 
 </Object> 
 </Delete> 
```

## Sample Response \(Deleting an Object with Version ID Specified from a Bucket\)<a name="section61723690"></a>

```
HTTP/1.1 200 OK 
 Server: OBS 
 x-amz-request-id: DCD2FC9CAB780000014390B1A5974C2C 
 x-amz-id-2: x9Vt2FIjXLjyu38NHeHG+IIYQIQKQjZrEDSHOElJMvEb/SUfY5k54C/uX8GfGUFz 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Content-Type: application/xml 
 Date: Tue, 14 Jan 2014 12:19:58 GMT 
 Content-Length: 223 

 <?xml version="1.0" encoding="UTF-8" standalone="yes"?> 
 <DeleteResult xmlns="http://obs.example.com/doc/2015-06-30/"> 
 <Deleted> 
 <Key>object</Key> 
 <VersionId>AAABQ4-glIvc0vycq3gAAAAVVURTRkha</VersionId> 
 </Deleted> 
 </DeleteResult>
```

## Sample Request \(Deleting a Deletion Mark in a Bucket with Version ID Specified\)<a name="section33563027"></a>

```
POST /example?delete HTTP/1.1 
 User-Agent: Jakarta Commons-HttpClient/3.1
 Host: bucketname.obs.example.com 
 Accept: */*
 Date: Wed, 15 Jan 2014 02:03:40 +0000 
 Authorization: AWS C9590CEB8EC051BDEC9D:N/UdjEab/8H5Llgw1HUpTd21wc4= 
 Content-MD5: n9LlSFB87vGiGDqDKLXPLA== 
 Content-Length: 124 
 Expect: 100-continue

 <Delete> 
 <Object> 
 <Key>object</Key> 
 <VersionId>AAABQ49lNT_c0vycq3gAAAAOVURTRkha</VersionId> 
 </Object> 
 </Delete>
```

## Sample Response \(Deleting a Deletion Mark in a Bucket with Version ID Specified\)<a name="section33631792"></a>

```
HTTP/1.1 200 OK 
 Server: OBS 
 x-amz-request-id: DCD2FC9CAB780000014393A3C5CEDE66 
 x-amz-id-2: N9UP5OvD4BwlQAfyqow6TLWq7HIsG8As4bP/CCNFjcp1Ab8Cc4JAFPm0bjV9WrTg 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Content-Type: application/xml 
 Date: Wed, 15 Jan 2014 02:03:40 GMT 
 Content-Length: 335 

 <?xml version="1.0" encoding="UTF-8" standalone="yes"?> 
 <DeleteResult xmlns="http://obs.example.com/doc/2015-06-30/"> 
 <Deleted> 
 <Key>object</Key> 
 <VersionId>AAABQ49lNT_c0vycq3gAAAAOVURTRkha</VersionId> 
 <DeleteMarker>true</DeleteMarker> 
 <DeleteMarkerVersionId>AAABQ49lNT_c0vycq3gAAAAOVURTRkha</DeleteMarkerVersionId> 
 </Deleted> 
 </DeleteResult>
```

