# Querying Details of a VPC Endpoint Service<a name="vpcep_06_0202"></a>

## Function<a name="en-us_topic_0088219405"></a>

This API is used to query details of a VPC endpoint service.

## URI<a name="section58687999"></a>

GET /v1/\{project\_id\}/vpc-endpoint-services/\{vpc\_endpoint\_service\_id\}

[Table 1](#d0e2452)  describes the required parameters.

**Table  1**  Parameters

<a name="d0e2452"></a>
<table><thead align="left"><tr id="row31935744"><th class="cellrowborder" valign="top" width="32.65%" id="mcps1.2.4.1.1"><p id="p36658438"><a name="p36658438"></a><a name="p36658438"></a><strong id="b175381112573"><a name="b175381112573"></a><a name="b175381112573"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26.529999999999998%" id="mcps1.2.4.1.2"><p id="p16543501"><a name="p16543501"></a><a name="p16543501"></a><strong id="b1686121315574"><a name="b1686121315574"></a><a name="b1686121315574"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="40.82%" id="mcps1.2.4.1.3"><p id="p64955196"><a name="p64955196"></a><a name="p64955196"></a><strong id="b19111814195711"><a name="b19111814195711"></a><a name="b19111814195711"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row26879548"><td class="cellrowborder" valign="top" width="32.65%" headers="mcps1.2.4.1.1 "><p id="p29759797"><a name="p29759797"></a><a name="p29759797"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.2 "><p id="p61733326"><a name="p61733326"></a><a name="p61733326"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="40.82%" headers="mcps1.2.4.1.3 "><p id="p34343471"><a name="p34343471"></a><a name="p34343471"></a>Specifies the project ID. For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
</td>
</tr>
<tr id="row40655786"><td class="cellrowborder" valign="top" width="32.65%" headers="mcps1.2.4.1.1 "><p id="p4784395"><a name="p4784395"></a><a name="p4784395"></a>vpc_endpoint_service_id</p>
</td>
<td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.2 "><p id="p51991753"><a name="p51991753"></a><a name="p51991753"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="40.82%" headers="mcps1.2.4.1.3 "><p id="p560816313116"><a name="p560816313116"></a><a name="p560816313116"></a>Specifies the ID of the VPC endpoint service.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section58429947"></a>

-   Parameter description

    None

-   Example request

    This request is to query details of the VPC endpoint service whose ID is  **4189d3c2-8882-4871-a3c2-d380272eed88**.

    ```
    GET https://{endpoint}/v1/{project_id}/vpc-endpoint-services/4189d3c2-8882-4871-a3c2-d380272eed88
    ```


## Response<a name="section56107479"></a>

-   Parameter description

    **Table  2**  Response parameters

    <a name="d0e2596"></a>
    <table><thead align="left"><tr id="row10160463"><th class="cellrowborder" valign="top" width="24%" id="mcps1.2.4.1.1"><p id="p17691163"><a name="p17691163"></a><a name="p17691163"></a><strong id="b877061311"><a name="b877061311"></a><a name="b877061311"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.2"><p id="p23698059"><a name="p23698059"></a><a name="p23698059"></a><strong id="b6478446444"><a name="b6478446444"></a><a name="b6478446444"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="54%" id="mcps1.2.4.1.3"><p id="p40494599"><a name="p40494599"></a><a name="p40494599"></a><strong id="b293557406"><a name="b293557406"></a><a name="b293557406"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row58837112"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p1076806"><a name="p1076806"></a><a name="p1076806"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p20112472"><a name="p20112472"></a><a name="p20112472"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="p18497559"><a name="p18497559"></a><a name="p18497559"></a>Specifies the unique ID of the VPC endpoint service.</p>
    </td>
    </tr>
    <tr id="row32260306"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p62948031"><a name="p62948031"></a><a name="p62948031"></a>port_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p65625740"><a name="p65625740"></a><a name="p65625740"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="p23501288"><a name="p23501288"></a><a name="p23501288"></a>Specifies the ID for identifying the backend resource of the VPC endpoint service. The ID is in the form of the UUID. The value is as follows:</p>
    <a name="ul16432132118180"></a><a name="ul16432132118180"></a><ul id="ul16432132118180"><li>If the backend service is an enhanced load balancer, the value is the ID of the port bound to the private IP address of the load balancer.</li><li>If the backend resource is an ECS, the value is the NIC ID of the ECS where the VPC endpoint service is deployed.</li><li>If the backend resource is a virtual IP address, the value is the NIC ID of the physical server where virtual resources are created.</li></ul>
    </td>
    </tr>
    <tr id="row9994711144512"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p769241384515"><a name="p769241384515"></a><a name="p769241384515"></a>pool_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p146925132458"><a name="p146925132458"></a><a name="p146925132458"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="p05087421426"><a name="p05087421426"></a><a name="p05087421426"></a>Specifies the ID of the cluster associated with the target VPCEP resource.</p>
    </td>
    </tr>
    <tr id="row1668212513398"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p12948182619398"><a name="p12948182619398"></a><a name="p12948182619398"></a>vip_port_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p4948326133915"><a name="p4948326133915"></a><a name="p4948326133915"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="p2948122613917"><a name="p2948122613917"></a><a name="p2948122613917"></a>Specifies the ID of the virtual NIC to which the virtual IP address is bound.</p>
    <p id="p10748193010109"><a name="p10748193010109"></a><a name="p10748193010109"></a>This parameter is returned only when <strong id="vpcep_06_0205_b14305337131"><a name="vpcep_06_0205_b14305337131"></a><a name="vpcep_06_0205_b14305337131"></a>port_id</strong> is set to VIP.</p>
    </td>
    </tr>
    <tr id="row59653487"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p94244"><a name="p94244"></a><a name="p94244"></a>service_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p7633781"><a name="p7633781"></a><a name="p7633781"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="p14356556"><a name="p14356556"></a><a name="p14356556"></a>Specifies the name of the VPC endpoint service.</p>
    </td>
    </tr>
    <tr id="row15376366"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p37526105"><a name="p37526105"></a><a name="p37526105"></a>server_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p19715669"><a name="p19715669"></a><a name="p19715669"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="p1497382074811"><a name="p1497382074811"></a><a name="p1497382074811"></a>Specifies the resource type.</p>
    <a name="ul1417663314354"></a><a name="ul1417663314354"></a><ul id="ul1417663314354"><li><strong id="vpcep_06_0201_b111511354539"><a name="vpcep_06_0201_b111511354539"></a><a name="vpcep_06_0201_b111511354539"></a>VM</strong>: indicates the ECS.</li><li><strong id="vpcep_06_0201_b111348551533"><a name="vpcep_06_0201_b111348551533"></a><a name="vpcep_06_0201_b111348551533"></a>VIP</strong>: indicates the virtual IP address.</li><li><strong id="vpcep_06_0201_b1842415561432"><a name="vpcep_06_0201_b1842415561432"></a><a name="vpcep_06_0201_b1842415561432"></a>LB</strong>: indicates the enhanced load balancer.</li></ul>
    </td>
    </tr>
    <tr id="row11782520543"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p6282859"><a name="p6282859"></a><a name="p6282859"></a>vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p39149581"><a name="p39149581"></a><a name="p39149581"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="p16536246191512"><a name="p16536246191512"></a><a name="p16536246191512"></a>Specifies the ID of the VPC to which the backend resource of the VPC endpoint service belongs.</p>
    </td>
    </tr>
    <tr id="row53101844"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p6282141"><a name="p6282141"></a><a name="p6282141"></a>approval_enabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p39091418"><a name="p39091418"></a><a name="p39091418"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="p11315182920485"><a name="p11315182920485"></a><a name="p11315182920485"></a>Specifies whether connection approval is required.</p>
    <a name="ul175221837143510"></a><a name="ul175221837143510"></a><ul id="ul175221837143510"><li><strong id="vpcep_06_0201_b1836705966"><a name="vpcep_06_0201_b1836705966"></a><a name="vpcep_06_0201_b1836705966"></a>false</strong>: indicates that connection approval is not required. The created VPC endpoint is in the <strong id="vpcep_06_0201_b15309009"><a name="vpcep_06_0201_b15309009"></a><a name="vpcep_06_0201_b15309009"></a>Accepted</strong> state.</li><li><strong id="vpcep_06_0201_b1374184052"><a name="vpcep_06_0201_b1374184052"></a><a name="vpcep_06_0201_b1374184052"></a>true</strong>: indicates that connection approval is required. The created VPC endpoint is in the <strong id="vpcep_06_0201_b724489048"><a name="vpcep_06_0201_b724489048"></a><a name="vpcep_06_0201_b724489048"></a>Pending acceptance</strong> state until the owner of the associated VPC endpoint service approves the connection.</li></ul>
    </td>
    </tr>
    <tr id="row25845597"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p13118588"><a name="p13118588"></a><a name="p13118588"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p55972696"><a name="p55972696"></a><a name="p55972696"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="p37494488"><a name="p37494488"></a><a name="p37494488"></a>Specifies the status of the VPC endpoint service.</p>
    <a name="ul14361641113518"></a><a name="ul14361641113518"></a><ul id="ul14361641113518"><li><strong id="b19738124413413"><a name="b19738124413413"></a><a name="b19738124413413"></a>creating</strong>: indicates the VPC endpoint service is being created.</li><li><strong id="b7753145494012"><a name="b7753145494012"></a><a name="b7753145494012"></a>available</strong>: indicates the VPC endpoint service is connectable.</li><li><strong id="b1994719550406"><a name="b1994719550406"></a><a name="b1994719550406"></a>failed</strong>: indicates the creation of the VPC endpoint service failed.</li><li><strong id="b1732610501247"><a name="b1732610501247"></a><a name="b1732610501247"></a>deleting</strong>: indicates the VPC endpoint service is being deleted.</li></ul>
    </td>
    </tr>
    <tr id="row24373216"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p28073492"><a name="p28073492"></a><a name="p28073492"></a>service_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p59360343"><a name="p59360343"></a><a name="p59360343"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="p135911520141219"><a name="p135911520141219"></a><a name="p135911520141219"></a>Specifies the type of the VPC endpoint service.</p>
    <div class="p" id="p3359114552814"><a name="p3359114552814"></a><a name="p3359114552814"></a>There are two types of VPC endpoint services: interface and gateway.<a name="vpcep_06_0201_ul87241928184613"></a><a name="vpcep_06_0201_ul87241928184613"></a><ul id="vpcep_06_0201_ul87241928184613"><li>Gateway: VPC endpoint services of this type are configured by operations people. You can use them directly without the need to create one by yourselves.</li><li>Interface: VPC endpoint services of this type include cloud services configured by operations people and private services created by yourselves. You cannot configure these cloud services, but can use them.</li></ul>
    </div>
    <p id="p941115410718"><a name="p941115410718"></a><a name="p941115410718"></a>You can perform the operations in <a href="creating-a-vpc-endpoint.md">Creating a VPC Endpoint</a> to create VPC endpoints for accessing VPC endpoints of the gateway and interface types.</p>
    </td>
    </tr>
    <tr id="row55582327"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p5874619"><a name="p5874619"></a><a name="p5874619"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p6082124"><a name="p6082124"></a><a name="p6082124"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="p22890001"><a name="p22890001"></a><a name="p22890001"></a>Specifies the creation time of the VPC endpoint service.</p>
    <p id="p871616113394"><a name="p871616113394"></a><a name="p871616113394"></a>The UTC time format is used: YYYY-MM-DDTHH:MM:SSZ.</p>
    </td>
    </tr>
    <tr id="row4683418"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p43812617"><a name="p43812617"></a><a name="p43812617"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p59161121"><a name="p59161121"></a><a name="p59161121"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="p27321481"><a name="p27321481"></a><a name="p27321481"></a>Specifies the update time of the VPC endpoint service.</p>
    <p id="p181016810016"><a name="p181016810016"></a><a name="p181016810016"></a>The UTC time format is used: YYYY-MM-DDTHH:MM:SSZ.</p>
    </td>
    </tr>
    <tr id="row44566738"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p53136054"><a name="p53136054"></a><a name="p53136054"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p9053118"><a name="p9053118"></a><a name="p9053118"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="p62213971"><a name="p62213971"></a><a name="p62213971"></a>Specifies the project ID. For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row1885683564819"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p20857123514817"><a name="p20857123514817"></a><a name="p20857123514817"></a>cidr_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p1185733574815"><a name="p1185733574815"></a><a name="p1185733574815"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="p12391036114918"><a name="p12391036114918"></a><a name="p12391036114918"></a>Specifies the network segment type. The value can be <strong id="b133654221218"><a name="b133654221218"></a><a name="b133654221218"></a>public</strong> or <strong id="b10365152214114"><a name="b10365152214114"></a><a name="b10365152214114"></a>internal</strong>.</p>
    <a name="ul159453471498"></a><a name="ul159453471498"></a><ul id="ul159453471498"><li><strong id="b48761917411"><a name="b48761917411"></a><a name="b48761917411"></a>public</strong>: indicates the public subnet CIDR block.</li><li><strong id="b196001819410"><a name="b196001819410"></a><a name="b196001819410"></a>internal</strong>: indicates the private subnet CIDR block.</li></ul>
    <p id="p1183713122495"><a name="p1183713122495"></a><a name="p1183713122495"></a>The default value is <strong id="b19502142015111"><a name="b19502142015111"></a><a name="b19502142015111"></a>internal</strong>.</p>
    </td>
    </tr>
    <tr id="row23054829"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p55501888"><a name="p55501888"></a><a name="p55501888"></a>ports</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p66467923"><a name="p66467923"></a><a name="p66467923"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="p206491548175719"><a name="p206491548175719"></a><a name="p206491548175719"></a>Lists the port mappings opened to the VPC endpoint service. For details, see <a href="#table22278337">Table 3</a>.</p>
    <p id="p3651104885713"><a name="p3651104885713"></a><a name="p3651104885713"></a>Duplicate port mappings are not allowed in the same VPC endpoint service. If multiple VPC endpoint services share the same <strong id="vpcep_06_0201_b159801931141111"><a name="vpcep_06_0201_b159801931141111"></a><a name="vpcep_06_0201_b159801931141111"></a>port_id</strong> value, service ports and terminal ports of all these endpoint services cannot be duplicated when the protocol is the same.</p>
    </td>
    </tr>
    <tr id="row561514451255"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p7185174718259"><a name="p7185174718259"></a><a name="p7185174718259"></a>tcp_proxy</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p218516477257"><a name="p218516477257"></a><a name="p218516477257"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="p3988426182213"><a name="p3988426182213"></a><a name="p3988426182213"></a>Specifies whether the client IP address and port number or <strong id="vpcep_06_0201_b1340623194912"><a name="vpcep_06_0201_b1340623194912"></a><a name="vpcep_06_0201_b1340623194912"></a>marker_id</strong> information is transmitted to the server. The following methods are supported:</p>
    <a name="ul113422343220"></a><a name="ul113422343220"></a><ul id="ul113422343220"><li>TCP TOA: The client information is inserted into field <strong id="vpcep_06_0201_b1328024583915"><a name="vpcep_06_0201_b1328024583915"></a><a name="vpcep_06_0201_b1328024583915"></a>tcp option</strong> and transmitted to the server.</li><li>Proxy Protocol: The client information is inserted into field <strong id="vpcep_06_0201_b18340846124016"><a name="vpcep_06_0201_b18340846124016"></a><a name="vpcep_06_0201_b18340846124016"></a>tcp payload</strong> and transmitted to the server.</li></ul>
    <p id="p117219186296"><a name="p117219186296"></a><a name="p117219186296"></a>This parameter is available only when the server can parse fields <strong id="vpcep_06_0201_b1246063817713"><a name="vpcep_06_0201_b1246063817713"></a><a name="vpcep_06_0201_b1246063817713"></a>tcp option</strong> and <strong id="vpcep_06_0201_b832154415710"><a name="vpcep_06_0201_b832154415710"></a><a name="vpcep_06_0201_b832154415710"></a>tcp payload</strong>.</p>
    <p id="p29385542114"><a name="p29385542114"></a><a name="p29385542114"></a>The values are as follows:</p>
    <a name="ul523712223"></a><a name="ul523712223"></a><ul id="ul523712223"><li><strong id="vpcep_06_0201_b485111422"><a name="vpcep_06_0201_b485111422"></a><a name="vpcep_06_0201_b485111422"></a>close</strong>: indicates that the TOA and Proxy Protocol methods are neither used.</li><li><strong id="vpcep_06_0201_b1432825911248"><a name="vpcep_06_0201_b1432825911248"></a><a name="vpcep_06_0201_b1432825911248"></a>toa_open</strong>: indicates that the TOA method is used.</li><li><strong id="vpcep_06_0201_b1394119162519"><a name="vpcep_06_0201_b1394119162519"></a><a name="vpcep_06_0201_b1394119162519"></a>proxy_open</strong>: indicates that the Proxy Protocol method is used.</li><li><strong id="vpcep_06_0201_b123462452517"><a name="vpcep_06_0201_b123462452517"></a><a name="vpcep_06_0201_b123462452517"></a>open</strong>: indicates that the TOA and Proxy Protocol methods are both used.</li></ul>
    <p id="p1725615331720"><a name="p1725615331720"></a><a name="p1725615331720"></a>The default value is <strong id="vpcep_06_0201_b842352706144841"><a name="vpcep_06_0201_b842352706144841"></a><a name="vpcep_06_0201_b842352706144841"></a>close</strong>.</p>
    </td>
    </tr>
    <tr id="row1134329377"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p13103244015"><a name="p13103244015"></a><a name="p13103244015"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p21037441512"><a name="p21037441512"></a><a name="p21037441512"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="p1510414411116"><a name="p1510414411116"></a><a name="p1510414411116"></a>Lists the resource tags. For details, see <a href="#table489217571060">Table 4</a>.</p>
    </td>
    </tr>
    <tr id="row101696588573"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p11518153913210"><a name="p11518153913210"></a><a name="p11518153913210"></a>error</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p1952093920326"><a name="p1952093920326"></a><a name="p1952093920326"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="p84071479448"><a name="p84071479448"></a><a name="p84071479448"></a>Specifies the error message.</p>
    <p id="p45203393322"><a name="p45203393322"></a><a name="p45203393322"></a>This field is returned when the status of the VPC endpoint service changes to <strong id="b109651353132615"><a name="b109651353132615"></a><a name="b109651353132615"></a>failed</strong>. For details, see <a href="#table8651145512302">Table 5</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Port mapping parameters

    <a name="table22278337"></a>
    <table><thead align="left"><tr id="vpcep_06_0201_en-us_topic_0178993304_row54069340"><th class="cellrowborder" valign="top" width="17.98%" id="mcps1.2.4.1.1"><p id="vpcep_06_0201_en-us_topic_0178993304_p17540449"><a name="vpcep_06_0201_en-us_topic_0178993304_p17540449"></a><a name="vpcep_06_0201_en-us_topic_0178993304_p17540449"></a><strong id="vpcep_06_0201_b8302057171210"><a name="vpcep_06_0201_b8302057171210"></a><a name="vpcep_06_0201_b8302057171210"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.650000000000002%" id="mcps1.2.4.1.2"><p id="vpcep_06_0201_en-us_topic_0178993304_p11490287"><a name="vpcep_06_0201_en-us_topic_0178993304_p11490287"></a><a name="vpcep_06_0201_en-us_topic_0178993304_p11490287"></a><strong id="vpcep_06_0201_b1355134319224"><a name="vpcep_06_0201_b1355134319224"></a><a name="vpcep_06_0201_b1355134319224"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="62.370000000000005%" id="mcps1.2.4.1.3"><p id="vpcep_06_0201_en-us_topic_0178993304_p58298029"><a name="vpcep_06_0201_en-us_topic_0178993304_p58298029"></a><a name="vpcep_06_0201_en-us_topic_0178993304_p58298029"></a><strong id="vpcep_06_0201_b735778700"><a name="vpcep_06_0201_b735778700"></a><a name="vpcep_06_0201_b735778700"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="vpcep_06_0201_en-us_topic_0178993304_row24519875"><td class="cellrowborder" valign="top" width="17.98%" headers="mcps1.2.4.1.1 "><p id="vpcep_06_0201_en-us_topic_0178993304_p39952858"><a name="vpcep_06_0201_en-us_topic_0178993304_p39952858"></a><a name="vpcep_06_0201_en-us_topic_0178993304_p39952858"></a>client_port</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.650000000000002%" headers="mcps1.2.4.1.2 "><p id="vpcep_06_0201_p88823381809"><a name="vpcep_06_0201_p88823381809"></a><a name="vpcep_06_0201_p88823381809"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.370000000000005%" headers="mcps1.2.4.1.3 "><p id="vpcep_06_0201_en-us_topic_0178993304_p3481129"><a name="vpcep_06_0201_en-us_topic_0178993304_p3481129"></a><a name="vpcep_06_0201_en-us_topic_0178993304_p3481129"></a>Specifies the port for accessing the VPC endpoint.</p>
    <p id="vpcep_06_0201_en-us_topic_0178993304_p209011349124811"><a name="vpcep_06_0201_en-us_topic_0178993304_p209011349124811"></a><a name="vpcep_06_0201_en-us_topic_0178993304_p209011349124811"></a>This port is provided by the VPC endpoint, allowing you to access the VPC endpoint service. The value ranges from <strong id="vpcep_06_0201_b1871853314113"><a name="vpcep_06_0201_b1871853314113"></a><a name="vpcep_06_0201_b1871853314113"></a>1</strong> to <strong id="vpcep_06_0201_b14719173314116"><a name="vpcep_06_0201_b14719173314116"></a><a name="vpcep_06_0201_b14719173314116"></a>65535</strong>.</p>
    </td>
    </tr>
    <tr id="vpcep_06_0201_en-us_topic_0178993304_row31330167"><td class="cellrowborder" valign="top" width="17.98%" headers="mcps1.2.4.1.1 "><p id="vpcep_06_0201_en-us_topic_0178993304_p54715587"><a name="vpcep_06_0201_en-us_topic_0178993304_p54715587"></a><a name="vpcep_06_0201_en-us_topic_0178993304_p54715587"></a>server_port</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.650000000000002%" headers="mcps1.2.4.1.2 "><p id="vpcep_06_0201_en-us_topic_0178993304_p2777523"><a name="vpcep_06_0201_en-us_topic_0178993304_p2777523"></a><a name="vpcep_06_0201_en-us_topic_0178993304_p2777523"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.370000000000005%" headers="mcps1.2.4.1.3 "><p id="vpcep_06_0201_en-us_topic_0178993304_p23652783"><a name="vpcep_06_0201_en-us_topic_0178993304_p23652783"></a><a name="vpcep_06_0201_en-us_topic_0178993304_p23652783"></a>Specifies the port for accessing the VPC endpoint service.</p>
    <p id="vpcep_06_0201_en-us_topic_0178993304_p1136918011496"><a name="vpcep_06_0201_en-us_topic_0178993304_p1136918011496"></a><a name="vpcep_06_0201_en-us_topic_0178993304_p1136918011496"></a>This port is provided by the backend service to provide services. The value ranges from <strong id="vpcep_06_0201_b1141065692215"><a name="vpcep_06_0201_b1141065692215"></a><a name="vpcep_06_0201_b1141065692215"></a>1</strong> to <strong id="vpcep_06_0201_b204105566224"><a name="vpcep_06_0201_b204105566224"></a><a name="vpcep_06_0201_b204105566224"></a>65535</strong>.</p>
    </td>
    </tr>
    <tr id="vpcep_06_0201_en-us_topic_0178993304_row11548462"><td class="cellrowborder" valign="top" width="17.98%" headers="mcps1.2.4.1.1 "><p id="vpcep_06_0201_en-us_topic_0178993304_p63010216"><a name="vpcep_06_0201_en-us_topic_0178993304_p63010216"></a><a name="vpcep_06_0201_en-us_topic_0178993304_p63010216"></a>protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.650000000000002%" headers="mcps1.2.4.1.2 "><p id="vpcep_06_0201_en-us_topic_0178993304_p3553891"><a name="vpcep_06_0201_en-us_topic_0178993304_p3553891"></a><a name="vpcep_06_0201_en-us_topic_0178993304_p3553891"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.370000000000005%" headers="mcps1.2.4.1.3 "><p id="vpcep_06_0201_en-us_topic_0178993304_p19429767"><a name="vpcep_06_0201_en-us_topic_0178993304_p19429767"></a><a name="vpcep_06_0201_en-us_topic_0178993304_p19429767"></a>Specifies the protocol used in port mappings. The value can be <strong id="vpcep_06_0201_b2110651230"><a name="vpcep_06_0201_b2110651230"></a><a name="vpcep_06_0201_b2110651230"></a>TCP</strong> or <strong id="vpcep_06_0201_b51117516233"><a name="vpcep_06_0201_b51117516233"></a><a name="vpcep_06_0201_b51117516233"></a>UDP</strong>. The default value is <strong id="vpcep_06_0201_b511115152312"><a name="vpcep_06_0201_b511115152312"></a><a name="vpcep_06_0201_b511115152312"></a>TCP</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **ResourceTags**  parameters

    <a name="table489217571060"></a>
    <table><thead align="left"><tr id="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_row4410728"><th class="cellrowborder" valign="top" width="18.09%" id="mcps1.2.4.1.1"><p id="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p21724664"><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p21724664"></a><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p21724664"></a><strong id="vpcep_06_0201_b1866348132314"><a name="vpcep_06_0201_b1866348132314"></a><a name="vpcep_06_0201_b1866348132314"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.2"><p id="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p63406242"><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p63406242"></a><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p63406242"></a><strong id="vpcep_06_0201_b616714104231"><a name="vpcep_06_0201_b616714104231"></a><a name="vpcep_06_0201_b616714104231"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="61.91%" id="mcps1.2.4.1.3"><p id="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p35632012"><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p35632012"></a><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p35632012"></a><strong id="vpcep_06_0201_b163691023811"><a name="vpcep_06_0201_b163691023811"></a><a name="vpcep_06_0201_b163691023811"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_row511887"><td class="cellrowborder" valign="top" width="18.09%" headers="mcps1.2.4.1.1 "><p id="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p41462866"><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p41462866"></a><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p41462866"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p45638969"><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p45638969"></a><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p45638969"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.91%" headers="mcps1.2.4.1.3 "><p id="vpcep_06_0201_en-us_topic_0178993304_p48921437201850"><a name="vpcep_06_0201_en-us_topic_0178993304_p48921437201850"></a><a name="vpcep_06_0201_en-us_topic_0178993304_p48921437201850"></a>Specifies the tag key. A tag key contains a maximum of 36 Unicode characters. This parameter cannot be left empty. It can contain only digits, letters, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    <tr id="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_row51921052"><td class="cellrowborder" valign="top" width="18.09%" headers="mcps1.2.4.1.1 "><p id="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p44855704"><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p44855704"></a><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p44855704"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p25911262"><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p25911262"></a><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p25911262"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.91%" headers="mcps1.2.4.1.3 "><p id="vpcep_06_0201_en-us_topic_0178993304_p61714725112922"><a name="vpcep_06_0201_en-us_topic_0178993304_p61714725112922"></a><a name="vpcep_06_0201_en-us_topic_0178993304_p61714725112922"></a>Specifies the tag value. A tag value contains a maximum of 43 Unicode characters and can be left blank. It can contain only digits, letters, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5**  Error parameters

    <a name="table8651145512302"></a>
    <table><thead align="left"><tr id="row4652255153018"><th class="cellrowborder" valign="top" width="18.34%" id="mcps1.2.4.1.1"><p id="p665015573309"><a name="p665015573309"></a><a name="p665015573309"></a><strong id="b085424117110"><a name="b085424117110"></a><a name="b085424117110"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.630000000000003%" id="mcps1.2.4.1.2"><p id="p865015710307"><a name="p865015710307"></a><a name="p865015710307"></a><strong id="b1597841565"><a name="b1597841565"></a><a name="b1597841565"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="61.029999999999994%" id="mcps1.2.4.1.3"><p id="p1565011575303"><a name="p1565011575303"></a><a name="p1565011575303"></a><strong id="b1010514442017"><a name="b1010514442017"></a><a name="b1010514442017"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row865255513010"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.2.4.1.1 "><p id="p96501057153013"><a name="p96501057153013"></a><a name="p96501057153013"></a>error_code</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.630000000000003%" headers="mcps1.2.4.1.2 "><p id="p6650155710309"><a name="p6650155710309"></a><a name="p6650155710309"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.029999999999994%" headers="mcps1.2.4.1.3 "><p id="p12650557133019"><a name="p12650557133019"></a><a name="p12650557133019"></a>Specifies the error code.</p>
    </td>
    </tr>
    <tr id="row186521755153018"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.2.4.1.1 "><p id="p10650057123018"><a name="p10650057123018"></a><a name="p10650057123018"></a>error_message</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.630000000000003%" headers="mcps1.2.4.1.2 "><p id="p14650157113016"><a name="p14650157113016"></a><a name="p14650157113016"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.029999999999994%" headers="mcps1.2.4.1.3 "><p id="p156501957183013"><a name="p156501957183013"></a><a name="p156501957183013"></a>Specifies the error message.</p>
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


## Status Code<a name="section48411964"></a>

For details about status codes, see  [Status Code](/vpcep/api-reference/common/status-code.md).

