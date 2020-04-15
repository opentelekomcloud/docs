# Having an ECS Without a Public IP Address Access the Internet<a name="EN-US_TOPIC_0027157850"></a>

## Scenarios<a name="section6427533194453"></a>

To ensure platform security and conserve public IP address resources, public IP addresses are assigned only to specified ECSs. ECSs without public IP addresses cannot access the Internet directly. If these ECSs need to access the Internet \(for example, to perform a software upgrade or install a patch\), you can select an ECS with a public IP address bound to function as a proxy ECS, providing an access channel for these ECS.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>NAT Gateway is recommended, which provides both the SNAT and DNAT functions for your ECSs in a VPC and allows the ECSs to access or provide services accessible from the Internet.   

## Prerequisites<a name="section2608915610029"></a>

-   A proxy ECS with a public IP address bound is available.

    In this example, the proxy ECS runs CentOS 6.5.

-   The IP address of the proxy ECS is in the same network segment and same security group as the ECSs that need to access the Internet.

## Procedure<a name="section6907807103042"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region-0.png)  in the upper left corner and select the desired region and project.
3.  Under  **Computing**, click  **Elastic Cloud Server**.
4.  In the search box above the upper right corner of the ECS list, enter the proxy ECS name for search.
5.  Click the name of the proxy ECS. The page providing details about the ECS is displayed.
6.  Click the  **NICs**  tab and then  ![](figures/icon-unfold.png). Then, disable  **Source/Destination Check**.

    By default, the source/destination check function is enabled. When this function is enabled, the system checks whether source IP addresses contained in the packets sent by ECSs are correct. If the IP addresses are incorrect, the system does not allow the ECSs to send the packets. This mechanism prevents packet spoofing, thereby improving system security. However, this mechanism prevents the packet sender from receiving returned packets. Therefore, disable the source/destination check.

7.  Log in to the proxy ECS.

    For more details, see  [Login Overview](login-overview-(linux).md).

8.  Run the following command to check whether the proxy ECS can access the Internet:

    **ping www.google.com**

    The proxy ECS can access the Internet if information similar to the following is displayed:

    ```
    64 bytes from 220.181.111.148: icmp_seq=1 ttl=51 time=9.34 ms
    64 bytes from 220.181.111.148: icmp_seq=2 ttl=51 time=9.11 ms
    64 bytes from 220.181.111.148: icmp_seq=3 ttl=51 time=8.99 ms
    ```

9.  Run the following command to check whether IP forwarding is enabled on the proxy ECS:

    **cat /proc/sys/net/ipv4/ip\_forward**

    -   If  **0**  \(disabled\) is displayed, go to  [10](#li51820417113959).
    -   If  **1**  \(enabled\), go to  [16](#li49419571113959).

10. <a name="li51820417113959"></a>Run the following command to open the IP forwarding configuration file in the vi editor:

    **vi /etc/sysctl.conf**

11. Press  **i**  to enter editing mode.
12. Set the  **net.ipv4.ip\_forward**  value to  **1**.

    Set the  **net.ipv4.ip\_forward**  value to  **1**.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If the  **sysctl.conf**  file does not contain the  **net.ipv4.ip\_forward**  parameter, run the following command to add it:  
    >**echo net.ipv4.ip\_forward=1 \>\> /etc/sysctl.conf**  

13. Press  **Esc**, type  **:wq**, and press  **Enter**.

    The system saves the configurations and exits the vi editor.

14. <a name="li61723653113959"></a>Run the following command to effect the modification:

    **sysctl -p /etc/sysctl.conf**

15. Run the following command to delete the original iptables rule:

    **iptables -F**

16. <a name="li49419571113959"></a>Run the following command to configure source network address translation \(SNAT\) to enable ECSs in the same network segment to access the Internet through the proxy ECS:

    **iptables -t nat -A POSTROUTING -o eth0 -s** _**subnet/netmask-bits**_ **-j SNAT --to** _**nat-instance-ip**_

    For example, if the proxy ECS is in network segment 192.168.125.0, the subnet mask has 24 bits, and the private IP address is 192.168.125.4, run the following command:

    **iptables -t nat -A POSTROUTING -o eth0 -s** _192.168.125.0/24_ **-j SNAT --to 192.168.125.4**

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >To retain the preceding configuration even after the ECS is restarted, run the  **vi /etc/rc.local**  command to edit the  **rc.local**  file. Specifically, copy the rule described in step  [14](#li61723653113959)  into  **rc.local**, press  **Esc**  to exit the editing mode, and enter  **:wq**  to save and exit the file.  

17. Run the following command to check whether SNAT has been configured:

    **iptables -t nat --list**

    SNAT has been configured if information similar to  [Figure 1](#fig27598108113959)  is displayed.

    **Figure  1**  Successful SNAT configuration<a name="fig27598108113959"></a>  
    ![](figures/successful-snat-configuration.png "successful-snat-configuration")

18. Add a route.
    1.  Log in to management console.
    2.  Click  ![](figures/icon-region-0.png)  in the upper left corner and select the desired region and project.
    3.  Under  **Network**, click  **Virtual Private Cloud**.
    4.  Select a VPC to which a route is to be added and click  **Route Tables**. On the  **Route Tables**  page, click  **Add Route**.
    5.  Set route information on the displayed page.
        -   **Destination**: indicates the destination network segment. The default value is  **0.0.0.0/0**.
        -   **Next Hop**: indicates the private IP address of the SNAT ECS.

            You can obtain the private IP address of the ECS on the  **Elastic Cloud Server**  page.




## Follow-up Procedure<a name="section1977851205413"></a>

To delete the added iptables rules, run the following command:

**iptables -t nat -D POSTROUTING -o eth0 -s** _**subnet/netmask-bits**_ **-j SNAT --to** _**nat-instance-ip**_

For example, if the proxy ECS is in network segment 192.168.125.0, the subnet mask has 24 bits, and the private IP address is 192.168.125.4, run the following command:

**iptables -t nat -D POSTROUTING -o eth0 -s 192.168.125.0/24 -j SNAT --to 192.168.125.4**

