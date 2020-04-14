# Bucket Owner Authorizing Bucket Permissions to Other Accounts<a name="obs_03_0081"></a>

The bucket owner can authorize bucket permissions to another account or IAM users in that account.

In the following example, the account authorizes another account with the permission to access the bucket and upload objects to the bucket.

## Procedure<a name="section435994418812"></a>

1.  In the bucket list, click the bucket to be operated. The  **Summary**  page of the bucket is displayed.
2.  In the navigation pane on the left, click  **Permissions**  to go to the permission management page.
3.  Choose  **Bucket Policies**  \>  **Custom Bucket Policies**.
4.  Click  **Create Bucket Policy**. The  **Create Bucket Policy**  dialog box is displayed.
5.  Set the following parameters to authorize another account with the permission to access the bucket:

    **Table  1**  Parameters for authorizing the permission to access a specified bucket

    <a name="table7531653104420"></a>
    <table><thead align="left"><tr id="row2532105311447"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p16532195364414"><a name="p16532195364414"></a><a name="p16532195364414"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p15532145310443"><a name="p15532145310443"></a><a name="p15532145310443"></a>Value</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row953216536449"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p1653265344417"><a name="p1653265344417"></a><a name="p1653265344417"></a>Policy Mode</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p95328538440"><a name="p95328538440"></a><a name="p95328538440"></a><strong id="b173011935194310"><a name="b173011935194310"></a><a name="b173011935194310"></a>Customized</strong></p>
    </td>
    </tr>
    <tr id="row16532753114417"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p353219537448"><a name="p353219537448"></a><a name="p353219537448"></a>Effect</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p5532353104418"><a name="p5532353104418"></a><a name="p5532353104418"></a><strong id="b19922174264316"><a name="b19922174264316"></a><a name="b19922174264316"></a>Allow</strong></p>
    </td>
    </tr>
    <tr id="row115321753164415"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p1553215538449"><a name="p1553215538449"></a><a name="p1553215538449"></a>Principal</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><a name="ul136938242519"></a><a name="ul136938242519"></a><ul id="ul136938242519"><li><strong id="b187704534318"><a name="b187704534318"></a><a name="b187704534318"></a>Include</strong></li><li><strong id="b158058444417"><a name="b158058444417"></a><a name="b158058444417"></a>Cloud service user</strong>. Select <strong id="b132601515104417"><a name="b132601515104417"></a><a name="b132601515104417"></a>Other account</strong>, and enter the account ID and user ID.<p id="p75419201471"><a name="p75419201471"></a><a name="p75419201471"></a>For <strong id="b12590151316220"><a name="b12590151316220"></a><a name="b12590151316220"></a>Account ID</strong>, enter the <strong id="b112021124529"><a name="b112021124529"></a><a name="b112021124529"></a>Domain ID</strong> that can be found on the <strong id="b145225442027"><a name="b145225442027"></a><a name="b145225442027"></a>My Credential</strong> page.</p>
    </li></ul>
    </td>
    </tr>
    <tr id="row653285374414"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p753212538444"><a name="p753212538444"></a><a name="p753212538444"></a>Resources</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><a name="ul964933612542"></a><a name="ul964933612542"></a><ul id="ul964933612542"><li><strong id="b1366645434417"><a name="b1366645434417"></a><a name="b1366645434417"></a>Include</strong></li><li>Leave it blank.</li></ul>
    </td>
    </tr>
    <tr id="row18790945165418"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p12791194519544"><a name="p12791194519544"></a><a name="p12791194519544"></a>Actions</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><a name="ul815102155519"></a><a name="ul815102155519"></a><ul id="ul815102155519"><li><strong id="b9707759204411"><a name="b9707759204411"></a><a name="b9707759204411"></a>Include</strong></li><li>ListBucket</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

6.  Click  **OK**.
7.  Click  **Create Bucket Policy**. The  **Create Bucket Policy**  dialog box is displayed.
8.  Set the following parameters to authorize another account with the permission to upload objects:

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >Before authorizing the user with the permission to operate objects, ensure that the user has the permission to access the bucket.  

    **Table  2**  Parameters for authorizing the permission to upload objects

    <a name="table566311261565"></a>
    <table><thead align="left"><tr id="row16664826175610"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p1466442615612"><a name="p1466442615612"></a><a name="p1466442615612"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p1466516269566"><a name="p1466516269566"></a><a name="p1466516269566"></a>Value</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row12665142619562"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p36664266562"><a name="p36664266562"></a><a name="p36664266562"></a>Policy Mode</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p14666152615562"><a name="p14666152615562"></a><a name="p14666152615562"></a><strong id="b16452350144517"><a name="b16452350144517"></a><a name="b16452350144517"></a>Customized</strong></p>
    </td>
    </tr>
    <tr id="row3667132613567"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p1866732655612"><a name="p1866732655612"></a><a name="p1866732655612"></a>Effect</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p966982619569"><a name="p966982619569"></a><a name="p966982619569"></a><strong id="b34165604519"><a name="b34165604519"></a><a name="b34165604519"></a>Allow</strong></p>
    </td>
    </tr>
    <tr id="row666915260561"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p8670112635619"><a name="p8670112635619"></a><a name="p8670112635619"></a>Principal</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><a name="ul1670726135620"></a><a name="ul1670726135620"></a><ul id="ul1670726135620"><li><strong id="b67530576453"><a name="b67530576453"></a><a name="b67530576453"></a>Include</strong></li><li><strong id="b4659916460"><a name="b4659916460"></a><a name="b4659916460"></a>Cloud service user</strong>. Select <strong id="b176616114616"><a name="b176616114616"></a><a name="b176616114616"></a>Other account</strong>, and enter the account ID and user ID.<p id="p12751112924814"><a name="p12751112924814"></a><a name="p12751112924814"></a>For <strong id="b163385912319"><a name="b163385912319"></a><a name="b163385912319"></a>Account ID</strong>, enter the <strong id="b0339491037"><a name="b0339491037"></a><a name="b0339491037"></a>Domain ID</strong> that can be found on the <strong id="b163391491434"><a name="b163391491434"></a><a name="b163391491434"></a>My Credential</strong> page.</p>
    </li></ul>
    </td>
    </tr>
    <tr id="row126721226135618"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p0673122685615"><a name="p0673122685615"></a><a name="p0673122685615"></a>Resources</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><a name="ul11674152619564"></a><a name="ul11674152619564"></a><ul id="ul11674152619564"><li><strong id="b929562318466"><a name="b929562318466"></a><a name="b929562318466"></a>Include</strong></li><li>Resource name: <strong id="b925182454617"><a name="b925182454617"></a><a name="b925182454617"></a>*</strong></li></ul>
    </td>
    </tr>
    <tr id="row167522618569"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p1367692611568"><a name="p1367692611568"></a><a name="p1367692611568"></a>Actions</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><a name="ul176761226135619"></a><a name="ul176761226135619"></a><ul id="ul176761226135619"><li><strong id="b517511270469"><a name="b517511270469"></a><a name="b517511270469"></a>Include</strong></li><li>PutObject</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

9.  Click  **OK**.

