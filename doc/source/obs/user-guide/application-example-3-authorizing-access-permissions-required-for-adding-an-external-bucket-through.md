# Application Example 3: Authorizing Access Permissions Required for Adding an External Bucket Through the Custom Bucket Policy<a name="obs_03_0136"></a>

A custom bucket policy can be used to grant the read and write access permissions to the bucket to be added.

If a custom bucket policy is used to authorize such permissions, the ListBucket, GetObject, and GetObjectVersion actions must be allowed. More actions can be allowed according to your actual needs.

## Procedure<a name="section9799102151917"></a>

1.  Log in to OBS Console.
2.  In the bucket list, click the bucket to be operated. The  **Overview**  page of the bucket is displayed.
3.  In the navigation pane on the left, click  **Permissions**  to go to the permission management page.
4.  In the  **Custom Bucket Policies**  area, click  **Create Bucket Policy**. The  **Create Bucket Policy**  dialog box is displayed.
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
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p95328538440"><a name="p95328538440"></a><a name="p95328538440"></a><strong id="b17344193373816"><a name="b17344193373816"></a><a name="b17344193373816"></a>Customized</strong></p>
    </td>
    </tr>
    <tr id="row16532753114417"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p353219537448"><a name="p353219537448"></a><a name="p353219537448"></a>Effect</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p5532353104418"><a name="p5532353104418"></a><a name="p5532353104418"></a><strong id="b1090113873816"><a name="b1090113873816"></a><a name="b1090113873816"></a>Allow</strong></p>
    </td>
    </tr>
    <tr id="row115321753164415"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p1553215538449"><a name="p1553215538449"></a><a name="p1553215538449"></a>Principal</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><a name="ul136938242519"></a><a name="ul136938242519"></a><ul id="ul136938242519"><li><strong id="b1934204183815"><a name="b1934204183815"></a><a name="b1934204183815"></a>Include</strong></li><li><strong id="b19986319396"><a name="b19986319396"></a><a name="b19986319396"></a>Other account</strong>: Enter the account ID. If you want to authorize the permissions all users, enter <strong id="b1970148163912"><a name="b1970148163912"></a><a name="b1970148163912"></a>*</strong>.</li></ul>
    <div class="note" id="note169743620209"><a name="note169743620209"></a><a name="note169743620209"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p19869727155311"><a name="p19869727155311"></a><a name="p19869727155311"></a>The account ID and user ID can be obtained on the <strong id="b5198195019394"><a name="b5198195019394"></a><a name="b5198195019394"></a>My Credentials</strong> page of the account or user to be authorized. <strong id="b620481417612"><a name="b620481417612"></a><a name="b620481417612"></a>Account ID</strong> corresponds to <strong id="b54734251867"><a name="b54734251867"></a><a name="b54734251867"></a>Domain ID</strong> on the <strong id="b1295920427618"><a name="b1295920427618"></a><a name="b1295920427618"></a>My Credential</strong> page. If you authorize the permission to only an account, you do not need to enter user IDs. If you want to authorize the permission to an IAM user, you need to enter the account ID and user ID. You can authorize the permission to multiple IAM users. Use commas (,) to separate the user IDs.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row653285374414"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p753212538444"><a name="p753212538444"></a><a name="p753212538444"></a>Resources</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><a name="ul964933612542"></a><a name="ul964933612542"></a><ul id="ul964933612542"><li><strong id="b9263916406"><a name="b9263916406"></a><a name="b9263916406"></a>Include</strong></li><li>Leave it blank.</li></ul>
    </td>
    </tr>
    <tr id="row18790945165418"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p12791194519544"><a name="p12791194519544"></a><a name="p12791194519544"></a>Actions</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><a name="ul815102155519"></a><a name="ul815102155519"></a><ul id="ul815102155519"><li><strong id="b14869544017"><a name="b14869544017"></a><a name="b14869544017"></a>Include</strong></li><li>ListBucket</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

