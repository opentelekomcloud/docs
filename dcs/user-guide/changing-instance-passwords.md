# Changing Instance Passwords<a name="en-us_topic_0054235820"></a>

## Scenario<a name="section10189001"></a>

On the DCS console, you can change the password required for accessing your DCS instance.

## Prerequisites<a name="section24592149"></a>

The DCS instance for which you want to change the password is in the  **Running**  state.

## Procedure<a name="section20002757"></a>

1.  Log in to the management console.
2.  Click  ![](figures/project.png) in the upper left corner of the management console and select a region and a project.
3.  Click  **Service List**, and choose **Database** \> **Distributed Cache Service**  to launch the DCS console.
4.  In the navigation pane, choose  **Cache Manager**.
5.  Choose  **More** \> **Change Password**  in the same row as the chosen instance.
6.  In the  **Change Password**  dialog box, enter the old password and new password.

    >![](public_sys-resources/icon-note.gif) **NOTE:** 
    >After 5 consecutive incorrect password attempts, the account for accessing the chosen DCS instance will be locked for 5 minutes. Passwords cannot be changed during the lockout period.
    >A DCS instance password cannot be left unspecified and must:
    >-   Consist of 8 to 32 characters.
    >-   Be different from the old password.
    >-   Contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters \(\`\~!@\#$^&\*\(\)-\_=+\\|\{\}:,<.\>/?\).

7.  Click **OK**  to confirm the password change.

