# PUT Object<a name="EN-US_TOPIC_0125560399"></a>

After creating a bucket in OBS, you can use this operation to upload an object to the bucket.

Uploading an object adds it to a bucket. This operation requires users to have the write permission.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>The objects uploaded by users are stored in buckets. Only the users with the write permission can upload objects to buckets. The names of objects in the same bucket must be unique.  

If objects with the same object keys exist in a specified bucket, the new objects uploaded by a user will overwrite the original objects.

To prevent data from being damaged during the transfer process, users can add  **Content-MD5**  to request headers. After OBS receives the objects that are uploaded, it executes MD5 verification and returns an error if inconsistency is detected.

Users can specify the  **x-amz-acl**  parameter and set a permission control policy when uploading objects.

This operation makes server-side encryption available.

After creating a bucket in OBS, you can send a  **PUT Object**  request to upload an object to the bucket.

## Versioning<a name="section51302964"></a>

If a bucket has versioning enabled, the system automatically generates a unique version ID for the requested object in this bucket and returns the version ID in response header  **x-amz-version-id**. If a bucket has versioning suspended, the version ID of the requested object in this bucket is **null**. For details about bucket versioning, see section [PUT Bucket versioning](put-bucket-versioning.md).

## Request Syntax<a name="section2166644"></a>

```
PUT /ObjectName HTTP/1.1
 User-Agent: agent 
 Host: bucketname.obs.example.com 
 Accept: */* 
 Content-Type: type 
 Content-Length: length 
 Authorization: authorization 
 Date: date 
 <Optional Additional Header> 

<object Content>
```

## Request Parameters<a name="section19499801"></a>

This request involves no parameters.

## Request Headers<a name="section41280485"></a>

