# Adding or Deleting Resource Tags in Batches<a name="EN-US_TOPIC_0094510675"></a>

## Function<a name="section2763065016101"></a>

Add or delete tags for a specified resource in batches.

Tag Management Service \(TMS\) may use this API to manage service resource tags.

You can add a maximum of 10 tags to a resource.

The API is idempotent.

-   When you are to create tags, if there are duplicate keys in the request body, an error is reported.

    If a to-be-created tag has the same key as an existing tag, the tag will be created and overwrite the existing one.

-   When tags are being deleted and some tags do not exist, the operation is considered successful by default. The character set of the tags will not be checked.

## URI<a name="section53701671161015"></a>

-   URI format

    POST /v2/\{resource\_type\}/\{resource\_id\}/tags/action

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

-   Parameter description

    **Table  2**  Parameters in the request

    <a name="table239794161830"></a><table><thead align="left"><tr id="row654560711830"><th class="cellrowborder" valign="top" width="19.251925192519252%" id="mcps1.2.5.1.1"><p id="p3415211830"><a name="p3415211830"></a><a name="p3415211830"></a><strong id="b162774213314533"><a name="b162774213314533"></a><a name="b162774213314533"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.23182318231823%" id="mcps1.2.5.1.2"><p id="p276632601830"><a name="p276632601830"></a><a name="p276632601830"></a><strong id="b53247500142936"><a name="b53247500142936"></a><a name="b53247500142936"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.151415141514152%" id="mcps1.2.5.1.3"><p id="p261316001830"><a name="p261316001830"></a><a name="p261316001830"></a><strong id="b84235270619112"><a name="b84235270619112"></a><a name="b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="48.36483648364836%" id="mcps1.2.5.1.4"><p id="p362848191830"><a name="p362848191830"></a><a name="p362848191830"></a><strong id="b842352706112423"><a name="b842352706112423"></a><a name="b842352706112423"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row533892641830"><td class="cellrowborder" valign="top" width="19.251925192519252%" headers="mcps1.2.5.1.1 "><p id="p13541101112236"><a name="p13541101112236"></a><a name="p13541101112236"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.23182318231823%" headers="mcps1.2.5.1.2 "><p id="p458022581830"><a name="p458022581830"></a><a name="p458022581830"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.151415141514152%" headers="mcps1.2.5.1.3 "><p id="p2132029112245"><a name="p2132029112245"></a><a name="p2132029112245"></a>List&lt;tag&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.36483648364836%" headers="mcps1.2.5.1.4 "><p id="p6613684112255"><a name="p6613684112255"></a><a name="p6613684112255"></a>Tag list. The tag list structure cannot be empty when you delete tags.</p>
    </td>
    </tr>
    <tr id="row232443661830"><td class="cellrowborder" valign="top" width="19.251925192519252%" headers="mcps1.2.5.1.1 "><p id="p2325915611235"><a name="p2325915611235"></a><a name="p2325915611235"></a>action</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.23182318231823%" headers="mcps1.2.5.1.2 "><p id="p349520711830"><a name="p349520711830"></a><a name="p349520711830"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.151415141514152%" headers="mcps1.2.5.1.3 "><p id="p125455181830"><a name="p125455181830"></a><a name="p125455181830"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.36483648364836%" headers="mcps1.2.5.1.4 "><p id="p11691022112319"><a name="p11691022112319"></a><a name="p11691022112319"></a>Operation, which can be <strong id="b842352706163653"><a name="b842352706163653"></a><a name="b842352706163653"></a>create</strong> or <strong id="b842352706163656"><a name="b842352706163656"></a><a name="b842352706163656"></a>delete</strong> (case sensitive)</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Parameters in the tag list

    <a name="table19530794112436"></a><table><thead align="left"><tr id="en-us_topic_0101702788_row15361836112436"><th class="cellrowborder" valign="top" width="22.36%" id="mcps1.2.5.1.1"><p id="en-us_topic_0101702788_p58707511112436"><a name="en-us_topic_0101702788_p58707511112436"></a><a name="en-us_topic_0101702788_p58707511112436"></a><strong id="b162774213314533_1"><a name="b162774213314533_1"></a><a name="b162774213314533_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15.21%" id="mcps1.2.5.1.2"><p id="en-us_topic_0101702788_p57687928112436"><a name="en-us_topic_0101702788_p57687928112436"></a><a name="en-us_topic_0101702788_p57687928112436"></a><strong id="b53247500142936_1"><a name="b53247500142936_1"></a><a name="b53247500142936_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.46%" id="mcps1.2.5.1.3"><p id="en-us_topic_0101702788_p42210623112436"><a name="en-us_topic_0101702788_p42210623112436"></a><a name="en-us_topic_0101702788_p42210623112436"></a><strong id="b84235270619112_1"><a name="b84235270619112_1"></a><a name="b84235270619112_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="45.97%" id="mcps1.2.5.1.4"><p id="en-us_topic_0101702788_p63617265112436"><a name="en-us_topic_0101702788_p63617265112436"></a><a name="en-us_topic_0101702788_p63617265112436"></a><strong id="b842352706112423_1"><a name="b842352706112423_1"></a><a name="b842352706112423_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0101702788_row35684479112436"><td class="cellrowborder" valign="top" width="22.36%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0101702788_p13313439112530"><a name="en-us_topic_0101702788_p13313439112530"></a><a name="en-us_topic_0101702788_p13313439112530"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.21%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0101702788_p50150432112436"><a name="en-us_topic_0101702788_p50150432112436"></a><a name="en-us_topic_0101702788_p50150432112436"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.46%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0101702788_p35653193112436"><a name="en-us_topic_0101702788_p35653193112436"></a><a name="en-us_topic_0101702788_p35653193112436"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.97%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0101702788_p48921437201850"><a name="en-us_topic_0101702788_p48921437201850"></a><a name="en-us_topic_0101702788_p48921437201850"></a>Tag key. The key cannot be left blank or be an empty string. It can contain only digits, letters, hyphens (-), and underscores (_).</p>
    <p id="p1005457710566"><a name="p1005457710566"></a><a name="p1005457710566"></a>When <strong id="b84235270693136"><a name="b84235270693136"></a><a name="b84235270693136"></a>action</strong> is set to <strong id="b84235270693142"><a name="b84235270693142"></a><a name="b84235270693142"></a>create</strong>, the key contains 36 Unicode characters at most.</p>
    <p id="p4459091710568"><a name="p4459091710568"></a><a name="p4459091710568"></a>When <strong id="b84235270693136_1"><a name="b84235270693136_1"></a><a name="b84235270693136_1"></a>action</strong> is set to <strong id="b84235270693142_1"><a name="b84235270693142_1"></a><a name="b84235270693142_1"></a>delete</strong>, the key contains 127 Unicode characters at most.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0101702788_row20048002112436"><td class="cellrowborder" valign="top" width="22.36%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0101702788_p66095544112533"><a name="en-us_topic_0101702788_p66095544112533"></a><a name="en-us_topic_0101702788_p66095544112533"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.21%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0101702788_p1570770112436"><a name="en-us_topic_0101702788_p1570770112436"></a><a name="en-us_topic_0101702788_p1570770112436"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.46%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0101702788_p60123528112436"><a name="en-us_topic_0101702788_p60123528112436"></a><a name="en-us_topic_0101702788_p60123528112436"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.97%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0101702788_p61714725112922"><a name="en-us_topic_0101702788_p61714725112922"></a><a name="en-us_topic_0101702788_p61714725112922"></a>Tag value, which can be an empty string. It can contain only digits, letters, hyphens (-), and underscores (_).</p>
    <p id="p29591721105842"><a name="p29591721105842"></a><a name="p29591721105842"></a>When <strong id="b842352706111733"><a name="b842352706111733"></a><a name="b842352706111733"></a>action</strong> is set to <strong id="b842352706111743"><a name="b842352706111743"></a><a name="b842352706111743"></a>create</strong>, the tag value is mandatory and contains 43 Unicode characters at most.</p>
    <p id="p64998902105842"><a name="p64998902105842"></a><a name="p64998902105842"></a>When <strong id="b1415673007112014"><a name="b1415673007112014"></a><a name="b1415673007112014"></a>action</strong> is set to <strong id="b1089647170112014"><a name="b1089647170112014"></a><a name="b1089647170112014"></a>delete</strong>, the tag value is optional and contains 255 Unicode characters. If you left it blank, tags are deleted by key.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    {
        "action": "create",
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
    or
    {
        "action": "delete",
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


## Response<a name="section40090803161031"></a>

None

## **Returned Value**<a name="section42637797161043"></a>

-   Normal

    **Table  4**  Return code for successful requests

    <a name="table47366596113822"></a><table><thead align="left"><tr id="row16575017113822"><th class="cellrowborder" valign="top" width="32.519999999999996%" id="mcps1.2.3.1.1"><p id="p3591919113822"><a name="p3591919113822"></a><a name="p3591919113822"></a><strong id="b8423527069424_1"><a name="b8423527069424_1"></a><a name="b8423527069424_1"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="67.47999999999999%" id="mcps1.2.3.1.2"><p id="p22510062113822"><a name="p22510062113822"></a><a name="p22510062113822"></a><strong id="b842352706112423_2"><a name="b842352706112423_2"></a><a name="b842352706112423_2"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1263974113822"><td class="cellrowborder" valign="top" width="32.519999999999996%" headers="mcps1.2.3.1.1 "><p id="p35273032113822"><a name="p35273032113822"></a><a name="p35273032113822"></a>204</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.47999999999999%" headers="mcps1.2.3.1.2 "><p id="p60003820113839"><a name="p60003820113839"></a><a name="p60003820113839"></a>No content.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    **Table  5**  Return code for failed requests

    <a name="table31052520113920"></a><table><thead align="left"><tr id="row42912532113920"><th class="cellrowborder" valign="top" width="32.89%" id="mcps1.2.3.1.1"><p id="p10505615113920"><a name="p10505615113920"></a><a name="p10505615113920"></a><strong id="b8423527069424_2"><a name="b8423527069424_2"></a><a name="b8423527069424_2"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="67.11%" id="mcps1.2.3.1.2"><p id="p45648486113920"><a name="p45648486113920"></a><a name="p45648486113920"></a><strong id="b842352706112423_3"><a name="b842352706112423_3"></a><a name="b842352706112423_3"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8183193113920"><td class="cellrowborder" valign="top" width="32.89%" headers="mcps1.2.3.1.1 "><p id="p58858900113920"><a name="p58858900113920"></a><a name="p58858900113920"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.11%" headers="mcps1.2.3.1.2 "><p id="p38508836113951"><a name="p38508836113951"></a><a name="p38508836113951"></a>Invalid action.</p>
    </td>
    </tr>
    <tr id="row25574142113920"><td class="cellrowborder" valign="top" width="32.89%" headers="mcps1.2.3.1.1 "><p id="p58239591113920"><a name="p58239591113920"></a><a name="p58239591113920"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.11%" headers="mcps1.2.3.1.2 "><p id="p8590733113958"><a name="p8590733113958"></a><a name="p8590733113958"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row43859803113920"><td class="cellrowborder" valign="top" width="32.89%" headers="mcps1.2.3.1.1 "><p id="p62983180113920"><a name="p62983180113920"></a><a name="p62983180113920"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.11%" headers="mcps1.2.3.1.2 "><p id="p2321538211404"><a name="p2321538211404"></a><a name="p2321538211404"></a>You do not have permission to perform this operation.</p>
    </td>
    </tr>
    <tr id="row12275951113920"><td class="cellrowborder" valign="top" width="32.89%" headers="mcps1.2.3.1.1 "><p id="p54827987113920"><a name="p54827987113920"></a><a name="p54827987113920"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.11%" headers="mcps1.2.3.1.2 "><p id="p59477271114010"><a name="p59477271114010"></a><a name="p59477271114010"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="row39828478113920"><td class="cellrowborder" valign="top" width="32.89%" headers="mcps1.2.3.1.1 "><p id="p4881294113920"><a name="p4881294113920"></a><a name="p4881294113920"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.11%" headers="mcps1.2.3.1.2 "><p id="p52714557114015"><a name="p52714557114015"></a><a name="p52714557114015"></a>An exception occurs in the system.</p>
    </td>
    </tr>
    </tbody>
    </table>