6.  Click  **OK**.
7.  Create another bucket policy and set the parameters according to the following table to grant the authorized account with access permissions to resources in the bucket.

    **Table  2**  Parameters for authorizing the permission to access a specified bucket

    <a name="table1411420256485"></a>
    <table><thead align="left"><tr id="row15115925144815"><th class="cellrowborder" valign="top" width="27.47%" id="mcps1.2.3.1.1"><p id="p12115172524813"><a name="p12115172524813"></a><a name="p12115172524813"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="72.53%" id="mcps1.2.3.1.2"><p id="p16115132554817"><a name="p16115132554817"></a><a name="p16115132554817"></a>Value</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row811513258484"><td class="cellrowborder" valign="top" width="27.47%" headers="mcps1.2.3.1.1 "><p id="p9115142594814"><a name="p9115142594814"></a><a name="p9115142594814"></a>Policy Mode</p>
    </td>
    <td class="cellrowborder" valign="top" width="72.53%" headers="mcps1.2.3.1.2 "><p id="p1611542518488"><a name="p1611542518488"></a><a name="p1611542518488"></a><strong id="b696771877"><a name="b696771877"></a><a name="b696771877"></a>Customized</strong></p>
    </td>
    </tr>
    <tr id="row1711512514810"><td class="cellrowborder" valign="top" width="27.47%" headers="mcps1.2.3.1.1 "><p id="p511511252487"><a name="p511511252487"></a><a name="p511511252487"></a>Effect</p>
    </td>
    <td class="cellrowborder" valign="top" width="72.53%" headers="mcps1.2.3.1.2 "><p id="p711532510482"><a name="p711532510482"></a><a name="p711532510482"></a><strong id="b295478701"><a name="b295478701"></a><a name="b295478701"></a>Allow</strong></p>
    </td>
    </tr>
    <tr id="row1115122518484"><td class="cellrowborder" valign="top" width="27.47%" headers="mcps1.2.3.1.1 "><p id="p1011552504817"><a name="p1011552504817"></a><a name="p1011552504817"></a><strong id="b7578192115249"><a name="b7578192115249"></a><a name="b7578192115249"></a>Principal</strong></p>
    </td>
    <td class="cellrowborder" valign="top" width="72.53%" headers="mcps1.2.3.1.2 "><p id="p15548111217516"><a name="p15548111217516"></a><a name="p15548111217516"></a>Keep the value consistent with the preceding policy.</p>
    </td>
    </tr>
    <tr id="row1811522524818"><td class="cellrowborder" valign="top" width="27.47%" headers="mcps1.2.3.1.1 "><p id="p31151725114811"><a name="p31151725114811"></a><a name="p31151725114811"></a><strong id="b9181154132420"><a name="b9181154132420"></a><a name="b9181154132420"></a>Resources</strong></p>
    </td>
    <td class="cellrowborder" valign="top" width="72.53%" headers="mcps1.2.3.1.2 "><a name="ul71161425124816"></a><a name="ul71161425124816"></a><ul id="ul71161425124816"><li><strong id="b2059891046"><a name="b2059891046"></a><a name="b2059891046"></a>Include</strong></li><li>Resource name: <strong id="b1360682014254"><a name="b1360682014254"></a><a name="b1360682014254"></a>*</strong></li></ul>
    </td>
    </tr>
    <tr id="row1111672520488"><td class="cellrowborder" valign="top" width="27.47%" headers="mcps1.2.3.1.1 "><p id="p1411622544813"><a name="p1411622544813"></a><a name="p1411622544813"></a><strong id="b13145211172519"><a name="b13145211172519"></a><a name="b13145211172519"></a>Actions</strong></p>
    </td>
    <td class="cellrowborder" valign="top" width="72.53%" headers="mcps1.2.3.1.2 "><a name="ul16116225174814"></a><a name="ul16116225174814"></a><ul id="ul16116225174814"><li><strong id="b2050635767"><a name="b2050635767"></a><a name="b2050635767"></a>Include</strong></li><li>GetObject</li><li>GetObjectVersion</li><li>PutObject</li><li>DeleteObject</li><li>DeleteObjectVersion</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

8.  Click  **OK**.

## Verification<a name="section88013218195"></a>

1.  Log in to OBS Browser.
2.  Click  **Add Bucket**  on the upper left corner of the page. The  **Add Bucket**  dialog box is displayed.
3.  Select  **Add external bucket**  and enter the bucket name.
4.  Click  **OK**. The external bucket is added successfully.
5.  Click the newly added external bucket to open the bucket.
6.  Click  **Upload Object**, and objects can be successfully uploaded to the bucket.
7.  Select an object in the bucket and click  **Delete**. The object can be deleted successfully.

