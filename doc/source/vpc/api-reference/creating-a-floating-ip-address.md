# Creating a Floating IP Address<a name="vpc_ipv6_0003"></a>

## Function<a name="section11888132742417"></a>

This API is used to assign a floating IP address and associates it with an internal port.

Restrictions

You can use  **GET /v2.0/networks?router:external=True**  or run the  **neutron net-external-list**  command to obtain the UUID of the external network required for creating a floating IP address. 

The  **port\_id**  parameter value must be the ECS port ID, which can be obtained from the  **NIC ID**  parameter in the ECS NIC details. 

## URI<a name="section18889102752414"></a>

POST /v2.0/eip/floatingips\_v6

## Request Message<a name="section12897127182417"></a>

-   Request parameter

**Table  1**  Request parameter

<a name="table9897182792411"></a>
<table><thead align="left"><tr id="row4901928152411"><th class="cellrowborder" valign="top" width="20.332033203320332%" id="mcps1.2.5.1.1"><p id="p17909286242"><a name="p17909286242"></a><a name="p17909286242"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.341434143414341%" id="mcps1.2.5.1.2"><p id="p990528122415"><a name="p990528122415"></a><a name="p990528122415"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="18.871887188718873%" id="mcps1.2.5.1.3"><p id="p1790172842414"><a name="p1790172842414"></a><a name="p1790172842414"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="46.45464546454646%" id="mcps1.2.5.1.4"><p id="p20908289240"><a name="p20908289240"></a><a name="p20908289240"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row390528202420"><td class="cellrowborder" valign="top" width="20.332033203320332%" headers="mcps1.2.5.1.1 "><p id="p18901928152418"><a name="p18901928152418"></a><a name="p18901928152418"></a>floatingip</p>
</td>
<td class="cellrowborder" valign="top" width="14.341434143414341%" headers="mcps1.2.5.1.2 "><p id="p59052812419"><a name="p59052812419"></a><a name="p59052812419"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="18.871887188718873%" headers="mcps1.2.5.1.3 "><p id="p10901328162413"><a name="p10901328162413"></a><a name="p10901328162413"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="46.45464546454646%" headers="mcps1.2.5.1.4 "><p id="p1290152892416"><a name="p1290152892416"></a><a name="p1290152892416"></a>Specifies the floating IP address list. For details, see <a href="#table1831319135111">Table 2</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  2** **floatingip**  objects

