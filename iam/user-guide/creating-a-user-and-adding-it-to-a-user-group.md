# Creating a User and Adding It to a User Group<a name="iam_01_0031"></a>

Use a security administrator to create a user, and add the user to a user group. The user inherits all of the permissions of the user group.

## Procedure<a name="s48a5715917aa42a2ab7d938695881936"></a>

1.  Choose  **Management & Deployment**  \>  **Identity and Access Management**.
2.  In the navigation pane, choose  **Users**.
3.  On the  **Users**  page, click  **Create User**.
4.  On the  **Create User**  page, enter  **Username**.
5.  <a name="l325822f9287240eb9847d7175bcc7196"></a>Specify  **Credential Type**.

    <a name="table11941958132116"></a>
    <table><thead align="left"><tr id="row294235815211"><th class="cellrowborder" valign="top" width="17%" id="mcps1.1.3.1.1"><p id="p129420581219"><a name="p129420581219"></a><a name="p129420581219"></a><strong id="b84235270618341_1"><a name="b84235270618341_1"></a><a name="b84235270618341_1"></a>Credential Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="83%" id="mcps1.1.3.1.2"><p id="p149421658132111"><a name="p149421658132111"></a><a name="p149421658132111"></a><strong id="b84235270614261"><a name="b84235270614261"></a><a name="b84235270614261"></a>Application Scenario</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row894265815219"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.3.1.1 "><p id="p18942958122113"><a name="p18942958122113"></a><a name="p18942958122113"></a>Password</p>
    </td>
    <td class="cellrowborder" valign="top" width="83%" headers="mcps1.1.3.1.2 "><a name="ul9680404223"></a><a name="ul9680404223"></a><ul id="ul9680404223"><li>Used to log in to the management console</li><li>Used to enable development tools (such as APIs, the CLI, and SDK) that can access cloud services through password authentication</li></ul>
    </td>
    </tr>
    <tr id="row11882043225"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.3.1.1 "><p id="p71897482210"><a name="p71897482210"></a><a name="p71897482210"></a>Access key</p>
    </td>
    <td class="cellrowborder" valign="top" width="83%" headers="mcps1.1.3.1.2 "><p id="p618974192212"><a name="p618974192212"></a><a name="p618974192212"></a>Used to enable development tools (such as APIs, the CLI, and SDK) that can access cloud services through key authentication</p>
    </td>
    </tr>
    </tbody>
    </table>

