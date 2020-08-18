# Modifying a VPC Endpoint Service<a name="vpcep_06_0203"></a>

## **Function**<a name="section49925986"></a>

This API is used to modify a VPC endpoint service.

## URI<a name="section46680697"></a>

PUT /v1/\{project\_id\}/vpc-endpoint-services/\{vpc\_endpoint\_service\_id\}

[Table 1](#table28352855)  describes the required parameters.

**Table  1**  Parameters

<a name="table28352855"></a>
<table><thead align="left"><tr id="row62825334"><th class="cellrowborder" valign="top" width="32.65%" id="mcps1.2.4.1.1"><p id="p55687332"><a name="p55687332"></a><a name="p55687332"></a><strong id="b92761418131619"><a name="b92761418131619"></a><a name="b92761418131619"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26.529999999999998%" id="mcps1.2.4.1.2"><p id="p14380054"><a name="p14380054"></a><a name="p14380054"></a><strong id="b181859190168"><a name="b181859190168"></a><a name="b181859190168"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="40.82%" id="mcps1.2.4.1.3"><p id="p23933749"><a name="p23933749"></a><a name="p23933749"></a><strong id="b203262205169"><a name="b203262205169"></a><a name="b203262205169"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row59585512"><td class="cellrowborder" valign="top" width="32.65%" headers="mcps1.2.4.1.1 "><p id="p61697176"><a name="p61697176"></a><a name="p61697176"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.2 "><p id="p31415340"><a name="p31415340"></a><a name="p31415340"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="40.82%" headers="mcps1.2.4.1.3 "><p id="p61614605"><a name="p61614605"></a><a name="p61614605"></a>Specifies the project ID. For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
</td>
</tr>
<tr id="row17660533"><td class="cellrowborder" valign="top" width="32.65%" headers="mcps1.2.4.1.1 "><p id="p21217075"><a name="p21217075"></a><a name="p21217075"></a>vpc_endpoint_service_id</p>
</td>
<td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.2 "><p id="p40861554"><a name="p40861554"></a><a name="p40861554"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="40.82%" headers="mcps1.2.4.1.3 "><p id="p21451610"><a name="p21451610"></a><a name="p21451610"></a>Specifies the ID of the VPC endpoint service.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section17473095"></a>

-   Parameter description

    **Table  2**  Request parameters

    <a name="table14879924"></a>
    <table><thead align="left"><tr id="row6602325"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.5.1.1"><p id="p65026297"><a name="p65026297"></a><a name="p65026297"></a><strong id="b17745537131614"><a name="b17745537131614"></a><a name="b17745537131614"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.2"><p id="p32638698"><a name="p32638698"></a><a name="p32638698"></a><strong id="b1628967667"><a name="b1628967667"></a><a name="b1628967667"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.3"><p id="p26488847"><a name="p26488847"></a><a name="p26488847"></a><strong id="b1273283321716"><a name="b1273283321716"></a><a name="b1273283321716"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="p65221840"><a name="p65221840"></a><a name="p65221840"></a><strong id="b177347256"><a name="b177347256"></a><a name="b177347256"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row48477719"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.1 "><p id="p34381129"><a name="p34381129"></a><a name="p34381129"></a>approval_enabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p33408080"><a name="p33408080"></a><a name="p33408080"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p21699988"><a name="p21699988"></a><a name="p21699988"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="p11315182920485"><a name="p11315182920485"></a><a name="p11315182920485"></a>Specifies whether connection approval is required.</p>
    <a name="ul15639203204411"></a><a name="ul15639203204411"></a><ul id="ul15639203204411"><li><strong id="b769518422617"><a name="b769518422617"></a><a name="b769518422617"></a>false</strong>: indicates that connection approval is not required. The created VPC endpoint is in the <strong id="b1670881064318"><a name="b1670881064318"></a><a name="b1670881064318"></a>Accepted</strong> state.</li><li><strong id="b264772611"><a name="b264772611"></a><a name="b264772611"></a>true</strong>: indicates that connection approval is required. The created VPC endpoint is unavailable until the owner of the associated VPC endpoint service approves the connection.</li></ul>
    <p id="p186091411112511"><a name="p186091411112511"></a><a name="p186091411112511"></a>The default value is <strong id="b126481817269"><a name="b126481817269"></a><a name="b126481817269"></a>true</strong>.</p>
    </td>
    </tr>
    <tr id="row06694455413"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.1 "><p id="p15295815134415"><a name="p15295815134415"></a><a name="p15295815134415"></a>service_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p6296815164417"><a name="p6296815164417"></a><a name="p6296815164417"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p629611150441"><a name="p629611150441"></a><a name="p629611150441"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="p1970935114472"><a name="p1970935114472"></a><a name="p1970935114472"></a>Specifies the name of the VPC endpoint service. The value contains a maximum of 16 characters, including letters, digits, underscores (_), and hyphens (-).</p>
    </td>
    </tr>
    <tr id="row7964250"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.1 "><p id="p41124512"><a name="p41124512"></a><a name="p41124512"></a>ports</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p42751146"><a name="p42751146"></a><a name="p42751146"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p40290784"><a name="p40290784"></a><a name="p40290784"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="p206491548175719"><a name="p206491548175719"></a><a name="p206491548175719"></a>Lists the port mappings opened to the VPC endpoint service. For details, see <a href="#table1186184673416">Table 3</a>.</p>
    <p id="p3651104885713"><a name="p3651104885713"></a><a name="p3651104885713"></a>Duplicate port mappings are not allowed in the same VPC endpoint service. If multiple VPC endpoint services share the same <strong id="b229032215128"><a name="b229032215128"></a><a name="b229032215128"></a>port_id</strong> value, service ports and terminal ports of all these endpoint services cannot be duplicated when the protocol is the same. A maximum of 200 port mappings can be created at a time.</p>
    </td>
    </tr>
    <tr id="row64921532133312"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.1 "><p id="p19878153315338"><a name="p19878153315338"></a><a name="p19878153315338"></a>port_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p3878133363311"><a name="p3878133363311"></a><a name="p3878133363311"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p15878103314332"><a name="p15878103314332"></a><a name="p15878103314332"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="p23501288"><a name="p23501288"></a><a name="p23501288"></a>Specifies the ID for identifying the backend resource of the VPC endpoint service. The ID is in the form of the UUID. The value is as follows:</p>
    <a name="ul1176004911819"></a><a name="ul1176004911819"></a><ul id="ul1176004911819"><li>If the backend service is an enhanced load balancer, the value is the ID of the port bound to the private IP address of the load balancer. For details, see response field <strong id="vpcep_06_0201_b760615179297"><a name="vpcep_06_0201_b760615179297"></a><a name="vpcep_06_0201_b760615179297"></a>vip_port_id</strong> in <a href="https://docs.otc.t-systems.com/en-us/api/elb/en-us_topic_0141008271.html" target="_blank" rel="noopener noreferrer">Querying Details of a Load Balancer</a> in the <em id="vpcep_06_0201_i454205722813"><a name="vpcep_06_0201_i454205722813"></a><a name="vpcep_06_0201_i454205722813"></a>Elastic Load Balance API Reference</em>.</li><li>If the backend resource is an ECS, the value is the NIC ID of the ECS where the VPC endpoint service is deployed. For details, see <a href="https://docs.otc.t-systems.com/en-us/api/ecs/en-us_topic_0020212662.html" target="_blank" rel="noopener noreferrer">Querying NICs of an ECS</a> in the <em id="vpcep_06_0201_i8649112044"><a name="vpcep_06_0201_i8649112044"></a><a name="vpcep_06_0201_i8649112044"></a>Elastic Load Balance API Reference</em>.</li><li>If the backend resource is a virtual IP address, the value is the NIC ID of the physical server where virtual resources are created.</li></ul>
    </td>
    </tr>
    <tr id="row1656963160"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.1 "><p id="p43501320364"><a name="p43501320364"></a><a name="p43501320364"></a>vip_port_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p2350192013610"><a name="p2350192013610"></a><a name="p2350192013610"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p143502204610"><a name="p143502204610"></a><a name="p143502204610"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="p835016203617"><a name="p835016203617"></a><a name="p835016203617"></a>Specifies the ID of the virtual NIC to which the virtual IP address is bound.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Port mapping parameters

    <a name="table1186184673416"></a>
    <table><thead align="left"><tr id="vpcep_06_0201_row54069340"><th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.1"><p id="vpcep_06_0201_p17540449"><a name="vpcep_06_0201_p17540449"></a><a name="vpcep_06_0201_p17540449"></a><strong id="vpcep_06_0201_b10452353115447"><a name="vpcep_06_0201_b10452353115447"></a><a name="vpcep_06_0201_b10452353115447"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.2"><p id="vpcep_06_0201_p37204434348"><a name="vpcep_06_0201_p37204434348"></a><a name="vpcep_06_0201_p37204434348"></a><strong id="vpcep_06_0201_b1956043410136"><a name="vpcep_06_0201_b1956043410136"></a><a name="vpcep_06_0201_b1956043410136"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="vpcep_06_0201_p11490287"><a name="vpcep_06_0201_p11490287"></a><a name="vpcep_06_0201_p11490287"></a><strong id="vpcep_06_0201_b542335796"><a name="vpcep_06_0201_b542335796"></a><a name="vpcep_06_0201_b542335796"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53%" id="mcps1.2.5.1.4"><p id="vpcep_06_0201_p58298029"><a name="vpcep_06_0201_p58298029"></a><a name="vpcep_06_0201_p58298029"></a><strong id="vpcep_06_0201_b303165984"><a name="vpcep_06_0201_b303165984"></a><a name="vpcep_06_0201_b303165984"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="vpcep_06_0201_row24519875"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="vpcep_06_0201_p39952858"><a name="vpcep_06_0201_p39952858"></a><a name="vpcep_06_0201_p39952858"></a>client_port</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="vpcep_06_0201_p472013433341"><a name="vpcep_06_0201_p472013433341"></a><a name="vpcep_06_0201_p472013433341"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="vpcep_06_0201_p137021518125918"><a name="vpcep_06_0201_p137021518125918"></a><a name="vpcep_06_0201_p137021518125918"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.5.1.4 "><p id="vpcep_06_0201_p3481129"><a name="vpcep_06_0201_p3481129"></a><a name="vpcep_06_0201_p3481129"></a>Specifies the port for accessing the VPC endpoint.</p>
    <p id="vpcep_06_0201_p209011349124811"><a name="vpcep_06_0201_p209011349124811"></a><a name="vpcep_06_0201_p209011349124811"></a>This port is provided by the VPC endpoint, allowing you to access the VPC endpoint service. The value ranges from <strong id="vpcep_06_0201_b89637271421"><a name="vpcep_06_0201_b89637271421"></a><a name="vpcep_06_0201_b89637271421"></a>1</strong> to <strong id="vpcep_06_0201_b62419321421"><a name="vpcep_06_0201_b62419321421"></a><a name="vpcep_06_0201_b62419321421"></a>65535</strong>.</p>
    </td>
    </tr>
    <tr id="vpcep_06_0201_row31330167"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="vpcep_06_0201_p54715587"><a name="vpcep_06_0201_p54715587"></a><a name="vpcep_06_0201_p54715587"></a>server_port</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="vpcep_06_0201_p77211043133417"><a name="vpcep_06_0201_p77211043133417"></a><a name="vpcep_06_0201_p77211043133417"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="vpcep_06_0201_p109821525125912"><a name="vpcep_06_0201_p109821525125912"></a><a name="vpcep_06_0201_p109821525125912"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.5.1.4 "><p id="vpcep_06_0201_p23652783"><a name="vpcep_06_0201_p23652783"></a><a name="vpcep_06_0201_p23652783"></a>Specifies the port for accessing the VPC endpoint service.</p>
    <p id="vpcep_06_0201_p1136918011496"><a name="vpcep_06_0201_p1136918011496"></a><a name="vpcep_06_0201_p1136918011496"></a>This port is provided by the backend service to provide services. The value ranges from <strong id="vpcep_06_0201_b99681543184114"><a name="vpcep_06_0201_b99681543184114"></a><a name="vpcep_06_0201_b99681543184114"></a>1</strong> to <strong id="vpcep_06_0201_b19968643184115"><a name="vpcep_06_0201_b19968643184115"></a><a name="vpcep_06_0201_b19968643184115"></a>65535</strong>.</p>
    </td>
    </tr>
    <tr id="vpcep_06_0201_row11548462"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="vpcep_06_0201_p63010216"><a name="vpcep_06_0201_p63010216"></a><a name="vpcep_06_0201_p63010216"></a>protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="vpcep_06_0201_p6721134319347"><a name="vpcep_06_0201_p6721134319347"></a><a name="vpcep_06_0201_p6721134319347"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="vpcep_06_0201_p3553891"><a name="vpcep_06_0201_p3553891"></a><a name="vpcep_06_0201_p3553891"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.5.1.4 "><p id="vpcep_06_0201_p19429767"><a name="vpcep_06_0201_p19429767"></a><a name="vpcep_06_0201_p19429767"></a>Specifies the protocol used in port mappings. The value can be <strong id="vpcep_06_0201_b721417262133"><a name="vpcep_06_0201_b721417262133"></a><a name="vpcep_06_0201_b721417262133"></a>TCP</strong> or <strong id="vpcep_06_0201_b91721032131317"><a name="vpcep_06_0201_b91721032131317"></a><a name="vpcep_06_0201_b91721032131317"></a>UDP</strong>. The default value is <strong id="vpcep_06_0201_b10810333141310"><a name="vpcep_06_0201_b10810333141310"></a><a name="vpcep_06_0201_b10810333141310"></a>TCP</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    This request is to modify the VPC endpoint service whose ID is  **4189d3c2-8882-4871-a3c2-d380272eed88**.

    ```
    PUT https://{endpoint}/v1/{project_id}/vpc-endpoint-services/4189d3c2-8882-4871-a3c2-d380272eed88
    ```

    ```
    {
       "approval_enabled":true,
       "service_name":"test",
       "ports":[
                 {
                    "client_port":8081,
                    "server_port":22,
                    "protocol":"TCP"
                 },
                 {
                    "client_port":8082,
                    "server_port":23,
                    "protocol":"UDP"
                 }
               ]
    }
    ```


## Response<a name="section6034613"></a>

-   Parameter description

    **Table  4**  Response parameters

    <a name="table66810458"></a>
    <table><thead align="left"><tr id="row35166537"><th class="cellrowborder" valign="top" width="24.240000000000002%" id="mcps1.2.4.1.1"><p id="p29917273"><a name="p29917273"></a><a name="p29917273"></a><strong id="b2006033585"><a name="b2006033585"></a><a name="b2006033585"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25.25%" id="mcps1.2.4.1.2"><p id="p7380066"><a name="p7380066"></a><a name="p7380066"></a><strong id="b1939668716"><a name="b1939668716"></a><a name="b1939668716"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.51%" id="mcps1.2.4.1.3"><p id="p60914443"><a name="p60914443"></a><a name="p60914443"></a><strong id="b2063692860"><a name="b2063692860"></a><a name="b2063692860"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row35122812"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.1 "><p id="p26375518"><a name="p26375518"></a><a name="p26375518"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p56042200"><a name="p56042200"></a><a name="p56042200"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.51%" headers="mcps1.2.4.1.3 "><p id="p18497559"><a name="p18497559"></a><a name="p18497559"></a>Specifies the unique ID of the VPC endpoint service.</p>
    </td>
    </tr>
    <tr id="row52575024"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.1 "><p id="p30718575"><a name="p30718575"></a><a name="p30718575"></a>port_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p5176642"><a name="p5176642"></a><a name="p5176642"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.51%" headers="mcps1.2.4.1.3 "><p id="p107701059124610"><a name="p107701059124610"></a><a name="p107701059124610"></a>Specifies the ID for identifying the backend resource of the VPC endpoint service. The ID is in the form of the UUID. The value is as follows:</p>
    <a name="ul16432132118180"></a><a name="ul16432132118180"></a><ul id="ul16432132118180"><li>If the backend service is an enhanced load balancer, the value is the ID of the port bound to the private IP address of the load balancer.</li><li>If the backend resource is an ECS, the value is the NIC ID of the ECS where the VPC endpoint service is deployed.</li><li>If the backend resource is a virtual IP address, the value is the NIC ID of the physical server where virtual resources are created.</li></ul>
    </td>
    </tr>
    <tr id="row148431405813"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.1 "><p id="p769241384515"><a name="p769241384515"></a><a name="p769241384515"></a>pool_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p146925132458"><a name="p146925132458"></a><a name="p146925132458"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.51%" headers="mcps1.2.4.1.3 "><p id="p05087421426"><a name="p05087421426"></a><a name="p05087421426"></a>Specifies the ID of the cluster associated with the target VPCEP resource.</p>
    </td>
    </tr>
    <tr id="row1428310195461"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.1 "><p id="p12948182619398"><a name="p12948182619398"></a><a name="p12948182619398"></a>vip_port_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p4948326133915"><a name="p4948326133915"></a><a name="p4948326133915"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.51%" headers="mcps1.2.4.1.3 "><p id="p2948122613917"><a name="p2948122613917"></a><a name="p2948122613917"></a>Specifies the ID of the virtual NIC to which the virtual IP address is bound.</p>
    </td>
    </tr>
    <tr id="row14179224135"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.1 "><p id="p43735040"><a name="p43735040"></a><a name="p43735040"></a>service_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p52877372"><a name="p52877372"></a><a name="p52877372"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.51%" headers="mcps1.2.4.1.3 "><p id="p55208773"><a name="p55208773"></a><a name="p55208773"></a>Specifies the name of the VPC endpoint service.</p>
    </td>
    </tr>
    <tr id="row27759212"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.1 "><p id="p33903709"><a name="p33903709"></a><a name="p33903709"></a>server_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p61845910"><a name="p61845910"></a><a name="p61845910"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.51%" headers="mcps1.2.4.1.3 "><p id="p1497382074811"><a name="p1497382074811"></a><a name="p1497382074811"></a>Specifies the resource type.</p>
    <a name="ul1417663314354"></a><a name="ul1417663314354"></a><ul id="ul1417663314354"><li><strong id="vpcep_06_0201_b111511354539"><a name="vpcep_06_0201_b111511354539"></a><a name="vpcep_06_0201_b111511354539"></a>VM</strong>: indicates the ECS.</li><li><strong id="vpcep_06_0201_b111348551533"><a name="vpcep_06_0201_b111348551533"></a><a name="vpcep_06_0201_b111348551533"></a>VIP</strong>: indicates the virtual IP address.</li><li><strong id="vpcep_06_0201_b1842415561432"><a name="vpcep_06_0201_b1842415561432"></a><a name="vpcep_06_0201_b1842415561432"></a>LB</strong>: indicates the enhanced load balancer.</li></ul>
    </td>
    </tr>
    <tr id="row178231600145"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.1 "><p id="p6282859"><a name="p6282859"></a><a name="p6282859"></a>vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p39149581"><a name="p39149581"></a><a name="p39149581"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.51%" headers="mcps1.2.4.1.3 "><p id="p16536246191512"><a name="p16536246191512"></a><a name="p16536246191512"></a>Specifies the ID of the VPC to which the backend resource of the VPC endpoint service belongs.</p>
    </td>
    </tr>
    <tr id="row9032989"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.1 "><p id="p60583479"><a name="p60583479"></a><a name="p60583479"></a>approval_enabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p8314749"><a name="p8314749"></a><a name="p8314749"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.51%" headers="mcps1.2.4.1.3 "><p id="p126331454145319"><a name="p126331454145319"></a><a name="p126331454145319"></a>Specifies whether connection approval is required.</p>
    <a name="ul175221837143510"></a><a name="ul175221837143510"></a><ul id="ul175221837143510"><li><strong id="vpcep_06_0201_b1836705966"><a name="vpcep_06_0201_b1836705966"></a><a name="vpcep_06_0201_b1836705966"></a>false</strong>: indicates that connection approval is not required. The created VPC endpoint is in the <strong id="vpcep_06_0201_b15309009"><a name="vpcep_06_0201_b15309009"></a><a name="vpcep_06_0201_b15309009"></a>Accepted</strong> state.</li><li><strong id="vpcep_06_0201_b1374184052"><a name="vpcep_06_0201_b1374184052"></a><a name="vpcep_06_0201_b1374184052"></a>true</strong>: indicates that connection approval is required. The created VPC endpoint is in the <strong id="vpcep_06_0201_b724489048"><a name="vpcep_06_0201_b724489048"></a><a name="vpcep_06_0201_b724489048"></a>Pending acceptance</strong> state until the owner of the associated VPC endpoint service approves the connection.</li></ul>
    </td>
    </tr>
    <tr id="row15872492"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.1 "><p id="p10603509"><a name="p10603509"></a><a name="p10603509"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p53577906"><a name="p53577906"></a><a name="p53577906"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.51%" headers="mcps1.2.4.1.3 "><p id="p44843148"><a name="p44843148"></a><a name="p44843148"></a>Specifies the status of the VPC endpoint service.</p>
    <p id="p2073619194316"><a name="p2073619194316"></a><a name="p2073619194316"></a><strong id="b21426442018"><a name="b21426442018"></a><a name="b21426442018"></a>available</strong>: indicates the VPC endpoint service is connectable.</p>
    </td>
    </tr>
    <tr id="row36653303"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.1 "><p id="p16127536"><a name="p16127536"></a><a name="p16127536"></a>service_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p31262001"><a name="p31262001"></a><a name="p31262001"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.51%" headers="mcps1.2.4.1.3 "><p id="p135911520141219"><a name="p135911520141219"></a><a name="p135911520141219"></a>Specifies the type of the VPC endpoint service.</p>
    <div class="p" id="p3359114552814"><a name="p3359114552814"></a><a name="p3359114552814"></a>There are two types of VPC endpoint services: interface and gateway.<a name="vpcep_06_0201_ul87241928184613"></a><a name="vpcep_06_0201_ul87241928184613"></a><ul id="vpcep_06_0201_ul87241928184613"><li>Gateway: VPC endpoint services of this type are configured by operations people. You can use them directly without the need to create one by yourselves.</li><li>Interface: VPC endpoint services of this type include cloud services configured by operations people and private services created by yourselves. You cannot configure these cloud services, but can use them.</li></ul>
    </div>
    <p id="p941115410718"><a name="p941115410718"></a><a name="p941115410718"></a>You can perform the operations in <a href="creating-a-vpc-endpoint.md">Creating a VPC Endpoint</a> to create VPC endpoints for accessing VPC endpoints of the gateway and interface types.</p>
    </td>
    </tr>
    <tr id="row40094141"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.1 "><p id="p26400027"><a name="p26400027"></a><a name="p26400027"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p58027453"><a name="p58027453"></a><a name="p58027453"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.51%" headers="mcps1.2.4.1.3 "><p id="p22890001"><a name="p22890001"></a><a name="p22890001"></a>Specifies the creation time of the VPC endpoint service.</p>
    <p id="p871616113394"><a name="p871616113394"></a><a name="p871616113394"></a>The UTC time format is used: YYYY-MM-DDTHH:MM:SSZ.</p>
    </td>
    </tr>
    <tr id="row23429487"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.1 "><p id="p18740332"><a name="p18740332"></a><a name="p18740332"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p41571913"><a name="p41571913"></a><a name="p41571913"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.51%" headers="mcps1.2.4.1.3 "><p id="p27321481"><a name="p27321481"></a><a name="p27321481"></a>Specifies the update time of the VPC endpoint service.</p>
    <p id="p181016810016"><a name="p181016810016"></a><a name="p181016810016"></a>The UTC time format is used: YYYY-MM-DDTHH:MM:SSZ.</p>
    </td>
    </tr>
    <tr id="row39827108"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.1 "><p id="p4770281"><a name="p4770281"></a><a name="p4770281"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p50848458"><a name="p50848458"></a><a name="p50848458"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.51%" headers="mcps1.2.4.1.3 "><p id="p25084465"><a name="p25084465"></a><a name="p25084465"></a>Specifies the project ID. For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row671754016266"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.1 "><p id="p20857123514817"><a name="p20857123514817"></a><a name="p20857123514817"></a>cidr_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p1185733574815"><a name="p1185733574815"></a><a name="p1185733574815"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.51%" headers="mcps1.2.4.1.3 "><p id="p12391036114918"><a name="p12391036114918"></a><a name="p12391036114918"></a>Specifies the network segment type. The value can be <strong id="b18302193614543"><a name="b18302193614543"></a><a name="b18302193614543"></a>public</strong> or <strong id="b2849133725418"><a name="b2849133725418"></a><a name="b2849133725418"></a>internal</strong>.</p>
    <a name="ul159453471498"></a><a name="ul159453471498"></a><ul id="ul159453471498"><li><strong id="b12976154418541"><a name="b12976154418541"></a><a name="b12976154418541"></a>public</strong>: indicates the public subnet CIDR block.</li><li><strong id="b49313257011"><a name="b49313257011"></a><a name="b49313257011"></a>internal</strong>: indicates the private subnet CIDR block.</li></ul>
    <p id="p1183713122495"><a name="p1183713122495"></a><a name="p1183713122495"></a>The default value is <strong id="b789259195017"><a name="b789259195017"></a><a name="b789259195017"></a>internal</strong>.</p>
    </td>
    </tr>
    <tr id="row24433593"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.1 "><p id="p32964001"><a name="p32964001"></a><a name="p32964001"></a>ports</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p52838401"><a name="p52838401"></a><a name="p52838401"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.51%" headers="mcps1.2.4.1.3 "><p id="p18151624114718"><a name="p18151624114718"></a><a name="p18151624114718"></a>Lists the port mappings opened to the VPC endpoint service. For details, see <a href="#table20064649">Table 5</a>.</p>
    <p id="p4537192002"><a name="p4537192002"></a><a name="p4537192002"></a>Duplicate port mappings are not allowed in the same VPC endpoint service. If multiple VPC endpoint services share the same <strong id="vpcep_06_0201_b159801931141111"><a name="vpcep_06_0201_b159801931141111"></a><a name="vpcep_06_0201_b159801931141111"></a>port_id</strong> value, service ports and terminal ports of all these endpoint services cannot be duplicated when the protocol is the same.</p>
    </td>
    </tr>
    <tr id="row1391314467277"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.1 "><p id="p7185174718259"><a name="p7185174718259"></a><a name="p7185174718259"></a>tcp_proxy</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p218516477257"><a name="p218516477257"></a><a name="p218516477257"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.51%" headers="mcps1.2.4.1.3 "><p id="p3988426182213"><a name="p3988426182213"></a><a name="p3988426182213"></a>Specifies whether the client IP address and port number or <strong id="vpcep_06_0201_b1340623194912"><a name="vpcep_06_0201_b1340623194912"></a><a name="vpcep_06_0201_b1340623194912"></a>marker_id</strong> information is transmitted to the server. The following methods are supported:</p>
    <a name="ul113422343220"></a><a name="ul113422343220"></a><ul id="ul113422343220"><li>TCP TOA: The client information is inserted into field <strong id="vpcep_06_0201_b1328024583915"><a name="vpcep_06_0201_b1328024583915"></a><a name="vpcep_06_0201_b1328024583915"></a>tcp option</strong> and transmitted to the server.</li><li>Proxy Protocol: The client information is inserted into field <strong id="vpcep_06_0201_b18340846124016"><a name="vpcep_06_0201_b18340846124016"></a><a name="vpcep_06_0201_b18340846124016"></a>tcp payload</strong> and transmitted to the server.</li></ul>
    <p id="p117219186296"><a name="p117219186296"></a><a name="p117219186296"></a>This parameter is available only when the server can parse fields <strong id="vpcep_06_0201_b1246063817713"><a name="vpcep_06_0201_b1246063817713"></a><a name="vpcep_06_0201_b1246063817713"></a>tcp option</strong> and <strong id="vpcep_06_0201_b832154415710"><a name="vpcep_06_0201_b832154415710"></a><a name="vpcep_06_0201_b832154415710"></a>tcp payload</strong>.</p>
    <p id="p29385542114"><a name="p29385542114"></a><a name="p29385542114"></a>The values are as follows:</p>
    <a name="ul523712223"></a><a name="ul523712223"></a><ul id="ul523712223"><li><strong id="vpcep_06_0201_b485111422"><a name="vpcep_06_0201_b485111422"></a><a name="vpcep_06_0201_b485111422"></a>close</strong>: indicates that the TOA and Proxy Protocol methods are neither used.</li><li><strong id="vpcep_06_0201_b1432825911248"><a name="vpcep_06_0201_b1432825911248"></a><a name="vpcep_06_0201_b1432825911248"></a>toa_open</strong>: indicates that the TOA method is used.</li><li><strong id="vpcep_06_0201_b1394119162519"><a name="vpcep_06_0201_b1394119162519"></a><a name="vpcep_06_0201_b1394119162519"></a>proxy_open</strong>: indicates that the Proxy Protocol method is used.</li><li><strong id="vpcep_06_0201_b123462452517"><a name="vpcep_06_0201_b123462452517"></a><a name="vpcep_06_0201_b123462452517"></a>open</strong>: indicates that the TOA and Proxy Protocol methods are both used.</li></ul>
    <p id="p1725615331720"><a name="p1725615331720"></a><a name="p1725615331720"></a>The default value is <strong id="vpcep_06_0201_b842352706144841"><a name="vpcep_06_0201_b842352706144841"></a><a name="vpcep_06_0201_b842352706144841"></a>close</strong>.</p>
    </td>
    </tr>
    <tr id="row12807657141616"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.1 "><p id="p13103244015"><a name="p13103244015"></a><a name="p13103244015"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p21037441512"><a name="p21037441512"></a><a name="p21037441512"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.51%" headers="mcps1.2.4.1.3 "><p id="p1510414411116"><a name="p1510414411116"></a><a name="p1510414411116"></a>Lists the resource tags. For details, see <a href="#table489217571060">Table 6</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5**  Port mapping parameters

    <a name="table20064649"></a>
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

    **Table  6** **ResourceTags**  parameters

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


## Status Code<a name="section19041619"></a>

For details about status codes, see  [Status Code](status-code.md).

