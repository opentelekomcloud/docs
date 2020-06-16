# SSE-C<a name="EN-US_TOPIC_0125560282"></a>

In SSE-C mode, OBS uses the keys and MD5 values provided by customers for server-side encryption.

OBS does not store your encryption keys. If you lost your encryption keys, you lost the objects. Six headers are added to support SSE-C.

[Table 1](#table44557321113316)  lists headers that are mandatory when you use SSE-C to encrypt objects.

**Table  1**  Mandatory headers in SSE-C mode

<a name="table44557321113316"></a>
<table><thead align="left"><tr id="row239914398"><th class="cellrowborder" valign="top" width="26.26%" id="mcps1.2.3.1.1"><p id="p839915390"><a name="p839915390"></a><a name="p839915390"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="73.74000000000001%" id="mcps1.2.3.1.2"><p id="p639181173919"><a name="p639181173919"></a><a name="p639181173919"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row62234724113316"><td class="cellrowborder" valign="top" width="26.26%" headers="mcps1.2.3.1.1 "><p id="p7847870113316"><a name="p7847870113316"></a><a name="p7847870113316"></a>x-amz-server-side-encryption-customer-algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="73.74000000000001%" headers="mcps1.2.3.1.2 "><p id="p31697753113316"><a name="p31697753113316"></a><a name="p31697753113316"></a>Indicates the algorithm used to encrypt an object. The header is used in SSE-C mode.</p>
<p id="p127523417618"><a name="p127523417618"></a><a name="p127523417618"></a>Example:</p>
<p id="p16844326113316"><a name="p16844326113316"></a><a name="p16844326113316"></a>x-amz-server-side-encryption-customer-algorithm:AES256</p>
</td>
</tr>
<tr id="row17381213113316"><td class="cellrowborder" valign="top" width="26.26%" headers="mcps1.2.3.1.1 "><p id="p65700976113316"><a name="p65700976113316"></a><a name="p65700976113316"></a>x-amz-server-side-encryption-customer-key</p>
</td>
<td class="cellrowborder" valign="top" width="73.74000000000001%" headers="mcps1.2.3.1.2 "><p id="p20178877113316"><a name="p20178877113316"></a><a name="p20178877113316"></a>Indicates the key used to encrypt an object. The header is used in SSE-C mode.</p>
<p id="p66180292399"><a name="p66180292399"></a><a name="p66180292399"></a>Example:</p>
<p id="p14819361262"><a name="p14819361262"></a><a name="p14819361262"></a>x-amz-server-side-encryption-customer-key:K7QkYpBkM5+hcs27fsNkUnNVaobncnLht/rCB2o/9Cw=</p>
</td>
</tr>
<tr id="row23876330113316"><td class="cellrowborder" valign="top" width="26.26%" headers="mcps1.2.3.1.1 "><p id="p54934559113316"><a name="p54934559113316"></a><a name="p54934559113316"></a>x-amz-server-side-encryption-customer-key-MD5</p>
</td>
<td class="cellrowborder" valign="top" width="73.74000000000001%" headers="mcps1.2.3.1.2 "><p id="p20514309113316"><a name="p20514309113316"></a><a name="p20514309113316"></a>Indicates the MD5 value of the key used to encrypt an object. The header is used in SSE-C mode. The MD5 value is used to check whether any error occurs during the transmission of the key.</p>
<p id="p33021432203915"><a name="p33021432203915"></a><a name="p33021432203915"></a>Example:</p>
<p id="p17705581362"><a name="p17705581362"></a><a name="p17705581362"></a>x-amz-server-side-encryption-customer-key-MD5:4XvB3tbNTN+tIEVa0/fGaQ==</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  Interfaces to which the newly added headers apply

<a name="table2731902311349"></a>
<table><thead align="left"><tr id="row6526771511349"><th class="cellrowborder" valign="top" width="100%" id="mcps1.2.2.1.1"><p id="p5219358711349"><a name="p5219358711349"></a><a name="p5219358711349"></a>Interface</p>
</th>
</tr>
</thead>
<tbody><tr id="row6693103611349"><td class="cellrowborder" valign="top" width="100%" headers="mcps1.2.2.1.1 "><p id="p5270480511349"><a name="p5270480511349"></a><a name="p5270480511349"></a>PUT Object</p>
</td>
</tr>
<tr id="row458119711349"><td class="cellrowborder" valign="top" width="100%" headers="mcps1.2.2.1.1 "><p id="p3553264911349"><a name="p3553264911349"></a><a name="p3553264911349"></a>POST Object</p>
</td>
</tr>
<tr id="row5135839211349"><td class="cellrowborder" valign="top" width="100%" headers="mcps1.2.2.1.1 "><p id="p6638907411349"><a name="p6638907411349"></a><a name="p6638907411349"></a>PUT Object - Copy (the newly added headers apply to target objects)</p>
</td>
</tr>
<tr id="row6063076011349"><td class="cellrowborder" valign="top" width="100%" headers="mcps1.2.2.1.1 "><p id="p1214453811349"><a name="p1214453811349"></a><a name="p1214453811349"></a>HEAD Object</p>
</td>
</tr>
<tr id="row4219198511349"><td class="cellrowborder" valign="top" width="100%" headers="mcps1.2.2.1.1 "><p id="p6210758811349"><a name="p6210758811349"></a><a name="p6210758811349"></a>GET Object</p>
</td>
</tr>
<tr id="row2209738811349"><td class="cellrowborder" valign="top" width="100%" headers="mcps1.2.2.1.1 "><p id="p4505801211349"><a name="p4505801211349"></a><a name="p4505801211349"></a>Initiate Multipart Upload</p>
</td>
</tr>
<tr id="row286892611349"><td class="cellrowborder" valign="top" width="100%" headers="mcps1.2.2.1.1 "><p id="p3105643511349"><a name="p3105643511349"></a><a name="p3105643511349"></a>Upload Part</p>
</td>
</tr>
<tr id="row1107246511349"><td class="cellrowborder" valign="top" width="100%" headers="mcps1.2.2.1.1 "><p id="p2445443811349"><a name="p2445443811349"></a><a name="p2445443811349"></a>Upload Part - Copy (the newly added headers apply to target parts)</p>
</td>
</tr>
</tbody>
</table>

[Table 3](#table50397498113431)  lists three headers that are added for PUT Object - Copy and Upload Part - Copy interfaces to support source objects encrypted using SSE-C.

**Table  3**  Headers

<a name="table50397498113431"></a>
<table><thead align="left"><tr id="row101932046143919"><th class="cellrowborder" valign="top" width="26.26%" id="mcps1.2.3.1.1"><p id="p1019313469398"><a name="p1019313469398"></a><a name="p1019313469398"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="73.74000000000001%" id="mcps1.2.3.1.2"><p id="p191938463398"><a name="p191938463398"></a><a name="p191938463398"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row46440433113431"><td class="cellrowborder" valign="top" width="26.26%" headers="mcps1.2.3.1.1 "><p id="p3578718113431"><a name="p3578718113431"></a><a name="p3578718113431"></a>x-amz-copy-source-server-side-encryption-customer-algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="73.74000000000001%" headers="mcps1.2.3.1.2 "><p id="p21440723113431"><a name="p21440723113431"></a><a name="p21440723113431"></a>Indicates the algorithm used to decrypt a source object. The header is used in SSE-C mode.</p>
<p id="p58748785113431"><a name="p58748785113431"></a><a name="p58748785113431"></a>Example: x-amz-copy-source-server-side-encryption-customer-algorithm:AES256</p>
</td>
</tr>
<tr id="row58977017113431"><td class="cellrowborder" valign="top" width="26.26%" headers="mcps1.2.3.1.1 "><p id="p12409079113431"><a name="p12409079113431"></a><a name="p12409079113431"></a>x-amz-copy-source-server-side-encryption-customer-key</p>
</td>
<td class="cellrowborder" valign="top" width="73.74000000000001%" headers="mcps1.2.3.1.2 "><p id="p65611382113431"><a name="p65611382113431"></a><a name="p65611382113431"></a>Indicates the key used to decrypt a source object. The header is used in SSE-C mode.</p>
<p id="p8162304408"><a name="p8162304408"></a><a name="p8162304408"></a>Example:</p>
<p id="p53631534113431"><a name="p53631534113431"></a><a name="p53631534113431"></a>x-amz-copy-source-server-side-encryption-customer-key:K7QkYpBkM5+hcs27fsNkUnNVaobncnLht/rCB2o/9Cw=</p>
</td>
</tr>
<tr id="row12921758113431"><td class="cellrowborder" valign="top" width="26.26%" headers="mcps1.2.3.1.1 "><p id="p40029462113431"><a name="p40029462113431"></a><a name="p40029462113431"></a>x-amz-copy-source-server-side-encryption-customer-key-MD5</p>
</td>
<td class="cellrowborder" valign="top" width="73.74000000000001%" headers="mcps1.2.3.1.2 "><p id="p21160966113431"><a name="p21160966113431"></a><a name="p21160966113431"></a>Indicates the MD5 value of the key used to decrypt a source object. The header is used in SSE-C mode. The MD5 value is used to check whether any error occurs during the transmission of the key.</p>
<p id="p044719212404"><a name="p044719212404"></a><a name="p044719212404"></a>Example:</p>
<p id="p56230971113431"><a name="p56230971113431"></a><a name="p56230971113431"></a>x-amz-copy-source-server-side-encryption-customer-key-MD5:4XvB3tbNTN+tIEVa0/fGaQ==</p>
</td>
</tr>
</tbody>
</table>

