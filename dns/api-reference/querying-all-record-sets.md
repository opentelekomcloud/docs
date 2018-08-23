# Querying All Record Sets<a name="EN-US_TOPIC_0037129969"></a>

## Function<a name="section29105235"></a>

Query record sets in list.

## URI<a name="section60620523"></a>

-   URI format

    GET /v2/recordsets?zone\_type=\{zone\_type\}&limit=\{limit\}&marker=\{marker\}&offset=\{offset\}&tags=\{tags\}

-   Parameter description

    **Table  1**  Parameters in the URI

    <a name="table40248354"></a><table><thead align="left"><tr id="row24110047"><th class="cellrowborder" valign="top" width="17.57%" id="mcps1.2.5.1.1"><p id="p6756797"><a name="p6756797"></a><a name="p6756797"></a><strong id="b162774213314533"><a name="b162774213314533"></a><a name="b162774213314533"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.81%" id="mcps1.2.5.1.2"><p id="p10429724"><a name="p10429724"></a><a name="p10429724"></a><strong id="b593421527191713"><a name="b593421527191713"></a><a name="b593421527191713"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="13.200000000000001%" id="mcps1.2.5.1.3"><p id="p39501348"><a name="p39501348"></a><a name="p39501348"></a><strong id="b84235270619112"><a name="b84235270619112"></a><a name="b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="49.419999999999995%" id="mcps1.2.5.1.4"><p id="p45492604"><a name="p45492604"></a><a name="p45492604"></a><strong id="b842352706112423"><a name="b842352706112423"></a><a name="b842352706112423"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row67046586114158"><td class="cellrowborder" valign="top" width="17.57%" headers="mcps1.2.5.1.1 "><p id="p10129219114159"><a name="p10129219114159"></a><a name="p10129219114159"></a>zone_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.2.5.1.2 "><p id="p15160399114159"><a name="p15160399114159"></a><a name="p15160399114159"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.200000000000001%" headers="mcps1.2.5.1.3 "><p id="p20032767114159"><a name="p20032767114159"></a><a name="p20032767114159"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.419999999999995%" headers="mcps1.2.5.1.4 "><p id="p12041403114159"><a name="p12041403114159"></a><a name="p12041403114159"></a>Zone type of the record set to be queried, which can be <strong id="b842352706203526"><a name="b842352706203526"></a><a name="b842352706203526"></a>public</strong> or <strong id="b842352706203523"><a name="b842352706203523"></a><a name="b842352706203523"></a>private</strong></p>
    <a name="ul35829612114159"></a><a name="ul35829612114159"></a><ul id="ul35829612114159"><li id="li16517498114159"><a name="li16517498114159"></a><a name="li16517498114159"></a><strong id="b842352706203559"><a name="b842352706203559"></a><a name="b842352706203559"></a>public</strong>: Record sets in public zones are queried.</li><li id="li14439759114159"><a name="li14439759114159"></a><a name="li14439759114159"></a><strong id="b842352706203618"><a name="b842352706203618"></a><a name="b842352706203618"></a>private</strong>: Record sets in private zones are queried.<p id="p5693402220383"><a name="p5693402220383"></a><a name="p5693402220383"></a>If the value is left blank, record sets in public zones are queried by default.</p>
    </li></ul>
    </td>
    </tr>
    <tr id="row61022284"><td class="cellrowborder" valign="top" width="17.57%" headers="mcps1.2.5.1.1 "><p id="p43857981"><a name="p43857981"></a><a name="p43857981"></a>marker</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.2.5.1.2 "><p id="p62835574"><a name="p62835574"></a><a name="p62835574"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.200000000000001%" headers="mcps1.2.5.1.3 "><p id="p56516768"><a name="p56516768"></a><a name="p56516768"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.419999999999995%" headers="mcps1.2.5.1.4 "><p id="p3582346592940"><a name="p3582346592940"></a><a name="p3582346592940"></a>Start resource ID of pagination query</p>
    <p id="p14455523"><a name="p14455523"></a><a name="p14455523"></a>If the parameter is left blank, only resources on the first page are queried.</p>
    </td>
    </tr>
    <tr id="row62990845"><td class="cellrowborder" valign="top" width="17.57%" headers="mcps1.2.5.1.1 "><p id="p1984791"><a name="p1984791"></a><a name="p1984791"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.2.5.1.2 "><p id="p26550365"><a name="p26550365"></a><a name="p26550365"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.200000000000001%" headers="mcps1.2.5.1.3 "><p id="p3095993"><a name="p3095993"></a><a name="p3095993"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.419999999999995%" headers="mcps1.2.5.1.4 "><a name="ul18169499193915"></a><a name="ul18169499193915"></a><ul id="ul18169499193915"><li id="li1013041292959"><a name="li1013041292959"></a><a name="li1013041292959"></a>Number of resources returned on each page</li><li id="li2912773893122"><a name="li2912773893122"></a><a name="li2912773893122"></a>Value range: 0–500<p id="p61821521193933"><a name="p61821521193933"></a><a name="p61821521193933"></a>Commonly used values are <strong id="b842352706165149"><a name="b842352706165149"></a><a name="b842352706165149"></a>10</strong>,&nbsp;<strong id="b842352706165151"><a name="b842352706165151"></a><a name="b842352706165151"></a>20</strong>, and&nbsp;<strong id="b842352706165154"><a name="b842352706165154"></a><a name="b842352706165154"></a>50</strong>.</p>
    </li></ul>
    </td>
    </tr>
    <tr id="row78856519552"><td class="cellrowborder" valign="top" width="17.57%" headers="mcps1.2.5.1.1 "><p id="p5702070419554"><a name="p5702070419554"></a><a name="p5702070419554"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.2.5.1.2 "><p id="p5527430219554"><a name="p5527430219554"></a><a name="p5527430219554"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.200000000000001%" headers="mcps1.2.5.1.3 "><p id="p4803348119554"><a name="p4803348119554"></a><a name="p4803348119554"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.419999999999995%" headers="mcps1.2.5.1.4 "><a name="ul6550672819554"></a><a name="ul6550672819554"></a><ul id="ul6550672819554"><li id="li5268964319554"><a name="li5268964319554"></a><a name="li5268964319554"></a>Start page of the list, which ranges from 0 to 2147483647.</li><li id="li444474019554"><a name="li444474019554"></a><a name="li444474019554"></a>When the value of <strong id="b842352706193255"><a name="b842352706193255"></a><a name="b842352706193255"></a>marker</strong> is not blank, it determines the start of a page.</li></ul>
    </td>
    </tr>
    <tr id="row55044453115726"><td class="cellrowborder" valign="top" width="17.57%" headers="mcps1.2.5.1.1 "><p id="p216770371221"><a name="p216770371221"></a><a name="p216770371221"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.2.5.1.2 "><p id="p110096061221"><a name="p110096061221"></a><a name="p110096061221"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.200000000000001%" headers="mcps1.2.5.1.3 "><p id="p193628991221"><a name="p193628991221"></a><a name="p193628991221"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.419999999999995%" headers="mcps1.2.5.1.4 "><p id="p248910051221"><a name="p248910051221"></a><a name="p248910051221"></a>Resource tag</p>
    <p id="p226924561221"><a name="p226924561221"></a><a name="p226924561221"></a>The format is as follows: <strong id="b8423527069140"><a name="b8423527069140"></a><a name="b8423527069140"></a>key1,value1|key2,value2</strong>.</p>
    <p id="p40552875114139"><a name="p40552875114139"></a><a name="p40552875114139"></a>Multiple tags are separated by vertical bar (|). The key and value of each tag are separated by comma (,).</p>
    <p id="p29055151221"><a name="p29055151221"></a><a name="p29055151221"></a>All tags listed will be queried.</p>
    <p id="p59717447115129"><a name="p59717447115129"></a><a name="p59717447115129"></a>For details, see section <a href="tag-management.html">Tag Management</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section8713795"></a>

