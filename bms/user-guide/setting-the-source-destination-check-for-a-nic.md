# Setting the Source/Destination Check for a NIC<a name="EN-US_TOPIC_0120711878"></a>

## Procedure<a name="section115981549125114"></a>

1.  Log in to the management console.
2.  Under  **Computing**, click  **Bare Metal Server**.

    The BMS console is displayed.

3.  Click the name of the target BMS.

    The page showing details of the BMS is displayed.

4.  Select the  **NIC**  tab. On the displayed page, click the icon before the NIC to be configured.
5.  Enable or disable the source/destination check function.

    By default, the source/destination check function is enabled. When this function is enabled, the system checks whether source IP addresses contained in the packets sent by BMSs are correct. If the IP addresses are incorrect, the system does not allow the BMSs to send the packets. This mechanism prevents packet spoofing, thereby improving system security. If the BMS functions as a NAT server, router, or firewall, you must disable the source/destination check for the BMS.


