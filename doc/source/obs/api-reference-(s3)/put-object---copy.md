# PUT Object - Copy<a name="EN-US_TOPIC_0125560348"></a>

You can use this operation to create a copy of an existing object in OBS.

By default, a  **PUT Object - Copy** operation copies object metadata together with the object. If you want to update the metadata, provide new metadata in the **PUT Object - Copy** request. The object ACL is not copied together with the object and the ACL of a copy object is set to **private** by default. You can send a **PUT Object acl**  request to modify the object ACL.

The  **PUT Object - Copy**  request must contain authentication information and cannot contain a request body.

This operation makes server-side encryption available, but cannot change encrypted objects to non-encrypted ones. If a user performs this operation to change the encrypted objects, the system returns error code  **400**.

When objects are copied, the storage classes of target objects are consistent with the default storage classes of target buckets.

## Versioning<a name="section35965948"></a>

By default,  **x-amz-copy-source**  specifies the latest version of the source object. If the latest version of the source object is a deletion mark, the object is considered to be deleted. You can add **versionId** to request header **x-amz-copy-source**  to copy an object with the specified version ID.

If a bucket has versioning enabled, the system automatically generates a unique version ID for the requested object in this bucket and returns the version ID in response header  **x-amz-version-id**. If a bucket has versioning suspended, the version ID of the requested object in this bucket is **null**.

>![](/images/icon-notice.gif) **NOTICE:**   
>If multi-version is not enabled for a bucket, you can replace source object  **objecta**  with target object **objectb**  by replication. If **objectb**  already exists before you perform replication, the new **objectb**  will overwrite the old **objectb**  after you perform replication.  
>After replication is performed successfully, only new  **objectb**  can be downloaded. The old **objectb**  will be deleted. Before using the copy interface, ensure that the target object does not exist or is useless to avoid incorrect data deletion. During the replication, the source object **objecta**  is not changed.  
>You cannot determine whether a request is executed successfully only using  **status\_code**  in the header returned by HTTP. If 200 in **status\_code**  is returned, the server has received the request and starts to process the request. The body in the response shows whether the replication operation succeeds. The replication operation succeeds only when the body has ETags. Otherwise, the replication operation fails.  

## OBS Cold Objects<a name="section3886489515555"></a>

If source objects are OBS cold objects, check the restore status of the objects. You can copy the OBS cold objects only after the objects are restored. If the objects are not restored or are being restored, the copy fails, and error "403 Forbidden" is returned. The fault is described as follows:

ErrorCode: InvalidObjectState

ErrorMessage: Operation is not valid for the source object's storage class

## Request Syntax<a name="section4469833"></a>

```
 PUT /destinationObjectName HTTP/1.1 
 User-Agent: agent
 Host: bucketname.obs.example.com 
 Accept: */*
 x-amz-copy-source: /sourceBucket/sourceObject 
 x-amz-metadata-directive: COPY 
 x-amz-copy-source-if-match: etag 
 x-amz-copy-source-if-none-match: etag 
 x-amz-copy-source-if-unmodified-since: time_stamp 
 x-amz-copy-source-if-modified-since: time_stamp 
 Authorization: signatureValue 
 Date: date
```

## Request Parameters<a name="section40228503"></a>

This request involves no parameters.

## Request Headers<a name="section26512207"></a>

