# Create or Replace Object<a name="obs_03_0058"></a>

Creating an object refers to creating an object in a specified container. In a container, each object must have a unique name. However, objects in different containers can have the same name. If you use this operation on an existing object, you replace the existing object and metadata, and delete the original metadata.

## Method<a name="section39869956112928"></a>

**Table  1**  Method description

<a name="table36630378113016"></a>
<table><thead align="left"><tr id="row48730343113016"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p5336715811413"><a name="p5336715811413"></a><a name="p5336715811413"></a>Method</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p51296332113016"><a name="p51296332113016"></a><a name="p51296332113016"></a><strong id="b39273688114629"><a name="b39273688114629"></a><a name="b39273688114629"></a>URI</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p61362190113016"><a name="p61362190113016"></a><a name="p61362190113016"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row15388804113016"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p38533588113016"><a name="p38533588113016"></a><a name="p38533588113016"></a>PUT</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p52757727113245"><a name="p52757727113245"></a><a name="p52757727113245"></a>/v1/{account}/{container}/{object}{?temp_url_sig,temp_url_expires,multipart-manifest}</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p19784190113016"><a name="p19784190113016"></a><a name="p19784190113016"></a>Creates an object in the specified container.</p>
</td>
</tr>
</tbody>
</table>

**\{account\}**  indicates the name of an account.  **\{container\}**  indicates the name of a container.  **\{object\}**  indicates the name of an object.

The request body of this operation is the object content.

## Example Request<a name="section16623225"></a>

Create an object:

```
curl -i $publicURL/marktwain/helloworld.txt -X PUT 
 -H "X-Auth-Token: $token"
```

## Request Query Parameters<a name="section5103708"></a>

