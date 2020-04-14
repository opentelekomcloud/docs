# Updating a Floating IP Address<a name="eip_apifloatip_0004"></a>

## Function<a name="en-us_topic_0201534155_section937595992415"></a>

This API is used to update a specific floating IP address and the port associated with the IP address. If  **port\_id**  is left blank, the floating IP address has been unbound from the port.

Restrictions

When you bind a floating IP address, if the floating IP address is in the  **error**  state, try unbinding the address first.

You are not allowed to bind a floating IP address that has been bound to a port to another port. You must first unbind the IP address from its original port and bind it to the required port.

## URI<a name="en-us_topic_0201534155_section1037655913249"></a>

PUT /v2.0/eip/floatingips\_v6/\{floatingip\_id\}

## Request Message<a name="en-us_topic_0201534155_section5385259162414"></a>

-   Request parameter

    **Table  1**  Request parameter

    <a name="en-us_topic_0201534155_table14386115942419"></a>
    <table><thead align="left"><tr id="en-us_topic_0201534155_row1559165992415"><th class="cellrowborder" valign="top" width="19.39%" id="mcps1.2.5.1.1"><p id="en-us_topic_0201534155_p65917591245"><a name="en-us_topic_0201534155_p65917591245"></a><a name="en-us_topic_0201534155_p65917591245"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.659999999999998%" id="mcps1.2.5.1.2"><p id="en-us_topic_0201534155_p559185992415"><a name="en-us_topic_0201534155_p559185992415"></a><a name="en-us_topic_0201534155_p559185992415"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.310000000000002%" id="mcps1.2.5.1.3"><p id="en-us_topic_0201534155_p205911159152411"><a name="en-us_topic_0201534155_p205911159152411"></a><a name="en-us_topic_0201534155_p205911159152411"></a><strong id="en-us_topic_0201534155_b84235270615219"><a name="en-us_topic_0201534155_b84235270615219"></a><a name="en-us_topic_0201534155_b84235270615219"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="46.64%" id="mcps1.2.5.1.4"><p id="en-us_topic_0201534155_p6591115942414"><a name="en-us_topic_0201534155_p6591115942414"></a><a name="en-us_topic_0201534155_p6591115942414"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0201534155_row159211597245"><td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534155_p75923592248"><a name="en-us_topic_0201534155_p75923592248"></a><a name="en-us_topic_0201534155_p75923592248"></a>floatingip</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.659999999999998%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534155_p18592559172418"><a name="en-us_topic_0201534155_p18592559172418"></a><a name="en-us_topic_0201534155_p18592559172418"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.310000000000002%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534155_p25921159132414"><a name="en-us_topic_0201534155_p25921159132414"></a><a name="en-us_topic_0201534155_p25921159132414"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.64%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0201534155_p1759245922417"><a name="en-us_topic_0201534155_p1759245922417"></a><a name="en-us_topic_0201534155_p1759245922417"></a>Specifies the floating IP address list. For details, see <a href="#en-us_topic_0201534155_table547993685510">Table 2</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2** **floatingip**  objects

    <a name="en-us_topic_0201534155_table547993685510"></a>
    <table><thead align="left"><tr id="en-us_topic_0201534155_row966719362553"><th class="cellrowborder" valign="top" width="19.878012198780123%" id="mcps1.2.5.1.1"><p id="en-us_topic_0201534155_p0685313416"><a name="en-us_topic_0201534155_p0685313416"></a><a name="en-us_topic_0201534155_p0685313416"></a><strong id="en-us_topic_0201534155_b1047913918573"><a name="en-us_topic_0201534155_b1047913918573"></a><a name="en-us_topic_0201534155_b1047913918573"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="12.938706129387059%" id="mcps1.2.5.1.2"><p id="en-us_topic_0201534155_p768561134110"><a name="en-us_topic_0201534155_p768561134110"></a><a name="en-us_topic_0201534155_p768561134110"></a><strong id="en-us_topic_0201534155_b16443144095716"><a name="en-us_topic_0201534155_b16443144095716"></a><a name="en-us_topic_0201534155_b16443144095716"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="12.84871512848715%" id="mcps1.2.5.1.3"><p id="en-us_topic_0201534155_p368681134120"><a name="en-us_topic_0201534155_p368681134120"></a><a name="en-us_topic_0201534155_p368681134120"></a><strong id="en-us_topic_0201534155_b199131741105711"><a name="en-us_topic_0201534155_b199131741105711"></a><a name="en-us_topic_0201534155_b199131741105711"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="54.334566543345666%" id="mcps1.2.5.1.4"><p id="en-us_topic_0201534155_p668612124119"><a name="en-us_topic_0201534155_p668612124119"></a><a name="en-us_topic_0201534155_p668612124119"></a><strong id="en-us_topic_0201534155_b1998164325720"><a name="en-us_topic_0201534155_b1998164325720"></a><a name="en-us_topic_0201534155_b1998164325720"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0201534155_row1667163613554"><td class="cellrowborder" valign="top" width="19.878012198780123%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534155_p1868717104113"><a name="en-us_topic_0201534155_p1868717104113"></a><a name="en-us_topic_0201534155_p1868717104113"></a>port_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.938706129387059%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534155_p26871119419"><a name="en-us_topic_0201534155_p26871119419"></a><a name="en-us_topic_0201534155_p26871119419"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.84871512848715%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534155_p66889116414"><a name="en-us_topic_0201534155_p66889116414"></a><a name="en-us_topic_0201534155_p66889116414"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.334566543345666%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0201534155_p14688213413"><a name="en-us_topic_0201534155_p14688213413"></a><a name="en-us_topic_0201534155_p14688213413"></a>Specifies the port ID. </p>
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


