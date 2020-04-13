# Updating a Floating IP Address<a name="vpc_ipv6_0004"></a>

## Function<a name="section937595992415"></a>

This API is used to update a specific floating IP address and the port associated with the IP address. If  **port\_id**  is left blank, the floating IP address has been unbound from the port.

Restrictions

When you bind a floating IP address, if the floating IP address is in the  **error**  state, try unbinding the address first.

You are not allowed to bind a floating IP address that has been bound to a port to another port. You must first unbind the IP address from its original port and bind it to the required port.

## URI<a name="section1037655913249"></a>

PUT /v2.0/eip/floatingips\_v6/\{floatingip\_id\}

## Request Message<a name="section5385259162414"></a>

-   Request parameter

    **Table  1**  Request parameter

    <a name="table14386115942419"></a>
    <table><thead align="left"><tr id="row1559165992415"><th class="cellrowborder" valign="top" width="19.39%" id="mcps1.2.5.1.1"><p id="p65917591245"><a name="p65917591245"></a><a name="p65917591245"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.659999999999998%" id="mcps1.2.5.1.2"><p id="p559185992415"><a name="p559185992415"></a><a name="p559185992415"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.310000000000002%" id="mcps1.2.5.1.3"><p id="p205911159152411"><a name="p205911159152411"></a><a name="p205911159152411"></a><strong id="b84235270615219"><a name="b84235270615219"></a><a name="b84235270615219"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="46.64%" id="mcps1.2.5.1.4"><p id="p6591115942414"><a name="p6591115942414"></a><a name="p6591115942414"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row159211597245"><td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.2.5.1.1 "><p id="p75923592248"><a name="p75923592248"></a><a name="p75923592248"></a>floatingip</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.659999999999998%" headers="mcps1.2.5.1.2 "><p id="p18592559172418"><a name="p18592559172418"></a><a name="p18592559172418"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.310000000000002%" headers="mcps1.2.5.1.3 "><p id="p25921159132414"><a name="p25921159132414"></a><a name="p25921159132414"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.64%" headers="mcps1.2.5.1.4 "><p id="p1759245922417"><a name="p1759245922417"></a><a name="p1759245922417"></a>Specifies the floating IP address list. For details, see <a href="#table547993685510">Table 2</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2** **floatingip**  objects

    <a name="table547993685510"></a>
    <table><thead align="left"><tr id="row966719362553"><th class="cellrowborder" valign="top" width="19.878012198780123%" id="mcps1.2.5.1.1"><p id="p0685313416"><a name="p0685313416"></a><a name="p0685313416"></a><strong id="b1047913918573"><a name="b1047913918573"></a><a name="b1047913918573"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="12.938706129387059%" id="mcps1.2.5.1.2"><p id="p768561134110"><a name="p768561134110"></a><a name="p768561134110"></a><strong id="b16443144095716"><a name="b16443144095716"></a><a name="b16443144095716"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="12.84871512848715%" id="mcps1.2.5.1.3"><p id="p368681134120"><a name="p368681134120"></a><a name="p368681134120"></a><strong id="b199131741105711"><a name="b199131741105711"></a><a name="b199131741105711"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="54.334566543345666%" id="mcps1.2.5.1.4"><p id="p668612124119"><a name="p668612124119"></a><a name="p668612124119"></a><strong id="b1998164325720"><a name="b1998164325720"></a><a name="b1998164325720"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1667163613554"><td class="cellrowborder" valign="top" width="19.878012198780123%" headers="mcps1.2.5.1.1 "><p id="p1868717104113"><a name="p1868717104113"></a><a name="p1868717104113"></a>port_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.938706129387059%" headers="mcps1.2.5.1.2 "><p id="p26871119419"><a name="p26871119419"></a><a name="p26871119419"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.84871512848715%" headers="mcps1.2.5.1.3 "><p id="p66889116414"><a name="p66889116414"></a><a name="p66889116414"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.334566543345666%" headers="mcps1.2.5.1.4 "><p id="p14688213413"><a name="p14688213413"></a><a name="p14688213413"></a>Specifies the port ID. </p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request 1 \(Binding to a port\)

    ```
    PUT https://{Endpoint}/v2.0/eip/floatingips_v6/b639c937-4737-4107-8978-fecc7327a5ae
    
    {
        "floatingip": {
            "port_id": "21b5c483-84e9-40a1-86b3-3041606106f5",
            "fixed_ip_address": "10.0.2.2"
        }
    }
    ```