<a name="table1831319135111"></a>
<table><thead align="left"><tr id="row19314513319"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p0685313416"><a name="p0685313416"></a><a name="p0685313416"></a><strong id="b135273324019"><a name="b135273324019"></a><a name="b135273324019"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="11.52%" id="mcps1.2.5.1.2"><p id="p768561134110"><a name="p768561134110"></a><a name="p768561134110"></a><strong id="b4456163419400"><a name="b4456163419400"></a><a name="b4456163419400"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.3"><p id="p368681134120"><a name="p368681134120"></a><a name="p368681134120"></a><strong id="b187798356407"><a name="b187798356407"></a><a name="b187798356407"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="43.480000000000004%" id="mcps1.2.5.1.4"><p id="p668612124119"><a name="p668612124119"></a><a name="p668612124119"></a><strong id="b88879361404"><a name="b88879361404"></a><a name="b88879361404"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row163140131813"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p176864111411"><a name="p176864111411"></a><a name="p176864111411"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="11.52%" headers="mcps1.2.5.1.2 "><p id="p136865110419"><a name="p136865110419"></a><a name="p136865110419"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.3 "><p id="p16861211413"><a name="p16861211413"></a><a name="p16861211413"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.480000000000004%" headers="mcps1.2.5.1.4 "><p id="p1068611114119"><a name="p1068611114119"></a><a name="p1068611114119"></a>Specifies the floating IP address ID.</p>
</td>
</tr>
<tr id="row16314131310111"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p868615164111"><a name="p868615164111"></a><a name="p868615164111"></a>floating_ip_address</p>
</td>
<td class="cellrowborder" valign="top" width="11.52%" headers="mcps1.2.5.1.2 "><p id="p1468611134120"><a name="p1468611134120"></a><a name="p1468611134120"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.3 "><p id="p1668716114415"><a name="p1668716114415"></a><a name="p1668716114415"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.480000000000004%" headers="mcps1.2.5.1.4 "><p id="p76878124112"><a name="p76878124112"></a><a name="p76878124112"></a>Specifies the floating IPv6 address.</p>
</td>
</tr>
<tr id="row2314413713"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1668781104117"><a name="p1668781104117"></a><a name="p1668781104117"></a>floating_network_id</p>
</td>
<td class="cellrowborder" valign="top" width="11.52%" headers="mcps1.2.5.1.2 "><p id="p1668731204116"><a name="p1668731204116"></a><a name="p1668731204116"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.3 "><p id="p1687610411"><a name="p1687610411"></a><a name="p1687610411"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.480000000000004%" headers="mcps1.2.5.1.4 "><p id="p14687611411"><a name="p14687611411"></a><a name="p14687611411"></a>Specifies the external network ID.</p>
<p id="p4687818419"><a name="p4687818419"></a><a name="p4687818419"></a>You can only use fixed external network. </p>
<p id="p9687151144115"><a name="p9687151144115"></a><a name="p9687151144115"></a>You can use <strong id="b859712515444"><a name="b859712515444"></a><a name="b859712515444"></a>GET /v2.0/networks?router:external=True</strong> or</p>
<p id="p1568711118416"><a name="p1568711118416"></a><a name="p1568711118416"></a><strong id="b250712598233"><a name="b250712598233"></a><a name="b250712598233"></a>GET /v2.0/networks?name={floating_network}</strong> or run the <strong id="b4508059182316"><a name="b4508059182316"></a><a name="b4508059182316"></a>neutron net-external-list</strong> command to obtain information about the external network. </p>
</td>
</tr>
<tr id="row11315913213"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p106871419413"><a name="p106871419413"></a><a name="p106871419413"></a>router_id</p>
</td>
<td class="cellrowborder" valign="top" width="11.52%" headers="mcps1.2.5.1.2 "><p id="p1268712115416"><a name="p1268712115416"></a><a name="p1268712115416"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.3 "><p id="p6687015419"><a name="p6687015419"></a><a name="p6687015419"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.480000000000004%" headers="mcps1.2.5.1.4 "><p id="p668714111415"><a name="p668714111415"></a><a name="p668714111415"></a>Specifies the ID of the belonged router. </p>
</td>
</tr>
<tr id="row1331541317114"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1868717104113"><a name="p1868717104113"></a><a name="p1868717104113"></a>port_id</p>
</td>
<td class="cellrowborder" valign="top" width="11.52%" headers="mcps1.2.5.1.2 "><p id="p26871119419"><a name="p26871119419"></a><a name="p26871119419"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.3 "><p id="p66889116414"><a name="p66889116414"></a><a name="p66889116414"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.480000000000004%" headers="mcps1.2.5.1.4 "><p id="p14688213413"><a name="p14688213413"></a><a name="p14688213413"></a>Specifies the port ID. </p>
</td>
</tr>
<tr id="row23153134114"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p868818134116"><a name="p868818134116"></a><a name="p868818134116"></a>fixed_ip_address</p>
</td>
<td class="cellrowborder" valign="top" width="11.52%" headers="mcps1.2.5.1.2 "><p id="p568817111417"><a name="p568817111417"></a><a name="p568817111417"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.3 "><p id="p96881617413"><a name="p96881617413"></a><a name="p96881617413"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.480000000000004%" headers="mcps1.2.5.1.4 "><p id="p1668816118413"><a name="p1668816118413"></a><a name="p1668816118413"></a>Specifies the private IP address of the associated port.</p>
<p id="p26881415412"><a name="p26881415412"></a><a name="p26881415412"></a>This value can only be dynamically assigned by the system.</p>
</td>
</tr>
<tr id="row10316113617"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p968813113416"><a name="p968813113416"></a><a name="p968813113416"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="11.52%" headers="mcps1.2.5.1.2 "><p id="p468815111414"><a name="p468815111414"></a><a name="p468815111414"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.3 "><p id="p12688141154119"><a name="p12688141154119"></a><a name="p12688141154119"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.480000000000004%" headers="mcps1.2.5.1.4 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

