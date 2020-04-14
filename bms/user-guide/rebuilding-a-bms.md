# Rebuilding a BMS<a name="EN-US_TOPIC_0095819241"></a>

## Scenarios<a name="section60394636111543"></a>

If the BMS cannot work properly due to hardware or SDI card damage, you can rebuild the BMS. This section describes how to rebuild a BMS.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>The BMS is not automatically rebuilt. You need to contact the administrator to have your BMS rebuilt.  

## Notes<a name="section37447471165714"></a>

-   Currently, only BMSs that are quickly provisioned can be rebuilt.
-   After a BMS is rebuilt, it will start automatically.
-   If the BMS uses an IB NIC, record the IP address of the IB NIC rebuilding the BMS.
-   If the BMS uses a QinQ network, record the IP address of the QinQ network before rebuilding the BMS.

## Restrictions and Limitations<a name="section4500313111616"></a>

-   A BMS can only be rebuilt in the same POD.
-   A BMS to be rebuilt must use an EVS disk as its system disk.
-   Data on local disks cannot be migrated after a BMS is rebuilt.

## Prerequisites<a name="section2641260214160"></a>

-   The BMS to be rebuilt must be stopped.
-   The BMS to be rebuilt must have a system disk.

## Procedure<a name="section1234316614565"></a>

1.  If your BMS uses a QinQ network, delete configurations of the original QinQ network before rebuilding the BMS. For example, if eth3 and eth5 form port group bond1 for the QinQ network, delete the following configuration files:

    **rm** **/etc/udev/rules.d/80-persistent-net.rules**

    **rm** **/etc/sysconfig/network-scripts/ifcfg-eth3**

    **rm** **/etc/sysconfig/network-scripts/ifcfg-eth5**

    **rm** **/etc/sysconfig/network-scripts/ifcfg-bond1**

2.  Contact the administrator and apply for rebuilding the BMS.
    -   If your BMS uses the QinQ network, reconfigure the QinQ network based on the original QinQ network configuration and by following the instructions in  [Configuring a User-defined VLAN \(SUSE Linux Enterprise Server 12\)](configuring-a-user-defined-vlan-(suse-linux-enterprise-server-12).md)  to  [Configuring a User-defined VLAN \(Windows Server\)](configuring-a-user-defined-vlan-(windows-server).md)  after the BMS is rebuilt.
    -   If your BMS uses the IB network and the IB NIC IP address assignment mode is DHCP, the IP address of the BMS will change after it is rebuilt. Therefore, if your service heavily depends on the IP address, you need to reconfigure the IP address of the IB network using the static configuration method. The operations describe how to set the IP address of the IB NIC to the original IP address.
        1.  Log in to the BMS OS.
        2.  Create the  **/etc/sysconfig/network-scripts/ifcfg-ib0**  configuration file. The following uses CentOS as an example. Set  **IPADDR**  to the IP address of the BMS before it is rebuilt.

            ```
            #/etc/sysconfig/network-scripts/ifcfg-ib0
            DEVICE=ib0
            ONBOOT=yes
            BOOTPROTO=none
            IPADDR=172.31.0.254
            NETWORK=172.31.0.0
            BROADCAST=172.31.0.255
            NETMASK=255.255.255.0
            ```

        3.  Change the value of  **enable\_ib**  in the  **/opt/huawei/network\_config/bms-network-config.conf**  file to  **False**.

            **Figure  1**  Changing the parameter value<a name="fig33321881271"></a>  
            ![](figures/changing-the-parameter-value.png "changing-the-parameter-value")

        4.  Save the configuration and exit. Then restart the NIC.

            **ifdown** **ib0**

            **ifup** **ib0**

        5.  Run the following command to check whether the configured IP address takes effect:

            **ifconfig** **ib0**




