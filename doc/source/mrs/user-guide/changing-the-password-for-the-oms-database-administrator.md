# Changing the Password for the OMS Database Administrator<a name="EN-US_TOPIC_0221415060"></a>

## Scenario<a name="section6298525417463"></a>

Periodically change the password for the OMS database administrator to ensure the system O&M security.

## Procedure<a name="section66822208174637"></a>

1.  Log in to the active management node.

    >![](/images/icon-note.gif) **NOTE:**   
    >The password of user  **ommdba**  cannot be changed on the standby management node; otherwise, the cluster cannot work properly. Change the password of user **ommdba**  on the active management node only.  

2.  Run the following command to switch the user:

    **sudo su - root**

    **su - omm**

3.  Run the following command to go to the related directory:

    **cd $OMS\_RUN\_PATH/tools**

4.  Run the following command to change the password for user  **ommdba**:

    **mod\_db\_passwd ommdba**

5.  Enter the old password of user  **ommdba**  and enter a new password twice. The password change takes effect on all servers.

    The password complexity requirements are as follows:

    -   The password must contain 16 to 32 characters.
    -   The password must contain at least three types of the following: lowercase letters, uppercase letters, digits, and special characters which can only be \~\`!@\#$%^&\*\(\)-+\_=\\|\[\{\}\];:",<.\>/?
    -   The password cannot be the same as the username or reverse username.
    -   The password cannot be the same as the last 20 historical passwords.

    If the following information is displayed, the password is changed successfully.

    ```
    Congratulations, update [ommdba] password successfully.
    ```


