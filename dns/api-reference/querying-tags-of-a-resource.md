# Querying Tags of a Resource<a name="EN-US_TOPIC_0094532733"></a>

## Function<a name="section2763065016101"></a>

Query tags of a specified resource.

TMS may use this API to query all tags of a specified DNS resource.

## URI<a name="section53701671161015"></a>

-   URI format

    GET /v2/\{resource\_type\}/\{resource\_id\}/tags

-   Parameter description

    **Table  1**  Parameters in the URI

    <a name="table6099729418149"></a><table><thead align="left"><tr id="en-us_topic_0101702788_row3442661918149"><th class="cellrowborder" valign="top" width="20.380000000000003%" id="mcps1.2.5.1.1"><p id="en-us_topic_0101702788_p3709279118149"><a name="en-us_topic_0101702788_p3709279118149"></a><a name="en-us_topic_0101702788_p3709279118149"></a><strong id="en-us_topic_0101702788_b162774213314533"><a name="en-us_topic_0101702788_b162774213314533"></a><a name="en-us_topic_0101702788_b162774213314533"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.439999999999998%" id="mcps1.2.5.1.2"><p id="en-us_topic_0101702788_p5172606218149"><a name="en-us_topic_0101702788_p5172606218149"></a><a name="en-us_topic_0101702788_p5172606218149"></a><strong id="en-us_topic_0101702788_b593421527191713"><a name="en-us_topic_0101702788_b593421527191713"></a><a name="en-us_topic_0101702788_b593421527191713"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="13.59%" id="mcps1.2.5.1.3"><p id="en-us_topic_0101702788_p2906151418149"><a name="en-us_topic_0101702788_p2906151418149"></a><a name="en-us_topic_0101702788_p2906151418149"></a><strong id="en-us_topic_0101702788_b84235270619112"><a name="en-us_topic_0101702788_b84235270619112"></a><a name="en-us_topic_0101702788_b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="46.589999999999996%" id="mcps1.2.5.1.4"><p id="en-us_topic_0101702788_p517246718149"><a name="en-us_topic_0101702788_p517246718149"></a><a name="en-us_topic_0101702788_p517246718149"></a><strong id="en-us_topic_0101702788_b842352706112423"><a name="en-us_topic_0101702788_b842352706112423"></a><a name="en-us_topic_0101702788_b842352706112423"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0101702788_row1923936518149"><td class="cellrowborder" valign="top" width="20.380000000000003%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0101702788_p1488470218149"><a name="en-us_topic_0101702788_p1488470218149"></a><a name="en-us_topic_0101702788_p1488470218149"></a>resource_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.439999999999998%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0101702788_p6481017518149"><a name="en-us_topic_0101702788_p6481017518149"></a><a name="en-us_topic_0101702788_p6481017518149"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.59%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0101702788_p1513281718149"><a name="en-us_topic_0101702788_p1513281718149"></a><a name="en-us_topic_0101702788_p1513281718149"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.589999999999996%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0101702788_p1779865118149"><a name="en-us_topic_0101702788_p1779865118149"></a><a name="en-us_topic_0101702788_p1779865118149"></a>Resource type, which can be <strong id="en-us_topic_0101702788_b84235270610339"><a name="en-us_topic_0101702788_b84235270610339"></a><a name="en-us_topic_0101702788_b84235270610339"></a>DNS-public_zone</strong>&nbsp;or&nbsp;<strong id="en-us_topic_0101702788_b84235270610347"><a name="en-us_topic_0101702788_b84235270610347"></a><a name="en-us_topic_0101702788_b84235270610347"></a>DNS-public_recordset</strong></p>
    </td>
    </tr>
    <tr id="en-us_topic_0101702788_row1082100911220"><td class="cellrowborder" valign="top" width="20.380000000000003%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0101702788_p408654311220"><a name="en-us_topic_0101702788_p408654311220"></a><a name="en-us_topic_0101702788_p408654311220"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.439999999999998%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0101702788_p6257460611220"><a name="en-us_topic_0101702788_p6257460611220"></a><a name="en-us_topic_0101702788_p6257460611220"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.59%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0101702788_p3537835811220"><a name="en-us_topic_0101702788_p3537835811220"></a><a name="en-us_topic_0101702788_p3537835811220"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.589999999999996%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0101702788_p4707473411220"><a name="en-us_topic_0101702788_p4707473411220"></a><a name="en-us_topic_0101702788_p4707473411220"></a>Resource ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section44958995161021"></a>

None

## Response<a name="section40090803161031"></a>

