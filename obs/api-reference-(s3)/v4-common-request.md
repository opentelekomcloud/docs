# V4 Common Request<a name="EN-US_TOPIC_0125560310"></a>

A V4 common request is in the following format:

```
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20150524/region-1/s3/aws4_request,SignedHeaders=host;range;x-amz-date,Signature=fe5f80f77d5fa3beca038a248ff027d0445342fe2855ddc963176630326f1024
```

**Table  1**  Request parameters

<a name="table43294633102033"></a>
<table><thead align="left"><tr id="row55880548102033"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p25411224102033"><a name="p25411224102033"></a><a name="p25411224102033"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p57838005102033"><a name="p57838005102033"></a><a name="p57838005102033"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row54829987102033"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p64118729102033"><a name="p64118729102033"></a><a name="p64118729102033"></a>Authorization</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p37484048102033"><a name="p37484048102033"></a><a name="p37484048102033"></a>Indicates signature information.</p>
</td>
</tr>
<tr id="row51980971102033"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p48314813102033"><a name="p48314813102033"></a><a name="p48314813102033"></a>AWS4-HMAC-SHA256</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p40040420102033"><a name="p40040420102033"></a><a name="p40040420102033"></a>Indicates the hash algorithm used by signatures. It is a fixed value.</p>
</td>
</tr>
<tr id="row37269559102033"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p34353168102033"><a name="p34353168102033"></a><a name="p34353168102033"></a>Credential=AKIAIOSFODNN7EXAMPLE/20150524/region-1/s3/aws4_request</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p62160145102033"><a name="p62160145102033"></a><a name="p62160145102033"></a>Indicates the AK and Signing Key information used to calculate the signature.</p>
<p id="p41396708102033"><a name="p41396708102033"></a><a name="p41396708102033"></a>AKIAIOSFODNN7EXAMPLE: AK of the user that sends a request.</p>
<p id="p2060834102033"><a name="p2060834102033"></a><a name="p2060834102033"></a>20150524: start time for calculating the Signing Key. After 7 days, the signature that is calculated by using the Signing Key is invalid. The definition of Signing Key is in the later part of the document.</p>
<p id="p16223213102033"><a name="p16223213102033"></a><a name="p16223213102033"></a>region-1: Indicates the region information about the request.</p>
<p id="p43443884102033"><a name="p43443884102033"></a><a name="p43443884102033"></a>s3: Indicates the service that is required.</p>
<p id="p17286994102033"><a name="p17286994102033"></a><a name="p17286994102033"></a>aws4_request: Indicates a fixed value.</p>
</td>
</tr>
<tr id="row53991063102033"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p22678090102033"><a name="p22678090102033"></a><a name="p22678090102033"></a>SignedHeaders=host;range;x-amz-date</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p55590574102033"><a name="p55590574102033"></a><a name="p55590574102033"></a>SignedHeaders: Indicates the HTTP request headers that are used for signature calculation.</p>
<div class="warning" id="note40851336215637"><a name="note40851336215637"></a><a name="note40851336215637"></a><span class="warningtitle"> WARNING: </span><div class="warningbody"><p id="p32117706215637"><a name="p32117706215637"></a><a name="p32117706215637"></a>If headers contain <em id="i16456172512295"><a name="i16456172512295"></a><a name="i16456172512295"></a>gzip</em>,&nbsp;<em id="i1456625202918"><a name="i1456625202918"></a><a name="i1456625202918"></a>no-cache</em>,&nbsp;<em id="i104564256299"><a name="i104564256299"></a><a name="i104564256299"></a>chunked</em>,&nbsp;<em id="i5456172512293"><a name="i5456172512293"></a><a name="i5456172512293"></a>identity</em>,&nbsp;<em id="i1945662552919"><a name="i1945662552919"></a><a name="i1945662552919"></a>keep-alive</em>,&nbsp;<em id="i10456182513298"><a name="i10456182513298"></a><a name="i10456182513298"></a>bytes</em>, and&nbsp;<em id="i17456122542917"><a name="i17456122542917"></a><a name="i17456122542917"></a>close</em>, please use lowercase letters. Otherwise, you will receive a&nbsp;<strong id="b17456825172916"><a name="b17456825172916"></a><a name="b17456825172916"></a>SignatureDoesNotMatch</strong> error response.</p>
</div></div>
</td>
</tr>
<tr id="row43439015102033"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p28040332102033"><a name="p28040332102033"></a><a name="p28040332102033"></a>Signature=fe5f80f77d5fa3beca038a248ff027d0445342fe2855ddc963176630326f1024</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p42600130102033"><a name="p42600130102033"></a><a name="p42600130102033"></a>The signature value of this request is <strong id="b22801750102033"><a name="b22801750102033"></a><a name="b22801750102033"></a>fe5f80f77d5fa3beca038a248ff027d0445342fe2855ddc963176630326f1024</strong>.</p>
</td>
</tr>
</tbody>
</table>

