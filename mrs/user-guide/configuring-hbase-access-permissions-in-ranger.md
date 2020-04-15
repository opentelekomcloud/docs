# Configuring HBase Access Permissions in Ranger<a name="EN-US_TOPIC_0228886237"></a>

After an MRS cluster with Ranger installed is created, HBase access control is not integrated into Ranger. This section describes how to integrate HBase into Ranger.

1.  Log in to the Ranger web UI.
2.  In the  **Service Manager**  area, click  ![](figures/en-us_image_0228886616.png)  next to  **HBASE**  to add an HBase service.

    **Figure  1**  Adding an HBase service<a name="fig1355517248383"></a>  
    ![](figures/adding-an-hbase-service.png "adding-an-hbase-service")

3.  Set the parameters for adding an HBase service according to  [Table 1](#table74220350178). Use the default values for the parameters that are not listed in the table.

    **Table  1**  Parameter description

    <a name="table74220350178"></a>
    <table><thead align="left"><tr id="row1743935151719"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p13378105233519"><a name="p13378105233519"></a><a name="p13378105233519"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p7378652143515"><a name="p7378652143515"></a><a name="p7378652143515"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p337875211359"><a name="p337875211359"></a><a name="p337875211359"></a>Example Value</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row94373551718"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p13783525354"><a name="p13783525354"></a><a name="p13783525354"></a>Service Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p10378952103511"><a name="p10378952103511"></a><a name="p10378952103511"></a>Name of the service to be created. The value is fixed to <strong id="b6341155601315"><a name="b6341155601315"></a><a name="b6341155601315"></a>hbasedev</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p143789524351"><a name="p143789524351"></a><a name="p143789524351"></a>hbasedev</p>
    </td>
    </tr>
    <tr id="row154353515177"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1037885253516"><a name="p1037885253516"></a><a name="p1037885253516"></a>Username</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p203781552183511"><a name="p203781552183511"></a><a name="p203781552183511"></a>You can set this parameter to any value.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p193781526356"><a name="p193781526356"></a><a name="p193781526356"></a>admin</p>
    </td>
    </tr>
    <tr id="row243143511179"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p13379115223515"><a name="p13379115223515"></a><a name="p13379115223515"></a>Password</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p437945273517"><a name="p437945273517"></a><a name="p437945273517"></a>You can set this parameter to any value.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p123791352153520"><a name="p123791352153520"></a><a name="p123791352153520"></a>-</p>
    </td>
    </tr>
    <tr id="row343153551716"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1243163517179"><a name="p1243163517179"></a><a name="p1243163517179"></a>hadoop.security.authentication</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p243103561716"><a name="p243103561716"></a><a name="p243103561716"></a>Hadoop authentication mode. The value is fixed to <strong id="b137387313142"><a name="b137387313142"></a><a name="b137387313142"></a>Simple</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p843133512171"><a name="p843133512171"></a><a name="p843133512171"></a>Simple</p>
    </td>
    </tr>
    <tr id="row174315352174"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p12432355173"><a name="p12432355173"></a><a name="p12432355173"></a>hbase.security.authentication</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p54303512175"><a name="p54303512175"></a><a name="p54303512175"></a>HBase authentication mode. The value is fixed to <strong id="b10695349144"><a name="b10695349144"></a><a name="b10695349144"></a>Simple</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p184373591715"><a name="p184373591715"></a><a name="p184373591715"></a>Simple</p>
    </td>
    </tr>
    <tr id="row174314357170"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p343153517173"><a name="p343153517173"></a><a name="p343153517173"></a>hbase.zookeeper.property.clientPort</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1543173551716"><a name="p1543173551716"></a><a name="p1543173551716"></a>Port number of ZooKeeper in the HBase cluster</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p16432358177"><a name="p16432358177"></a><a name="p16432358177"></a>2181</p>
    </td>
    </tr>
    <tr id="row1043335111715"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p343183531710"><a name="p343183531710"></a><a name="p343183531710"></a>hbase.zookeeper.quorum</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p14431735181716"><a name="p14431735181716"></a><a name="p14431735181716"></a>ZooKeeper address in the HBase cluster</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p13980205719194"><a name="p13980205719194"></a><a name="p13980205719194"></a>192.168.0.7,192.168.0.8,192.168.0.9</p>
    </td>
    </tr>
    <tr id="row19708163015201"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1370953092011"><a name="p1370953092011"></a><a name="p1370953092011"></a>zookeeper.znode.parent</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p4709123012208"><a name="p4709123012208"></a><a name="p4709123012208"></a>Path of the root node of HBase in ZooKeeper. The value is fixed to <strong id="b1550684011515"><a name="b1550684011515"></a><a name="b1550684011515"></a>/hbase</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p4709163092020"><a name="p4709163092020"></a><a name="p4709163092020"></a>/hbase</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Figure  2**  Create Service<a name="fig39091316015"></a>  
    ![](figures/create-service-61.png "create-service-61")

4.  Click  **Add**  to add the service.
5.  Start the Ranger HBase plugin to authorize Ranger to manage HBase.
    1.  Log in to MRS Manager.
    2.  Choose  **Services**  \>  **HBase**  \>  **Service Configuration**, and set  **Type**  to  **All**.
    3.  Search for  **hbase.security.authorization**  and change its value to  **true**  \(select the first HBase parameter\).
    4.  Search for  **hbase.coprocessor.master.classes**  and append  **,org.apache.ranger.authorization.hbase.RangerAuthorizationCoprocessor**  to its original value.
    5.  Search for  **hbase.coprocessor.region.classes**  and append  **,org.apache.ranger.authorization.hbase.RangerAuthorizationCoprocessor**  to its original value.
    6.  Click  **Save Configuration**  and select  **Restart the affected services or instances**  to restart the HMaster and RegionServer instances.

6.  Create a policy under  **HBase Service hbasedev**.
    1.  Log in to the Ranger web UI.
    2.  In the  **HBASE**  area, click the added service  **hbasedev**.
    3.  Click  **Add New Policy**  to add an access control policy.
    4.  Set the parameters according to  [Table 2](#table116322231534). Use the default values for the parameters that are not listed in the table.

        **Table  2**  Parameter description

        <a name="table116322231534"></a>
        <table><thead align="left"><tr id="row11633152314316"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p1260833016420"><a name="p1260833016420"></a><a name="p1260833016420"></a>Parameter</p>
        </th>
        <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p156082301046"><a name="p156082301046"></a><a name="p156082301046"></a>Description</p>
        </th>
        <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p1060811302417"><a name="p1060811302417"></a><a name="p1060811302417"></a>Example Value</p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row1163310231234"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1865510429816"><a name="p1865510429816"></a><a name="p1865510429816"></a>Policy Name</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p19547132615414"><a name="p19547132615414"></a><a name="p19547132615414"></a>Policy name</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p46331231316"><a name="p46331231316"></a><a name="p46331231316"></a>Policy002</p>
        </td>
        </tr>
        <tr id="row9633142318314"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p11633172313315"><a name="p11633172313315"></a><a name="p11633172313315"></a>HBase Table</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p45473261944"><a name="p45473261944"></a><a name="p45473261944"></a>Name of the HBase table that the policy allows to access</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p2063314239314"><a name="p2063314239314"></a><a name="p2063314239314"></a>test1</p>
        </td>
        </tr>
        <tr id="row863372320317"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p16335231835"><a name="p16335231835"></a><a name="p16335231835"></a>HBase Column-family</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p054718261244"><a name="p054718261244"></a><a name="p054718261244"></a>Column family of the HBase table that the policy allows to access</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p176331023136"><a name="p176331023136"></a><a name="p176331023136"></a>cf1</p>
        </td>
        </tr>
        <tr id="row1663420237318"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p663414239318"><a name="p663414239318"></a><a name="p663414239318"></a>HBase Column</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1754752616416"><a name="p1754752616416"></a><a name="p1754752616416"></a>Column name of the table corresponding to the HBase table that the policy allows to access</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1063412318311"><a name="p1063412318311"></a><a name="p1063412318311"></a>name</p>
        </td>
        </tr>
        <tr id="row463413231318"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1263412231934"><a name="p1263412231934"></a><a name="p1263412231934"></a>Allow Conditions</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><a name="ul291972075620"></a><a name="ul291972075620"></a><ul id="ul291972075620"><li><strong id="b1804939152017"><a name="b1804939152017"></a><a name="b1804939152017"></a>Select Group</strong>: user group that the policy allows to access</li><li><strong id="b106013419203"><a name="b106013419203"></a><a name="b106013419203"></a>Select User</strong>: user in the user group that the policy allows to access</li><li><strong id="b18863104282018"><a name="b18863104282018"></a><a name="b18863104282018"></a>Permissions</strong>: permissions that the policy allows the user to use</li></ul>
        </td>
        <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><a name="ul11428874228"></a><a name="ul11428874228"></a><ul id="ul11428874228"><li>Select Group: <strong id="b21006446206"><a name="b21006446206"></a><a name="b21006446206"></a>testuser</strong></li><li>Select User: <strong id="b1437524511209"><a name="b1437524511209"></a><a name="b1437524511209"></a>testuser</strong></li><li>Permissions: <strong id="b17345104615201"><a name="b17345104615201"></a><a name="b17345104615201"></a>Create</strong> and <strong id="b183461146132016"><a name="b183461146132016"></a><a name="b183461146132016"></a>select</strong></li></ul>
        </td>
        </tr>
        </tbody>
        </table>

        **Figure  3**  Adding an access control policy<a name="fig2047532791212"></a>  
        ![](figures/adding-an-access-control-policy-62.png "adding-an-access-control-policy-62")

    5.  Click  **Add**  to add the policy. According to the preceding policy, user  **testuser**  in the  **testuser**  user group has the  **Create**  and  **select**  permissions on the  **cf1:name**  column in the  **test1**  table of the  **default**  namespace in HBase, but no permission to access other columns.

7.  Update and log in to the HBase client by referring to  [Using HBase from Scratch](using-hbase-from-scratch.md), and check whether HBase has been integrated into Ranger.
    1.  Run the following command to access the HBase shell:

        **source /opt/client/bigdata\_env**

        **hbase shell**

        **Figure  4**  Accessing the HBase shell<a name="fig194139416157"></a>  
        ![](figures/accessing-the-hbase-shell.png "accessing-the-hbase-shell")

    2.  Add data and check whether Ranger is integrated.

        1.  Add data to the  **cf1:name**  column in the  **test1**  table.

            **put 'test1','001','cf1:name','tom'**

        2.  Add data to the  **cf1:age**  column in the  **test1**  table. If the user has no permission to access this column, the data fails to be added.

            **put 'test1','001','cf1:age',10**

        **Figure  5**  Verifying Ranger integration<a name="fig11361364170"></a>  
        ![](figures/verifying-ranger-integration-63.png "verifying-ranger-integration-63")



