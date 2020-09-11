# Changing the Login Password on an ECS<a name="EN-US_TOPIC_0122627689"></a>

## Scenarios<a name="section11722115773514"></a>

This section describes how to change the password for logging in to an ECS when the password is about to expire, the password is forgotten, or you log in to the ECS for the first time. You are advised to change the initial password upon the first login.

## Prerequisites<a name="section3844435019"></a>

The ECS can be logged in.

## Background<a name="section8845441181739"></a>

[Table 1](#en-us_topic_0021426802_table4381109318958)  shows the ECS password complexity requirements.

**Table  1**  Password complexity requirements

<a name="en-us_topic_0021426802_table4381109318958"></a>
<table><thead align="left"><tr id="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_row925712618958"><th class="cellrowborder" valign="top" width="18.000000000000004%" id="mcps1.2.4.1.1"><p id="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p1162970218958"><a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p1162970218958"></a><a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p1162970218958"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="58.910000000000004%" id="mcps1.2.4.1.2"><p id="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p248177818958"><a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p248177818958"></a><a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p248177818958"></a>Requirement</p>
</th>
<th class="cellrowborder" valign="top" width="23.090000000000003%" id="mcps1.2.4.1.3"><p id="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p6680635518958"><a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p6680635518958"></a><a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p6680635518958"></a>Example Value</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_row4260571318958"><td class="cellrowborder" valign="top" width="18.000000000000004%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p2851073918958"><a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p2851073918958"></a><a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p2851073918958"></a>Password</p>
</td>
<td class="cellrowborder" valign="top" width="58.910000000000004%" headers="mcps1.2.4.1.2 "><a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_ul5961106018958"></a><a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_ul5961106018958"></a><ul id="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_ul5961106018958"><li>Consists of 8 characters to 26 characters.</li><li>Contains at least three of the following character types:<a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_ul24583583181022"></a><a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_ul24583583181022"></a><ul id="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_ul24583583181022"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters: $!@%-_=+[]:./^,{}?</li></ul>
</li><li>Cannot contain the username or the username spelled backwards.</li><li>Cannot contain more than two characters in the same sequence as they appear in the username. (This requirement applies only to Windows ECSs.)</li></ul>
</td>
<td class="cellrowborder" valign="top" width="23.090000000000003%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p6481855218958"><a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p6481855218958"></a><a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p6481855218958"></a>YNbUwp!dUc9MClnv</p>
<div class="note" id="en-us_topic_0035643949_note18511011891"><a name="en-us_topic_0035643949_note18511011891"></a><a name="en-us_topic_0035643949_note18511011891"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0035643949_p351011796"><a name="en-us_topic_0035643949_p351011796"></a><a name="en-us_topic_0035643949_p351011796"></a>The example password is generated randomly. Do not copy this example password.</p>
</div></div>
</td>
</tr>
</tbody>
</table>

## Windows<a name="section5482101418386"></a>

1.  Log in to the ECS.

    For details, see  [Login Overview](login-overview-(windows).md).

2.  Press  **Win+R**  to start the  **Run**  dialog box.
3.  Enter  **cmd**  to open the command-line interface \(CLI\) window.
4.  Run the following command to change the password \(the new password must meet the requirements described in  [Table 1](#en-us_topic_0021426802_table4381109318958)\):

    **net user Administrator **_New password_


## Linux<a name="section114862031133811"></a>

1.  Use the existing key file to log in to the Linux ECS as user  **root**  through SSH.

    For details, see  [Login Using an SSH Key](login-using-an-ssh-key.md).

2.  Run the following command to reset the password of user  **root**:

    **passwd**

    To reset the passwords of other users, replace  **passwd**  with  **passwd username**.

3.  Enter the new password as prompted. Ensure that the new password meets the requirements described in  [Table 1](#en-us_topic_0021426802_table4381109318958).

    ```
    New password:
    Retype new password:
    ```

    If the following information is displayed, the password has been changed:

    ```
    passwd: password updated successfully
    ```


