# Step 3: Add a DNAT Rule<a name="nat_qs_0010"></a>

## Scenarios<a name="section1272311025717"></a>

After a NAT gateway is created, you can add DNAT rules to allow servers in your VPC to provide services accessible from the Internet.

You can configure a DNAT rule for each port of a server. If multiple servers need to provide services accessible from the Internet, you need to create multiple DNAT rules.

## Prerequisites<a name="section36544171152448"></a>

A NAT gateway has been created.

## Procedure<a name="section61166376152513"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  Under  **Network**, click  **NAT Gateway**.
4.  On the displayed page, click the name of the NAT gateway for which you want to add the DNAT rule.
5.  On the NAT gateway details page, click the  **DNAT Rules**  tab.
6.  Click  **Add DNAT Rule**.

    **Figure  1**  Add DNAT Rule<a name="fig648232499"></a>  
    ![](figures/add-dnat-rule.png "add-dnat-rule")

7.  Set the parameters as prompted. For details, see  [Table 1](#table30787259144637).

    **Table  1**  Parameter description

    <a name="table30787259144637"></a>
    <table><thead align="left"><tr id="row1287982144637"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.3.1.1"><p id="p66523784144637"><a name="p66523784144637"></a><a name="p66523784144637"></a><strong id="b11637162712319"><a name="b11637162712319"></a><a name="b11637162712319"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="75%" id="mcps1.2.3.1.2"><p id="p19717393144637"><a name="p19717393144637"></a><a name="p19717393144637"></a><strong id="b1249912811318"><a name="b1249912811318"></a><a name="b1249912811318"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row20452749101411"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="p930811171516"><a name="p930811171516"></a><a name="p930811171516"></a>Scenario</p>
    </td>
    <td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="p82551491578"><a name="p82551491578"></a><a name="p82551491578"></a>Select <strong id="b13126164315525"><a name="b13126164315525"></a><a name="b13126164315525"></a>VPC</strong> when your servers use the DNAT rule to provide services accessible from the Internet.</p>
    <p id="p69201244181513"><a name="p69201244181513"></a><a name="p69201244181513"></a>Servers in the VPC can share one EIP to provide services accessible from the Internet.</p>
    </td>
    </tr>
    <tr id="row1895714384610"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="p11008481568"><a name="p11008481568"></a><a name="p11008481568"></a>Port Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="p181028481868"><a name="p181028481868"></a><a name="p181028481868"></a>Specifies the port type, including <strong id="b134254517595"><a name="b134254517595"></a><a name="b134254517595"></a>All ports</strong> and <strong id="b342511511590"><a name="b342511511590"></a><a name="b342511511590"></a>Specific port</strong>.</p>
    <a name="ul2946142220261"></a><a name="ul2946142220261"></a><ul id="ul2946142220261"><li><strong id="b36175279414"><a name="b36175279414"></a><a name="b36175279414"></a>All ports</strong>: indicates the IP mapping method. This method is equivalent to assigning an EIP to a server. Any requests on the EIP will be forwarded by the NAT gateway to your server based on the mapping IP addresses.</li><li><strong id="b185517286191"><a name="b185517286191"></a><a name="b185517286191"></a>Specific port</strong>: indicates the port mapping method. The NAT gateway forwards the requests with specific protocol and port on the EIP to the corresponding port of the target server.</li></ul>
    </td>
    </tr>
    <tr id="row13591056167"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="p42842275144637"><a name="p42842275144637"></a><a name="p42842275144637"></a>Protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="p1747101415356"><a name="p1747101415356"></a><a name="p1747101415356"></a>The protocol can be TCP or UDP. This parameter is available if you select <strong id="b1775485544614"><a name="b1775485544614"></a><a name="b1775485544614"></a>Specific port</strong> for <strong id="b16755255124616"><a name="b16755255124616"></a><a name="b16755255124616"></a>Port Type</strong>. If you select <strong id="b13755155512467"><a name="b13755155512467"></a><a name="b13755155512467"></a>All ports</strong>, this parameter is <strong id="b117551455144617"><a name="b117551455144617"></a><a name="b117551455144617"></a>All</strong> by default.</p>
    </td>
    </tr>
    <tr id="row43238809144637"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="p1448715913116"><a name="p1448715913116"></a><a name="p1448715913116"></a>EIP</p>
    <p id="p1901342115116"><a name="p1901342115116"></a><a name="p1901342115116"></a></p>
    </td>
    <td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="p480029104814"><a name="p480029104814"></a><a name="p480029104814"></a>Specifies the EIP and port.</p>
    <p id="en-us_topic_0127293981_p578114194614"><a name="en-us_topic_0127293981_p578114194614"></a><a name="en-us_topic_0127293981_p578114194614"></a>You can only select an EIP that has not been bound, has been bound to a DNAT rule with <strong id="b16811155815414"><a name="b16811155815414"></a><a name="b16811155815414"></a>Port Type</strong> set to <strong id="b1381265884112"><a name="b1381265884112"></a><a name="b1381265884112"></a>Specific port</strong> of the current NAT gateway, or has been bound to an SNAT rule of the current NAT gateway.</p>
    </td>
    </tr>
    <tr id="row189841183384"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="p89861618173810"><a name="p89861618173810"></a><a name="p89861618173810"></a>Outside Port</p>
    </td>
    <td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="p18986618153813"><a name="p18986618153813"></a><a name="p18986618153813"></a>Specifies the EIP port. This parameter is available if you select <strong id="b0109471190"><a name="b0109471190"></a><a name="b0109471190"></a>Specific port</strong> for <strong id="b9122047171914"><a name="b9122047171914"></a><a name="b9122047171914"></a>Port Type</strong>. The port number must range from 1 to 65535.</p>
    <p id="p1213391252"><a name="p1213391252"></a><a name="p1213391252"></a>The value is a single port number, for example, 80.</p>
    </td>
    </tr>
    <tr id="row35593477144637"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="p64499384144637"><a name="p64499384144637"></a><a name="p64499384144637"></a>Private IP Address</p>
    </td>
    <td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="p47826341544"><a name="p47826341544"></a><a name="p47826341544"></a>Specifies the IP address of the server that provides services for the Internet through the DNAT rule.</p>
    <p id="p6921952172615"><a name="p6921952172615"></a><a name="p6921952172615"></a>Configure the port of <strong id="b1580810372202"><a name="b1580810372202"></a><a name="b1580810372202"></a>Private IP Address</strong> if you select <strong id="b1280853772014"><a name="b1280853772014"></a><a name="b1280853772014"></a>Specific port</strong> for <strong id="b18087378202"><a name="b18087378202"></a><a name="b18087378202"></a>Port Type</strong>.</p>
    </td>
    </tr>
    <tr id="row1423724123219"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="p1323715410320"><a name="p1323715410320"></a><a name="p1323715410320"></a>Inside Port</p>
    </td>
    <td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="p4994201474513"><a name="p4994201474513"></a><a name="p4994201474513"></a>Specifies the port of the server that provides services for the Internet through the DNAT rule. This parameter is available if you select <strong id="b11757104291211"><a name="b11757104291211"></a><a name="b11757104291211"></a>Specific port</strong> for <strong id="b19758742161218"><a name="b19758742161218"></a><a name="b19758742161218"></a>Port Type</strong>. The port number must range from 1 to 65535.</p>
    <p id="p22373473214"><a name="p22373473214"></a><a name="p22373473214"></a>The value is a single port number, for example, 80.</p>
    </td>
    </tr>
    </tbody>
    </table>

8.  Click  **OK**.

