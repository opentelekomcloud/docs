# Step 1: Create a BMS<a name="EN-US_TOPIC_0140737434"></a>

## Scenarios<a name="section847213219013"></a>

You can create a BMS on the management console by performing the steps in this section. This section describes how to create a BMS quickly to deploy a web application server. Not all parameters are included. For details about the parameters required for creating a BMS, see  [Creating a BMS](creating-a-bms.md). To create a BMS by calling an API, see  [Creating a BMS](https://docs.otc.t-systems.com/en-us/api/bms/en-us_topic_0053158682.html).

## Procedure<a name="section48261028182215"></a>

1.  Log in to the Cloud Server Console.
2.  In the navigation pane, choose  **Bare Metal Server**.
3.  In the upper right corner, click  **Allocate BMS**.
4.  Configure required parameters.
    -   Specify  **Region**  and  **AZ**. 

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >After the BMS is created, you cannot change the region and AZ.  

    -   Set  **Flavor**.

        Available  [flavors](instance-family.md)  vary depending on the region and AZ you select. Web servers are mainly used for web page access and do not require strong computing capabilities. In addition, only a small amount of storage is required for recording logs. Based on this, select  **physical.h2.large**.

    -   Set  **Image**.

        In this example, select  **Public image**  and  **CentOS 7.4 64bit for BareMetal**.

    -   Set  **License Type**.

        In this example, select  **Use system license**. You need to pay for the license. If you have an OS license, select  **Bring your own license \(BYOL\)**.

    -   Specify  **Disk**.

        Whether EVS disks can be attached to a BMS is determined by the flavor and image you select. 

    -   Set  **VPC**  and  **NIC**.

        When you use cloud services for the first time, the system automatically creates a VPC \(default-vpc\) and a subnet  **default-subnet**  for you. Retain the default values.

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >The system creates a security group for you by default. The default security group rule is to allow all outgoing data packets and restrict incoming data packets. The BMS is protected by the default security group, and the default security group rule only ensures basic communication.  

    -   Set  **EIP**.

        BMSs without an EIP cannot communicate with the Internet and are only used for deploying services in a private network or used in a cluster. In this example, select  **Automatically Assign**  and set  **Bandwidth**.

    -   Set  **Login Mode**.

        Select the key pair created in  [Making Preparations](making-preparations.md)  from the drop-down list and select  **I acknowledge that I have obtained private key file xxx.pem and that without this file I will not be able to log in to my BMS**.

    -   Configure  **Advanced Settings**.

        In this example, select  **Do not configure**.

    -   Set  **BMS Name**.

        The BMS name is in the format bms-_four random digits_. To distinguish BMSs, you can add the function of a BMS to its name, for example,  **bms-7676-nginx**.

    -   Set  **Quantity**.

        In this example, set the value to  **1**.

5.  Click  **Allocate Now**. Confirm the specifications and click  **Submit**.

## Result<a name="section1423814816371"></a>

Click  **Back to the BMS List**. Generally, it takes 5 to 30 minutes for a BMS to be created. Click the refresh button. After the BMS status changes from  **Creating**  to  **Running**, the BMS is created successfully.

## Follow-up Operations<a name="section11418184575513"></a>

A BMS functioning as a web server must allow ICMP traffic on ports 80 and 443. These rules are not configured for the default security group. You need to add the rules after the BMS is created. For details, see  _Virtual Private Cloud User Guide_.

<a name="table16931175453217"></a>
<table><thead align="left"><tr id="row199311654123217"><th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.1"><p id="p593175443218"><a name="p593175443218"></a><a name="p593175443218"></a>Protocol</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.2"><p id="p3931175418326"><a name="p3931175418326"></a><a name="p3931175418326"></a>Direction</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.3"><p id="p15931185417321"><a name="p15931185417321"></a><a name="p15931185417321"></a>Port Range</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.4"><p id="p17931654113219"><a name="p17931654113219"></a><a name="p17931654113219"></a>Source</p>
</th>
</tr>
</thead>
<tbody><tr id="row8607627970"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p1260717271716"><a name="p1260717271716"></a><a name="p1260717271716"></a>TCP</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="p12607527279"><a name="p12607527279"></a><a name="p12607527279"></a>Inbound</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.3 "><p id="p18607112717719"><a name="p18607112717719"></a><a name="p18607112717719"></a>80</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.4 "><p id="p0607122711712"><a name="p0607122711712"></a><a name="p0607122711712"></a>0.0.0.0/0</p>
</td>
</tr>
<tr id="row5607142710713"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p660716277718"><a name="p660716277718"></a><a name="p660716277718"></a>TCP</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="p36072270718"><a name="p36072270718"></a><a name="p36072270718"></a>Inbound</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.3 "><p id="p960713271377"><a name="p960713271377"></a><a name="p960713271377"></a>443</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.4 "><p id="p186088271970"><a name="p186088271970"></a><a name="p186088271970"></a>0.0.0.0/0</p>
</td>
</tr>
<tr id="row3931354103218"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p10931205413321"><a name="p10931205413321"></a><a name="p10931205413321"></a>ICMP</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="p15931175403219"><a name="p15931175403219"></a><a name="p15931175403219"></a>Inbound</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.3 "><p id="p093195483219"><a name="p093195483219"></a><a name="p093195483219"></a>All</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.4 "><p id="p15931175493216"><a name="p15931175493216"></a><a name="p15931175493216"></a>0.0.0.0/0</p>
</td>
</tr>
</tbody>
</table>

