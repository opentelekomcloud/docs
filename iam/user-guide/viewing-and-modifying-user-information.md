# Viewing and Modifying User Information<a name="en-us_topic_0046661675"></a>

Administrators can view and modify the basic information of a user, belonged user groups, and logs generated for the user. They can change the group of a user after the user's responsibilities change, or modify the login credentials of a user if the user's password or access key was forgotten or lost.

## Viewing User Information<a name="section36783718"></a>

In the user list, expand a user to view the detailed user information, including  **Basic Information**,  **User Groups**, and  **User Logs**.

## Modifying User Information<a name="section4671248204913"></a>

Click  **Modify**  in the  **Operation**  column of the row that contains the target user.

-   **Status**: A user is enabled by default after being created. You can change the status of a user to  **Disabled**  if you do not use it again.
-   Login authentication method
    -   **Virtual MFA**: Change the login authentication mode of a user to virtual MFA only if the user has been bound to an MFA device. After the change, the user must enter virtual MFA verification codes when logging in.
    -   **SMS**: Change the login authentication mode of a user to SMS only if the user has been bound to a mobile number. After the change, the user must enter a mobile verification code when logging in.
    -   **Email**: Change the login authentication mode of a user to SMS only if the user has been bound to an email address. After the change, the user must enter an email verification code when logging in.

-   **Email**,  **Mobile Number**, and  **Description**
-   **Virtual MFA Device**: Bind an MFA device to or unbind an MFA device from a user.
-   **User Groups**: Add a user to or remove it from target user groups.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >Enter a keyword to quickly find the target user group.  


## Setting User Credentials<a name="section17362720871"></a>

In the user list, click  **Set Credentials**  in the  **Operation**  column of the row that contains the target user to change its password or manage its access keys.

<a name="table022714719410"></a>
<table><thead align="left"><tr id="row722464717416"><th class="cellrowborder" valign="top" width="17.990000000000002%" id="mcps1.1.5.1.1"><p id="p10224194774113"><a name="p10224194774113"></a><a name="p10224194774113"></a><strong id="b84235270618341"><a name="b84235270618341"></a><a name="b84235270618341"></a>Credential Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="21.89%" id="mcps1.1.5.1.2"><p id="p5224164714415"><a name="p5224164714415"></a><a name="p5224164714415"></a><strong id="b84235270615166"><a name="b84235270615166"></a><a name="b84235270615166"></a>Generation Method</strong></p>
</th>
<th class="cellrowborder" valign="top" width="30.75%" id="mcps1.1.5.1.3"><p id="p7224154712411"><a name="p7224154712411"></a><a name="p7224154712411"></a><strong id="b14438018113629"><a name="b14438018113629"></a><a name="b14438018113629"></a>Description</strong></p>
</th>
<th class="cellrowborder" valign="top" width="29.37%" id="mcps1.1.5.1.4"><p id="p8224184754119"><a name="p8224184754119"></a><a name="p8224184754119"></a><strong id="b84235270614261"><a name="b84235270614261"></a><a name="b84235270614261"></a>Application Scenario</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1522584713416"><td class="cellrowborder" rowspan="3" valign="top" width="17.990000000000002%" headers="mcps1.1.5.1.1 "><p id="p13224194734115"><a name="p13224194734115"></a><a name="p13224194734115"></a>Password</p>
</td>
<td class="cellrowborder" valign="top" width="21.89%" headers="mcps1.1.5.1.2 "><p id="p14225247144115"><a name="p14225247144115"></a><a name="p14225247144115"></a>Using email</p>
</td>
<td class="cellrowborder" valign="top" width="30.75%" headers="mcps1.1.5.1.3 "><p id="p1522514473413"><a name="p1522514473413"></a><a name="p1522514473413"></a>The system will send you a one-time login link through email. You can click this link to log in to the management console and set the password.</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.1.5.1.4 "><p id="p17225154719413"><a name="p17225154719413"></a><a name="p17225154719413"></a>Used to reset the API passwords of users who have email addresses bound to their accounts. The user needs to use the password to log in to the management console.</p>
</td>
</tr>
<tr id="row1522534712416"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="p722513477410"><a name="p722513477410"></a><a name="p722513477410"></a>Automatically generated</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="p12225247154111"><a name="p12225247154111"></a><a name="p12225247154111"></a>The system randomly generates a 10-character API password.</p>
<div class="note" id="note10225164718417"><a name="note10225164718417"></a><a name="note10225164718417"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1622512472412"><a name="p1622512472412"></a><a name="p1622512472412"></a>Click <strong id="b842352706162536"><a name="b842352706162536"></a><a name="b842352706162536"></a>OK</strong> to download the automatically generated password file.</p>
</div></div>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="p1922518479415"><a name="p1922518479415"></a><a name="p1922518479415"></a>Used to reset the password of a user who is using a development tool (such as APIs, the CLI, and SDK) that can access the cloud system through password authentication.</p>
</td>
</tr>
<tr id="row7225847114115"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="p2225247194118"><a name="p2225247194118"></a><a name="p2225247194118"></a>Set manually</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="p222574713418"><a name="p222574713418"></a><a name="p222574713418"></a>Users set their own API passwords.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="p14225184794110"><a name="p14225184794110"></a><a name="p14225184794110"></a>Used to reset any user's password.</p>
</td>
</tr>
<tr id="row522714764114"><td class="cellrowborder" valign="top" width="17.990000000000002%" headers="mcps1.1.5.1.1 "><p id="p13226124724116"><a name="p13226124724116"></a><a name="p13226124724116"></a>Access key</p>
</td>
<td class="cellrowborder" valign="top" width="21.89%" headers="mcps1.1.5.1.2 "><p id="p3226174719417"><a name="p3226174719417"></a><a name="p3226174719417"></a>Created by a user or a security administrator</p>
</td>
<td class="cellrowborder" valign="top" width="30.75%" headers="mcps1.1.5.1.3 "><p id="p182265470415"><a name="p182265470415"></a><a name="p182265470415"></a>Users can add or delete access keys in the <strong id="b842352706162923"><a name="b842352706162923"></a><a name="b842352706162923"></a>Access Keys</strong> area.</p>
<div class="note" id="note14226847114115"><a name="note14226847114115"></a><a name="note14226847114115"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p14226114754118"><a name="p14226114754118"></a><a name="p14226114754118"></a>Each user can create a maximum of two access keys, which are valid within 360 days. To ensure account security, keep them securely.</p>
</div></div>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.1.5.1.4 "><p id="p42261547134110"><a name="p42261547134110"></a><a name="p42261547134110"></a>Users can access the cloud system by using access keys.</p>
</td>
</tr>
</tbody>
</table>

-   **Require Password Reset**: If you select  **Automatically generated**  or  **Set manually**, you can choose whether to require password reset at the next login. This function is enabled by default to ensure account security.

