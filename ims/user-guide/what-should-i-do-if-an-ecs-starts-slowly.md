# What Should I Do If an ECS Starts Slowly?<a name="EN-US_TOPIC_0117142739"></a>

## Symptom<a name="section1972220920140"></a>

If an ECS starts slowly, you can change the default timeout duration to speed up the startup.

## Solution<a name="section418210278148"></a>

1.  Log in to the ECS.
2.  Run the following command to switch to user  **root**:

    **sudo su**

3.  Run the following command to query the version of the GRUB file:

    **rpm -qa | grep grub**

    **Figure  1**  Querying the GRUB file version<a name="fig13368111814580"></a>  
    ![](figures/querying-the-grub-file-version.jpg "querying-the-grub-file-version")

4.  Set  **timeout**  in the GRUB file to  **0**.
    -   If the GRUB file version is earlier than 2:

        Open  **/boot/grub/grub.cfg**  or  **/boot/grub/menu.lst**  and set  **timeout**  to  **0**.

    -   If the GRUB file version is 2:

        Open  **/boot/grub2/grub.cfg**  and set the value of  **timeout**  to  **0**.

        **Figure  2**  Modifying the timeout duration<a name="fig6468173217348"></a>  
        ![](figures/modifying-the-timeout-duration.jpg "modifying-the-timeout-duration")



