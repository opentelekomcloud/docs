# Configuring an SNAT Server<a name="vpc_route_0004"></a>

## Scenarios<a name="section46985825185725"></a>

To use the route table function provided by the VPC service, you need to configure SNAT on an ECS to enable other ECSs that do not have EIPs bound in a VPC to access the Internet through this ECS.

The configured SNAT takes effect for all subnets in a VPC.

## Prerequisites<a name="section55962461185854"></a>

-   You have an ECS where SNAT is to be configured.
-   The ECS where SNAT is to be configured runs the Linux OS.
-   The ECS where SNAT is to be configured has only one network interface card \(NIC\).

## Procedure<a name="section27146196185725"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  On the console homepage, under  **Computing**, click  **Elastic Cloud Server**.
4.  On the displayed page, locate the target ECS in the ECS list and click the ECS name to switch to the page showing ECS details.
5.  On the displayed ECS details page, click the  **NICs**  tab.
6.  Click the NIC IP address. In the displayed area showing the NIC details, disable the source/destination check function.

    By default, the source/destination check is enabled. When this check is enabled, the system checks whether source IP addresses contained in the packets sent by ECSs are correct. If the IP addresses are incorrect, the system does not allow the ECSs to send the packets. This mechanism prevents packet spoofing, thereby improving system security. If SNAT is used, the SNAT server needs to forward packets. This mechanism prevents the packet sender from receiving returned packets. Therefore, you need to disable the source/destination check for SNAT servers.

7.  Bind an EIP.
    -   Bind an EIP with the private IP address of the ECS. For details, see  [Assigning an EIP and Binding It to an ECS](assigning-an-eip-and-binding-it-to-an-ecs.md).
    -   Bind an EIP with the virtual IP address of the ECS. For details, see  [Binding a Virtual IP Address to an EIP or ECS](binding-a-virtual-ip-address-to-an-eip-or-ecs.md).

8.  On the ECS console, use the remote login function to log in to the ECS where you plan to configure SNAT.
9.  Run the following command and enter the password of user  **root**  to switch to user  **root**:

    **su - root**

10. Run the following command to check whether the ECS can successfully connect to the Internet:

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >Before running the command, you must disable the response iptables rule on the ECS where SNAT is configured and enable the security group rules.  

    **ping www.google.com**

    The ECS can access the Internet if the following information is displayed:

    ```
    [root@localhost ~]# ping www.google.com
    PING www.a.shifen.com (xxx.xxx.xxx.xxx) 56(84) bytes of data.
    64 bytes from xxx.xxx.xxx.xxx: icmp_seq=1 ttl=51 time=9.34 ms
    64 bytes from xxx.xxx.xxx.xxx: icmp_seq=2 ttl=51 time=9.11 ms
    64 bytes from xxx.xxx.xxx.xxx: icmp_seq=3 ttl=51 time=8.99 ms
    ```

11. Run the following command to check whether IP forwarding of the Linux OS is enabled:

    **cat /proc/sys/net/ipv4/ip\_forward**

    In the command output,  **1**  indicates it is enabled, and  **0**  indicates it is disabled. The default value is  **0**.

    -   If IP forwarding in Linux is enabled, go to step  [14](#li2168883919851).
    -   If IP forwarding in Linux is disabled, perform step  [12](#li3948189019612)  to enable IP forwarding in Linux.

    Many OSs support packet routing. Before forwarding packets, OSs change source IP addresses in the packets to OS IP addresses. Therefore, the forwarded packets contain the IP address of the public sender so that the response packets can be sent back along the same path to the initial packet sender. This method is called SNAT. The OSs need to keep track of the packets where IP addresses have been changed to ensure that the destination IP addresses in the packets can be rewritten and that packets can be forwarded to the initial packet sender. To achieve these purposes, you need to enable the IP forwarding function and configure SNAT rules.

12. <a name="li3948189019612"></a>Use the vi editor to open the  **/etc/sysctl.conf**  file, change the value of  **net.ipv4.ip\_forward**  to  **1**, and enter  **:wq**  to save the change and exit.
13. Run the following command to make the change take effect:

    **sysctl -p /etc/sysctl.conf**

14. <a name="li2168883919851"></a>Configure SNAT.

    Run the following command to enable all ECSs on the network segment \(for example, 192.168.1.0/24\) to access the Internet using the SNAT function:  [Figure 1](#fig27328760201321)  shows the example command.

    **iptables -t nat -A POSTROUTING -o eth0 -s subnet -j SNAT --to nat-instance-ip**

    **Figure  1**  Configuring SNAT<a name="fig27328760201321"></a>  
    ![](figures/configuring-snat.png "configuring-snat")

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >To ensure that the rule will not be lost after the restart, write the rule into the  **/etc/rc.local**  file.  
    >1.  Run the following command to switch to the  **/etc/sysctl.conf**  file:  
    >    **vi /etc/rc.local**  
    >2.  Perform  [14](#li2168883919851)  to configure SNAT.  
    >3.  Run the following command to save the configuration and exit:  
    >    **:wq**  
    >4.  Run the following command to add the execute permission for the  **rc.local**  file:  
    >    **\# chmod +x /etc/rc.local**  

15. Run the following command to check whether the operation is successful: If information similar to  [Figure 2](#fig8358771201535)  \(for example, 192.168.1.0/24\) is displayed, the operation was successful.

    **iptables -t nat --list**

    **Figure  2**  Verifying configuration<a name="fig8358771201535"></a>  
    ![](figures/verifying-configuration.png "verifying-configuration")

16. Add a route. For details, see section  [Adding a Custom Route](adding-a-custom-route.md).

    Set the destination to  **0.0.0.0/0**, and the next hop to the private or virtual IP address of the ECS where SNAT is deployed. For example, the next hop is  **192.168.1.4**.


After these operations are complete, if the network communication still fails, check your security group and firewall configuration to see whether required traffic is allowed.

