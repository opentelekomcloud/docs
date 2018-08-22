# Querying Subnet Details<a name="EN-US_TOPIC_0020090591"></a>

## Function<a name="section6925935"></a>

This interface is used to query details about a subnet.

## URI<a name="section62333418"></a>

-   GET /v1/\{tenant\_id\}/subnets/\{subnet\_id\}
-   Parameter description

    <a name="table61566768"></a><table><thead align="left"><tr id="row44407631"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="p40248354"><a name="p40248354"></a><a name="p40248354"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="p38891250"><a name="p38891250"></a><a name="p38891250"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="p63183526"><a name="p63183526"></a><a name="p63183526"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row17591975"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p15663836"><a name="p15663836"></a><a name="p15663836"></a>tenant_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p60811181"><a name="p60811181"></a><a name="p60811181"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p26758660"><a name="p26758660"></a><a name="p26758660"></a>Specifies the tenant ID of the operator.</p>
    </td>
    </tr>
    <tr id="row39501348"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p45492604"><a name="p45492604"></a><a name="p45492604"></a>subnet_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p61022284"><a name="p61022284"></a><a name="p61022284"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p43857981"><a name="p43857981"></a><a name="p43857981"></a>Specifies the subnet ID, which uniquely identifies the subnet.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section24129853"></a>

-   Parameter description

    None

-   Example request

    None


## Response<a name="section15842089"></a>

