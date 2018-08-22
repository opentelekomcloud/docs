# Querying Subnets<a name="EN-US_TOPIC_0020090592"></a>

## Function<a name="section49967061"></a>

This interface is used to query subnets using search criteria and to display the subnets in a list.

## URI<a name="section47050372"></a>

-   GET /v1/\{tenant\_id\}/subnets
-   Example:

    ```
    /v1/{tenant_id}/subnets?limit=10&marker=4779ab1c-7c1a-44b1-a02e-93dfc361b32d&vpc_id=3ec3b33f-ac1c-4630-ad1c-7dba1ed79d85
    ```

-   Parameter description

    <a name="table42526340"></a><table><thead align="left"><tr id="row55636561"><th class="cellrowborder" valign="top" width="20.11201120112011%" id="mcps1.1.5.1.1"><p id="p10267631"><a name="p10267631"></a><a name="p10267631"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.04180418041804%" id="mcps1.1.5.1.2"><p id="p26371793"><a name="p26371793"></a><a name="p26371793"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.72137213721372%" id="mcps1.1.5.1.3"><p id="p6814361175820"><a name="p6814361175820"></a><a name="p6814361175820"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="48.12481248124813%" id="mcps1.1.5.1.4"><p id="p55740512"><a name="p55740512"></a><a name="p55740512"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row18687619"><td class="cellrowborder" valign="top" width="20.11201120112011%" headers="mcps1.1.5.1.1 "><p id="p37302179"><a name="p37302179"></a><a name="p37302179"></a>tenant_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.04180418041804%" headers="mcps1.1.5.1.2 "><p id="p1577639"><a name="p1577639"></a><a name="p1577639"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.72137213721372%" headers="mcps1.1.5.1.3 "><p id="p15092369175820"><a name="p15092369175820"></a><a name="p15092369175820"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.12481248124813%" headers="mcps1.1.5.1.4 "><p id="p60679928"><a name="p60679928"></a><a name="p60679928"></a>Specifies the tenant ID of the operator.</p>
    </td>
    </tr>
    <tr id="row9248440"><td class="cellrowborder" valign="top" width="20.11201120112011%" headers="mcps1.1.5.1.1 "><p id="p10926182"><a name="p10926182"></a><a name="p10926182"></a>marker</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.04180418041804%" headers="mcps1.1.5.1.2 "><p id="p12605589"><a name="p12605589"></a><a name="p12605589"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.72137213721372%" headers="mcps1.1.5.1.3 "><p id="p14522390175820"><a name="p14522390175820"></a><a name="p14522390175820"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.12481248124813%" headers="mcps1.1.5.1.4 "><p id="p28526205175853"><a name="p28526205175853"></a><a name="p28526205175853"></a>Specifies the resource ID of pagination query. If the parameter is left blank, only resources on the first page are queried.</p>
    </td>
    </tr>
    <tr id="row43066942"><td class="cellrowborder" valign="top" width="20.11201120112011%" headers="mcps1.1.5.1.1 "><p id="p65870306"><a name="p65870306"></a><a name="p65870306"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.04180418041804%" headers="mcps1.1.5.1.2 "><p id="p33894570"><a name="p33894570"></a><a name="p33894570"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.72137213721372%" headers="mcps1.1.5.1.3 "><p id="p35462927175820"><a name="p35462927175820"></a><a name="p35462927175820"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.12481248124813%" headers="mcps1.1.5.1.4 "><p id="p61105663"><a name="p61105663"></a><a name="p61105663"></a>Specifies the number of records returned on each page.</p>
    <p id="p50611656"><a name="p50611656"></a><a name="p50611656"></a>The value ranges from 0 to intmax.</p>
    </td>
    </tr>
    <tr id="row4071301142654"><td class="cellrowborder" valign="top" width="20.11201120112011%" headers="mcps1.1.5.1.1 "><p id="p61339955142654"><a name="p61339955142654"></a><a name="p61339955142654"></a>vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.04180418041804%" headers="mcps1.1.5.1.2 "><p id="p2480462142654"><a name="p2480462142654"></a><a name="p2480462142654"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.72137213721372%" headers="mcps1.1.5.1.3 "><p id="p66699709142654"><a name="p66699709142654"></a><a name="p66699709142654"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.12481248124813%" headers="mcps1.1.5.1.4 "><p id="p2678389014283"><a name="p2678389014283"></a><a name="p2678389014283"></a>Specifies that the VPC ID is used as the filtering condition.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section20800170"></a>

