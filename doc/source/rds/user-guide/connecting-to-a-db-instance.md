# Connecting to a DB Instance<a name="rds_02_0060"></a>

An RDS DB instance can be connected through a private network or a public network.

**Table  1**  RDS connection methods

<a name="table34881931174318"></a>
<table><thead align="left"><tr id="row248916316436"><th class="cellrowborder" valign="top" width="22.772277227722775%" id="mcps1.2.5.1.1"><p id="p94898312434"><a name="p94898312434"></a><a name="p94898312434"></a><strong id="b2661739175512"><a name="b2661739175512"></a><a name="b2661739175512"></a>Connect Through</strong></p>
</th>
<th class="cellrowborder" valign="top" width="22.772277227722775%" id="mcps1.2.5.1.2"><p id="p10489131104311"><a name="p10489131104311"></a><a name="p10489131104311"></a><strong id="b1793194110559"><a name="b1793194110559"></a><a name="b1793194110559"></a>IP Address</strong></p>
</th>
<th class="cellrowborder" valign="top" width="29.7029702970297%" id="mcps1.2.5.1.3"><p id="p5489103154315"><a name="p5489103154315"></a><a name="p5489103154315"></a><strong id="b9504164312554"><a name="b9504164312554"></a><a name="b9504164312554"></a>Scenarios</strong></p>
</th>
<th class="cellrowborder" valign="top" width="24.752475247524753%" id="mcps1.2.5.1.4"><p id="p98541156195517"><a name="p98541156195517"></a><a name="p98541156195517"></a><strong id="a97668864bf874d57b57a1c1492147784"><a name="a97668864bf874d57b57a1c1492147784"></a><a name="a97668864bf874d57b57a1c1492147784"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row248973134318"><td class="cellrowborder" valign="top" width="22.772277227722775%" headers="mcps1.2.5.1.1 "><p id="p48571255124517"><a name="p48571255124517"></a><a name="p48571255124517"></a>Private network</p>
</td>
<td class="cellrowborder" valign="top" width="22.772277227722775%" headers="mcps1.2.5.1.2 "><p id="p15489153115438"><a name="p15489153115438"></a><a name="p15489153115438"></a>Floating IP</p>
</td>
<td class="cellrowborder" valign="top" width="29.7029702970297%" headers="mcps1.2.5.1.3 "><p id="p7735048144619"><a name="p7735048144619"></a><a name="p7735048144619"></a>RDS provides a floating IP address by default.</p>
<p id="p273517483465"><a name="p273517483465"></a><a name="p273517483465"></a>When your applications are deployed on an ECS that is in the same region and VPC as RDS, you are advised to use a floating IP address to connect to RDS DB instance through the ECS.</p>
</td>
<td class="cellrowborder" valign="top" width="24.752475247524753%" headers="mcps1.2.5.1.4 "><a name="ul589414895513"></a><a name="ul589414895513"></a><ul id="ul589414895513"><li>Secure and excellent performance</li><li>Recommended</li></ul>
</td>
</tr>
<tr id="row871255113459"><td class="cellrowborder" valign="top" width="22.772277227722775%" headers="mcps1.2.5.1.1 "><p id="p55021336184516"><a name="p55021336184516"></a><a name="p55021336184516"></a>Public network</p>
</td>
<td class="cellrowborder" valign="top" width="22.772277227722775%" headers="mcps1.2.5.1.2 "><p id="p3714351114515"><a name="p3714351114515"></a><a name="p3714351114515"></a>EIP</p>
</td>
<td class="cellrowborder" valign="top" width="29.7029702970297%" headers="mcps1.2.5.1.3 "><p id="p209631558165410"><a name="p209631558165410"></a><a name="p209631558165410"></a>If you cannot access an RDS DB instance through a floating IP address, bind an EIP to the DB instance and connect the ECS to the DB instance through the EIP.</p>
</td>
<td class="cellrowborder" valign="top" width="24.752475247524753%" headers="mcps1.2.5.1.4 "><a name="ul58856110012"></a><a name="ul58856110012"></a><ul id="ul58856110012"><li>Low security</li><li>To achieve a higher transmission rate and security level, you are advised to migrate your applications to an ECS that is in the same subnet as your RDS DB instance and use a floating IP address to access the DB instance.</li></ul>
</td>
</tr>
</tbody>
</table>

>![](/images/icon-note.gif) **NOTE:**   
>-   VPC: indicates the Virtual Private Cloud.  
>-   ECS: indicates the Elastic Cloud Server.  
>-   If the ECS is in the same VPC subnet as the RDS DB instance, you do not need to apply for an EIP.  

[Figure 1](#fig6120201385414)  illustrates the connection over a private network or a public network.

**Figure  1**  DB instance connection<a name="fig6120201385414"></a>  
![](figures/db-instance-connection.png "db-instance-connection")