-   Example request 2 \(Unbinding from a port\)

    ```
    PUT https://{Endpoint}/v2.0/eip/floatingips_v6/3870858f-91dc-489f-92a1-c04dbdc6d781
    
    {
        "floatingip": {
            "port_id": null
        }
    }
    ```


## Response Message<a name="section183951559182418"></a>

-   Response parameter

    **Table  3**  Response parameter

    <a name="table639619595248"></a>
    <table><thead align="left"><tr id="row18592059102412"><th class="cellrowborder" valign="top" width="21.11%" id="mcps1.2.4.1.1"><p id="p759210594240"><a name="p759210594240"></a><a name="p759210594240"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.89%" id="mcps1.2.4.1.2"><p id="p2592125917247"><a name="p2592125917247"></a><a name="p2592125917247"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="60%" id="mcps1.2.4.1.3"><p id="p1592145917246"><a name="p1592145917246"></a><a name="p1592145917246"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4592105910246"><td class="cellrowborder" valign="top" width="21.11%" headers="mcps1.2.4.1.1 "><p id="p1592115992411"><a name="p1592115992411"></a><a name="p1592115992411"></a>floatingip</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.89%" headers="mcps1.2.4.1.2 "><p id="p2059225912243"><a name="p2059225912243"></a><a name="p2059225912243"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p1593125932418"><a name="p1593125932418"></a><a name="p1593125932418"></a>Specifies the floating IP address list. For details, see <a href="#table1935317341267">Table 4</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **floatingip**  objects

    <a name="table1935317341267"></a>
    <table><thead align="left"><tr id="row63486341164"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p9993174855413"><a name="p9993174855413"></a><a name="p9993174855413"></a><strong id="b19349172101010"><a name="b19349172101010"></a><a name="b19349172101010"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.55185518551855%" id="mcps1.2.4.1.2"><p id="p16993194812541"><a name="p16993194812541"></a><a name="p16993194812541"></a><strong id="b02721133104"><a name="b02721133104"></a><a name="b02721133104"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="48.11481148114812%" id="mcps1.2.4.1.3"><p id="p99938485541"><a name="p99938485541"></a><a name="p99938485541"></a><strong id="b112779412107"><a name="b112779412107"></a><a name="b112779412107"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row935017340612"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p109931248105412"><a name="p109931248105412"></a><a name="p109931248105412"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.55185518551855%" headers="mcps1.2.4.1.2 "><p id="p209935484543"><a name="p209935484543"></a><a name="p209935484543"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.11481148114812%" headers="mcps1.2.4.1.3 "><p id="p1099384811549"><a name="p1099384811549"></a><a name="p1099384811549"></a>Specifies the floating IP address status. The value can be <strong id="b1759616711011"><a name="b1759616711011"></a><a name="b1759616711011"></a>ACTIVE</strong>, <strong id="b3597275105"><a name="b3597275105"></a><a name="b3597275105"></a>DOWN</strong>, or <strong id="b759814719103"><a name="b759814719103"></a><a name="b759814719103"></a>ERROR</strong>.</p>
    <a name="ul10994124825413"></a><a name="ul10994124825413"></a><ul id="ul10994124825413"><li><strong id="b196632050181412"><a name="b196632050181412"></a><a name="b196632050181412"></a>ACTIVE</strong> indicates that the floating IP address has been bound.</li><li><strong id="b168791538143"><a name="b168791538143"></a><a name="b168791538143"></a>ERROR</strong> indicates that the floating IP address is abnormal.</li><li><strong id="b17928855161410"><a name="b17928855161410"></a><a name="b17928855161410"></a>DOWN</strong> indicates that the floating IP address has not been bound.</li></ul>
    </td>
    </tr>
    <tr id="row1035123410619"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p6994144818541"><a name="p6994144818541"></a><a name="p6994144818541"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.55185518551855%" headers="mcps1.2.4.1.2 "><p id="p1399416486549"><a name="p1399416486549"></a><a name="p1399416486549"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.11481148114812%" headers="mcps1.2.4.1.3 "><p id="p1899418480541"><a name="p1899418480541"></a><a name="p1899418480541"></a>Specifies the floating IP address ID.</p>
    </td>
    </tr>
    <tr id="row435118341261"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p29942484542"><a name="p29942484542"></a><a name="p29942484542"></a>floating_ip_address</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.55185518551855%" headers="mcps1.2.4.1.2 "><p id="p9994348155412"><a name="p9994348155412"></a><a name="p9994348155412"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.11481148114812%" headers="mcps1.2.4.1.3 "><p id="p8994174818549"><a name="p8994174818549"></a><a name="p8994174818549"></a>Specifies the floating IPv6 address.</p>
    </td>
    </tr>
    <tr id="row73521344612"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p119948483548"><a name="p119948483548"></a><a name="p119948483548"></a>floating_network_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.55185518551855%" headers="mcps1.2.4.1.2 "><p id="p89942482546"><a name="p89942482546"></a><a name="p89942482546"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.11481148114812%" headers="mcps1.2.4.1.3 "><p id="p59942486544"><a name="p59942486544"></a><a name="p59942486544"></a>Specifies the external network ID.</p>
    </td>
    </tr>
    <tr id="row1235211345615"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p99954487543"><a name="p99954487543"></a><a name="p99954487543"></a>router_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.55185518551855%" headers="mcps1.2.4.1.2 "><p id="p1999574817544"><a name="p1999574817544"></a><a name="p1999574817544"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.11481148114812%" headers="mcps1.2.4.1.3 "><p id="p1199594812543"><a name="p1199594812543"></a><a name="p1199594812543"></a>Specifies the ID of the belonged router.</p>
    </td>
    </tr>
    <tr id="row535273416619"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p399515488546"><a name="p399515488546"></a><a name="p399515488546"></a>port_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.55185518551855%" headers="mcps1.2.4.1.2 "><p id="p499534814543"><a name="p499534814543"></a><a name="p499534814543"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.11481148114812%" headers="mcps1.2.4.1.3 "><p id="p16995248135411"><a name="p16995248135411"></a><a name="p16995248135411"></a>Specifies the port ID.</p>
    </td>
    </tr>
    <tr id="row1835217343617"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p2099514875417"><a name="p2099514875417"></a><a name="p2099514875417"></a>fixed_ip_address</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.55185518551855%" headers="mcps1.2.4.1.2 "><p id="p1599514484541"><a name="p1599514484541"></a><a name="p1599514484541"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.11481148114812%" headers="mcps1.2.4.1.3 "><p id="p6995134819542"><a name="p6995134819542"></a><a name="p6995134819542"></a>Specifies the private IP address of the associated port.</p>
    </td>
    </tr>
    <tr id="row15353534660"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p139951748155418"><a name="p139951748155418"></a><a name="p139951748155418"></a>tenant_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.55185518551855%" headers="mcps1.2.4.1.2 "><p id="p209957480545"><a name="p209957480545"></a><a name="p209957480545"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.11481148114812%" headers="mcps1.2.4.1.3 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response 1 \(Binding a specified floating IP address to a port\)

    ```
    {
        "floatingip": {
            "router_id": "76c052d6-6a92-444c-b67d-147ee166a480",
            "status": "ACTIVE",
            "tenant_id": "6fbe9263116a4b68818cf1edce16bc4f",
            "floating_network_id": "0a2228f2-7f8a-45f1-8e09-9039e1d09975",
            "fixed_ip_address": "10.0.2.2",
            "floating_ip_address": "cdcd:910a:2222:5498:8475:1111:c013:8096",
            "port_id": "21b5c483-84e9-40a1-86b3-3041606106f5",
            "id": "b639c937-4737-4107-8978-fecc7327a5ae"
        }
    }
    ```


-   Example response 2 \(Unbinding a specified floating IP address from a port\)

    ```
    {
        "floatingip": {
            "floating_network_id": "809fdbbc-2e3e-426e-897c-cb632b081a72",
            "router_id": null,
            "fixed_ip_address": null,
            "floating_ip_address": "cdcd:910a:2222:5498:8475:1111:c013:8096",
            "tenant_id": "3c8c36e1520147ccbc83d2ccfbb9ab24",
            "status": "ACTIVE",
            "port_id": null,
            "id": "3870858f-91dc-489f-92a1-c04dbdc6d781"
        }
    }
    ```


## Status Code<a name="section31981619"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

