# Creating a BMS<a name="EN-US_TOPIC_0053536933"></a>

## Scenarios<a name="section11670076181730"></a>

This section describes how to create a BMS to deploy your services.

## Prerequisites<a name="section1936519509264"></a>

-   You have completed  [Preparations](making-preparations.md).
-   To configure user data injection, you have prepared  [user data scripts](injecting-user-data-into-bmss.md).

## Procedure<a name="section45090433181819"></a>

1.  Log in to the management console.
2.  Under  **Computing**, click  **Bare Metal Server**.

    The BMS console is displayed.

3.  Click  **Allocate BMS**.
4.  Select a region.

    ECSs in different regions cannot communicate with each other over an intranet. You are advised to select the region closest to your services to lower the network delay and improve the access speed. Note that after a BMS is obtained, its region cannot be changed.

5.  Select an AZ.

    An AZ is a physical region where resources use independent power supply and networks. AZs are physically isolated but interconnected through an internal network.

    -   It is recommended that you apply for BMSs in different AZs to ensure high availability of applications running on the BMSs.
    -   To lower the network delay, create BMSs in the same AZ.

6.  Set  **Flavor**.

    The flavor contains the name, CPU, memory, local disks, and extended configuration of the BMS. After you select a flavor, the name and use scenarios of the flavor are displayed under the flavor list.

    **Extended Configuration**  provides the NIC information of the selected flavor. For example, 2 x 2\*10GE indicates that a 10GE NIC with two ports connects to the VPC network and a 10GE extended NIC with two ports supports high-speed interconnection between BMSs.

    >![](/images/icon-note.gif) **NOTE:**   
    >-   Configuration in the flavor, such as CPUs, memory, and local disks, cannot be changed.  
    >-   The bandwidth of different BMS flavors varies. Choose a flavor that meets your requirements.  
    >-   Some flavors support quick BMS provisioning. If you select a flavor of this type, parameter  **System Disk**  is displayed under  **Disk**. The OS of this type of BMS is installed on an EVS disk.  

7.  Set  **Image**.
    -   Public Image

        A public image is a common standard OS image that is available to all users. It contains an OS and pre-installed public applications, such as the SDI iNIC driver, bms-network-config \(a network configuration program\), and Cloud-Init \(an initialization tool\). You can configure the applications and software in a public image as needed.

    -   Private Image

        A private image is an image available only to the user who created it using an external image file or a BMS. It contains an OS, preinstalled public applications, and the user's private applications. Using a private image to create BMSs removes the need to configure multiple BMSs repeatedly.

    -   Shared Image

        A shared image is a private image shared by another public cloud user with you.

8.  Set  **License Type**.

    Set a license type for using an OS or software on the cloud platform. This parameter is available only if the image you selected is charged.

    -   Use license from the system

        Allows you to use the license provided by the cloud platform. Obtaining the authorization of such a license is charged.

    -   Bring your own licenses \(BYOL\)

        Allows you to use your existing OS license. In such a case, you do not need to apply for a license again.

9.  Set  **Disk**.

    A disk can be a system or data disk. You can add multiple data disks to a BMS and customize the system disk size.

    -   System disk

        If you select a flavor that supports quick provisioning, the system disk is available. You can set the disk type and size as needed.

    -   Data disk

        You can add multiple data disks to a BMS and enable sharing for each data disk.

        -   Currently, BMSs only support SCSI disks.
        -   **Share**: indicates that the EVS disk can be shared. A shared disk can be attached to multiple BMSs simultaneously.

