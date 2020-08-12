# Creating a DCS Instance<a name="en-us_topic_0054235810"></a>

## Scenario<a name="section48889850"></a>

DCS can be used only after DCS instances are created. DCS supports three types of DCS instances: single-node, master/standby, and Proxy Cluster.

>![](public_sys-resources/icon-notice.gif) **NOTICE:** 
>DCS does not provide built-in encryption. Encrypt any sensitive data before transmitting or storing it. The purpose, scope, processing method, and time limits of data processed by DCS must comply with local laws and regulations.

## Prerequisites<a name="section37355470"></a>

The VPC where the DCS instance to be created is available. Security groups and subnets have been configured for the VPC.

For more information on how to create VPCs, security groups, and subnets, see  [Setting Up Environments](setting-up-environments.md) or the  _Virtual Private Cloud User Guide_.

## Procedure<a name="section654914"></a>

1.  Log in to the management console.
2.  Click  ![](figures/project.png) in the upper left corner of the management console and select a region and a project.
3.  Click  **Service List**, and choose **Database** \> **Distributed Cache Service**  to launch the DCS console.
4.  Click **Create DCS Instance**.
5.  Specify DCS instance parameters, such as the name, AZ, VPC, security group, and subnet.

    **Table  1**  DCS instance parameters

    <a name="table1612926193015"></a>
    <table><thead align="left"><tr id="row5933206518728"><th class="cellrowborder" valign="top" width="17.03%" id="mcps1.2.3.1.1"><p id="p1632215115318"><a name="p1632215115318"></a><a name="p1632215115318"></a><strong id="b432215163119"><a name="b432215163119"></a><a name="b432215163119"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="82.97%" id="mcps1.2.3.1.2"><p id="p2032241123112"><a name="p2032241123112"></a><a name="p2032241123112"></a><strong id="b113226163116"><a name="b113226163116"></a><a name="b113226163116"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row153681361123"><td class="cellrowborder" valign="top" width="17.03%" headers="mcps1.2.3.1.1 "><p id="p8116813183210"><a name="p8116813183210"></a><a name="p8116813183210"></a>Region</p>
    </td>
    <td class="cellrowborder" valign="top" width="82.97%" headers="mcps1.2.3.1.2 "><p id="p131168131320"><a name="p131168131320"></a><a name="p131168131320"></a>Region in which DCS is located. To select a different region, use the region selector at the upper left of the main menu bar.</p>
    </td>
    </tr>
    <tr id="row1267964613916"><td class="cellrowborder" valign="top" width="17.03%" headers="mcps1.2.3.1.1 "><p id="p1578164103312"><a name="p1578164103312"></a><a name="p1578164103312"></a>Cache Engine</p>
    </td>
    <td class="cellrowborder" valign="top" width="82.97%" headers="mcps1.2.3.1.2 "><p id="p6399183713512"><a name="p6399183713512"></a><a name="p6399183713512"></a>Cache engine used. Currently supported: <strong id="b5399193712511"><a name="b5399193712511"></a><a name="b5399193712511"></a>Redis</strong>.</p>
    </td>
    </tr>
    <tr id="row7166652194"><td class="cellrowborder" valign="top" width="17.03%" headers="mcps1.2.3.1.1 "><p id="p5613947218728"><a name="p5613947218728"></a><a name="p5613947218728"></a>Version</p>
    </td>
    <td class="cellrowborder" valign="top" width="82.97%" headers="mcps1.2.3.1.2 "><p id="p1965113231616"><a name="p1965113231616"></a><a name="p1965113231616"></a>Currently, only Redis 3.0 is supported.</p>
    </td>
    </tr>
    <tr id="row1516616521097"><td class="cellrowborder" valign="top" width="17.03%" headers="mcps1.2.3.1.1 "><p id="p67851128371"><a name="p67851128371"></a><a name="p67851128371"></a>Instance Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="82.97%" headers="mcps1.2.3.1.2 "><p id="p126326399375"><a name="p126326399375"></a><a name="p126326399375"></a>Type of the DCS instance being created.</p>
    <p id="p369017404"><a name="p369017404"></a><a name="p369017404"></a>Single-node, master/standby, and Proxy Cluster types are supported.</p>
    </td>
    </tr>
    <tr id="row113682295213"><td class="cellrowborder" valign="top" width="17.03%" headers="mcps1.2.3.1.1 "><p id="p64171416133812"><a name="p64171416133812"></a><a name="p64171416133812"></a>AZ</p>
    </td>
    <td class="cellrowborder" valign="top" width="82.97%" headers="mcps1.2.3.1.2 "><p id="p5417181612383"><a name="p5417181612383"></a><a name="p5417181612383"></a>AZ in which the new DCS instance resides. If the instance type is master/standby or Proxy Cluster, this parameter is displayed as <strong id="b4851195811614"><a name="b4851195811614"></a><a name="b4851195811614"></a>Master AZ</strong>.</p>
    </td>
    </tr>
    <tr id="row5850290918728"><td class="cellrowborder" valign="top" width="17.03%" headers="mcps1.2.3.1.1 "><p id="p541711663810"><a name="p541711663810"></a><a name="p541711663810"></a>Standby AZ</p>
    </td>
    <td class="cellrowborder" valign="top" width="82.97%" headers="mcps1.2.3.1.2 "><p id="p1841741623818"><a name="p1841741623818"></a><a name="p1841741623818"></a>Standby AZ in which the new DCS instance resides.</p>
    <p id="p28264691214"><a name="p28264691214"></a><a name="p28264691214"></a>If the instance type is master/standby or Proxy Cluster, <strong id="b74231751194416"><a name="b74231751194416"></a><a name="b74231751194416"></a>Standby AZ</strong> is displayed. Select a standby AZ for the standby node of the instance.</p>
    </td>
    </tr>
    <tr id="row1286332818728"><td class="cellrowborder" valign="top" width="17.03%" headers="mcps1.2.3.1.1 "><p id="p5731035618728"><a name="p5731035618728"></a><a name="p5731035618728"></a>Instance Specification</p>
    </td>
    <td class="cellrowborder" valign="top" width="82.97%" headers="mcps1.2.3.1.2 "><p id="p16149104718389"><a name="p16149104718389"></a><a name="p16149104718389"></a>Total memory of the new DCS instance.</p>
    <a name="ul432662513395"></a><a name="ul432662513395"></a><ul id="ul432662513395"><li>2, 4, 8, 16, 32, or 64 GB if the DCS instance is in single-node or master/standby mode</li></ul>
    <a name="ul1015018475384"></a><a name="ul1015018475384"></a><ul id="ul1015018475384"><li>64, 128, 256 or 512 GB if the DCS instance is in Proxy Cluster mode</li></ul>
    <p id="p615074783818"><a name="p615074783818"></a><a name="p615074783818"></a>When creating a DCS instance on the DCS console, available free memory is listed below the <strong id="b16150547123815"><a name="b16150547123815"></a><a name="b16150547123815"></a>Instance Specification </strong>field. If you need more memory, click&nbsp;<strong id="b161505474383"><a name="b161505474383"></a><a name="b161505474383"></a>Increase quota</strong>&nbsp;below the&nbsp;<strong id="b1915044733813"><a name="b1915044733813"></a><a name="b1915044733813"></a>Instance Specification</strong>&nbsp;field and contact customer service. </p>
    </td>
    </tr>
    <tr id="row9592143451919"><td class="cellrowborder" valign="top" width="17.03%" headers="mcps1.2.3.1.1 "><p id="p0355176194516"><a name="p0355176194516"></a><a name="p0355176194516"></a>VPC</p>
    </td>
    <td class="cellrowborder" valign="top" width="82.97%" headers="mcps1.2.3.1.2 "><p id="li14333139771p0"><a name="li14333139771p0"></a><a name="li14333139771p0"></a>Select a created VPC, subnet, and specify the IP address.</p>
    </td>
    </tr>
    <tr id="row115921134201915"><td class="cellrowborder" valign="top" width="17.03%" headers="mcps1.2.3.1.1 "><p id="p13454122314456"><a name="p13454122314456"></a><a name="p13454122314456"></a>Security Group</p>
    </td>
    <td class="cellrowborder" valign="top" width="82.97%" headers="mcps1.2.3.1.2 "><p id="p1454723194519"><a name="p1454723194519"></a><a name="p1454723194519"></a>Security group that controls access to the new DCS instance.</p>
    <p id="p15454623134510"><a name="p15454623134510"></a><a name="p15454623134510"></a>A security group is a set of access control rules that implements access control for mutually trusted ECSs with the same security protection requirements in the same VPC.</p>
    </td>
    </tr>
    <tr id="row106362162119"><td class="cellrowborder" valign="top" width="17.03%" headers="mcps1.2.3.1.1 "><p id="p207601405451"><a name="p207601405451"></a><a name="p207601405451"></a>Password</p>
    </td>
    <td class="cellrowborder" valign="top" width="82.97%" headers="mcps1.2.3.1.2 "><p id="p1576074012453"><a name="p1576074012453"></a><a name="p1576074012453"></a>Password required for accessing the new DCS instance.</p>
    <div class="note" id="note187606402454"><a name="note187606402454"></a><a name="note187606402454"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p476184010458"><a name="p476184010458"></a><a name="p476184010458"></a>For security purposes, the system prompts you to enter an instance-specific password when you are accessing the DCS instance. Keep your instance password secure and change it periodically.</p>
    </div></div>
    <p id="p137611040194516"><a name="p137611040194516"></a><a name="p137611040194516"></a>Passwords cannot be left unspecified and must:</p>
    <a name="ul5761184094510"></a><a name="ul5761184094510"></a><ul id="ul5761184094510"><li><span>Consist of </span>8 to 32 characters.</li><li><span>Contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters </span>(`~!@#$^&amp;*()-_=+\|{}:,&lt;.&gt;/?).</li></ul>
    </td>
    </tr>
    <tr id="row843819295217"><td class="cellrowborder" colspan="2" valign="top" headers="mcps1.2.3.1.1 mcps1.2.3.1.2 "><p id="p741553422110"><a name="p741553422110"></a><a name="p741553422110"></a><strong id="b78101317555"><a name="b78101317555"></a><a name="b78101317555"></a>More Settings</strong></p>
    </td>
    </tr>
    <tr id="row10641524217"><td class="cellrowborder" valign="top" width="17.03%" headers="mcps1.2.3.1.1 "><p id="p4116798118728"><a name="p4116798118728"></a><a name="p4116798118728"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="82.97%" headers="mcps1.2.3.1.2 "><p id="p984394814472"><a name="p984394814472"></a><a name="p984394814472"></a>Name of the new DCS instance.</p>
    <p id="p28431348144719"><a name="p28431348144719"></a><a name="p28431348144719"></a>A DCS instance name cannot be left unspecified and must:</p>
    <a name="ul13843154813472"></a><a name="ul13843154813472"></a><ul id="ul13843154813472"><li>Consist of 4 to 64 characters.</li><li>Consist of only letters, digits, hyphens (-), and underscores (_).</li><li>Start with an uppercase or lowercase letter.</li></ul>
    </td>
    </tr>
    <tr id="row2846066118728"><td class="cellrowborder" valign="top" width="17.03%" headers="mcps1.2.3.1.1 "><p id="p5676413618728"><a name="p5676413618728"></a><a name="p5676413618728"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="82.97%" headers="mcps1.2.3.1.2 "><p id="p2843174812474"><a name="p2843174812474"></a><a name="p2843174812474"></a>Description of the new DCS instance.</p>
    </td>
    </tr>
    <tr id="row55532325104357"><td class="cellrowborder" valign="top" width="17.03%" headers="mcps1.2.3.1.1 "><p id="p296021334717"><a name="p296021334717"></a><a name="p296021334717"></a>Auto Backup</p>
    </td>
    <td class="cellrowborder" valign="top" width="82.97%" headers="mcps1.2.3.1.2 "><p id="p1192184223411"><a name="p1192184223411"></a><a name="p1192184223411"></a>Data backup policy. This parameter is displayed only when the instance type is master/standby or Proxy Cluster. For more information on how to configure a backup policy, see&nbsp;<a href="configuring-a-backup-policy.md">Configuring a Backup Policy</a>.</p>
    </td>
    </tr>
    <tr id="row6747134473311"><td class="cellrowborder" valign="top" width="17.03%" headers="mcps1.2.3.1.1 "><p id="p3799172814713"><a name="p3799172814713"></a><a name="p3799172814713"></a>Maintenance</p>
    </td>
    <td class="cellrowborder" valign="top" width="82.97%" headers="mcps1.2.3.1.2 "><p id="p14799132874719"><a name="p14799132874719"></a><a name="p14799132874719"></a>Time range for any scheduled maintenance activities to occur for cache nodes of this DCS instance.</p>
    <p id="p57999284475"><a name="p57999284475"></a><a name="p57999284475"></a>Values:</p>
    <a name="ul197995287476"></a><a name="ul197995287476"></a><ul id="ul197995287476"><li>02:00-06:00</li><li>06:00-10:00</li><li>10:00-14:00</li><li>14:00-18:00</li><li>18:00-22:00</li><li>22:00-02:00</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

6.  Click **Create Now**.

    The displayed page shows the instance information you have specified.

7.  Confirm the instance information and click **Submit**.
8.  After the new DCS instance has been created, return to the  **Cache Manager**  page to view and manage your DCS instances.

    It takes 5 to 15 minutes to create a DCS instance. However, it will take up to approximately 30 minutes if the DCS instance is in Proxy Cluster mode.

    After a DCS instance has been successfully created, it enters the  **Running**  state by default.

    >![](public_sys-resources/icon-note.gif) **NOTE:** 
    >-   If the new DCS instance failed to be created, delete the unsuccessful instance creation task by following the procedure in  [Deleting Instance Creation Tasks That Have Failed to Run](deleting-dcs-instances.md#section61981843115915). Then, create the DCS instance again. If the DCS instance still fails to be created, contact customer service.
    >-   There is the management plane and the tenant plane. The tenant plane is also called the pod zone. During the creation of a DCS instance, a VM is created in the pod zone. If the instance creation fails, the instance status changes to  **Faulty**, and the error message "Failed to connect to the instance. Network exceptions may have occurred in the pod zone." is displayed, indicating that the management plane cannot be connected to the tenant plane.


