# Unsetting a PTR Record<a name="EN-US_TOPIC_0042318616"></a>

## Function<a name="section8391370"></a>

Unset the PTR record to the original value.

## URI<a name="section8413469"></a>

-   URI format

    PATCH /v2/reverse/floatingips/\{region\}:\{floatingip\_id\}

    Parameter description

    **Table  1**  Parameters in the URI

    <a name="table48883615"></a><table><thead align="left"><tr id="en-us_topic_0042318613_row3442661918149"><th class="cellrowborder" valign="top" width="20.380000000000003%" id="mcps1.2.5.1.1"><p id="en-us_topic_0042318613_p3709279118149"><a name="en-us_topic_0042318613_p3709279118149"></a><a name="en-us_topic_0042318613_p3709279118149"></a><strong id="en-us_topic_0042318613_b162774213314533"><a name="en-us_topic_0042318613_b162774213314533"></a><a name="en-us_topic_0042318613_b162774213314533"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.439999999999998%" id="mcps1.2.5.1.2"><p id="en-us_topic_0042318613_p5172606218149"><a name="en-us_topic_0042318613_p5172606218149"></a><a name="en-us_topic_0042318613_p5172606218149"></a><strong id="en-us_topic_0042318613_b593421527191713"><a name="en-us_topic_0042318613_b593421527191713"></a><a name="en-us_topic_0042318613_b593421527191713"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="13.59%" id="mcps1.2.5.1.3"><p id="en-us_topic_0042318613_p2906151418149"><a name="en-us_topic_0042318613_p2906151418149"></a><a name="en-us_topic_0042318613_p2906151418149"></a><strong id="en-us_topic_0042318613_b84235270619112"><a name="en-us_topic_0042318613_b84235270619112"></a><a name="en-us_topic_0042318613_b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="46.589999999999996%" id="mcps1.2.5.1.4"><p id="en-us_topic_0042318613_p517246718149"><a name="en-us_topic_0042318613_p517246718149"></a><a name="en-us_topic_0042318613_p517246718149"></a><strong id="en-us_topic_0042318613_b842352706112423"><a name="en-us_topic_0042318613_b842352706112423"></a><a name="en-us_topic_0042318613_b842352706112423"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0042318613_row1631668818149"><td class="cellrowborder" valign="top" width="20.380000000000003%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0042318613_p4658337018149"><a name="en-us_topic_0042318613_p4658337018149"></a><a name="en-us_topic_0042318613_p4658337018149"></a>region</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.439999999999998%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0042318613_p1515661618149"><a name="en-us_topic_0042318613_p1515661618149"></a><a name="en-us_topic_0042318613_p1515661618149"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.59%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0042318613_p1972638718149"><a name="en-us_topic_0042318613_p1972638718149"></a><a name="en-us_topic_0042318613_p1972638718149"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.589999999999996%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0042318613_p5433349018149"><a name="en-us_topic_0042318613_p5433349018149"></a><a name="en-us_topic_0042318613_p5433349018149"></a>Region of the tenant</p>
    </td>
    </tr>
    <tr id="en-us_topic_0042318613_row1923936518149"><td class="cellrowborder" valign="top" width="20.380000000000003%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0042318613_p1488470218149"><a name="en-us_topic_0042318613_p1488470218149"></a><a name="en-us_topic_0042318613_p1488470218149"></a>floatingip_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.439999999999998%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0042318613_p6481017518149"><a name="en-us_topic_0042318613_p6481017518149"></a><a name="en-us_topic_0042318613_p6481017518149"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.59%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0042318613_p1513281718149"><a name="en-us_topic_0042318613_p1513281718149"></a><a name="en-us_topic_0042318613_p1513281718149"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.589999999999996%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0042318613_p1779865118149"><a name="en-us_topic_0042318613_p1779865118149"></a><a name="en-us_topic_0042318613_p1779865118149"></a>EIP ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section8612359"></a>

-   Parameter description

    **Table  2**  Parameter in the request

    <a name="table239794161830"></a><table><thead align="left"><tr id="row654560711830"><th class="cellrowborder" valign="top" width="20.757924207579244%" id="mcps1.2.5.1.1"><p id="p3415211830"><a name="p3415211830"></a><a name="p3415211830"></a><strong id="b162774213314533"><a name="b162774213314533"></a><a name="b162774213314533"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.987801219878016%" id="mcps1.2.5.1.2"><p id="p276632601830"><a name="p276632601830"></a><a name="p276632601830"></a><strong id="b593421527191713"><a name="b593421527191713"></a><a name="b593421527191713"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.71852814718528%" id="mcps1.2.5.1.3"><p id="p261316001830"><a name="p261316001830"></a><a name="p261316001830"></a><strong id="b84235270619112"><a name="b84235270619112"></a><a name="b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="42.53574642535746%" id="mcps1.2.5.1.4"><p id="p362848191830"><a name="p362848191830"></a><a name="p362848191830"></a><strong id="b842352706112423"><a name="b842352706112423"></a><a name="b842352706112423"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row533892641830"><td class="cellrowborder" valign="top" width="20.757924207579244%" headers="mcps1.2.5.1.1 "><p id="p295631171830"><a name="p295631171830"></a><a name="p295631171830"></a>ptrdname</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.987801219878016%" headers="mcps1.2.5.1.2 "><p id="p458022581830"><a name="p458022581830"></a><a name="p458022581830"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.71852814718528%" headers="mcps1.2.5.1.3 "><p id="p189954321830"><a name="p189954321830"></a><a name="p189954321830"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.53574642535746%" headers="mcps1.2.5.1.4 "><p id="p26704373161818"><a name="p26704373161818"></a><a name="p26704373161818"></a>Domain name of the PTR record</p>
    <p id="p622350301830"><a name="p622350301830"></a><a name="p622350301830"></a>Set it to <strong id="b842352706172057"><a name="b842352706172057"></a><a name="b842352706172057"></a>null</strong> in the request.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Request example

    ```
    {
        "ptrdname": null
    }
    ```


## Response<a name="section10402369"></a>

None

## **Returned Value**<a name="section26512460"></a>

See  [General Request Return Code](general-request-return-code.md).

