# Adding a DNAT Rule<a name="en-us_topic_0127489530"></a>

## Scenarios<a name="en-us_topic_0127293986_section1272311025717"></a>

After a NAT gateway is created, you can add DNAT rules to allow servers in your VPC to provide services accessible from the Internet.

You can configure a DNAT rule for each port of a server. If multiple servers need to provide services accessible from the Internet, you need to create multiple DNAT rules.

## Prerequisites<a name="en-us_topic_0127293986_section36544171152448"></a>

A NAT gateway has been created.

## Procedure<a name="en-us_topic_0127293986_section61166376152513"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  Under  **Network**, click  **NAT Gateway**.
4.  On the displayed page, click the name of the NAT gateway for which you want to add the DNAT rule.
5.  On the NAT gateway details page, click the  **DNAT Rules**  tab.
6.  Click  **Add DNAT Rule**.

    >![](public_sys-resources/icon-notice.gif) **NOTICE:**   
    >You need to add security group rules to allow inbound or outbound traffic after you add a DNAT rule. Otherwise, the DNAT rule does not take effect.  

7.  Set the parameters as prompted. For details, see  [Table 1](#en-us_topic_0127293986_table30787259144637).

    **Table  1**  Parameter description

    <a name="en-us_topic_0127293986_table30787259144637"></a>
    <table><thead align="left"><tr id="en-us_topic_0127293986_row1287982144637"><th class="cellrowborder" valign="top" width="23.189999999999998%" id="mcps1.2.3.1.1"><p id="en-us_topic_0127293986_p66523784144637"><a name="en-us_topic_0127293986_p66523784144637"></a><a name="en-us_topic_0127293986_p66523784144637"></a><strong id="b9146819105510"><a name="b9146819105510"></a><a name="b9146819105510"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="76.81%" id="mcps1.2.3.1.2"><p id="en-us_topic_0127293986_p19717393144637"><a name="en-us_topic_0127293986_p19717393144637"></a><a name="en-us_topic_0127293986_p19717393144637"></a><strong id="b6509122011557"><a name="b6509122011557"></a><a name="b6509122011557"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0127293986_row20452749101411"><td class="cellrowborder" valign="top" width="23.189999999999998%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0127293986_p930811171516"><a name="en-us_topic_0127293986_p930811171516"></a><a name="en-us_topic_0127293986_p930811171516"></a>Scenario</p>
    </td>
    <td class="cellrowborder" valign="top" width="76.81%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0127293986_p82551491578"><a name="en-us_topic_0127293986_p82551491578"></a><a name="en-us_topic_0127293986_p82551491578"></a><strong id="b1883613173385"><a name="b1883613173385"></a><a name="b1883613173385"></a>VPC</strong>: indicates the VPC scenario where all servers in the subnet share one EIP to provide services accessible from the Internet through the DNAT rule.</p>
    <p id="p191738561313"><a name="p191738561313"></a><a name="p191738561313"></a><strong id="b171121219135611"><a name="b171121219135611"></a><a name="b171121219135611"></a>Direct Connect</strong>: indicates that servers in your data center connected to a VPC using a Direct Connect or VPN connection can provide services accessible from the Internet through the DNAT rule.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0127293986_row1895714384610"><td class="cellrowborder" valign="top" width="23.189999999999998%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0127293986_p11008481568"><a name="en-us_topic_0127293986_p11008481568"></a><a name="en-us_topic_0127293986_p11008481568"></a>Port Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="76.81%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0127293986_p181028481868"><a name="en-us_topic_0127293986_p181028481868"></a><a name="en-us_topic_0127293986_p181028481868"></a>Specifies the port type, including <strong id="b1268910328141"><a name="b1268910328141"></a><a name="b1268910328141"></a>All ports</strong> and <strong id="b166919323147"><a name="b166919323147"></a><a name="b166919323147"></a>Specific port</strong>.</p>
    <a name="ul410617281189"></a><a name="ul410617281189"></a><ul id="ul410617281189"><li><strong id="b14883135318591"><a name="b14883135318591"></a><a name="b14883135318591"></a>All ports</strong>: indicates the IP mapping method. This method is equivalent to assigning an EIP to a server. Any requests on the EIP will be forwarded by the NAT gateway to your server based on the mapping IP addresses.</li><li><strong id="b28132101011"><a name="b28132101011"></a><a name="b28132101011"></a>Specific port</strong>: indicates the port mapping method. The NAT gateway forwards the requests with specific protocol and port on the EIP to the corresponding port of the target server.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0127293986_row13591056167"><td class="cellrowborder" valign="top" width="23.189999999999998%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0127293986_p42842275144637"><a name="en-us_topic_0127293986_p42842275144637"></a><a name="en-us_topic_0127293986_p42842275144637"></a>Protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="76.81%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0127293986_p1747101415356"><a name="en-us_topic_0127293986_p1747101415356"></a><a name="en-us_topic_0127293986_p1747101415356"></a>The protocol type can be TCP or UDP. This parameter is available if you select <strong id="b109348376481"><a name="b109348376481"></a><a name="b109348376481"></a>Specific port</strong> for <strong id="b14934123794815"><a name="b14934123794815"></a><a name="b14934123794815"></a>Port Type</strong>. If you select <strong id="b17935203774810"><a name="b17935203774810"></a><a name="b17935203774810"></a>All ports</strong>, this parameter is <strong id="b179351137164815"><a name="b179351137164815"></a><a name="b179351137164815"></a>All</strong> by default.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0127293986_row43238809144637"><td class="cellrowborder" valign="top" width="23.189999999999998%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0127293986_p1448715913116"><a name="en-us_topic_0127293986_p1448715913116"></a><a name="en-us_topic_0127293986_p1448715913116"></a>EIP</p>
    <p id="en-us_topic_0127293986_p1901342115116"><a name="en-us_topic_0127293986_p1901342115116"></a><a name="en-us_topic_0127293986_p1901342115116"></a></p>
    </td>
    <td class="cellrowborder" valign="top" width="76.81%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0127293986_p480029104814"><a name="en-us_topic_0127293986_p480029104814"></a><a name="en-us_topic_0127293986_p480029104814"></a>Specifies the EIP and port.</p>
    <p id="en-us_topic_0127293981_p578114194614"><a name="en-us_topic_0127293981_p578114194614"></a><a name="en-us_topic_0127293981_p578114194614"></a>You can only select an EIP that has not been bound, has been bound to a DNAT rule with <strong id="b150710921210"><a name="b150710921210"></a><a name="b150710921210"></a>Port Type</strong> set to <strong id="b550711971218"><a name="b550711971218"></a><a name="b550711971218"></a>Specific port</strong> of the current NAT gateway, or has been bound to an SNAT rule of the current NAT gateway.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0127293986_row189841183384"><td class="cellrowborder" valign="top" width="23.189999999999998%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0127293986_p89861618173810"><a name="en-us_topic_0127293986_p89861618173810"></a><a name="en-us_topic_0127293986_p89861618173810"></a>Outside Port</p>
    </td>
    <td class="cellrowborder" valign="top" width="76.81%" headers="mcps1.2.3.1.2 "><p id="p18986618153813"><a name="p18986618153813"></a><a name="p18986618153813"></a>Specifies the EIP port. This parameter is available if you select <strong id="b6624204065118"><a name="b6624204065118"></a><a name="b6624204065118"></a>Specific port</strong> for <strong id="b962517403514"><a name="b962517403514"></a><a name="b962517403514"></a>Port Type</strong>. The port number must range from 1 to 65535.</p>
    <p id="p1213391252"><a name="p1213391252"></a><a name="p1213391252"></a>The value is a single port number, for example, 80.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0127293986_row35593477144637"><td class="cellrowborder" valign="top" width="23.189999999999998%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0127293986_p64499384144637"><a name="en-us_topic_0127293986_p64499384144637"></a><a name="en-us_topic_0127293986_p64499384144637"></a>Private IP Address</p>
    </td>
    <td class="cellrowborder" valign="top" width="76.81%" headers="mcps1.2.3.1.2 "><a name="ul6112191010186"></a><a name="ul6112191010186"></a><ul id="ul6112191010186"><li>In the VPC scenario, set this parameter to the IP address of the server in a VPC. This IP address is used by the server to provide services accessible from the Internet through DNAT.</li><li>In the Direct Connect scenario, set this parameter to IP address of the server in the local data center or the user's private IP address. This IP address is used by local servers that are connected to a VPC through Direct Connect or VPN to provide services for the Internet through DNAT.</li><li>Configure the port of <strong id="b842352706174822"><a name="b842352706174822"></a><a name="b842352706174822"></a>Private IP Address</strong> if you select <strong id="b2915537113914"><a name="b2915537113914"></a><a name="b2915537113914"></a>Specific port</strong> for <strong id="b119151372397"><a name="b119151372397"></a><a name="b119151372397"></a>Port Type</strong>.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0127293986_row1423724123219"><td class="cellrowborder" valign="top" width="23.189999999999998%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0127293986_p1323715410320"><a name="en-us_topic_0127293986_p1323715410320"></a><a name="en-us_topic_0127293986_p1323715410320"></a>Inside Port</p>
    </td>
    <td class="cellrowborder" valign="top" width="76.81%" headers="mcps1.2.3.1.2 "><p id="p4994201474513"><a name="p4994201474513"></a><a name="p4994201474513"></a>Specifies the port of the server that provides services for the Internet through the DNAT rule. This parameter is available if you select <strong id="b14358195925117"><a name="b14358195925117"></a><a name="b14358195925117"></a>Specific port</strong> for <strong id="b735935955110"><a name="b735935955110"></a><a name="b735935955110"></a>Port Type</strong>. The port number must range from 1 to 65535.</p>
    <p id="p22373473214"><a name="p22373473214"></a><a name="p22373473214"></a>The value is a single port number, for example, 80.</p>
    </td>
    </tr>
    </tbody>
    </table>

8.  After the configuration is complete, click  **OK**. Once the rule is created, its status changes to  **Running**.

