# Querying Private Zones<a name="EN-US_TOPIC_0057311029"></a>

## Function<a name="section2763065016101"></a>

Query private zones in list.

## URI<a name="section53701671161015"></a>

-   URI format

    GET /v2/zones?type=\{type\}&limit=\{limit\}&marker=\{marker\}&offset=\{offset\}&tags=\{tags\}


-   Parameter description

    **Table  1**  Parameters in the URI

    <a name="table36421405182556"></a><table><thead align="left"><tr id="row35113810182556"><th class="cellrowborder" valign="top" width="18.61%" id="mcps1.2.5.1.1"><p id="p29205341182624"><a name="p29205341182624"></a><a name="p29205341182624"></a><strong id="b162774213314533"><a name="b162774213314533"></a><a name="b162774213314533"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.869999999999997%" id="mcps1.2.5.1.2"><p id="p16822416182624"><a name="p16822416182624"></a><a name="p16822416182624"></a><strong id="b593421527191713"><a name="b593421527191713"></a><a name="b593421527191713"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="13.780000000000001%" id="mcps1.2.5.1.3"><p id="p20438464182624"><a name="p20438464182624"></a><a name="p20438464182624"></a><strong id="b84235270619112"><a name="b84235270619112"></a><a name="b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="47.74%" id="mcps1.2.5.1.4"><p id="p44902868182624"><a name="p44902868182624"></a><a name="p44902868182624"></a><strong id="b842352706112423"><a name="b842352706112423"></a><a name="b842352706112423"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row7883687182556"><td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.2.5.1.1 "><p id="p29178851182717"><a name="p29178851182717"></a><a name="p29178851182717"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.869999999999997%" headers="mcps1.2.5.1.2 "><p id="p2590622182717"><a name="p2590622182717"></a><a name="p2590622182717"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.780000000000001%" headers="mcps1.2.5.1.3 "><p id="p66359104182717"><a name="p66359104182717"></a><a name="p66359104182717"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.74%" headers="mcps1.2.5.1.4 "><p id="p41213064154029"><a name="p41213064154029"></a><a name="p41213064154029"></a>Zone type</p>
    <p id="p34437364141042"><a name="p34437364141042"></a><a name="p34437364141042"></a>The value is <strong id="b19216603"><a name="b19216603"></a><a name="b19216603"></a>private</strong>, indicating that private zones are queried.</p>
    </td>
    </tr>
    <tr id="row12208459182556"><td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.2.5.1.1 "><p id="p17456213182720"><a name="p17456213182720"></a><a name="p17456213182720"></a>marker</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.869999999999997%" headers="mcps1.2.5.1.2 "><p id="p4667185182720"><a name="p4667185182720"></a><a name="p4667185182720"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.780000000000001%" headers="mcps1.2.5.1.3 "><p id="p42497672182720"><a name="p42497672182720"></a><a name="p42497672182720"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.74%" headers="mcps1.2.5.1.4 "><p id="p352216816854"><a name="p352216816854"></a><a name="p352216816854"></a>Start resource ID of pagination query</p>
    <p id="p19759428182720"><a name="p19759428182720"></a><a name="p19759428182720"></a>If the parameter is left blank, only resources on the first page are queried.</p>
    </td>
    </tr>
    <tr id="row29489517182630"><td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.2.5.1.1 "><p id="p43326778182720"><a name="p43326778182720"></a><a name="p43326778182720"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.869999999999997%" headers="mcps1.2.5.1.2 "><p id="p19808096182720"><a name="p19808096182720"></a><a name="p19808096182720"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.780000000000001%" headers="mcps1.2.5.1.3 "><p id="p60951943182720"><a name="p60951943182720"></a><a name="p60951943182720"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.74%" headers="mcps1.2.5.1.4 "><a name="ul38160342182720"></a><a name="ul38160342182720"></a><ul id="ul38160342182720"><li id="li5212254514952"><a name="li5212254514952"></a><a name="li5212254514952"></a>Number of resources returned on each page</li><li id="li3804710814952"><a name="li3804710814952"></a><a name="li3804710814952"></a>Value range: 0–500<p id="p11803393165013"><a name="p11803393165013"></a><a name="p11803393165013"></a>Commonly used values are <strong id="b29013199165033"><a name="b29013199165033"></a><a name="b29013199165033"></a>10</strong>,&nbsp;<strong id="b18730602165036"><a name="b18730602165036"></a><a name="b18730602165036"></a>20</strong>, and&nbsp;<strong id="b46176072165040"><a name="b46176072165040"></a><a name="b46176072165040"></a>50</strong>.</p>
    </li></ul>
    </td>
    </tr>
    <tr id="row2721615319547"><td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.2.5.1.1 "><p id="p626980719549"><a name="p626980719549"></a><a name="p626980719549"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.869999999999997%" headers="mcps1.2.5.1.2 "><p id="p3809236019549"><a name="p3809236019549"></a><a name="p3809236019549"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.780000000000001%" headers="mcps1.2.5.1.3 "><p id="p6558235419549"><a name="p6558235419549"></a><a name="p6558235419549"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.74%" headers="mcps1.2.5.1.4 "><a name="ul1057048519549"></a><a name="ul1057048519549"></a><ul id="ul1057048519549"><li id="li2802550319549"><a name="li2802550319549"></a><a name="li2802550319549"></a>Start page of the list, which ranges from 0 to 2147483647.</li><li id="li5090293619549"><a name="li5090293619549"></a><a name="li5090293619549"></a>When the value of <strong id="b842352706193255"><a name="b842352706193255"></a><a name="b842352706193255"></a>marker</strong> is not blank, it determines the start of a page.</li></ul>
    </td>
    </tr>
    <tr id="row58681680125046"><td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.2.5.1.1 "><p id="p47666033125046"><a name="p47666033125046"></a><a name="p47666033125046"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.869999999999997%" headers="mcps1.2.5.1.2 "><p id="p35743447125046"><a name="p35743447125046"></a><a name="p35743447125046"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.780000000000001%" headers="mcps1.2.5.1.3 "><p id="p9538131125046"><a name="p9538131125046"></a><a name="p9538131125046"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.74%" headers="mcps1.2.5.1.4 "><p id="p34391114125046"><a name="p34391114125046"></a><a name="p34391114125046"></a>Resource tag</p>
    <p id="p41084576125046"><a name="p41084576125046"></a><a name="p41084576125046"></a>The format is as follows: <strong id="b8423527069140"><a name="b8423527069140"></a><a name="b8423527069140"></a>key1,value1|key2,value2</strong>.</p>
    <p id="p34216870125046"><a name="p34216870125046"></a><a name="p34216870125046"></a>Multiple tags are separated by vertical bar (|). The key and value of each tag are separated by comma (,).</p>
    <p id="p1526014454308"><a name="p1526014454308"></a><a name="p1526014454308"></a>All tags listed will be queried.</p>
    <p id="p16628284115121"><a name="p16628284115121"></a><a name="p16628284115121"></a>For details, see section <a href="tag-management.html">Tag Management</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section44958995161021"></a>

