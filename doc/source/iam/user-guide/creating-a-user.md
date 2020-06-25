# Creating a User<a name="en-us_topic_0046611303"></a>

You can create users by using the console or by calling an API, and set security credentials and permissions that allow the users to access resources under your account. The users can access the cloud system through the management console or by calling APIs.

## Procedure<a name="section4493316"></a>

1.  In the navigation pane, choose  **Users**.
2.  On the  **Users**  page, click  **Create User**.
3.  On the  **Create User**  page, enter  **Username**.
4.  <a name="li34423699191838"></a>Specify  **Credential Type**.

    <a name="td98b272b49bd4db1a588159c255cdaa5"></a>
    <table><thead align="left"><tr id="r7717a44256bf4607bd7b2c0b36dc3eef"><th class="cellrowborder" valign="top" width="17%" id="mcps1.1.3.1.1"><p id="en-us_topic_0075357586_p129420581219"><a name="en-us_topic_0075357586_p129420581219"></a><a name="en-us_topic_0075357586_p129420581219"></a><strong id="b84235270618341"><a name="b84235270618341"></a><a name="b84235270618341"></a>Credential Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="83%" id="mcps1.1.3.1.2"><p id="adbfd95bc43394042b6120f8384a3be73"><a name="adbfd95bc43394042b6120f8384a3be73"></a><a name="adbfd95bc43394042b6120f8384a3be73"></a><strong id="b84235270614261"><a name="b84235270614261"></a><a name="b84235270614261"></a>Application Scenario</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r314973e6d1244c5d9de4cd09008c76e8"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.3.1.1 "><p id="ad266b6140fe44bf2b2aa61b0c835cdd1"><a name="ad266b6140fe44bf2b2aa61b0c835cdd1"></a><a name="ad266b6140fe44bf2b2aa61b0c835cdd1"></a>Password</p>
    </td>
    <td class="cellrowborder" valign="top" width="83%" headers="mcps1.1.3.1.2 "><a name="en-us_topic_0075357586_ul9680404223"></a><a name="en-us_topic_0075357586_ul9680404223"></a><ul id="en-us_topic_0075357586_ul9680404223"><li>Used to log in to the management console</li><li>Used to enable development tools (such as APIs, the CLI, and SDK) that can access cloud services through password authentication</li></ul>
    </td>
    </tr>
    <tr id="r467f09ef88bc4fe5aac2ba79104e7238"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0075357586_p71897482210"><a name="en-us_topic_0075357586_p71897482210"></a><a name="en-us_topic_0075357586_p71897482210"></a>Access Key</p>
    </td>
    <td class="cellrowborder" valign="top" width="83%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0075357586_p618974192212"><a name="en-us_topic_0075357586_p618974192212"></a><a name="en-us_topic_0075357586_p618974192212"></a>Used to enable development tools (such as APIs, the CLI, and SDK) that can access cloud services through key authentication</p>
    </td>
    </tr>
    </tbody>
    </table>

