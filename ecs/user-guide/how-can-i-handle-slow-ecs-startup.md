# How Can I Handle Slow ECS Startup?<a name="EN-US_TOPIC_0117006217"></a>

If an ECS requires a long period of time to start, you can change the default timeout to speed up the startup.

1.  Log in to the ECS.
2.  Run the following command to switch to user  **root**:

    **sudo su**

3.  Run the following command to obtain the grub version:

    **rpm -qa | grep grub**

    **Figure  1**  Viewing the grub version<a name="fig165801156121217"></a>  
    ![](figures/viewing-the-grub-version.png "viewing-the-grub-version")

4.  Change the timeout in the grub file to 0s.

    -   If the grub version is earlier than 2:

        Open the  **/boot/grub/grub.cfg**  or  **/boot/grub/menu.lst**  file and change the  **timeout**  value to  **0**.

    -   If the grub version is 2:

        Open the  **/boot/grub2/grub.cfg**  file and change the  **timeout**  value to  **0**.

    **Figure  2**  Changing timeout duration<a name="fig109003411818"></a>  
    ![](figures/changing-timeout-duration.gif "changing-timeout-duration")