None

## Response<a name="section40090803161031"></a>

-   Parameter description

    **Table  2**  Parameters in the response

    <a name="table6655637171923"></a><table><thead align="left"><tr id="row12436182171923"><th class="cellrowborder" valign="top" width="20.41%" id="mcps1.2.4.1.1"><p id="p18040723171923"><a name="p18040723171923"></a><a name="p18040723171923"></a><strong id="b162774213314533_1"><a name="b162774213314533_1"></a><a name="b162774213314533_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.57%" id="mcps1.2.4.1.2"><p id="p12288867171923"><a name="p12288867171923"></a><a name="p12288867171923"></a><strong id="b84235270619112_1"><a name="b84235270619112_1"></a><a name="b84235270619112_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="51.019999999999996%" id="mcps1.2.4.1.3"><p id="p16021685171923"><a name="p16021685171923"></a><a name="p16021685171923"></a><strong id="b842352706112423_1"><a name="b842352706112423_1"></a><a name="b842352706112423_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row33084878171923"><td class="cellrowborder" valign="top" width="20.41%" headers="mcps1.2.4.1.1 "><p id="p10518479171923"><a name="p10518479171923"></a><a name="p10518479171923"></a>zones</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.2.4.1.2 "><p id="p17816324171923"><a name="p17816324171923"></a><a name="p17816324171923"></a>List data structure</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.019999999999996%" headers="mcps1.2.4.1.3 "><p id="p64387025171923"><a name="p64387025171923"></a><a name="p64387025171923"></a>Zone list object</p>
    </td>
    </tr>
    <tr id="row45921614175143"><td class="cellrowborder" valign="top" width="20.41%" headers="mcps1.2.4.1.1 "><p id="p10641344175143"><a name="p10641344175143"></a><a name="p10641344175143"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.2.4.1.2 "><p id="p24643947175143"><a name="p24643947175143"></a><a name="p24643947175143"></a>object</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.019999999999996%" headers="mcps1.2.4.1.3 "><p id="p50002691175143"><a name="p50002691175143"></a><a name="p50002691175143"></a>Number of resources that meet the filter condition</p>
    </td>
    </tr>
    </tbody>
    </table>

    [Table 3](#table10871190151410) describes parameters under the **zones** field, and [Table 4](#table141615131414) describes the parameter under the **metadata**  field.

    **Table  3**  Description of the  **zones**  field

    <a name="table10871190151410"></a><table><thead align="left"><tr id="row1187914015145"><th class="cellrowborder" valign="top" width="18.38%" id="mcps1.2.4.1.1"><p id="p488213014145"><a name="p488213014145"></a><a name="p488213014145"></a><strong id="b162774213314533_2"><a name="b162774213314533_2"></a><a name="b162774213314533_2"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.33%" id="mcps1.2.4.1.2"><p id="p1388515051418"><a name="p1388515051418"></a><a name="p1388515051418"></a><strong id="b84235270619112_2"><a name="b84235270619112_2"></a><a name="b84235270619112_2"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="62.29%" id="mcps1.2.4.1.3"><p id="p8887707143"><a name="p8887707143"></a><a name="p8887707143"></a><strong id="b842352706112423_2"><a name="b842352706112423_2"></a><a name="b842352706112423_2"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row14889200191410"><td class="cellrowborder" valign="top" width="18.38%" headers="mcps1.2.4.1.1 "><p id="p11890180121420"><a name="p11890180121420"></a><a name="p11890180121420"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.33%" headers="mcps1.2.4.1.2 "><p id="p178921305144"><a name="p178921305144"></a><a name="p178921305144"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.29%" headers="mcps1.2.4.1.3 "><p id="p1589419081418"><a name="p1589419081418"></a><a name="p1589419081418"></a>Zone ID, which is a UUID used to identify the zone</p>
    </td>
    </tr>
    <tr id="row208952016144"><td class="cellrowborder" valign="top" width="18.38%" headers="mcps1.2.4.1.1 "><p id="p198981207149"><a name="p198981207149"></a><a name="p198981207149"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.33%" headers="mcps1.2.4.1.2 "><p id="p0901205148"><a name="p0901205148"></a><a name="p0901205148"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.29%" headers="mcps1.2.4.1.3 "><p id="p5904140161420"><a name="p5904140161420"></a><a name="p5904140161420"></a>Zone name</p>
    </td>
    </tr>
    <tr id="row1905180111413"><td class="cellrowborder" valign="top" width="18.38%" headers="mcps1.2.4.1.1 "><p id="p129067010142"><a name="p129067010142"></a><a name="p129067010142"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.33%" headers="mcps1.2.4.1.2 "><p id="p1890800161415"><a name="p1890800161415"></a><a name="p1890800161415"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.29%" headers="mcps1.2.4.1.3 "><p id="p790916010141"><a name="p790916010141"></a><a name="p790916010141"></a>Zone description</p>
    </td>
    </tr>
    <tr id="row89101018143"><td class="cellrowborder" valign="top" width="18.38%" headers="mcps1.2.4.1.1 "><p id="p791270191413"><a name="p791270191413"></a><a name="p791270191413"></a>email</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.33%" headers="mcps1.2.4.1.2 "><p id="p09136021413"><a name="p09136021413"></a><a name="p09136021413"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.29%" headers="mcps1.2.4.1.3 "><p id="p791613013147"><a name="p791613013147"></a><a name="p791613013147"></a>Email address of the administrator managing the zone</p>
    </td>
    </tr>
    <tr id="row69166031414"><td class="cellrowborder" valign="top" width="18.38%" headers="mcps1.2.4.1.1 "><p id="p179190018143"><a name="p179190018143"></a><a name="p179190018143"></a>zone_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.33%" headers="mcps1.2.4.1.2 "><p id="p292119018147"><a name="p292119018147"></a><a name="p292119018147"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.29%" headers="mcps1.2.4.1.3 "><p id="p492370131414"><a name="p492370131414"></a><a name="p492370131414"></a>Zone type, which can be <strong id="b842352706115152"><a name="b842352706115152"></a><a name="b842352706115152"></a>public</strong> or <strong id="b842352706115156"><a name="b842352706115156"></a><a name="b842352706115156"></a>private</strong></p>
    </td>
    </tr>
    <tr id="row1792616091413"><td class="cellrowborder" valign="top" width="18.38%" headers="mcps1.2.4.1.1 "><p id="p109283011142"><a name="p109283011142"></a><a name="p109283011142"></a>ttl</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.33%" headers="mcps1.2.4.1.2 "><p id="p189301209147"><a name="p189301209147"></a><a name="p189301209147"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.29%" headers="mcps1.2.4.1.3 "><p id="p1893460141411"><a name="p1893460141411"></a><a name="p1893460141411"></a>TTL value of the SOA record set in the zone</p>
    </td>
    </tr>
    <tr id="row49346041419"><td class="cellrowborder" valign="top" width="18.38%" headers="mcps1.2.4.1.1 "><p id="p193630171412"><a name="p193630171412"></a><a name="p193630171412"></a>serial</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.33%" headers="mcps1.2.4.1.2 "><p id="p19940160111416"><a name="p19940160111416"></a><a name="p19940160111416"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.29%" headers="mcps1.2.4.1.3 "><p id="p1894211012145"><a name="p1894211012145"></a><a name="p1894211012145"></a>Serial number in the SOA record set in the zone, which identifies the change on the primary DNS server</p>
    </td>
    </tr>
    <tr id="row1494311013144"><td class="cellrowborder" valign="top" width="18.38%" headers="mcps1.2.4.1.1 "><p id="p1394519012141"><a name="p1394519012141"></a><a name="p1394519012141"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.33%" headers="mcps1.2.4.1.2 "><p id="p199461401144"><a name="p199461401144"></a><a name="p199461401144"></a>enum</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.29%" headers="mcps1.2.4.1.3 "><p id="p494720017143"><a name="p494720017143"></a><a name="p494720017143"></a>Resource status</p>
    <p id="p29501003143"><a name="p29501003143"></a><a name="p29501003143"></a>The value can be <strong id="b84235270695628"><a name="b84235270695628"></a><a name="b84235270695628"></a>PENDING_CREATE</strong>,&nbsp;<strong id="b84235270695635"><a name="b84235270695635"></a><a name="b84235270695635"></a>ACTIVE</strong>,&nbsp;<strong id="b84235270695643"><a name="b84235270695643"></a><a name="b84235270695643"></a>PENDING_DELETE</strong>, or&nbsp;<strong id="b84235270695650"><a name="b84235270695650"></a><a name="b84235270695650"></a>ERROR</strong>.</p>
    </td>
    </tr>
    <tr id="row1595113017149"><td class="cellrowborder" valign="top" width="18.38%" headers="mcps1.2.4.1.1 "><p id="p1395410081413"><a name="p1395410081413"></a><a name="p1395410081413"></a>record_num</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.33%" headers="mcps1.2.4.1.2 "><p id="p179551801147"><a name="p179551801147"></a><a name="p179551801147"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.29%" headers="mcps1.2.4.1.3 "><p id="p595712021413"><a name="p595712021413"></a><a name="p595712021413"></a>Number of record sets in the zone</p>
    </td>
    </tr>
    <tr id="row69595020143"><td class="cellrowborder" valign="top" width="18.38%" headers="mcps1.2.4.1.1 "><p id="p15962150151419"><a name="p15962150151419"></a><a name="p15962150151419"></a>pool_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.33%" headers="mcps1.2.4.1.2 "><p id="p6965803142"><a name="p6965803142"></a><a name="p6965803142"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.29%" headers="mcps1.2.4.1.3 "><p id="p1596710031411"><a name="p1596710031411"></a><a name="p1596710031411"></a>Pool ID of the zone, which is assigned by the system</p>
    </td>
    </tr>
    <tr id="row49683010141"><td class="cellrowborder" valign="top" width="18.38%" headers="mcps1.2.4.1.1 "><p id="p2097010181418"><a name="p2097010181418"></a><a name="p2097010181418"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.33%" headers="mcps1.2.4.1.2 "><p id="p1397430121412"><a name="p1397430121412"></a><a name="p1397430121412"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.29%" headers="mcps1.2.4.1.3 "><p id="p149761809149"><a name="p149761809149"></a><a name="p149761809149"></a>Project ID of the zone</p>
    </td>
    </tr>
    <tr id="row129774031419"><td class="cellrowborder" valign="top" width="18.38%" headers="mcps1.2.4.1.1 "><p id="p15980200171419"><a name="p15980200171419"></a><a name="p15980200171419"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.33%" headers="mcps1.2.4.1.2 "><p id="p69816019146"><a name="p69816019146"></a><a name="p69816019146"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.29%" headers="mcps1.2.4.1.3 "><p id="p159835018143"><a name="p159835018143"></a><a name="p159835018143"></a>Time when the zone was created</p>
    </td>
    </tr>
    <tr id="row1498413011412"><td class="cellrowborder" valign="top" width="18.38%" headers="mcps1.2.4.1.1 "><p id="p398715081417"><a name="p398715081417"></a><a name="p398715081417"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.33%" headers="mcps1.2.4.1.2 "><p id="p1988190121420"><a name="p1988190121420"></a><a name="p1988190121420"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.29%" headers="mcps1.2.4.1.3 "><p id="p169905051413"><a name="p169905051413"></a><a name="p169905051413"></a>Time when the zone was updated</p>
    </td>
    </tr>
    <tr id="row999050111419"><td class="cellrowborder" valign="top" width="18.38%" headers="mcps1.2.4.1.1 "><p id="p8993407142"><a name="p8993407142"></a><a name="p8993407142"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.33%" headers="mcps1.2.4.1.2 "><p id="p899518011417"><a name="p899518011417"></a><a name="p899518011417"></a>object</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.29%" headers="mcps1.2.4.1.3 "><p id="p1799719041413"><a name="p1799719041413"></a><a name="p1799719041413"></a>Link of the current resource or other related resources</p>
    <p id="p109986017142"><a name="p109986017142"></a><a name="p109986017142"></a>When a response is broken into pages, a <strong id="b84235270695245"><a name="b84235270695245"></a><a name="b84235270695245"></a>next</strong> link is provided to retrieve all results.</p>
    </td>
    </tr>
    <tr id="row29991001416"><td class="cellrowborder" valign="top" width="18.38%" headers="mcps1.2.4.1.1 "><p id="p1311419142"><a name="p1311419142"></a><a name="p1311419142"></a>masters</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.33%" headers="mcps1.2.4.1.2 "><p id="p185151151417"><a name="p185151151417"></a><a name="p185151151417"></a>enum</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.29%" headers="mcps1.2.4.1.3 "><p id="p1876191410"><a name="p1876191410"></a><a name="p1876191410"></a>Master DNS servers, from which the slave servers get DNS information</p>
    </td>
    </tr>
    <tr id="row18881161418"><td class="cellrowborder" valign="top" width="18.38%" headers="mcps1.2.4.1.1 "><p id="p6114111411"><a name="p6114111411"></a><a name="p6114111411"></a>routers</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.33%" headers="mcps1.2.4.1.2 "><p id="p10131212146"><a name="p10131212146"></a><a name="p10131212146"></a>List&lt;Router&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.29%" headers="mcps1.2.4.1.3 "><p id="p161561141410"><a name="p161561141410"></a><a name="p161561141410"></a>Routers (VPCs associated with the zone)</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  Description of the  **metadata**  field

    <a name="table141615131414"></a><table><thead align="left"><tr id="row223813147"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p1266151412"><a name="p1266151412"></a><a name="p1266151412"></a><strong id="b162774213314533_3"><a name="b162774213314533_3"></a><a name="b162774213314533_3"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p12286121410"><a name="p12286121410"></a><a name="p12286121410"></a><strong id="b84235270619112_3"><a name="b84235270619112_3"></a><a name="b84235270619112_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p02911119140"><a name="p02911119140"></a><a name="p02911119140"></a><strong id="b842352706112423_3"><a name="b842352706112423_3"></a><a name="b842352706112423_3"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row33219131412"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p8341314143"><a name="p8341314143"></a><a name="p8341314143"></a>total_count</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p123671111420"><a name="p123671111420"></a><a name="p123671111420"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1339111149"><a name="p1339111149"></a><a name="p1339111149"></a>Total number of resources</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "links": {
            "self": "https://Endpoint/v2/zones?type=private&limit=11&marker=&name=&status="
        },
        "zones": [
            {
                "id": "ff8080825b8fc86c015b94bc6f8712c3",
                "name": "example.com.",
                "description": "This is an example zone.",
                "email": "xx@example.com",
                "ttl": 300,
                "serial": 0,
                "masters": [],
                "status": "ACTIVE",
                "links": {
                    "self": "https://Endpoint/v2/zones/ff8080825b8fc86c015b94bc6f8712c3"
                },
                "pool_id": "ff8080825ab738f4015ab7513298010e",
                "project_id": "e55c6f3dc4e34c9f86353b664ae0e70c",
                "zone_type": "private",
                "created_at": "2017-04-22T08:17:08.997",
                "updated_at": "2017-04-22T08:17:09.997",
                "record_num": 2,
                "routers": [
                    {
                        "status": "ACTIVE",
                        "router_id": "19664294-0bf6-4271-ad3a-94b8c79c6558",
                        "router_region": "xx"
                    },
                    {
                        "status": "ACTIVE",
                        "router_id": "f0791650-db8c-4a20-8a44-a06c6e24b15b",
                        "router_region": "xx"
                    }
                ]
            },
            {
                "id": "ff8080825b95142f015b951f87280029",
                "name": "example.org.",
                "description": "This is an example zone.",
                "email": "xx@example.org",
                "ttl": 300,
                "serial": 0,
                "masters": [],
                "status": "ACTIVE",
                "links": {
                    "self": "https://Endpoint/v2/zones/ff8080825b95142f015b951f87280029"
                },
                "pool_id": "ff8080825ab738f4015ab7513298010e",
                "project_id": "e55c6f3dc4e34c9f86353b664ae0e70c",
                "zone_type": "private",
                "created_at": "2017-04-22T08:17:08.997",
                "updated_at": "2017-04-22T08:17:09.997",
                "record_num": 2,
                "routers": [
                    {
                        "status": "ACTIVE",
                        "router_id": "19664294-0bf6-4271-ad3a-94b8c79c6558",
                        "router_region": "xx"
                    },
                    {
                        "status": "ACTIVE",
                        "router_id": "f0791650-db8c-4a20-8a44-a06c6e24b15b",
                        "router_region": "xx"
                    }
                ]
    
            }
        ],
        "metadata": {
            "total_count": 2
        }
    }
    ```


## **Returned Value**<a name="section42637797161043"></a>

See  [General Request Return Code](general-request-return-code.md).