[Figure 1](#fig15907824205112)  shows the signature computing process in V4 authentication mode.

**Figure  1**  Signature calculation process in V4 authentication mode<a name="fig15907824205112"></a>  
![](figures/signature-calculation-process-in-v4-authentication-mode.png "signature-calculation-process-in-v4-authentication-mode")

The signature computing process in V4 authentication mode is detailed in the following steps:

1.  Generate StringToSign.

    StringToSign of a common V4 request is in the following format:

    ```
    "AWS4-HMAC-SHA256" + \n" + TimeStampISO8601Format + "\n" + <Scope> + "\n" +Hex(SHA256Hash(<CanonicalRequest>))
    ```

    Example:

    ```
    AWS4-HMAC-SHA256 20150524T000000Z 20150524/region-1/s3/aws4_request 9e0e90d9c76de8fa5b200d8c849cd5b8dc7a3be3951ddb7f6a76b4158342019d
    ```

    [Table 2](#table63418753102033)  lists parameters of Canonical Request.

    **Table  2**  Parameters of Canonical Request

    <a name="table63418753102033"></a>
    <table><thead align="left"><tr id="row48420225102033"><th class="cellrowborder" valign="top" width="50.51%" id="mcps1.2.3.1.1"><p id="p64907308102033"><a name="p64907308102033"></a><a name="p64907308102033"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="49.49%" id="mcps1.2.3.1.2"><p id="p11964273102033"><a name="p11964273102033"></a><a name="p11964273102033"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4190517102033"><td class="cellrowborder" valign="top" width="50.51%" headers="mcps1.2.3.1.1 "><p id="p51126242102033"><a name="p51126242102033"></a><a name="p51126242102033"></a>HTTP Method</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.49%" headers="mcps1.2.3.1.2 "><p id="p56869472102033"><a name="p56869472102033"></a><a name="p56869472102033"></a>Indicates the HTTP request method such as GET, PUT, or POST.</p>
    </td>
    </tr>
    <tr id="row57830793102033"><td class="cellrowborder" valign="top" width="50.51%" headers="mcps1.2.3.1.1 "><p id="p16392826102033"><a name="p16392826102033"></a><a name="p16392826102033"></a>Canonical URI</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.49%" headers="mcps1.2.3.1.2 "><p id="p48740272102033"><a name="p48740272102033"></a><a name="p48740272102033"></a>Indicates the absolute path of the URI. It starts with the "/" special character. Example:</p>
    <p id="p5955131114725"><a name="p5955131114725"></a><a name="p5955131114725"></a>The absolute path of http://bucketname.obs.example.com/myphoto.jpg is /bucketname/myphoto.jpg.</p>
    </td>
    </tr>
    <tr id="row57436700102033"><td class="cellrowborder" valign="top" width="50.51%" headers="mcps1.2.3.1.1 "><p id="p63755460102033"><a name="p63755460102033"></a><a name="p63755460102033"></a>CanonicalQueryString</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.49%" headers="mcps1.2.3.1.2 "><p id="p47778605102033"><a name="p47778605102033"></a><a name="p47778605102033"></a>Indicates that name and values are encoded using URI-encode and sorted in the dictionary order.</p>
    <p id="p65286101102033"><a name="p65286101102033"></a><a name="p65286101102033"></a>Example:</p>
    <p id="p5159867811487"><a name="p5159867811487"></a><a name="p5159867811487"></a>CanonicalQueryString of http://bucketname.obs.example.com/?prefix=somePrefix&amp;marker=someMarker&amp;max-keys=20 is as follows:</p>
    <p id="p53578079102033"><a name="p53578079102033"></a><a name="p53578079102033"></a>URI-encode("marker")+"="+URI-encode("someMarker")+"&amp;"+URI-encode("max-keys")+"="+URI-encode("20")+"&amp;"+URI-encode("prefix")+"="+URI-encode("somePrefix")</p>
    <p id="p18885714102033"><a name="p18885714102033"></a><a name="p18885714102033"></a>If a parameter of the querystring request does not have a value, enter the value in the "" format. The following is an example:</p>
    <p id="p31592912114847"><a name="p31592912114847"></a><a name="p31592912114847"></a>CanonicalQueryString of http://bucketname.obs.example.com/?acl is as follows:</p>
    <p id="p45784519102033"><a name="p45784519102033"></a><a name="p45784519102033"></a>URI-encode("acl") + "=" + ""</p>
    </td>
    </tr>
    <tr id="row53935604102033"><td class="cellrowborder" valign="top" width="50.51%" headers="mcps1.2.3.1.1 "><p id="p62681399102033"><a name="p62681399102033"></a><a name="p62681399102033"></a>Canonical Headers</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.49%" headers="mcps1.2.3.1.2 "><p id="p28363307102033"><a name="p28363307102033"></a><a name="p28363307102033"></a>Indicates the request header list. The name and value of each header are connected using a colon (:). Headers are separated by <strong id="b57255522102033"><a name="b57255522102033"></a><a name="b57255522102033"></a>\n</strong>. The name of a header must use lowercase letters. The list is sorted in the dictionary order.</p>
    <p id="p18903607102033"><a name="p18903607102033"></a><a name="p18903607102033"></a>Canonical Headers are constructed using the value of SignedHeaders=date;host;x-amz-content-sha256;x-amz-date;x-amz-storage-class in the <strong id="b37786074102033"><a name="b37786074102033"></a><a name="b37786074102033"></a>Authentication</strong> field of the HTTP header. In this example, the server uses date, host, x-amz-content-sha256, x-amz-date, and xamz-storage-class to calculate signatures. OBS must extract the five fields from the HTTP header to calculate signatures.</p>
    <p id="p11620650125446"><a name="p11620650125446"></a><a name="p11620650125446"></a>Host: bucketname..obs.example.com</p>
    <p id="p35398262102033"><a name="p35398262102033"></a><a name="p35398262102033"></a>Date: Fri, 24 May 2015 00:00:00 GMT</p>
    <p id="p33936313102033"><a name="p33936313102033"></a><a name="p33936313102033"></a>x-amz-content-sha256: 44ce7dd67c959e0d3524ffac1771dfbba87d2b6b4b4e99e42034a8b803f8b072</p>
    <p id="p61431774102033"><a name="p61431774102033"></a><a name="p61431774102033"></a>x-amz-date: 20150524T000000Z</p>
    <p id="p55334527102033"><a name="p55334527102033"></a><a name="p55334527102033"></a>x-amz-storage-class: STANDARD</p>
    </td>
    </tr>
    <tr id="row12888635102033"><td class="cellrowborder" valign="top" width="50.51%" headers="mcps1.2.3.1.1 "><p id="p31171124102033"><a name="p31171124102033"></a><a name="p31171124102033"></a>SignedHeaders</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.49%" headers="mcps1.2.3.1.2 "><p id="p16486642102033"><a name="p16486642102033"></a><a name="p16486642102033"></a>Indicates the name that can be used to calculate signature headers. The names are sorted in the dictionary order. Fields are separated from each other by a semicolon (;).</p>
    <p id="p62674243102033"><a name="p62674243102033"></a><a name="p62674243102033"></a>Example:</p>
    <p id="p11816989102033"><a name="p11816989102033"></a><a name="p11816989102033"></a>date;host;x-amz-content-sha256;x-amz-date;x-amz-storage-class</p>
    </td>
    </tr>
    <tr id="row57333850102033"><td class="cellrowborder" valign="top" width="50.51%" headers="mcps1.2.3.1.1 "><p id="p52541386102033"><a name="p52541386102033"></a><a name="p52541386102033"></a>Hashed Payload</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.49%" headers="mcps1.2.3.1.2 "><p id="p14869883102033"><a name="p14869883102033"></a><a name="p14869883102033"></a>Indicates the SHA256 hash value of the data that is uploaded.</p>
    </td>
    </tr>
    </tbody>
    </table>

    The following is a Canonical Request example.

    ```
    PUT /test%24file.text date:Fri, 24 May 2015 00:00:00 GMT 
    host:bucketname.obs.example.com
    x-amz-content-sha256:44ce7dd67c959e0d3524ffac1771dfbba87d2b6b4b4e99e42034a8b803f8b072 x-amz-date:20150524T000000Z x-amz-storage-class:STANDARD date;host;x-amz-content-sha256;x-amz-date;x-amz-storage-class 44ce7dd67c959e0d3524ffac1771dfbba87d2b6b4b4e99e42034a8b803f8b072
    ```

2.  Generate SigningKey.

    SigningKey is calculated as follows:

    ```
    DateKey = HMAC-SHA256("AWS4"+"<SecretAccessKey>", "<yyyymmdd>") 
    DateRegionKey = HMAC-SHA256(<DateKey>, "<aws-region>") 
    DateRegionServiceKey = HMAC-SHA256(<DateRegionKey>, "<aws-service>") 
    SigningKey = HMAC-SHA256(<DateRegionServiceKey>, "aws4_request"
    ```

    Each field is described as follows:

    -   **<SecretAccessKey\>**: Indicates the SK of the requester.

    -   _<yyyymmdd\>_: Indicates the period in which Signing Key obtained from Authorization in the HTTP header is valid.

    -   **<aws-region\>**: Indicates the region of the request.

    -   **<aws-service\>**: Indicates the service type of the request.

3.  Use StringToSign and SigningKey to calculate the signature.

```
HMAC-SHA256(SigningKey, StringToSign)
```

After the HMAC-SHA256 algorithm is used to calculate the signature, convert the signature into a hexadecimal code to get the ultimate signature.

The common request authentication involves a special authentication method known as chunked uploading authentication. You can use this method when authenticating objects uploaded in a chunked manner.

Chunked uploading indicates that the data flows are composed of data blocks. Each data block is called a chunk. Each chunk consists of chunk metadata and chunk data. Chunk metadata includes the size and signature of the current chunk data. The chunk format is as follows:

```
chunk-size + ";chunk-signature=" + signature + \r\n + chunk-data + \r\n
```

[Figure 2](#fig727315155523)  shows the signature computing process of each chunk.

**Figure  2**  Signature calculation process of each chunk<a name="fig727315155523"></a>  
![](figures/signature-calculation-process-of-each-chunk.png "signature-calculation-process-of-each-chunk")

Chunk signature calculation is an iterative process. The signature of each chunk is calculated based on the previous chunk signature. For the first chunk, its previous chunk signature is the seed signature in the header.

After OBS receives the object uploading request, OBS verifies the signature in the request header and then verifies the signature of each chunk when user data is uploaded. Objects are uploaded successfully only after the header signature and each chunk signature are verified.

