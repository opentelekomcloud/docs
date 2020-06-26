# Comparison Between RDS and Self-Built Databases<a name="rds_01_0006"></a>

## Performance<a name="section53851353125220"></a>

<a name="table16430134385214"></a>
<table><thead align="left"><tr id="row65749432527"><th class="cellrowborder" valign="top" width="18.15%" id="mcps1.1.4.1.1"><p id="p25741443185217"><a name="p25741443185217"></a><a name="p25741443185217"></a>Item</p>
</th>
<th class="cellrowborder" valign="top" width="38.15%" id="mcps1.1.4.1.2"><p id="p10574643175217"><a name="p10574643175217"></a><a name="p10574643175217"></a>Cloud Database RDS</p>
</th>
<th class="cellrowborder" valign="top" width="43.7%" id="mcps1.1.4.1.3"><p id="p3574114318521"><a name="p3574114318521"></a><a name="p3574114318521"></a>Self-Built Database Service</p>
</th>
</tr>
</thead>
<tbody><tr id="row65749437523"><td class="cellrowborder" valign="top" width="18.15%" headers="mcps1.1.4.1.1 "><p id="p757494319521"><a name="p757494319521"></a><a name="p757494319521"></a>Service availability</p>
</td>
<td class="cellrowborder" valign="top" width="38.15%" headers="mcps1.1.4.1.2 "><p id="p76401257185214"><a name="p76401257185214"></a><a name="p76401257185214"></a>For more information, see the <em id="i93210210418"><a name="i93210210418"></a><a name="i93210210418"></a>Elastic Cloud Server User Guide</em>.</p>
</td>
<td class="cellrowborder" valign="top" width="43.7%" headers="mcps1.1.4.1.3 "><p id="p1588112652216"><a name="p1588112652216"></a><a name="p1588112652216"></a>Requires device procurement, primary/standby relationship setup, and RAID setup.</p>
</td>
</tr>
<tr id="row15741343145214"><td class="cellrowborder" valign="top" width="18.15%" headers="mcps1.1.4.1.1 "><p id="p05746437523"><a name="p05746437523"></a><a name="p05746437523"></a>Data reliability</p>
</td>
<td class="cellrowborder" valign="top" width="38.15%" headers="mcps1.1.4.1.2 "><p id="p1542794165316"><a name="p1542794165316"></a><a name="p1542794165316"></a>For more information, see the <em id="i842352697162817"><a name="i842352697162817"></a><a name="i842352697162817"></a>Elastic Volume Service User Guide</em>.</p>
</td>
<td class="cellrowborder" valign="top" width="43.7%" headers="mcps1.1.4.1.3 "><p id="p1882826202215"><a name="p1882826202215"></a><a name="p1882826202215"></a>Requires device procurement, primary/standby relationship setup, and RAID setup.</p>
</td>
</tr>
<tr id="row65748431522"><td class="cellrowborder" valign="top" width="18.15%" headers="mcps1.1.4.1.1 "><p id="p9574643175214"><a name="p9574643175214"></a><a name="p9574643175214"></a>System security</p>
</td>
<td class="cellrowborder" valign="top" width="38.15%" headers="mcps1.1.4.1.2 "><p id="p1676521712319"><a name="p1676521712319"></a><a name="p1676521712319"></a>Defends against Anti-DDoS attacks and promptly repairs database security vulnerabilities.</p>
</td>
<td class="cellrowborder" valign="top" width="43.7%" headers="mcps1.1.4.1.3 "><p id="p14882326112219"><a name="p14882326112219"></a><a name="p14882326112219"></a>Requires procurement of expensive devices and software, as well as manual detection and repair of security vulnerabilities.</p>
</td>
</tr>
<tr id="row1757444375215"><td class="cellrowborder" valign="top" width="18.15%" headers="mcps1.1.4.1.1 "><p id="p14574144305216"><a name="p14574144305216"></a><a name="p14574144305216"></a>Database backup</p>
</td>
<td class="cellrowborder" valign="top" width="38.15%" headers="mcps1.1.4.1.2 "><p id="p1576561719238"><a name="p1576561719238"></a><a name="p1576561719238"></a>Supports automated backups, manual backups, and custom backup retention periods.</p>
</td>
<td class="cellrowborder" valign="top" width="43.7%" headers="mcps1.1.4.1.3 "><p id="p15882122614224"><a name="p15882122614224"></a><a name="p15882122614224"></a>Requires device procurement, setup, and maintenance.</p>
</td>
</tr>
<tr id="row35751343135215"><td class="cellrowborder" valign="top" width="18.15%" headers="mcps1.1.4.1.1 "><p id="p1457584316526"><a name="p1457584316526"></a><a name="p1457584316526"></a>Hardware and software investment</p>
</td>
<td class="cellrowborder" valign="top" width="38.15%" headers="mcps1.1.4.1.2 "><p id="p1576561712318"><a name="p1576561712318"></a><a name="p1576561712318"></a>Supports on-demand pricing and scaling without requiring hardware and software investment.</p>
</td>
<td class="cellrowborder" valign="top" width="43.7%" headers="mcps1.1.4.1.3 "><p id="p1588214263223"><a name="p1588214263223"></a><a name="p1588214263223"></a>Requires large investment in database servers. The Microsoft SQL Server license must be paid for separately.</p>
</td>
</tr>
<tr id="row135751343125213"><td class="cellrowborder" valign="top" width="18.15%" headers="mcps1.1.4.1.1 "><p id="p7575124313526"><a name="p7575124313526"></a><a name="p7575124313526"></a>System hosting</p>
</td>
<td class="cellrowborder" valign="top" width="38.15%" headers="mcps1.1.4.1.2 "><p id="p1176651782317"><a name="p1176651782317"></a><a name="p1176651782317"></a>Not required.</p>
</td>
<td class="cellrowborder" valign="top" width="43.7%" headers="mcps1.1.4.1.3 "><p id="p27862184183821"><a name="p27862184183821"></a><a name="p27862184183821"></a>If a 2U server and primary/standby DB instances are required, you need to purchase and set up two servers.</p>
</td>
</tr>
<tr id="row12575143155215"><td class="cellrowborder" valign="top" width="18.15%" headers="mcps1.1.4.1.1 "><p id="p8575204313524"><a name="p8575204313524"></a><a name="p8575204313524"></a>Maintenance cost</p>
</td>
<td class="cellrowborder" valign="top" width="38.15%" headers="mcps1.1.4.1.2 "><p id="p2076641719232"><a name="p2076641719232"></a><a name="p2076641719232"></a>Not required.</p>
</td>
<td class="cellrowborder" valign="top" width="43.7%" headers="mcps1.1.4.1.3 "><p id="p388452616224"><a name="p388452616224"></a><a name="p388452616224"></a>Requires large manpower investment and professional database administrator (DBA) for maintenance.</p>
</td>
</tr>
<tr id="row057515435524"><td class="cellrowborder" valign="top" width="18.15%" headers="mcps1.1.4.1.1 "><p id="p1657534305214"><a name="p1657534305214"></a><a name="p1657534305214"></a>Deployment and scaling</p>
</td>
<td class="cellrowborder" valign="top" width="38.15%" headers="mcps1.1.4.1.2 "><p id="p27667178232"><a name="p27667178232"></a><a name="p27667178232"></a>Supports elastic scaling, fast upgrade, and on-demand enabling.</p>
</td>
<td class="cellrowborder" valign="top" width="43.7%" headers="mcps1.1.4.1.3 "><p id="p4884112610226"><a name="p4884112610226"></a><a name="p4884112610226"></a>Requires procurement, deployment, and coordination of hardware that matches original devices.</p>
</td>
</tr>
<tr id="row175751743105218"><td class="cellrowborder" valign="top" width="18.15%" headers="mcps1.1.4.1.1 "><p id="p1457594395210"><a name="p1457594395210"></a><a name="p1457594395210"></a>Resource utilization</p>
</td>
<td class="cellrowborder" valign="top" width="38.15%" headers="mcps1.1.4.1.2 "><p id="p2766817122310"><a name="p2766817122310"></a><a name="p2766817122310"></a>Bills users based on the resources actually used, resulting in 100% resource utilization.</p>
</td>
<td class="cellrowborder" valign="top" width="43.7%" headers="mcps1.1.4.1.3 "><p id="p1557520431528"><a name="p1557520431528"></a><a name="p1557520431528"></a>Considers peak traffic, resulting in low resource utilization.</p>
</td>
</tr>
</tbody>
</table>

