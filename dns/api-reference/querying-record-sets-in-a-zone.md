# Querying Record Sets in a Zone<a name="EN-US_TOPIC_0037129970"></a>

## Function<a name="section8391370"></a>

Query all record sets in a specified zone.

## URI<a name="section8413469"></a>

-   URI format

    GET /v2/zones/\{zone\_id\}/recordsets?limit=\{limit\}&marker=\{marker\}

-   Parameter description

    **Table  1**  Parameters in the URI

    <a name="table48883615"></a><table><thead align="left"><tr id="row57562809"><th class="cellrowborder" valign="top" width="17.95%" id="mcps1.2.5.1.1"><p id="p32075938"><a name="p32075938"></a><a name="p32075938"></a><strong id="b162774213314533"><a name="b162774213314533"></a><a name="b162774213314533"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.11%" id="mcps1.2.5.1.2"><p id="p48014184"><a name="p48014184"></a><a name="p48014184"></a><strong id="b593421527191713"><a name="b593421527191713"></a><a name="b593421527191713"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="13.58%" id="mcps1.2.5.1.3"><p id="p63943666"><a name="p63943666"></a><a name="p63943666"></a><strong id="b84235270619112"><a name="b84235270619112"></a><a name="b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.36000000000001%" id="mcps1.2.5.1.4"><p id="p12054440"><a name="p12054440"></a><a name="p12054440"></a><strong id="b842352706112423"><a name="b842352706112423"></a><a name="b842352706112423"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row36885620"><td class="cellrowborder" valign="top" width="17.95%" headers="mcps1.2.5.1.1 "><p id="p34945211"><a name="p34945211"></a><a name="p34945211"></a>zone_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.11%" headers="mcps1.2.5.1.2 "><p id="p11989863"><a name="p11989863"></a><a name="p11989863"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.58%" headers="mcps1.2.5.1.3 "><p id="p31654880"><a name="p31654880"></a><a name="p31654880"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.36000000000001%" headers="mcps1.2.5.1.4 "><p id="p13908493"><a name="p13908493"></a><a name="p13908493"></a>Zone ID</p>
    </td>
    </tr>
    <tr id="row58067579"><td class="cellrowborder" valign="top" width="17.95%" headers="mcps1.2.5.1.1 "><p id="p5853458"><a name="p5853458"></a><a name="p5853458"></a>marker</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.11%" headers="mcps1.2.5.1.2 "><p id="p4368081"><a name="p4368081"></a><a name="p4368081"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.58%" headers="mcps1.2.5.1.3 "><p id="p18270305"><a name="p18270305"></a><a name="p18270305"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.36000000000001%" headers="mcps1.2.5.1.4 "><p id="p3966512193622"><a name="p3966512193622"></a><a name="p3966512193622"></a>Start resource ID of pagination query</p>
    <p id="p3499754"><a name="p3499754"></a><a name="p3499754"></a>If the parameter is left blank, only resources on the first page are queried.</p>
    </td>
    </tr>
    <tr id="row31497787"><td class="cellrowborder" valign="top" width="17.95%" headers="mcps1.2.5.1.1 "><p id="p1183915"><a name="p1183915"></a><a name="p1183915"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.11%" headers="mcps1.2.5.1.2 "><p id="p28788263"><a name="p28788263"></a><a name="p28788263"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.58%" headers="mcps1.2.5.1.3 "><p id="p50147992"><a name="p50147992"></a><a name="p50147992"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.36000000000001%" headers="mcps1.2.5.1.4 "><a name="ul2143191219534"></a><a name="ul2143191219534"></a><ul id="ul2143191219534"><li id="li2908323993656"><a name="li2908323993656"></a><a name="li2908323993656"></a>Number of resources returned on each page</li><li id="li5312032319538"><a name="li5312032319538"></a><a name="li5312032319538"></a>Value range: 0–500<p id="p13936864195316"><a name="p13936864195316"></a><a name="p13936864195316"></a>Commonly used values are <strong id="b84235270611435"><a name="b84235270611435"></a><a name="b84235270611435"></a>10</strong>, <strong id="b84235270611439"><a name="b84235270611439"></a><a name="b84235270611439"></a>20</strong>, and <strong id="b84235270611443"><a name="b84235270611443"></a><a name="b84235270611443"></a>50</strong>.</p>
    </li></ul>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section8612359"></a>

