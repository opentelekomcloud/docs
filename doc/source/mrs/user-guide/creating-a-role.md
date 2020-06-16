# Creating a Role<a name="EN-US_TOPIC_0125376150"></a>

## Scenario<a name="s2a4e18c3d67344e095feb6098a3c0d64"></a>

This section describes how to create a role on MRS Manager and authorize and manage Manager and components.

Up to 1000 roles can be created on MRS Manager.

## Prerequisites<a name="sa50ec446ec444bf7999681ddc6dda6ec"></a>

-   You have learned service requirements.
-   You have obtained a cluster with Kerberos authentication enabled or a normal cluster with the EIP function enabled.

## Procedure<a name="s6552ae48ae8c4abf9484bf1e3c6c8628"></a>

1.  On MRS Manager, choose  **System**  \>  **Manage Role**.
2.  Click  **Create Role** and fill in **Role Name** and **Description**.

    **Role Name** is mandatory and contains 3 to 30 digits, letters, and underscores \(\_\). **Description**  is optional.

3.  In  **Permission**, set role permission.

    1.  Click  **Service Name** and select a name in **View Name**.
    2.  Select one or more permissions.

    >![](/images/icon-note.gif) **NOTE:**   
    >-   The  **Permission**  parameter is optional.  
    >-   If you select  **View Name** to set component permissions, you can enter a resource name in the **Search** box in the upper-right corner and click ![](figures/icon_mrs_search_l_l.jpg). The search result is displayed.  
    >-   The search scope covers only directories with current permissions. You cannot search subdirectories. Search by keywords supports fuzzy match and is case-insensitive. Results of the next page can be searched.  

    **Table  1**  Manager permission description

    <a name="tc56250b1d9b24576a9f8744115ce4c2e"></a>
    <table><thead align="left"><tr id="r37272add0b71458da808b26c4989cbbf"><th class="cellrowborder" valign="top" width="35%" id="mcps1.2.3.1.1"><p id="en-us_topic_0043021164_p134738881521"><a name="en-us_topic_0043021164_p134738881521"></a><a name="en-us_topic_0043021164_p134738881521"></a><strong id="af502b9e682fb440180e28fb55b830eee"><a name="af502b9e682fb440180e28fb55b830eee"></a><a name="af502b9e682fb440180e28fb55b830eee"></a>Resource Supporting Permission Management</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="65%" id="mcps1.2.3.1.2"><p id="en-us_topic_0043021164_p198085731521"><a name="en-us_topic_0043021164_p198085731521"></a><a name="en-us_topic_0043021164_p198085731521"></a><strong id="a9c5f5d5cba4f4fa490a35968e48d96f9"><a name="a9c5f5d5cba4f4fa490a35968e48d96f9"></a><a name="a9c5f5d5cba4f4fa490a35968e48d96f9"></a>Permission Setting</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r89180ac0e3c94e4fbbfe1871a8b8f106"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0043021164_p120441861521"><a name="en-us_topic_0043021164_p120441861521"></a><a name="en-us_topic_0043021164_p120441861521"></a><span class="parmname" id="pb628858ba9084a608e8c7b557ff26c6d"><a name="pb628858ba9084a608e8c7b557ff26c6d"></a><a name="pb628858ba9084a608e8c7b557ff26c6d"></a><b>Alarms</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0043021164_p347729681521"><a name="en-us_topic_0043021164_p347729681521"></a><a name="en-us_topic_0043021164_p347729681521"></a>Authorizes the Manager alarm function. You can select <span class="parmvalue" id="parmvalue964114206154236"><a name="parmvalue964114206154236"></a><a name="parmvalue964114206154236"></a><b>View</b></span>&nbsp;to view alarms and&nbsp;<span class="parmvalue" id="parmvalue686252866154236"><a name="parmvalue686252866154236"></a><a name="parmvalue686252866154236"></a><b>Management</b></span> to manage alarms.</p>
    </td>
    </tr>
    <tr id="r72032fadf93e4ebaa14a4f0787b12687"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.3.1.1 "><p id="ae000540e57eb4fc8b8f3f8c37978f11c"><a name="ae000540e57eb4fc8b8f3f8c37978f11c"></a><a name="ae000540e57eb4fc8b8f3f8c37978f11c"></a><span class="parmname" id="p2abaead37ab5463d9fd17a93c4a73e1f"><a name="p2abaead37ab5463d9fd17a93c4a73e1f"></a><a name="p2abaead37ab5463d9fd17a93c4a73e1f"></a><b>Audit</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.3.1.2 "><p id="aacd0d66f60864e9f81a32bd6d97e7acc"><a name="aacd0d66f60864e9f81a32bd6d97e7acc"></a><a name="aacd0d66f60864e9f81a32bd6d97e7acc"></a>Authorizes the Manager audit log function. You can select <span class="parmvalue" id="parmvalue861918199154233"><a name="parmvalue861918199154233"></a><a name="parmvalue861918199154233"></a><b>View</b></span>&nbsp;to view audit logs and&nbsp;<span class="parmvalue" id="parmvalue203651694154233"><a name="parmvalue203651694154233"></a><a name="parmvalue203651694154233"></a><b>Management</b></span> to manage audit logs.</p>
    </td>
    </tr>
    <tr id="rf23879aeef2b4b28b0e202f3a03c2cad"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.3.1.1 "><p id="a81729e50effb44e5b36a18dd8c175df1"><a name="a81729e50effb44e5b36a18dd8c175df1"></a><a name="a81729e50effb44e5b36a18dd8c175df1"></a><span class="parmname" id="pa426fed02b744a7aacfb7d54b5adb0f3"><a name="pa426fed02b744a7aacfb7d54b5adb0f3"></a><a name="pa426fed02b744a7aacfb7d54b5adb0f3"></a><b>Dashboard</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.3.1.2 "><p id="a3ab5699701d641588cd6dc8fe3b39909"><a name="a3ab5699701d641588cd6dc8fe3b39909"></a><a name="a3ab5699701d641588cd6dc8fe3b39909"></a>Authorizes the Manager overview function. You can select <span class="parmvalue" id="parmvalue109150551010536"><a name="parmvalue109150551010536"></a><a name="parmvalue109150551010536"></a><b>View</b></span> to view the cluster overview.</p>
    </td>
    </tr>
    <tr id="r85faeed2387a4683ae80c406cfd64154"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0043021164_p269194115754"><a name="en-us_topic_0043021164_p269194115754"></a><a name="en-us_topic_0043021164_p269194115754"></a><span class="parmname" id="p307757eb1dac4702afe0c92a1969ff64"><a name="p307757eb1dac4702afe0c92a1969ff64"></a><a name="p307757eb1dac4702afe0c92a1969ff64"></a><b>Hosts</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.3.1.2 "><p id="ad7ecaeb339d94b039e284e98b66a534b"><a name="ad7ecaeb339d94b039e284e98b66a534b"></a><a name="ad7ecaeb339d94b039e284e98b66a534b"></a>Authorizes the node management function. You can select <span class="parmvalue" id="parmvalue637088266154214"><a name="parmvalue637088266154214"></a><a name="parmvalue637088266154214"></a><b>View</b></span>&nbsp;to view node information and&nbsp;<span class="parmvalue" id="parmvalue2134710340154214"><a name="parmvalue2134710340154214"></a><a name="parmvalue2134710340154214"></a><b>Management</b></span> to manage nodes.</p>
    </td>
    </tr>
    <tr id="rabcef47088b847aeb56b57d1d336e34e"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.3.1.1 "><p id="a533d14891b944fe0bcfa0f4010049b00"><a name="a533d14891b944fe0bcfa0f4010049b00"></a><a name="a533d14891b944fe0bcfa0f4010049b00"></a><span class="parmname" id="pf868c39efbc7449da3911c1b9eeb6f75"><a name="pf868c39efbc7449da3911c1b9eeb6f75"></a><a name="pf868c39efbc7449da3911c1b9eeb6f75"></a><b>Services</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.3.1.2 "><p id="af5097bc6f390403885ef01263f1776fd"><a name="af5097bc6f390403885ef01263f1776fd"></a><a name="af5097bc6f390403885ef01263f1776fd"></a>Authorizes the service management function. You can select <span class="parmvalue" id="parmvalue78715356815429"><a name="parmvalue78715356815429"></a><a name="parmvalue78715356815429"></a><b>View</b></span>&nbsp;to view service information and&nbsp;<span class="parmvalue" id="parmvalue150290310415429"><a name="parmvalue150290310415429"></a><a name="parmvalue150290310415429"></a><b>Management</b></span> to manage services.</p>
    </td>
    </tr>
    <tr id="rb255e14205aa482cbf649a4868a08baf"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.3.1.1 "><p id="a7c271a233b4b41cabe913b464899e4b4"><a name="a7c271a233b4b41cabe913b464899e4b4"></a><a name="a7c271a233b4b41cabe913b464899e4b4"></a><span class="parmname" id="p23f93bd0e54a4283beb5e900c9c7da9b"><a name="p23f93bd0e54a4283beb5e900c9c7da9b"></a><a name="p23f93bd0e54a4283beb5e900c9c7da9b"></a><b>System_cluster_management</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.3.1.2 "><p id="a260d209155f94b86812f3e3ebdb1c6a5"><a name="a260d209155f94b86812f3e3ebdb1c6a5"></a><a name="a260d209155f94b86812f3e3ebdb1c6a5"></a>Authorizes the MRS cluster management function. You can select <span class="parmvalue" id="parmvalue249147332154150"><a name="parmvalue249147332154150"></a><a name="parmvalue249147332154150"></a><b>Management</b></span> to use the MRS patch management function.</p>
    </td>
    </tr>
    <tr id="rb77670173ad54a9ba7b9d4e81f45d52f"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.3.1.1 "><p id="a74255f30d47645dd9ed3421d4e66c251"><a name="a74255f30d47645dd9ed3421d4e66c251"></a><a name="a74255f30d47645dd9ed3421d4e66c251"></a><span class="parmname" id="p897fb2fcb15b49ae831ab8b78d1a6456"><a name="p897fb2fcb15b49ae831ab8b78d1a6456"></a><a name="p897fb2fcb15b49ae831ab8b78d1a6456"></a><b>System_configuration</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.3.1.2 "><p id="a8fed8392d6e74a8fb6b6849e6452ed52"><a name="a8fed8392d6e74a8fb6b6849e6452ed52"></a><a name="a8fed8392d6e74a8fb6b6849e6452ed52"></a>Authorizes the MRS cluster configuration function. You can select <span class="parmvalue" id="parmvalue2070195755154148"><a name="parmvalue2070195755154148"></a><a name="parmvalue2070195755154148"></a><b>Management</b></span> to configure MRS clusters on Manager.</p>
    </td>
    </tr>
    <tr id="ra1691d0abe2e4813810a252fd34ee3f8"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.3.1.1 "><p id="a984fdc4de8ee4da5ad67a5e189c32915"><a name="a984fdc4de8ee4da5ad67a5e189c32915"></a><a name="a984fdc4de8ee4da5ad67a5e189c32915"></a><span class="parmname" id="p8e1936d0826946c6ae88521948f72504"><a name="p8e1936d0826946c6ae88521948f72504"></a><a name="p8e1936d0826946c6ae88521948f72504"></a><b>System_task</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.3.1.2 "><p id="a5d0ee28131ea41959c6dcf069649f1ce"><a name="a5d0ee28131ea41959c6dcf069649f1ce"></a><a name="a5d0ee28131ea41959c6dcf069649f1ce"></a>Authorizes the MRS cluster task function. You can select <span class="parmvalue" id="parmvalue250162168154131"><a name="parmvalue250162168154131"></a><a name="parmvalue250162168154131"></a><b>Management</b></span> to manage periodic tasks of MRS clusters on Manager.</p>
    </td>
    </tr>
    <tr id="rdf3fbdf181c64353a194162d40f786f0"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.3.1.1 "><p id="a8a5d49c5c5ae4defa45fbddf012504df"><a name="a8a5d49c5c5ae4defa45fbddf012504df"></a><a name="a8a5d49c5c5ae4defa45fbddf012504df"></a><span class="parmname" id="p0a06e3b86e974f32a0db65fedf113d27"><a name="p0a06e3b86e974f32a0db65fedf113d27"></a><a name="p0a06e3b86e974f32a0db65fedf113d27"></a><b>Tenant</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0043021164_p751318515755"><a name="en-us_topic_0043021164_p751318515755"></a><a name="en-us_topic_0043021164_p751318515755"></a>Authorizes the Manager multi-tenant management function. You can select <span class="parmvalue" id="parmvalue987894592154111"><a name="parmvalue987894592154111"></a><a name="parmvalue987894592154111"></a><b>Management</b></span> to view the Manager tenant management page.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  HBase permission description

    <a name="tbed1cdc10ace49f2a7bd3a687abc6503"></a>
    <table><thead align="left"><tr id="rd1743e3c7f8247af8f9d5e8e53d56632"><th class="cellrowborder" valign="top" width="35%" id="mcps1.2.3.1.1"><p id="a84d36e0717a34f6a8b92c8cf7dee94da"><a name="a84d36e0717a34f6a8b92c8cf7dee94da"></a><a name="a84d36e0717a34f6a8b92c8cf7dee94da"></a><strong id="a7d5f06a93c674d6a9fa9c91452ba479b"><a name="a7d5f06a93c674d6a9fa9c91452ba479b"></a><a name="a7d5f06a93c674d6a9fa9c91452ba479b"></a>Resource Supporting Permission Management</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="65%" id="mcps1.2.3.1.2"><p id="acd9b243effdc4b03a7553fdd0d3aec20"><a name="acd9b243effdc4b03a7553fdd0d3aec20"></a><a name="acd9b243effdc4b03a7553fdd0d3aec20"></a><strong id="b27098321102259"><a name="b27098321102259"></a><a name="b27098321102259"></a>Permission Setting</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r1f2816a69b2746429e5dfa8ca67ab2b4"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.3.1.1 "><p id="a55acda0b20304794be7213130169e061"><a name="a55acda0b20304794be7213130169e061"></a><a name="a55acda0b20304794be7213130169e061"></a><span class="parmname" id="pa0ace66604314170b6513535f10ef147"><a name="pa0ace66604314170b6513535f10ef147"></a><a name="pa0ace66604314170b6513535f10ef147"></a><b>SUPER_USER_GROUP</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0043021164_p482733115136"><a name="en-us_topic_0043021164_p482733115136"></a><a name="en-us_topic_0043021164_p482733115136"></a>Grants you HBase administrator rights.</p>
    </td>
    </tr>
    <tr id="r672f32f898b74e5a8ab1d9fbd0865d84"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.3.1.1 "><p id="ada140e1943f04eafad1430da979b5116"><a name="ada140e1943f04eafad1430da979b5116"></a><a name="ada140e1943f04eafad1430da979b5116"></a><span class="parmname" id="p6f80aa2d62ed466ab1aaf845af02bf81"><a name="p6f80aa2d62ed466ab1aaf845af02bf81"></a><a name="p6f80aa2d62ed466ab1aaf845af02bf81"></a><b>Global</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.3.1.2 "><p id="ad3eaf0f51f70477bba1f7015dc824b12"><a name="ad3eaf0f51f70477bba1f7015dc824b12"></a><a name="ad3eaf0f51f70477bba1f7015dc824b12"></a>HBase resource type, indicating the whole HBase.</p>
    </td>
    </tr>
    <tr id="re7ec715d849e437f9983f34009f29fa5"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0043021164_p757502015136"><a name="en-us_topic_0043021164_p757502015136"></a><a name="en-us_topic_0043021164_p757502015136"></a><span class="parmname" id="p906c1eb62e114db5b6bea6abcff7d697"><a name="p906c1eb62e114db5b6bea6abcff7d697"></a><a name="p906c1eb62e114db5b6bea6abcff7d697"></a><b>Namespace</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0043021164_p959685515136"><a name="en-us_topic_0043021164_p959685515136"></a><a name="en-us_topic_0043021164_p959685515136"></a>HBase resource type, indicating namespace, which is used to store HBase tables. It has the following permissions:</p>
    <a name="u93e3c43d3f8c4ca882d6d69f795ce81f"></a><a name="u93e3c43d3f8c4ca882d6d69f795ce81f"></a><ul id="u93e3c43d3f8c4ca882d6d69f795ce81f"><li><span class="parmname" id="parmname371467394105353"><a name="parmname371467394105353"></a><a name="parmname371467394105353"></a><b>Admin</b></span>: permission to manage the namespace</li><li><span class="parmname" id="parmname150297642410542"><a name="parmname150297642410542"></a><a name="parmname150297642410542"></a><b>Create</b></span>: permission to create HBase tables in the namespace</li><li><span class="parmname" id="parmname747513224105410"><a name="parmname747513224105410"></a><a name="parmname747513224105410"></a><b>Read</b></span>: permission to access the namespace</li><li><span class="parmname" id="parmname76898432105417"><a name="parmname76898432105417"></a><a name="parmname76898432105417"></a><b>Write</b></span>: permission to write data to the namespace</li><li><span class="parmname" id="parmname2066802822105426"><a name="parmname2066802822105426"></a><a name="parmname2066802822105426"></a><b>Execute</b></span>: permission to execute the coprocessor (Endpoint)</li></ul>
    </td>
    </tr>
    <tr id="rf5f57e80296645b0bc7987e245566404"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.3.1.1 "><p id="a3dcd369c32f945d194e6bc81d58fe5f5"><a name="a3dcd369c32f945d194e6bc81d58fe5f5"></a><a name="a3dcd369c32f945d194e6bc81d58fe5f5"></a><span class="parmname" id="pa3874e02d8df4aea8c0910f1bb2f3a49"><a name="pa3874e02d8df4aea8c0910f1bb2f3a49"></a><a name="pa3874e02d8df4aea8c0910f1bb2f3a49"></a><b>Table</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.3.1.2 "><p id="a9e8517e858e14687bae542877284bb0a"><a name="a9e8517e858e14687bae542877284bb0a"></a><a name="a9e8517e858e14687bae542877284bb0a"></a>HBase resource type, indicating a data table, which is used to store data. It has the following permissions:</p>
    <a name="ub172197063964825bb32a8d4e4ba84c8"></a><a name="ub172197063964825bb32a8d4e4ba84c8"></a><ul id="ub172197063964825bb32a8d4e4ba84c8"><li><span class="parmname" id="parmname636231661105442"><a name="parmname636231661105442"></a><a name="parmname636231661105442"></a><b>Admin</b></span>: permission to manage a data table</li><li><span class="parmname" id="parmname1041458789105447"><a name="parmname1041458789105447"></a><a name="parmname1041458789105447"></a><b>Create</b></span>: permission to create column families and columns in a data table</li><li><span class="parmname" id="parmname1311507823105455"><a name="parmname1311507823105455"></a><a name="parmname1311507823105455"></a><b>Read</b></span>: permission to read a data table</li><li><span class="parmname" id="parmname120351856510551"><a name="parmname120351856510551"></a><a name="parmname120351856510551"></a><b>Write</b></span>: permission to write data to a data table</li><li><span class="parmname" id="p3628fa3091de4befaebfa4df81543cdc"><a name="p3628fa3091de4befaebfa4df81543cdc"></a><a name="p3628fa3091de4befaebfa4df81543cdc"></a><b>Execute</b></span>: permission to execute the coprocessor (Endpoint)</li></ul>
    </td>
    </tr>
    <tr id="r69f0fc5f928b4ab89454cccb722b0bc1"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.3.1.1 "><p id="ae41cbf363f6847ca901e0f3f033829bd"><a name="ae41cbf363f6847ca901e0f3f033829bd"></a><a name="ae41cbf363f6847ca901e0f3f033829bd"></a><span class="parmname" id="p516a865a88d64505a5ba18b6b56308af"><a name="p516a865a88d64505a5ba18b6b56308af"></a><a name="p516a865a88d64505a5ba18b6b56308af"></a><b>ColumnFamily</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.3.1.2 "><p id="a1e14aaa65c2a4940ab1448ff596c0275"><a name="a1e14aaa65c2a4940ab1448ff596c0275"></a><a name="a1e14aaa65c2a4940ab1448ff596c0275"></a>HBase resource type, indicating a column family, which is used to store data. It has the following permissions:</p>
    <a name="uc005d7eaa2074cdda7a46e94fbbddb33"></a><a name="uc005d7eaa2074cdda7a46e94fbbddb33"></a><ul id="uc005d7eaa2074cdda7a46e94fbbddb33"><li><span class="parmname" id="parmname1978002451105516"><a name="parmname1978002451105516"></a><a name="parmname1978002451105516"></a><b>Create</b></span>: permission to create columns in a column family</li><li><span class="parmname" id="parmname2033230682105523"><a name="parmname2033230682105523"></a><a name="parmname2033230682105523"></a><b>Read</b></span>: permission to read a column family</li><li><span class="parmname" id="parmname1750636397105528"><a name="parmname1750636397105528"></a><a name="parmname1750636397105528"></a><b>Write</b></span>: permission to write data to a column family</li></ul>
    </td>
    </tr>
    <tr id="ra9af25f5ca3b4af095c82d286a5e262c"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.3.1.1 "><p id="aa6d45669084844b39a69f72f302813c6"><a name="aa6d45669084844b39a69f72f302813c6"></a><a name="aa6d45669084844b39a69f72f302813c6"></a><span class="parmname" id="p473e5e996a2a483f9a574929bc3a02e7"><a name="p473e5e996a2a483f9a574929bc3a02e7"></a><a name="p473e5e996a2a483f9a574929bc3a02e7"></a><b>Qualifier</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.3.1.2 "><p id="a2eeed8b3940048de812edbecaf828a36"><a name="a2eeed8b3940048de812edbecaf828a36"></a><a name="a2eeed8b3940048de812edbecaf828a36"></a>HBase resource type, indicating a column, which is used to store data. It has the following permissions:</p>
    <a name="u5101c6e3d7c24361ad128e61f6538fa8"></a><a name="u5101c6e3d7c24361ad128e61f6538fa8"></a><ul id="u5101c6e3d7c24361ad128e61f6538fa8"><li><span class="parmname" id="parmname55074005102259"><a name="parmname55074005102259"></a><a name="parmname55074005102259"></a><b>Read</b></span>: permission to read a column</li><li><span class="parmname" id="parmname31809384102259"><a name="parmname31809384102259"></a><a name="parmname31809384102259"></a><b>Write</b></span>: permission to write data to a column</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    Permissions of an HBase resource type of each level are shared by subdirectories by default. For example, if  **Read** and **Write** permissions are added to the **default**  namespace, they are automatically added to the tables, column families, and columns in the namespace.

    **Table  3**  HDFS permission description

    <a name="t2a7f9ef7588a40cda5da55025e3904db"></a>
    <table><thead align="left"><tr id="rd160f3f0fb5540fea52b71048d3e5aca"><th class="cellrowborder" valign="top" width="35%" id="mcps1.2.3.1.1"><p id="abe57163ce00348d0b8a264dac3a7d331"><a name="abe57163ce00348d0b8a264dac3a7d331"></a><a name="abe57163ce00348d0b8a264dac3a7d331"></a><strong id="aa0a284e33df0487b96fb8dbcd3a4e255"><a name="aa0a284e33df0487b96fb8dbcd3a4e255"></a><a name="aa0a284e33df0487b96fb8dbcd3a4e255"></a>Resource Supporting Permission Management</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="65%" id="mcps1.2.3.1.2"><p id="aeafc5a6cee3148a7b37785c7c377120f"><a name="aeafc5a6cee3148a7b37785c7c377120f"></a><a name="aeafc5a6cee3148a7b37785c7c377120f"></a><strong id="b34035435102259"><a name="b34035435102259"></a><a name="b34035435102259"></a>Permission Setting</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="rd29b84c84672423fa78a8530c3013568"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.3.1.1 "><p id="ac415dc2fb0f546e0bf3340f7cd40cb48"><a name="ac415dc2fb0f546e0bf3340f7cd40cb48"></a><a name="ac415dc2fb0f546e0bf3340f7cd40cb48"></a><span class="parmname" id="pcefbd4f9f640469f84cf8dd1befa74d9"><a name="pcefbd4f9f640469f84cf8dd1befa74d9"></a><a name="pcefbd4f9f640469f84cf8dd1befa74d9"></a><b>Folder</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.3.1.2 "><p id="a7809b95c7ebb4105a366b5e691b93338"><a name="a7809b95c7ebb4105a366b5e691b93338"></a><a name="a7809b95c7ebb4105a366b5e691b93338"></a>HDFS resource type, indicating an HDFS directory, which is used to store files or subdirectories. It has the following permissions:</p>
    <a name="ucae7bcaf0c114c9fb73462ef0a456d17"></a><a name="ucae7bcaf0c114c9fb73462ef0a456d17"></a><ul id="ucae7bcaf0c114c9fb73462ef0a456d17"><li><span class="parmname" id="p1ddd09b15c164589a581c42870fee2bc"><a name="p1ddd09b15c164589a581c42870fee2bc"></a><a name="p1ddd09b15c164589a581c42870fee2bc"></a><b>Read</b></span>: permission to access the HDFS directory</li><li><span class="parmname" id="p0183cf61b4004e85b0cd5513ac45a19a"><a name="p0183cf61b4004e85b0cd5513ac45a19a"></a><a name="p0183cf61b4004e85b0cd5513ac45a19a"></a><b>Write</b></span>: permission to write data to the HDFS directory</li><li><span class="parmname" id="pff0f7c559c234a61b7d73b0ec6103e5a"><a name="pff0f7c559c234a61b7d73b0ec6103e5a"></a><a name="pff0f7c559c234a61b7d73b0ec6103e5a"></a><b>Execute</b></span>: permission to perform an operation. It must be selected when you add access or write permission.</li></ul>
    </td>
    </tr>
    <tr id="r54eb87c3650e4a2eb4acb7259388fef4"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.3.1.1 "><p id="af67bc44007bd452d8cbc6628a4c66195"><a name="af67bc44007bd452d8cbc6628a4c66195"></a><a name="af67bc44007bd452d8cbc6628a4c66195"></a><span class="parmname" id="pcc7f725d83fd46e59028af9969bd047f"><a name="pcc7f725d83fd46e59028af9969bd047f"></a><a name="pcc7f725d83fd46e59028af9969bd047f"></a><b>Files</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.3.1.2 "><p id="a564bf4462e94432db48caeeda638f7e0"><a name="a564bf4462e94432db48caeeda638f7e0"></a><a name="a564bf4462e94432db48caeeda638f7e0"></a>HDFS resource type, indicating a file in HDFS. It has the following permissions:</p>
    <a name="ucd9cb560a42f4b1b925a085e2647c31f"></a><a name="ucd9cb560a42f4b1b925a085e2647c31f"></a><ul id="ucd9cb560a42f4b1b925a085e2647c31f"><li><span class="parmname" id="p47019fabe7704834968fbbe5471c9f30"><a name="p47019fabe7704834968fbbe5471c9f30"></a><a name="p47019fabe7704834968fbbe5471c9f30"></a><b>Read</b></span>: permission to access the file</li><li><span class="parmname" id="pef5ec56195584efb84f787c7c2d4e01d"><a name="pef5ec56195584efb84f787c7c2d4e01d"></a><a name="pef5ec56195584efb84f787c7c2d4e01d"></a><b>Write</b></span>: permission to write data to the file</li><li><span class="parmname" id="p80a9121febdf48758c7fcf0a0dc2c848"><a name="p80a9121febdf48758c7fcf0a0dc2c848"></a><a name="p80a9121febdf48758c7fcf0a0dc2c848"></a><b>Execute</b></span>: permission to perform an operation. It must be selected when you add access or write permission.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    Permissions of an HDFS directory of each level are not shared by subdirectories by default. For example, if  **Read** and **Execute** permissions are added to the **tmp** directory, you must select **Recursive**  at the same time to add permissions to subdirectories.

    **Table  4**  Hive permission description

    <a name="t4f7df0830053493aa66863ccf1cd8c11"></a>
    <table><thead align="left"><tr id="r8ed047735c404203b81801681516a649"><th class="cellrowborder" valign="top" width="35%" id="mcps1.2.3.1.1"><p id="en-us_topic_0043021164_p298664815444"><a name="en-us_topic_0043021164_p298664815444"></a><a name="en-us_topic_0043021164_p298664815444"></a><strong id="aec9b9448acd34048b84ea34d2b4b2b83"><a name="aec9b9448acd34048b84ea34d2b4b2b83"></a><a name="aec9b9448acd34048b84ea34d2b4b2b83"></a>Resource Supporting Permission Management</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="65%" id="mcps1.2.3.1.2"><p id="a0ae4dda008f8417e96c0d3afa315a20e"><a name="a0ae4dda008f8417e96c0d3afa315a20e"></a><a name="a0ae4dda008f8417e96c0d3afa315a20e"></a><strong id="b4681674102259"><a name="b4681674102259"></a><a name="b4681674102259"></a>Permission Setting</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r4a67402b51ea416caf1219f2a706f1f7"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0043021164_p527748815444"><a name="en-us_topic_0043021164_p527748815444"></a><a name="en-us_topic_0043021164_p527748815444"></a><span class="parmname" id="p721b2c3374964b79b49bfe37b7da43a7"><a name="p721b2c3374964b79b49bfe37b7da43a7"></a><a name="p721b2c3374964b79b49bfe37b7da43a7"></a><b>Hive Admin Privilege</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.3.1.2 "><p id="ad8eee4230b144af6a9643f82d6222585"><a name="ad8eee4230b144af6a9643f82d6222585"></a><a name="ad8eee4230b144af6a9643f82d6222585"></a>Grants you Hive administrator rights.</p>
    </td>
    </tr>
    <tr id="r019cbf65411d4bedaddbeb6b8bdbd80c"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.3.1.1 "><p id="ac9a672e0f02546648dc9052d06e37e4a"><a name="ac9a672e0f02546648dc9052d06e37e4a"></a><a name="ac9a672e0f02546648dc9052d06e37e4a"></a><span class="parmname" id="p1076d705fbb245d1a22a8ba404cba257"><a name="p1076d705fbb245d1a22a8ba404cba257"></a><a name="p1076d705fbb245d1a22a8ba404cba257"></a><b>Database</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.3.1.2 "><p id="aaaeb77be1a2147ef8317843dbf82d82f"><a name="aaaeb77be1a2147ef8317843dbf82d82f"></a><a name="aaaeb77be1a2147ef8317843dbf82d82f"></a>Hive resource type, indicating a Hive database, which is used to store Hive tables. It has the following permissions:</p>
    <a name="u9e402a1b7e534acf93b86ed96d2f5494"></a><a name="u9e402a1b7e534acf93b86ed96d2f5494"></a><ul id="u9e402a1b7e534acf93b86ed96d2f5494"><li><span class="parmname" id="p92489014a5bc4aa48d6441cc73a75b19"><a name="p92489014a5bc4aa48d6441cc73a75b19"></a><a name="p92489014a5bc4aa48d6441cc73a75b19"></a><b>Select</b></span>: permission to query the Hive database</li><li><span class="parmname" id="p6d1a3ab54e1c4f5b843d5f5421d11a7a"><a name="p6d1a3ab54e1c4f5b843d5f5421d11a7a"></a><a name="p6d1a3ab54e1c4f5b843d5f5421d11a7a"></a><b>Delete</b></span>: permission to perform the deletion operation in the Hive database</li><li><span class="parmname" id="peb8374b9126244ac90b6401396ca26fd"><a name="peb8374b9126244ac90b6401396ca26fd"></a><a name="peb8374b9126244ac90b6401396ca26fd"></a><b>Insert</b></span>: permission to perform the insertion operation in the Hive database</li><li><span class="parmname" id="pd9827b0e6305477596b84f7a6cf3bf98"><a name="pd9827b0e6305477596b84f7a6cf3bf98"></a><a name="pd9827b0e6305477596b84f7a6cf3bf98"></a><b>Create</b></span>: permission to perform the creation operation in the Hive database</li></ul>
    </td>
    </tr>
    <tr id="r1496547ec63e44d3bd18c82c107cc037"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.3.1.1 "><p id="ae1a93b27dcbb4924bd4c5df1540861d3"><a name="ae1a93b27dcbb4924bd4c5df1540861d3"></a><a name="ae1a93b27dcbb4924bd4c5df1540861d3"></a><span class="parmname" id="p340ca8696f0a4f04ab6b6dd17177ab9b"><a name="p340ca8696f0a4f04ab6b6dd17177ab9b"></a><a name="p340ca8696f0a4f04ab6b6dd17177ab9b"></a><b>Table</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.3.1.2 "><p id="a8956be3a5ee84da8be666573b8018ff6"><a name="a8956be3a5ee84da8be666573b8018ff6"></a><a name="a8956be3a5ee84da8be666573b8018ff6"></a>Hive resource type, indicating a Hive table, which is used to store data. It has the following permissions:</p>
    <a name="u6af9766df03f44b1b7442d40c1a2d89e"></a><a name="u6af9766df03f44b1b7442d40c1a2d89e"></a><ul id="u6af9766df03f44b1b7442d40c1a2d89e"><li><span class="parmname" id="p3e66e991302c43958b27fd221313b1af"><a name="p3e66e991302c43958b27fd221313b1af"></a><a name="p3e66e991302c43958b27fd221313b1af"></a><b>Select</b></span>: permission to query the Hive table</li><li><span class="parmname" id="p69ca2686c2924639af31593ef953a5c4"><a name="p69ca2686c2924639af31593ef953a5c4"></a><a name="p69ca2686c2924639af31593ef953a5c4"></a><b>Delete</b></span>: permission to perform the deletion operation in the Hive table</li><li><span class="parmname" id="p7e7493f2ca824372911e9d207582cc8a"><a name="p7e7493f2ca824372911e9d207582cc8a"></a><a name="p7e7493f2ca824372911e9d207582cc8a"></a><b>Update</b></span>: grants users the&nbsp;<span class="parmvalue" id="p3f7f9e941e5644bcbb92c012a20a0730"><a name="p3f7f9e941e5644bcbb92c012a20a0730"></a><a name="p3f7f9e941e5644bcbb92c012a20a0730"></a><b>Update</b></span> permission of the Hive table</li><li><span class="parmname" id="pc46ad2290ddf45bb9ca81a095b86500f"><a name="pc46ad2290ddf45bb9ca81a095b86500f"></a><a name="pc46ad2290ddf45bb9ca81a095b86500f"></a><b>Insert</b></span>: permission to perform the insertion operation in the Hive table</li><li><span class="parmname" id="pa41f5e05a5624afeb5eae793cc28adf0"><a name="pa41f5e05a5624afeb5eae793cc28adf0"></a><a name="pa41f5e05a5624afeb5eae793cc28adf0"></a><b>Grant of Select</b></span>: permission to grant the&nbsp;<span class="parmvalue" id="p982e6612aca04d7a8735f39fe773f7c5"><a name="p982e6612aca04d7a8735f39fe773f7c5"></a><a name="p982e6612aca04d7a8735f39fe773f7c5"></a><b>Select</b></span> permission to other users using Hive statements</li><li><span class="parmname" id="pac54a1eee7074dd4a615b21e72af641e"><a name="pac54a1eee7074dd4a615b21e72af641e"></a><a name="pac54a1eee7074dd4a615b21e72af641e"></a><b>Grant of Delete</b></span>: permission to grant the&nbsp;<span class="parmvalue" id="p1b2c95f007764f7f9d6de8d9a3274eba"><a name="p1b2c95f007764f7f9d6de8d9a3274eba"></a><a name="p1b2c95f007764f7f9d6de8d9a3274eba"></a><b>Delete</b></span> permission to other users using Hive statements</li><li><span class="parmname" id="p567761cfbfef436691db183e8f2ec494"><a name="p567761cfbfef436691db183e8f2ec494"></a><a name="p567761cfbfef436691db183e8f2ec494"></a><b>Grant of Update</b></span>: permission to grant the&nbsp;<span class="parmvalue" id="p22bf19195d7a4cf58cb91b500e7b9a65"><a name="p22bf19195d7a4cf58cb91b500e7b9a65"></a><a name="p22bf19195d7a4cf58cb91b500e7b9a65"></a><b>Update</b></span> permission to other users using Hive statements</li><li><span class="parmname" id="p4899e94a6e2649c492b35d9a8cceb521"><a name="p4899e94a6e2649c492b35d9a8cceb521"></a><a name="p4899e94a6e2649c492b35d9a8cceb521"></a><b>Grant of Insert</b></span>: permission to grant the&nbsp;<span class="parmvalue" id="p791d56ddd6b1402db82c493eacc182d6"><a name="p791d56ddd6b1402db82c493eacc182d6"></a><a name="p791d56ddd6b1402db82c493eacc182d6"></a><b>Insert</b></span> permission to other users using Hive statements</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    Permissions of a Hive resource type of each level are shared by resource types of sub-levels by default. For example, if  **Select** and **Insert** permissions are added to the **default**  database, they are automatically added to the tables and columns in the database.

    **Table  5**  Yarn permission description

    <a name="t0bd2a70a5b84454984f26bcbb9c096c8"></a>
    <table><thead align="left"><tr id="rc63110d6d7bd4a888fc2e50582f17f15"><th class="cellrowborder" valign="top" width="35%" id="mcps1.2.3.1.1"><p id="a7f3f0fb3249144a193fcbef10281e43d"><a name="a7f3f0fb3249144a193fcbef10281e43d"></a><a name="a7f3f0fb3249144a193fcbef10281e43d"></a><strong id="a603438a561704c2cb24411e12dcf4244"><a name="a603438a561704c2cb24411e12dcf4244"></a><a name="a603438a561704c2cb24411e12dcf4244"></a>Resource Supporting Permission Management</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="65%" id="mcps1.2.3.1.2"><p id="a5035dfa0c3db4b6994119475cc5800e1"><a name="a5035dfa0c3db4b6994119475cc5800e1"></a><a name="a5035dfa0c3db4b6994119475cc5800e1"></a><strong id="b4768778102259"><a name="b4768778102259"></a><a name="b4768778102259"></a>Permission Setting</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r8fad2f7f4bfb49379d576ad267057d09"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.3.1.1 "><p id="a233e4eb974674f988682738fff463ff7"><a name="a233e4eb974674f988682738fff463ff7"></a><a name="a233e4eb974674f988682738fff463ff7"></a><span class="parmname" id="pfefb19c81d7043eda591cd3928cb0cd8"><a name="pfefb19c81d7043eda591cd3928cb0cd8"></a><a name="pfefb19c81d7043eda591cd3928cb0cd8"></a><b>Cluster Admin Operations</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.3.1.2 "><p id="a4ee049d431d24be3af9a6fdd383f3c59"><a name="a4ee049d431d24be3af9a6fdd383f3c59"></a><a name="a4ee049d431d24be3af9a6fdd383f3c59"></a>Grants you Yarn administrator rights.</p>
    </td>
    </tr>
    <tr id="rfd065a6baa114020985679c7d93d9f1b"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.3.1.1 "><p id="a5a155bee77be4b859d885a4719402b03"><a name="a5a155bee77be4b859d885a4719402b03"></a><a name="a5a155bee77be4b859d885a4719402b03"></a><span class="parmname" id="pf524ecda90a3419c99afd99e9cc96025"><a name="pf524ecda90a3419c99afd99e9cc96025"></a><a name="pf524ecda90a3419c99afd99e9cc96025"></a><b>root</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.3.1.2 "><p id="a9161217e4c5f4957ae04e5ce47729dde"><a name="a9161217e4c5f4957ae04e5ce47729dde"></a><a name="a9161217e4c5f4957ae04e5ce47729dde"></a>Root queue of Yarn. It has the following permissions:</p>
    <a name="uea4d58ac23fc41149fa19145092fe078"></a><a name="uea4d58ac23fc41149fa19145092fe078"></a><ul id="uea4d58ac23fc41149fa19145092fe078"><li><span class="parmname" id="p73cae124a40a445ca99790834449f01e"><a name="p73cae124a40a445ca99790834449f01e"></a><a name="p73cae124a40a445ca99790834449f01e"></a><b>Submit</b></span>: permission to submit jobs in the queue</li><li><span class="parmname" id="pe9471cef642040efa38574c0b3232891"><a name="pe9471cef642040efa38574c0b3232891"></a><a name="pe9471cef642040efa38574c0b3232891"></a><b>Admin</b></span>: permission to manage permissions of the current queue</li></ul>
    </td>
    </tr>
    <tr id="rd1d3b2f9377a425bb4c09973eacf2d7a"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.3.1.1 "><p id="a3ab24dec2ca5406cbe47470afc68bd42"><a name="a3ab24dec2ca5406cbe47470afc68bd42"></a><a name="a3ab24dec2ca5406cbe47470afc68bd42"></a><span class="parmname" id="p040c76b3a2a24a5da2879ed5bcee4ed7"><a name="p040c76b3a2a24a5da2879ed5bcee4ed7"></a><a name="p040c76b3a2a24a5da2879ed5bcee4ed7"></a><b>Parent Queue</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.3.1.2 "><p id="a1f889df4003c479399c65a23d0f46b68"><a name="a1f889df4003c479399c65a23d0f46b68"></a><a name="a1f889df4003c479399c65a23d0f46b68"></a>Yarn resource type, indicating a parent queue containing sub-queues. A root queue is a type of a parent queue. It has the following permissions:</p>
    <a name="uf5c5302087dd427e89b4364d86397a45"></a><a name="uf5c5302087dd427e89b4364d86397a45"></a><ul id="uf5c5302087dd427e89b4364d86397a45"><li><span class="parmname" id="parmname42097550102259"><a name="parmname42097550102259"></a><a name="parmname42097550102259"></a><b>Submit</b></span>: permission to submit jobs in the queue</li><li><span class="parmname" id="parmname54458361102259"><a name="parmname54458361102259"></a><a name="parmname54458361102259"></a><b>Admin</b></span>: permission to manage permissions of the current queue</li></ul>
    </td>
    </tr>
    <tr id="r3e309bc7386546fb93cd70f3caad8608"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.3.1.1 "><p id="a2bb2113b87e747b789b694bbd6fb6b01"><a name="a2bb2113b87e747b789b694bbd6fb6b01"></a><a name="a2bb2113b87e747b789b694bbd6fb6b01"></a><span class="parmname" id="pea85898b0e8645fa9444785594fbf32b"><a name="pea85898b0e8645fa9444785594fbf32b"></a><a name="pea85898b0e8645fa9444785594fbf32b"></a><b>Leaf Queue</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.3.1.2 "><p id="aeb439c9008a048b287979c05687c21b1"><a name="aeb439c9008a048b287979c05687c21b1"></a><a name="aeb439c9008a048b287979c05687c21b1"></a>Yarn resource type, indicating a leaf queue. It has the following permissions:</p>
    <a name="u76dc8616f21f48498452b627cd2a8cd6"></a><a name="u76dc8616f21f48498452b627cd2a8cd6"></a><ul id="u76dc8616f21f48498452b627cd2a8cd6"><li><span class="parmname" id="parmname41168445102259"><a name="parmname41168445102259"></a><a name="parmname41168445102259"></a><b>Submit</b></span>: permission to submit jobs in the queue</li><li><span class="parmname" id="pd53de07f43e7475990e8c8920ded95f6"><a name="pd53de07f43e7475990e8c8920ded95f6"></a><a name="pd53de07f43e7475990e8c8920ded95f6"></a><b>Admin</b></span>: permission to manage permissions of the current queue</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    Permissions of a Yarn resource type of each level are shared by resource types of sub-levels by default. For example, if the  **Submit** permission is added to the **root** queue, it is automatically added to the sub-queue. Permissions inherited by sub-queues will not be displayed as selected in the **Permission**  table.

    **Table  6**  Hue permission description

    <a name="table1633343619133"></a>
    <table><thead align="left"><tr id="row6155653719133"><th class="cellrowborder" valign="top" width="35%" id="mcps1.2.3.1.1"><p id="p2002362019133"><a name="p2002362019133"></a><a name="p2002362019133"></a><strong id="b2984254519319"><a name="b2984254519319"></a><a name="b2984254519319"></a>Resource Supporting Permission Management</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="65%" id="mcps1.2.3.1.2"><p id="p3459596019133"><a name="p3459596019133"></a><a name="p3459596019133"></a><strong id="b25127605102259"><a name="b25127605102259"></a><a name="b25127605102259"></a>Permission Setting</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5463116019133"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.3.1.1 "><p id="p6304782919133"><a name="p6304782919133"></a><a name="p6304782919133"></a><span class="parmname" id="parmname3055955119133"><a name="parmname3055955119133"></a><a name="parmname3055955119133"></a><b>Storage Policy Admin</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.3.1.2 "><p id="p5940456019133"><a name="p5940456019133"></a><a name="p5940456019133"></a>Grants you storage policy administrator rights.</p>
    </td>
    </tr>
    </tbody>
    </table>

4.  Click  **OK**. Return to **Manage Role**.

## Related Tasks<a name="s1930a76617e44577bb8e3d0fd36d1c17"></a>

**Modifying a role**

1.  On MRS Manager, click  **System**.
2.  In the  **Permission** area, click **Manage Role**.
3.  In the row of the role to be modified, click  **Modify**  to modify role information.

    >![](/images/icon-note.gif) **NOTE:**   
    >If you change permissions assigned to the role, it takes 3 minutes to make new configurations take effect.  

4.  Click  **OK**. The modification is complete.

**Deleting a role**

1.  On MRS Manager, click  **System**.
2.  In the  **Permission** area, click **Manage Role**.
3.  In the row of the role to be deleted, click  **Delete**.
4.  Click  **OK**. The role is deleted.

