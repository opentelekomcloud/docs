# Creating a Sub-tenant<a name="EN-US_TOPIC_0125375834"></a>

## Scenario<a name="section50407764192941"></a>

You can create a sub-tenant on MRS Manager if the resources of the current tenant need to be further allocated.

## Prerequisites<a name="section3418666519304"></a>

-   A parent tenant has been added.
-   A tenant name has been planned. The name must not be the same as that of a role or Yarn queue that exists in the current cluster.
-   If a sub-tenant requires storage resources, a storage directory has been planned in advance based on service requirements, and the planned directory does not exist under the storage directory of the parent tenant.
-   The resources that can be allocated to the current tenant have been planned and the sum of the resource percentages of direct sub-tenants under the parent tenant at every level does not exceed 100%.

## Procedure<a name="section52488736193659"></a>

1.  On MRS Manager, click  **Tenant**.
2.  In the tenant list on the left, move the cursor to the tenant node to which a sub-tenant is to be added. Click  **Create sub-tenant**. On the displayed page, configure the sub-tenant attributes according to the following table.

    **Table  1**  Sub-tenant parameters

    <a name="table2976617193725"></a>
    <table><thead align="left"><tr id="row8158217193725"><th class="cellrowborder" valign="top" width="32.5%" id="mcps1.2.3.1.1"><p id="p56835818193725"><a name="p56835818193725"></a><a name="p56835818193725"></a><strong id="b547523193731"><a name="b547523193731"></a><a name="b547523193731"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="67.5%" id="mcps1.2.3.1.2"><p id="p40298577193725"><a name="p40298577193725"></a><a name="p40298577193725"></a><strong id="b44349382193731"><a name="b44349382193731"></a><a name="b44349382193731"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row42959267193725"><td class="cellrowborder" valign="top" width="32.5%" headers="mcps1.2.3.1.1 "><p id="p57148618193725"><a name="p57148618193725"></a><a name="p57148618193725"></a><span class="parmname" id="parmname7490696192519"><a name="parmname7490696192519"></a><a name="parmname7490696192519"></a><b>Parent tenant</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="67.5%" headers="mcps1.2.3.1.2 "><p id="p65635374193725"><a name="p65635374193725"></a><a name="p65635374193725"></a>Specifies the name of the parent tenant.</p>
    </td>
    </tr>
    <tr id="row53847458193725"><td class="cellrowborder" valign="top" width="32.5%" headers="mcps1.2.3.1.1 "><p id="p66676843193725"><a name="p66676843193725"></a><a name="p66676843193725"></a><span class="parmname" id="parmname12645823192522"><a name="parmname12645823192522"></a><a name="parmname12645823192522"></a><b>Name</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="67.5%" headers="mcps1.2.3.1.2 "><p id="p32115237193725"><a name="p32115237193725"></a><a name="p32115237193725"></a>Specifies the name of the current tenant. The value consists of 3 to 20 characters, <span id="ph143207516819"><a name="ph143207516819"></a><a name="ph143207516819"></a>and</span> can contain letters, digits, and underscores (_).</p>
    </td>
    </tr>
    <tr id="row20601684193725"><td class="cellrowborder" valign="top" width="32.5%" headers="mcps1.2.3.1.1 "><p id="p58123706193725"><a name="p58123706193725"></a><a name="p58123706193725"></a><span class="parmname" id="parmname34475158192525"><a name="parmname34475158192525"></a><a name="parmname34475158192525"></a><b>Tenant Type</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="67.5%" headers="mcps1.2.3.1.2 "><p id="p10399716193725"><a name="p10399716193725"></a><a name="p10399716193725"></a>The options include <span class="parmvalue" id="parmvalue9919057124858"><a name="parmvalue9919057124858"></a><a name="parmvalue9919057124858"></a><b>Leaf</b></span>&nbsp;and&nbsp;<span class="parmvalue" id="parmvalue5885367611597"><a name="parmvalue5885367611597"></a><a name="parmvalue5885367611597"></a><b>Non-leaf</b></span>.&nbsp;<span id="ph6172340716914"><a name="ph6172340716914"></a><a name="ph6172340716914"></a>If</span>&nbsp;<span class="parmvalue" id="parmvalue65246159124858"><a name="parmvalue65246159124858"></a><a name="parmvalue65246159124858"></a><b>Leaf</b></span>&nbsp;is selected, the current tenant is a leaf tenant and no sub-tenant can be added.&nbsp;<span id="ph5871442816919"><a name="ph5871442816919"></a><a name="ph5871442816919"></a>If</span>&nbsp;<span class="parmvalue" id="parmvalue40174197115910"><a name="parmvalue40174197115910"></a><a name="parmvalue40174197115910"></a><b>Non-leaf</b></span> is selected, sub-tenants can be added to the current tenant.</p>
    </td>
    </tr>
    <tr id="row26488582193725"><td class="cellrowborder" valign="top" width="32.5%" headers="mcps1.2.3.1.1 "><p id="p65200402193725"><a name="p65200402193725"></a><a name="p65200402193725"></a><span class="parmname" id="parmname46904930192530"><a name="parmname46904930192530"></a><a name="parmname46904930192530"></a><b>Dynamic Resource</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="67.5%" headers="mcps1.2.3.1.2 "><p id="p46741206193725"><a name="p46741206193725"></a><a name="p46741206193725"></a>Specifies the dynamic computing resources for the current tenant. The system automatically creates a task queue in the Yarn parent tenant queue and the task queue name is the same as the name of the sub-tenant. If dynamic resources are not <span class="parmvalue" id="parmvalue58263416181729"><a name="parmvalue58263416181729"></a><a name="parmvalue58263416181729"></a><b>Yarn</b></span> resources, the system does not automatically create a task queue. If the parent tenant does not have dynamic resources, the sub-tenant cannot use dynamic resources.</p>
    </td>
    </tr>
    <tr id="row18017677193725"><td class="cellrowborder" valign="top" width="32.5%" headers="mcps1.2.3.1.1 "><p id="p50145753193725"><a name="p50145753193725"></a><a name="p50145753193725"></a><span class="parmname" id="parmname20147291192536"><a name="parmname20147291192536"></a><a name="parmname20147291192536"></a><b>Default Resource Pool Capacity (%)</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="67.5%" headers="mcps1.2.3.1.2 "><p id="p35274226193725"><a name="p35274226193725"></a><a name="p35274226193725"></a>Specifies the percentage of the computing resources used by the current tenant. The base value is the total resources of the parent tenant.</p>
    </td>
    </tr>
    <tr id="row49032583193725"><td class="cellrowborder" valign="top" width="32.5%" headers="mcps1.2.3.1.1 "><p id="p12216253193725"><a name="p12216253193725"></a><a name="p12216253193725"></a><span class="parmname" id="parmname33310982192548"><a name="parmname33310982192548"></a><a name="parmname33310982192548"></a><b>Default Resource Pool Max. Capacity (%)</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="67.5%" headers="mcps1.2.3.1.2 "><p id="p49992436193725"><a name="p49992436193725"></a><a name="p49992436193725"></a>Specifies the maximum percentage of the computing resources used by the current tenant. The base value is the total resources of the parent tenant.</p>
    </td>
    </tr>
    <tr id="row47278743193725"><td class="cellrowborder" valign="top" width="32.5%" headers="mcps1.2.3.1.1 "><p id="p4372978193725"><a name="p4372978193725"></a><a name="p4372978193725"></a><span class="parmname" id="parmname29020328192551"><a name="parmname29020328192551"></a><a name="parmname29020328192551"></a><b>Storage Resource</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="67.5%" headers="mcps1.2.3.1.2 "><p id="p18666913193725"><a name="p18666913193725"></a><a name="p18666913193725"></a>Specifies the storage resources for the current tenant. The system automatically creates a file folder in the HDFS parent tenant directory<span id="ph38547690102358"><a name="ph38547690102358"></a><a name="ph38547690102358"></a>, which is given</span>&nbsp;the same&nbsp;name as&nbsp;the sub-tenant. If storage resources are not&nbsp;<strong id="b3226754410857"><a name="b3226754410857"></a><a name="b3226754410857"></a>HDFS</strong>, the system does not create a storage directory under the HDFS directory. If the parent tenant does not have storage resources, the sub-tenant cannot use storage resources.</p>
    </td>
    </tr>
    <tr id="row33784492193725"><td class="cellrowborder" valign="top" width="32.5%" headers="mcps1.2.3.1.1 "><p id="p52189301193725"><a name="p52189301193725"></a><a name="p52189301193725"></a><span class="parmname" id="parmname8203799103923"><a name="parmname8203799103923"></a><a name="parmname8203799103923"></a><b>Space Quota (MB)</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="67.5%" headers="mcps1.2.3.1.2 "><p id="p66583814193725"><a name="p66583814193725"></a><a name="p66583814193725"></a>Specifies the quota for HDFS storage space&nbsp;used by the current tenant. The&nbsp;minimum value&nbsp;<span id="ph4998402611828"><a name="ph4998402611828"></a><a name="ph4998402611828"></a>is 1. The maximum value is the entire space quota of the parent tenant.</span>&nbsp;The unit is MB. This parameter indicates the maximum HDFS storage space that can be used by the tenant, but does not indicate the actual space used. If the value is greater than the size of the HDFS physical disk,&nbsp;<span id="ph1485312210292"><a name="ph1485312210292"></a><a name="ph1485312210292"></a>the maximum space available is the full space of the HDFS physical disk</span>. If this quota is greater than the quota of the parent tenant, the actual storage space will be affected by the quota of the parent tenant.</p>
    <div class="note" id="note4900057418446"><a name="note4900057418446"></a><a name="note4900057418446"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p3835198618446"><a name="p3835198618446"></a><a name="p3835198618446"></a>To ensure data reliability, two more copies of a file are automatically generated when the file is stored in HDFS. That is, three copies of the same file are stored by default. The HDFS storage space indicates the total disk space occupied by all these copies. For example, if <span class="parmname" id="parmname1597032318448"><a name="parmname1597032318448"></a><a name="parmname1597032318448"></a><b>Space Quota</b></span>&nbsp;is set to&nbsp;<span class="parmvalue" id="parmvalue1852778718448"><a name="parmvalue1852778718448"></a><a name="parmvalue1852778718448"></a><b>500</b></span>, the actual space for storing files is about 166 MB (500/3 = 166).</p>
    </div></div>
    </td>
    </tr>
    <tr id="row62383417193725"><td class="cellrowborder" valign="top" width="32.5%" headers="mcps1.2.3.1.1 "><p id="p19892042193725"><a name="p19892042193725"></a><a name="p19892042193725"></a><span class="parmname" id="parmname2403367519261"><a name="parmname2403367519261"></a><a name="parmname2403367519261"></a><b>Storage Path</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="67.5%" headers="mcps1.2.3.1.2 "><p id="p642744193725"><a name="p642744193725"></a><a name="p642744193725"></a>Specifies the tenant's HDFS storage directory. The system automatically creates a file folder in the parent tenant directory<span id="ph48882996103550"><a name="ph48882996103550"></a><a name="ph48882996103550"></a>, which is given the same name as</span>&nbsp;the sub-tenant. For example, if the sub-tenant is&nbsp;<span class="parmname" id="parmname43133454124858"><a name="parmname43133454124858"></a><a name="parmname43133454124858"></a><b>ta1s</b></span>&nbsp;and the parent directory is&nbsp;<span class="filepath" id="filepath52656769124858"><a name="filepath52656769124858"></a><a name="filepath52656769124858"></a><b>tenant/ta1</b></span>, the system sets this parameter for the sub-tenant to&nbsp;<span class="filepath" id="filepath4148876124858"><a name="filepath4148876124858"></a><a name="filepath4148876124858"></a><b>tenant/ta1/ta1s</b></span> by default. The storage path is customizable in the parent directory. The parent directory for the storage path must be the storage directory of the parent tenant.</p>
    </td>
    </tr>
    <tr id="row5784701193725"><td class="cellrowborder" valign="top" width="32.5%" headers="mcps1.2.3.1.1 "><p id="p65907649193725"><a name="p65907649193725"></a><a name="p65907649193725"></a><span class="parmname" id="parmname8773423192628"><a name="parmname8773423192628"></a><a name="parmname8773423192628"></a><b>Service</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="67.5%" headers="mcps1.2.3.1.2 "><p id="p36919316193725"><a name="p36919316193725"></a><a name="p36919316193725"></a>Specifies other service resources associated with the current tenant. HBase is supported. <span id="ph46425733103836"><a name="ph46425733103836"></a><a name="ph46425733103836"></a>To configure this parameter, c</span>lick&nbsp;<span class="uicontrol" id="uicontrol21366962124858"><a name="uicontrol21366962124858"></a><a name="uicontrol21366962124858"></a><b>Associate Services</b></span>. In the dialog box that is displayed, set&nbsp;<span class="parmname" id="parmname58084930124858"><a name="parmname58084930124858"></a><a name="parmname58084930124858"></a><b>Service</b></span>&nbsp;to&nbsp;<span class="parmvalue" id="parmvalue53002322124858"><a name="parmvalue53002322124858"></a><a name="parmvalue53002322124858"></a><b>HBase</b></span>. If&nbsp;<span class="parmname" id="parmname7258851124858"><a name="parmname7258851124858"></a><a name="parmname7258851124858"></a><b>Association Mode</b></span>&nbsp;is set to&nbsp;<span class="parmvalue" id="parmvalue65329662124858"><a name="parmvalue65329662124858"></a><a name="parmvalue65329662124858"></a><b>Exclusive</b></span>, service resources are occupied exclusively. If&nbsp;<span class="parmvalue" id="parmvalue51096053124858"><a name="parmvalue51096053124858"></a><a name="parmvalue51096053124858"></a><b>Share</b></span> is selected, service resources are shared.</p>
    </td>
    </tr>
    <tr id="row63838396193725"><td class="cellrowborder" valign="top" width="32.5%" headers="mcps1.2.3.1.1 "><p id="p3527596193725"><a name="p3527596193725"></a><a name="p3527596193725"></a><span class="parmname" id="parmname36215396192632"><a name="parmname36215396192632"></a><a name="parmname36215396192632"></a><b>Description</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="67.5%" headers="mcps1.2.3.1.2 "><p id="p17299840193725"><a name="p17299840193725"></a><a name="p17299840193725"></a>Specifies the description of the current tenant.</p>
    </td>
    </tr>
    </tbody>
    </table>

3.  Click  **OK**  to save the settings.

    It takes a few minutes to save the settings.The  **Tenant created successfully**  is displayed in the upper-right corner. The tenant is added successfully.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   Roles, computing resources, and storage resources are automatically created when tenants are created.  
    >-   The new role has the rights on the computing and storage resources. The role and the rights are controlled by the system automatically and cannot be controlled manually under  **Manage Role**.  
    >-   When using this tenant, create a system user and assign the user a related tenant role. For details, see  [Creating a User](creating-a-user.md).  