None

## Response<a name="section10402369"></a>

-   Parameter description

    **Table  2**  Parameters in the response

    <a name="table53402119"></a><table><thead align="left"><tr id="en-us_topic_0037129969_row41580444"><th class="cellrowborder" valign="top" width="20.41%" id="mcps1.2.4.1.1"><p id="en-us_topic_0037129969_p12572829"><a name="en-us_topic_0037129969_p12572829"></a><a name="en-us_topic_0037129969_p12572829"></a><strong id="en-us_topic_0037129969_b162774213314533"><a name="en-us_topic_0037129969_b162774213314533"></a><a name="en-us_topic_0037129969_b162774213314533"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23.47%" id="mcps1.2.4.1.2"><p id="en-us_topic_0037129969_p13543581"><a name="en-us_topic_0037129969_p13543581"></a><a name="en-us_topic_0037129969_p13543581"></a><strong id="en-us_topic_0037129969_b84235270619112"><a name="en-us_topic_0037129969_b84235270619112"></a><a name="en-us_topic_0037129969_b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="56.120000000000005%" id="mcps1.2.4.1.3"><p id="en-us_topic_0037129969_p23288300"><a name="en-us_topic_0037129969_p23288300"></a><a name="en-us_topic_0037129969_p23288300"></a><strong id="en-us_topic_0037129969_b842352706112423"><a name="en-us_topic_0037129969_b842352706112423"></a><a name="en-us_topic_0037129969_b842352706112423"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0037129969_row7304143"><td class="cellrowborder" valign="top" width="20.41%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037129969_p54764719"><a name="en-us_topic_0037129969_p54764719"></a><a name="en-us_topic_0037129969_p54764719"></a>recordsets</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.47%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037129969_p10465156"><a name="en-us_topic_0037129969_p10465156"></a><a name="en-us_topic_0037129969_p10465156"></a>List data structure</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.120000000000005%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037129969_p45797138"><a name="en-us_topic_0037129969_p45797138"></a><a name="en-us_topic_0037129969_p45797138"></a>Record set list object</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037129969_row2133747418458"><td class="cellrowborder" valign="top" width="20.41%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037129969_p5781953918458"><a name="en-us_topic_0037129969_p5781953918458"></a><a name="en-us_topic_0037129969_p5781953918458"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.47%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037129969_p5469790918458"><a name="en-us_topic_0037129969_p5469790918458"></a><a name="en-us_topic_0037129969_p5469790918458"></a>object</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.120000000000005%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037129969_p5673028518536"><a name="en-us_topic_0037129969_p5673028518536"></a><a name="en-us_topic_0037129969_p5673028518536"></a>Number of resources that meet the filter condition</p>
    </td>
    </tr>
    </tbody>
    </table>

    [Table 3](#table7192645154740)  describes parameters under the  **recordsets**  field, and  [Table 4](#table2908319718932)  describes the parameter under the  **metadata**  field.

    **Table  3**  Description of the  **recordsets**  field

    <a name="table7192645154740"></a><table><thead align="left"><tr id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_row52466955175323"><th class="cellrowborder" valign="top" width="27.889999999999997%" id="mcps1.2.4.1.1"><p id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p2769858175323"><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p2769858175323"></a><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p2769858175323"></a><strong id="en-us_topic_0037129969_b162774213314533_1"><a name="en-us_topic_0037129969_b162774213314533_1"></a><a name="en-us_topic_0037129969_b162774213314533_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23.810000000000002%" id="mcps1.2.4.1.2"><p id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p46296309175323"><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p46296309175323"></a><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p46296309175323"></a><strong id="en-us_topic_0037129969_b84235270619112_1"><a name="en-us_topic_0037129969_b84235270619112_1"></a><a name="en-us_topic_0037129969_b84235270619112_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="48.3%" id="mcps1.2.4.1.3"><p id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p62697904175323"><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p62697904175323"></a><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p62697904175323"></a><strong id="en-us_topic_0037129969_b842352706112423_1"><a name="en-us_topic_0037129969_b842352706112423_1"></a><a name="en-us_topic_0037129969_b842352706112423_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_row47909891175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p64112397175323"><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p64112397175323"></a><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p64112397175323"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p1660870175323"><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p1660870175323"></a><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p1660870175323"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.3%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p1249204175323"><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p1249204175323"></a><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p1249204175323"></a>Record set ID</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_row6942422175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p64097412175323"><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p64097412175323"></a><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p64097412175323"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p44990515175323"><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p44990515175323"></a><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p44990515175323"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.3%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p32019574175323"><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p32019574175323"></a><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p32019574175323"></a>Record set name</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_row61442071175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p51194416175323"><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p51194416175323"></a><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p51194416175323"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p63301991175323"><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p63301991175323"></a><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p63301991175323"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.3%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p43966660175323"><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p43966660175323"></a><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p43966660175323"></a>Record set description</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_row2176746175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p11805366175323"><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p11805366175323"></a><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p11805366175323"></a>zone_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p1051908175323"><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p1051908175323"></a><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p1051908175323"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.3%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p10043845175323"><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p10043845175323"></a><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p10043845175323"></a>Zone ID of the record set</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_row61212722175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p8318586175323"><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p8318586175323"></a><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p8318586175323"></a>zone_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p31287919175323"><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p31287919175323"></a><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p31287919175323"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.3%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p16372315175323"><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p16372315175323"></a><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p16372315175323"></a>Zone name of the record set</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_row38132372175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p37461920175323"><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p37461920175323"></a><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p37461920175323"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p27536075175323"><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p27536075175323"></a><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p27536075175323"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.3%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p24813356175323"><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p24813356175323"></a><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p24813356175323"></a>Record set type</p>
    <p id="en-us_topic_0037129969_p1484155154215"><a name="en-us_topic_0037129969_p1484155154215"></a><a name="en-us_topic_0037129969_p1484155154215"></a>The value can be <strong id="en-us_topic_0037129969_b84235270693731"><a name="en-us_topic_0037129969_b84235270693731"></a><a name="en-us_topic_0037129969_b84235270693731"></a>A</strong>,&nbsp;<strong id="en-us_topic_0037129969_b84235270693735"><a name="en-us_topic_0037129969_b84235270693735"></a><a name="en-us_topic_0037129969_b84235270693735"></a>AAAA</strong>,&nbsp;<strong id="en-us_topic_0037129969_b84235270693738"><a name="en-us_topic_0037129969_b84235270693738"></a><a name="en-us_topic_0037129969_b84235270693738"></a>MX</strong>,&nbsp;<strong id="en-us_topic_0037129969_b84235270693741"><a name="en-us_topic_0037129969_b84235270693741"></a><a name="en-us_topic_0037129969_b84235270693741"></a>CNAME</strong>,&nbsp;<strong id="en-us_topic_0037129969_b84235270693746"><a name="en-us_topic_0037129969_b84235270693746"></a><a name="en-us_topic_0037129969_b84235270693746"></a>TXT</strong>,&nbsp;<strong id="en-us_topic_0037129969_b84235270693755"><a name="en-us_topic_0037129969_b84235270693755"></a><a name="en-us_topic_0037129969_b84235270693755"></a>NS</strong>&nbsp;(only in public zones),&nbsp;<strong id="en-us_topic_0037129969_b8423527069382"><a name="en-us_topic_0037129969_b8423527069382"></a><a name="en-us_topic_0037129969_b8423527069382"></a>SRV</strong>,&nbsp;<strong id="en-us_topic_0037129969_b8423527069385"><a name="en-us_topic_0037129969_b8423527069385"></a><a name="en-us_topic_0037129969_b8423527069385"></a>PTR</strong>&nbsp;(only in private zones), and&nbsp;<strong id="en-us_topic_0037129969_b84235270693810"><a name="en-us_topic_0037129969_b84235270693810"></a><a name="en-us_topic_0037129969_b84235270693810"></a>CAA</strong> (only in public zones).</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_row20796819175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p4811553175323"><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p4811553175323"></a><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p4811553175323"></a>ttl</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p47559731175323"><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p47559731175323"></a><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p47559731175323"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.3%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037129969_p40578139142936"><a name="en-us_topic_0037129969_p40578139142936"></a><a name="en-us_topic_0037129969_p40578139142936"></a>Caching period of a domain name (in seconds)</p>
    <p id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p22097398175323"><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p22097398175323"></a><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p22097398175323"></a>A longer caching period makes a change on the authoritative DNS server take longer time to be synchronized to other DNS servers.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_row13978060175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p43388342175323"><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p43388342175323"></a><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p43388342175323"></a>records</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p29596719175323"><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p29596719175323"></a><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p29596719175323"></a>List&lt;string&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.3%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p30492925175323"><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p30492925175323"></a><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p30492925175323"></a>Domain name resolution result</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_row23148559175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p36524189175323"><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p36524189175323"></a><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p36524189175323"></a>create_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p47080972175323"><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p47080972175323"></a><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p47080972175323"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.3%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p15737135175323"><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p15737135175323"></a><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p15737135175323"></a>Time when the record set was created</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_row33465792175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p42570937175323"><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p42570937175323"></a><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p42570937175323"></a>update_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p27449776175323"><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p27449776175323"></a><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p27449776175323"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.3%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p63703533175323"><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p63703533175323"></a><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p63703533175323"></a>Time when the record set was updated</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_row17850883175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p36228271175323"><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p36228271175323"></a><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p36228271175323"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p6480061175323"><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p6480061175323"></a><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p6480061175323"></a>enum</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.3%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p65781854175323"><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p65781854175323"></a><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p65781854175323"></a>Resource status</p>
    <p id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p51374523175323"><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p51374523175323"></a><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p51374523175323"></a>The value can be <strong id="en-us_topic_0037129969_b84235270695628"><a name="en-us_topic_0037129969_b84235270695628"></a><a name="en-us_topic_0037129969_b84235270695628"></a>PENDING_CREATE</strong>,&nbsp;<strong id="en-us_topic_0037129969_b84235270695635"><a name="en-us_topic_0037129969_b84235270695635"></a><a name="en-us_topic_0037129969_b84235270695635"></a>ACTIVE</strong>,&nbsp;<strong id="en-us_topic_0037129969_b84235270683910"><a name="en-us_topic_0037129969_b84235270683910"></a><a name="en-us_topic_0037129969_b84235270683910"></a>PENDING_UPDATE</strong>,&nbsp;<strong id="en-us_topic_0037129969_b84235270695643"><a name="en-us_topic_0037129969_b84235270695643"></a><a name="en-us_topic_0037129969_b84235270695643"></a>PENDING_DELETE</strong>, or&nbsp;<strong id="en-us_topic_0037129969_b84235270695650"><a name="en-us_topic_0037129969_b84235270695650"></a><a name="en-us_topic_0037129969_b84235270695650"></a>ERROR</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_row61184424175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p49633411175323"><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p49633411175323"></a><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p49633411175323"></a>default</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p56048766175323"><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p56048766175323"></a><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p56048766175323"></a>boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.3%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037129969_p1942025514322"><a name="en-us_topic_0037129969_p1942025514322"></a><a name="en-us_topic_0037129969_p1942025514322"></a>Whether the record set is created by default</p>
    <p id="en-us_topic_0037129969_p4056457114322"><a name="en-us_topic_0037129969_p4056457114322"></a><a name="en-us_topic_0037129969_p4056457114322"></a>A default record set cannot be deleted.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_row15199048201026"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p23163408201026"><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p23163408201026"></a><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p23163408201026"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p40653752201026"><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p40653752201026"></a><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p40653752201026"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.3%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p4619625201026"><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p4619625201026"></a><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p4619625201026"></a>Project ID of the record set</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_row3965248419366"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p2132803819366"><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p2132803819366"></a><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p2132803819366"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p1127763319366"><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p1127763319366"></a><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p1127763319366"></a>object</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.3%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037129969_p34781370143021"><a name="en-us_topic_0037129969_p34781370143021"></a><a name="en-us_topic_0037129969_p34781370143021"></a>Link of the current resource or other related resources</p>
    <p id="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p4107308719366"><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p4107308719366"></a><a name="en-us_topic_0037129969_en-us_topic_0037129968_en-us_topic_0037134404_p4107308719366"></a>When a response is broken into pages, a <strong id="en-us_topic_0037129969_b22743378143011"><a name="en-us_topic_0037129969_b22743378143011"></a><a name="en-us_topic_0037129969_b22743378143011"></a>next</strong> link is provided to retrieve all results.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  Description of the  **metadata**  field

    <a name="table2908319718932"></a><table><thead align="left"><tr id="en-us_topic_0037134402_row58979189175457"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="en-us_topic_0037134402_p46156243175457"><a name="en-us_topic_0037134402_p46156243175457"></a><a name="en-us_topic_0037134402_p46156243175457"></a><strong id="en-us_topic_0037134402_b162774213314533"><a name="en-us_topic_0037134402_b162774213314533"></a><a name="en-us_topic_0037134402_b162774213314533"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="en-us_topic_0037134402_p47668234175457"><a name="en-us_topic_0037134402_p47668234175457"></a><a name="en-us_topic_0037134402_p47668234175457"></a><strong id="en-us_topic_0037134402_b84235270619112"><a name="en-us_topic_0037134402_b84235270619112"></a><a name="en-us_topic_0037134402_b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="en-us_topic_0037134402_p35921708175457"><a name="en-us_topic_0037134402_p35921708175457"></a><a name="en-us_topic_0037134402_p35921708175457"></a><strong id="en-us_topic_0037134402_b842352706112423"><a name="en-us_topic_0037134402_b842352706112423"></a><a name="en-us_topic_0037134402_b842352706112423"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0037134402_row54859922175457"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037134402_p14468674175457"><a name="en-us_topic_0037134402_p14468674175457"></a><a name="en-us_topic_0037134402_p14468674175457"></a>total_count</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037134402_p31111955175457"><a name="en-us_topic_0037134402_p31111955175457"></a><a name="en-us_topic_0037134402_p31111955175457"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037134402_p37040428175457"><a name="en-us_topic_0037134402_p37040428175457"></a><a name="en-us_topic_0037134402_p37040428175457"></a>Total number of resources</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "links": {
            "self": "https://Endpoint/v2/recordsets?limit=11&marker=&name=&status=&zone_id=2c9eb155587194ec01587224c9f90149"
        },
        "recordsets": [
            {
                "id": "2c9eb155587194ec01587224c9f9014a",
                "name": "example.com.",
                "type": "SOA",
                "ttl": 300,
                "records": [
                    "ns1.hotrot.de. xx.example.com. (1 7200 900 1209600 300)"
                ],
                "status": "ACTIVE",
                "links": {
                    "self": "https://Endpoint/v2/zones/2c9eb155587194ec01587224c9f90149/recordsets/2c9eb155587194ec01587224c9f9014a"
                },
                "zone_id": "2c9eb155587194ec01587224c9f90149",
                "zone_name": "example.com.",
                "create_at": "2016-11-17T11:56:03.439",
                "update_at": "2016-11-17T12:56:03.827",
                "default": true,
                "project_id": "e55c6f3dc4e34c9f86353b664ae0e70c"
            },
            {
                "id": "2c9eb155587194ec01587224c9f9014c",
                "name": "example.com.",
                "type": "NS",
                "ttl": 172800,
                "records": [
                    "ns2.hotrot.de.",
                    "ns1.hotrot.de."
                ],
                "status": "ACTIVE",
                "links": {
                    "self": "https://Endpoint/v2/zones/2c9eb155587194ec01587224c9f90149/recordsets/2c9eb155587194ec01587224c9f9014c"
                },
                "zone_id": "2c9eb155587194ec01587224c9f90149",
                "zone_name": "example.com.",
                "create_at": "2016-11-17T11:56:03.439",
                "update_at": "2016-11-17T12:56:03.827",
                "default": true,
                "project_id": "e55c6f3dc4e34c9f86353b664ae0e70c"
            },
            {
                "id": "2c9eb155587228570158722b6ac30007",
                "name": "www.example.com.",
                "description": "This is an example record set.",
                "type": "A",
                "ttl": 300,
                "records": [
                    "192.168.10.2",
                    "192.168.10.1"
                ],
                "status": "PENDING_CREATE",
                "links": {
                    "self": "https://Endpoint/v2/zones/2c9eb155587194ec01587224c9f90149/recordsets/2c9eb155587228570158722b6ac30007"
                },
                "zone_id": "2c9eb155587194ec01587224c9f90149",
                "zone_name": "example.com.",
                "create_at": "2016-11-17T12:03:17.827",
                "update_at": "2016-11-17T12:56:03.827",
                "default": false,
                "project_id": "e55c6f3dc4e34c9f86353b664ae0e70c"
            }
        ],
        "metadata": {
            "total_count": 3
        }
    }
    ```


## Returned Value<a name="section26512460"></a>

See  [General Request Return Code](general-request-return-code.md).

