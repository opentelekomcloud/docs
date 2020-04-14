# V4 Browser-based Authorized POST Request<a name="EN-US_TOPIC_0125560309"></a>

OBS supports browser-based  **POST**  object uploading requests. The authentication information about these requests is uploaded by a form. [Table 1](#table27141505)  lists the mandatory parameters.

**Table  1**  V4 POST uploading authentication parameters in the form

<a name="table27141505"></a>
<table><thead align="left"><tr id="row53734669"><th class="cellrowborder" valign="top" width="35.15%" id="mcps1.2.3.1.1"><p id="p57540904"><a name="p57540904"></a><a name="p57540904"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="64.85%" id="mcps1.2.3.1.2"><p id="p30301652"><a name="p30301652"></a><a name="p30301652"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row38514744"><td class="cellrowborder" valign="top" width="35.15%" headers="mcps1.2.3.1.1 "><p id="p32686589"><a name="p32686589"></a><a name="p32686589"></a>Policy</p>
</td>
<td class="cellrowborder" valign="top" width="64.85%" headers="mcps1.2.3.1.2 "><p id="p30368075"><a name="p30368075"></a><a name="p30368075"></a>The value of this parameter is a code in Base64 format. It is the code of the security policy of this request.</p>
</td>
</tr>
<tr id="row4877220"><td class="cellrowborder" valign="top" width="35.15%" headers="mcps1.2.3.1.1 "><p id="p59510545"><a name="p59510545"></a><a name="p59510545"></a>x-amz-algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="64.85%" headers="mcps1.2.3.1.2 "><p id="p55624859"><a name="p55624859"></a><a name="p55624859"></a>Indicates a signature algorithm. For a V4 signature, the value of the parameter is fixed to <strong id="b30861686"><a name="b30861686"></a><a name="b30861686"></a>AWS4-HMAC-SHA256</strong>.</p>
</td>
</tr>
<tr id="row9319721"><td class="cellrowborder" valign="top" width="35.15%" headers="mcps1.2.3.1.1 "><p id="p16699940"><a name="p16699940"></a><a name="p16699940"></a>x-amz-credential</p>
</td>
<td class="cellrowborder" valign="top" width="64.85%" headers="mcps1.2.3.1.2 "><p id="p10517875"><a name="p10517875"></a><a name="p10517875"></a>In addition to the <strong id="b27552014"><a name="b27552014"></a><a name="b27552014"></a>access key ID</strong>, region and service information must be provided. The information must be the same as that used to calculate the <strong id="b4466122517520"><a name="b4466122517520"></a><a name="b4466122517520"></a>Signing Key</strong>. The value of this parameter is expressed in the following format:</p>
<p id="p17120631"><a name="p17120631"></a><a name="p17120631"></a>&lt;your-access-key-id&gt;/&lt;date&gt;/&lt;AWS-region&gt;/&lt;AWS-service&gt;/aws4_request.OBS region</p>
<p id="p19867951"><a name="p19867951"></a><a name="p19867951"></a>The value is the same as that used for common authentication.</p>
<p id="p44593832"><a name="p44593832"></a><a name="p44593832"></a>Example:</p>
<p id="p65800171"><a name="p65800171"></a><a name="p65800171"></a>AKIAIOSFODNN7EXAMPLE/20150721/region-1/s3/aws4_request.</p>
</td>
</tr>
<tr id="row55330634"><td class="cellrowborder" valign="top" width="35.15%" headers="mcps1.2.3.1.1 "><p id="p52596356"><a name="p52596356"></a><a name="p52596356"></a>x-amz-date</p>
</td>
<td class="cellrowborder" valign="top" width="64.85%" headers="mcps1.2.3.1.2 "><p id="p32446463"><a name="p32446463"></a><a name="p32446463"></a>Indicates the request generation time. It is in the ISO 8601 format. The value must be the same as that of the <strong id="b15530630185218"><a name="b15530630185218"></a><a name="b15530630185218"></a>x-am-date</strong> field in the policy.</p>
<p id="p10917859"><a name="p10917859"></a><a name="p10917859"></a>Example:</p>
<p id="p31151867"><a name="p31151867"></a><a name="p31151867"></a>20150721T201207Z.</p>
</td>
</tr>
<tr id="row11931350"><td class="cellrowborder" valign="top" width="35.15%" headers="mcps1.2.3.1.1 "><p id="p26915331"><a name="p26915331"></a><a name="p26915331"></a>x-amz-signature</p>
</td>
<td class="cellrowborder" valign="top" width="64.85%" headers="mcps1.2.3.1.2 "><p id="p32658192"><a name="p32658192"></a><a name="p32658192"></a>Indicates the HMAC-SHA256 hash value of the policy in V4.</p>
</td>
</tr>
</tbody>
</table>

Policy is a character string in JSON format and consists of two parts:****

-   **expiration**  \(indicates the request expiration time\).
-   **conditions**  \(indicates parameter restrictions in the form\).

An example is as follows:

```
{ 
 "expiration": "2015-08-06T12:00:00.000Z", 
 "conditions": [ 
   {"bucket": "bucketname"}, 
   ["starts-with", "$key", "user/user1/"], 
   {"acl": "public-read"}, 
   {"success_action_redirect": 
"http://acl6.obs.example.com/successful_upload.html"}, 
   ["starts-with", "$Content-Type", "image/"], 
   {"x-amz-meta-uuid": "14365123651274"}, 
   ["starts-with", "$x-amz-meta-tag", ""], 
   {"x-amz-credential": "AKIAIOSFODNN7EXAMPLE/20150806/region-1/s3/aws4_request"}, 
   {"x-amz-algorithm": "AWS4-HMAC-SHA256"}, 
   {"x-amz-date": "20150806T000000Z" } 
 ] 
 }
```

[Table 2](#table42946954)  lists the mandatory parameters of Policy.

**Table  2**  Mandatory parameters of Policy in V4 POST uploading requests

<a name="table42946954"></a>
<table><thead align="left"><tr id="row63147504"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p14674162"><a name="p14674162"></a><a name="p14674162"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p47756489"><a name="p47756489"></a><a name="p47756489"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row43070429"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p66152725"><a name="p66152725"></a><a name="p66152725"></a>x-amz-algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p56770522"><a name="p56770522"></a><a name="p56770522"></a>Indicates the used signature algorithm. In V4, the value of the parameter is <strong id="b41172652"><a name="b41172652"></a><a name="b41172652"></a>AWS4-HMAC-SHA256</strong>.</p>
</td>
</tr>
<tr id="row35009555"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p17201705"><a name="p17201705"></a><a name="p17201705"></a>x-amz-credential</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p51160835"><a name="p51160835"></a><a name="p51160835"></a>In addition to the <strong id="b57794333"><a name="b57794333"></a><a name="b57794333"></a>access key ID</strong>, region and service information must be provided. The information must be the same as that used to calculate the&nbsp;<strong id="b50386953"><a name="b50386953"></a><a name="b50386953"></a>Signing Key</strong>. The value of this parameter is expressed in the following format:</p>
<p id="p50829401"><a name="p50829401"></a><a name="p50829401"></a>&lt;your-access-key-id&gt;/&lt;date&gt;/&lt;AWS-region&gt;/&lt;AWS-service&gt;/aws4_request.</p>
<p id="p54811429"><a name="p54811429"></a><a name="p54811429"></a>Example:</p>
<p id="p23540813"><a name="p23540813"></a><a name="p23540813"></a>AKIAIOSFODNN7EXAMPLE/20150721/region-1/s3/aws4_request.</p>
</td>
</tr>
<tr id="row10540732"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p48492984"><a name="p48492984"></a><a name="p48492984"></a>x-amz-date</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p35617665"><a name="p35617665"></a><a name="p35617665"></a>Indicates the Start time of the validity period of <strong id="b52123534"><a name="b52123534"></a><a name="b52123534"></a>Signing Key</strong>. The value is expressed in ISO 8601 format. The value must be the same as that of the&nbsp;<strong id="b66458622"><a name="b66458622"></a><a name="b66458622"></a>x-am-date</strong> field in the Signing Key.</p>
<p id="p61256692"><a name="p61256692"></a><a name="p61256692"></a>Example:</p>
<p id="p14439320"><a name="p14439320"></a><a name="p14439320"></a>20150721T201207Z</p>
</td>
</tr>
</tbody>
</table>

The signature calculation process of V4 POST uploading requests is similar to that of V4 common requests. The only difference lies in the  **Policy**  in the request used by **StringToSign** in V4. The **Policy** is obtained by Base64 encoding based on the original **Policy** character string. [Figure 1](#fig1971331315531)  shows the computing process.

**Figure  1**  Signature calculation process of objects uploaded using V4 POST uploading requests<a name="fig1971331315531"></a>  
![](figures/signature-calculation-process-of-objects-uploaded-using-v4-post-uploading-requests.png "signature-calculation-process-of-objects-uploaded-using-v4-post-uploading-requests")

