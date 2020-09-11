# How Can I Activate a Windows BMS?<a name="EN-US_TOPIC_0093431546"></a>

Perform the following operations to manually activate a Windows BMS:

1.  Log in to the Windows BMS.
2.  Click  ![](figures/81-13.png)  in the lower left corner and choose  **Windows PowerShell**.
3.  Run the following command to configure the IP address of the KMS server:

    **slmgr -skms 100.125.4.21**

4.  Run the following command to check whether the BMS has been activated:

    **slmgr -ato**

    If error 0xC004F074 occurs, the BMS cannot be activated. In such an event, go to  [5](#li58311247179).

5.  <a name="li58311247179"></a>Verify that the time in the BMS is the same as the standard time. If the time is significantly different, the BMS cannot be activated.
6.  Run the following command on the BMS to check whether the link between the BMS and the KMS server port is reachable:

    **telnet 100.125.4.21 1688**

    If the link is unreachable, port 1688 is not enabled on the BMS firewall. You must disable the firewall or enable port 1688 on the firewall. If the BMS has any security software such as safedog, stop using it.

7.  Run the following command to check whether the BMS has been activated:

    **slmgr -ato**