5.  Select a user group which you want to add the user from the drop-down list box in the  **User Groups**  area.

    >![](/images/icon-note.gif) **NOTE:**   
    >-   You can also enter a keyword to quickly find the target user group.  
    >-   A user can be added to multiple user groups.  

    Perform one of the following based on the credential type you selected in  [4](#li34423699191838).

    <a name="t002a008fb3244abd8cc0ac6ab51456e5"></a>
    <table><thead align="left"><tr id="rdbaf75f2799e4ef6b9d03eac859f0831"><th class="cellrowborder" valign="top" width="16%" id="mcps1.1.3.1.1"><p id="a67a8f255288b482aa46f73c41b7b3ced"><a name="a67a8f255288b482aa46f73c41b7b3ced"></a><a name="a67a8f255288b482aa46f73c41b7b3ced"></a><strong id="b790950683"><a name="b790950683"></a><a name="b790950683"></a>Credential Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="84%" id="mcps1.1.3.1.2"><p id="af9afabffec864412bc2a65e5702e5cd7"><a name="af9afabffec864412bc2a65e5702e5cd7"></a><a name="af9afabffec864412bc2a65e5702e5cd7"></a><strong id="b842352706173910"><a name="b842352706173910"></a><a name="b842352706173910"></a>Follow-up Operation</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r8e8df4545b654261a67935ce2939dc8d"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.3.1.1 "><p id="a41e9eb5de45c4bc99cb260387bf331ce"><a name="a41e9eb5de45c4bc99cb260387bf331ce"></a><a name="a41e9eb5de45c4bc99cb260387bf331ce"></a>Password</p>
    </td>
    <td class="cellrowborder" valign="top" width="84%" headers="mcps1.1.3.1.2 "><p id="abfed9bc2ae8c4708bca176da52aec042"><a name="abfed9bc2ae8c4708bca176da52aec042"></a><a name="abfed9bc2ae8c4708bca176da52aec042"></a>Go to <a href="#li3972832419523">6</a>.</p>
    </td>
    </tr>
    <tr id="re8d39dbcd9584536819ec534cba2cb25"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.3.1.1 "><p id="ab47f7b937dc64cbc9b967aa1b1a48032"><a name="ab47f7b937dc64cbc9b967aa1b1a48032"></a><a name="ab47f7b937dc64cbc9b967aa1b1a48032"></a>Access Key</p>
    </td>
    <td class="cellrowborder" valign="top" width="84%" headers="mcps1.1.3.1.2 "><p id="a811d50246c11440a9a1f563e88eb6b73"><a name="a811d50246c11440a9a1f563e88eb6b73"></a><a name="a811d50246c11440a9a1f563e88eb6b73"></a>Click <strong id="b842352706162233_1"><a name="b842352706162233_1"></a><a name="b842352706162233_1"></a>OK</strong>. Download the generated key. User creation is complete.</p>
    <div class="note" id="n12fd1ad7f40542e2aa13a80d760fd107"><a name="n12fd1ad7f40542e2aa13a80d760fd107"></a><a name="n12fd1ad7f40542e2aa13a80d760fd107"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0075357586_p78500233013"><a name="en-us_topic_0075357586_p78500233013"></a><a name="en-us_topic_0075357586_p78500233013"></a>Access keys are credentials for identity authentication in IAM. You can only obtain an access key by downloading it. If the user needs to use an access key for authentication in IAM but it has not been downloaded, you must generate a new access key.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

6.  <a name="li3972832419523"></a>Click  **Next**.
7.  Specify  **Password Type**.

    <a name="table41771955153717"></a>
    <table><thead align="left"><tr id="r95ec921bc2264c819359f7085aca2962"><th class="cellrowborder" valign="top" width="23.11%" id="mcps1.1.4.1.1"><p id="a87f4a3d370f945889dec3fabfa91e946"><a name="a87f4a3d370f945889dec3fabfa91e946"></a><a name="a87f4a3d370f945889dec3fabfa91e946"></a><strong id="b842352706183927"><a name="b842352706183927"></a><a name="b842352706183927"></a>Password Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="30.680000000000003%" id="mcps1.1.4.1.2"><p id="en-us_topic_0075357586_p817875553713"><a name="en-us_topic_0075357586_p817875553713"></a><a name="en-us_topic_0075357586_p817875553713"></a><strong id="b14438018113629"><a name="b14438018113629"></a><a name="b14438018113629"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="46.21%" id="mcps1.1.4.1.3"><p id="a3c0d2c149cb54f4783986dfcc2e0ce6b"><a name="a3c0d2c149cb54f4783986dfcc2e0ce6b"></a><a name="a3c0d2c149cb54f4783986dfcc2e0ce6b"></a><strong id="b842352706173910_1"><a name="b842352706173910_1"></a><a name="b842352706173910_1"></a>Follow-up Operation</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r00d0b5789a23428d805f49e7f6921d53"><td class="cellrowborder" valign="top" width="23.11%" headers="mcps1.1.4.1.1 "><p id="afefba4c8d2ab46d8808e23b57fcd3871"><a name="afefba4c8d2ab46d8808e23b57fcd3871"></a><a name="afefba4c8d2ab46d8808e23b57fcd3871"></a>Set at first login</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.4.1.2 "><p id="a42fe316a2d7f4c6b8125ea8266af121d"><a name="a42fe316a2d7f4c6b8125ea8266af121d"></a><a name="a42fe316a2d7f4c6b8125ea8266af121d"></a>The system will send you a one-time login link through email. You need to use this link to set a password before you can log in to the management console.</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.21%" headers="mcps1.1.4.1.3 "><a name="oa5e508c6d289487996e9e50eafa92ac4"></a><a name="oa5e508c6d289487996e9e50eafa92ac4"></a><ol id="oa5e508c6d289487996e9e50eafa92ac4"><li>Set <strong id="b1951543216274"><a name="b1951543216274"></a><a name="b1951543216274"></a>Email</strong> for receiving the login link.</li><li>(Optional) Set <strong id="b6054922315720_1"><a name="b6054922315720_1"></a><a name="b6054922315720_1"></a>Mobile Number</strong>.</li><li>Click <span class="uicontrol" id="uicontrol196331156152319"><a name="uicontrol196331156152319"></a><a name="uicontrol196331156152319"></a><b>OK</b></span>.</li></ol>
    </td>
    </tr>
    <tr id="r3952b78c8d63445d806d65977d171578"><td class="cellrowborder" valign="top" width="23.11%" headers="mcps1.1.4.1.1 "><p id="aacba1eb6a43a488ca8137acdb687e244"><a name="aacba1eb6a43a488ca8137acdb687e244"></a><a name="aacba1eb6a43a488ca8137acdb687e244"></a>Automatically generated</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.4.1.2 "><p id="a280ddfe669a64dbdad38f1708d83bbec"><a name="a280ddfe669a64dbdad38f1708d83bbec"></a><a name="a280ddfe669a64dbdad38f1708d83bbec"></a>The system randomly generates a 10-character password. This option enables development tools (such as APIs, the CLI, and SDK) that can access cloud services through password authentication.</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.21%" headers="mcps1.1.4.1.3 "><a name="ofcf4d47e12fa47c5bebe105ba38916ad"></a><a name="ofcf4d47e12fa47c5bebe105ba38916ad"></a><ol id="ofcf4d47e12fa47c5bebe105ba38916ad"><li>(Optional) Set <strong id="b6054922315720_3"><a name="b6054922315720_3"></a><a name="b6054922315720_3"></a>Email</strong>.</li><li>(Optional) Set <strong id="b948629141"><a name="b948629141"></a><a name="b948629141"></a>Mobile Number</strong>.</li><li>Click <span class="uicontrol" id="uicontrol4803122018241"><a name="uicontrol4803122018241"></a><a name="uicontrol4803122018241"></a><b>OK</b></span>.</li><li>Download the password file.</li></ol>
    </td>
    </tr>
    <tr id="r55ec8743987c4776a12332c8f461a080"><td class="cellrowborder" valign="top" width="23.11%" headers="mcps1.1.4.1.1 "><p id="adcfeb2293dd54c60a080796044d4cf49"><a name="adcfeb2293dd54c60a080796044d4cf49"></a><a name="adcfeb2293dd54c60a080796044d4cf49"></a>Set manually</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0075357586_p317810557375"><a name="en-us_topic_0075357586_p317810557375"></a><a name="en-us_topic_0075357586_p317810557375"></a>Users set their own passwords.</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.21%" headers="mcps1.1.4.1.3 "><a name="oa0341cb6937247769b46169b089e354e"></a><a name="oa0341cb6937247769b46169b089e354e"></a><ol id="oa0341cb6937247769b46169b089e354e"><li>(Optional) Set <strong id="b956866590"><a name="b956866590"></a><a name="b956866590"></a>Email</strong>.</li><li>(Optional) Set <strong id="b295651306"><a name="b295651306"></a><a name="b295651306"></a>Mobile Number</strong>.</li><li>Set <strong id="b842352706222132"><a name="b842352706222132"></a><a name="b842352706222132"></a>New Password</strong> and <strong id="b842352706222134"><a name="b842352706222134"></a><a name="b842352706222134"></a>Confirm Password</strong>.<div class="note" id="n7f8fa3a12c3344659022c6193ae3b008"><a name="n7f8fa3a12c3344659022c6193ae3b008"></a><a name="n7f8fa3a12c3344659022c6193ae3b008"></a><span class="notetitle"> NOTE: </span><div class="notebody"><div class="p" id="aaf4b22233e2745009fc7b1515f136ee3"><a name="aaf4b22233e2745009fc7b1515f136ee3"></a><a name="aaf4b22233e2745009fc7b1515f136ee3"></a>The password must meet the following requirements:<a name="u4d2703e3722d4f56ac1e0e60d83f4a42"></a><a name="u4d2703e3722d4f56ac1e0e60d83f4a42"></a><ul id="u4d2703e3722d4f56ac1e0e60d83f4a42"><li>It must be 6 to 32 characters long.</li><li>It must contain at least two of the following character types: uppercase letters, lowercase letters, digits, and special characters (!"#$%&amp;'()*+,-./:;&lt;=&gt;?@[]^`{_|}~ and spaces).</li><li>It cannot be the username or the username spelled backwards. For example, if the username is <strong id="b842352706113947"><a name="b842352706113947"></a><a name="b842352706113947"></a>A12345</strong>, the password cannot be <strong id="b84235270611407"><a name="b84235270611407"></a><a name="b84235270611407"></a>A12345</strong>, <strong id="b842352706114013"><a name="b842352706114013"></a><a name="b842352706114013"></a>a12345</strong>, <strong id="b842352706114020"><a name="b842352706114020"></a><a name="b842352706114020"></a>54321A</strong> or <strong id="b842352706114028"><a name="b842352706114028"></a><a name="b842352706114028"></a>54321a</strong>.</li><li>It cannot contain the user's mobile number or email address.</li></ul>
    </div>
    </div></div>
    </li><li>Click <span class="uicontrol" id="uicontrol14498122672419"><a name="uicontrol14498122672419"></a><a name="uicontrol14498122672419"></a><b>OK</b></span>.</li></ol>
    </td>
    </tr>
    </tbody>
    </table>

    >![](/images/icon-note.gif) **NOTE:**   
    >-   The SMS-based login verification function can be enabled only when a user is bound with an email address and a mobile number.  
    >-   You can log in to the system with your username, mobile number, or email address.  
    >-   If you forget your password, you can reset it using the email address or mobile number that was bound to your account.  

8.  If you select  **Automatically generated**  or  **Set manually**, choose whether to require password reset at the next login. This function is enabled by default to ensure account security.
9.  Click  **OK**.

    The user is created successfully.


## Related Operations<a name="section5017677711856"></a>

-   View and modify information about the user, including the user status, bound email address, bound mobile number, user group, and logs.
-   Delete a user. In the user list, click  **Delete**  in the row that contains the target user.