You can add optional headers to this request. For details about the optional headers, see  [Table 1](#table21799862).

**Table  1**  Optional request headers

<a name="table21799862"></a>
<table><thead align="left"><tr id="row52930045"><th class="cellrowborder" valign="top" width="24.09%" id="mcps1.2.4.1.1"><p id="p59475228"><a name="p59475228"></a><a name="p59475228"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="42.58%" id="mcps1.2.4.1.2"><p id="p52764152"><a name="p52764152"></a><a name="p52764152"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="33.33%" id="mcps1.2.4.1.3"><p id="p46037880"><a name="p46037880"></a><a name="p46037880"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row38080772"><td class="cellrowborder" valign="top" width="24.09%" headers="mcps1.2.4.1.1 "><p id="p64643717"><a name="p64643717"></a><a name="p64643717"></a>Content-MD5</p>
</td>
<td class="cellrowborder" valign="top" width="42.58%" headers="mcps1.2.4.1.2 "><p id="p1649763"><a name="p1649763"></a><a name="p1649763"></a>The MD5 digest string of the message body is calculated according to the RFC 1864 standard. That is, calculate the 128-bit binary array (the message header data encrypted with MD5) first, and then use Base 64 encoding to convert the binary data to a character string.</p>
<p id="p14847872"><a name="p14847872"></a><a name="p14847872"></a>Type: String</p>
<p id="p66521989"><a name="p66521989"></a><a name="p66521989"></a>Example: <strong id="b20704191319109"><a name="b20704191319109"></a><a name="b20704191319109"></a>n58IG6hfM7vqI4K0vnWpog==</strong></p>
</td>
<td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p41930743"><a name="p41930743"></a><a name="p41930743"></a>Optional</p>
</td>
</tr>
<tr id="row41832375"><td class="cellrowborder" valign="top" width="24.09%" headers="mcps1.2.4.1.1 "><p id="p32979223"><a name="p32979223"></a><a name="p32979223"></a>x-amz-acl</p>
</td>
<td class="cellrowborder" valign="top" width="42.58%" headers="mcps1.2.4.1.2 "><p id="p1338284833911"><a name="p1338284833911"></a><a name="p1338284833911"></a>Indicates the ACL applied to an object.</p>
<p id="p41156112408"><a name="p41156112408"></a><a name="p41156112408"></a>The value of this header is a predefined character string that is not user-configurable.</p>
<p id="p54071387"><a name="p54071387"></a><a name="p54071387"></a>Possible values are <strong id="b16880438"><a name="b16880438"></a><a name="b16880438"></a>private</strong>,&nbsp;<strong id="b17706220"><a name="b17706220"></a><a name="b17706220"></a>public-read</strong>,&nbsp;<strong id="b25138252"><a name="b25138252"></a><a name="b25138252"></a>public-read-write</strong>,&nbsp;<strong id="b24917681"><a name="b24917681"></a><a name="b24917681"></a>authenticated-read</strong>,&nbsp;<strong id="b22932538"><a name="b22932538"></a><a name="b22932538"></a>bucket-owner-read</strong>, and&nbsp;<strong id="b5066258"><a name="b5066258"></a><a name="b5066258"></a>bucket-owner-full-control</strong>. For further details, see&nbsp;<a href="acl.md#table40200743">Table 4</a>.</p>
<p id="p7713785"><a name="p7713785"></a><a name="p7713785"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p10060146"><a name="p10060146"></a><a name="p10060146"></a>Optional</p>
</td>
</tr>
<tr id="row14907262256"><td class="cellrowborder" valign="top" width="24.09%" headers="mcps1.2.4.1.1 "><p id="p1057752116419"><a name="p1057752116419"></a><a name="p1057752116419"></a>x-amz-storage-class</p>
</td>
<td class="cellrowborder" valign="top" width="42.58%" headers="mcps1.2.4.1.2 "><p id="p7305518157"><a name="p7305518157"></a><a name="p7305518157"></a>When creating an object, you can add this header in the request to set the storage class of the object. If you do not add this header, the object will use the default storage class of the bucket.</p>
<p id="p183055181656"><a name="p183055181656"></a><a name="p183055181656"></a>Type: String</p>
<p id="p83054181511"><a name="p83054181511"></a><a name="p83054181511"></a>Note: The storage class can be <strong id="b4305121814519"><a name="b4305121814519"></a><a name="b4305121814519"></a>STANDARD</strong>&nbsp;(OBS Standard),&nbsp;<strong id="b1830516181052"><a name="b1830516181052"></a><a name="b1830516181052"></a>STANDARD_IA</strong>&nbsp;(OBS Warm), or&nbsp;<strong id="b43051018859"><a name="b43051018859"></a><a name="b43051018859"></a>GLACIER</strong> (OBS Cold). Note that the three storage class values are case-sensitive.</p>
<p id="p63051018859"><a name="p63051018859"></a><a name="p63051018859"></a>Example: x-amz-storage-class: STANDARD</p>
</td>
<td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p1157872174110"><a name="p1157872174110"></a><a name="p1157872174110"></a>Optional</p>
</td>
</tr>
<tr id="row23432457"><td class="cellrowborder" valign="top" width="24.09%" headers="mcps1.2.4.1.1 "><p id="p18980874"><a name="p18980874"></a><a name="p18980874"></a>x-amz-meta-*</p>
</td>
<td class="cellrowborder" valign="top" width="42.58%" headers="mcps1.2.4.1.2 "><p id="p61055827"><a name="p61055827"></a><a name="p61055827"></a>This prefix is used to construct a header in an HTTP request for returning self-defined metadata. If this prefix is specified, user-defined metadata is returned in one or more response headers prefixed with <strong id="b12631539"><a name="b12631539"></a><a name="b12631539"></a>x-amz-meta-</strong>.</p>
<p id="p162423294106"><a name="p162423294106"></a><a name="p162423294106"></a>Note: The format of the user-defined metadata header is x-amz-meta-key:value. The total size of the key and value of all user-defined metadata in the request cannot exceed 2 KB.</p>
<p id="p16521724"><a name="p16521724"></a><a name="p16521724"></a>Type: String</p>
<p id="p77431826184012"><a name="p77431826184012"></a><a name="p77431826184012"></a>Example:</p>
<p id="p14477792"><a name="p14477792"></a><a name="p14477792"></a>x-amz-meta-test: test metadata</p>
</td>
<td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p18218892"><a name="p18218892"></a><a name="p18218892"></a>Optional</p>
</td>
</tr>
<tr id="row29752302"><td class="cellrowborder" valign="top" width="24.09%" headers="mcps1.2.4.1.1 "><p id="p61126266"><a name="p61126266"></a><a name="p61126266"></a>x-amz-website-redirect-location</p>
</td>
<td class="cellrowborder" valign="top" width="42.58%" headers="mcps1.2.4.1.2 "><p id="p11530945154019"><a name="p11530945154019"></a><a name="p11530945154019"></a>If a bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL.</p>
<p id="p1366553914409"><a name="p1366553914409"></a><a name="p1366553914409"></a>OBS stores the value of this header in the object metadata.</p>
<p id="p762549"><a name="p762549"></a><a name="p762549"></a>In the following example, the request header sets the redirection to an object (anotherPage.html) in the same bucket:</p>
<p id="p6862947"><a name="p6862947"></a><a name="p6862947"></a>x-amz-website-redirect-location:/anotherPage.html</p>
<p id="p61766529"><a name="p61766529"></a><a name="p61766529"></a>In the following example, the request header sets the object redirection to an external URL:</p>
<p id="p299214691204"><a name="p299214691204"></a><a name="p299214691204"></a>x-amz-website-redirect-location:http://www.example.com/</p>
<p id="p37032986"><a name="p37032986"></a><a name="p37032986"></a>Type: String</p>
<p id="p64861423"><a name="p64861423"></a><a name="p64861423"></a>Default: None</p>
<p id="p46881895"><a name="p46881895"></a><a name="p46881895"></a>Constraint: The value must be prefixed by a slash (/), <strong id="b19283877"><a name="b19283877"></a><a name="b19283877"></a>http://</strong>, or <strong id="b3985524151014"><a name="b3985524151014"></a><a name="b3985524151014"></a>https://</strong>. The length of the value cannot exceed 2 K.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p32194111"><a name="p32194111"></a><a name="p32194111"></a>Optional</p>
</td>
</tr>
<tr id="row46731220101837"><td class="cellrowborder" valign="top" width="24.09%" headers="mcps1.2.4.1.1 "><p id="p47424020165233"><a name="p47424020165233"></a><a name="p47424020165233"></a>x-amz-server-side-encryption</p>
</td>
<td class="cellrowborder" valign="top" width="42.58%" headers="mcps1.2.4.1.2 "><p id="p16140446165233"><a name="p16140446165233"></a><a name="p16140446165233"></a>Indicates that SSE-KMS is used.</p>
<p id="p11046293165233"><a name="p11046293165233"></a><a name="p11046293165233"></a>Type: string</p>
<p id="p32307777165233"><a name="p32307777165233"></a><a name="p32307777165233"></a>Example: x-amz-server-side-encryption:aws:kms</p>
</td>
<td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p66793124165233"><a name="p66793124165233"></a><a name="p66793124165233"></a>No. This header is mandatory when SSE-KMS is used.</p>
</td>
</tr>
<tr id="row37370995101841"><td class="cellrowborder" valign="top" width="24.09%" headers="mcps1.2.4.1.1 "><p id="p38261099165233"><a name="p38261099165233"></a><a name="p38261099165233"></a>x-amz-server-side-encryption-aws-kms-key-id</p>
</td>
<td class="cellrowborder" valign="top" width="42.58%" headers="mcps1.2.4.1.2 "><p id="p12141351165233"><a name="p12141351165233"></a><a name="p12141351165233"></a>Indicates the master key ID. This header is used in SSE-KMS mode. If the customer does not provide the master key, the default master key will be used.</p>
<p id="p42163295165233"><a name="p42163295165233"></a><a name="p42163295165233"></a>Type: string</p>
<p id="p73991784117"><a name="p73991784117"></a><a name="p73991784117"></a>Example: x-amz-server-side-encryption-aws-kms-key-id:arn:aws:kms:sichuan:domainiddomainiddomainiddoma0001:key/4f1cd4de-ab64-4807-920a-47fc42e7f0d0</p>
</td>
<td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p1182970165233"><a name="p1182970165233"></a><a name="p1182970165233"></a>No</p>
</td>
</tr>
<tr id="row483319101847"><td class="cellrowborder" valign="top" width="24.09%" headers="mcps1.2.4.1.1 "><p id="p22293922165233"><a name="p22293922165233"></a><a name="p22293922165233"></a>x-amz-server-side-encryption-customer-algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="42.58%" headers="mcps1.2.4.1.2 "><p id="p60977246165233"><a name="p60977246165233"></a><a name="p60977246165233"></a>Indicates an encryption algorithm. The header is used in SSE-C mode.</p>
<p id="p11924302165233"><a name="p11924302165233"></a><a name="p11924302165233"></a>Type: string</p>
<p id="p40209854165233"><a name="p40209854165233"></a><a name="p40209854165233"></a>Example: x-amz-server-side-encryption-customer-algorithm:AES256</p>
<p id="p26344367165233"><a name="p26344367165233"></a><a name="p26344367165233"></a>Constraints: This header must be used together with <strong id="b35772714165233"><a name="b35772714165233"></a><a name="b35772714165233"></a>x-amz-server-side-encryption-customer-key</strong>&nbsp;and&nbsp;<strong id="b53518977165233"><a name="b53518977165233"></a><a name="b53518977165233"></a>x-amz-server-side-encryption-customer-key-MD5</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p40069867165233"><a name="p40069867165233"></a><a name="p40069867165233"></a>No. This header is mandatory when SSE-C is used.</p>
</td>
</tr>
<tr id="row10298317101850"><td class="cellrowborder" valign="top" width="24.09%" headers="mcps1.2.4.1.1 "><p id="p18577739165233"><a name="p18577739165233"></a><a name="p18577739165233"></a>x-amz-server-side-encryption-customer-key</p>
</td>
<td class="cellrowborder" valign="top" width="42.58%" headers="mcps1.2.4.1.2 "><p id="p28401914165233"><a name="p28401914165233"></a><a name="p28401914165233"></a>Indicates a key used to encrypt objects. The header is used in SSE-C mode.</p>
<p id="p54290637165233"><a name="p54290637165233"></a><a name="p54290637165233"></a>Type: string</p>
<p id="p18853693165233"><a name="p18853693165233"></a><a name="p18853693165233"></a>Example: x-amz-server-side-encryption-customer-key:K7QkYpBkM5+hcs27fsNkUnNVaobncnLht/rCB2o/9Cw=</p>
<p id="p35465514165233"><a name="p35465514165233"></a><a name="p35465514165233"></a>Constraints: This header is a base64-encoded 256-bit or 512-bit key and must be used together with <strong id="b50754173165233"><a name="b50754173165233"></a><a name="b50754173165233"></a>x-amz-server-side-encryption-customer-algorithm</strong>&nbsp;and&nbsp;<strong id="b54134375165233"><a name="b54134375165233"></a><a name="b54134375165233"></a>x-amz-server-side-encryption-customer-key-MD5</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p22808236165233"><a name="p22808236165233"></a><a name="p22808236165233"></a>No. This header is mandatory when SSE-C is used.</p>
</td>
</tr>
<tr id="row58340811101911"><td class="cellrowborder" valign="top" width="24.09%" headers="mcps1.2.4.1.1 "><p id="p51315127165233"><a name="p51315127165233"></a><a name="p51315127165233"></a>x-amz-server-side-encryption-customer-key-MD5</p>
</td>
<td class="cellrowborder" valign="top" width="42.58%" headers="mcps1.2.4.1.2 "><p id="p62884600165233"><a name="p62884600165233"></a><a name="p62884600165233"></a>Indicates the MD5 value of a key used to encrypt objects. The header is used in SSE-C mode. The MD5 value is used to check whether any error occurs during the transmission of the key.</p>
<p id="p29090495165233"><a name="p29090495165233"></a><a name="p29090495165233"></a>Type: string</p>
<p id="p60487871165233"><a name="p60487871165233"></a><a name="p60487871165233"></a>Example: x-amz-server-side-encryption-customer-key-MD5:4XvB3tbNTN+tIEVa0/fGaQ==</p>
<p id="p7519927165233"><a name="p7519927165233"></a><a name="p7519927165233"></a>Constraints: This header is a base64-encoded 128-bit MD5 value and must be used together with <strong id="b570481165233"><a name="b570481165233"></a><a name="b570481165233"></a>x-amz-server-side-encryption-customer-algorithm</strong>&nbsp;and&nbsp;<strong id="b5134335165233"><a name="b5134335165233"></a><a name="b5134335165233"></a>x-amz-server-side-encryption-customer-key</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p13227967165233"><a name="p13227967165233"></a><a name="p13227967165233"></a>No. This header is mandatory when SSE-C is used.</p>
</td>
</tr>
<tr id="row12141032102819"><td class="cellrowborder" valign="top" width="24.09%" headers="mcps1.2.4.1.1 "><p id="p1721163362816"><a name="p1721163362816"></a><a name="p1721163362816"></a>x-amz-security-token</p>
</td>
<td class="cellrowborder" valign="top" width="42.58%" headers="mcps1.2.4.1.2 "><p id="p221119335284"><a name="p221119335284"></a><a name="p221119335284"></a>Header field used to identify the request of a federated user. When the federal authentication function is enabled, users sending such requests are identified as federated users.</p>
<p id="p162111233152811"><a name="p162111233152811"></a><a name="p162111233152811"></a>Type: string</p>
</td>
<td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p112111033132816"><a name="p112111033132816"></a><a name="p112111033132816"></a>Optional. This parameter must be carried in the request sent by federated users.</p>
</td>
</tr>
</tbody>
</table>

## Request Elements<a name="section35980049"></a>

This request involves no elements. Its body contains only the content of the requested object.

## Response Syntax<a name="section20366724"></a>

```
HTTP/1.1 status_code 
 Server: Server Name 
 x-amz-request-id: request id 
 x-amz-id-2: id 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 ETag: etag
 Date: date 
 Content-Length: length 
 Content-Type: type
```

## Response Headers<a name="section49082792"></a>

This response uses common headers. For details about common response headers, see section  [Common Response Headers](common-response-headers.md).

This response also uses optional headers, as described in  [Table 2](#table8944551125949).

**Table  2**  Optional response headers

<a name="table8944551125949"></a>
<table><thead align="left"><tr id="row49696704125949"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p9155250125954"><a name="p9155250125954"></a><a name="p9155250125954"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p186203125954"><a name="p186203125954"></a><a name="p186203125954"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row61967414125949"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p151958931300"><a name="p151958931300"></a><a name="p151958931300"></a>x-amz-version-id</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p456268941300"><a name="p456268941300"></a><a name="p456268941300"></a>Indicates the version ID of an object. The version ID of an object will be returned if the bucket housing the object has versioning enabled.</p>
<p id="p424289971300"><a name="p424289971300"></a><a name="p424289971300"></a>Type: String</p>
</td>
</tr>
<tr id="row53835842102025"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p30672596165320"><a name="p30672596165320"></a><a name="p30672596165320"></a>x-amz-server-side-encryption</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p1452353165320"><a name="p1452353165320"></a><a name="p1452353165320"></a>This header is included in a response if SSE-KMS is used.</p>
<p id="p13071183165320"><a name="p13071183165320"></a><a name="p13071183165320"></a>Type: string</p>
<p id="p50531787165320"><a name="p50531787165320"></a><a name="p50531787165320"></a>Example: x-amz-server-side-encryption:aws:kms</p>
</td>
</tr>
<tr id="row11959653102029"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p62015525165320"><a name="p62015525165320"></a><a name="p62015525165320"></a>x-amz-server-side-encryption-aws-kms-key-id</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p57201653165320"><a name="p57201653165320"></a><a name="p57201653165320"></a>Indicates the master key ID. This header is included in a response if SSE-KMS is used.</p>
<p id="p18715217104213"><a name="p18715217104213"></a><a name="p18715217104213"></a>Example: x-amz-server-side-encryption-aws-kms-key-id:arn:aws:kms:sichuan:domainiddomainiddomainiddoma0001:key/4f1cd4de-ab64-4807-920a-47fc42e7f0d0</p>
</td>
</tr>
<tr id="row43117683102033"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p27282471165320"><a name="p27282471165320"></a><a name="p27282471165320"></a>x-amz-server-side-encryption-customer-algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p62396504165320"><a name="p62396504165320"></a><a name="p62396504165320"></a>Indicates an encryption algorithm. This header is included in a response if SSE-C is used.</p>
<p id="p24697627165320"><a name="p24697627165320"></a><a name="p24697627165320"></a>Type: string</p>
<p id="p20952058165320"><a name="p20952058165320"></a><a name="p20952058165320"></a>Example: x-amz-server-side-encryption-customer-algorithm:AES256</p>
</td>
</tr>
<tr id="row35024478102037"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p40338394165320"><a name="p40338394165320"></a><a name="p40338394165320"></a>x-amz-server-side-encryption-customer-key-MD5</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p46184492165320"><a name="p46184492165320"></a><a name="p46184492165320"></a>Indicates the MD5 value of a key used to encrypt objects. This header is included in a response if SSE-C is used.</p>
<p id="p13007251165320"><a name="p13007251165320"></a><a name="p13007251165320"></a>Type: string</p>
<p id="p49956395165320"><a name="p49956395165320"></a><a name="p49956395165320"></a>Example: x-amz-server-side-encryption-customer-key-MD5:4XvB3tbNTN+tIEVa0/fGaQ==</p>
</td>
</tr>
<tr id="row366835349589"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p1717259495813"><a name="p1717259495813"></a><a name="p1717259495813"></a>x-amz-storage-class</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p3516896295847"><a name="p3516896295847"></a><a name="p3516896295847"></a>This header is returned when the storage class of an object is not Standard.</p>
<p id="p4914001095856"><a name="p4914001095856"></a><a name="p4914001095856"></a>Type: String</p>
<p id="p4880287995813"><a name="p4880287995813"></a><a name="p4880287995813"></a>Valid values: <strong id="b3657273395813"><a name="b3657273395813"></a><a name="b3657273395813"></a>STANDARD_IA</strong>&nbsp;and&nbsp;<strong id="b6071914595813"><a name="b6071914595813"></a><a name="b6071914595813"></a>GLACIER</strong></p>
</td>
</tr>
</tbody>
</table>

## Response Elements<a name="section39091944"></a>

This response involves no elements.

## Error Responses<a name="section16283183"></a>

No special error responses are returned. For details about error responses, see  [Table 1](error-codes.md#table30733758).

## Sample Request<a name="section54232646"></a>

```
PUT /object02 HTTP/1.1 
 User-Agent: Jakarta Commons-HttpClient/3.1 
 Host: bucketname.obs.example.com
 Accept: */* 
 Date: Sat, 03 Dec 2011 07:12:31 +0000 
 Authorization: AWS BF6C09F302931425E9A7:KUxrlwKGWYpUOTgwNxIHALsRdT4= 
 x-amz-meta-key: value 
 Content-Length: 256 

 1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456
```

## Sample Request for Redirecting Object Location<a name="section18331773"></a>

```
PUT /object02 HTTP/1.1
User-Agent: Jakarta Commons-HttpClient/3.1
Host: bucketname.obs.example.com
Accept: */*
Date: Sat, 03 Dec 2011 07:12:31 +0000
Authorization: AWS BF6C09F302931425E9A7:KUxrlwKGWYpUOTgwNxIHALsRdT4=
x-amz-meta-key: value
Content-Length: 256
x-amz-website-redirect-location: www.example.com
1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456
```

## Sample Response for Uploading Objects to a Bucket with No Versioning Configured<a name="section30768229"></a>

```
HTTP/1.1 200 OK 
 Server: OBS 
 x-amz-request-id: 001B21A61C6C0000013402C4616D5285 
 x-amz-id-2: MDAxQjIxQTYxQzZDMDAwMDAxMzQwMkM0NjE2RDUyODVBQUFBQUFBQWJiYmJiYmJi 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon 
 Technologies, Inc 
 Content-Type: text/xml 
 ETag: "33bee59f4c1f859a7aedd36779b321cf" 
 Date: Sat, 03 Dec 2011 07:12:31 GMT 
 Content-Length: 0
```

## Sample Response for Uploading Objects to a Bucket with Versioning Enabled<a name="section8478608"></a>

```
HTTP/1.1 200 OK 
 Server: OBS 
 x-amz-request-id: DCD2FC9CAB78000001438AB633CF1A73 
 x-amz-id-2: zvOE6GmblPrMk544Fg7BEt4LAmwdRuPx5s2qDVeGHZZJhUMmdxKsW4MzeJLkoVvX 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Content-Type: text/xml 
 ETag: "ba1f2511fc30423bdbb183fe33f3dd0f" 
 x-amz-version-id: AAABQ4q2M9_c0vycq3gAAAAAVURTRkha 
 Date: Mon, 13 Jan 2014 08:27:13 GMT 
 Content-Length: 0
```

## Sample Response for Uploading Objects to a Bucket with Versioning Suspended<a name="section9198616"></a>

```
HTTP/1.1 200 OK 
 Server: OBS 
 x-amz-request-id: DCD2FC9CAB78000001439A51DB2B2577 
 x-amz-id-2: GcVgfeOJHx8JZHTHrRqkPsbKdB583fYbr3RBbHT6mMrBstReVILBZbMAdLiBYy1l 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Content-Type: text/xml 
 ETag: "0b55edbacf50d5086ea83ee08e55cbbd" 
 Date: Thu, 13 Jan 2014 09:11:32 GMT 
 Content-Length: 0
```

