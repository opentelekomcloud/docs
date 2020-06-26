# GET Bucket \(List Objects\)<a name="EN-US_TOPIC_0125560237"></a>

After being granted the  **READ**  permission for a bucket, you can use this operation to obtain the list of objects in this bucket.

If you specify only the bucket name in the  **GET Bucket**  request, OBS returns descriptions for some or all objects \(a maximum of 1000 objects\) in the bucket.

If you also specify one or more parameters among  **prefix**,  **marker**,  **max-keys**, and  **delimiter**  in the request, OBS returns a list of objects as specified.  [Table 1](#table14681180)  describes the parameters in this request.

When the number of listed objects exceeds the default upper limit 1000 or the specified  **max-keys**  value, the  **NextMarker**  field is displayed in the response message, indicating the last object to be listed in the request. For subsequent requests, you can set the  **marker**  to the value of  **NextMarker**  returned last time, and list subsequent objects.

## Request Syntax<a name="section14380054"></a>

```
GET /?prefix=p&delimiter=d HTTP/1.1 
 User-Agent: agent
 Host: bucketname.obs.example.com 
 Accept: */*
 Date: date 
 Authorization: authorization
```

## Request Parameters<a name="section62311629"></a>

You can specify parameters in this request to list desired objects in a bucket.  [Table 1](#table14681180)  describes the parameters.

**Table  1**  Request parameters

<a name="table14681180"></a>
<table><thead align="left"><tr id="row12739091"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p25233452"><a name="p25233452"></a><a name="p25233452"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p30643766"><a name="p30643766"></a><a name="p30643766"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p66226009"><a name="p66226009"></a><a name="p66226009"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row62706492"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p46061063"><a name="p46061063"></a><a name="p46061063"></a>prefix</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p39958627"><a name="p39958627"></a><a name="p39958627"></a>Limits the response to object keys that begin with the specified prefix.</p>
<p id="p24083327"><a name="p24083327"></a><a name="p24083327"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p4592438"><a name="p4592438"></a><a name="p4592438"></a>Optional</p>
</td>
</tr>
<tr id="row41331948"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p59553514"><a name="p59553514"></a><a name="p59553514"></a>marker</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p59105304"><a name="p59105304"></a><a name="p59105304"></a>Indicates the object key to start with when listing objects in a bucket. All objects are listed in the dictionary order.</p>
<p id="p62185688"><a name="p62185688"></a><a name="p62185688"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p3875986"><a name="p3875986"></a><a name="p3875986"></a>Optional</p>
</td>
</tr>
<tr id="row34883877"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p7021780"><a name="p7021780"></a><a name="p7021780"></a>max-keys</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p31893332"><a name="p31893332"></a><a name="p31893332"></a>Sets the maximum number of object keys returned in the response body. The value ranges from 1 to 1000. If the value is not in this range, 1000 is returned by default.</p>
<p id="p18604538"><a name="p18604538"></a><a name="p18604538"></a>Type: Integer</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p30572598"><a name="p30572598"></a><a name="p30572598"></a>Optional</p>
</td>
</tr>
<tr id="row6717926"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p7281095"><a name="p7281095"></a><a name="p7281095"></a>delimiter</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p52897817"><a name="p52897817"></a><a name="p52897817"></a>Indicates a character or a sequence of characters used to group object keys.</p>
<p id="p6318307"><a name="p6318307"></a><a name="p6318307"></a>All object keys that contain the same string between the prefix, if specified, and the first occurrence of delimiter after the prefix are grouped under a single result element, <strong id="b56864771"><a name="b56864771"></a><a name="b56864771"></a>CommonPrefixes</strong>.</p>
<p id="p42020897"><a name="p42020897"></a><a name="p42020897"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p48249507"><a name="p48249507"></a><a name="p48249507"></a>Optional</p>
</td>
</tr>
</tbody>
</table>

## Request Headers<a name="section23933749"></a>

This request uses common headers. For details about common request headers, see section  [Common Request Headers](common-request-headers.md).

If you want to obtain CORS configuration information, you must use the headers in  [Table 2](#table26112624).

**Table  2**  Request headers of CORS configuration

<a name="table26112624"></a>
<table><thead align="left"><tr id="row50125655"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p33646287"><a name="p33646287"></a><a name="p33646287"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p40994711"><a name="p40994711"></a><a name="p40994711"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p32237271"><a name="p32237271"></a><a name="p32237271"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row61082168"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p48708577"><a name="p48708577"></a><a name="p48708577"></a>Origin</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p53080699"><a name="p53080699"></a><a name="p53080699"></a>Indicates an origin specified by a pre-request. Generally, it is a domain name.</p>
<p id="p7964250"><a name="p7964250"></a><a name="p7964250"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p41124512"><a name="p41124512"></a><a name="p41124512"></a>Mandatory</p>
</td>
</tr>
<tr id="row34576289"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p49215996"><a name="p49215996"></a><a name="p49215996"></a>Access-Control-Request-Headers</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p27072744"><a name="p27072744"></a><a name="p27072744"></a>Indicates the HTTP headers of a request. The request can use multiple HTTP headers.</p>
<p id="p42328108"><a name="p42328108"></a><a name="p42328108"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p6024691"><a name="p6024691"></a><a name="p6024691"></a>Optional</p>
</td>
</tr>
<tr id="row1674252311610"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p118132513166"><a name="p118132513166"></a><a name="p118132513166"></a>x-amz-security-token</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p41832511161"><a name="p41832511161"></a><a name="p41832511161"></a>Header field used to identify the request of a federated user. When the federal authentication function is enabled, users sending such requests are identified as federated users.</p>
<p id="p818172513166"><a name="p818172513166"></a><a name="p818172513166"></a>Type: string</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p5181725171616"><a name="p5181725171616"></a><a name="p5181725171616"></a>Optional. This parameter must be carried in the request sent by federated users.</p>
</td>
</tr>
</tbody>
</table>

## Request Elements<a name="section14077152"></a>

This request involves no elements.

## Response Syntax<a name="section55470411"></a>

```
HTTP/1.1 status_code 
 Server: Server Name 
 x-amz-request-id: request id 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 x-amz-bucket-region: region name
 x-amz-id-2: id  
 Content-Type: type 
 Date: date
 Content-Length: length 

<Response Body>
```

## Response Headers<a name="section29471659"></a>

This response uses common headers. For details about common response headers, see section  [Common Response Headers](common-response-headers.md).

In addition to common headers, when CORS is configured for buckets, you can use the response headers in  [Table 3](#table881688).

**Table  3**  Appended response headers

<a name="table881688"></a>
<table><thead align="left"><tr id="row53632486"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p49264104"><a name="p49264104"></a><a name="p49264104"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p30969474"><a name="p30969474"></a><a name="p30969474"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row25499485"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p52192417"><a name="p52192417"></a><a name="p52192417"></a>Access-Control-Allow-Origin</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p66836212"><a name="p66836212"></a><a name="p66836212"></a>If <strong id="b64655004"><a name="b64655004"></a><a name="b64655004"></a>Origin</strong>&nbsp;in the request meets the CORS configuration requirements,&nbsp;<strong id="b45024129"><a name="b45024129"></a><a name="b45024129"></a>Origin</strong> is included in the response.</p>
<p id="p2563980"><a name="p2563980"></a><a name="p2563980"></a>Type: String</p>
</td>
</tr>
<tr id="row23075822"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p57202275"><a name="p57202275"></a><a name="p57202275"></a>Access-Control-Allow-Headers</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p2872713"><a name="p2872713"></a><a name="p2872713"></a>CORS is configured for buckets. If <strong id="b25854422"><a name="b25854422"></a><a name="b25854422"></a>headers</strong>&nbsp;in the request meet the CORS configuration requirements,&nbsp;<strong id="b31363207"><a name="b31363207"></a><a name="b31363207"></a>headers</strong> are included in the response.</p>
<p id="p13833415"><a name="p13833415"></a><a name="p13833415"></a>Type: String</p>
</td>
</tr>
<tr id="row57391878"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p18230574"><a name="p18230574"></a><a name="p18230574"></a>Access-Control-Max-Age</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p281510"><a name="p281510"></a><a name="p281510"></a>Indicates <strong id="b2533591"><a name="b2533591"></a><a name="b2533591"></a>MaxAgeSeconds</strong> in the CORS configuration of a server.</p>
<p id="p22802326"><a name="p22802326"></a><a name="p22802326"></a>Type: Integer</p>
</td>
</tr>
<tr id="row3894347"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p47006691"><a name="p47006691"></a><a name="p47006691"></a>Access-Control-Allow-Methods</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p49445640"><a name="p49445640"></a><a name="p49445640"></a>If <strong id="b42357578"><a name="b42357578"></a><a name="b42357578"></a>Access-Control-Request-Method</strong> in the request meets the CORS configuration requirements, methods in the rule are included in the response.</p>
<p id="p45673889"><a name="p45673889"></a><a name="p45673889"></a>Type: String</p>
<p id="p8411821"><a name="p8411821"></a><a name="p8411821"></a>Valid values: <strong id="b8597527"><a name="b8597527"></a><a name="b8597527"></a>GET</strong>,&nbsp;<strong id="b10268880"><a name="b10268880"></a><a name="b10268880"></a>PUT</strong>,&nbsp;<strong id="b25311057"><a name="b25311057"></a><a name="b25311057"></a>HEAD</strong>,&nbsp;<strong id="b26472923"><a name="b26472923"></a><a name="b26472923"></a>POST</strong>, and&nbsp;<strong id="b36929719"><a name="b36929719"></a><a name="b36929719"></a>DELETE</strong></p>
</td>
</tr>
<tr id="row63932023"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p11111371"><a name="p11111371"></a><a name="p11111371"></a>Access-Control-Expose-Headers</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p27605888"><a name="p27605888"></a><a name="p27605888"></a>Indicates <strong id="b1028412284583"><a name="b1028412284583"></a><a name="b1028412284583"></a>ExposeHeader</strong> in the CORS configuration of a server.</p>
<p id="p21484478"><a name="p21484478"></a><a name="p21484478"></a>Type: String</p>
</td>
</tr>
<tr id="row10074419569"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p22811237152020"><a name="p22811237152020"></a><a name="p22811237152020"></a>x-amz-bucket-region</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p84051542131913"><a name="p84051542131913"></a><a name="p84051542131913"></a>Indicates the region of the bucket.</p>
<p id="p184051742181910"><a name="p184051742181910"></a><a name="p184051742181910"></a>Type: String</p>
</td>
</tr>
</tbody>
</table>

## Response Elements<a name="section63918341"></a>

This response contains the XML list of the objects in a bucket.  [Table 4](#table51351348142023)  describes the elements in the XML list.

**Table  4**  Response elements

<a name="table51351348142023"></a>
<table><thead align="left"><tr id="row6230702"><th class="cellrowborder" valign="top" width="30.45%" id="mcps1.2.3.1.1"><p id="p34924842"><a name="p34924842"></a><a name="p34924842"></a>Element</p>
</th>
<th class="cellrowborder" valign="top" width="69.55%" id="mcps1.2.3.1.2"><p id="p10339914"><a name="p10339914"></a><a name="p10339914"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row32226678"><td class="cellrowborder" valign="top" width="30.45%" headers="mcps1.2.3.1.1 "><p id="p60224151"><a name="p60224151"></a><a name="p60224151"></a>ListBucketResult</p>
</td>
<td class="cellrowborder" valign="top" width="69.55%" headers="mcps1.2.3.1.2 "><p id="p46318101"><a name="p46318101"></a><a name="p46318101"></a>A list of objects in a bucket</p>
<p id="p14209730"><a name="p14209730"></a><a name="p14209730"></a>Type: XML</p>
</td>
</tr>
<tr id="row60778711"><td class="cellrowborder" valign="top" width="30.45%" headers="mcps1.2.3.1.1 "><p id="p24128582"><a name="p24128582"></a><a name="p24128582"></a>Contents</p>
</td>
<td class="cellrowborder" valign="top" width="69.55%" headers="mcps1.2.3.1.2 "><p id="p8258121"><a name="p8258121"></a><a name="p8258121"></a>Metadata of the objects</p>
<p id="p7214230"><a name="p7214230"></a><a name="p7214230"></a>Type: XML</p>
<p id="p64928073"><a name="p64928073"></a><a name="p64928073"></a>Parent node: ListBucketResult</p>
</td>
</tr>
<tr id="row47481747"><td class="cellrowborder" valign="top" width="30.45%" headers="mcps1.2.3.1.1 "><p id="p20816280"><a name="p20816280"></a><a name="p20816280"></a>CommonPrefixes</p>
</td>
<td class="cellrowborder" valign="top" width="69.55%" headers="mcps1.2.3.1.2 "><p id="p8397134"><a name="p8397134"></a><a name="p8397134"></a>Grouping information. If you specify a delimiter in the request, the response contains grouping information in <strong id="b8465347"><a name="b8465347"></a><a name="b8465347"></a>CommonPrefixes</strong>.</p>
<p id="p9079260"><a name="p9079260"></a><a name="p9079260"></a>Type: XML</p>
<p id="p14604484"><a name="p14604484"></a><a name="p14604484"></a>Parent node: ListBucketResult</p>
</td>
</tr>
<tr id="row64331499"><td class="cellrowborder" valign="top" width="30.45%" headers="mcps1.2.3.1.1 "><p id="p43468963"><a name="p43468963"></a><a name="p43468963"></a>Delimiter</p>
</td>
<td class="cellrowborder" valign="top" width="69.55%" headers="mcps1.2.3.1.2 "><p id="p31325099"><a name="p31325099"></a><a name="p31325099"></a>The <strong id="b13490436"><a name="b13490436"></a><a name="b13490436"></a>delimiter</strong> parameter specified in a request</p>
<p id="p54305067"><a name="p54305067"></a><a name="p54305067"></a>Type: String</p>
<p id="p18983560"><a name="p18983560"></a><a name="p18983560"></a>Parent node: ListBucketResult</p>
</td>
</tr>
<tr id="row36634316"><td class="cellrowborder" valign="top" width="30.45%" headers="mcps1.2.3.1.1 "><p id="p14589621"><a name="p14589621"></a><a name="p14589621"></a>DisplayName</p>
</td>
<td class="cellrowborder" valign="top" width="69.55%" headers="mcps1.2.3.1.2 "><p id="p40908687"><a name="p40908687"></a><a name="p40908687"></a>Name of an object owner</p>
<p id="p32633870"><a name="p32633870"></a><a name="p32633870"></a>Type: String</p>
<p id="p25269378"><a name="p25269378"></a><a name="p25269378"></a>Parent node: ListBucketResult.Contents.Owner</p>
</td>
</tr>
<tr id="row26097812"><td class="cellrowborder" valign="top" width="30.45%" headers="mcps1.2.3.1.1 "><p id="p33547998"><a name="p33547998"></a><a name="p33547998"></a>ETag</p>
</td>
<td class="cellrowborder" valign="top" width="69.55%" headers="mcps1.2.3.1.2 "><p id="p12714465165016"><a name="p12714465165016"></a><a name="p12714465165016"></a>The MD5 value of an object. (If an object is encrypted using server-side encryption, the ETag value is not the MD5 value of the object.)</p>
<p id="p28864252"><a name="p28864252"></a><a name="p28864252"></a>Type: String</p>
<p id="p58451680"><a name="p58451680"></a><a name="p58451680"></a>Parent node: ListBucketResult.Contents</p>
</td>
</tr>
<tr id="row56303072"><td class="cellrowborder" valign="top" width="30.45%" headers="mcps1.2.3.1.1 "><p id="p64255013"><a name="p64255013"></a><a name="p64255013"></a>ID</p>
</td>
<td class="cellrowborder" valign="top" width="69.55%" headers="mcps1.2.3.1.2 "><p id="p37273587"><a name="p37273587"></a><a name="p37273587"></a>DomainId of an object owner</p>
<p id="p67026828"><a name="p67026828"></a><a name="p67026828"></a>Type: String</p>
<p id="p66370545"><a name="p66370545"></a><a name="p66370545"></a>Parent node: ListBucketResult.Contents.Owner</p>
</td>
</tr>
<tr id="row60463993"><td class="cellrowborder" valign="top" width="30.45%" headers="mcps1.2.3.1.1 "><p id="p65745283"><a name="p65745283"></a><a name="p65745283"></a>IsTruncated</p>
</td>
<td class="cellrowborder" valign="top" width="69.55%" headers="mcps1.2.3.1.2 "><p id="p23767697"><a name="p23767697"></a><a name="p23767697"></a>Determines whether the returned list is truncated. <strong id="b12582685"><a name="b12582685"></a><a name="b12582685"></a>true</strong>&nbsp;indicates that the result is incomplete while&nbsp;<strong id="b46135308"><a name="b46135308"></a><a name="b46135308"></a>false</strong> indicates that the result is complete.</p>
<p id="p12564589"><a name="p12564589"></a><a name="p12564589"></a>Type: Boolean</p>
<p id="p45972443"><a name="p45972443"></a><a name="p45972443"></a>Parent node: ListBucketResult</p>
</td>
</tr>
<tr id="row11098806"><td class="cellrowborder" valign="top" width="30.45%" headers="mcps1.2.3.1.1 "><p id="p26588063"><a name="p26588063"></a><a name="p26588063"></a>Key</p>
</td>
<td class="cellrowborder" valign="top" width="69.55%" headers="mcps1.2.3.1.2 "><p id="p6149456"><a name="p6149456"></a><a name="p6149456"></a>Name of an object</p>
<p id="p55345107"><a name="p55345107"></a><a name="p55345107"></a>Type: String</p>
<p id="p28343922"><a name="p28343922"></a><a name="p28343922"></a>Parent node: ListBucketResult.Contents</p>
</td>
</tr>
<tr id="row53768708"><td class="cellrowborder" valign="top" width="30.45%" headers="mcps1.2.3.1.1 "><p id="p60298130"><a name="p60298130"></a><a name="p60298130"></a>LastModified</p>
</td>
<td class="cellrowborder" valign="top" width="69.55%" headers="mcps1.2.3.1.2 "><p id="p52310372"><a name="p52310372"></a><a name="p52310372"></a>Date and time when the last modification was made to an object</p>
<p id="p1031307"><a name="p1031307"></a><a name="p1031307"></a>Type: Date</p>
<p id="p9281763"><a name="p9281763"></a><a name="p9281763"></a>Parent node: ListBucketResult.Contents</p>
</td>
</tr>
<tr id="row16427006"><td class="cellrowborder" valign="top" width="30.45%" headers="mcps1.2.3.1.1 "><p id="p55519147"><a name="p55519147"></a><a name="p55519147"></a>Marker</p>
</td>
<td class="cellrowborder" valign="top" width="69.55%" headers="mcps1.2.3.1.2 "><p id="p757048"><a name="p757048"></a><a name="p757048"></a>Start point for listing objects</p>
<p id="p6813434"><a name="p6813434"></a><a name="p6813434"></a>Type: String</p>
<p id="p61320909"><a name="p61320909"></a><a name="p61320909"></a>Parent node: ListBucketResult</p>
</td>
</tr>
<tr id="row15017275"><td class="cellrowborder" valign="top" width="30.45%" headers="mcps1.2.3.1.1 "><p id="p8439728"><a name="p8439728"></a><a name="p8439728"></a>NextMarker</p>
</td>
<td class="cellrowborder" valign="top" width="69.55%" headers="mcps1.2.3.1.2 "><p id="p12529345"><a name="p12529345"></a><a name="p12529345"></a>A marker for the last returned object in the list. <strong id="b45655248"><a name="b45655248"></a><a name="b45655248"></a>NextMarker</strong>&nbsp;is returned when not all the objects are listed. You can set the&nbsp;<strong id="b8244056"><a name="b8244056"></a><a name="b8244056"></a>Marker</strong> value to list the remaining objects in follow-up requests.</p>
<p id="p7087640"><a name="p7087640"></a><a name="p7087640"></a>Type: String</p>
<p id="p63788762"><a name="p63788762"></a><a name="p63788762"></a>Parent node: ListBucketResult</p>
</td>
</tr>
<tr id="row37227952"><td class="cellrowborder" valign="top" width="30.45%" headers="mcps1.2.3.1.1 "><p id="p62674112"><a name="p62674112"></a><a name="p62674112"></a>MaxKeys</p>
</td>
<td class="cellrowborder" valign="top" width="69.55%" headers="mcps1.2.3.1.2 "><p id="p43438321"><a name="p43438321"></a><a name="p43438321"></a>The maximum objects returned.</p>
<p id="p55400573"><a name="p55400573"></a><a name="p55400573"></a>Type: String</p>
<p id="p28843114"><a name="p28843114"></a><a name="p28843114"></a>Parent node: ListBucketResult</p>
</td>
</tr>
<tr id="row58261442"><td class="cellrowborder" valign="top" width="30.45%" headers="mcps1.2.3.1.1 "><p id="p21556347"><a name="p21556347"></a><a name="p21556347"></a>Name</p>
</td>
<td class="cellrowborder" valign="top" width="69.55%" headers="mcps1.2.3.1.2 "><p id="p1233681"><a name="p1233681"></a><a name="p1233681"></a>Name of the requested bucket</p>
<p id="p11103130"><a name="p11103130"></a><a name="p11103130"></a>Type: String</p>
<p id="p32819307"><a name="p32819307"></a><a name="p32819307"></a>Parent node: ListBucketResult</p>
</td>
</tr>
<tr id="row26938309"><td class="cellrowborder" valign="top" width="30.45%" headers="mcps1.2.3.1.1 "><p id="p34519425"><a name="p34519425"></a><a name="p34519425"></a>Owner</p>
</td>
<td class="cellrowborder" valign="top" width="69.55%" headers="mcps1.2.3.1.2 "><p id="p44610037"><a name="p44610037"></a><a name="p44610037"></a>User information, including the DomainId and name</p>
<p id="p65946020"><a name="p65946020"></a><a name="p65946020"></a>Type: XML</p>
<p id="p56643274"><a name="p56643274"></a><a name="p56643274"></a>Parent node: ListBucketResult.Contents</p>
</td>
</tr>
<tr id="row40027424"><td class="cellrowborder" valign="top" width="30.45%" headers="mcps1.2.3.1.1 "><p id="p20995945"><a name="p20995945"></a><a name="p20995945"></a>Prefix</p>
</td>
<td class="cellrowborder" valign="top" width="69.55%" headers="mcps1.2.3.1.2 "><p id="p22949990"><a name="p22949990"></a><a name="p22949990"></a>Prefix of an object key. Only objects whose keys have this prefix are listed.</p>
<p id="p5223324"><a name="p5223324"></a><a name="p5223324"></a>Type: String</p>
<p id="p47009920"><a name="p47009920"></a><a name="p47009920"></a>Parent node: ListBucketResult</p>
</td>
</tr>
<tr id="row20436099"><td class="cellrowborder" valign="top" width="30.45%" headers="mcps1.2.3.1.1 "><p id="p44711314"><a name="p44711314"></a><a name="p44711314"></a>Size</p>
</td>
<td class="cellrowborder" valign="top" width="69.55%" headers="mcps1.2.3.1.2 "><p id="p64846706"><a name="p64846706"></a><a name="p64846706"></a>Number of bytes of an object</p>
<p id="p46749448"><a name="p46749448"></a><a name="p46749448"></a>Type: String</p>
<p id="p18091851"><a name="p18091851"></a><a name="p18091851"></a>Parent node: ListBucketResult.Contents</p>
</td>
</tr>
<tr id="row28608932"><td class="cellrowborder" valign="top" width="30.45%" headers="mcps1.2.3.1.1 "><p id="p35622116"><a name="p35622116"></a><a name="p35622116"></a>StorageClass</p>
</td>
<td class="cellrowborder" valign="top" width="69.55%" headers="mcps1.2.3.1.2 "><p id="p66819120"><a name="p66819120"></a><a name="p66819120"></a>Storage class of an object</p>
<p id="p64501175"><a name="p64501175"></a><a name="p64501175"></a>Type: String</p>
<p id="p383909911665"><a name="p383909911665"></a><a name="p383909911665"></a>Values: STANDARD | STANDARD_IA |GLACIER</p>
<p id="p57212673"><a name="p57212673"></a><a name="p57212673"></a>Parent node: ListBucketResult.Contents</p>
</td>
</tr>
</tbody>
</table>

## Error Responses<a name="section38394164"></a>

No special error responses are returned. For details about error responses, see  [Table 1](error-codes.md#table30733758).

## Sample Request<a name="section14854840"></a>

```
GET / HTTP/1.1
 User-Agent: Jakarta Commons-HttpClient/3.1 
 Host: bucketname.obs.example.com
 Accept: */*
 Date: Sun, 26 Sep 2010 09:16:00 GMT  
 Authorization: AWS 04RZT432N80TGDF2Y2G2:QaTwEcRs5E4p/uahBMYHB+dY00k= 
```

## Sample Response<a name="section66584700"></a>

```
HTTP/1.1 200 OK 
 Server: OBS 
 x-amz-request-id: 367CB63A2F283044981285492719060 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 x-amz-bucket-region: R1
 x-amz-id-2: MzY3Q0I2M0EyRjI4MzA0NDk4MTI4NTQ5MjcxOTA2MEFBQUFBQUFBYmJiYmJiYmJD 
 Content-Type: application/xml 
 Date: Sun, 26 Sep 2010 09:18:36 GMT 
 Content-Length: 560 

 <?xml version="1.0" encoding="UTF-8" standalone="yes"?> 
 <ListBucketResult xmlns="http://obs.example.com/doc/2015-06-30/"> 
 <Name>example</Name> 
 <Prefix></Prefix> 
 <Marker></Marker> 
 <MaxKeys>1000</MaxKeys> 
 <IsTruncated>false</IsTruncated> 
 <Contents> 
 <Key>test</Key> 
 <LastModified>2013-01-15T05:52:15.920Z</LastModified> 
 <ETag>0f64741bf7cb1089e988e4585d0d3434</ETag> 
 <Size>11</Size> 
 <Owner> 
 <ID>bcaf1ffd86f41caff1a493dc2ad8c2c281e37522a640e161ca5fb16fd081034f</ID> 
 <DisplayName>apple</DisplayName> 
 </Owner> 
 <StorageClass>STANDARD</StorageClass> 
 </Contents> 
 </ListBucketResult>
```

## Sample Request \(Example of listing objects in a bucket by specifying prefix\)<a name="section24651644"></a>

```
GET /?prefix=photos/2006/&delimiter=/ HTTP/1.1 
 User-Agent: Jakarta Commons-HttpClient/3.1 
 Host: bucketname.obs.example.com
 Accept: */*
 Date: Sun, 26 Sep 2010 09:18:36 GMT 
 Authorization: AWS 04RZT432N80TGDF2Y2G2:QaTwEcRs5E4p/uahBMYHB+dY00k= 
```

## Sample Response \(Example of listing objects in a bucket by specifying prefix\)<a name="section20538210"></a>

```
HTTP/1.1 200 OK 
 Server: OBS 
 x-amz-request-id: 367CB63A2F283044981285492719060 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 x-amz-bucket-region: R1
 x-amz-id-2: MzY3Q0I2M0EyRjI4MzA0NDk4MTI4NTQ5MjcxOTA2MEFBQUFBQUFBYmJiYmJiYmJD 
 Content-Type: application/xml 
 Date: Sun, 26 Sep 2010 09:18:36 GMT 
 Content-Length: 560 

 <?xml version="1.0" encoding="UTF-8" standalone="yes"?> 
 <ListBucketResult xmlns="http://obs.example.com/doc/2015-06-30/"> 
 <Name>example</Name> 
 <Prefix>photos/2006/</Prefix> 
 <Marker></Marker> 
 <MaxKeys>1000</MaxKeys> 
 <Delimiter>/</Delimiter> 
 <IsTruncated>false</IsTruncated> 
 <Contents> 
 <Key>photos/2006/index.html</Key> 
 <LastModified>2009-01-01T12:00:00.000Z</LastModified> 
 <ETag>ce1acdafcc879d7eee54cf4e97334078</ETag> 
 <Size>1234</Size> 
 <Owner> 
 <ID>214153b66967d86f031c7487b4566cb1b</ID> 
 <DisplayName>John Smith</DisplayName> 
 </Owner> 
 <StorageClass>STANDARD</StorageClass> 
 </Contents> 
 <CommonPrefixes> 
 <Prefix>photos/2006/January/</Prefix> 
 </CommonPrefixes> 
 </ListBucketResult>
```

## Sample Request \(list of objects in a bucket and the CORS configuration being obtained with CORS configured for the bucket\)<a name="section231362422611"></a>

```
GET / HTTP/1.1
User-Agent: curl/7.19.0 (x86_64-suse-linux-gnu) libcurl/7.19.0 OpenSSL/0.9.8{ zlib/1.2.3 libidn/1.10
Host: bucketname.obs.example.com
Accept: */*
Date: Tue, 28 Apr 2015 13:52:29 +0000
Authorization: AWS D13E0C94E722DD69423C:m/jxIj4ZYv4mjpk4xqlMTQKe7aQ=
Origin:www.example.com
Access-Control-Request-Headers:AllowedHeader_1
```

## Sample Response \(list of objects in a bucket and the CORS configuration being obtained with CORS configured for the bucket\)<a name="section9366232142615"></a>

```
HTTP/1.1 200 OK
Server: OBS
x-amz-request-id: B50AD92B37C934BAD314B5EB0BB5BEF2
x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc
Access-Control-Allow-Origin: www.example.com
Access-Control-Allow-Methods: POST,GET,HEAD,PUT,DELETE
Access-Control-Allow-Headers: AllowedHeader_1
Access-Control-Max-Age: 100
Access-Control-Expose-Headers: ExposeHeader_1
x-amz-id-2: 1jSuajz0BqBC0sly+aYIIpbK4ETxBVeCYtBq3Lvc7H7zuCefvq9Kowtp0o3cmQ3X
Content-Type: application/xml
Date: Tue, 28 Apr 2015 13:52:29 GMT
Content-Length: 559
```

