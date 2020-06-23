# Creating a DCS Instance<a name="EN-US_TOPIC_0237964714"></a>

## Scenario<a name="section19013575"></a>

DCS can be used only after DCS instances are created. DCS supports three types of DCS instances: single-node, master/standby, and cluster.

>![](/images/icon-notice.gif) **NOTICE:**   
>DCS does not provide built-in encryption. Encrypt any sensitive data before transmitting or storing it. The purpose, scope, processing method, and time limits of data processed by DCS must comply with local laws and regulations.  

## Prerequisites<a name="section36904447"></a>

The VPC where the DCS instance to be created is available. Security groups and subnets have been configured for the VPC.

For more information on how to create VPCs, security groups, and subnets, see  [Setting Up Environments](setting-up-environments.md)  or the  _Virtual Private Cloud User Guide_.

## Procedure<a name="section63704574"></a>

1.  Log in to the management console.
2.  Click![](figures/icon-region.png)  in the upper left corner of the management console and select a region and a project.
3.  Click  **Service List**, and choose  **Database**  \>  **Distributed Cache Service**  to launch the DCS console.
4.  In the navigation pane, choose  **Cache Manager**.
5.  On the  **Cache Manager**  page, click  **Create DCS Instance**.
6.  Specify DCS instance parameters, such as the name, AZ, VPC, security group, and subnet.

    **Table  1**  DCS instance parameters

    <a name="table28272749"></a>
    <table><thead align="left"><tr id="row26512460"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.3.1.1"><p id="p25666"><a name="p25666"></a><a name="p25666"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="82%" id="mcps1.2.3.1.2"><p id="p2078992"><a name="p2078992"></a><a name="p2078992"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row34180703"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p17173591"><a name="p17173591"></a><a name="p17173591"></a>Region</p>
    </td>
    <td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p48883615"><a name="p48883615"></a><a name="p48883615"></a>Region in which DCS is located. To select a different region, use the region selector at the upper left of the main menu bar.</p>
    </td>
    </tr>
    <tr id="row37299352"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p1348700"><a name="p1348700"></a><a name="p1348700"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p42135876"><a name="p42135876"></a><a name="p42135876"></a>Name of the new DCS instance.</p>
    <p id="p43678569"><a name="p43678569"></a><a name="p43678569"></a>A DCS instance name cannot be left unspecified and must:</p>
    <a name="ul57562809"></a><a name="ul57562809"></a><ul id="ul57562809"><li>Consist of 4 to 64 characters.</li><li>Consist of only letters, digits, hyphens (-), and underscores (_).</li><li>Start with an uppercase or lowercase letter.</li></ul>
    </td>
    </tr>
    <tr id="row48014184"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p63943666"><a name="p63943666"></a><a name="p63943666"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p12054440"><a name="p12054440"></a><a name="p12054440"></a>Description of the new DCS instance.</p>
    </td>
    </tr>
    <tr id="row41381104"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p63535124"><a name="p63535124"></a><a name="p63535124"></a>Cache Engine</p>
    </td>
    <td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p46071449"><a name="p46071449"></a><a name="p46071449"></a>Cache engine used. Currently supported: <strong id="b11989863"><a name="b11989863"></a><a name="b11989863"></a>Redis</strong>.</p>
    </td>
    </tr>
    <tr id="row40799911"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p16458469"><a name="p16458469"></a><a name="p16458469"></a>Version</p>
    </td>
    <td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p58067579"><a name="p58067579"></a><a name="p58067579"></a>Cache engine version.</p>
    </td>
    </tr>
    <tr id="row52846167"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p52681125"><a name="p52681125"></a><a name="p52681125"></a>Instance Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p39312736"><a name="p39312736"></a><a name="p39312736"></a>Type of the DCS instance being created.</p>
    <p id="p18270305"><a name="p18270305"></a><a name="p18270305"></a>Currently, single-node, master/standby, and cluster types are supported.</p>
    <p id="p30215023"><a name="p30215023"></a><a name="p30215023"></a>Select an instance type based on your service scenario. For more information, see <a href="dcs.md#li4080300">DCS Instance Types</a>.</p>
    <div class="note" id="note31497787"><a name="note31497787"></a><a name="note31497787"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p class="NotesTextinTable" id="p15044627"><a name="p15044627"></a><a name="p15044627"></a>Cluster DCS instances do not support cross-VPC access through VPC peering connections.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row1183915"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p28788263"><a name="p28788263"></a><a name="p28788263"></a>AZ</p>
    </td>
    <td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p50147992"><a name="p50147992"></a><a name="p50147992"></a>AZ in which the new DCS instance resides.</p>
    </td>
    </tr>
    <tr id="row48678752"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p50664859"><a name="p50664859"></a><a name="p50664859"></a>Standby AZ</p>
    </td>
    <td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p10212927"><a name="p10212927"></a><a name="p10212927"></a>Standby AZ in which the new DCS instance resides.</p>
    <div class="note" id="note24807479"><a name="note24807479"></a><a name="note24807479"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p class="NotesTextinTable" id="p21940722"><a name="p21940722"></a><a name="p21940722"></a>This parameter is displayed if both of the following conditions are true:</p>
    <a name="ul63248778"></a><a name="ul63248778"></a><ul id="ul63248778"><li>The DCS instance is of the master/standby or cluster type.</li><li>Multiple AZs exist.</li></ul>
    </div></div>
    </td>
    </tr>
    <tr id="row4570028"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p34627969"><a name="p34627969"></a><a name="p34627969"></a>Instance Specification</p>
    </td>
    <td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p53402119"><a name="p53402119"></a><a name="p53402119"></a>Total memory of the new DCS instance.</p>
    <p id="p10857028"><a name="p10857028"></a><a name="p10857028"></a>Value:</p>
    <a name="ul30604389"></a><a name="ul30604389"></a><ul id="ul30604389"><li>64, 128, 256, or 512 GB if the DCS instance is in cluster mode</li><li>2, 4, 8, 16, 32, or 64 GB if the DCS instance is in single-node or master/standby mode</li></ul>
    <p id="p30457452"><a name="p30457452"></a><a name="p30457452"></a>By default, each user can create a maximum of five DCS instances and use a total of 400 GB memory.</p>
    <p id="p5681612"><a name="p5681612"></a><a name="p5681612"></a>When creating a DCS instance on the DCS console, available free memory is listed below the <strong id="b16936555182813"><a name="b16936555182813"></a><a name="b16936555182813"></a>Instance Specification</strong> field. If you need more memory, click <strong id="b57557412"><a name="b57557412"></a><a name="b57557412"></a>Increase quota</strong> below the <strong id="b48254661"><a name="b48254661"></a><a name="b48254661"></a>Instance Specification</strong> field and contact customer service. For more information, see <a href="https://docs.otc.t-systems.com/faq/iaas/en-us_topic_0040259342.html" target="_blank" rel="noopener noreferrer">How Can I Apply for a Higher Quota?</a>.</p>
    </td>
    </tr>
    <tr id="row16313497"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p46324881"><a name="p46324881"></a><a name="p46324881"></a>VPC</p>
    </td>
    <td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p61327894"><a name="p61327894"></a><a name="p61327894"></a>VPC in which the new DCS instance resides.</p>
    <p id="p15080136"><a name="p15080136"></a><a name="p15080136"></a>A VPC provides an isolated, user-configurable, and user-manageable virtual network environment for your DCS instances.</p>
    <p id="p1503503"><a name="p1503503"></a><a name="p1503503"></a>Click <strong id="b13531531"><a name="b13531531"></a><a name="b13531531"></a>View VPC</strong> to show more details of the chosen VPC, including security group rules.</p>
    </td>
    </tr>
    <tr id="row54674917"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p66592127"><a name="p66592127"></a><a name="p66592127"></a>Subnet</p>
    </td>
    <td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p25253189"><a name="p25253189"></a><a name="p25253189"></a>Name and IP address range of the subnet in which the new DCS instance resides.</p>
    </td>
    </tr>
    <tr id="row25952117"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p21746729"><a name="p21746729"></a><a name="p21746729"></a>IP Address</p>
    </td>
    <td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p16654654"><a name="p16654654"></a><a name="p16654654"></a>Select either <strong id="b15674164"><a name="b15674164"></a><a name="b15674164"></a>Automatically allocate</strong> or <strong id="b6849756"><a name="b6849756"></a><a name="b6849756"></a>Manually assign</strong>.</p>
    <a name="ul61647805"></a><a name="ul61647805"></a><ul id="ul61647805"><li>If <strong id="b27416314"><a name="b27416314"></a><a name="b27416314"></a>Automatically allocate</strong> is selected, an available IP address in the current subnet is randomly allocated.</li><li>If <strong id="b6128980"><a name="b6128980"></a><a name="b6128980"></a>Manually assign</strong> is selected, a text box is displayed. You can enter an available IP address in the current subnet. Click <strong id="b55160823"><a name="b55160823"></a><a name="b55160823"></a>View In-Use IP Address</strong> to view IP addresses that are already in use in the current subnet.</li></ul>
    </td>
    </tr>
    <tr id="row26685362"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p14030717"><a name="p14030717"></a><a name="p14030717"></a>Security Group</p>
    </td>
    <td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p62746268"><a name="p62746268"></a><a name="p62746268"></a>Security group that controls access to the new DCS instance.</p>
    <p id="p27845503"><a name="p27845503"></a><a name="p27845503"></a>A security group is a set of access control rules that implements access control for mutually trusted ECSs with the same security protection requirements in the same VPC.</p>
    </td>
    </tr>
    <tr id="row49282936"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p32494840"><a name="p32494840"></a><a name="p32494840"></a>Password</p>
    </td>
    <td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p14836356"><a name="p14836356"></a><a name="p14836356"></a>Password required for accessing the new DCS instance.</p>
    <div class="note" id="note66418347"><a name="note66418347"></a><a name="note66418347"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p class="NotesTextinTable" id="p60894213"><a name="p60894213"></a><a name="p60894213"></a>For security purposes, the system prompts you to enter an instance-specific password when you are accessing the DCS instance. Keep your instance password secure and change it periodically.</p>
    </div></div>
    <p id="p11177013"><a name="p11177013"></a><a name="p11177013"></a>Passwords cannot be left unspecified and must:</p>
    <a name="ul33484259"></a><a name="ul33484259"></a><ul id="ul33484259"><li>Consist of 8 to 32 characters.</li><li>Contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters (`~!@#$%^&amp;*()-_=+\|[{}]:'",&lt;.&gt;/?).</li></ul>
    </td>
    </tr>
    <tr id="row49507636"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p50695543"><a name="p50695543"></a><a name="p50695543"></a>Time Window</p>
    </td>
    <td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p12698356"><a name="p12698356"></a><a name="p12698356"></a>Time range for any scheduled maintenance activities to occur for cache nodes of this DCS instance.</p>
    <p id="p47176343"><a name="p47176343"></a><a name="p47176343"></a>Values:</p>
    <a name="ul21933905"></a><a name="ul21933905"></a><ul id="ul21933905"><li>22:00-02:00</li><li>02:00-06:00</li><li>06:00-10:00</li><li>10:00-14:00</li><li>14:00-18:00</li><li>18:00-22:00</li></ul>
    </td>
    </tr>
    <tr id="row49336210"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p36810105"><a name="p36810105"></a><a name="p36810105"></a>Backup Policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p28828491"><a name="p28828491"></a><a name="p28828491"></a>Data backup policy. This parameter is displayed only when the instance type is master/standby. For more information on how to configure a backup policy, see <a href="configuring-a-backup-policy.md">Configuring a Backup Policy</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

7.  Click  **Create Now**.

    The  **Confirm**  tab page is displayed, providing information about the new DCS instance, including the instance name, cache engine version, and instance specifications.

8.  On the  **Confirm**  tab page, review the instance information and click  **Submit**.
9.  After the new DCS instance has been created, return to the  **Cache Manager**  page to view and manage your DCS instances.

    It takes 5 to 15 minutes to create a DCS instance. However, it will take up to approximately 30 minutes if the DCS instance is in cluster mode.

    After a DCS instance has been successfully created, it enters the  **Running**  state by default.

    >![](/images/icon-note.gif) **NOTE:**   
    >-   If the new DCS instance failed to be created, delete the unsuccessful instance creation task by following the procedure in  [Deleting Instance Creation Tasks That Have Failed to Run](deleting-dcs-instances.md#section61981843115915). Then, create the DCS instance again. If the DCS instance still fails to be created, contact customer service.  
    >-   There is the management plane and the tenant plane. The tenant plane is also called the pod zone. During the creation of a DCS instance, a VM is created in the pod zone. If the instance creation fails, the instance status changes to  **Faulty**, and the error message "Failed to connect to the instance. Network exceptions may have occurred in the pod zone." is displayed, indicating that the management plane cannot be connected to the tenant plane.  