-   Example request

```
POST https://{Endpoint}/v2.0/eip/floatingips_v6

{
    "floatingip": {
        "floating_network_id": "5ce655fa-c911-4d2c-99f7-445bc1162ef8",
        "port_id": "552389f5-8f4c-4bb7-9991-07233c315d60"
    }
}
```

## Response Message<a name="section139091627162419"></a>

-   Response parameter

    **Table  3**  Response parameter

    <a name="table191022715241"></a>
    <table><thead align="left"><tr id="row199117287241"><th class="cellrowborder" valign="top" width="21.11%" id="mcps1.2.4.1.1"><p id="p1691162832419"><a name="p1691162832419"></a><a name="p1691162832419"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.89%" id="mcps1.2.4.1.2"><p id="p891928172418"><a name="p891928172418"></a><a name="p891928172418"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="60%" id="mcps1.2.4.1.3"><p id="p129117281246"><a name="p129117281246"></a><a name="p129117281246"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row19118289247"><td class="cellrowborder" valign="top" width="21.11%" headers="mcps1.2.4.1.1 "><p id="p149182852411"><a name="p149182852411"></a><a name="p149182852411"></a>floatingip</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.89%" headers="mcps1.2.4.1.2 "><p id="p16918288244"><a name="p16918288244"></a><a name="p16918288244"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p092102892415"><a name="p092102892415"></a><a name="p092102892415"></a>Specifies the floating IP address list. For details, see <a href="#table71601678316">Table 4</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **floatingip**  objects

    <a name="table71601678316"></a>
    <table><thead align="left"><tr id="row17155271333"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p9993174855413"><a name="p9993174855413"></a><a name="p9993174855413"></a><strong id="b339913394486"><a name="b339913394486"></a><a name="b339913394486"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.39193919391939%" id="mcps1.2.4.1.2"><p id="p16993194812541"><a name="p16993194812541"></a><a name="p16993194812541"></a><strong id="b17558440144816"><a name="b17558440144816"></a><a name="b17558440144816"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="47.27472747274727%" id="mcps1.2.4.1.3"><p id="p99938485541"><a name="p99938485541"></a><a name="p99938485541"></a><strong id="b1959374114815"><a name="b1959374114815"></a><a name="b1959374114815"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1715517135"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p109931248105412"><a name="p109931248105412"></a><a name="p109931248105412"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39193919391939%" headers="mcps1.2.4.1.2 "><p id="p209935484543"><a name="p209935484543"></a><a name="p209935484543"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.27472747274727%" headers="mcps1.2.4.1.3 "><p id="p1099384811549"><a name="p1099384811549"></a><a name="p1099384811549"></a>Specifies the floating IP address status. The value can be <strong id="b613454355810"><a name="b613454355810"></a><a name="b613454355810"></a>ACTIVE</strong>, <strong id="b121361643165817"><a name="b121361643165817"></a><a name="b121361643165817"></a>DOWN</strong>, or <strong id="b9138134310585"><a name="b9138134310585"></a><a name="b9138134310585"></a>ERROR</strong>.</p>
    <a name="ul10994124825413"></a><a name="ul10994124825413"></a><ul id="ul10994124825413"><li><strong id="b116140273491"><a name="b116140273491"></a><a name="b116140273491"></a>ACTIVE</strong> indicates that the floating IP address has been bound.</li><li><strong id="b196830292497"><a name="b196830292497"></a><a name="b196830292497"></a>ERROR</strong> indicates that the floating IP address is abnormal.</li><li><strong id="b18992123054911"><a name="b18992123054911"></a><a name="b18992123054911"></a>DOWN</strong> indicates that the floating IP address has not been bound.</li></ul>
    </td>
    </tr>
    <tr id="row8155177311"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p6994144818541"><a name="p6994144818541"></a><a name="p6994144818541"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39193919391939%" headers="mcps1.2.4.1.2 "><p id="p1399416486549"><a name="p1399416486549"></a><a name="p1399416486549"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.27472747274727%" headers="mcps1.2.4.1.3 "><p id="p1899418480541"><a name="p1899418480541"></a><a name="p1899418480541"></a>Specifies the floating IP address ID.</p>
    </td>
    </tr>
    <tr id="row1415647130"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p29942484542"><a name="p29942484542"></a><a name="p29942484542"></a>floating_ip_address</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39193919391939%" headers="mcps1.2.4.1.2 "><p id="p9994348155412"><a name="p9994348155412"></a><a name="p9994348155412"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.27472747274727%" headers="mcps1.2.4.1.3 "><p id="p8994174818549"><a name="p8994174818549"></a><a name="p8994174818549"></a>Specifies the floating IPv6 address.</p>
    </td>
    </tr>
    <tr id="row1015857132"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p119948483548"><a name="p119948483548"></a><a name="p119948483548"></a>floating_network_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39193919391939%" headers="mcps1.2.4.1.2 "><p id="p89942482546"><a name="p89942482546"></a><a name="p89942482546"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.27472747274727%" headers="mcps1.2.4.1.3 "><p id="p59942486544"><a name="p59942486544"></a><a name="p59942486544"></a>Specifies the external network ID.</p>
    </td>
    </tr>
    <tr id="row11158171133"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p99954487543"><a name="p99954487543"></a><a name="p99954487543"></a>router_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39193919391939%" headers="mcps1.2.4.1.2 "><p id="p1999574817544"><a name="p1999574817544"></a><a name="p1999574817544"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.27472747274727%" headers="mcps1.2.4.1.3 "><p id="p1199594812543"><a name="p1199594812543"></a><a name="p1199594812543"></a>Specifies the ID of the belonged router.</p>
    </td>
    </tr>
    <tr id="row12158071318"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p399515488546"><a name="p399515488546"></a><a name="p399515488546"></a>port_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39193919391939%" headers="mcps1.2.4.1.2 "><p id="p499534814543"><a name="p499534814543"></a><a name="p499534814543"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.27472747274727%" headers="mcps1.2.4.1.3 "><p id="p16995248135411"><a name="p16995248135411"></a><a name="p16995248135411"></a>Specifies the port ID.</p>
    </td>
    </tr>
    <tr id="row7160207935"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p2099514875417"><a name="p2099514875417"></a><a name="p2099514875417"></a>fixed_ip_address</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39193919391939%" headers="mcps1.2.4.1.2 "><p id="p1599514484541"><a name="p1599514484541"></a><a name="p1599514484541"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.27472747274727%" headers="mcps1.2.4.1.3 "><p id="p6995134819542"><a name="p6995134819542"></a><a name="p6995134819542"></a>Specifies the private IP address of the associated port.</p>
    </td>
    </tr>
    <tr id="row141601171432"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p139951748155418"><a name="p139951748155418"></a><a name="p139951748155418"></a>tenant_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39193919391939%" headers="mcps1.2.4.1.2 "><p id="p209957480545"><a name="p209957480545"></a><a name="p209957480545"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.27472747274727%" headers="mcps1.2.4.1.3 "><p id="p13201132212420"><a name="p13201132212420"></a><a name="p13201132212420"></a>Specifies the project ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "floatingip": {
            "router_id": "76c052d6-6a92-444c-b67d-147ee166a480",
            "status": "DOWN",
            "tenant_id": "6fd9b5fdb997425f97bc5ba1f0846084",
            "floating_network_id": "5ce655fa-c911-4d2c-99f7-445bc1162ef8",
            "fixed_ip_address": "12.xx.xx.5",
            "floating_ip_address": "cdcd:910a:2222:5498:8475:1111:c013:8096",
            "port_id": "552389f5-8f4c-4bb7-9991-07233c315d60",
            "id": "2567f393-5c76-42db-a397-477723ce41f7"
        }
    }
    ```


## Status Code<a name="section31981619"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

