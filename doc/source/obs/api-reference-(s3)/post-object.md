# POST Object<a name="EN-US_TOPIC_0125560263"></a>

You can use this operation to upload an object to an existing bucket.

Uploading an object indicates that an object is added to a bucket. This operation requires the write permission.

>![](/images/icon-note.gif) **NOTE:**   
>The objects that are uploaded by users are stored in buckets. Only the users who have the write permission can upload objects to buckets. The names of objects in the same bucket must be unique.  

If objects whose object keys are the same exist in a specified bucket, the new objects that are uploaded by a user will overwrite the original objects. To prevent data from being damaged during the transfer process, users can add  **Content-MD5** to request headers. After OBS receives the objects that are uploaded, it executes MD5 verification and will return an error if inconsistency is detected.

Users can specify the **x-amz-acl**  parameter and set a permission control policy when uploading objects.

After creating a bucket in OBS, you can send a  **PUT Object**  request to upload an object to the bucket.

This operation makes server-side encryption available.

## Versioning<a name="section779118"></a>

If a bucket has versioning enabled, the system automatically generates a unique version ID for the requested object in this bucket and returns the version ID in response header  **x-amz-version-id**. If a bucket has versioning suspended, the version ID of the requested object in this bucket is **null**. For details about bucket versioning, see section  [PUT Bucket versioning](put-bucket-versioning.md).

## Request Syntax<a name="section17540457"></a>

```
POST / HTTP/1.1 
 Host: bucketname.obs.example.com 
 User-Agent: browser_data 
 Accept: file_types 
 Accept-Language: Regions 
 Accept-Encoding: encoding 
 Accept-Charset: character_set 
 Keep-Alive: 300 
 Connection: keep-alive 
 Content-Type: multipart/form-data; boundary=-9431149156168 
 Content-Length: length 


 --9431149156168 
 Content-Disposition: form-data; name="key" 
 acl 
 --9431149156168 
 Content-Disposition: form-data; name="success_action_redirect" 
 success_redirect 
 --9431149156168 
 Content-Disposition: form-data; name="content-Type" 
 content_type 
 --9431149156168 
 Content-Disposition: form-data; name="x-amz-meta-uuid" 
 uuid 
 --9431149156168 
 Content-Disposition: form-data; name="x-amz-meta-tag" 
 metadata 
 --9431149156168 
 Content-Disposition: form-data; name="AWSAccessKeyId" 
 access-key-id 
 --9431149156168 
 Content-Disposition: form-data; name="policy" 
 encoded_policy 
 --9431149156168 
 Content-Disposition: form-data; name="signature" 
 signature= 
 --9431149156168 
 Content-Disposition: form-data; name="file"; filename="MyFilename" 
 Content-Type: image/jpeg 
 file_content 
 --9431149156168 
 Content-Disposition: form-data; name="submit" 
 Upload to OBS 
 --9431149156168--
```

## Request Parameters<a name="section23646388"></a>

This request involves no parameters.

## Request Headers<a name="section11490904"></a>

