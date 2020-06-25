# Querying Public Zones<a name="EN-US_TOPIC_0037134402"></a>

## Function<a name="section2763065016101"></a>

Query public zones in list.

## URI<a name="section53701671161015"></a>

-   URI format

    GET /v2/zones?type=\{type\}&limit=\{limit\}&marker=\{marker\}&offset=\{offset\}&tags=\{tags\}


-   Parameter description

    **Table  1**  Parameters in the URI

    <a name="table36421405182556"></a><table><thead align="left"><tr id="row35113810182556"><th class="cellrowborder" valign="top" width="17.669999999999998%" id="mcps1.2.5.1.1"><p id="p29205341182624"><a name="p29205341182624"></a><a name="p29205341182624"></a><strong id="b162774213314533"><a name="b162774213314533"></a><a name="b162774213314533"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.49%" id="mcps1.2.5.1.2"><p id="p16822416182624"><a name="p16822416182624"></a><a name="p16822416182624"></a><strong id="b593421527191713"><a name="b593421527191713"></a><a name="b593421527191713"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="12.839999999999998%" id="mcps1.2.5.1.3"><p id="p20438464182624"><a name="p20438464182624"></a><a name="p20438464182624"></a><strong id="b84235270619112"><a name="b84235270619112"></a><a name="b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="p44902868182624"><a name="p44902868182624"></a><a name="p44902868182624"></a><strong id="b842352706112423"><a name="b842352706112423"></a><a name="b842352706112423"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row7883687182556"><td class="cellrowborder" valign="top" width="17.669999999999998%" headers="mcps1.2.5.1.1 "><p id="p29178851182717"><a name="p29178851182717"></a><a name="p29178851182717"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.49%" headers="mcps1.2.5.1.2 "><p id="p2590622182717"><a name="p2590622182717"></a><a name="p2590622182717"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.839999999999998%" headers="mcps1.2.5.1.3 "><p id="p66359104182717"><a name="p66359104182717"></a><a name="p66359104182717"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="p53225083153722"><a name="p53225083153722"></a><a name="p53225083153722"></a>Zone type, which can be <strong id="b1982092916111747"><a name="b1982092916111747"></a><a name="b1982092916111747"></a>public</strong>&nbsp;or&nbsp;<strong id="b1971245989111747"><a name="b1971245989111747"></a><a name="b1971245989111747"></a>private</strong></p>
    <a name="ul7470137153957"></a><a name="ul7470137153957"></a><ul id="ul7470137153957"><li id="li58095704153957"><a name="li58095704153957"></a><a name="li58095704153957"></a><strong id="b1702127103733"><a name="b1702127103733"></a><a name="b1702127103733"></a>public</strong>: Public zones are queried.</li><li id="li54676736153957"><a name="li54676736153957"></a><a name="li54676736153957"></a><strong id="b2104944103740"><a name="b2104944103740"></a><a name="b2104944103740"></a>private</strong>: Private zones are queried.<p id="p47260004103624"><a name="p47260004103624"></a><a name="p47260004103624"></a>If the value is left blank, public zones are queried by default.</p>
    </li></ul>
    </td>
    </tr>
    <tr id="row12208459182556"><td class="cellrowborder" valign="top" width="17.669999999999998%" headers="mcps1.2.5.1.1 "><p id="p17456213182720"><a name="p17456213182720"></a><a name="p17456213182720"></a>marker</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.49%" headers="mcps1.2.5.1.2 "><p id="p4667185182720"><a name="p4667185182720"></a><a name="p4667185182720"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.839999999999998%" headers="mcps1.2.5.1.3 "><p id="p42497672182720"><a name="p42497672182720"></a><a name="p42497672182720"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="p4485307103956"><a name="p4485307103956"></a><a name="p4485307103956"></a>Start resource ID of pagination query</p>
    <p id="p33507717104015"><a name="p33507717104015"></a><a name="p33507717104015"></a>If the parameter is left blank, only resources on the first page are queried.</p>
    </td>
    </tr>
    <tr id="row29489517182630"><td class="cellrowborder" valign="top" width="17.669999999999998%" headers="mcps1.2.5.1.1 "><p id="p43326778182720"><a name="p43326778182720"></a><a name="p43326778182720"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.49%" headers="mcps1.2.5.1.2 "><p id="p19808096182720"><a name="p19808096182720"></a><a name="p19808096182720"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.839999999999998%" headers="mcps1.2.5.1.3 "><p id="p60951943182720"><a name="p60951943182720"></a><a name="p60951943182720"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><a name="ul38160342182720"></a><a name="ul38160342182720"></a><ul id="ul38160342182720"><li id="li33285943103832"><a name="li33285943103832"></a><a name="li33285943103832"></a>Number of resources returned on each page</li><li id="li35820204182720"><a name="li35820204182720"></a><a name="li35820204182720"></a>Value range: 0–500<p id="p4242767103910"><a name="p4242767103910"></a><a name="p4242767103910"></a>Commonly used values are <strong id="b16019034103915"><a name="b16019034103915"></a><a name="b16019034103915"></a>10</strong>,&nbsp;<strong id="b22998024103927"><a name="b22998024103927"></a><a name="b22998024103927"></a>20</strong>, and&nbsp;<strong id="b12834458103923"><a name="b12834458103923"></a><a name="b12834458103923"></a>50</strong>.</p>
    </li></ul>
    </td>
    </tr>
    <tr id="row56409238193951"><td class="cellrowborder" valign="top" width="17.669999999999998%" headers="mcps1.2.5.1.1 "><p id="p5745576193951"><a name="p5745576193951"></a><a name="p5745576193951"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.49%" headers="mcps1.2.5.1.2 "><p id="p62738535193951"><a name="p62738535193951"></a><a name="p62738535193951"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.839999999999998%" headers="mcps1.2.5.1.3 "><p id="p48656570193951"><a name="p48656570193951"></a><a name="p48656570193951"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><a name="ul35486924194016"></a><a name="ul35486924194016"></a><ul id="ul35486924194016"><li id="li50946860194016"><a name="li50946860194016"></a><a name="li50946860194016"></a>Start page of the list, which ranges from 0 to 2147483647.</li><li id="li38280782194034"><a name="li38280782194034"></a><a name="li38280782194034"></a>When the value of <strong id="b842352706193255"><a name="b842352706193255"></a><a name="b842352706193255"></a>marker</strong> is not blank, it determines the start of a page.</li></ul>
    </td>
    </tr>
    <tr id="row1736769311550"><td class="cellrowborder" valign="top" width="17.669999999999998%" headers="mcps1.2.5.1.1 "><p id="p1821826211550"><a name="p1821826211550"></a><a name="p1821826211550"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.49%" headers="mcps1.2.5.1.2 "><p id="p6639315411550"><a name="p6639315411550"></a><a name="p6639315411550"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.839999999999998%" headers="mcps1.2.5.1.3 "><p id="p913636111550"><a name="p913636111550"></a><a name="p913636111550"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="p28691609115519"><a name="p28691609115519"></a><a name="p28691609115519"></a>Resource tag</p>
    <p id="p6833525115523"><a name="p6833525115523"></a><a name="p6833525115523"></a>The format is as follows: <strong id="b8423527069140"><a name="b8423527069140"></a><a name="b8423527069140"></a>key1,value1|key2,value2</strong>.</p>
    <p id="p32051112114146"><a name="p32051112114146"></a><a name="p32051112114146"></a>Multiple tags are separated by vertical bar (|). The key and value of each tag are separated by comma (,).</p>
    <p id="p15239506115938"><a name="p15239506115938"></a><a name="p15239506115938"></a>All tags listed will be queried.</p>
    <p id="p39866681115027"><a name="p39866681115027"></a><a name="p39866681115027"></a>For details, see section <a href="tag-management.html">Tag Management</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section44958995161021"></a>

