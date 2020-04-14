# Get Object Content and Metadata<a name="obs_03_0054"></a>

This operation returns the object metadata in the response headers and the object content in the response body.

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
<tbody><tr id="row15388804113016"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p38533588113016"><a name="p38533588113016"></a><a name="p38533588113016"></a>GET</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p66153545194815"><a name="p66153545194815"></a><a name="p66153545194815"></a>/v1/{account}/{container}/{object}{?temp_url_sig,temp_url_expires,multipart-manifest}</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p19784190113016"><a name="p19784190113016"></a><a name="p19784190113016"></a>Downloads the object content and gets the object metadata.</p>
</td>
</tr>
</tbody>
</table>

**\{account\}** indicates the name of an account. **\{container\}** indicates the name of a container. **\{object\}**  indicates the name of an object.

This operation does not involve a request body.

## Example Request<a name="section16623225"></a>

Show the content and metadata of the  **goodbye** object in the **marktwain**  container:

```
curl -i $publicURL/marktwain/goodbye -X GET -H "X-Auth-Token:$token"
```

## Request Query Parameters<a name="section5103708"></a>

[Table 2](#table2272850011511)  describes the query parameters for getting the object content:

**Table  2**  Request query parameters

<a name="table2272850011511"></a>
<table><thead align="left"><tr id="row6616787111511"><th class="cellrowborder" valign="top" width="22.68%" id="mcps1.2.4.1.1"><p id="p5221421211511"><a name="p5221421211511"></a><a name="p5221421211511"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.09%" id="mcps1.2.4.1.2"><p id="p149275011511"><a name="p149275011511"></a><a name="p149275011511"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="63.23%" id="mcps1.2.4.1.3"><p id="p5380390811511"><a name="p5380390811511"></a><a name="p5380390811511"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1447313211511"><td class="cellrowborder" valign="top" width="22.68%" headers="mcps1.2.4.1.1 "><p id="p3147304011511"><a name="p3147304011511"></a><a name="p3147304011511"></a>temp_url_sig</p>
</td>
<td class="cellrowborder" valign="top" width="14.09%" headers="mcps1.2.4.1.2 "><p id="p6628834111511"><a name="p6628834111511"></a><a name="p6628834111511"></a>String</p>
<p id="p40578909144350"><a name="p40578909144350"></a><a name="p40578909144350"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="63.23%" headers="mcps1.2.4.1.3 "><p id="p64656311511"><a name="p64656311511"></a><a name="p64656311511"></a>Used with TempURL to sign the request.</p>
</td>
</tr>
<tr id="row581906811511"><td class="cellrowborder" valign="top" width="22.68%" headers="mcps1.2.4.1.1 "><p id="p158250511511"><a name="p158250511511"></a><a name="p158250511511"></a>temp_url_expires</p>
</td>
<td class="cellrowborder" valign="top" width="14.09%" headers="mcps1.2.4.1.2 "><p id="p6107409911511"><a name="p6107409911511"></a><a name="p6107409911511"></a>String</p>
<p id="p263167614445"><a name="p263167614445"></a><a name="p263167614445"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="63.23%" headers="mcps1.2.4.1.3 "><p id="p4805497711511"><a name="p4805497711511"></a><a name="p4805497711511"></a>Used with TempURL to specify the expiry time of the signature.</p>
</td>
</tr>
<tr id="row2984161311511"><td class="cellrowborder" valign="top" width="22.68%" headers="mcps1.2.4.1.1 "><p id="p125161311511"><a name="p125161311511"></a><a name="p125161311511"></a>multipart-manifest</p>
</td>
<td class="cellrowborder" valign="top" width="14.09%" headers="mcps1.2.4.1.2 "><p id="p27063604115613"><a name="p27063604115613"></a><a name="p27063604115613"></a>String</p>
<p id="p4187753014447"><a name="p4187753014447"></a><a name="p4187753014447"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="63.23%" headers="mcps1.2.4.1.3 "><p id="p2455611111511"><a name="p2455611111511"></a><a name="p2455611111511"></a>If the value is <strong id="b84235270615282"><a name="b84235270615282"></a><a name="b84235270615282"></a>get</strong>&nbsp;and the object is a large object, the content of the&nbsp;<strong id="b842352706152842"><a name="b842352706152842"></a><a name="b842352706152842"></a>manifest</strong> file for the static or dynamic large object, instead of the content of the large object, is returned.</p>
</td>
</tr>
<tr id="row3477494317475"><td class="cellrowborder" valign="top" width="22.68%" headers="mcps1.2.4.1.1 "><p id="p6530699917475"><a name="p6530699917475"></a><a name="p6530699917475"></a>filename</p>
</td>
<td class="cellrowborder" valign="top" width="14.09%" headers="mcps1.2.4.1.2 "><p id="p66830643174919"><a name="p66830643174919"></a><a name="p66830643174919"></a>String</p>
<p id="p64604883174919"><a name="p64604883174919"></a><a name="p64604883174919"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="63.23%" headers="mcps1.2.4.1.3 "><p id="p5623698117475"><a name="p5623698117475"></a><a name="p5623698117475"></a>If objects are accessed based on TempURL, use the value of <strong id="b42121251"><a name="b42121251"></a><a name="b42121251"></a>filename</strong>&nbsp;to replace that of&nbsp;<strong id="b43546944"><a name="b43546944"></a><a name="b43546944"></a>filename</strong>&nbsp;in the&nbsp;<strong id="b56378176"><a name="b56378176"></a><a name="b56378176"></a>Content-Disposition</strong> header.</p>
</td>
</tr>
<tr id="row674571317476"><td class="cellrowborder" valign="top" width="22.68%" headers="mcps1.2.4.1.1 "><p id="p953184217476"><a name="p953184217476"></a><a name="p953184217476"></a>inline</p>
</td>
<td class="cellrowborder" valign="top" width="14.09%" headers="mcps1.2.4.1.2 "><p id="p3388173217476"><a name="p3388173217476"></a><a name="p3388173217476"></a>NA</p>
<p id="p15446161175116"><a name="p15446161175116"></a><a name="p15446161175116"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="63.23%" headers="mcps1.2.4.1.3 "><p id="p6006575817476"><a name="p6006575817476"></a><a name="p6006575817476"></a>If objects are accessed based on TempURL, replace the content of the <strong id="b46852469"><a name="b46852469"></a><a name="b46852469"></a>Content-Disposition</strong>&nbsp;response header with&nbsp;<strong id="b19019038"><a name="b19019038"></a><a name="b19019038"></a>inline</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Request Headers<a name="section2186955"></a>

Request URI parameters

<a name="table22572327145255"></a>
<table><thead align="left"><tr id="row16509377145255"><th class="cellrowborder" valign="top" width="20.66%" id="mcps1.1.4.1.1"><p id="p62191138145255"><a name="p62191138145255"></a><a name="p62191138145255"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.399999999999999%" id="mcps1.1.4.1.2"><p id="p38857041145255"><a name="p38857041145255"></a><a name="p38857041145255"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="64.94%" id="mcps1.1.4.1.3"><p id="p6842498145255"><a name="p6842498145255"></a><a name="p6842498145255"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row22125722145255"><td class="cellrowborder" valign="top" width="20.66%" headers="mcps1.1.4.1.1 "><p id="p47353059145255"><a name="p47353059145255"></a><a name="p47353059145255"></a>{account}</p>
</td>
<td class="cellrowborder" valign="top" width="14.399999999999999%" headers="mcps1.1.4.1.2 "><p id="p10392605145255"><a name="p10392605145255"></a><a name="p10392605145255"></a>String</p>
<p id="p26424588145255"><a name="p26424588145255"></a><a name="p26424588145255"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.1.4.1.3 "><p id="p60016882145255"><a name="p60016882145255"></a><a name="p60016882145255"></a>Unique name of the account. In the current version, it indicates the unique ID of the account.</p>
</td>
</tr>
<tr id="row3281027145255"><td class="cellrowborder" valign="top" width="20.66%" headers="mcps1.1.4.1.1 "><p id="p64436606145255"><a name="p64436606145255"></a><a name="p64436606145255"></a>{container}</p>
</td>
<td class="cellrowborder" valign="top" width="14.399999999999999%" headers="mcps1.1.4.1.2 "><p id="p51982602145255"><a name="p51982602145255"></a><a name="p51982602145255"></a>String</p>
<p id="p65190238145255"><a name="p65190238145255"></a><a name="p65190238145255"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.1.4.1.3 "><p id="p45917893145255"><a name="p45917893145255"></a><a name="p45917893145255"></a>Unique name of the container.</p>
<p id="p10607859145255"><a name="p10607859145255"></a><a name="p10607859145255"></a>For details about container naming rules, see <a href="naming-rules.md">Naming Rules</a>.</p>
</td>
</tr>
<tr id="row4090594414533"><td class="cellrowborder" valign="top" width="20.66%" headers="mcps1.1.4.1.1 "><p id="p3260917814533"><a name="p3260917814533"></a><a name="p3260917814533"></a>{object}</p>
</td>
<td class="cellrowborder" valign="top" width="14.399999999999999%" headers="mcps1.1.4.1.2 "><p id="p15345569145319"><a name="p15345569145319"></a><a name="p15345569145319"></a>String</p>
<p id="p3892401145319"><a name="p3892401145319"></a><a name="p3892401145319"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.1.4.1.3 "><p id="p576202614533"><a name="p576202614533"></a><a name="p576202614533"></a>Name of the object.</p>
<p id="p63081133145352"><a name="p63081133145352"></a><a name="p63081133145352"></a>For details about object naming rules, see <a href="naming-rules.md#section23579102">Object Naming Rules</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Request header parameters

<a name="table2401366117510"></a>
<table><thead align="left"><tr id="row677888617510"><th class="cellrowborder" valign="top" width="36.54%" id="mcps1.2.4.1.1"><p id="p1221893217510"><a name="p1221893217510"></a><a name="p1221893217510"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="16.939999999999998%" id="mcps1.2.4.1.2"><p id="p4923183717510"><a name="p4923183717510"></a><a name="p4923183717510"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="46.52%" id="mcps1.2.4.1.3"><p id="p5387583217510"><a name="p5387583217510"></a><a name="p5387583217510"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row6543608016258"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p276595101632"><a name="p276595101632"></a><a name="p276595101632"></a>X-Auth-Token</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p258278761632"><a name="p258278761632"></a><a name="p258278761632"></a>String</p>
<p id="p311242971632"><a name="p311242971632"></a><a name="p311242971632"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p380401411632"><a name="p380401411632"></a><a name="p380401411632"></a>Authentication token.</p>
</td>
</tr>
<tr id="row3085148517510"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p1594232217510"><a name="p1594232217510"></a><a name="p1594232217510"></a>Range</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p1625968317510"><a name="p1625968317510"></a><a name="p1625968317510"></a>String</p>
<p id="p610616616332"><a name="p610616616332"></a><a name="p610616616332"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p4196597817510"><a name="p4196597817510"></a><a name="p4196597817510"></a>Range of the content to get.</p>
<p id="p10636357175328"><a name="p10636357175328"></a><a name="p10636357175328"></a>For example:</p>
<a name="ul43144865144956"></a><a name="ul43144865144956"></a><ul id="ul43144865144956"><li>Range: bytes=-5. The last five bytes.</li><li>Range: bytes=10-15. The five bytes of data after a 10-byte offset.</li><li>Range: bytes=6-. Byte 6 and after.</li><li>Range: bytes=1-3,2-5. A multi-part response that contains bytes 1 to 3 inclusive, and bytes 2 to 5 inclusive.</li></ul>
</td>
</tr>
<tr id="row5866486617510"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p5423368217510"><a name="p5423368217510"></a><a name="p5423368217510"></a>If-Match</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p3085213117510"><a name="p3085213117510"></a><a name="p3085213117510"></a>String</p>
<p id="p1811496216334"><a name="p1811496216334"></a><a name="p1811496216334"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p1599468417510"><a name="p1599468417510"></a><a name="p1599468417510"></a>If the MD5 value of the queried object is equal to the specified value, the object is returned.</p>
</td>
</tr>
<tr id="row5029183717510"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p4710699517510"><a name="p4710699517510"></a><a name="p4710699517510"></a>If-None-Match</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p5757022117510"><a name="p5757022117510"></a><a name="p5757022117510"></a>String</p>
<p id="p6571943116336"><a name="p6571943116336"></a><a name="p6571943116336"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p10059610175736"><a name="p10059610175736"></a><a name="p10059610175736"></a>If the MD5 value of the queried object is not equal to the specified value, the object is returned.</p>
</td>
</tr>
<tr id="row6449063117510"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p5635865217510"><a name="p5635865217510"></a><a name="p5635865217510"></a>If-Modified-Since</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p164812217510"><a name="p164812217510"></a><a name="p164812217510"></a>String</p>
<p id="p821133216338"><a name="p821133216338"></a><a name="p821133216338"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p6638903217510"><a name="p6638903217510"></a><a name="p6638903217510"></a>If the queried object was modified before the specified time, the object is returned.</p>
</td>
</tr>
<tr id="row1211344217510"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p1966997217586"><a name="p1966997217586"></a><a name="p1966997217586"></a>If-Unmodified-Since</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p1940045917510"><a name="p1940045917510"></a><a name="p1940045917510"></a>String</p>
<p id="p3751039816340"><a name="p3751039816340"></a><a name="p3751039816340"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p2793332217510"><a name="p2793332217510"></a><a name="p2793332217510"></a>If the queried object was not modified before the specified time, the object is returned.</p>
</td>
</tr>
</tbody>
</table>

## Response Headers<a name="section30570743"></a>

The following table describes the response headers:

**Table  4**  Response header parameters

<a name="table59658522144238"></a>
<table><thead align="left"><tr id="row55181501144238"><th class="cellrowborder" valign="top" width="33.39%" id="mcps1.2.4.1.1"><p id="p29104717144238"><a name="p29104717144238"></a><a name="p29104717144238"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="20.4%" id="mcps1.2.4.1.2"><p id="p8671853144238"><a name="p8671853144238"></a><a name="p8671853144238"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="46.21%" id="mcps1.2.4.1.3"><p id="p31331502144238"><a name="p31331502144238"></a><a name="p31331502144238"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row13548066144238"><td class="cellrowborder" valign="top" width="33.39%" headers="mcps1.2.4.1.1 "><p id="p23651575144238"><a name="p23651575144238"></a><a name="p23651575144238"></a>Accept-Ranges</p>
</td>
<td class="cellrowborder" valign="top" width="20.4%" headers="mcps1.2.4.1.2 "><p id="p36729408144238"><a name="p36729408144238"></a><a name="p36729408144238"></a>String</p>
<p id="p30712559145926"><a name="p30712559145926"></a><a name="p30712559145926"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="46.21%" headers="mcps1.2.4.1.3 "><p id="p22292070144238"><a name="p22292070144238"></a><a name="p22292070144238"></a>Type of ranges that the object accepts.</p>
</td>
</tr>
<tr id="row6423655915944"><td class="cellrowborder" valign="top" width="33.39%" headers="mcps1.2.4.1.1 "><p id="p3577876015944"><a name="p3577876015944"></a><a name="p3577876015944"></a>X-Object-Meta-name</p>
</td>
<td class="cellrowborder" valign="top" width="20.4%" headers="mcps1.2.4.1.2 "><p id="p1239840915944"><a name="p1239840915944"></a><a name="p1239840915944"></a>String</p>
<p id="p36702715145941"><a name="p36702715145941"></a><a name="p36702715145941"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="46.21%" headers="mcps1.2.4.1.3 "><p id="p6474706715944"><a name="p6474706715944"></a><a name="p6474706715944"></a>Custom object metadata item, where <strong id="b35178749"><a name="b35178749"></a><a name="b35178749"></a>{name}</strong> is the name of the metadata item.</p>
</td>
</tr>
<tr id="row37782275102328"><td class="cellrowborder" valign="top" width="33.39%" headers="mcps1.2.4.1.1 "><p id="p40465454102328"><a name="p40465454102328"></a><a name="p40465454102328"></a>X-Timestamp</p>
</td>
<td class="cellrowborder" valign="top" width="20.4%" headers="mcps1.2.4.1.2 "><p id="p227314485311"><a name="p227314485311"></a><a name="p227314485311"></a>Datetime</p>
<p id="p42390779145944"><a name="p42390779145944"></a><a name="p42390779145944"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="46.21%" headers="mcps1.2.4.1.3 "><p id="p11181925102328"><a name="p11181925102328"></a><a name="p11181925102328"></a>Object creation time and date, in UNIX Epoch timestamp format.</p>
</td>
</tr>
<tr id="row60159480102332"><td class="cellrowborder" valign="top" width="33.39%" headers="mcps1.2.4.1.1 "><p id="p41079706102332"><a name="p41079706102332"></a><a name="p41079706102332"></a>ETag</p>
</td>
<td class="cellrowborder" valign="top" width="20.4%" headers="mcps1.2.4.1.2 "><p id="p39121876102332"><a name="p39121876102332"></a><a name="p39121876102332"></a>String</p>
<p id="p271798811504"><a name="p271798811504"></a><a name="p271798811504"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="46.21%" headers="mcps1.2.4.1.3 "><p id="p44738538161017"><a name="p44738538161017"></a><a name="p44738538161017"></a>For ordinary objects, this value is the MD5 checksum of the object content.</p>
<p id="p14755407102332"><a name="p14755407102332"></a><a name="p14755407102332"></a>For manifest objects, this value is the MD5 checksum of the concatenated string of MD5 checksums for each of the segments in the manifest.</p>
</td>
</tr>
<tr id="row16695428102337"><td class="cellrowborder" valign="top" width="33.39%" headers="mcps1.2.4.1.1 "><p id="p10152397102337"><a name="p10152397102337"></a><a name="p10152397102337"></a>Content-Encoding</p>
</td>
<td class="cellrowborder" valign="top" width="20.4%" headers="mcps1.2.4.1.2 "><p id="p17037790102337"><a name="p17037790102337"></a><a name="p17037790102337"></a>String</p>
<p id="p2879614015040"><a name="p2879614015040"></a><a name="p2879614015040"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.21%" headers="mcps1.2.4.1.3 "><p id="p37883744102337"><a name="p37883744102337"></a><a name="p37883744102337"></a>Code used when an object is downloaded through a browser.</p>
</td>
</tr>
<tr id="row45902091102652"><td class="cellrowborder" valign="top" width="33.39%" headers="mcps1.2.4.1.1 "><p id="p27081929102652"><a name="p27081929102652"></a><a name="p27081929102652"></a>Content-Disposition</p>
</td>
<td class="cellrowborder" valign="top" width="20.4%" headers="mcps1.2.4.1.2 "><p id="p46152651102652"><a name="p46152651102652"></a><a name="p46152651102652"></a>String</p>
<p id="p1969381415038"><a name="p1969381415038"></a><a name="p1969381415038"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.21%" headers="mcps1.2.4.1.3 "><p id="p47377274102652"><a name="p47377274102652"></a><a name="p47377274102652"></a>When an object is downloaded through a browser, the default object name is <strong id="b49409500"><a name="b49409500"></a><a name="b49409500"></a>newname</strong>.</p>
</td>
</tr>
<tr id="row50936082102832"><td class="cellrowborder" valign="top" width="33.39%" headers="mcps1.2.4.1.1 "><p id="p32181953102832"><a name="p32181953102832"></a><a name="p32181953102832"></a>X-Object-Manifest</p>
</td>
<td class="cellrowborder" valign="top" width="20.4%" headers="mcps1.2.4.1.2 "><p id="p56601389102832"><a name="p56601389102832"></a><a name="p56601389102832"></a>String</p>
<p id="p3317542315036"><a name="p3317542315036"></a><a name="p3317542315036"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.21%" headers="mcps1.2.4.1.3 "><p id="p21309757102832"><a name="p21309757102832"></a><a name="p21309757102832"></a>This is the identifier of a dynamic large object. The value is the container and object name prefix of the segment objects in the form of <em id="i1075393796111726"><a name="i1075393796111726"></a><a name="i1075393796111726"></a>container/prefix</em>.</p>
</td>
</tr>
<tr id="row62438886102858"><td class="cellrowborder" valign="top" width="33.39%" headers="mcps1.2.4.1.1 "><p id="p24385026102858"><a name="p24385026102858"></a><a name="p24385026102858"></a>X-Static-Large-Object</p>
</td>
<td class="cellrowborder" valign="top" width="20.4%" headers="mcps1.2.4.1.2 "><p id="p63707726102928"><a name="p63707726102928"></a><a name="p63707726102928"></a>String</p>
<p id="p679015315027"><a name="p679015315027"></a><a name="p679015315027"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.21%" headers="mcps1.2.4.1.3 "><p id="p2629768102858"><a name="p2629768102858"></a><a name="p2629768102858"></a>Identifier of a large static object.</p>
</td>
</tr>
<tr id="row3879482820419"><td class="cellrowborder" valign="top" width="33.39%" headers="mcps1.2.4.1.1 "><p id="p1931059020451"><a name="p1931059020451"></a><a name="p1931059020451"></a>Content-Length</p>
</td>
<td class="cellrowborder" valign="top" width="20.4%" headers="mcps1.2.4.1.2 "><p id="p2065397620451"><a name="p2065397620451"></a><a name="p2065397620451"></a>String</p>
<p id="p5166805920451"><a name="p5166805920451"></a><a name="p5166805920451"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="46.21%" headers="mcps1.2.4.1.3 "><p id="p2436324220451"><a name="p2436324220451"></a><a name="p2436324220451"></a>If the operation succeeds, the value is the content length of the obtained object.</p>
<p id="p1794259320451"><a name="p1794259320451"></a><a name="p1794259320451"></a>If the operation fails, this value is the length of the error text in the response body.</p>
</td>
</tr>
<tr id="row6587446420421"><td class="cellrowborder" valign="top" width="33.39%" headers="mcps1.2.4.1.1 "><p id="p6103081920451"><a name="p6103081920451"></a><a name="p6103081920451"></a>Content-Type</p>
</td>
<td class="cellrowborder" valign="top" width="20.4%" headers="mcps1.2.4.1.2 "><p id="p4454927620451"><a name="p4454927620451"></a><a name="p4454927620451"></a>String</p>
<p id="p6539916420451"><a name="p6539916420451"></a><a name="p6539916420451"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="46.21%" headers="mcps1.2.4.1.3 "><p id="p6284090420451"><a name="p6284090420451"></a><a name="p6284090420451"></a>MIME type of the object.</p>
</td>
</tr>
<tr id="row4811664420422"><td class="cellrowborder" valign="top" width="33.39%" headers="mcps1.2.4.1.1 "><p id="p4277436120451"><a name="p4277436120451"></a><a name="p4277436120451"></a>Date</p>
</td>
<td class="cellrowborder" valign="top" width="20.4%" headers="mcps1.2.4.1.2 "><p id="p4217123620451"><a name="p4217123620451"></a><a name="p4217123620451"></a>Datetime</p>
<p id="p4399680920451"><a name="p4399680920451"></a><a name="p4399680920451"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="46.21%" headers="mcps1.2.4.1.3 "><p id="p697180020451"><a name="p697180020451"></a><a name="p697180020451"></a>Transaction date and time.</p>
</td>
</tr>
<tr id="row6539430520423"><td class="cellrowborder" valign="top" width="33.39%" headers="mcps1.2.4.1.1 "><p id="p4927772020451"><a name="p4927772020451"></a><a name="p4927772020451"></a>X-Trans-Id</p>
</td>
<td class="cellrowborder" valign="top" width="20.4%" headers="mcps1.2.4.1.2 "><p id="p3207237320451"><a name="p3207237320451"></a><a name="p3207237320451"></a>Uuid</p>
<p id="p2021590320451"><a name="p2021590320451"></a><a name="p2021590320451"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="46.21%" headers="mcps1.2.4.1.3 "><p id="p2687544020451"><a name="p2687544020451"></a><a name="p2687544020451"></a>Unique transaction identifier.</p>
<p id="p4055236820451"><a name="p4055236820451"></a><a name="p4055236820451"></a></p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>If the MIME type of the object in the object upload is not in  _XXX/XXX_  format, OBS \(compatible with OpenStack Swift\) adopts the default type  **application/octet-stream**. OpenStack Swift is able to return  **Content-Type**  in non-_XXX/XXX_  format.  

## Show Object Details<a name="section2201390"></a>

Show the content and metadata of the  **goodbye**  object in the  **marktwain**  container:

```
curl -i http://172.28.54.12:80/v1/AUTH_4b34aa268d8c45879cf4da16443d3f95/marketwain/goodbye -H "X-Auth-Token:74565091b56b4783818430cecb283e7f"  -XGET
```

```
HTTP/1.1 200 OK
X-Trans-Id: tx000001513c8f3596370c0-d09b6a1f24
Accept-Ranges: bytes
Content-Length: 15
Content-Type: application/octet-stream
Date: Wed, 25 Nov 2015 02:53:17 GMT
ETag: e85f5c28b588fa64a379ba876e3591d2
Last-Modified: Wed, 25 Nov 2015 02:53:08 GMT
X-Timestamp: 1448419988.76750

[15 Byte data content]
```

## Show Object Details for a Non-Existing Object<a name="section60098234144536"></a>

Show object details for the  **notexist**  object, which does not exist, in the  **marktwain**  container:

```
curl -i http://172.28.54.12:80/v1/AUTH_4b34aa268d8c45879cf4da16443d3f95/marketwain/notexist -H "X-Auth-Token:74565091b56b4783818430cecb283e7f"  -XGET
```

```
HTTP/1.1 404 Not Found
X-Trans-Id: tx000001513c90aab6370c0-b90ea4b1b7
Content-Type: text/html;charset=UTF-8
Date: Wed, 25 Nov 2015 02:54:52 GMT
Content-Length: 70

<html><h1>Not Found</h1><p>The resource could not be found.</p></html>
```

