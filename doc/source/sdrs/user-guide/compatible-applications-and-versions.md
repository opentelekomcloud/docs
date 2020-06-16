# Compatible Applications and Versions<a name="sdrs_pro_0009"></a>

SDRS ensures data consistency but not application consistency. The following table lists the applications and application versions that have passed the verification in the lab. Services of these applications can start properly after you perform a planned failover or failover.

**Table  1**  Supported applications and versions

<a name="table1697315153819"></a>
<table><thead align="left"><tr id="row1497375103811"><th class="cellrowborder" valign="top" width="32.41%" id="mcps1.2.3.1.1"><p id="p19742516386"><a name="p19742516386"></a><a name="p19742516386"></a>Application</p>
</th>
<th class="cellrowborder" valign="top" width="67.58999999999999%" id="mcps1.2.3.1.2"><p id="p097415513388"><a name="p097415513388"></a><a name="p097415513388"></a>Version</p>
</th>
</tr>
</thead>
<tbody><tr id="row8974251153812"><td class="cellrowborder" rowspan="2" valign="top" width="32.41%" headers="mcps1.2.3.1.1 "><p id="p27711839193917"><a name="p27711839193917"></a><a name="p27711839193917"></a>Oracle</p>
</td>
<td class="cellrowborder" valign="top" width="67.58999999999999%" headers="mcps1.2.3.1.2 "><p id="p19771113912394"><a name="p19771113912394"></a><a name="p19771113912394"></a>Oracle Database 11g Release 2 (11.2.0.4)</p>
<p id="p157711939153911"><a name="p157711939153911"></a><a name="p157711939153911"></a>Oracle Grid 11g Release 2 (11.2.0.4)</p>
</td>
</tr>
<tr id="row11974175120385"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p19771173915399"><a name="p19771173915399"></a><a name="p19771173915399"></a>Oracle Database 12c Release 2 (12.2.0.1.0)</p>
<p id="p87711039173912"><a name="p87711039173912"></a><a name="p87711039173912"></a>Oracle Grid 12c Release 2 (12.2.0.1.0)</p>
</td>
</tr>
<tr id="row9974155120384"><td class="cellrowborder" valign="top" width="32.41%" headers="mcps1.2.3.1.1 "><p id="p7771193911399"><a name="p7771193911399"></a><a name="p7771193911399"></a>SQL Server</p>
</td>
<td class="cellrowborder" valign="top" width="67.58999999999999%" headers="mcps1.2.3.1.2 "><p id="p17711139143918"><a name="p17711139143918"></a><a name="p17711139143918"></a>Microsoft SQL Server 2012</p>
</td>
</tr>
<tr id="row169741651153810"><td class="cellrowborder" valign="top" width="32.41%" headers="mcps1.2.3.1.1 "><p id="p18771163973912"><a name="p18771163973912"></a><a name="p18771163973912"></a>WSFC</p>
</td>
<td class="cellrowborder" valign="top" width="67.58999999999999%" headers="mcps1.2.3.1.2 "><p id="p1577153910390"><a name="p1577153910390"></a><a name="p1577153910390"></a>Windows Server Failover Cluster on Windows Server 2008R2/2012R2/2016</p>
</td>
</tr>
<tr id="row17974145163813"><td class="cellrowborder" valign="top" width="32.41%" headers="mcps1.2.3.1.1 "><p id="p37711839103912"><a name="p37711839103912"></a><a name="p37711839103912"></a>MySQL</p>
</td>
<td class="cellrowborder" valign="top" width="67.58999999999999%" headers="mcps1.2.3.1.2 "><p id="p2771103943920"><a name="p2771103943920"></a><a name="p2771103943920"></a>MySQL 5.7.x</p>
</td>
</tr>
<tr id="row1897414516381"><td class="cellrowborder" valign="top" width="32.41%" headers="mcps1.2.3.1.1 "><p id="p477113917391"><a name="p477113917391"></a><a name="p477113917391"></a>Zookeeper</p>
</td>
<td class="cellrowborder" valign="top" width="67.58999999999999%" headers="mcps1.2.3.1.2 "><p id="p1771183963911"><a name="p1771183963911"></a><a name="p1771183963911"></a>Zookeeper 3.4.5</p>
</td>
</tr>
<tr id="row12974125133810"><td class="cellrowborder" valign="top" width="32.41%" headers="mcps1.2.3.1.1 "><p id="p17719391395"><a name="p17719391395"></a><a name="p17719391395"></a>Hadoop</p>
</td>
<td class="cellrowborder" valign="top" width="67.58999999999999%" headers="mcps1.2.3.1.2 "><p id="p2771339173915"><a name="p2771339173915"></a><a name="p2771339173915"></a>Hadoop 3.0</p>
</td>
</tr>
</tbody>
</table>

>![](/images/icon-notice.gif) **NOTICE:**   
>-   For servers with Cloud-Init/Cloudbase-Init installed, the system automatically changes the configuration information, such as the host name, password, and host fingerprint, after a planned failover. Therefore, you need to uninstall or stop the Cloud-init service after the application is deployed.  
>-   Applications and versions listed in  [Table 1](#table1697315153819)  will be continuously updated.  

