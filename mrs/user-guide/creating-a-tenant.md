# Creating a Tenant<a name="EN-US_TOPIC_0125375708"></a>

## Scenario<a name="section54537506192610"></a>

You can create a tenant on MRS Manager to specify the resource usage.

## Prerequisites<a name="section57491743192637"></a>

-   A tenant name has been planned. The name must not be the same as that of a role or Yarn queue that exists in the current cluster.
-   If a tenant requires storage resources, a storage directory has been planned in advance based on service requirements, and the planned directory does not exist under the HDFS directory.
-   The resources that can be allocated to the current tenant have been planned and the sum of the resource percentages of direct sub-tenants under the parent tenant at every level does not exceed 100%.

## Procedure<a name="section34570625192643"></a>

1.  On MRS Manager, click  **Tenant**.
2.  Click  **Create Tenant**. On the displayed page, configure tenant attributes according to the following table.

    **Table  1**  Tenant parameters

    <a name="table269395619271"></a>
    <table><thead align="left"><tr id="row2745194719271"><th class="cellrowborder" valign="top" width="32.5%" id="mcps1.2.3.1.1"><p id="p901521119271"><a name="p901521119271"></a><a name="p901521119271"></a><strong id="b1074858819279"><a name="b1074858819279"></a><a name="b1074858819279"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="67.5%" id="mcps1.2.3.1.2"><p id="p5914350019271"><a name="p5914350019271"></a><a name="p5914350019271"></a><strong id="b6532929019279"><a name="b6532929019279"></a><a name="b6532929019279"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2589419719271"><td class="cellrowborder" valign="top" width="32.5%" headers="mcps1.2.3.1.1 "><p id="p1705524719271"><a name="p1705524719271"></a><a name="p1705524719271"></a><span class="parmname" id="parmname49124446192359"><a name="parmname49124446192359"></a><a name="parmname49124446192359"></a><b>Name</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="67.5%" headers="mcps1.2.3.1.2 "><p id="p3929779419271"><a name="p3929779419271"></a><a name="p3929779419271"></a>Specifies the name of the current tenant. The value consists of 3 to 20 characters, and can contain letters, digits, and underscores (_).</p>
    </td>
    </tr>
    <tr id="row1813582819271"><td class="cellrowborder" valign="top" width="32.5%" headers="mcps1.2.3.1.1 "><p id="p5971593419271"><a name="p5971593419271"></a><a name="p5971593419271"></a><span class="parmname" id="parmname3121375819244"><a name="parmname3121375819244"></a><a name="parmname3121375819244"></a><b>Tenant Type</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="67.5%" headers="mcps1.2.3.1.2 "><p id="p515246819271"><a name="p515246819271"></a><a name="p515246819271"></a>The options include <span class="parmvalue" id="parmvalue1303902812031"><a name="parmvalue1303902812031"></a><a name="parmvalue1303902812031"></a><b>Leaf</b></span>&nbsp;and&nbsp;<span class="parmvalue" id="parmvalue45070224115854"><a name="parmvalue45070224115854"></a><a name="parmvalue45070224115854"></a><b>Non-leaf</b></span>. If&nbsp;<span class="parmvalue" id="parmvalue4952837612031"><a name="parmvalue4952837612031"></a><a name="parmvalue4952837612031"></a><b>Leaf</b></span>&nbsp;is selected, the current tenant is a leaf tenant and no sub-tenant can be added. If&nbsp;<span class="parmvalue" id="parmvalue52379591115858"><a name="parmvalue52379591115858"></a><a name="parmvalue52379591115858"></a><b>Non-leaf</b></span> is selected, sub-tenants can be added to the current tenant.</p>
    </td>
    </tr>
    <tr id="row4637222019271"><td class="cellrowborder" valign="top" width="32.5%" headers="mcps1.2.3.1.1 "><p id="p6516233619271"><a name="p6516233619271"></a><a name="p6516233619271"></a><span class="parmname" id="parmname2130366819247"><a name="parmname2130366819247"></a><a name="parmname2130366819247"></a><b>Dynamic Resource</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="67.5%" headers="mcps1.2.3.1.2 "><p id="p4365789319271"><a name="p4365789319271"></a><a name="p4365789319271"></a>Specifies the dynamic computing resources for the current tenant. The system automatically creates a task queue in Yarn and the queue is given the same name as the tenant. If dynamic resources are not <span class="parmvalue" id="parmvalue1012190612031"><a name="parmvalue1012190612031"></a><a name="parmvalue1012190612031"></a><b>Yarn</b></span> resources, the system does not automatically create a task queue.</p>
    </td>
    </tr>
    <tr id="row5737672319271"><td class="cellrowborder" valign="top" width="32.5%" headers="mcps1.2.3.1.1 "><p id="p1700302019271"><a name="p1700302019271"></a><a name="p1700302019271"></a><span class="parmname" id="parmname5742701192411"><a name="parmname5742701192411"></a><a name="parmname5742701192411"></a><b>Default Resource Pool Capacity (%)</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="67.5%" headers="mcps1.2.3.1.2 "><p id="p3506738519271"><a name="p3506738519271"></a><a name="p3506738519271"></a>Specifies the percentage of the computing resources used by the current tenant in the <span class="parmname" id="parmname1786935612031"><a name="parmname1786935612031"></a><a name="parmname1786935612031"></a><b>default</b></span> resource pool.</p>
    </td>
    </tr>
    <tr id="row4717101519271"><td class="cellrowborder" valign="top" width="32.5%" headers="mcps1.2.3.1.1 "><p id="p6275587019271"><a name="p6275587019271"></a><a name="p6275587019271"></a><span class="parmname" id="parmname57924488192413"><a name="parmname57924488192413"></a><a name="parmname57924488192413"></a><b>Default Resource Pool Max. Capacity (%)</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="67.5%" headers="mcps1.2.3.1.2 "><p id="p5006070119271"><a name="p5006070119271"></a><a name="p5006070119271"></a>Specifies the maximum percentage of the computing resources used by the current tenant in the <span class="parmname" id="parmname42806712031"><a name="parmname42806712031"></a><a name="parmname42806712031"></a><b>default</b></span> resource pool.</p>
    </td>
    </tr>
    <tr id="row4789313219271"><td class="cellrowborder" valign="top" width="32.5%" headers="mcps1.2.3.1.1 "><p id="p5413845919271"><a name="p5413845919271"></a><a name="p5413845919271"></a><span class="parmname" id="parmname59066008192420"><a name="parmname59066008192420"></a><a name="parmname59066008192420"></a><b>Storage Resource</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="67.5%" headers="mcps1.2.3.1.2 "><p id="p2313904719271"><a name="p2313904719271"></a><a name="p2313904719271"></a>Specifies the storage resources for the current tenant. The system automatically creates a file folder in the <span class="filepath" id="filepath6050683012031"><a name="filepath6050683012031"></a><a name="filepath6050683012031"></a><b>/tenant</b></span>&nbsp;directory, which is given the same name as the tenant. When the tenant is created, the system automatically creates the&nbsp;<span class="filepath" id="filepath769056112031"><a name="filepath769056112031"></a><a name="filepath769056112031"></a><b>/tenant</b></span>&nbsp;directory under the root directory of HDFS. If storage resources are not&nbsp;<strong id="b1505182718163"><a name="b1505182718163"></a><a name="b1505182718163"></a>HDFS</strong>, the system does not create a storage directory under the root directory of HDFS.</p>
    </td>
    </tr>
    <tr id="row692483119271"><td class="cellrowborder" valign="top" width="32.5%" headers="mcps1.2.3.1.1 "><p id="p2404040019271"><a name="p2404040019271"></a><a name="p2404040019271"></a><span class="parmname" id="parmname49387720192423"><a name="parmname49387720192423"></a><a name="parmname49387720192423"></a><b>Space Quota (MB)</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="67.5%" headers="mcps1.2.3.1.2 "><p id="p111537819271"><a name="p111537819271"></a><a name="p111537819271"></a>Specifies the quota for HDFS storage space used by the current tenant. The value of <span class="parmname" id="parmname213204301471"><a name="parmname213204301471"></a><a name="parmname213204301471"></a><b>Space Quota</b></span>&nbsp;ranges from&nbsp;<span class="parmvalue" id="parmvalue492332591471"><a name="parmvalue492332591471"></a><a name="parmvalue492332591471"></a><b>1</b></span>&nbsp;to&nbsp;<span class="parmvalue" id="parmvalue284710241471"><a name="parmvalue284710241471"></a><a name="parmvalue284710241471"></a><b>8796093022208</b></span> and the unit is MB. This parameter indicates the maximum HDFS storage space that can be used by the tenant, not the actual space used. If the value is greater than the size of the HDFS physical disk, the maximum space available is the full space of the HDFS physical disk.</p>
    <div class="note" id="note17069590164928"><a name="note17069590164928"></a><a name="note17069590164928"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p32992694175822"><a name="p32992694175822"></a><a name="p32992694175822"></a>To ensure data reliability, two more copies of a file are automatically generated when the file is stored in HDFS. That is, three copies of the same file are stored by default. The HDFS storage space indicates the total disk space occupied by all these copies. For example, if <span class="parmname" id="parmname21566615175846"><a name="parmname21566615175846"></a><a name="parmname21566615175846"></a><b>Space Quota</b></span>&nbsp;is set to&nbsp;<span class="parmvalue" id="parmvalue42238099175858"><a name="parmvalue42238099175858"></a><a name="parmvalue42238099175858"></a><b>500</b></span>, the actual space for storing files is about 166 MB (500/3 = 166).</p>
    </div></div>
    </td>
    </tr>
    <tr id="row1003840419271"><td class="cellrowborder" valign="top" width="32.5%" headers="mcps1.2.3.1.1 "><p id="p780443419271"><a name="p780443419271"></a><a name="p780443419271"></a><span class="parmname" id="parmname48291605192426"><a name="parmname48291605192426"></a><a name="parmname48291605192426"></a><b>Storage Path</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="67.5%" headers="mcps1.2.3.1.2 "><p id="p2817942819271"><a name="p2817942819271"></a><a name="p2817942819271"></a>Specifies the tenant's HDFS storage directory. The system automatically creates a file folder in the <span class="filepath" id="filepath671608412031"><a name="filepath671608412031"></a><a name="filepath671608412031"></a><b>/tenant</b></span>&nbsp;directory, which is given the same name as the tenant. For example, the default HDFS storage directory for tenant&nbsp;<span class="parmname" id="parmname6044476412031"><a name="parmname6044476412031"></a><a name="parmname6044476412031"></a><b>ta1</b></span>&nbsp;is&nbsp;<span class="filepath" id="filepath713197012031"><a name="filepath713197012031"></a><a name="filepath713197012031"></a><b>tenant/ta1</b></span>. When the tenant is created, the system automatically creates the&nbsp;<span class="filepath" id="filepath6418773512031"><a name="filepath6418773512031"></a><a name="filepath6418773512031"></a><b>/tenant</b></span> directory under the root directory of HDFS. The storage path is customizable.</p>
    </td>
    </tr>
    <tr id="row5228826719271"><td class="cellrowborder" valign="top" width="32.5%" headers="mcps1.2.3.1.1 "><p id="p749119819271"><a name="p749119819271"></a><a name="p749119819271"></a><span class="parmname" id="parmname44855382192430"><a name="parmname44855382192430"></a><a name="parmname44855382192430"></a><b>Service</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="67.5%" headers="mcps1.2.3.1.2 "><p id="p280733919271"><a name="p280733919271"></a><a name="p280733919271"></a>Specifies other service resources associated with the current tenant. HBase is supported. To configure this parameter, click <span class="uicontrol" id="uicontrol2197551512031"><a name="uicontrol2197551512031"></a><a name="uicontrol2197551512031"></a><b>Associate Services</b></span>. In the dialog box that is displayed, set&nbsp;<span class="parmname" id="parmname6356191012031"><a name="parmname6356191012031"></a><a name="parmname6356191012031"></a><b>Service</b></span>&nbsp;to&nbsp;<span class="parmvalue" id="parmvalue3518628012031"><a name="parmvalue3518628012031"></a><a name="parmvalue3518628012031"></a><b>HBase</b></span>. If&nbsp;<span class="parmname" id="parmname4824106612031"><a name="parmname4824106612031"></a><a name="parmname4824106612031"></a><b>Association Mode</b></span>&nbsp;is set to&nbsp;<span class="parmvalue" id="parmvalue3151641312031"><a name="parmvalue3151641312031"></a><a name="parmvalue3151641312031"></a><b>Exclusive</b></span>, service resources are occupied exclusively. If&nbsp;<span class="parmvalue" id="parmvalue1521226712031"><a name="parmvalue1521226712031"></a><a name="parmvalue1521226712031"></a><b>share</b></span> is selected, service resources are shared.</p>
    </td>
    </tr>
    <tr id="row2526605419271"><td class="cellrowborder" valign="top" width="32.5%" headers="mcps1.2.3.1.1 "><p id="p3328447419271"><a name="p3328447419271"></a><a name="p3328447419271"></a><span class="parmname" id="parmname42153003192435"><a name="parmname42153003192435"></a><a name="parmname42153003192435"></a><b>Description</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="67.5%" headers="mcps1.2.3.1.2 "><p id="p1168786719271"><a name="p1168786719271"></a><a name="p1168786719271"></a>Specifies the description of the current tenant.</p>
    </td>
    </tr>
    </tbody>
    </table>

3.  Click  **OK**  to save the settings.

    It takes a few minutes to save the settings. If the  **Tenant created successfully**  is displayed in the upper-right corner, the tenant is added successfully.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   Roles, computing resources, and storage resources are automatically created when tenants are created.  
    >-   The new role has the rights on the computing and storage resources. The role and the rights are controlled by the system automatically and cannot be controlled manually under  **Manage Role**.  
    >-   If you want to use the tenant, create a system user and assign the Manager\_tenant role and the role corresponding to the tenant to the user. For details, see  [Creating a User](creating-a-user.md).  


## Related Tasks<a name="section28781070132624"></a>

Viewing an added tenant

1.  On MRS Manager, click  **Tenant**.
2.  In the tenant list on the left, click the name of an added tenant.

    The  **Summary**  tab is displayed on the right by default.

3.  View  **Basic Information**, **Resource Quota**, and **Statistics**  of the tenant.

    If HDFS is in the  **Stopped** state, **Available** and **Usage** of **Space** in **Resource Quota** are  **unknown**.