## Response Message<a name="en-us_topic_0201534155_section183951559182418"></a>

-   Response parameter

    **Table  3**  Response parameter

    <a name="en-us_topic_0201534155_table639619595248"></a>
    <table><thead align="left"><tr id="en-us_topic_0201534155_row18592059102412"><th class="cellrowborder" valign="top" width="21.11%" id="mcps1.2.4.1.1"><p id="en-us_topic_0201534155_p759210594240"><a name="en-us_topic_0201534155_p759210594240"></a><a name="en-us_topic_0201534155_p759210594240"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.89%" id="mcps1.2.4.1.2"><p id="en-us_topic_0201534155_p2592125917247"><a name="en-us_topic_0201534155_p2592125917247"></a><a name="en-us_topic_0201534155_p2592125917247"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="60%" id="mcps1.2.4.1.3"><p id="en-us_topic_0201534155_p1592145917246"><a name="en-us_topic_0201534155_p1592145917246"></a><a name="en-us_topic_0201534155_p1592145917246"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0201534155_row4592105910246"><td class="cellrowborder" valign="top" width="21.11%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534155_p1592115992411"><a name="en-us_topic_0201534155_p1592115992411"></a><a name="en-us_topic_0201534155_p1592115992411"></a>floatingip</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.89%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534155_p2059225912243"><a name="en-us_topic_0201534155_p2059225912243"></a><a name="en-us_topic_0201534155_p2059225912243"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534155_p1593125932418"><a name="en-us_topic_0201534155_p1593125932418"></a><a name="en-us_topic_0201534155_p1593125932418"></a>Specifies the floating IP address list. For details, see <a href="#en-us_topic_0201534155_table1935317341267">Table 4</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **floatingip**  objects

    <a name="en-us_topic_0201534155_table1935317341267"></a>
    <table><thead align="left"><tr id="en-us_topic_0201534155_row63486341164"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="en-us_topic_0201534155_p9993174855413"><a name="en-us_topic_0201534155_p9993174855413"></a><a name="en-us_topic_0201534155_p9993174855413"></a><strong id="en-us_topic_0201534155_b19349172101010"><a name="en-us_topic_0201534155_b19349172101010"></a><a name="en-us_topic_0201534155_b19349172101010"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.55185518551855%" id="mcps1.2.4.1.2"><p id="en-us_topic_0201534155_p16993194812541"><a name="en-us_topic_0201534155_p16993194812541"></a><a name="en-us_topic_0201534155_p16993194812541"></a><strong id="en-us_topic_0201534155_b02721133104"><a name="en-us_topic_0201534155_b02721133104"></a><a name="en-us_topic_0201534155_b02721133104"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="48.11481148114812%" id="mcps1.2.4.1.3"><p id="en-us_topic_0201534155_p99938485541"><a name="en-us_topic_0201534155_p99938485541"></a><a name="en-us_topic_0201534155_p99938485541"></a><strong id="en-us_topic_0201534155_b112779412107"><a name="en-us_topic_0201534155_b112779412107"></a><a name="en-us_topic_0201534155_b112779412107"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0201534155_row935017340612"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534155_p109931248105412"><a name="en-us_topic_0201534155_p109931248105412"></a><a name="en-us_topic_0201534155_p109931248105412"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.55185518551855%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534155_p209935484543"><a name="en-us_topic_0201534155_p209935484543"></a><a name="en-us_topic_0201534155_p209935484543"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.11481148114812%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534155_p1099384811549"><a name="en-us_topic_0201534155_p1099384811549"></a><a name="en-us_topic_0201534155_p1099384811549"></a>Specifies the floating IP address status. The value can be <strong id="en-us_topic_0201534155_b1759616711011"><a name="en-us_topic_0201534155_b1759616711011"></a><a name="en-us_topic_0201534155_b1759616711011"></a>ACTIVE</strong>, <strong id="en-us_topic_0201534155_b3597275105"><a name="en-us_topic_0201534155_b3597275105"></a><a name="en-us_topic_0201534155_b3597275105"></a>DOWN</strong>, or <strong id="en-us_topic_0201534155_b759814719103"><a name="en-us_topic_0201534155_b759814719103"></a><a name="en-us_topic_0201534155_b759814719103"></a>ERROR</strong>.</p>
    <a name="en-us_topic_0201534155_ul10994124825413"></a><a name="en-us_topic_0201534155_ul10994124825413"></a><ul id="en-us_topic_0201534155_ul10994124825413"><li><strong id="en-us_topic_0201534155_b196632050181412"><a name="en-us_topic_0201534155_b196632050181412"></a><a name="en-us_topic_0201534155_b196632050181412"></a>ACTIVE</strong> indicates that the floating IP address has been bound.</li><li><strong id="en-us_topic_0201534155_b168791538143"><a name="en-us_topic_0201534155_b168791538143"></a><a name="en-us_topic_0201534155_b168791538143"></a>ERROR</strong> indicates that the floating IP address is abnormal.</li><li><strong id="en-us_topic_0201534155_b17928855161410"><a name="en-us_topic_0201534155_b17928855161410"></a><a name="en-us_topic_0201534155_b17928855161410"></a>DOWN</strong> indicates that the floating IP address has not been bound.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0201534155_row1035123410619"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534155_p6994144818541"><a name="en-us_topic_0201534155_p6994144818541"></a><a name="en-us_topic_0201534155_p6994144818541"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.55185518551855%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534155_p1399416486549"><a name="en-us_topic_0201534155_p1399416486549"></a><a name="en-us_topic_0201534155_p1399416486549"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.11481148114812%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534155_p1899418480541"><a name="en-us_topic_0201534155_p1899418480541"></a><a name="en-us_topic_0201534155_p1899418480541"></a>Specifies the floating IP address ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0201534155_row435118341261"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534155_p29942484542"><a name="en-us_topic_0201534155_p29942484542"></a><a name="en-us_topic_0201534155_p29942484542"></a>floating_ip_address</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.55185518551855%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534155_p9994348155412"><a name="en-us_topic_0201534155_p9994348155412"></a><a name="en-us_topic_0201534155_p9994348155412"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.11481148114812%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534155_p8994174818549"><a name="en-us_topic_0201534155_p8994174818549"></a><a name="en-us_topic_0201534155_p8994174818549"></a>Specifies the floating IPv6 address.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0201534155_row73521344612"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534155_p119948483548"><a name="en-us_topic_0201534155_p119948483548"></a><a name="en-us_topic_0201534155_p119948483548"></a>floating_network_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.55185518551855%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534155_p89942482546"><a name="en-us_topic_0201534155_p89942482546"></a><a name="en-us_topic_0201534155_p89942482546"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.11481148114812%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534155_p59942486544"><a name="en-us_topic_0201534155_p59942486544"></a><a name="en-us_topic_0201534155_p59942486544"></a>Specifies the external network ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0201534155_row1235211345615"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534155_p99954487543"><a name="en-us_topic_0201534155_p99954487543"></a><a name="en-us_topic_0201534155_p99954487543"></a>router_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.55185518551855%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534155_p1999574817544"><a name="en-us_topic_0201534155_p1999574817544"></a><a name="en-us_topic_0201534155_p1999574817544"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.11481148114812%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534155_p1199594812543"><a name="en-us_topic_0201534155_p1199594812543"></a><a name="en-us_topic_0201534155_p1199594812543"></a>Specifies the ID of the belonged router.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0201534155_row535273416619"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534155_p399515488546"><a name="en-us_topic_0201534155_p399515488546"></a><a name="en-us_topic_0201534155_p399515488546"></a>port_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.55185518551855%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534155_p499534814543"><a name="en-us_topic_0201534155_p499534814543"></a><a name="en-us_topic_0201534155_p499534814543"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.11481148114812%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534155_p16995248135411"><a name="en-us_topic_0201534155_p16995248135411"></a><a name="en-us_topic_0201534155_p16995248135411"></a>Specifies the port ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0201534155_row1835217343617"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534155_p2099514875417"><a name="en-us_topic_0201534155_p2099514875417"></a><a name="en-us_topic_0201534155_p2099514875417"></a>fixed_ip_address</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.55185518551855%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534155_p1599514484541"><a name="en-us_topic_0201534155_p1599514484541"></a><a name="en-us_topic_0201534155_p1599514484541"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.11481148114812%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534155_p6995134819542"><a name="en-us_topic_0201534155_p6995134819542"></a><a name="en-us_topic_0201534155_p6995134819542"></a>Specifies the private IP address of the associated port.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0201534155_row15353534660"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534155_p139951748155418"><a name="en-us_topic_0201534155_p139951748155418"></a><a name="en-us_topic_0201534155_p139951748155418"></a>tenant_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.55185518551855%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534155_p209957480545"><a name="en-us_topic_0201534155_p209957480545"></a><a name="en-us_topic_0201534155_p209957480545"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.11481148114812%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534155_p10487112"><a name="en-us_topic_0201534155_p10487112"></a><a name="en-us_topic_0201534155_p10487112"></a>Specifies the project ID.</p>
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


## Status Code<a name="en-us_topic_0201534155_section31981619"></a>

See  [Status Codes](status-codes.md#eip_api05_0001).

## Error Code<a name="en-us_topic_0201534155_section85821649202813"></a>

See  [Error Codes](error-codes.md#eip_api05_0002).