10. Set network parameters, including  **VPC**,  **NIC**, and  **Security Group**.

    When you use VPC for the first time, the system automatically creates a VPC for you, including the security group and NIC. The default subnet segment is 192.168.1.0/24 and the subnet gateway is 192.168.1.1. Dynamic Host Configuration Protocol \(DHCP\) is enabled for the subnet.

    **Table  1**  Network parameters

    <a name="table1150612233101"></a>
    <table><thead align="left"><tr id="row95061923191020"><th class="cellrowborder" valign="top" width="24.05%" id="mcps1.2.3.1.1"><p id="p16507123141019"><a name="p16507123141019"></a><a name="p16507123141019"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="75.94999999999999%" id="mcps1.2.3.1.2"><p id="p1350712236106"><a name="p1350712236106"></a><a name="p1350712236106"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row350718236109"><td class="cellrowborder" valign="top" width="24.05%" headers="mcps1.2.3.1.1 "><p id="p1750722381015"><a name="p1750722381015"></a><a name="p1750722381015"></a>VPC</p>
    </td>
    <td class="cellrowborder" valign="top" width="75.94999999999999%" headers="mcps1.2.3.1.2 "><p id="p5630132955419"><a name="p5630132955419"></a><a name="p5630132955419"></a>You can select an existing VPC or create one.</p>
    </td>
    </tr>
    <tr id="row2507132371017"><td class="cellrowborder" valign="top" width="24.05%" headers="mcps1.2.3.1.1 "><p id="p950782310108"><a name="p950782310108"></a><a name="p950782310108"></a>NIC</p>
    </td>
    <td class="cellrowborder" valign="top" width="75.94999999999999%" headers="mcps1.2.3.1.2 "><p id="p1050716237101"><a name="p1050716237101"></a><a name="p1050716237101"></a>Includes primary and extension NICs. You can add an extension NIC to a BMS and specify an IP address for it (including primary NIC).</p>
    <div class="notice" id="note156851537914"><a name="note156851537914"></a><a name="note156851537914"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><a name="ul15380578550"></a><a name="ul15380578550"></a><ul id="ul15380578550"><li>The active NIC cannot be deleted because it is used to provide the default route.</li><li>If you choose to assign an IP address automatically, do not change the private IP address of the BMS after the BMS is provisioned. Otherwise, the IP address may conflict with that of another BMS.</li><li>If a fixed IP address is assigned to a NIC, you cannot create BMSs in a batch.</li></ul>
    </div></div>
    </td>
    </tr>
    <tr id="row75071323121015"><td class="cellrowborder" valign="top" width="24.05%" headers="mcps1.2.3.1.1 "><p id="p175071230102"><a name="p175071230102"></a><a name="p175071230102"></a>High-Speed NIC</p>
    </td>
    <td class="cellrowborder" valign="top" width="75.94999999999999%" headers="mcps1.2.3.1.2 "><p id="p62071654174520"><a name="p62071654174520"></a><a name="p62071654174520"></a>The high-speed NIC provides high-speed network ports for communication between BMSs. It provides high bandwidth.</p>
    <p id="p176011543525"><a name="p176011543525"></a><a name="p176011543525"></a>You cannot configure the same high-speed network for multiple high-speed NICs of a BMS.</p>
    </td>
    </tr>
    <tr id="row1942223817216"><td class="cellrowborder" valign="top" width="24.05%" headers="mcps1.2.3.1.1 "><p id="p7840171310412"><a name="p7840171310412"></a><a name="p7840171310412"></a>Security Group</p>
    </td>
    <td class="cellrowborder" valign="top" width="75.94999999999999%" headers="mcps1.2.3.1.2 "><p id="p1868012213105"><a name="p1868012213105"></a><a name="p1868012213105"></a>A security group implements access control for BMSs within a security group and between different security groups. You can define different access control rules for a security group, and these rules take effect for all BMSs added to this security group.</p>
    <p id="p14750093614"><a name="p14750093614"></a><a name="p14750093614"></a>When creating a BMS, you can select only one security group. After a BMS is created, you can associate it with multiple security groups. For details, see <a href="changing-a-security-group.md">Changing a Security Group</a>.</p>
    <div class="note" id="note147511915615"><a name="note147511915615"></a><a name="note147511915615"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p157511192611"><a name="p157511192611"></a><a name="p157511192611"></a>Before initializing a BMS, ensure that security group rules in the outbound direction meet the following requirements:</p>
    <a name="ul197511591664"></a><a name="ul197511591664"></a><ul id="ul197511591664"><li>Protocol: TCP</li><li>Port Range: 80</li><li>Remote End: 169.254.0.0/16</li></ul>
    <p id="p10751893615"><a name="p10751893615"></a><a name="p10751893615"></a>If you use the default outbound security group rule, the preceding requirements are met, and the BMS can be initialized. The default outbound security group rule is as follows:</p>
    <a name="ul47511891963"></a><a name="ul47511891963"></a><ul id="ul47511891963"><li>Protocol: Any</li><li>Port Range: Any</li><li>Remote End: 0.0.0.0/16</li></ul>
    </div></div>
    </td>
    </tr>
    <tr id="row950872311018"><td class="cellrowborder" valign="top" width="24.05%" headers="mcps1.2.3.1.1 "><p id="p19508172310103"><a name="p19508172310103"></a><a name="p19508172310103"></a>EIP</p>
    </td>
    <td class="cellrowborder" valign="top" width="75.94999999999999%" headers="mcps1.2.3.1.2 "><p id="p12630162913549"><a name="p12630162913549"></a><a name="p12630162913549"></a>An EIP is a static public IP address bound to a BMS in a VPC. Using the EIP, the BMS provides services externally.</p>
    <p id="p1963018299549"><a name="p1963018299549"></a><a name="p1963018299549"></a>You can select one of the following three options for <strong id="b84235270616623"><a name="b84235270616623"></a><a name="b84235270616623"></a>EIP</strong> as required:</p>
    <a name="ul8445823113211"></a><a name="ul8445823113211"></a><ul id="ul8445823113211"><li><strong id="b84235270618401"><a name="b84235270618401"></a><a name="b84235270618401"></a>Do not use</strong>: The BMS cannot communicate with the Internet and can be used only on a private network for deploying services or used to deploy a cluster.</li><li><strong id="b101737766"><a name="b101737766"></a><a name="b101737766"></a>Automatically assign</strong>: The system automatically assigns an EIP with a dedicated bandwidth to the BMS. The bandwidth is configurable.</li><li><strong id="b692360912"><a name="b692360912"></a><a name="b692360912"></a>Specify</strong>: An existing EIP is assigned to the BMS.</li></ul>
    <div class="note" id="note684184743013"><a name="note684184743013"></a><a name="note684184743013"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p884134712300"><a name="p884134712300"></a><a name="p884134712300"></a>If you select <strong id="b84235270685229"><a name="b84235270685229"></a><a name="b84235270685229"></a>Specify</strong>, you can create only one BMS at a time.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row292761818119"><td class="cellrowborder" valign="top" width="24.05%" headers="mcps1.2.3.1.1 "><p id="p1192716188117"><a name="p1192716188117"></a><a name="p1192716188117"></a>Bandwidth</p>
    </td>
    <td class="cellrowborder" valign="top" width="75.94999999999999%" headers="mcps1.2.3.1.2 "><p id="p11344193821114"><a name="p11344193821114"></a><a name="p11344193821114"></a>This parameter is required when you select <strong id="b7433131944217"><a name="b7433131944217"></a><a name="b7433131944217"></a>Automatically assign</strong> for <strong id="b1043361974213"><a name="b1043361974213"></a><a name="b1043361974213"></a>EIP</strong>.</p>
    <p id="p1492741816118"><a name="p1492741816118"></a><a name="p1492741816118"></a>Specifies the bandwidth size in Mbit/s.</p>
    </td>
    </tr>
    </tbody>
    </table>

