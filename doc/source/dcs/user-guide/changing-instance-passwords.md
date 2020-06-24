# Changing Instance Passwords<a name="EN-US_TOPIC_0237964724"></a>

## Scenario<a name="section25182135"></a>

On the DCS console, you can change the password required for accessing your DCS instance.

## Prerequisites<a name="section25312629"></a>

The DCS instance for which you want to change the password is in the  **Running**  state.

## Procedure<a name="section26487069"></a>

1.  Log in to the management console.
2.  Click![](figures/icon-region.png)  in the upper left corner of the management console and select a region and a project.
3.  Click  **Service List**, and choose  **Database**  \>  **Distributed Cache Service**  to launch the DCS console.
4.  In the navigation pane, choose  **Cache Manager**.
5.  Choose  **More**  \>  **Change Password**  in the same row as the chosen instance.
6.  In the  **Change Password**  dialog box, enter the old password and new password.

    >![](/images/icon-note.gif) **NOTE:**   
    >After 5 consecutive incorrect password attempts, the account for accessing the chosen DCS instance will be locked for 5 minutes. Passwords cannot be changed during the lockout period.  
    >A DCS instance password cannot be left unspecified and must:  
    >-   Be different from the old password.  
    >-   Consist of 8 to 32 characters.  
    >-   Contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters \(\`\~!@\#$%^&\*\(\)-\_=+\\|\[\{\}\]:'",<.\>/?\).  

7.  In the  **Change Password**  dialog box, click  **OK**  to confirm the password change.

