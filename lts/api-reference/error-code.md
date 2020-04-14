# Error Code<a name="lts_02_0012"></a>

## Description<a name="section49811902"></a>

This section explains the meanings of error code responses returned by LTS APIs.

## Response Format<a name="section45653938"></a>

\{"error\_msg":"Current user is not authenticated correctly, check your token.","error\_code":"LTS.0002"\}

## Error Code Description<a name="section8232261"></a>

**Table  1**  Error code description

<a name="table7806951"></a>
<table><thead align="left"><tr id="row51412450"><th class="cellrowborder" valign="top" width="13%" id="mcps1.2.6.1.1"><p id="p3658885"><a name="p3658885"></a><a name="p3658885"></a><strong id="b132034917466"><a name="b132034917466"></a><a name="b132034917466"></a>Response Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="10%" id="mcps1.2.6.1.2"><p id="p27934306"><a name="p27934306"></a><a name="p27934306"></a><strong id="b1521459480"><a name="b1521459480"></a><a name="b1521459480"></a>Error Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="21%" id="mcps1.2.6.1.3"><p id="p48086303"><a name="p48086303"></a><a name="p48086303"></a><strong id="b82209541461"><a name="b82209541461"></a><a name="b82209541461"></a>Description</strong></p>
</th>
<th class="cellrowborder" valign="top" width="28.000000000000004%" id="mcps1.2.6.1.4"><p id="p2676452"><a name="p2676452"></a><a name="p2676452"></a><strong id="b5938146145210"><a name="b5938146145210"></a><a name="b5938146145210"></a>Error Message</strong></p>
</th>
<th class="cellrowborder" valign="top" width="28.000000000000004%" id="mcps1.2.6.1.5"><p id="p072561563"><a name="p072561563"></a><a name="p072561563"></a><strong id="b04831408619"><a name="b04831408619"></a><a name="b04831408619"></a>Handling Measure</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row44792488"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.6.1.1 "><p id="p4312951"><a name="p4312951"></a><a name="p4312951"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10%" headers="mcps1.2.6.1.2 "><p id="p13804783"><a name="p13804783"></a><a name="p13804783"></a>LTS.0101</p>
<p id="p57134185"><a name="p57134185"></a><a name="p57134185"></a></p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.6.1.3 "><p id="p64466288"><a name="p64466288"></a><a name="p64466288"></a>Failed to create the log group because a log group with the same name already exists.</p>
</td>
<td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.6.1.4 "><p id="p54386868"><a name="p54386868"></a><a name="p54386868"></a>Failed to create log group, the group name has been existed</p>
</td>
<td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.6.1.5 "><p id="p43260188"><a name="p43260188"></a><a name="p43260188"></a>Check the log group name.</p>
</td>
</tr>
<tr id="row53797377"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.6.1.1 "><p id="p62620315"><a name="p62620315"></a><a name="p62620315"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10%" headers="mcps1.2.6.1.2 "><p id="p39080782"><a name="p39080782"></a><a name="p39080782"></a>LTS.0104</p>
<p id="p16182720"><a name="p16182720"></a><a name="p16182720"></a></p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.6.1.3 "><p id="p35731914"><a name="p35731914"></a><a name="p35731914"></a>Failed to create the log group because the maximum number of log groups has been reached.</p>
</td>
<td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.6.1.4 "><p id="p8603904"><a name="p8603904"></a><a name="p8603904"></a>Failed to create log group, the number of log groups exceeds the quota</p>
</td>
<td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.6.1.5 "><p id="p25827660"><a name="p25827660"></a><a name="p25827660"></a>Check whether the number of log groups reaches the quota (100 by default).</p>
</td>
</tr>
<tr id="row31122348"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.6.1.1 "><p id="p37882289"><a name="p37882289"></a><a name="p37882289"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10%" headers="mcps1.2.6.1.2 "><p id="p48566591"><a name="p48566591"></a><a name="p48566591"></a>LTS.0105</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.6.1.3 "><p id="p41579773"><a name="p41579773"></a><a name="p41579773"></a>Failed to delete the log group because the log group has associated log transfer tasks.</p>
</td>
<td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.6.1.4 "><p id="p12518419"><a name="p12518419"></a><a name="p12518419"></a>Log group is associated by transfer</p>
</td>
<td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.6.1.5 "><p id="p7359018"><a name="p7359018"></a><a name="p7359018"></a>Check whether the associated log transfer tasks have been deleted.</p>
</td>
</tr>
<tr id="row66231165"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.6.1.1 "><p id="p63124152"><a name="p63124152"></a><a name="p63124152"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="10%" headers="mcps1.2.6.1.2 "><p id="p12782663"><a name="p12782663"></a><a name="p12782663"></a>LTS.0201</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.6.1.3 "><p id="p28762771"><a name="p28762771"></a><a name="p28762771"></a>Failed to create the log topic because the associated log group does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.6.1.4 "><p id="p48083075"><a name="p48083075"></a><a name="p48083075"></a>The group is not existed</p>
</td>
<td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.6.1.5 "><p id="p2414975"><a name="p2414975"></a><a name="p2414975"></a>Check the ID of the log group.</p>
</td>
</tr>
<tr id="row21734782"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.6.1.1 "><p id="p15686904"><a name="p15686904"></a><a name="p15686904"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10%" headers="mcps1.2.6.1.2 "><p id="p62679731"><a name="p62679731"></a><a name="p62679731"></a>LTS.0205</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.6.1.3 "><p id="p43893463"><a name="p43893463"></a><a name="p43893463"></a>Failed to create the log topic because a log topic with the same name already exists.</p>
</td>
<td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.6.1.4 "><p id="p65709578"><a name="p65709578"></a><a name="p65709578"></a>The topic name has been existed</p>
</td>
<td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.6.1.5 "><p id="p20875639"><a name="p20875639"></a><a name="p20875639"></a>Check whether the log topic with the same name already exists.</p>
</td>
</tr>
<tr id="row53663026"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.6.1.1 "><p id="p51737830"><a name="p51737830"></a><a name="p51737830"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10%" headers="mcps1.2.6.1.2 "><p id="p30014695"><a name="p30014695"></a><a name="p30014695"></a>LTS.0206</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.6.1.3 "><p id="p15271196"><a name="p15271196"></a><a name="p15271196"></a>Failed to create the log topic because the maximum number of log topics has been reached.</p>
</td>
<td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.6.1.4 "><p id="p29007341"><a name="p29007341"></a><a name="p29007341"></a>Failed to create log topic, the number of log topics exceeds the quota</p>
</td>
<td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.6.1.5 "><p id="p784452"><a name="p784452"></a><a name="p784452"></a>Check whether the number of log topics reaches the quota (100 by default).</p>
</td>
</tr>
<tr id="row7060068"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.6.1.1 "><p id="p34994620"><a name="p34994620"></a><a name="p34994620"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10%" headers="mcps1.2.6.1.2 "><p id="p15991948"><a name="p15991948"></a><a name="p15991948"></a>LTS.0207</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.6.1.3 "><p id="p20279421"><a name="p20279421"></a><a name="p20279421"></a>Failed to delete the log topic because the log topic has associated a log transfer task.</p>
</td>
<td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.6.1.4 "><p id="p32020406"><a name="p32020406"></a><a name="p32020406"></a>Log topic is associated by transfer</p>
</td>
<td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.6.1.5 "><p id="p43516128"><a name="p43516128"></a><a name="p43516128"></a>Check whether the associated log transfer task has been deleted.</p>
</td>
</tr>
<tr id="row56100839"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.6.1.1 "><p id="p47874109"><a name="p47874109"></a><a name="p47874109"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="10%" headers="mcps1.2.6.1.2 "><p id="p52597591"><a name="p52597591"></a><a name="p52597591"></a>LTS.0010</p>
<p id="p3616273"><a name="p3616273"></a><a name="p3616273"></a></p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.6.1.3 "><p id="p24482701"><a name="p24482701"></a><a name="p24482701"></a>System internal error.</p>
</td>
<td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.6.1.4 "><p id="p36941761"><a name="p36941761"></a><a name="p36941761"></a>The system encountered an internal error</p>
</td>
<td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.6.1.5 "><p id="p39492694"><a name="p39492694"></a><a name="p39492694"></a>Contact the administrator.</p>
</td>
</tr>
<tr id="row19889932"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.6.1.1 "><p id="p471829"><a name="p471829"></a><a name="p471829"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="10%" headers="mcps1.2.6.1.2 "><p id="p38218194"><a name="p38218194"></a><a name="p38218194"></a>LTS.0102</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.6.1.3 "><p id="p8666028"><a name="p8666028"></a><a name="p8666028"></a>Failed to create the log group.</p>
</td>
<td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.6.1.4 "><p id="p30859658"><a name="p30859658"></a><a name="p30859658"></a>Failed to create log group.</p>
</td>
<td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.6.1.5 "><p id="p16604373"><a name="p16604373"></a><a name="p16604373"></a>Check whether the project ID is correct and whether the log group name meets the requirements.</p>
</td>
</tr>
<tr id="row15221630"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.6.1.1 "><p id="p24992535"><a name="p24992535"></a><a name="p24992535"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="10%" headers="mcps1.2.6.1.2 "><p id="p11129424"><a name="p11129424"></a><a name="p11129424"></a>LTS.0103</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.6.1.3 "><p id="p29068113"><a name="p29068113"></a><a name="p29068113"></a>Failed to delete the log group.</p>
</td>
<td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.6.1.4 "><p id="p5706947"><a name="p5706947"></a><a name="p5706947"></a>Failed to delete log group</p>
</td>
<td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.6.1.5 "><p id="p59609549"><a name="p59609549"></a><a name="p59609549"></a>Check whether the database is normal or whether the network connection is normal.</p>
</td>
</tr>
<tr id="row66723899"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.6.1.1 "><p id="p35926749"><a name="p35926749"></a><a name="p35926749"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="10%" headers="mcps1.2.6.1.2 "><p id="p24385580"><a name="p24385580"></a><a name="p24385580"></a>LTS.0202</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.6.1.3 "><p id="p29074959"><a name="p29074959"></a><a name="p29074959"></a>Failed to create the log topic.</p>
</td>
<td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.6.1.4 "><p id="p6261487"><a name="p6261487"></a><a name="p6261487"></a>Failed to create log topic</p>
</td>
<td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.6.1.5 "><p id="p37418419"><a name="p37418419"></a><a name="p37418419"></a>Check whether the project and group IDs are correct and whether the log topic name meets the requirements.</p>
</td>
</tr>
<tr id="row1221454"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.6.1.1 "><p id="p31828964"><a name="p31828964"></a><a name="p31828964"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="10%" headers="mcps1.2.6.1.2 "><p id="p28009298"><a name="p28009298"></a><a name="p28009298"></a>LTS.0203</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.6.1.3 "><p id="p54160705"><a name="p54160705"></a><a name="p54160705"></a>Failed to delete the log topic.</p>
</td>
<td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.6.1.4 "><p id="p24941017"><a name="p24941017"></a><a name="p24941017"></a>Failed to delete log topic</p>
</td>
<td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.6.1.5 "><p id="p6956481"><a name="p6956481"></a><a name="p6956481"></a>Check whether the database is normal or whether the network connection is normal.</p>
</td>
</tr>
<tr id="row1791194395619"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.6.1.1 "><p id="p18580211145717"><a name="p18580211145717"></a><a name="p18580211145717"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10%" headers="mcps1.2.6.1.2 "><p id="p7580911205715"><a name="p7580911205715"></a><a name="p7580911205715"></a>LTS.0001</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.6.1.3 "><p id="p13580111195714"><a name="p13580111195714"></a><a name="p13580111195714"></a>The API version /projectId is invalid or does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.6.1.4 "><p id="p2058011111573"><a name="p2058011111573"></a><a name="p2058011111573"></a>API version/project id invalid or missing</p>
</td>
<td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.6.1.5 "><p id="p1580201112571"><a name="p1580201112571"></a><a name="p1580201112571"></a>Check whether the version and projectID information is correct.</p>
</td>
</tr>
<tr id="row1120544917564"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.6.1.1 "><p id="p10580191165711"><a name="p10580191165711"></a><a name="p10580191165711"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="10%" headers="mcps1.2.6.1.2 "><p id="p13580151112578"><a name="p13580151112578"></a><a name="p13580151112578"></a>LTS.0002</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.6.1.3 "><p id="p6580171195710"><a name="p6580171195710"></a><a name="p6580171195710"></a>Invalid user token.</p>
</td>
<td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.6.1.4 "><p id="p958011117576"><a name="p958011117576"></a><a name="p958011117576"></a>Current user is not authenticated correctly, check your token</p>
</td>
<td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.6.1.5 "><p id="p65801411105717"><a name="p65801411105717"></a><a name="p65801411105717"></a>Check the token information of the current user.</p>
</td>
</tr>
<tr id="row4120105465610"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.6.1.1 "><p id="p1580131115573"><a name="p1580131115573"></a><a name="p1580131115573"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10%" headers="mcps1.2.6.1.2 "><p id="p8580181195712"><a name="p8580181195712"></a><a name="p8580181195712"></a>LTS.0011</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.6.1.3 "><p id="p358041125710"><a name="p358041125710"></a><a name="p358041125710"></a>Invalid resource ID.</p>
</td>
<td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.6.1.4 "><p id="p958071120574"><a name="p958071120574"></a><a name="p958071120574"></a>The resource id is invalid or missing</p>
</td>
<td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.6.1.5 "><p id="p1858051110578"><a name="p1858051110578"></a><a name="p1858051110578"></a>Check whether the resource ID in the request is correct.</p>
</td>
</tr>
</tbody>
</table>