This request uses common headers. For details about common request headers, see section  [Common Request Headers](common-request-headers.md). In addition, you can add optional headers to specify the object to be copied. [Table 1](#table59683248)  describes the optional headers.

**Table  1**  Optional request headers

<a name="table59683248"></a>
<table><thead align="left"><tr id="row66482620"><th class="cellrowborder" valign="top" width="26.842684268426847%" id="mcps1.2.4.1.1"><p id="p16383173"><a name="p16383173"></a><a name="p16383173"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="50.155015501550146%" id="mcps1.2.4.1.2"><p id="p51968642"><a name="p51968642"></a><a name="p51968642"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="23.002300230023003%" id="mcps1.2.4.1.3"><p id="p48710492"><a name="p48710492"></a><a name="p48710492"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row53235770"><td class="cellrowborder" valign="top" width="26.842684268426847%" headers="mcps1.2.4.1.1 "><p id="p17130117"><a name="p17130117"></a><a name="p17130117"></a>x-amz-acl</p>
</td>
<td class="cellrowborder" valign="top" width="50.155015501550146%" headers="mcps1.2.4.1.2 "><p id="p20507816152311"><a name="p20507816152311"></a><a name="p20507816152311"></a>Indicates the ACL applied to the copy object. Possible values are <strong id="b19507121613233"><a name="b19507121613233"></a><a name="b19507121613233"></a>private</strong>,&nbsp;<strong id="b1650711619237"><a name="b1650711619237"></a><a name="b1650711619237"></a>public-read</strong>,&nbsp;<strong id="b12507316152316"><a name="b12507316152316"></a><a name="b12507316152316"></a>public-read-write</strong>,&nbsp;<strong id="b25071416172318"><a name="b25071416172318"></a><a name="b25071416172318"></a>authenticated-read</strong>,&nbsp;<strong id="b1650791622317"><a name="b1650791622317"></a><a name="b1650791622317"></a>bucket-owner-read</strong>, and&nbsp;<strong id="b135071162233"><a name="b135071162233"></a><a name="b135071162233"></a>bucket-owner-full-control</strong>.</p>
<p id="p45362212"><a name="p45362212"></a><a name="p45362212"></a>Type: String</p>
<p id="p10940237105513"><a name="p10940237105513"></a><a name="p10940237105513"></a>Example:</p>
<p id="p26779645"><a name="p26779645"></a><a name="p26779645"></a>x-amz-acl: acl</p>
</td>
<td class="cellrowborder" valign="top" width="23.002300230023003%" headers="mcps1.2.4.1.3 "><p id="p60791181"><a name="p60791181"></a><a name="p60791181"></a>Optional</p>
</td>
</tr>
<tr id="row10249724"><td class="cellrowborder" valign="top" width="26.842684268426847%" headers="mcps1.2.4.1.1 "><p id="p24921279"><a name="p24921279"></a><a name="p24921279"></a>x-amz-copy-source</p>
</td>
<td class="cellrowborder" valign="top" width="50.155015501550146%" headers="mcps1.2.4.1.2 "><p id="p5357756"><a name="p5357756"></a><a name="p5357756"></a>Indicates the name of the source bucket and the key of the source object. If the source object has multiple version IDs, <strong id="b48219807"><a name="b48219807"></a><a name="b48219807"></a>versionId</strong> is used to specify the required version ID.</p>
<p id="p31325081"><a name="p31325081"></a><a name="p31325081"></a>Type: String</p>
<p id="p177681539125616"><a name="p177681539125616"></a><a name="p177681539125616"></a>Example: x-amz-copy-source: /source_bucket/sourceObject</p>
</td>
<td class="cellrowborder" valign="top" width="23.002300230023003%" headers="mcps1.2.4.1.3 "><p id="p36516628"><a name="p36516628"></a><a name="p36516628"></a>Mandatory</p>
</td>
</tr>
<tr id="row60214201"><td class="cellrowborder" valign="top" width="26.842684268426847%" headers="mcps1.2.4.1.1 "><p id="p45512090"><a name="p45512090"></a><a name="p45512090"></a>x-amz-metadata-directive</p>
</td>
<td class="cellrowborder" valign="top" width="50.155015501550146%" headers="mcps1.2.4.1.2 "><p id="p62600705"><a name="p62600705"></a><a name="p62600705"></a>Indicates whether the metadata is copied from the source object or replaced with the metadata provided in the request.</p>
<p id="p26535433"><a name="p26535433"></a><a name="p26535433"></a>Type: String</p>
<p id="p37492307"><a name="p37492307"></a><a name="p37492307"></a>Valid values: <strong id="b1886449"><a name="b1886449"></a><a name="b1886449"></a>COPY</strong>&nbsp;or&nbsp;<strong id="b16978042"><a name="b16978042"></a><a name="b16978042"></a>REPLACE</strong></p>
<p id="p18584657"><a name="p18584657"></a><a name="p18584657"></a>Default: <strong id="b33044190"><a name="b33044190"></a><a name="b33044190"></a>COPY</strong></p>
<p id="p166073287567"><a name="p166073287567"></a><a name="p166073287567"></a>Example: x-amz-metadata-directive: <strong id="b22531436163515"><a name="b22531436163515"></a><a name="b22531436163515"></a>COPY</strong></p>
<p id="p64241563"><a name="p64241563"></a><a name="p64241563"></a>Constraints:</p>
<a name="ul41303163"></a><a name="ul41303163"></a><ul id="ul41303163"><li>If the value is neither <strong id="b57221892"><a name="b57221892"></a><a name="b57221892"></a>COPY</strong>&nbsp;nor&nbsp;<strong id="b45234984"><a name="b45234984"></a><a name="b45234984"></a>REPLACE</strong>, OBS returns status code&nbsp;<strong id="b2215046577"><a name="b2215046577"></a><a name="b2215046577"></a>400</strong>.</li><li>If you want to copy an object to itself, set the value to <strong id="b40155067"><a name="b40155067"></a><a name="b40155067"></a>REPLACE</strong>. Otherwise, OBS considers the request invalid and returns status code&nbsp;<strong id="b2178201265715"><a name="b2178201265715"></a><a name="b2178201265715"></a>400</strong>.</li></ul>
</td>
<td class="cellrowborder" valign="top" width="23.002300230023003%" headers="mcps1.2.4.1.3 "><p id="p31334966"><a name="p31334966"></a><a name="p31334966"></a>Optional</p>
</td>
</tr>
<tr id="row13579242"><td class="cellrowborder" valign="top" width="26.842684268426847%" headers="mcps1.2.4.1.1 "><p id="p26176854"><a name="p26176854"></a><a name="p26176854"></a>x-amz-copy-source-if-match</p>
</td>
<td class="cellrowborder" valign="top" width="50.155015501550146%" headers="mcps1.2.4.1.2 "><p id="p39950397"><a name="p39950397"></a><a name="p39950397"></a>Copies the source object only if its ETag matches the one specified by this header, otherwise a 412 HTTP status code error (failed precondition) is returned.</p>
<p id="p24009259"><a name="p24009259"></a><a name="p24009259"></a>Type: String</p>
<p id="p1325511618579"><a name="p1325511618579"></a><a name="p1325511618579"></a>Example: x-amz-copy-source-if-match: etag</p>
<p id="p54445730"><a name="p54445730"></a><a name="p54445730"></a>Constraints: This header can be used with <strong id="b20249527"><a name="b20249527"></a><a name="b20249527"></a>x-amz-copy-source-if-unmodified-since</strong> but cannot be used with other conditional copy headers.</p>
</td>
<td class="cellrowborder" valign="top" width="23.002300230023003%" headers="mcps1.2.4.1.3 "><p id="p29598957"><a name="p29598957"></a><a name="p29598957"></a>Optional</p>
</td>
</tr>
<tr id="row65064025"><td class="cellrowborder" valign="top" width="26.842684268426847%" headers="mcps1.2.4.1.1 "><p id="p35694663"><a name="p35694663"></a><a name="p35694663"></a>x-amz-copy-source-if-none-match</p>
</td>
<td class="cellrowborder" valign="top" width="50.155015501550146%" headers="mcps1.2.4.1.2 "><p id="p5586594"><a name="p5586594"></a><a name="p5586594"></a>Copies the source object only if its ETag is different from the one specified by this header, otherwise a 412 HTTP status code error (failed precondition) is returned.</p>
<p id="p50279347"><a name="p50279347"></a><a name="p50279347"></a>Type: String</p>
<p id="p422542920571"><a name="p422542920571"></a><a name="p422542920571"></a>Example: x-amz-copy-source-if-none-match: etag</p>
</td>
<td class="cellrowborder" valign="top" width="23.002300230023003%" headers="mcps1.2.4.1.3 "><p id="p42733733"><a name="p42733733"></a><a name="p42733733"></a>Optional</p>
</td>
</tr>
<tr id="row49059277"><td class="cellrowborder" valign="top" width="26.842684268426847%" headers="mcps1.2.4.1.1 "><p id="p14378473"><a name="p14378473"></a><a name="p14378473"></a>x-amz-copy-source-if-unmodified-since</p>
</td>
<td class="cellrowborder" valign="top" width="50.155015501550146%" headers="mcps1.2.4.1.2 "><p id="p23805690"><a name="p23805690"></a><a name="p23805690"></a>Copies the source object only if it has not been modified since the time specified by this header, otherwise a 412 HTTP status code error (failed precondition) is returned.</p>
<p id="p12924626"><a name="p12924626"></a><a name="p12924626"></a>Type: HTTP time string complying with the format specified in http://www.ietf.org/rfc/rfc2616.txt.</p>
<p id="p8196113755710"><a name="p8196113755710"></a><a name="p8196113755710"></a>Example: x-amz-copy-source-if-unmodified-since: time-stamp</p>
<p id="p26811930"><a name="p26811930"></a><a name="p26811930"></a>Constraints: This header can be used with <strong id="b39980785"><a name="b39980785"></a><a name="b39980785"></a>x-amz-copy-source-if-match</strong> but cannot be used with other conditional copy headers.</p>
</td>
<td class="cellrowborder" valign="top" width="23.002300230023003%" headers="mcps1.2.4.1.3 "><p id="p17218116"><a name="p17218116"></a><a name="p17218116"></a>Optional</p>
</td>
</tr>
<tr id="row20745324"><td class="cellrowborder" valign="top" width="26.842684268426847%" headers="mcps1.2.4.1.1 "><p id="p2649692"><a name="p2649692"></a><a name="p2649692"></a>x-amz-copy-source-if-modified-since</p>
</td>
<td class="cellrowborder" valign="top" width="50.155015501550146%" headers="mcps1.2.4.1.2 "><p id="p13298480"><a name="p13298480"></a><a name="p13298480"></a>Copies the source object only if it has not been modified since the time specified by this header, otherwise a 412 HTTP status code error (failed precondition) is returned.</p>
<p id="p52577459"><a name="p52577459"></a><a name="p52577459"></a>Type: HTTP time string complying with the format specified in http://www.ietf.org/rfc/rfc2616.txt.</p>
<p id="p20227659195720"><a name="p20227659195720"></a><a name="p20227659195720"></a>Example: x-amz-copy-source-if-modified-since: time-stamp</p>
<p id="p9806758"><a name="p9806758"></a><a name="p9806758"></a>Constraints: This header can be used with <strong id="b21151959"><a name="b21151959"></a><a name="b21151959"></a>x-amz-copy-source-if-none-match</strong> but cannot be used with other conditional copy headers.</p>
</td>
<td class="cellrowborder" valign="top" width="23.002300230023003%" headers="mcps1.2.4.1.3 "><p id="p35587158"><a name="p35587158"></a><a name="p35587158"></a>Optional</p>
</td>
</tr>
<tr id="row3055850814546"><td class="cellrowborder" valign="top" width="26.842684268426847%" headers="mcps1.2.4.1.1 "><p id="p1666552019542"><a name="p1666552019542"></a><a name="p1666552019542"></a>x-amz-storage-class</p>
</td>
<td class="cellrowborder" valign="top" width="50.155015501550146%" headers="mcps1.2.4.1.2 "><p id="p7305518157"><a name="p7305518157"></a><a name="p7305518157"></a>When creating an object, you can add this header in the request to set the storage class of the object. If you do not add this header, the object will use the default storage class of the bucket.</p>
<p id="p183055181656"><a name="p183055181656"></a><a name="p183055181656"></a>Type: String</p>
<p id="p83054181511"><a name="p83054181511"></a><a name="p83054181511"></a>Note: The storage class can be <strong id="b4305121814519"><a name="b4305121814519"></a><a name="b4305121814519"></a>STANDARD</strong>&nbsp;(OBS Standard),&nbsp;<strong id="b1830516181052"><a name="b1830516181052"></a><a name="b1830516181052"></a>STANDARD_IA</strong>&nbsp;(OBS Warm), or&nbsp;<strong id="b43051018859"><a name="b43051018859"></a><a name="b43051018859"></a>GLACIER</strong> (OBS Cold). Note that the three storage class values are case-sensitive.</p>
<p id="p63051018859"><a name="p63051018859"></a><a name="p63051018859"></a>Example: x-amz-storage-class: STANDARD</p>
</td>
<td class="cellrowborder" valign="top" width="23.002300230023003%" headers="mcps1.2.4.1.3 "><p id="p1157872174110"><a name="p1157872174110"></a><a name="p1157872174110"></a>Optional</p>
</td>
</tr>
<tr id="row51848974"><td class="cellrowborder" valign="top" width="26.842684268426847%" headers="mcps1.2.4.1.1 "><p id="p39017328"><a name="p39017328"></a><a name="p39017328"></a>x-amz-website-redirect-location</p>
</td>
<td class="cellrowborder" valign="top" width="50.155015501550146%" headers="mcps1.2.4.1.2 "><p id="p6287015"><a name="p6287015"></a><a name="p6287015"></a>If a bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL. OBS stores the value of this header in the object metadata.</p>
<p id="p56583142"><a name="p56583142"></a><a name="p56583142"></a>Type: String</p>
<p id="p39486235"><a name="p39486235"></a><a name="p39486235"></a>Default: None</p>
<p id="p19831799"><a name="p19831799"></a><a name="p19831799"></a>Constraint: The value must be prefixed by a slash (/), <strong id="b44268467"><a name="b44268467"></a><a name="b44268467"></a>http://</strong>, or <strong id="b87443517142"><a name="b87443517142"></a><a name="b87443517142"></a>https://</strong>. The length of the value cannot exceed 2 K.</p>
</td>
<td class="cellrowborder" valign="top" width="23.002300230023003%" headers="mcps1.2.4.1.3 "><p id="p59458202"><a name="p59458202"></a><a name="p59458202"></a>Optional</p>
</td>
</tr>
<tr id="row42184781102735"><td class="cellrowborder" valign="top" width="26.842684268426847%" headers="mcps1.2.4.1.1 "><p id="p21220179123822"><a name="p21220179123822"></a><a name="p21220179123822"></a>x-amz-server-side-encryption</p>
</td>
<td class="cellrowborder" valign="top" width="50.155015501550146%" headers="mcps1.2.4.1.2 "><p id="p41112973123822"><a name="p41112973123822"></a><a name="p41112973123822"></a>Indicates the SSE-KMS mode. The destination object uses SSE-KMS for encryption.</p>
<p id="p34472444123822"><a name="p34472444123822"></a><a name="p34472444123822"></a>Type: string</p>
<p id="p41816544123822"><a name="p41816544123822"></a><a name="p41816544123822"></a>Example: x-amz-server-side-encryption:aws:kms</p>
</td>
<td class="cellrowborder" valign="top" width="23.002300230023003%" headers="mcps1.2.4.1.3 "><p id="p31696883123822"><a name="p31696883123822"></a><a name="p31696883123822"></a>No. This header is mandatory when SSE-KMS is used.</p>
</td>
</tr>
<tr id="row32920370102833"><td class="cellrowborder" valign="top" width="26.842684268426847%" headers="mcps1.2.4.1.1 "><p id="p21578594123822"><a name="p21578594123822"></a><a name="p21578594123822"></a>x-amz-server-side-encryption-aws-kms-key-id</p>
</td>
<td class="cellrowborder" valign="top" width="50.155015501550146%" headers="mcps1.2.4.1.2 "><p id="p3035726123822"><a name="p3035726123822"></a><a name="p3035726123822"></a>Indicates the master key ID. This header is used in SSE-KMS mode. If the customer does not provide the master key, the default master key will be used.</p>
<p id="p27321534123822"><a name="p27321534123822"></a><a name="p27321534123822"></a>Type: string</p>
<p id="p3578182595819"><a name="p3578182595819"></a><a name="p3578182595819"></a>Example: x-amz-server-side-encryption-aws-kms-key-id:arn:aws:kms:sichuan:domainiddomainiddomainiddoma0001:key/4f1cd4de-ab64-4807-920a-47fc42e7f0d0</p>
</td>
<td class="cellrowborder" valign="top" width="23.002300230023003%" headers="mcps1.2.4.1.3 "><p id="p53175169123822"><a name="p53175169123822"></a><a name="p53175169123822"></a>No</p>
</td>
</tr>
<tr id="row62153691102822"><td class="cellrowborder" valign="top" width="26.842684268426847%" headers="mcps1.2.4.1.1 "><p id="p4432417512395"><a name="p4432417512395"></a><a name="p4432417512395"></a>x-amz-server-side-encryption-customer-algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="50.155015501550146%" headers="mcps1.2.4.1.2 "><p id="p3348839412395"><a name="p3348839412395"></a><a name="p3348839412395"></a>Indicates an encryption algorithm. The header is used in SSE-C mode.</p>
<p id="p3296009412395"><a name="p3296009412395"></a><a name="p3296009412395"></a>Type: string</p>
<p id="p2820539812395"><a name="p2820539812395"></a><a name="p2820539812395"></a>Example: x-amz-server-side-encryption-customer-algorithm:AES256</p>
<p id="p5252199412395"><a name="p5252199412395"></a><a name="p5252199412395"></a>Constraints: This header must be used together with <strong id="b293589812395"><a name="b293589812395"></a><a name="b293589812395"></a>x-amz-server-side-encryption-customer-key</strong>&nbsp;and&nbsp;<strong id="b2642308912395"><a name="b2642308912395"></a><a name="b2642308912395"></a>x-amz-server-side-encryption-customer-key-MD5</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="23.002300230023003%" headers="mcps1.2.4.1.3 "><p id="p5989548512395"><a name="p5989548512395"></a><a name="p5989548512395"></a>No. This parameter is mandatory when SSE-C is used.</p>
</td>
</tr>
<tr id="row17017962102815"><td class="cellrowborder" valign="top" width="26.842684268426847%" headers="mcps1.2.4.1.1 "><p id="p4304762712395"><a name="p4304762712395"></a><a name="p4304762712395"></a>x-amz-server-side-encryption-customer-key</p>
</td>
<td class="cellrowborder" valign="top" width="50.155015501550146%" headers="mcps1.2.4.1.2 "><p id="p6430572912395"><a name="p6430572912395"></a><a name="p6430572912395"></a>Indicates a key used to encrypt destination objects. The header is used in SSE-C mode.</p>
<p id="p4188065312395"><a name="p4188065312395"></a><a name="p4188065312395"></a>Type: string</p>
<p id="p4138156012395"><a name="p4138156012395"></a><a name="p4138156012395"></a>Example: x-amz-server-side-encryption-customer-key:K7QkYpBkM5+hcs27fsNkUnNVaobncnLht/rCB2o/9Cw=</p>
<p id="p3688972312395"><a name="p3688972312395"></a><a name="p3688972312395"></a>Constraints: This header is a base64-encoded 256-bit or 512-bit key and must be used together with <strong id="b6357205512395"><a name="b6357205512395"></a><a name="b6357205512395"></a>x-amz-server-side-encryption-customer-algorithm</strong>&nbsp;and&nbsp;<strong id="b3527759012395"><a name="b3527759012395"></a><a name="b3527759012395"></a>x-amz-server-side-encryption-customer-key-MD5</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="23.002300230023003%" headers="mcps1.2.4.1.3 "><p id="p3891251712395"><a name="p3891251712395"></a><a name="p3891251712395"></a>No. This header is mandatory when SSE-C is used.</p>
</td>
</tr>
<tr id="row65245422102749"><td class="cellrowborder" valign="top" width="26.842684268426847%" headers="mcps1.2.4.1.1 "><p id="p4728453712395"><a name="p4728453712395"></a><a name="p4728453712395"></a>x-amz-server-side-encryption-customer-key-MD5</p>
</td>
<td class="cellrowborder" valign="top" width="50.155015501550146%" headers="mcps1.2.4.1.2 "><p id="p484225012395"><a name="p484225012395"></a><a name="p484225012395"></a>Indicates the MD5 value of a key used to encrypt objects. The header is used in SSE-C mode. The MD5 value is used to check whether any error occurs during the transmission of the key.</p>
<p id="p4358025312395"><a name="p4358025312395"></a><a name="p4358025312395"></a>Type: string</p>
<p id="p5667796412395"><a name="p5667796412395"></a><a name="p5667796412395"></a>Example: x-amz-server-side-encryption-customer-key-MD5:4XvB3tbNTN+tIEVa0/fGaQ==</p>
<p id="p4033963012395"><a name="p4033963012395"></a><a name="p4033963012395"></a>Constraints: This header is a base64-encoded 128-bit MD5 value and must be used together with <strong id="b2751235812395"><a name="b2751235812395"></a><a name="b2751235812395"></a>x-amz-server-side-encryption-customer-algorithm</strong>&nbsp;and&nbsp;<strong id="b4628463612395"><a name="b4628463612395"></a><a name="b4628463612395"></a>x-amz-server-side-encryption-customer-key</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="23.002300230023003%" headers="mcps1.2.4.1.3 "><p id="p5806804612395"><a name="p5806804612395"></a><a name="p5806804612395"></a>No. This header is mandatory when SSE-C is used.</p>
</td>
</tr>
<tr id="row45574092102745"><td class="cellrowborder" valign="top" width="26.842684268426847%" headers="mcps1.2.4.1.1 "><p id="p12564056123925"><a name="p12564056123925"></a><a name="p12564056123925"></a>x-amz-copy-source-server-side-encryption-customer-algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="50.155015501550146%" headers="mcps1.2.4.1.2 "><p id="p11055621123925"><a name="p11055621123925"></a><a name="p11055621123925"></a>Indicates the algorithm used to decrypt a source object. The header is used in SSE-C mode.</p>
<p id="p32391731123925"><a name="p32391731123925"></a><a name="p32391731123925"></a>Type: string</p>
<p id="p23090127123925"><a name="p23090127123925"></a><a name="p23090127123925"></a>Example: x-amz-copy-source-server-side-encryption-customer-algorithm:AES256</p>
<p id="p6484554123925"><a name="p6484554123925"></a><a name="p6484554123925"></a>Constraints: This header must be used together with <strong id="b183691442181411"><a name="b183691442181411"></a><a name="b183691442181411"></a>x-amz-copy-source-server-side-encryption-customer-key</strong> and&nbsp;<strong id="b55486857123925"><a name="b55486857123925"></a><a name="b55486857123925"></a>x-amz-copy-source-server-side-encryption-customer-key-MD5</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="23.002300230023003%" headers="mcps1.2.4.1.3 "><p id="p65250457123925"><a name="p65250457123925"></a><a name="p65250457123925"></a>No. This header is mandatory when SSE-C is used to copy a source object.</p>
</td>
</tr>
<tr id="row45537881102741"><td class="cellrowborder" valign="top" width="26.842684268426847%" headers="mcps1.2.4.1.1 "><p id="p54507955123925"><a name="p54507955123925"></a><a name="p54507955123925"></a>x-amz-copy-source-server-side-encryption-customer-key</p>
</td>
<td class="cellrowborder" valign="top" width="50.155015501550146%" headers="mcps1.2.4.1.2 "><p id="p53068195123925"><a name="p53068195123925"></a><a name="p53068195123925"></a>Indicates the key used to decrypt a source object. The header is used in SSE-C mode.</p>
<p id="p7851708123925"><a name="p7851708123925"></a><a name="p7851708123925"></a>Type: string</p>
<p id="p3556511123925"><a name="p3556511123925"></a><a name="p3556511123925"></a>Example: x-amz-copy-source-server-side-encryption-customer-key:K7QkYpBkM5+hcs27fsNkUnNVaobncnLht/rCB2o/9Cw=</p>
<p id="p32008606123925"><a name="p32008606123925"></a><a name="p32008606123925"></a>Constraints: This header is a base64-encoded 256-bit or 512-bit key and must be used together with <strong id="b19642000123925"><a name="b19642000123925"></a><a name="b19642000123925"></a>x-amz-copy-source-server-side-encryption-customer-algorithm</strong>&nbsp;and&nbsp;<strong id="b42560280123925"><a name="b42560280123925"></a><a name="b42560280123925"></a>x-amz-copy-source-server-side-encryption-customer-key-MD5</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="23.002300230023003%" headers="mcps1.2.4.1.3 "><p id="p24830675123925"><a name="p24830675123925"></a><a name="p24830675123925"></a>No. This header is mandatory when SSE-C is used to copy a source object.</p>
</td>
</tr>
<tr id="row13212054102811"><td class="cellrowborder" valign="top" width="26.842684268426847%" headers="mcps1.2.4.1.1 "><p id="p49278127123925"><a name="p49278127123925"></a><a name="p49278127123925"></a>x-amz-copy-source-server-side-encryption-customer-key-MD5</p>
</td>
<td class="cellrowborder" valign="top" width="50.155015501550146%" headers="mcps1.2.4.1.2 "><p id="p32105346123925"><a name="p32105346123925"></a><a name="p32105346123925"></a>Indicates the MD5 value of the key used to decrypt a source object. The header is used in SSE-C mode. The MD5 value is used to check whether any error occurs during the transmission of the key.</p>
<p id="p20512663123925"><a name="p20512663123925"></a><a name="p20512663123925"></a>Type: string</p>
<p id="p50396242123925"><a name="p50396242123925"></a><a name="p50396242123925"></a>Example: x-amz-copy-source-server-side-encryption-customer-key-MD5:4XvB3tbNTN+tIEVa0/fGaQ==</p>
<p id="p50912996123925"><a name="p50912996123925"></a><a name="p50912996123925"></a>Constraints: This header is a base64-encoded 128-bit MD5 value and must be used together with <strong id="b55563782123925"><a name="b55563782123925"></a><a name="b55563782123925"></a>x-amz-copy-source-server-side-encryption-customer-algorithm</strong>&nbsp;and&nbsp;<strong id="b30311993123925"><a name="b30311993123925"></a><a name="b30311993123925"></a>x-amz-copy-source-server-side-encryption-customer-key</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="23.002300230023003%" headers="mcps1.2.4.1.3 "><p id="p39352383123925"><a name="p39352383123925"></a><a name="p39352383123925"></a>No. This header is mandatory when SSE-C is used to copy a source object.</p>
</td>
</tr>
<tr id="row89721291390"><td class="cellrowborder" valign="top" width="26.842684268426847%" headers="mcps1.2.4.1.1 "><p id="p588915106396"><a name="p588915106396"></a><a name="p588915106396"></a>x-amz-security-token</p>
</td>
<td class="cellrowborder" valign="top" width="50.155015501550146%" headers="mcps1.2.4.1.2 "><p id="p488919106393"><a name="p488919106393"></a><a name="p488919106393"></a>Header field used to identify the request of a federated user. When the federal authentication function is enabled, users sending such requests are identified as federated users.</p>
<p id="p4889191015391"><a name="p4889191015391"></a><a name="p4889191015391"></a>Type: string</p>
</td>
<td class="cellrowborder" valign="top" width="23.002300230023003%" headers="mcps1.2.4.1.3 "><p id="p1988913104399"><a name="p1988913104399"></a><a name="p1988913104399"></a>Optional. This parameter must be carried in the request sent by federated users.</p>
</td>
</tr>
</tbody>
</table>

For details about other headers, see section  [Common Request Headers](common-request-headers.md).

## Request Elements<a name="section37283276"></a>

This request involves no elements.

## Response Syntax<a name="section35297384"></a>

```
HTTP/1.1 status_code 
 Server: Server Name 
 x-amz-request-id: request id 
 x-amz-id-2: id  
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Content-Type: type  
 Date: date 
 Content-Length: length 

 <?xml version="1.0" encoding="UTF-8" standalone="yes"?> 
 <CopyObjectResult xmlns="http://obs.example.com/doc/2015-06-30/"> 
 <LastModified>modifiedDate</LastModified> 
 <ETag>etagValue</ETag> 
 </CopyObjectResult>
```

## Response Headers<a name="section49241002"></a>

This response uses common headers. For details about common response headers, see section  [Common Response Headers](common-response-headers.md).

This response also uses optional headers, as described in  [Table 2](#table44830087).

**Table  2**  Optional response header

<a name="table44830087"></a>
<table><thead align="left"><tr id="row57259714"><th class="cellrowborder" valign="top" width="42.870000000000005%" id="mcps1.2.3.1.1"><p id="p7525275"><a name="p7525275"></a><a name="p7525275"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="57.13%" id="mcps1.2.3.1.2"><p id="p5567508"><a name="p5567508"></a><a name="p5567508"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row48314965"><td class="cellrowborder" valign="top" width="42.870000000000005%" headers="mcps1.2.3.1.1 "><p id="p21198087"><a name="p21198087"></a><a name="p21198087"></a>x-amz-copy-source-version-id</p>
</td>
<td class="cellrowborder" valign="top" width="57.13%" headers="mcps1.2.3.1.2 "><p id="p39323473"><a name="p39323473"></a><a name="p39323473"></a>Indicates the version ID of the source object.</p>
<p id="p18366943"><a name="p18366943"></a><a name="p18366943"></a>Type: String</p>
</td>
</tr>
<tr id="row31084764"><td class="cellrowborder" valign="top" width="42.870000000000005%" headers="mcps1.2.3.1.1 "><p id="p34837968"><a name="p34837968"></a><a name="p34837968"></a>x-amz-version-id</p>
</td>
<td class="cellrowborder" valign="top" width="57.13%" headers="mcps1.2.3.1.2 "><p id="p3303123"><a name="p3303123"></a><a name="p3303123"></a>Indicates the version ID of the target object.</p>
<p id="p29728115"><a name="p29728115"></a><a name="p29728115"></a>Type: String</p>
</td>
</tr>
<tr id="row63702400102931"><td class="cellrowborder" valign="top" width="42.870000000000005%" headers="mcps1.2.3.1.1 "><p id="p3616339517113"><a name="p3616339517113"></a><a name="p3616339517113"></a>x-amz-server-side-encryption</p>
</td>
<td class="cellrowborder" valign="top" width="57.13%" headers="mcps1.2.3.1.2 "><p id="p4355391217113"><a name="p4355391217113"></a><a name="p4355391217113"></a>This header is included in a response if SSE-KMS is used.</p>
<p id="p5644089417113"><a name="p5644089417113"></a><a name="p5644089417113"></a>Type: string</p>
<p id="p3820600617113"><a name="p3820600617113"></a><a name="p3820600617113"></a>Example: x-amz-server-side-encryption:aws:kms</p>
</td>
</tr>
<tr id="row3814548102942"><td class="cellrowborder" valign="top" width="42.870000000000005%" headers="mcps1.2.3.1.1 "><p id="p199994017113"><a name="p199994017113"></a><a name="p199994017113"></a>x-amz-server-side-encryption-aws-kms-key-id</p>
</td>
<td class="cellrowborder" valign="top" width="57.13%" headers="mcps1.2.3.1.2 "><p id="p2777747017113"><a name="p2777747017113"></a><a name="p2777747017113"></a>Indicates the master key ID. This header is included in a response if SSE-KMS is used.</p>
<p id="p4867064117113"><a name="p4867064117113"></a><a name="p4867064117113"></a>Example: x-amz-server-side-encryption-aws-kms-key-id:arn:aws:kms:sichuan:domainiddomainiddomainiddoma0001:key/4f1cd4de-ab64-4807-920a-47fc42e7f0d0</p>
</td>
</tr>
<tr id="row57904797102938"><td class="cellrowborder" valign="top" width="42.870000000000005%" headers="mcps1.2.3.1.1 "><p id="p4741738317113"><a name="p4741738317113"></a><a name="p4741738317113"></a>x-amz-server-side-encryption-customer-algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="57.13%" headers="mcps1.2.3.1.2 "><p id="p1560279017113"><a name="p1560279017113"></a><a name="p1560279017113"></a>Indicates an encryption algorithm. This header is included in a response if SSE-C is used.</p>
<p id="p620738517113"><a name="p620738517113"></a><a name="p620738517113"></a>Type: string</p>
<p id="p5586646617113"><a name="p5586646617113"></a><a name="p5586646617113"></a>Example: x-amz-server-side-encryption-customer-algorithm:AES256</p>
</td>
</tr>
<tr id="row43265229102935"><td class="cellrowborder" valign="top" width="42.870000000000005%" headers="mcps1.2.3.1.1 "><p id="p5868213117113"><a name="p5868213117113"></a><a name="p5868213117113"></a>x-amz-server-side-encryption-customer-key-MD5</p>
</td>
<td class="cellrowborder" valign="top" width="57.13%" headers="mcps1.2.3.1.2 "><p id="p5563216517113"><a name="p5563216517113"></a><a name="p5563216517113"></a>Indicates the MD5 value of a key used to encrypt objects. This header is included in a response if SSE-C is used.</p>
<p id="p3092743917113"><a name="p3092743917113"></a><a name="p3092743917113"></a>Type: string</p>
<p id="p991150317113"><a name="p991150317113"></a><a name="p991150317113"></a>Example: x-amz-server-side-encryption-customer-key-MD5:4XvB3tbNTN+tIEVa0/fGaQ==</p>
</td>
</tr>
</tbody>
</table>

## Response Elements<a name="section40515840"></a>

This response contains elements to indicate the copy results.  [Table 3](#table5815269)  describes the elements.

**Table  3**  Response elements

<a name="table5815269"></a>
<table><thead align="left"><tr id="row43001397"><th class="cellrowborder" valign="top" width="32.550000000000004%" id="mcps1.2.3.1.1"><p id="p60561095"><a name="p60561095"></a><a name="p60561095"></a>Element</p>
</th>
<th class="cellrowborder" valign="top" width="67.45%" id="mcps1.2.3.1.2"><p id="p6501678"><a name="p6501678"></a><a name="p6501678"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row56873938"><td class="cellrowborder" valign="top" width="32.550000000000004%" headers="mcps1.2.3.1.1 "><p id="p43386266"><a name="p43386266"></a><a name="p43386266"></a>CopyObjectResult</p>
</td>
<td class="cellrowborder" valign="top" width="67.45%" headers="mcps1.2.3.1.2 "><p id="p24626671"><a name="p24626671"></a><a name="p24626671"></a>Indicates the container for copy results.</p>
<p id="p20313449"><a name="p20313449"></a><a name="p20313449"></a>Type: XML</p>
</td>
</tr>
<tr id="row48603320"><td class="cellrowborder" valign="top" width="32.550000000000004%" headers="mcps1.2.3.1.1 "><p id="p44554846"><a name="p44554846"></a><a name="p44554846"></a>LastModified</p>
</td>
<td class="cellrowborder" valign="top" width="67.45%" headers="mcps1.2.3.1.2 "><p id="p52172744"><a name="p52172744"></a><a name="p52172744"></a>Indicates the date when the object was last modified.</p>
<p id="p66901514"><a name="p66901514"></a><a name="p66901514"></a>Type: String</p>
</td>
</tr>
<tr id="row65242718"><td class="cellrowborder" valign="top" width="32.550000000000004%" headers="mcps1.2.3.1.1 "><p id="p50168842"><a name="p50168842"></a><a name="p50168842"></a>ETag</p>
</td>
<td class="cellrowborder" valign="top" width="67.45%" headers="mcps1.2.3.1.2 "><p id="p37144369"><a name="p37144369"></a><a name="p37144369"></a>Indicates the ETag of the new object.</p>
<p id="p65863871"><a name="p65863871"></a><a name="p65863871"></a>Type: String</p>
</td>
</tr>
</tbody>
</table>

## Error Responses<a name="section29098241"></a>

No special error responses are returned. For details about error responses, see  [Table 1](error-codes.md#table30733758).

## Sample Request<a name="section28473001"></a>

```
PUT /destobject HTTP/1.1 
 User-Agent: Jakarta Commons-HttpClient/3.1 
 Host: bucketname.obs.example.com 
 Accept: */* 
 Date: Sat, 03 Dec 2011 08:48:07 +0000 
 Authorization: AWS BF6C09F302931425E9A7:2rZR+iaH8xUewvUKuicLhLHpNoU= 
 x-amz-copy-source: /bucket/srcobject
```

## Sample Response<a name="section54930419"></a>

```
HTTP/1.1 200 OK 
 Server: OBS 
 x-amz-request-id: 001B21A61C6C00000134031BE8005293 
 x-amz-id-2: MDAxQjIxQTYxQzZDMDAwMDAxMzQwMzFCRTgwMDUyOTNBQUFBQUFBQWJiYmJiYmJi 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Content-Type: application/xml 
 Date: Sat, 03 Dec 2011 08:48:07 GMT 
 Content-Length: 254 

 <?xml version="1.0" encoding="UTF-8" standalone="yes"?> 
 <CopyObjectResult xmlns="http://obs.example.com/doc/2015-06-30/"> 
 <LastModified>2011-12-03T08:48:07.706Z</LastModified> 
 <ETag>"507e3fff69b69bf57d303e807448560b"</ETag> 
 </CopyObjectResult>
```

## Sample Request \(Copying an Object with Version ID Specified to a Bucket with Versioning Enabled\)<a name="section20178982"></a>

```
PUT /destobject HTTP/1.1 
 User-Agent: Jakarta Commons-HttpClient/3.1 
 Host: bucketname.obs.example.com 
 Accept: */* 
 Date: Mon, 13 Jan 2014 12:19:13 +0000 
 Authorization: AWS C5780CDE717D50F4CDAA:4BLYv+1UxfRSHBMvrhVLDszxvcY= 
 x-amz-copy-source: versionbucket/srcobject?versionId=AAABQ4uBLdLc0vycq3gAAAAEVURTRkha
```

## Sample Response \(Copying an Object with Version ID Specified to a Bucket with Versioning Enabled\)<a name="section47393112"></a>

```
HTTP/1.1 200 OK 
 Server: OBS 
 x-amz-request-id: DCD2FC9CAB78000001438B8A9C898B79 
 x-amz-id-2: DB/qBZmbN6AIoX9mrrSNYdLxwvbO0tLR/l6/XKTT4NmZspzhWrwp5Z74ybAYVOgr 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Content-Type: application/xml 
 x-amz-version-id: AAABQ4uKnOrc0vycq3gAAAAFVURTRkha 
 x-amz-copy-source-version-id: AAABQ4uBLdLc0vycq3gAAAAEVURTRkha 
 Date: Mon, 13 Jan 2014 12:19:14 GMT 
 Transfer-Encoding: chunked
 <?xml version="1.0" encoding="UTF-8" standalone="yes"?> 
 <CopyObjectResult xmlns="http://obs.example.com/doc/2015-06-30/"> 
 <LastModified>2014-01-13T12:19:13.770Z</LastModified> 
 <ETag>"ba1f2511fc30423bdbb183fe33f3dd0f"</ETag> 
 </CopyObjectResult>
```

## Sample Request \(Copying an Object with Version ID Specified to a Bucket with Versioning Suspended\)<a name="section13636834"></a>

```
PUT /object03 HTTP/1.1 
 User-Agent: Jakarta Commons-HttpClient/3.1 
 Host: bucketname.obs.example.com 
 Accept: */* 
 Date: Mon, 13 Jan 2014 12:30:11 +0000 
 Authorization: AWS C5780CDE717D50F4CDAA:TzFaMXTynxWqPdhhRy9l/8Litb8= 
 x-amz-copy-source: versionbucket/srcobject?versionId=AAABQ4uBLdLc0vycq3gAAAAEVURTRkha
```

## Sample Response \(Copying an Object with Version ID Specified to a Bucket with Versioning Suspended\)<a name="section55622644"></a>

```
HTTP/1.1 200 OK 
 Server: OBS 
 x-amz-request-id: DCD2FC9CAB78000001438B94A6CE90D3 
 x-amz-id-2: ITdGwAvGXezuPzC6m87LVpk2F0i6P5W8GxhBOhmwdf03VjrcL/OXSeOlTpnTLnJy 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Content-Type: application/xml 
 x-amz-version-id: null 
 Date: Mon, 13 Jan 2014 12:30:11 GMT 
 Transfer-Encoding: chunked
 <?xml version="1.0" encoding="UTF-8" standalone="yes"?> 
 <CopyObjectResult xmlns="http://obs.example.com/doc/2015-06-30/"> 
 <LastModified>2014-01-13T12:30:11.690Z</LastModified> 
 <ETag>"ba1f2511fc30423bdbb183fe33f3dd0f"</ETag> 
 </CopyObjectResult>
```

