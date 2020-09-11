# Querying Details of a Backend Server<a name="EN-US_TOPIC_0096561555"></a>

## Function<a name="section3489469347"></a>

This API is used to query details about a backend server.

## URI<a name="section1926292013415"></a>

GET /v2.0/lbaas/pools/\{pool\_id\}/members/\{member\_id\}

**Table  1**  Parameter description

<a name="table1498425144"></a>
<table><thead align="left"><tr id="row1044204241416"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="p174464221419"><a name="p174464221419"></a><a name="p174464221419"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.2"><p id="p444124218140"><a name="p444124218140"></a><a name="p444124218140"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.3"><p id="p1644144231415"><a name="p1644144231415"></a><a name="p1644144231415"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="54%" id="mcps1.2.5.1.4"><p id="p644154211142"><a name="p644154211142"></a><a name="p644154211142"></a><strong id="b84235270681620"><a name="b84235270681620"></a><a name="b84235270681620"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row134684241415"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p1846742161412"><a name="p1846742161412"></a><a name="p1846742161412"></a>pool_id</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p1694481915147"><a name="p1694481915147"></a><a name="p1694481915147"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p172911640205310"><a name="p172911640205310"></a><a name="p172911640205310"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.5.1.4 "><p id="p16462042161417"><a name="p16462042161417"></a><a name="p16462042161417"></a>Specifies the ID of the backend server group.</p>
</td>
</tr>
<tr id="row184611422148"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p19468428144"><a name="p19468428144"></a><a name="p19468428144"></a>member_id</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p298351716532"><a name="p298351716532"></a><a name="p298351716532"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p6222842195313"><a name="p6222842195313"></a><a name="p6222842195313"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.5.1.4 "><p id="p946142141419"><a name="p946142141419"></a><a name="p946142141419"></a>Specifies the backend server ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0049139656_section51524015"></a>

None

## Response<a name="en-us_topic_0049139656_section61062956"></a>

**Table  2**  Response parameters

<a name="en-us_topic_0049139656_table63335993"></a>
<table><thead align="left"><tr id="en-us_topic_0049139656_row52988976"><th class="cellrowborder" valign="top" width="19%" id="mcps1.2.4.1.1"><p id="en-us_topic_0049139656_p64248638"><a name="en-us_topic_0049139656_p64248638"></a><a name="en-us_topic_0049139656_p64248638"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.4.1.2"><p id="en-us_topic_0049139656_p36757156"><a name="en-us_topic_0049139656_p36757156"></a><a name="en-us_topic_0049139656_p36757156"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.2.4.1.3"><p id="en-us_topic_0049139656_p41555354"><a name="en-us_topic_0049139656_p41555354"></a><a name="en-us_topic_0049139656_p41555354"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0049139656_row10540538"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0049139656_p48477267"><a name="en-us_topic_0049139656_p48477267"></a><a name="en-us_topic_0049139656_p48477267"></a>member</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0049139656_p34344524"><a name="en-us_topic_0049139656_p34344524"></a><a name="en-us_topic_0049139656_p34344524"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0049139656_p49965631"><a name="en-us_topic_0049139656_p49965631"></a><a name="en-us_topic_0049139656_p49965631"></a>Lists the backend servers. For details, see <a href="#table1080991113150">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **members**  parameter description

