# \(Optional\) Step 5: Add a DNAT Rule<a name="nat_qs_0018"></a>

## Scenarios<a name="section1272311025717"></a>

After a NAT gateway is created, you can add DNAT rules to allow servers in your data center to provide services accessible from the Internet.

You can configure a DNAT rule for each port of a server. If there are multiple servers, you can create several DNAT rules to make servers share EIPs.

## Prerequisites<a name="section36544171152448"></a>

A NAT gateway has been created.

## Procedure<a name="section61166376152513"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  Under  **Network**, click  **NAT Gateway**.
4.  On the displayed page, click the name of the NAT gateway for which you want to add the DNAT rule.
5.  On the NAT gateway details page, click the  **DNAT Rules**  tab.
6.  Click  **Add DNAT Rule**.

    **Figure  1**  Add DNAT Rule<a name="fig1728320514312"></a>  
    ![](figures/add-dnat-rule-2.png "add-dnat-rule-2")

7.  Set the parameters as prompted. For details, see  [Table 1](#table30787259144637).

    **Table  1**  Parameter description

    <a name="table30787259144637"></a>
    <table><thead align="left"><tr id="row1287982144637"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.3.1.1"><p id="p66523784144637"><a name="p66523784144637"></a><a name="p66523784144637"></a><strong id="b954171111396"><a name="b954171111396"></a><a name="b954171111396"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="75%" id="mcps1.2.3.1.2"><p id="p19717393144637"><a name="p19717393144637"></a><a name="p19717393144637"></a><strong id="b1744611515396"><a name="b1744611515396"></a><a name="b1744611515396"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1684913403168"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="p930811171516"><a name="p930811171516"></a><a name="p930811171516"></a>Scenario</p>
    </td>
    <td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="p4320122201011"><a name="p4320122201011"></a><a name="p4320122201011"></a>Select <strong id="b1359354520489"><a name="b1359354520489"></a><a name="b1359354520489"></a>Direct Connect</strong> when servers in your data center need to access the Internet.</p>
    <p id="p555513762014"><a name="p555513762014"></a><a name="p555513762014"></a>Servers in your data center connected to a VPC using a Direct Connect or VPN connection can provide services accessible from the Internet through the DNAT rule.</p>
    </td>
    </tr>
    <tr id="row1895714384610"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="p11008481568"><a name="p11008481568"></a><a name="p11008481568"></a>Port Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="p181028481868"><a name="p181028481868"></a><a name="p181028481868"></a>Specifies the port type, including <strong id="b134254517595"><a name="b134254517595"></a><a name="b134254517595"></a>All ports</strong> and <strong id="b342511511590"><a name="b342511511590"></a><a name="b342511511590"></a>Specific port</strong>.</p>
    <a name="ul108491838102519"></a><a name="ul108491838102519"></a><ul id="ul108491838102519"><li><strong id="b93821147103912"><a name="b93821147103912"></a><a name="b93821147103912"></a>All ports</strong>: indicates the IP mapping method. This method is equivalent to assigning an EIP to a server. Any requests on the EIP will be forwarded by the NAT gateway to your server based on the mapping IP addresses.</li><li><strong id="b384531894018"><a name="b384531894018"></a><a name="b384531894018"></a>Specific port</strong>: indicates the port mapping method. The NAT gateway forwards the requests with specific protocol and port on the EIP to the corresponding port of the target server.</li></ul>
    </td>
    </tr>
    <tr id="row13591056167"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="p42842275144637"><a name="p42842275144637"></a><a name="p42842275144637"></a>Protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="p1747101415356"><a name="p1747101415356"></a><a name="p1747101415356"></a>The protocol can be TCP or UDP. This parameter is available if you select <strong id="b77461019134716"><a name="b77461019134716"></a><a name="b77461019134716"></a>Specific port</strong> for <strong id="b1674612199478"><a name="b1674612199478"></a><a name="b1674612199478"></a>Port Type</strong>. If you select <strong id="b15746171916477"><a name="b15746171916477"></a><a name="b15746171916477"></a>All ports</strong>, this parameter is <strong id="b1774771917476"><a name="b1774771917476"></a><a name="b1774771917476"></a>All</strong> by default.</p>
    </td>
    </tr>
    <tr id="row43238809144637"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="p1477472143719"><a name="p1477472143719"></a><a name="p1477472143719"></a>EIP</p>
    <p id="p1901342115116"><a name="p1901342115116"></a><a name="p1901342115116"></a></p>
    </td>
    <td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="p480029104814"><a name="p480029104814"></a><a name="p480029104814"></a>Specifies the EIP and port.</p>
    <p id="en-us_topic_0127293981_p578114194614"><a name="en-us_topic_0127293981_p578114194614"></a><a name="en-us_topic_0127293981_p578114194614"></a>You can only select an EIP that has not been bound, has been bound to a DNAT rule with <strong id="b57001541997"><a name="b57001541997"></a><a name="b57001541997"></a>Port Type</strong> set to <strong id="b14701454792"><a name="b14701454792"></a><a name="b14701454792"></a>Specific port</strong> of the current NAT gateway, or has been bound to an SNAT rule of the current NAT gateway.</p>
    </td>
    </tr>
    <tr id="row11271163819519"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="p1927110381657"><a name="p1927110381657"></a><a name="p1927110381657"></a>Outside Port</p>
    </td>
    <td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="p18696162813117"><a name="p18696162813117"></a><a name="p18696162813117"></a>Specifies the EIP port. This parameter is available if you select <strong id="b189781016292"><a name="b189781016292"></a><a name="b189781016292"></a>Specific port</strong> for <strong id="b14978913295"><a name="b14978913295"></a><a name="b14978913295"></a>Port Type</strong>. The port number must range from 1 to 65535.</p>
    <p id="p1213391252"><a name="p1213391252"></a><a name="p1213391252"></a>The value is a single port number, for example, 80.</p>
    </td>
    </tr>
    <tr id="row35593477144637"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="p64499384144637"><a name="p64499384144637"></a><a name="p64499384144637"></a>Private IP Address</p>
    </td>
    <td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="p57067624144637"><a name="p57067624144637"></a><a name="p57067624144637"></a>Specifies the IP address of the servers in the local data center or the user's private IP address. With DNAT, servers in your data center that are connected to a VPC through Direct Connect or VPN can provide services for the Internet using this private IP address. Configure the port of <strong id="b19130134917209"><a name="b19130134917209"></a><a name="b19130134917209"></a>Private IP Address</strong> if you select <strong id="b11130849132011"><a name="b11130849132011"></a><a name="b11130849132011"></a>Specific port</strong> for <strong id="b16130449142013"><a name="b16130449142013"></a><a name="b16130449142013"></a>Port Type</strong>.</p>
    <p id="p1012516592253"><a name="p1012516592253"></a><a name="p1012516592253"></a>This IP address is used by the server to provide services accessible from the Internet through DNAT.</p>
    </td>
    </tr>
    <tr id="row172121240365"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="p42222059865"><a name="p42222059865"></a><a name="p42222059865"></a>Inside Port</p>
    </td>
    <td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="p4994201474513"><a name="p4994201474513"></a><a name="p4994201474513"></a>Specifies the port of the server that provides services for the Internet through the DNAT rule. This parameter is available if you select <strong>Specific port</strong> for <strong>Port Type</strong>. The port number must range from 1 to 65535.</p>
    <p id="p22373473214"><a name="p22373473214"></a><a name="p22373473214"></a>The value is a single port number, for example, 80.</p>
    </td>
    </tr>
    </tbody>
    </table>

8.  Click  **OK**.

