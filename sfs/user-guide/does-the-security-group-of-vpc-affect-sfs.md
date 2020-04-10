# Does the Security Group of VPC Affect SFS?<a name="sfs_01_0081"></a>

A security group is a collection of access control rules for ECSs that have the same security protection requirements and are mutually trusted in a VPC. After a security group is created, you can create different access rules for the security group to protect the ECSs that are added to this security group. The default security group rule allows all outgoing data packets. ECSs in a security group can access each other without the need to add rules. The system creates a security group for each cloud account by default. Users can also create custom security groups by themselves.

When creating the security group, you need to add the inbound and outbound access rule, and enable the ports needed by the NFS protocol and DNS server of SFS to ensure that the file system can be successfully mounted. The port numbers required by the NFS protocol are  **111**,  **2049**,  **2050**,  **2051**, and  **2052**. The port number required by the DNS server is  **53**.

## **Example Value**<a name="section54544852203537"></a>

-   Inbound rule

    <a name="table54184017205651"></a>
    <table><thead align="left"><tr id="row35424582205651"><th class="cellrowborder" valign="top" id="mcps1.1.7.1.1"><p id="p50818907205651"><a name="p50818907205651"></a><a name="p50818907205651"></a>Direction</p>
    </th>
    <th class="cellrowborder" valign="top" id="mcps1.1.7.1.2"><p id="p22690788205651"><a name="p22690788205651"></a><a name="p22690788205651"></a>Protocol</p>
    </th>
    <th class="cellrowborder" valign="top" id="mcps1.1.7.1.3"><p id="p26014538205651"><a name="p26014538205651"></a><a name="p26014538205651"></a>Port Range</p>
    </th>
    <th class="cellrowborder" colspan="2" valign="top" id="mcps1.1.7.1.4"><p id="p26802804205651"><a name="p26802804205651"></a><a name="p26802804205651"></a>Source IP Address</p>
    </th>
    <th class="cellrowborder" valign="top" id="mcps1.1.7.1.5"><p id="p8223146205917"><a name="p8223146205917"></a><a name="p8223146205917"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row23543498205651"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.7.1.1 "><p id="p27975222205651"><a name="p27975222205651"></a><a name="p27975222205651"></a>Inbound</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.1.7.1.2 "><p id="p51400477205651"><a name="p51400477205651"></a><a name="p51400477205651"></a>TCP and UDP</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.1.7.1.3 "><p id="p2689129205651"><a name="p2689129205651"></a><a name="p2689129205651"></a>111</p>
    </td>
    <td class="cellrowborder" valign="top" width="9.090909090909092%" headers="mcps1.1.7.1.4 "><p id="p16492930205651"><a name="p16492930205651"></a><a name="p16492930205651"></a>IP Address</p>
    </td>
    <td class="cellrowborder" valign="top" width="9.090909090909092%" headers="mcps1.1.7.1.4 "><p id="p60858959205651"><a name="p60858959205651"></a><a name="p60858959205651"></a>0.0.0.0/0 (configurable)</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.38383838383839%" headers="mcps1.1.7.1.5 "><p id="p5197130205930"><a name="p5197130205930"></a><a name="p5197130205930"></a>One port corresponds to one access rule. You need to add information to the ports one by one.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Outbound rule

    <a name="table44923309203526"></a>
    <table><thead align="left"><tr id="row52561756203526"><th class="cellrowborder" valign="top" id="mcps1.1.7.1.1"><p id="p49783918204530"><a name="p49783918204530"></a><a name="p49783918204530"></a>Direction</p>
    </th>
    <th class="cellrowborder" valign="top" id="mcps1.1.7.1.2"><p id="p55722220204537"><a name="p55722220204537"></a><a name="p55722220204537"></a>Protocol</p>
    </th>
    <th class="cellrowborder" valign="top" id="mcps1.1.7.1.3"><p id="p11644070203526"><a name="p11644070203526"></a><a name="p11644070203526"></a>Port Range</p>
    </th>
    <th class="cellrowborder" colspan="2" valign="top" id="mcps1.1.7.1.4"><p id="p3645591203526"><a name="p3645591203526"></a><a name="p3645591203526"></a>Source IP Address</p>
    </th>
    <th class="cellrowborder" valign="top" id="mcps1.1.7.1.5"><p id="p8146189211017"><a name="p8146189211017"></a><a name="p8146189211017"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row26857486203526"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.7.1.1 "><p id="p13451176204530"><a name="p13451176204530"></a><a name="p13451176204530"></a>Outbound</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.7.1.2 "><p id="p51509273204537"><a name="p51509273204537"></a><a name="p51509273204537"></a>TCP and UDP</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.7.1.3 "><p id="p53386267203526"><a name="p53386267203526"></a><a name="p53386267203526"></a>111</p>
    </td>
    <td class="cellrowborder" valign="top" width="9%" headers="mcps1.1.7.1.4 "><p id="p29320371203526"><a name="p29320371203526"></a><a name="p29320371203526"></a>IP Address</p>
    </td>
    <td class="cellrowborder" valign="top" width="8%" headers="mcps1.1.7.1.4 "><p id="p37075380204554"><a name="p37075380204554"></a><a name="p37075380204554"></a>0.0.0.0/0 (configurable)</p>
    </td>
    <td class="cellrowborder" valign="top" width="38%" headers="mcps1.1.7.1.5 "><p id="p28494090211017"><a name="p28494090211017"></a><a name="p28494090211017"></a>One port corresponds to one access rule. You need to add information to the ports one by one.</p>
    </td>
    </tr>
    </tbody>
    </table>

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >The bidirectional access rule must be configured for port  **111**. The inbound rule can be set to the front-end service IP range of SFS. You can obtain it by running the following command:  **ping** _File system domain name or IP address_  or  **dig** _File system domain name or IP address_.  
    >For port  **2049**,  **2050**,  **2051**, and  **2052**, only the outbound rule needs to be added, which is the same as the outbound rule of port  **111**.  


