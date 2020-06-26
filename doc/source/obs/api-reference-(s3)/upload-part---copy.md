# Upload Part - Copy<a name="EN-US_TOPIC_0125560361"></a>

After initiating a multipart upload, you can send an  **Upload Part** request to upload parts for the multipart upload using its **uploadId**. The **Upload Part – Copy**  operation allows you to upload a part by copying data from an existing object as data source.

This operation makes server-side encryption available.

>![](/images/icon-notice.gif) **NOTICE:**   
>You cannot determine whether a request is executed successfully only using  **status\_code**  in the header returned by HTTP.  
>If  **200** in **status\_code**  is returned, the server has received the request and starts to process the request from the upload part. The body in the response shows whether the upload operation succeeds. The upload operation succeeds only when the body has ETags. Otherwise, the upload operation fails.  
>Copy the source object as  **part1**. If part1 already exists before you copy the source object, the old **part1**  will be overwritten by the new **part1**.  
>After the source object is copied, only the latest  **part1**  is listed. The old **part1**  will be deleted. Before using the copy interface, ensure that the target part does not exist or is useless to avoid incorrect data deletion.  
>During the copy process, the source object is not changed.  

## OBS Cold Objects<a name="section3886489515555"></a>

If source objects are OBS cold objects, check the restore status of the objects. You can copy the OBS cold objects only after the objects are restored. If the objects are not restored or are being restored, the copy fails, and error "403 Forbidden" is returned. The fault is described as follows:

ErrorCode: InvalidObjectState

ErrorMessage: Operation is not valid for the source object's storage class

## Request Syntax<a name="section11408737"></a>

```
PUT /ObjectName?partNumber=partNum&uploadId=UploadID HTTP/1.1 
 User-Agent: agent 
 Host: bucketname.obs.example.com 
 Accept: */*
 Date: date 
 x-amz-copy-source: sourceobject 
 x-amz-copy-source-range:bytes=start-end 
 Authorization: auth 
 Content-Length: length
```

## Request Parameters<a name="section35569777"></a>

