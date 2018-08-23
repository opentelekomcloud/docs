# Querying All PTR Records<a name="EN-US_TOPIC_0042318615"></a>

## Function<a name="section29105235"></a>

Query PTR records of EIPs.

## URI<a name="section60620523"></a>

-   URI format

    GET /v2/reverse/floatingips?limit=\{limit\}&marker=\{marker\}&offset=\{offset\}&tags=\{tags\}

-   Parameter description

    **Table  1**  Parameters in the URI

    <a name="table1562846014112"></a><table><thead align="left"><tr id="en-us_topic_0037134402_en-us_topic_0037129969_row24110047"><th class="cellrowborder" valign="top" width="20.202020202020204%" id="mcps1.2.5.1.1"><p id="en-us_topic_0037134402_en-us_topic_0037129969_p6756797"><a name="en-us_topic_0037134402_en-us_topic_0037129969_p6756797"></a><a name="en-us_topic_0037134402_en-us_topic_0037129969_p6756797"></a><strong id="b162774213314533"><a name="b162774213314533"></a><a name="b162774213314533"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.17171717171717%" id="mcps1.2.5.1.2"><p id="en-us_topic_0037134402_en-us_topic_0037129969_p10429724"><a name="en-us_topic_0037134402_en-us_topic_0037129969_p10429724"></a><a name="en-us_topic_0037134402_en-us_topic_0037129969_p10429724"></a><strong id="b593421527191713"><a name="b593421527191713"></a><a name="b593421527191713"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.14141414141414%" id="mcps1.2.5.1.3"><p id="en-us_topic_0037134402_en-us_topic_0037129969_p39501348"><a name="en-us_topic_0037134402_en-us_topic_0037129969_p39501348"></a><a name="en-us_topic_0037134402_en-us_topic_0037129969_p39501348"></a><strong id="b84235270619112"><a name="b84235270619112"></a><a name="b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="48.484848484848484%" id="mcps1.2.5.1.4"><p id="en-us_topic_0037134402_en-us_topic_0037129969_p45492604"><a name="en-us_topic_0037134402_en-us_topic_0037129969_p45492604"></a><a name="en-us_topic_0037134402_en-us_topic_0037129969_p45492604"></a><strong id="b842352706112423"><a name="b842352706112423"></a><a name="b842352706112423"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0037134402_en-us_topic_0037129969_row61022284"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0037134402_en-us_topic_0037129969_p43857981"><a name="en-us_topic_0037134402_en-us_topic_0037129969_p43857981"></a><a name="en-us_topic_0037134402_en-us_topic_0037129969_p43857981"></a>marker</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0037134402_en-us_topic_0037129969_p62835574"><a name="en-us_topic_0037134402_en-us_topic_0037129969_p62835574"></a><a name="en-us_topic_0037134402_en-us_topic_0037129969_p62835574"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0037134402_en-us_topic_0037129969_p56516768"><a name="en-us_topic_0037134402_en-us_topic_0037129969_p56516768"></a><a name="en-us_topic_0037134402_en-us_topic_0037129969_p56516768"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.2.5.1.4 "><p id="p6505910417182"><a name="p6505910417182"></a><a name="p6505910417182"></a>Start resource ID of pagination query</p>
    <p id="en-us_topic_0037134402_en-us_topic_0037129969_p14455523"><a name="en-us_topic_0037134402_en-us_topic_0037129969_p14455523"></a><a name="en-us_topic_0037134402_en-us_topic_0037129969_p14455523"></a>If the parameter is left blank, only resources on the first page are queried.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037134402_en-us_topic_0037129969_row62990845"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0037134402_en-us_topic_0037129969_p1984791"><a name="en-us_topic_0037134402_en-us_topic_0037129969_p1984791"></a><a name="en-us_topic_0037134402_en-us_topic_0037129969_p1984791"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0037134402_en-us_topic_0037129969_p26550365"><a name="en-us_topic_0037134402_en-us_topic_0037129969_p26550365"></a><a name="en-us_topic_0037134402_en-us_topic_0037129969_p26550365"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0037134402_en-us_topic_0037129969_p3095993"><a name="en-us_topic_0037134402_en-us_topic_0037129969_p3095993"></a><a name="en-us_topic_0037134402_en-us_topic_0037129969_p3095993"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0037134402_en-us_topic_0037129969_ul18169499193915"></a><a name="en-us_topic_0037134402_en-us_topic_0037129969_ul18169499193915"></a><ul id="en-us_topic_0037134402_en-us_topic_0037129969_ul18169499193915"><li id="li63087119165322"><a name="li63087119165322"></a><a name="li63087119165322"></a>Number of resources returned on each page</li><li id="li1676974165333"><a name="li1676974165333"></a><a name="li1676974165333"></a>Value range: 0–500<p id="p21932815165334"><a name="p21932815165334"></a><a name="p21932815165334"></a>Commonly used values are <strong id="b1862183916542"><a name="b1862183916542"></a><a name="b1862183916542"></a>10</strong>, <strong id="b3506876216546"><a name="b3506876216546"></a><a name="b3506876216546"></a>20</strong>, and <strong id="b1964630516549"><a name="b1964630516549"></a><a name="b1964630516549"></a>50</strong>.</p>
    </li></ul>
    </td>
    </tr>
    <tr id="row58150604195642"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p11536930195644"><a name="p11536930195644"></a><a name="p11536930195644"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.2.5.1.2 "><p id="p62076162195644"><a name="p62076162195644"></a><a name="p62076162195644"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.3 "><p id="p62113243195644"><a name="p62113243195644"></a><a name="p62113243195644"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.2.5.1.4 "><a name="ul65116756195644"></a><a name="ul65116756195644"></a><ul id="ul65116756195644"><li id="li49179892195644"><a name="li49179892195644"></a><a name="li49179892195644"></a>Start page of the list, which ranges from 0 to 2147483647.</li><li id="li39965845195644"><a name="li39965845195644"></a><a name="li39965845195644"></a>When the value of <strong id="b842352706193255"><a name="b842352706193255"></a><a name="b842352706193255"></a>marker</strong> is not blank, it determines the start of a page.</li></ul>
    </td>
    </tr>
    <tr id="row6180858115857"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p6537624212219"><a name="p6537624212219"></a><a name="p6537624212219"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.2.5.1.2 "><p id="p6098421112219"><a name="p6098421112219"></a><a name="p6098421112219"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.3 "><p id="p4077405312219"><a name="p4077405312219"></a><a name="p4077405312219"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.2.5.1.4 "><p id="p1436398312219"><a name="p1436398312219"></a><a name="p1436398312219"></a>Resource tag</p>
    <p id="p6216698912219"><a name="p6216698912219"></a><a name="p6216698912219"></a>The format is as follows: <strong id="b8423527069140"><a name="b8423527069140"></a><a name="b8423527069140"></a>key1,value1|key2,value2</strong>.</p>
    <p id="p64141841114123"><a name="p64141841114123"></a><a name="p64141841114123"></a>Multiple tags are separated by vertical bar (|). The key and value of each tag are separated by comma (,).</p>
    <p id="p2263199412219"><a name="p2263199412219"></a><a name="p2263199412219"></a>All tags listed will be queried.</p>
    <p id="p65263192115146"><a name="p65263192115146"></a><a name="p65263192115146"></a>For details, see section <a href="tag-management.html">Tag Management</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section8713795"></a>

