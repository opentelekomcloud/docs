# Firewall Configuration Examples<a name="acl_0002"></a>

This section provides examples for configuring firewalls.

-   [Denying Access from a Specific Port](#section11312173319432)
-   [Allowing Access from Specific Ports and Protocols](#section61291659102216)

## Denying Access from a Specific Port<a name="section11312173319432"></a>

You might want to block TCP 445 to protect against the WannaCry ransomware attacks. You can add a firewall rule to deny all incoming traffic from TCP port 445.

**Firewall configuration**

[Table 1](#table553618145582)  lists the inbound rule required.

**Table  1**  Firewall rule

<a name="table553618145582"></a>
<table><thead align="left"><tr id="row1536191465810"><th class="cellrowborder" valign="top" width="9.000000000000002%" id="mcps1.2.9.1.1"><p id="p6536131425817"><a name="p6536131425817"></a><a name="p6536131425817"></a><strong id="b118251314859"><a name="b118251314859"></a><a name="b118251314859"></a>Direction</strong></p>
</th>
<th class="cellrowborder" valign="top" width="6.000000000000001%" id="mcps1.2.9.1.2"><p id="p1253641416587"><a name="p1253641416587"></a><a name="p1253641416587"></a><strong id="b187114616617"><a name="b187114616617"></a><a name="b187114616617"></a>Action</strong></p>
</th>
<th class="cellrowborder" valign="top" width="9.000000000000002%" id="mcps1.2.9.1.3"><p id="p5536171415817"><a name="p5536171415817"></a><a name="p5536171415817"></a><strong id="b1976385613"><a name="b1976385613"></a><a name="b1976385613"></a>Protocol</strong></p>
</th>
<th class="cellrowborder" valign="top" width="9.000000000000002%" id="mcps1.2.9.1.4"><p id="p853691455815"><a name="p853691455815"></a><a name="p853691455815"></a><strong id="b63477914611"><a name="b63477914611"></a><a name="b63477914611"></a>Source</strong></p>
</th>
<th class="cellrowborder" valign="top" width="12.000000000000002%" id="mcps1.2.9.1.5"><p id="p8536114165813"><a name="p8536114165813"></a><a name="p8536114165813"></a><strong id="b19670523366"><a name="b19670523366"></a><a name="b19670523366"></a>Source Port Range</strong></p>
</th>
<th class="cellrowborder" valign="top" width="18.000000000000004%" id="mcps1.2.9.1.6"><p id="p15536181495819"><a name="p15536181495819"></a><a name="p15536181495819"></a><strong id="b246520201615"><a name="b246520201615"></a><a name="b246520201615"></a>Destination</strong></p>
</th>
<th class="cellrowborder" valign="top" width="13.000000000000004%" id="mcps1.2.9.1.7"><p id="p135361214105818"><a name="p135361214105818"></a><a name="p135361214105818"></a><strong id="b1231942917613"><a name="b1231942917613"></a><a name="b1231942917613"></a>Destination Port Range</strong></p>
</th>
<th class="cellrowborder" valign="top" width="24.000000000000004%" id="mcps1.2.9.1.8"><p id="p85369147584"><a name="p85369147584"></a><a name="p85369147584"></a><strong id="b1638217306615"><a name="b1638217306615"></a><a name="b1638217306615"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row20536131455815"><td class="cellrowborder" valign="top" width="9.000000000000002%" headers="mcps1.2.9.1.1 "><p id="p175361814165817"><a name="p175361814165817"></a><a name="p175361814165817"></a>Inbound</p>
</td>
<td class="cellrowborder" valign="top" width="6.000000000000001%" headers="mcps1.2.9.1.2 "><p id="p1053616146583"><a name="p1053616146583"></a><a name="p1053616146583"></a>Deny</p>
</td>
<td class="cellrowborder" valign="top" width="9.000000000000002%" headers="mcps1.2.9.1.3 "><p id="p453651419586"><a name="p453651419586"></a><a name="p453651419586"></a>TCP</p>
</td>
<td class="cellrowborder" valign="top" width="9.000000000000002%" headers="mcps1.2.9.1.4 "><p id="p153691419583"><a name="p153691419583"></a><a name="p153691419583"></a>0.0.0.0/0</p>
</td>
<td class="cellrowborder" valign="top" width="12.000000000000002%" headers="mcps1.2.9.1.5 "><p id="p5536181412589"><a name="p5536181412589"></a><a name="p5536181412589"></a>1-65535</p>
</td>
<td class="cellrowborder" valign="top" width="18.000000000000004%" headers="mcps1.2.9.1.6 "><p id="p8536171495815"><a name="p8536171495815"></a><a name="p8536171495815"></a>0.0.0.0/0</p>
</td>
<td class="cellrowborder" valign="top" width="13.000000000000004%" headers="mcps1.2.9.1.7 "><p id="p65360144584"><a name="p65360144584"></a><a name="p65360144584"></a>445</p>
</td>
<td class="cellrowborder" valign="top" width="24.000000000000004%" headers="mcps1.2.9.1.8 "><p id="p13536614155813"><a name="p13536614155813"></a><a name="p13536614155813"></a>Denies inbound traffic from any IP address through TCP port 445.</p>
</td>
</tr>
</tbody>
</table>

## Allowing Access from Specific Ports and Protocols<a name="section61291659102216"></a>

In this example, an ECS in a subnet is used as the web server, and you need to allow inbound traffic from HTTP port 80 and HTTPS port 443 and allow all outbound traffic regardless of the port. You need to configure both the firewall rules and security group rules to allow the traffic.

**Firewall configuration**

[Table 2](#table195634095313)  lists the inbound and outbound firewall rules required.

**Table  2**  Firewall rule

<a name="table195634095313"></a>
<table><thead align="left"><tr id="row56214055319"><th class="cellrowborder" valign="top" width="8.91089108910891%" id="mcps1.2.9.1.1"><p id="p16212405538"><a name="p16212405538"></a><a name="p16212405538"></a><strong id="b1324725910194"><a name="b1324725910194"></a><a name="b1324725910194"></a>Direction</strong></p>
</th>
<th class="cellrowborder" valign="top" width="8.91089108910891%" id="mcps1.2.9.1.2"><p id="p1863340165319"><a name="p1863340165319"></a><a name="p1863340165319"></a><strong id="b131356012020"><a name="b131356012020"></a><a name="b131356012020"></a>Action</strong></p>
</th>
<th class="cellrowborder" valign="top" width="10.891089108910892%" id="mcps1.2.9.1.3"><p id="p10631640155318"><a name="p10631640155318"></a><a name="p10631640155318"></a><strong id="b223313112204"><a name="b223313112204"></a><a name="b223313112204"></a>Protocol</strong></p>
</th>
<th class="cellrowborder" valign="top" width="10.891089108910892%" id="mcps1.2.9.1.4"><p id="p66324013535"><a name="p66324013535"></a><a name="p66324013535"></a><strong id="b1656915916213"><a name="b1656915916213"></a><a name="b1656915916213"></a>Source</strong></p>
</th>
<th class="cellrowborder" valign="top" width="12.871287128712872%" id="mcps1.2.9.1.5"><p id="p1659407534"><a name="p1659407534"></a><a name="p1659407534"></a><strong id="b13983339192419"><a name="b13983339192419"></a><a name="b13983339192419"></a>Source Port Range</strong></p>
</th>
<th class="cellrowborder" valign="top" width="9.900990099009901%" id="mcps1.2.9.1.6"><p id="p56554075310"><a name="p56554075310"></a><a name="p56554075310"></a><strong id="b87684114247"><a name="b87684114247"></a><a name="b87684114247"></a>Destination</strong></p>
</th>
<th class="cellrowborder" valign="top" width="12.871287128712872%" id="mcps1.2.9.1.7"><p id="p106694013537"><a name="p106694013537"></a><a name="p106694013537"></a><strong id="b1720864232419"><a name="b1720864232419"></a><a name="b1720864232419"></a>Destination Port Range</strong></p>
</th>
<th class="cellrowborder" valign="top" width="24.752475247524753%" id="mcps1.2.9.1.8"><p id="p66717405533"><a name="p66717405533"></a><a name="p66717405533"></a><strong id="b113781445162411"><a name="b113781445162411"></a><a name="b113781445162411"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row196712405536"><td class="cellrowborder" valign="top" width="8.91089108910891%" headers="mcps1.2.9.1.1 "><p id="p069124055316"><a name="p069124055316"></a><a name="p069124055316"></a>Inbound</p>
</td>
<td class="cellrowborder" valign="top" width="8.91089108910891%" headers="mcps1.2.9.1.2 "><p id="p1670204016533"><a name="p1670204016533"></a><a name="p1670204016533"></a>Allow</p>
</td>
<td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.2.9.1.3 "><p id="p117112409536"><a name="p117112409536"></a><a name="p117112409536"></a>TCP</p>
</td>
<td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.2.9.1.4 "><p id="p10721240185320"><a name="p10721240185320"></a><a name="p10721240185320"></a>0.0.0.0/0</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.9.1.5 "><p id="p7742404539"><a name="p7742404539"></a><a name="p7742404539"></a>1-65535</p>
</td>
<td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.2.9.1.6 "><p id="p177484025315"><a name="p177484025315"></a><a name="p177484025315"></a>0.0.0.0/0</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.9.1.7 "><p id="p1211320362012"><a name="p1211320362012"></a><a name="p1211320362012"></a>80</p>
</td>
<td class="cellrowborder" valign="top" width="24.752475247524753%" headers="mcps1.2.9.1.8 "><p id="p3772407536"><a name="p3772407536"></a><a name="p3772407536"></a>Allows inbound HTTP traffic from any IP address to ECSs in the subnet through port 80.</p>
</td>
</tr>
<tr id="row160981135413"><td class="cellrowborder" valign="top" width="8.91089108910891%" headers="mcps1.2.9.1.1 "><p id="p11609119544"><a name="p11609119544"></a><a name="p11609119544"></a>Inbound</p>
</td>
<td class="cellrowborder" valign="top" width="8.91089108910891%" headers="mcps1.2.9.1.2 "><p id="p960910113543"><a name="p960910113543"></a><a name="p960910113543"></a>Allow</p>
</td>
<td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.2.9.1.3 "><p id="p96091313540"><a name="p96091313540"></a><a name="p96091313540"></a>TCP</p>
</td>
<td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.2.9.1.4 "><p id="p12609616544"><a name="p12609616544"></a><a name="p12609616544"></a>0.0.0.0/0</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.9.1.5 "><p id="p1760910165412"><a name="p1760910165412"></a><a name="p1760910165412"></a>1-65535</p>
</td>
<td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.2.9.1.6 "><p id="p136093175411"><a name="p136093175411"></a><a name="p136093175411"></a>0.0.0.0/0</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.9.1.7 "><p id="p9208174116114"><a name="p9208174116114"></a><a name="p9208174116114"></a>443</p>
</td>
<td class="cellrowborder" valign="top" width="24.752475247524753%" headers="mcps1.2.9.1.8 "><p id="p36241816183320"><a name="p36241816183320"></a><a name="p36241816183320"></a>Allows inbound HTTPS traffic from any IP address to ECSs in the subnet through port 443.</p>
</td>
</tr>
<tr id="row27210235717"><td class="cellrowborder" valign="top" width="8.91089108910891%" headers="mcps1.2.9.1.1 "><p id="p1372192105711"><a name="p1372192105711"></a><a name="p1372192105711"></a>Outbound</p>
</td>
<td class="cellrowborder" valign="top" width="8.91089108910891%" headers="mcps1.2.9.1.2 "><p id="p16721823575"><a name="p16721823575"></a><a name="p16721823575"></a>Allow</p>
</td>
<td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.2.9.1.3 "><p id="p1372192145710"><a name="p1372192145710"></a><a name="p1372192145710"></a>All</p>
</td>
<td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.2.9.1.4 "><p id="p204401137135716"><a name="p204401137135716"></a><a name="p204401137135716"></a>0.0.0.0/0</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.9.1.5 "><p id="p37211215719"><a name="p37211215719"></a><a name="p37211215719"></a>All</p>
</td>
<td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.2.9.1.6 "><p id="p99971040195713"><a name="p99971040195713"></a><a name="p99971040195713"></a>0.0.0.0/0</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.9.1.7 "><p id="p1972114217575"><a name="p1972114217575"></a><a name="p1972114217575"></a>All</p>
</td>
<td class="cellrowborder" valign="top" width="24.752475247524753%" headers="mcps1.2.9.1.8 "><p id="p207214210578"><a name="p207214210578"></a><a name="p207214210578"></a>Allow all outbound traffic from the subnet.</p>
</td>
</tr>
</tbody>
</table>

**Security group configuration**

[Table 3](#table30323767195135)  lists the inbound and outbound security group rules required.

**Table  3**  Security group rules

<a name="table30323767195135"></a>
<table><thead align="left"><tr id="row15770184195135"><th class="cellrowborder" valign="top" width="10%" id="mcps1.2.6.1.1"><p id="p1235112172119"><a name="p1235112172119"></a><a name="p1235112172119"></a><strong id="b15280238142814"><a name="b15280238142814"></a><a name="b15280238142814"></a>Direction</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.330000000000002%" id="mcps1.2.6.1.2"><p id="p2316559195135"><a name="p2316559195135"></a><a name="p2316559195135"></a><strong id="b842352706104812"><a name="b842352706104812"></a><a name="b842352706104812"></a>Protocol/Application</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.879999999999999%" id="mcps1.2.6.1.3"><p id="p32340552195135"><a name="p32340552195135"></a><a name="p32340552195135"></a><strong id="b842352706161911_1"><a name="b842352706161911_1"></a><a name="b842352706161911_1"></a>Port</strong></p>
</th>
<th class="cellrowborder" valign="top" width="24.759999999999998%" id="mcps1.2.6.1.4"><p id="p2339084195135"><a name="p2339084195135"></a><a name="p2339084195135"></a><strong id="b84235270615214"><a name="b84235270615214"></a><a name="b84235270615214"></a>Source/Destination</strong></p>
</th>
<th class="cellrowborder" valign="top" width="35.03%" id="mcps1.2.6.1.5"><p id="p1096519542911"><a name="p1096519542911"></a><a name="p1096519542911"></a><strong id="b142754662817"><a name="b142754662817"></a><a name="b142754662817"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row55248116195135"><td class="cellrowborder" valign="top" width="10%" headers="mcps1.2.6.1.1 "><p id="p153542182110"><a name="p153542182110"></a><a name="p153542182110"></a>Inbound</p>
</td>
<td class="cellrowborder" valign="top" width="14.330000000000002%" headers="mcps1.2.6.1.2 "><p id="p45912425195135"><a name="p45912425195135"></a><a name="p45912425195135"></a>TCP</p>
</td>
<td class="cellrowborder" valign="top" width="15.879999999999999%" headers="mcps1.2.6.1.3 "><p id="p46840856195135"><a name="p46840856195135"></a><a name="p46840856195135"></a>80</p>
</td>
<td class="cellrowborder" valign="top" width="24.759999999999998%" headers="mcps1.2.6.1.4 "><p id="p36012962195135"><a name="p36012962195135"></a><a name="p36012962195135"></a>Source: 0.0.0.0/0</p>
</td>
<td class="cellrowborder" valign="top" width="35.03%" headers="mcps1.2.6.1.5 "><p id="p1616504613311"><a name="p1616504613311"></a><a name="p1616504613311"></a>Allows inbound HTTP traffic from any IP address to ECSs associated with the security group through port 80.</p>
</td>
</tr>
<tr id="row5566305020026"><td class="cellrowborder" valign="top" width="10%" headers="mcps1.2.6.1.1 "><p id="p1335112162119"><a name="p1335112162119"></a><a name="p1335112162119"></a>Inbound</p>
</td>
<td class="cellrowborder" valign="top" width="14.330000000000002%" headers="mcps1.2.6.1.2 "><p id="p3120540920026"><a name="p3120540920026"></a><a name="p3120540920026"></a>TCP</p>
</td>
<td class="cellrowborder" valign="top" width="15.879999999999999%" headers="mcps1.2.6.1.3 "><p id="p5665449220026"><a name="p5665449220026"></a><a name="p5665449220026"></a>443</p>
</td>
<td class="cellrowborder" valign="top" width="24.759999999999998%" headers="mcps1.2.6.1.4 "><p id="p2561110020026"><a name="p2561110020026"></a><a name="p2561110020026"></a>Source: 0.0.0.0/0</p>
</td>
<td class="cellrowborder" valign="top" width="35.03%" headers="mcps1.2.6.1.5 "><p id="p11273949183317"><a name="p11273949183317"></a><a name="p11273949183317"></a>Allows inbound HTTPS traffic from any IP address to ECSs associated with the security group through port 443.</p>
</td>
</tr>
<tr id="row711437142712"><td class="cellrowborder" valign="top" width="10%" headers="mcps1.2.6.1.1 "><p id="p31141071272"><a name="p31141071272"></a><a name="p31141071272"></a>Outbound</p>
</td>
<td class="cellrowborder" valign="top" width="14.330000000000002%" headers="mcps1.2.6.1.2 "><p id="p711457182715"><a name="p711457182715"></a><a name="p711457182715"></a>All</p>
</td>
<td class="cellrowborder" valign="top" width="15.879999999999999%" headers="mcps1.2.6.1.3 "><p id="p1011487182717"><a name="p1011487182717"></a><a name="p1011487182717"></a>All</p>
</td>
<td class="cellrowborder" valign="top" width="24.759999999999998%" headers="mcps1.2.6.1.4 "><p id="p20126774286"><a name="p20126774286"></a><a name="p20126774286"></a>Destination: 0.0.0.0/0</p>
</td>
<td class="cellrowborder" valign="top" width="35.03%" headers="mcps1.2.6.1.5 "><p id="p20965751299"><a name="p20965751299"></a><a name="p20965751299"></a>Allow all outbound traffic from the security group.</p>
</td>
</tr>
</tbody>
</table>

A firewall adds an additional layer of security. Even if the security group rules allow more traffic than that actually required, the firewall rules allow only access from HTTP port 80 and HTTPS port 443 and deny other inbound traffic.

