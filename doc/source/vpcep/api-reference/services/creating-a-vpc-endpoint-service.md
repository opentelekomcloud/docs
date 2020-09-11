# Creating a VPC Endpoint Service<a name="vpcep_06_0201"></a>

## Function<a name="section49369256"></a>

This API is used to create a VPC endpoint service. Other users can create a VPC endpoint to connect to the endpoint service.

>![](/images/icon-note.gif) **NOTE:** 
>This API is an asynchronous interface. If it is successfully invoked, status code  **200**  is returned, indicating that the request has been successfully delivered. It takes 1 to 2 minutes to create a VPC endpoint service. You can view the creation result by performing operations in  [Querying Details of a VPC Endpoint Service](querying-details-of-a-vpc-endpoint-service.md).

## URI<a name="section41670120"></a>

POST /v1/\{project\_id\}/vpc-endpoint-services

[Table 1](#d0e2135)  describes the required parameters.

**Table  1**  Parameters

<a name="d0e2135"></a>
<table><thead align="left"><tr id="row8845746"><th class="cellrowborder" valign="top" width="27%" id="mcps1.2.4.1.1"><p id="p45416839"><a name="p45416839"></a><a name="p45416839"></a><strong id="b6872143614716"><a name="b6872143614716"></a><a name="b6872143614716"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="32%" id="mcps1.2.4.1.2"><p id="p54885328"><a name="p54885328"></a><a name="p54885328"></a><strong id="b84235270619640"><a name="b84235270619640"></a><a name="b84235270619640"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="41%" id="mcps1.2.4.1.3"><p id="p16526582"><a name="p16526582"></a><a name="p16526582"></a><strong id="b1320433479"><a name="b1320433479"></a><a name="b1320433479"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row63584736"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.1 "><p id="p50089974"><a name="p50089974"></a><a name="p50089974"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="p30756130"><a name="p30756130"></a><a name="p30756130"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="41%" headers="mcps1.2.4.1.3 "><p id="p8218569"><a name="p8218569"></a><a name="p8218569"></a>Specifies the project ID. For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section39486763"></a>

-   Parameter description

    **Table  2**  Request parameters

    <a name="ref520834027"></a>
    <table><thead align="left"><tr id="row4849437"><th class="cellrowborder" valign="top" width="18.181818181818183%" id="mcps1.2.5.1.1"><p id="p57260105"><a name="p57260105"></a><a name="p57260105"></a><strong id="b796910283482"><a name="b796910283482"></a><a name="b796910283482"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.191919191919194%" id="mcps1.2.5.1.2"><p id="p7556889"><a name="p7556889"></a><a name="p7556889"></a><strong id="b2115490898"><a name="b2115490898"></a><a name="b2115490898"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="13.131313131313133%" id="mcps1.2.5.1.3"><p id="p8128245"><a name="p8128245"></a><a name="p8128245"></a><strong id="b1501836154812"><a name="b1501836154812"></a><a name="b1501836154812"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="49.494949494949495%" id="mcps1.2.5.1.4"><p id="p54408134"><a name="p54408134"></a><a name="p54408134"></a><strong id="b1939355184"><a name="b1939355184"></a><a name="b1939355184"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row44982772"><td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.1 "><p id="p19725926"><a name="p19725926"></a><a name="p19725926"></a>port_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.2 "><p id="p54296197"><a name="p54296197"></a><a name="p54296197"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.3 "><p id="p35915832"><a name="p35915832"></a><a name="p35915832"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.2.5.1.4 "><p id="p1984135532819"><a name="p1984135532819"></a><a name="p1984135532819"></a>Specifies the ID for identifying the backend resource of the VPC endpoint service. The ID is in the form of the UUID.</p>
    <p id="p23501288"><a name="p23501288"></a><a name="p23501288"></a>The value is as follows:</p>
    <a name="ul930495217232"></a><a name="ul930495217232"></a><ul id="ul930495217232"><li>If the backend service is an enhanced load balancer, the value is the ID of the port bound to the private IP address of the load balancer. For details, see response field <strong id="b760615179297"><a name="b760615179297"></a><a name="b760615179297"></a>vip_port_id</strong> in <a href="https://docs.otc.t-systems.com/en-us/api/elb/en-us_topic_0141008271.html" target="_blank" rel="noopener noreferrer">Querying Details of a Load Balancer</a> in the <em id="i454205722813"><a name="i454205722813"></a><a name="i454205722813"></a>Elastic Load Balance API Reference</em>.</li><li>If the backend resource is an ECS, the value is the NIC ID of the ECS where the VPC endpoint service is deployed. For details, see <a href="https://docs.otc.t-systems.com/en-us/api/ecs/en-us_topic_0020212662.html" target="_blank" rel="noopener noreferrer">Querying NICs of an ECS</a> in the <em id="i8649112044"><a name="i8649112044"></a><a name="i8649112044"></a>Elastic Load Balance API Reference</em>.</li><li>If the backend resource is a virtual IP address, the value is the NIC ID of the physical server where virtual resources are created.</li></ul>
    <div class="note" id="note246113343810"><a name="note246113343810"></a><a name="note246113343810"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul846143103818"></a><a name="ul846143103818"></a><ul id="ul846143103818"><li>To create a VPC endpoint service, the CIDR block of the VPC where the VPC endpoint service is deployed cannot overlap with 198.19.128.0/20.</li><li>The destination address of the custom route in the VPC route table cannot overlap with 198.19.128.0/20.</li></ul>
    </div></div>
    </td>
    </tr>
    <tr id="row970518853214"><td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.1 "><p id="p244314143323"><a name="p244314143323"></a><a name="p244314143323"></a>pool_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.2 "><p id="p124439147323"><a name="p124439147323"></a><a name="p124439147323"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.3 "><p id="p1644381433213"><a name="p1644381433213"></a><a name="p1644381433213"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.2.5.1.4 "><p id="p6443514133211"><a name="p6443514133211"></a><a name="p6443514133211"></a>Specifies the ID of the cluster associated with the target VPCEP resource.</p>
    </td>
    </tr>
    <tr id="row12740175511711"><td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.1 "><p id="p157419556179"><a name="p157419556179"></a><a name="p157419556179"></a>vip_port_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.2 "><p id="p8742155520176"><a name="p8742155520176"></a><a name="p8742155520176"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.3 "><p id="p10742185591714"><a name="p10742185591714"></a><a name="p10742185591714"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.2.5.1.4 "><p id="p12742155131712"><a name="p12742155131712"></a><a name="p12742155131712"></a>Specifies the ID of the virtual NIC to which the virtual IP address is bound.</p>
    </td>
    </tr>
    <tr id="row1729441514442"><td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.1 "><p id="p15295815134415"><a name="p15295815134415"></a><a name="p15295815134415"></a>service_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.2 "><p id="p6296815164417"><a name="p6296815164417"></a><a name="p6296815164417"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.3 "><p id="p629611150441"><a name="p629611150441"></a><a name="p629611150441"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.2.5.1.4 "><p id="p1970935114472"><a name="p1970935114472"></a><a name="p1970935114472"></a>Specifies the name of the VPC endpoint service. The value contains a maximum of 16 characters, including letters, digits, underscores (_), and hyphens (-).</p>
    <a name="ul16118939152215"></a><a name="ul16118939152215"></a><ul id="ul16118939152215"><li>If you do not specify this parameter, the VPC endpoint service name is in the format: <strong id="b124119223595"><a name="b124119223595"></a><a name="b124119223595"></a>regionName.serviceId</strong>.</li><li>If you specify this parameter, the VPC endpoint service name is in the format: <strong id="b1540117284016"><a name="b1540117284016"></a><a name="b1540117284016"></a>regionName.serviceName.serviceId</strong>.</li></ul>
    </td>
    </tr>
    <tr id="row11878883"><td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.1 "><p id="p22665468"><a name="p22665468"></a><a name="p22665468"></a>vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.2 "><p id="p23963654"><a name="p23963654"></a><a name="p23963654"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.3 "><p id="p62007849"><a name="p62007849"></a><a name="p62007849"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.2.5.1.4 "><p id="p1490095811316"><a name="p1490095811316"></a><a name="p1490095811316"></a>Specifies the ID of the VPC to which the backend resource of the VPC endpoint service belongs.</p>
    <p id="p161940143417"><a name="p161940143417"></a><a name="p161940143417"></a>For details, see response field <strong id="b9758154713317"><a name="b9758154713317"></a><a name="b9758154713317"></a>id</strong> in <a href="https://docs.otc.t-systems.com/api/vpc/vpc_api01_0002.html" target="_blank" rel="noopener noreferrer">Querying VPC Details</a> in the <em id="i12759144715337"><a name="i12759144715337"></a><a name="i12759144715337"></a>Virtual Private Cloud API Reference</em>.</p>
    </td>
    </tr>
    <tr id="row39456621"><td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.1 "><p id="p41869715"><a name="p41869715"></a><a name="p41869715"></a>approval_enabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.2 "><p id="p36003791"><a name="p36003791"></a><a name="p36003791"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.3 "><p id="p30625926"><a name="p30625926"></a><a name="p30625926"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.2.5.1.4 "><p id="p0379724124813"><a name="p0379724124813"></a><a name="p0379724124813"></a>Specifies whether connection approval is required.</p>
    <a name="ul11323972220"></a><a name="ul11323972220"></a><ul id="ul11323972220"><li><strong id="b75811234123816"><a name="b75811234123816"></a><a name="b75811234123816"></a>false</strong>: indicates that connection approval is not required. The created VPC endpoint is in the <strong id="b78271532134215"><a name="b78271532134215"></a><a name="b78271532134215"></a>Accepted</strong> state.</li><li><strong id="b15111167142314"><a name="b15111167142314"></a><a name="b15111167142314"></a>true</strong>: indicates that connection approval is required. The created VPC endpoint is in the <strong id="b109861945115019"><a name="b109861945115019"></a><a name="b109861945115019"></a>Pending acceptance</strong> state until the owner of the associated VPC endpoint service approves the connection.</li></ul>
    <p id="p1138312242488"><a name="p1138312242488"></a><a name="p1138312242488"></a>The default value is <strong id="b1593639103810"><a name="b1593639103810"></a><a name="b1593639103810"></a>true</strong>.</p>
    </td>
    </tr>
    <tr id="row27461928"><td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.1 "><p id="p9823714"><a name="p9823714"></a><a name="p9823714"></a>service_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.2 "><p id="p57523360"><a name="p57523360"></a><a name="p57523360"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.3 "><p id="p28880587"><a name="p28880587"></a><a name="p28880587"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.2.5.1.4 "><p id="p08121553172517"><a name="p08121553172517"></a><a name="p08121553172517"></a>Specifies the type of the VPC endpoint service. Only your private services can be configured into interface VPC endpoint services.</p>
    <div class="p" id="p767124834219"><a name="p767124834219"></a><a name="p767124834219"></a>There are two types of VPC endpoint services: interface and gateway.<a name="ul87241928184613"></a><a name="ul87241928184613"></a><ul id="ul87241928184613"><li>Gateway: VPC endpoint services of this type are configured by operations people. You can use them directly without the need to create one by yourselves.</li><li>Interface: VPC endpoint services of this type include cloud services configured by operations people and private services created by yourselves. You cannot configure these cloud services, but can use them.</li></ul>
    </div>
    <p id="p1318010403317"><a name="p1318010403317"></a><a name="p1318010403317"></a>You can view those VPC endpoint services that are configured by operations people and are visible and accessible to all users. For detailed steps, see <a href="querying-public-vpc-endpoint-services.md">Querying Public VPC Endpoint Services</a>. Perform the operations in <a href="creating-a-vpc-endpoint.md">Creating a VPC Endpoint</a> to create VPC endpoints for accessing VPC endpoint services of the gateway type and interface type.</p>
    </td>
    </tr>
    <tr id="row37209478"><td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.1 "><p id="p61177702"><a name="p61177702"></a><a name="p61177702"></a>server_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.2 "><p id="p56446802"><a name="p56446802"></a><a name="p56446802"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.3 "><p id="p8788275"><a name="p8788275"></a><a name="p8788275"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.2.5.1.4 "><p id="p139061546194411"><a name="p139061546194411"></a><a name="p139061546194411"></a>Specifies the resource type.</p>
    <a name="ul093471482216"></a><a name="ul093471482216"></a><ul id="ul093471482216"><li><strong id="b18688124125214"><a name="b18688124125214"></a><a name="b18688124125214"></a>VM</strong>: Select this value if the backend resource is an ECS. Backend resources of this type serve as servers.</li><li><strong id="b1862905514533"><a name="b1862905514533"></a><a name="b1862905514533"></a>VIP</strong>: Select this value if the backend resource is a virtual IP address that functions as a physical server hosting virtual resources.</li><li><strong id="b16791645512"><a name="b16791645512"></a><a name="b16791645512"></a>LB</strong>: Select this value if the backend resource is an enhanced load balancer. Backend resources of this type suit services that receive high access traffic and demand high reliability and disaster recovery (DR) performance.</li></ul>
    </td>
    </tr>
    <tr id="row8780066"><td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.1 "><p id="p40096741"><a name="p40096741"></a><a name="p40096741"></a>ports</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.2 "><p id="p26610597"><a name="p26610597"></a><a name="p26610597"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.3 "><p id="p7974729"><a name="p7974729"></a><a name="p7974729"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.2.5.1.4 "><p id="p5656200651"><a name="p5656200651"></a><a name="p5656200651"></a>Lists the port mappings opened to the VPC endpoint service. For details, see <a href="#table56834929">Table 3</a>.</p>
    <p id="p41973306"><a name="p41973306"></a><a name="p41973306"></a>Duplicate port mappings are not allowed in the same VPC endpoint service. If multiple VPC endpoint services share the same <strong id="b19168134611101"><a name="b19168134611101"></a><a name="b19168134611101"></a>port_id</strong> value, service ports and terminal ports of all these endpoint services cannot be duplicated when the protocol is the same. A maximum of 200 port mappings can be created at a time.</p>
    </td>
    </tr>
    <tr id="row191058366348"><td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.1 "><p id="p6679144311349"><a name="p6679144311349"></a><a name="p6679144311349"></a>tcp_proxy</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.2 "><p id="p1867920439347"><a name="p1867920439347"></a><a name="p1867920439347"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.3 "><p id="p368018439344"><a name="p368018439344"></a><a name="p368018439344"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.2.5.1.4 "><p id="p17290163812450"><a name="p17290163812450"></a><a name="p17290163812450"></a>Specifies whether the client IP address and port number or <strong id="b1340623194912"><a name="b1340623194912"></a><a name="b1340623194912"></a>marker_id</strong> information is transmitted to the server. The following methods are supported:</p>
    <a name="ul18589152018359"></a><a name="ul18589152018359"></a><ul id="ul18589152018359"><li>TCP TOA: The client information is inserted into field <strong id="b1328024583915"><a name="b1328024583915"></a><a name="b1328024583915"></a>tcp option</strong> and transmitted to the server.</li><li>Proxy Protocol: The client information is inserted into field <strong id="b18340846124016"><a name="b18340846124016"></a><a name="b18340846124016"></a>tcp payload</strong> and transmitted to the server.</li></ul>
    <p id="p2849528112718"><a name="p2849528112718"></a><a name="p2849528112718"></a>This parameter is available only when the server can parse fields <strong id="b1246063817713"><a name="b1246063817713"></a><a name="b1246063817713"></a>tcp option</strong> and <strong id="b832154415710"><a name="b832154415710"></a><a name="b832154415710"></a>tcp payload</strong>.</p>
    <p id="p12999539124717"><a name="p12999539124717"></a><a name="p12999539124717"></a>The values are as follows:</p>
    <a name="ul10684011476"></a><a name="ul10684011476"></a><ul id="ul10684011476"><li><strong id="b485111422"><a name="b485111422"></a><a name="b485111422"></a>close</strong>: indicates that the TOA and Proxy Protocol methods are neither used.</li><li><strong id="b1432825911248"><a name="b1432825911248"></a><a name="b1432825911248"></a>toa_open</strong>: indicates that the TOA method is used.</li><li><strong id="b1394119162519"><a name="b1394119162519"></a><a name="b1394119162519"></a>proxy_open</strong>: indicates that the Proxy Protocol method is used.</li><li><strong id="b123462452517"><a name="b123462452517"></a><a name="b123462452517"></a>open</strong>: indicates that the TOA and Proxy Protocol methods are both used.</li></ul>
    <p id="p249810201616"><a name="p249810201616"></a><a name="p249810201616"></a>The default value is <strong id="b842352706144841"><a name="b842352706144841"></a><a name="b842352706144841"></a>close</strong>.</p>
    </td>
    </tr>
    <tr id="row1522122419321"><td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.1 "><p id="p1322222413216"><a name="p1322222413216"></a><a name="p1322222413216"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.2 "><p id="p522232411328"><a name="p522232411328"></a><a name="p522232411328"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.3 "><p id="p1722217249324"><a name="p1722217249324"></a><a name="p1722217249324"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.2.5.1.4 "><p id="p222215247324"><a name="p222215247324"></a><a name="p222215247324"></a>Lists the resource tags. For details, see <a href="#table194945101376">Table 4</a>.</p>
    <p id="p1140222914213"><a name="p1140222914213"></a><a name="p1140222914213"></a>A maximum of 10 tags can be added to each VPC endpoint service.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Port mapping parameters

    <a name="table56834929"></a>
    <table><thead align="left"><tr id="row54069340"><th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.1"><p id="p17540449"><a name="p17540449"></a><a name="p17540449"></a><strong id="b10452353115447"><a name="b10452353115447"></a><a name="b10452353115447"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.2"><p id="p37204434348"><a name="p37204434348"></a><a name="p37204434348"></a><strong id="b1956043410136"><a name="b1956043410136"></a><a name="b1956043410136"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="p11490287"><a name="p11490287"></a><a name="p11490287"></a><strong id="b542335796"><a name="b542335796"></a><a name="b542335796"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53%" id="mcps1.2.5.1.4"><p id="p58298029"><a name="p58298029"></a><a name="p58298029"></a><strong id="b303165984"><a name="b303165984"></a><a name="b303165984"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row24519875"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="p39952858"><a name="p39952858"></a><a name="p39952858"></a>client_port</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p472013433341"><a name="p472013433341"></a><a name="p472013433341"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p137021518125918"><a name="p137021518125918"></a><a name="p137021518125918"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.5.1.4 "><p id="p3481129"><a name="p3481129"></a><a name="p3481129"></a>Specifies the port for accessing the VPC endpoint.</p>
    <p id="p209011349124811"><a name="p209011349124811"></a><a name="p209011349124811"></a>This port is provided by the VPC endpoint, allowing you to access the VPC endpoint service. The value ranges from <strong id="b89637271421"><a name="b89637271421"></a><a name="b89637271421"></a>1</strong> to <strong id="b62419321421"><a name="b62419321421"></a><a name="b62419321421"></a>65535</strong>.</p>
    </td>
    </tr>
    <tr id="row31330167"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="p54715587"><a name="p54715587"></a><a name="p54715587"></a>server_port</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p77211043133417"><a name="p77211043133417"></a><a name="p77211043133417"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p109821525125912"><a name="p109821525125912"></a><a name="p109821525125912"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.5.1.4 "><p id="p23652783"><a name="p23652783"></a><a name="p23652783"></a>Specifies the port for accessing the VPC endpoint service.</p>
    <p id="p1136918011496"><a name="p1136918011496"></a><a name="p1136918011496"></a>This port is provided by the backend service to provide services. The value ranges from <strong id="b99681543184114"><a name="b99681543184114"></a><a name="b99681543184114"></a>1</strong> to <strong id="b19968643184115"><a name="b19968643184115"></a><a name="b19968643184115"></a>65535</strong>.</p>
    </td>
    </tr>
    <tr id="row11548462"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="p63010216"><a name="p63010216"></a><a name="p63010216"></a>protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p6721134319347"><a name="p6721134319347"></a><a name="p6721134319347"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p3553891"><a name="p3553891"></a><a name="p3553891"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.5.1.4 "><p id="p19429767"><a name="p19429767"></a><a name="p19429767"></a>Specifies the protocol used in port mappings. The value can be <strong id="b721417262133"><a name="b721417262133"></a><a name="b721417262133"></a>TCP</strong> or <strong id="b91721032131317"><a name="b91721032131317"></a><a name="b91721032131317"></a>UDP</strong>. The default value is <strong id="b10810333141310"><a name="b10810333141310"></a><a name="b10810333141310"></a>TCP</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **ResourceTags**  parameters

    <a name="table194945101376"></a>
    <table><thead align="left"><tr id="en-us_topic_0056765542_row4410728"><th class="cellrowborder" valign="top" width="15.601560156015601%" id="mcps1.2.5.1.1"><p id="en-us_topic_0056765542_p21724664"><a name="en-us_topic_0056765542_p21724664"></a><a name="en-us_topic_0056765542_p21724664"></a><strong id="b1563612711"><a name="b1563612711"></a><a name="b1563612711"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15.061506150615061%" id="mcps1.2.5.1.2"><p id="p10931647101614"><a name="p10931647101614"></a><a name="p10931647101614"></a><strong id="b1948657836"><a name="b1948657836"></a><a name="b1948657836"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.121712171217123%" id="mcps1.2.5.1.3"><p id="en-us_topic_0056765542_p63406242"><a name="en-us_topic_0056765542_p63406242"></a><a name="en-us_topic_0056765542_p63406242"></a><strong id="b1564672112114"><a name="b1564672112114"></a><a name="b1564672112114"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="52.21522152215221%" id="mcps1.2.5.1.4"><p id="en-us_topic_0056765542_p35632012"><a name="en-us_topic_0056765542_p35632012"></a><a name="en-us_topic_0056765542_p35632012"></a><strong id="b12940209153810"><a name="b12940209153810"></a><a name="b12940209153810"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0056765542_row511887"><td class="cellrowborder" valign="top" width="15.601560156015601%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0056765542_p41462866"><a name="en-us_topic_0056765542_p41462866"></a><a name="en-us_topic_0056765542_p41462866"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.061506150615061%" headers="mcps1.2.5.1.2 "><p id="p12931547141613"><a name="p12931547141613"></a><a name="p12931547141613"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.121712171217123%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0056765542_p45638969"><a name="en-us_topic_0056765542_p45638969"></a><a name="en-us_topic_0056765542_p45638969"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.21522152215221%" headers="mcps1.2.5.1.4 "><p id="p48921437201850"><a name="p48921437201850"></a><a name="p48921437201850"></a>Specifies the tag key. A tag key contains a maximum of 36 Unicode characters. This parameter cannot be left empty. It can contain only digits, letters, hyphens (-), at signs (@), and underscores (_).</p>
    </td>
    </tr>
    <tr id="en-us_topic_0056765542_row51921052"><td class="cellrowborder" valign="top" width="15.601560156015601%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0056765542_p44855704"><a name="en-us_topic_0056765542_p44855704"></a><a name="en-us_topic_0056765542_p44855704"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.061506150615061%" headers="mcps1.2.5.1.2 "><p id="p2093118475163"><a name="p2093118475163"></a><a name="p2093118475163"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.121712171217123%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0056765542_p25911262"><a name="en-us_topic_0056765542_p25911262"></a><a name="en-us_topic_0056765542_p25911262"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.21522152215221%" headers="mcps1.2.5.1.4 "><p id="p61714725112922"><a name="p61714725112922"></a><a name="p61714725112922"></a>Specifies the tag value. A tag value contains a maximum of 43 Unicode characters and can be left blank. It can contain only digits, letters, hyphens (-), at signs (@), and underscores (_).</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    POST https://{endpoint}/v1/{project_id}/vpc-endpoint-services
    ```

    ```
    {
       "port_id":"4189d3c2-8882-4871-a3c2-d380272eed88",
       "vpc_id":"4189d3c2-8882-4871-a3c2-d380272eed80",
       "approval_enabled":false,
       "service_type":"interface",
       "server_type":"VM",
       "ports":
      [
        {
          "client_port":8080,
          "server_port":90,
          "protocol":"TCP"
        },
        {
          "client_port":8081,
          "server_port":80,
          "protocol":"TCP"
        }
      ]
    }
    ```


## Response<a name="section19836555"></a>

-   Parameter description

    **Table  5**  Response parameters

    <a name="d0e2279"></a>
    <table><thead align="left"><tr id="row66860061"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.1"><p id="p46955892"><a name="p46955892"></a><a name="p46955892"></a><strong id="b10635914719"><a name="b10635914719"></a><a name="b10635914719"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.2"><p id="p45330870"><a name="p45330870"></a><a name="p45330870"></a><strong id="b1126555927"><a name="b1126555927"></a><a name="b1126555927"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="56.99999999999999%" id="mcps1.2.4.1.3"><p id="p47921869"><a name="p47921869"></a><a name="p47921869"></a><strong id="b788480299"><a name="b788480299"></a><a name="b788480299"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row56466209"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p10360217"><a name="p10360217"></a><a name="p10360217"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p33871262"><a name="p33871262"></a><a name="p33871262"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p59217687"><a name="p59217687"></a><a name="p59217687"></a>Specifies the unique ID of the VPC endpoint service.</p>
    </td>
    </tr>
    <tr id="row63197139"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p18694614"><a name="p18694614"></a><a name="p18694614"></a>port_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p37868737"><a name="p37868737"></a><a name="p37868737"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p6738104653019"><a name="p6738104653019"></a><a name="p6738104653019"></a>Specifies the ID for identifying the backend resource of the VPC endpoint service. The ID is in the form of the UUID. The value is as follows:</p>
    <a name="ul633165518179"></a><a name="ul633165518179"></a><ul id="ul633165518179"><li>If the backend service is an enhanced load balancer, the value is the ID of the port bound to the private IP address of the load balancer.</li><li>If the backend resource is an ECS, the value is the NIC ID of the ECS where the VPC endpoint service is deployed.</li><li>If the backend resource is a virtual IP address, the value is the NIC ID of the physical server where virtual resources are created.</li></ul>
    </td>
    </tr>
    <tr id="row315238134111"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p139691715114119"><a name="p139691715114119"></a><a name="p139691715114119"></a>vip_port_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p1396916151415"><a name="p1396916151415"></a><a name="p1396916151415"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p1896916158417"><a name="p1896916158417"></a><a name="p1896916158417"></a>Specifies the ID of the virtual NIC to which the virtual IP address is bound.</p>
    <p id="p10748193010109"><a name="p10748193010109"></a><a name="p10748193010109"></a>This parameter is returned only when <strong id="vpcep_06_0205_b14305337131"><a name="vpcep_06_0205_b14305337131"></a><a name="vpcep_06_0205_b14305337131"></a>port_id</strong> is set to VIP.</p>
    </td>
    </tr>
    <tr id="row24566569"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p43735040"><a name="p43735040"></a><a name="p43735040"></a>service_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p52877372"><a name="p52877372"></a><a name="p52877372"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p55208773"><a name="p55208773"></a><a name="p55208773"></a>Specifies the name of the VPC endpoint service.</p>
    </td>
    </tr>
    <tr id="row27116914"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p48986392"><a name="p48986392"></a><a name="p48986392"></a>service_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p8474815"><a name="p8474815"></a><a name="p8474815"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p135911520141219"><a name="p135911520141219"></a><a name="p135911520141219"></a>Specifies the type of the VPC endpoint service.</p>
    <div class="p" id="p3359114552814"><a name="p3359114552814"></a><a name="p3359114552814"></a>There are two types of VPC endpoint services: interface and gateway.<a name="vpcep_06_0201_ul87241928184613"></a><a name="vpcep_06_0201_ul87241928184613"></a><ul id="vpcep_06_0201_ul87241928184613"><li>Gateway: VPC endpoint services of this type are configured by operations people. You can use them directly without the need to create one by yourselves.</li><li>Interface: VPC endpoint services of this type include cloud services configured by operations people and private services created by yourselves. You cannot configure these cloud services, but can use them.</li></ul>
    </div>
    <p id="p20491271179"><a name="p20491271179"></a><a name="p20491271179"></a>You can perform the operations in <a href="creating-a-vpc-endpoint.md">Creating a VPC Endpoint</a> to create VPC endpoints for accessing VPC endpoints of the gateway and interface types.</p>
    </td>
    </tr>
    <tr id="row4124933"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p65684132"><a name="p65684132"></a><a name="p65684132"></a>server_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p18814464"><a name="p18814464"></a><a name="p18814464"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p115742037154612"><a name="p115742037154612"></a><a name="p115742037154612"></a>Specifies the resource type.</p>
    <a name="ul180115619307"></a><a name="ul180115619307"></a><ul id="ul180115619307"><li><strong id="b111511354539"><a name="b111511354539"></a><a name="b111511354539"></a>VM</strong>: indicates the ECS.</li><li><strong id="b111348551533"><a name="b111348551533"></a><a name="b111348551533"></a>VIP</strong>: indicates the virtual IP address.</li><li><strong id="b1842415561432"><a name="b1842415561432"></a><a name="b1842415561432"></a>LB</strong>: indicates the enhanced load balancer.</li></ul>
    </td>
    </tr>
    <tr id="row26589709"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p6282859"><a name="p6282859"></a><a name="p6282859"></a>vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p39149581"><a name="p39149581"></a><a name="p39149581"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p16536246191512"><a name="p16536246191512"></a><a name="p16536246191512"></a>Specifies the ID of the VPC to which the backend resource of the VPC endpoint service belongs.</p>
    </td>
    </tr>
    <tr id="row13433388428"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p15508124214211"><a name="p15508124214211"></a><a name="p15508124214211"></a>pool_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p145081342114217"><a name="p145081342114217"></a><a name="p145081342114217"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p05087421426"><a name="p05087421426"></a><a name="p05087421426"></a>Specifies the ID of the cluster associated with the target VPCEP resource.</p>
    </td>
    </tr>
    <tr id="row18777919"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p44616508"><a name="p44616508"></a><a name="p44616508"></a>approval_enabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p57167385"><a name="p57167385"></a><a name="p57167385"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p1875615510237"><a name="p1875615510237"></a><a name="p1875615510237"></a>Specifies whether connection approval is required.</p>
    <a name="ul1775615522311"></a><a name="ul1775615522311"></a><ul id="ul1775615522311"><li><strong id="b1836705966"><a name="b1836705966"></a><a name="b1836705966"></a>false</strong>: indicates that connection approval is not required. The created VPC endpoint is in the <strong id="b15309009"><a name="b15309009"></a><a name="b15309009"></a>Accepted</strong> state.</li><li><strong id="b1374184052"><a name="b1374184052"></a><a name="b1374184052"></a>true</strong>: indicates that connection approval is required. The created VPC endpoint is in the <strong id="b724489048"><a name="b724489048"></a><a name="b724489048"></a>Pending acceptance</strong> state until the owner of the associated VPC endpoint service approves the connection.</li></ul>
    </td>
    </tr>
    <tr id="row37245954"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p64132337"><a name="p64132337"></a><a name="p64132337"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p27336841"><a name="p27336841"></a><a name="p27336841"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p107216429310"><a name="p107216429310"></a><a name="p107216429310"></a>Specifies the status of the VPC endpoint service.</p>
    <a name="ul7855793119"></a><a name="ul7855793119"></a><ul id="ul7855793119"><li><strong id="b1334122644213"><a name="b1334122644213"></a><a name="b1334122644213"></a>creating</strong>: indicates the VPC endpoint service is being created.</li><li><strong id="b133221721148"><a name="b133221721148"></a><a name="b133221721148"></a>available</strong>: indicates the VPC endpoint service is connectable.</li><li><strong id="b122361971147"><a name="b122361971147"></a><a name="b122361971147"></a>failed</strong>: indicates the creation of the VPC endpoint service failed.</li></ul>
    </td>
    </tr>
    <tr id="row1088027"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p21021397"><a name="p21021397"></a><a name="p21021397"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p25011624"><a name="p25011624"></a><a name="p25011624"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p12675643"><a name="p12675643"></a><a name="p12675643"></a>Specifies the creation time of the VPC endpoint service.</p>
    <p id="p17561950164517"><a name="p17561950164517"></a><a name="p17561950164517"></a>The UTC time format is used: YYYY-MM-DDTHH:MM:SSZ.</p>
    </td>
    </tr>
    <tr id="row46971924"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p46629482"><a name="p46629482"></a><a name="p46629482"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p18891734"><a name="p18891734"></a><a name="p18891734"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p53835453"><a name="p53835453"></a><a name="p53835453"></a>Specifies the update time of the VPC endpoint service.</p>
    <p id="p2629419134616"><a name="p2629419134616"></a><a name="p2629419134616"></a>The UTC time format is used: YYYY-MM-DDTHH:MM:SSZ.</p>
    </td>
    </tr>
    <tr id="row14757035"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p54469209"><a name="p54469209"></a><a name="p54469209"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p49929783"><a name="p49929783"></a><a name="p49929783"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p17780589"><a name="p17780589"></a><a name="p17780589"></a>Specifies the project ID. For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row99731029202518"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p20857123514817"><a name="p20857123514817"></a><a name="p20857123514817"></a>cidr_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p1185733574815"><a name="p1185733574815"></a><a name="p1185733574815"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p12391036114918"><a name="p12391036114918"></a><a name="p12391036114918"></a>Specifies the network segment type. The value can be <strong id="b5818502113"><a name="b5818502113"></a><a name="b5818502113"></a>public</strong> or <strong id="b919115020119"><a name="b919115020119"></a><a name="b919115020119"></a>internal</strong>.</p>
    <a name="ul159453471498"></a><a name="ul159453471498"></a><ul id="ul159453471498"><li><strong id="b1445019521317"><a name="b1445019521317"></a><a name="b1445019521317"></a>public</strong>: indicates the public subnet CIDR block.</li><li><strong id="b17823551414"><a name="b17823551414"></a><a name="b17823551414"></a>internal</strong>: indicates the private subnet CIDR block.</li></ul>
    <p id="p1183713122495"><a name="p1183713122495"></a><a name="p1183713122495"></a>The default value is <strong id="b12723756919"><a name="b12723756919"></a><a name="b12723756919"></a>internal</strong>.</p>
    </td>
    </tr>
    <tr id="row25807577"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p10038983"><a name="p10038983"></a><a name="p10038983"></a>ports</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p7851298"><a name="p7851298"></a><a name="p7851298"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p7734311105614"><a name="p7734311105614"></a><a name="p7734311105614"></a>Lists the port mappings opened to the VPC endpoint service. For details, see <a href="#table9158581886">Table 6</a>.</p>
    <p id="p1373601110564"><a name="p1373601110564"></a><a name="p1373601110564"></a>Duplicate port mappings are not allowed in the same VPC endpoint service. If multiple VPC endpoint services share the same <strong id="b159801931141111"><a name="b159801931141111"></a><a name="b159801931141111"></a>port_id</strong> value, service ports and terminal ports of all these endpoint services cannot be duplicated when the protocol is the same.</p>
    </td>
    </tr>
    <tr id="row3628122492213"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p1898819266227"><a name="p1898819266227"></a><a name="p1898819266227"></a>tcp_proxy</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p139881326142212"><a name="p139881326142212"></a><a name="p139881326142212"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p3988426182213"><a name="p3988426182213"></a><a name="p3988426182213"></a>Specifies whether the client IP address and port number or <strong id="vpcep_06_0201_b1340623194912"><a name="vpcep_06_0201_b1340623194912"></a><a name="vpcep_06_0201_b1340623194912"></a>marker_id</strong> information is transmitted to the server. The following methods are supported:</p>
    <a name="ul113422343220"></a><a name="ul113422343220"></a><ul id="ul113422343220"><li>TCP TOA: The client information is inserted into field <strong id="vpcep_06_0201_b1328024583915"><a name="vpcep_06_0201_b1328024583915"></a><a name="vpcep_06_0201_b1328024583915"></a>tcp option</strong> and transmitted to the server.</li><li>Proxy Protocol: The client information is inserted into field <strong id="vpcep_06_0201_b18340846124016"><a name="vpcep_06_0201_b18340846124016"></a><a name="vpcep_06_0201_b18340846124016"></a>tcp payload</strong> and transmitted to the server.</li></ul>
    <p id="p117219186296"><a name="p117219186296"></a><a name="p117219186296"></a>This parameter is available only when the server can parse fields <strong id="vpcep_06_0201_b1246063817713"><a name="vpcep_06_0201_b1246063817713"></a><a name="vpcep_06_0201_b1246063817713"></a>tcp option</strong> and <strong id="vpcep_06_0201_b832154415710"><a name="vpcep_06_0201_b832154415710"></a><a name="vpcep_06_0201_b832154415710"></a>tcp payload</strong>.</p>
    <p id="p29385542114"><a name="p29385542114"></a><a name="p29385542114"></a>The values are as follows:</p>
    <a name="ul523712223"></a><a name="ul523712223"></a><ul id="ul523712223"><li><strong id="vpcep_06_0201_b485111422"><a name="vpcep_06_0201_b485111422"></a><a name="vpcep_06_0201_b485111422"></a>close</strong>: indicates that the TOA and Proxy Protocol methods are neither used.</li><li><strong id="vpcep_06_0201_b1432825911248"><a name="vpcep_06_0201_b1432825911248"></a><a name="vpcep_06_0201_b1432825911248"></a>toa_open</strong>: indicates that the TOA method is used.</li><li><strong id="vpcep_06_0201_b1394119162519"><a name="vpcep_06_0201_b1394119162519"></a><a name="vpcep_06_0201_b1394119162519"></a>proxy_open</strong>: indicates that the Proxy Protocol method is used.</li><li><strong id="vpcep_06_0201_b123462452517"><a name="vpcep_06_0201_b123462452517"></a><a name="vpcep_06_0201_b123462452517"></a>open</strong>: indicates that the TOA and Proxy Protocol methods are both used.</li></ul>
    <p id="p1725615331720"><a name="p1725615331720"></a><a name="p1725615331720"></a>The default value is <strong id="vpcep_06_0201_b842352706144841"><a name="vpcep_06_0201_b842352706144841"></a><a name="vpcep_06_0201_b842352706144841"></a>close</strong>.</p>
    </td>
    </tr>
    <tr id="row6103144416112"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p13103244015"><a name="p13103244015"></a><a name="p13103244015"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p21037441512"><a name="p21037441512"></a><a name="p21037441512"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p1510414411116"><a name="p1510414411116"></a><a name="p1510414411116"></a>Lists the resource tags. For details, see <a href="#table489217571060">Table 7</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6**  Port mapping parameters

    <a name="table9158581886"></a>
    <table><thead align="left"><tr id="en-us_topic_0178993304_row54069340"><th class="cellrowborder" valign="top" width="17.98%" id="mcps1.2.4.1.1"><p id="en-us_topic_0178993304_p17540449"><a name="en-us_topic_0178993304_p17540449"></a><a name="en-us_topic_0178993304_p17540449"></a><strong id="b8302057171210"><a name="b8302057171210"></a><a name="b8302057171210"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.650000000000002%" id="mcps1.2.4.1.2"><p id="en-us_topic_0178993304_p11490287"><a name="en-us_topic_0178993304_p11490287"></a><a name="en-us_topic_0178993304_p11490287"></a><strong id="b1355134319224"><a name="b1355134319224"></a><a name="b1355134319224"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="62.370000000000005%" id="mcps1.2.4.1.3"><p id="en-us_topic_0178993304_p58298029"><a name="en-us_topic_0178993304_p58298029"></a><a name="en-us_topic_0178993304_p58298029"></a><strong id="b735778700"><a name="b735778700"></a><a name="b735778700"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0178993304_row24519875"><td class="cellrowborder" valign="top" width="17.98%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0178993304_p39952858"><a name="en-us_topic_0178993304_p39952858"></a><a name="en-us_topic_0178993304_p39952858"></a>client_port</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.650000000000002%" headers="mcps1.2.4.1.2 "><p id="p88823381809"><a name="p88823381809"></a><a name="p88823381809"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.370000000000005%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0178993304_p3481129"><a name="en-us_topic_0178993304_p3481129"></a><a name="en-us_topic_0178993304_p3481129"></a>Specifies the port for accessing the VPC endpoint.</p>
    <p id="en-us_topic_0178993304_p209011349124811"><a name="en-us_topic_0178993304_p209011349124811"></a><a name="en-us_topic_0178993304_p209011349124811"></a>This port is provided by the VPC endpoint, allowing you to access the VPC endpoint service. The value ranges from <strong id="b1871853314113"><a name="b1871853314113"></a><a name="b1871853314113"></a>1</strong> to <strong id="b14719173314116"><a name="b14719173314116"></a><a name="b14719173314116"></a>65535</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0178993304_row31330167"><td class="cellrowborder" valign="top" width="17.98%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0178993304_p54715587"><a name="en-us_topic_0178993304_p54715587"></a><a name="en-us_topic_0178993304_p54715587"></a>server_port</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.650000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0178993304_p2777523"><a name="en-us_topic_0178993304_p2777523"></a><a name="en-us_topic_0178993304_p2777523"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.370000000000005%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0178993304_p23652783"><a name="en-us_topic_0178993304_p23652783"></a><a name="en-us_topic_0178993304_p23652783"></a>Specifies the port for accessing the VPC endpoint service.</p>
    <p id="en-us_topic_0178993304_p1136918011496"><a name="en-us_topic_0178993304_p1136918011496"></a><a name="en-us_topic_0178993304_p1136918011496"></a>This port is provided by the backend service to provide services. The value ranges from <strong id="b1141065692215"><a name="b1141065692215"></a><a name="b1141065692215"></a>1</strong> to <strong id="b204105566224"><a name="b204105566224"></a><a name="b204105566224"></a>65535</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0178993304_row11548462"><td class="cellrowborder" valign="top" width="17.98%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0178993304_p63010216"><a name="en-us_topic_0178993304_p63010216"></a><a name="en-us_topic_0178993304_p63010216"></a>protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.650000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0178993304_p3553891"><a name="en-us_topic_0178993304_p3553891"></a><a name="en-us_topic_0178993304_p3553891"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.370000000000005%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0178993304_p19429767"><a name="en-us_topic_0178993304_p19429767"></a><a name="en-us_topic_0178993304_p19429767"></a>Specifies the protocol used in port mappings. The value can be <strong id="b2110651230"><a name="b2110651230"></a><a name="b2110651230"></a>TCP</strong> or <strong id="b51117516233"><a name="b51117516233"></a><a name="b51117516233"></a>UDP</strong>. The default value is <strong id="b511115152312"><a name="b511115152312"></a><a name="b511115152312"></a>TCP</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  7** **ResourceTags**  parameters

    <a name="table489217571060"></a>
    <table><thead align="left"><tr id="en-us_topic_0178993304_en-us_topic_0056765542_row4410728"><th class="cellrowborder" valign="top" width="18.09%" id="mcps1.2.4.1.1"><p id="en-us_topic_0178993304_en-us_topic_0056765542_p21724664"><a name="en-us_topic_0178993304_en-us_topic_0056765542_p21724664"></a><a name="en-us_topic_0178993304_en-us_topic_0056765542_p21724664"></a><strong id="b1866348132314"><a name="b1866348132314"></a><a name="b1866348132314"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.2"><p id="en-us_topic_0178993304_en-us_topic_0056765542_p63406242"><a name="en-us_topic_0178993304_en-us_topic_0056765542_p63406242"></a><a name="en-us_topic_0178993304_en-us_topic_0056765542_p63406242"></a><strong id="b616714104231"><a name="b616714104231"></a><a name="b616714104231"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="61.91%" id="mcps1.2.4.1.3"><p id="en-us_topic_0178993304_en-us_topic_0056765542_p35632012"><a name="en-us_topic_0178993304_en-us_topic_0056765542_p35632012"></a><a name="en-us_topic_0178993304_en-us_topic_0056765542_p35632012"></a><strong id="b163691023811"><a name="b163691023811"></a><a name="b163691023811"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0178993304_en-us_topic_0056765542_row511887"><td class="cellrowborder" valign="top" width="18.09%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0178993304_en-us_topic_0056765542_p41462866"><a name="en-us_topic_0178993304_en-us_topic_0056765542_p41462866"></a><a name="en-us_topic_0178993304_en-us_topic_0056765542_p41462866"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0178993304_en-us_topic_0056765542_p45638969"><a name="en-us_topic_0178993304_en-us_topic_0056765542_p45638969"></a><a name="en-us_topic_0178993304_en-us_topic_0056765542_p45638969"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.91%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0178993304_p48921437201850"><a name="en-us_topic_0178993304_p48921437201850"></a><a name="en-us_topic_0178993304_p48921437201850"></a>Specifies the tag key. A tag key contains a maximum of 36 Unicode characters. This parameter cannot be left empty. It can contain only digits, letters, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    <tr id="en-us_topic_0178993304_en-us_topic_0056765542_row51921052"><td class="cellrowborder" valign="top" width="18.09%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0178993304_en-us_topic_0056765542_p44855704"><a name="en-us_topic_0178993304_en-us_topic_0056765542_p44855704"></a><a name="en-us_topic_0178993304_en-us_topic_0056765542_p44855704"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0178993304_en-us_topic_0056765542_p25911262"><a name="en-us_topic_0178993304_en-us_topic_0056765542_p25911262"></a><a name="en-us_topic_0178993304_en-us_topic_0056765542_p25911262"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.91%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0178993304_p61714725112922"><a name="en-us_topic_0178993304_p61714725112922"></a><a name="en-us_topic_0178993304_p61714725112922"></a>Specifies the tag value. A tag value contains a maximum of 43 Unicode characters and can be left blank. It can contain only digits, letters, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "id":"4189d3c2-8882-4871-a3c2-d380272eed83",
        "port_id":"4189d3c2-8882-4871-a3c2-d380272eed88",
        "vpc_id":"4189d3c2-8882-4871-a3c2-d380272eed80",
        "pool_id":"5289d3c2-8882-4871-a3c2-d380272eed80",
        "status":"available",
        "approval_enabled":false,
        "service_name":"test123",
        "service_type":"interface",
        "server_type":"VM",
        "project_id":"6e9dfd51d1124e8d8498dce894923a0d",
        "created_at":"2018-01-30T07:42:01.174",
        "ports":
                  [
                    {
                        "client_port":8080,
                        "server_port":90,
                        "protocol":"TCP"
                    },
                    {
                        "client_port":8081,
                        "server_port":80,
                        "protocol":"TCP"
                    }
                  ]
    }
    ```


## Status Code<a name="section63257131"></a>

For details about status codes, see  [Status Code](/vpcep/api-reference/common/status-code.md).

