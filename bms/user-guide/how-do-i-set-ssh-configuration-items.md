# How Do I Set SSH Configuration Items?<a name="EN-US_TOPIC_0096201996"></a>

You can select the BMS login mode or account type. If you have requirements for special configuration, perform the following operations:

1.  To improve security of the BMS, disable remote login using the password and retain only the certificate login mode. Configure the following parameters:
    -   Check whether the  **/etc/cloud/cloud.cfg**  file contains parameter  **ssh\_pwauth**  and its value is  **false**. If not, add the parameter or change its value to  **false**. This ensures that password cannot be used to log in to the BMS using Xshell.
    -   Check whether the value of parameter  **ChallengeResponseAuthentication**  in the  **/etc/ssh/sshd\_config**  file is  **no**. If not, change it to  **no**. This ensures that password cannot be entered using the keyboard inactive method to log in to the BMS using Xshell.

2.  To enable remote login as user  **root**  and enable SSH permissions of user  **root**, perform the following operations:

    >![](public_sys-resources/icon-notice.gif) **NOTICE:**   
    >This operation may cause risks. Exercise caution before performing this operation.  

    1.  Modify the Cloud-Init configuration file.

        Take CentOS 6.7 as an example. Modify the following parameters:

        ```
        users: 
          - name: root 
            lock_passwd: false 
        disable_root: 0 
        ssh_pwauth: 1
        ```

        In the preceding information:

        -   If the value of  **lock\_passwd**  is set to  **false**, user password is not locked.
        -   **disable\_root**  specifies whether to disable remote SSH login as user  **root**. Set the value to  **0**, indicating that the remote SSH login as user  **root**  is enabled \(In some OSs, value  **true**  indicates disabled and  **false**  indicates enabled\).
        -   **ssh\_pwauth**  specifies whether to support SSH password login. Set this parameter to  **1**, indicating that SSH password login is supported.

    2.  Run the following command to open the  **/etc/ssh/sshd\_config**  file using the vi editor:

        **vi /etc/ssh/sshd\_config**

        Change the value of  **PasswordAuthentication**  in the  **sshd\_config**  file to  **yes**.

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >-   For SUSE and openSUSE, set  **PasswordAuthentication**  and  **ChallengeResponseAuthentication**  in the  **sshd\_config**  file to  **yes**.  
        >-   For  **Ubuntu**, set  **PermitRootLogin**  to  **yes**.  

    3.  Lock the initial password of user  **root**  in the image template by modifying the  **shadow**  file to prevent risks.
        1.  Run the following command to open the  **/etc/shadow**  configuration file using the vim editor:

            **vim /etc/shadow**

            Add  **!!**  to the password hash value of the root account. The modified configuration file is as follows:

            ```
            # cat /etc/shadow | grep root 
             root:!!$6$SphQRPXu$Nvg6izXbhDPrcY3j1vRiHaQFVRpNiV3HD/bjDgnZrACOWPXwJahx78iaut1IigIUrwavVGSYQ1JOIw.rDlVh7.:17376:0:99999:7::
            ```

        2.  After the configuration file is modified, press  **Esc**  and enter  **:wq**  to save and exit the file.

            >![](public_sys-resources/icon-note.gif) **NOTE:**   
            >For Ubuntu, delete the user created during the OS installation. For example, run the  **userdel -rf ubuntu**  command to delete user  **ubuntu**  created during OS installation.  




