# Configuring a User-defined VLAN \(SUSE Linux Enterprise Server 12\)<a name="EN-US_TOPIC_0095251843"></a>

>![](/images/icon-note.gif) **NOTE:**   
>The network segment of the user-defined VLAN cannot overlap the network information configured on the BMS.  

This section uses SUSE Linux Enterprise Server 12 SP1 \(x86\_64\) as an example to describe how to configure a user-defined VLAN for BMSs.

1.  Use a key or password to log in to the BMS as user  **root**.
2.  <a name="li1143133511162"></a>On the BMS CLI, run the following command to check the NIC information:

    **ip** **link**

    Information similar to the following is displayed.

    ```
    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default 
        link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    2: eth0: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 8888 qdisc mq master bond0 state UP mode DEFAULT group default qlen 1000
        link/ether fa:16:3e:3d:1c:e0 brd ff:ff:ff:ff:ff:ff
    3: eth1: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 8888 qdisc mq master bond0 state UP mode DEFAULT group default qlen 1000
        link/ether fa:16:3e:3d:1c:e0 brd ff:ff:ff:ff:ff:ff
    4: eth2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state DOWN mode DEFAULT group default qlen 1000
        link/ether 38:4c:4f:89:55:8d brd ff:ff:ff:ff:ff:ff
    5: eth3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state DOWN mode DEFAULT group default qlen 1000
        link/ether 38:4c:4f:89:55:8e brd ff:ff:ff:ff:ff:ff
    6: bond0: <BROADCAST,MULTICAST,MASTER,UP,LOWER_UP> mtu 8888 qdisc noqueue state UP mode DEFAULT group default 
        link/ether fa:16:3e:3d:1c:e0 brd ff:ff:ff:ff:ff:ff
    7: bond0.3133@bond0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 8888 qdisc noqueue state UP mode DEFAULT group default 
        link/ether fa:16:3e:57:87:6e brd ff:ff:ff:ff:ff:ff
    ```

    >![](/images/icon-note.gif) **NOTE:**   
    >Among the devices, eth0 and eth1 bear the VPC, and eth2 and eth3 bear the user-defined VLAN.  

