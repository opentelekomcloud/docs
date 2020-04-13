# Deploying NSX<a name="EN-US_TOPIC_0159392322"></a>

1.  Log in to vCenter \(Mozilla Firefox is recommended\) and deploy NSX Manager.
    1.  Right-click  **Data Center**  and select  **Deploy OVF Template**  from the drop-down list. Select the VMware-NSX-Manager OVA file that has been uploaded to the jump VM.
    2.  The configurations are as follows:
        -   **Download Size**:  **2.5 GB**
        -   **Disk Space**:  **60.0 GB**
        -   **Name**:  **NSX Manager**
        -   **Data Store**:  **Datastore**
        -   **Destination**:  **11.11.11.101**
        -   **Disk Storage**:  **thick provisioning lazy zeroed**
        -   **Network Mapping**:  **Management Network to DPortGroup-mgmt**
        -   **IP Address Assignment Mode**:  **static-manual, IPv4**
        -   Properties:

            Hostname=NSX-manager

            Network 1 IPv4 address=11.11.11.4

            Network 1 subnet mask=255.255.255.0

            Default IPv4 gateway: 11.11.11.1

            DNS server list=11.11.11.6

            NTP server list=11.11.11.6

            Enable SSH=False


2.  Open a browser and connect to the NSX Manager GUI.

    The login address is https://_nsx-manager-ip_  or https://_nsx-manager-hostname_.

    Use the password configured during installation to log in as user  **admin**  and click  **View Summary**. Ensure that the vPostgres, RabbitMQ, and NSX management services are running.

    ![](figures/8-(1).png)

3.  Register vCenter Server on NSX Manager.
    1.  Under  **NSX Manager Virtual Appliance Management**, click  **Manage vCenter Registration**.

        ![](figures/9.png)

    2.  Edit the vCenter Server element to point to the IP address or host name of the vCenter Server, and enter the username and password of the vCenter Server. You are advised to enter username  **administrator@vsphere.local**  or your secondary account instead of user  **root**.

4.  Configure Single Sign On.
    1.  On the  **NSX Management Service**  page, click  **Edit**  of  **Lookup Service**. In the displayed dialog box, enter the following information.

        **Figure  1**  Lookup Service page<a name="fig562810491467"></a>  
        ![](figures/lookup-service-page.png "lookup-service-page")

        -   **Lookup Service Host**: Enter the vCenter Server IP address or host name and its username and password.
        -   **Lookup Service Port**: Enter  **443**.

    2.  Verify that the  **Status**  of  **Lookup Service**  is  **Connected**.

        **Figure  2**  Lookup Service status<a name="fig11373752164914"></a>  
        ![](figures/lookup-service-status.png "lookup-service-status")

5.  Install and allocate the NSX for vSphere license \(this solution relies on vSphere 6.5\).
    1.  Log in to the vSphere Web Client.
    2.  Choose  **Administration**  \>  **Licenses**  \>  **Assets**  \>  **Solutions**  and select  **NSX for vSphere**  in the  **Solution**  list. Select  **Assign license...**  from the  **All Actions**  drop-down list.
    3.  Click  **Add**, enter the license key, and click  **Next**.
    4.  Add the license name, click  **Next**, and click  **Finish**.
    5.  Select a new license and click  **View Features**  to view the functions that can be enabled by the license.
    6.  Click  **OK**  to allocate the new license to NSX.

