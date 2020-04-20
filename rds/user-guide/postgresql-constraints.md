# PostgreSQL Constraints<a name="rds_02_0012"></a>

[Table 1](#table60364850123535)  shows the constraints designed to ensure the stability and security of RDS for PostgreSQL.

**Table  1**  Function constraints

<a name="table60364850123535"></a>
<table><thead align="left"><tr id="row63835418123535"><th class="cellrowborder" valign="top" width="34.21%" id="mcps1.2.3.1.1"><p id="p3286360123535"><a name="p3286360123535"></a><a name="p3286360123535"></a><strong id="b11666728132511"><a name="b11666728132511"></a><a name="b11666728132511"></a>Function Item</strong></p>
</th>
<th class="cellrowborder" valign="top" width="65.79%" id="mcps1.2.3.1.2"><p id="p46946588123535"><a name="p46946588123535"></a><a name="p46946588123535"></a><strong id="b19712840162511"><a name="b19712840162511"></a><a name="b19712840162511"></a>Constraints</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row65651390123535"><td class="cellrowborder" valign="top" width="34.21%" headers="mcps1.2.3.1.1 "><p id="p16162334123535"><a name="p16162334123535"></a><a name="p16162334123535"></a>Database access</p>
</td>
<td class="cellrowborder" valign="top" width="65.79%" headers="mcps1.2.3.1.2 "><a name="ul11391624405"></a><a name="ul11391624405"></a><ul id="ul11391624405"><li>If remote access is not enabled, RDS DB instances must be in the same VPC subnet as the ECS.</li><li>RDS read replicas must be created in the same subnet as the primary DB instance.</li></ul>
<a name="ul34363141508"></a><a name="ul34363141508"></a><ul id="ul34363141508"><li>The ECS must be allowed by the security group to access RDS DB instances.<p id="p1491083014167"><a name="p1491083014167"></a><a name="p1491083014167"></a>By default, RDS cannot be accessed through an ECS in a different security group. You need to add an inbound rule to the RDS security group.</p>
</li><li>The default RDS port is <strong id="b270534514350"><a name="b270534514350"></a><a name="b270534514350"></a>5432</strong>. You can change it if you want to access RDS through another port.</li></ul>
</td>
</tr>
<tr id="row53074217123535"><td class="cellrowborder" valign="top" width="34.21%" headers="mcps1.2.3.1.1 "><p id="p4044355123535"><a name="p4044355123535"></a><a name="p4044355123535"></a>Deployment</p>
</td>
<td class="cellrowborder" valign="top" width="65.79%" headers="mcps1.2.3.1.2 "><p id="p41829298123535"><a name="p41829298123535"></a><a name="p41829298123535"></a>ECSs in which DB instances are deployed are not visible to you. You can access the DB instances only through an IP address and a port number.</p>
</td>
</tr>
<tr id="row60017787123535"><td class="cellrowborder" valign="top" width="34.21%" headers="mcps1.2.3.1.1 "><p id="p29602599123535"><a name="p29602599123535"></a><a name="p29602599123535"></a>Database root permissions</p>
</td>
<td class="cellrowborder" valign="top" width="65.79%" headers="mcps1.2.3.1.2 "><p id="p19341371123535"><a name="p19341371123535"></a><a name="p19341371123535"></a>Only the <strong id="b84235270694322"><a name="b84235270694322"></a><a name="b84235270694322"></a>root</strong> user permissions are provided on the instance creation page.</p>
<div class="note" id="note1962164414312"><a name="note1962164414312"></a><a name="note1962164414312"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p78912441432"><a name="p78912441432"></a><a name="p78912441432"></a>The <strong id="b135221145112116"><a name="b135221145112116"></a><a name="b135221145112116"></a>root</strong> user has the following permissions: Create role, Create DB, and Replication.</p>
</div></div>
</td>
</tr>
<tr id="row62985361123535"><td class="cellrowborder" valign="top" width="34.21%" headers="mcps1.2.3.1.1 "><p id="p1540641123535"><a name="p1540641123535"></a><a name="p1540641123535"></a>Database parameter modification</p>
</td>
<td class="cellrowborder" valign="top" width="65.79%" headers="mcps1.2.3.1.2 "><p id="p15541162812366"><a name="p15541162812366"></a><a name="p15541162812366"></a>Most parameters can be modified on the RDS console.</p>
</td>
</tr>
<tr id="row19812839123535"><td class="cellrowborder" valign="top" width="34.21%" headers="mcps1.2.3.1.1 "><p id="p61336152123535"><a name="p61336152123535"></a><a name="p61336152123535"></a>Data import</p>
</td>
<td class="cellrowborder" valign="top" width="65.79%" headers="mcps1.2.3.1.2 "><a name="ul4481493883833"></a><a name="ul4481493883833"></a><ul id="ul4481493883833"><li>You can use the psql command line tool to migrate data.</li></ul>
<p id="p967061841211"><a name="p967061841211"></a><a name="p967061841211"></a>For details, see section <a href="migrating-postgresql-data-using-psql.md">Migrating PostgreSQL Data Using psql</a>.</p>
</td>
</tr>
<tr id="row32746860123535"><td class="cellrowborder" valign="top" width="34.21%" headers="mcps1.2.3.1.1 "><p id="p35249985123535"><a name="p35249985123535"></a><a name="p35249985123535"></a>Database replication setup</p>
</td>
<td class="cellrowborder" valign="top" width="65.79%" headers="mcps1.2.3.1.2 "><p id="p36676551123535"><a name="p36676551123535"></a><a name="p36676551123535"></a>RDS for PostgreSQL provides a dual-node cluster with primary/standby replication architecture. You do not need to set up replication. The standby DB instance is not visible to users and therefore you cannot access it directly.</p>
</td>
</tr>
<tr id="row43544108123535"><td class="cellrowborder" valign="top" width="34.21%" headers="mcps1.2.3.1.1 "><p id="p37411822123535"><a name="p37411822123535"></a><a name="p37411822123535"></a>DB instance reboot</p>
</td>
<td class="cellrowborder" valign="top" width="65.79%" headers="mcps1.2.3.1.2 "><p id="p41132837123535"><a name="p41132837123535"></a><a name="p41132837123535"></a>DB instances cannot be rebooted through commands. They must be rebooted on the RDS console.</p>
</td>
</tr>
<tr id="row27804808123535"><td class="cellrowborder" valign="top" width="34.21%" headers="mcps1.2.3.1.1 "><p id="p37597003123535"><a name="p37597003123535"></a><a name="p37597003123535"></a>RDS backup files</p>
</td>
<td class="cellrowborder" valign="top" width="65.79%" headers="mcps1.2.3.1.2 "><p id="p48863033123535"><a name="p48863033123535"></a><a name="p48863033123535"></a>RDS backup files are stored in OBS buckets and are not visible to you.</p>
</td>
</tr>
</tbody>
</table>

