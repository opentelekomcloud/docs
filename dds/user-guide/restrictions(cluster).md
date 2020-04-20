# Restrictions<a name="dds_02_0002"></a>

To improve the stability and security of DB instances, there are some restrictions on the use of DDS. For details, see  [Table 1](#table60364850123535).

**Table  1**  Function restrictions

<a name="table60364850123535"></a>
<table><thead align="left"><tr id="row63835418123535"><th class="cellrowborder" valign="top" width="27.26%" id="mcps1.2.3.1.1"><p id="p3286360123535"><a name="p3286360123535"></a><a name="p3286360123535"></a><strong id="b29577244123535"><a name="b29577244123535"></a><a name="b29577244123535"></a>Operation</strong></p>
</th>
<th class="cellrowborder" valign="top" width="72.74000000000001%" id="mcps1.2.3.1.2"><p id="p46946588123535"><a name="p46946588123535"></a><a name="p46946588123535"></a><strong id="b842352706171539"><a name="b842352706171539"></a><a name="b842352706171539"></a>Restrictions</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row65651390123535"><td class="cellrowborder" valign="top" width="27.26%" headers="mcps1.2.3.1.1 "><p id="p16162334123535"><a name="p16162334123535"></a><a name="p16162334123535"></a>Use a client to connect to the DB instance.</p>
</td>
<td class="cellrowborder" valign="top" width="72.74000000000001%" headers="mcps1.2.3.1.2 "><a name="ul53814073144559"></a><a name="ul53814073144559"></a><ul id="ul53814073144559"><li>To access a <span class="keyword" id="keyword159551725101016"><a name="keyword159551725101016"></a><a name="keyword159551725101016"></a>DDS DB instance</span> which is not publicly accessible from an ECS, the instance must be in the same VPC subnet as the ECS.</li><li>By default, DDS cannot be accessed through an ECS in a different security group. You need to add an inbound rule to the DDS security group.</li><li>The default DDS port number is 8635. You can change it if you want to access DDS through another port.</li></ul>
</td>
</tr>
<tr id="row53074217123535"><td class="cellrowborder" valign="top" width="27.26%" headers="mcps1.2.3.1.1 "><p id="p4044355123535"><a name="p4044355123535"></a><a name="p4044355123535"></a>Deployment</p>
</td>
<td class="cellrowborder" valign="top" width="72.74000000000001%" headers="mcps1.2.3.1.2 "><p id="p41829298123535"><a name="p41829298123535"></a><a name="p41829298123535"></a>ECSs in which DB instances are deployed are not visible to you. Your applications can access the database only through an IP address and port.</p>
</td>
</tr>
<tr id="row60017787123535"><td class="cellrowborder" valign="top" width="27.26%" headers="mcps1.2.3.1.1 "><p id="p29602599123535"><a name="p29602599123535"></a><a name="p29602599123535"></a>Obtaining permissions of user <strong id="b84235270617431"><a name="b84235270617431"></a><a name="b84235270617431"></a>rwuser</strong></p>
</td>
<td class="cellrowborder" valign="top" width="72.74000000000001%" headers="mcps1.2.3.1.2 "><p id="p738283513565"><a name="p738283513565"></a><a name="p738283513565"></a>Only the <strong id="en-us_topic_0105284934_b84235270694322"><a name="en-us_topic_0105284934_b84235270694322"></a><a name="en-us_topic_0105284934_b84235270694322"></a>rwuser</strong> user permissions are provided on the instance creation page.</p>
<p id="p1716401218589"><a name="p1716401218589"></a><a name="p1716401218589"></a>For details about the related commands, see <a href="which-commands-are-supported-or-restricted-by-dds.md">Which Commands are Supported or Restricted by DDS?</a></p>
</td>
</tr>
<tr id="row62985361123535"><td class="cellrowborder" valign="top" width="27.26%" headers="mcps1.2.3.1.1 "><p id="p1540641123535"><a name="p1540641123535"></a><a name="p1540641123535"></a>Setting database parameters</p>
</td>
<td class="cellrowborder" valign="top" width="72.74000000000001%" headers="mcps1.2.3.1.2 "><p id="p3859309423"><a name="p3859309423"></a><a name="p3859309423"></a></p>
<p id="p159333074217"><a name="p159333074217"></a><a name="p159333074217"></a></p>
<p id="p109814306422"><a name="p109814306422"></a><a name="p109814306422"></a>Most database parameters in the parameter groups you created can be modified. For details, see section <a href="editing-a-parameter-group.md">Editing a Parameter Group</a>.</p>
<p id="p51021730164220"><a name="p51021730164220"></a><a name="p51021730164220"></a></p>
</td>
</tr>
<tr id="row19812839123535"><td class="cellrowborder" valign="top" width="27.26%" headers="mcps1.2.3.1.1 "><p id="p61336152123535"><a name="p61336152123535"></a><a name="p61336152123535"></a>Migrating data</p>
</td>
<td class="cellrowborder" valign="top" width="72.74000000000001%" headers="mcps1.2.3.1.2 "><p id="p52021072133834"><a name="p52021072133834"></a><a name="p52021072133834"></a>You can use command line tools, including mongoexport and mongoimport, to migrate data. For details, see section <a href="migrating-data.md">Migrating Data</a>.</p>
</td>
</tr>
<tr id="row18357798134159"><td class="cellrowborder" valign="top" width="27.26%" headers="mcps1.2.3.1.1 "><p id="p255375813428"><a name="p255375813428"></a><a name="p255375813428"></a>Storage engine</p>
</td>
<td class="cellrowborder" valign="top" width="72.74000000000001%" headers="mcps1.2.3.1.2 "><p id="p2528698134215"><a name="p2528698134215"></a><a name="p2528698134215"></a>The WiredTiger storage engine is supported.</p>
</td>
</tr>
<tr id="row43544108123535"><td class="cellrowborder" valign="top" width="27.26%" headers="mcps1.2.3.1.1 "><p id="p37411822123535"><a name="p37411822123535"></a><a name="p37411822123535"></a>Restarting a DB instance or a node</p>
</td>
<td class="cellrowborder" valign="top" width="72.74000000000001%" headers="mcps1.2.3.1.2 "><p id="p41132837123535"><a name="p41132837123535"></a><a name="p41132837123535"></a>A DDS DB instance must be restarted on the DDS console.</p>
</td>
</tr>
<tr id="row27804808123535"><td class="cellrowborder" valign="top" width="27.26%" headers="mcps1.2.3.1.1 "><p id="p37597003123535"><a name="p37597003123535"></a><a name="p37597003123535"></a>Viewing DDS backup files</p>
</td>
<td class="cellrowborder" valign="top" width="72.74000000000001%" headers="mcps1.2.3.1.2 "><p id="p63693518173"><a name="p63693518173"></a><a name="p63693518173"></a>You can download and view the backup files on the DDS console. For details, see section <a href="downloading-backup-files.md">Downloading Backup Files</a>.</p>
</td>
</tr>
</tbody>
</table>