11. Set the BMS login mode.

    **Key pair**: A key pair is used for BMS login authentication. You can select an existing key pair, or click  **View Key Pair**  and create one.

    >![](/images/icon-note.gif) **NOTE:**   
    >If you use an existing key pair, ensure that you have saved the key file locally. Otherwise, logging in to the BMS will fail.  

12. \(Optional\) Configure  **Advanced Settings**.

    To use functions listed in  **Advanced Settings**, click  **Configure now**. Otherwise, click  **Do not configure**.

    -   **User Data Injection**  enables the BMS to automatically inject user data when the BMS starts for the first time. After this function is enabled, the BMS automatically injects the user data upon its first startup.

        This parameter is available only when  **Key pair**  is selected for  **Login Mode**. For detailed operations, see  [Injecting User Data into BMSs](injecting-user-data-into-bmss.md).

    -   Tag

        Tags a BMS. This configuration is optional. Adding tags to BMSs helps you better identify and manage your BMSs. You can add up to nine tags to a BMS.

        For detailed operations on tags, see section  [Adding Tags](adding-tags.md).

    -   Agency

        An agency provides BMSs with temporary security credentials for accessing other cloud services. The agency is created by the tenant administrator on the IAM console.

        If you have created an agency in IAM, you can select the agency from the drop-down list and obtain specified operation permissions. Currently, agencies are mainly used for server monitoring. For more information, see  [Installing and Configuring Agent](installing-and-configuring-agent.md).

