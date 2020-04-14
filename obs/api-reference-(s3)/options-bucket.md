# OPTIONS Bucket<a name="EN-US_TOPIC_0125560464"></a>

**OPTIONS**  refers to pre-requests that are sent to servers by clients. Generally, you can use these requests to check whether clients have permission to perform operations on servers. Only after a pre-request is returned successfully, clients start to execute the follow-up requests.

OBS allows buckets to store static web resources. The buckets of OBS can serve as website resources if the buckets are properly used. In this scenario, buckets in OBS serve as servers to process  **OPTIONS**  pre-requests from clients.

OBS can process  **OPTIONS** pre-requests only after CORS is configured for buckets in OBS. For details about CORS, see section [PUT Bucket CORS](put-bucket-cors.md).

## Request Syntax<a name="section6578292"></a>

```
OPTIONS / HTTP/1.1
 User-Agent: agent 
 Host: bucketname.obs.example.com 
 Accept: */*
 Date: date 
 Authorization: authorization 
 Origin: origin 
 Access-Control-Request-Method: method
```

## Request Parameters<a name="section59204636"></a>

This request involves no parameters.

## Request Headers<a name="section63079676"></a>

[Table 1](#table57465365)  lists the request headers.

**Table  1**  OPTIONS request headers

<a name="table57465365"></a>
<table><thead align="left"><tr id="row44805132"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p5337050"><a name="p5337050"></a><a name="p5337050"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p29647872"><a name="p29647872"></a><a name="p29647872"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p52667431"><a name="p52667431"></a><a name="p52667431"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row38203510"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p7476630"><a name="p7476630"></a><a name="p7476630"></a>Origin</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1627311"><a name="p1627311"></a><a name="p1627311"></a>Indicates an origin specified by a pre-request. Generally, it is a domain name.</p>
<p id="p14645800"><a name="p14645800"></a><a name="p14645800"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p45459112"><a name="p45459112"></a><a name="p45459112"></a>Mandatory</p>
</td>
</tr>
<tr id="row6478825"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p55022811"><a name="p55022811"></a><a name="p55022811"></a>Access-Control-Request-Method</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p27662693"><a name="p27662693"></a><a name="p27662693"></a>Indicates an HTTP method that can be used by a request. The request can use multiple method headers.</p>
<p id="p47637651"><a name="p47637651"></a><a name="p47637651"></a>Type: String</p>
<p id="p26085680"><a name="p26085680"></a><a name="p26085680"></a>Valid values: <strong id="b33444533"><a name="b33444533"></a><a name="b33444533"></a>GET</strong>,&nbsp;<strong id="b32565348"><a name="b32565348"></a><a name="b32565348"></a>PUT</strong>,&nbsp;<strong id="b24652676"><a name="b24652676"></a><a name="b24652676"></a>HEAD</strong>,&nbsp;<strong id="b20547495"><a name="b20547495"></a><a name="b20547495"></a>POST</strong>, and&nbsp;<strong id="b50709735"><a name="b50709735"></a><a name="b50709735"></a>DELETE</strong></p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p13847879"><a name="p13847879"></a><a name="p13847879"></a>Mandatory</p>
</td>
</tr>
<tr id="row57522049"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p28774374"><a name="p28774374"></a><a name="p28774374"></a>Access-Control-Request-Headers</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p49022972"><a name="p49022972"></a><a name="p49022972"></a>Indicates the HTTP headers of a request. The request can use multiple HTTP headers.</p>
<p id="p38553569"><a name="p38553569"></a><a name="p38553569"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p35831362"><a name="p35831362"></a><a name="p35831362"></a>Optional</p>
</td>
</tr>
<tr id="row13892162514268"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p13931152772615"><a name="p13931152772615"></a><a name="p13931152772615"></a>x-amz-security-token</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p9931142712260"><a name="p9931142712260"></a><a name="p9931142712260"></a>Header field used to identify the request of a federated user. When the federal authentication function is enabled, users sending such requests are identified as federated users.</p>
<p id="p19316279264"><a name="p19316279264"></a><a name="p19316279264"></a>Type: string</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p59311327112611"><a name="p59311327112611"></a><a name="p59311327112611"></a>Optional. This parameter must be carried in the request sent by federated users.</p>
</td>
</tr>
</tbody>
</table>

## Request Elements<a name="section30846174"></a>

This request involves no elements.

## Response Syntax<a name="section39517886"></a>

```
HTTP/1.1 status_code 
 x-amz-request-id: request id 
 x-amz-id-2: id  
 Access-Control-Allow-Origin: origin 
 Access-Control-Allow-Methods: method 
 Access-Control-Allow-Header: header 
 Access-Control-Max-Age: seconds 
 Access-Control-Expose-Headers: header 
 Date: date 
 Content-Length: length
```

## Response Headers<a name="section20116657"></a>

[Table 2](#table7221243)  lists the response headers.

**Table  2**  CORS response headers

<a name="table7221243"></a>
<table><thead align="left"><tr id="row23871500"><th class="cellrowborder" valign="top" width="35.3%" id="mcps1.2.3.1.1"><p id="p54543318"><a name="p54543318"></a><a name="p54543318"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="64.7%" id="mcps1.2.3.1.2"><p id="p55932620"><a name="p55932620"></a><a name="p55932620"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row34248408"><td class="cellrowborder" valign="top" width="35.3%" headers="mcps1.2.3.1.1 "><p id="p22657631"><a name="p22657631"></a><a name="p22657631"></a>Access-Control-Allow-Origin</p>
</td>
<td class="cellrowborder" valign="top" width="64.7%" headers="mcps1.2.3.1.2 "><p id="p23328843"><a name="p23328843"></a><a name="p23328843"></a>If the origin of a request meets server CORS configuration requirements, the response contains the origin.</p>
<p id="p8633003"><a name="p8633003"></a><a name="p8633003"></a>Type: String</p>
</td>
</tr>
<tr id="row10588164"><td class="cellrowborder" valign="top" width="35.3%" headers="mcps1.2.3.1.1 "><p id="p52334961"><a name="p52334961"></a><a name="p52334961"></a>Access-Control-Allow-Headers</p>
</td>
<td class="cellrowborder" valign="top" width="64.7%" headers="mcps1.2.3.1.2 "><p id="p11273467"><a name="p11273467"></a><a name="p11273467"></a>If the headers of a request meet server CORS configuration requirements, the response contains the headers.</p>
<p id="p34352342"><a name="p34352342"></a><a name="p34352342"></a>Type: String</p>
</td>
</tr>
<tr id="row40735625"><td class="cellrowborder" valign="top" width="35.3%" headers="mcps1.2.3.1.1 "><p id="p11251332"><a name="p11251332"></a><a name="p11251332"></a>Access-Control-Max-Age</p>
</td>
<td class="cellrowborder" valign="top" width="64.7%" headers="mcps1.2.3.1.2 "><p id="p38942675"><a name="p38942675"></a><a name="p38942675"></a>Indicates <strong id="b132633127712"><a name="b132633127712"></a><a name="b132633127712"></a>MaxAgeSeconds</strong> in the CORS configuration of a server.</p>
<p id="p240095"><a name="p240095"></a><a name="p240095"></a>Type: Integer</p>
</td>
</tr>
<tr id="row2160855"><td class="cellrowborder" valign="top" width="35.3%" headers="mcps1.2.3.1.1 "><p id="p40811528"><a name="p40811528"></a><a name="p40811528"></a>Access-Control-Allow-Methods</p>
</td>
<td class="cellrowborder" valign="top" width="64.7%" headers="mcps1.2.3.1.2 "><p id="p17399466"><a name="p17399466"></a><a name="p17399466"></a>If the <strong id="b22377468"><a name="b22377468"></a><a name="b22377468"></a>Access-Control-Request-Method</strong> of a request meets server CORS configuration requirements, the response contains the methods in the rule.</p>
<p id="p70628"><a name="p70628"></a><a name="p70628"></a>Type: String</p>
<p id="p635658"><a name="p635658"></a><a name="p635658"></a>Valid values: <strong id="b5720927"><a name="b5720927"></a><a name="b5720927"></a>GET</strong>,&nbsp;<strong id="b51488348"><a name="b51488348"></a><a name="b51488348"></a>PUT</strong>,&nbsp;<strong id="b60741955"><a name="b60741955"></a><a name="b60741955"></a>HEAD</strong>,&nbsp;<strong id="b9806683"><a name="b9806683"></a><a name="b9806683"></a>POST</strong>, and&nbsp;<strong id="b21151286"><a name="b21151286"></a><a name="b21151286"></a>DELETE</strong></p>
</td>
</tr>
<tr id="row56143854"><td class="cellrowborder" valign="top" width="35.3%" headers="mcps1.2.3.1.1 "><p id="p51358334"><a name="p51358334"></a><a name="p51358334"></a>Access-Control-Expose-Headers</p>
</td>
<td class="cellrowborder" valign="top" width="64.7%" headers="mcps1.2.3.1.2 "><p id="p66384370"><a name="p66384370"></a><a name="p66384370"></a>Indicates <strong id="b60588421"><a name="b60588421"></a><a name="b60588421"></a>ExposeHeader</strong> in the CORS configuration of a server.</p>
<p id="p8424883"><a name="p8424883"></a><a name="p8424883"></a>Type: String</p>
</td>
</tr>
</tbody>
</table>

## Response Elements<a name="section46832193"></a>

This response involves no elements.

## Error Responses<a name="section18836558"></a>

For details about other errors, see  [Table 1](error-codes.md#table30733758). In addition, this response also may contain special errors, as described in  [Table 3](#table64991193).

**Table  3**  Special errors

<a name="table64991193"></a>
<table><thead align="left"><tr id="row53469045"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p36025402"><a name="p36025402"></a><a name="p36025402"></a>Error Code</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p32376435"><a name="p32376435"></a><a name="p32376435"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p5245577"><a name="p5245577"></a><a name="p5245577"></a>HTTP Status Code</p>
</th>
</tr>
</thead>
<tbody><tr id="row22238563"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p56493161"><a name="p56493161"></a><a name="p56493161"></a>Bad Request</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p12543365"><a name="p12543365"></a><a name="p12543365"></a>Invalid Access-Control-Request-Method: null</p>
<p id="p45781421"><a name="p45781421"></a><a name="p45781421"></a>When CORS and OPTIONS are configured for a bucket, no method header is added.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p17307650"><a name="p17307650"></a><a name="p17307650"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row21551128"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p810977"><a name="p810977"></a><a name="p810977"></a>Bad Request</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p65689182"><a name="p65689182"></a><a name="p65689182"></a>Insufficient information. Origin request header needed.</p>
<p id="p54331732"><a name="p54331732"></a><a name="p54331732"></a>When CORS and OPTIONS are configured for a bucket, no origin header is added.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p38794171"><a name="p38794171"></a><a name="p38794171"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row13603222"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p28119201"><a name="p28119201"></a><a name="p28119201"></a>AccessForbidden</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p63062784"><a name="p63062784"></a><a name="p63062784"></a>CORSResponse: This CORS request is not allowed. This is usually because the evaluation of Origin, request method / Access-Control-Request-Method or Access-Control-Request-Headers are not whitelisted by the resource's CORS spec.</p>
<p id="p30694147"><a name="p30694147"></a><a name="p30694147"></a>When CORS and OPTIONS are configured for a bucket, origin, method, and headers do not match any rule.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p3197948"><a name="p3197948"></a><a name="p3197948"></a>403 Forbidden</p>
</td>
</tr>
</tbody>
</table>

## Sample Request<a name="section49531474"></a>

```
OPTIONS / HTTP/1.1 
 User-Agent: curl/7.19.0 (x86_64-suse-linux-gnu) libcurl/7.19.0 OpenSSL/0.9.8{ zlib/1.2.3 libidn/1.10 
 Host: bucketname.obs.example.com
 Accept: */* 
 Date: Tue, 28 Apr 2015 12:43:15 +0000 
 Authorization: AWS D13E0C94E722DD69423C:02VOjl2Z5B7mUd+G6zr0Dql5CW8= 
 Origin:www.example.com 
 Access-Control-Request-Method:HEAD 
 Access-Control-Request-Headers:acc_header_1 
 Access-Control-Request-Headers:acc_header_2
```

## Sample Response<a name="section1462434713910"></a>

```
HTTP/1.1 200 OK 
 x-amz-request-id: 0350FC4D73DDA0D3A6FC2CBE01A7943A 
 x-amz-id-2: ANHl/5gbYTwbfQat5+QZpWdnuE5DV83RXCyGZgBrbDVzVtdtGkqb9ZOepAX3Yr/z 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc  
 Access-Control-Allow-Origin: www.example.com 
 Access-Control-Allow-Methods: POST,GET,HEAD,PUT 
 Access-Control-Allow-Headers: acc_header_1,acc_header_2 
 Access-Control-Max-Age: 100 
 Access-Control-Expose-Headers: exp_header_1 
 Date: Tue, 28 Apr 2015 12:45:34 GMT 
 Content-Length: 0
```

