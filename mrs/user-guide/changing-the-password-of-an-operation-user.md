# Changing the Password of an Operation User<a name="EN-US_TOPIC_0125376103"></a>

## Scenario<a name="s6fbdb5e15c264e738c391ae16b364829"></a>

Passwords of  **Human-machine**  system users must be regularly changed to ensure MRS cluster security. This section describes how to change your passwords on MRS Manager.

## Impact on the System<a name="s5502748e84e7460994d4e4f133786e82"></a>

If you have downloaded a user authentication file, download it again and obtain the keytab file after changing the password of the MRS cluster user.

## Prerequisites<a name="s8d0f12ccfdc24464a109bcaab3d4e44b"></a>

-   You have obtained the current password policies from the administrator.
-   You have obtained the URL to access MRS Manager from the administrator.

## Procedure<a name="s907e908244c449769e272990cc5c4c52"></a>

1.  On MRS Manager, move the mouse cursor to  ![](figures/en-us_image_0125375212.jpg)  in the upper-right corner.

    On the menu that is displayed, select  **Change Password**.

2.  Fill in  **Old Password**, **New Password**, and **Confirm Password**. Click **OK**.

    For the MRS 1.6.3 or later cluster, the password complexity requirements are as follows:

    -   The password must contain 8 to 32 characters.
    -   The password must contain at least three types of the following: lowercase letters, uppercase letters, digits, spaces, and special characters which can only be \~\`!?,.:;-\_'\(\)\{\}\[\]/<\>@\#$%^&\*+|\\=
    -   The password cannot be the same as the username or reverse username.


