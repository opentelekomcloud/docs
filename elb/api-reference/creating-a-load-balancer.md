# Creating a Load Balancer<a name="EN-US_TOPIC_0096561499"></a>

## Function<a name="en-us_topic_0020100178_section58605492"></a>

This API is used to create a load balancer.

## URI<a name="en-us_topic_0020100178_section57687380"></a>

POST /v1.0/\{project\_id\}/elbaas/loadbalancers

**Table  1**  Parameter description

<a name="en-us_topic_0020100178_table1264194815326"></a>
<table><thead align="left"><tr id="en-us_topic_0020100178_row1071104816322"><th class="cellrowborder" valign="top" width="17.171717171717173%" id="mcps1.2.5.1.1"><p id="en-us_topic_0020100178_p10731248113213"><a name="en-us_topic_0020100178_p10731248113213"></a><a name="en-us_topic_0020100178_p10731248113213"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.171717171717173%" id="mcps1.2.5.1.2"><p id="en-us_topic_0020100178_p37584818329"><a name="en-us_topic_0020100178_p37584818329"></a><a name="en-us_topic_0020100178_p37584818329"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15.151515151515152%" id="mcps1.2.5.1.3"><p id="en-us_topic_0020100178_p1378154873218"><a name="en-us_topic_0020100178_p1378154873218"></a><a name="en-us_topic_0020100178_p1378154873218"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50.505050505050505%" id="mcps1.2.5.1.4"><p id="en-us_topic_0020100178_p1580134812328"><a name="en-us_topic_0020100178_p1580134812328"></a><a name="en-us_topic_0020100178_p1580134812328"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0020100178_row1884144813327"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100178_p11336155310138"><a name="en-us_topic_0020100178_p11336155310138"></a><a name="en-us_topic_0020100178_p11336155310138"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100178_p190194815329"><a name="en-us_topic_0020100178_p190194815329"></a><a name="en-us_topic_0020100178_p190194815329"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100178_p1991124812322"><a name="en-us_topic_0020100178_p1991124812322"></a><a name="en-us_topic_0020100178_p1991124812322"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.505050505050505%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020100178_p39412487322"><a name="en-us_topic_0020100178_p39412487322"></a><a name="en-us_topic_0020100178_p39412487322"></a>Specifies the project ID of the operator.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0020100178_section1793623903417"></a>