13. Set  **BMS Name**.

    The name can be customized but can contain only letters, digits, underscores \(\_\), hyphens \(-\), and periods \(.\).

    If you create multiple BMSs at a time, suffixes will be added to the BMSs in sequence, such as  **bms-0001**  and  **bms-0002**. If you create multiple BMSs again, the values in the new BMS names increase from the existing maximum value. For example, the existing BMS with the maximum number in name is  **bms-0010**. If you enter  **bms**, the names of the new BMSs will be  **bms-0011**,  **bms-0012**, .... When the value reaches 9999, it will start from 0001 again.

14. Set your desired number of BMSs, which can be 24 at most.

    After the configuration, click  **Price Calculator**  to view the BMS configuration fee.

    >![](/images/icon-note.gif) **NOTE:**   
    >-   If the quota is sufficient, you can create a maximum of 24 BMSs. If the quota is less than 24, you can create a maximum of all available BMSs.  
    >-   If you manually set an IP address for the user-defined NICs or high-speed NIC, or specify an EIP, you can create only one BMS at a time.  

15. Click  **Allocate Now**.
16. On the displayed page, confirm the specifications and click  **Submit**.

    The BMS status changes to  **Running**  after about 30 minutes. If you select a flavor that supports quick provisioning, you can obtain a BMS in about five minutes.

    >![](/images/icon-note.gif) **NOTE:**   
    >You can view the BMS creation status. For details, see  [Viewing BMS Creation Statuses](viewing-bms-creation-statuses.md).  


## Follow-up Operations<a name="section1138175315355"></a>

-   After the BMS is created, you can view its details, such as name/ID, disks, and private IP address. For details, see  [Viewing BMS Details](viewing-bms-details.md).
-   After logging in to the BMS, you can install software or deploy services as needed. The login mode varies depending on the BMS OS. For details, see  [Linux BMS Login Methods](linux-bms-login-methods.md)  or  [Windows BMS Login Methods](windows-bms-login-methods.md).
-   If you have created data disks when creating the BMS, you must format partitions of the data disks. For details, see  [Introduction to Data Disk Initialization Scenarios and Partition Styles](introduction-to-data-disk-initialization-scenarios-and-partition-styles.md).
-   Change the validity period of the password to prevent any inconvenience caused by password expiration. For detailed operations, see  [How Do I Set the Password Validity Period?](how-do-i-set-the-password-validity-period.md).
-   Some types of BMSs require drivers. For details about how to install drivers, see  [Installing Drivers and Toolkits](installing_drivers_and_toolkits).
-   Currently, Windows Server 2012 BMSs have the same security identifier \(SID\), which is used to identify users, groups, and computer accounts. In cluster deployment scenarios, change the SIDs of BMSs by following the instructions in  [How Do I Change the SID of a Windows Server 2012 BMS?](how-do-i-change-the-sid-of-a-windows-server-2012-bms.md)  to ensure that each BMS has a unique SID.

