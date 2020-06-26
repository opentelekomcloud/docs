# Configuring a Virtual IP Address for the Server \(Deprecated\)<a name="evs_01_0026"></a>

## Scenarios<a name="section44945912112556"></a>

Before you use EVS replication, bind a virtual IP address to the production server and DR server, respectively. Then configure the virtual IP address as the static IP address for the servers. This virtual IP address is used to access applications on servers.

-   If a virtual IP address has not been configured for the production server, assign one and bind it to the production server and DR server.
-   If a virtual IP address has been configured for the production server, bind this virtual IP address to the DR server.

    >![](/images/icon-note.gif) **NOTE:**   
    >EVS replication APIs have been deprecated. If you need to use the replication function, see  [Storage Disaster Recovery Service User Guide](https://docs.otc.t-systems.com/en-us/usermanual/sdrs/en-us_topic_0125068221.html)  and  [Storage Disaster Recovery Service API Reference](https://docs.otc.t-systems.com/en-us/api/sdrs/en-us_topic_0108184470.html).  


## Prerequisites<a name="section3065738815149"></a>

You have obtained the VPC, subnet, MAC address, and virtual IP address of the production server. For details, see  [Collecting ECS Information \(Deprecated\)](collecting-ecs-information-(deprecated).md).

## Procedure<a name="section61097236151453"></a>

The following operations are for reference only. For details, see  **Assigning a Virtual IP Address**  in the  _Virtual Private Cloud User Guide_.

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  Under  **Computing**, click  **Elastic Cloud Server**.

    The  **Elastic Cloud Server**  page is displayed.

4.  In the ECS list, locate the production ECS and click the ECS name.

    The ECS details page is displayed.

5.  On the ECS details page, locate the VPC and click the VPC name.

    The  **Virtual Private Cloud**  page is displayed.

6.  In the VPC list, locate the VPC of the production ECS and click the VPC name.

    The VPC details page is displayed.

7.  On the  **Subnets**  tab, locate the subnet of the production ECS and click the subnet name.

    The subnet details page is displayed.

8.  Click the  **Virtual IP Addresses**  tab and check whether the production ECS is bound with a virtual IP address.
    -   If yes, perform the following operation:
        1.  Locate the row that contains the virtual IP address and click  **Bind to Server**  in the  **Operation**  column. On the displayed page, bind the virtual IP address to the NIC of the DR server.

            After the virtual IP address is bound with the DR server, the subnet details page is displayed.

    -   If no, perform the following operations:
        1.  Click  **Assign Virtual IP Address**.

            After the application succeeds, you can view the virtual IP address in the virtual IP address list.

            >![](/images/icon-note.gif) **NOTE:**   
            >When assigning the virtual IP address, you can select the  **Automatic**  or  **Manual**  mode based on your service requirements.  

        2.  Locate the row that contains the virtual IP address and click  **Bind to Server**  in the  **Operation**  column. On the displayed page, bind the virtual IP address to the NIC of the production server.

            After the virtual IP address is bound with the production server, the subnet details page is displayed.

        3.  Locate the row that contains the virtual IP address and click  **Bind to Server**  in the  **Operation**  column. On the displayed page, bind the virtual IP address to the NIC of the DR server.

            After the virtual IP address is bound with the DR server, the subnet details page is displayed.


9.  <a name="li894545421812"></a>On the subnet details page, take note of the subnet and the IP address of the server's NIC where the virtual IP address has been bound.

    An example is provided as follows:

    -   Subnet: 192.168.0.0/24
    -   Bound server \(NIC\): ecs-001 \(192.168.0.176\)

10. After a virtual IP address is bound with a server, perform the following substeps to configure the bound IP address as the static IP address:

    The following example uses CentOS 7.2 64bit as the sample OS.

    >![](/images/icon-note.gif) **NOTE:**   
    >The configuration method varies depending on the server OS. This document is used for reference only. For the detailed operations and differences, see the corresponding OS documents.  
    >For the Windows OS, see the  [Microsoft official documentation](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/ff710457(v=ws.10)).  

    1.  Log in to the server as user  **root**.
    2.  <a name="li1422712286426"></a>Run the following command to check the name of the NIC bound with the virtual IP address in the server:

        **ifconfig**

        You can obtain the NIC name using the NIC IP address recorded in  [9](#li894545421812). In this example, the NIC name is  **eth0**.

    3.  Run the following command to switch to the directory containing NIC configuration files:

        **cd /etc/sysconfig/network-scripts**

    4.  Run the following command to copy NIC configuration file  **eth0**  and change its name to  **eth0:1**:

        **cp eth0 eth0:1**

    5.  Perform the following operations to modify the configuration parameters of  **eth0:1**  using the vi editor:
        1.  Run the following command to open the  **ifcfg-eth0:1**  file:

            **vi ifcfg-**eth0:1****

        2.  Press  **i**  to enter editing mode.
        3.  Configure the parameters according to the following example:

            ```
            BOOTPROTO=static
            DEVICE=eth0:1
            NAME=eth0:1
            ONBOOT=yes
            TYPE=Ethernet
            USERCTL=no
            IPADDR=192.168.0.176
            NETMASK=255.255.255.0
            ```

            Configuration descriptions of the  **NAME**,  **IPADDR**, and  **NETMASK**  fields:

            -   **NAME**: Specifies the NIC name recorded in  [10.b](#li1422712286426).
            -   **IPADDR**: Specifies the NIC IP address recorded in  [9](#li894545421812).
            -   **NETMASK**: Specifies the subnet recorded in  [9](#li894545421812).

                In this example, the subnet mask has 24 bits. Therefore, enter  **255.255.255.0**  for  **NETMASK**.

        4.  Press  **Esc**, enter  **:wq**, and press  **Enter**.

            The system saves the configurations and exits the vi editor.

    6.  Run the following command to delete unnecessary NIC files from the  **/etc/sysconfig/network-scripts**  directory:

        **rm** _Name of the unnecessary NIC file_

        For example, run the following command:

        **rm ifcfg-eth1**

        >![](/images/icon-note.gif) **NOTE:**   
        >Before deleting the unnecessary NIC files, you are advised to back up the files.  
        >If multiple unnecessary NIC files exist, delete them one by one. Ensure that the  **/etc/sysconfig/network-scripts**  directory contains only the in-use NIC file.  

    7.  Run the following command to check whether the  **70-persistent-ipoib.rules**  file exists in the  **/etc/udev/rules.d/**  directory:

        **ls /etc/udev/rules.d/70-persistent-ipoib.rules**

        -   If yes, use the vi editor to configure the NIC information, including the NIC name and MAC address, for production and DR servers.
            1.  Run the following command to open the  **70-persistent-ipoib.rules**  file:

                **vi /etc/udev/rules.d/70-persistent-ipoib.rules**

            2.  Press  **i**  to enter editing mode.
            3.  Add NIC information for the DR server based on that of the production server. For details, see the following example:

                ```
                ACTION=="add", SUBSYSTEM=="net", DRIVERS=="?*", ATTR{type}=="32", ATTR{address}=="fa:16:3e:9e:74:ed", NAME="eth0" 
                ACTION=="add", SUBSYSTEM=="net", DRIVERS=="?*", ATTR{type}=="32", ATTR{address}=="fa:16:3e:b1:3b:08", NAME="eth1"
                
                ACTION=="add", SUBSYSTEM=="net", DRIVERS=="?*", ATTR{type}=="32", ATTR{address}=="fa:16:3e:72:2b:aa", NAME="eth0" 
                ACTION=="add", SUBSYSTEM=="net", DRIVERS=="?*", ATTR{type}=="32", ATTR{address}=="fa:16:3e:f1:52:0b", NAME="eth1"
                ```

                Configuration descriptions of the  **ATTR\{address\}**  and  **NAME**  fields:

                -   **ATTR\{address\}**: specifies the MAC address of server's NIC.
                -   **NAME**: Specifies the NIC name recorded in  [10.b](#li1422712286426).

                    >![](/images/icon-note.gif) **NOTE:**   
                    >Ensure that the  **NAME**  \(NIC name\) values of the production and DR servers are consistent. The  **ATTR\{address\}**  \(MAC address\) value can be obtained in  [Collecting ECS Information \(Deprecated\)](collecting-ecs-information-(deprecated).md).  


            4.  Press  **Esc**, enter  **:wq**, and press  **Enter**.

                The system saves the configurations and exits the vi editor.

        -   If no, go to  [10.h](#li145676502016).

    8.  <a name="li145676502016"></a>Run the following command to restart the network service for the configuration to take effect:

        **service network restart**



