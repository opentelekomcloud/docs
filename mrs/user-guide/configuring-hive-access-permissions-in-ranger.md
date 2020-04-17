# Configuring Hive Access Permissions in Ranger<a name="EN-US_TOPIC_0228886236"></a>

After an MRS cluster with Ranger installed is created, Hive access control is not integrated into Ranger. This section describes how to integrate Hive into Ranger.

1.  Log in to the Ranger web UI.
2.  In the  **Service Manager**  area, click  ![](figures/icon_mrs_jiahao.png)  next to  **HIVE**  to add a Hive service.

    **Figure  1**  Adding a Hive service<a name="fig1355517248383"></a>  
    ![](figures/adding-a-hive-service.png "adding-a-hive-service")

3.  Set the parameters for adding a Hive service according to  [Table 1](#table54444329411). Use the default values for the parameters that are not listed in the table.

    **Table  1**  Parameter description

    <a name="table54444329411"></a>
    <table><thead align="left"><tr id="row1844243264112"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p12442193220418"><a name="p12442193220418"></a><a name="p12442193220418"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p1744210322416"><a name="p1744210322416"></a><a name="p1744210322416"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p84421328419"><a name="p84421328419"></a><a name="p84421328419"></a>Example Value</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row644393284112"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p18442232184110"><a name="p18442232184110"></a><a name="p18442232184110"></a>Service Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p8442203254115"><a name="p8442203254115"></a><a name="p8442203254115"></a>Name of the service to be created. The value is fixed to <strong id="b6448272528"><a name="b6448272528"></a><a name="b6448272528"></a>hivedev</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p14442133211411"><a name="p14442133211411"></a><a name="p14442133211411"></a>hivedev</p>
    </td>
    </tr>
    <tr id="row34433328419"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p6443153216418"><a name="p6443153216418"></a><a name="p6443153216418"></a>Username</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p12443832114118"><a name="p12443832114118"></a><a name="p12443832114118"></a>You can set this parameter to any value.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p0443532194110"><a name="p0443532194110"></a><a name="p0443532194110"></a>admin</p>
    </td>
    </tr>
    <tr id="row74431532164110"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p544313323411"><a name="p544313323411"></a><a name="p544313323411"></a>Password</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p7443133224114"><a name="p7443133224114"></a><a name="p7443133224114"></a>You can set this parameter to any value.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p044333212412"><a name="p044333212412"></a><a name="p044333212412"></a>-</p>
    </td>
    </tr>
    <tr id="row144353274113"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p94431332194118"><a name="p94431332194118"></a><a name="p94431332194118"></a>jdbc.driverClassName</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p14431132144114"><a name="p14431132144114"></a><a name="p14431132144114"></a>Driver class for connecting to Hive. The value is fixed to <strong id="b8102631115313"><a name="b8102631115313"></a><a name="b8102631115313"></a>org.apache.hive.jdbc.HiveDriver</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p5443153210414"><a name="p5443153210414"></a><a name="p5443153210414"></a>org.apache.hive.jdbc.HiveDriver</p>
    </td>
    </tr>
    <tr id="row104441332194110"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p13443123216418"><a name="p13443123216418"></a><a name="p13443123216418"></a>jdbc.url</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p15443132174118"><a name="p15443132174118"></a><a name="p15443132174118"></a>URL for connecting to Hive. The format is ZooKeeper mode:</p>
    <p id="p11444132204117"><a name="p11444132204117"></a><a name="p11444132204117"></a><strong id="b136610246548"><a name="b136610246548"></a><a name="b136610246548"></a>jdbc:hive2://&lt;host&gt;:2181/;serviceDiscoveryMode=zooKeeper;zooKeeperNamespace=hiveserver2</strong></p>
    <p id="p717612451575"><a name="p717612451575"></a><a name="p717612451575"></a><strong id="b743982811548"><a name="b743982811548"></a><a name="b743982811548"></a>&lt;host&gt;</strong> indicates a ZooKeeper address. To obtain the ZooKeeper address, log in to MRS Manager, choose <strong id="b14494144916543"><a name="b14494144916543"></a><a name="b14494144916543"></a>Services</strong> &gt; <strong id="b88704510546"><a name="b88704510546"></a><a name="b88704510546"></a>ZooKeeper</strong> &gt; <strong id="b912545413542"><a name="b912545413542"></a><a name="b912545413542"></a>Instance</strong>, and view the management IP address of the ZooKeeper instance.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p12444163244112"><a name="p12444163244112"></a><a name="p12444163244112"></a>jdbc:hive2://xx.xx.xx.xx:2181,xx.xx.xx.xx:2181,xx.xx.xx.xx:2181/;serviceDiscoveryMode=zooKeeper;zooKeeperNamespace=hiveserver2</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Figure  2**  Create Service<a name="fig39091316015"></a>  
    ![](figures/create-service.png "create-service")

4.  Click  **Add**  to add the service.
5.  Start the Ranger Hive plugin to authorize Ranger to manage Hive.
    1.  Log in to MRS Manager.
    2.  Choose  **Services**  \>  **Hive**  \>  **Service Configuration**, and set  **Type**  to  **All**.
    3.  Search for  **hive.security.authorization**  and modify the following configurations:
        -   hive.security.authorization.enabled = true
        -   hive.security.authorization.manager = org.apache.ranger.authorization.hive.authorizer.RangerHiveAuthorizerFactory

    4.  Click  **Save Configuration**  and select  **Restart the affected services or instances**  to restart the Hive service.

6.  Add an access control policy.
    1.  Log in to the Ranger web UI.
    2.  In the  **HIVE**  area, click the added service  **hivedev**.
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
        <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p46331231316"><a name="p46331231316"></a><a name="p46331231316"></a>Policy001</p>
        </td>
        </tr>
        <tr id="row9633142318314"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p11633172313315"><a name="p11633172313315"></a><a name="p11633172313315"></a>database</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p45473261944"><a name="p45473261944"></a><a name="p45473261944"></a>Name of the database that the policy allows to access</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p2063314239314"><a name="p2063314239314"></a><a name="p2063314239314"></a>test</p>
        </td>
        </tr>
        <tr id="row863372320317"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p16335231835"><a name="p16335231835"></a><a name="p16335231835"></a>table</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p054718261244"><a name="p054718261244"></a><a name="p054718261244"></a>Name of the table corresponding to the database that the policy allows to access</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p176331023136"><a name="p176331023136"></a><a name="p176331023136"></a>table1</p>
        </td>
        </tr>
        <tr id="row1663420237318"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p663414239318"><a name="p663414239318"></a><a name="p663414239318"></a>Hive Column</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1754752616416"><a name="p1754752616416"></a><a name="p1754752616416"></a>Column name of the table corresponding to the database that the policy allows to access</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1063412318311"><a name="p1063412318311"></a><a name="p1063412318311"></a>name</p>
        </td>
        </tr>
        <tr id="row463413231318"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1263412231934"><a name="p1263412231934"></a><a name="p1263412231934"></a>Allow Conditions</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><a name="ul291972075620"></a><a name="ul291972075620"></a><ul id="ul291972075620"><li><strong id="b375917178217"><a name="b375917178217"></a><a name="b375917178217"></a>Select Group</strong>: user group that the policy allows to access</li><li><strong id="b291717191610"><a name="b291717191610"></a><a name="b291717191610"></a>Select User</strong>: user in the user group that the policy allows to access</li><li><strong id="b11552113913610"><a name="b11552113913610"></a><a name="b11552113913610"></a>Permissions</strong>: permissions that the policy allows the user to use</li></ul>
        </td>
        <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><a name="ul11428874228"></a><a name="ul11428874228"></a><ul id="ul11428874228"><li>Select Group: <strong id="b4790438473"><a name="b4790438473"></a><a name="b4790438473"></a>testuser</strong></li><li>Select User: <strong id="b12144183717717"><a name="b12144183717717"></a><a name="b12144183717717"></a>testuser</strong></li><li>Permissions: <strong id="b19928193317712"><a name="b19928193317712"></a><a name="b19928193317712"></a>Create</strong> and <strong id="b10441153518712"><a name="b10441153518712"></a><a name="b10441153518712"></a>select</strong></li></ul>
        </td>
        </tr>
        </tbody>
        </table>

        **Figure  3**  Adding an access control policy<a name="fig2047532791212"></a>  
        ![](figures/adding-an-access-control-policy.png "adding-an-access-control-policy")

    5.  Click  **Add**  to add the policy. According to the preceding policy, user  **testuser**  in the  **testuser**  user group has the  **Create**  and  **select**  permissions on the  **name**  column of  **table1**  in the  **test**  database of Hive, but no permission to access other columns.

7.  Log in to the Hive client by referring to  [Using Hive from Scratch](using-hive-from-scratch.md), and check whether Hive has been integrated into Ranger.
    1.  Run the following command to access the Hive beeline:

        **source /opt/client/bigdata\_env**

        **beeline**

    2.  Run the following command to set up a connection and log in as user  **testuser**:

        **!connect jdbc:hive2://xx.xx.xx.xx:2181,xx.xx.3.81:2181,192.168.3.153:2181/;serviceDiscoveryMode=zooKeeper;zooKeeperNamespace=hiveserver2**

        **Figure  4**  Logging in to Hive<a name="fig6187121122713"></a>  
        ![](figures/logging-in-to-hive.png "logging-in-to-hive")

    3.  Query data and check whether Ranger is integrated.

        **Figure  5**  Verifying Ranger integration<a name="fig19585153615368"></a>  
        ![](figures/verifying-ranger-integration.png "verifying-ranger-integration")



