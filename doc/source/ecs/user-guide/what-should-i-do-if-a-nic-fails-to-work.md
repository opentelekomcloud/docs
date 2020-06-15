# What Should I Do If a NIC Fails to Work?<a name="EN-US_TOPIC_0036068717"></a>

## Symptom<a name="section17904250171325"></a>

The NIC equipped on a disk-intensive or large-memory ECS fails to work.

## Possible Causes<a name="section50053646171330"></a>

The NIC driver has not been correctly installed.

## Solution<a name="section38560614171337"></a>

Disk-intensive and large-memory ECSs use passthrough NICs to improve network performance. You must install the passthrough NIC driver on the ECS or the image that is used for creating the ECS.

>![](/images/icon-note.gif) **NOTE:**   
>If you mount the CD/DVD-ROM driver over a VPN, ensure that the VPN bandwidth is greater than 8 Mbit/s.  

You can do so by performing the following operations:

1.  Obtain the passthrough NIC driver.

    Passthrough NIC driver versions vary depending on the OS. For details, see  [Table 1](#table39612229174432).

    **Table  1**  NIC driver versions and OSs

    <a name="table39612229174432"></a>
    <table><thead align="left"><tr id="row4221119174432"><th class="cellrowborder" valign="top" width="21.68%" id="mcps1.2.4.1.1"><p id="p35195222174432"><a name="p35195222174432"></a><a name="p35195222174432"></a>NIC Driver Version</p>
    </th>
    <th class="cellrowborder" valign="top" width="44.24%" id="mcps1.2.4.1.2"><p id="p32240719174432"><a name="p32240719174432"></a><a name="p32240719174432"></a>OS</p>
    </th>
    <th class="cellrowborder" valign="top" width="34.08%" id="mcps1.2.4.1.3"><p id="p61361445174432"><a name="p61361445174432"></a><a name="p61361445174432"></a>How to Obtain</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row40188444174432"><td class="cellrowborder" rowspan="2" valign="top" width="21.68%" headers="mcps1.2.4.1.1 "><p id="p6366341174432"><a name="p6366341174432"></a><a name="p6366341174432"></a>ixgbevf 2.16.4</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.24%" headers="mcps1.2.4.1.2 "><p id="p45911649174432"><a name="p45911649174432"></a><a name="p45911649174432"></a>CentOS 7.2 64bit</p>
    </td>
    <td class="cellrowborder" rowspan="2" valign="top" width="34.08%" headers="mcps1.2.4.1.3 "><p id="p49377918174432"><a name="p49377918174432"></a><a name="p49377918174432"></a><a href="https://sourceforge.net/projects/e1000/files/ixgbevf stable/2.16.4/" target="_blank" rel="noopener noreferrer">https://sourceforge.net/projects/e1000/files/ixgbevf%20stable/2.16.4/</a></p>
    </td>
    </tr>
    <tr id="row37911098174432"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p26151677174432"><a name="p26151677174432"></a><a name="p26151677174432"></a>Red Hat Enterprise Linux 7.2 64bit</p>
    </td>
    </tr>
    <tr id="row34222271174432"><td class="cellrowborder" valign="top" width="21.68%" headers="mcps1.2.4.1.1 "><p id="p5655568174432"><a name="p5655568174432"></a><a name="p5655568174432"></a>ixgbevf 2.16.1</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.24%" headers="mcps1.2.4.1.2 "><p id="p55447863174432"><a name="p55447863174432"></a><a name="p55447863174432"></a>SUSE Linux Enterprise Server 11 SP3 64bit</p>
    <p id="p29268722174432"><a name="p29268722174432"></a><a name="p29268722174432"></a>SUSE Linux Enterprise Server 11 SP4 64bit</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.08%" headers="mcps1.2.4.1.3 "><p id="p63388838174432"><a name="p63388838174432"></a><a name="p63388838174432"></a><a href="https://sourceforge.net/projects/e1000/files/ixgbevf stable/2.16.1/" target="_blank" rel="noopener noreferrer">https://sourceforge.net/projects/e1000/files/ixgbevf%20stable/2.16.1/</a></p>
    </td>
    </tr>
    </tbody>
    </table>

2.  Log in to the ECS.

    For more details, see  [Login Overview](login-overview-(linux).md).

3.  Install the passthrough NIC driver on the ECS. In this procedure, Red Hat Enterprise Linux 7.2 64bit is used as an example.
    1.  Configure the passthrough NIC.

        Not all ECS OSs identify passthrough NICs using the standard NIC naming rule of  **eth**_x_, where  _x_  is a number. If this is the case, you must configure the ECS so that it can identify the passthrough NIC. The procedure is as follows:

        1.  Run the following command to view all NICs on the ECS and identify the passthrough NIC:

            **ifconfig -a**

        2.  Run the following command to switch to the directory where configuration files are stored:

            **cd /etc/sysconfig/network-scripts/**

        3.  Run the following command to create a configuration file for the passthrough NIC:

            **cp ifcfg-eth0 ifcfg-**_NIC\_name_

            In the preceding command,  _NIC\_name_  specifies the name of the passthrough NIC.

        4.  Use the vi editor to edit this configuration file:

            **vi ifcfg-**_NIC\_name_

        5.  Set the  **DEVICE**  parameter in the configuration file to the name of the passthrough NIC. The following is an example configuration:

            ```
            DEVICE="NIC_name"
            BOOTPROTO="dhcp"
            ONBOOT="yes"
            STARTMODE="onboot"
            ```

        6.  Run the following command to restart the network service and allow the configuration to take effect:

            **service network restart**

    2.  Upload the obtained passthrough NIC driver to a directory on the ECS, for example,  **/home**.
    3.  Switch to user  **root**  on the ECS CLI and open the target directory.

        In this example, the passthrough NIC driver is stored in the  **/home**  directory. Run the  **cd** _/home_  command to switch to the target directory.

    4.  Run the following command to decompress the software package. \(In this procedure, ixgbevf version 2.16.4 is used as an example.\)

        **tar -zxvf ixgbevf-2.16.4.tar.gz**

    5.  Run the following command to switch to the generated  **src**  directory:

        **cd ixgbevf-2.16.4/src**

    6.  Run the following commands to install the driver:

        **make**

        **make install**

    7.  Run the following command to restart the ECS to make the drive take effect:

        **reboot**

    8.  Switch to user  **root**  on the ECS CLI and open the  **src**  directory, for example, by running the  **cd** _/home/ixgbevf-2.16.4/src_  command. Then, run the following commands to check whether the driver has been installed:

        **rmmod ixgbevf**

        **insmod ./ixgbevf.ko**

        **ethtool -i **_NIC\_name_

        _NIC\_name_  is the name of the passthrough NIC, for example,  **ens5**.

        >![](/images/icon-note.gif) **NOTE:**   
        >-   After you run the  **rmmod ixgbevf**  command, the system may display an error message. This message does not affect the installation of the passthrough NIC driver and can be ignored.  
        >-   _NIC\_name_  specifies the passthrough NIC name, for example,  **ens5.**  

    9.  Check the driver status based on the displayed information.

        In this example, the driver is installed if  **driver**  is  **ixgbevf**  and  **version**  is  **2.16.4**.



