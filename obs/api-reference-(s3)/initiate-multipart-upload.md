# Initiate Multipart Upload<a name="EN-US_TOPIC_0125560339"></a>

You can use this operation to obtain a globally unique upload ID.

This upload ID is used to associate all parts in the specific multipart upload. You can specify this upload ID in each of your subsequent requests such as  **Upload Part**, **Complete Multipart Upload**, and **List Parts**.

The key of the object for which a multipart upload is intended can be the same as an existing object. You can initiate one or more multipart uploads for one object.

An **Initiate Multipart Upload** request can contain multiple headers such as **x-amz-acl**, **x-amz-meta-\***, **Content-Type**, and **Content-Encoding**. The headers are recorded in the metadata of parts uploaded for the specific multipart upload.

This operation makes server-side encryption available.

## Request Syntax<a name="section55982574"></a>

```
POST /ObjectName?uploads  HTTP/1.1  
 User-Agent: agent
 Host: bucketname.obs.example.com
 Accept: */*  
 Date: date  
 Authorization: signatureValue  
```

## Request Parameters<a name="section34081122"></a>

This request uses a parameter to specify a multipart upload.  [Table 1](#table13291134)  describes the parameters.

**Table  1**  Request parameter

<a name="table13291134"></a>
<table><thead align="left"><tr id="row3756927"><th class="cellrowborder" valign="top" width="25.662566256625663%" id="mcps1.2.4.1.1"><p id="p35875689"><a name="p35875689"></a><a name="p35875689"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="45.62456245624562%" id="mcps1.2.4.1.2"><p id="p20249687"><a name="p20249687"></a><a name="p20249687"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="28.712871287128717%" id="mcps1.2.4.1.3"><p id="p29611954"><a name="p29611954"></a><a name="p29611954"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row49758049"><td class="cellrowborder" valign="top" width="25.662566256625663%" headers="mcps1.2.4.1.1 "><p id="p3870157"><a name="p3870157"></a><a name="p3870157"></a>uploads</p>
</td>
<td class="cellrowborder" valign="top" width="45.62456245624562%" headers="mcps1.2.4.1.2 "><p id="p45047261"><a name="p45047261"></a><a name="p45047261"></a>Indicates the ID of the multipart upload to be initiated.</p>
<p id="p2772166"><a name="p2772166"></a><a name="p2772166"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="28.712871287128717%" headers="mcps1.2.4.1.3 "><p id="p23218888"><a name="p23218888"></a><a name="p23218888"></a>Mandatory</p>
</td>
</tr>
</tbody>
</table>

## Request Headers<a name="section38294646"></a>

This request uses common headers. For details about common request headers, see section  [Common Request Headers](common-request-headers.md).

This request also uses one optional header, as described in  [Table 2](#table46028401).

**Table  2**  Request headers

<a name="table46028401"></a>
<table><thead align="left"><tr id="row33955681"><th class="cellrowborder" valign="top" width="26.652665266526654%" id="mcps1.2.4.1.1"><p id="p66055606"><a name="p66055606"></a><a name="p66055606"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="44.44444444444445%" id="mcps1.2.4.1.2"><p id="p48903847"><a name="p48903847"></a><a name="p48903847"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="28.9028902890289%" id="mcps1.2.4.1.3"><p id="p1788702"><a name="p1788702"></a><a name="p1788702"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row181128589338"><td class="cellrowborder" valign="top" width="26.652665266526654%" headers="mcps1.2.4.1.1 "><p id="p163061637105"><a name="p163061637105"></a><a name="p163061637105"></a>x-amz-storage-class</p>
</td>
<td class="cellrowborder" valign="top" width="44.44444444444445%" headers="mcps1.2.4.1.2 "><p id="p7305518157"><a name="p7305518157"></a><a name="p7305518157"></a>When creating an object, you can add this header in the request to set the storage class of the object. If you do not add this header, the object will use the default storage class of the bucket.</p>
<p id="p183055181656"><a name="p183055181656"></a><a name="p183055181656"></a>Type: String</p>
<p id="p83054181511"><a name="p83054181511"></a><a name="p83054181511"></a>Note: The storage class can be <strong id="b4305121814519"><a name="b4305121814519"></a><a name="b4305121814519"></a>STANDARD</strong>&nbsp;(OBS Standard),&nbsp;<strong id="b1830516181052"><a name="b1830516181052"></a><a name="b1830516181052"></a>STANDARD_IA</strong>&nbsp;(OBS Warm), or&nbsp;<strong id="b43051018859"><a name="b43051018859"></a><a name="b43051018859"></a>GLACIER</strong> (OBS Cold). Note that the three storage class values are case-sensitive.</p>
<p id="p63051018859"><a name="p63051018859"></a><a name="p63051018859"></a>Example: x-amz-storage-class: STANDARD</p>
</td>
<td class="cellrowborder" valign="top" width="28.9028902890289%" headers="mcps1.2.4.1.3 "><p id="p1157872174110"><a name="p1157872174110"></a><a name="p1157872174110"></a>Optional</p>
</td>
</tr>
<tr id="row10667136"><td class="cellrowborder" valign="top" width="26.652665266526654%" headers="mcps1.2.4.1.1 "><p id="p58731703"><a name="p58731703"></a><a name="p58731703"></a>x-amz-website-redirect-location</p>
</td>
<td class="cellrowborder" valign="top" width="44.44444444444445%" headers="mcps1.2.4.1.2 "><p id="p59647531"><a name="p59647531"></a><a name="p59647531"></a>If a bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL. OBS stores the value of this header in the object metadata.</p>
<p id="p67065735"><a name="p67065735"></a><a name="p67065735"></a>Type: String</p>
<p id="p66720707"><a name="p66720707"></a><a name="p66720707"></a>Default: None</p>
<p id="p63615456"><a name="p63615456"></a><a name="p63615456"></a>Constraint: The value must be prefixed by a slash (/), <strong id="b35668200"><a name="b35668200"></a><a name="b35668200"></a>http://</strong>, or <strong id="b1977818131160"><a name="b1977818131160"></a><a name="b1977818131160"></a>https://</strong>. The length of the value cannot exceed 2 K.</p>
</td>
<td class="cellrowborder" valign="top" width="28.9028902890289%" headers="mcps1.2.4.1.3 "><p id="p30987661"><a name="p30987661"></a><a name="p30987661"></a>Optional</p>
</td>
</tr>
<tr id="row2007564010347"><td class="cellrowborder" valign="top" width="26.652665266526654%" headers="mcps1.2.4.1.1 "><p id="p421387661741"><a name="p421387661741"></a><a name="p421387661741"></a>x-amz-server-side-encryption</p>
</td>
<td class="cellrowborder" valign="top" width="44.44444444444445%" headers="mcps1.2.4.1.2 "><p id="p577968631741"><a name="p577968631741"></a><a name="p577968631741"></a>Indicates that SSE-KMS is used.</p>
<p id="p504097261741"><a name="p504097261741"></a><a name="p504097261741"></a>Type: string</p>
<p id="p510343581741"><a name="p510343581741"></a><a name="p510343581741"></a>Example: x-amz-server-side-encryption:aws:kms</p>
</td>
<td class="cellrowborder" valign="top" width="28.9028902890289%" headers="mcps1.2.4.1.3 "><p id="p401422961741"><a name="p401422961741"></a><a name="p401422961741"></a>No. This header is mandatory when SSE-KMS is used.</p>
</td>
</tr>
<tr id="row10741677103426"><td class="cellrowborder" valign="top" width="26.652665266526654%" headers="mcps1.2.4.1.1 "><p id="p42695821741"><a name="p42695821741"></a><a name="p42695821741"></a>x-amz-server-side-encryption-aws-kms-key-id</p>
</td>
<td class="cellrowborder" valign="top" width="44.44444444444445%" headers="mcps1.2.4.1.2 "><p id="p102918711741"><a name="p102918711741"></a><a name="p102918711741"></a>Indicates the master key ID. This header is used in SSE-KMS mode. If the customer does not provide the master key, the default master key will be used.</p>
<p id="p255179791741"><a name="p255179791741"></a><a name="p255179791741"></a>Type: string</p>
<p id="p283352241741"><a name="p283352241741"></a><a name="p283352241741"></a>Example: x-amz-server-side-encryption-aws-kms-key-id:arn:aws:kms:sichuan:domainiddomainiddomainiddoma0001:key/4f1cd4de-ab64-4807-920a-47fc42e7f0d0</p>
</td>
<td class="cellrowborder" valign="top" width="28.9028902890289%" headers="mcps1.2.4.1.3 "><p id="p134518421741"><a name="p134518421741"></a><a name="p134518421741"></a>No</p>
</td>
</tr>
<tr id="row21510552103418"><td class="cellrowborder" valign="top" width="26.652665266526654%" headers="mcps1.2.4.1.1 "><p id="p146481841741"><a name="p146481841741"></a><a name="p146481841741"></a>x-amz-server-side-encryption-customer-algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="44.44444444444445%" headers="mcps1.2.4.1.2 "><p id="p456522781741"><a name="p456522781741"></a><a name="p456522781741"></a>Indicates an encryption algorithm. The header is used in SSE-C mode.</p>
<p id="p82173191741"><a name="p82173191741"></a><a name="p82173191741"></a>Type: string</p>
<p id="p68470121741"><a name="p68470121741"></a><a name="p68470121741"></a>Example: x-amz-server-side-encryption-customer-algorithm:AES256</p>
<p id="p616231081741"><a name="p616231081741"></a><a name="p616231081741"></a>Constraints: This header must be used together with <strong id="b177370661741"><a name="b177370661741"></a><a name="b177370661741"></a>x-amz-server-side-encryption-customer-key</strong>&nbsp;and&nbsp;<strong id="b254158701741"><a name="b254158701741"></a><a name="b254158701741"></a>x-amz-server-side-encryption-customer-key-MD5</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="28.9028902890289%" headers="mcps1.2.4.1.3 "><p id="p454195801741"><a name="p454195801741"></a><a name="p454195801741"></a>No. This header is mandatory when SSE-C is used.</p>
</td>
</tr>
<tr id="row28371036103415"><td class="cellrowborder" valign="top" width="26.652665266526654%" headers="mcps1.2.4.1.1 "><p id="p262042561741"><a name="p262042561741"></a><a name="p262042561741"></a>x-amz-server-side-encryption-customer-key</p>
</td>
<td class="cellrowborder" valign="top" width="44.44444444444445%" headers="mcps1.2.4.1.2 "><p id="p421700091741"><a name="p421700091741"></a><a name="p421700091741"></a>Indicates a key used to encrypt objects. The header is used in SSE-C mode.</p>
<p id="p439857621741"><a name="p439857621741"></a><a name="p439857621741"></a>Type: string</p>
<p id="p603275381741"><a name="p603275381741"></a><a name="p603275381741"></a>Example: x-amz-server-side-encryption-customer-key:K7QkYpBkM5+hcs27fsNkUnNVaobncnLht/rCB2o/9Cw=</p>
<p id="p60769301741"><a name="p60769301741"></a><a name="p60769301741"></a>Constraints: This header is a base64-encoded 256-bit or 512-bit key and must be used together with <strong id="b546923711741"><a name="b546923711741"></a><a name="b546923711741"></a>x-amz-server-side-encryption-customer-algorithm</strong>&nbsp;and&nbsp;<strong id="b224692941741"><a name="b224692941741"></a><a name="b224692941741"></a>x-amz-server-side-encryption-customer-key-MD5</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="28.9028902890289%" headers="mcps1.2.4.1.3 "><p id="p80735511741"><a name="p80735511741"></a><a name="p80735511741"></a>No. This header is mandatory when SSE-C is used.</p>
</td>
</tr>
<tr id="row66494507103411"><td class="cellrowborder" valign="top" width="26.652665266526654%" headers="mcps1.2.4.1.1 "><p id="p471482181741"><a name="p471482181741"></a><a name="p471482181741"></a>x-amz-server-side-encryption-customer-key-MD5</p>
</td>
<td class="cellrowborder" valign="top" width="44.44444444444445%" headers="mcps1.2.4.1.2 "><p id="p609093261741"><a name="p609093261741"></a><a name="p609093261741"></a>Indicates the MD5 value of a key used to encrypt objects. The header is used in SSE-C mode. The MD5 value is used to check whether any error occurs during the transmission of the key.</p>
<p id="p113130221741"><a name="p113130221741"></a><a name="p113130221741"></a>Type: string</p>
<p id="p347083371741"><a name="p347083371741"></a><a name="p347083371741"></a>Example: x-amz-server-side-encryption-customer-key-MD5:4XvB3tbNTN+tIEVa0/fGaQ==</p>
<p id="p439395851741"><a name="p439395851741"></a><a name="p439395851741"></a>Constraints: This header is a base64-encoded 128-bit MD5 value and must be used together with <strong id="b599119501741"><a name="b599119501741"></a><a name="b599119501741"></a>x-amz-server-side-encryption-customer-algorithm</strong>&nbsp;and&nbsp;<strong id="b23366411741"><a name="b23366411741"></a><a name="b23366411741"></a>x-amz-server-side-encryption-customer-key</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="28.9028902890289%" headers="mcps1.2.4.1.3 "><p id="p550502131741"><a name="p550502131741"></a><a name="p550502131741"></a>No. This header is mandatory when SSE-C is used.</p>
</td>
</tr>
<tr id="row123906544396"><td class="cellrowborder" valign="top" width="26.652665266526654%" headers="mcps1.2.4.1.1 "><p id="p257218553398"><a name="p257218553398"></a><a name="p257218553398"></a>x-amz-security-token</p>
</td>
<td class="cellrowborder" valign="top" width="44.44444444444445%" headers="mcps1.2.4.1.2 "><p id="p1457265563919"><a name="p1457265563919"></a><a name="p1457265563919"></a>Header field used to identify the request of a federated user. When the federal authentication function is enabled, users sending such requests are identified as federated users.</p>
<p id="p1757218551392"><a name="p1757218551392"></a><a name="p1757218551392"></a>Type: string</p>
</td>
<td class="cellrowborder" valign="top" width="28.9028902890289%" headers="mcps1.2.4.1.3 "><p id="p157275523911"><a name="p157275523911"></a><a name="p157275523911"></a>Optional. This parameter must be carried in the request sent by federated users.</p>
</td>
</tr>
</tbody>
</table>

For details about common request headers, see section  [Common Request Headers](common-request-headers.md).

## Request Elements<a name="section9107499"></a>

This request involves no elements.

## Response Syntax<a name="section6423738"></a>

```
HTTP/1.1 status_code 
 Server: server 
 x-amz-id-2: id 
 x-amz-request-id: request id 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Content-Type: type    
 Content-Length: length 
 Date: date  

 <?xml version="1.0" encoding="UTF-8" standalone="yes"?> 
 <InitiateMultipartUploadResult xmlns="http://obs.example.com/doc/2015-06-30/"> 
 <Bucket>BucketName</Bucket>  
 <Key>ObjectName</Key>  
 <UploadId>uploadID</UploadId> 
 </InitiateMultipartUploadResult> 
```

## Response Headers<a name="section57813648"></a>

This response uses common headers. For details about common response headers, see section  [Common Response Headers](common-response-headers.md).

**Table  3**  Response Headers

<a name="table13282587103527"></a>
<table><thead align="left"><tr id="row65459064103527"><th class="cellrowborder" valign="top" width="44.440000000000005%" id="mcps1.2.3.1.1"><p id="p42924963103629"><a name="p42924963103629"></a><a name="p42924963103629"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="55.559999999999995%" id="mcps1.2.3.1.2"><p id="p54369994103629"><a name="p54369994103629"></a><a name="p54369994103629"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row6462231103527"><td class="cellrowborder" valign="top" width="44.440000000000005%" headers="mcps1.2.3.1.1 "><p id="p1450872317433"><a name="p1450872317433"></a><a name="p1450872317433"></a>x-amz-server-side-encryption</p>
</td>
<td class="cellrowborder" valign="top" width="55.559999999999995%" headers="mcps1.2.3.1.2 "><p id="p3435594617433"><a name="p3435594617433"></a><a name="p3435594617433"></a>This header is included in a response if SSE-KMS is used.</p>
<p id="p4076805817433"><a name="p4076805817433"></a><a name="p4076805817433"></a>Type: string</p>
<p id="p3136820417433"><a name="p3136820417433"></a><a name="p3136820417433"></a>Example: x-amz-server-side-encryption:aws:kms</p>
</td>
</tr>
<tr id="row7303564103527"><td class="cellrowborder" valign="top" width="44.440000000000005%" headers="mcps1.2.3.1.1 "><p id="p5040745817433"><a name="p5040745817433"></a><a name="p5040745817433"></a>x-amz-server-side-encryption-aws-kms-key-id</p>
</td>
<td class="cellrowborder" valign="top" width="55.559999999999995%" headers="mcps1.2.3.1.2 "><p id="p5647230717433"><a name="p5647230717433"></a><a name="p5647230717433"></a>Indicates the master key ID. This header is included in a response if SSE-KMS is used.</p>
<p id="p3848871917433"><a name="p3848871917433"></a><a name="p3848871917433"></a>Example: x-amz-server-side-encryption-aws-kms-key-id:arn:aws:kms:sichuan:domainiddomainiddomainiddoma0001:key/4f1cd4de-ab64-4807-920a-47fc42e7f0d0</p>
</td>
</tr>
<tr id="row26606372103527"><td class="cellrowborder" valign="top" width="44.440000000000005%" headers="mcps1.2.3.1.1 "><p id="p677147817433"><a name="p677147817433"></a><a name="p677147817433"></a>x-amz-server-side-encryption-customer-algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="55.559999999999995%" headers="mcps1.2.3.1.2 "><p id="p1161887317433"><a name="p1161887317433"></a><a name="p1161887317433"></a>Indicates an encryption algorithm. This header is included in a response if SSE-C is used.</p>
<p id="p3746099517433"><a name="p3746099517433"></a><a name="p3746099517433"></a>Type: string</p>
<p id="p160463617433"><a name="p160463617433"></a><a name="p160463617433"></a>Example: x-amz-server-side-encryption-customer-algorithm:AES256</p>
</td>
</tr>
<tr id="row61167020103527"><td class="cellrowborder" valign="top" width="44.440000000000005%" headers="mcps1.2.3.1.1 "><p id="p2892905917433"><a name="p2892905917433"></a><a name="p2892905917433"></a>x-amz-server-side-encryption-customer-key-MD5</p>
</td>
<td class="cellrowborder" valign="top" width="55.559999999999995%" headers="mcps1.2.3.1.2 "><p id="p6155247917433"><a name="p6155247917433"></a><a name="p6155247917433"></a>Indicates the MD5 value of a key used to encrypt objects. This header is included in a response if SSE-C is used.</p>
<p id="p1710139917433"><a name="p1710139917433"></a><a name="p1710139917433"></a>Type: string</p>
<p id="p1969487017433"><a name="p1969487017433"></a><a name="p1969487017433"></a>Example: x-amz-server-side-encryption-customer-key-MD5:4XvB3tbNTN+tIEVa0/fGaQ==</p>
</td>
</tr>
</tbody>
</table>

## Response Elements<a name="section50560785"></a>

This response contains elements to indicate the upload ID and the key \(name\) of the object \(bucket\) for which the multipart upload was initiated. The returned information is used in the subsequent  **Upload Part**  and **Complete Multipart Upload** operations. [Table 4](#table6651816)  describes the elements.

**Table  4**  Response elements

<a name="table6651816"></a>
<table><thead align="left"><tr id="row10894532"><th class="cellrowborder" valign="top" width="45.129999999999995%" id="mcps1.2.3.1.1"><p id="p10041872"><a name="p10041872"></a><a name="p10041872"></a>Element</p>
</th>
<th class="cellrowborder" valign="top" width="54.87%" id="mcps1.2.3.1.2"><p id="p8085329"><a name="p8085329"></a><a name="p8085329"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row50931951"><td class="cellrowborder" valign="top" width="45.129999999999995%" headers="mcps1.2.3.1.1 "><p id="p31847377"><a name="p31847377"></a><a name="p31847377"></a>InitiateMultipartUploadResult</p>
</td>
<td class="cellrowborder" valign="top" width="54.87%" headers="mcps1.2.3.1.2 "><p id="p29500768"><a name="p29500768"></a><a name="p29500768"></a>Indicates the container for the response.</p>
<p id="p64180323"><a name="p64180323"></a><a name="p64180323"></a>Type: XML</p>
</td>
</tr>
<tr id="row40752003"><td class="cellrowborder" valign="top" width="45.129999999999995%" headers="mcps1.2.3.1.1 "><p id="p12577955"><a name="p12577955"></a><a name="p12577955"></a>Bucket</p>
</td>
<td class="cellrowborder" valign="top" width="54.87%" headers="mcps1.2.3.1.2 "><p id="p12181415"><a name="p12181415"></a><a name="p12181415"></a>Indicates the name of the bucket for which the multipart upload was initiated.</p>
<p id="p42523874"><a name="p42523874"></a><a name="p42523874"></a>Type: String</p>
</td>
</tr>
<tr id="row47170552"><td class="cellrowborder" valign="top" width="45.129999999999995%" headers="mcps1.2.3.1.1 "><p id="p62718333"><a name="p62718333"></a><a name="p62718333"></a>Key</p>
</td>
<td class="cellrowborder" valign="top" width="54.87%" headers="mcps1.2.3.1.2 "><p id="p47020190"><a name="p47020190"></a><a name="p47020190"></a>Indicates the key of the object for which the multipart upload was initiated.</p>
<p id="p20528533"><a name="p20528533"></a><a name="p20528533"></a>Type: String</p>
</td>
</tr>
<tr id="row50539077"><td class="cellrowborder" valign="top" width="45.129999999999995%" headers="mcps1.2.3.1.1 "><p id="p24535"><a name="p24535"></a><a name="p24535"></a>UploadId</p>
</td>
<td class="cellrowborder" valign="top" width="54.87%" headers="mcps1.2.3.1.2 "><p id="p1987390"><a name="p1987390"></a><a name="p1987390"></a>Indicates the ID for the initiated multipart upload. This ID is used for the subsequent <strong id="b107946278162"><a name="b107946278162"></a><a name="b107946278162"></a>Upload Part</strong> operation.</p>
<p id="p26760930"><a name="p26760930"></a><a name="p26760930"></a>Type: String</p>
</td>
</tr>
</tbody>
</table>

## Error Responses<a name="section52393888"></a>

-   If an AK or signature is invalid, OBS returns status code  **403 Forbidden** and error code **AccessDenied**.
-   If the requested bucket does not exist, OBS returns status code  **404 Not Found** and error code **NoSuchBucket**.
-   If the requester does not have  **WRITE** permission for the requested bucket, OBS returns status code **403 Forbidden** and error code **AccessDenied**.

For details about other error responses, see  [Table 1](error-codes.md#table30733758).

## Sample Request<a name="section44716440"></a>

```
POST /objectkey?uploads  HTTP/1.1 
 User-Agent: Jakarta Commons-HttpClient/3.1 
 Host: bucketname.obs.example.com
 Accept: */*
 Date: Mon, 1 Nov 2010 20:34:56 GMT
 Authorization: AWS AKIAIOSFODNN7EXAMPLE:VGhpcyBtZXNzYWdlIHNpZ25lZGGieSRlbHZpbmc=
```

## Sample Response<a name="section66903647"></a>

```
HTTP/1.1 200 OK  
 Server: OBS
 x-amz-id-2: Weag1LuByRx9e6j5Onimru9pO4ZVKnJ2Qz7/C1NPcfTWAtRPfTaOFg==  
 x-amz-request-id: 996c76696e6727732072657175657374  
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Date: Mon, 1 Nov 2010 20:34:56 GMT  
 Content-Type: application/xml
 Content-Length: 146    

 <?xml version="1.0" encoding="UTF-8" standalone="yes"?>  
 <InitiateMultipartUploadResult xmlns="http://obs.example.com/doc/2015-06-30/"> 
 <Bucket>bucket01</Bucket>  
 <Key>objectkey</Key>  
 <UploadId>DCD2FC98B4F70000013DF578ACA318E7</UploadId> 
 </InitiateMultipartUploadResult>
```