None

## Response<a name="section11315292"></a>

-   Parameter description

    **Table  2**  Parameters in the response

    <a name="table13410777181232"></a><table><thead align="left"><tr id="row8598877181232"><th class="cellrowborder" valign="top" width="18.18%" id="mcps1.2.4.1.1"><p id="p25420464181232"><a name="p25420464181232"></a><a name="p25420464181232"></a><strong id="b162774213314533_1"><a name="b162774213314533_1"></a><a name="b162774213314533_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15.43%" id="mcps1.2.4.1.2"><p id="p45791683181232"><a name="p45791683181232"></a><a name="p45791683181232"></a><strong id="b84235270619112_1"><a name="b84235270619112_1"></a><a name="b84235270619112_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="66.39%" id="mcps1.2.4.1.3"><p id="p18138814181232"><a name="p18138814181232"></a><a name="p18138814181232"></a><strong id="b842352706112423_1"><a name="b842352706112423_1"></a><a name="b842352706112423_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row59957834181232"><td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.1 "><p id="p24746382181232"><a name="p24746382181232"></a><a name="p24746382181232"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.43%" headers="mcps1.2.4.1.2 "><p id="p58299955181232"><a name="p58299955181232"></a><a name="p58299955181232"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.39%" headers="mcps1.2.4.1.3 "><p id="p5040034717923"><a name="p5040034717923"></a><a name="p5040034717923"></a>Link of the current resource or other related resources</p>
    <p id="p5094994217923"><a name="p5094994217923"></a><a name="p5094994217923"></a>When a response is broken into pages, a <strong id="b84235270695245"><a name="b84235270695245"></a><a name="b84235270695245"></a>next</strong> link is provided to retrieve all results.</p>
    </td>
    </tr>
    <tr id="row17649295181232"><td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.1 "><p id="p20306794181232"><a name="p20306794181232"></a><a name="p20306794181232"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.43%" headers="mcps1.2.4.1.2 "><p id="p34237593181232"><a name="p34237593181232"></a><a name="p34237593181232"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.39%" headers="mcps1.2.4.1.3 "><p id="p21781637181232"><a name="p21781637181232"></a><a name="p21781637181232"></a>Number of resources that meet the filter condition</p>
    </td>
    </tr>
    <tr id="row61817005181232"><td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.1 "><p id="p41121470181232"><a name="p41121470181232"></a><a name="p41121470181232"></a>floatingips</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.43%" headers="mcps1.2.4.1.2 "><p id="p42504768181232"><a name="p42504768181232"></a><a name="p42504768181232"></a>List object</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.39%" headers="mcps1.2.4.1.3 "><p id="p20334170181232"><a name="p20334170181232"></a><a name="p20334170181232"></a>PTR record object list</p>
    </td>
    </tr>
    </tbody>
    </table>

    [Table 3](#table43740677113542)  describes parameters in the  **floatingips**  field, and  [Table 4](#table16355953155210)  describes the parameter under the  **metadata**  field.

    **Table  3**  Description of the  **floatingips**  field

    <a name="table43740677113542"></a><table><thead align="left"><tr id="en-us_topic_0042318613_row5725206118456"><th class="cellrowborder" valign="top" width="18.18%" id="mcps1.2.4.1.1"><p id="en-us_topic_0042318613_p690539418456"><a name="en-us_topic_0042318613_p690539418456"></a><a name="en-us_topic_0042318613_p690539418456"></a><strong id="b162774213314533_2"><a name="b162774213314533_2"></a><a name="b162774213314533_2"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.189999999999998%" id="mcps1.2.4.1.2"><p id="en-us_topic_0042318613_p2246606418456"><a name="en-us_topic_0042318613_p2246606418456"></a><a name="en-us_topic_0042318613_p2246606418456"></a><strong id="b84235270619112_2"><a name="b84235270619112_2"></a><a name="b84235270619112_2"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="62.629999999999995%" id="mcps1.2.4.1.3"><p id="en-us_topic_0042318613_p781187018456"><a name="en-us_topic_0042318613_p781187018456"></a><a name="en-us_topic_0042318613_p781187018456"></a><strong id="b842352706112423_2"><a name="b842352706112423_2"></a><a name="b842352706112423_2"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0042318613_row2878170018456"><td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0042318613_p4961636318456"><a name="en-us_topic_0042318613_p4961636318456"></a><a name="en-us_topic_0042318613_p4961636318456"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0042318613_p5950245818456"><a name="en-us_topic_0042318613_p5950245818456"></a><a name="en-us_topic_0042318613_p5950245818456"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.629999999999995%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0042318613_p5496981818456"><a name="en-us_topic_0042318613_p5496981818456"></a><a name="en-us_topic_0042318613_p5496981818456"></a>PTR record ID, which is in <strong id="b842352706151833"><a name="b842352706151833"></a><a name="b842352706151833"></a>{region}:{floatingip_id}</strong> format</p>
    </td>
    </tr>
    <tr id="en-us_topic_0042318613_row3274940018456"><td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0042318613_p3545576918456"><a name="en-us_topic_0042318613_p3545576918456"></a><a name="en-us_topic_0042318613_p3545576918456"></a>ptrdname</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0042318613_p5334507918456"><a name="en-us_topic_0042318613_p5334507918456"></a><a name="en-us_topic_0042318613_p5334507918456"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.629999999999995%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0042318613_p2598415318456"><a name="en-us_topic_0042318613_p2598415318456"></a><a name="en-us_topic_0042318613_p2598415318456"></a>Domain name of the PTR record</p>
    </td>
    </tr>
    <tr id="en-us_topic_0042318613_row3253079218456"><td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0042318613_p1774845918456"><a name="en-us_topic_0042318613_p1774845918456"></a><a name="en-us_topic_0042318613_p1774845918456"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0042318613_p2833911218456"><a name="en-us_topic_0042318613_p2833911218456"></a><a name="en-us_topic_0042318613_p2833911218456"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.629999999999995%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0042318613_p1376672518456"><a name="en-us_topic_0042318613_p1376672518456"></a><a name="en-us_topic_0042318613_p1376672518456"></a>PTR record description</p>
    </td>
    </tr>
    <tr id="en-us_topic_0042318613_row5679166318456"><td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0042318613_p3672198418456"><a name="en-us_topic_0042318613_p3672198418456"></a><a name="en-us_topic_0042318613_p3672198418456"></a>ttl</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0042318613_p2169069318456"><a name="en-us_topic_0042318613_p2169069318456"></a><a name="en-us_topic_0042318613_p2169069318456"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.629999999999995%" headers="mcps1.2.4.1.3 "><p id="p27862757171912"><a name="p27862757171912"></a><a name="p27862757171912"></a>Caching period of a PTR record (in seconds)</p>
    <p id="en-us_topic_0042318613_p1211568618456"><a name="en-us_topic_0042318613_p1211568618456"></a><a name="en-us_topic_0042318613_p1211568618456"></a>The default value is <strong id="b556287791322"><a name="b556287791322"></a><a name="b556287791322"></a>300s</strong>.</p>
    <p id="en-us_topic_0042318613_p4184654118456"><a name="en-us_topic_0042318613_p4184654118456"></a><a name="en-us_topic_0042318613_p4184654118456"></a>The value range is 300–2147483647.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0042318613_row3412662318456"><td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0042318613_p1279309418456"><a name="en-us_topic_0042318613_p1279309418456"></a><a name="en-us_topic_0042318613_p1279309418456"></a>address</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0042318613_p2960772218456"><a name="en-us_topic_0042318613_p2960772218456"></a><a name="en-us_topic_0042318613_p2960772218456"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.629999999999995%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0042318613_p4941528218456"><a name="en-us_topic_0042318613_p4941528218456"></a><a name="en-us_topic_0042318613_p4941528218456"></a>EIP</p>
    </td>
    </tr>
    <tr id="en-us_topic_0042318613_row4208435918456"><td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0042318613_p5338995318456"><a name="en-us_topic_0042318613_p5338995318456"></a><a name="en-us_topic_0042318613_p5338995318456"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0042318613_p2961896418456"><a name="en-us_topic_0042318613_p2961896418456"></a><a name="en-us_topic_0042318613_p2961896418456"></a>enum</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.629999999999995%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0042318613_p5032586318456"><a name="en-us_topic_0042318613_p5032586318456"></a><a name="en-us_topic_0042318613_p5032586318456"></a>Resource status</p>
    <p id="p1427831035118"><a name="p1427831035118"></a><a name="p1427831035118"></a>The value can be <strong id="b84235270695628"><a name="b84235270695628"></a><a name="b84235270695628"></a>PENDING_CREATE</strong>, <strong id="b84235270695635"><a name="b84235270695635"></a><a name="b84235270695635"></a>ACTIVE</strong>, <strong id="b84235270695643"><a name="b84235270695643"></a><a name="b84235270695643"></a>PENDING_DELETE</strong>, <strong id="b842352706141041"><a name="b842352706141041"></a><a name="b842352706141041"></a>PENDING_UPDATE</strong>, or <strong id="b84235270695650"><a name="b84235270695650"></a><a name="b84235270695650"></a>ERROR</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0042318613_row4986307418456"><td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0042318613_p1237719818456"><a name="en-us_topic_0042318613_p1237719818456"></a><a name="en-us_topic_0042318613_p1237719818456"></a>action</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0042318613_p6302897818456"><a name="en-us_topic_0042318613_p6302897818456"></a><a name="en-us_topic_0042318613_p6302897818456"></a>enum</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.629999999999995%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0042318613_p507362318456"><a name="en-us_topic_0042318613_p507362318456"></a><a name="en-us_topic_0042318613_p507362318456"></a>Requested operation on the resource</p>
    <p id="p3570202615112"><a name="p3570202615112"></a><a name="p3570202615112"></a>The value can be <strong id="b842352706141356"><a name="b842352706141356"></a><a name="b842352706141356"></a>CREATE</strong>, <strong id="b84235270614144"><a name="b84235270614144"></a><a name="b84235270614144"></a>UPDATE</strong>, or <strong id="b84235270614146"><a name="b84235270614146"></a><a name="b84235270614146"></a>DELETE</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0042318613_row831034118456"><td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0042318613_p204899518456"><a name="en-us_topic_0042318613_p204899518456"></a><a name="en-us_topic_0042318613_p204899518456"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0042318613_p3175087318456"><a name="en-us_topic_0042318613_p3175087318456"></a><a name="en-us_topic_0042318613_p3175087318456"></a>object</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.629999999999995%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0042318613_p2168392018456"><a name="en-us_topic_0042318613_p2168392018456"></a><a name="en-us_topic_0042318613_p2168392018456"></a>Link of the current resource or other related resources</p>
    <p id="en-us_topic_0042318613_p6093755518456"><a name="en-us_topic_0042318613_p6093755518456"></a><a name="en-us_topic_0042318613_p6093755518456"></a>When a response is broken into pages, a <strong id="b2670674215521"><a name="b2670674215521"></a><a name="b2670674215521"></a>next</strong> link is provided to retrieve all results.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  Description of the  **metadata**  field

    <a name="table16355953155210"></a><table><thead align="left"><tr id="en-us_topic_0037134402_row58979189175457"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="en-us_topic_0037134402_p46156243175457"><a name="en-us_topic_0037134402_p46156243175457"></a><a name="en-us_topic_0037134402_p46156243175457"></a><strong id="en-us_topic_0037134402_b162774213314533"><a name="en-us_topic_0037134402_b162774213314533"></a><a name="en-us_topic_0037134402_b162774213314533"></a>Parameter</strong></p>
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
            "self": "https://Endpoint/v2/reverse/floatingips"
        },
        "metadata": {
            "total_count": 1
        },
        "floatingips": [
            {
                "id": "region\_id:c5504932-bf23-4171-b655-b87a6bc59334",
                "ptrdname": "www.example.com.",
                "description": "Description for this PTR record",
                "address": "10.154.52.138",
                "action": "NONE",
                "ttl": 300,
                "status": "ACTIVE",
                "links": {
                    "self": "https://Endpoint/v2/reverse/floatingips/region\_id:c5504932-bf23-4171-b655-b87a6bc59334"
                }
            }
        ]
    }
    ```


## **Returned Value**<a name="section34728767"></a>

See  [General Request Return Code](general-request-return-code.md).

