# Configuring the Database Audit Log<a name="dws_01_0075"></a>

## Scenario<a name="section43782126162722"></a>

DWS allows you to record the audit log of specific operations, involving audit log retention policy, unauthorized access and DML, SELECT COPY, and DDL operations performed on the stored procedures and database objects.

After configuring the audit log, you can query the audit information to locate the fault cause or the historical operation record as needed when a data warehouse cluster is abnormal.

For details about how to view the audit log information, see section  **Database Security Management \> Viewing the Auditing Information**  in the  _Data Warehouse Service Database Developer Guide_.

## Prerequisites<a name="section6488541984957"></a>

You can change security settings only when  **Cluster Status**  is  **Available**  and  **Low performance**  and  **Task Information**  cannot be  **Creating snapshot**,  **Scaling out**,  **Configuring**, or  **Restarting**.

## Procedure<a name="section37372909114419"></a>

1.  Log in to the DWS management console.
2.  Click  **Cluster Management**.
3.  In the cluster list, click the name of a cluster. On the page that is displayed, click  **Security Settings**.

    By default,  **Configuration Status**  is  **Synchronized**, which indicates that the latest database result is displayed.

4.  In the  **Audit Settings**  area, set the audit log retention policy.

    **Figure  1**  Audit log retention policy<a name="fig168002419182"></a>  
    ![](figures/audit-log-retention-policy.png "audit-log-retention-policy")

    [Table 1](#table6661375615299)  describes the detailed information.

    **Table  1**  Audit log retention policy

    <a name="table6661375615299"></a>
    <table><thead align="left"><tr id="row1350660815299"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.3.1.1"><p id="p2029345315299"><a name="p2029345315299"></a><a name="p2029345315299"></a><strong id="b84235270692541_1"><a name="b84235270692541_1"></a><a name="b84235270692541_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="70%" id="mcps1.2.3.1.2"><p id="p3315697815299"><a name="p3315697815299"></a><a name="p3315697815299"></a><strong id="b842352706191716_1"><a name="b842352706191716_1"></a><a name="b842352706191716_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row136071215299"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p4310885415299"><a name="p4310885415299"></a><a name="p4310885415299"></a><strong id="b172633267343"><a name="b172633267343"></a><a name="b172633267343"></a>Audit Log Retention Policy</strong></p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p215632515299"><a name="p215632515299"></a><a name="p215632515299"></a>Specifies the audit log retention policy. Possible values are:</p>
    <a name="ul1940693315299"></a><a name="ul1940693315299"></a><ul id="ul1940693315299"><li><span class="parmname" id="parmname76964790510518"><a name="parmname76964790510518"></a><a name="parmname76964790510518"></a><b>Space priority</b></span>: Audit logs will be automatically deleted if the size of audit logs on a single node exceeds 1 GB.</li><li><span class="parmvalue" id="parmvalue55512574410647"><a name="parmvalue55512574410647"></a><a name="parmvalue55512574410647"></a><b>Time priority</b></span>: Audit logs will be retained within the minimum retention period. After this period expires, audit logs will be automatically deleted if the size of audit logs on a single node exceeds 1 GB.</li></ul>
    <p id="p1413425815299"><a name="p1413425815299"></a><a name="p1413425815299"></a><span class="parmname" id="parmname93152852510822"><a name="parmname93152852510822"></a><a name="parmname93152852510822"></a><b>Space priority</b></span> is preferred.</p>
    <div class="note" id="note402425015299"><a name="note402425015299"></a><a name="note402425015299"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p3621825515299"><a name="p3621825515299"></a><a name="p3621825515299"></a>Clusters 1.0.0 and 1.1.0 do not support the audit log retention policy.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row5752884715299"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p2932501615299"><a name="p2932501615299"></a><a name="p2932501615299"></a><strong id="b139252053181518"><a name="b139252053181518"></a><a name="b139252053181518"></a>Minimum Retention Period (Day)</strong></p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p2651609415299"><a name="p2651609415299"></a><a name="p2651609415299"></a>This parameter is valid when <span class="parmname" id="parmname769647905102052"><a name="parmname769647905102052"></a><a name="parmname769647905102052"></a><b>Audit Log Retention Policy</b></span> is set to <span class="parmvalue" id="parmvalue2023397336102111"><a name="parmvalue2023397336102111"></a><a name="parmvalue2023397336102111"></a><b>Time priority</b></span>.</p>
    <p id="p287978615299"><a name="p287978615299"></a><a name="p287978615299"></a>The value ranges from 0 to 730 days. The default value is <strong id="b842352706102151"><a name="b842352706102151"></a><a name="b842352706102151"></a>90</strong> days.</p>
    </td>
    </tr>
    </tbody>
    </table>

5.  Enable the audit function for the following operations if necessary.

    ![](figures/icon-button4.png)  indicates that the audit function is enabled.  ![](figures/icon_dws_off.jpg)  indicates that the audit function is disabled.

    **Figure  2**  Audit items<a name="fig33013552162725"></a>  
    ![](figures/audit-items.png "audit-items")

    [Table 2](#table48954270153356)  describes the detailed information about the audit items.

    **Table  2**  Audit items

    <a name="table48954270153356"></a>
    <table><thead align="left"><tr id="row11786533153356"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.3.1.1"><p id="p15185148153356"><a name="p15185148153356"></a><a name="p15185148153356"></a><strong id="b84235270692541_3"><a name="b84235270692541_3"></a><a name="b84235270692541_3"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="70%" id="mcps1.2.3.1.2"><p id="p22037438153356"><a name="p22037438153356"></a><a name="p22037438153356"></a><strong id="b842352706191716_3"><a name="b842352706191716_3"></a><a name="b842352706191716_3"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row40202069153356"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p35142185153356"><a name="p35142185153356"></a><a name="p35142185153356"></a><strong id="b20858182043518"><a name="b20858182043518"></a><a name="b20858182043518"></a>Audit Unauthorized Access</strong></p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p27944737153356"><a name="p27944737153356"></a><a name="p27944737153356"></a>Specifies whether to record unauthorized operations. This parameter is disabled by default.</p>
    </td>
    </tr>
    <tr id="row48931238153356"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p4007327153356"><a name="p4007327153356"></a><a name="p4007327153356"></a><strong id="b13708516151710"><a name="b13708516151710"></a><a name="b13708516151710"></a>Audit DML Execution</strong></p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p56158069153356"><a name="p56158069153356"></a><a name="p56158069153356"></a>Specifies whether to record <strong id="b115161075393652"><a name="b115161075393652"></a><a name="b115161075393652"></a>INSERT</strong>, <strong id="b7000329193652"><a name="b7000329193652"></a><a name="b7000329193652"></a>UPDATE</strong>, and <strong id="b16768784293652"><a name="b16768784293652"></a><a name="b16768784293652"></a>DELETE</strong> operations on tables. This parameter is disabled by default.</p>
    </td>
    </tr>
    <tr id="row15098169153356"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p14992206153356"><a name="p14992206153356"></a><a name="p14992206153356"></a><strong id="b14991153916171"><a name="b14991153916171"></a><a name="b14991153916171"></a>Audit SELECT Execution</strong></p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p6409196153356"><a name="p6409196153356"></a><a name="p6409196153356"></a>Specifies whether to record the <strong id="b151641596594749"><a name="b151641596594749"></a><a name="b151641596594749"></a>SELECT</strong> operation. This parameter is disabled by default.</p>
    </td>
    </tr>
    <tr id="row41792394153356"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p29740772153356"><a name="p29740772153356"></a><a name="p29740772153356"></a><strong id="b1079743214362"><a name="b1079743214362"></a><a name="b1079743214362"></a>Audit Stored Procedure Execution</strong></p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p60192322153356"><a name="p60192322153356"></a><a name="p60192322153356"></a>Specifies whether to record operations when executing the stored procedure or user-defined functions. This parameter is disabled by default.</p>
    </td>
    </tr>
    <tr id="row43739917153356"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p53272364153356"><a name="p53272364153356"></a><a name="p53272364153356"></a><strong id="b695333783619"><a name="b695333783619"></a><a name="b695333783619"></a>Audit COPY Execution</strong></p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p20094216153356"><a name="p20094216153356"></a><a name="p20094216153356"></a>Specifies whether to record the <strong id="b46630216153356"><a name="b46630216153356"></a><a name="b46630216153356"></a>COPY</strong> operation. This parameter is disabled by default.</p>
    </td>
    </tr>
    <tr id="row18951113153356"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p58645179153356"><a name="p58645179153356"></a><a name="p58645179153356"></a><strong id="b153698461817"><a name="b153698461817"></a><a name="b153698461817"></a>Audit DDL Objects</strong></p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p52639045153356"><a name="p52639045153356"></a><a name="p52639045153356"></a>Specifies whether to record the <strong id="b84235270695347"><a name="b84235270695347"></a><a name="b84235270695347"></a>CREATE</strong>, <strong id="b84235270695352"><a name="b84235270695352"></a><a name="b84235270695352"></a>DROP</strong>, and <strong id="b84235270695356"><a name="b84235270695356"></a><a name="b84235270695356"></a>ALTER</strong> operations of specified database objects. <span class="parmname" id="parmname1346420704102813"><a name="parmname1346420704102813"></a><a name="parmname1346420704102813"></a><b>Database</b></span>, <span class="parmname" id="parmname297077118102813"><a name="parmname297077118102813"></a><a name="parmname297077118102813"></a><b>Schema</b></span>, and <span class="parmname" id="parmname1289243348102813"><a name="parmname1289243348102813"></a><a name="parmname1289243348102813"></a><b>User</b></span> are selected by default. Other objects are not selected by default.</p>
    </td>
    </tr>
    </tbody>
    </table>

    Except audit items listed in  [Table 2](#table48954270153356), key audit items in  [Table 3](#table24262392153654)  are enabled by default in DWS.

    **Table  3**  Key audit items

    <a name="table24262392153654"></a>
    <table><thead align="left"><tr id="row1697543153654"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.3.1.1"><p id="p3283271153654"><a name="p3283271153654"></a><a name="p3283271153654"></a><strong id="b84235270692541_5"><a name="b84235270692541_5"></a><a name="b84235270692541_5"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="70%" id="mcps1.2.3.1.2"><p id="p64618408153654"><a name="p64618408153654"></a><a name="p64618408153654"></a><strong id="b842352706191716_5"><a name="b842352706191716_5"></a><a name="b842352706191716_5"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row66708561153654"><td class="cellrowborder" rowspan="5" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p34684395153654"><a name="p34684395153654"></a><a name="p34684395153654"></a>Key audit items</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p51991696153654"><a name="p51991696153654"></a><a name="p51991696153654"></a>Records successful and failed login and deregistration information.</p>
    </td>
    </tr>
    <tr id="row65272081153654"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p52547180153654"><a name="p52547180153654"></a><a name="p52547180153654"></a>Records database startup, stop, recovery, and failover audit information.</p>
    </td>
    </tr>
    <tr id="row3162576153654"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p54842140153654"><a name="p54842140153654"></a><a name="p54842140153654"></a>Records a user's lock and unlock information.</p>
    </td>
    </tr>
    <tr id="row23817212153654"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p50146049153654"><a name="p50146049153654"></a><a name="p50146049153654"></a>Records the grants and reclaims of a user's permission.</p>
    </td>
    </tr>
    <tr id="row48661263153654"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p49248264153654"><a name="p49248264153654"></a><a name="p49248264153654"></a>Records the audit function of the SET operation.</p>
    </td>
    </tr>
    </tbody>
    </table>

6.  Click  **Apply**.

    On the  **Security Settings**  page, click  ![](figures/icon_dws_refresh_blue.jpg). If  **Configuration Status**  is  **Applying**, the system is saving the settings.

    Wait for a moment and then refresh  **Configuration Status**. When  **Configuration Status**  is  **Synchronized**, the configuration is saved and takes effect.