<a name="table1080991113150"></a>
<table><thead align="left"><tr id="en-us_topic_0096561556_row1215463171615"><th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.4.1.1"><p id="en-us_topic_0096561556_p1315410319169"><a name="en-us_topic_0096561556_p1315410319169"></a><a name="en-us_topic_0096561556_p1315410319169"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.4.1.2"><p id="en-us_topic_0096561556_p141541431101611"><a name="en-us_topic_0096561556_p141541431101611"></a><a name="en-us_topic_0096561556_p141541431101611"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="72%" id="mcps1.2.4.1.3"><p id="en-us_topic_0096561556_p2154153161615"><a name="en-us_topic_0096561556_p2154153161615"></a><a name="en-us_topic_0096561556_p2154153161615"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0096561556_row161541231151616"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561556_p71549319164"><a name="en-us_topic_0096561556_p71549319164"></a><a name="en-us_topic_0096561556_p71549319164"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561556_p937416199308"><a name="en-us_topic_0096561556_p937416199308"></a><a name="en-us_topic_0096561556_p937416199308"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561556_p6154231141610"><a name="en-us_topic_0096561556_p6154231141610"></a><a name="en-us_topic_0096561556_p6154231141610"></a>Specifies the backend server ID.</p>
</td>
</tr>
<tr id="en-us_topic_0096561556_row8154123119164"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561556_p2015420313169"><a name="en-us_topic_0096561556_p2015420313169"></a><a name="en-us_topic_0096561556_p2015420313169"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561556_p131565312169"><a name="en-us_topic_0096561556_p131565312169"></a><a name="en-us_topic_0096561556_p131565312169"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561556_p201561631141618"><a name="en-us_topic_0096561556_p201561631141618"></a><a name="en-us_topic_0096561556_p201561631141618"></a>Specifies the ID of the project where the backend server is used.</p>
<p id="en-us_topic_0096561556_p4289054517"><a name="en-us_topic_0096561556_p4289054517"></a><a name="en-us_topic_0096561556_p4289054517"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0096561556_row41561731101617"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561556_p2015683161617"><a name="en-us_topic_0096561556_p2015683161617"></a><a name="en-us_topic_0096561556_p2015683161617"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561556_p915643117163"><a name="en-us_topic_0096561556_p915643117163"></a><a name="en-us_topic_0096561556_p915643117163"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561556_p13156193151618"><a name="en-us_topic_0096561556_p13156193151618"></a><a name="en-us_topic_0096561556_p13156193151618"></a>Specifies the backend server name.</p>
<p id="en-us_topic_0096561556_p126641735112"><a name="en-us_topic_0096561556_p126641735112"></a><a name="en-us_topic_0096561556_p126641735112"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0096561556_row12156113141613"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561556_p215633112161"><a name="en-us_topic_0096561556_p215633112161"></a><a name="en-us_topic_0096561556_p215633112161"></a>address</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561556_p61561331181617"><a name="en-us_topic_0096561556_p61561331181617"></a><a name="en-us_topic_0096561556_p61561331181617"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561556_p2611194017408"><a name="en-us_topic_0096561556_p2611194017408"></a><a name="en-us_topic_0096561556_p2611194017408"></a>Specifies the private IP address of the backend server. This IP address must be in the subnet specified by <strong id="en-us_topic_0096561556_b17159113041919"><a name="en-us_topic_0096561556_b17159113041919"></a><a name="en-us_topic_0096561556_b17159113041919"></a>subnet_id</strong>.</p>
<p id="en-us_topic_0096561556_p18611164024019"><a name="en-us_topic_0096561556_p18611164024019"></a><a name="en-us_topic_0096561556_p18611164024019"></a>This parameter can be set only to the IP address of the primary NIC, for example, 192.168.3.11.</p>
<p id="en-us_topic_0096561556_p1314571145112"><a name="en-us_topic_0096561556_p1314571145112"></a><a name="en-us_topic_0096561556_p1314571145112"></a>The value contains a maximum of 64 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0096561556_row121562031101617"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561556_p1115653101620"><a name="en-us_topic_0096561556_p1115653101620"></a><a name="en-us_topic_0096561556_p1115653101620"></a>protocol_port</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561556_p111561631171619"><a name="en-us_topic_0096561556_p111561631171619"></a><a name="en-us_topic_0096561556_p111561631171619"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561556_p141561431161615"><a name="en-us_topic_0096561556_p141561431161615"></a><a name="en-us_topic_0096561556_p141561431161615"></a>Specifies the port used by the backend server. The port number ranges from 1 to 65535.</p>
</td>
</tr>
<tr id="en-us_topic_0096561556_row111561931111610"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561556_p171561231151617"><a name="en-us_topic_0096561556_p171561231151617"></a><a name="en-us_topic_0096561556_p171561231151617"></a>subnet_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561556_p1577372523116"><a name="en-us_topic_0096561556_p1577372523116"></a><a name="en-us_topic_0096561556_p1577372523116"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561556_p986015317414"><a name="en-us_topic_0096561556_p986015317414"></a><a name="en-us_topic_0096561556_p986015317414"></a>Specifies the ID of the subnet where the backend server works. The private IP address of the backend server is in this subnet.</p>
<p id="en-us_topic_0096561556_p88604374112"><a name="en-us_topic_0096561556_p88604374112"></a><a name="en-us_topic_0096561556_p88604374112"></a>IPv6 subnets are not supported.</p>
</td>
</tr>
<tr id="en-us_topic_0096561556_row111561331101617"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561556_p19156231141611"><a name="en-us_topic_0096561556_p19156231141611"></a><a name="en-us_topic_0096561556_p19156231141611"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561556_p1915603181610"><a name="en-us_topic_0096561556_p1915603181610"></a><a name="en-us_topic_0096561556_p1915603181610"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561556_p38145286413"><a name="en-us_topic_0096561556_p38145286413"></a><a name="en-us_topic_0096561556_p38145286413"></a>Specifies the administrative status of the backend server. The value can be <strong id="en-us_topic_0096561556_b1686217011263"><a name="en-us_topic_0096561556_b1686217011263"></a><a name="en-us_topic_0096561556_b1686217011263"></a>true</strong> or <strong id="en-us_topic_0096561556_b1886220182612"><a name="en-us_topic_0096561556_b1886220182612"></a><a name="en-us_topic_0096561556_b1886220182612"></a>false</strong>.</p>
<p id="en-us_topic_0096561556_p1881412814419"><a name="en-us_topic_0096561556_p1881412814419"></a><a name="en-us_topic_0096561556_p1881412814419"></a>Currently, the value can only be <strong id="en-us_topic_0096561556_b5251147172616"><a name="en-us_topic_0096561556_b5251147172616"></a><a name="en-us_topic_0096561556_b5251147172616"></a>true</strong>.</p>
<div class="note" id="en-us_topic_0096561556_note1873514247366"><a name="en-us_topic_0096561556_note1873514247366"></a><a name="en-us_topic_0096561556_note1873514247366"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0096561556_p1773662413613"><a name="en-us_topic_0096561556_p1773662413613"></a><a name="en-us_topic_0096561556_p1773662413613"></a>This parameter can be used during creation and update and its actual value depends on whether the backend server exists. If the backend server exists, the value is <strong id="en-us_topic_0096561556_b1772198369"><a name="en-us_topic_0096561556_b1772198369"></a><a name="en-us_topic_0096561556_b1772198369"></a>true</strong>. Otherwise, the value is <strong id="en-us_topic_0096561556_b2084725659"><a name="en-us_topic_0096561556_b2084725659"></a><a name="en-us_topic_0096561556_b2084725659"></a>false</strong>.</p>
</div></div>
</td>
</tr>
<tr id="en-us_topic_0096561556_row8156193116164"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561556_p171561931151617"><a name="en-us_topic_0096561556_p171561931151617"></a><a name="en-us_topic_0096561556_p171561931151617"></a>weight</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561556_p4156103110161"><a name="en-us_topic_0096561556_p4156103110161"></a><a name="en-us_topic_0096561556_p4156103110161"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561556_p8605175104117"><a name="en-us_topic_0096561556_p8605175104117"></a><a name="en-us_topic_0096561556_p8605175104117"></a>Specifies the backend server weight. The value ranges from <strong id="en-us_topic_0096561556_b736895210190"><a name="en-us_topic_0096561556_b736895210190"></a><a name="en-us_topic_0096561556_b736895210190"></a>0</strong> to <strong id="en-us_topic_0096561556_b10369135211196"><a name="en-us_topic_0096561556_b10369135211196"></a><a name="en-us_topic_0096561556_b10369135211196"></a>100</strong>.</p>
<p id="en-us_topic_0096561556_p1460555119418"><a name="en-us_topic_0096561556_p1460555119418"></a><a name="en-us_topic_0096561556_p1460555119418"></a>If the value is <strong id="en-us_topic_0096561556_b142577543194"><a name="en-us_topic_0096561556_b142577543194"></a><a name="en-us_topic_0096561556_b142577543194"></a>0</strong>, the backend server will not accept new requests. The default value is <strong id="en-us_topic_0096561556_b7720155541911"><a name="en-us_topic_0096561556_b7720155541911"></a><a name="en-us_topic_0096561556_b7720155541911"></a>1</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0096561556_row7156631161615"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561556_p31561031161610"><a name="en-us_topic_0096561556_p31561031161610"></a><a name="en-us_topic_0096561556_p31561031161610"></a>operating_status</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561556_p715663171614"><a name="en-us_topic_0096561556_p715663171614"></a><a name="en-us_topic_0096561556_p715663171614"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561556_p187109210289"><a name="en-us_topic_0096561556_p187109210289"></a><a name="en-us_topic_0096561556_p187109210289"></a>Specifies the health check result of the backend server. The value can be one of the following:</p>
<a name="en-us_topic_0096561556_ul1229315244282"></a><a name="en-us_topic_0096561556_ul1229315244282"></a><ul id="en-us_topic_0096561556_ul1229315244282"><li><strong id="en-us_topic_0096561556_b1785155722116"><a name="en-us_topic_0096561556_b1785155722116"></a><a name="en-us_topic_0096561556_b1785155722116"></a>ONLINE</strong>: The health check is successfully conducted and the backend server is running properly.</li><li><strong id="en-us_topic_0096561556_b1827011282210"><a name="en-us_topic_0096561556_b1827011282210"></a><a name="en-us_topic_0096561556_b1827011282210"></a>OFFLINE</strong>: The health check is abnormal and the backend server is running improperly. The load balancer stops distributing traffic to this server until it recovers.</li><li><strong id="en-us_topic_0096561556_b23251732215"><a name="en-us_topic_0096561556_b23251732215"></a><a name="en-us_topic_0096561556_b23251732215"></a>NO_MONITOR</strong>: No health check is conducted. No health checks are configured, or the value of <strong id="en-us_topic_0096561556_b18170131918319"><a name="en-us_topic_0096561556_b18170131918319"></a><a name="en-us_topic_0096561556_b18170131918319"></a>admin_state_up</strong> is <strong id="en-us_topic_0096561556_b074113410326"><a name="en-us_topic_0096561556_b074113410326"></a><a name="en-us_topic_0096561556_b074113410326"></a>false</strong>.</li><li>The value contains a maximum of 16 characters.</li></ul>
</td>
</tr>
</tbody>
</table>

## Example<a name="section1753633913395"></a>

-   Example request: Querying details of a backend server

    ```
    GET https://{Endpoint}/v2.0/lbaas/pools/5a9a3e9e-d1aa-448e-af37-a70171f2a332/members/cf024846-7516-4e3a-b0fb-6590322c836f
    ```


-   Example response

    ```
    {
        "member": {
            "name": "", 
            "weight": 1, 
            "admin_state_up": true, 
            "subnet_id": "823d5866-6e30-45c2-9b1a-a1ebc3757fdb", 
            "tenant_id": "145483a5107745e9b3d80f956713e6a3", 
     
            "address": "192.172.3.100", 
            "protocol_port": 8080, 
            "operating_status": "ONLINE", 
            "id": "e58f5bfa-0e46-4bc5-951c-8473d3e5f24a"
        }
    }
    ```


## Status Code<a name="en-us_topic_0049139655_section64643717"></a>

For details, see  [HTTP Status Codes for Enhanced Load Balancers](http-status-codes-for-enhanced-load-balancers.md).

