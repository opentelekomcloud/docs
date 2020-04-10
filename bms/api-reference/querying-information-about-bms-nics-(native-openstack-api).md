# Querying Information About BMS NICs \(Native OpenStack API\)<a name="EN-US_TOPIC_0053158678"></a>

## Function<a name="section36073588"></a>

This API is used to query information about BMS NICs, such as the MAC addresses and private IP addresses.

## URI<a name="section56226836"></a>

GET /v2.1/\{project\_id\}/servers/\{server\_id\}/os-interface

[Table 1](#table132771041114617)  lists the parameters.

**Table  1**  Parameter description

<a name="table132771041114617"></a>
<table><thead align="left"><tr id="row8277114114465"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p27097356"><a name="p27097356"></a><a name="p27097356"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p47402253"><a name="p47402253"></a><a name="p47402253"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p14377323"><a name="p14377323"></a><a name="p14377323"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row17277041134613"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p41666396"><a name="p41666396"></a><a name="p41666396"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p19534911"><a name="p19534911"></a><a name="p19534911"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p38823967"><a name="p38823967"></a><a name="p38823967"></a>Specifies the project ID.</p>
<p id="p9141450142010"><a name="p9141450142010"></a><a name="p9141450142010"></a>For how to obtain the project ID, see <a href="https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328009.html" target="_blank" rel="noopener noreferrer">Obtaining Required Information</a>.</p>
</td>
</tr>
<tr id="row1127715418461"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p6481999114812"><a name="p6481999114812"></a><a name="p6481999114812"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p55279920114812"><a name="p55279920114812"></a><a name="p55279920114812"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p48488537114812"><a name="p48488537114812"></a><a name="p48488537114812"></a>Specifies the <span id="text184810181544"><a name="text184810181544"></a><a name="text184810181544"></a>BMS</span><span id="text12848418745"><a name="text12848418745"></a><a name="text12848418745"></a></span> ID.</p>
<p id="p29791113277"><a name="p29791113277"></a><a name="p29791113277"></a>You can obtain the BMS ID from the <span id="en-us_topic_0113746489_text013014803615"><a name="en-us_topic_0113746489_text013014803615"></a><a name="en-us_topic_0113746489_text013014803615"></a>BMS</span><span id="en-us_topic_0113746489_text10131448133612"><a name="en-us_topic_0113746489_text10131448133612"></a><a name="en-us_topic_0113746489_text10131448133612"></a></span> console or using the <a href="querying-bmss-(native-openstack-api).md">Querying BMSs (Native OpenStack API)</a> API.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section36279478"></a>

-   Request parameters

    None

-   Example request

    ```
    GET https://{ECS Endpoint}/v2.1/c685484a8cc2416b97260938705deb65/servers/95bf2490-5428-432c-ad9b-5e3406f869dd/os-interface
    ```


## Response Message<a name="section58079852"></a>

-   Response parameters

    <a name="table25276401"></a>
    <table><thead align="left"><tr id="row30840926"><th class="cellrowborder" valign="top" width="28.799999999999997%" id="mcps1.1.4.1.1"><p id="p59978491115233"><a name="p59978491115233"></a><a name="p59978491115233"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="27.38%" id="mcps1.1.4.1.2"><p id="p26419641115233"><a name="p26419641115233"></a><a name="p26419641115233"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="43.82%" id="mcps1.1.4.1.3"><p id="p64181866115233"><a name="p64181866115233"></a><a name="p64181866115233"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row13119252"><td class="cellrowborder" valign="top" width="28.799999999999997%" headers="mcps1.1.4.1.1 "><p id="p56026474"><a name="p56026474"></a><a name="p56026474"></a>interfaceAttachments</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.38%" headers="mcps1.1.4.1.2 "><p id="p34453949"><a name="p34453949"></a><a name="p34453949"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.82%" headers="mcps1.1.4.1.3 "><p id="p18214233"><a name="p18214233"></a><a name="p18214233"></a>Specifies information about NICs of the <span id="text81510245413"><a name="text81510245413"></a><a name="text81510245413"></a>BMS</span><span id="text111516241643"><a name="text111516241643"></a><a name="text111516241643"></a></span>. For details, see <a href="#table49805933">Table 2</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2** **interfaceAttachments**  field data structure description

    <a name="table49805933"></a>
    <table><thead align="left"><tr id="row9026257"><th class="cellrowborder" valign="top" width="28.799999999999997%" id="mcps1.2.4.1.1"><p id="p1725119981520"><a name="p1725119981520"></a><a name="p1725119981520"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="27.38%" id="mcps1.2.4.1.2"><p id="p1725215901512"><a name="p1725215901512"></a><a name="p1725215901512"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="43.82%" id="mcps1.2.4.1.3"><p id="p1325513931517"><a name="p1325513931517"></a><a name="p1325513931517"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row10727144"><td class="cellrowborder" valign="top" width="28.799999999999997%" headers="mcps1.2.4.1.1 "><p id="p63592346"><a name="p63592346"></a><a name="p63592346"></a>port_state</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.38%" headers="mcps1.2.4.1.2 "><p id="p13579756"><a name="p13579756"></a><a name="p13579756"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.82%" headers="mcps1.2.4.1.3 "><p id="p34639550"><a name="p34639550"></a><a name="p34639550"></a>Specifies the status of the NIC port. The value can be <strong id="b878875920166"><a name="b878875920166"></a><a name="b878875920166"></a>ACTIVE</strong>, <strong id="b179681926170"><a name="b179681926170"></a><a name="b179681926170"></a>BUILD</strong>, or <strong id="b108261064171"><a name="b108261064171"></a><a name="b108261064171"></a>DOWN</strong>.</p>
    </td>
    </tr>
    <tr id="row43320496"><td class="cellrowborder" valign="top" width="28.799999999999997%" headers="mcps1.2.4.1.1 "><p id="p19299281"><a name="p19299281"></a><a name="p19299281"></a>fixed_ips</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.38%" headers="mcps1.2.4.1.2 "><p id="p55265559"><a name="p55265559"></a><a name="p55265559"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.82%" headers="mcps1.2.4.1.3 "><p id="p23274750"><a name="p23274750"></a><a name="p23274750"></a>Specifies the NIC private IP address. For details, see <a href="#table19750463">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="row8146160"><td class="cellrowborder" valign="top" width="28.799999999999997%" headers="mcps1.2.4.1.1 "><p id="p55859239"><a name="p55859239"></a><a name="p55859239"></a>net_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.38%" headers="mcps1.2.4.1.2 "><p id="p10966323"><a name="p10966323"></a><a name="p10966323"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.82%" headers="mcps1.2.4.1.3 "><p id="p8495130"><a name="p8495130"></a><a name="p8495130"></a>Specifies the ID of the subnet (<strong id="b1150020102175"><a name="b1150020102175"></a><a name="b1150020102175"></a>network_id</strong>) to which the NIC ports belong.</p>
    </td>
    </tr>
    <tr id="row9347313"><td class="cellrowborder" valign="top" width="28.799999999999997%" headers="mcps1.2.4.1.1 "><p id="p18934887"><a name="p18934887"></a><a name="p18934887"></a>port_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.38%" headers="mcps1.2.4.1.2 "><p id="p13287175"><a name="p13287175"></a><a name="p13287175"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.82%" headers="mcps1.2.4.1.3 "><p id="p22674843"><a name="p22674843"></a><a name="p22674843"></a>Specifies the ID of the NIC port.</p>
    </td>
    </tr>
    <tr id="row2747002"><td class="cellrowborder" valign="top" width="28.799999999999997%" headers="mcps1.2.4.1.1 "><p id="p21180630"><a name="p21180630"></a><a name="p21180630"></a>mac_addr</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.38%" headers="mcps1.2.4.1.2 "><p id="p50770908"><a name="p50770908"></a><a name="p50770908"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.82%" headers="mcps1.2.4.1.3 "><p id="p35008393"><a name="p35008393"></a><a name="p35008393"></a>Specifies the MAC address of the NIC.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **fixed\_ips**  field data structure description

    <a name="table19750463"></a>
    <table><thead align="left"><tr id="row60761195"><th class="cellrowborder" valign="top" width="29.18%" id="mcps1.2.4.1.1"><p id="p1975316192155"><a name="p1975316192155"></a><a name="p1975316192155"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="27.589999999999996%" id="mcps1.2.4.1.2"><p id="p9754171910158"><a name="p9754171910158"></a><a name="p9754171910158"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="43.230000000000004%" id="mcps1.2.4.1.3"><p id="p17562199153"><a name="p17562199153"></a><a name="p17562199153"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row61624137"><td class="cellrowborder" valign="top" width="29.18%" headers="mcps1.2.4.1.1 "><p id="p25499238"><a name="p25499238"></a><a name="p25499238"></a>subnet_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.589999999999996%" headers="mcps1.2.4.1.2 "><p id="p65213800"><a name="p65213800"></a><a name="p65213800"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.230000000000004%" headers="mcps1.2.4.1.3 "><p id="p27784979"><a name="p27784979"></a><a name="p27784979"></a>Specifies the ID of the subnet (<strong id="b1673012142176"><a name="b1673012142176"></a><a name="b1673012142176"></a>subnet_id</strong>) corresponding to the private IP address of the NIC.</p>
    </td>
    </tr>
    <tr id="row48738220"><td class="cellrowborder" valign="top" width="29.18%" headers="mcps1.2.4.1.1 "><p id="p55481787"><a name="p55481787"></a><a name="p55481787"></a>ip_address</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.589999999999996%" headers="mcps1.2.4.1.2 "><p id="p17532027"><a name="p17532027"></a><a name="p17532027"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.230000000000004%" headers="mcps1.2.4.1.3 "><p id="p30163672"><a name="p30163672"></a><a name="p30163672"></a>Specifies the NIC private IP address.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "interfaceAttachments": [
            {
                "port_state": "ACTIVE",
                "fixed_ips": [
                    {
                        "subnet_id": "f8a6e8f8-c2ec-497c-9f23-da9616de54ef",
                        "ip_address": "192.168.1.3"
                    }
                ],
                "net_id": "3cb9bc59-5699-4588-a4b1-b87f96708bc6",
                "port_id": "ce531f90-199f-48c0-816c-13e38010b442",
                "mac_addr": "fa:16:3e:4c:2c:30"
            }
        ]
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

