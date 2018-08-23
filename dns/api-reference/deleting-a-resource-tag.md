# Deleting a Resource Tag<a name="EN-US_TOPIC_0101709621"></a>

## Function<a name="section2763065016101"></a>

Delete a resource tag.

The API is idempotent.

When you delete a tag but it does not exist, the system reports that the tag does not exist.

## URI<a name="section53701671161015"></a>

-   URI format

    DELETE /v2/\{resource\_type\}/\{resource\_id\}/tags/\{key\}

-   Parameter description

    **Table  1**  Parameters in the URI

    <a name="table6099729418149"></a><table><thead align="left"><tr id="row3442661918149"><th class="cellrowborder" valign="top" width="20.380000000000003%" id="mcps1.2.5.1.1"><p id="p3709279118149"><a name="p3709279118149"></a><a name="p3709279118149"></a><strong id="b162774213314533"><a name="b162774213314533"></a><a name="b162774213314533"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.439999999999998%" id="mcps1.2.5.1.2"><p id="p5172606218149"><a name="p5172606218149"></a><a name="p5172606218149"></a><strong id="b593421527191713"><a name="b593421527191713"></a><a name="b593421527191713"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="13.59%" id="mcps1.2.5.1.3"><p id="p2906151418149"><a name="p2906151418149"></a><a name="p2906151418149"></a><strong id="b84235270619112"><a name="b84235270619112"></a><a name="b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="46.589999999999996%" id="mcps1.2.5.1.4"><p id="p517246718149"><a name="p517246718149"></a><a name="p517246718149"></a><strong id="b842352706112423"><a name="b842352706112423"></a><a name="b842352706112423"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1923936518149"><td class="cellrowborder" valign="top" width="20.380000000000003%" headers="mcps1.2.5.1.1 "><p id="p1488470218149"><a name="p1488470218149"></a><a name="p1488470218149"></a>resource_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.439999999999998%" headers="mcps1.2.5.1.2 "><p id="p6481017518149"><a name="p6481017518149"></a><a name="p6481017518149"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.59%" headers="mcps1.2.5.1.3 "><p id="p1513281718149"><a name="p1513281718149"></a><a name="p1513281718149"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.589999999999996%" headers="mcps1.2.5.1.4 "><p id="p1779865118149"><a name="p1779865118149"></a><a name="p1779865118149"></a>Resource type, which can be <strong id="b84235270610339"><a name="b84235270610339"></a><a name="b84235270610339"></a>DNS-public_zone</strong>&nbsp;or&nbsp;<strong id="b84235270610347"><a name="b84235270610347"></a><a name="b84235270610347"></a>DNS-public_recordset</strong></p>
    </td>
    </tr>
    <tr id="row1082100911220"><td class="cellrowborder" valign="top" width="20.380000000000003%" headers="mcps1.2.5.1.1 "><p id="p408654311220"><a name="p408654311220"></a><a name="p408654311220"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.439999999999998%" headers="mcps1.2.5.1.2 "><p id="p6257460611220"><a name="p6257460611220"></a><a name="p6257460611220"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.59%" headers="mcps1.2.5.1.3 "><p id="p3537835811220"><a name="p3537835811220"></a><a name="p3537835811220"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.589999999999996%" headers="mcps1.2.5.1.4 "><p id="p4707473411220"><a name="p4707473411220"></a><a name="p4707473411220"></a>Resource ID</p>
    </td>
    </tr>
    <tr id="row41443070202518"><td class="cellrowborder" valign="top" width="20.380000000000003%" headers="mcps1.2.5.1.1 "><p id="p16287090202522"><a name="p16287090202522"></a><a name="p16287090202522"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.439999999999998%" headers="mcps1.2.5.1.2 "><p id="p5844905202518"><a name="p5844905202518"></a><a name="p5844905202518"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.59%" headers="mcps1.2.5.1.3 "><p id="p3675282202518"><a name="p3675282202518"></a><a name="p3675282202518"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.589999999999996%" headers="mcps1.2.5.1.4 "><p id="p38832579202531"><a name="p38832579202531"></a><a name="p38832579202531"></a>Tag key</p>
    <p id="p1510133720226"><a name="p1510133720226"></a><a name="p1510133720226"></a>The key cannot be left blank or be an empty string.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section44958995161021"></a>

None

## Response<a name="section40090803161031"></a>

None

## **Returned Value**<a name="section42637797161043"></a>

-   Normal

    **Table  2**  Return code for successful requests

    <a name="table47366596113822"></a><table><thead align="left"><tr id="row16575017113822"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p3591919113822"><a name="p3591919113822"></a><a name="p3591919113822"></a><strong id="b8423527069424_1"><a name="b8423527069424_1"></a><a name="b8423527069424_1"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p22510062113822"><a name="p22510062113822"></a><a name="p22510062113822"></a><strong id="b842352706112423_1"><a name="b842352706112423_1"></a><a name="b842352706112423_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1263974113822"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p35273032113822"><a name="p35273032113822"></a><a name="p35273032113822"></a>204</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p60003820113839"><a name="p60003820113839"></a><a name="p60003820113839"></a>No content.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    **Table  3**  Return code for failed requests

    <a name="table31052520113920"></a><table><thead align="left"><tr id="row42912532113920"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p10505615113920"><a name="p10505615113920"></a><a name="p10505615113920"></a><strong id="b8423527069424_2"><a name="b8423527069424_2"></a><a name="b8423527069424_2"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p45648486113920"><a name="p45648486113920"></a><a name="p45648486113920"></a><strong id="b842352706112423_2"><a name="b842352706112423_2"></a><a name="b842352706112423_2"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8183193113920"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p58858900113920"><a name="p58858900113920"></a><a name="p58858900113920"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p38508836113951"><a name="p38508836113951"></a><a name="p38508836113951"></a>Invalid action.</p>
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


