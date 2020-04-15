# Creating a Direct Connection<a name="EN-US_TOPIC_0034301493"></a>

## Scenarios<a name="section6511504717102"></a>

Apply for a direct connection to enable ECSs in your VPC to communicate with your data center or private network.

## Procedure<a name="section22771322171016"></a>

1.  Collect the information listed in  [Table 1](#table27593495173236).

    **Table  1**  Parameters required for creating a direct connection

    <a name="table27593495173236"></a>
    <table><thead align="left"><tr id="row20729321173236"><th class="cellrowborder" valign="top" width="22.869999999999997%" id="mcps1.2.4.1.1"><p id="p34545082173236"><a name="p34545082173236"></a><a name="p34545082173236"></a><strong id="b84235270616452"><a name="b84235270616452"></a><a name="b84235270616452"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="51.44%" id="mcps1.2.4.1.2"><p id="p17541007173236"><a name="p17541007173236"></a><a name="p17541007173236"></a><strong id="b46688243173236"><a name="b46688243173236"></a><a name="b46688243173236"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25.69%" id="mcps1.2.4.1.3"><p id="p36710115173236"><a name="p36710115173236"></a><a name="p36710115173236"></a><strong id="b11535442173236"><a name="b11535442173236"></a><a name="b11535442173236"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row49534062173236"><td class="cellrowborder" valign="top" width="22.869999999999997%" headers="mcps1.2.4.1.1 "><p id="p1353477173236"><a name="p1353477173236"></a><a name="p1353477173236"></a>Domain Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.44%" headers="mcps1.2.4.1.2 "><p id="p47160706173236"><a name="p47160706173236"></a><a name="p47160706173236"></a>Specifies the domain name. For details about how to obtain the domain name, see <a href="obtaining-the-domain-name.md">Obtaining the Domain Name</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.69%" headers="mcps1.2.4.1.3 "><p id="p61920864173236"><a name="p61920864173236"></a><a name="p61920864173236"></a>abc123</p>
    </td>
    </tr>
    <tr id="row23456554173236"><td class="cellrowborder" valign="top" width="22.869999999999997%" headers="mcps1.2.4.1.1 "><p id="p43153374173236"><a name="p43153374173236"></a><a name="p43153374173236"></a>Region</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.44%" headers="mcps1.2.4.1.2 "><p id="p51861819173236"><a name="p51861819173236"></a><a name="p51861819173236"></a>Specifies the region where the direct connect is created. For details about how to obtain the region, see <a href="obtaining-the-region.md">Obtaining the Region</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.69%" headers="mcps1.2.4.1.3 "><p id="p40057802173236"><a name="p40057802173236"></a><a name="p40057802173236"></a>eu-de</p>
    </td>
    </tr>
    <tr id="row13638511173236"><td class="cellrowborder" valign="top" width="22.869999999999997%" headers="mcps1.2.4.1.1 "><p id="p9782400173236"><a name="p9782400173236"></a><a name="p9782400173236"></a>VPC ID</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.44%" headers="mcps1.2.4.1.2 "><p id="p17830268173236"><a name="p17830268173236"></a><a name="p17830268173236"></a>Specifies the VPC ID. For details about how to obtain the VPC ID, see <a href="obtaining-the-vpc-id.md">Obtaining the VPC ID</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.69%" headers="mcps1.2.4.1.3 "><p id="p34965565173236"><a name="p34965565173236"></a><a name="p34965565173236"></a>13e2e8cb-5894-496c-8688-7b08c485e70b</p>
    </td>
    </tr>
    <tr id="row6545908104814"><td class="cellrowborder" valign="top" width="22.869999999999997%" headers="mcps1.2.4.1.1 "><p id="p58913176104814"><a name="p58913176104814"></a><a name="p58913176104814"></a>Project Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.44%" headers="mcps1.2.4.1.2 "><p id="p7237976104814"><a name="p7237976104814"></a><a name="p7237976104814"></a>Specifies the name of the project to which the direct connection belongs, which can be obtained by performing the following steps:</p>
    <p id="p7520175316368"><a name="p7520175316368"></a><a name="p7520175316368"></a>Click the username in the upper right corner and select <strong id="b1751153517128"><a name="b1751153517128"></a><a name="b1751153517128"></a>My Credential</strong> from the drop-down list.</p>
    <p id="p15467798192043"><a name="p15467798192043"></a><a name="p15467798192043"></a>Under the <strong id="b63511737191214"><a name="b63511737191214"></a><a name="b63511737191214"></a>Projects</strong> tab, view the project names.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.69%" headers="mcps1.2.4.1.3 "><p id="p49405201104814"><a name="p49405201104814"></a><a name="p49405201104814"></a>DeC_001</p>
    </td>
    </tr>
    <tr id="row9626488173236"><td class="cellrowborder" valign="top" width="22.869999999999997%" headers="mcps1.2.4.1.1 "><p id="p55637737173236"><a name="p55637737173236"></a><a name="p55637737173236"></a>Port Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.44%" headers="mcps1.2.4.1.2 "><p id="p9438060174740"><a name="p9438060174740"></a><a name="p9438060174740"></a>Specifies the port type.</p>
    <p id="p20305571122457"><a name="p20305571122457"></a><a name="p20305571122457"></a>The value can be <strong id="b842352706163436"><a name="b842352706163436"></a><a name="b842352706163436"></a>1GE</strong> or <strong id="b842352706163440"><a name="b842352706163440"></a><a name="b842352706163440"></a>10GE</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.69%" headers="mcps1.2.4.1.3 "><p id="p34087529173236"><a name="p34087529173236"></a><a name="p34087529173236"></a>1GE or 10GE</p>
    </td>
    </tr>
    <tr id="row12769101618429"><td class="cellrowborder" valign="top" width="22.869999999999997%" headers="mcps1.2.4.1.1 "><p id="p7770416124220"><a name="p7770416124220"></a><a name="p7770416124220"></a>Local Subnet</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.44%" headers="mcps1.2.4.1.2 "><p id="p2335329185214"><a name="p2335329185214"></a><a name="p2335329185214"></a>Specifies the subnet segment of the local VPC connected to the direct connection.</p>
    <p id="p105949945211"><a name="p105949945211"></a><a name="p105949945211"></a>A maximum of 25 local subnets can be configured.</p>
    <p id="p75171811131419"><a name="p75171811131419"></a><a name="p75171811131419"></a>The local subnet and remote subnet cannot be in the same network segment.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.69%" headers="mcps1.2.4.1.3 "><p id="p1955958185112"><a name="p1955958185112"></a><a name="p1955958185112"></a>192.168.1.0/24,192.168.51.0/24</p>
    </td>
    </tr>
    <tr id="row5520954173236"><td class="cellrowborder" valign="top" width="22.869999999999997%" headers="mcps1.2.4.1.1 "><p id="p19529531173236"><a name="p19529531173236"></a><a name="p19529531173236"></a>Remote Subnet</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.44%" headers="mcps1.2.4.1.2 "><p id="p5636670317492"><a name="p5636670317492"></a><a name="p5636670317492"></a>Specifies the tenant subnet.</p>
    <p id="p3921374317485"><a name="p3921374317485"></a><a name="p3921374317485"></a>The value must be a private IP address with a subnet mask. Multiple subnets are separated with commas (,).</p>
    <p id="p4471553510588"><a name="p4471553510588"></a><a name="p4471553510588"></a>A maximum of 50 remote subnets can be configured. </p>
    <p id="p19920113911146"><a name="p19920113911146"></a><a name="p19920113911146"></a>The local subnet and remote subnet cannot be in the same network segment.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.69%" headers="mcps1.2.4.1.3 "><p id="p22437781173236"><a name="p22437781173236"></a><a name="p22437781173236"></a>192.168.10.0/24,192.168.52.0/24</p>
    </td>
    </tr>
    <tr id="row22377693173236"><td class="cellrowborder" valign="top" width="22.869999999999997%" headers="mcps1.2.4.1.1 "><p id="p49688592173236"><a name="p49688592173236"></a><a name="p49688592173236"></a>Bandwidth</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.44%" headers="mcps1.2.4.1.2 "><p id="p5904665171045"><a name="p5904665171045"></a><a name="p5904665171045"></a>Specifies the bandwidth size.</p>
    <p id="p57878187122457"><a name="p57878187122457"></a><a name="p57878187122457"></a>The maximum value is <strong id="b31674111153544"><a name="b31674111153544"></a><a name="b31674111153544"></a>10240 Mbit/s.</strong></p>
    </td>
    <td class="cellrowborder" valign="top" width="25.69%" headers="mcps1.2.4.1.3 "><p id="p59100086173236"><a name="p59100086173236"></a><a name="p59100086173236"></a>10240 Mbit/s</p>
    </td>
    </tr>
    <tr id="row19093454173236"><td class="cellrowborder" valign="top" width="22.869999999999997%" headers="mcps1.2.4.1.1 "><p id="p72645173236"><a name="p72645173236"></a><a name="p72645173236"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.44%" headers="mcps1.2.4.1.2 "><p id="p168860174929"><a name="p168860174929"></a><a name="p168860174929"></a>Specifies the direct connection name.</p>
    <p id="p29414514122722"><a name="p29414514122722"></a><a name="p29414514122722"></a>The value is a string of no more than 64 characters that can contain letters, digits, underscores (_), and hyphens (-).</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.69%" headers="mcps1.2.4.1.3 "><p id="p6863757173236"><a name="p6863757173236"></a><a name="p6863757173236"></a>directconnect-001</p>
    </td>
    </tr>
    </tbody>
    </table>

2.  Creating a direct connection based on the parameters in  [Table 1](#table27593495173236)  using either of the following methods:
    -   [Send us an email](https://docs.otc.t-systems.com/en-us/public/learnmore.html)  with the title "Applying for Creating a Direct Connection".
    -   [Call us](https://docs.otc.t-systems.com/en-us/public/learnmore.html)  and provide the collected information to our customer service personnel.
    -   Contact our sales personnel to send the collected information.

3.  Wait for the notification of the result from the email, our customer service personnel, or sales personnel.

