# Creating a VPN<a name="en-us_topic_0060118606"></a>

## **Overview**<a name="en-us_topic_0013748707_section55639012123559"></a>

By default, ECSs in a VPC cannot communicate with your data center or private network. To enable communication between them, use a VPN. You need to create a VPN in your VPC and update the security group rules.

## Description of a Simple IPsec VPN Intranet Topology<a name="en-us_topic_0013748707_section46486636123559"></a>

In  [Figure 1](#fig19884520114220), a VPC has two subnets: 192.168.1.0/24 and 192.168.2.0/24. On your router deployed in your physical data center, you also have two subnets: 192.168.3.0/24 and 192.168.4.0/24. You can create a VPN to enable subnets in your VPC to communicate with those in your data center.

**Figure  1**  IPsec VPN<a name="fig19884520114220"></a>  
![](figures/ipsec-vpn-1.png "ipsec-vpn-1")

Currently, the site-to-site VPN and hub-spoke VPN are supported. You need to set up VPNs in both your data center and the VPC to establish the VPN connection.

Ensure that the VPN in your VPC and that in your data center use the same Internet Key Exchange \(IKE\) and IPsec policy configurations. Before creating a VPN, familiarize yourself with the protocols described in  [Table 1](#en-us_topic_0013748707_table1573616693718)  and ensure that your device meets the requirements and configuration constraints of the involved protocols.

**Table  1**  Involved protocols

<a name="en-us_topic_0013748707_table1573616693718"></a>
<table><thead align="left"><tr id="en-us_topic_0013748707_row580761493718"><th class="cellrowborder" valign="top" width="16.16%" id="mcps1.2.4.1.1"><p id="en-us_topic_0013748707_p65469593718"><a name="en-us_topic_0013748707_p65469593718"></a><a name="en-us_topic_0013748707_p65469593718"></a><strong id="b842352706184931"><a name="b842352706184931"></a><a name="b842352706184931"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="48.980000000000004%" id="mcps1.2.4.1.2"><p id="en-us_topic_0013748707_p5303029693718"><a name="en-us_topic_0013748707_p5303029693718"></a><a name="en-us_topic_0013748707_p5303029693718"></a><strong id="b842352706191717"><a name="b842352706191717"></a><a name="b842352706191717"></a>Description</strong></p>
</th>
<th class="cellrowborder" valign="top" width="34.86%" id="mcps1.2.4.1.3"><p id="en-us_topic_0013748707_p48671493718"><a name="en-us_topic_0013748707_p48671493718"></a><a name="en-us_topic_0013748707_p48671493718"></a><strong id="b84235270617755"><a name="b84235270617755"></a><a name="b84235270617755"></a>Constraint</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0013748707_row3942386093718"><td class="cellrowborder" valign="top" width="16.16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0013748707_p3921611193718"><a name="en-us_topic_0013748707_p3921611193718"></a><a name="en-us_topic_0013748707_p3921611193718"></a>RFC 2409</p>
</td>
<td class="cellrowborder" valign="top" width="48.980000000000004%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0013748707_p16932393718"><a name="en-us_topic_0013748707_p16932393718"></a><a name="en-us_topic_0013748707_p16932393718"></a>Defines the IKE protocol, which negotiates and verifies key information to safeguard VPNs.</p>
</td>
<td class="cellrowborder" valign="top" width="34.86%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0013748707_ul2936692693858"></a><a name="en-us_topic_0013748707_ul2936692693858"></a><ul id="en-us_topic_0013748707_ul2936692693858"><li>Use the pre-shared key (PSK) to reach an IKE peer agreement.</li><li>Use the main mode and aggressive mode for negotiation.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0013748707_row3718926293718"><td class="cellrowborder" valign="top" width="16.16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0013748707_p5954022693718"><a name="en-us_topic_0013748707_p5954022693718"></a><a name="en-us_topic_0013748707_p5954022693718"></a>RFC 4301</p>
</td>
<td class="cellrowborder" valign="top" width="48.980000000000004%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0013748707_p5249890793718"><a name="en-us_topic_0013748707_p5249890793718"></a><a name="en-us_topic_0013748707_p5249890793718"></a>Defines the IPsec architecture, the security services that IPsec offers, and the collaboration between components.</p>
</td>
<td class="cellrowborder" valign="top" width="34.86%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0013748707_p2455308193718"><a name="en-us_topic_0013748707_p2455308193718"></a><a name="en-us_topic_0013748707_p2455308193718"></a>Use the IPsec tunnel to set up a VPN connection.</p>
</td>
</tr>
</tbody>
</table>

## **Scenarios**<a name="en-us_topic_0013748707_section50291515214628"></a>

Perform the following procedure to create a VPN that sets up a secure, isolated communication tunnel between your data center and cloud services. 

## **Procedure**<a name="en-us_topic_0013748707_section272021120388"></a>

1.  Log in to the management console.
2.  Click  ![](figures/d00356819-云计算开发部-公有云_iaas-image-f1cac6ef-c4f7-462b-a7f1-85e988937e64-2.png)  in the upper left corner and select the desired region and project.
3.  On the console homepage, under  **Network**, click  **Virtual Private Network**.
4.  On the  **Virtual Private Network**  page, click  **Create VPN**.
5.  Set the parameters as prompted and click  **Create Now**.

    **Figure  2**  Creating a VPN<a name="fig12119136431"></a>  
    ![](figures/creating-a-vpn.png "creating-a-vpn")

    **Table  2**  Basic parameters

    <a name="en-us_topic_0013748707_table968099720388"></a>
    <table><thead align="left"><tr id="en-us_topic_0013748707_row5614613420388"><th class="cellrowborder" valign="top" width="25.510000000000005%" id="mcps1.2.4.1.1"><p id="en-us_topic_0013748707_p4208626520388"><a name="en-us_topic_0013748707_p4208626520388"></a><a name="en-us_topic_0013748707_p4208626520388"></a><strong id="b517364668"><a name="b517364668"></a><a name="b517364668"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="45.940000000000005%" id="mcps1.2.4.1.2"><p id="en-us_topic_0013748707_p5354426720388"><a name="en-us_topic_0013748707_p5354426720388"></a><a name="en-us_topic_0013748707_p5354426720388"></a><strong id="b836315532"><a name="b836315532"></a><a name="b836315532"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.550000000000004%" id="mcps1.2.4.1.3"><p id="en-us_topic_0013748707_p4211838620388"><a name="en-us_topic_0013748707_p4211838620388"></a><a name="en-us_topic_0013748707_p4211838620388"></a><strong id="b842352706184940"><a name="b842352706184940"></a><a name="b842352706184940"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row15623741164413"><td class="cellrowborder" valign="top" width="25.510000000000005%" headers="mcps1.2.4.1.1 "><p id="p3624241174411"><a name="p3624241174411"></a><a name="p3624241174411"></a>Region</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.940000000000005%" headers="mcps1.2.4.1.2 "><p id="p662414413442"><a name="p662414413442"></a><a name="p662414413442"></a>Specifies the desired region. Regions are geographic areas isolated from each other. Resources are region-specific and cannot be used across regions through internal network connections. For low network latency and quick resource access, select the nearest region.</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.550000000000004%" headers="mcps1.2.4.1.3 "><p id="p1062412415444"><a name="p1062412415444"></a><a name="p1062412415444"></a>eu-de</p>
    </td>
    </tr>
    <tr id="row117220913414"><td class="cellrowborder" valign="top" width="25.510000000000005%" headers="mcps1.2.4.1.1 "><p id="p15458115174110"><a name="p15458115174110"></a><a name="p15458115174110"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.940000000000005%" headers="mcps1.2.4.1.2 "><p id="p1845801518415"><a name="p1845801518415"></a><a name="p1845801518415"></a>Specifies the VPN name.</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.550000000000004%" headers="mcps1.2.4.1.3 "><p id="p114591915154110"><a name="p114591915154110"></a><a name="p114591915154110"></a>VPN-001</p>
    </td>
    </tr>
    <tr id="en-us_topic_0013748707_row11610186223633"><td class="cellrowborder" valign="top" width="25.510000000000005%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0013748707_p37382811223633"><a name="en-us_topic_0013748707_p37382811223633"></a><a name="en-us_topic_0013748707_p37382811223633"></a>VPC</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.940000000000005%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0013748707_p8108833223633"><a name="en-us_topic_0013748707_p8108833223633"></a><a name="en-us_topic_0013748707_p8108833223633"></a>Specifies the VPC name.</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.550000000000004%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0013748707_p52835773223633"><a name="en-us_topic_0013748707_p52835773223633"></a><a name="en-us_topic_0013748707_p52835773223633"></a>VPC-001</p>
    </td>
    </tr>
    <tr id="row39921327164317"><td class="cellrowborder" valign="top" width="25.510000000000005%" headers="mcps1.2.4.1.1 "><p id="p2014819297435"><a name="p2014819297435"></a><a name="p2014819297435"></a>Local Subnet</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.940000000000005%" headers="mcps1.2.4.1.2 "><p id="p1714982934316"><a name="p1714982934316"></a><a name="p1714982934316"></a>A local subnet is a VPC subnet that accesses a customer network through a VPN.</p>
    <a name="ul714914296431"></a><a name="ul714914296431"></a><ul id="ul714914296431"><li><strong id="b18715105117014"><a name="b18715105117014"></a><a name="b18715105117014"></a>Select subnet</strong>: If you select this option, you can then select the subnets that need to communicate with your data center.</li><li><strong id="b814012376212"><a name="b814012376212"></a><a name="b814012376212"></a>Specify CIDR block</strong>: If you select this option, you can then enter the CIDR blocks that need to communicate with your data center.</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="28.550000000000004%" headers="mcps1.2.4.1.3 "><p id="p61491129184311"><a name="p61491129184311"></a><a name="p61491129184311"></a>192.168.1.0/24,</p>
    <p id="p31491229164316"><a name="p31491229164316"></a><a name="p31491229164316"></a>192.168.2.0/24</p>
    </td>
    </tr>
    <tr id="row925613201443"><td class="cellrowborder" valign="top" width="25.510000000000005%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0013748707_p4476936120388"><a name="en-us_topic_0013748707_p4476936120388"></a><a name="en-us_topic_0013748707_p4476936120388"></a>Remote Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.940000000000005%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0013748707_p243961520388"><a name="en-us_topic_0013748707_p243961520388"></a><a name="en-us_topic_0013748707_p243961520388"></a>Specifies the public IP address of the VPN in your data center or on the private network. This IP address is used for communicating with the VPN in the VPC.</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.550000000000004%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0013748707_p6339113020388"><a name="en-us_topic_0013748707_p6339113020388"></a><a name="en-us_topic_0013748707_p6339113020388"></a>N/A</p>
    </td>
    </tr>
    <tr id="row19256102084416"><td class="cellrowborder" valign="top" width="25.510000000000005%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0013748707_p4123547620388"><a name="en-us_topic_0013748707_p4123547620388"></a><a name="en-us_topic_0013748707_p4123547620388"></a>Remote Subnet</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.940000000000005%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0013748707_p5173922920388"><a name="en-us_topic_0013748707_p5173922920388"></a><a name="en-us_topic_0013748707_p5173922920388"></a>A remote subnet is a subnet in the customer data center that accesses a VPC through a VPN. The remote and local subnets cannot have overlapping or matching CIDR blocks. The remote subnet CIDR block cannot overlap with CIDR blocks involved in existing VPC peering connections created for the local VPC.</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.550000000000004%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0013748707_p3012798220388"><a name="en-us_topic_0013748707_p3012798220388"></a><a name="en-us_topic_0013748707_p3012798220388"></a>192.168.3.0/24,</p>
    <p id="en-us_topic_0013748707_p271638520388"><a name="en-us_topic_0013748707_p271638520388"></a><a name="en-us_topic_0013748707_p271638520388"></a>192.168.4.0/24</p>
    </td>
    </tr>
    <tr id="en-us_topic_0013748707_row497437320388"><td class="cellrowborder" valign="top" width="25.510000000000005%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0013748707_p4969878720388"><a name="en-us_topic_0013748707_p4969878720388"></a><a name="en-us_topic_0013748707_p4969878720388"></a>PSK</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.940000000000005%" headers="mcps1.2.4.1.2 "><p id="p141362143116"><a name="p141362143116"></a><a name="p141362143116"></a>Specifies the pre-shared key, which is a private key shared by two ends of a VPN connection. The PSK configurations for both ends of a VPN connection must be the same. This key is used for VPN connection negotiation.</p>
    <p id="p913952383511"><a name="p913952383511"></a><a name="p913952383511"></a>The value is a string of 6 to 128 characters.</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.550000000000004%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0013748707_p5888523120388"><a name="en-us_topic_0013748707_p5888523120388"></a><a name="en-us_topic_0013748707_p5888523120388"></a>Test@123</p>
    </td>
    </tr>
    <tr id="en-us_topic_0013748707_row62355196223836"><td class="cellrowborder" valign="top" width="25.510000000000005%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0013748707_p24325852223836"><a name="en-us_topic_0013748707_p24325852223836"></a><a name="en-us_topic_0013748707_p24325852223836"></a>Confirm PSK</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.940000000000005%" headers="mcps1.2.4.1.2 "><p id="p2140323163515"><a name="p2140323163515"></a><a name="p2140323163515"></a>Specifies the confirm pre-shared key.</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.550000000000004%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0013748707_p17040185223836"><a name="en-us_topic_0013748707_p17040185223836"></a><a name="en-us_topic_0013748707_p17040185223836"></a>Test@123</p>
    </td>
    </tr>
    <tr id="en-us_topic_0013748707_row1270712483340"><td class="cellrowborder" valign="top" width="25.510000000000005%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0013748707_en-us_topic_0030971658_en-us_topic_0013935842_p42735861211138"><a name="en-us_topic_0013748707_en-us_topic_0030971658_en-us_topic_0013935842_p42735861211138"></a><a name="en-us_topic_0013748707_en-us_topic_0030971658_en-us_topic_0013935842_p42735861211138"></a>Tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.940000000000005%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0013748707_en-us_topic_0030971658_en-us_topic_0013935842_p20140951169"><a name="en-us_topic_0013748707_en-us_topic_0030971658_en-us_topic_0013935842_p20140951169"></a><a name="en-us_topic_0013748707_en-us_topic_0030971658_en-us_topic_0013935842_p20140951169"></a>Specifies the VPN tag, which consists of a key and value pair. You can add a maximum of ten tags to each VPN.</p>
    <p id="en-us_topic_0013748707_en-us_topic_0030971658_en-us_topic_0013935842_p39052702211138"><a name="en-us_topic_0013748707_en-us_topic_0030971658_en-us_topic_0013935842_p39052702211138"></a><a name="en-us_topic_0013748707_en-us_topic_0030971658_en-us_topic_0013935842_p39052702211138"></a>The tag key and value must meet the requirements listed in <a href="#en-us_topic_0013748707_en-us_topic_0013935842_table248245914136">Table 3</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.550000000000004%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0013748707_en-us_topic_0030971658_en-us_topic_0013935842_ul122375031712"></a><a name="en-us_topic_0013748707_en-us_topic_0030971658_en-us_topic_0013935842_ul122375031712"></a><ul id="en-us_topic_0013748707_en-us_topic_0030971658_en-us_topic_0013935842_ul122375031712"><li>Key: vpn_key1</li><li>Value: vpn-01</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0013748707_row1322495315453"><td class="cellrowborder" valign="top" width="25.510000000000005%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0013748707_p8564815114611"><a name="en-us_topic_0013748707_p8564815114611"></a><a name="en-us_topic_0013748707_p8564815114611"></a>Advanced Settings</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.940000000000005%" headers="mcps1.2.4.1.2 "><a name="en-us_topic_0013748707_ul657461594613"></a><a name="en-us_topic_0013748707_ul657461594613"></a><ul id="en-us_topic_0013748707_ul657461594613"><li><strong id="b842352706153531"><a name="b842352706153531"></a><a name="b842352706153531"></a>Default</strong>: uses default IKE and IPsec policies.</li><li><strong id="b842352706151151"><a name="b842352706151151"></a><a name="b842352706151151"></a>Existing</strong>: uses existing IKE and IPsec policies. This option is available only after you have created IKE and IPsec policies.</li><li><strong id="b84235270615367"><a name="b84235270615367"></a><a name="b84235270615367"></a>Custom</strong>: uses custom IKE and IPsec policies. For details about the policies, see <a href="#en-us_topic_0013748707_table505541520388">Table 4</a> and <a href="#en-us_topic_0013748707_table4625367220388">Table 5</a>.</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="28.550000000000004%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0013748707_p145981515104620"><a name="en-us_topic_0013748707_p145981515104620"></a><a name="en-us_topic_0013748707_p145981515104620"></a>Custom</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  VPN tag key and value requirements

    <a name="en-us_topic_0013748707_en-us_topic_0013935842_table248245914136"></a>
    <table><thead align="left"><tr id="en-us_topic_0013748707_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_row2997812223119"><th class="cellrowborder" valign="top" width="18.54%" id="mcps1.2.4.1.1"><p id="en-us_topic_0013748707_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_p4367076523119"><a name="en-us_topic_0013748707_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_p4367076523119"></a><a name="en-us_topic_0013748707_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_p4367076523119"></a><strong id="b1484127105"><a name="b1484127105"></a><a name="b1484127105"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.39%" id="mcps1.2.4.1.2"><p id="en-us_topic_0013748707_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_p4767111023119"><a name="en-us_topic_0013748707_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_p4767111023119"></a><a name="en-us_topic_0013748707_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_p4767111023119"></a><strong id="b842352706171418"><a name="b842352706171418"></a><a name="b842352706171418"></a>Requirement</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.07%" id="mcps1.2.4.1.3"><p id="en-us_topic_0013748707_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_p3615470723119"><a name="en-us_topic_0013748707_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_p3615470723119"></a><a name="en-us_topic_0013748707_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_p3615470723119"></a><strong id="b84235270610336"><a name="b84235270610336"></a><a name="b84235270610336"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0013748707_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_row5695691323119"><td class="cellrowborder" valign="top" width="18.54%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0013748707_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_p5010724023119"><a name="en-us_topic_0013748707_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_p5010724023119"></a><a name="en-us_topic_0013748707_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_p5010724023119"></a>Key</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.39%" headers="mcps1.2.4.1.2 "><a name="ub2cf5f68e02742d49e3f8d80289eab77"></a><a name="ub2cf5f68e02742d49e3f8d80289eab77"></a><ul id="ub2cf5f68e02742d49e3f8d80289eab77"><li>Cannot be left blank.</li><li>Must be unique for the same VPN and can be the same for different VPNs.</li><li>Contains a maximum of 36 characters.</li><li>Can contain only the following character types:<a name="uccb317c6616b4445aa84b125e5aa017f"></a><a name="uccb317c6616b4445aa84b125e5aa017f"></a><ul id="uccb317c6616b4445aa84b125e5aa017f"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
    </li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="28.07%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0013748707_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_p5438834323119"><a name="en-us_topic_0013748707_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_p5438834323119"></a><a name="en-us_topic_0013748707_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_p5438834323119"></a>vpn_key1</p>
    </td>
    </tr>
    <tr id="en-us_topic_0013748707_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_row1973304523119"><td class="cellrowborder" valign="top" width="18.54%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0013748707_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_p5487280123119"><a name="en-us_topic_0013748707_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_p5487280123119"></a><a name="en-us_topic_0013748707_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_p5487280123119"></a>Value</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.39%" headers="mcps1.2.4.1.2 "><a name="u463eb9034f3d456b81073b15ba62f102"></a><a name="u463eb9034f3d456b81073b15ba62f102"></a><ul id="u463eb9034f3d456b81073b15ba62f102"><li>Can contain a maximum of 43 characters.</li><li>Can contain only the following character types:<a name="ub74c759faad544c3b4428accc9c42b80"></a><a name="ub74c759faad544c3b4428accc9c42b80"></a><ul id="ub74c759faad544c3b4428accc9c42b80"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
    </li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="28.07%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0013748707_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_p4850087723119"><a name="en-us_topic_0013748707_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_p4850087723119"></a><a name="en-us_topic_0013748707_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_p4850087723119"></a>vpn-01</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  IKE policy

    <a name="en-us_topic_0013748707_table505541520388"></a>
    <table><thead align="left"><tr id="en-us_topic_0013748707_row4594157720388"><th class="cellrowborder" valign="top" width="28.07%" id="mcps1.2.4.1.1"><p id="en-us_topic_0013748707_p1992624420388"><a name="en-us_topic_0013748707_p1992624420388"></a><a name="en-us_topic_0013748707_p1992624420388"></a><strong id="b2105239613"><a name="b2105239613"></a><a name="b2105239613"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="55.169999999999995%" id="mcps1.2.4.1.2"><p id="en-us_topic_0013748707_p341307620388"><a name="en-us_topic_0013748707_p341307620388"></a><a name="en-us_topic_0013748707_p341307620388"></a><strong id="b1244849777"><a name="b1244849777"></a><a name="b1244849777"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.76%" id="mcps1.2.4.1.3"><p id="en-us_topic_0013748707_p802372020388"><a name="en-us_topic_0013748707_p802372020388"></a><a name="en-us_topic_0013748707_p802372020388"></a><strong id="b1935699262"><a name="b1935699262"></a><a name="b1935699262"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0013748707_row29141197225437"><td class="cellrowborder" valign="top" width="28.07%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0013748707_p31419233225456"><a name="en-us_topic_0013748707_p31419233225456"></a><a name="en-us_topic_0013748707_p31419233225456"></a>Authentication Algorithm</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.169999999999995%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0013748707_p61929926225456"><a name="en-us_topic_0013748707_p61929926225456"></a><a name="en-us_topic_0013748707_p61929926225456"></a>Specifies the authentication hash algorithm. The value can be <strong id="b10432515105713"><a name="b10432515105713"></a><a name="b10432515105713"></a>SHA1</strong>, <strong id="b343251585711"><a name="b343251585711"></a><a name="b343251585711"></a>SHA2-256</strong>, <strong id="b114341015185717"><a name="b114341015185717"></a><a name="b114341015185717"></a>SHA2-384</strong>, <strong id="b1743461565715"><a name="b1743461565715"></a><a name="b1743461565715"></a>SHA2-512</strong>, or <strong id="b1843461565719"><a name="b1843461565719"></a><a name="b1843461565719"></a>MD5</strong>.</p>
    <p id="en-us_topic_0013748707_p15463274192621"><a name="en-us_topic_0013748707_p15463274192621"></a><a name="en-us_topic_0013748707_p15463274192621"></a>The default value is <strong id="b1810618354577"><a name="b1810618354577"></a><a name="b1810618354577"></a>SHA1</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.76%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0013748707_p50268124225456"><a name="en-us_topic_0013748707_p50268124225456"></a><a name="en-us_topic_0013748707_p50268124225456"></a>SHA1</p>
    </td>
    </tr>
    <tr id="en-us_topic_0013748707_row6462784820388"><td class="cellrowborder" valign="top" width="28.07%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0013748707_p4707473420388"><a name="en-us_topic_0013748707_p4707473420388"></a><a name="en-us_topic_0013748707_p4707473420388"></a>Encryption Algorithm</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.169999999999995%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0013748707_p5495708620388"><a name="en-us_topic_0013748707_p5495708620388"></a><a name="en-us_topic_0013748707_p5495708620388"></a>Specifies the encryption algorithm. The value can be <strong id="b164081443205716"><a name="b164081443205716"></a><a name="b164081443205716"></a>AES-128</strong>, <strong id="b84081643125719"><a name="b84081643125719"></a><a name="b84081643125719"></a>AES-192</strong>, <strong id="b15409174312576"><a name="b15409174312576"></a><a name="b15409174312576"></a>AES-256</strong>, or <strong id="b54116437574"><a name="b54116437574"></a><a name="b54116437574"></a>3DES</strong>. The 3DES algorithm is not recommended because it is risky.</p>
    <p id="en-us_topic_0013748707_p49866280192648"><a name="en-us_topic_0013748707_p49866280192648"></a><a name="en-us_topic_0013748707_p49866280192648"></a>The default value is <strong id="b1614814583574"><a name="b1614814583574"></a><a name="b1614814583574"></a>AES-128</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.76%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0013748707_p2233899120388"><a name="en-us_topic_0013748707_p2233899120388"></a><a name="en-us_topic_0013748707_p2233899120388"></a>AES-128</p>
    </td>
    </tr>
    <tr id="en-us_topic_0013748707_row4089666520388"><td class="cellrowborder" valign="top" width="28.07%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0013748707_p4477972820388"><a name="en-us_topic_0013748707_p4477972820388"></a><a name="en-us_topic_0013748707_p4477972820388"></a>DH Algorithm</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.169999999999995%" headers="mcps1.2.4.1.2 "><p id="p1232161818316"><a name="p1232161818316"></a><a name="p1232161818316"></a>Specifies the Diffie-Hellman key exchange algorithm. The value can be <strong id="b135722486582"><a name="b135722486582"></a><a name="b135722486582"></a>Group 1</strong>, <strong id="b161675914587"><a name="b161675914587"></a><a name="b161675914587"></a>Group 2</strong>, <strong id="b151491911597"><a name="b151491911597"></a><a name="b151491911597"></a>Group 5</strong>, <strong id="b1514342113597"><a name="b1514342113597"></a><a name="b1514342113597"></a>Group 14</strong>, <strong id="b72419342599"><a name="b72419342599"></a><a name="b72419342599"></a>Group 15</strong>, <strong id="b1641144515912"><a name="b1641144515912"></a><a name="b1641144515912"></a>Group 16</strong>, <strong id="b15115656125918"><a name="b15115656125918"></a><a name="b15115656125918"></a>Group 19</strong>, <strong id="b10760166302"><a name="b10760166302"></a><a name="b10760166302"></a>Group 20</strong>, or <strong id="b84231019803"><a name="b84231019803"></a><a name="b84231019803"></a>Group 21</strong>.</p>
    <p id="p12384121215456"><a name="p12384121215456"></a><a name="p12384121215456"></a>The DH group security level from the highest to lowest is as follows: Group 21 &gt; Group 20 &gt; Group 19 &gt; Group 16 &gt; Group 15 &gt; Group 14 &gt; Group 5 &gt; Group 2 &gt; Group 1.</p>
    <p id="en-us_topic_0013748707_p32611406193039"><a name="en-us_topic_0013748707_p32611406193039"></a><a name="en-us_topic_0013748707_p32611406193039"></a>The default value is <strong id="b1482215401335"><a name="b1482215401335"></a><a name="b1482215401335"></a>Group 5</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.76%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0013748707_p6429974320388"><a name="en-us_topic_0013748707_p6429974320388"></a><a name="en-us_topic_0013748707_p6429974320388"></a>Group 5</p>
    </td>
    </tr>
    <tr id="en-us_topic_0013748707_row4186074420388"><td class="cellrowborder" valign="top" width="28.07%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0013748707_p3252566720388"><a name="en-us_topic_0013748707_p3252566720388"></a><a name="en-us_topic_0013748707_p3252566720388"></a>Version</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.169999999999995%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0013748707_p1733337520388"><a name="en-us_topic_0013748707_p1733337520388"></a><a name="en-us_topic_0013748707_p1733337520388"></a>Specifies the version of the IKE protocol. The value can be <strong id="b842352706145820"><a name="b842352706145820"></a><a name="b842352706145820"></a>v1</strong> or <strong id="b842352706145823"><a name="b842352706145823"></a><a name="b842352706145823"></a>v2</strong>.</p>
    <p id="en-us_topic_0013748707_p8012213193059"><a name="en-us_topic_0013748707_p8012213193059"></a><a name="en-us_topic_0013748707_p8012213193059"></a>The default value is <strong id="b84235270613487"><a name="b84235270613487"></a><a name="b84235270613487"></a>v1</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.76%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0013748707_p6182613120388"><a name="en-us_topic_0013748707_p6182613120388"></a><a name="en-us_topic_0013748707_p6182613120388"></a>v1</p>
    </td>
    </tr>
    <tr id="en-us_topic_0013748707_row4474617720388"><td class="cellrowborder" valign="top" width="28.07%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0013748707_p4120238220388"><a name="en-us_topic_0013748707_p4120238220388"></a><a name="en-us_topic_0013748707_p4120238220388"></a>Lifecycle (s)</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.169999999999995%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0013748707_p4905867920388"><a name="en-us_topic_0013748707_p4905867920388"></a><a name="en-us_topic_0013748707_p4905867920388"></a>Specifies the lifetime of the security association (SA), in seconds.</p>
    <p id="en-us_topic_0013748707_p3887493220388"><a name="en-us_topic_0013748707_p3887493220388"></a><a name="en-us_topic_0013748707_p3887493220388"></a>The SA will be renegotiated if its lifetime expires.</p>
    <p id="en-us_topic_0013748707_p13790324193132"><a name="en-us_topic_0013748707_p13790324193132"></a><a name="en-us_topic_0013748707_p13790324193132"></a>The default value is <strong id="b70025824"><a name="b70025824"></a><a name="b70025824"></a>86400</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.76%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0013748707_p6186175420388"><a name="en-us_topic_0013748707_p6186175420388"></a><a name="en-us_topic_0013748707_p6186175420388"></a>86400</p>
    </td>
    </tr>
    <tr id="en-us_topic_0013748707_row1641723314617"><td class="cellrowborder" valign="top" width="28.07%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0013748707_p144171133134614"><a name="en-us_topic_0013748707_p144171133134614"></a><a name="en-us_topic_0013748707_p144171133134614"></a>Negotiation Mode</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.169999999999995%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0013748707_p4417203315468"><a name="en-us_topic_0013748707_p4417203315468"></a><a name="en-us_topic_0013748707_p4417203315468"></a>If the IKE policy version is <strong id="b66730370367"><a name="b66730370367"></a><a name="b66730370367"></a>v1</strong>, the negotiation mode can be configured. The value can only be <strong id="b367443715364"><a name="b367443715364"></a><a name="b367443715364"></a>Main</strong>.</p>
    <p id="en-us_topic_0013748707_p5950183912308"><a name="en-us_topic_0013748707_p5950183912308"></a><a name="en-us_topic_0013748707_p5950183912308"></a>The default value is <strong id="b98256551314"><a name="b98256551314"></a><a name="b98256551314"></a>Main</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.76%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0013748707_p1041723318465"><a name="en-us_topic_0013748707_p1041723318465"></a><a name="en-us_topic_0013748707_p1041723318465"></a>Main</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5**  IPsec policy

    <a name="en-us_topic_0013748707_table4625367220388"></a>
    <table><thead align="left"><tr id="en-us_topic_0013748707_row2378492720388"><th class="cellrowborder" valign="top" width="32.65%" id="mcps1.2.4.1.1"><p id="en-us_topic_0013748707_p1698445020388"><a name="en-us_topic_0013748707_p1698445020388"></a><a name="en-us_topic_0013748707_p1698445020388"></a><strong id="b1073777526"><a name="b1073777526"></a><a name="b1073777526"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.4%" id="mcps1.2.4.1.2"><p id="en-us_topic_0013748707_p3356317120388"><a name="en-us_topic_0013748707_p3356317120388"></a><a name="en-us_topic_0013748707_p3356317120388"></a><strong id="b1485229029"><a name="b1485229029"></a><a name="b1485229029"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.950000000000003%" id="mcps1.2.4.1.3"><p id="en-us_topic_0013748707_p3426232520388"><a name="en-us_topic_0013748707_p3426232520388"></a><a name="en-us_topic_0013748707_p3426232520388"></a><strong id="b114458899"><a name="b114458899"></a><a name="b114458899"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0013748707_row23039761225648"><td class="cellrowborder" valign="top" width="32.65%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0013748707_p26665535225653"><a name="en-us_topic_0013748707_p26665535225653"></a><a name="en-us_topic_0013748707_p26665535225653"></a>Authentication Algorithm</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.4%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0013748707_p12424687225653"><a name="en-us_topic_0013748707_p12424687225653"></a><a name="en-us_topic_0013748707_p12424687225653"></a>Specifies the authentication hash algorithm. The value can be <strong id="b382515712315"><a name="b382515712315"></a><a name="b382515712315"></a>SHA1</strong>, <strong id="b1082565710311"><a name="b1082565710311"></a><a name="b1082565710311"></a>SHA2-256</strong>, <strong id="b198261557338"><a name="b198261557338"></a><a name="b198261557338"></a>SHA2-384</strong>, <strong id="b178271657236"><a name="b178271657236"></a><a name="b178271657236"></a>SHA2-512</strong>, or <strong id="b382718576313"><a name="b382718576313"></a><a name="b382718576313"></a>MD5</strong>.</p>
    <p id="en-us_topic_0013748707_p5677327619325"><a name="en-us_topic_0013748707_p5677327619325"></a><a name="en-us_topic_0013748707_p5677327619325"></a>The default value is <strong id="b41811147417"><a name="b41811147417"></a><a name="b41811147417"></a>SHA1</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.950000000000003%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0013748707_p66875563225653"><a name="en-us_topic_0013748707_p66875563225653"></a><a name="en-us_topic_0013748707_p66875563225653"></a>SHA1</p>
    </td>
    </tr>
    <tr id="en-us_topic_0013748707_row2352845920388"><td class="cellrowborder" valign="top" width="32.65%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0013748707_p2116763320388"><a name="en-us_topic_0013748707_p2116763320388"></a><a name="en-us_topic_0013748707_p2116763320388"></a>Encryption Algorithm</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.4%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0013748707_p3685669320388"><a name="en-us_topic_0013748707_p3685669320388"></a><a name="en-us_topic_0013748707_p3685669320388"></a>Specifies the encryption algorithm. The value can be <strong id="b610181615411"><a name="b610181615411"></a><a name="b610181615411"></a>AES-128</strong>, <strong id="b410310169410"><a name="b410310169410"></a><a name="b410310169410"></a>AES-192</strong>, <strong id="b18103101617414"><a name="b18103101617414"></a><a name="b18103101617414"></a>AES-256</strong>, or <strong id="b8103616742"><a name="b8103616742"></a><a name="b8103616742"></a>3DES</strong>. The 3DES algorithm is not recommended because it is risky.</p>
    <p id="en-us_topic_0013748707_p40843636193223"><a name="en-us_topic_0013748707_p40843636193223"></a><a name="en-us_topic_0013748707_p40843636193223"></a>The default value is <strong id="b273202318412"><a name="b273202318412"></a><a name="b273202318412"></a>AES-128</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.950000000000003%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0013748707_p3260215020388"><a name="en-us_topic_0013748707_p3260215020388"></a><a name="en-us_topic_0013748707_p3260215020388"></a>AES-128</p>
    </td>
    </tr>
    <tr id="en-us_topic_0013748707_row3039582720388"><td class="cellrowborder" valign="top" width="32.65%" headers="mcps1.2.4.1.1 "><p id="p1557114392400"><a name="p1557114392400"></a><a name="p1557114392400"></a>PFS</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.4%" headers="mcps1.2.4.1.2 "><p id="p123601755192211"><a name="p123601755192211"></a><a name="p123601755192211"></a>Specifies the perfect forward secrecy (PFS), which is used to configure the IPsec tunnel negotiation.</p>
    <p id="p5754151010215"><a name="p5754151010215"></a><a name="p5754151010215"></a>This function enables two parties to exchange the DH keys during the phase-two negotiation, improving key security. It is recommended that you enable this function.</p>
    <p id="p195246466218"><a name="p195246466218"></a><a name="p195246466218"></a>You can disable this function by selecting <strong id="b926402254317"><a name="b926402254317"></a><a name="b926402254317"></a>Disable</strong> from the drop-down list.</p>
    <p id="p1938514498214"><a name="p1938514498214"></a><a name="p1938514498214"></a>The PFS used at the two sides of a VPN must be the same. Otherwise, the negotiation will fail. If you disable this function on the console, you also need to disable it at the customer side of the VPN.</p>
    <p id="p4279163415333"><a name="p4279163415333"></a><a name="p4279163415333"></a>The value can be <strong id="b156776431875"><a name="b156776431875"></a><a name="b156776431875"></a>DH group 1</strong>, <strong id="b162301647476"><a name="b162301647476"></a><a name="b162301647476"></a>DH group 2</strong>, <strong id="b1134950474"><a name="b1134950474"></a><a name="b1134950474"></a>DH group 5</strong>, <strong id="b1853052778"><a name="b1853052778"></a><a name="b1853052778"></a>DH group 14</strong>, <strong id="b198439561479"><a name="b198439561479"></a><a name="b198439561479"></a>DH group 15</strong>, <strong id="b173761711981"><a name="b173761711981"></a><a name="b173761711981"></a>DH group 16</strong>, <strong id="b56250412813"><a name="b56250412813"></a><a name="b56250412813"></a>DH group 19</strong>, <strong id="b814918712815"><a name="b814918712815"></a><a name="b814918712815"></a>DH group 20</strong>, or <strong id="b1915710104810"><a name="b1915710104810"></a><a name="b1915710104810"></a>DH group 21</strong>.</p>
    <p id="p205453326474"><a name="p205453326474"></a><a name="p205453326474"></a>The PFS group security level from the highest to lowest is as follows: DH group 21 &gt; DH group 20 &gt; DH group 19 &gt; DH group 16 &gt; DH group 15 &gt; DH group 14 &gt; DH group 5 &gt; DH group 2 &gt; DH group 1.</p>
    <p id="en-us_topic_0013748707_p54958613193259"><a name="en-us_topic_0013748707_p54958613193259"></a><a name="en-us_topic_0013748707_p54958613193259"></a>The default value is <strong id="b66020298119"><a name="b66020298119"></a><a name="b66020298119"></a>DH group 5</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.950000000000003%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0013748707_p4428599520388"><a name="en-us_topic_0013748707_p4428599520388"></a><a name="en-us_topic_0013748707_p4428599520388"></a>DH group 5</p>
    </td>
    </tr>
    <tr id="en-us_topic_0013748707_row509188520388"><td class="cellrowborder" valign="top" width="32.65%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0013748707_p512698820388"><a name="en-us_topic_0013748707_p512698820388"></a><a name="en-us_topic_0013748707_p512698820388"></a>Transfer Protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.4%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0013748707_p1263291220388"><a name="en-us_topic_0013748707_p1263291220388"></a><a name="en-us_topic_0013748707_p1263291220388"></a>Specifies the security protocol used for IPsec to transmit and encapsulate user data. The value can be <strong id="b84235270615053"><a name="b84235270615053"></a><a name="b84235270615053"></a>AH</strong>, <strong id="b8423527061515"><a name="b8423527061515"></a><a name="b8423527061515"></a>ESP</strong>, or <strong id="b84235270615110"><a name="b84235270615110"></a><a name="b84235270615110"></a>AH-ESP</strong>.</p>
    <p id="en-us_topic_0013748707_p49737586193324"><a name="en-us_topic_0013748707_p49737586193324"></a><a name="en-us_topic_0013748707_p49737586193324"></a>The default value is <strong id="b841991331215"><a name="b841991331215"></a><a name="b841991331215"></a>ESP</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.950000000000003%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0013748707_p1663295220388"><a name="en-us_topic_0013748707_p1663295220388"></a><a name="en-us_topic_0013748707_p1663295220388"></a>ESP</p>
    </td>
    </tr>
    <tr id="en-us_topic_0013748707_row816438020388"><td class="cellrowborder" valign="top" width="32.65%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0013748707_p4582696720388"><a name="en-us_topic_0013748707_p4582696720388"></a><a name="en-us_topic_0013748707_p4582696720388"></a>Lifecycle (s)</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.4%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0013748707_p2099687420388"><a name="en-us_topic_0013748707_p2099687420388"></a><a name="en-us_topic_0013748707_p2099687420388"></a>Specifies the lifetime of the SA, in seconds.</p>
    <p id="en-us_topic_0013748707_p5475414020388"><a name="en-us_topic_0013748707_p5475414020388"></a><a name="en-us_topic_0013748707_p5475414020388"></a>The SA will be renegotiated if its lifetime expires.</p>
    <p id="en-us_topic_0013748707_p19068246193342"><a name="en-us_topic_0013748707_p19068246193342"></a><a name="en-us_topic_0013748707_p19068246193342"></a>The default value is <strong id="b788986380"><a name="b788986380"></a><a name="b788986380"></a>3600</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.950000000000003%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0013748707_p590032620388"><a name="en-us_topic_0013748707_p590032620388"></a><a name="en-us_topic_0013748707_p590032620388"></a>3600</p>
    </td>
    </tr>
    </tbody>
    </table>

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >The IKE policy specifies the encryption and authentication algorithms to use in the negotiation phase of an IPsec tunnel. The IPsec policy specifies the protocol, encryption algorithm, and authentication algorithm to use in the data transmission phase of an IPsec tunnel. These parameters must be the same between the VPN in your VPC and that in your data center. If they are different, the VPN cannot be set up.  

6.  Click  **Submit**.

    After the IPsec VPN is created, a public network egress IP address is assigned to the IPsec VPN. The IP address is the local gateway address of a created VPN on the network console. When configuring the remote tunnel in your data center, you must set the remote gateway address to this IP address.

    **Figure  3**  Gateway egress IP address<a name="en-us_topic_0013748707_fig4815144716272"></a>  
    ![](figures/gateway-egress-ip-address.png "gateway-egress-ip-address")

7.  Due to the symmetry of the tunnel, you also need to configure the IPsec VPN on your router or firewall in the data center.
    -   For the protocols supported by VPN connections, see section  [Reference Standards and Protocols](reference-standards-and-protocols.md).
    -   For a list of supported VPN devices, see  [Which Remote VPN Devices Are Supported?](which-remote-vpn-devices-are-supported.md).