-   Parameter description

    **Table  2**  Parameter in the response

    <a name="table4239867614339"></a><table><thead align="left"><tr id="row4164086314339"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p2298305614339"><a name="p2298305614339"></a><a name="p2298305614339"></a><strong id="b162774213314533"><a name="b162774213314533"></a><a name="b162774213314533"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p4968821114339"><a name="p4968821114339"></a><a name="p4968821114339"></a><strong id="b84235270619112"><a name="b84235270619112"></a><a name="b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p6532219214339"><a name="p6532219214339"></a><a name="p6532219214339"></a><strong id="b842352706112423"><a name="b842352706112423"></a><a name="b842352706112423"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5102881914339"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p3969365514339"><a name="p3969365514339"></a><a name="p3969365514339"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p41141022143341"><a name="p41141022143341"></a><a name="p41141022143341"></a>List&lt;tag&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p4768081314339"><a name="p4768081314339"></a><a name="p4768081314339"></a>Tag list</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Parameters in the tag list

    <a name="table44639169143435"></a><table><thead align="left"><tr id="row42700170143435"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p57020104143435"><a name="p57020104143435"></a><a name="p57020104143435"></a><strong id="b912578598"><a name="b912578598"></a><a name="b912578598"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p55225708143435"><a name="p55225708143435"></a><a name="p55225708143435"></a><strong id="b780001266"><a name="b780001266"></a><a name="b780001266"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p44097393143435"><a name="p44097393143435"></a><a name="p44097393143435"></a><strong id="b1184031127"><a name="b1184031127"></a><a name="b1184031127"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row61332223143435"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1854200143435"><a name="p1854200143435"></a><a name="p1854200143435"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p15972517143435"><a name="p15972517143435"></a><a name="p15972517143435"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p65896092182816"><a name="p65896092182816"></a><a name="p65896092182816"></a>Tag key. The key contains 36 Unicode characters at most and cannot be blank. It can contain only digits, letters, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    <tr id="row34131946143435"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p13224233143435"><a name="p13224233143435"></a><a name="p13224233143435"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p64529977143435"><a name="p64529977143435"></a><a name="p64529977143435"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p55413571182816"><a name="p55413571182816"></a><a name="p55413571182816"></a>Tag value. Each value contains 43 Unicode characters at most and can be an empty string. It can contain only digits, letters, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "tags": [
            {
                "key": "key1", 
                "value": "value1"
            }, 
            {
                "key": "key2", 
                "value": "value2"
            }
        ]
    }
    ```


## **Returned Value**<a name="section42637797161043"></a>

-   Normal

    **Table  4**  Return code for successful requests

    <a name="table47366596113822"></a><table><thead align="left"><tr id="row16575017113822"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p3591919113822"><a name="p3591919113822"></a><a name="p3591919113822"></a><strong id="b1230056238"><a name="b1230056238"></a><a name="b1230056238"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p22510062113822"><a name="p22510062113822"></a><a name="p22510062113822"></a><strong id="b1786624219"><a name="b1786624219"></a><a name="b1786624219"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1263974113822"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p35273032113822"><a name="p35273032113822"></a><a name="p35273032113822"></a>200</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p60003820113839"><a name="p60003820113839"></a><a name="p60003820113839"></a>OK</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    **Table  5**  Return code for failed requests

    <a name="table31052520113920"></a><table><thead align="left"><tr id="row42912532113920"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p10505615113920"><a name="p10505615113920"></a><a name="p10505615113920"></a><strong id="b1828760291"><a name="b1828760291"></a><a name="b1828760291"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p45648486113920"><a name="p45648486113920"></a><a name="p45648486113920"></a><strong id="b1553737722"><a name="b1553737722"></a><a name="b1553737722"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8183193113920"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p58858900113920"><a name="p58858900113920"></a><a name="p58858900113920"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p38508836113951"><a name="p38508836113951"></a><a name="p38508836113951"></a>Invalid tag.</p>
    </td>
    </tr>
    <tr id="row25574142113920"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p58239591113920"><a name="p58239591113920"></a><a name="p58239591113920"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p8590733113958"><a name="p8590733113958"></a><a name="p8590733113958"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row43859803113920"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p62983180113920"><a name="p62983180113920"></a><a name="p62983180113920"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p2321538211404"><a name="p2321538211404"></a><a name="p2321538211404"></a>You do not have permission to perform this operation.</p>
    </td>
    </tr>
    <tr id="row12275951113920"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p54827987113920"><a name="p54827987113920"></a><a name="p54827987113920"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p59477271114010"><a name="p59477271114010"></a><a name="p59477271114010"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="row39828478113920"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p4881294113920"><a name="p4881294113920"></a><a name="p4881294113920"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p52714557114015"><a name="p52714557114015"></a><a name="p52714557114015"></a>An exception occurs in the system.</p>
    </td>
    </tr>
    </tbody>
    </table>


