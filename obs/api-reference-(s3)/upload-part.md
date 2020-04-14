# Upload Part<a name="EN-US_TOPIC_0125560486"></a>

After initiating a multipart upload, you can use this operation to upload parts for the multipart upload using its **uploadId**.

In a multipart upload for a specific object, parts of the object can be uploaded in any sequence and multiple parts can be uploaded concurrently.

Part sizes range from 5 MB to 5 GB. However, in a  **complete multipart** operation, the size of the last uploaded part must range from 0 to 5 GB. In addition, the **uploadId**  of each part must be in the range of 1 to 10000.

This operation makes server-side encryption available.

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>When the same multipart of the same object is uploaded concurrently, the server complies with the Last Write Win policy.  
>The time of Last Write is the creation time of the multipart metadata. To ensure data security, you must add a lock to the client to ensure the upload consistency of the same multipart. There is no need to add a lock when different parts of the same object are uploaded.  

## Request Syntax<a name="section11065523"></a>

```
PUT /ObjectName?partNumber=partNum&uploadId=uploadID  HTTP/1.1 
 User-Agent: agent 
 Host: bucketname.obs.example.com 
 Accept: */*
 Date: date 
 Content-Length: Size  
 Authorization: Signature 
 Content-MD5: md5
 Expect: expect
```

## Request Parameters<a name="section32480848"></a>

