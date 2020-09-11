# Authorizing Folder Access Permissions to Anonymous Users<a name="obs_03_0096"></a>

If all objects in a folder need to be accessible to anonymous users, you can configure a bucket policy or an object policy to grant anonymous users the permission to access the folder. In this example, a bucket policy is used. If you want to use an object policy to authorize the permission, select the target folder and configure the object policy directly. Parameters are the same as those in the bucket policy.

## Procedure<a name="section17557163019204"></a>

1.  In the bucket list, click the bucket to be operated. The  **Overview**  page of the bucket is displayed.
2.  In the navigation pane on the left, click  **Permissions**  to go to the permission management page.
3.  Choose  **Bucket Policies**  \>  **Custom Bucket Policies**.
4.  Click  **Create Bucket Policy**. The  **Create Bucket Policy**  dialog box is displayed.
5.  Configure parameters according to the following table, so that you can grant anonymous users the permission to access the folder and objects in it:

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
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p55421614212"><a name="p55421614212"></a><a name="p55421614212"></a><strong id="b199557458122"><a name="b199557458122"></a><a name="b199557458122"></a>Customized</strong></p>
    </td>
    </tr>
    <tr id="row16532753114417"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p353219537448"><a name="p353219537448"></a><a name="p353219537448"></a>Effect</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p26391018182813"><a name="p26391018182813"></a><a name="p26391018182813"></a><strong id="b39263566122"><a name="b39263566122"></a><a name="b39263566122"></a>Allow</strong></p>
    </td>
    </tr>
    <tr id="row115321753164415"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p1553215538449"><a name="p1553215538449"></a><a name="p1553215538449"></a>Principal</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><a name="ul1133312113418"></a><a name="ul1133312113418"></a><ul id="ul1133312113418"><li><strong id="b16596155891220"><a name="b16596155891220"></a><a name="b16596155891220"></a>Include</strong></li><li>Select <strong id="b1374419592122"><a name="b1374419592122"></a><a name="b1374419592122"></a>Other account</strong>, and enter an asterisk (*) as the account ID, indicating all anonymous users.</li></ul>
    </td>
    </tr>
    <tr id="row653285374414"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p753212538444"><a name="p753212538444"></a><a name="p753212538444"></a>Resources</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><a name="ul12411915123314"></a><a name="ul12411915123314"></a><ul id="ul12411915123314"><li><strong id="b977832111316"><a name="b977832111316"></a><a name="b977832111316"></a>Include</strong></li><li>Set this parameter to all objects in the selected folder. If the folder name is <strong id="b1597164181314"><a name="b1597164181314"></a><a name="b1597164181314"></a>folder-001</strong>, enter the value <strong id="b10981245131"><a name="b10981245131"></a><a name="b10981245131"></a>folder-001/*</strong>.</li></ul>
    </td>
    </tr>
    <tr id="row18790945165418"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p12791194519544"><a name="p12791194519544"></a><a name="p12791194519544"></a>Actions</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><a name="ul1691025316358"></a><a name="ul1691025316358"></a><ul id="ul1691025316358"><li><strong id="b18301420171317"><a name="b18301420171317"></a><a name="b18301420171317"></a>Include</strong></li><li>GetObject</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

6.  Click  **OK**.

## Verification<a name="section1285315186104"></a>

1.  After the permission is successfully configured, select an object in the folder and click the object name to view its details. The object link \(URL\) is displayed on the details page. Share the URL over the Internet, so that all users can access or download the object through the Internet.
2.  An anonymous user can view the object by copying the URL of the object to the web browser.

