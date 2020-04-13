# V2 Common Request<a name="EN-US_TOPIC_0125560243"></a>

A common HTTP/HTTPS request is authenticated by its  **Authorization** header. The following is the format of the  **Authorization**  header:

```
Authorization: AWS AccessKeyID:signature
```

To generate the signature, perform the following steps:

1.  Construct  **StringToSign**  using request parameters.

    ```
    StringToSign = HTTP-Verb + "\n" + Content-MD5 + "\n" + Content-Type + "\n" + Date + "\n" + CanonicalizedOBSHeaders + CanonicalizedResource
    ```

    [Table 1](#table41134075)  describes the parameters of a request.

    **Table  1**  Request parameters

    <a name="table41134075"></a>
    <table><thead align="left"><tr id="row19019073"><th class="cellrowborder" valign="top" width="35.9%" id="mcps1.2.3.1.1"><p id="p64149930"><a name="p64149930"></a><a name="p64149930"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="64.1%" id="mcps1.2.3.1.2"><p id="p28761840"><a name="p28761840"></a><a name="p28761840"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row48007674"><td class="cellrowborder" valign="top" width="35.9%" headers="mcps1.2.3.1.1 "><p id="p63416368"><a name="p63416368"></a><a name="p63416368"></a>HTTP-Verb</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.1%" headers="mcps1.2.3.1.2 "><p id="p36452220"><a name="p36452220"></a><a name="p36452220"></a>Indicates an HTTP request method supported by OBS REST API. The value can be an HTTP verb such as PUT, GET, or DELETE.</p>
    </td>
    </tr>
    <tr id="row59634524"><td class="cellrowborder" valign="top" width="35.9%" headers="mcps1.2.3.1.1 "><p id="p65667169"><a name="p65667169"></a><a name="p65667169"></a>Date</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.1%" headers="mcps1.2.3.1.2 "><p id="p17440495"><a name="p17440495"></a><a name="p17440495"></a>Indicates the time when the request is initiated. The value must be in RFC 1123 format. This parameter is an empty string when the <strong id="b22746728"><a name="b22746728"></a><a name="b22746728"></a>x-amz-date</strong>&nbsp;is specified. For details, see&nbsp;<a href="#table25172842">Table 3</a>.</p>
    <p id="p30545685"><a name="p30545685"></a><a name="p30545685"></a>This parameter can be omitted if the request is for a temporarily authorized operation.</p>
    </td>
    </tr>
    <tr id="row6475715"><td class="cellrowborder" valign="top" width="35.9%" headers="mcps1.2.3.1.1 "><p id="p54770906"><a name="p54770906"></a><a name="p54770906"></a>Content-Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.1%" headers="mcps1.2.3.1.2 "><p id="p7258393"><a name="p7258393"></a><a name="p7258393"></a>Indicates the content type and is used for specifying the request content type, for example, <strong id="b65325544"><a name="b65325544"></a><a name="b65325544"></a>text/plain</strong>.</p>
    <p id="p55733946154843"><a name="p55733946154843"></a><a name="p55733946154843"></a>This parameter is an empty string when the request does not contain the header. See <a href="#table54992765">Table 2</a>.</p>
    </td>
    </tr>
    <tr id="row51058985"><td class="cellrowborder" valign="top" width="35.9%" headers="mcps1.2.3.1.1 "><p id="p42137138"><a name="p42137138"></a><a name="p42137138"></a>Content-MD5</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.1%" headers="mcps1.2.3.1.2 "><p id="p17853175621510"><a name="p17853175621510"></a><a name="p17853175621510"></a>The MD5 digest string of the message body is calculated according to the RFC 1864 standard. That is, calculate the 128-bit binary array (the message header data encrypted with MD5) first, and then use Base 64 encoding to convert the binary data to a character string.</p>
    </td>
    </tr>
    <tr id="row49222835"><td class="cellrowborder" valign="top" width="35.9%" headers="mcps1.2.3.1.1 "><p id="ole_link13"><a name="ole_link13"></a><a name="ole_link13"></a>CanonicalizedOBSHeaders</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.1%" headers="mcps1.2.3.1.2 "><p id="p23167904"><a name="p23167904"></a><a name="p23167904"></a>Indicates an OBS-defined header prefixed with <strong id="b19459151815508"><a name="b19459151815508"></a><a name="b19459151815508"></a>x-amz-</strong>, for example,&nbsp;<strong id="b64660974"><a name="b64660974"></a><a name="b64660974"></a>x-amz-date</strong>&nbsp;or&nbsp;<strong id="b45077859"><a name="b45077859"></a><a name="b45077859"></a>x-amz-acl</strong>.</p>
    <p id="p3047552"><a name="p3047552"></a><a name="p3047552"></a>1. All characters in the OBS-defined header must be converted to lower-case letters. If a request contains multiple OBS-defined headers, the headers are organized in a dictionary order.</p>
    <p id="p27427975"><a name="p27427975"></a><a name="p27427975"></a>2. If multiple OBS-defined headers in a request have the same prefix, combine the headers into one. For example, if headers <strong id="b45525183"><a name="b45525183"></a><a name="b45525183"></a>x-amz-meta-name:name1</strong>&nbsp;and&nbsp;<strong id="b7073466"><a name="b7073466"></a><a name="b7073466"></a>x-amz-meta-name:name2</strong>&nbsp;are added, combine the headers to&nbsp;<strong id="b63661202"><a name="b63661202"></a><a name="b63661202"></a>x-amze-meta-name:name1,name2</strong>.</p>
    <p id="p36079911"><a name="p36079911"></a><a name="p36079911"></a>3. If an OBS-defined header contains non-ASCII or unrecognizable characters, the header must be Base64 encoded.</p>
    <p id="p56283746"><a name="p56283746"></a><a name="p56283746"></a>4. An OBS-defined header contains spaces or tabs only when necessary. Unnecessary spaces must be omitted. For example, <strong id="b734115283504"><a name="b734115283504"></a><a name="b734115283504"></a>x-amz-meta-name: name</strong>&nbsp;must be changed to&nbsp;<strong id="b62689558"><a name="b62689558"></a><a name="b62689558"></a>x-amz-meta-name:name</strong>. The space between&nbsp;<strong id="b03131043165011"><a name="b03131043165011"></a><a name="b03131043165011"></a>x-amz-meta-name:</strong> and <strong id="b1842645516502"><a name="b1842645516502"></a><a name="b1842645516502"></a>name</strong> is omitted.</p>
    <p id="p66660559"><a name="p66660559"></a><a name="p66660559"></a>5. Each OBS-defined header occupies a separate line. For details, see <a href="#table25228990">Table 4</a>.</p>
    </td>
    </tr>
    <tr id="row30796205"><td class="cellrowborder" valign="top" width="35.9%" headers="mcps1.2.3.1.1 "><p id="p11464716"><a name="p11464716"></a><a name="p11464716"></a>CanonicalizedResource</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.1%" headers="mcps1.2.3.1.2 "><p id="p56226836"><a name="p56226836"></a><a name="p56226836"></a>Indicates a requested resource. This parameter is constructed as follows:</p>
    <p id="p36279478"><a name="p36279478"></a><a name="p36279478"></a>["/" + Bucket ] + &lt;HTTP-Request-URI, ["/" + object name]&gt; + [subresource].</p>
    <p id="p1923153182713"><a name="p1923153182713"></a><a name="p1923153182713"></a>[subresource] is mandatory if any subresource exists.</p>
    <p id="p6847548"><a name="p6847548"></a><a name="p6847548"></a>In virtual-style requests, the bucket name is required. In other requests, the bucket name is not required. For details, see <a href="#table54992765">Table 2</a>.</p>
    <p id="p17780525"><a name="p17780525"></a><a name="p17780525"></a>If a subresource (such as <strong id="b4074007"><a name="b4074007"></a><a name="b4074007"></a>?acl</strong>&nbsp;and&nbsp;<strong id="b36666067"><a name="b36666067"></a><a name="b36666067"></a>?logging</strong>) exists, the subresource must be added. The subresource includes&nbsp;<strong id="b165461624143414"><a name="b165461624143414"></a><a name="b165461624143414"></a>acl</strong>,&nbsp;<strong id="b75122267347"><a name="b75122267347"></a><a name="b75122267347"></a>lifecycle</strong>,&nbsp;<strong id="b13398427143410"><a name="b13398427143410"></a><a name="b13398427143410"></a>location</strong>,&nbsp;<strong id="b423562820349"><a name="b423562820349"></a><a name="b423562820349"></a>logging</strong>,&nbsp;<strong id="b7540185852219"><a name="b7540185852219"></a><a name="b7540185852219"></a>notification</strong>,&nbsp;<strong id="b17251431163419"><a name="b17251431163419"></a><a name="b17251431163419"></a>partNumber</strong>,&nbsp;<strong id="b1433513318346"><a name="b1433513318346"></a><a name="b1433513318346"></a>policy</strong>,&nbsp;<strong id="b143398347344"><a name="b143398347344"></a><a name="b143398347344"></a>uploadId</strong>,&nbsp;<strong id="b532853523417"><a name="b532853523417"></a><a name="b532853523417"></a>uploads</strong>,&nbsp;<strong id="b5422036143415"><a name="b5422036143415"></a><a name="b5422036143415"></a>versionId</strong>,&nbsp;<strong id="b938413373342"><a name="b938413373342"></a><a name="b938413373342"></a>versioning</strong>,&nbsp;<strong id="b133931638193412"><a name="b133931638193412"></a><a name="b133931638193412"></a>versions</strong>,&nbsp;<strong id="b4601183963420"><a name="b4601183963420"></a><a name="b4601183963420"></a>website</strong>,&nbsp;<strong id="b17441341113415"><a name="b17441341113415"></a><a name="b17441341113415"></a>quota</strong>,&nbsp;<strong id="b20382442183415"><a name="b20382442183415"></a><a name="b20382442183415"></a>storagePolicy</strong>,&nbsp;<strong id="b134604317344"><a name="b134604317344"></a><a name="b134604317344"></a>storageinfo</strong>, and&nbsp;<strong id="b12383124413342"><a name="b12383124413342"></a><a name="b12383124413342"></a>deletebucket</strong>. For details, see&nbsp;<a href="#table4097412592916">Table 5</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    Note that the calculation method of Content-MD5 is to first calculate the binary array encrypted by MD5, and then perform Base-64 encoding for the binary array, instead of directly encoding the 32-bit character string. The following is an example of the Java code used to calculate the Content-MD5 value:

    ```
    MessageDigest md = MessageDigest.getInstance("MD5");
    md.update(buffer);            
    byte[] digests = md.digest();
    String md5 = Base64.encode(digests);
    ```

    In the code, buffer stands for the byte stream of the message body, and digests stands for the 128-bit binary array calculated from the message body with MD5. Then the binary data is converted to the correct Content-MD5 value by Base-64 encoding.

    [Table 2](#table54992765) lists example **StringToSign**.

    **Table  2**  StringToSign generated for GET Object ACL

    <a name="table54992765"></a>
    <table><thead align="left"><tr id="row58090788"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p7733362"><a name="p7733362"></a><a name="p7733362"></a>Request Header</p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p22422552"><a name="p22422552"></a><a name="p22422552"></a>StringToSign</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4287423"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p47194909212511"><a name="p47194909212511"></a><a name="p47194909212511"></a>GET /object.txt HTTP/1.1</p>
    <p id="p15880148162927"><a name="p15880148162927"></a><a name="p15880148162927"></a>Host: bucketname.obs.example.com</p>
    <p id="p64691321212511"><a name="p64691321212511"></a><a name="p64691321212511"></a>Date: Sat, 12 Oct 2015 08:12:38 GMT</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p5505616212511"><a name="p5505616212511"></a><a name="p5505616212511"></a>GET \n</p>
    <p id="p43301772212511"><a name="p43301772212511"></a><a name="p43301772212511"></a>\n</p>
    <p id="p54171636212511"><a name="p54171636212511"></a><a name="p54171636212511"></a>Sat, 12 Oct 2015 08:12:38 GMT\n</p>
    <p id="p17782677212511"><a name="p17782677212511"></a><a name="p17782677212511"></a>/bucket/object.txt</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  StringToSign generated for a PUT Object request containing OBS-defined headers \(1\)

    <a name="table25172842"></a>
    <table><thead align="left"><tr id="row12086140"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p39453247"><a name="p39453247"></a><a name="p39453247"></a>Request Header</p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p41596476"><a name="p41596476"></a><a name="p41596476"></a>StringToSign</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row13871385"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p45738961212511"><a name="p45738961212511"></a><a name="p45738961212511"></a>PUT /object.txt HTTP/1.1</p>
    <p id="p8997468212511"><a name="p8997468212511"></a><a name="p8997468212511"></a>User-Agent: curl/7.15.5</p>
    <p id="p41479500162750"><a name="p41479500162750"></a><a name="p41479500162750"></a>Host: bucketname.obs.example.com</p>
    <p id="p57706333212511"><a name="p57706333212511"></a><a name="p57706333212511"></a>x-amz-date:Tue, 15 Oct 2015 07:20:09 GMT</p>
    <p id="p49594957212511"><a name="p49594957212511"></a><a name="p49594957212511"></a>content-type: text/plain</p>
    <p id="p43701435212511"><a name="p43701435212511"></a><a name="p43701435212511"></a>Content-Length: 5913339</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p50155357212511"><a name="p50155357212511"></a><a name="p50155357212511"></a>PUT\n</p>
    <p id="p48745036212511"><a name="p48745036212511"></a><a name="p48745036212511"></a>\n</p>
    <p id="p56033807212511"><a name="p56033807212511"></a><a name="p56033807212511"></a>\n</p>
    <p id="p34542223212511"><a name="p34542223212511"></a><a name="p34542223212511"></a>x-amz-date:Tue, 15 Oct 2015 07:20:09 GMT\n</p>
    <p id="p42444556212511"><a name="p42444556212511"></a><a name="p42444556212511"></a>/bucket/object.txt</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  StringToSign generated for a PUT Object request containing OBS-defined headers \(2\)

    <a name="table25228990"></a>
    <table><thead align="left"><tr id="row6738088"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p8914235"><a name="p8914235"></a><a name="p8914235"></a>Request Header</p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p50964406"><a name="p50964406"></a><a name="p50964406"></a>StringToSign</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row34476226"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p17563722212511"><a name="p17563722212511"></a><a name="p17563722212511"></a>PUT /object.txt HTTP/1.1</p>
    <p id="p23855777212511"><a name="p23855777212511"></a><a name="p23855777212511"></a>User-Agent: curl/7.15.5</p>
    <p id="p59920569162952"><a name="p59920569162952"></a><a name="p59920569162952"></a>Host: bucketname.obs.example.com</p>
    <p id="p53269794212511"><a name="p53269794212511"></a><a name="p53269794212511"></a>Date: Mon, 14 Oct 2015 12:08:34 GMT</p>
    <p id="p9666102212511"><a name="p9666102212511"></a><a name="p9666102212511"></a>x-amz-acl: public-read</p>
    <p id="p19886059212511"><a name="p19886059212511"></a><a name="p19886059212511"></a>content-type: text/plain</p>
    <p id="p44756811212511"><a name="p44756811212511"></a><a name="p44756811212511"></a>Content-Length: 5913339</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p1423060212511"><a name="p1423060212511"></a><a name="p1423060212511"></a>PUT\n</p>
    <p id="p12807544212511"><a name="p12807544212511"></a><a name="p12807544212511"></a>\n</p>
    <p id="p48159034212511"><a name="p48159034212511"></a><a name="p48159034212511"></a>text/plain\n</p>
    <p id="p1271843311328"><a name="p1271843311328"></a><a name="p1271843311328"></a>\n</p>
    <p id="p30778123212511"><a name="p30778123212511"></a><a name="p30778123212511"></a>Mon, 14 Oct 2015 12:08:34 GMT\n</p>
    <p id="p8567652212511"><a name="p8567652212511"></a><a name="p8567652212511"></a>x-amz-acl:public-read\n</p>
    <p id="p10000006212511"><a name="p10000006212511"></a><a name="p10000006212511"></a>/bucket/object.txt</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5**  StringToSign generated for GET Object ACL

    <a name="table4097412592916"></a>
    <table><thead align="left"><tr id="row8146160"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p55859239"><a name="p55859239"></a><a name="p55859239"></a>Request Header</p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p28304539"><a name="p28304539"></a><a name="p28304539"></a>StringToSign</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row10966323"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p12968078212511"><a name="p12968078212511"></a><a name="p12968078212511"></a>GET /object.txt?acl HTTP/1.1</p>
    <p id="p5976225163058"><a name="p5976225163058"></a><a name="p5976225163058"></a>Host: bucketname.obs.example.com</p>
    <p id="p43781379212511"><a name="p43781379212511"></a><a name="p43781379212511"></a>Date: Sat, 12 Oct 2015 08:12:38 GMT</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p56630825212511"><a name="p56630825212511"></a><a name="p56630825212511"></a>GET \n</p>
    <p id="p23694119212511"><a name="p23694119212511"></a><a name="p23694119212511"></a>\n</p>
    <p id="p11920487212511"><a name="p11920487212511"></a><a name="p11920487212511"></a>Sat, 12 Oct 2015 08:12:38 GMT\n</p>
    <p id="p40175526212511"><a name="p40175526212511"></a><a name="p40175526212511"></a>/bucket/object.txt?acl</p>
    </td>
    </tr>
    </tbody>
    </table>

2.  Generate the signature using  **StringToSign**  and the SK.

    Use the hash-based message authentication code \(HMAC\) algorithm to calculate the signature.

    ```
    Signature = Base64( HMAC-SHA1( UTF-8-Encoding-Of(YourSecretAccessKeyID, StringToSign ) ) )
    ```