-   Request parameters

    **Table  2**  Request parameters

    <a name="en-us_topic_0020100178_table10126151233715"></a>
    <table><thead align="left"><tr id="en-us_topic_0020100178_row17136161263712"><th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.1"><p id="en-us_topic_0020100178_p191381312193715"><a name="en-us_topic_0020100178_p191381312193715"></a><a name="en-us_topic_0020100178_p191381312193715"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0020100178_p1214141263711"><a name="en-us_topic_0020100178_p1214141263711"></a><a name="en-us_topic_0020100178_p1214141263711"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0020100178_p71439129377"><a name="en-us_topic_0020100178_p71439129377"></a><a name="en-us_topic_0020100178_p71439129377"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53%" id="mcps1.2.5.1.4"><p id="en-us_topic_0020100178_p1914651223712"><a name="en-us_topic_0020100178_p1914651223712"></a><a name="en-us_topic_0020100178_p1914651223712"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0020100178_row11641212153716"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100178_p5167121263712"><a name="en-us_topic_0020100178_p5167121263712"></a><a name="en-us_topic_0020100178_p5167121263712"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100178_p1016911263718"><a name="en-us_topic_0020100178_p1016911263718"></a><a name="en-us_topic_0020100178_p1016911263718"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100178_p1917311243716"><a name="en-us_topic_0020100178_p1917311243716"></a><a name="en-us_topic_0020100178_p1917311243716"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100178_ul151751412173717"></a><a name="en-us_topic_0020100178_ul151751412173717"></a><ul id="en-us_topic_0020100178_ul151751412173717"><li>Specifies the load balancer name.</li><li>The value is a string of 1 to 64 characters that consist of Chinese characters, letters, digits, underscores (_), and hyphens (-).</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0020100178_row4183112153712"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100178_p111859124375"><a name="en-us_topic_0020100178_p111859124375"></a><a name="en-us_topic_0020100178_p111859124375"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100178_p171891112153717"><a name="en-us_topic_0020100178_p171891112153717"></a><a name="en-us_topic_0020100178_p171891112153717"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100178_p9191181217373"><a name="en-us_topic_0020100178_p9191181217373"></a><a name="en-us_topic_0020100178_p9191181217373"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100178_ul21941212163720"></a><a name="en-us_topic_0020100178_ul21941212163720"></a><ul id="en-us_topic_0020100178_ul21941212163720"><li>Provides supplementary information about the load balancer.</li><li>The value contains 0 to 128 characters and cannot contain angle brackets (&lt; and &gt;).</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0020100178_row17201121219376"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100178_p1204412113711"><a name="en-us_topic_0020100178_p1204412113711"></a><a name="en-us_topic_0020100178_p1204412113711"></a>vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100178_p16206131213373"><a name="en-us_topic_0020100178_p16206131213373"></a><a name="en-us_topic_0020100178_p16206131213373"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100178_p1920919129374"><a name="en-us_topic_0020100178_p1920919129374"></a><a name="en-us_topic_0020100178_p1920919129374"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020100178_p021211129372"><a name="en-us_topic_0020100178_p021211129372"></a><a name="en-us_topic_0020100178_p021211129372"></a>Specifies the VPC ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100178_row112131612113718"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100178_p121711293716"><a name="en-us_topic_0020100178_p121711293716"></a><a name="en-us_topic_0020100178_p121711293716"></a>bandwidth</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100178_p162195129373"><a name="en-us_topic_0020100178_p162195129373"></a><a name="en-us_topic_0020100178_p162195129373"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100178_p20221181220372"><a name="en-us_topic_0020100178_p20221181220372"></a><a name="en-us_topic_0020100178_p20221181220372"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100178_ul9226161220375"></a><a name="en-us_topic_0020100178_ul9226161220375"></a><ul id="en-us_topic_0020100178_ul9226161220375"><li>Specifies the bandwidth (Mbit/s). This parameter is mandatory when <strong id="en-us_topic_0020100178_b84235270614519"><a name="en-us_topic_0020100178_b84235270614519"></a><a name="en-us_topic_0020100178_b84235270614519"></a>type</strong> is set to <strong id="en-us_topic_0020100178_b842352706145112"><a name="en-us_topic_0020100178_b842352706145112"></a><a name="en-us_topic_0020100178_b842352706145112"></a>External</strong>.</li><li>The value ranges from <strong id="b105794319816"><a name="b105794319816"></a><a name="b105794319816"></a>1</strong> to <strong id="b125901562083"><a name="b125901562083"></a><a name="b125901562083"></a>500</strong>.<p id="en-us_topic_0020100178_p116594145716"><a name="en-us_topic_0020100178_p116594145716"></a><a name="en-us_topic_0020100178_p116594145716"></a>(The specific range may vary depending on the configuration in each region. You can see the bandwidth range of each region on the management console.)</p>
    </li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0020100178_row1523613121374"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100178_p13239112143716"><a name="en-us_topic_0020100178_p13239112143716"></a><a name="en-us_topic_0020100178_p13239112143716"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100178_p0242151213377"><a name="en-us_topic_0020100178_p0242151213377"></a><a name="en-us_topic_0020100178_p0242151213377"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100178_p10246111212375"><a name="en-us_topic_0020100178_p10246111212375"></a><a name="en-us_topic_0020100178_p10246111212375"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100178_ul1324912120372"></a><a name="en-us_topic_0020100178_ul1324912120372"></a><ul id="en-us_topic_0020100178_ul1324912120372"><li>Specifies the network type of the load balancer.</li><li>The value is <strong id="en-us_topic_0020100178_b62038661201538"><a name="en-us_topic_0020100178_b62038661201538"></a><a name="en-us_topic_0020100178_b62038661201538"></a>Internal</strong> or <strong id="en-us_topic_0020100178_b21477043201538"><a name="en-us_topic_0020100178_b21477043201538"></a><a name="en-us_topic_0020100178_b21477043201538"></a>External</strong>.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0020100178_row5257191253719"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100178_p7260612163710"><a name="en-us_topic_0020100178_p7260612163710"></a><a name="en-us_topic_0020100178_p7260612163710"></a>admin_state_up</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100178_p2263161215375"><a name="en-us_topic_0020100178_p2263161215375"></a><a name="en-us_topic_0020100178_p2263161215375"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100178_p11266161216375"><a name="en-us_topic_0020100178_p11266161216375"></a><a name="en-us_topic_0020100178_p11266161216375"></a>Integer/Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100178_ul127141218371"></a><a name="en-us_topic_0020100178_ul127141218371"></a><ul id="en-us_topic_0020100178_ul127141218371"><li>Specifies the administrative status of the load balancer.</li><li>Optional values:<p id="en-us_topic_0020100178_p1327921211377"><a name="en-us_topic_0020100178_p1327921211377"></a><a name="en-us_topic_0020100178_p1327921211377"></a><strong id="en-us_topic_0020100178_b842352706162920"><a name="en-us_topic_0020100178_b842352706162920"></a><a name="en-us_topic_0020100178_b842352706162920"></a>0</strong> or <strong id="en-us_topic_0020100178_b842352706162916"><a name="en-us_topic_0020100178_b842352706162916"></a><a name="en-us_topic_0020100178_b842352706162916"></a>false</strong>: indicates that the load balancer is stopped. Only tenants are allowed to enter the two values. </p>
    <p id="en-us_topic_0020100178_p3280612113710"><a name="en-us_topic_0020100178_p3280612113710"></a><a name="en-us_topic_0020100178_p3280612113710"></a><strong id="en-us_topic_0020100178_b842352706163138"><a name="en-us_topic_0020100178_b842352706163138"></a><a name="en-us_topic_0020100178_b842352706163138"></a>1</strong> or <strong id="en-us_topic_0020100178_b842352706163141"><a name="en-us_topic_0020100178_b842352706163141"></a><a name="en-us_topic_0020100178_b842352706163141"></a>true</strong>: indicates that the load balancer is running properly.</p>
    <p id="en-us_topic_0020100178_p19282212203713"><a name="en-us_topic_0020100178_p19282212203713"></a><a name="en-us_topic_0020100178_p19282212203713"></a><strong id="en-us_topic_0020100178_b842352706163213"><a name="en-us_topic_0020100178_b842352706163213"></a><a name="en-us_topic_0020100178_b842352706163213"></a>2</strong> or <strong id="en-us_topic_0020100178_b842352706163217"><a name="en-us_topic_0020100178_b842352706163217"></a><a name="en-us_topic_0020100178_b842352706163217"></a>false</strong>: indicates that the load balancer is frozen. Only the administrator is allowed to enter the two values. </p>
    </li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0020100178_row1528371283717"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100178_p92861612173717"><a name="en-us_topic_0020100178_p92861612173717"></a><a name="en-us_topic_0020100178_p92861612173717"></a>vip_subnet_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100178_p928813129373"><a name="en-us_topic_0020100178_p928813129373"></a><a name="en-us_topic_0020100178_p928813129373"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100178_p132915126372"><a name="en-us_topic_0020100178_p132915126372"></a><a name="en-us_topic_0020100178_p132915126372"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020100178_p929615120375"><a name="en-us_topic_0020100178_p929615120375"></a><a name="en-us_topic_0020100178_p929615120375"></a>Specifies the subnet ID of backend ECSs. This parameter is mandatory when <strong id="en-us_topic_0020100178_b475684332145828"><a name="en-us_topic_0020100178_b475684332145828"></a><a name="en-us_topic_0020100178_b475684332145828"></a>type</strong> is set to <strong id="en-us_topic_0020100178_b321259615145828"><a name="en-us_topic_0020100178_b321259615145828"></a><a name="en-us_topic_0020100178_b321259615145828"></a>Internal</strong>. Only IPv4 subnets can be specified.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100178_row122971312123711"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100178_p2299191217371"><a name="en-us_topic_0020100178_p2299191217371"></a><a name="en-us_topic_0020100178_p2299191217371"></a>az</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100178_p103035124378"><a name="en-us_topic_0020100178_p103035124378"></a><a name="en-us_topic_0020100178_p103035124378"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100178_p1930414121371"><a name="en-us_topic_0020100178_p1930414121371"></a><a name="en-us_topic_0020100178_p1930414121371"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020100178_p60687211154523"><a name="en-us_topic_0020100178_p60687211154523"></a><a name="en-us_topic_0020100178_p60687211154523"></a>Specifies the AZ where the load balancer works. This parameter is valid when <strong id="b842352706181626"><a name="b842352706181626"></a><a name="b842352706181626"></a>type</strong> is set to <strong id="b842352706181630"><a name="b842352706181630"></a><a name="b842352706181630"></a>Internal</strong>. If <strong id="b842352706181659"><a name="b842352706181659"></a><a name="b842352706181659"></a>type</strong> is set to <strong id="b84235270618171"><a name="b84235270618171"></a><a name="b84235270618171"></a>Internal</strong> and an AZ is specified, the specified AZ must support private network load balancers. Otherwise, an error message is returned. </p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100178_row0322141263714"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100178_p113241312103711"><a name="en-us_topic_0020100178_p113241312103711"></a><a name="en-us_topic_0020100178_p113241312103711"></a>charge_mode</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100178_p6328712153715"><a name="en-us_topic_0020100178_p6328712153715"></a><a name="en-us_topic_0020100178_p6328712153715"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100178_p532912124378"><a name="en-us_topic_0020100178_p532912124378"></a><a name="en-us_topic_0020100178_p532912124378"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100178_ul0333191243716"></a><a name="en-us_topic_0020100178_ul0333191243716"></a><ul id="en-us_topic_0020100178_ul0333191243716"><li>Specifies how a new elastic IP address (EIP) is billed. This is a reserved parameter. If the system supports billing by traffic and this parameter is specified, the EIP will be billed by traffic.</li><li>Specifies whether the EIP is billed by traffic or fixed bandwidth. If this parameter is left blank or incorrectly set, the EIP is billed by traffic by default.</li><li>The value is <strong id="en-us_topic_0020100178_b842352706102437"><a name="en-us_topic_0020100178_b842352706102437"></a><a name="en-us_topic_0020100178_b842352706102437"></a>traffic</strong>. </li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0020100178_row13347712193710"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100178_p1434911216374"><a name="en-us_topic_0020100178_p1434911216374"></a><a name="en-us_topic_0020100178_p1434911216374"></a>eip_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100178_p1335531211375"><a name="en-us_topic_0020100178_p1335531211375"></a><a name="en-us_topic_0020100178_p1335531211375"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100178_p1035981210372"><a name="en-us_topic_0020100178_p1035981210372"></a><a name="en-us_topic_0020100178_p1035981210372"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100178_ul173613124379"></a><a name="en-us_topic_0020100178_ul173613124379"></a><ul id="en-us_topic_0020100178_ul173613124379"><li>This parameter is reserved. </li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0020100178_row3378212193714"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100178_p1638171293712"><a name="en-us_topic_0020100178_p1638171293712"></a><a name="en-us_topic_0020100178_p1638171293712"></a>security_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100178_p7386112123714"><a name="en-us_topic_0020100178_p7386112123714"></a><a name="en-us_topic_0020100178_p7386112123714"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100178_p1438941210375"><a name="en-us_topic_0020100178_p1438941210375"></a><a name="en-us_topic_0020100178_p1438941210375"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100178_ul139213129372"></a><a name="en-us_topic_0020100178_ul139213129372"></a><ul id="en-us_topic_0020100178_ul139213129372"><li>Specifies the security group ID. </li><li>The value is a string of 1 to 200 characters that consists of uppercase and lowercase letters, digits, and hyphens (-).</li><li>This parameter is mandatory if the value of <strong id="b1096785210508"><a name="b1096785210508"></a><a name="b1096785210508"></a>type</strong> is <strong id="en-us_topic_0020100178_b842352706183122"><a name="en-us_topic_0020100178_b842352706183122"></a><a name="en-us_topic_0020100178_b842352706183122"></a>Internal</strong>, while it is ignored when the value of <strong id="b5472945175015"><a name="b5472945175015"></a><a name="b5472945175015"></a>type</strong> is <strong id="en-us_topic_0020100178_b842352706183226"><a name="en-us_topic_0020100178_b842352706183226"></a><a name="en-us_topic_0020100178_b842352706183226"></a>External</strong>.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0020100178_row140131293712"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100178_p184038120374"><a name="en-us_topic_0020100178_p184038120374"></a><a name="en-us_topic_0020100178_p184038120374"></a>vip_address</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100178_p19407412163710"><a name="en-us_topic_0020100178_p19407412163710"></a><a name="en-us_topic_0020100178_p19407412163710"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100178_p11410101283718"><a name="en-us_topic_0020100178_p11410101283718"></a><a name="en-us_topic_0020100178_p11410101283718"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100178_ul154121312153716"></a><a name="en-us_topic_0020100178_ul154121312153716"></a><ul id="en-us_topic_0020100178_ul154121312153716"><li>Specifies the private IP address of the load balancer. When <strong id="en-us_topic_0020100178_b372029376135217"><a name="en-us_topic_0020100178_b372029376135217"></a><a name="en-us_topic_0020100178_b372029376135217"></a>type</strong> is set to <strong id="en-us_topic_0020100178_b372029376135219"><a name="en-us_topic_0020100178_b372029376135219"></a><a name="en-us_topic_0020100178_b372029376135219"></a>External</strong>, the parameter value is the EIP. When <strong id="en-us_topic_0020100178_b199361158313535"><a name="en-us_topic_0020100178_b199361158313535"></a><a name="en-us_topic_0020100178_b199361158313535"></a>type</strong> is set to <strong id="en-us_topic_0020100178_b101664784913535"><a name="en-us_topic_0020100178_b101664784913535"></a><a name="en-us_topic_0020100178_b101664784913535"></a>Internal</strong>, the parameter value is the private network IP address.</li><li>You can select an existing EIP to create a public network load balancer. When this parameter is configured, parameters <strong id="en-us_topic_0020100178_b84235270612361"><a name="en-us_topic_0020100178_b84235270612361"></a><a name="en-us_topic_0020100178_b84235270612361"></a>bandwidth</strong>, <strong id="en-us_topic_0020100178_b84235270612368"><a name="en-us_topic_0020100178_b84235270612368"></a><a name="en-us_topic_0020100178_b84235270612368"></a>charge_mode</strong>, and <strong id="en-us_topic_0020100178_b842352706123617"><a name="en-us_topic_0020100178_b842352706123617"></a><a name="en-us_topic_0020100178_b842352706123617"></a>eip_type</strong> are invalid.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0020100178_row7422191223720"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100178_p64267126371"><a name="en-us_topic_0020100178_p64267126371"></a><a name="en-us_topic_0020100178_p64267126371"></a>tenantId</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100178_p1542831293718"><a name="en-us_topic_0020100178_p1542831293718"></a><a name="en-us_topic_0020100178_p1542831293718"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100178_p16431121220375"><a name="en-us_topic_0020100178_p16431121220375"></a><a name="en-us_topic_0020100178_p16431121220375"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100178_ul1043411283720"></a><a name="en-us_topic_0020100178_ul1043411283720"></a><ul id="en-us_topic_0020100178_ul1043411283720"><li>Specifies the project ID.</li><li>This parameter is mandatory when <strong id="en-us_topic_0020100178_b84235270616465"><a name="en-us_topic_0020100178_b84235270616465"></a><a name="en-us_topic_0020100178_b84235270616465"></a>type</strong> is set to <strong id="en-us_topic_0020100178_b842352706164610"><a name="en-us_topic_0020100178_b842352706164610"></a><a name="en-us_topic_0020100178_b842352706164610"></a>Internal</strong>.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request 1

    ```
    {
        "name": "loadbalancer1",
        "description": "simple lb",
        "vpc_id": "f54a3ffd-7a55-4568-9e3d-f0ff2d46a107",
        "bandwidth": 200,
        "type": "External",
        "admin_state_up": true
    }
    ```


