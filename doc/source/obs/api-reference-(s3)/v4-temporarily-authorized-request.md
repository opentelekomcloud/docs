# V4 Temporarily Authorized Request<a name="EN-US_TOPIC_0125560420"></a>

The authentication information in V4 temporarily authorized requests is delivered using the query parameters. The URL of V4 temporary authentication has six mandatory query parameters unlike V2 authentication. The following is an example of a V4 temporarily authorized request.

```
https://bucketname.obs.example.com/test.txt?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE%2F20150524%2Fregion-1%2Fs3%2Faws4_request&X-Amz-Date=20150524T000000Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=<signature-value>
```

[Table 1](#table43771375)  lists the six mandatory query parameters.

**Table  1**  Six mandatory query parameters

<a name="table43771375"></a>
<table><thead align="left"><tr id="row17706563"><th class="cellrowborder" valign="top" width="35.9%" id="mcps1.2.3.1.1"><p id="p24945537"><a name="p24945537"></a><a name="p24945537"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="64.1%" id="mcps1.2.3.1.2"><p id="p7322627"><a name="p7322627"></a><a name="p7322627"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row56261938"><td class="cellrowborder" valign="top" width="35.9%" headers="mcps1.2.3.1.1 "><p id="p60923125"><a name="p60923125"></a><a name="p60923125"></a>X-Amz-Algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="64.1%" headers="mcps1.2.3.1.2 "><p id="p35826101"><a name="p35826101"></a><a name="p35826101"></a>Indicates the AWS signature algorithm.</p>
</td>
</tr>
<tr id="row16233049"><td class="cellrowborder" valign="top" width="35.9%" headers="mcps1.2.3.1.1 "><p id="p39808586"><a name="p39808586"></a><a name="p39808586"></a>X-Amz-Credential</p>
</td>
<td class="cellrowborder" valign="top" width="64.1%" headers="mcps1.2.3.1.2 "><p id="p3269999"><a name="p3269999"></a><a name="p3269999"></a>In addition to the <strong id="b41961348185112"><a name="b41961348185112"></a><a name="b41961348185112"></a>access key ID</strong>, region and service information must be provided. The information must be the same as that used to calculate the&nbsp;<strong id="b63543344"><a name="b63543344"></a><a name="b63543344"></a>Signing Key</strong>. The value of this parameter is expressed in the following format:</p>
<p id="p35019191"><a name="p35019191"></a><a name="p35019191"></a>&lt;your-access-key-id&gt;/&lt;date&gt;/&lt;AWS-region&gt;/&lt;AWS-service&gt;/aws4_request.OBS region</p>
<p id="p46737271"><a name="p46737271"></a><a name="p46737271"></a>The value is the same as that used for common authentication.</p>
<p id="p17982255"><a name="p17982255"></a><a name="p17982255"></a>Example:</p>
<p id="p27622569"><a name="p27622569"></a><a name="p27622569"></a>AKIAIOSFODNN7EXAMPLE/20150721/region-1/s3/aws4_request</p>
</td>
</tr>
<tr id="row22835632"><td class="cellrowborder" valign="top" width="35.9%" headers="mcps1.2.3.1.1 "><p id="p37746932"><a name="p37746932"></a><a name="p37746932"></a>X-Amz-Date</p>
</td>
<td class="cellrowborder" valign="top" width="64.1%" headers="mcps1.2.3.1.2 "><p id="p37602652"><a name="p37602652"></a><a name="p37602652"></a>Indicates the request generation time. It is in the ISO 8601 format. The value must be the same as that used for signature calculation.</p>
<p id="p2879553"><a name="p2879553"></a><a name="p2879553"></a>Example:</p>
<p id="p25915985"><a name="p25915985"></a><a name="p25915985"></a>20150721T201207Z</p>
</td>
</tr>
<tr id="row18820026"><td class="cellrowborder" valign="top" width="35.9%" headers="mcps1.2.3.1.1 "><p id="p48027136"><a name="p48027136"></a><a name="p48027136"></a>X-Amz-Expires</p>
</td>
<td class="cellrowborder" valign="top" width="64.1%" headers="mcps1.2.3.1.2 "><p id="p64992778"><a name="p64992778"></a><a name="p64992778"></a>Indicates the URL expiration time. The value is an integer expressed in seconds such as 86,400 seconds (24 hours). It ranges from 1 to 604,800 (7 days). The maximum validity period of the URL is 7 days because the validity period for <strong id="b1072915419511"><a name="b1072915419511"></a><a name="b1072915419511"></a>Signing Key</strong> calculation is 7 days.</p>
</td>
</tr>
<tr id="row29923648"><td class="cellrowborder" valign="top" width="35.9%" headers="mcps1.2.3.1.1 "><p id="p7896460"><a name="p7896460"></a><a name="p7896460"></a>X-Amz-SignedHeaders</p>
</td>
<td class="cellrowborder" valign="top" width="64.1%" headers="mcps1.2.3.1.2 "><p id="p35633491"><a name="p35633491"></a><a name="p35633491"></a>Indicates the header list for signature calculation. The HTTP host header is mandatory. All headers that start with <strong id="b52265969"><a name="b52265969"></a><a name="b52265969"></a>x-amz-*</strong> must be used to calculate signatures and contained in the header list. All request headers must be included to ensure security.</p>
<div class="warning" id="note3414026722559"><a name="note3414026722559"></a><a name="note3414026722559"></a><span class="warningtitle"> WARNING: </span><div class="warningbody"><p id="p3882695522559"><a name="p3882695522559"></a><a name="p3882695522559"></a>If headers contain <em id="i12139152853210"><a name="i12139152853210"></a><a name="i12139152853210"></a>gzip</em>, <em id="i213982814328"><a name="i213982814328"></a><a name="i213982814328"></a>no-cache</em>,&nbsp;<em id="i15139172813329"><a name="i15139172813329"></a><a name="i15139172813329"></a>chunked</em>,&nbsp;<em id="i1139152813322"><a name="i1139152813322"></a><a name="i1139152813322"></a>identity</em>,&nbsp;<em id="i5139152812323"><a name="i5139152812323"></a><a name="i5139152812323"></a>keep-alive</em>,&nbsp;<em id="i171391928143218"><a name="i171391928143218"></a><a name="i171391928143218"></a>bytes</em>, and&nbsp;<em id="i3139142818326"><a name="i3139142818326"></a><a name="i3139142818326"></a>close</em>, please use lowercase letters. Otherwise, you will receive a&nbsp;<strong id="b9182141414523"><a name="b9182141414523"></a><a name="b9182141414523"></a>SignatureDoesNotMatch</strong> error response.</p>
</div></div>
</td>
</tr>
<tr id="row631679"><td class="cellrowborder" valign="top" width="35.9%" headers="mcps1.2.3.1.1 "><p id="p51166072"><a name="p51166072"></a><a name="p51166072"></a>X-Amz-Signature</p>
</td>
<td class="cellrowborder" valign="top" width="64.1%" headers="mcps1.2.3.1.2 "><p id="p50811173"><a name="p50811173"></a><a name="p50811173"></a>Indicates the signature of a request.</p>
<p id="p54647379"><a name="p54647379"></a><a name="p54647379"></a>Example:</p>
<p id="p22064367"><a name="p22064367"></a><a name="p22064367"></a>733255ef022bec3f2a8701cd61d4b371f3f28c9f193a1f02279211d48d5193d7</p>
</td>
</tr>
</tbody>
</table>

[Figure 1](#fig11837114385216)  shows the signature computing process of V4 temporarily authorized requests.

**Figure  1**  Signature calculation process of V4 temporarily authorized requests<a name="fig11837114385216"></a>  
![](figures/signature-calculation-process-of-v4-temporarily-authorized-requests.png "signature-calculation-process-of-v4-temporarily-authorized-requests")

The signature calculation process of V4 temporarily authorized requests is the same as that of V4 common requests. The only difference lies in the  **Hashed Payload** value that is used to calculate the signature of **Canonical Request**. The **Hashed Payload** value is the fixed character string: **UNSIGNED-PAYLOAD**.