3.  Configure the udev rules:

    Run the following command to create the  **80-persistent-net.rules**  file:

    **cp** **/etc/udev/rules.d/70-persistent-net.rules** **/etc/udev/rules.d/80-persistent-net.rules**

    Write the NIC MAC address and name that are queried in  [2](#li1143133511162)  and that are not displayed in  **80-persistent-net.rules**  to the file. In this way, after the BMS is restarted, the NIC name and sequence will not change.

    >![](/images/icon-note.gif) **NOTE:**   
    >Ensure that the NIC MAC address and name are lowercase letters.  

    **vim** **/etc/udev/rules.d/80-persistent-net.rules**

    The modification result is as follows:

    ```
    SUBSYSTEM=="net", ACTION=="add", DRIVERS=="?*", ATTR{address}=="38:4c:4f:29:0b:e0", NAME="eth0"
    SUBSYSTEM=="net", ACTION=="add", DRIVERS=="?*", ATTR{address}=="38:4c:4f:29:0b:e1", NAME="eth1"
    SUBSYSTEM=="net", ACTION=="add", DRIVERS=="?*", ATTR{address}=="38:4c:4f:89:55:8d", NAME="eth2"
    SUBSYSTEM=="net", ACTION=="add", DRIVERS=="?*", ATTR{address}=="38:4c:4f:89:55:8e", NAME="eth3"
    ```

    After the modification, save the change and exit.

4.  Run the following command to check the NIC IP address:

    **ifconfig**

    Information similar to the following is displayed, where  **bond0**  and  **bond0.313**  show the NIC IP addresses automatically allocated by the system when you apply for the BMS:

    ```
    bond0     Link encap:Ethernet  HWaddr FA:16:3E:3D:1C:E0  
              inet addr:10.0.1.2  Bcast:10.0.1.255  Mask:255.255.255.0
              inet6 addr: fe80::f816:3eff:fe3d:1ce0/64 Scope:Link
              UP BROADCAST RUNNING MASTER MULTICAST  MTU:8888  Metric:1
              RX packets:852 errors:0 dropped:160 overruns:0 frame:0
              TX packets:1121 errors:0 dropped:0 overruns:0 carrier:0
              collisions:0 txqueuelen:0 
              RX bytes:125429 (122.4 Kb)  TX bytes:107221 (104.7 Kb)
    
    bond0.313 Link encap:Ethernet  HWaddr FA:16:3E:57:87:6E  
              inet addr:10.0.3.2  Bcast:10.0.3.255  Mask:255.255.255.0
              inet6 addr: fe80::f816:3eff:fe57:876e/64 Scope:Link
              UP BROADCAST RUNNING MULTICAST  MTU:8888  Metric:1
              RX packets:169 errors:0 dropped:0 overruns:0 frame:0
              TX packets:13 errors:0 dropped:0 overruns:0 carrier:0
              collisions:0 txqueuelen:0 
              RX bytes:8684 (8.4 Kb)  TX bytes:1696 (1.6 Kb)
    
    eth0      Link encap:Ethernet  HWaddr FA:16:3E:3D:1C:E0  
              UP BROADCAST RUNNING SLAVE MULTICAST  MTU:8888  Metric:1
              RX packets:428 errors:0 dropped:10 overruns:0 frame:0
              TX packets:547 errors:0 dropped:0 overruns:0 carrier:0
              collisions:0 txqueuelen:1000 
              RX bytes:64670 (63.1 Kb)  TX bytes:50132 (48.9 Kb)
    
    eth1      Link encap:Ethernet  HWaddr FA:16:3E:3D:1C:E0  
              UP BROADCAST RUNNING SLAVE MULTICAST  MTU:8888  Metric:1
              RX packets:424 errors:0 dropped:7 overruns:0 frame:0
              TX packets:574 errors:0 dropped:0 overruns:0 carrier:0
              collisions:0 txqueuelen:1000 
              RX bytes:60759 (59.3 Kb)  TX bytes:57089 (55.7 Kb)
    
    lo        Link encap:Local Loopback  
              inet addr:127.0.0.1  Mask:255.0.0.0
              inet6 addr: ::1/128 Scope:Host
              UP LOOPBACK RUNNING  MTU:65536  Metric:1
              RX packets:8 errors:0 dropped:0 overruns:0 frame:0
              TX packets:8 errors:0 dropped:0 overruns:0 carrier:0
              collisions:0 txqueuelen:0 
              RX bytes:520 (520.0 b)  TX bytes:520 (520.0 b)
    ```

5.  Run the following commands to check the names of bonded NICs:

    The in-service bonded NICs cannot be used on the internal communication plane. Therefore, you must obtain them by name.

    **cd** **/etc/sysconfig/network**

    **vi** **ifcfg-**_bond0_

    Information similar to the following is displayed, where  **bond0**  is composed of NICs  **eth0**  and  **eth1**:

    ```
    BONDING_MASTER=yes
    TYPE=Bond
    STARTMODE=auto
    BONDING_MODULE_OPTS="mode=4 xmit_hash_policy=layer3+4 miimon=100"
    NM_CONTROLLED=no
    BOOTPROTO=dhcp
    DEVICE=bond0
    USERCONTRL=no
    LLADDR=fa:16:3e:3d:1c:e0
    BONDING_SLAVE1=eth1
    BONDING_SLAVE0=eth0
    ```

    After the query, exit.

6.  Run the following commands to check the statuses of all NICs:

    **ip** **link**

    Information similar to the following is displayed.

    ```
    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default 
        link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    2: eth0: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 8888 qdisc mq master bond0 state UP mode DEFAULT group default qlen 1000
        link/ether fa:16:3e:3d:1c:e0 brd ff:ff:ff:ff:ff:ff
    3: eth1: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 8888 qdisc mq master bond0 state UP mode DEFAULT group default qlen 1000
        link/ether fa:16:3e:3d:1c:e0 brd ff:ff:ff:ff:ff:ff
    4: eth2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state DOWN mode DEFAULT group default qlen 1000
        link/ether 38:4c:4f:89:55:8d brd ff:ff:ff:ff:ff:ff
    5: eth3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state DOWN mode DEFAULT group default qlen 1000
        link/ether 38:4c:4f:89:55:8e brd ff:ff:ff:ff:ff:ff
    6: bond0: <BROADCAST,MULTICAST,MASTER,UP,LOWER_UP> mtu 8888 qdisc noqueue state UP mode DEFAULT group default 
        link/ether fa:16:3e:3d:1c:e0 brd ff:ff:ff:ff:ff:ff
    7: bond0.3133@bond0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 8888 qdisc noqueue state UP mode DEFAULT group default 
        link/ether fa:16:3e:57:87:6e brd ff:ff:ff:ff:ff:ff
    ```

7.  Run the following commands to change the NIC status  **qdisc mq state DOWN**  to  **qdisc mq state UP**. The following commands use NICs  **eth2**  and  **eth3**  as examples.

    **ip** **link** **set** _eth2_ **up**

    **ip** **link** **set** _eth3_ **up**

8.  <a name="li345243551618"></a>Run the following commands to check the statuses of all NICs:

    **ip** **link**

    Information similar to the following is displayed.

    ```
    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default 
        link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    2: eth0: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 8888 qdisc mq master bond0 state UP mode DEFAULT group default qlen 1000
        link/ether fa:16:3e:3d:1c:e0 brd ff:ff:ff:ff:ff:ff
    3: eth1: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 8888 qdisc mq master bond0 state UP mode DEFAULT group default qlen 1000
        link/ether fa:16:3e:3d:1c:e0 brd ff:ff:ff:ff:ff:ff
    4: eth2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP mode DEFAULT group default qlen 1000
        link/ether 38:4c:4f:89:55:8d brd ff:ff:ff:ff:ff:ff
    5: eth3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP mode DEFAULT group default qlen 1000
        link/ether 38:4c:4f:89:55:8e brd ff:ff:ff:ff:ff:ff
    6: bond0: <BROADCAST,MULTICAST,MASTER,UP,LOWER_UP> mtu 8888 qdisc noqueue state UP mode DEFAULT group default 
        link/ether fa:16:3e:3d:1c:e0 brd ff:ff:ff:ff:ff:ff
    7: bond0.3133@bond0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 8888 qdisc noqueue state UP mode DEFAULT group default 
        link/ether fa:16:3e:57:87:6e brd ff:ff:ff:ff:ff:ff
    ```

9.  Check the statuses of the NICs in  [8](#li345243551618)  and obtain the names of the NICs in  **qdisc mq state UP**  state.

    Only the NICs that are in  **qdisc mq state UP**  state and have not been used can be bonded. In this example, such NICs are  **eth2**  and  **eth3**.

    The LLADR values of NICs  **eth2**  and  **eth3**  are  **38:4c:4f:89:55:8d**  and  **38:4c:4f:89:55:8e**, respectively.

10. Run the following commands to create the configuration files of NICs  **eth2**  and  **eth3**:

    You can copy an existing NIC configuration file and modify it to improve the creation efficiency.

    **cp** _ifcfg-eth0_ _ifcfg-eth2_

    **cp** _ifcfg-eth__1_ _ifcfg-eth3_

11. Run the following commands to modify the configuration files of NICs  **eth2**  and  **eth3**:

    **vi** _ifcfg-eth2_

    **vi** _ifcfg-eth3_

    Modified configuration file of NIC  **eth2**  is as follows.

    In this configuration file, set  **MTU**  to  **8888**,  **BOOTPROTO**  to  **STATIC**, and configure  **DEVICE**  and  **LLADDR**  as required.

    ```
    STARTMODE=auto
    MTU=8888
    NM_CONTROLLED=no
    BOOTPROTO=STATIC
    DEVICE=eth2
    USERCONTRL=no
    LLADDR=38:4c:4f:89:55:8d
    TYPE=Ethernet
    ```

    Modified configuration file of NIC  **eth3**  is as follows:

    ```
    STARTMODE=auto
    MTU=8888
    NM_CONTROLLED=no
    BOOTPROTO=STATIC
    DEVICE=eth3
    USERCONTRL=no
    LLADDR=38:4c:4f:89:55:8e
    TYPE=Ethernet
    ```

    After the modification, save the change and exit.

12. Run the following command to bond NICs  **eth2**  and  **eth3**  to a NIC, for example,  **bond1**:

    Run the following commands to create the  **ifcfg-bond1**  file and modify the configuration file:

    **cp** _ifcfg-bond0_ _ifcfg-bond1_

    **vi** _ifcfg-bond1_

    Modified configuration file of NIC  **bond1**  is as follows.

    In this configuration file,  **MTU**  is set to  **8888**,  **BONDING\_MODULE\_OPTS**  is set to  **mode=1 miimon=100**,  **BOOTPROTO**  is set to  **STATIC**.  **DEVICE**,  **BONDING\_SLAVE1**,  **BONDING\_SLAVE0**,  **IPADDR**,  **NETMASK**, and  **NETWORK**  are configured as required.  **LLADDR**  is set to the LLADDR value of the  **BONDING\_SLAVE1**  NIC.

    ```
    BONDING_MASTER=yes
    TYPE=Bond
    MTU=8888
    STARTMODE=auto
    BONDING_MODULE_OPTS="mode=1 miimon=100"
    NM_CONTROLLED=no
    BOOTPROTO=STATIC
    DEVICE=bond1
    USERCONTRL=no
    LLADDR=38:4c:4f:89:55:8d
    BONDING_SLAVE1=eth2
    BONDING_SLAVE0=eth3
    IPADDR=10.0.2.2
    NETMASK=255.255.255.0
    NETWORK=10.0.2.0
    ```

    After the modification, save the change and exit.

13. Make the configuration file take effect.
    1.  Run the following commands to create a temporary directory and copy the NIC configuration file to this directory:

        **mkdir** **/opt**_/tmp/_

        **mkdir** **/opt/tmp/**_xml_

        **cp** **/etc/sysconfig/network/ifcfg\*** **/opt/tmp/**

        **cp** **/etc/sysconfig/network/config** **/opt/tmp/**

        **cp** **/etc/sysconfig/network/dhcp** **/opt/tmp/**

    2.  Run the following commands to stop NICs to form  **bond1**:

        **ip** **link** **set** _eth2_ **down**

        **ip** **link** **set** _eth3_ **down**

    3.  Run the following command to convert the NIC configuration file to a configuration file that can be recognized by the OS:

        **/usr/sbin/wicked** **--log-target=stderr** **--log-level=debug3** **--debug** **all** **convert** **--output** **/opt/tmp/xml** **/opt/tmp/**

    4.  Run the following commands to restart the NICs to form  **bond1**:

        **ip** **link** **set** _eth2_ **up**

        **/usr/sbin/wicked** **--log-target=stderr** **--log-level=debug3** **--debug** **all** **ifup** **--ifconfig** **/opt/tmp/xml/**_eth2_**.xml** _eth2_

        **ip link set** _eth3_ **up**

        **/usr/sbin/wicked** **--log-target=stderr** **--log-level=debug3** **--debug** **all** **ifup** **--ifconfig** **/opt/tmp/xml/**_eth3_**.xml** _eth3_

        **/usr/sbin/wicked** **--log-target=stderr** **--log-level=debug3** **--debug** **all** **ifup** **--ifconfig** **/opt/tmp/xml/bond1.xml** _bond1_

14. Run the following command to query IP addresses:

    **ip** **addr** **show**

    An example is provided as follows:

    ```
    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default 
        link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
        inet 127.0.0.1/8 scope host lo
           valid_lft forever preferred_lft forever
        inet6 ::1/128 scope host 
           valid_lft forever preferred_lft forever
    2: eth0: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 8888 qdisc mq master bond0 state UP group default qlen 1000
        link/ether fa:16:3e:3d:1c:e0 brd ff:ff:ff:ff:ff:ff
    3: eth1: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 8888 qdisc mq master bond0 state UP group default qlen 1000
        link/ether fa:16:3e:3d:1c:e0 brd ff:ff:ff:ff:ff:ff
    4: eth2: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 8888 qdisc mq master bond1 state UP group default qlen 1000
        link/ether 38:4c:4f:89:55:8d brd ff:ff:ff:ff:ff:ff
    5: eth3: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 8888 qdisc mq master bond1 state UP group default qlen 1000
        link/ether 38:4c:4f:89:55:8d brd ff:ff:ff:ff:ff:ff
    6: bond0: <BROADCAST,MULTICAST,MASTER,UP,LOWER_UP> mtu 8888 qdisc noqueue state UP group default 
        link/ether fa:16:3e:3d:1c:e0 brd ff:ff:ff:ff:ff:ff
        inet 10.0.1.2/24 brd 10.0.1.255 scope global bond0
           valid_lft forever preferred_lft forever
        inet6 fe80::f816:3eff:fe3d:1ce0/64 scope link 
           valid_lft forever preferred_lft forever
    7: bond0.3133@bond0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 8888 qdisc noqueue state UP group default 
        link/ether fa:16:3e:57:87:6e brd ff:ff:ff:ff:ff:ff
        inet 10.0.3.2/24 brd 10.0.2.255 scope global bond0.3133
           valid_lft forever preferred_lft forever
        inet6 fe80::f816:3eff:fe57:876e/64 scope link 
           valid_lft forever preferred_lft forever
    8: bond1: <BROADCAST,MULTICAST,MASTER,UP,LOWER_UP> mtu 8888 qdisc noqueue state UP group default 
        link/ether 38:4c:4f:89:55:8d brd ff:ff:ff:ff:ff:ff
        inet 10.0.2.2/24 brd 10.0.2.255 scope global bond1
           valid_lft forever preferred_lft forever
        inet6 fe80::3a4c:4fff:fe29:b36/64 scope link 
           valid_lft forever preferred_lft forever
    ```

15. Run the following commands to delete the temporary directory:

    **cd** **/opt**

    **rm** **-rf** **tmp/**

16. Repeat the preceding operations to configure other BMSs.

