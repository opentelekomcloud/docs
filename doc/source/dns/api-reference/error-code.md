# Error Code<a name="EN-US_TOPIC_0088854494"></a>

## Introduction<a name="section33673592114748"></a>

When an API calling encounters an error, an error structure is returned. This section describes parameters of the DNS error code.

## Error Code Structure Format<a name="section6566165711485"></a>

```
{
    "code": "DNS.0001",
    "message": "Internal error"
}
```

## Error Code Description<a name="section16829001114854"></a>

<a name="en-us_topic_0084006833_table16297103162150"></a><table><thead align="left"><tr id="en-us_topic_0084006833_row13261892162150"><th class="cellrowborder" valign="top" width="14.04%" id="mcps1.1.6.1.1"><p id="p37215688105158"><a name="p37215688105158"></a><a name="p37215688105158"></a>Category</p>
</th>
<th class="cellrowborder" valign="top" width="12.44%" id="mcps1.1.6.1.2"><p id="p2431403311153"><a name="p2431403311153"></a><a name="p2431403311153"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="20.01%" id="mcps1.1.6.1.3"><p id="en-us_topic_0084006833_p38186090162150"><a name="en-us_topic_0084006833_p38186090162150"></a><a name="en-us_topic_0084006833_p38186090162150"></a>Error Code</p>
</th>
<th class="cellrowborder" valign="top" width="23.119999999999997%" id="mcps1.1.6.1.4"><p id="p44024730142756"><a name="p44024730142756"></a><a name="p44024730142756"></a>Error Information</p>
</th>
<th class="cellrowborder" valign="top" width="30.39%" id="mcps1.1.6.1.5"><p id="p44915791110"><a name="p44915791110"></a><a name="p44915791110"></a>Handling Measure</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0084006833_row21552931162150"><td class="cellrowborder" rowspan="22" valign="top" width="14.04%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0084006833_p957002162150"><a name="en-us_topic_0084006833_p957002162150"></a><a name="en-us_topic_0084006833_p957002162150"></a>General</p>
</td>
<td class="cellrowborder" valign="top" width="12.44%" headers="mcps1.1.6.1.2 "><p id="p2327963311153"><a name="p2327963311153"></a><a name="p2327963311153"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="20.01%" headers="mcps1.1.6.1.3 "><p id="p2992447911956"><a name="p2992447911956"></a><a name="p2992447911956"></a>DNS.0000</p>
</td>
<td class="cellrowborder" valign="top" width="23.119999999999997%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0084006833_p37771318162150"><a name="en-us_topic_0084006833_p37771318162150"></a><a name="en-us_topic_0084006833_p37771318162150"></a>Unknown error.</p>
</td>
<td class="cellrowborder" valign="top" width="30.39%" headers="mcps1.1.6.1.5 "><p id="p282736231110"><a name="p282736231110"></a><a name="p282736231110"></a>Retry the operation. If the error persists, contact customer service.</p>
</td>
</tr>
<tr id="en-us_topic_0084006833_row4397547162150"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p660213011153"><a name="p660213011153"></a><a name="p660213011153"></a>500</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p3391609011103"><a name="p3391609011103"></a><a name="p3391609011103"></a>DNS.0001</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0084006833_p62609272162150"><a name="en-us_topic_0084006833_p62609272162150"></a><a name="en-us_topic_0084006833_p62609272162150"></a>Internal error.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p84621231110"><a name="p84621231110"></a><a name="p84621231110"></a>Retry the operation. If the error persists, contact customer service.</p>
</td>
</tr>
<tr id="en-us_topic_0084006833_row26612538162150"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p6501052311153"><a name="p6501052311153"></a><a name="p6501052311153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="en-us_topic_0084006833_p8131940162150"><a name="en-us_topic_0084006833_p8131940162150"></a><a name="en-us_topic_0084006833_p8131940162150"></a>DNS.0002</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0084006833_p54707386162150"><a name="en-us_topic_0084006833_p54707386162150"></a><a name="en-us_topic_0084006833_p54707386162150"></a>Invalid request.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p41534675113210"><a name="p41534675113210"></a><a name="p41534675113210"></a>Check whether the request parameter is empty or invalid.</p>
</td>
</tr>
<tr id="en-us_topic_0084006833_row22604434162150"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p3136104511153"><a name="p3136104511153"></a><a name="p3136104511153"></a>500</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="en-us_topic_0084006833_p19019862162150"><a name="en-us_topic_0084006833_p19019862162150"></a><a name="en-us_topic_0084006833_p19019862162150"></a>DNS.0003</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0084006833_p64213883162150"><a name="en-us_topic_0084006833_p64213883162150"></a><a name="en-us_topic_0084006833_p64213883162150"></a>DB exception.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p209641261110"><a name="p209641261110"></a><a name="p209641261110"></a>Retry the operation. If the error persists, contact customer service.</p>
</td>
</tr>
<tr id="en-us_topic_0084006833_row41054041162150"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p5721674411153"><a name="p5721674411153"></a><a name="p5721674411153"></a>404</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="en-us_topic_0084006833_p37043058162150"><a name="en-us_topic_0084006833_p37043058162150"></a><a name="en-us_topic_0084006833_p37043058162150"></a>DNS.0004</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0084006833_p47697727162150"><a name="en-us_topic_0084006833_p47697727162150"></a><a name="en-us_topic_0084006833_p47697727162150"></a>No record sets found.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p203726201110"><a name="p203726201110"></a><a name="p203726201110"></a>Check whether the resource is available.</p>
</td>
</tr>
<tr id="en-us_topic_0084006833_row26626365162150"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p404466711153"><a name="p404466711153"></a><a name="p404466711153"></a>401</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="en-us_topic_0084006833_p9251956162150"><a name="en-us_topic_0084006833_p9251956162150"></a><a name="en-us_topic_0084006833_p9251956162150"></a>DNS.0005</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0084006833_p11210963162150"><a name="en-us_topic_0084006833_p11210963162150"></a><a name="en-us_topic_0084006833_p11210963162150"></a>Authentication required.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p395694901110"><a name="p395694901110"></a><a name="p395694901110"></a>1. When calling an API, check whether the token is valid.</p>
<p id="p5990265111260"><a name="p5990265111260"></a><a name="p5990265111260"></a>2. Check whether you have operation permission on the required resources.</p>
</td>
</tr>
<tr id="en-us_topic_0084006833_row33789810162150"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p5918258211153"><a name="p5918258211153"></a><a name="p5918258211153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="en-us_topic_0084006833_p52620065162150"><a name="en-us_topic_0084006833_p52620065162150"></a><a name="en-us_topic_0084006833_p52620065162150"></a>DNS.0006</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0084006833_p34366861162150"><a name="en-us_topic_0084006833_p34366861162150"></a><a name="en-us_topic_0084006833_p34366861162150"></a>The <strong id="b84235270615169"><a name="b84235270615169"></a><a name="b84235270615169"></a>limit</strong> parameter is invalid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p510121211110"><a name="p510121211110"></a><a name="p510121211110"></a>Check the value of <strong id="b842352706203318"><a name="b842352706203318"></a><a name="b842352706203318"></a>limit</strong> in the request.</p>
</td>
</tr>
<tr id="en-us_topic_0084006833_row40866293162150"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p2905984211153"><a name="p2905984211153"></a><a name="p2905984211153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="en-us_topic_0084006833_p21835398162150"><a name="en-us_topic_0084006833_p21835398162150"></a><a name="en-us_topic_0084006833_p21835398162150"></a>DNS.0007</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0084006833_p23836808162150"><a name="en-us_topic_0084006833_p23836808162150"></a><a name="en-us_topic_0084006833_p23836808162150"></a>The <strong id="b842352706151615"><a name="b842352706151615"></a><a name="b842352706151615"></a>marker</strong> parameter is invalid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p383411281110"><a name="p383411281110"></a><a name="p383411281110"></a>Check the value of <strong id="b842352706203318_1"><a name="b842352706203318_1"></a><a name="b842352706203318_1"></a>marker</strong> in the request.</p>
</td>
</tr>
<tr id="en-us_topic_0084006833_row13204682162150"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p503699811153"><a name="p503699811153"></a><a name="p503699811153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="en-us_topic_0084006833_p62946360162150"><a name="en-us_topic_0084006833_p62946360162150"></a><a name="en-us_topic_0084006833_p62946360162150"></a>DNS.0008</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0084006833_p65490410162150"><a name="en-us_topic_0084006833_p65490410162150"></a><a name="en-us_topic_0084006833_p65490410162150"></a>The zone of this type is not supported now.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p186236881110"><a name="p186236881110"></a><a name="p186236881110"></a>Check the zone type and try again.</p>
</td>
</tr>
<tr id="en-us_topic_0084006833_row52542785162150"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p534372311153"><a name="p534372311153"></a><a name="p534372311153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="en-us_topic_0084006833_p28107156162150"><a name="en-us_topic_0084006833_p28107156162150"></a><a name="en-us_topic_0084006833_p28107156162150"></a>DNS.0009</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0084006833_p62087201162150"><a name="en-us_topic_0084006833_p62087201162150"></a><a name="en-us_topic_0084006833_p62087201162150"></a>The <strong id="b842352706151729"><a name="b842352706151729"></a><a name="b842352706151729"></a>startTime</strong> parameter is invalid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p321237771110"><a name="p321237771110"></a><a name="p321237771110"></a>Check the value of <strong id="b842352706203318_2"><a name="b842352706203318_2"></a><a name="b842352706203318_2"></a>startTime</strong> in the request.</p>
</td>
</tr>
<tr id="en-us_topic_0084006833_row21913900162150"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p3018844111153"><a name="p3018844111153"></a><a name="p3018844111153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="en-us_topic_0084006833_p30195456162150"><a name="en-us_topic_0084006833_p30195456162150"></a><a name="en-us_topic_0084006833_p30195456162150"></a>DNS.0010</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0084006833_p29912865162150"><a name="en-us_topic_0084006833_p29912865162150"></a><a name="en-us_topic_0084006833_p29912865162150"></a>The <strong id="b842352706151812"><a name="b842352706151812"></a><a name="b842352706151812"></a>endTime</strong> parameter is invalid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p518891141110"><a name="p518891141110"></a><a name="p518891141110"></a>Check the value of <strong id="b842352706203318_3"><a name="b842352706203318_3"></a><a name="b842352706203318_3"></a>endTime</strong> in the request.</p>
</td>
</tr>
<tr id="en-us_topic_0084006833_row780329162150"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p2934463111153"><a name="p2934463111153"></a><a name="p2934463111153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="en-us_topic_0084006833_p63206695162150"><a name="en-us_topic_0084006833_p63206695162150"></a><a name="en-us_topic_0084006833_p63206695162150"></a>DNS.0011</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0084006833_p19468710162150"><a name="en-us_topic_0084006833_p19468710162150"></a><a name="en-us_topic_0084006833_p19468710162150"></a>The <strong id="b842352706151850"><a name="b842352706151850"></a><a name="b842352706151850"></a>start</strong> parameter is invalid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p422686671110"><a name="p422686671110"></a><a name="p422686671110"></a>Check the value of <strong id="b842352706203318_4"><a name="b842352706203318_4"></a><a name="b842352706203318_4"></a>start</strong> in the request.</p>
</td>
</tr>
<tr id="en-us_topic_0084006833_row41000670162150"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p2810487711153"><a name="p2810487711153"></a><a name="p2810487711153"></a>500</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="en-us_topic_0084006833_p32719936162150"><a name="en-us_topic_0084006833_p32719936162150"></a><a name="en-us_topic_0084006833_p32719936162150"></a>DNS.0012</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0084006833_p33069175162150"><a name="en-us_topic_0084006833_p33069175162150"></a><a name="en-us_topic_0084006833_p33069175162150"></a>An error occurred when the VPC service is called.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p12099971110"><a name="p12099971110"></a><a name="p12099971110"></a>Retry the operation. If the error persists, contact customer service.</p>
</td>
</tr>
<tr id="en-us_topic_0084006833_row29187126162150"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p6190256411153"><a name="p6190256411153"></a><a name="p6190256411153"></a>401</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="en-us_topic_0084006833_p15347015162150"><a name="en-us_topic_0084006833_p15347015162150"></a><a name="en-us_topic_0084006833_p15347015162150"></a>DNS.0013</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0084006833_p35148704162150"><a name="en-us_topic_0084006833_p35148704162150"></a><a name="en-us_topic_0084006833_p35148704162150"></a>You do not have the permission to perform this operation using the API.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p26502802113816"><a name="p26502802113816"></a><a name="p26502802113816"></a>The project of the requested resource may be frozen. Log in to the IAM console with the domain account and check whether the project status is normal.</p>
</td>
</tr>
<tr id="en-us_topic_0084006833_row47902888162150"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p4805177911153"><a name="p4805177911153"></a><a name="p4805177911153"></a>403</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="en-us_topic_0084006833_p54928705162150"><a name="en-us_topic_0084006833_p54928705162150"></a><a name="en-us_topic_0084006833_p54928705162150"></a>DNS.0014</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0084006833_p20040119162150"><a name="en-us_topic_0084006833_p20040119162150"></a><a name="en-us_topic_0084006833_p20040119162150"></a>Request forbidden by flow control.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p199465301110"><a name="p199465301110"></a><a name="p199465301110"></a>Try again some time later.</p>
</td>
</tr>
<tr id="en-us_topic_0084006833_row46143344162150"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p6698891511153"><a name="p6698891511153"></a><a name="p6698891511153"></a>500</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="en-us_topic_0084006833_p46623355162150"><a name="en-us_topic_0084006833_p46623355162150"></a><a name="en-us_topic_0084006833_p46623355162150"></a>DNS.0015</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0084006833_p18395415162150"><a name="en-us_topic_0084006833_p18395415162150"></a><a name="en-us_topic_0084006833_p18395415162150"></a>An error occurred when the IAM service is called.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p50562461110"><a name="p50562461110"></a><a name="p50562461110"></a>Retry the operation. If the error persists, contact customer service.</p>
</td>
</tr>
<tr id="en-us_topic_0084006833_row31341011162150"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p5739305211153"><a name="p5739305211153"></a><a name="p5739305211153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="en-us_topic_0084006833_p55593930162150"><a name="en-us_topic_0084006833_p55593930162150"></a><a name="en-us_topic_0084006833_p55593930162150"></a>DNS.0016</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0084006833_p6814502162150"><a name="en-us_topic_0084006833_p6814502162150"></a><a name="en-us_topic_0084006833_p6814502162150"></a>This record already exists.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p69027451110"><a name="p69027451110"></a><a name="p69027451110"></a>Check the record.</p>
</td>
</tr>
<tr id="row1816353620216"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p6196029220216"><a name="p6196029220216"></a><a name="p6196029220216"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p5272774920216"><a name="p5272774920216"></a><a name="p5272774920216"></a>DNS.0017</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p43055323202140"><a name="p43055323202140"></a><a name="p43055323202140"></a>The <strong id="b842352706105338"><a name="b842352706105338"></a><a name="b842352706105338"></a>offset</strong> parameter is invalid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p64929130202140"><a name="p64929130202140"></a><a name="p64929130202140"></a>Check the value of <strong id="b842352706203318_5"><a name="b842352706203318_5"></a><a name="b842352706203318_5"></a>offset</strong> in the request.</p>
</td>
</tr>
<tr id="row2171521710114"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p1832560511153"><a name="p1832560511153"></a><a name="p1832560511153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p3662475810131"><a name="p3662475810131"></a><a name="p3662475810131"></a>DNS.0601</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p4530505310131"><a name="p4530505310131"></a><a name="p4530505310131"></a>Invalid region.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p4583067310131"><a name="p4583067310131"></a><a name="p4583067310131"></a>Check the value of <strong id="b842352706203318_6"><a name="b842352706203318_6"></a><a name="b842352706203318_6"></a>region</strong> in the request.</p>
</td>
</tr>
<tr id="row413220610125"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p797899811153"><a name="p797899811153"></a><a name="p797899811153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p1973201410131"><a name="p1973201410131"></a><a name="p1973201410131"></a>DNS.0603</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p875043910131"><a name="p875043910131"></a><a name="p875043910131"></a>Invalid input.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p3769692810131"><a name="p3769692810131"></a><a name="p3769692810131"></a>Check whether the request parameter is empty.</p>
</td>
</tr>
<tr id="row6683200110120"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p4231909611153"><a name="p4231909611153"></a><a name="p4231909611153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p3353514810131"><a name="p3353514810131"></a><a name="p3353514810131"></a>DNS.0604</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p4125517910131"><a name="p4125517910131"></a><a name="p4125517910131"></a>The <strong id="b842352706152347"><a name="b842352706152347"></a><a name="b842352706152347"></a>interval</strong> parameter is invalid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p5333521310131"><a name="p5333521310131"></a><a name="p5333521310131"></a>Check the value of <strong id="b842352706203318_7"><a name="b842352706203318_7"></a><a name="b842352706203318_7"></a>interval</strong> in the request.</p>
</td>
</tr>
<tr id="row142492021031"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p2622065311153"><a name="p2622065311153"></a><a name="p2622065311153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p778803110328"><a name="p778803110328"></a><a name="p778803110328"></a>DNS.0608</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p2742897510328"><a name="p2742897510328"></a><a name="p2742897510328"></a>This resource is in use.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p715448510328"><a name="p715448510328"></a><a name="p715448510328"></a>Check whether the resource is in use.</p>
</td>
</tr>
<tr id="en-us_topic_0084006833_row61330526162150"><td class="cellrowborder" rowspan="9" valign="top" width="14.04%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0084006833_p1716684162150"><a name="en-us_topic_0084006833_p1716684162150"></a><a name="en-us_topic_0084006833_p1716684162150"></a>Pool</p>
</td>
<td class="cellrowborder" valign="top" width="12.44%" headers="mcps1.1.6.1.2 "><p id="p4349816111153"><a name="p4349816111153"></a><a name="p4349816111153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="20.01%" headers="mcps1.1.6.1.3 "><p id="p66823171033"><a name="p66823171033"></a><a name="p66823171033"></a>DNS.0101</p>
</td>
<td class="cellrowborder" valign="top" width="23.119999999999997%" headers="mcps1.1.6.1.4 "><p id="p2963104110128"><a name="p2963104110128"></a><a name="p2963104110128"></a>Invalid pool name.</p>
</td>
<td class="cellrowborder" valign="top" width="30.39%" headers="mcps1.1.6.1.5 "><p id="p166483101222"><a name="p166483101222"></a><a name="p166483101222"></a>Check the pool name in the request.</p>
</td>
</tr>
<tr id="en-us_topic_0084006833_row34093604162150"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p3369011611153"><a name="p3369011611153"></a><a name="p3369011611153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p1979847110131"><a name="p1979847110131"></a><a name="p1979847110131"></a>DNS.0102</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p4212060610131"><a name="p4212060610131"></a><a name="p4212060610131"></a>Invalid pool description.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p5632596310131"><a name="p5632596310131"></a><a name="p5632596310131"></a>Check the pool description in the request.</p>
</td>
</tr>
<tr id="en-us_topic_0084006833_row61551809162150"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p4454491311153"><a name="p4454491311153"></a><a name="p4454491311153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p57260682101311"><a name="p57260682101311"></a><a name="p57260682101311"></a>DNS.0103</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p11919068101311"><a name="p11919068101311"></a><a name="p11919068101311"></a>Invalid pool type.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p25920460101311"><a name="p25920460101311"></a><a name="p25920460101311"></a>Check whether the pool type you specify is supported or valid.</p>
</td>
</tr>
<tr id="en-us_topic_0084006833_row23810838162150"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p5136819011153"><a name="p5136819011153"></a><a name="p5136819011153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p1330544311205"><a name="p1330544311205"></a><a name="p1330544311205"></a>DNS.0104</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p21787416115341"><a name="p21787416115341"></a><a name="p21787416115341"></a>Invalid server configuration in the pool.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p448836301110"><a name="p448836301110"></a><a name="p448836301110"></a>Check the server configuration in the pool.</p>
</td>
</tr>
<tr id="en-us_topic_0084006833_row10242102162150"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p7384311153"><a name="p7384311153"></a><a name="p7384311153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p3599217011205"><a name="p3599217011205"></a><a name="p3599217011205"></a>DNS.0105</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0084006833_p22458678162150"><a name="en-us_topic_0084006833_p22458678162150"></a><a name="en-us_topic_0084006833_p22458678162150"></a>Invalid name server configuration in the pool.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p116954201110"><a name="p116954201110"></a><a name="p116954201110"></a>Check the name server configuration in the pool.</p>
</td>
</tr>
<tr id="en-us_topic_0084006833_row801513162150"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p598133711153"><a name="p598133711153"></a><a name="p598133711153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p6583518711205"><a name="p6583518711205"></a><a name="p6583518711205"></a>DNS.0106</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0084006833_p24237054162150"><a name="en-us_topic_0084006833_p24237054162150"></a><a name="en-us_topic_0084006833_p24237054162150"></a>Invalid pool region.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p78050031110"><a name="p78050031110"></a><a name="p78050031110"></a>Check the region configuration in the pool.</p>
</td>
</tr>
<tr id="en-us_topic_0084006833_row16806894162150"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p1472629511153"><a name="p1472629511153"></a><a name="p1472629511153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p1101417911205"><a name="p1101417911205"></a><a name="p1101417911205"></a>DNS.0107</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0084006833_p10171787162150"><a name="en-us_topic_0084006833_p10171787162150"></a><a name="en-us_topic_0084006833_p10171787162150"></a>Invalid pool ID.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p282255391110"><a name="p282255391110"></a><a name="p282255391110"></a>Check the pool ID in the request.</p>
</td>
</tr>
<tr id="en-us_topic_0084006833_row24437227162150"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p5197928611153"><a name="p5197928611153"></a><a name="p5197928611153"></a>404</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p4338205211205"><a name="p4338205211205"></a><a name="p4338205211205"></a>DNS.0108</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0084006833_p9570468162150"><a name="en-us_topic_0084006833_p9570468162150"></a><a name="en-us_topic_0084006833_p9570468162150"></a>This pool does not exist.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p45673071110"><a name="p45673071110"></a><a name="p45673071110"></a>Check whether the pool is available.</p>
</td>
</tr>
<tr id="en-us_topic_0084006833_row19025355162150"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p4957267011153"><a name="p4957267011153"></a><a name="p4957267011153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p1724119311205"><a name="p1724119311205"></a><a name="p1724119311205"></a>DNS.0109</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0084006833_p2871125162150"><a name="en-us_topic_0084006833_p2871125162150"></a><a name="en-us_topic_0084006833_p2871125162150"></a>This pool is in use.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p29068727115724"><a name="p29068727115724"></a><a name="p29068727115724"></a>A pool in use cannot be deleted. Contact customer service.</p>
</td>
</tr>
<tr id="en-us_topic_0084006833_row56701709162150"><td class="cellrowborder" rowspan="12" valign="top" width="14.04%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0084006833_p29435734162150"><a name="en-us_topic_0084006833_p29435734162150"></a><a name="en-us_topic_0084006833_p29435734162150"></a>Zone</p>
</td>
<td class="cellrowborder" valign="top" width="12.44%" headers="mcps1.1.6.1.2 "><p id="p5596331811153"><a name="p5596331811153"></a><a name="p5596331811153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="20.01%" headers="mcps1.1.6.1.3 "><p id="p14418658115946"><a name="p14418658115946"></a><a name="p14418658115946"></a>DNS.0201</p>
</td>
<td class="cellrowborder" valign="top" width="23.119999999999997%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0084006833_p55649776162150"><a name="en-us_topic_0084006833_p55649776162150"></a><a name="en-us_topic_0084006833_p55649776162150"></a>The email address of the zone is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="30.39%" headers="mcps1.1.6.1.5 "><p id="p180524001110"><a name="p180524001110"></a><a name="p180524001110"></a>Check the email address in the request.</p>
</td>
</tr>
<tr id="en-us_topic_0084006833_row31085939162150"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p3673488611153"><a name="p3673488611153"></a><a name="p3673488611153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p42219252115946"><a name="p42219252115946"></a><a name="p42219252115946"></a>DNS.0202</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0084006833_p11013426162150"><a name="en-us_topic_0084006833_p11013426162150"></a><a name="en-us_topic_0084006833_p11013426162150"></a>Invalid zone name.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p529583001110"><a name="p529583001110"></a><a name="p529583001110"></a>1. Check whether the zone name format is correct.</p>
<p id="p21225994121126"><a name="p21225994121126"></a><a name="p21225994121126"></a>2. Ensure that the zone name cannot be a top-level or public second-level domain name.</p>
</td>
</tr>
<tr id="en-us_topic_0084006833_row32011975162150"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p2273579911153"><a name="p2273579911153"></a><a name="p2273579911153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p41975384115946"><a name="p41975384115946"></a><a name="p41975384115946"></a>DNS.0203</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p6701514612746"><a name="p6701514612746"></a><a name="p6701514612746"></a>Invalid zone TTL value. The value ranges from <strong id="b842352706153732"><a name="b842352706153732"></a><a name="b842352706153732"></a>{minTTL}</strong>&nbsp;to&nbsp;<strong id="b842352706153727"><a name="b842352706153727"></a><a name="b842352706153727"></a>{maxTTL}</strong>.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p617639041110"><a name="p617639041110"></a><a name="p617639041110"></a>Check the TTL value in the request. If the limit does not meet your requirements, contact customer service.</p>
</td>
</tr>
<tr id="en-us_topic_0084006833_row19777430162150"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p2966043211153"><a name="p2966043211153"></a><a name="p2966043211153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p65522330115946"><a name="p65522330115946"></a><a name="p65522330115946"></a>DNS.0204</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0084006833_p38288026162150"><a name="en-us_topic_0084006833_p38288026162150"></a><a name="en-us_topic_0084006833_p38288026162150"></a>Invalid zone type.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p368203571110"><a name="p368203571110"></a><a name="p368203571110"></a>Check whether the zone type you specify is supported.</p>
</td>
</tr>
<tr id="en-us_topic_0084006833_row9047917162150"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p5368482611153"><a name="p5368482611153"></a><a name="p5368482611153"></a>404/500</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p45009478115950"><a name="p45009478115950"></a><a name="p45009478115950"></a>DNS.0205</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0084006833_p17202032162150"><a name="en-us_topic_0084006833_p17202032162150"></a><a name="en-us_topic_0084006833_p17202032162150"></a>No pools available.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p60219861122237"><a name="p60219861122237"></a><a name="p60219861122237"></a>Contact customer service.</p>
</td>
</tr>
<tr id="en-us_topic_0084006833_row20600568162150"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p5350367711153"><a name="p5350367711153"></a><a name="p5350367711153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p62784013115950"><a name="p62784013115950"></a><a name="p62784013115950"></a>DNS.0206</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0084006833_p3074769162150"><a name="en-us_topic_0084006833_p3074769162150"></a><a name="en-us_topic_0084006833_p3074769162150"></a>Invalid zone description. The description can contain a maximum of 255 characters.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p535657771110"><a name="p535657771110"></a><a name="p535657771110"></a>Check the zone description in the request.</p>
</td>
</tr>
<tr id="en-us_topic_0084006833_row27672928162150"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p3883056011153"><a name="p3883056011153"></a><a name="p3883056011153"></a>500</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p1300720115950"><a name="p1300720115950"></a><a name="p1300720115950"></a>DNS.0207</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0084006833_p32607498162150"><a name="en-us_topic_0084006833_p32607498162150"></a><a name="en-us_topic_0084006833_p32607498162150"></a>No views available.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p438606471110"><a name="p438606471110"></a><a name="p438606471110"></a>Contact customer service.</p>
</td>
</tr>
<tr id="en-us_topic_0084006833_row25032034162150"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p5826762711153"><a name="p5826762711153"></a><a name="p5826762711153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p8700944115950"><a name="p8700944115950"></a><a name="p8700944115950"></a>DNS.0208</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0084006833_p59237387162150"><a name="en-us_topic_0084006833_p59237387162150"></a><a name="en-us_topic_0084006833_p59237387162150"></a>This zone already exists.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p630515181110"><a name="p630515181110"></a><a name="p630515181110"></a>Check whether the requested zone already exists.</p>
</td>
</tr>
<tr id="en-us_topic_0084006833_row63374437162150"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p2205735111153"><a name="p2205735111153"></a><a name="p2205735111153"></a>400/409/500</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="en-us_topic_0084006833_p33055777162150"><a name="en-us_topic_0084006833_p33055777162150"></a><a name="en-us_topic_0084006833_p33055777162150"></a>DNS.0209</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0084006833_p60272277162150"><a name="en-us_topic_0084006833_p60272277162150"></a><a name="en-us_topic_0084006833_p60272277162150"></a>The zone is not in the normal state.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p49178767122632"><a name="p49178767122632"></a><a name="p49178767122632"></a>The zone status is not stable. Try again later.</p>
</td>
</tr>
<tr id="en-us_topic_0084006833_row5579588162150"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p4181500311153"><a name="p4181500311153"></a><a name="p4181500311153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="en-us_topic_0084006833_p49293504162150"><a name="en-us_topic_0084006833_p49293504162150"></a><a name="en-us_topic_0084006833_p49293504162150"></a>DNS.0210</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0084006833_p33350921162150"><a name="en-us_topic_0084006833_p33350921162150"></a><a name="en-us_topic_0084006833_p33350921162150"></a>The zone name is used by the system.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p219744771110"><a name="p219744771110"></a><a name="p219744771110"></a>Check the zone name in the request.</p>
</td>
</tr>
<tr id="row35506751122936"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p3157211211153"><a name="p3157211211153"></a><a name="p3157211211153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p2651801122949"><a name="p2651801122949"></a><a name="p2651801122949"></a>DNS.0211</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p6877613122936"><a name="p6877613122936"></a><a name="p6877613122936"></a>The zone name is used by another tenant.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p5720093122936"><a name="p5720093122936"></a><a name="p5720093122936"></a>Check the zone name in the request.</p>
</td>
</tr>
<tr id="row56140977122936"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p720430211153"><a name="p720430211153"></a><a name="p720430211153"></a>400/409</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p54115307122949"><a name="p54115307122949"></a><a name="p54115307122949"></a>DNS.0212</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p61268515122936"><a name="p61268515122936"></a><a name="p61268515122936"></a>This VPC has already been associated with the zone.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p32998019122936"><a name="p32998019122936"></a><a name="p32998019122936"></a>Check whether that the VPC has been associated with the private zone.</p>
</td>
</tr>
<tr id="row43175475123726"><td class="cellrowborder" rowspan="21" valign="top" width="14.04%" headers="mcps1.1.6.1.1 "><p id="p50843522123726"><a name="p50843522123726"></a><a name="p50843522123726"></a>Record Set</p>
<p id="p4869295142410"><a name="p4869295142410"></a><a name="p4869295142410"></a></p>
<p id="p34547811142422"><a name="p34547811142422"></a><a name="p34547811142422"></a></p>
<p id="p21447008124129"><a name="p21447008124129"></a><a name="p21447008124129"></a></p>
</td>
<td class="cellrowborder" valign="top" width="12.44%" headers="mcps1.1.6.1.2 "><p id="p4667756411153"><a name="p4667756411153"></a><a name="p4667756411153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="20.01%" headers="mcps1.1.6.1.3 "><p id="p13253131123740"><a name="p13253131123740"></a><a name="p13253131123740"></a>DNS.0301</p>
</td>
<td class="cellrowborder" valign="top" width="23.119999999999997%" headers="mcps1.1.6.1.4 "><p id="p28337724123726"><a name="p28337724123726"></a><a name="p28337724123726"></a>Invalid zone ID.</p>
</td>
<td class="cellrowborder" valign="top" width="30.39%" headers="mcps1.1.6.1.5 "><p id="p5253357123726"><a name="p5253357123726"></a><a name="p5253357123726"></a>Check the zone ID in the request.</p>
</td>
</tr>
<tr id="row27166896123726"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p2278630611153"><a name="p2278630611153"></a><a name="p2278630611153"></a>400/404</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p64965176123740"><a name="p64965176123740"></a><a name="p64965176123740"></a>DNS.0302</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p9651200123726"><a name="p9651200123726"></a><a name="p9651200123726"></a>This zone does not exist.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p17624920123726"><a name="p17624920123726"></a><a name="p17624920123726"></a>Check the zone of the requested record set.</p>
</td>
</tr>
<tr id="row12762961123726"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p4951672811153"><a name="p4951672811153"></a><a name="p4951672811153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p63615314123740"><a name="p63615314123740"></a><a name="p63615314123740"></a>DNS.0304</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p24953620123726"><a name="p24953620123726"></a><a name="p24953620123726"></a>Invalid record set name.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p6087487123726"><a name="p6087487123726"></a><a name="p6087487123726"></a>Check whether the record set name is a valid domain name ended with the zone name.</p>
</td>
</tr>
<tr id="row1418106123726"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p5143205611153"><a name="p5143205611153"></a><a name="p5143205611153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p3339213123740"><a name="p3339213123740"></a><a name="p3339213123740"></a>DNS.0305</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p2975445123726"><a name="p2975445123726"></a><a name="p2975445123726"></a>Invalid record set description. The description can contain a maximum of 255 characters.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p42087851123726"><a name="p42087851123726"></a><a name="p42087851123726"></a>Check the record set description in the request.</p>
</td>
</tr>
<tr id="row13273579123726"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p2235585011153"><a name="p2235585011153"></a><a name="p2235585011153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p35404799123740"><a name="p35404799123740"></a><a name="p35404799123740"></a>DNS.0307</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p27737757123726"><a name="p27737757123726"></a><a name="p27737757123726"></a>Invalid record set type.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p24802189123726"><a name="p24802189123726"></a><a name="p24802189123726"></a>Check whether the record set type you specify is supported.</p>
</td>
</tr>
<tr id="row38757544123726"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p6599338711153"><a name="p6599338711153"></a><a name="p6599338711153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p40295220123740"><a name="p40295220123740"></a><a name="p40295220123740"></a>DNS.0308</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p38242323123726"><a name="p38242323123726"></a><a name="p38242323123726"></a>Invalid record set value.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p66510579123726"><a name="p66510579123726"></a><a name="p66510579123726"></a>Check whether the record set value you specify is well-formatted.</p>
</td>
</tr>
<tr id="row49045636123726"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p4386412511153"><a name="p4386412511153"></a><a name="p4386412511153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p48642098123740"><a name="p48642098123740"></a><a name="p48642098123740"></a>DNS.0309</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p29529526123726"><a name="p29529526123726"></a><a name="p29529526123726"></a>Invalid record set ID.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p51254129123726"><a name="p51254129123726"></a><a name="p51254129123726"></a>Check the record set ID in the request.</p>
</td>
</tr>
<tr id="row65101838123726"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p6333322311153"><a name="p6333322311153"></a><a name="p6333322311153"></a>400/401</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p26609388123740"><a name="p26609388123740"></a><a name="p26609388123740"></a>DNS.0310</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p52828542123726"><a name="p52828542123726"></a><a name="p52828542123726"></a>Invalid tenant ID.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p45123135123726"><a name="p45123135123726"></a><a name="p45123135123726"></a>Check whether the tenant ID is empty or in incorrect format.</p>
</td>
</tr>
<tr id="row14690078123726"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p2971745811153"><a name="p2971745811153"></a><a name="p2971745811153"></a>400/401</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p3782237123740"><a name="p3782237123740"></a><a name="p3782237123740"></a>DNS.0311</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p4684258123726"><a name="p4684258123726"></a><a name="p4684258123726"></a>Invalid domain ID.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p35392791123726"><a name="p35392791123726"></a><a name="p35392791123726"></a>Check whether the domain ID is empty or in incorrect format.</p>
</td>
</tr>
<tr id="row46371473123726"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p5830391011153"><a name="p5830391011153"></a><a name="p5830391011153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p5787464123740"><a name="p5787464123740"></a><a name="p5787464123740"></a>DNS.0312</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p44648922123726"><a name="p44648922123726"></a><a name="p44648922123726"></a>This record set already exists.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p60331566123726"><a name="p60331566123726"></a><a name="p60331566123726"></a>Check whether the record set name already exists.</p>
</td>
</tr>
<tr id="row42435088123726"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p2499623311153"><a name="p2499623311153"></a><a name="p2499623311153"></a>404</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p5076192313742"><a name="p5076192313742"></a><a name="p5076192313742"></a>DNS.0313</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p1917151123726"><a name="p1917151123726"></a><a name="p1917151123726"></a>This record set does not exist.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p39673919123726"><a name="p39673919123726"></a><a name="p39673919123726"></a>Check the requested record set.</p>
</td>
</tr>
<tr id="row56910792123726"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p1142903011153"><a name="p1142903011153"></a><a name="p1142903011153"></a>400/409</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p2845805513742"><a name="p2845805513742"></a><a name="p2845805513742"></a>DNS.0314</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p1749736123726"><a name="p1749736123726"></a><a name="p1749736123726"></a>The record set is not in a steady state.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p47624831123726"><a name="p47624831123726"></a><a name="p47624831123726"></a>Check the record set status. If it is not stable, you cannot perform operations.</p>
</td>
</tr>
<tr id="row28693042123726"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p5333622711153"><a name="p5333622711153"></a><a name="p5333622711153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p928313113742"><a name="p928313113742"></a><a name="p928313113742"></a>DNS.0315</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p54626414123726"><a name="p54626414123726"></a><a name="p54626414123726"></a>Invalid status.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p33821865123726"><a name="p33821865123726"></a><a name="p33821865123726"></a>Check the status in the request.</p>
</td>
</tr>
<tr id="row31837405123726"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p2526711211153"><a name="p2526711211153"></a><a name="p2526711211153"></a>400/409</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p6293537213742"><a name="p6293537213742"></a><a name="p6293537213742"></a>DNS.0317</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p64960080123726"><a name="p64960080123726"></a><a name="p64960080123726"></a>This record set is a default one and cannot be deleted.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p58341909123726"><a name="p58341909123726"></a><a name="p58341909123726"></a>Check whether the record set to be deleted is created by default.</p>
</td>
</tr>
<tr id="row63189813123726"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p3337020611153"><a name="p3337020611153"></a><a name="p3337020611153"></a>400/409</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p4453264613742"><a name="p4453264613742"></a><a name="p4453264613742"></a>DNS.0318</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p21659163123726"><a name="p21659163123726"></a><a name="p21659163123726"></a>This record set is a default one and cannot be updated.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p2705223123726"><a name="p2705223123726"></a><a name="p2705223123726"></a>Check whether the record set to be updated is created by default.</p>
</td>
</tr>
<tr id="row55545651164523"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p1863217211153"><a name="p1863217211153"></a><a name="p1863217211153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p10433101164526"><a name="p10433101164526"></a><a name="p10433101164526"></a>DNS.0319</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p537264164526"><a name="p537264164526"></a><a name="p537264164526"></a>The TTL parameter has been out of range. The value ranges from <strong id="b842352706154626"><a name="b842352706154626"></a><a name="b842352706154626"></a>{minTTL}</strong>&nbsp;to&nbsp;<strong id="b842352706154634"><a name="b842352706154634"></a><a name="b842352706154634"></a>{maxTTL}</strong>.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p43518404164526"><a name="p43518404164526"></a><a name="p43518404164526"></a>Check the TTL value in the request. If the limit does not meet your requirements, contact customer service.</p>
</td>
</tr>
<tr id="row34738100164656"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p3281100311153"><a name="p3281100311153"></a><a name="p3281100311153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p41273207164658"><a name="p41273207164658"></a><a name="p41273207164658"></a>DNS.0320</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p9250435164658"><a name="p9250435164658"></a><a name="p9250435164658"></a>The zone name levels have been out of MAX count. The maximum is <strong id="b84235270615473"><a name="b84235270615473"></a><a name="b84235270615473"></a>{maxLevel}</strong>.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p11087784164658"><a name="p11087784164658"></a><a name="p11087784164658"></a>Check the domain name level in the request.</p>
</td>
</tr>
<tr id="row8047827164731"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p4044561911153"><a name="p4044561911153"></a><a name="p4044561911153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p14815106164734"><a name="p14815106164734"></a><a name="p14815106164734"></a>DNS.0321</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p28281455164734"><a name="p28281455164734"></a><a name="p28281455164734"></a>The sub domain levels have been out of MAX count. The maximum is <strong id="b842352706154729"><a name="b842352706154729"></a><a name="b842352706154729"></a>{maxLevel}</strong>.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p9096498164734"><a name="p9096498164734"></a><a name="p9096498164734"></a>Check the subdomain name in the request.</p>
</td>
</tr>
<tr id="row7997573142410"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p24606048142412"><a name="p24606048142412"></a><a name="p24606048142412"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p46932834142412"><a name="p46932834142412"></a><a name="p46932834142412"></a>DNS.0322</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p43463225142412"><a name="p43463225142412"></a><a name="p43463225142412"></a>Invalid <strong id="b842352706101453"><a name="b842352706101453"></a><a name="b842352706101453"></a>setId</strong> for the weighted record set.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p30860365142412"><a name="p30860365142412"></a><a name="p30860365142412"></a>Check the value of <strong id="b168857609599"><a name="b168857609599"></a><a name="b168857609599"></a>setId</strong> for the weighted record set.</p>
</td>
</tr>
<tr id="row63392857142422"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p59652051142425"><a name="p59652051142425"></a><a name="p59652051142425"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p67086855142425"><a name="p67086855142425"></a><a name="p67086855142425"></a>DNS.0323</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p65326175142425"><a name="p65326175142425"></a><a name="p65326175142425"></a>Invalid weight value for the record set.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p7664920142619"><a name="p7664920142619"></a><a name="p7664920142619"></a>1. Check whether a weight needs to be specified for the record set.</p>
<p id="p3823671415235"><a name="p3823671415235"></a><a name="p3823671415235"></a>2. Check the weight value for specified.</p>
</td>
</tr>
<tr id="row9839541124129"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p33464492124136"><a name="p33464492124136"></a><a name="p33464492124136"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p26269361124136"><a name="p26269361124136"></a><a name="p26269361124136"></a>DNS.0324</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p47443519124136"><a name="p47443519124136"></a><a name="p47443519124136"></a>The number of record sets of the same name, type, and resolution line exceeds the limit.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p17719805124136"><a name="p17719805124136"></a><a name="p17719805124136"></a>If the limit does not meet your requirements, contact customer service.</p>
</td>
</tr>
<tr id="row17075672135051"><td class="cellrowborder" rowspan="5" valign="top" width="14.04%" headers="mcps1.1.6.1.1 "><p id="p17090938151747"><a name="p17090938151747"></a><a name="p17090938151747"></a>Quota</p>
</td>
<td class="cellrowborder" valign="top" width="12.44%" headers="mcps1.1.6.1.2 "><p id="p5486969111153"><a name="p5486969111153"></a><a name="p5486969111153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="20.01%" headers="mcps1.1.6.1.3 "><p id="p17545474135051"><a name="p17545474135051"></a><a name="p17545474135051"></a>DNS.0401</p>
</td>
<td class="cellrowborder" valign="top" width="23.119999999999997%" headers="mcps1.1.6.1.4 "><p id="p24159522135051"><a name="p24159522135051"></a><a name="p24159522135051"></a>Invalid quota type.</p>
</td>
<td class="cellrowborder" valign="top" width="30.39%" headers="mcps1.1.6.1.5 "><p id="p10764289135051"><a name="p10764289135051"></a><a name="p10764289135051"></a>Check the quota type in the request.</p>
</td>
</tr>
<tr id="row39179999135051"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p1525996311153"><a name="p1525996311153"></a><a name="p1525996311153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p62538777135051"><a name="p62538777135051"></a><a name="p62538777135051"></a>DNS.0402</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p13323771135051"><a name="p13323771135051"></a><a name="p13323771135051"></a>Invalid quota value.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p5483681135051"><a name="p5483681135051"></a><a name="p5483681135051"></a>The quota value exceeds the limit. Contact customer service.</p>
</td>
</tr>
<tr id="row56549116135051"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p2809750011153"><a name="p2809750011153"></a><a name="p2809750011153"></a>403</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p38180895135051"><a name="p38180895135051"></a><a name="p38180895135051"></a>DNS.0403</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p34930589135641"><a name="p34930589135641"></a><a name="p34930589135641"></a>Insufficient record set quota.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p58693295135051"><a name="p58693295135051"></a><a name="p58693295135051"></a>The number of record sets exceeds the quota limit. If the limit does not meet your requirements, contact customer service.</p>
</td>
</tr>
<tr id="row65935558135051"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p6130502911153"><a name="p6130502911153"></a><a name="p6130502911153"></a>403</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p39066303135051"><a name="p39066303135051"></a><a name="p39066303135051"></a>DNS.0404</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p25265762135051"><a name="p25265762135051"></a><a name="p25265762135051"></a>Insufficient zone quota.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p24900237135824"><a name="p24900237135824"></a><a name="p24900237135824"></a>The number of zones exceeds the quota limit. If the limit does not meet your requirements, contact customer service.</p>
</td>
</tr>
<tr id="row7326173135051"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p6676035111153"><a name="p6676035111153"></a><a name="p6676035111153"></a>403</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p20873769135051"><a name="p20873769135051"></a><a name="p20873769135051"></a>DNS.0405</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p50717707135051"><a name="p50717707135051"></a><a name="p50717707135051"></a>Insufficient PTR record quota.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p14493570135051"><a name="p14493570135051"></a><a name="p14493570135051"></a>The number of PTR records exceeds the quota limit. If the limit does not meet your requirements, contact customer service.</p>
</td>
</tr>
<tr id="row60466342135051"><td class="cellrowborder" rowspan="9" valign="top" width="14.04%" headers="mcps1.1.6.1.1 "><p id="p1648103214136"><a name="p1648103214136"></a><a name="p1648103214136"></a>PTR</p>
</td>
<td class="cellrowborder" valign="top" width="12.44%" headers="mcps1.1.6.1.2 "><p id="p3887937811153"><a name="p3887937811153"></a><a name="p3887937811153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="20.01%" headers="mcps1.1.6.1.3 "><p id="p29721430135051"><a name="p29721430135051"></a><a name="p29721430135051"></a>DNS.0501</p>
</td>
<td class="cellrowborder" valign="top" width="23.119999999999997%" headers="mcps1.1.6.1.4 "><p id="p51053450135051"><a name="p51053450135051"></a><a name="p51053450135051"></a>Invalid PTR ID.</p>
</td>
<td class="cellrowborder" valign="top" width="30.39%" headers="mcps1.1.6.1.5 "><p id="p41688785135051"><a name="p41688785135051"></a><a name="p41688785135051"></a>Check whether the PTR record ID is empty or in incorrect format.</p>
</td>
</tr>
<tr id="row6718482135051"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p6222189311153"><a name="p6222189311153"></a><a name="p6222189311153"></a>404</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p57918023135051"><a name="p57918023135051"></a><a name="p57918023135051"></a>DNS.0502</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p29762178135051"><a name="p29762178135051"></a><a name="p29762178135051"></a>This EIP address does not exist.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p61926178135051"><a name="p61926178135051"></a><a name="p61926178135051"></a>Check whether the EIP is available.</p>
</td>
</tr>
<tr id="row23116119135051"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p680854411153"><a name="p680854411153"></a><a name="p680854411153"></a>409</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p47027269135051"><a name="p47027269135051"></a><a name="p47027269135051"></a>DNS.0503</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p46466266135051"><a name="p46466266135051"></a><a name="p46466266135051"></a>The PTR record is not in a steady state.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p5671214135051"><a name="p5671214135051"></a><a name="p5671214135051"></a>Check the PTR record status. If it is not stable, you cannot perform operations.</p>
</td>
</tr>
<tr id="row47307700135051"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p1462119611153"><a name="p1462119611153"></a><a name="p1462119611153"></a>400/500</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p40674337135051"><a name="p40674337135051"></a><a name="p40674337135051"></a>DNS.0504</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p39485701135051"><a name="p39485701135051"></a><a name="p39485701135051"></a>Invalid EIP address ID.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p44225206135051"><a name="p44225206135051"></a><a name="p44225206135051"></a>Check whether the EIP ID is empty or in incorrect format.</p>
</td>
</tr>
<tr id="row27626032135051"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p4346622411153"><a name="p4346622411153"></a><a name="p4346622411153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p27920500135051"><a name="p27920500135051"></a><a name="p27920500135051"></a>DNS.0505</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p46317115135051"><a name="p46317115135051"></a><a name="p46317115135051"></a>Invalid domain name in the PTR record.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p60698819135051"><a name="p60698819135051"></a><a name="p60698819135051"></a>Check the domain name in the PTR record.</p>
</td>
</tr>
<tr id="row62721882135051"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p3110328511153"><a name="p3110328511153"></a><a name="p3110328511153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p24697824135051"><a name="p24697824135051"></a><a name="p24697824135051"></a>DNS.0506</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p41628861135051"><a name="p41628861135051"></a><a name="p41628861135051"></a>Invalid PTR TTL value. The value ranges from 300 to 2147483647.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p16494566135051"><a name="p16494566135051"></a><a name="p16494566135051"></a>Check whether the PTR record TTL value exceeds the limit.</p>
</td>
</tr>
<tr id="row6969098135051"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p3633817911153"><a name="p3633817911153"></a><a name="p3633817911153"></a>404</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p12052301135051"><a name="p12052301135051"></a><a name="p12052301135051"></a>DNS.0507</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p20906004135051"><a name="p20906004135051"></a><a name="p20906004135051"></a>This PTR record does not exist.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p15664760135051"><a name="p15664760135051"></a><a name="p15664760135051"></a>Check the requested PTR record.</p>
</td>
</tr>
<tr id="row23143965135051"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p5771136111153"><a name="p5771136111153"></a><a name="p5771136111153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p11103787135051"><a name="p11103787135051"></a><a name="p11103787135051"></a>DNS.0508</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p38835025135051"><a name="p38835025135051"></a><a name="p38835025135051"></a>Invalid PTR description. The description can contain a maximum of 255 characters.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p58629339135051"><a name="p58629339135051"></a><a name="p58629339135051"></a>Check whether the PTR record description in the request exceeds 255 characters.</p>
</td>
</tr>
<tr id="row8570772135051"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p4410863111153"><a name="p4410863111153"></a><a name="p4410863111153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p44374059135051"><a name="p44374059135051"></a><a name="p44374059135051"></a>DNS.0602</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p19954410135051"><a name="p19954410135051"></a><a name="p19954410135051"></a>Invalid floating IP address.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p5694524135051"><a name="p5694524135051"></a><a name="p5694524135051"></a>Check the floating IP address in the request.</p>
</td>
</tr>
<tr id="row5070030914134"><td class="cellrowborder" rowspan="11" valign="top" width="14.04%" headers="mcps1.1.6.1.1 "><p id="p6056213914134"><a name="p6056213914134"></a><a name="p6056213914134"></a>Associating or disassociating a VPC from a private zone</p>
</td>
<td class="cellrowborder" valign="top" width="12.44%" headers="mcps1.1.6.1.2 "><p id="p1602935811153"><a name="p1602935811153"></a><a name="p1602935811153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="20.01%" headers="mcps1.1.6.1.3 "><p id="p658618714134"><a name="p658618714134"></a><a name="p658618714134"></a>DNS.0701</p>
</td>
<td class="cellrowborder" valign="top" width="23.119999999999997%" headers="mcps1.1.6.1.4 "><p id="p6097439214134"><a name="p6097439214134"></a><a name="p6097439214134"></a>Invalid VPC.</p>
</td>
<td class="cellrowborder" valign="top" width="30.39%" headers="mcps1.1.6.1.5 "><p id="p3997875814134"><a name="p3997875814134"></a><a name="p3997875814134"></a>Check the VPC ID and region in the request.</p>
</td>
</tr>
<tr id="row31694926143054"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p6038394211153"><a name="p6038394211153"></a><a name="p6038394211153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p23812201143054"><a name="p23812201143054"></a><a name="p23812201143054"></a>DNS.0704</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p2415689143054"><a name="p2415689143054"></a><a name="p2415689143054"></a>The VPC is not in a steady state.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p61453110143054"><a name="p61453110143054"></a><a name="p61453110143054"></a>Check whether the zone and VPC are normally associated.</p>
</td>
</tr>
<tr id="row10978198143054"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p5926110311153"><a name="p5926110311153"></a><a name="p5926110311153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p34213982143054"><a name="p34213982143054"></a><a name="p34213982143054"></a>DNS.0705</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p65896134143054"><a name="p65896134143054"></a><a name="p65896134143054"></a>No VPCs are associated with this zone.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p35986600143054"><a name="p35986600143054"></a><a name="p35986600143054"></a>Associate the zone with a VPC and try again.</p>
</td>
</tr>
<tr id="row44658303143056"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p3542000011153"><a name="p3542000011153"></a><a name="p3542000011153"></a>403</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p58054028143056"><a name="p58054028143056"></a><a name="p58054028143056"></a>DNS.0706</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p49677903143056"><a name="p49677903143056"></a><a name="p49677903143056"></a>You are not allowed to disassociate this VPC because this is the last VPC associated with this zone.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p64487234143056"><a name="p64487234143056"></a><a name="p64487234143056"></a>Associate another VPC with the zone and then disassociate the previous one.</p>
</td>
</tr>
<tr id="row4962033143056"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p5044774611153"><a name="p5044774611153"></a><a name="p5044774611153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p50240416143056"><a name="p50240416143056"></a><a name="p50240416143056"></a>DNS.0707</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p55738899143056"><a name="p55738899143056"></a><a name="p55738899143056"></a>The VPC is not associated with the zone.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p18557004143056"><a name="p18557004143056"></a><a name="p18557004143056"></a>Check whether the zone is associated with the VPC.</p>
</td>
</tr>
<tr id="row37834039143056"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p5973561211153"><a name="p5973561211153"></a><a name="p5973561211153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p19031134143056"><a name="p19031134143056"></a><a name="p19031134143056"></a>DNS.0708</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p40785709143056"><a name="p40785709143056"></a><a name="p40785709143056"></a>This VPC cannot be disassociated because it is being associated with the zone.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p15308150143056"><a name="p15308150143056"></a><a name="p15308150143056"></a>Check the association status between the zone and VPC. Disassociate them when the status is stable.</p>
</td>
</tr>
<tr id="row19116863143056"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p674642311153"><a name="p674642311153"></a><a name="p674642311153"></a>403</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p41666707143056"><a name="p41666707143056"></a><a name="p41666707143056"></a>DNS.0709</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p40866898143056"><a name="p40866898143056"></a><a name="p40866898143056"></a>This VPC cannot be disassociated because this is the only normal VPC associated with this zone.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p31692957145334"><a name="p31692957145334"></a><a name="p31692957145334"></a>Check whether other VPCs are normally associated with the zone. If no, perform the following operations:</p>
<p id="p5555209114544"><a name="p5555209114544"></a><a name="p5555209114544"></a>1. Disassociate VPCs in abnormal association state.</p>
<p id="p19609964145435"><a name="p19609964145435"></a><a name="p19609964145435"></a>2. Associate another VPC.</p>
<p id="p16640374145358"><a name="p16640374145358"></a><a name="p16640374145358"></a>2. Disassociate the required VPC.</p>
</td>
</tr>
<tr id="row20503390143432"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p958940311153"><a name="p958940311153"></a><a name="p958940311153"></a>500</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p8193465143432"><a name="p8193465143432"></a><a name="p8193465143432"></a>DNS.0710</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p3129862143432"><a name="p3129862143432"></a><a name="p3129862143432"></a>Invalid VPC URL configuration.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p52192249143432"><a name="p52192249143432"></a><a name="p52192249143432"></a>Check the region in the request. If the region is correct, contact customer service.</p>
</td>
</tr>
<tr id="row24647775143432"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p3854414211153"><a name="p3854414211153"></a><a name="p3854414211153"></a>404</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p59758148143432"><a name="p59758148143432"></a><a name="p59758148143432"></a>DNS.0711</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p15343987145719"><a name="p15343987145719"></a><a name="p15343987145719"></a>This VPC could not be found.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p2271408143432"><a name="p2271408143432"></a><a name="p2271408143432"></a>Log in to the VPC console and check whether the VPC exists.</p>
</td>
</tr>
<tr id="row40021343143432"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p3506783511153"><a name="p3506783511153"></a><a name="p3506783511153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p40894050143432"><a name="p40894050143432"></a><a name="p40894050143432"></a>DNS.0712</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p4626353143432"><a name="p4626353143432"></a><a name="p4626353143432"></a>This port parameter is invalid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p39190330143432"><a name="p39190330143432"></a><a name="p39190330143432"></a>Check whether the port ID in the request is empty.</p>
</td>
</tr>
<tr id="row22677096165458"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p2192237611153"><a name="p2192237611153"></a><a name="p2192237611153"></a>400/500</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p2854446416552"><a name="p2854446416552"></a><a name="p2854446416552"></a>DNS.0805</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p22531483165521"><a name="p22531483165521"></a><a name="p22531483165521"></a>Failed to check the VPC validity.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p13110821165521"><a name="p13110821165521"></a><a name="p13110821165521"></a>Retry the operation. If the error persists, contact customer service.</p>
</td>
</tr>
<tr id="row26631250143522"><td class="cellrowborder" rowspan="2" valign="top" width="14.04%" headers="mcps1.1.6.1.1 "><p id="p42312595143522"><a name="p42312595143522"></a><a name="p42312595143522"></a>Resolution lines</p>
</td>
<td class="cellrowborder" valign="top" width="12.44%" headers="mcps1.1.6.1.2 "><p id="p3088201311153"><a name="p3088201311153"></a><a name="p3088201311153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="20.01%" headers="mcps1.1.6.1.3 "><p id="p4768195143522"><a name="p4768195143522"></a><a name="p4768195143522"></a>DNS.0806</p>
</td>
<td class="cellrowborder" valign="top" width="23.119999999999997%" headers="mcps1.1.6.1.4 "><p id="p11401397143522"><a name="p11401397143522"></a><a name="p11401397143522"></a>This line is not supported in this DNS version.</p>
</td>
<td class="cellrowborder" valign="top" width="30.39%" headers="mcps1.1.6.1.5 "><p id="p51097926143522"><a name="p51097926143522"></a><a name="p51097926143522"></a>Check the resolution line name in the request.</p>
</td>
</tr>
<tr id="row551878801505"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p1841513911153"><a name="p1841513911153"></a><a name="p1841513911153"></a>409</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p580522031519"><a name="p580522031519"></a><a name="p580522031519"></a>DNS.0807</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p289758331505"><a name="p289758331505"></a><a name="p289758331505"></a>This line is a default one and cannot be operated.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p69305001505"><a name="p69305001505"></a><a name="p69305001505"></a>Check the resolution line name in the request.</p>
</td>
</tr>
<tr id="row3679027017049"><td class="cellrowborder" valign="top" width="14.04%" headers="mcps1.1.6.1.1 "><p id="p171903217056"><a name="p171903217056"></a><a name="p171903217056"></a>Name server</p>
</td>
<td class="cellrowborder" valign="top" width="12.44%" headers="mcps1.1.6.1.2 "><p id="p1523129711153"><a name="p1523129711153"></a><a name="p1523129711153"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="20.01%" headers="mcps1.1.6.1.3 "><p id="p2450436017049"><a name="p2450436017049"></a><a name="p2450436017049"></a>DNS.0901</p>
</td>
<td class="cellrowborder" valign="top" width="23.119999999999997%" headers="mcps1.1.6.1.4 "><p id="p4738120317049"><a name="p4738120317049"></a><a name="p4738120317049"></a>The name server does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="30.39%" headers="mcps1.1.6.1.5 "><p id="p1267223517049"><a name="p1267223517049"></a><a name="p1267223517049"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row2481236614390"><td class="cellrowborder" rowspan="3" valign="top" width="14.04%" headers="mcps1.1.6.1.1 "><p id="p6364460214390"><a name="p6364460214390"></a><a name="p6364460214390"></a>TAG</p>
</td>
<td class="cellrowborder" valign="top" width="12.44%" headers="mcps1.1.6.1.2 "><p id="p5493916314390"><a name="p5493916314390"></a><a name="p5493916314390"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="20.01%" headers="mcps1.1.6.1.3 "><p id="p2088725714390"><a name="p2088725714390"></a><a name="p2088725714390"></a>DNS.1001</p>
</td>
<td class="cellrowborder" valign="top" width="23.119999999999997%" headers="mcps1.1.6.1.4 "><p id="p1414626714390"><a name="p1414626714390"></a><a name="p1414626714390"></a>Insufficient tag quota.</p>
</td>
<td class="cellrowborder" valign="top" width="30.39%" headers="mcps1.1.6.1.5 "><p id="p499700214390"><a name="p499700214390"></a><a name="p499700214390"></a>The number of tags reaches the quota limit. If the limit does not meet your requirements, contact customer service.</p>
</td>
</tr>
<tr id="row24680077144215"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p59406882144215"><a name="p59406882144215"></a><a name="p59406882144215"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p47228103144215"><a name="p47228103144215"></a><a name="p47228103144215"></a>DNS.1002</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p271112144215"><a name="p271112144215"></a><a name="p271112144215"></a>Invalid resource type.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p21960143144215"><a name="p21960143144215"></a><a name="p21960143144215"></a>Check the resource type in the request.</p>
</td>
</tr>
<tr id="row45472346201831"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p45163689201831"><a name="p45163689201831"></a><a name="p45163689201831"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p34380163201831"><a name="p34380163201831"></a><a name="p34380163201831"></a>DNS.1003</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p33329801201831"><a name="p33329801201831"></a><a name="p33329801201831"></a>Invalid tag.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p15359397201831"><a name="p15359397201831"></a><a name="p15359397201831"></a>Check the tag in the request.</p>
</td>
</tr>
</tbody>
</table>