This request uses parameters to specify the ID of a multipart upload and part number.  [Table 1](#table12334196)  describes the parameters.

**Table  1**  Request parameters

<a name="table12334196"></a>
<table><thead align="left"><tr id="row56919892"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p47108560"><a name="p47108560"></a><a name="p47108560"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p57697049"><a name="p57697049"></a><a name="p57697049"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p42949398"><a name="p42949398"></a><a name="p42949398"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row56349232"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p885070"><a name="p885070"></a><a name="p885070"></a>partNumber</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p4581849"><a name="p4581849"></a><a name="p4581849"></a>Indicates the number that identifies a part to be uploaded.</p>
<p id="p41236642"><a name="p41236642"></a><a name="p41236642"></a>Type: Integer</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p51833723"><a name="p51833723"></a><a name="p51833723"></a>Mandatory</p>
</td>
</tr>
<tr id="row63850324"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p4493716"><a name="p4493716"></a><a name="p4493716"></a>uploadId</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p28446688"><a name="p28446688"></a><a name="p28446688"></a>Indicates the ID of a multipart upload.</p>
<p id="p54693607"><a name="p54693607"></a><a name="p54693607"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p997169"><a name="p997169"></a><a name="p997169"></a>Mandatory</p>
</td>
</tr>
</tbody>
</table>

## Request Headers<a name="section51692544"></a>

This request uses headers listed in  [Table 2](#table6620500)  in addition to common headers.

**Table  2**  Request headers

<a name="table6620500"></a>
<table><thead align="left"><tr id="row64282674"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p39514120"><a name="p39514120"></a><a name="p39514120"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p46527158"><a name="p46527158"></a><a name="p46527158"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p10603493"><a name="p10603493"></a><a name="p10603493"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row53576637"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p44740325"><a name="p44740325"></a><a name="p44740325"></a>x-amz-copy-source</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p87685"><a name="p87685"></a><a name="p87685"></a>Indicates the source object to be copied.</p>
<p id="p789170"><a name="p789170"></a><a name="p789170"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p63922810"><a name="p63922810"></a><a name="p63922810"></a>Mandatory</p>
</td>
</tr>
<tr id="row38434383"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p26177353"><a name="p26177353"></a><a name="p26177353"></a>x-amz-copy-source-range</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p39990876"><a name="p39990876"></a><a name="p39990876"></a>Indicates the range of bytes (start-end) to be copied from the source object. <strong id="b24373566"><a name="b24373566"></a><a name="b24373566"></a>start</strong>&nbsp;indicates the start byte of the part to be copied and&nbsp;<strong id="b18035503"><a name="b18035503"></a><a name="b18035503"></a>end</strong> indicates the end byte.</p>
<p id="p28101800"><a name="p28101800"></a><a name="p28101800"></a>Type: Integer</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p61653310"><a name="p61653310"></a><a name="p61653310"></a>Optional</p>
</td>
</tr>
<tr id="row3775240104116"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p15457196171120"><a name="p15457196171120"></a><a name="p15457196171120"></a>x-amz-server-side-encryption-customer-algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p44073379171120"><a name="p44073379171120"></a><a name="p44073379171120"></a>Indicates an algorithm used to encrypt a destination part. The header is used in SSE-C mode.</p>
<p id="p61116098171120"><a name="p61116098171120"></a><a name="p61116098171120"></a>Type: string</p>
<p id="p13173975171120"><a name="p13173975171120"></a><a name="p13173975171120"></a>Example: x-amz-server-side-encryption-customer-algorithm:AES256</p>
<p id="p51456915171120"><a name="p51456915171120"></a><a name="p51456915171120"></a>Constraints: This header must be used together with <strong id="b60459055171120"><a name="b60459055171120"></a><a name="b60459055171120"></a>x-amz-server-side-encryption-customer-key</strong>&nbsp;and&nbsp;<strong id="b7260588171120"><a name="b7260588171120"></a><a name="b7260588171120"></a>x-amz-server-side-encryption-customer-key-MD5</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p51236790171120"><a name="p51236790171120"></a><a name="p51236790171120"></a>No. This header is mandatory when SSE-C is used. The encryption algorithm must be the same as the algorithm used to initiate multipart upload tasks.</p>
</td>
</tr>
<tr id="row56120066104125"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p39092131171120"><a name="p39092131171120"></a><a name="p39092131171120"></a>x-amz-server-side-encryption-customer-key</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p12346013171120"><a name="p12346013171120"></a><a name="p12346013171120"></a>Indicates a key used to encrypt a destination part. The header is used in SSE-C mode.</p>
<p id="p44005255171120"><a name="p44005255171120"></a><a name="p44005255171120"></a>Type: string</p>
<p id="p60502979171120"><a name="p60502979171120"></a><a name="p60502979171120"></a>Example: x-amz-server-side-encryption-customer-key:K7QkYpBkM5+hcs27fsNkUnNVaobncnLht/rCB2o/9Cw=</p>
<p id="p7655907171120"><a name="p7655907171120"></a><a name="p7655907171120"></a>Constraints: This header is a base64-encoded 256-bit or 512-bit key and must be used together with <strong id="b1794303171120"><a name="b1794303171120"></a><a name="b1794303171120"></a>x-amz-server-side-encryption-customer-algorithm</strong>&nbsp;and&nbsp;<strong id="b16148727171120"><a name="b16148727171120"></a><a name="b16148727171120"></a>x-amz-server-side-encryption-customer-key-MD5</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p32978540171120"><a name="p32978540171120"></a><a name="p32978540171120"></a>No. This header is mandatory when SSE-C is used. The key must be the same as that used to initiate multipart upload tasks.</p>
</td>
</tr>
<tr id="row30895979104122"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p16382907171120"><a name="p16382907171120"></a><a name="p16382907171120"></a>x-amz-server-side-encryption-customer-key-MD5</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p51947096171120"><a name="p51947096171120"></a><a name="p51947096171120"></a>Indicates the MD5 value of a key used to encrypt a destination part. The header is used in SSE-C mode. The MD5 value is used to check whether any error occurs during the transmission of the key.</p>
<p id="p64870686171120"><a name="p64870686171120"></a><a name="p64870686171120"></a>Type: string</p>
<p id="p46965266171120"><a name="p46965266171120"></a><a name="p46965266171120"></a>Example: x-amz-server-side-encryption-customer-key-MD5:4XvB3tbNTN+tIEVa0/fGaQ==</p>
<p id="p20034213171120"><a name="p20034213171120"></a><a name="p20034213171120"></a>Constraints: This header is a base64-encoded 128-bit MD5 value and must be used together with <strong id="b46090192171120"><a name="b46090192171120"></a><a name="b46090192171120"></a>x-amz-server-side-encryption-customer-algorithm</strong>&nbsp;and&nbsp;<strong id="b12158548171120"><a name="b12158548171120"></a><a name="b12158548171120"></a>x-amz-server-side-encryption-customer-key</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p45318356171120"><a name="p45318356171120"></a><a name="p45318356171120"></a>No. This header is mandatory when SSE-C is used. The MD5 value must be the same as that used to initiate multipart upload tasks.</p>
</td>
</tr>
<tr id="row62470581171042"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p19520950171120"><a name="p19520950171120"></a><a name="p19520950171120"></a>x-amz-copy-source-server-side-encryption-customer-algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p37693078171120"><a name="p37693078171120"></a><a name="p37693078171120"></a>Indicates an algorithm used by a source object. The header is used in SSE-C mode.</p>
<p id="p3693383171120"><a name="p3693383171120"></a><a name="p3693383171120"></a>Type: string</p>
<p id="p33240450171120"><a name="p33240450171120"></a><a name="p33240450171120"></a>Example: x-amz-copy-source-server-side-encryption-customer-algorithm:AES256</p>
<p id="p30728601171120"><a name="p30728601171120"></a><a name="p30728601171120"></a>Constraints: This header must be used together with <strong id="b368315326171"><a name="b368315326171"></a><a name="b368315326171"></a>x-amz-copy-source-server-side-encryption-customer-key</strong> and&nbsp;<strong id="b5988739171120"><a name="b5988739171120"></a><a name="b5988739171120"></a>x-amz-copy-source-server-side-encryption-customer-key-MD5</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p15325870171120"><a name="p15325870171120"></a><a name="p15325870171120"></a>No. This header is mandatory when SSE-C is used to copy a source object.</p>
</td>
</tr>
<tr id="row58030305171045"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p28508285171211"><a name="p28508285171211"></a><a name="p28508285171211"></a><span>x-amz-copy-source-server-side-encryption-customer-key</span></p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p27469759171211"><a name="p27469759171211"></a><a name="p27469759171211"></a><span>Indicates the customer-provided key used to decrypt the source object when customer-provided keys are used.</span></p>
<p id="p45901246171211"><a name="p45901246171211"></a><a name="p45901246171211"></a><span>Type: string</span></p>
<p id="p10458030171211"><a name="p10458030171211"></a><a name="p10458030171211"></a>Example: x-amz-copy-source-server-side-encryption-customer-key:K7QkYpBkM5+hcs27fsNkUnNVaobncnLht/rCB2o/9Cw=</p>
<p id="p29878705171211"><a name="p29878705171211"></a><a name="p29878705171211"></a><span>Constraints: This header is a base64-encoded 256-bit or 512-bit key and must be used together with </span><strong id="b61144017170"><a name="b61144017170"></a><a name="b61144017170"></a>x-amz-copy-source-server-side-encryption-customer-algorithm</strong><span> and </span><strong id="b4256021171211"><a name="b4256021171211"></a><a name="b4256021171211"></a><span>x-amz-copy-source-server-side-encryption-customer-key-MD5</span></strong><span>.</span></p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p10665747183114"><a name="p10665747183114"></a><a name="p10665747183114"></a>No.</p>
<p id="p15631862171211"><a name="p15631862171211"></a><a name="p15631862171211"></a><span>This header is mandatory when customer-provided keys are used to copy source objects.</span></p>
</td>
</tr>
<tr id="row65640039171048"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p54229804171211"><a name="p54229804171211"></a><a name="p54229804171211"></a><span>x-amz-copy-source-server-side-encryption-customer-key-MD5</span></p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p30538035171211"><a name="p30538035171211"></a><a name="p30538035171211"></a><span>Indicates the MD5 value of the customer-provided key used to decrypt the source object when customer-provided keys are used.</span></p>
<p id="p6406859171211"><a name="p6406859171211"></a><a name="p6406859171211"></a><span>Type: string</span></p>
<p id="p57661733171211"><a name="p57661733171211"></a><a name="p57661733171211"></a><span>Example: x-amz-copy-source-server-side-encryption-customer-key-MD5:4XvB3tbNTN+tIEVa0/fGaQ==</span></p>
<p id="p49193555171211"><a name="p49193555171211"></a><a name="p49193555171211"></a><span>Constraints: This header is a 128-bit base64-encoded string and must be used together with </span><strong id="b1097174871711"><a name="b1097174871711"></a><a name="b1097174871711"></a>x-amz-copy-source-server-side-encryption-customer-algorithm</strong><span> and </span><strong id="b25254995171211"><a name="b25254995171211"></a><a name="b25254995171211"></a><span>x-amz-copy-source-server-side-encryption-customer-key</span></strong><span>.</span></p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p196246112322"><a name="p196246112322"></a><a name="p196246112322"></a>No.</p>
<p id="p23063064171211"><a name="p23063064171211"></a><a name="p23063064171211"></a><span>This header is mandatory when customer-provided keys are used to copy source objects.</span></p>
</td>
</tr>
<tr id="row78811024164014"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p12787226114018"><a name="p12787226114018"></a><a name="p12787226114018"></a>x-amz-security-token</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p77873262402"><a name="p77873262402"></a><a name="p77873262402"></a>Header field used to identify the request of a federated user. When the federal authentication function is enabled, users sending such requests are identified as federated users.</p>
<p id="p1078718261401"><a name="p1078718261401"></a><a name="p1078718261401"></a>Type: string</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p278712265406"><a name="p278712265406"></a><a name="p278712265406"></a>Optional. This parameter must be carried in the request sent by federated users.</p>
</td>
</tr>
</tbody>
</table>

## Request Elements<a name="section62579720"></a>

This request involves no elements.

## Response Syntax<a name="section41575528"></a>

```
HTTP/1.1 status_code 
 x-amz-id-2: id 
 x-amz-request-id: request id 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Content-Type: type 
 Date: date 
 Server: server 
 Transfer-Encoding: chunked

 <?xml version="1.0" encoding="UTF-8" standalone="yes"?> 
 <CopyPartResult xmlns="http://obs.example.com/doc/2015-06-30/"> 
 <LastModified>modifiedDate</LastModified>  
 <ETag>etagValue</ETag>  
 </CopyPartResult> 
```

## Response Headers<a name="section38635439"></a>

This response uses common headers. For details about common response headers, see section  [Common Response Headers](common-response-headers.md).

**Table  3**  Response Headers

<a name="table37553038104158"></a>
<table><thead align="left"><tr id="row55004863104158"><th class="cellrowborder" valign="top" width="39.629999999999995%" id="mcps1.2.3.1.1"><p id="p7661080104233"><a name="p7661080104233"></a><a name="p7661080104233"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="60.370000000000005%" id="mcps1.2.3.1.2"><p id="p16567776104233"><a name="p16567776104233"></a><a name="p16567776104233"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row23588107104158"><td class="cellrowborder" valign="top" width="39.629999999999995%" headers="mcps1.2.3.1.1 "><p id="p99682917136"><a name="p99682917136"></a><a name="p99682917136"></a>x-amz-server-side-encryption</p>
</td>
<td class="cellrowborder" valign="top" width="60.370000000000005%" headers="mcps1.2.3.1.2 "><p id="p1363432817136"><a name="p1363432817136"></a><a name="p1363432817136"></a>This header is included in a response if SSE-KMS is used.</p>
<p id="p5560008917136"><a name="p5560008917136"></a><a name="p5560008917136"></a>Type: string</p>
<p id="p93561753183319"><a name="p93561753183319"></a><a name="p93561753183319"></a>Example: x-amz-server-side-encryption:aws:kms</p>
</td>
</tr>
<tr id="row9705093104158"><td class="cellrowborder" valign="top" width="39.629999999999995%" headers="mcps1.2.3.1.1 "><p id="p5551271517136"><a name="p5551271517136"></a><a name="p5551271517136"></a>x-amz-server-side-encryption-aws-kms-key-id</p>
</td>
<td class="cellrowborder" valign="top" width="60.370000000000005%" headers="mcps1.2.3.1.2 "><p id="p23602817136"><a name="p23602817136"></a><a name="p23602817136"></a>Indicates the master key ID. This header is included in a response if SSE-KMS is used.</p>
<p id="p74823673418"><a name="p74823673418"></a><a name="p74823673418"></a>Example: x-amz-server-side-encryption-aws-kms-key-id:arn:aws:kms:sichuan:domainiddomainiddomainiddoma0001:key/4f1cd4de-ab64-4807-920a-47fc42e7f0d0</p>
</td>
</tr>
<tr id="row33446976104158"><td class="cellrowborder" valign="top" width="39.629999999999995%" headers="mcps1.2.3.1.1 "><p id="p507861617136"><a name="p507861617136"></a><a name="p507861617136"></a>x-amz-server-side-encryption-customer-algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="60.370000000000005%" headers="mcps1.2.3.1.2 "><p id="p871477117136"><a name="p871477117136"></a><a name="p871477117136"></a>Indicates an encryption algorithm. This header is included in a response if SSE-C is used.</p>
<p id="p1132408017136"><a name="p1132408017136"></a><a name="p1132408017136"></a>Type: string</p>
<p id="p75301113103410"><a name="p75301113103410"></a><a name="p75301113103410"></a>Example: x-amz-server-side-encryption-customer-algorithm:AES256</p>
</td>
</tr>
<tr id="row63746658104158"><td class="cellrowborder" valign="top" width="39.629999999999995%" headers="mcps1.2.3.1.1 "><p id="p778157017136"><a name="p778157017136"></a><a name="p778157017136"></a>x-amz-server-side-encryption-customer-key-MD5</p>
</td>
<td class="cellrowborder" valign="top" width="60.370000000000005%" headers="mcps1.2.3.1.2 "><p id="p2632744217136"><a name="p2632744217136"></a><a name="p2632744217136"></a>Indicates the MD5 value of a key used to encrypt objects. This header is included in a response if SSE-C is used.</p>
<p id="p3562038817136"><a name="p3562038817136"></a><a name="p3562038817136"></a>Type: string</p>
<p id="p642020167342"><a name="p642020167342"></a><a name="p642020167342"></a>Example: x-amz-server-side-encryption-customer-key-MD5:4XvB3tbNTN+tIEVa0/fGaQ==</p>
</td>
</tr>
</tbody>
</table>

## Response Elements<a name="section12174636"></a>

This response contains elements to indicate the copy results.  [Table 4](#table44628158)  describes the elements.

**Table  4**  Response elements

<a name="table44628158"></a>
<table><thead align="left"><tr id="row48346426"><th class="cellrowborder" valign="top" width="39.72%" id="mcps1.2.3.1.1"><p id="p23746403"><a name="p23746403"></a><a name="p23746403"></a>Element</p>
</th>
<th class="cellrowborder" valign="top" width="60.28%" id="mcps1.2.3.1.2"><p id="p44410452"><a name="p44410452"></a><a name="p44410452"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row40476854"><td class="cellrowborder" valign="top" width="39.72%" headers="mcps1.2.3.1.1 "><p id="p57399728"><a name="p57399728"></a><a name="p57399728"></a>LastModified</p>
</td>
<td class="cellrowborder" valign="top" width="60.28%" headers="mcps1.2.3.1.2 "><p id="p18866411"><a name="p18866411"></a><a name="p18866411"></a>Indicates the date the part was last modified.</p>
<p id="p35579976"><a name="p35579976"></a><a name="p35579976"></a>Type: String</p>
</td>
</tr>
<tr id="row51784335"><td class="cellrowborder" valign="top" width="39.72%" headers="mcps1.2.3.1.1 "><p id="p33781570"><a name="p33781570"></a><a name="p33781570"></a>ETag</p>
</td>
<td class="cellrowborder" valign="top" width="60.28%" headers="mcps1.2.3.1.2 "><p id="p51952687"><a name="p51952687"></a><a name="p51952687"></a>Indicates the ETag of the source part.</p>
<p id="p64921002"><a name="p64921002"></a><a name="p64921002"></a>Type: String</p>
</td>
</tr>
</tbody>
</table>

## Error Responses<a name="section42462864"></a>

-   If an AccessKey or signature is invalid, OBS returns status code  **403 Forbidden** and error code **AccessDenied**.
-   If the requested bucket does not exist, OBS returns status code  **404 Not Found** and error code **NoSuchBucket**.
-   If the requested source object does not exist, OBS returns status code  **404 Not Found** and error code **NoSuchKey**.
-   If the requester does not have  **READ** permission for the requested bucket, OBS returns status code **403 Forbidden** and error code **AccessDenied**.
-   If the requester does not have  **WRITE** permission for the requested bucket, OBS returns status code **403 Forbidden** and error code **AccessDenied**.
-   If the requested multipart upload does not exist, OBS returns status code  **404 Not Found** and error code **NoSuchUpload**.
-   If the requester is not the initiator of the multipart upload, OBS returns status code  **403 Forbidden** and error code **AccessDenied**.
-   If the part size is greater than 5 GB, OBS returns status code  **400 Bad Request**.
-   If the part number exceeds the range of 1 to 10,000, OBS returns status code  **400 Bad Request**.

For details about other error responses, see  [Table 1](error-codes.md#table30733758).

## Sample Request<a name="section6063624"></a>

```
PUT /newobject?partNumber=1&uploadId=VCVsb2FkIElEIGZvciBlbZZpbmcncyBteS1tb3ZpZS5tMnRzIHVwbG9hZR HTTP/1.1 
 User-Agent: Jakarta Commons-HttpClient/3.1
 Host: bucketname.obs.example.com
 Accept: */* 
 Date: Mon, 11 Apr 2011 20:34:56 GMT 
 x-amz-copy-source: /source-bucket/sourceobject 
 x-amz-copy-source-range:bytes=500-6291456 
 Authorization: AWS AKIAIOSFODNN7EXAMPLE:VGhpcyBtZXNzYWdlIHNpZ25lZGGieSRlbHZpbmc= 
 Content-Length: 5120
```

## Sample Response<a name="section54572624"></a>

```
HTTP/1.1 200 OK 
 Server: OBS
 x-amz-id-2: Vvag1LuByRx9e6j5Onimru9pO4ZVKnJ2Qz7/C1NPcfTWAtRPfTaOFg== 
 x-amz-request-id: 656c76696e6727732072657175657374 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Content-Type: application/xml
 Date: Mon, 11 Apr 2011 20:34:56 GMT   
 Transfer-Encoding: chunked

 <?xml version="1.0" encoding="UTF-8" standalone="yes"?> 
 <CopyPartResult xmlns="http://obs.example.com/doc/2015-06-30/"> 
 <LastModified>2009-10-28T22:32:00</LastModified> <ETag>"9b2cf535f27731c974343645a3985328"</ETag>  
 </CopyPartResult> 
```