None

## Response<a name="section11315292"></a>

-   Parameter description

    **Table  2**  Parameters in the response

    <a name="table21574462"></a><table><thead align="left"><tr id="row41580444"><th class="cellrowborder" valign="top" width="20.41%" id="mcps1.2.4.1.1"><p id="p12572829"><a name="p12572829"></a><a name="p12572829"></a><strong id="b162774213314533_1"><a name="b162774213314533_1"></a><a name="b162774213314533_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23.47%" id="mcps1.2.4.1.2"><p id="p13543581"><a name="p13543581"></a><a name="p13543581"></a><strong id="b84235270619112_1"><a name="b84235270619112_1"></a><a name="b84235270619112_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="56.120000000000005%" id="mcps1.2.4.1.3"><p id="p23288300"><a name="p23288300"></a><a name="p23288300"></a><strong id="b842352706112423_1"><a name="b842352706112423_1"></a><a name="b842352706112423_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row7304143"><td class="cellrowborder" valign="top" width="20.41%" headers="mcps1.2.4.1.1 "><p id="p54764719"><a name="p54764719"></a><a name="p54764719"></a>recordsets</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.47%" headers="mcps1.2.4.1.2 "><p id="p10465156"><a name="p10465156"></a><a name="p10465156"></a>List data structure</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.120000000000005%" headers="mcps1.2.4.1.3 "><p id="p45797138"><a name="p45797138"></a><a name="p45797138"></a>Record set list object</p>
    </td>
    </tr>
    <tr id="row2133747418458"><td class="cellrowborder" valign="top" width="20.41%" headers="mcps1.2.4.1.1 "><p id="p5781953918458"><a name="p5781953918458"></a><a name="p5781953918458"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.47%" headers="mcps1.2.4.1.2 "><p id="p5469790918458"><a name="p5469790918458"></a><a name="p5469790918458"></a>object</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.120000000000005%" headers="mcps1.2.4.1.3 "><p id="p5673028518536"><a name="p5673028518536"></a><a name="p5673028518536"></a>Number of resources that meet the filter condition</p>
    </td>
    </tr>
    </tbody>
    </table>

    [Table 2](#table21574462) describes parameters under the **recordsets** field, and [Table 4](#table9971756154520) describes the parameter under the **metadata**  field.

    **Table  3**  Description of the  **recordsets**  field

    <a name="table18580737"></a><table><thead align="left"><tr id="en-us_topic_0037129968_en-us_topic_0037134404_row52466955175323"><th class="cellrowborder" valign="top" width="27.889999999999997%" id="mcps1.2.4.1.1"><p id="en-us_topic_0037129968_en-us_topic_0037134404_p2769858175323"><a name="en-us_topic_0037129968_en-us_topic_0037134404_p2769858175323"></a><a name="en-us_topic_0037129968_en-us_topic_0037134404_p2769858175323"></a><strong id="b162774213314533_2"><a name="b162774213314533_2"></a><a name="b162774213314533_2"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23.810000000000002%" id="mcps1.2.4.1.2"><p id="en-us_topic_0037129968_en-us_topic_0037134404_p46296309175323"><a name="en-us_topic_0037129968_en-us_topic_0037134404_p46296309175323"></a><a name="en-us_topic_0037129968_en-us_topic_0037134404_p46296309175323"></a><strong id="b84235270619112_2"><a name="b84235270619112_2"></a><a name="b84235270619112_2"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="48.3%" id="mcps1.2.4.1.3"><p id="en-us_topic_0037129968_en-us_topic_0037134404_p62697904175323"><a name="en-us_topic_0037129968_en-us_topic_0037134404_p62697904175323"></a><a name="en-us_topic_0037129968_en-us_topic_0037134404_p62697904175323"></a><strong id="b842352706112423_2"><a name="b842352706112423_2"></a><a name="b842352706112423_2"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0037129968_en-us_topic_0037134404_row47909891175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037129968_en-us_topic_0037134404_p64112397175323"><a name="en-us_topic_0037129968_en-us_topic_0037134404_p64112397175323"></a><a name="en-us_topic_0037129968_en-us_topic_0037134404_p64112397175323"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037129968_en-us_topic_0037134404_p1660870175323"><a name="en-us_topic_0037129968_en-us_topic_0037134404_p1660870175323"></a><a name="en-us_topic_0037129968_en-us_topic_0037134404_p1660870175323"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.3%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037129968_en-us_topic_0037134404_p1249204175323"><a name="en-us_topic_0037129968_en-us_topic_0037134404_p1249204175323"></a><a name="en-us_topic_0037129968_en-us_topic_0037134404_p1249204175323"></a>Record set ID</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037129968_en-us_topic_0037134404_row6942422175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037129968_en-us_topic_0037134404_p64097412175323"><a name="en-us_topic_0037129968_en-us_topic_0037134404_p64097412175323"></a><a name="en-us_topic_0037129968_en-us_topic_0037134404_p64097412175323"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037129968_en-us_topic_0037134404_p44990515175323"><a name="en-us_topic_0037129968_en-us_topic_0037134404_p44990515175323"></a><a name="en-us_topic_0037129968_en-us_topic_0037134404_p44990515175323"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.3%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037129968_en-us_topic_0037134404_p32019574175323"><a name="en-us_topic_0037129968_en-us_topic_0037134404_p32019574175323"></a><a name="en-us_topic_0037129968_en-us_topic_0037134404_p32019574175323"></a>Record set name</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037129968_en-us_topic_0037134404_row61442071175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037129968_en-us_topic_0037134404_p51194416175323"><a name="en-us_topic_0037129968_en-us_topic_0037134404_p51194416175323"></a><a name="en-us_topic_0037129968_en-us_topic_0037134404_p51194416175323"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037129968_en-us_topic_0037134404_p63301991175323"><a name="en-us_topic_0037129968_en-us_topic_0037134404_p63301991175323"></a><a name="en-us_topic_0037129968_en-us_topic_0037134404_p63301991175323"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.3%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037129968_en-us_topic_0037134404_p43966660175323"><a name="en-us_topic_0037129968_en-us_topic_0037134404_p43966660175323"></a><a name="en-us_topic_0037129968_en-us_topic_0037134404_p43966660175323"></a>Record set description</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037129968_en-us_topic_0037134404_row2176746175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037129968_en-us_topic_0037134404_p11805366175323"><a name="en-us_topic_0037129968_en-us_topic_0037134404_p11805366175323"></a><a name="en-us_topic_0037129968_en-us_topic_0037134404_p11805366175323"></a>zone_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037129968_en-us_topic_0037134404_p1051908175323"><a name="en-us_topic_0037129968_en-us_topic_0037134404_p1051908175323"></a><a name="en-us_topic_0037129968_en-us_topic_0037134404_p1051908175323"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.3%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037129968_en-us_topic_0037134404_p10043845175323"><a name="en-us_topic_0037129968_en-us_topic_0037134404_p10043845175323"></a><a name="en-us_topic_0037129968_en-us_topic_0037134404_p10043845175323"></a>Zone ID of the record set</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037129968_en-us_topic_0037134404_row61212722175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037129968_en-us_topic_0037134404_p8318586175323"><a name="en-us_topic_0037129968_en-us_topic_0037134404_p8318586175323"></a><a name="en-us_topic_0037129968_en-us_topic_0037134404_p8318586175323"></a>zone_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037129968_en-us_topic_0037134404_p31287919175323"><a name="en-us_topic_0037129968_en-us_topic_0037134404_p31287919175323"></a><a name="en-us_topic_0037129968_en-us_topic_0037134404_p31287919175323"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.3%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037129968_en-us_topic_0037134404_p16372315175323"><a name="en-us_topic_0037129968_en-us_topic_0037134404_p16372315175323"></a><a name="en-us_topic_0037129968_en-us_topic_0037134404_p16372315175323"></a>Zone name of the record set</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037129968_en-us_topic_0037134404_row38132372175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037129968_en-us_topic_0037134404_p37461920175323"><a name="en-us_topic_0037129968_en-us_topic_0037134404_p37461920175323"></a><a name="en-us_topic_0037129968_en-us_topic_0037134404_p37461920175323"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037129968_en-us_topic_0037134404_p27536075175323"><a name="en-us_topic_0037129968_en-us_topic_0037134404_p27536075175323"></a><a name="en-us_topic_0037129968_en-us_topic_0037134404_p27536075175323"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.3%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037129968_en-us_topic_0037134404_p24813356175323"><a name="en-us_topic_0037129968_en-us_topic_0037134404_p24813356175323"></a><a name="en-us_topic_0037129968_en-us_topic_0037134404_p24813356175323"></a>Record set type</p>
    <p id="p1484155154215"><a name="p1484155154215"></a><a name="p1484155154215"></a>The value can be <strong id="b84235270693731"><a name="b84235270693731"></a><a name="b84235270693731"></a>A</strong>,&nbsp;<strong id="b84235270693735"><a name="b84235270693735"></a><a name="b84235270693735"></a>AAAA</strong>,&nbsp;<strong id="b84235270693738"><a name="b84235270693738"></a><a name="b84235270693738"></a>MX</strong>,&nbsp;<strong id="b84235270693741"><a name="b84235270693741"></a><a name="b84235270693741"></a>CNAME</strong>,&nbsp;<strong id="b84235270693746"><a name="b84235270693746"></a><a name="b84235270693746"></a>TXT</strong>,&nbsp;<strong id="b84235270693755"><a name="b84235270693755"></a><a name="b84235270693755"></a>NS</strong>&nbsp;(only in public zones),&nbsp;<strong id="b8423527069382"><a name="b8423527069382"></a><a name="b8423527069382"></a>SRV</strong>,&nbsp;<strong id="b8423527069385"><a name="b8423527069385"></a><a name="b8423527069385"></a>PTR</strong>&nbsp;(only in private zones), and&nbsp;<strong id="b84235270693810"><a name="b84235270693810"></a><a name="b84235270693810"></a>CAA</strong> (only in public zones).</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037129968_en-us_topic_0037134404_row20796819175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037129968_en-us_topic_0037134404_p4811553175323"><a name="en-us_topic_0037129968_en-us_topic_0037134404_p4811553175323"></a><a name="en-us_topic_0037129968_en-us_topic_0037134404_p4811553175323"></a>ttl</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037129968_en-us_topic_0037134404_p47559731175323"><a name="en-us_topic_0037129968_en-us_topic_0037134404_p47559731175323"></a><a name="en-us_topic_0037129968_en-us_topic_0037134404_p47559731175323"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.3%" headers="mcps1.2.4.1.3 "><p id="p40578139142936"><a name="p40578139142936"></a><a name="p40578139142936"></a>Caching period of a domain name (in seconds)</p>
    <p id="en-us_topic_0037129968_en-us_topic_0037134404_p22097398175323"><a name="en-us_topic_0037129968_en-us_topic_0037134404_p22097398175323"></a><a name="en-us_topic_0037129968_en-us_topic_0037134404_p22097398175323"></a>A longer caching period makes a change on the authoritative DNS server take longer time to be synchronized to other DNS servers.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037129968_en-us_topic_0037134404_row13978060175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037129968_en-us_topic_0037134404_p43388342175323"><a name="en-us_topic_0037129968_en-us_topic_0037134404_p43388342175323"></a><a name="en-us_topic_0037129968_en-us_topic_0037134404_p43388342175323"></a>records</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037129968_en-us_topic_0037134404_p29596719175323"><a name="en-us_topic_0037129968_en-us_topic_0037134404_p29596719175323"></a><a name="en-us_topic_0037129968_en-us_topic_0037134404_p29596719175323"></a>List&lt;string&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.3%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037129968_en-us_topic_0037134404_p30492925175323"><a name="en-us_topic_0037129968_en-us_topic_0037134404_p30492925175323"></a><a name="en-us_topic_0037129968_en-us_topic_0037134404_p30492925175323"></a>Domain name resolution result</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037129968_en-us_topic_0037134404_row23148559175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037129968_en-us_topic_0037134404_p36524189175323"><a name="en-us_topic_0037129968_en-us_topic_0037134404_p36524189175323"></a><a name="en-us_topic_0037129968_en-us_topic_0037134404_p36524189175323"></a>create_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037129968_en-us_topic_0037134404_p47080972175323"><a name="en-us_topic_0037129968_en-us_topic_0037134404_p47080972175323"></a><a name="en-us_topic_0037129968_en-us_topic_0037134404_p47080972175323"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.3%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037129968_en-us_topic_0037134404_p15737135175323"><a name="en-us_topic_0037129968_en-us_topic_0037134404_p15737135175323"></a><a name="en-us_topic_0037129968_en-us_topic_0037134404_p15737135175323"></a>Time when the record set was created</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037129968_en-us_topic_0037134404_row33465792175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037129968_en-us_topic_0037134404_p42570937175323"><a name="en-us_topic_0037129968_en-us_topic_0037134404_p42570937175323"></a><a name="en-us_topic_0037129968_en-us_topic_0037134404_p42570937175323"></a>update_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037129968_en-us_topic_0037134404_p27449776175323"><a name="en-us_topic_0037129968_en-us_topic_0037134404_p27449776175323"></a><a name="en-us_topic_0037129968_en-us_topic_0037134404_p27449776175323"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.3%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037129968_en-us_topic_0037134404_p63703533175323"><a name="en-us_topic_0037129968_en-us_topic_0037134404_p63703533175323"></a><a name="en-us_topic_0037129968_en-us_topic_0037134404_p63703533175323"></a>Time when the record set was updated</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037129968_en-us_topic_0037134404_row17850883175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037129968_en-us_topic_0037134404_p36228271175323"><a name="en-us_topic_0037129968_en-us_topic_0037134404_p36228271175323"></a><a name="en-us_topic_0037129968_en-us_topic_0037134404_p36228271175323"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037129968_en-us_topic_0037134404_p6480061175323"><a name="en-us_topic_0037129968_en-us_topic_0037134404_p6480061175323"></a><a name="en-us_topic_0037129968_en-us_topic_0037134404_p6480061175323"></a>enum</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.3%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037129968_en-us_topic_0037134404_p65781854175323"><a name="en-us_topic_0037129968_en-us_topic_0037134404_p65781854175323"></a><a name="en-us_topic_0037129968_en-us_topic_0037134404_p65781854175323"></a>Resource status</p>
    <p id="en-us_topic_0037129968_en-us_topic_0037134404_p51374523175323"><a name="en-us_topic_0037129968_en-us_topic_0037134404_p51374523175323"></a><a name="en-us_topic_0037129968_en-us_topic_0037134404_p51374523175323"></a>The value can be <strong id="b84235270695628"><a name="b84235270695628"></a><a name="b84235270695628"></a>PENDING_CREATE</strong>,&nbsp;<strong id="b84235270695635"><a name="b84235270695635"></a><a name="b84235270695635"></a>ACTIVE</strong>,&nbsp;<strong id="b84235270683910"><a name="b84235270683910"></a><a name="b84235270683910"></a>PENDING_UPDATE</strong>,&nbsp;<strong id="b84235270695643"><a name="b84235270695643"></a><a name="b84235270695643"></a>PENDING_DELETE</strong>, or&nbsp;<strong id="b84235270695650"><a name="b84235270695650"></a><a name="b84235270695650"></a>ERROR</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037129968_en-us_topic_0037134404_row61184424175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037129968_en-us_topic_0037134404_p49633411175323"><a name="en-us_topic_0037129968_en-us_topic_0037134404_p49633411175323"></a><a name="en-us_topic_0037129968_en-us_topic_0037134404_p49633411175323"></a>default</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037129968_en-us_topic_0037134404_p56048766175323"><a name="en-us_topic_0037129968_en-us_topic_0037134404_p56048766175323"></a><a name="en-us_topic_0037129968_en-us_topic_0037134404_p56048766175323"></a>boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.3%" headers="mcps1.2.4.1.3 "><p id="p1942025514322"><a name="p1942025514322"></a><a name="p1942025514322"></a>Whether the record set is created by default</p>
    <p id="p4056457114322"><a name="p4056457114322"></a><a name="p4056457114322"></a>A default record set cannot be deleted.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037129968_en-us_topic_0037134404_row15199048201026"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037129968_en-us_topic_0037134404_p23163408201026"><a name="en-us_topic_0037129968_en-us_topic_0037134404_p23163408201026"></a><a name="en-us_topic_0037129968_en-us_topic_0037134404_p23163408201026"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037129968_en-us_topic_0037134404_p40653752201026"><a name="en-us_topic_0037129968_en-us_topic_0037134404_p40653752201026"></a><a name="en-us_topic_0037129968_en-us_topic_0037134404_p40653752201026"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.3%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037129968_en-us_topic_0037134404_p4619625201026"><a name="en-us_topic_0037129968_en-us_topic_0037134404_p4619625201026"></a><a name="en-us_topic_0037129968_en-us_topic_0037134404_p4619625201026"></a>Project ID of the record set</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037129968_en-us_topic_0037134404_row3965248419366"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037129968_en-us_topic_0037134404_p2132803819366"><a name="en-us_topic_0037129968_en-us_topic_0037134404_p2132803819366"></a><a name="en-us_topic_0037129968_en-us_topic_0037134404_p2132803819366"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037129968_en-us_topic_0037134404_p1127763319366"><a name="en-us_topic_0037129968_en-us_topic_0037134404_p1127763319366"></a><a name="en-us_topic_0037129968_en-us_topic_0037134404_p1127763319366"></a>object</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.3%" headers="mcps1.2.4.1.3 "><p id="p34781370143021"><a name="p34781370143021"></a><a name="p34781370143021"></a>Link of the current resource or other related resources</p>
    <p id="en-us_topic_0037129968_en-us_topic_0037134404_p4107308719366"><a name="en-us_topic_0037129968_en-us_topic_0037134404_p4107308719366"></a><a name="en-us_topic_0037129968_en-us_topic_0037134404_p4107308719366"></a>When a response is broken into pages, a <strong id="b22743378143011"><a name="b22743378143011"></a><a name="b22743378143011"></a>next</strong> link is provided to retrieve all results.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  Description of the  **metadata**  field

    <a name="table9971756154520"></a><table><thead align="left"><tr id="en-us_topic_0037134402_row58979189175457"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="en-us_topic_0037134402_p46156243175457"><a name="en-us_topic_0037134402_p46156243175457"></a><a name="en-us_topic_0037134402_p46156243175457"></a><strong id="en-us_topic_0037134402_b162774213314533"><a name="en-us_topic_0037134402_b162774213314533"></a><a name="en-us_topic_0037134402_b162774213314533"></a>Parameter</strong></p>
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
            "self": "https://Endpoint/v2/recordsets"
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
                "update_at": "2016-11-17T11:56:03.827",
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
                "update_at": "2016-11-17T11:56:03.827",
                "default": true,
                "project_id": "e55c6f3dc4e34c9f86353b664ae0e70c"
            },
            {
                "id": "2c9eb155587228570158722996ca0002",
                "name": "example.org.",
                "type": "SOA",
                "ttl": 300,
                "records": [
                    "ns1.hotrot.de. xx.example.org. (1 7200 900 1209600 300)"
                ],
                "status": "ACTIVE",
                "links": {
                    "self": "https://Endpoint/v2/zones/2c9eb155587228570158722996c50001/recordsets/2c9eb155587228570158722996ca0002"
                },
                "zone_id": "2c9eb155587228570158722996c50001",
                "zone_name": "example.org.",
                "create_at": "2016-11-17T12:01:17.996",
                "update_at": "2016-11-17T12:56:03.827",
                "default": true,
                "project_id": "e55c6f3dc4e34c9f86353b664ae0e70c"
            },
            {
                "id": "2c9eb155587228570158722996ca0004",
                "name": "example.org.",
                "type": "NS",
                "ttl": 172800,
                "records": [
                    "ns2.hotrot.de.",
                    "ns1.hotrot.de."
                ],
                "status": "ACTIVE",
                "links": {
                    "self": "https://Endpoint/v2/zones/2c9eb155587228570158722996c50001/recordsets/2c9eb155587228570158722996ca0004"
                },
                "zone_id": "2c9eb155587228570158722996c50001",
                "zone_name": "example.org.",
                "create_at": "2016-11-17T12:01:17.996",
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
                "status": "ACTIVE",
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
            "total_count": 5
        }
    }
    
    ```


## Returned Value<a name="section34728767"></a>

See  [General Request Return Code](general-request-return-code.md).