None

## Response<a name="section40090803161031"></a>

-   Parameter description

    **Table  2**  Parameters in the response

    <a name="table6655637171923"></a><table><thead align="left"><tr id="row12436182171923"><th class="cellrowborder" valign="top" width="18.529999999999998%" id="mcps1.2.4.1.1"><p id="p18040723171923"><a name="p18040723171923"></a><a name="p18040723171923"></a><strong id="b162774213314533_1"><a name="b162774213314533_1"></a><a name="b162774213314533_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="30.45%" id="mcps1.2.4.1.2"><p id="p12288867171923"><a name="p12288867171923"></a><a name="p12288867171923"></a><strong id="b84235270619112_1"><a name="b84235270619112_1"></a><a name="b84235270619112_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="51.019999999999996%" id="mcps1.2.4.1.3"><p id="p16021685171923"><a name="p16021685171923"></a><a name="p16021685171923"></a><strong id="b842352706112423_1"><a name="b842352706112423_1"></a><a name="b842352706112423_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row33084878171923"><td class="cellrowborder" valign="top" width="18.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p10518479171923"><a name="p10518479171923"></a><a name="p10518479171923"></a>zones</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.45%" headers="mcps1.2.4.1.2 "><p id="p17816324171923"><a name="p17816324171923"></a><a name="p17816324171923"></a>List data structure</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.019999999999996%" headers="mcps1.2.4.1.3 "><p id="p64387025171923"><a name="p64387025171923"></a><a name="p64387025171923"></a>Zone list object</p>
    </td>
    </tr>
    <tr id="row45921614175143"><td class="cellrowborder" valign="top" width="18.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p10641344175143"><a name="p10641344175143"></a><a name="p10641344175143"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.45%" headers="mcps1.2.4.1.2 "><p id="p24643947175143"><a name="p24643947175143"></a><a name="p24643947175143"></a>object</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.019999999999996%" headers="mcps1.2.4.1.3 "><p id="p50002691175143"><a name="p50002691175143"></a><a name="p50002691175143"></a>Number of resources that meet the filter condition</p>
    </td>
    </tr>
    </tbody>
    </table>

    [Table 3](#table6348803417233) describes parameters under the **zones** field, and [Table 4](#table52442344175457) describes the parameter under the **metadata**  field.

    **Table  3**  Description of the  **zones**  field

    <a name="table6348803417233"></a><table><thead align="left"><tr id="en-us_topic_0037139748_row54125868171039"><th class="cellrowborder" valign="top" width="18.37%" id="mcps1.2.4.1.1"><p id="en-us_topic_0037139748_p46128019171039"><a name="en-us_topic_0037139748_p46128019171039"></a><a name="en-us_topic_0037139748_p46128019171039"></a><strong id="b162774213314533_2"><a name="b162774213314533_2"></a><a name="b162774213314533_2"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.39%" id="mcps1.2.4.1.2"><p id="en-us_topic_0037139748_p61288737171039"><a name="en-us_topic_0037139748_p61288737171039"></a><a name="en-us_topic_0037139748_p61288737171039"></a><strong id="b84235270619112_2"><a name="b84235270619112_2"></a><a name="b84235270619112_2"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="62.239999999999995%" id="mcps1.2.4.1.3"><p id="en-us_topic_0037139748_p39427830171039"><a name="en-us_topic_0037139748_p39427830171039"></a><a name="en-us_topic_0037139748_p39427830171039"></a><strong id="b842352706112423_2"><a name="b842352706112423_2"></a><a name="b842352706112423_2"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0037139748_row3275315171039"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037139748_p13677558171039"><a name="en-us_topic_0037139748_p13677558171039"></a><a name="en-us_topic_0037139748_p13677558171039"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037139748_p31480160171039"><a name="en-us_topic_0037139748_p31480160171039"></a><a name="en-us_topic_0037139748_p31480160171039"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.239999999999995%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037139748_p55186322171039"><a name="en-us_topic_0037139748_p55186322171039"></a><a name="en-us_topic_0037139748_p55186322171039"></a>Zone ID, which is a UUID used to identify the zone</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037139748_row62038903171039"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037139748_p21725743171039"><a name="en-us_topic_0037139748_p21725743171039"></a><a name="en-us_topic_0037139748_p21725743171039"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037139748_p55078653171039"><a name="en-us_topic_0037139748_p55078653171039"></a><a name="en-us_topic_0037139748_p55078653171039"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.239999999999995%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037139748_p65545475171039"><a name="en-us_topic_0037139748_p65545475171039"></a><a name="en-us_topic_0037139748_p65545475171039"></a>Zone name</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037139748_row24663709171039"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037139748_p56112529171039"><a name="en-us_topic_0037139748_p56112529171039"></a><a name="en-us_topic_0037139748_p56112529171039"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037139748_p46656524171039"><a name="en-us_topic_0037139748_p46656524171039"></a><a name="en-us_topic_0037139748_p46656524171039"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.239999999999995%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037139748_p31778607171039"><a name="en-us_topic_0037139748_p31778607171039"></a><a name="en-us_topic_0037139748_p31778607171039"></a>Zone description</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037139748_row34212800171039"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037139748_p51657401171039"><a name="en-us_topic_0037139748_p51657401171039"></a><a name="en-us_topic_0037139748_p51657401171039"></a>email</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037139748_p336297171039"><a name="en-us_topic_0037139748_p336297171039"></a><a name="en-us_topic_0037139748_p336297171039"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.239999999999995%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037139748_p66322352171039"><a name="en-us_topic_0037139748_p66322352171039"></a><a name="en-us_topic_0037139748_p66322352171039"></a>Email address of the administrator managing the zone</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037139748_row45341886171039"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037139748_p22374403171039"><a name="en-us_topic_0037139748_p22374403171039"></a><a name="en-us_topic_0037139748_p22374403171039"></a>zone_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037139748_p16323247171039"><a name="en-us_topic_0037139748_p16323247171039"></a><a name="en-us_topic_0037139748_p16323247171039"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.239999999999995%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037139748_p58527202171039"><a name="en-us_topic_0037139748_p58527202171039"></a><a name="en-us_topic_0037139748_p58527202171039"></a>Zone type, which can be <strong id="b842352706115152"><a name="b842352706115152"></a><a name="b842352706115152"></a>public</strong>&nbsp;or&nbsp;<strong id="b842352706115156"><a name="b842352706115156"></a><a name="b842352706115156"></a>private</strong></p>
    </td>
    </tr>
    <tr id="en-us_topic_0037139748_row36905265171039"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037139748_p4888971171039"><a name="en-us_topic_0037139748_p4888971171039"></a><a name="en-us_topic_0037139748_p4888971171039"></a>ttl</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037139748_p16027579171039"><a name="en-us_topic_0037139748_p16027579171039"></a><a name="en-us_topic_0037139748_p16027579171039"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.239999999999995%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037139748_p41240291171039"><a name="en-us_topic_0037139748_p41240291171039"></a><a name="en-us_topic_0037139748_p41240291171039"></a>TTL value of the SOA record set in the zone</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037139748_row29641334171039"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037139748_p63311148171039"><a name="en-us_topic_0037139748_p63311148171039"></a><a name="en-us_topic_0037139748_p63311148171039"></a>serial</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037139748_p26678057171039"><a name="en-us_topic_0037139748_p26678057171039"></a><a name="en-us_topic_0037139748_p26678057171039"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.239999999999995%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037139748_p7524749171039"><a name="en-us_topic_0037139748_p7524749171039"></a><a name="en-us_topic_0037139748_p7524749171039"></a>Serial number in the SOA record set in the zone, which identifies the change on the primary DNS server</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037139748_row44990376171039"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037139748_p30244483171039"><a name="en-us_topic_0037139748_p30244483171039"></a><a name="en-us_topic_0037139748_p30244483171039"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037139748_p47406357171039"><a name="en-us_topic_0037139748_p47406357171039"></a><a name="en-us_topic_0037139748_p47406357171039"></a>enum</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.239999999999995%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037139748_p9822846171039"><a name="en-us_topic_0037139748_p9822846171039"></a><a name="en-us_topic_0037139748_p9822846171039"></a>Resource status</p>
    <p id="en-us_topic_0037139748_p36239781171039"><a name="en-us_topic_0037139748_p36239781171039"></a><a name="en-us_topic_0037139748_p36239781171039"></a>The value can be <strong id="b84235270695628"><a name="b84235270695628"></a><a name="b84235270695628"></a>PENDING_CREATE</strong>,&nbsp;<strong id="b84235270695635"><a name="b84235270695635"></a><a name="b84235270695635"></a>ACTIVE</strong>,&nbsp;<strong id="b84235270695643"><a name="b84235270695643"></a><a name="b84235270695643"></a>PENDING_DELETE</strong>, or&nbsp;<strong id="b84235270695650"><a name="b84235270695650"></a><a name="b84235270695650"></a>ERROR</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037139748_row1454557171039"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037139748_p51202644171039"><a name="en-us_topic_0037139748_p51202644171039"></a><a name="en-us_topic_0037139748_p51202644171039"></a>record_num</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037139748_p32016130171039"><a name="en-us_topic_0037139748_p32016130171039"></a><a name="en-us_topic_0037139748_p32016130171039"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.239999999999995%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037139748_p53878535171039"><a name="en-us_topic_0037139748_p53878535171039"></a><a name="en-us_topic_0037139748_p53878535171039"></a>Number of record sets in the zone</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037139748_row48476716171039"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037139748_p54136527171039"><a name="en-us_topic_0037139748_p54136527171039"></a><a name="en-us_topic_0037139748_p54136527171039"></a>pool_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037139748_p48020249171039"><a name="en-us_topic_0037139748_p48020249171039"></a><a name="en-us_topic_0037139748_p48020249171039"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.239999999999995%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037139748_p63987755171039"><a name="en-us_topic_0037139748_p63987755171039"></a><a name="en-us_topic_0037139748_p63987755171039"></a>Pool ID of the zone, which is assigned by the system</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037139748_row49967872171039"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037139748_p35791512171039"><a name="en-us_topic_0037139748_p35791512171039"></a><a name="en-us_topic_0037139748_p35791512171039"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037139748_p10454086171039"><a name="en-us_topic_0037139748_p10454086171039"></a><a name="en-us_topic_0037139748_p10454086171039"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.239999999999995%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037139748_p8704812171039"><a name="en-us_topic_0037139748_p8704812171039"></a><a name="en-us_topic_0037139748_p8704812171039"></a>Project ID of the zone</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037139748_row27690345171039"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037139748_p48529730171039"><a name="en-us_topic_0037139748_p48529730171039"></a><a name="en-us_topic_0037139748_p48529730171039"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037139748_p59988242171039"><a name="en-us_topic_0037139748_p59988242171039"></a><a name="en-us_topic_0037139748_p59988242171039"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.239999999999995%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037139748_p9292793171039"><a name="en-us_topic_0037139748_p9292793171039"></a><a name="en-us_topic_0037139748_p9292793171039"></a>Time when the zone was created</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037139748_row4377608115654"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037139748_p5844041115654"><a name="en-us_topic_0037139748_p5844041115654"></a><a name="en-us_topic_0037139748_p5844041115654"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037139748_p3605288915654"><a name="en-us_topic_0037139748_p3605288915654"></a><a name="en-us_topic_0037139748_p3605288915654"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.239999999999995%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037139748_p3460290715654"><a name="en-us_topic_0037139748_p3460290715654"></a><a name="en-us_topic_0037139748_p3460290715654"></a>Time when the zone was updated</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037139748_row384676871572"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037139748_p288749251572"><a name="en-us_topic_0037139748_p288749251572"></a><a name="en-us_topic_0037139748_p288749251572"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037139748_p571676251572"><a name="en-us_topic_0037139748_p571676251572"></a><a name="en-us_topic_0037139748_p571676251572"></a>object</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.239999999999995%" headers="mcps1.2.4.1.3 "><p id="p20067569143314"><a name="p20067569143314"></a><a name="p20067569143314"></a>Link of the current resource or other related resources</p>
    <p id="en-us_topic_0037139748_p660161572"><a name="en-us_topic_0037139748_p660161572"></a><a name="en-us_topic_0037139748_p660161572"></a>When a response is broken into pages, a <strong id="b84235270695245"><a name="b84235270695245"></a><a name="b84235270695245"></a>next</strong> link is provided to retrieve all results.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037139748_row177328815945"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037139748_p1595959815945"><a name="en-us_topic_0037139748_p1595959815945"></a><a name="en-us_topic_0037139748_p1595959815945"></a>masters</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037139748_p1765902715945"><a name="en-us_topic_0037139748_p1765902715945"></a><a name="en-us_topic_0037139748_p1765902715945"></a>enum</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.239999999999995%" headers="mcps1.2.4.1.3 "><p id="p33087898183618"><a name="p33087898183618"></a><a name="p33087898183618"></a>Master DNS servers, from which the slave servers get DNS information</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  Description of the  **metadata**  field

    <a name="table52442344175457"></a><table><thead align="left"><tr id="row58979189175457"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p46156243175457"><a name="p46156243175457"></a><a name="p46156243175457"></a><strong id="b162774213314533_3"><a name="b162774213314533_3"></a><a name="b162774213314533_3"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p47668234175457"><a name="p47668234175457"></a><a name="p47668234175457"></a><strong id="b84235270619112_3"><a name="b84235270619112_3"></a><a name="b84235270619112_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p35921708175457"><a name="p35921708175457"></a><a name="p35921708175457"></a><strong id="b842352706112423_3"><a name="b842352706112423_3"></a><a name="b842352706112423_3"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row54859922175457"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p14468674175457"><a name="p14468674175457"></a><a name="p14468674175457"></a>total_count</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p31111955175457"><a name="p31111955175457"></a><a name="p31111955175457"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p37040428175457"><a name="p37040428175457"></a><a name="p37040428175457"></a>Total number of resources</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "links": {
            "self": "https://Endpoint/v2/zones?type=public&limit=11&marker=&name=&status="
        },
        "zones": [
            {
                "id": "2c9eb155587194ec01587224c9f90149",
                "name": "example.com.",
                "description": "This is an example zone.",
                "email": "xx@example.com",
                "ttl": 300,
                "serial": 0,
                "masters": [],
                "status": "ACTIVE",
                "links": {
                    "self": "https://Endpoint/v2/zones/2c9eb155587194ec01587224c9f90149"
                },
                "pool_id": "00000000570e54ee01570e9939b20019",
                "project_id": "e55c6f3dc4e34c9f86353b664ae0e70c",
                "zone_type": "public",
                "created_at": "2016-11-17T11:56:03.439",
                "updated_at": "2016-11-17T11:56:05.528",
                "record_num": 2
            },
            {
                "id": "2c9eb155587228570158722996c50001",
                "name": "example.org.",
                "description": "This is an example zone.",
                "email": "xx@example.org",
                "ttl": 300,
                "serial": 0,
                "masters": [],
                "status": "PENDING_CREATE",
                "links": {
                    "self": "https://Endpoint/v2/zones/2c9eb155587228570158722996c50001"
                },
                "pool_id": "00000000570e54ee01570e9939b20019",
                "project_id": "e55c6f3dc4e34c9f86353b664ae0e70c",
                "zone_type": "public",
                "created_at": "2016-11-17T12:01:17.996",
                "updated_at": "2016-11-17T12:01:18.528",
                "record_num": 2
            }
        ],
        "metadata": {
            "total_count": 2
        }
    }
    
    ```


## Returned Value<a name="section42637797161043"></a>

See  [General Request Return Code](general-request-return-code.md).