-   Example request 2

    ```
    {
        "name": "loadbalancer1",
        "description": "simple lb",
        "vpc_id": "f54a3ffd-7a55-4568-9e3d-f0ff2d46a107",
        "vip_address": "192.144.164.74",
        "type": "External",
        "admin_state_up": true
    }
    ```


## Response<a name="en-us_topic_0020100178_section42166233"></a>

-   Response parameters

    **Table  3**  Response parameters

    <a name="en-us_topic_0020100178_table36506827154359"></a>
    <table><thead align="left"><tr id="en-us_topic_0020100178_row52456621154359"><th class="cellrowborder" valign="top" width="13.131313131313133%" id="mcps1.2.4.1.1"><p id="en-us_topic_0020100178_p21127946154359"><a name="en-us_topic_0020100178_p21127946154359"></a><a name="en-us_topic_0020100178_p21127946154359"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="25.252525252525253%" id="mcps1.2.4.1.2"><p id="en-us_topic_0020100178_p2757358517366"><a name="en-us_topic_0020100178_p2757358517366"></a><a name="en-us_topic_0020100178_p2757358517366"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="61.61616161616161%" id="mcps1.2.4.1.3"><p id="en-us_topic_0020100178_p40651916154359"><a name="en-us_topic_0020100178_p40651916154359"></a><a name="en-us_topic_0020100178_p40651916154359"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0020100178_row4470914154359"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100178_p26599760154359"><a name="en-us_topic_0020100178_p26599760154359"></a><a name="en-us_topic_0020100178_p26599760154359"></a>uri</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100178_p5190825317366"><a name="en-us_topic_0020100178_p5190825317366"></a><a name="en-us_topic_0020100178_p5190825317366"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.61616161616161%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100178_p37985431154359"><a name="en-us_topic_0020100178_p37985431154359"></a><a name="en-us_topic_0020100178_p37985431154359"></a>Specifies the URI returned by Combined API after the job for creating a load balancer is issued.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100178_row6324561154359"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100178_p42527448154359"><a name="en-us_topic_0020100178_p42527448154359"></a><a name="en-us_topic_0020100178_p42527448154359"></a>job_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100178_p5882648417366"><a name="en-us_topic_0020100178_p5882648417366"></a><a name="en-us_topic_0020100178_p5882648417366"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.61616161616161%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100178_p51044228154359"><a name="en-us_topic_0020100178_p51044228154359"></a><a name="en-us_topic_0020100178_p51044228154359"></a>Specifies the unique job ID in Combined API.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "uri": "/v1/73cd9140bec7427ab9952b4ed75924e0/jobs/4010b39b4fbb4645014fcfc8f2d178d1",
        "job_id": "4010b39b4fbb4645014fcfc8f2d178d1"
    }
    ```


## Status Code<a name="en-us_topic_0020100178_section43951783"></a>

-   Normal

    200

-   Abnormal

    <a name="en-us_topic_0020100178_table26444277"></a>
    <table><thead align="left"><tr id="en-us_topic_0020100178_row19065136"><th class="cellrowborder" valign="top" width="15%" id="mcps1.1.4.1.1"><p id="en-us_topic_0020100178_p772170"><a name="en-us_topic_0020100178_p772170"></a><a name="en-us_topic_0020100178_p772170"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="21%" id="mcps1.1.4.1.2"><p id="p15957631192911"><a name="p15957631192911"></a><a name="p15957631192911"></a>Message</p>
    </th>
    <th class="cellrowborder" valign="top" width="64%" id="mcps1.1.4.1.3"><p id="en-us_topic_0020100178_p62545829"><a name="en-us_topic_0020100178_p62545829"></a><a name="en-us_topic_0020100178_p62545829"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0020100178_row33047401"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100178_p59593788"><a name="en-us_topic_0020100178_p59593788"></a><a name="en-us_topic_0020100178_p59593788"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.4.1.2 "><p id="p475423296"><a name="p475423296"></a><a name="p475423296"></a>badRequest</p>
    </td>
    <td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100178_p62367561"><a name="en-us_topic_0020100178_p62367561"></a><a name="en-us_topic_0020100178_p62367561"></a>Request error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100178_row24437140"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100178_p33251304"><a name="en-us_topic_0020100178_p33251304"></a><a name="en-us_topic_0020100178_p33251304"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.4.1.2 "><p id="p147542132919"><a name="p147542132919"></a><a name="p147542132919"></a>unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100178_p9001097"><a name="en-us_topic_0020100178_p9001097"></a><a name="en-us_topic_0020100178_p9001097"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100178_row13901009"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100178_p52239951"><a name="en-us_topic_0020100178_p52239951"></a><a name="en-us_topic_0020100178_p52239951"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.4.1.2 "><p id="p1771242172919"><a name="p1771242172919"></a><a name="p1771242172919"></a>userDisabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100178_p3577678"><a name="en-us_topic_0020100178_p3577678"></a><a name="en-us_topic_0020100178_p3577678"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100178_row6655870215929"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100178_p2254579915929"><a name="en-us_topic_0020100178_p2254579915929"></a><a name="en-us_topic_0020100178_p2254579915929"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.4.1.2 "><p id="p167542122915"><a name="p167542122915"></a><a name="p167542122915"></a>Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100178_p1427040015929"><a name="en-us_topic_0020100178_p1427040015929"></a><a name="en-us_topic_0020100178_p1427040015929"></a>The requested page does not exist.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100178_row32199110"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100178_p57991080"><a name="en-us_topic_0020100178_p57991080"></a><a name="en-us_topic_0020100178_p57991080"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.4.1.2 "><p id="p175429294"><a name="p175429294"></a><a name="p175429294"></a>authFault</p>
    </td>
    <td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100178_p66765919"><a name="en-us_topic_0020100178_p66765919"></a><a name="en-us_topic_0020100178_p66765919"></a>System error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100178_row64022366"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100178_p18429167"><a name="en-us_topic_0020100178_p18429167"></a><a name="en-us_topic_0020100178_p18429167"></a>503</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.4.1.2 "><p id="p2081842192913"><a name="p2081842192913"></a><a name="p2081842192913"></a>serviceUnavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100178_p16367560"><a name="en-us_topic_0020100178_p16367560"></a><a name="en-us_topic_0020100178_p16367560"></a>The service is unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


