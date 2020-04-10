# Querying IP Addresses of a BMS \(Native OpenStack API\)<a name="EN-US_TOPIC_0053158696"></a>

## Function<a name="section53922917165259"></a>

This API is used to query private IP addresses of a BMS.

## Constraints<a name="section64211377173223"></a>

Pagination query is not supported.

## URI<a name="section51121191165259"></a>

GET /v2.1/\{project\_id\}/servers/\{server\_id\}/ips

[Table 1](#table1152617127395)  lists the parameters.

**Table  1**  Parameter description

<a name="table1152617127395"></a>
<table><thead align="left"><tr id="row195261122394"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p58268319165259"><a name="p58268319165259"></a><a name="p58268319165259"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p22113407165259"><a name="p22113407165259"></a><a name="p22113407165259"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p46355523165259"><a name="p46355523165259"></a><a name="p46355523165259"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row6528101219392"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1217433165259"><a name="p1217433165259"></a><a name="p1217433165259"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p31503226165259"><a name="p31503226165259"></a><a name="p31503226165259"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1624545165259"><a name="p1624545165259"></a><a name="p1624545165259"></a>Specifies the project ID.</p>
<p id="p9141450142010"><a name="p9141450142010"></a><a name="p9141450142010"></a>For how to obtain the project ID, see <a href="https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328009.html" target="_blank" rel="noopener noreferrer">Obtaining Required Information</a>.</p>
</td>
</tr>
<tr id="row8528101220397"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p43442641165259"><a name="p43442641165259"></a><a name="p43442641165259"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p29193009165259"><a name="p29193009165259"></a><a name="p29193009165259"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p15823538165259"><a name="p15823538165259"></a><a name="p15823538165259"></a>Specifies the <span id="text4562161113465"><a name="text4562161113465"></a><a name="text4562161113465"></a>BMS</span><span id="text2563211104613"><a name="text2563211104613"></a><a name="text2563211104613"></a></span> ID.</p>
<p id="p29791113277"><a name="p29791113277"></a><a name="p29791113277"></a>You can obtain the BMS ID from the <span id="en-us_topic_0113746489_text013014803615"><a name="en-us_topic_0113746489_text013014803615"></a><a name="en-us_topic_0113746489_text013014803615"></a>BMS</span><span id="en-us_topic_0113746489_text10131448133612"><a name="en-us_topic_0113746489_text10131448133612"></a><a name="en-us_topic_0113746489_text10131448133612"></a></span> console or using the <a href="querying-bmss-(native-openstack-api).md">Querying BMSs (Native OpenStack API)</a> API.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section8194118165259"></a>

-   Request parameters

    None

-   Example request

    ```
    GET https://{ECS Endpoint}/v2.1/c685484a8cc2416b97260938705deb65/servers/95bf2490-5428-432c-ad9b-5e3406f869dd/ips
    ```


## Response Message<a name="section58140617165259"></a>

-   Response parameters

    <a name="table53480673143936"></a>
    <table><thead align="left"><tr id="row28382388143936"><th class="cellrowborder" valign="top" width="24.8%" id="mcps1.1.4.1.1"><p id="p59978491115233"><a name="p59978491115233"></a><a name="p59978491115233"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.869999999999997%" id="mcps1.1.4.1.2"><p id="p26419641115233"><a name="p26419641115233"></a><a name="p26419641115233"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="52.33%" id="mcps1.1.4.1.3"><p id="p64181866115233"><a name="p64181866115233"></a><a name="p64181866115233"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8940324143936"><td class="cellrowborder" valign="top" width="24.8%" headers="mcps1.1.4.1.1 "><p id="p53077645143936"><a name="p53077645143936"></a><a name="p53077645143936"></a>addresses</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.869999999999997%" headers="mcps1.1.4.1.2 "><p id="p4322023143936"><a name="p4322023143936"></a><a name="p4322023143936"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.33%" headers="mcps1.1.4.1.3 "><p id="p36857741143936"><a name="p36857741143936"></a><a name="p36857741143936"></a>Specifies IP addresses of the <span id="text185671317174716"><a name="text185671317174716"></a><a name="text185671317174716"></a>BMS</span><span id="text10567111744715"><a name="text10567111744715"></a><a name="text10567111744715"></a></span>. For details, see <a href="#table56891490143956">Table 2</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2** **addresses**  parameter structure description

    <a name="table56891490143956"></a>
    <table><thead align="left"><tr id="row33903869143956"><th class="cellrowborder" valign="top" width="24.86%" id="mcps1.2.4.1.1"><p id="p9236182413102"><a name="p9236182413102"></a><a name="p9236182413102"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="23.51%" id="mcps1.2.4.1.2"><p id="p19238124121016"><a name="p19238124121016"></a><a name="p19238124121016"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="51.629999999999995%" id="mcps1.2.4.1.3"><p id="p52411424141017"><a name="p52411424141017"></a><a name="p52411424141017"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row33776430143956"><td class="cellrowborder" valign="top" width="24.86%" headers="mcps1.2.4.1.1 "><p id="p51536339143956"><a name="p51536339143956"></a><a name="p51536339143956"></a>VPC where the <span id="text58422614477"><a name="text58422614477"></a><a name="text58422614477"></a>BMS</span><span id="text10849265476"><a name="text10849265476"></a><a name="text10849265476"></a></span> is located</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.51%" headers="mcps1.2.4.1.2 "><p id="p13693953143956"><a name="p13693953143956"></a><a name="p13693953143956"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.629999999999995%" headers="mcps1.2.4.1.3 "><p id="p54366741143956"><a name="p54366741143956"></a><a name="p54366741143956"></a>Specifies the ID of the VPC where the <span id="text9198102174816"><a name="text9198102174816"></a><a name="text9198102174816"></a>BMS</span><span id="text161999215482"><a name="text161999215482"></a><a name="text161999215482"></a></span> is located. For details about the format, see <a href="#table22651992144025">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Network parameter structure description

    <a name="table22651992144025"></a>
    <table><thead align="left"><tr id="row15576094144025"><th class="cellrowborder" valign="top" width="25.41%" id="mcps1.2.4.1.1"><p id="p355273111016"><a name="p355273111016"></a><a name="p355273111016"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="23.419999999999998%" id="mcps1.2.4.1.2"><p id="p16554153131017"><a name="p16554153131017"></a><a name="p16554153131017"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="51.17%" id="mcps1.2.4.1.3"><p id="p055523151012"><a name="p055523151012"></a><a name="p055523151012"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1498246144025"><td class="cellrowborder" valign="top" width="25.41%" headers="mcps1.2.4.1.1 "><p id="p54249095144025"><a name="p54249095144025"></a><a name="p54249095144025"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.419999999999998%" headers="mcps1.2.4.1.2 "><p id="p32100540144025"><a name="p32100540144025"></a><a name="p32100540144025"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.17%" headers="mcps1.2.4.1.3 "><p id="p16571197144025"><a name="p16571197144025"></a><a name="p16571197144025"></a>Specifies the IP address version. The value can be:</p>
    <a name="ul1882101316162"></a><a name="ul1882101316162"></a><ul id="ul1882101316162"><li><strong id="b9297191175814"><a name="b9297191175814"></a><a name="b9297191175814"></a>4</strong>: IPv4 address</li><li><strong id="b17364111518584"><a name="b17364111518584"></a><a name="b17364111518584"></a>6</strong>: IPv6 address</li></ul>
    </td>
    </tr>
    <tr id="row14923052144025"><td class="cellrowborder" valign="top" width="25.41%" headers="mcps1.2.4.1.1 "><p id="p807709144025"><a name="p807709144025"></a><a name="p807709144025"></a>addr</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.419999999999998%" headers="mcps1.2.4.1.2 "><p id="p65424470144025"><a name="p65424470144025"></a><a name="p65424470144025"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.17%" headers="mcps1.2.4.1.3 "><p id="p39086769144025"><a name="p39086769144025"></a><a name="p39086769144025"></a>Specifies the IP address.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "addresses": {
            "08a7715f-7de6-4ff9-a343-95ba4209f24a": [
                {
                    "version": 4,
                    "addr": "192.168.2.90"
                }
            ]
        }
    }
    ```


## Returned Values<a name="section7610951"></a>

Normal values

<a name="en-us_topic_0106040941_table753804619176"></a>
<table><thead align="left"><tr id="en-us_topic_0106040941_row10735134615172"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="en-us_topic_0106040941_p19735204616177"><a name="en-us_topic_0106040941_p19735204616177"></a><a name="en-us_topic_0106040941_p19735204616177"></a>Returned Values</p>
</th>
<th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="en-us_topic_0106040941_p207355465176"><a name="en-us_topic_0106040941_p207355465176"></a><a name="en-us_topic_0106040941_p207355465176"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0106040941_row1473514621713"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0106040941_p13735144611178"><a name="en-us_topic_0106040941_p13735144611178"></a><a name="en-us_topic_0106040941_p13735144611178"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0106040941_p207351246161711"><a name="en-us_topic_0106040941_p207351246161711"></a><a name="en-us_topic_0106040941_p207351246161711"></a>The server has successfully processed the request.</p>
</td>
</tr>
</tbody>
</table>

For details about other returned values, see  [Status Codes](status-codes.md).

## Error Codes<a name="section14752650154917"></a>

See  [Error Codes](error-codes.md).

