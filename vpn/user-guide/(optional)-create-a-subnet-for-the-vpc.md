# \(Optional\) Create a Subnet for the VPC<a name="vpn_03_0003"></a>

## Scenarios<a name="en-us_topic_0118498844_en-us_topic_0118498823_s708dc29819a94a009f142b0c0b6b8893"></a>

You can add subnets during VPC creation. If required, you can also create subnets for an existing VPC.

The created subnet is configured with DHCP by default. After an ECS using this VPC starts, the ECS automatically obtains an IP address using DHCP.

## Procedure<a name="en-us_topic_0118498844_en-us_topic_0118498823_section8897384201653"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  On the console homepage, under  **Network**, click  **Virtual Private Cloud**.
4.  In the navigation pane on the left, click  **Virtual Private Cloud**.
5.  On the  **Virtual Private Cloud**  page, locate the VPC for which a subnet is to be created and click the VPC name.
6.  On the displayed  **Subnets**  tab, click  **Create Subnet**. 
7.  In the  **Create Subnet**  area, set parameters as prompted.

    **Figure  1**  Create Subnet<a name="en-us_topic_0118498844_en-us_topic_0118498823_fig9187184162612"></a>  
    ![](figures/create-subnet.png "create-subnet")

    **Table  1**  Parameter description

    <a name="en-us_topic_0118498844_en-us_topic_0118498823_t9c09e108a58e47cd8be10575494ef9c2"></a>
    <table><thead align="left"><tr id="en-us_topic_0118498844_en-us_topic_0118498823_r243a457356d844a28b2c5dfcb381d3ca"><th class="cellrowborder" valign="top" width="19.24%" id="mcps1.2.4.1.1"><p id="en-us_topic_0118498844_en-us_topic_0118498823_a351cf2430e0e40d2bc4e0b8e509649bb"><a name="en-us_topic_0118498844_en-us_topic_0118498823_a351cf2430e0e40d2bc4e0b8e509649bb"></a><a name="en-us_topic_0118498844_en-us_topic_0118498823_a351cf2430e0e40d2bc4e0b8e509649bb"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="55.7%" id="mcps1.2.4.1.2"><p id="en-us_topic_0118498844_en-us_topic_0118498823_abf569c9e39bd4ba99a7ab37cc60e6883"><a name="en-us_topic_0118498844_en-us_topic_0118498823_abf569c9e39bd4ba99a7ab37cc60e6883"></a><a name="en-us_topic_0118498844_en-us_topic_0118498823_abf569c9e39bd4ba99a7ab37cc60e6883"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="25.06%" id="mcps1.2.4.1.3"><p id="en-us_topic_0118498844_en-us_topic_0118498823_af6ab204c10ca462f889acfe449817860"><a name="en-us_topic_0118498844_en-us_topic_0118498823_af6ab204c10ca462f889acfe449817860"></a><a name="en-us_topic_0118498844_en-us_topic_0118498823_af6ab204c10ca462f889acfe449817860"></a>Example Value</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0118498844_en-us_topic_0118498823_rc908647483fd4e478dc43fd83fcb6575"><td class="cellrowborder" valign="top" width="19.24%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0118498844_en-us_topic_0118498823_a22acb391d20242989d8f5dd96c13651f"><a name="en-us_topic_0118498844_en-us_topic_0118498823_a22acb391d20242989d8f5dd96c13651f"></a><a name="en-us_topic_0118498844_en-us_topic_0118498823_a22acb391d20242989d8f5dd96c13651f"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.7%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0118498844_en-us_topic_0118498823_a4b3e19d17d4141a5afca8cce53ac9383"><a name="en-us_topic_0118498844_en-us_topic_0118498823_a4b3e19d17d4141a5afca8cce53ac9383"></a><a name="en-us_topic_0118498844_en-us_topic_0118498823_a4b3e19d17d4141a5afca8cce53ac9383"></a>Specifies the subnet name.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0118498844_en-us_topic_0118498823_a2fa81825f84e4c2cad5544ee60356fc8"><a name="en-us_topic_0118498844_en-us_topic_0118498823_a2fa81825f84e4c2cad5544ee60356fc8"></a><a name="en-us_topic_0118498844_en-us_topic_0118498823_a2fa81825f84e4c2cad5544ee60356fc8"></a>Subnet</p>
    </td>
    </tr>
    <tr id="en-us_topic_0118498844_en-us_topic_0118498823_ra338f8572c2042b1909a2e07a43a1868"><td class="cellrowborder" valign="top" width="19.24%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0118498844_en-us_topic_0118498823_en-us_topic_0029397261_p39320517305"><a name="en-us_topic_0118498844_en-us_topic_0118498823_en-us_topic_0029397261_p39320517305"></a><a name="en-us_topic_0118498844_en-us_topic_0118498823_en-us_topic_0029397261_p39320517305"></a>CIDR Block</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.7%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0118498844_en-us_topic_0118498823_a9adafdbd17fa4d288fb3a60619789bb7"><a name="en-us_topic_0118498844_en-us_topic_0118498823_a9adafdbd17fa4d288fb3a60619789bb7"></a><a name="en-us_topic_0118498844_en-us_topic_0118498823_a9adafdbd17fa4d288fb3a60619789bb7"></a>Specifies the CIDR block for the subnet. This value must be within the VPC CIDR block.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0118498844_en-us_topic_0118498823_a4759f7fcda144bfaa8c0bbc806948e71"><a name="en-us_topic_0118498844_en-us_topic_0118498823_a4759f7fcda144bfaa8c0bbc806948e71"></a><a name="en-us_topic_0118498844_en-us_topic_0118498823_a4759f7fcda144bfaa8c0bbc806948e71"></a>192.168.0.0/24</p>
    </td>
    </tr>
    <tr id="en-us_topic_0118498844_en-us_topic_0118498823_ra7655f6b0a5c4d13a2b144962179f7c7"><td class="cellrowborder" valign="top" width="19.24%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0118498844_en-us_topic_0118498823_a143f3bcfe0154e18a8ea46a21b06c56f"><a name="en-us_topic_0118498844_en-us_topic_0118498823_a143f3bcfe0154e18a8ea46a21b06c56f"></a><a name="en-us_topic_0118498844_en-us_topic_0118498823_a143f3bcfe0154e18a8ea46a21b06c56f"></a>Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.7%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0118498844_en-us_topic_0118498823_en-us_topic_0029397261_p190934817305"><a name="en-us_topic_0118498844_en-us_topic_0118498823_en-us_topic_0029397261_p190934817305"></a><a name="en-us_topic_0118498844_en-us_topic_0118498823_en-us_topic_0029397261_p190934817305"></a>Specifies the gateway address of the subnet.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0118498844_en-us_topic_0118498823_a4ea86de1e68d4f31afd5550e894d9c4b"><a name="en-us_topic_0118498844_en-us_topic_0118498823_a4ea86de1e68d4f31afd5550e894d9c4b"></a><a name="en-us_topic_0118498844_en-us_topic_0118498823_a4ea86de1e68d4f31afd5550e894d9c4b"></a>192.168.0.1</p>
    </td>
    </tr>
    <tr id="en-us_topic_0118498844_en-us_topic_0118498823_row193951299013"><td class="cellrowborder" valign="top" width="19.24%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0118498844_en-us_topic_0118498823_p1984172312520"><a name="en-us_topic_0118498844_en-us_topic_0118498823_p1984172312520"></a><a name="en-us_topic_0118498844_en-us_topic_0118498823_p1984172312520"></a>NTP Server Address</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.7%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0118498844_en-us_topic_0118498823_p138416231255"><a name="en-us_topic_0118498844_en-us_topic_0118498823_p138416231255"></a><a name="en-us_topic_0118498844_en-us_topic_0118498823_p138416231255"></a>Specifies the NTP server IP address. A maximum of four IP addresses can be configured. Multiple IP addresses must be separated using commas (,).</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0118498844_en-us_topic_0118498823_p484723192518"><a name="en-us_topic_0118498844_en-us_topic_0118498823_p484723192518"></a><a name="en-us_topic_0118498844_en-us_topic_0118498823_p484723192518"></a>192.168.2.1</p>
    </td>
    </tr>
    <tr id="en-us_topic_0118498844_en-us_topic_0118498823_row54331447162214"><td class="cellrowborder" valign="top" width="19.24%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0118498844_en-us_topic_0118498823_p8238528162216"><a name="en-us_topic_0118498844_en-us_topic_0118498823_p8238528162216"></a><a name="en-us_topic_0118498844_en-us_topic_0118498823_p8238528162216"></a>Tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.7%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0118498844_en-us_topic_0118498823_p63340999162216"><a name="en-us_topic_0118498844_en-us_topic_0118498823_p63340999162216"></a><a name="en-us_topic_0118498844_en-us_topic_0118498823_p63340999162216"></a>Specifies the subnet tag, which consists of a key and value pair. You can add a maximum of ten tags to each subnet.</p>
    <p id="en-us_topic_0118498844_en-us_topic_0118498823_p33198085162216"><a name="en-us_topic_0118498844_en-us_topic_0118498823_p33198085162216"></a><a name="en-us_topic_0118498844_en-us_topic_0118498823_p33198085162216"></a>The tag key and value must meet the requirements listed in <a href="#en-us_topic_0118498844_en-us_topic_0118498823_table4528555192814">Table 2</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0118498844_en-us_topic_0118498823_ul42213484162216"></a><a name="en-us_topic_0118498844_en-us_topic_0118498823_ul42213484162216"></a><ul id="en-us_topic_0118498844_en-us_topic_0118498823_ul42213484162216"><li>Key: subnet_key1</li><li>Value: subnet-01</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0118498844_en-us_topic_0118498823_row696919302813"><td class="cellrowborder" valign="top" width="19.24%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0118498844_en-us_topic_0118498823_p3868137104715"><a name="en-us_topic_0118498844_en-us_topic_0118498823_p3868137104715"></a><a name="en-us_topic_0118498844_en-us_topic_0118498823_p3868137104715"></a>DNS Server Address</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.7%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0118498844_en-us_topic_0118498823_p587119375475"><a name="en-us_topic_0118498844_en-us_topic_0118498823_p587119375475"></a><a name="en-us_topic_0118498844_en-us_topic_0118498823_p587119375475"></a>The external DNS server address is used by default. If you need to change the DNS server address, ensure that the configured DNS server address is available.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0118498844_en-us_topic_0118498823_p2875193744719"><a name="en-us_topic_0118498844_en-us_topic_0118498823_p2875193744719"></a><a name="en-us_topic_0118498844_en-us_topic_0118498823_p2875193744719"></a>-</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  Subnet tag key and value requirements

    <a name="en-us_topic_0118498844_en-us_topic_0118498823_table4528555192814"></a>
    <table><thead align="left"><tr id="en-us_topic_0118498932_rd57708e01e6443a9805ca72f554fae7f"><th class="cellrowborder" valign="top" width="18.54%" id="mcps1.2.4.1.1"><p id="en-us_topic_0118498932_abc7708d69440476086850b219c70efa8"><a name="en-us_topic_0118498932_abc7708d69440476086850b219c70efa8"></a><a name="en-us_topic_0118498932_abc7708d69440476086850b219c70efa8"></a><strong id="en-us_topic_0118498932_b842352706165123"><a name="en-us_topic_0118498932_b842352706165123"></a><a name="en-us_topic_0118498932_b842352706165123"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.39%" id="mcps1.2.4.1.2"><p id="en-us_topic_0118498932_a0df2f83c3277432ab05b525e4ffb1c2c"><a name="en-us_topic_0118498932_a0df2f83c3277432ab05b525e4ffb1c2c"></a><a name="en-us_topic_0118498932_a0df2f83c3277432ab05b525e4ffb1c2c"></a><strong id="en-us_topic_0118498932_b842352706174218"><a name="en-us_topic_0118498932_b842352706174218"></a><a name="en-us_topic_0118498932_b842352706174218"></a>Requirements</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.07%" id="mcps1.2.4.1.3"><p id="en-us_topic_0118498932_a902e732241f94e96b0b1b718cf7ed639"><a name="en-us_topic_0118498932_a902e732241f94e96b0b1b718cf7ed639"></a><a name="en-us_topic_0118498932_a902e732241f94e96b0b1b718cf7ed639"></a><strong id="en-us_topic_0118498932_b842352706174227"><a name="en-us_topic_0118498932_b842352706174227"></a><a name="en-us_topic_0118498932_b842352706174227"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0118498932_r95612b479088487b99e620f90b71f798"><td class="cellrowborder" valign="top" width="18.54%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0118498932_a7694a48138124d1daf3804556a27bfd6"><a name="en-us_topic_0118498932_a7694a48138124d1daf3804556a27bfd6"></a><a name="en-us_topic_0118498932_a7694a48138124d1daf3804556a27bfd6"></a>Key</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.39%" headers="mcps1.2.4.1.2 "><a name="en-us_topic_0118498932_uac40e19ce4ac49d0913d48b334564c45"></a><a name="en-us_topic_0118498932_uac40e19ce4ac49d0913d48b334564c45"></a><ul id="en-us_topic_0118498932_uac40e19ce4ac49d0913d48b334564c45"><li>Cannot be left blank.</li><li>Must be unique for each subnet.</li><li>Can contain a maximum of 36 characters.</li><li>Can contain only the following character types:<a name="en-us_topic_0118498932_uccb317c6616b4445aa84b125e5aa017f"></a><a name="en-us_topic_0118498932_uccb317c6616b4445aa84b125e5aa017f"></a><ul id="en-us_topic_0118498932_uccb317c6616b4445aa84b125e5aa017f"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
    </li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="28.07%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0118498932_a1a10de6d67c04555a3508a8cdc3500e7"><a name="en-us_topic_0118498932_a1a10de6d67c04555a3508a8cdc3500e7"></a><a name="en-us_topic_0118498932_a1a10de6d67c04555a3508a8cdc3500e7"></a>subnet_key1</p>
    </td>
    </tr>
    <tr id="en-us_topic_0118498932_r32a79d8bde844fda8a6254383317e58f"><td class="cellrowborder" valign="top" width="18.54%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0118498932_a1ebd1dda592448d49631c7f099519113"><a name="en-us_topic_0118498932_a1ebd1dda592448d49631c7f099519113"></a><a name="en-us_topic_0118498932_a1ebd1dda592448d49631c7f099519113"></a>Value</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.39%" headers="mcps1.2.4.1.2 "><a name="en-us_topic_0118498932_uaf17b1ea9b9a4e58b95cafefa2898283"></a><a name="en-us_topic_0118498932_uaf17b1ea9b9a4e58b95cafefa2898283"></a><ul id="en-us_topic_0118498932_uaf17b1ea9b9a4e58b95cafefa2898283"><li>Can contain a maximum of 43 characters.</li><li>Can contain only the following character types:<a name="en-us_topic_0118498932_ub74c759faad544c3b4428accc9c42b80"></a><a name="en-us_topic_0118498932_ub74c759faad544c3b4428accc9c42b80"></a><ul id="en-us_topic_0118498932_ub74c759faad544c3b4428accc9c42b80"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
    </li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="28.07%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0118498932_a21a035aeb72143f5ab0fd45a08248d08"><a name="en-us_topic_0118498932_a21a035aeb72143f5ab0fd45a08248d08"></a><a name="en-us_topic_0118498932_a21a035aeb72143f5ab0fd45a08248d08"></a>subnet-01</p>
    </td>
    </tr>
    </tbody>
    </table>

8.  The external DNS server address is used by default. If you need to change the DNS server address, select  **Custom**  for  **Advanced Settings**  and configure the DNS server addresses. You must ensure that the configured DNS server addresses are available.
9.  Click  **OK**.

## Precautions<a name="en-us_topic_0118498844_en-us_topic_0118498823_section231019253518"></a>

After a subnet is created, five IP addresses in the subnet will be reserved and cannot be used. For example, in a subnet with CIDR block 192.168.0.0/24, the following IP addresses are reserved:

-   192.168.0.0: Network address.
-   192.168.0.1: Gateway address.
-   192.168.0.253: Reserved for the system interface. This IP address is used by the VPC for external communication.
-   192.168.0.254: DHCP service address.
-   192.168.0.255: Network broadcast address.

If you set  **Advanced Settings**  to  **Custom**  during subnet creation, the reserved IP addresses may be different from the preceding default ones. The system will reserve five IP addresses based on your subnet settings.