This request uses common headers. For details about common request headers, see section  [Common Request Headers](common-request-headers.md). If you want to obtain CORS configuration information, you must use the headers in [Table 1](#table48637933).

**Table  1**  Request headers of CORS configuration

<a name="table48637933"></a>
<table><thead align="left"><tr id="row22385437"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p1281126"><a name="p1281126"></a><a name="p1281126"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p36662351"><a name="p36662351"></a><a name="p36662351"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p16860416"><a name="p16860416"></a><a name="p16860416"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row23516450"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p25784284"><a name="p25784284"></a><a name="p25784284"></a>Origin</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p8152279"><a name="p8152279"></a><a name="p8152279"></a>Indicates an origin specified by a pre-request. Generally, it is a domain name.</p>
<p id="p6261652"><a name="p6261652"></a><a name="p6261652"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p37431827"><a name="p37431827"></a><a name="p37431827"></a>Mandatory</p>
</td>
</tr>
<tr id="row1342126"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p41603419"><a name="p41603419"></a><a name="p41603419"></a>Access-Control-Request-Headers</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p14433768"><a name="p14433768"></a><a name="p14433768"></a>Indicates the HTTP headers of a request. The request can use multiple HTTP headers.</p>
<p id="p62795050"><a name="p62795050"></a><a name="p62795050"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p53234283"><a name="p53234283"></a><a name="p53234283"></a>Optional</p>
</td>
</tr>
<tr id="row133743171618"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p10584027164"><a name="p10584027164"></a><a name="p10584027164"></a>x-amz-security-token</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p13589112161616"><a name="p13589112161616"></a><a name="p13589112161616"></a>Header field used to identify the request of a federated user. When the federal authentication function is enabled, users sending such requests are identified as federated users.</p>
<p id="p459017221614"><a name="p459017221614"></a><a name="p459017221614"></a>Type: string</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p15921241616"><a name="p15921241616"></a><a name="p15921241616"></a>Optional. This parameter must be carried in the request sent by federated users.</p>
</td>
</tr>
</tbody>
</table>

## Request Elements<a name="section2355172710170"></a>

This request uses form fields.  [Table 2](#table13225554)  describes the form fields.

**Table  2**  Form fields

<a name="table13225554"></a>
<table><thead align="left"><tr id="row35727861"><th class="cellrowborder" valign="top" width="26.062606260626065%" id="mcps1.2.4.1.1"><p id="p8275629"><a name="p8275629"></a><a name="p8275629"></a>Form Field</p>
</th>
<th class="cellrowborder" valign="top" width="50.83508350835084%" id="mcps1.2.4.1.2"><p id="p66346226"><a name="p66346226"></a><a name="p66346226"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="23.102310231023104%" id="mcps1.2.4.1.3"><p id="p5335211"><a name="p5335211"></a><a name="p5335211"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row29498945"><td class="cellrowborder" valign="top" width="26.062606260626065%" headers="mcps1.2.4.1.1 "><p id="p40604315"><a name="p40604315"></a><a name="p40604315"></a>file</p>
</td>
<td class="cellrowborder" valign="top" width="50.83508350835084%" headers="mcps1.2.4.1.2 "><p id="p615201"><a name="p615201"></a><a name="p615201"></a>Indicates the content of the object to be uploaded.</p>
<p id="p5536817"><a name="p5536817"></a><a name="p5536817"></a>Type: Binary or text content</p>
<p id="p49831357"><a name="p49831357"></a><a name="p49831357"></a>Constraints: This field must be the last one in a form. Each request can contain only one <strong id="b45829029"><a name="b45829029"></a><a name="b45829029"></a>file</strong>&nbsp;field. All excessive&nbsp;<strong id="b9808084"><a name="b9808084"></a><a name="b9808084"></a>file</strong> fields are discarded.</p>
</td>
<td class="cellrowborder" valign="top" width="23.102310231023104%" headers="mcps1.2.4.1.3 "><p id="p56257360"><a name="p56257360"></a><a name="p56257360"></a>Mandatory</p>
</td>
</tr>
<tr id="row36554200"><td class="cellrowborder" valign="top" width="26.062606260626065%" headers="mcps1.2.4.1.1 "><p id="p8100198"><a name="p8100198"></a><a name="p8100198"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="50.83508350835084%" headers="mcps1.2.4.1.2 "><p id="p52136268"><a name="p52136268"></a><a name="p52136268"></a>Indicates the name of the object to be uploaded.</p>
<p id="p66573232"><a name="p66573232"></a><a name="p66573232"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="23.102310231023104%" headers="mcps1.2.4.1.3 "><p id="p23722702"><a name="p23722702"></a><a name="p23722702"></a>Mandatory</p>
</td>
</tr>
<tr id="row12177730"><td class="cellrowborder" valign="top" width="26.062606260626065%" headers="mcps1.2.4.1.1 "><p id="p46872098"><a name="p46872098"></a><a name="p46872098"></a>AWSAccessKeyId</p>
</td>
<td class="cellrowborder" valign="top" width="50.83508350835084%" headers="mcps1.2.4.1.2 "><p id="p38543611"><a name="p38543611"></a><a name="p38543611"></a>Indicates the AK of the requester.</p>
<p id="p11348180"><a name="p11348180"></a><a name="p11348180"></a>Type: String</p>
<p id="p35024756"><a name="p35024756"></a><a name="p35024756"></a>Constraints: Required if the <strong id="b46787348"><a name="b46787348"></a><a name="b46787348"></a>policy</strong> field is included in the request.</p>
</td>
<td class="cellrowborder" valign="top" width="23.102310231023104%" headers="mcps1.2.4.1.3 "><p id="p31678816"><a name="p31678816"></a><a name="p31678816"></a>Optional</p>
</td>
</tr>
<tr id="row16673895"><td class="cellrowborder" valign="top" width="26.062606260626065%" headers="mcps1.2.4.1.1 "><p id="p8408241"><a name="p8408241"></a><a name="p8408241"></a>policy</p>
</td>
<td class="cellrowborder" valign="top" width="50.83508350835084%" headers="mcps1.2.4.1.2 "><p id="p9978940"><a name="p9978940"></a><a name="p9978940"></a>Indicates the security policy of the request.</p>
<p id="p22701601"><a name="p22701601"></a><a name="p22701601"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="23.102310231023104%" headers="mcps1.2.4.1.3 "><p id="p26890416"><a name="p26890416"></a><a name="p26890416"></a>Optional</p>
</td>
</tr>
<tr id="row40687155"><td class="cellrowborder" valign="top" width="26.062606260626065%" headers="mcps1.2.4.1.1 "><p id="p7325296"><a name="p7325296"></a><a name="p7325296"></a>expires</p>
</td>
<td class="cellrowborder" valign="top" width="50.83508350835084%" headers="mcps1.2.4.1.2 "><p id="p56478093"><a name="p56478093"></a><a name="p56478093"></a>Indicates the date and time at which an object is no longer cacheable. The time is expressed in milliseconds in RFC 2616 format. If this field is specified, it will be returned in response headers after you send a <strong id="b78715716106"><a name="b78715716106"></a><a name="b78715716106"></a>GET Object</strong> or&nbsp;<strong id="b11322802"><a name="b11322802"></a><a name="b11322802"></a>HEAD Object</strong> request.</p>
<p id="p34796360"><a name="p34796360"></a><a name="p34796360"></a>Type: String</p>
<p id="p44731784"><a name="p44731784"></a><a name="p44731784"></a>Example:</p>
<p id="p67041741"><a name="p67041741"></a><a name="p67041741"></a>Policy: {" expires ": "1000" }</p>
<p id="p66504758"><a name="p66504758"></a><a name="p66504758"></a>HTML: &lt;input type="text" name=" expires " value="1000" /&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="23.102310231023104%" headers="mcps1.2.4.1.3 "><p id="p18176357"><a name="p18176357"></a><a name="p18176357"></a>Optional</p>
</td>
</tr>
<tr id="row29369493"><td class="cellrowborder" valign="top" width="26.062606260626065%" headers="mcps1.2.4.1.1 "><p id="p30118695"><a name="p30118695"></a><a name="p30118695"></a>x-amz-acl</p>
</td>
<td class="cellrowborder" valign="top" width="50.83508350835084%" headers="mcps1.2.4.1.2 "><p id="p23695246"><a name="p23695246"></a><a name="p23695246"></a>Indicates the ACL applied to the object to be uploaded. Possible values are <strong id="b11930629"><a name="b11930629"></a><a name="b11930629"></a>private</strong>,&nbsp;<strong id="b40266802"><a name="b40266802"></a><a name="b40266802"></a>public-read</strong>,&nbsp;<strong id="b26856902"><a name="b26856902"></a><a name="b26856902"></a>public-read-write</strong>,&nbsp;<strong id="b40385530"><a name="b40385530"></a><a name="b40385530"></a>authenticated-read</strong>,&nbsp;<strong id="b27925455"><a name="b27925455"></a><a name="b27925455"></a>bucket-owner-read</strong>, and&nbsp;<strong id="b50002511"><a name="b50002511"></a><a name="b50002511"></a>bucket-owner-full-control</strong>. For details, see&nbsp;<a href="acl.md#table40200743">Table 4</a>.</p>
<p id="p23671576"><a name="p23671576"></a><a name="p23671576"></a>Type: String</p>
<p id="p11717596"><a name="p11717596"></a><a name="p11717596"></a>Example:</p>
<p id="p38349502"><a name="p38349502"></a><a name="p38349502"></a>Policy: {"acl": "public-read" }</p>
<p id="p9601199"><a name="p9601199"></a><a name="p9601199"></a>HTML:&lt;input type="text" name="acl" value="public-read" /&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="23.102310231023104%" headers="mcps1.2.4.1.3 "><p id="p39499626"><a name="p39499626"></a><a name="p39499626"></a>Optional</p>
</td>
</tr>
<tr id="row18755193052610"><td class="cellrowborder" valign="top" width="26.062606260626065%" headers="mcps1.2.4.1.1 "><p id="p1075125011447"><a name="p1075125011447"></a><a name="p1075125011447"></a>x-amz-storage-class</p>
</td>
<td class="cellrowborder" valign="top" width="50.83508350835084%" headers="mcps1.2.4.1.2 "><p id="p7305518157"><a name="p7305518157"></a><a name="p7305518157"></a>When creating an object, you can add this header in the request to set the storage class of the object. If you do not add this header, the object will use the default storage class of the bucket.</p>
<p id="p183055181656"><a name="p183055181656"></a><a name="p183055181656"></a>Type: String</p>
<p id="p83054181511"><a name="p83054181511"></a><a name="p83054181511"></a>Note: The storage class can be <strong id="b4305121814519"><a name="b4305121814519"></a><a name="b4305121814519"></a>STANDARD</strong>&nbsp;(OBS Standard),&nbsp;<strong id="b1830516181052"><a name="b1830516181052"></a><a name="b1830516181052"></a>STANDARD_IA</strong>&nbsp;(OBS Warm), or&nbsp;<strong id="b43051018859"><a name="b43051018859"></a><a name="b43051018859"></a>GLACIER</strong> (OBS Cold). Note that the three storage class values are case-sensitive.</p>
<p id="p63051018859"><a name="p63051018859"></a><a name="p63051018859"></a>Example: x-amz-storage-class: STANDARD</p>
</td>
<td class="cellrowborder" valign="top" width="23.102310231023104%" headers="mcps1.2.4.1.3 "><p id="p1157872174110"><a name="p1157872174110"></a><a name="p1157872174110"></a>Optional</p>
</td>
</tr>
<tr id="row19952318"><td class="cellrowborder" valign="top" width="26.062606260626065%" headers="mcps1.2.4.1.1 "><p id="p5525098"><a name="p5525098"></a><a name="p5525098"></a>Cache-Control, Content-Type, Content-Disposition, Content-Encoding</p>
</td>
<td class="cellrowborder" valign="top" width="50.83508350835084%" headers="mcps1.2.4.1.2 "><p id="p44879761"><a name="p44879761"></a><a name="p44879761"></a>Indicate standard HTTP headers. If these fields are specified, they are returned in response headers after you send a <strong id="b1264671"><a name="b1264671"></a><a name="b1264671"></a>GET Object</strong>&nbsp;or&nbsp;<strong id="b11382045"><a name="b11382045"></a><a name="b11382045"></a>HEAD Object</strong> request.</p>
<p id="p35329549"><a name="p35329549"></a><a name="p35329549"></a>Type: String</p>
<p id="p49530486"><a name="p49530486"></a><a name="p49530486"></a>Example:</p>
<p id="p43121195"><a name="p43121195"></a><a name="p43121195"></a>Policy: ["starts-with", "$Content-Type", "text/"]</p>
<p id="p52546435"><a name="p52546435"></a><a name="p52546435"></a>HTML: &lt;input type="text" name="content-type" value="text/plain" /&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="23.102310231023104%" headers="mcps1.2.4.1.3 "><p id="p28402861"><a name="p28402861"></a><a name="p28402861"></a>Optional</p>
</td>
</tr>
<tr id="row54299160"><td class="cellrowborder" valign="top" width="26.062606260626065%" headers="mcps1.2.4.1.1 "><p id="p36155831"><a name="p36155831"></a><a name="p36155831"></a>success_action_redirect</p>
</td>
<td class="cellrowborder" valign="top" width="50.83508350835084%" headers="mcps1.2.4.1.2 "><p id="p42941223"><a name="p42941223"></a><a name="p42941223"></a>Indicates the URL to which the client is redirected after the request is successfully responded to.</p>
<a name="ul50926693"></a><a name="ul50926693"></a><ul id="ul50926693"><li>If the value is valid and the request is successful, OBS returns status code 303. <strong id="b31421457"><a name="b31421457"></a><a name="b31421457"></a>Location</strong> contains success_action_redirect, bucket name, object name, and object ETag.</li><li>If the value is invalid, OBS ignores this field and returns status code 204. <strong id="b62110049"><a name="b62110049"></a><a name="b62110049"></a>Location</strong> contains the object address.</li></ul>
<p id="p22119530"><a name="p22119530"></a><a name="p22119530"></a>Type: String</p>
<p id="p64858045"><a name="p64858045"></a><a name="p64858045"></a>Example:</p>
<p id="p46851500"><a name="p46851500"></a><a name="p46851500"></a>Policy: {"success_action_redirect": "http://123458.com"}</p>
<p id="p19010318"><a name="p19010318"></a><a name="p19010318"></a>HTML: &lt;input type="text" name="success_action_redirect" value="http://123458.com" /&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="23.102310231023104%" headers="mcps1.2.4.1.3 "><p id="p63440828"><a name="p63440828"></a><a name="p63440828"></a>Optional</p>
</td>
</tr>
<tr id="row34096545"><td class="cellrowborder" valign="top" width="26.062606260626065%" headers="mcps1.2.4.1.1 "><p id="p10356773"><a name="p10356773"></a><a name="p10356773"></a>x-amz-meta-*</p>
</td>
<td class="cellrowborder" valign="top" width="50.83508350835084%" headers="mcps1.2.4.1.2 "><p id="p33592248"><a name="p33592248"></a><a name="p33592248"></a>This prefix is used to construct a field in a <strong id="b33894784"><a name="b33894784"></a><a name="b33894784"></a>POST</strong>&nbsp;request for returning self-defined metadata. If this prefix is specified, user-defined metadata is returned in one or more response headers prefixed with&nbsp;<strong id="b36617605"><a name="b36617605"></a><a name="b36617605"></a>x-amz-meta-</strong>.</p>
<p id="p7423105101115"><a name="p7423105101115"></a><a name="p7423105101115"></a>Note: The format of the user-defined metadata header is x-amz-meta-key:value. The total size of the key and value of all user-defined metadata in the request cannot exceed 2 KB.</p>
<p id="p61122992"><a name="p61122992"></a><a name="p61122992"></a>Type: String</p>
<p id="p13236018"><a name="p13236018"></a><a name="p13236018"></a>Example:</p>
<p id="p52015300"><a name="p52015300"></a><a name="p52015300"></a>Policy: {" x-amz-meta-test ": " test metadata " }</p>
<p id="p65484519"><a name="p65484519"></a><a name="p65484519"></a>HTML: &lt;input type="text" name=" x-amz-meta-test " value=" test metadata " /&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="23.102310231023104%" headers="mcps1.2.4.1.3 "><p id="p2645837"><a name="p2645837"></a><a name="p2645837"></a>Optional</p>
</td>
</tr>
<tr id="row23812538"><td class="cellrowborder" valign="top" width="26.062606260626065%" headers="mcps1.2.4.1.1 "><p id="p49767403"><a name="p49767403"></a><a name="p49767403"></a>success_action_status</p>
</td>
<td class="cellrowborder" valign="top" width="50.83508350835084%" headers="mcps1.2.4.1.2 "><p id="p4627874"><a name="p4627874"></a><a name="p4627874"></a>Indicates the status code returned after a <strong id="b1489418516114"><a name="b1489418516114"></a><a name="b1489418516114"></a>POST Object</strong> request is successfully received. Possible values are&nbsp;<strong id="b39313476"><a name="b39313476"></a><a name="b39313476"></a>200</strong>,&nbsp;<strong id="b18276970"><a name="b18276970"></a><a name="b18276970"></a>201</strong>, and&nbsp;<strong id="b30275003"><a name="b30275003"></a><a name="b30275003"></a>204</strong>.</p>
<a name="ul4039578"></a><a name="ul4039578"></a><ul id="ul4039578"><li>If the value is set to <strong id="b58770411"><a name="b58770411"></a><a name="b58770411"></a>200</strong>&nbsp;or&nbsp;<strong id="b59171655"><a name="b59171655"></a><a name="b59171655"></a>204</strong>, OBS returns an empty response body.</li><li>If the value is set to <strong id="b28174764"><a name="b28174764"></a><a name="b28174764"></a>201</strong>, OBS returns a response containing an XML file recording request details.</li><li>If the value is not set or is invalid, OBS returns status code 204.</li></ul>
<p id="p454533"><a name="p454533"></a><a name="p454533"></a>Type: String</p>
<p id="p4090801"><a name="p4090801"></a><a name="p4090801"></a>Example:</p>
<p id="p36817211"><a name="p36817211"></a><a name="p36817211"></a>Policy: ["starts-with", "$success_action_status", ""]</p>
<p id="p62919444"><a name="p62919444"></a><a name="p62919444"></a>HTML: &lt;input type="text" name="success_action_status" value="200" /&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="23.102310231023104%" headers="mcps1.2.4.1.3 "><p id="p63310175"><a name="p63310175"></a><a name="p63310175"></a>Optional</p>
</td>
</tr>
<tr id="row32920667"><td class="cellrowborder" valign="top" width="26.062606260626065%" headers="mcps1.2.4.1.1 "><p id="p49328407"><a name="p49328407"></a><a name="p49328407"></a>x-amz-website-redirect-location</p>
</td>
<td class="cellrowborder" valign="top" width="50.83508350835084%" headers="mcps1.2.4.1.2 "><p id="p36177998"><a name="p36177998"></a><a name="p36177998"></a>If a bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL. OBS stores the value of this header in the object metadata.</p>
<p id="p57166532"><a name="p57166532"></a><a name="p57166532"></a>Default: None</p>
<p id="p44736746"><a name="p44736746"></a><a name="p44736746"></a>Constraint: The value must be prefixed by a slash (/), <strong id="b67086402"><a name="b67086402"></a><a name="b67086402"></a>http://</strong>, or <strong id="b089551381110"><a name="b089551381110"></a><a name="b089551381110"></a>https://</strong>. The length of the value cannot exceed 2 K.</p>
</td>
<td class="cellrowborder" valign="top" width="23.102310231023104%" headers="mcps1.2.4.1.3 "><p id="p50734192"><a name="p50734192"></a><a name="p50734192"></a>Optional</p>
</td>
</tr>
<tr id="row53360395102221"><td class="cellrowborder" valign="top" width="26.062606260626065%" headers="mcps1.2.4.1.1 "><p id="p14442198165530"><a name="p14442198165530"></a><a name="p14442198165530"></a>x-amz-server-side-encryption</p>
</td>
<td class="cellrowborder" valign="top" width="50.83508350835084%" headers="mcps1.2.4.1.2 "><p id="p28967360165530"><a name="p28967360165530"></a><a name="p28967360165530"></a>Indicates that SSE-KMS is used.</p>
<p id="p59379650165530"><a name="p59379650165530"></a><a name="p59379650165530"></a>Type: string</p>
<p id="p64654806165530"><a name="p64654806165530"></a><a name="p64654806165530"></a>Example: x-amz-server-side-encryption:aws:kms</p>
</td>
<td class="cellrowborder" valign="top" width="23.102310231023104%" headers="mcps1.2.4.1.3 "><p id="p1093962910237"><a name="p1093962910237"></a><a name="p1093962910237"></a><span>No. This header is mandatory when KMS-managed keys are used.</span></p>
</td>
</tr>
<tr id="row62019588102226"><td class="cellrowborder" valign="top" width="26.062606260626065%" headers="mcps1.2.4.1.1 "><p id="p22931730165530"><a name="p22931730165530"></a><a name="p22931730165530"></a>x-amz-server-side-encryption-aws-kms-key-id</p>
</td>
<td class="cellrowborder" valign="top" width="50.83508350835084%" headers="mcps1.2.4.1.2 "><p id="p45530871165530"><a name="p45530871165530"></a><a name="p45530871165530"></a>Indicates the master key ID. This header is used in SSE-KMS mode. If the customer does not provide the master key, the default master key will be used.</p>
<p id="p7124661165530"><a name="p7124661165530"></a><a name="p7124661165530"></a>Type: string</p>
<p id="p124692385453"><a name="p124692385453"></a><a name="p124692385453"></a>Example: x-amz-server-side-encryption-aws-kms-key-id:arn:aws:kms:sichuan:domainiddomainiddomainiddoma0001:key/4f1cd4de-ab64-4807-920a-47fc42e7f0d0</p>
</td>
<td class="cellrowborder" valign="top" width="23.102310231023104%" headers="mcps1.2.4.1.3 "><p id="p944193310237"><a name="p944193310237"></a><a name="p944193310237"></a><span>No</span></p>
</td>
</tr>
<tr id="row31579001102234"><td class="cellrowborder" valign="top" width="26.062606260626065%" headers="mcps1.2.4.1.1 "><p id="p40004351165530"><a name="p40004351165530"></a><a name="p40004351165530"></a>x-amz-server-side-encryption-customer-algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="50.83508350835084%" headers="mcps1.2.4.1.2 "><p id="p19127016165530"><a name="p19127016165530"></a><a name="p19127016165530"></a>Indicates an encryption algorithm. The header is used in SSE-C mode.</p>
<p id="p37925417165530"><a name="p37925417165530"></a><a name="p37925417165530"></a>Type: string</p>
<p id="p5784433165530"><a name="p5784433165530"></a><a name="p5784433165530"></a>Example: x-amz-server-side-encryption-customer-algorithm:AES256</p>
<p id="p52059897165530"><a name="p52059897165530"></a><a name="p52059897165530"></a>Constraints: This header must be used together with <strong id="b65885890165530"><a name="b65885890165530"></a><a name="b65885890165530"></a>x-amz-server-side-encryption-customer-key</strong>&nbsp;and&nbsp;<strong id="b56102101165530"><a name="b56102101165530"></a><a name="b56102101165530"></a>x-amz-server-side-encryption-customer-key-MD5</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="23.102310231023104%" headers="mcps1.2.4.1.3 "><p id="p5213447810237"><a name="p5213447810237"></a><a name="p5213447810237"></a><span>No. This header is mandatory when customer-provided keys are used.</span></p>
</td>
</tr>
<tr id="row12930993102238"><td class="cellrowborder" valign="top" width="26.062606260626065%" headers="mcps1.2.4.1.1 "><p id="p29134046165530"><a name="p29134046165530"></a><a name="p29134046165530"></a>x-amz-server-side-encryption-customer-key</p>
</td>
<td class="cellrowborder" valign="top" width="50.83508350835084%" headers="mcps1.2.4.1.2 "><p id="p11047545165530"><a name="p11047545165530"></a><a name="p11047545165530"></a>Indicates a key used to encrypt objects. The header is used in SSE-C mode.</p>
<p id="p32319046165530"><a name="p32319046165530"></a><a name="p32319046165530"></a>Type: string</p>
<p id="p22435965165530"><a name="p22435965165530"></a><a name="p22435965165530"></a>Example: x-amz-server-side-encryption-customer-key:K7QkYpBkM5+hcs27fsNkUnNVaobncnLht/rCB2o/9Cw=</p>
<p id="p597093165530"><a name="p597093165530"></a><a name="p597093165530"></a>Constraints: This header is a base64-encoded 256-bit or 512-bit key and must be used together with <strong id="b5373840165530"><a name="b5373840165530"></a><a name="b5373840165530"></a>x-amz-server-side-encryption-customer-algorithm</strong>&nbsp;and&nbsp;<strong id="b48364568165530"><a name="b48364568165530"></a><a name="b48364568165530"></a>x-amz-server-side-encryption-customer-key-MD5</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="23.102310231023104%" headers="mcps1.2.4.1.3 "><p id="p4579914410237"><a name="p4579914410237"></a><a name="p4579914410237"></a><span>No. This header is mandatory when customer-provided keys are used.</span></p>
</td>
</tr>
<tr id="row61346682102242"><td class="cellrowborder" valign="top" width="26.062606260626065%" headers="mcps1.2.4.1.1 "><p id="p25616906165530"><a name="p25616906165530"></a><a name="p25616906165530"></a>x-amz-server-side-encryption-customer-key-MD5</p>
</td>
<td class="cellrowborder" valign="top" width="50.83508350835084%" headers="mcps1.2.4.1.2 "><p id="p61703487165530"><a name="p61703487165530"></a><a name="p61703487165530"></a>Indicates the MD5 value of a key used to encrypt objects. The header is used in SSE-C mode. The MD5 value is used to check whether any error occurs during the transmission of the key.</p>
<p id="p18460477165530"><a name="p18460477165530"></a><a name="p18460477165530"></a>Type: string</p>
<p id="p31926565165530"><a name="p31926565165530"></a><a name="p31926565165530"></a>Example: x-amz-server-side-encryption-customer-key-MD5:4XvB3tbNTN+tIEVa0/fGaQ==</p>
<p id="p18903634165530"><a name="p18903634165530"></a><a name="p18903634165530"></a>Constraints: This header is a base64-encoded 128-bit MD5 value and must be used together with <strong id="b35914979165530"><a name="b35914979165530"></a><a name="b35914979165530"></a>x-amz-server-side-encryption-customer-algorithm</strong>&nbsp;and&nbsp;<strong id="b54799363165530"><a name="b54799363165530"></a><a name="b54799363165530"></a>x-amz-server-side-encryption-customer-key</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="23.102310231023104%" headers="mcps1.2.4.1.3 "><p id="p5512158810237"><a name="p5512158810237"></a><a name="p5512158810237"></a><span>No. This header is mandatory when customer-provided keys are used.</span></p>
</td>
</tr>
</tbody>
</table>

## Response Syntax<a name="section4600155"></a>

```
HTTP/1.1 status_code 
 Server: Server Name 
 x-amz-request-id: request id 
 x-amz-id-2: id 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Content-Type: type 
 Location: location 
 Date: date 
 ETag: etag
```

## Response Headers<a name="section41401397"></a>

This response uses common headers. For details about common response headers, see section  [Common Response Headers](common-response-headers.md). This response also uses one optional header, as described in [Table 3](#table15828906).

**Table  3**  Optional response header

<a name="table15828906"></a>
<table><thead align="left"><tr id="row56780500"><th class="cellrowborder" valign="top" width="43.76%" id="mcps1.2.3.1.1"><p id="p35817813"><a name="p35817813"></a><a name="p35817813"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="56.24%" id="mcps1.2.3.1.2"><p id="p15561779"><a name="p15561779"></a><a name="p15561779"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row52544597"><td class="cellrowborder" valign="top" width="43.76%" headers="mcps1.2.3.1.1 "><p id="p28253988"><a name="p28253988"></a><a name="p28253988"></a>x-amz-version-id</p>
</td>
<td class="cellrowborder" valign="top" width="56.24%" headers="mcps1.2.3.1.2 "><p id="p6871687"><a name="p6871687"></a><a name="p6871687"></a>Indicates the version ID of an object. The version ID of an object will be returned if the bucket housing the object has versioning enabled. A string "<strong id="b61845188"><a name="b61845188"></a><a name="b61845188"></a>null</strong>" will be returned if the bucket housing the object has versioning suspended.</p>
<p id="p19735783"><a name="p19735783"></a><a name="p19735783"></a>Type: String</p>
</td>
</tr>
<tr id="row27094327163230"><td class="cellrowborder" valign="top" width="43.76%" headers="mcps1.2.3.1.1 "><p id="p4888192163315"><a name="p4888192163315"></a><a name="p4888192163315"></a>Access-Control-Allow-Origin</p>
</td>
<td class="cellrowborder" valign="top" width="56.24%" headers="mcps1.2.3.1.2 "><p id="p60399258163315"><a name="p60399258163315"></a><a name="p60399258163315"></a>CORS is configured for buckets. If <strong id="b6722416163315"><a name="b6722416163315"></a><a name="b6722416163315"></a>Origin</strong>&nbsp;in the request meets the CORS configuration requirements,&nbsp;<strong id="b60501749163315"><a name="b60501749163315"></a><a name="b60501749163315"></a>Origin</strong> is included in the response.</p>
<p id="p7644834163315"><a name="p7644834163315"></a><a name="p7644834163315"></a>Type: String</p>
</td>
</tr>
<tr id="row21192939163237"><td class="cellrowborder" valign="top" width="43.76%" headers="mcps1.2.3.1.1 "><p id="p3048844163315"><a name="p3048844163315"></a><a name="p3048844163315"></a>Access-Control-Allow-Headers</p>
</td>
<td class="cellrowborder" valign="top" width="56.24%" headers="mcps1.2.3.1.2 "><p id="p45629849163315"><a name="p45629849163315"></a><a name="p45629849163315"></a>CORS is configured for buckets. If <strong id="b8015460163315"><a name="b8015460163315"></a><a name="b8015460163315"></a>headers</strong>&nbsp;in the request meet the CORS configuration requirements,&nbsp;<strong id="b5030278163315"><a name="b5030278163315"></a><a name="b5030278163315"></a>headers</strong> are included in the response.</p>
<p id="p45272504163315"><a name="p45272504163315"></a><a name="p45272504163315"></a>Type: String</p>
</td>
</tr>
<tr id="row1816317163243"><td class="cellrowborder" valign="top" width="43.76%" headers="mcps1.2.3.1.1 "><p id="p53203489163315"><a name="p53203489163315"></a><a name="p53203489163315"></a>Access-Control-Max-Age</p>
</td>
<td class="cellrowborder" valign="top" width="56.24%" headers="mcps1.2.3.1.2 "><p id="p14515359163315"><a name="p14515359163315"></a><a name="p14515359163315"></a>Indicates <strong id="b63529375163315"><a name="b63529375163315"></a><a name="b63529375163315"></a>MaxAgeSeconds</strong> in the CORS configuration of a server when CORS is configured for buckets.</p>
<p id="p34893470163315"><a name="p34893470163315"></a><a name="p34893470163315"></a>Type: Integer</p>
</td>
</tr>
<tr id="row5613687716333"><td class="cellrowborder" valign="top" width="43.76%" headers="mcps1.2.3.1.1 "><p id="p3080824163315"><a name="p3080824163315"></a><a name="p3080824163315"></a>Access-Control-Allow-Methods</p>
</td>
<td class="cellrowborder" valign="top" width="56.24%" headers="mcps1.2.3.1.2 "><p id="p48220207163315"><a name="p48220207163315"></a><a name="p48220207163315"></a>CORS is configured for buckets. If <strong id="b31328686163315"><a name="b31328686163315"></a><a name="b31328686163315"></a>Access-Control-Request-Method</strong> in the request meets the CORS configuration requirements, methods in the rule are included in the response.</p>
<p id="p13522723163315"><a name="p13522723163315"></a><a name="p13522723163315"></a>Type: String</p>
<p id="p54595647163315"><a name="p54595647163315"></a><a name="p54595647163315"></a>Valid values: <strong id="b21598779163315"><a name="b21598779163315"></a><a name="b21598779163315"></a>GET</strong>,&nbsp;<strong id="b60171288163315"><a name="b60171288163315"></a><a name="b60171288163315"></a>PUT</strong>,&nbsp;<strong id="b4670688163315"><a name="b4670688163315"></a><a name="b4670688163315"></a>HEAD</strong>,&nbsp;<strong id="b42036194163315"><a name="b42036194163315"></a><a name="b42036194163315"></a>POST</strong>, and&nbsp;<strong id="b42781433163315"><a name="b42781433163315"></a><a name="b42781433163315"></a>DELETE</strong></p>
</td>
</tr>
<tr id="row42062386163310"><td class="cellrowborder" valign="top" width="43.76%" headers="mcps1.2.3.1.1 "><p id="p49152104163315"><a name="p49152104163315"></a><a name="p49152104163315"></a>Access-Control-Expose-Headers</p>
</td>
<td class="cellrowborder" valign="top" width="56.24%" headers="mcps1.2.3.1.2 "><p id="p21897459163315"><a name="p21897459163315"></a><a name="p21897459163315"></a>Indicates <strong id="b132551625101114"><a name="b132551625101114"></a><a name="b132551625101114"></a>ExposeHeader</strong> in the CORS configuration of a server when CORS is configured for buckets.</p>
<p id="p28863759163315"><a name="p28863759163315"></a><a name="p28863759163315"></a>Type: String</p>
</td>
</tr>
<tr id="row53465640102323"><td class="cellrowborder" valign="top" width="43.76%" headers="mcps1.2.3.1.1 "><p id="p8517062165713"><a name="p8517062165713"></a><a name="p8517062165713"></a>x-amz-server-side-encryption</p>
</td>
<td class="cellrowborder" valign="top" width="56.24%" headers="mcps1.2.3.1.2 "><p id="p18793394165713"><a name="p18793394165713"></a><a name="p18793394165713"></a>This header is included in a response if SSE-KMS is used.</p>
<p id="p34922825165713"><a name="p34922825165713"></a><a name="p34922825165713"></a>Type: string</p>
<p id="p45869971165713"><a name="p45869971165713"></a><a name="p45869971165713"></a>Example: x-amz-server-side-encryption:aws:kms</p>
</td>
</tr>
<tr id="row50047651102330"><td class="cellrowborder" valign="top" width="43.76%" headers="mcps1.2.3.1.1 "><p id="p18995294165713"><a name="p18995294165713"></a><a name="p18995294165713"></a>x-amz-server-side-encryption-aws-kms-key-id</p>
</td>
<td class="cellrowborder" valign="top" width="56.24%" headers="mcps1.2.3.1.2 "><p id="p62223858165713"><a name="p62223858165713"></a><a name="p62223858165713"></a>Indicates the master key ID. This header is included in a response if SSE-KMS is used.</p>
<p id="p2119104834619"><a name="p2119104834619"></a><a name="p2119104834619"></a>Example: x-amz-server-side-encryption-aws-kms-key-id:arn:aws:kms:sichuan:domainiddomainiddomainiddoma0001:key/4f1cd4de-ab64-4807-920a-47fc42e7f0d0</p>
</td>
</tr>
<tr id="row11281438102334"><td class="cellrowborder" valign="top" width="43.76%" headers="mcps1.2.3.1.1 "><p id="p27512946165713"><a name="p27512946165713"></a><a name="p27512946165713"></a>x-amz-server-side-encryption-customer-algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="56.24%" headers="mcps1.2.3.1.2 "><p id="p13956143165713"><a name="p13956143165713"></a><a name="p13956143165713"></a>Indicates an encryption algorithm. This header is included in a response if SSE-C is used.</p>
<p id="p58496425165713"><a name="p58496425165713"></a><a name="p58496425165713"></a>Type: string</p>
<p id="p56705780165713"><a name="p56705780165713"></a><a name="p56705780165713"></a>Example: x-amz-server-side-encryption-customer-algorithm:AES256</p>
</td>
</tr>
<tr id="row42371356102326"><td class="cellrowborder" valign="top" width="43.76%" headers="mcps1.2.3.1.1 "><p id="p66562751165713"><a name="p66562751165713"></a><a name="p66562751165713"></a>x-amz-server-side-encryption-customer-key-MD5</p>
</td>
<td class="cellrowborder" valign="top" width="56.24%" headers="mcps1.2.3.1.2 "><p id="p22873728165713"><a name="p22873728165713"></a><a name="p22873728165713"></a>Indicates the MD5 value of a key used to encrypt objects. This header is included in a response if SSE-C is used.</p>
<p id="p4536967165713"><a name="p4536967165713"></a><a name="p4536967165713"></a>Type: string</p>
<p id="p40832711165713"><a name="p40832711165713"></a><a name="p40832711165713"></a>Example: x-amz-server-side-encryption-customer-key-MD5:4XvB3tbNTN+tIEVa0/fGaQ==</p>
</td>
</tr>
</tbody>
</table>

## Response Elements<a name="section37068254"></a>

This response involves no elements.

## Error Responses<a name="section65178831"></a>

No special error responses are returned. For details about error responses, see  [Table 1](error-codes.md#table30733758).

## Sample Request<a name="section4443775"></a>

```
POST / HTTP/1.1 
 Date: Fri, 18 Nov 2011 01:19:49 GMT 
 Host: bucketname.obs.example.com
 Content-Type: multipart/form-data; boundary=---------------------------7db143f50da2 
 Content-Length: 2424 


 -----------------------------7db143f50da2 
 Content-Disposition: form-data; name="key" 
 object01 
 -----------------------------7db143f50da2 
 Content-Disposition: form-data; name="acl" 
 public-read 
 -----------------------------7db143f50da2 
 Content-Disposition: form-data; name="content-type" 
 text/plain 
 -----------------------------7db143f50da2 
 Content-Disposition: form-data; name="expires" 
 1000 
 -----------------------------7db143f50da2 
 Content-Disposition: form-data; name="AWSAccessKeyId" 
 14RZT432N80TGDF2Y2G2 
 -----------------------------7db143f50da2 
 Content-Disposition: form-data; name="policy" 
 ewogICJleHBpcmF0aW9uIjogIjIwMTItMDEtMDFUMTI6MDA6MDAuMDAwWiIsCiAgImNvbmRpdGlvbnMiOiBbCiAgICB7ImJ1Y2tldCI6ICJ0Yy5wb3N0LmV4cGlyZXMuMDAxIiB9LAogICAgeyJhY2wiOiAicHVibGljLXJlYWQiIH0sCiAgICB7IkV4cGlyZXMiOiAiMTAwMCIgfSwKICAgIFsiZXEiLCAiJGtleSIsICJvYmplY3QwMSJdLAogICAgWyJzdGFydHMtd2l0aCIsICIkQ29udGVudC1UeXBlIiwgInRleHQvIl0sCiAgXQp9Cg== 
 -----------------------------7db143f50da2 
 Content-Disposition: form-data; name="signature" 
 Vk6rwO0Nq09BLhvNSIYwSJTRQ+k= 
 -----------------------------7db143f50da2 
 Content-Disposition: form-data; name="file"; filename="C:\Testtools\UpLoadFiles\object\1024Bytes.txt" 
 Content-Type: text/plain 
 01234567890 
 -----------------------------7db143f50da2 
 Content-Disposition: form-data; name="submit" 
 Upload 
 -----------------------------7db143f50da2--
```

## Sample Response for Uploading Objects to a Bucket with No Versioning Configured<a name="section39993975"></a>

```
HTTP/1.1 204 No Content 
 Server: OBS 
 x-amz-request-id: 90E2BA00C26C00000133B442A90063FD 
 x-amz-id-2: OTBFMkJBMDBDMjZDMDAwMDAxMzNCNDQyQTkwMDYzRkRBQUFBQUFBQWJiYmJiYmJi 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Content-Type: text/xml 
 Location: http://obs.example.com/tc.post.expires.001/object01
 Date: Fri, 18 Nov 2011 01:20:27 GMT 
 ETag: "ab7abb0da4bca5323ab6119bb5dcd296"
```

## Sample Response for Uploading Objects to a Bucket with Versioning Enabled<a name="section24401462"></a>

```
HTTP/1.1 204 No Content 
 Server: OBS 
 x-amz-request-id: DCD2FC9CAB780000014394C8D18D7A7F 
 x-amz-id-2: ebDwZjh64WVojaUVqPaWaXPqqfqLcp15DNr1KkAkP9EXyWrLsrqQoUs1Xn49VC9h 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Content-Type: text/xml 
 Location: http://192.168.69.11/example/testfile.txt 
 ETag: "098f6bcd4621d373cade4e832627b4f6" 
 x-amz-version-id: AAABQ5TI0anc0vycq3gAAAAyVURTRkha 
 Date: Wed, 15 Jan 2014 07:23:45 GMT
```

## Sample Response for Uploading Objects to a Bucket with Versioning Suspended<a name="section18286572"></a>

```
HTTP/1.1 204 No Content 
 Server: OBS 
 x-amz-request-id: DCD2FC9CAB780000014394F041CA8F94 
 x-amz-id-2: 8EUVTpv5QBvTslQVlaDrzEauRpDP9fusd4IiJrgjExdPlyz+xleFMCNZD/zK0aZg 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Content-Type: text/xml 
 Location: http://192.168.69.11/example/testfile.txt 
 ETag: "cc03e747a6afbbcbf8be7668acfebee5" 
 x-amz-version-id: null 
 Date: Wed, 15 Jan 2014 08:06:50 GMT
```