6.  Deploy the NSX Controller cluster.
    1.  Log in to the vSphere Web Client.
    2.  Choose  **Home**  \>  **Network and Security**  \>  **Installation and Upgrade**  and click the  **Management**  tab.
    3.  Click the  **NSX Controller Node**  tab and click the  **+**  icon under the controller node.
    4.  Specify the following parameters.

        -   **Name**:  **NSX-controller01**
        -   **Data Center**:  **DataCenter**
        -   **Cluster/Resource Pool**:  **test**
        -   **Data Store**:  **vsanDatastore**
        -   **Connected To**:  **DPortGroup-mgmt**
        -   **IP Address Pool**:  **ippool**

        Connect NSX Controller to the vSphere Distributed Switch port group of NSX Manager, other controllers and hosts.

    5.  If you have not configured an IP address pool for the controller cluster, click  **Create IP Address Pool**  and create one. Use the IP network segment planned in  [Table 2](environment-preparations.md#table9652104520446).
    6.  Enter the password of the controller. If the password does not comply with the password requirements, a prompt will be displayed.
    7.  After you finish deploying the first controller, deploy the other two using the same method.

7.  Exclude VMs from the firewall protection \(the network of vCenter Server will be interrupted in case of a misoperation\). NSX Manager, NSX Controller, and NSX Edge will be automatically excluded from the protection of the NSX distributed firewall. You need to add the vCenter, Windows jump VMs, and DNS VMs to the exclusion list.
    1.  On the vSphere Web Client, click  **Network and Security**. In  **Security**, click  **Firewall Configuration**.
    2.  Click the  **Exclusion list**  tab.
    3.  Click  **+**, select the VMs that you want to exclude, and click  ![](figures/15.png).
    4.  Click  **OK**.

8.  Prepare a host cluster for NSX. This step is applicable to preparing for hosts for the first time. If NSX nodes have been added to the cluster before the ESX nodes are created, you are advised to reinstall ESX and then perform this step.
    1.  On the vCenter Web Client, choose  **Network and Security**  \>  **Installation and Upgrade**. Then click the  **Host Preparation**  tab.
    2.  Click the cluster that requires the NSX logical switching, routing, and firewall functions, click  **Operation**, and select  **Install**  from the drop-down list.

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >A computing cluster \(also referred to as payload cluster\) uses application program VMs \(such as web and database VMs\). If a computing cluster requires the NSX logical switching, routing, and firewall functions, you must perform installation operations for the computing cluster.  
        >In this example, in the shared  **Management and Edge**  cluster, NSX Manager VMs and controller VMs share a cluster containing Edge devices, including distributed logical routers \(DLRs\) and Edge service gateways \(ESGs\). In this case, you must perform installation operations for the shared cluster. On the contrary, if  **Management and Edge**  has a specified cluster that is not shared \(recommended in the production environment\), perform installation operations on the Edge and management clusters, respectively.  

    3.  If a green tick is displayed in the  **NSX Installation**  column, the installation is complete.
    4.  Verify the installation. Log in to each ESX host and run the  **esxcli software vib list | grep esx**  command. If  **esx-nsxv**  is displayed, the installation is successful.

9.  Configure the VXLAN transmission parameters.
    1.  On the vCenter Web Client, choose  **Network and Security**  \>  **Installation and Upgrade**  \>  **Host Preparation**, and click  **Configure**  next to  **VXLAN**.
    2.  Configure the logical network.

        Specify the parameters shown in the preceding figure. Set  **MTU**  to  **1550**  or a greater value for each switch. By default, the value is  **1600**.

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >If the MTU value is greater than that of the VXLAN MTU, the value of MTU will not be adjusted. If the value is set to a small one, it will be adjusted to match VXLAN MTU. For example, if the value of MTU is set to 2000 and you accept the default VXLAN MTU value 1600, the value of MTU will not be changed. If the value of MTU is 1500 and that of VXLAN MTU is 1600, the value of MTU will be changed to 1600.  

    3.  Add an IP address pool. Ensure that the selected VLAN does not contain IP address segments used by other resources.
    4.  When you configure the VXLAN, a new distributed port group will be created. You can view its information on the  **Summary**  page.

10. Allocate a segment ID pool and the multicast address range.
    1.  On the vCenter Web Client, choose  **Home**  \>  **Network and Security**  \>  **Installation and Upgrade**  and click the  **Configure Logical Network**  tab.
    2.  Click  **VXLAN Configuration**, click  **Edit**  next to  **Segment ID**, and set the segment ID range to  **5000-5999**. Disable the multicast addressing.

11. Add a transmission area \(select the unicast mode\).
    1.  On the vCenter Web Client, choose  **Home**  \>  **Network and Security**  \>  **Installation and Upgrade**  and click the  **Configure Logical Network**  tab.
    2.  Click the  **Transport Zones**  tab and then click the  **+**  icon to create a transport zone.
    3.  In the  **Create Transport Zone**  dialog box, specify  **Name**  and  **Description**  \(optional\), select  **Unicast**  for  **Replication Mode**, select the clusters to be added, and click  **Add**.

12. Create a logical switch and two VMs. Connect the VMs to the logical switch to verify the connectivity. For details, see  [Add a Logical Switch](https://docs.vmware.com/en/VMware-NSX-Data-Center-for-vSphere/6.4/com.vmware.nsx.install.doc/GUID-DD31D6BC-2E56-4E91-B45F-FCA3E80FF786.html).
13. Create an NSX Edge to enable VMware VMs to communicate with the external network.
    1.  On the vCenter Web Client, choose  **Home**  \>  **Networking & Security**  \>  **NSX Edges**, create a new logical router and uplink interface to access the hb-edge-internal port group. Set the IP address to 11.11.8.2/24. Create internal to access logical switch to which the VM belongs. For details, see  [Add a Distributed Logical Router](https://docs.vmware.com/en/VMware-NSX-Data-Center-for-vSphere/6.4/com.vmware.nsx.install.doc/GUID-E825C0C7-F4CC-4B26-90AF-A2167AC519DB.html).
    2.  On the  **NSX Edge**  page, create an NSX Edge device as the Edge service gateway.
    3.  Connect the uplink to the DPortgroup-mgmt port group and set the IP address to 11.11.11.30, which is the IP address of the port reserved by edge. Add an internal interface to connect to the edge-internal port group and set the IP address to 11.11.8.1/24.

        For details, see  [Add an Edge Services Gateway](https://docs.vmware.com/en/VMware-NSX-Data-Center-for-vSphere/6.4/com.vmware.nsx.install.doc/GUID-B9A97F20-4996-4E16-822C-0B98DDE70571.html).

    4.  Configure an OSPF dynamic route between the created logical router and Edge service gateway \(the Edge gateway detects the routing topology on the logical router\). For details, see  [Configure OSPF on a Logical \(Distributed\) Router](https://docs.vmware.com/en/VMware-NSX-Data-Center-for-vSphere/6.4/com.vmware.nsx.install.doc/GUID-6E985577-3629-42FE-AC22-C4B56EFA8C9B.html)  and  [Configure OSPF on an Edge Services Gateway](https://docs.vmware.com/en/VMware-NSX-Data-Center-for-vSphere/6.4/com.vmware.nsx.install.doc/GUID-EF251ED4-5BCA-43D5-9C01-975601EACF1E.html).

        After the preceding configurations are complete, VMs in the VXLAN network connected to the BMS router can communicate with each other through the logical router. The IP requests for accessing the Internet from VMs will be routed to the uplink of the Edge service gateway and then to the VPC.

    5.  \(Optional\) If a VMware VM needs to access the Internet through EIP, you need to configure NAT rules on the Edge gateway to convert the internal network IP address of the VM into an uplink IP address of the Edge gateway.