This request uses parameters to specify the ID of a multipart upload and part number.  [Table 1](#table6481817)  describes the parameters.

**Table  1**  Request parameters

<a name="table6481817"></a>
<table><thead align="left"><tr id="row40139983"><th class="cellrowborder" valign="top" width="27.532753275327533%" id="mcps1.2.4.1.1"><p id="p30113190"><a name="p30113190"></a><a name="p30113190"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="45.62456245624562%" id="mcps1.2.4.1.2"><p id="p23249317"><a name="p23249317"></a><a name="p23249317"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="26.842684268426847%" id="mcps1.2.4.1.3"><p id="p4146549"><a name="p4146549"></a><a name="p4146549"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row326206"><td class="cellrowborder" valign="top" width="27.532753275327533%" headers="mcps1.2.4.1.1 "><p id="p26422695"><a name="p26422695"></a><a name="p26422695"></a>partNumber</p>
</td>
<td class="cellrowborder" valign="top" width="45.62456245624562%" headers="mcps1.2.4.1.2 "><p id="p59863512"><a name="p59863512"></a><a name="p59863512"></a>Indicates the number that identifies a part to be uploaded. It can be any number from 1 to 10,000</p>
<p id="p1900699"><a name="p1900699"></a><a name="p1900699"></a>Type: Integer</p>
</td>
<td class="cellrowborder" valign="top" width="26.842684268426847%" headers="mcps1.2.4.1.3 "><p id="p19738956"><a name="p19738956"></a><a name="p19738956"></a>Mandatory</p>
</td>
</tr>
<tr id="row43432884"><td class="cellrowborder" valign="top" width="27.532753275327533%" headers="mcps1.2.4.1.1 "><p id="p28402735"><a name="p28402735"></a><a name="p28402735"></a>uploadId</p>
</td>
<td class="cellrowborder" valign="top" width="45.62456245624562%" headers="mcps1.2.4.1.2 "><p id="p18920211"><a name="p18920211"></a><a name="p18920211"></a>Indicates the ID of a multipart upload.</p>
<p id="p36064171"><a name="p36064171"></a><a name="p36064171"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="26.842684268426847%" headers="mcps1.2.4.1.3 "><p id="p35516734"><a name="p35516734"></a><a name="p35516734"></a>Mandatory</p>
</td>
</tr>
</tbody>
</table>

## Request Headers<a name="section23892180"></a>

This request uses common headers. For details about common request headers, see section  [Common Request Headers](common-request-headers.md).

**Table  2**  Request Headers

<a name="table64989796103741"></a>
<table><thead align="left"><tr id="row15560039103741"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p45145935103825"><a name="p45145935103825"></a><a name="p45145935103825"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p32942147103825"><a name="p32942147103825"></a><a name="p32942147103825"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p51068251103825"><a name="p51068251103825"></a><a name="p51068251103825"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row60209390103741"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p851681417555"><a name="p851681417555"></a><a name="p851681417555"></a>x-amz-server-side-encryption-customer-algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1877331917555"><a name="p1877331917555"></a><a name="p1877331917555"></a>Indicates an encryption algorithm. The header is used in SSE-C mode.</p>
<p id="p3474214717555"><a name="p3474214717555"></a><a name="p3474214717555"></a>Type: string</p>
<p id="p4424386917555"><a name="p4424386917555"></a><a name="p4424386917555"></a>Example: x-amz-server-side-encryption-customer-algorithm:AES256</p>
<p id="p6265050217555"><a name="p6265050217555"></a><a name="p6265050217555"></a>Constraints: This header must be used together with <strong id="b2698360717555"><a name="b2698360717555"></a><a name="b2698360717555"></a>x-amz-server-side-encryption-customer-key</strong>&nbsp;and&nbsp;<strong id="b4152587317555"><a name="b4152587317555"></a><a name="b4152587317555"></a>x-amz-server-side-encryption-customer-key-MD5</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p29781360103758"><a name="p29781360103758"></a><a name="p29781360103758"></a><span>No. This header is mandatory when customer-provided keys are used.</span></p>
</td>
</tr>
<tr id="row12202830103741"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p626415317555"><a name="p626415317555"></a><a name="p626415317555"></a>x-amz-server-side-encryption-customer-key</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p3763435217555"><a name="p3763435217555"></a><a name="p3763435217555"></a>Indicates a key used to encrypt objects. The header is used in SSE-C mode.</p>
<p id="p316485417555"><a name="p316485417555"></a><a name="p316485417555"></a>Type: string</p>
<p id="p2848369217555"><a name="p2848369217555"></a><a name="p2848369217555"></a>Example: x-amz-server-side-encryption-customer-key:K7QkYpBkM5+hcs27fsNkUnNVaobncnLht/rCB2o/9Cw=</p>
<p id="p5502664417555"><a name="p5502664417555"></a><a name="p5502664417555"></a>Constraints: This header is a base64-encoded 256-bit or 512-bit key and must be used together with <strong id="b2547774917555"><a name="b2547774917555"></a><a name="b2547774917555"></a>x-amz-server-side-encryption-customer-algorithm</strong>&nbsp;and&nbsp;<strong id="b2797315417555"><a name="b2797315417555"></a><a name="b2797315417555"></a>x-amz-server-side-encryption-customer-key-MD5</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p21180961103758"><a name="p21180961103758"></a><a name="p21180961103758"></a><span>No. This header is mandatory when customer-provided keys are used.</span></p>
</td>
</tr>
<tr id="row37964325103741"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p5844353217555"><a name="p5844353217555"></a><a name="p5844353217555"></a>x-amz-server-side-encryption-customer-key-MD5</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p3630564217555"><a name="p3630564217555"></a><a name="p3630564217555"></a>Indicates the MD5 value of a key used to encrypt objects. The header is used in SSE-C mode. The MD5 value is used to check whether any error occurs during the transmission of the key.</p>
<p id="p5831532617555"><a name="p5831532617555"></a><a name="p5831532617555"></a>Type: string</p>
<p id="p5507589317555"><a name="p5507589317555"></a><a name="p5507589317555"></a>Example: x-amz-server-side-encryption-customer-key-MD5:4XvB3tbNTN+tIEVa0/fGaQ==</p>
<p id="p2592099017555"><a name="p2592099017555"></a><a name="p2592099017555"></a>Constraints: This header is a base64-encoded 128-bit MD5 value and must be used together with <strong id="b3196232417555"><a name="b3196232417555"></a><a name="b3196232417555"></a>x-amz-server-side-encryption-customer-algorithm</strong>&nbsp;and&nbsp;<strong id="b1922546317555"><a name="b1922546317555"></a><a name="b1922546317555"></a>x-amz-server-side-encryption-customer-key</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p9355952103758"><a name="p9355952103758"></a><a name="p9355952103758"></a><span>No. This header is mandatory when customer-provided keys are used.</span></p>
</td>
</tr>
<tr id="row214861134013"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p634621224018"><a name="p634621224018"></a><a name="p634621224018"></a>x-amz-security-token</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p834691215402"><a name="p834691215402"></a><a name="p834691215402"></a>Header field used to identify the request of a federated user. When the federal authentication function is enabled, users sending such requests are identified as federated users.</p>
<p id="p5346512184013"><a name="p5346512184013"></a><a name="p5346512184013"></a>Type: string</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1434621216403"><a name="p1434621216403"></a><a name="p1434621216403"></a>Optional. This parameter must be carried in the request sent by federated users.</p>
</td>
</tr>
</tbody>
</table>

## Request Elements<a name="section13703032"></a>

This request involves no elements.

## Response Syntax<a name="section1842005"></a>

```
HTTP/1.1 status_code 
 x-amz-id-2: id 
 x-amz-request-id: request id 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Date: date 
 ETag: etagValue 
 Content-Length: length 
 Server: server
```

## Response Headers<a name="section16578052"></a>

This response uses common headers. For details about common response headers, see section  [Common Response Headers](common-response-headers.md).

**Table  3**  Response Headers

<a name="table5987923310397"></a>
<table><thead align="left"><tr id="row6148827010397"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p42968163103932"><a name="p42968163103932"></a><a name="p42968163103932"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p57869165103932"><a name="p57869165103932"></a><a name="p57869165103932"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row158288710397"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p3127668017642"><a name="p3127668017642"></a><a name="p3127668017642"></a>x-amz-server-side-encryption</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p5038316017642"><a name="p5038316017642"></a><a name="p5038316017642"></a>This header is included in a response if SSE-KMS is used.</p>
<p id="p5079525817642"><a name="p5079525817642"></a><a name="p5079525817642"></a>Type: string</p>
<p id="p5450414017642"><a name="p5450414017642"></a><a name="p5450414017642"></a>Example: x-amz-server-side-encryption:aws:kms</p>
</td>
</tr>
<tr id="row5241401610397"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p507086917642"><a name="p507086917642"></a><a name="p507086917642"></a>x-amz-server-side-encryption-aws-kms-key-id</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p808725117642"><a name="p808725117642"></a><a name="p808725117642"></a>Indicates the master key ID. This header is included in a response if SSE-KMS is used.</p>
<p id="p567640317642"><a name="p567640317642"></a><a name="p567640317642"></a>Example: x-amz-server-side-encryption-aws-kms-key-id:arn:aws:kms:sichuan:domainiddomainiddomainiddoma0001:key/4f1cd4de-ab64-4807-920a-47fc42e7f0d0</p>
</td>
</tr>
<tr id="row157267910397"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p4445772217642"><a name="p4445772217642"></a><a name="p4445772217642"></a>x-amz-server-side-encryption-customer-algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p4430571417642"><a name="p4430571417642"></a><a name="p4430571417642"></a>Indicates an encryption algorithm. This header is included in a response if SSE-C is used.</p>
<p id="p6320710717642"><a name="p6320710717642"></a><a name="p6320710717642"></a>Type: string</p>
<p id="p3199305817642"><a name="p3199305817642"></a><a name="p3199305817642"></a>Example: x-amz-server-side-encryption-customer-algorithm:AES256</p>
</td>
</tr>
<tr id="row5359392110397"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p3616391917642"><a name="p3616391917642"></a><a name="p3616391917642"></a>x-amz-server-side-encryption-customer-key-MD5</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p4359634017642"><a name="p4359634017642"></a><a name="p4359634017642"></a>Indicates the MD5 value of a key used to encrypt objects. This header is included in a response if SSE-C is used.</p>
<p id="p5682274217642"><a name="p5682274217642"></a><a name="p5682274217642"></a>Type: string</p>
<p id="p4164263717642"><a name="p4164263717642"></a><a name="p4164263717642"></a>Example: x-amz-server-side-encryption-customer-key-MD5:4XvB3tbNTN+tIEVa0/fGaQ==</p>
</td>
</tr>
</tbody>
</table>

## Response Elements<a name="section14984742"></a>

This response involves no elements.

## Error Responses<a name="section644958"></a>

-   If the part number exceeds the range of 1 to 10,000, OBS returns status code  **400 Bad Request**.
-   If the part size is greater than 5 GB, OBS returns status code  **400 Bad Request**.
-   If an AK or signature is invalid, OBS returns status code  **403 Forbidden** and error code **AccessDenied**.
-   If the requested bucket does not exist, OBS returns status code  **404 Not Found** and error code **NoSuchBucket**.
-   If the requester does not have  **READ**  permission for the requested bucket, OBS returns status code **403 Forbidden** and error code **AccessDenied**.
-   If the requested multipart upload does not exist, OBS returns status code  **404 Not Found**  and error code **NoSuchUpload**.
-   If the requester is not the initiator of the multipart upload, OBS returns status code  **403 Forbidden** and error code **AccessDenied**.

For details about other error responses, see  [Table 1](error-codes.md#table30733758).

## Sample Request<a name="section23819137"></a>

```
PUT /ObjectName?partNumber=1&uploadId=VCVsb2FkIElEIGZvciBlbZZpbmcncyBteS1tb3ZpZS5tMnRzIHVwbG9hZR  HTTP/1.1  
 User-Agent: Jakarta Commons-HttpClient/3.1 
 Host: bucketname.obs.example.com
 Accept: */* 
 Date: Mon, 1 Nov 2010 20:34:56 GMT 
 Content-Length: 1048596  
 Authorization:AWS 14RZT432N80TGDF2Y2G2:8se2hm3YLchJhuPMDrybeITcuo0= 
 Content-MD5:q3q7DaS8pTI6thGbtdzSlg==
```

## Sample Response<a name="section13045645"></a>

```
HTTP/1.1 200 OK 
 x-amz-id-2: Vvag1LuByRx9e6j5Onimru9pO4ZVKnJ2Qz7/C1NPcfTWAtRPfTaOFg== 
 x-amz-request-id: 656c76696e6727732072657175657374 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Date: Mon, 1 Nov 2010 20:34:56 GMT 
 ETag: "b54357faf0632cce46e942fa68356b38" 
 Content-Length: 1048596
```

