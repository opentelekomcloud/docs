# Querying Details About a Specified Image \(Discarded\)<a name="EN-US_TOPIC_0065817697"></a>

## Function<a name="en-us_topic_0057973108_section56055574"></a>

This API is used to query the details about the specified image.

## Constraints<a name="en-us_topic_0057973108_section44207621"></a>

-   This API will be discarded. You are advised to use the IMS API "Querying Image Details \(Native OpenStack API\)".

## URI<a name="en-us_topic_0057973108_section34738119"></a>

GET /v2/\{project\_id\}/images/\{image\_id\}

GET /v2.1/\{project\_id\}/images/\{image\_id\}

[Table 1](#en-us_topic_0057973108_en-us_topic_0020212650_table62669527)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="en-us_topic_0057973108_en-us_topic_0020212650_table62669527"></a>
<table><thead align="left"><tr id="en-us_topic_0057973108_en-us_topic_0020212650_row33894570"><th class="cellrowborder" valign="top" width="20.74%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.05%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="60.209999999999994%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973108_en-us_topic_0020212650_row8419032"><td class="cellrowborder" valign="top" width="20.74%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973108_en-us_topic_0020212650_p10852974"><a name="en-us_topic_0057973108_en-us_topic_0020212650_p10852974"></a><a name="en-us_topic_0057973108_en-us_topic_0020212650_p10852974"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973108_en-us_topic_0020212650_p6675738"><a name="en-us_topic_0057973108_en-us_topic_0020212650_p6675738"></a><a name="en-us_topic_0057973108_en-us_topic_0020212650_p6675738"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="60.209999999999994%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0057973108_row132721948105411"><td class="cellrowborder" valign="top" width="20.74%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973108_p11272124885417"><a name="en-us_topic_0057973108_p11272124885417"></a><a name="en-us_topic_0057973108_p11272124885417"></a>image_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973108_p11272104895417"><a name="en-us_topic_0057973108_p11272104895417"></a><a name="en-us_topic_0057973108_p11272104895417"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="60.209999999999994%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973108_p11272948145412"><a name="en-us_topic_0057973108_p11272948145412"></a><a name="en-us_topic_0057973108_p11272948145412"></a>Specifies the image ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0057973108_section24047537"></a>

None

## Response<a name="en-us_topic_0057973108_section15101241"></a>

[Table 2](#en-us_topic_0057973108_table61215668)  describes the response parameters.

**Table  2**  Response parameters

<a name="en-us_topic_0057973108_table61215668"></a>
<table><thead align="left"><tr id="en-us_topic_0057973108_row24851438"><th class="cellrowborder" valign="top" width="20.792079207920786%" id="mcps1.2.5.1.1"><p id="en-us_topic_0057973108_p66809482"><a name="en-us_topic_0057973108_p66809482"></a><a name="en-us_topic_0057973108_p66809482"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.8019801980198%" id="mcps1.2.5.1.2"><p id="p722815295256"><a name="p722815295256"></a><a name="p722815295256"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="19.8019801980198%" id="mcps1.2.5.1.3"><p id="en-us_topic_0057973108_p42858995"><a name="en-us_topic_0057973108_p42858995"></a><a name="en-us_topic_0057973108_p42858995"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="39.6039603960396%" id="mcps1.2.5.1.4"><p id="en-us_topic_0057973108_p11729738"><a name="en-us_topic_0057973108_p11729738"></a><a name="en-us_topic_0057973108_p11729738"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973108_row10584712"><td class="cellrowborder" valign="top" width="20.792079207920786%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973108_p52055347"><a name="en-us_topic_0057973108_p52055347"></a><a name="en-us_topic_0057973108_p52055347"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="19.8019801980198%" headers="mcps1.2.5.1.2 "><p id="p102281629102517"><a name="p102281629102517"></a><a name="p102281629102517"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="19.8019801980198%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973108_p55733554"><a name="en-us_topic_0057973108_p55733554"></a><a name="en-us_topic_0057973108_p55733554"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.6039603960396%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973108_p58758990"><a name="en-us_topic_0057973108_p58758990"></a><a name="en-us_topic_0057973108_p58758990"></a>Specifies the image ID in UUID format.</p>
</td>
</tr>
<tr id="en-us_topic_0057973108_row59068863"><td class="cellrowborder" valign="top" width="20.792079207920786%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973108_p19848593"><a name="en-us_topic_0057973108_p19848593"></a><a name="en-us_topic_0057973108_p19848593"></a>links</p>
</td>
<td class="cellrowborder" valign="top" width="19.8019801980198%" headers="mcps1.2.5.1.2 "><p id="p6228182922512"><a name="p6228182922512"></a><a name="p6228182922512"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="19.8019801980198%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973108_p64232187"><a name="en-us_topic_0057973108_p64232187"></a><a name="en-us_topic_0057973108_p64232187"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="39.6039603960396%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973108_p50826682"><a name="en-us_topic_0057973108_p50826682"></a><a name="en-us_topic_0057973108_p50826682"></a>Specifies the shortcut link of the image.</p>
</td>
</tr>
<tr id="en-us_topic_0057973108_row54786954"><td class="cellrowborder" valign="top" width="20.792079207920786%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973108_p8558285"><a name="en-us_topic_0057973108_p8558285"></a><a name="en-us_topic_0057973108_p8558285"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="19.8019801980198%" headers="mcps1.2.5.1.2 "><p id="p122913290251"><a name="p122913290251"></a><a name="p122913290251"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="19.8019801980198%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973108_p22132493"><a name="en-us_topic_0057973108_p22132493"></a><a name="en-us_topic_0057973108_p22132493"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.6039603960396%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973108_p54815394"><a name="en-us_topic_0057973108_p54815394"></a><a name="en-us_topic_0057973108_p54815394"></a>Specifies the image name.</p>
</td>
</tr>
<tr id="en-us_topic_0057973108_row23576498"><td class="cellrowborder" valign="top" width="20.792079207920786%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973108_p30648192"><a name="en-us_topic_0057973108_p30648192"></a><a name="en-us_topic_0057973108_p30648192"></a>metadata</p>
</td>
<td class="cellrowborder" valign="top" width="19.8019801980198%" headers="mcps1.2.5.1.2 "><p id="p9229122916254"><a name="p9229122916254"></a><a name="p9229122916254"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="19.8019801980198%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973108_p66584527"><a name="en-us_topic_0057973108_p66584527"></a><a name="en-us_topic_0057973108_p66584527"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="39.6039603960396%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973108_p49491727"><a name="en-us_topic_0057973108_p49491727"></a><a name="en-us_topic_0057973108_p49491727"></a>Specifies the key pair of the metadata.</p>
</td>
</tr>
<tr id="en-us_topic_0057973108_row42772360"><td class="cellrowborder" valign="top" width="20.792079207920786%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973108_p42009164"><a name="en-us_topic_0057973108_p42009164"></a><a name="en-us_topic_0057973108_p42009164"></a>OS-EXT-IMG-SIZE:size</p>
</td>
<td class="cellrowborder" valign="top" width="19.8019801980198%" headers="mcps1.2.5.1.2 "><p id="p12291529122513"><a name="p12291529122513"></a><a name="p12291529122513"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="19.8019801980198%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973108_p47299124"><a name="en-us_topic_0057973108_p47299124"></a><a name="en-us_topic_0057973108_p47299124"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="39.6039603960396%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973108_p18169746"><a name="en-us_topic_0057973108_p18169746"></a><a name="en-us_topic_0057973108_p18169746"></a>Specifies the image size. The value must be greater than zero.</p>
</td>
</tr>
<tr id="en-us_topic_0057973108_row29309990"><td class="cellrowborder" valign="top" width="20.792079207920786%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973108_p25298969"><a name="en-us_topic_0057973108_p25298969"></a><a name="en-us_topic_0057973108_p25298969"></a>minDisk</p>
</td>
<td class="cellrowborder" valign="top" width="19.8019801980198%" headers="mcps1.2.5.1.2 "><p id="p7229529152517"><a name="p7229529152517"></a><a name="p7229529152517"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="19.8019801980198%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973108_p35950580"><a name="en-us_topic_0057973108_p35950580"></a><a name="en-us_topic_0057973108_p35950580"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="39.6039603960396%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973108_p51210884"><a name="en-us_topic_0057973108_p51210884"></a><a name="en-us_topic_0057973108_p51210884"></a>Specifies the minimum disk size in GB required by the image. The value must be greater than zero.</p>
</td>
</tr>
<tr id="en-us_topic_0057973108_row58244779"><td class="cellrowborder" valign="top" width="20.792079207920786%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973108_p20206679"><a name="en-us_topic_0057973108_p20206679"></a><a name="en-us_topic_0057973108_p20206679"></a>minRam</p>
</td>
<td class="cellrowborder" valign="top" width="19.8019801980198%" headers="mcps1.2.5.1.2 "><p id="p12229132942510"><a name="p12229132942510"></a><a name="p12229132942510"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="19.8019801980198%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973108_p26128336"><a name="en-us_topic_0057973108_p26128336"></a><a name="en-us_topic_0057973108_p26128336"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="39.6039603960396%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973108_p31977543"><a name="en-us_topic_0057973108_p31977543"></a><a name="en-us_topic_0057973108_p31977543"></a>Specifies the minimum memory size in GB required by the image. The value must be greater than zero.</p>
</td>
</tr>
<tr id="en-us_topic_0057973108_row19362434"><td class="cellrowborder" valign="top" width="20.792079207920786%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973108_p24853313"><a name="en-us_topic_0057973108_p24853313"></a><a name="en-us_topic_0057973108_p24853313"></a>progress</p>
</td>
<td class="cellrowborder" valign="top" width="19.8019801980198%" headers="mcps1.2.5.1.2 "><p id="p1022912922511"><a name="p1022912922511"></a><a name="p1022912922511"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="19.8019801980198%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973108_p66961361"><a name="en-us_topic_0057973108_p66961361"></a><a name="en-us_topic_0057973108_p66961361"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="39.6039603960396%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973108_p38870403"><a name="en-us_topic_0057973108_p38870403"></a><a name="en-us_topic_0057973108_p38870403"></a>Specifies the image upload progress. The value must be greater than zero.</p>
</td>
</tr>
<tr id="en-us_topic_0057973108_row14289307"><td class="cellrowborder" valign="top" width="20.792079207920786%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973108_p16583191"><a name="en-us_topic_0057973108_p16583191"></a><a name="en-us_topic_0057973108_p16583191"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="19.8019801980198%" headers="mcps1.2.5.1.2 "><p id="p142291929182517"><a name="p142291929182517"></a><a name="p142291929182517"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="19.8019801980198%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973108_p1061256"><a name="en-us_topic_0057973108_p1061256"></a><a name="en-us_topic_0057973108_p1061256"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.6039603960396%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973108_p50693992"><a name="en-us_topic_0057973108_p50693992"></a><a name="en-us_topic_0057973108_p50693992"></a>Specifies the image status.</p>
</td>
</tr>
<tr id="en-us_topic_0057973108_row53592751"><td class="cellrowborder" valign="top" width="20.792079207920786%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973108_p46045538"><a name="en-us_topic_0057973108_p46045538"></a><a name="en-us_topic_0057973108_p46045538"></a>created</p>
</td>
<td class="cellrowborder" valign="top" width="19.8019801980198%" headers="mcps1.2.5.1.2 "><p id="p13230152918256"><a name="p13230152918256"></a><a name="p13230152918256"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="19.8019801980198%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973108_p38701135"><a name="en-us_topic_0057973108_p38701135"></a><a name="en-us_topic_0057973108_p38701135"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.6039603960396%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973108_p45316593"><a name="en-us_topic_0057973108_p45316593"></a><a name="en-us_topic_0057973108_p45316593"></a>Specifies the image creation time. The value is in ISO8601 format, such as <strong id="en-us_topic_0057973108_b49080483"><a name="en-us_topic_0057973108_b49080483"></a><a name="en-us_topic_0057973108_b49080483"></a>2013-06-09T06:42:18Z</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0057973108_row5196159"><td class="cellrowborder" valign="top" width="20.792079207920786%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973108_p18235700"><a name="en-us_topic_0057973108_p18235700"></a><a name="en-us_topic_0057973108_p18235700"></a>updated</p>
</td>
<td class="cellrowborder" valign="top" width="19.8019801980198%" headers="mcps1.2.5.1.2 "><p id="p9230112914252"><a name="p9230112914252"></a><a name="p9230112914252"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="19.8019801980198%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973108_p696709"><a name="en-us_topic_0057973108_p696709"></a><a name="en-us_topic_0057973108_p696709"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.6039603960396%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973108_p7710750"><a name="en-us_topic_0057973108_p7710750"></a><a name="en-us_topic_0057973108_p7710750"></a>Specifies the image update time. The value is in ISO8601 format, such as <strong id="en-us_topic_0057973108_b59084293"><a name="en-us_topic_0057973108_b59084293"></a><a name="en-us_topic_0057973108_b59084293"></a>2013-06-09T06:42:18Z</strong>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **links**  parameter description

<a name="table82851550164111"></a>
<table><thead align="left"><tr id="en-us_topic_0065817695_en-us_topic_0057973086_row54901254195115"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.1"><p id="en-us_topic_0065817695_p131661047125817"><a name="en-us_topic_0065817695_p131661047125817"></a><a name="en-us_topic_0065817695_p131661047125817"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.2"><p id="en-us_topic_0065817695_p15166194715818"><a name="en-us_topic_0065817695_p15166194715818"></a><a name="en-us_topic_0065817695_p15166194715818"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.3"><p id="en-us_topic_0065817695_p10166194719587"><a name="en-us_topic_0065817695_p10166194719587"></a><a name="en-us_topic_0065817695_p10166194719587"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="44%" id="mcps1.2.5.1.4"><p id="en-us_topic_0065817695_p91661478589"><a name="en-us_topic_0065817695_p91661478589"></a><a name="en-us_topic_0065817695_p91661478589"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0065817695_en-us_topic_0057973086_row1549185415113"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0065817695_en-us_topic_0057973086_p1449195414513"><a name="en-us_topic_0065817695_en-us_topic_0057973086_p1449195414513"></a><a name="en-us_topic_0065817695_en-us_topic_0057973086_p1449195414513"></a>href</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0065817695_en-us_topic_0057973086_p1449195455118"><a name="en-us_topic_0065817695_en-us_topic_0057973086_p1449195455118"></a><a name="en-us_topic_0065817695_en-us_topic_0057973086_p1449195455118"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0065817695_en-us_topic_0057973086_p449195425114"><a name="en-us_topic_0065817695_en-us_topic_0057973086_p449195425114"></a><a name="en-us_topic_0065817695_en-us_topic_0057973086_p449195425114"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0065817695_en-us_topic_0057973086_p18491754135111"><a name="en-us_topic_0065817695_en-us_topic_0057973086_p18491754135111"></a><a name="en-us_topic_0065817695_en-us_topic_0057973086_p18491754135111"></a>Specifies the link of the corresponding resource.</p>
</td>
</tr>
<tr id="en-us_topic_0065817695_en-us_topic_0057973086_row16491145435118"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0065817695_en-us_topic_0057973086_p4491155415518"><a name="en-us_topic_0065817695_en-us_topic_0057973086_p4491155415518"></a><a name="en-us_topic_0065817695_en-us_topic_0057973086_p4491155415518"></a>rel</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0065817695_en-us_topic_0057973086_p2491185485110"><a name="en-us_topic_0065817695_en-us_topic_0057973086_p2491185485110"></a><a name="en-us_topic_0065817695_en-us_topic_0057973086_p2491185485110"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0065817695_en-us_topic_0057973086_p1449165411514"><a name="en-us_topic_0065817695_en-us_topic_0057973086_p1449165411514"></a><a name="en-us_topic_0065817695_en-us_topic_0057973086_p1449165411514"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0065817695_en-us_topic_0057973086_p44540131181624"><a name="en-us_topic_0065817695_en-us_topic_0057973086_p44540131181624"></a><a name="en-us_topic_0065817695_en-us_topic_0057973086_p44540131181624"></a>The value can be:</p>
<a name="en-us_topic_0065817695_en-us_topic_0057973086_ul50320171175059"></a><a name="en-us_topic_0065817695_en-us_topic_0057973086_ul50320171175059"></a><ul id="en-us_topic_0065817695_en-us_topic_0057973086_ul50320171175059"><li><strong id="en-us_topic_0065817695_b11003816175111"><a name="en-us_topic_0065817695_b11003816175111"></a><a name="en-us_topic_0065817695_b11003816175111"></a>self</strong>: A self link contains a version link to the resource. Use these links when the link is followed immediately.</li><li><strong id="en-us_topic_0065817695_b60630642175154"><a name="en-us_topic_0065817695_b60630642175154"></a><a name="en-us_topic_0065817695_b60630642175154"></a>bookmark</strong>: A bookmark link provides a permanent link to a resource, which is suitable for long term storage.</li><li><strong id="en-us_topic_0065817695_b28772520175321"><a name="en-us_topic_0065817695_b28772520175321"></a><a name="en-us_topic_0065817695_b28772520175321"></a>alternate</strong>: An alternate link can contain an alternate representation of the resource. For example, an OpenStack Compute image may have an alternate representation in the OpenStack image service.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0065817695_en-us_topic_0057973086_row15491195465112"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0065817695_en-us_topic_0057973086_p149145411510"><a name="en-us_topic_0065817695_en-us_topic_0057973086_p149145411510"></a><a name="en-us_topic_0065817695_en-us_topic_0057973086_p149145411510"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0065817695_en-us_topic_0057973086_p1949195405118"><a name="en-us_topic_0065817695_en-us_topic_0057973086_p1949195405118"></a><a name="en-us_topic_0065817695_en-us_topic_0057973086_p1949195405118"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0065817695_en-us_topic_0057973086_p649155425114"><a name="en-us_topic_0065817695_en-us_topic_0057973086_p649155425114"></a><a name="en-us_topic_0065817695_en-us_topic_0057973086_p649155425114"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0065817695_en-us_topic_0057973086_p1671811201581"><a name="en-us_topic_0065817695_en-us_topic_0057973086_p1671811201581"></a><a name="en-us_topic_0065817695_en-us_topic_0057973086_p1671811201581"></a>The type attribute provides a hint as to the type of representation to expect when following the link.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="en-us_topic_0057973108_section1693441"></a>

```
GET https://{endpoint}/v2/9c53a566cb3443ab910cf0daebca90c4/images/17a1890b-0fa4-485e-8505-14e294017988
GET https://{endpoint}/v2.1/9c53a566cb3443ab910cf0daebca90c4/images/17a1890b-0fa4-485e-8505-14e294017988
```

## Example Response<a name="section1027013622314"></a>

```
{
    "image": {
        "status": "ACTIVE", 
        "updated": "2015-12-27T02:52:25Z", 
        "name": "cirror", 
        "links": [
            {
                "href": "https://compute.localdomain.com:8001/v2/719e9483f42d4784a089862ac4c3e8d0/images/17a1890b-0fa4-485e-8505-14e294017988", 
                "rel": "self"
            }, 
            {
                "href": "https://compute.localdomain.com:8001/719e9483f42d4784a089862ac4c3e8d0/images/17a1890b-0fa4-485e-8505-14e294017988", 
                "rel": "bookmark"
            }, 
            {
                "href": "https://https://image.az2.dc1.domainname.com:443/719e9483f42d4784a089862ac4c3e8d0/images/17a1890b-0fa4-485e-8505-14e294017988", 
                "type": "application/vnd.openstack.image", 
                "rel": "alternate"
            }
        ], 
        "created": "2015-12-27T02:52:24Z", 
        "minDisk": 0, 
        "progress": 100, 
        "minRam": 0, 
        "metadata": {
            "__os_version": "CentOS 4.4 32bit", 
            "file_format": "img", 
            "file_name": "**.img", 
            "describe": "", 
            "__os_type": "Linux", 
            "virtual_env_type": "KVM", 
            "hw_disk_bus": "scsi"
        }, 
        "id": "17a1890b-0fa4-485e-8505-14e294017988", 
        "OS-EXT-IMG-SIZE:size": 13167616
    }
}
```

## Returned Values<a name="en-us_topic_0057973108_section3564114017426"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

