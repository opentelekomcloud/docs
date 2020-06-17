# Connecting to a DB Instance<a name="rds_03_0060"></a>

An RDS DB instance can be connected through a private network or a public network.

**Table  1**  RDS connection methods

<a name="en-us_topic_0193421516_table34881931174318"></a>
<table><thead align="left"><tr id="en-us_topic_0193421516_row248916316436"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.1"><p id="en-us_topic_0193421516_p94898312434"><a name="en-us_topic_0193421516_p94898312434"></a><a name="en-us_topic_0193421516_p94898312434"></a><strong id="b156461945537"><a name="b156461945537"></a><a name="b156461945537"></a>Connect Through</strong></p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.2"><p id="en-us_topic_0193421516_p10489131104311"><a name="en-us_topic_0193421516_p10489131104311"></a><a name="en-us_topic_0193421516_p10489131104311"></a><strong id="b1340619461734"><a name="b1340619461734"></a><a name="b1340619461734"></a>IP Address</strong></p>
</th>
<th class="cellrowborder" valign="top" width="35%" id="mcps1.2.5.1.3"><p id="en-us_topic_0193421516_p5489103154315"><a name="en-us_topic_0193421516_p5489103154315"></a><a name="en-us_topic_0193421516_p5489103154315"></a><strong id="b19366114713317"><a name="b19366114713317"></a><a name="b19366114713317"></a>Scenarios</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="en-us_topic_0193421516_p98541156195517"><a name="en-us_topic_0193421516_p98541156195517"></a><a name="en-us_topic_0193421516_p98541156195517"></a><strong id="b143080488314"><a name="b143080488314"></a><a name="b143080488314"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0193421516_row248973134318"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0193421516_p48571255124517"><a name="en-us_topic_0193421516_p48571255124517"></a><a name="en-us_topic_0193421516_p48571255124517"></a>Private network</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0193421516_p15489153115438"><a name="en-us_topic_0193421516_p15489153115438"></a><a name="en-us_topic_0193421516_p15489153115438"></a>Floating IP</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0193421516_p7735048144619"><a name="en-us_topic_0193421516_p7735048144619"></a><a name="en-us_topic_0193421516_p7735048144619"></a>RDS provides a floating IP address by default.</p>
<p id="en-us_topic_0193421516_p273517483465"><a name="en-us_topic_0193421516_p273517483465"></a><a name="en-us_topic_0193421516_p273517483465"></a>When your applications are deployed on an ECS that is in the same region and VPC as RDS, you are advised to use a floating IP address to connect to RDS DB instance through the ECS.</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0193421516_ul589414895513"></a><a name="en-us_topic_0193421516_ul589414895513"></a><ul id="en-us_topic_0193421516_ul589414895513"><li>Secure and excellent performance</li><li>Recommended</li></ul>
</td>
</tr>
<tr id="en-us_topic_0193421516_row871255113459"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0193421516_p55021336184516"><a name="en-us_topic_0193421516_p55021336184516"></a><a name="en-us_topic_0193421516_p55021336184516"></a>Public network</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0193421516_p3714351114515"><a name="en-us_topic_0193421516_p3714351114515"></a><a name="en-us_topic_0193421516_p3714351114515"></a>EIP</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0193421516_p209631558165410"><a name="en-us_topic_0193421516_p209631558165410"></a><a name="en-us_topic_0193421516_p209631558165410"></a>If you cannot access an RDS DB instance through a floating IP address, bind an EIP to the DB instance and connect the ECS to the DB instance through the EIP.</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0193421516_ul58856110012"></a><a name="en-us_topic_0193421516_ul58856110012"></a><ul id="en-us_topic_0193421516_ul58856110012"><li>Low security</li><li>To achieve a higher transmission rate and security level, you are advised to migrate your applications to an ECS that is in the same subnet as your RDS DB instance and use a floating IP address to access the DB instance.</li></ul>
</td>
</tr>
</tbody>
</table>

>![](/images/icon-note.gif) **NOTE:**   
>-   VPC: indicates the Virtual Private Cloud.  
>-   ECS: indicates the Elastic Cloud Server.  
>-   If the ECS is in the same VPC subnet as the RDS DB instance, you do not need to apply for an EIP.  

[Figure 1](#en-us_topic_0193421516_fig6120201385414)  illustrates the connection over a private network or a public network.

**Figure  1**  DB instance connection<a name="en-us_topic_0193421516_fig6120201385414"></a>  
![](figures/db-instance-connection.png "db-instance-connection")