[Table 2](#table21447202143412)  describes the query parameters for getting the object content:

**Table  2**  Request query parameters

<a name="table21447202143412"></a>
<table><thead align="left"><tr id="row59154676143412"><th class="cellrowborder" valign="top" width="18.05%" id="mcps1.2.5.1.1"><p id="p26799486143412"><a name="p26799486143412"></a><a name="p26799486143412"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="9.46%" id="mcps1.2.5.1.2"><p id="p8146475143412"><a name="p8146475143412"></a><a name="p8146475143412"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="58.599999999999994%" id="mcps1.2.5.1.3"><p id="p33200335143412"><a name="p33200335143412"></a><a name="p33200335143412"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="13.889999999999999%" id="mcps1.2.5.1.4"><p id="p43853575143412"><a name="p43853575143412"></a><a name="p43853575143412"></a>Required or Not</p>
</th>
</tr>
</thead>
<tbody><tr id="row25436980143412"><td class="cellrowborder" valign="top" width="18.05%" headers="mcps1.2.5.1.1 "><p id="p47129522143412"><a name="p47129522143412"></a><a name="p47129522143412"></a>temp_url_sig</p>
</td>
<td class="cellrowborder" valign="top" width="9.46%" headers="mcps1.2.5.1.2 "><p id="p59394912143412"><a name="p59394912143412"></a><a name="p59394912143412"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.599999999999994%" headers="mcps1.2.5.1.3 "><p id="p46258534143412"><a name="p46258534143412"></a><a name="p46258534143412"></a>Used with TempURL to sign the request.</p>
</td>
<td class="cellrowborder" valign="top" width="13.889999999999999%" headers="mcps1.2.5.1.4 "><p id="p55953773143412"><a name="p55953773143412"></a><a name="p55953773143412"></a>No</p>
</td>
</tr>
<tr id="row33821912143412"><td class="cellrowborder" valign="top" width="18.05%" headers="mcps1.2.5.1.1 "><p id="p55220355143412"><a name="p55220355143412"></a><a name="p55220355143412"></a>temp_url_expires</p>
</td>
<td class="cellrowborder" valign="top" width="9.46%" headers="mcps1.2.5.1.2 "><p id="p43663746143412"><a name="p43663746143412"></a><a name="p43663746143412"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.599999999999994%" headers="mcps1.2.5.1.3 "><p id="p47102526143412"><a name="p47102526143412"></a><a name="p47102526143412"></a>Used with TempURL to specify the expiry time of the signature.</p>
</td>
<td class="cellrowborder" valign="top" width="13.889999999999999%" headers="mcps1.2.5.1.4 "><p id="p57208222143412"><a name="p57208222143412"></a><a name="p57208222143412"></a>No</p>
</td>
</tr>
<tr id="row45111951143412"><td class="cellrowborder" valign="top" width="18.05%" headers="mcps1.2.5.1.1 "><p id="p30189409143412"><a name="p30189409143412"></a><a name="p30189409143412"></a>multipart-manifest</p>
</td>
<td class="cellrowborder" valign="top" width="9.46%" headers="mcps1.2.5.1.2 "><p id="p29423051143412"><a name="p29423051143412"></a><a name="p29423051143412"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.599999999999994%" headers="mcps1.2.5.1.3 "><p id="p34456950143412"><a name="p34456950143412"></a><a name="p34456950143412"></a>If <strong id="b18330915"><a name="b18330915"></a><a name="b18330915"></a>multipart-manifest=put</strong> is set, the object is a static large object manifest and the body contains the manifest.</p>
</td>
<td class="cellrowborder" valign="top" width="13.889999999999999%" headers="mcps1.2.5.1.4 "><p id="p39549578143412"><a name="p39549578143412"></a><a name="p39549578143412"></a>No</p>
</td>
</tr>
</tbody>
</table>

## Request Headers<a name="section2186955"></a>

Request URI parameters

<a name="table20938788155054"></a>
<table><thead align="left"><tr id="row7298938155054"><th class="cellrowborder" valign="top" width="20.66%" id="mcps1.1.4.1.1"><p id="p54343123155054"><a name="p54343123155054"></a><a name="p54343123155054"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.399999999999999%" id="mcps1.1.4.1.2"><p id="p21906988155054"><a name="p21906988155054"></a><a name="p21906988155054"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="64.94%" id="mcps1.1.4.1.3"><p id="p65393599155054"><a name="p65393599155054"></a><a name="p65393599155054"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row24640471155054"><td class="cellrowborder" valign="top" width="20.66%" headers="mcps1.1.4.1.1 "><p id="p49721145155054"><a name="p49721145155054"></a><a name="p49721145155054"></a>{account}</p>
</td>
<td class="cellrowborder" valign="top" width="14.399999999999999%" headers="mcps1.1.4.1.2 "><p id="p880968155054"><a name="p880968155054"></a><a name="p880968155054"></a>String</p>
<p id="p7928715155054"><a name="p7928715155054"></a><a name="p7928715155054"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.1.4.1.3 "><p id="p38246216155054"><a name="p38246216155054"></a><a name="p38246216155054"></a>Unique name of the account. In the current version, it indicates the unique ID of the account.</p>
</td>
</tr>
<tr id="row8671627155054"><td class="cellrowborder" valign="top" width="20.66%" headers="mcps1.1.4.1.1 "><p id="p31313167155054"><a name="p31313167155054"></a><a name="p31313167155054"></a>{container}</p>
</td>
<td class="cellrowborder" valign="top" width="14.399999999999999%" headers="mcps1.1.4.1.2 "><p id="p53338592155054"><a name="p53338592155054"></a><a name="p53338592155054"></a>String</p>
<p id="p10285280155054"><a name="p10285280155054"></a><a name="p10285280155054"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.1.4.1.3 "><p id="p27801358155054"><a name="p27801358155054"></a><a name="p27801358155054"></a>Unique name of the container.</p>
<p id="p48885638155054"><a name="p48885638155054"></a><a name="p48885638155054"></a>For details about container naming rules, see <a href="naming-rules.md">Naming Rules</a>.</p>
</td>
</tr>
<tr id="row313773155054"><td class="cellrowborder" valign="top" width="20.66%" headers="mcps1.1.4.1.1 "><p id="p25415615155054"><a name="p25415615155054"></a><a name="p25415615155054"></a>{object}</p>
</td>
<td class="cellrowborder" valign="top" width="14.399999999999999%" headers="mcps1.1.4.1.2 "><p id="p45398950155054"><a name="p45398950155054"></a><a name="p45398950155054"></a>String</p>
<p id="p5937373155054"><a name="p5937373155054"></a><a name="p5937373155054"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.1.4.1.3 "><p id="p11165214155054"><a name="p11165214155054"></a><a name="p11165214155054"></a>Name of the object.</p>
<p id="p33378066155054"><a name="p33378066155054"></a><a name="p33378066155054"></a>For details about object naming rules, see <a href="naming-rules.md#section23579102">Object Naming Rules</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Request header parameters

<a name="table2213898993436"></a>
<table><thead align="left"><tr id="row2383841493436"><th class="cellrowborder" valign="top" width="36.54%" id="mcps1.2.4.1.1"><p id="p5186338393436"><a name="p5186338393436"></a><a name="p5186338393436"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="16.939999999999998%" id="mcps1.2.4.1.2"><p id="p2611644893436"><a name="p2611644893436"></a><a name="p2611644893436"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="46.52%" id="mcps1.2.4.1.3"><p id="p4708242393436"><a name="p4708242393436"></a><a name="p4708242393436"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row3814052016141"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p5685283816144"><a name="p5685283816144"></a><a name="p5685283816144"></a>X-Auth-Token</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p4167717016144"><a name="p4167717016144"></a><a name="p4167717016144"></a>String</p>
<p id="p3955021416144"><a name="p3955021416144"></a><a name="p3955021416144"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p4945073316144"><a name="p4945073316144"></a><a name="p4945073316144"></a>Authentication token.</p>
</td>
</tr>
<tr id="row4968641311486"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p6517651711486"><a name="p6517651711486"></a><a name="p6517651711486"></a>X-Object-Meta-name</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p4480653811486"><a name="p4480653811486"></a><a name="p4480653811486"></a>String</p>
<p id="p27124764155127"><a name="p27124764155127"></a><a name="p27124764155127"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p545094711486"><a name="p545094711486"></a><a name="p545094711486"></a>Object metadata, where <strong id="b1762272501142013"><a name="b1762272501142013"></a><a name="b1762272501142013"></a>{name}</strong> is the name of the metadata item. To delete this item, send an empty value in this header. You must specify an <strong id="b48314965"><a name="b48314965"></a><a name="b48314965"></a>X-Object-Meta-{name}</strong> header for each metadata item (for each <strong id="b32181504"><a name="b32181504"></a><a name="b32181504"></a>{name}</strong>) that you want to add or update.</p>
</td>
</tr>
<tr id="row25807474114824"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p10030672114824"><a name="p10030672114824"></a><a name="p10030672114824"></a>Content-Type</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p7178078114824"><a name="p7178078114824"></a><a name="p7178078114824"></a>String</p>
<p id="p24211892155138"><a name="p24211892155138"></a><a name="p24211892155138"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p44553412114824"><a name="p44553412114824"></a><a name="p44553412114824"></a>Sets the MIME type of the object.</p>
</td>
</tr>
<tr id="row21879157114848"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p27381313114848"><a name="p27381313114848"></a><a name="p27381313114848"></a>X-Detect-Content-Type</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p3293914114848"><a name="p3293914114848"></a><a name="p3293914114848"></a>Boolean</p>
<p id="p49629676155141"><a name="p49629676155141"></a><a name="p49629676155141"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p65480487114848"><a name="p65480487114848"></a><a name="p65480487114848"></a>If it is set to <strong id="b4892200"><a name="b4892200"></a><a name="b4892200"></a>true</strong>, OBS guesses the content type based on the file name extension and ignores the value sent in the <strong id="b44029805"><a name="b44029805"></a><a name="b44029805"></a>Content-Type</strong> header, if present.</p>
</td>
</tr>
<tr id="row17969257114918"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p46223730114918"><a name="p46223730114918"></a><a name="p46223730114918"></a>If-None-Match</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p53134619114918"><a name="p53134619114918"></a><a name="p53134619114918"></a>String</p>
<p id="p50459426155146"><a name="p50459426155146"></a><a name="p50459426155146"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p11758873115557"><a name="p11758873115557"></a><a name="p11758873115557"></a>Only an <strong id="b58515109"><a name="b58515109"></a><a name="b58515109"></a>If-None-Match: *</strong> header can be specified. If an object already exists, the object fails to be created and a 412 status code is returned.</p>
</td>
</tr>
<tr id="row6571188214568"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p2106220114568"><a name="p2106220114568"></a><a name="p2106220114568"></a>X-Object-Manifest</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p2831670914568"><a name="p2831670914568"></a><a name="p2831670914568"></a>String</p>
<p id="p14630575155148"><a name="p14630575155148"></a><a name="p14630575155148"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p5280846145718"><a name="p5280846145718"></a><a name="p5280846145718"></a>Set to specify that this is a dynamic large object manifest object. The value is the container and object name prefix of the segment objects in the form of <em id="i1338325061142219"><a name="i1338325061142219"></a><a name="i1338325061142219"></a>container/prefix</em>. The UTF-8 encoding format must be used.</p>
</td>
</tr>
<tr id="row9176580145948"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p5105498145948"><a name="p5105498145948"></a><a name="p5105498145948"></a>Content-Length</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p10892230145948"><a name="p10892230145948"></a><a name="p10892230145948"></a>String</p>
<p id="p24680746155150"><a name="p24680746155150"></a><a name="p24680746155150"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p9855405145948"><a name="p9855405145948"></a><a name="p9855405145948"></a>Set to the length of the object content. Do not set if chunked transfer encoding is being used.</p>
</td>
</tr>
<tr id="row3910282215125"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p1321203615125"><a name="p1321203615125"></a><a name="p1321203615125"></a>Transfer-Encoding</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p6354197015125"><a name="p6354197015125"></a><a name="p6354197015125"></a>String</p>
<p id="p47544805155153"><a name="p47544805155153"></a><a name="p47544805155153"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p4662591215125"><a name="p4662591215125"></a><a name="p4662591215125"></a>Set to <strong id="b37078712"><a name="b37078712"></a><a name="b37078712"></a>chunked</strong> to enable chunked transfer encoding. If used, the <strong id="b2130495650142348"><a name="b2130495650142348"></a><a name="b2130495650142348"></a>Content-Length</strong> header is ignored.</p>
</td>
</tr>
<tr id="row61594862151320"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p23127957151320"><a name="p23127957151320"></a><a name="p23127957151320"></a>X-Copy-From</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p61425191151320"><a name="p61425191151320"></a><a name="p61425191151320"></a>String</p>
<p id="p24362120155156"><a name="p24362120155156"></a><a name="p24362120155156"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p727792152047"><a name="p727792152047"></a><a name="p727792152047"></a>The format is {container}/{object}. When this header is set, {container}/{object} is copied to create an object. The UTF-8 encoding format must be used.</p>
<p id="p46800850161740"><a name="p46800850161740"></a><a name="p46800850161740"></a>Using <strong id="b62710946014282"><a name="b62710946014282"></a><a name="b62710946014282"></a>PUT</strong> with <strong id="b153332216214282"><a name="b153332216214282"></a><a name="b153332216214282"></a>X-Copy-From</strong> has the same effect as using the <strong id="b168272620814282"><a name="b168272620814282"></a><a name="b168272620814282"></a>COPY</strong> operation to copy an object.</p>
<p id="p9384590151320"><a name="p9384590151320"></a><a name="p9384590151320"></a>Using <strong id="b1857925880154747"><a name="b1857925880154747"></a><a name="b1857925880154747"></a>PUT</strong> with <strong id="b1525796805154747"><a name="b1525796805154747"></a><a name="b1525796805154747"></a>X-Copy-From</strong> has the same effect as <strong id="b84235270615486"><a name="b84235270615486"></a><a name="b84235270615486"></a>COPY</strong> to create an object.</p>
</td>
</tr>
<tr id="row62839590152125"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p56842021152125"><a name="p56842021152125"></a><a name="p56842021152125"></a>ETag</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p40801013152125"><a name="p40801013152125"></a><a name="p40801013152125"></a>String</p>
<p id="p4822192155159"><a name="p4822192155159"></a><a name="p4822192155159"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p16547774152125"><a name="p16547774152125"></a><a name="p16547774152125"></a>MD5 checksum value of the request body. If the MD5 checksum value of the request body is equal to the value of <strong id="b1468687397142847"><a name="b1468687397142847"></a><a name="b1468687397142847"></a>ETag</strong>, the upload is successful. If not equal, a 422 status code is returned.</p>
<p id="p4116140416199"><a name="p4116140416199"></a><a name="p4116140416199"></a>It is recommended to check the MD5 checksum value for an upload.</p>
</td>
</tr>
<tr id="row59308873153414"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p39289375153414"><a name="p39289375153414"></a><a name="p39289375153414"></a>Content-Disposition</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p28322806153414"><a name="p28322806153414"></a><a name="p28322806153414"></a>String</p>
<p id="p292305315521"><a name="p292305315521"></a><a name="p292305315521"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p12445941153414"><a name="p12445941153414"></a><a name="p12445941153414"></a>Sets the value to <strong id="b8640850"><a name="b8640850"></a><a name="b8640850"></a>{newname}</strong>. When an object is downloaded through a browser, the default object name <strong id="b516206548142932"><a name="b516206548142932"></a><a name="b516206548142932"></a>{newname}</strong> is returned.</p>
</td>
</tr>
<tr id="row1381650115387"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p4539478315387"><a name="p4539478315387"></a><a name="p4539478315387"></a>Content-Encoding</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p5309882615387"><a name="p5309882615387"></a><a name="p5309882615387"></a>String</p>
<p id="p3426566415524"><a name="p3426566415524"></a><a name="p3426566415524"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p603766215387"><a name="p603766215387"></a><a name="p603766215387"></a>If this header is set, the value is the encoding format used when an object is downloaded through a browser.</p>
</td>
</tr>
</tbody>
</table>

>![](/images/icon-note.gif) **NOTE:**   
>If chunked transfer encoding is used and the value of  **Content-Length**  in a request is greater than the actual length of an object to be uploaded, OBS \(compatible with OpenStack Swift\) returns a 201 status code to indicate that the object is created successfully. In the same scenario, however, OpenStack Swift returns a 408 \(Request Timeout\) status code but the object is created successfully.  

## Response Headers<a name="section30570743"></a>

<a name="table16031651162224"></a>
<table><thead align="left"><tr id="row15369639162224"><th class="cellrowborder" valign="top" width="24.177582241775823%" id="mcps1.1.4.1.1"><p id="p36981265162224"><a name="p36981265162224"></a><a name="p36981265162224"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="18.7981201879812%" id="mcps1.1.4.1.2"><p id="p22196875162259"><a name="p22196875162259"></a><a name="p22196875162259"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="57.02429757024298%" id="mcps1.1.4.1.3"><p id="p42692479162224"><a name="p42692479162224"></a><a name="p42692479162224"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row35538778162224"><td class="cellrowborder" valign="top" width="24.177582241775823%" headers="mcps1.1.4.1.1 "><p id="p60068745162224"><a name="p60068745162224"></a><a name="p60068745162224"></a>Content-Length</p>
</td>
<td class="cellrowborder" valign="top" width="18.7981201879812%" headers="mcps1.1.4.1.2 "><p id="p53116488162259"><a name="p53116488162259"></a><a name="p53116488162259"></a>String</p>
<p id="p45093393162316"><a name="p45093393162316"></a><a name="p45093393162316"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="57.02429757024298%" headers="mcps1.1.4.1.3 "><p id="p33730165162224"><a name="p33730165162224"></a><a name="p33730165162224"></a>If the operation succeeds, this value is 0.</p>
<p id="p38242298162446"><a name="p38242298162446"></a><a name="p38242298162446"></a>If the operation fails, this value is the length of the error text in the response body.</p>
</td>
</tr>
<tr id="row11471508162531"><td class="cellrowborder" valign="top" width="24.177582241775823%" headers="mcps1.1.4.1.1 "><p id="p36134709162531"><a name="p36134709162531"></a><a name="p36134709162531"></a>Etag</p>
</td>
<td class="cellrowborder" valign="top" width="18.7981201879812%" headers="mcps1.1.4.1.2 "><p id="p38885166162539"><a name="p38885166162539"></a><a name="p38885166162539"></a>String</p>
<p id="p14422176162539"><a name="p14422176162539"></a><a name="p14422176162539"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="57.02429757024298%" headers="mcps1.1.4.1.3 "><p id="p51324572162531"><a name="p51324572162531"></a><a name="p51324572162531"></a>For ordinary objects, this value is the MD5 checksum of the uploaded object content.</p>
<p id="p50500432162628"><a name="p50500432162628"></a><a name="p50500432162628"></a>For static large objects, this value is the MD5 checksum of the concatenated string of MD5 checksums for each of the segments.</p>
<p id="p16674431162731"><a name="p16674431162731"></a><a name="p16674431162731"></a>For dynamic large objects, the value is the MD5 checksum of the manifest file.</p>
</td>
</tr>
<tr id="row27446062162224"><td class="cellrowborder" valign="top" width="24.177582241775823%" headers="mcps1.1.4.1.1 "><p id="p8538544162224"><a name="p8538544162224"></a><a name="p8538544162224"></a>Content-Type</p>
</td>
<td class="cellrowborder" valign="top" width="18.7981201879812%" headers="mcps1.1.4.1.2 "><p id="p34894691162334"><a name="p34894691162334"></a><a name="p34894691162334"></a>String</p>
<p id="p45616764162334"><a name="p45616764162334"></a><a name="p45616764162334"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="57.02429757024298%" headers="mcps1.1.4.1.3 "><p id="p20533450162224"><a name="p20533450162224"></a><a name="p20533450162224"></a>MIME type of the object.</p>
</td>
</tr>
<tr id="row3608914162224"><td class="cellrowborder" valign="top" width="24.177582241775823%" headers="mcps1.1.4.1.1 "><p id="p23886641162224"><a name="p23886641162224"></a><a name="p23886641162224"></a>Date</p>
</td>
<td class="cellrowborder" valign="top" width="18.7981201879812%" headers="mcps1.1.4.1.2 "><p id="p42567954162335"><a name="p42567954162335"></a><a name="p42567954162335"></a>Datetime</p>
<p id="p47567272162335"><a name="p47567272162335"></a><a name="p47567272162335"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="57.02429757024298%" headers="mcps1.1.4.1.3 "><p id="p55769764162224"><a name="p55769764162224"></a><a name="p55769764162224"></a>Transaction date and time.</p>
</td>
</tr>
<tr id="row55295670162224"><td class="cellrowborder" valign="top" width="24.177582241775823%" headers="mcps1.1.4.1.1 "><p id="p49764267162224"><a name="p49764267162224"></a><a name="p49764267162224"></a>X-Trans-Id</p>
</td>
<td class="cellrowborder" valign="top" width="18.7981201879812%" headers="mcps1.1.4.1.2 "><p id="p49172077162355"><a name="p49172077162355"></a><a name="p49172077162355"></a>Uuid</p>
<p id="p39895516162355"><a name="p39895516162355"></a><a name="p39895516162355"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="57.02429757024298%" headers="mcps1.1.4.1.3 "><p id="p4373841162224"><a name="p4373841162224"></a><a name="p4373841162224"></a>Unique transaction identifier.</p>
<p id="p39364574162224"><a name="p39364574162224"></a><a name="p39364574162224"></a></p>
</td>
</tr>
<tr id="row18736847162224"><td class="cellrowborder" valign="top" width="24.177582241775823%" headers="mcps1.1.4.1.1 "><p id="p41289678162224"><a name="p41289678162224"></a><a name="p41289678162224"></a>X-Timestamp</p>
</td>
<td class="cellrowborder" valign="top" width="18.7981201879812%" headers="mcps1.1.4.1.2 "><p id="p54910478162259"><a name="p54910478162259"></a><a name="p54910478162259"></a>Datetime</p>
<p id="p31618078162346"><a name="p31618078162346"></a><a name="p31618078162346"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="57.02429757024298%" headers="mcps1.1.4.1.3 "><p id="p17123915163011"><a name="p17123915163011"></a><a name="p17123915163011"></a>Object creation time and date, in UNIX Epoch timestamp format.</p>
</td>
</tr>
</tbody>
</table>

## Create Object<a name="section2201390"></a>

Create  **marktwain/goodbye**:

```
curl -i http://172.28.54.12:80/v1/AUTH_4b34aa268d8c45879cf4da16443d3f95/marketwain/goodbye -H "X-Auth-Token:74565091b56b4783818430cecb283e7f"  -XPUT -T ./goodbye.txt
```

```
HTTP/1.1 201 Created
X-Trans-Id: tx000001513c8f12fd370c0-b7e3f340fc
Content-Type: text/html;charset=UTF-8
Date: Wed, 25 Nov 2015 02:53:08 GMT
ETag: e85f5c28b588fa64a379ba876e3591d2
Last-Modified: Wed, 25 Nov 2015 02:53:08 GMT
Content-Length: 0
```

## Replace Object<a name="section60098234144536"></a>

Replace  **marktwain/goodbye**  \(repeated creation\):

```
curl -i http://172.28.54.12:80/v1/AUTH_4b34aa268d8c45879cf4da16443d3f95/marketwain/goodbye -H "X-Auth-Token:74565091b56b4783818430cecb283e7f"  -XPUT -T ./goodbye.txt
```

```
HTTP/1.1 201 Created
X-Trans-Id: tx000001513c99de91370c0-8a64466f2c
Content-Type: text/html;charset=UTF-8
Date: Wed, 25 Nov 2015 03:04:55 GMT
ETag: e85f5c28b588fa64a379ba876e3591d2
Last-Modified: Wed, 25 Nov 2015 03:04:55 GMT
Content-Length: 0
```

