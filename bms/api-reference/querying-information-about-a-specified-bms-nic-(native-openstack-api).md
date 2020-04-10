# Querying Information About a Specified BMS NIC \(Native OpenStack API\)<a name="EN-US_TOPIC_0053158687"></a>

## Function<a name="section44739342"></a>

This API is used to query information about a specified BMS NIC based on the NIC ID.

## URI<a name="section901"></a>

GET /v2.1/\{project\_id\}/servers/\{server\_id\}/os-interface/\{id\}

[Table 1](#table1210415012480)  lists the parameters.

**Table  1**  Parameter description

<a name="table1210415012480"></a>
<table><thead align="left"><tr id="row110416020487"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p588929"><a name="p588929"></a><a name="p588929"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p47703261"><a name="p47703261"></a><a name="p47703261"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p38758958"><a name="p38758958"></a><a name="p38758958"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row51045024817"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p22044110"><a name="p22044110"></a><a name="p22044110"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p40742509"><a name="p40742509"></a><a name="p40742509"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p11808928"><a name="p11808928"></a><a name="p11808928"></a>Specifies the project ID.</p>
<p id="p9141450142010"><a name="p9141450142010"></a><a name="p9141450142010"></a>For how to obtain the project ID, see <a href="https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328009.html" target="_blank" rel="noopener noreferrer">Obtaining Required Information</a>.</p>
</td>
</tr>
<tr id="row610413044818"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p3575612917451"><a name="p3575612917451"></a><a name="p3575612917451"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1056536017451"><a name="p1056536017451"></a><a name="p1056536017451"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p5048782717451"><a name="p5048782717451"></a><a name="p5048782717451"></a>Specifies the <span id="text1054235953211"><a name="text1054235953211"></a><a name="text1054235953211"></a>BMS</span><span id="text1554255916321"><a name="text1554255916321"></a><a name="text1554255916321"></a></span> ID.</p>
<p id="p29791113277"><a name="p29791113277"></a><a name="p29791113277"></a>You can obtain the BMS ID from the <span id="en-us_topic_0113746489_text013014803615"><a name="en-us_topic_0113746489_text013014803615"></a><a name="en-us_topic_0113746489_text013014803615"></a>BMS</span><span id="en-us_topic_0113746489_text10131448133612"><a name="en-us_topic_0113746489_text10131448133612"></a><a name="en-us_topic_0113746489_text10131448133612"></a></span> console or using the <a href="querying-bmss-(native-openstack-api).md">Querying BMSs (Native OpenStack API)</a> API.</p>
</td>
</tr>
<tr id="row210616034814"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p18774354"><a name="p18774354"></a><a name="p18774354"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p44327687"><a name="p44327687"></a><a name="p44327687"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p33772909"><a name="p33772909"></a><a name="p33772909"></a>Specifies the ID of the NIC.</p>
<p id="p7979630184012"><a name="p7979630184012"></a><a name="p7979630184012"></a>You can obtain the NIC ID from the <strong id="b10816166172117"><a name="b10816166172117"></a><a name="b10816166172117"></a>NICs</strong> tab page on the <span id="text182199293316"><a name="text182199293316"></a><a name="text182199293316"></a>BMS</span><span id="text1621910223311"><a name="text1621910223311"></a><a name="text1621910223311"></a></span> details page or by calling the <a href="querying-information-about-bms-nics-(native-openstack-api).md">Querying Information About BMS NICs (Native OpenStack API)</a> API. (The NIC ID is the value of <strong id="b1348017565215"><a name="b1348017565215"></a><a name="b1348017565215"></a>port_id</strong>).</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section8117"></a>

-   Request parameters

    None

-   Example request

    ```
    GET https://{ECS Endpoint}/v2.1/c685484a8cc2416b97260938705deb65/servers/95bf2490-5428-432c-ad9b-5e3406f869dd/os-interface/ce531f90-199f-48c0-816c-13e38010b442
    ```


## Response Message<a name="section73053"></a>

-   Response parameters

    <a name="table59131099"></a>
    <table><thead align="left"><tr id="row30342446"><th class="cellrowborder" valign="top" width="25.97%" id="mcps1.1.4.1.1"><p id="p59978491115233"><a name="p59978491115233"></a><a name="p59978491115233"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="23.49%" id="mcps1.1.4.1.2"><p id="p26419641115233"><a name="p26419641115233"></a><a name="p26419641115233"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="50.54%" id="mcps1.1.4.1.3"><p id="p64181866115233"><a name="p64181866115233"></a><a name="p64181866115233"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row59560431"><td class="cellrowborder" valign="top" width="25.97%" headers="mcps1.1.4.1.1 "><p id="p59665636"><a name="p59665636"></a><a name="p59665636"></a>interfaceAttachment</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.49%" headers="mcps1.1.4.1.2 "><p id="p20239120"><a name="p20239120"></a><a name="p20239120"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.54%" headers="mcps1.1.4.1.3 "><p id="p57477322"><a name="p57477322"></a><a name="p57477322"></a>Specifies information about the specified <span id="text1983216693312"><a name="text1983216693312"></a><a name="text1983216693312"></a>BMS</span><span id="text78321066336"><a name="text78321066336"></a><a name="text78321066336"></a></span> NIC. For details, see <a href="#table24005299">Table 2</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2** **interfaceAttachment**  field data structure description

    <a name="table24005299"></a>
    <table><thead align="left"><tr id="row46441279"><th class="cellrowborder" valign="top" width="26.08%" id="mcps1.2.4.1.1"><p id="p7555195314159"><a name="p7555195314159"></a><a name="p7555195314159"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="23.599999999999998%" id="mcps1.2.4.1.2"><p id="p2558155381518"><a name="p2558155381518"></a><a name="p2558155381518"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="50.32%" id="mcps1.2.4.1.3"><p id="p1456215301510"><a name="p1456215301510"></a><a name="p1456215301510"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row64586077"><td class="cellrowborder" valign="top" width="26.08%" headers="mcps1.2.4.1.1 "><p id="p64089786"><a name="p64089786"></a><a name="p64089786"></a>port_state</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.599999999999998%" headers="mcps1.2.4.1.2 "><p id="p56055356"><a name="p56055356"></a><a name="p56055356"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.32%" headers="mcps1.2.4.1.3 "><p id="p62165703"><a name="p62165703"></a><a name="p62165703"></a>Specifies the status of the NIC port. The value can be <strong id="b117416109239"><a name="b117416109239"></a><a name="b117416109239"></a>ACTIVE</strong>, <strong id="b37510108234"><a name="b37510108234"></a><a name="b37510108234"></a>BUILD</strong>, or <strong id="b117615105233"><a name="b117615105233"></a><a name="b117615105233"></a>DOWN</strong>.</p>
    </td>
    </tr>
    <tr id="row22620416"><td class="cellrowborder" valign="top" width="26.08%" headers="mcps1.2.4.1.1 "><p id="p20314447"><a name="p20314447"></a><a name="p20314447"></a>fixed_ips</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.599999999999998%" headers="mcps1.2.4.1.2 "><p id="p4888719"><a name="p4888719"></a><a name="p4888719"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.32%" headers="mcps1.2.4.1.3 "><p id="p7106508"><a name="p7106508"></a><a name="p7106508"></a>Specifies the IP addresses of NICs. For details, see <a href="#table53180163">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="row63958576"><td class="cellrowborder" valign="top" width="26.08%" headers="mcps1.2.4.1.1 "><p id="p13262169"><a name="p13262169"></a><a name="p13262169"></a>net_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.599999999999998%" headers="mcps1.2.4.1.2 "><p id="p40009126"><a name="p40009126"></a><a name="p40009126"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.32%" headers="mcps1.2.4.1.3 "><p id="p41406050"><a name="p41406050"></a><a name="p41406050"></a>Specifies the ID of the subnet (<strong id="b1389971112239"><a name="b1389971112239"></a><a name="b1389971112239"></a>network_id</strong>) to which the NIC ports belong.</p>
    </td>
    </tr>
    <tr id="row37110132"><td class="cellrowborder" valign="top" width="26.08%" headers="mcps1.2.4.1.1 "><p id="p53130720"><a name="p53130720"></a><a name="p53130720"></a>port_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.599999999999998%" headers="mcps1.2.4.1.2 "><p id="p27217289"><a name="p27217289"></a><a name="p27217289"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.32%" headers="mcps1.2.4.1.3 "><p id="p44289360"><a name="p44289360"></a><a name="p44289360"></a>Specifies the ID of the NIC port.</p>
    </td>
    </tr>
    <tr id="row63059925"><td class="cellrowborder" valign="top" width="26.08%" headers="mcps1.2.4.1.1 "><p id="p7580267"><a name="p7580267"></a><a name="p7580267"></a>mac_addr</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.599999999999998%" headers="mcps1.2.4.1.2 "><p id="p6466753"><a name="p6466753"></a><a name="p6466753"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.32%" headers="mcps1.2.4.1.3 "><p id="p16643039"><a name="p16643039"></a><a name="p16643039"></a>Specifies the MAC address of the NIC.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **fixed\_ips**  field data structure description

    <a name="table53180163"></a>
    <table><thead align="left"><tr id="row34896342"><th class="cellrowborder" valign="top" width="26.150000000000002%" id="mcps1.2.4.1.1"><p id="p720221141617"><a name="p720221141617"></a><a name="p720221141617"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="23.66%" id="mcps1.2.4.1.2"><p id="p5203141181611"><a name="p5203141181611"></a><a name="p5203141181611"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="50.19%" id="mcps1.2.4.1.3"><p id="p9205011169"><a name="p9205011169"></a><a name="p9205011169"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row66523006"><td class="cellrowborder" valign="top" width="26.150000000000002%" headers="mcps1.2.4.1.1 "><p id="p64293480112230"><a name="p64293480112230"></a><a name="p64293480112230"></a>subnet_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.66%" headers="mcps1.2.4.1.2 "><p id="p40389402112230"><a name="p40389402112230"></a><a name="p40389402112230"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.19%" headers="mcps1.2.4.1.3 "><p id="p50192196112230"><a name="p50192196112230"></a><a name="p50192196112230"></a>Specifies the ID of the subnet (<strong id="b142571652315"><a name="b142571652315"></a><a name="b142571652315"></a>subnet_id</strong>) corresponding to the private IP address of the NIC.</p>
    </td>
    </tr>
    <tr id="row12592542"><td class="cellrowborder" valign="top" width="26.150000000000002%" headers="mcps1.2.4.1.1 "><p id="p15780700112230"><a name="p15780700112230"></a><a name="p15780700112230"></a>ip_address</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.66%" headers="mcps1.2.4.1.2 "><p id="p3168304112230"><a name="p3168304112230"></a><a name="p3168304112230"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.19%" headers="mcps1.2.4.1.3 "><p id="p27992537112230"><a name="p27992537112230"></a><a name="p27992537112230"></a>Specifies the NIC IP address.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "interfaceAttachment": {
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

