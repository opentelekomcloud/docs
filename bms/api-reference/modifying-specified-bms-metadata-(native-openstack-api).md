# Modifying Specified BMS Metadata \(Native OpenStack API\)<a name="EN-US_TOPIC_0053158695"></a>

## Function<a name="section19950704192629"></a>

This API is used to modify specified BMS metadata.

## Constraints<a name="section48821040143631"></a>

The BMS  **OS-EXT-STS:vm\_state**  attribute \(BMS status\) must be  **active**,  **stopped**,  **paused**, or  **suspended**.

## URI<a name="section48549151192629"></a>

PUT /v2.1/\{project\_id\}/servers/\{server\_id\}/metadata/\{key\}

[Table 1](#table1370626163519)  lists the parameters.

**Table  1**  Parameter description

<a name="table1370626163519"></a>
<table><thead align="left"><tr id="row1708361352"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p11130554192629"><a name="p11130554192629"></a><a name="p11130554192629"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p29159654192629"><a name="p29159654192629"></a><a name="p29159654192629"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p13121799192629"><a name="p13121799192629"></a><a name="p13121799192629"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row17708565350"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p58565959192629"><a name="p58565959192629"></a><a name="p58565959192629"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p46222262192629"><a name="p46222262192629"></a><a name="p46222262192629"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p53015737192629"><a name="p53015737192629"></a><a name="p53015737192629"></a>Specifies the project ID.</p>
<p id="p9141450142010"><a name="p9141450142010"></a><a name="p9141450142010"></a>For how to obtain the project ID, see <a href="https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328009.html" target="_blank" rel="noopener noreferrer">Obtaining Required Information</a>.</p>
</td>
</tr>
<tr id="row137081065353"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p60875907192629"><a name="p60875907192629"></a><a name="p60875907192629"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p32001416192629"><a name="p32001416192629"></a><a name="p32001416192629"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p41977918192629"><a name="p41977918192629"></a><a name="p41977918192629"></a>Specifies the <span id="text92533163920"><a name="text92533163920"></a><a name="text92533163920"></a>BMS</span><span id="text1125517110395"><a name="text1125517110395"></a><a name="text1125517110395"></a></span> ID.</p>
<p id="p29791113277"><a name="p29791113277"></a><a name="p29791113277"></a>You can obtain the BMS ID from the <span id="en-us_topic_0113746489_text013014803615"><a name="en-us_topic_0113746489_text013014803615"></a><a name="en-us_topic_0113746489_text013014803615"></a>BMS</span><span id="en-us_topic_0113746489_text10131448133612"><a name="en-us_topic_0113746489_text10131448133612"></a><a name="en-us_topic_0113746489_text10131448133612"></a></span> console or using the <a href="querying-bmss-(native-openstack-api).md">Querying BMSs (Native OpenStack API)</a> API.</p>
</td>
</tr>
<tr id="row570816103517"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p2044590819279"><a name="p2044590819279"></a><a name="p2044590819279"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p4550582719279"><a name="p4550582719279"></a><a name="p4550582719279"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p6209335919279"><a name="p6209335919279"></a><a name="p6209335919279"></a>Specifies the <span id="text1279921102018"><a name="text1279921102018"></a><a name="text1279921102018"></a>BMS</span><span id="text11799017207"><a name="text11799017207"></a><a name="text11799017207"></a></span> metadata key value to be modified</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section42256947192629"></a>

-   Request parameters

    <a name="table21113531192629"></a>
    <table><thead align="left"><tr id="row12974012192629"><th class="cellrowborder" valign="top" width="17.2%" id="mcps1.1.5.1.1"><p id="p59978491115233"><a name="p59978491115233"></a><a name="p59978491115233"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.27%" id="mcps1.1.5.1.2"><p id="p87612353016"><a name="p87612353016"></a><a name="p87612353016"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.28%" id="mcps1.1.5.1.3"><p id="p26419641115233"><a name="p26419641115233"></a><a name="p26419641115233"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="41.25%" id="mcps1.1.5.1.4"><p id="p64181866115233"><a name="p64181866115233"></a><a name="p64181866115233"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8613312192629"><td class="cellrowborder" valign="top" width="17.2%" headers="mcps1.1.5.1.1 "><p id="p26589676192629"><a name="p26589676192629"></a><a name="p26589676192629"></a>meta</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.27%" headers="mcps1.1.5.1.2 "><p id="p57785097181826"><a name="p57785097181826"></a><a name="p57785097181826"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.28%" headers="mcps1.1.5.1.3 "><p id="p38929685192629"><a name="p38929685192629"></a><a name="p38929685192629"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.25%" headers="mcps1.1.5.1.4 "><p id="p59800316192629"><a name="p59800316192629"></a><a name="p59800316192629"></a>Specifies the user-defined metadata key and value pair. For details, see <a href="#table40778039192629">Table 2</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2** **meta**  field data structure description

    <a name="table40778039192629"></a>
    <table><thead align="left"><tr id="row63796811192629"><th class="cellrowborder" valign="top" width="17.810000000000002%" id="mcps1.2.5.1.1"><p id="p16744351100"><a name="p16744351100"></a><a name="p16744351100"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.759999999999998%" id="mcps1.2.5.1.2"><p id="p6539153311416"><a name="p6539153311416"></a><a name="p6539153311416"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="23.630000000000003%" id="mcps1.2.5.1.3"><p id="p14755351010"><a name="p14755351010"></a><a name="p14755351010"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="39.800000000000004%" id="mcps1.2.5.1.4"><p id="p47711354019"><a name="p47711354019"></a><a name="p47711354019"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row30326018192629"><td class="cellrowborder" valign="top" width="17.810000000000002%" headers="mcps1.2.5.1.1 "><p id="p40488404192629"><a name="p40488404192629"></a><a name="p40488404192629"></a>User-defined field key and value pair</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.759999999999998%" headers="mcps1.2.5.1.2 "><p id="p14539633743"><a name="p14539633743"></a><a name="p14539633743"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.630000000000003%" headers="mcps1.2.5.1.3 "><p id="p27540070192629"><a name="p27540070192629"></a><a name="p27540070192629"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.5.1.4 "><p id="p11161128192629"><a name="p11161128192629"></a><a name="p11161128192629"></a>Specifies the user-defined metadata key and value pair.</p>
    <a name="ul687584551016"></a><a name="ul687584551016"></a><ul id="ul687584551016"><li>The maximum size for each metadata key and value pair is 255 bytes.</li><li>The key does not support the following special characters:<p id="en-us_topic_0053158712_p104281244172319"><a name="en-us_topic_0053158712_p104281244172319"></a><a name="en-us_topic_0053158712_p104281244172319"></a>:`~!@#$%^&amp;*()=+&lt;,&gt;?/'";{[]}|\</p>
    </li><li>The value does not support the following special characters:<p id="en-us_topic_0053158712_p15830162842312"><a name="en-us_topic_0053158712_p15830162842312"></a><a name="en-us_topic_0053158712_p15830162842312"></a>\"</p>
    </li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    PUT https://{ECS Endpoint}/v2.1/c685484a8cc2416b97260938705deb65/servers/95bf2490-5428-432c-ad9b-5e3406f869dd/metadata/{key}
    ```

    ```
    {
        "meta": {
            "key": "value"
        }
    }
    ```


## Response Message<a name="section12391939192629"></a>

-   Response parameters

    <a name="table34681280192629"></a>
    <table><thead align="left"><tr id="row7754416192629"><th class="cellrowborder" valign="top" width="23.912391239123913%" id="mcps1.1.4.1.1"><p id="p053124814019"><a name="p053124814019"></a><a name="p053124814019"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="23.7023702370237%" id="mcps1.1.4.1.2"><p id="p165594820018"><a name="p165594820018"></a><a name="p165594820018"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="52.38523852385239%" id="mcps1.1.4.1.3"><p id="p958124812019"><a name="p958124812019"></a><a name="p958124812019"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row34495047192629"><td class="cellrowborder" valign="top" width="23.912391239123913%" headers="mcps1.1.4.1.1 "><p id="p42635402192629"><a name="p42635402192629"></a><a name="p42635402192629"></a>meta</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.7023702370237%" headers="mcps1.1.4.1.2 "><p id="p30915509192629"><a name="p30915509192629"></a><a name="p30915509192629"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.38523852385239%" headers="mcps1.1.4.1.3 "><p id="p55937021192629"><a name="p55937021192629"></a><a name="p55937021192629"></a>Specifies the user-defined metadata key and value pair. For details, see <a href="#table34604820192629">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **meta**  field data structure description

    <a name="table34604820192629"></a>
    <table><thead align="left"><tr id="row41672406192629"><th class="cellrowborder" valign="top" width="24.26%" id="mcps1.2.4.1.1"><p id="p168451154608"><a name="p168451154608"></a><a name="p168451154608"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="23.26%" id="mcps1.2.4.1.2"><p id="p158471654902"><a name="p158471654902"></a><a name="p158471654902"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="52.480000000000004%" id="mcps1.2.4.1.3"><p id="p6848125412010"><a name="p6848125412010"></a><a name="p6848125412010"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row64139640192629"><td class="cellrowborder" valign="top" width="24.26%" headers="mcps1.2.4.1.1 "><p id="p27928340192629"><a name="p27928340192629"></a><a name="p27928340192629"></a>User-defined field key and value pair</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.26%" headers="mcps1.2.4.1.2 "><p id="p47603028192629"><a name="p47603028192629"></a><a name="p47603028192629"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.480000000000004%" headers="mcps1.2.4.1.3 "><p id="p30640032192629"><a name="p30640032192629"></a><a name="p30640032192629"></a>Specifies the user-defined metadata key and value pair.</p>
    <p id="p16870474174442"><a name="p16870474174442"></a><a name="p16870474174442"></a>The maximum size for each metadata key and value pair is 255 bytes.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "meta": {
            "key": "value"
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

