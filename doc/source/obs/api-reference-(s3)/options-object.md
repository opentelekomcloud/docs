# OPTIONS Object<a name="EN-US_TOPIC_0125560261"></a>

For details, see section  [OPTIONS Bucket](options-bucket.md).

## Request Syntax<a name="section54969651"></a>

```
OPTIONS /object HTTP/1.1 
 User-Agent: agent
 Host: bucketname.obs.example.com 
 Accept: */*
 Date: date 
 Authorization: authorization 
 Origin: origin 
 Access-Control-Request-Method: method
```

## Request Parameters<a name="section24964816"></a>

This request involves no parameters.

## Request Headers<a name="section23356753"></a>

[Table 1](#table58188993)  lists the request headers.

**Table  1**  OPTIONS request headers

<a name="table58188993"></a>
<table><thead align="left"><tr id="row32819733"><th class="cellrowborder" valign="top" width="28.02280228022802%" id="mcps1.2.4.1.1"><p id="p41152746"><a name="p41152746"></a><a name="p41152746"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="38.64386438643865%" id="mcps1.2.4.1.2"><p id="p45038152"><a name="p45038152"></a><a name="p45038152"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p24211670"><a name="p24211670"></a><a name="p24211670"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row14988220"><td class="cellrowborder" valign="top" width="28.02280228022802%" headers="mcps1.2.4.1.1 "><p id="p6086307"><a name="p6086307"></a><a name="p6086307"></a>Origin</p>
</td>
<td class="cellrowborder" valign="top" width="38.64386438643865%" headers="mcps1.2.4.1.2 "><p id="p23228850"><a name="p23228850"></a><a name="p23228850"></a>Indicates an origin specified by a pre-request. Generally, it is a domain name.</p>
<p id="p7733065"><a name="p7733065"></a><a name="p7733065"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p22398504"><a name="p22398504"></a><a name="p22398504"></a>Mandatory</p>
</td>
</tr>
<tr id="row259947"><td class="cellrowborder" valign="top" width="28.02280228022802%" headers="mcps1.2.4.1.1 "><p id="p21055716"><a name="p21055716"></a><a name="p21055716"></a>Access-Control-Request-Method</p>
</td>
<td class="cellrowborder" valign="top" width="38.64386438643865%" headers="mcps1.2.4.1.2 "><p id="p27791397"><a name="p27791397"></a><a name="p27791397"></a>Indicates an HTTP method that can be used by a request. The request can use multiple method headers.</p>
<p id="p48795984"><a name="p48795984"></a><a name="p48795984"></a>Type: String</p>
<p id="p36510679"><a name="p36510679"></a><a name="p36510679"></a>Valid values: <strong id="b60160657"><a name="b60160657"></a><a name="b60160657"></a>GET</strong>,&nbsp;<strong id="b4575009"><a name="b4575009"></a><a name="b4575009"></a>PUT</strong>,&nbsp;<strong id="b41175087"><a name="b41175087"></a><a name="b41175087"></a>HEAD</strong>,&nbsp;<strong id="b35031468"><a name="b35031468"></a><a name="b35031468"></a>POST</strong>, and&nbsp;<strong id="b46847761"><a name="b46847761"></a><a name="b46847761"></a>DELETE</strong></p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p36572320"><a name="p36572320"></a><a name="p36572320"></a>Mandatory</p>
</td>
</tr>
<tr id="row60715427"><td class="cellrowborder" valign="top" width="28.02280228022802%" headers="mcps1.2.4.1.1 "><p id="p19002592"><a name="p19002592"></a><a name="p19002592"></a>Access-Control-Request-Headers</p>
</td>
<td class="cellrowborder" valign="top" width="38.64386438643865%" headers="mcps1.2.4.1.2 "><p id="p62814973"><a name="p62814973"></a><a name="p62814973"></a>Indicates the HTTP headers of a request. The request can use multiple HTTP headers.</p>
<p id="p28463847"><a name="p28463847"></a><a name="p28463847"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p23870264"><a name="p23870264"></a><a name="p23870264"></a>Optional</p>
</td>
</tr>
<tr id="row3353184244011"><td class="cellrowborder" valign="top" width="28.02280228022802%" headers="mcps1.2.4.1.1 "><p id="p7527144324018"><a name="p7527144324018"></a><a name="p7527144324018"></a>x-amz-security-token</p>
</td>
<td class="cellrowborder" valign="top" width="38.64386438643865%" headers="mcps1.2.4.1.2 "><p id="p19527124310403"><a name="p19527124310403"></a><a name="p19527124310403"></a>Header field used to identify the request of a federated user. When the federal authentication function is enabled, users sending such requests are identified as federated users.</p>
<p id="p1852713433401"><a name="p1852713433401"></a><a name="p1852713433401"></a>Type: string</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p18527843164011"><a name="p18527843164011"></a><a name="p18527843164011"></a>Optional. This parameter must be carried in the request sent by federated users.</p>
</td>
</tr>
</tbody>
</table>

## Request Elements<a name="section8884193"></a>

This request involves no elements.

## Response Syntax<a name="section18040105"></a>

```
HTTP/1.1 status_code 
 Server: server
 x-amz-request-id: request id 
 x-amz-id-2: id 
 Content-Type: type 
 Access-Control-Allow-Origin: origin 
 Access-Control-Allow-Methods: method 
 Access-Control-Allow-Header: header 
 Access-Control-Max-Age: seconds 
 Access-Control-Expose-Headers: header 
 Date: date 
 Content-Length: length
```

## Response Headers<a name="section28143222"></a>

[Table 2](#table47822814)  lists the request headers.

**Table  2**  CORS request headers

<a name="table47822814"></a>
<table><thead align="left"><tr id="row18565881"><th class="cellrowborder" valign="top" width="33.82%" id="mcps1.2.3.1.1"><p id="p27441378"><a name="p27441378"></a><a name="p27441378"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="66.18%" id="mcps1.2.3.1.2"><p id="p8159144"><a name="p8159144"></a><a name="p8159144"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row56910898"><td class="cellrowborder" valign="top" width="33.82%" headers="mcps1.2.3.1.1 "><p id="p46380008"><a name="p46380008"></a><a name="p46380008"></a>Access-Control-Allow-Origin</p>
</td>
<td class="cellrowborder" valign="top" width="66.18%" headers="mcps1.2.3.1.2 "><p id="p65793204"><a name="p65793204"></a><a name="p65793204"></a>If the origin of a request meets server CORS configuration requirements, the response contains the origin.</p>
<p id="p55267924"><a name="p55267924"></a><a name="p55267924"></a>Type: String</p>
</td>
</tr>
<tr id="row27649275"><td class="cellrowborder" valign="top" width="33.82%" headers="mcps1.2.3.1.1 "><p id="p24998823"><a name="p24998823"></a><a name="p24998823"></a>Access-Control-Allow-Headers</p>
</td>
<td class="cellrowborder" valign="top" width="66.18%" headers="mcps1.2.3.1.2 "><p id="p11638816"><a name="p11638816"></a><a name="p11638816"></a>If the headers of a request meet server CORS configuration requirements, the response contains the headers.</p>
<p id="p37640485"><a name="p37640485"></a><a name="p37640485"></a>Type: String</p>
</td>
</tr>
<tr id="row3220045"><td class="cellrowborder" valign="top" width="33.82%" headers="mcps1.2.3.1.1 "><p id="p59497111"><a name="p59497111"></a><a name="p59497111"></a>Access-Control-Max-Age</p>
</td>
<td class="cellrowborder" valign="top" width="66.18%" headers="mcps1.2.3.1.2 "><p id="p54536677"><a name="p54536677"></a><a name="p54536677"></a>Indicates <strong id="b114731030191815"><a name="b114731030191815"></a><a name="b114731030191815"></a>MaxAgeSeconds</strong> in the CORS configuration of a server.</p>
<p id="p55394720"><a name="p55394720"></a><a name="p55394720"></a>Type: Integer</p>
</td>
</tr>
<tr id="row28790433"><td class="cellrowborder" valign="top" width="33.82%" headers="mcps1.2.3.1.1 "><p id="p50323754"><a name="p50323754"></a><a name="p50323754"></a>Access-Control-Allow-Methods</p>
</td>
<td class="cellrowborder" valign="top" width="66.18%" headers="mcps1.2.3.1.2 "><p id="p49692243"><a name="p49692243"></a><a name="p49692243"></a>If the <strong id="b44577003"><a name="b44577003"></a><a name="b44577003"></a>Access-Control-Request-Method</strong> of a request meets server CORS configuration requirements, the response contains the methods in the rule.</p>
<p id="p65648708"><a name="p65648708"></a><a name="p65648708"></a>Type: String</p>
<p id="p53967463"><a name="p53967463"></a><a name="p53967463"></a>Valid values: <strong id="b15945126"><a name="b15945126"></a><a name="b15945126"></a>GET</strong>,&nbsp;<strong id="b9288408"><a name="b9288408"></a><a name="b9288408"></a>PUT</strong>,&nbsp;<strong id="b16486816"><a name="b16486816"></a><a name="b16486816"></a>HEAD</strong>,&nbsp;<strong id="b14163622"><a name="b14163622"></a><a name="b14163622"></a>POST</strong>, and&nbsp;<strong id="b60363739"><a name="b60363739"></a><a name="b60363739"></a>DELETE</strong></p>
</td>
</tr>
<tr id="row6402744"><td class="cellrowborder" valign="top" width="33.82%" headers="mcps1.2.3.1.1 "><p id="p48860279"><a name="p48860279"></a><a name="p48860279"></a>Access-Control-Expose-Headers</p>
</td>
<td class="cellrowborder" valign="top" width="66.18%" headers="mcps1.2.3.1.2 "><p id="p65368522"><a name="p65368522"></a><a name="p65368522"></a>Indicates <strong id="b51445791"><a name="b51445791"></a><a name="b51445791"></a>ExposeHeader</strong> in the CORS configuration of a server.</p>
<p id="p60358938"><a name="p60358938"></a><a name="p60358938"></a>Type: String</p>
</td>
</tr>
</tbody>
</table>

## Response Elements<a name="section51962411"></a>

This response involves no elements.

## Error Responses<a name="section65008522"></a>

[Table 3](#table27752149)  describes possible special errors in the request.

**Table  3**  Special errors

<a name="table27752149"></a>
<table><thead align="left"><tr id="row804613"><th class="cellrowborder" valign="top" width="25.072507250725067%" id="mcps1.2.4.1.1"><p id="p65173721"><a name="p65173721"></a><a name="p65173721"></a>Error Code</p>
</th>
<th class="cellrowborder" valign="top" width="45.82458245824582%" id="mcps1.2.4.1.2"><p id="p44580049"><a name="p44580049"></a><a name="p44580049"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="29.1029102910291%" id="mcps1.2.4.1.3"><p id="p54214230"><a name="p54214230"></a><a name="p54214230"></a>HTTP Status Code</p>
</th>
</tr>
</thead>
<tbody><tr id="row29276495"><td class="cellrowborder" valign="top" width="25.072507250725067%" headers="mcps1.2.4.1.1 "><p id="p22585893"><a name="p22585893"></a><a name="p22585893"></a>Bad Request</p>
</td>
<td class="cellrowborder" valign="top" width="45.82458245824582%" headers="mcps1.2.4.1.2 "><p id="p17518015"><a name="p17518015"></a><a name="p17518015"></a>Invalid Access-Control-Request-Method: null</p>
<p id="p23444409"><a name="p23444409"></a><a name="p23444409"></a>When CORS and OPTIONS are configured for a bucket, no method header is added.</p>
</td>
<td class="cellrowborder" valign="top" width="29.1029102910291%" headers="mcps1.2.4.1.3 "><p id="p19948981"><a name="p19948981"></a><a name="p19948981"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row45323105"><td class="cellrowborder" valign="top" width="25.072507250725067%" headers="mcps1.2.4.1.1 "><p id="p47292856"><a name="p47292856"></a><a name="p47292856"></a>Bad Request</p>
</td>
<td class="cellrowborder" valign="top" width="45.82458245824582%" headers="mcps1.2.4.1.2 "><p id="p5516148"><a name="p5516148"></a><a name="p5516148"></a>Insufficient information. Origin request header needed.</p>
<p id="p49645340"><a name="p49645340"></a><a name="p49645340"></a>When CORS and OPTIONS are configured for a bucket, no origin header is added.</p>
</td>
<td class="cellrowborder" valign="top" width="29.1029102910291%" headers="mcps1.2.4.1.3 "><p id="p61849578"><a name="p61849578"></a><a name="p61849578"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row19775290"><td class="cellrowborder" valign="top" width="25.072507250725067%" headers="mcps1.2.4.1.1 "><p id="p58294676"><a name="p58294676"></a><a name="p58294676"></a>AccessForbidden</p>
</td>
<td class="cellrowborder" valign="top" width="45.82458245824582%" headers="mcps1.2.4.1.2 "><p id="p24248306"><a name="p24248306"></a><a name="p24248306"></a>CORSResponse: This CORS request is not allowed. This is usually because the evaluation of Origin, request method / Access-Control-Request-Method or Access-Control-Request-Headers are not whitelisted by the resource's CORS spec.</p>
<p id="p16908166"><a name="p16908166"></a><a name="p16908166"></a>When CORS and OPTIONS are configured for a bucket, origin, method, and headers do not match any rule.</p>
</td>
<td class="cellrowborder" valign="top" width="29.1029102910291%" headers="mcps1.2.4.1.3 "><p id="p27384230"><a name="p27384230"></a><a name="p27384230"></a>403 Forbidden</p>
</td>
</tr>
</tbody>
</table>

For details about other errors, see  [Table 1](error-codes.md#table30733758).

## Sample Request<a name="section15592595"></a>

```
OPTIONS /object HTTP/1.1 
 User-Agent: curl/7.19.0 (x86_64-suse-linux-gnu) libcurl/7.19.0 OpenSSL/0.9.8{ zlib/1.2.3 libidn/1.10 
 Host: bucketname.obs.example.com 
 Accept: */* 
 Date: Tue, 28 Apr 2015 12:44:17 +0000 
 Authorization: AWS D13E0C94E722DD69423C:9U2ZGZebzPsbjsbxd6Qx1552LCI= 
 Origin:www.example.com 
 Access-Control-Request-Method:HEAD 
 Access-Control-Request-Headers:acc_header_1
 Access-Control-Request-Headers:acc_header_2
```

## Sample Response<a name="section6115634"></a>

```
HTTP/1.1 200 OK
 Server: OBS 
 x-amz-request-id: EB916A17C4CA9863E10CB3875D12D921 
 x-amz-id-2: xuXo/62YzJOvNjQ3179xVyqlTSY8cWbI/EBDbKmhEoqdvKw7bU4KwFzeBX9oq212 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Content-Type: text/xml 
 Access-Control-Allow-Origin: www.example.com 
 Access-Control-Allow-Methods: POST,GET,HEAD,PUT 
 Access-Control-Allow-Headers: acc_header_1,acc_header_2 
 Access-Control-Max-Age: 100 
 Access-Control-Expose-Headers: exp_header_1 
 Date: Tue, 28 Apr 2015 12:46:56 GMT 
 Content-Length: 0
```

