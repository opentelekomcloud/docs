# Creating a Subnet for the VPC<a name="en-us_topic_0030971611"></a>

## Scenarios<a name="en-us_topic_0013748726_s708dc29819a94a009f142b0c0b6b8893"></a>

A subnet is automatically created when you create a VPC. If required, you can create another subnet in the VPC.

The created subnet is configured with DHCP by default. After an ECS using this VPC starts, the ECS automatically obtains an IP address using DHCP.

## Procedure<a name="en-us_topic_0013748726_section8897384201653"></a>

1.  Log in to the management console.
2.  Click  ![](figures/en-us_image_0118621993.png)  in the upper left corner and select the desired region and project.
3.  On the console homepage, under  **Network**, click **Virtual Private Cloud**.
4.  In the navigation pane on the left, click  **Virtual Private Cloud**.
5.  On the  **Virtual Private Cloud**  page, locate the VPC for which a subnet is to be created and click the VPC name.
6.  On the displayed  **Subnets** tab, click **Create Subnet**.
7.  In the  **Create Subnet**  area, set parameters as prompted.

    **Figure  1**  Create Subnet<a name="en-us_topic_0013748726_fig43371504191921"></a>
    ![](figures/create-subnet.png "Create Subnet")

    **Table  1**  Parameter description

    <a name="en-us_topic_0013748726_t9c09e108a58e47cd8be10575494ef9c2"></a><table><thead align="left"><tr id="en-us_topic_0013748726_r243a457356d844a28b2c5dfcb381d3ca"><th class="cellrowborder" valign="top" width="19.24%" id="mcps1.2.4.1.1"><p id="en-us_topic_0013748726_a351cf2430e0e40d2bc4e0b8e509649bb"><a name="en-us_topic_0013748726_a351cf2430e0e40d2bc4e0b8e509649bb"></a><a name="en-us_topic_0013748726_a351cf2430e0e40d2bc4e0b8e509649bb"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="55.7%" id="mcps1.2.4.1.2"><p id="en-us_topic_0013748726_abf569c9e39bd4ba99a7ab37cc60e6883"><a name="en-us_topic_0013748726_abf569c9e39bd4ba99a7ab37cc60e6883"></a><a name="en-us_topic_0013748726_abf569c9e39bd4ba99a7ab37cc60e6883"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="25.06%" id="mcps1.2.4.1.3"><p id="en-us_topic_0013748726_af6ab204c10ca462f889acfe449817860"><a name="en-us_topic_0013748726_af6ab204c10ca462f889acfe449817860"></a><a name="en-us_topic_0013748726_af6ab204c10ca462f889acfe449817860"></a>Example Value</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0013748726_rc908647483fd4e478dc43fd83fcb6575"><td class="cellrowborder" valign="top" width="19.24%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0013748726_a22acb391d20242989d8f5dd96c13651f"><a name="en-us_topic_0013748726_a22acb391d20242989d8f5dd96c13651f"></a><a name="en-us_topic_0013748726_a22acb391d20242989d8f5dd96c13651f"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.7%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0013748726_a4b3e19d17d4141a5afca8cce53ac9383"><a name="en-us_topic_0013748726_a4b3e19d17d4141a5afca8cce53ac9383"></a><a name="en-us_topic_0013748726_a4b3e19d17d4141a5afca8cce53ac9383"></a>Specifies the subnet name.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0013748726_a2fa81825f84e4c2cad5544ee60356fc8"><a name="en-us_topic_0013748726_a2fa81825f84e4c2cad5544ee60356fc8"></a><a name="en-us_topic_0013748726_a2fa81825f84e4c2cad5544ee60356fc8"></a>Subnet</p>
    </td>
    </tr>
    <tr id="en-us_topic_0013748726_ra338f8572c2042b1909a2e07a43a1868"><td class="cellrowborder" valign="top" width="19.24%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0013748726_en-us_topic_0029397261_p39320517305"><a name="en-us_topic_0013748726_en-us_topic_0029397261_p39320517305"></a><a name="en-us_topic_0013748726_en-us_topic_0029397261_p39320517305"></a>CIDR</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.7%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0013748726_a9adafdbd17fa4d288fb3a60619789bb7"><a name="en-us_topic_0013748726_a9adafdbd17fa4d288fb3a60619789bb7"></a><a name="en-us_topic_0013748726_a9adafdbd17fa4d288fb3a60619789bb7"></a>Specifies the CIDR block for the subnet. This value must be within the VPC CIDR range.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0013748726_a4759f7fcda144bfaa8c0bbc806948e71"><a name="en-us_topic_0013748726_a4759f7fcda144bfaa8c0bbc806948e71"></a><a name="en-us_topic_0013748726_a4759f7fcda144bfaa8c0bbc806948e71"></a>192.168.0.0/24</p>
    </td>
    </tr>
    <tr id="en-us_topic_0013748726_ra7655f6b0a5c4d13a2b144962179f7c7"><td class="cellrowborder" valign="top" width="19.24%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0013748726_a143f3bcfe0154e18a8ea46a21b06c56f"><a name="en-us_topic_0013748726_a143f3bcfe0154e18a8ea46a21b06c56f"></a><a name="en-us_topic_0013748726_a143f3bcfe0154e18a8ea46a21b06c56f"></a>Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.7%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0013748726_en-us_topic_0029397261_p190934817305"><a name="en-us_topic_0013748726_en-us_topic_0029397261_p190934817305"></a><a name="en-us_topic_0013748726_en-us_topic_0029397261_p190934817305"></a>Specifies the gateway address of the subnet.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0013748726_a4ea86de1e68d4f31afd5550e894d9c4b"><a name="en-us_topic_0013748726_a4ea86de1e68d4f31afd5550e894d9c4b"></a><a name="en-us_topic_0013748726_a4ea86de1e68d4f31afd5550e894d9c4b"></a>192.168.0.1</p>
    </td>
    </tr>
    <tr id="en-us_topic_0013748726_row54331447162214"><td class="cellrowborder" valign="top" width="19.24%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0013748726_p8238528162216"><a name="en-us_topic_0013748726_p8238528162216"></a><a name="en-us_topic_0013748726_p8238528162216"></a>Tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.7%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0013748726_p63340999162216"><a name="en-us_topic_0013748726_p63340999162216"></a><a name="en-us_topic_0013748726_p63340999162216"></a>Specifies the subnet tag, which consists of a key and value pair. You can add a maximum of ten tags to each subnet.</p>
    <p id="en-us_topic_0013748726_p33198085162216"><a name="en-us_topic_0013748726_p33198085162216"></a><a name="en-us_topic_0013748726_p33198085162216"></a>The tag key and value must meet the requirements listed in <a href="#en-us_topic_0030971611__en-us_topic_0013748726_table4528555192814">Table 2</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0013748726_ul42213484162216"></a><a name="en-us_topic_0013748726_ul42213484162216"></a><ul id="en-us_topic_0013748726_ul42213484162216"><li id="en-us_topic_0013748726_li44377041162216"><a name="en-us_topic_0013748726_li44377041162216"></a><a name="en-us_topic_0013748726_li44377041162216"></a>Key: subnet_key1</li><li id="en-us_topic_0013748726_li63849049162216"><a name="en-us_topic_0013748726_li63849049162216"></a><a name="en-us_topic_0013748726_li63849049162216"></a>Value: subnet-01</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  Subnet tag key and value requirements

    <a name="en-us_topic_0013748726_table4528555192814"></a><table><thead align="left"><tr id="en-us_topic_0013748726_en-us_topic_0073603607_rd57708e01e6443a9805ca72f554fae7f"><th class="cellrowborder" valign="top" width="18.54%" id="mcps1.2.4.1.1"><p id="en-us_topic_0013748726_en-us_topic_0073603607_abc7708d69440476086850b219c70efa8"><a name="en-us_topic_0013748726_en-us_topic_0073603607_abc7708d69440476086850b219c70efa8"></a><a name="en-us_topic_0013748726_en-us_topic_0073603607_abc7708d69440476086850b219c70efa8"></a><strong id="en-us_topic_0013748726_en-us_topic_0073603607_b842352706165123"><a name="en-us_topic_0013748726_en-us_topic_0073603607_b842352706165123"></a><a name="en-us_topic_0013748726_en-us_topic_0073603607_b842352706165123"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.39%" id="mcps1.2.4.1.2"><p id="en-us_topic_0013748726_en-us_topic_0073603607_a0df2f83c3277432ab05b525e4ffb1c2c"><a name="en-us_topic_0013748726_en-us_topic_0073603607_a0df2f83c3277432ab05b525e4ffb1c2c"></a><a name="en-us_topic_0013748726_en-us_topic_0073603607_a0df2f83c3277432ab05b525e4ffb1c2c"></a><strong id="en-us_topic_0013748726_en-us_topic_0073603607_b842352706174218"><a name="en-us_topic_0013748726_en-us_topic_0073603607_b842352706174218"></a><a name="en-us_topic_0013748726_en-us_topic_0073603607_b842352706174218"></a>Requirements</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.07%" id="mcps1.2.4.1.3"><p id="en-us_topic_0013748726_en-us_topic_0073603607_a902e732241f94e96b0b1b718cf7ed639"><a name="en-us_topic_0013748726_en-us_topic_0073603607_a902e732241f94e96b0b1b718cf7ed639"></a><a name="en-us_topic_0013748726_en-us_topic_0073603607_a902e732241f94e96b0b1b718cf7ed639"></a><strong id="en-us_topic_0013748726_en-us_topic_0073603607_b842352706174227"><a name="en-us_topic_0013748726_en-us_topic_0073603607_b842352706174227"></a><a name="en-us_topic_0013748726_en-us_topic_0073603607_b842352706174227"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0013748726_en-us_topic_0073603607_r95612b479088487b99e620f90b71f798"><td class="cellrowborder" valign="top" width="18.54%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0013748726_en-us_topic_0073603607_a7694a48138124d1daf3804556a27bfd6"><a name="en-us_topic_0013748726_en-us_topic_0073603607_a7694a48138124d1daf3804556a27bfd6"></a><a name="en-us_topic_0013748726_en-us_topic_0073603607_a7694a48138124d1daf3804556a27bfd6"></a>Key</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.39%" headers="mcps1.2.4.1.2 "><a name="en-us_topic_0013748726_en-us_topic_0073603607_uac40e19ce4ac49d0913d48b334564c45"></a><a name="en-us_topic_0013748726_en-us_topic_0073603607_uac40e19ce4ac49d0913d48b334564c45"></a><ul id="en-us_topic_0013748726_en-us_topic_0073603607_uac40e19ce4ac49d0913d48b334564c45"><li id="en-us_topic_0013748726_en-us_topic_0073603607_l09e5379e37734886b85606e1a1512982"><a name="en-us_topic_0013748726_en-us_topic_0073603607_l09e5379e37734886b85606e1a1512982"></a><a name="en-us_topic_0013748726_en-us_topic_0073603607_l09e5379e37734886b85606e1a1512982"></a>Cannot be left blank.</li><li id="en-us_topic_0013748726_en-us_topic_0073603607_lf627e2e989ad4bf8a759780682976c4a"><a name="en-us_topic_0013748726_en-us_topic_0073603607_lf627e2e989ad4bf8a759780682976c4a"></a><a name="en-us_topic_0013748726_en-us_topic_0073603607_lf627e2e989ad4bf8a759780682976c4a"></a>Must be unique for each subnet.</li><li id="en-us_topic_0013748726_en-us_topic_0073603607_l740724b56b3948fdb336c21388d6e283"><a name="en-us_topic_0013748726_en-us_topic_0073603607_l740724b56b3948fdb336c21388d6e283"></a><a name="en-us_topic_0013748726_en-us_topic_0073603607_l740724b56b3948fdb336c21388d6e283"></a>Can contain a maximum of 36 characters.</li><li id="en-us_topic_0013748726_en-us_topic_0073603607_lb10c975c495c4de1bc52fc96d084697c"><a name="en-us_topic_0013748726_en-us_topic_0073603607_lb10c975c495c4de1bc52fc96d084697c"></a><a name="en-us_topic_0013748726_en-us_topic_0073603607_lb10c975c495c4de1bc52fc96d084697c"></a>Can contain only the following character types:<a name="en-us_topic_0013748726_en-us_topic_0073603607_uccb317c6616b4445aa84b125e5aa017f"></a><a name="en-us_topic_0013748726_en-us_topic_0073603607_uccb317c6616b4445aa84b125e5aa017f"></a><ul id="en-us_topic_0013748726_en-us_topic_0073603607_uccb317c6616b4445aa84b125e5aa017f"><li id="en-us_topic_0013748726_en-us_topic_0073603607_la4975a0b714d486381ef36c8599a4dae"><a name="en-us_topic_0013748726_en-us_topic_0073603607_la4975a0b714d486381ef36c8599a4dae"></a><a name="en-us_topic_0013748726_en-us_topic_0073603607_la4975a0b714d486381ef36c8599a4dae"></a>Uppercase letters</li><li id="en-us_topic_0013748726_en-us_topic_0073603607_l05872030add74e7ab50152845826fa0a"><a name="en-us_topic_0013748726_en-us_topic_0073603607_l05872030add74e7ab50152845826fa0a"></a><a name="en-us_topic_0013748726_en-us_topic_0073603607_l05872030add74e7ab50152845826fa0a"></a>Lowercase letters</li><li id="en-us_topic_0013748726_en-us_topic_0073603607_le70c062519174a9cae474c99c0f4f976"><a name="en-us_topic_0013748726_en-us_topic_0073603607_le70c062519174a9cae474c99c0f4f976"></a><a name="en-us_topic_0013748726_en-us_topic_0073603607_le70c062519174a9cae474c99c0f4f976"></a>Digits</li><li id="en-us_topic_0013748726_en-us_topic_0073603607_li77869551443"><a name="en-us_topic_0013748726_en-us_topic_0073603607_li77869551443"></a><a name="en-us_topic_0013748726_en-us_topic_0073603607_li77869551443"></a>Special characters, including hyphens (-) and underscores (_)</li></ul>
    </li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="28.07%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0013748726_en-us_topic_0073603607_a1a10de6d67c04555a3508a8cdc3500e7"><a name="en-us_topic_0013748726_en-us_topic_0073603607_a1a10de6d67c04555a3508a8cdc3500e7"></a><a name="en-us_topic_0013748726_en-us_topic_0073603607_a1a10de6d67c04555a3508a8cdc3500e7"></a>subnet_key1</p>
    </td>
    </tr>
    <tr id="en-us_topic_0013748726_en-us_topic_0073603607_r32a79d8bde844fda8a6254383317e58f"><td class="cellrowborder" valign="top" width="18.54%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0013748726_en-us_topic_0073603607_a1ebd1dda592448d49631c7f099519113"><a name="en-us_topic_0013748726_en-us_topic_0073603607_a1ebd1dda592448d49631c7f099519113"></a><a name="en-us_topic_0013748726_en-us_topic_0073603607_a1ebd1dda592448d49631c7f099519113"></a>Value</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.39%" headers="mcps1.2.4.1.2 "><a name="en-us_topic_0013748726_en-us_topic_0073603607_uaf17b1ea9b9a4e58b95cafefa2898283"></a><a name="en-us_topic_0013748726_en-us_topic_0073603607_uaf17b1ea9b9a4e58b95cafefa2898283"></a><ul id="en-us_topic_0013748726_en-us_topic_0073603607_uaf17b1ea9b9a4e58b95cafefa2898283"><li id="en-us_topic_0013748726_en-us_topic_0073603607_l88703260ac20431f961a641ebe7dbe00"><a name="en-us_topic_0013748726_en-us_topic_0073603607_l88703260ac20431f961a641ebe7dbe00"></a><a name="en-us_topic_0013748726_en-us_topic_0073603607_l88703260ac20431f961a641ebe7dbe00"></a>Can contain a maximum of 43 characters.</li><li id="en-us_topic_0013748726_en-us_topic_0073603607_lf4772afe9a8143b086ea935ee84656f3"><a name="en-us_topic_0013748726_en-us_topic_0073603607_lf4772afe9a8143b086ea935ee84656f3"></a><a name="en-us_topic_0013748726_en-us_topic_0073603607_lf4772afe9a8143b086ea935ee84656f3"></a>Can contain only the following character types:<a name="en-us_topic_0013748726_en-us_topic_0073603607_ub74c759faad544c3b4428accc9c42b80"></a><a name="en-us_topic_0013748726_en-us_topic_0073603607_ub74c759faad544c3b4428accc9c42b80"></a><ul id="en-us_topic_0013748726_en-us_topic_0073603607_ub74c759faad544c3b4428accc9c42b80"><li id="en-us_topic_0013748726_en-us_topic_0073603607_lf275cde186b24b9a9e3d4d52784a16ba"><a name="en-us_topic_0013748726_en-us_topic_0073603607_lf275cde186b24b9a9e3d4d52784a16ba"></a><a name="en-us_topic_0013748726_en-us_topic_0073603607_lf275cde186b24b9a9e3d4d52784a16ba"></a>Uppercase letters</li><li id="en-us_topic_0013748726_en-us_topic_0073603607_l3a58e993d925444bb0eba6c38feeedfb"><a name="en-us_topic_0013748726_en-us_topic_0073603607_l3a58e993d925444bb0eba6c38feeedfb"></a><a name="en-us_topic_0013748726_en-us_topic_0073603607_l3a58e993d925444bb0eba6c38feeedfb"></a>Lowercase letters</li><li id="en-us_topic_0013748726_en-us_topic_0073603607_l8679b69b2cd9428caecf8e14cafe5d4f"><a name="en-us_topic_0013748726_en-us_topic_0073603607_l8679b69b2cd9428caecf8e14cafe5d4f"></a><a name="en-us_topic_0013748726_en-us_topic_0073603607_l8679b69b2cd9428caecf8e14cafe5d4f"></a>Digits</li><li id="en-us_topic_0013748726_en-us_topic_0073603607_li13827436174517"><a name="en-us_topic_0013748726_en-us_topic_0073603607_li13827436174517"></a><a name="en-us_topic_0013748726_en-us_topic_0073603607_li13827436174517"></a>Special characters, including hyphens (-) and underscores (_)</li></ul>
    </li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="28.07%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0013748726_en-us_topic_0073603607_a21a035aeb72143f5ab0fd45a08248d08"><a name="en-us_topic_0013748726_en-us_topic_0073603607_a21a035aeb72143f5ab0fd45a08248d08"></a><a name="en-us_topic_0013748726_en-us_topic_0073603607_a21a035aeb72143f5ab0fd45a08248d08"></a>subnet-01</p>
    </td>
    </tr>
    </tbody>
    </table>

8.  The external DNS server address is used by default. If you need to change the DNS server address, select  **Custom** for **Advanced Settings**  and configure the DNS server addresses. You must ensure that the configured DNS server addresses are available.
9.  Click  **OK**.

## Precautions<a name="en-us_topic_0013748726_section231019253518"></a>

After a subnet is created, five IP addresses in the subnet will be reserved and cannot be used. For example, in a subnet with CIDR block 192.168.0.0/24, the following five IP addresses are reserved:

-   192.168.0.0: Network address.
-   192.168.0.1: Gateway address.
-   192.168.0.253: DHCP service address.
-   192.168.0.254: Reserved for the system interface. This IP address is used by the VPC for external communication.
-   192.168.0.255: Network broadcast address.

If you set  **Advanced Settings** to **Custom**  during subnet creation, the reserved IP addresses may be different from the preceding default ones. The system will reserve five IP addresses based on your subnet settings.

