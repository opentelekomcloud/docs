# How Can I Manually Configure an IP Address for an InfiniBand NIC?<a name="EN-US_TOPIC_0083225171"></a>

IP over InfiniBand \(IPoIB\) allows IP data transmission over InfiniBand. For SUSE high-performance H2 and HL1 ECSs, if IPoIB is required, you must manually configure an IP address for the InfiniBand NIC after installing the InfiniBand NIC driver.

## Prerequisites<a name="section35761724112321"></a>

The InfiniBand NIC driver has been installed on the high-performance H2 or HL1 ECSs.

## Background<a name="section42060912112551"></a>

To prevent IP address conflict of the InfiniBand NICs configured for the ECSs of a tenant, determine the IP address to be configured for an InfiniBand NIC according to the IP addresses available in the VPC. The method is as follows:

For example, if the first two eight-bits of the IP address \(specified by  **IPADDR**\) to be configured for the InfiniBand NIC are consistently  **169.254**, the latter two eight-bits must be the same as those of the  **eth0**  IP address, and the subnet mask must be the same as that of the  **eth0**  NIC.

An example is provided as follows:

If the IP address of the  **eth0**  NIC is 192.168.0.100/24, the IP address to be configured for the InfiniBand NIC is 169.254.0.100/24.

## Procedure<a name="section25685995112359"></a>

1.  Log in to the ECS.
2.  Run the following command to switch to user  **root**:

    **sudo su -**

3.  Run the following command to edit the  **/etc/sysconfig/network/ifcfg-ib0**  file:

    **vi  /etc/sysconfig/network/ifcfg-ib0**

4.  Enter the following information:

    **DEVICE=ib0**

    **BOOTPROTO=static**

    **IPADDR=**_IP address to be configured for the InfiniBand NIC_

    **NETMASK=**_Subnet mask_

    **STARTMODE=auto**

    >![](/images/icon-note.gif) **NOTE:**   
    >For instructions about how to obtain the IP address and subnet mask for an InfiniBand NIC, see  [Background](#section42060912112551).  

5.  Run the following command to restart the network for the configuration to take effect:

    **service network restart**