-   Parameter description

    None

-   Example request

    None


## Response<a name="section52983808"></a>

-   Parameter description

    <a name="table162269121588"></a><table><thead align="left"><tr id="row95582811588"><th class="cellrowborder" valign="top" width="18.34%" id="mcps1.1.4.1.1"><p id="p360232861588"><a name="p360232861588"></a><a name="p360232861588"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.15%" id="mcps1.1.4.1.2"><p id="p584710571588"><a name="p584710571588"></a><a name="p584710571588"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="59.51%" id="mcps1.1.4.1.3"><p id="p385351831588"><a name="p385351831588"></a><a name="p385351831588"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row343421581588"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.1.4.1.1 "><p id="p302514461588"><a name="p302514461588"></a><a name="p302514461588"></a>subnets</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.15%" headers="mcps1.1.4.1.2 "><p id="p388283181588"><a name="p388283181588"></a><a name="p388283181588"></a><em id="i1342385115821"><a name="i1342385115821"></a><a name="i1342385115821"></a>List data structure</em></p>
    </td>
    <td class="cellrowborder" valign="top" width="59.51%" headers="mcps1.1.4.1.3 "><p id="p530125231588"><a name="p530125231588"></a><a name="p530125231588"></a>Specifies the subnet list objects.</p>
    </td>
    </tr>
    </tbody>
    </table>

    Descriptions of  **subnets**  fields

    <a name="table946390317596"></a><table><thead align="left"><tr id="row2260217717596"><th class="cellrowborder" valign="top" width="29.017098290170978%" id="mcps1.1.4.1.1"><p id="p1883706917596"><a name="p1883706917596"></a><a name="p1883706917596"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.6983301669833%" id="mcps1.1.4.1.2"><p id="p4259704317596"><a name="p4259704317596"></a><a name="p4259704317596"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="54.284571542845704%" id="mcps1.1.4.1.3"><p id="p2780847717596"><a name="p2780847717596"></a><a name="p2780847717596"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3789415517596"><td class="cellrowborder" valign="top" width="29.017098290170978%" headers="mcps1.1.4.1.1 "><p id="p4952771817596"><a name="p4952771817596"></a><a name="p4952771817596"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.6983301669833%" headers="mcps1.1.4.1.2 "><p id="p1023955317596"><a name="p1023955317596"></a><a name="p1023955317596"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.284571542845704%" headers="mcps1.1.4.1.3 "><p id="p2409742517596"><a name="p2409742517596"></a><a name="p2409742517596"></a>Specifies a resource ID in UUID format.</p>
    </td>
    </tr>
    <tr id="row1555023417596"><td class="cellrowborder" valign="top" width="29.017098290170978%" headers="mcps1.1.4.1.1 "><p id="p5160943617596"><a name="p5160943617596"></a><a name="p5160943617596"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.6983301669833%" headers="mcps1.1.4.1.2 "><p id="p4529288117596"><a name="p4529288117596"></a><a name="p4529288117596"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.284571542845704%" headers="mcps1.1.4.1.3 "><p id="p4484475717596"><a name="p4484475717596"></a><a name="p4484475717596"></a>Specifies the subnet name.</p>
    </td>
    </tr>
    <tr id="row94962917596"><td class="cellrowborder" valign="top" width="29.017098290170978%" headers="mcps1.1.4.1.1 "><p id="p981112017596"><a name="p981112017596"></a><a name="p981112017596"></a>cidr</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.6983301669833%" headers="mcps1.1.4.1.2 "><p id="p1336165217596"><a name="p1336165217596"></a><a name="p1336165217596"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.284571542845704%" headers="mcps1.1.4.1.3 "><p id="p855202117596"><a name="p855202117596"></a><a name="p855202117596"></a>Specifies the subnet network segment.</p>
    </td>
    </tr>
    <tr id="row985932517596"><td class="cellrowborder" valign="top" width="29.017098290170978%" headers="mcps1.1.4.1.1 "><p id="p6040786717596"><a name="p6040786717596"></a><a name="p6040786717596"></a>gateway_ip</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.6983301669833%" headers="mcps1.1.4.1.2 "><p id="p5817993817596"><a name="p5817993817596"></a><a name="p5817993817596"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.284571542845704%" headers="mcps1.1.4.1.3 "><p id="p1495452217596"><a name="p1495452217596"></a><a name="p1495452217596"></a>Specifies the subnet gateway address.</p>
    </td>
    </tr>
    <tr id="row37297117596"><td class="cellrowborder" valign="top" width="29.017098290170978%" headers="mcps1.1.4.1.1 "><p id="p3021071917596"><a name="p3021071917596"></a><a name="p3021071917596"></a>dhcp_enable</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.6983301669833%" headers="mcps1.1.4.1.2 "><p id="p4005526017596"><a name="p4005526017596"></a><a name="p4005526017596"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.284571542845704%" headers="mcps1.1.4.1.3 "><p id="p2325061317596"><a name="p2325061317596"></a><a name="p2325061317596"></a>Specifies whether the DHCP function is enabled for the subnet.</p>
    </td>
    </tr>
    <tr id="row792892917596"><td class="cellrowborder" valign="top" width="29.017098290170978%" headers="mcps1.1.4.1.1 "><p id="p3826349217596"><a name="p3826349217596"></a><a name="p3826349217596"></a>primary_dns</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.6983301669833%" headers="mcps1.1.4.1.2 "><p id="p5962058717596"><a name="p5962058717596"></a><a name="p5962058717596"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.284571542845704%" headers="mcps1.1.4.1.3 "><p id="p6453823917596"><a name="p6453823917596"></a><a name="p6453823917596"></a>Specifies the IP address of DNS server 1 on the subnet.</p>
    </td>
    </tr>
    <tr id="row4397324617596"><td class="cellrowborder" valign="top" width="29.017098290170978%" headers="mcps1.1.4.1.1 "><p id="p506319417596"><a name="p506319417596"></a><a name="p506319417596"></a>secondary_dns</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.6983301669833%" headers="mcps1.1.4.1.2 "><p id="p73411217596"><a name="p73411217596"></a><a name="p73411217596"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.284571542845704%" headers="mcps1.1.4.1.3 "><p id="p5946313017596"><a name="p5946313017596"></a><a name="p5946313017596"></a>Specifies the IP address of DNS server 2 on the subnet.</p>
    </td>
    </tr>
    <tr id="row545834911143"><td class="cellrowborder" valign="top" width="29.017098290170978%" headers="mcps1.1.4.1.1 "><p id="p591866701143"><a name="p591866701143"></a><a name="p591866701143"></a>dnsList</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.6983301669833%" headers="mcps1.1.4.1.2 "><p id="p318589811143"><a name="p318589811143"></a><a name="p318589811143"></a>List</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.284571542845704%" headers="mcps1.1.4.1.3 "><p id="p304407061143"><a name="p304407061143"></a><a name="p304407061143"></a>Specifies the IP address list of DNS servers on the subnet.</p>
    </td>
    </tr>
    <tr id="row6540612517596"><td class="cellrowborder" valign="top" width="29.017098290170978%" headers="mcps1.1.4.1.1 "><p id="p6340476417596"><a name="p6340476417596"></a><a name="p6340476417596"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.6983301669833%" headers="mcps1.1.4.1.2 "><p id="p5792277317596"><a name="p5792277317596"></a><a name="p5792277317596"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.284571542845704%" headers="mcps1.1.4.1.3 "><p id="p6123300617596"><a name="p6123300617596"></a><a name="p6123300617596"></a>Identifies the AZ to which the subnet belongs.</p>
    </td>
    </tr>
    <tr id="row1422614217596"><td class="cellrowborder" valign="top" width="29.017098290170978%" headers="mcps1.1.4.1.1 "><p id="p1146682617596"><a name="p1146682617596"></a><a name="p1146682617596"></a>vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.6983301669833%" headers="mcps1.1.4.1.2 "><p id="p481418517596"><a name="p481418517596"></a><a name="p481418517596"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.284571542845704%" headers="mcps1.1.4.1.3 "><p id="p5440471517596"><a name="p5440471517596"></a><a name="p5440471517596"></a>Specifies the ID of the VPC to which the subnet belongs.</p>
    </td>
    </tr>
    <tr id="row1988039417596"><td class="cellrowborder" valign="top" width="29.017098290170978%" headers="mcps1.1.4.1.1 "><p id="p6680804517596"><a name="p6680804517596"></a><a name="p6680804517596"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.6983301669833%" headers="mcps1.1.4.1.2 "><p id="p3959872717596"><a name="p3959872717596"></a><a name="p3959872717596"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.284571542845704%" headers="mcps1.1.4.1.3 "><p id="p5338030017596"><a name="p5338030017596"></a><a name="p5338030017596"></a>Specifies the status of the subnet.</p>
    <p id="p1066065817596"><a name="p1066065817596"></a><a name="p1066065817596"></a>The value can be <strong>ACTIVE</strong>,&nbsp;<strong>DOWN</strong>,&nbsp;<strong>UNKNOWN</strong>, or&nbsp;<strong>ERROR</strong>.</p>
    </td>
    </tr>
    <tr id="row6437766611027"><td class="cellrowborder" valign="top" width="29.017098290170978%" headers="mcps1.1.4.1.1 "><p id="p2150517711033"><a name="p2150517711033"></a><a name="p2150517711033"></a>neutron_network_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.6983301669833%" headers="mcps1.1.4.1.2 "><p id="p3263900011033"><a name="p3263900011033"></a><a name="p3263900011033"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.284571542845704%" headers="mcps1.1.4.1.3 "><p id="p2651330711033"><a name="p2651330711033"></a><a name="p2651330711033"></a>Specifies the network (Native OpenStack API) ID.</p>
    </td>
    </tr>
    <tr id="row2552805011031"><td class="cellrowborder" valign="top" width="29.017098290170978%" headers="mcps1.1.4.1.1 "><p id="p84866711033"><a name="p84866711033"></a><a name="p84866711033"></a>neutron_subnet_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.6983301669833%" headers="mcps1.1.4.1.2 "><p id="p6517899211033"><a name="p6517899211033"></a><a name="p6517899211033"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.284571542845704%" headers="mcps1.1.4.1.3 "><p id="p4500696511033"><a name="p4500696511033"></a><a name="p4500696511033"></a>Specifies the subnet (Native OpenStack API) ID.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "subnets": [
            {
                "id": "4779ab1c-7c1a-44b1-a02e-93dfc361b32d",
                "name": "subnet",
                "cidr": "192.168.20.0/24",
                "dnsList": [
                    "114.xx.xx.114",
                    "114.xx.xx.115"
                ],
                "status": "ACTIVE",
                "vpc_id": "3ec3b33f-ac1c-4630-ad1c-7dba1ed79d85",
                "gateway_ip": "192.168.20.1",
                "dhcp_enable": true,
                "primary_dns": "114.xx.xx.114",
                "secondary_dns": "114.xx.xx.115",
                "availability_zone": "aa-bb-cc"//For example, the AZ name is aa-bb-cc.
                "neutron_network_id": "4779ab1c-7c1a-44b1-a02e-93dfc361b32d",
                "neutron_subnet_id": "213cb9d-3122-2ac1-1a29-91ffc1231a12"
    
            },
            {
                "id": "531dec0f-3116-411b-a21b-e612e42349fd",
                "name": "Subnet1",
                "cidr": "192.168.1.0/24",
                "dnsList": [
                    "114.xx.xx.114",
                    "114.xx.xx.115"
                ],
                "status": "ACTIVE",
                "vpc_id": "3ec3b33f-ac1c-4630-ad1c-7dba1ed79d85",
                "gateway_ip": "192.168.1.1",
                "dhcp_enable": true,
                "primary_dns": "114.xx.xx.114",
                "secondary_dns": "114.xx.xx.115",
                "availability_zone": "aa-bb-cc"//For example, the AZ name is aa-bb-cc.
                "neutron_network_id": "531dec0f-3116-411b-a21b-e612e42349fd",
                "neutron_subnet_id": "1aac193-a2ad-f153-d122-12d64c2c1d78"
            }
        ]
    }
    ```


## Returned Value<a name="section7092232"></a>

-   Normal

    200

-   Abnormal

    <a name="table406008069542"></a><table><thead align="left"><tr id="row399748249542"><th class="cellrowborder" valign="top" width="43.419999999999995%" id="mcps1.1.3.1.1"><p id="p167352919542"><a name="p167352919542"></a><a name="p167352919542"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.58%" id="mcps1.1.3.1.2"><p id="p133813029542"><a name="p133813029542"></a><a name="p133813029542"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row101436829542"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p163319109542"><a name="p163319109542"></a><a name="p163319109542"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p478163639542"><a name="p478163639542"></a><a name="p478163639542"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row276940899542"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p286287709542"><a name="p286287709542"></a><a name="p286287709542"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p372290399542"><a name="p372290399542"></a><a name="p372290399542"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row666259019542"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p279889009542"><a name="p279889009542"></a><a name="p279889009542"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p525084199542"><a name="p525084199542"></a><a name="p525084199542"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row28137309542"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p265855539542"><a name="p265855539542"></a><a name="p265855539542"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p59461739542"><a name="p59461739542"></a><a name="p59461739542"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row535155579542"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p397928229542"><a name="p397928229542"></a><a name="p397928229542"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p19931449542"><a name="p19931449542"></a><a name="p19931449542"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row179382989542"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p437160729542"><a name="p437160729542"></a><a name="p437160729542"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p513409549542"><a name="p513409549542"></a><a name="p513409549542"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row594154099542"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p479187889542"><a name="p479187889542"></a><a name="p479187889542"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p562166579542"><a name="p562166579542"></a><a name="p562166579542"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row361878689542"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p455361769542"><a name="p455361769542"></a><a name="p455361769542"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p645516339542"><a name="p645516339542"></a><a name="p645516339542"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row440937859542"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p148268399542"><a name="p148268399542"></a><a name="p148268399542"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p601233509542"><a name="p601233509542"></a><a name="p601233509542"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row42392469542"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p78346089542"><a name="p78346089542"></a><a name="p78346089542"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p306235279542"><a name="p306235279542"></a><a name="p306235279542"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row71762949542"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p444089519542"><a name="p444089519542"></a><a name="p444089519542"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p403552809542"><a name="p403552809542"></a><a name="p403552809542"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row276532089542"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p253173619542"><a name="p253173619542"></a><a name="p253173619542"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p374403599542"><a name="p374403599542"></a><a name="p374403599542"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row14189129542"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p478230199542"><a name="p478230199542"></a><a name="p478230199542"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p484593359542"><a name="p484593359542"></a><a name="p484593359542"></a>Failed to complete the request because the service is unavailable.</p>
    </td>
    </tr>
    <tr id="row334808359542"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p275930829542"><a name="p275930829542"></a><a name="p275930829542"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p204471909542"><a name="p204471909542"></a><a name="p204471909542"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section85821649202813"></a>

For details, see section  [Error Codes](error-codes-27.md).

