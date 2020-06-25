# How Do I Handle Error Messages Displayed on the Management Console?<a name="EN-US_TOPIC_0032398121"></a>

## Symptom<a name="section4858569817051"></a>

This section helps you resolve the following issues:

-   An error message was displayed on the management console after you performed ECS-related operations.
-   An error code was displayed after you used an ECS API \(see  _Elastic Cloud Server API Reference_\).

## Background<a name="section5832519917307"></a>

After you perform ECS-related operations on the management console, the system displays the request status on the  **Elastic Cloud Server**  page. You can determine the request execution status based on the information displayed in the request status.

-   If the operation request is executed, the system automatically clears the task prompt.
-   If an error occurs during the request execution, the system displays an error code and its description in the taskbar.

## Solution<a name="section32147499165439"></a>

If an error occurs, find the error code and perform the corresponding operations listed in  [Table 1](#table52205309173837).

**Table  1**  Error codes and solution suggestions

<a name="table52205309173837"></a>
<table><thead align="left"><tr id="row62230802173837"><th class="cellrowborder" valign="top" width="13.969999999999999%" id="mcps1.2.4.1.1"><p id="p663130173837"><a name="p663130173837"></a><a name="p663130173837"></a>Error Code</p>
</th>
<th class="cellrowborder" valign="top" width="31.259999999999998%" id="mcps1.2.4.1.2"><p id="p53713593173837"><a name="p53713593173837"></a><a name="p53713593173837"></a>Message Displayed on the Management Console</p>
</th>
<th class="cellrowborder" valign="top" width="54.769999999999996%" id="mcps1.2.4.1.3"><p id="p55833772173837"><a name="p55833772173837"></a><a name="p55833772173837"></a>Solution Suggestion</p>
</th>
</tr>
</thead>
<tbody><tr id="row32741905173837"><td class="cellrowborder" valign="top" width="13.969999999999999%" headers="mcps1.2.4.1.1 "><p id="p4826907174720"><a name="p4826907174720"></a><a name="p4826907174720"></a>Ecs.0000</p>
</td>
<td class="cellrowborder" valign="top" width="31.259999999999998%" headers="mcps1.2.4.1.2 "><p id="p55435215174720"><a name="p55435215174720"></a><a name="p55435215174720"></a>Request error. Try again later or contact customer service.</p>
</td>
<td class="cellrowborder" valign="top" width="54.769999999999996%" headers="mcps1.2.4.1.3 "><p id="p61067431174720"><a name="p61067431174720"></a><a name="p61067431174720"></a>Adjust the request structure as directed in <em id="i84235269723631"><a name="i84235269723631"></a><a name="i84235269723631"></a>Elastic Cloud Server API Reference</em>.</p>
</td>
</tr>
<tr id="row18144230173837"><td class="cellrowborder" valign="top" width="13.969999999999999%" headers="mcps1.2.4.1.1 "><p id="p24980846174720"><a name="p24980846174720"></a><a name="p24980846174720"></a>Ecs.0001</p>
</td>
<td class="cellrowborder" valign="top" width="31.259999999999998%" headers="mcps1.2.4.1.2 "><p id="p10182673174720"><a name="p10182673174720"></a><a name="p10182673174720"></a>The maximum number of ECSs or EVS disks has been reached. Contact customer service and request a quota increase.</p>
</td>
<td class="cellrowborder" valign="top" width="54.769999999999996%" headers="mcps1.2.4.1.3 "><p id="p9669831175942"><a name="p9669831175942"></a><a name="p9669831175942"></a>Contact customer service and request an ECS quota increase.</p>
<div class="note" id="note51834969175942"><a name="note51834969175942"></a><a name="note51834969175942"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p63861538175942"><a name="p63861538175942"></a><a name="p63861538175942"></a>Before requesting for increasing your ECS quota, consider the number of to-be-added ECSs, vCPUs, and memory capacity required.</p>
</div></div>
</td>
</tr>
<tr id="row53906742173837"><td class="cellrowborder" valign="top" width="13.969999999999999%" headers="mcps1.2.4.1.1 "><p id="p41129247174818"><a name="p41129247174818"></a><a name="p41129247174818"></a>Ecs.0003</p>
</td>
<td class="cellrowborder" valign="top" width="31.259999999999998%" headers="mcps1.2.4.1.2 "><p id="p43134685174818"><a name="p43134685174818"></a><a name="p43134685174818"></a>You do not have the permission or your balance is insufficient.</p>
</td>
<td class="cellrowborder" valign="top" width="54.769999999999996%" headers="mcps1.2.4.1.3 "><p id="p4248563174818"><a name="p4248563174818"></a><a name="p4248563174818"></a>Contact customer service to check your account information.</p>
</td>
</tr>
<tr id="row8103960173837"><td class="cellrowborder" valign="top" width="13.969999999999999%" headers="mcps1.2.4.1.1 "><p id="p10195037174818"><a name="p10195037174818"></a><a name="p10195037174818"></a>Ecs.0005</p>
</td>
<td class="cellrowborder" valign="top" width="31.259999999999998%" headers="mcps1.2.4.1.2 "><p id="p20491672174818"><a name="p20491672174818"></a><a name="p20491672174818"></a>System error. Try again later or contact customer service.</p>
</td>
<td class="cellrowborder" valign="top" width="54.769999999999996%" headers="mcps1.2.4.1.3 "><p id="p49212711174818"><a name="p49212711174818"></a><a name="p49212711174818"></a>Adjust the request structure as directed in <em id="i1303976047"><a name="i1303976047"></a><a name="i1303976047"></a>Elastic Cloud Server API Reference</em>.</p>
</td>
</tr>
<tr id="row51965547173837"><td class="cellrowborder" valign="top" width="13.969999999999999%" headers="mcps1.2.4.1.1 "><p id="p39933195174818"><a name="p39933195174818"></a><a name="p39933195174818"></a>Ecs.0010</p>
</td>
<td class="cellrowborder" valign="top" width="31.259999999999998%" headers="mcps1.2.4.1.2 "><p id="p13363324174818"><a name="p13363324174818"></a><a name="p13363324174818"></a>The private IP address is in use. Select an available IP address for ECS creation.</p>
</td>
<td class="cellrowborder" valign="top" width="54.769999999999996%" headers="mcps1.2.4.1.3 "><p id="p8687454174818"><a name="p8687454174818"></a><a name="p8687454174818"></a>Use an idle IP address for ECS creation.</p>
</td>
</tr>
<tr id="row46901142173837"><td class="cellrowborder" valign="top" width="13.969999999999999%" headers="mcps1.2.4.1.1 "><p id="p61649301174845"><a name="p61649301174845"></a><a name="p61649301174845"></a>Ecs.0011</p>
</td>
<td class="cellrowborder" valign="top" width="31.259999999999998%" headers="mcps1.2.4.1.2 "><p id="p27537490174845"><a name="p27537490174845"></a><a name="p27537490174845"></a>Invalid password. Change the password to make it meet the password complexity requirements, and perform the required operation again.</p>
</td>
<td class="cellrowborder" valign="top" width="54.769999999999996%" headers="mcps1.2.4.1.3 "><p id="p15944236174845"><a name="p15944236174845"></a><a name="p15944236174845"></a>Input a password that meets password complexity requirements. Then, initial the request again.</p>
</td>
</tr>
<tr id="row33853513173837"><td class="cellrowborder" valign="top" width="13.969999999999999%" headers="mcps1.2.4.1.1 "><p id="p13514846174845"><a name="p13514846174845"></a><a name="p13514846174845"></a>Ecs.0012</p>
</td>
<td class="cellrowborder" valign="top" width="31.259999999999998%" headers="mcps1.2.4.1.2 "><p id="p20960766174845"><a name="p20960766174845"></a><a name="p20960766174845"></a>Insufficient IP addresses in the subnet. Release IP addresses in the subnet or select another subnet for ECS creation.</p>
</td>
<td class="cellrowborder" valign="top" width="54.769999999999996%" headers="mcps1.2.4.1.3 "><p id="p20100503174845"><a name="p20100503174845"></a><a name="p20100503174845"></a>Release IP addresses in the subnet or select another subnet for ECS creation.</p>
</td>
</tr>
<tr id="row7438280174856"><td class="cellrowborder" valign="top" width="13.969999999999999%" headers="mcps1.2.4.1.1 "><p id="p6972819174924"><a name="p6972819174924"></a><a name="p6972819174924"></a>Ecs.0013</p>
</td>
<td class="cellrowborder" valign="top" width="31.259999999999998%" headers="mcps1.2.4.1.2 "><p id="p27927429174924"><a name="p27927429174924"></a><a name="p27927429174924"></a>Insufficient EIP quota. Contact customer service and request a quota increase.</p>
</td>
<td class="cellrowborder" valign="top" width="54.769999999999996%" headers="mcps1.2.4.1.3 "><p id="p47529292174924"><a name="p47529292174924"></a><a name="p47529292174924"></a>Contact customer service and request an EIP quota increase.</p>
</td>
</tr>
<tr id="row26998677174856"><td class="cellrowborder" valign="top" width="13.969999999999999%" headers="mcps1.2.4.1.1 "><p id="p20680660174924"><a name="p20680660174924"></a><a name="p20680660174924"></a>Ecs.0015</p>
</td>
<td class="cellrowborder" valign="top" width="31.259999999999998%" headers="mcps1.2.4.1.2 "><p id="p64520765174924"><a name="p64520765174924"></a><a name="p64520765174924"></a>The disk of this type is not supported by the ECS.</p>
</td>
<td class="cellrowborder" valign="top" width="54.769999999999996%" headers="mcps1.2.4.1.3 "><p id="p58799511174924"><a name="p58799511174924"></a><a name="p58799511174924"></a>Select a proper disk and attach it to the ECS.</p>
</td>
</tr>
<tr id="row55845998174856"><td class="cellrowborder" valign="top" width="13.969999999999999%" headers="mcps1.2.4.1.1 "><p id="p49388892174924"><a name="p49388892174924"></a><a name="p49388892174924"></a>Ecs.0100</p>
</td>
<td class="cellrowborder" valign="top" width="31.259999999999998%" headers="mcps1.2.4.1.2 "><p id="p41077286174924"><a name="p41077286174924"></a><a name="p41077286174924"></a>Invalid ECS status. Change the status and try again.</p>
</td>
<td class="cellrowborder" valign="top" width="54.769999999999996%" headers="mcps1.2.4.1.3 "><p id="p38925852174924"><a name="p38925852174924"></a><a name="p38925852174924"></a>Change the ECS status to the desired one and try again.</p>
</td>
</tr>
<tr id="row12553814174856"><td class="cellrowborder" valign="top" width="13.969999999999999%" headers="mcps1.2.4.1.1 "><p id="p57006184174924"><a name="p57006184174924"></a><a name="p57006184174924"></a>Ecs.0103</p>
</td>
<td class="cellrowborder" valign="top" width="31.259999999999998%" headers="mcps1.2.4.1.2 "><p id="p54098221174924"><a name="p54098221174924"></a><a name="p54098221174924"></a>The disk is unavailable.</p>
</td>
<td class="cellrowborder" valign="top" width="54.769999999999996%" headers="mcps1.2.4.1.3 "><p id="p19879803174924"><a name="p19879803174924"></a><a name="p19879803174924"></a>Change the ECS status to the desired one and try again. If the EVS disk is faulty, contact customer service for troubleshooting.</p>
</td>
</tr>
<tr id="row22772756174856"><td class="cellrowborder" valign="top" width="13.969999999999999%" headers="mcps1.2.4.1.1 "><p id="p63970753174924"><a name="p63970753174924"></a><a name="p63970753174924"></a>Ecs.0104</p>
</td>
<td class="cellrowborder" valign="top" width="31.259999999999998%" headers="mcps1.2.4.1.2 "><p id="p14248523174924"><a name="p14248523174924"></a><a name="p14248523174924"></a>The number of disks to be attached to an ECS exceeds the number allowed.</p>
</td>
<td class="cellrowborder" valign="top" width="54.769999999999996%" headers="mcps1.2.4.1.3 "><p id="p13279705174924"><a name="p13279705174924"></a><a name="p13279705174924"></a>Detach EVS disks from the ECS before attaching new ones.</p>
</td>
</tr>
<tr id="row64515963174856"><td class="cellrowborder" valign="top" width="13.969999999999999%" headers="mcps1.2.4.1.1 "><p id="p5681440175014"><a name="p5681440175014"></a><a name="p5681440175014"></a>Ecs.0105</p>
</td>
<td class="cellrowborder" valign="top" width="31.259999999999998%" headers="mcps1.2.4.1.2 "><p id="p57543461175014"><a name="p57543461175014"></a><a name="p57543461175014"></a>No system disk found.</p>
</td>
<td class="cellrowborder" valign="top" width="54.769999999999996%" headers="mcps1.2.4.1.3 "><p id="p30508742175014"><a name="p30508742175014"></a><a name="p30508742175014"></a>Attach the system disk to the ECS and perform the desired operation again.</p>
</td>
</tr>
<tr id="row14037923174856"><td class="cellrowborder" valign="top" width="13.969999999999999%" headers="mcps1.2.4.1.1 "><p id="p27839573175014"><a name="p27839573175014"></a><a name="p27839573175014"></a>Ecs.0107</p>
</td>
<td class="cellrowborder" valign="top" width="31.259999999999998%" headers="mcps1.2.4.1.2 "><p id="p40412925175014"><a name="p40412925175014"></a><a name="p40412925175014"></a>The number of shared disks to be attached to an ECS exceeds the maximum limit.</p>
</td>
<td class="cellrowborder" valign="top" width="54.769999999999996%" headers="mcps1.2.4.1.3 "><p id="p52221469175014"><a name="p52221469175014"></a><a name="p52221469175014"></a>Detach EVS disks from the ECS before attaching new ones.</p>
</td>
</tr>
<tr id="row12659197174959"><td class="cellrowborder" valign="top" width="13.969999999999999%" headers="mcps1.2.4.1.1 "><p id="p18725458175014"><a name="p18725458175014"></a><a name="p18725458175014"></a>Other error codes</p>
</td>
<td class="cellrowborder" valign="top" width="31.259999999999998%" headers="mcps1.2.4.1.2 "><p id="p40367143175014"><a name="p40367143175014"></a><a name="p40367143175014"></a>Other error messages</p>
</td>
<td class="cellrowborder" valign="top" width="54.769999999999996%" headers="mcps1.2.4.1.3 "><p id="p48513136175014"><a name="p48513136175014"></a><a name="p48513136175014"></a>Initiate the request again. If the error persists, record the returned error code and contact customer service for troubleshooting.</p>
</td>
</tr>
</tbody>
</table>