-   Parameter description

    <a name="table6005374015751"></a><table><thead align="left"><tr id="row4874046215751"><th class="cellrowborder" valign="top" width="18.34%" id="mcps1.1.4.1.1"><p id="p5566332215751"><a name="p5566332215751"></a><a name="p5566332215751"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="24.84%" id="mcps1.1.4.1.2"><p id="p62309715751"><a name="p62309715751"></a><a name="p62309715751"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.82000000000001%" id="mcps1.1.4.1.3"><p id="p5047090715751"><a name="p5047090715751"></a><a name="p5047090715751"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6161169015751"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.1.4.1.1 "><p id="p2449098915751"><a name="p2449098915751"></a><a name="p2449098915751"></a>subnet</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.84%" headers="mcps1.1.4.1.2 "><p id="p2676232115751"><a name="p2676232115751"></a><a name="p2676232115751"></a><em id="i3953430015751"><a name="i3953430015751"></a><a name="i3953430015751"></a>Dictionary data structure</em></p>
    </td>
    <td class="cellrowborder" valign="top" width="56.82000000000001%" headers="mcps1.1.4.1.3 "><p id="p4816174615751"><a name="p4816174615751"></a><a name="p4816174615751"></a>Specifies the subnet objects.</p>
    </td>
    </tr>
    </tbody>
    </table>

    Descriptions of  **subnet**  fields

    <a name="table6614597017585"></a><table><thead align="left"><tr id="row5931021317585"><th class="cellrowborder" valign="top" width="28.95%" id="mcps1.1.4.1.1"><p id="p3939794017585"><a name="p3939794017585"></a><a name="p3939794017585"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.950000000000003%" id="mcps1.1.4.1.2"><p id="p5365431717585"><a name="p5365431717585"></a><a name="p5365431717585"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="51.1%" id="mcps1.1.4.1.3"><p id="p5103239017585"><a name="p5103239017585"></a><a name="p5103239017585"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3998288717585"><td class="cellrowborder" valign="top" width="28.95%" headers="mcps1.1.4.1.1 "><p id="p1738840917585"><a name="p1738840917585"></a><a name="p1738840917585"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.950000000000003%" headers="mcps1.1.4.1.2 "><p id="p28481417585"><a name="p28481417585"></a><a name="p28481417585"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.1%" headers="mcps1.1.4.1.3 "><p id="p2306998617585"><a name="p2306998617585"></a><a name="p2306998617585"></a>Specifies a resource ID in UUID format.</p>
    </td>
    </tr>
    <tr id="row630328217585"><td class="cellrowborder" valign="top" width="28.95%" headers="mcps1.1.4.1.1 "><p id="p4080382917585"><a name="p4080382917585"></a><a name="p4080382917585"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.950000000000003%" headers="mcps1.1.4.1.2 "><p id="p1666748117585"><a name="p1666748117585"></a><a name="p1666748117585"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.1%" headers="mcps1.1.4.1.3 "><p id="p788871417585"><a name="p788871417585"></a><a name="p788871417585"></a>Specifies the subnet name.</p>
    </td>
    </tr>
    <tr id="row388956217585"><td class="cellrowborder" valign="top" width="28.95%" headers="mcps1.1.4.1.1 "><p id="p4661911217585"><a name="p4661911217585"></a><a name="p4661911217585"></a>cidr</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.950000000000003%" headers="mcps1.1.4.1.2 "><p id="p5290705517585"><a name="p5290705517585"></a><a name="p5290705517585"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.1%" headers="mcps1.1.4.1.3 "><p id="p5761304717585"><a name="p5761304717585"></a><a name="p5761304717585"></a>Specifies the subnet network segment.</p>
    </td>
    </tr>
    <tr id="row4875537617585"><td class="cellrowborder" valign="top" width="28.95%" headers="mcps1.1.4.1.1 "><p id="p5687141217585"><a name="p5687141217585"></a><a name="p5687141217585"></a>gateway_ip</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.950000000000003%" headers="mcps1.1.4.1.2 "><p id="p805358517585"><a name="p805358517585"></a><a name="p805358517585"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.1%" headers="mcps1.1.4.1.3 "><p id="p4836063417585"><a name="p4836063417585"></a><a name="p4836063417585"></a>Specifies the subnet gateway address.</p>
    </td>
    </tr>
    <tr id="row3259252617585"><td class="cellrowborder" valign="top" width="28.95%" headers="mcps1.1.4.1.1 "><p id="p2274892917585"><a name="p2274892917585"></a><a name="p2274892917585"></a>dhcp_enable</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.950000000000003%" headers="mcps1.1.4.1.2 "><p id="p561056817585"><a name="p561056817585"></a><a name="p561056817585"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.1%" headers="mcps1.1.4.1.3 "><p id="p5180286017585"><a name="p5180286017585"></a><a name="p5180286017585"></a>Specifies whether the DHCP function is enabled for the subnet.</p>
    </td>
    </tr>
    <tr id="row6357256317585"><td class="cellrowborder" valign="top" width="28.95%" headers="mcps1.1.4.1.1 "><p id="p4910399917585"><a name="p4910399917585"></a><a name="p4910399917585"></a>primary_dns</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.950000000000003%" headers="mcps1.1.4.1.2 "><p id="p4879619717585"><a name="p4879619717585"></a><a name="p4879619717585"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.1%" headers="mcps1.1.4.1.3 "><p id="p6017790317585"><a name="p6017790317585"></a><a name="p6017790317585"></a>Specifies the IP address of DNS server 1 on the subnet.</p>
    </td>
    </tr>
    <tr id="row473021817585"><td class="cellrowborder" valign="top" width="28.95%" headers="mcps1.1.4.1.1 "><p id="p4760336917585"><a name="p4760336917585"></a><a name="p4760336917585"></a>secondary_dns</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.950000000000003%" headers="mcps1.1.4.1.2 "><p id="p105619417585"><a name="p105619417585"></a><a name="p105619417585"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.1%" headers="mcps1.1.4.1.3 "><p id="p1844285917585"><a name="p1844285917585"></a><a name="p1844285917585"></a>Specifies the IP address of DNS server 2 on the subnet.</p>
    </td>
    </tr>
    <tr id="row5602880311213"><td class="cellrowborder" valign="top" width="28.95%" headers="mcps1.1.4.1.1 "><p id="p4203922911213"><a name="p4203922911213"></a><a name="p4203922911213"></a>dnsList</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.950000000000003%" headers="mcps1.1.4.1.2 "><p id="p195587511213"><a name="p195587511213"></a><a name="p195587511213"></a>List</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.1%" headers="mcps1.1.4.1.3 "><p id="p2420815811213"><a name="p2420815811213"></a><a name="p2420815811213"></a>Specifies the IP address list of DNS servers on the subnet.</p>
    </td>
    </tr>
    <tr id="row3176800317585"><td class="cellrowborder" valign="top" width="28.95%" headers="mcps1.1.4.1.1 "><p id="p2307142317585"><a name="p2307142317585"></a><a name="p2307142317585"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.950000000000003%" headers="mcps1.1.4.1.2 "><p id="p4112332617585"><a name="p4112332617585"></a><a name="p4112332617585"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.1%" headers="mcps1.1.4.1.3 "><p id="p4265512017585"><a name="p4265512017585"></a><a name="p4265512017585"></a>Identifies the AZ to which the subnet belongs.</p>
    </td>
    </tr>
    <tr id="row4835176717585"><td class="cellrowborder" valign="top" width="28.95%" headers="mcps1.1.4.1.1 "><p id="p2417901817585"><a name="p2417901817585"></a><a name="p2417901817585"></a>vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.950000000000003%" headers="mcps1.1.4.1.2 "><p id="p6029773217585"><a name="p6029773217585"></a><a name="p6029773217585"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.1%" headers="mcps1.1.4.1.3 "><p id="p5227810517585"><a name="p5227810517585"></a><a name="p5227810517585"></a>Specifies the ID of the VPC to which the subnet belongs.</p>
    </td>
    </tr>
    <tr id="row74090317585"><td class="cellrowborder" valign="top" width="28.95%" headers="mcps1.1.4.1.1 "><p id="p6001314817585"><a name="p6001314817585"></a><a name="p6001314817585"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.950000000000003%" headers="mcps1.1.4.1.2 "><p id="p1856038817585"><a name="p1856038817585"></a><a name="p1856038817585"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.1%" headers="mcps1.1.4.1.3 "><p id="p39256569134811"><a name="p39256569134811"></a><a name="p39256569134811"></a>Specifies the status of the subnet.</p>
    <p id="p2699642217585"><a name="p2699642217585"></a><a name="p2699642217585"></a>The value can be <strong>ACTIVE</strong>, <strong>DOWN</strong>, <strong>UNKNOWN</strong>, or <strong>ERROR</strong>.</p>
    </td>
    </tr>
    <tr id="row21291622105956"><td class="cellrowborder" valign="top" width="28.95%" headers="mcps1.1.4.1.1 "><p id="p442246351103"><a name="p442246351103"></a><a name="p442246351103"></a>neutron_network_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.950000000000003%" headers="mcps1.1.4.1.2 "><p id="p462170191103"><a name="p462170191103"></a><a name="p462170191103"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.1%" headers="mcps1.1.4.1.3 "><p id="p525910351103"><a name="p525910351103"></a><a name="p525910351103"></a>Specifies the network (Native OpenStack API) ID.</p>
    </td>
    </tr>
    <tr id="row136513311102"><td class="cellrowborder" valign="top" width="28.95%" headers="mcps1.1.4.1.1 "><p id="p197036161103"><a name="p197036161103"></a><a name="p197036161103"></a>neutron_subnet_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.950000000000003%" headers="mcps1.1.4.1.2 "><p id="p237568301103"><a name="p237568301103"></a><a name="p237568301103"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.1%" headers="mcps1.1.4.1.3 "><p id="p452550761103"><a name="p452550761103"></a><a name="p452550761103"></a>Specifies the subnet (Native OpenStack API) ID.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "subnet": {
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
            "availability_zone": "aa-bb-cc"//AZ aa-bb-cc is used as an example.
            "neutron_network_id": "4779ab1c-7c1a-44b1-a02e-93dfc361b32d",
            "neutron_subnet_id": "213cb9d-3122-2ac1-1a29-91ffc1231a12"
        }
    }
    ```


## Returned Value<a name="section8361080"></a>

-   Normal

    200

-   Abnormal

    <a name="table2047757195354"></a><table><thead align="left"><tr id="row1261913895354"><th class="cellrowborder" valign="top" width="43.419999999999995%" id="mcps1.1.3.1.1"><p id="p1551725995354"><a name="p1551725995354"></a><a name="p1551725995354"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.58%" id="mcps1.1.3.1.2"><p id="p4893850195354"><a name="p4893850195354"></a><a name="p4893850195354"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row459567295354"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p3670513195354"><a name="p3670513195354"></a><a name="p3670513195354"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p2032560695354"><a name="p2032560695354"></a><a name="p2032560695354"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row4871273095354"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p5341709495354"><a name="p5341709495354"></a><a name="p5341709495354"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p3181732595354"><a name="p3181732595354"></a><a name="p3181732595354"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row1792047595354"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p4227239395354"><a name="p4227239395354"></a><a name="p4227239395354"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p151178395354"><a name="p151178395354"></a><a name="p151178395354"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row1360604795354"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p2834804195354"><a name="p2834804195354"></a><a name="p2834804195354"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p1448997595354"><a name="p1448997595354"></a><a name="p1448997595354"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row6330091595354"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p2710051595354"><a name="p2710051595354"></a><a name="p2710051595354"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p4765812495354"><a name="p4765812495354"></a><a name="p4765812495354"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row2626993395354"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p4748978995354"><a name="p4748978995354"></a><a name="p4748978995354"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p2146767395354"><a name="p2146767395354"></a><a name="p2146767395354"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row5899133695354"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p1356889895354"><a name="p1356889895354"></a><a name="p1356889895354"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p2533897395354"><a name="p2533897395354"></a><a name="p2533897395354"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row2672417095354"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p1717418595354"><a name="p1717418595354"></a><a name="p1717418595354"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p4893174095354"><a name="p4893174095354"></a><a name="p4893174095354"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row3773248195354"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p3643211095354"><a name="p3643211095354"></a><a name="p3643211095354"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p6531977995354"><a name="p6531977995354"></a><a name="p6531977995354"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row5100710595354"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p3793480695354"><a name="p3793480695354"></a><a name="p3793480695354"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p5282042395354"><a name="p5282042395354"></a><a name="p5282042395354"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row562176695354"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p5270993495354"><a name="p5270993495354"></a><a name="p5270993495354"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p4164624695354"><a name="p4164624695354"></a><a name="p4164624695354"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row3927189595354"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p2690695595354"><a name="p2690695595354"></a><a name="p2690695595354"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p3197974795354"><a name="p3197974795354"></a><a name="p3197974795354"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row1938227295354"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p2646023495354"><a name="p2646023495354"></a><a name="p2646023495354"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p6290423795354"><a name="p6290423795354"></a><a name="p6290423795354"></a>Failed to complete the request because the service is unavailable.</p>
    </td>
    </tr>
    <tr id="row2926722395354"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p2183483395354"><a name="p2183483395354"></a><a name="p2183483395354"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p2379103195354"><a name="p2379103195354"></a><a name="p2379103195354"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section85821649202813"></a>

For details, see section  [Error Codes](error-codes-27.md).

