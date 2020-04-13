# Deploying VMware vSAN<a name="EN-US_TOPIC_0159392321"></a>

The vSAN cluster requires at least three ESXi hosts.

1.  Log in to the vSphere Web Client. In the navigation pane, choose  **Host**. On the  **Configuration**  page, click  **VMkernel Adapter**  under  **Network**  and create a VMkernel.
2.  On the  **Select Target Device**  page, select  **DPortGroup-vsan**  for  **Select an existing network**  and click  **Next**.
3.  On the  **Port Attributes**  page, select  **vSAN**  and click  **Next**.
4.  On the  **Set IPv4 Address**  page, select  **Use a static IPv4 address**. Set the IP address of the three ESXi hosts to  **11.11.12.101**,  **11.11.12.102**, and  **11.11.12.103**, respectively. Then click  **Next**.
5.  You can create a vSAN cluster or enable vSAN for an existing cluster. For details, see  [Creating a vSAN Cluster](https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.virtualsan.doc/GUID-3332D48C-E8F2-4462-BC30-60C9532C624C.html).

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   A disk on each ESXi host is reserved as the local datastore. Other SSDs form a disk group and are added to the vSAN cluster.  
    >-   VM disks that have been created on the first ESXi host can be migrated to the vSAN cluster.  


