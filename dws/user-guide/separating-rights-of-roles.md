# Separating Rights of Roles<a name="dws_01_0074"></a>

## Scenario<a name="section43782126162722"></a>

By default, the administrator user created during data warehouse cluster creation is a database system administrator, who can create other users and view the audit logs of the database. The rights separation mode is disabled.

To protect cluster data, DWS supports separation of rights of roles so that different roles have different rights.

For details about the default permission model and the permission model with rights separation enabled, see section  **Separation of Rights**  in the  _Data Warehouse Service Database Developer Guide_.

## Impact on the System<a name="section32447445163911"></a>

After you have modified the security parameters and the modifications take effect, the cluster may be restarted, which makes the cluster unavailable temporarily.

## Prerequisites<a name="section6488541984957"></a>

To modify the cluster's security configuration, ensure that the following conditions are met:

-   The  **Cluster Status**  is  **Available**  or  **Low performance**.
-   The  **Task Information**  cannot be  **Creating snapshot**,  **Scaling out**,  **Configuring**, or  **Restarting**.

## Procedure<a name="section63097435164448"></a>

1.  Log in to the management console at  [https://console.otc.t-systems.com/dws/](https://console.otc.t-systems.com/dws/).
2.  In the navigation tree on the left, click  **Cluster Management**.
3.  In the cluster list, click the name of a cluster. On the page that is displayed, click  **Security Settings**.

    By default,  **Configuration Status**  is  **Synchronized**, which indicates that the latest database result is displayed.

4.  On the  **Security Settings**  page, specify  **Security**.

    **Figure  1**  View of security configurations<a name="fig151823755214"></a>  
    ![](figures/view-of-security-configurations.png "view-of-security-configurations")

    **Table  1**  Security parameters

    <a name="table19251053172511"></a>
    <table><thead align="left"><tr id="row1625953112519"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.1"><p id="p32612535253"><a name="p32612535253"></a><a name="p32612535253"></a><strong id="b7617970162543"><a name="b7617970162543"></a><a name="b7617970162543"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="59%" id="mcps1.2.4.1.2"><p id="p11261153202515"><a name="p11261153202515"></a><a name="p11261153202515"></a><strong id="b842352706181449"><a name="b842352706181449"></a><a name="b842352706181449"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.3"><p id="p15261253162517"><a name="p15261253162517"></a><a name="p15261253162517"></a><strong id="b60793810112357"><a name="b60793810112357"></a><a name="b60793810112357"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1026135312253"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p026165312514"><a name="p026165312514"></a><a name="p026165312514"></a>Rights Separation</p>
    </td>
    <td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.2 "><p id="p19353101144415"><a name="p19353101144415"></a><a name="p19353101144415"></a><a name="image216611212216"></a><a name="image216611212216"></a><span><img id="image216611212216" src="figures/icon-button1.png"></span> indicates that <strong id="b18640311446"><a name="b18640311446"></a><a name="b18640311446"></a>Rights Separation</strong> is enabled. After <strong id="b11513713112915"><a name="b11513713112915"></a><a name="b11513713112915"></a>Rights Separation</strong> is enabled, set the usernames and passwords of the <span class="parmname" id="parmname19781122834618"><a name="parmname19781122834618"></a><a name="parmname19781122834618"></a><b>Security Administrator</b></span> and <span class="parmname" id="parmname97821028144614"><a name="parmname97821028144614"></a><a name="parmname97821028144614"></a><b>Audit Administrator</b></span>. The system automatically creates the two users. You can use the two users to connect to the databases and perform database-related operations.</p>
    <p id="p1326125372513"><a name="p1326125372513"></a><a name="p1326125372513"></a><a name="image12352443922"></a><a name="image12352443922"></a><span><img id="image12352443922" src="figures/icon-dws-off.jpg"></span> indicates that <strong id="b9728317508"><a name="b9728317508"></a><a name="b9728317508"></a>Rights Separation</strong> is disabled. By default, <strong id="b1786383994418"><a name="b1786383994418"></a><a name="b1786383994418"></a>Rights Separation</strong> is disabled.</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.3 "><p id="p5268539256"><a name="p5268539256"></a><a name="p5268539256"></a>-</p>
    </td>
    </tr>
    <tr id="row626115316259"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p326105342511"><a name="p326105342511"></a><a name="p326105342511"></a>Security Administrator</p>
    </td>
    <td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.2 "><p id="p1125715255316"><a name="p1125715255316"></a><a name="p1125715255316"></a>The administrator username must:</p>
    <a name="ul925811254311"></a><a name="ul925811254311"></a><ul id="ul925811254311"><li>Consist of lowercase letters, digits, or underscores.</li><li>Start with a lowercase letter or an underscore.</li><li>Contain 6 to 63 characters.</li><li>Cannot be a keyword of the DWS database. For details about the keywords of the DWS database, see section <span class="filepath" id="filepath16209193871219"><a name="filepath16209193871219"></a><a name="filepath16209193871219"></a><b>Keyword</b></span> in the <em id="i104558519297"><a name="i104558519297"></a><a name="i104558519297"></a>Data Warehouse Service Database Developer Guide</em>.</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.3 "><p id="p62610537258"><a name="p62610537258"></a><a name="p62610537258"></a>security_admin</p>
    </td>
    </tr>
    <tr id="row326125322513"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p1026853112518"><a name="p1026853112518"></a><a name="p1026853112518"></a>Password</p>
    </td>
    <td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.2 "><div class="p" id="p14892133520320"><a name="p14892133520320"></a><a name="p14892133520320"></a>The password complexity requirements are as follows:<a name="dws_01_0019_ul13418111318144"></a><a name="dws_01_0019_ul13418111318144"></a><ul id="dws_01_0019_ul13418111318144"><li>Consists of 8 to 32 characters.</li><li>Cannot be the same as the username or the username written in reverse order.</li><li>Must contain at least 3 of the following character types: uppercase letters, lowercase letters, digits, and special characters ~!@#%^&amp;*()-_=+|[{}];:,&lt;.&gt;/?</li><li>Passes the weak password check.</li></ul>
    </div>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.3 "><p id="p226753172513"><a name="p226753172513"></a><a name="p226753172513"></a>Dws_2018!</p>
    </td>
    </tr>
    <tr id="row82645310256"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p126195319254"><a name="p126195319254"></a><a name="p126195319254"></a>Confirm Password</p>
    </td>
    <td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.2 "><p id="p82612538250"><a name="p82612538250"></a><a name="p82612538250"></a>Enter the password of the security administrator again.</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.3 "><p id="p14262538253"><a name="p14262538253"></a><a name="p14262538253"></a>-</p>
    </td>
    </tr>
    <tr id="row3931218192713"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p1695718122717"><a name="p1695718122717"></a><a name="p1695718122717"></a>Audit Administrator</p>
    </td>
    <td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.2 "><p id="p138595192390"><a name="p138595192390"></a><a name="p138595192390"></a>The administrator username must:</p>
    <a name="ul615614912298"></a><a name="ul615614912298"></a><ul id="ul615614912298"><li>Consist of lowercase letters, digits, or underscores.</li><li>Start with a lowercase letter or an underscore.</li><li>Contain 6 to 63 characters.</li><li>Cannot be a keyword of the DWS database. For details about the keywords of the DWS database, see section <span class="filepath" id="dws_01_0074_filepath16209193871219"><a name="dws_01_0074_filepath16209193871219"></a><a name="dws_01_0074_filepath16209193871219"></a><b>Keyword</b></span> in the <em id="dws_01_0074_i104558519297"><a name="dws_01_0074_i104558519297"></a><a name="dws_01_0074_i104558519297"></a>Data Warehouse Service Database Developer Guide</em>.</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.3 "><p id="p159510181272"><a name="p159510181272"></a><a name="p159510181272"></a>audit_admin</p>
    </td>
    </tr>
    <tr id="row16584121102717"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p6584182110274"><a name="p6584182110274"></a><a name="p6584182110274"></a>Password</p>
    </td>
    <td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.2 "><div class="p" id="p1358411211270"><a name="p1358411211270"></a><a name="p1358411211270"></a>The password complexity requirements are as follows:<a name="dws_01_0074_dws_01_0019_ul13418111318144"></a><a name="dws_01_0074_dws_01_0019_ul13418111318144"></a><ul id="dws_01_0074_dws_01_0019_ul13418111318144"><li>Consists of 8 to 32 characters.</li><li>Cannot be the same as the username or the username written in reverse order.</li><li>Must contain at least 3 of the following character types: uppercase letters, lowercase letters, digits, and special characters ~!@#%^&amp;*()-_=+|[{}];:,&lt;.&gt;/?</li><li>Passes the weak password check.</li></ul>
    </div>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.3 "><p id="p205846217277"><a name="p205846217277"></a><a name="p205846217277"></a>Dws_2018!</p>
    </td>
    </tr>
    <tr id="row16526153272717"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p7526183215279"><a name="p7526183215279"></a><a name="p7526183215279"></a>Confirm Password</p>
    </td>
    <td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.2 "><p id="p352613262718"><a name="p352613262718"></a><a name="p352613262718"></a>Enter the password of the audit administrator again.</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.3 "><p id="p9526163215277"><a name="p9526163215277"></a><a name="p9526163215277"></a>-</p>
    </td>
    </tr>
    </tbody>
    </table>

5.  Click  **Apply**.
6.  In the displayed  **Save Configuration**  dialog box, select or deselect  **Restart the cluster**  and click  **OK**.

    -   If you select  **Restart the cluster**, the system saves the settings on the  **Security Settings**  page and restarts the cluster immediately. After the cluster is restarted, the security settings take effect immediately.
    -   If you do not select  **Restart the cluster**, the system only saves the settings on the  **Security Settings**  page. Later, you need to manually restart the cluster for the security settings to take effect.

    After the security settings are complete,  **Configuration Status**  can be one of the following on the  **Security Settings**  page:

    -   **Applying**: The system is saving the settings.
    -   **Synchronized**: The settings have been saved and taken effect.
    -   **Take effect after restart**: The settings have been saved but have not taken effect. Restart the cluster for the settings to take effect.


