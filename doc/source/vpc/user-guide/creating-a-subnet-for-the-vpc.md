# Creating a Subnet for the VPC<a name="en-us_topic_0013748726"></a>

## Scenarios<a name="s708dc29819a94a009f142b0c0b6b8893"></a>

A VPC comes with a default subnet. If the default subnet cannot meet your requirements, you can create one.

The subnet is configured with DHCP by default. When an ECS using this VPC starts, the ECS automatically uses DHCP to obtain an IP address.

## Procedure<a name="section8897384201653"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  On the console homepage, under  **Network**, click  **Virtual Private Cloud**.
4.  In the navigation pane on the left, click  **Virtual Private Cloud**.
5.  On the  **Virtual Private Cloud**  page, locate the VPC for which a subnet is to be created and click the VPC name.
6.  On the displayed  **Subnets**  tab, click  **Create Subnet**. 
7.  Set the parameters as prompted.

    **Figure  1**  Create Subnet<a name="fig1520802719398"></a>  
    ![](figures/create-subnet.png "create-subnet")

    **Table  1**  Parameter description

    <a name="table102110278397"></a>
    <table><thead align="left"><tr id="row152091427193914"><th class="cellrowborder" valign="top" width="19.24%" id="mcps1.2.4.1.1"><p id="p19208192712392"><a name="p19208192712392"></a><a name="p19208192712392"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="55.7%" id="mcps1.2.4.1.2"><p id="p1720812710393"><a name="p1720812710393"></a><a name="p1720812710393"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="25.06%" id="mcps1.2.4.1.3"><p id="p2209132715398"><a name="p2209132715398"></a><a name="p2209132715398"></a>Example Value</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1420922733913"><td class="cellrowborder" valign="top" width="19.24%" headers="mcps1.2.4.1.1 "><p id="p2020911276399"><a name="p2020911276399"></a><a name="p2020911276399"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.7%" headers="mcps1.2.4.1.2 "><p id="p18209427203910"><a name="p18209427203910"></a><a name="p18209427203910"></a>Specifies the subnet name.</p>
    <p id="p24201817123619"><a name="p24201817123619"></a><a name="p24201817123619"></a>The VPC flow log name can contain a maximum of 64 characters, which may consist of letters, digits, underscores (_), hyphens (-), and periods (.). The name cannot contain spaces.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.3 "><p id="p7209192718395"><a name="p7209192718395"></a><a name="p7209192718395"></a>Subnet</p>
    </td>
    </tr>
    <tr id="row820919275399"><td class="cellrowborder" valign="top" width="19.24%" headers="mcps1.2.4.1.1 "><p id="p17209132723919"><a name="p17209132723919"></a><a name="p17209132723919"></a>CIDR Block</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.7%" headers="mcps1.2.4.1.2 "><p id="p142091427143916"><a name="p142091427143916"></a><a name="p142091427143916"></a>Specifies the CIDR block for the subnet. This value must be within the VPC CIDR block.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.3 "><p id="p13209132714399"><a name="p13209132714399"></a><a name="p13209132714399"></a>192.168.0.0/24</p>
    </td>
    </tr>
    <tr id="row1968522515187"><td class="cellrowborder" valign="top" width="19.24%" headers="mcps1.2.4.1.1 "><p id="p1236582318816"><a name="p1236582318816"></a><a name="p1236582318816"></a>Advanced Settings</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.7%" headers="mcps1.2.4.1.2 "><p id="p1636617235820"><a name="p1636617235820"></a><a name="p1636617235820"></a>Two options are available, <strong id="b448422410434"><a name="b448422410434"></a><a name="b448422410434"></a>Default</strong> and <strong id="b64851124104317"><a name="b64851124104317"></a><a name="b64851124104317"></a>Custom</strong>. You can set <strong id="b5682154017593"><a name="b5682154017593"></a><a name="b5682154017593"></a>Advanced Settings</strong> to <strong id="b19682740115913"><a name="b19682740115913"></a><a name="b19682740115913"></a>Custom</strong> to configure advanced subnet parameters.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.3 "><p id="p1936610239811"><a name="p1936610239811"></a><a name="p1936610239811"></a>Default</p>
    </td>
    </tr>
    <tr id="row1221062712396"><td class="cellrowborder" valign="top" width="19.24%" headers="mcps1.2.4.1.1 "><p id="p92098271396"><a name="p92098271396"></a><a name="p92098271396"></a>Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.7%" headers="mcps1.2.4.1.2 "><p id="p13209427163915"><a name="p13209427163915"></a><a name="p13209427163915"></a>Specifies the gateway address of the subnet.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.3 "><p id="p820982723914"><a name="p820982723914"></a><a name="p820982723914"></a>192.168.0.1</p>
    </td>
    </tr>
    <tr id="row814813278462"><td class="cellrowborder" valign="top" width="19.24%" headers="mcps1.2.4.1.1 "><p id="p16210927153913"><a name="p16210927153913"></a><a name="p16210927153913"></a>DNS Server Address</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.7%" headers="mcps1.2.4.1.2 "><p id="p15436112194319"><a name="p15436112194319"></a><a name="p15436112194319"></a>By default, two DNS server addresses are configured. You can change them if necessary. A maximum of five DNS server addresses can be configured. Multiple IP addresses must be separated using commas (,).</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.3 "><p id="p42104273396"><a name="p42104273396"></a><a name="p42104273396"></a>100.125.x.x</p>
    </td>
    </tr>
    <tr id="row19210152793912"><td class="cellrowborder" valign="top" width="19.24%" headers="mcps1.2.4.1.1 "><p id="p4210132713399"><a name="p4210132713399"></a><a name="p4210132713399"></a>NTP Server Address</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.7%" headers="mcps1.2.4.1.2 "><p id="p927533664219"><a name="p927533664219"></a><a name="p927533664219"></a>Specifies the IP address of the NTP server. This parameter is optional.</p>
    <p id="p195514432428"><a name="p195514432428"></a><a name="p195514432428"></a>You can configure the NTP server IP addresses to be added to the subnet as required. The IP addresses are added in addition to the default NTP server addresses. If this parameter is left empty, no IP address of the NTP server is added.</p>
    <p id="p7667123710153"><a name="p7667123710153"></a><a name="p7667123710153"></a>A maximum of four IP addresses can be configured. Multiple IP addresses must be separated using commas (,).</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.3 "><p id="p221062715396"><a name="p221062715396"></a><a name="p221062715396"></a>192.168.2.1</p>
    </td>
    </tr>
    <tr id="row18210162714395"><td class="cellrowborder" valign="top" width="19.24%" headers="mcps1.2.4.1.1 "><p id="p721082713914"><a name="p721082713914"></a><a name="p721082713914"></a>Tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.7%" headers="mcps1.2.4.1.2 "><p id="p1221072714396"><a name="p1221072714396"></a><a name="p1221072714396"></a>Specifies the subnet tag, which consists of a key and value pair. You can add a maximum of ten tags to each subnet.</p>
    <p id="p0210112710395"><a name="p0210112710395"></a><a name="p0210112710395"></a>The tag key and value must meet the requirements listed in <a href="#table42131827173915">Table 2</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.3 "><a name="ul13210152793913"></a><a name="ul13210152793913"></a><ul id="ul13210152793913"><li>Key: subnet_key1</li><li>Value: subnet-01</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  Subnet tag key and value requirements

    <a name="table42131827173915"></a>
    <table><thead align="left"><tr id="vpc_vpc_0005_rd57708e01e6443a9805ca72f554fae7f"><th class="cellrowborder" valign="top" width="18.54%" id="mcps1.2.4.1.1"><p id="vpc_vpc_0005_abc7708d69440476086850b219c70efa8"><a name="vpc_vpc_0005_abc7708d69440476086850b219c70efa8"></a><a name="vpc_vpc_0005_abc7708d69440476086850b219c70efa8"></a><strong id="vpc_vpc_0005_b842352706165123"><a name="vpc_vpc_0005_b842352706165123"></a><a name="vpc_vpc_0005_b842352706165123"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.39%" id="mcps1.2.4.1.2"><p id="vpc_vpc_0005_a0df2f83c3277432ab05b525e4ffb1c2c"><a name="vpc_vpc_0005_a0df2f83c3277432ab05b525e4ffb1c2c"></a><a name="vpc_vpc_0005_a0df2f83c3277432ab05b525e4ffb1c2c"></a><strong id="vpc_vpc_0005_b842352706174218"><a name="vpc_vpc_0005_b842352706174218"></a><a name="vpc_vpc_0005_b842352706174218"></a>Requirements</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.07%" id="mcps1.2.4.1.3"><p id="vpc_vpc_0005_a902e732241f94e96b0b1b718cf7ed639"><a name="vpc_vpc_0005_a902e732241f94e96b0b1b718cf7ed639"></a><a name="vpc_vpc_0005_a902e732241f94e96b0b1b718cf7ed639"></a><strong id="vpc_vpc_0005_b842352706174227"><a name="vpc_vpc_0005_b842352706174227"></a><a name="vpc_vpc_0005_b842352706174227"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="vpc_vpc_0005_r95612b479088487b99e620f90b71f798"><td class="cellrowborder" valign="top" width="18.54%" headers="mcps1.2.4.1.1 "><p id="vpc_vpc_0005_a7694a48138124d1daf3804556a27bfd6"><a name="vpc_vpc_0005_a7694a48138124d1daf3804556a27bfd6"></a><a name="vpc_vpc_0005_a7694a48138124d1daf3804556a27bfd6"></a>Key</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.39%" headers="mcps1.2.4.1.2 "><a name="vpc_vpc_0005_uac40e19ce4ac49d0913d48b334564c45"></a><a name="vpc_vpc_0005_uac40e19ce4ac49d0913d48b334564c45"></a><ul id="vpc_vpc_0005_uac40e19ce4ac49d0913d48b334564c45"><li>Cannot be left blank.</li><li>Must be unique for each subnet.</li><li>Can contain a maximum of 36 characters.</li><li>Can contain only the following character types:<a name="vpc_vpc_0005_uccb317c6616b4445aa84b125e5aa017f"></a><a name="vpc_vpc_0005_uccb317c6616b4445aa84b125e5aa017f"></a><ul id="vpc_vpc_0005_uccb317c6616b4445aa84b125e5aa017f"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
    </li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="28.07%" headers="mcps1.2.4.1.3 "><p id="vpc_vpc_0005_a1a10de6d67c04555a3508a8cdc3500e7"><a name="vpc_vpc_0005_a1a10de6d67c04555a3508a8cdc3500e7"></a><a name="vpc_vpc_0005_a1a10de6d67c04555a3508a8cdc3500e7"></a>subnet_key1</p>
    </td>
    </tr>
    <tr id="vpc_vpc_0005_r32a79d8bde844fda8a6254383317e58f"><td class="cellrowborder" valign="top" width="18.54%" headers="mcps1.2.4.1.1 "><p id="vpc_vpc_0005_a1ebd1dda592448d49631c7f099519113"><a name="vpc_vpc_0005_a1ebd1dda592448d49631c7f099519113"></a><a name="vpc_vpc_0005_a1ebd1dda592448d49631c7f099519113"></a>Value</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.39%" headers="mcps1.2.4.1.2 "><a name="vpc_vpc_0005_uaf17b1ea9b9a4e58b95cafefa2898283"></a><a name="vpc_vpc_0005_uaf17b1ea9b9a4e58b95cafefa2898283"></a><ul id="vpc_vpc_0005_uaf17b1ea9b9a4e58b95cafefa2898283"><li>Can contain a maximum of 43 characters.</li><li>Can contain only the following character types:<a name="vpc_vpc_0005_ub74c759faad544c3b4428accc9c42b80"></a><a name="vpc_vpc_0005_ub74c759faad544c3b4428accc9c42b80"></a><ul id="vpc_vpc_0005_ub74c759faad544c3b4428accc9c42b80"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
    </li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="28.07%" headers="mcps1.2.4.1.3 "><p id="vpc_vpc_0005_a21a035aeb72143f5ab0fd45a08248d08"><a name="vpc_vpc_0005_a21a035aeb72143f5ab0fd45a08248d08"></a><a name="vpc_vpc_0005_a21a035aeb72143f5ab0fd45a08248d08"></a>subnet-01</p>
    </td>
    </tr>
    </tbody>
    </table>

8.  Click  **OK**.

## Precautions<a name="section231019253518"></a>

When a subnet is created, there are five reserved IP addresses, which cannot be used. For example, in a subnet with CIDR block 192.168.0.0/24, the following IP addresses are reserved:

-   192.168.0.0: Network ID. This address is the beginning of the private IP address range and will not be assigned to any instance.
-   192.168.0.1: Gateway address.
-   192.168.0.253: Reserved for the system interface. This IP address is used by the VPC for external communication.
-   192.168.0.254: DHCP service address.
-   192.168.0.255: Network broadcast address.

If you set  **Advanced Settings**  to  **Custom**  during subnet creation, the reserved IP addresses may be different from the default ones, but there will still be five of them. The specific addresses depend on your subnet settings.