6.  Select a user group which you want to add the user from the drop-down list box in the  **User Groups**  area.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   You can also enter a keyword to quickly find the target user group.  
    >-   A user can be added to multiple user groups.  

    Perform one of the following based on the credential type you selected in  [5](#l325822f9287240eb9847d7175bcc7196).

    <a name="table11413182652819"></a>
    <table><thead align="left"><tr id="row2414526172817"><th class="cellrowborder" valign="top" width="16%" id="mcps1.1.3.1.1"><p id="p16414152614281"><a name="p16414152614281"></a><a name="p16414152614281"></a><strong id="b84235270618341_3"><a name="b84235270618341_3"></a><a name="b84235270618341_3"></a>Credential Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="84%" id="mcps1.1.3.1.2"><p id="p1841442616282"><a name="p1841442616282"></a><a name="p1841442616282"></a><strong id="b842352706173910_1"><a name="b842352706173910_1"></a><a name="b842352706173910_1"></a>Follow-up Operation</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1541472672811"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.3.1.1 "><p id="p1941419268286"><a name="p1941419268286"></a><a name="p1941419268286"></a>Password</p>
    </td>
    <td class="cellrowborder" valign="top" width="84%" headers="mcps1.1.3.1.2 "><p id="p15414192617282"><a name="p15414192617282"></a><a name="p15414192617282"></a>Go to <a href="#l6ac3dbbcc63947a39b9d7a4de76d7d3b">8</a>.</p>
    </td>
    </tr>
    <tr id="row124141526132813"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.3.1.1 "><p id="p194151926102812"><a name="p194151926102812"></a><a name="p194151926102812"></a>Access key</p>
    </td>
    <td class="cellrowborder" valign="top" width="84%" headers="mcps1.1.3.1.2 "><p id="p134151826132816"><a name="p134151826132816"></a><a name="p134151826132816"></a>Click <strong id="b842352706162233_1"><a name="b842352706162233_1"></a><a name="b842352706162233_1"></a>OK</strong>. Download the generated key. User creation is complete.</p>
    <div class="note" id="note1485015253019"><a name="note1485015253019"></a><a name="note1485015253019"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p78500233013"><a name="p78500233013"></a><a name="p78500233013"></a>Access keys are credentials for identity authentication in IAM. You can only obtain an access key by downloading it. If the user needs to use an access key for authentication in IAM but it has not been downloaded, you must generate a new access key.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

7.  Click  **Next**.
8.  <a name="l6ac3dbbcc63947a39b9d7a4de76d7d3b"></a>Specify  **Password Type**.

    <a name="table41771955153717"></a>
    <table><thead align="left"><tr id="row18178115520375"><th class="cellrowborder" valign="top" width="23.11%" id="mcps1.1.4.1.1"><p id="p16178855133711"><a name="p16178855133711"></a><a name="p16178855133711"></a><strong id="b842352706183927"><a name="b842352706183927"></a><a name="b842352706183927"></a>Password Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="30.680000000000003%" id="mcps1.1.4.1.2"><p id="p817875553713"><a name="p817875553713"></a><a name="p817875553713"></a><strong id="b14438018113629"><a name="b14438018113629"></a><a name="b14438018113629"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="46.21%" id="mcps1.1.4.1.3"><p id="p1178125519371"><a name="p1178125519371"></a><a name="p1178125519371"></a><strong id="b842352706173910_3"><a name="b842352706173910_3"></a><a name="b842352706173910_3"></a>Follow-up Operation</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1178105516375"><td class="cellrowborder" valign="top" width="23.11%" headers="mcps1.1.4.1.1 "><p id="p3178195510371"><a name="p3178195510371"></a><a name="p3178195510371"></a>Set at first login</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.4.1.2 "><p id="p8178155183716"><a name="p8178155183716"></a><a name="p8178155183716"></a>The system will send you a one-time login link through email. You need to use this link to set a password before you can log in to the management console.</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.21%" headers="mcps1.1.4.1.3 "><a name="ol1645633512389"></a><a name="ol1645633512389"></a><ol id="ol1645633512389"><li>Set <strong id="b1134478122710"><a name="b1134478122710"></a><a name="b1134478122710"></a>Email</strong> for receiving the login link.</li><li>(Optional) Set <strong id="b6054922315720_1_1"><a name="b6054922315720_1_1"></a><a name="b6054922315720_1_1"></a>Mobile Number</strong>.</li></ol>
    </td>
    </tr>
    <tr id="row131781955173710"><td class="cellrowborder" valign="top" width="23.11%" headers="mcps1.1.4.1.1 "><p id="p1517805563715"><a name="p1517805563715"></a><a name="p1517805563715"></a>Automatically generated</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.4.1.2 "><p id="p9178555133719"><a name="p9178555133719"></a><a name="p9178555133719"></a>The system randomly generates a 10-character password. This option enables development tools (such as APIs, the CLI, and SDK) that can access cloud services through password authentication.</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.21%" headers="mcps1.1.4.1.3 "><a name="ol14682551123819"></a><a name="ol14682551123819"></a><ol id="ol14682551123819"><li>(Optional) Set <strong id="b6054922315720_3_1"><a name="b6054922315720_3_1"></a><a name="b6054922315720_3_1"></a>Email</strong>.</li><li>(Optional) Set <strong id="b6054922315720_1_3"><a name="b6054922315720_1_3"></a><a name="b6054922315720_1_3"></a>Mobile Number</strong>.</li></ol>
    </td>
    </tr>
    <tr id="row2017825517379"><td class="cellrowborder" valign="top" width="23.11%" headers="mcps1.1.4.1.1 "><p id="p14178195516375"><a name="p14178195516375"></a><a name="p14178195516375"></a>Set manually</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.680000000000003%" headers="mcps1.1.4.1.2 "><p id="p317810557375"><a name="p317810557375"></a><a name="p317810557375"></a>Users set their own passwords.</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.21%" headers="mcps1.1.4.1.3 "><a name="ol1910491713396"></a><a name="ol1910491713396"></a><ol id="ol1910491713396"><li>(Optional) Set <strong id="b6054922315720_3_3"><a name="b6054922315720_3_3"></a><a name="b6054922315720_3_3"></a>Email</strong>.</li><li>(Optional) Set <strong id="b6054922315720_1_5"><a name="b6054922315720_1_5"></a><a name="b6054922315720_1_5"></a>Mobile Number</strong>.</li><li>Set <strong id="b842352706222132"><a name="b842352706222132"></a><a name="b842352706222132"></a>New Password</strong> and <strong id="b842352706222134"><a name="b842352706222134"></a><a name="b842352706222134"></a>Confirm Password</strong>.<div class="note" id="note98311814124017"><a name="note98311814124017"></a><a name="note98311814124017"></a><span class="notetitle"> NOTE: </span><div class="notebody"><div class="p" id="p2833514104017"><a name="p2833514104017"></a><a name="p2833514104017"></a>The password must meet the following requirements:<a name="ul1083331413403"></a><a name="ul1083331413403"></a><ul id="ul1083331413403"><li>It must be 6 to 32 characters long.</li><li>It must contain at least two of the following character types: uppercase letters, lowercase letters, digits, and special characters (!"#$%&amp;'()*+,-./:;&lt;=&gt;?@[]^`{_|}~ and spaces).</li><li>It cannot be the username or the username spelled backwards. For example, if the username is <strong id="b842352706113947"><a name="b842352706113947"></a><a name="b842352706113947"></a>A12345</strong>, the password cannot be <strong id="b84235270611407"><a name="b84235270611407"></a><a name="b84235270611407"></a>A12345</strong>, <strong id="b842352706114013"><a name="b842352706114013"></a><a name="b842352706114013"></a>a12345</strong>, <strong id="b842352706114020"><a name="b842352706114020"></a><a name="b842352706114020"></a>54321A</strong> or <strong id="b842352706114028"><a name="b842352706114028"></a><a name="b842352706114028"></a>54321a</strong>.</li><li>It cannot contain the user's mobile number or email address.</li></ul>
    </div>
    </div></div>
    </li></ol>
    </td>
    </tr>
    </tbody>
    </table>

9.  Select  **Require Password Reset**  to ensure that users are forced to change their password the first time they log in. The  **Require Password Reset**  option is selected by default. It is recommended that you retain the default setting to ensure that your password is set by yourself, preventing password leakage.
10. Click  **OK**.

    The user is created successfully.


