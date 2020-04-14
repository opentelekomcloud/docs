# Querying Floating IP Addresses<a name="vpc_ipv6_0001"></a>

## Function<a name="section14945458192213"></a>

This API is used to query all floating IP addresses accessible to the tenant submitting the request.

## URI<a name="section494655812215"></a>

GET /v2.0/eip/floatingips\_v6

Example:

```
GET https://{Endpoint}/v2.0/eip/floatingips_v6?id={id}&router_id={router_id}&floating_network_id={floating_network_id}&floating_ip_address={floating_ip_address}&port_id={port_id }&fixed_ip_address={fixed_ip_address}&tenant_id={tenant_id}
```

[Table 1](#table668331194113)  describes the parameters.

**Table  1**  Parameter description

<a name="table668331194113"></a>
<table><thead align="left"><tr id="row10685111104111"><th class="cellrowborder" valign="top" width="23.43765623437656%" id="mcps1.2.5.1.1"><p id="p0685313416"><a name="p0685313416"></a><a name="p0685313416"></a><strong id="b91094311293"><a name="b91094311293"></a><a name="b91094311293"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="9.37906209379062%" id="mcps1.2.5.1.2"><p id="p768561134110"><a name="p768561134110"></a><a name="p768561134110"></a><strong id="b5814142784412"><a name="b5814142784412"></a><a name="b5814142784412"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="23.43765623437656%" id="mcps1.2.5.1.3"><p id="p368681134120"><a name="p368681134120"></a><a name="p368681134120"></a><strong id="b994730174413"><a name="b994730174413"></a><a name="b994730174413"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="43.745625437456255%" id="mcps1.2.5.1.4"><p id="p668612124119"><a name="p668612124119"></a><a name="p668612124119"></a><strong id="b1313533174414"><a name="b1313533174414"></a><a name="b1313533174414"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row3686171204116"><td class="cellrowborder" valign="top" width="23.43765623437656%" headers="mcps1.2.5.1.1 "><p id="p176864111411"><a name="p176864111411"></a><a name="p176864111411"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="9.37906209379062%" headers="mcps1.2.5.1.2 "><p id="p136865110419"><a name="p136865110419"></a><a name="p136865110419"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="23.43765623437656%" headers="mcps1.2.5.1.3 "><p id="p16861211413"><a name="p16861211413"></a><a name="p16861211413"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.745625437456255%" headers="mcps1.2.5.1.4 "><p id="p1068611114119"><a name="p1068611114119"></a><a name="p1068611114119"></a>Specifies the floating IP address ID.</p>
</td>
</tr>
<tr id="row19686619418"><td class="cellrowborder" valign="top" width="23.43765623437656%" headers="mcps1.2.5.1.1 "><p id="p868615164111"><a name="p868615164111"></a><a name="p868615164111"></a>floating_ip_address</p>
</td>
<td class="cellrowborder" valign="top" width="9.37906209379062%" headers="mcps1.2.5.1.2 "><p id="p1468611134120"><a name="p1468611134120"></a><a name="p1468611134120"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="23.43765623437656%" headers="mcps1.2.5.1.3 "><p id="p1668716114415"><a name="p1668716114415"></a><a name="p1668716114415"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.745625437456255%" headers="mcps1.2.5.1.4 "><p id="p76878124112"><a name="p76878124112"></a><a name="p76878124112"></a>Specifies the floating IPv6 address.</p>
</td>
</tr>
<tr id="row126871811412"><td class="cellrowborder" valign="top" width="23.43765623437656%" headers="mcps1.2.5.1.1 "><p id="p1668781104117"><a name="p1668781104117"></a><a name="p1668781104117"></a>floating_network_id</p>
</td>
<td class="cellrowborder" valign="top" width="9.37906209379062%" headers="mcps1.2.5.1.2 "><p id="p1668731204116"><a name="p1668731204116"></a><a name="p1668731204116"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="23.43765623437656%" headers="mcps1.2.5.1.3 "><p id="p1687610411"><a name="p1687610411"></a><a name="p1687610411"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.745625437456255%" headers="mcps1.2.5.1.4 "><p id="p14687611411"><a name="p14687611411"></a><a name="p14687611411"></a>Specifies the external network ID.</p>
<p id="p4687818419"><a name="p4687818419"></a><a name="p4687818419"></a>You can only use fixed external network. </p>
<p id="p9687151144115"><a name="p9687151144115"></a><a name="p9687151144115"></a>You can use <strong id="b16947183205511"><a name="b16947183205511"></a><a name="b16947183205511"></a>GET /v2.0/networks?router:external=True</strong> or</p>
<p id="p1568711118416"><a name="p1568711118416"></a><a name="p1568711118416"></a><strong id="b1132415435015"><a name="b1132415435015"></a><a name="b1132415435015"></a>GET /v2.0/networks?name={floating_network}</strong> or run the <strong id="b14326354145013"><a name="b14326354145013"></a><a name="b14326354145013"></a>neutron net-external-list</strong> command to obtain information about the external network. </p>
</td>
</tr>
<tr id="row5687814417"><td class="cellrowborder" valign="top" width="23.43765623437656%" headers="mcps1.2.5.1.1 "><p id="p106871419413"><a name="p106871419413"></a><a name="p106871419413"></a>router_id</p>
</td>
<td class="cellrowborder" valign="top" width="9.37906209379062%" headers="mcps1.2.5.1.2 "><p id="p1268712115416"><a name="p1268712115416"></a><a name="p1268712115416"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="23.43765623437656%" headers="mcps1.2.5.1.3 "><p id="p6687015419"><a name="p6687015419"></a><a name="p6687015419"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.745625437456255%" headers="mcps1.2.5.1.4 "><p id="p668714111415"><a name="p668714111415"></a><a name="p668714111415"></a>Specifies the ID of the belonged router. </p>
</td>
</tr>
<tr id="row116871516414"><td class="cellrowborder" valign="top" width="23.43765623437656%" headers="mcps1.2.5.1.1 "><p id="p1868717104113"><a name="p1868717104113"></a><a name="p1868717104113"></a>port_id</p>
</td>
<td class="cellrowborder" valign="top" width="9.37906209379062%" headers="mcps1.2.5.1.2 "><p id="p26871119419"><a name="p26871119419"></a><a name="p26871119419"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="23.43765623437656%" headers="mcps1.2.5.1.3 "><p id="p66889116414"><a name="p66889116414"></a><a name="p66889116414"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.745625437456255%" headers="mcps1.2.5.1.4 "><p id="p14688213413"><a name="p14688213413"></a><a name="p14688213413"></a>Specifies the port ID. </p>
</td>
</tr>
<tr id="row1168817194115"><td class="cellrowborder" valign="top" width="23.43765623437656%" headers="mcps1.2.5.1.1 "><p id="p868818134116"><a name="p868818134116"></a><a name="p868818134116"></a>fixed_ip_address</p>
</td>
<td class="cellrowborder" valign="top" width="9.37906209379062%" headers="mcps1.2.5.1.2 "><p id="p568817111417"><a name="p568817111417"></a><a name="p568817111417"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="23.43765623437656%" headers="mcps1.2.5.1.3 "><p id="p96881617413"><a name="p96881617413"></a><a name="p96881617413"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.745625437456255%" headers="mcps1.2.5.1.4 "><p id="p1668816118413"><a name="p1668816118413"></a><a name="p1668816118413"></a>Specifies the private IP address of the associated port.</p>
</td>
</tr>
<tr id="row116884115417"><td class="cellrowborder" valign="top" width="23.43765623437656%" headers="mcps1.2.5.1.1 "><p id="p968813113416"><a name="p968813113416"></a><a name="p968813113416"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="9.37906209379062%" headers="mcps1.2.5.1.2 "><p id="p468815111414"><a name="p468815111414"></a><a name="p468815111414"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="23.43765623437656%" headers="mcps1.2.5.1.3 "><p id="p12688141154119"><a name="p12688141154119"></a><a name="p12688141154119"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.745625437456255%" headers="mcps1.2.5.1.4 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section5957155814226"></a>

-   Request parameter

    None

-   Example request

    None


## Response Message<a name="section2957195852214"></a>

-   Response parameter

**Table  2**  Response parameter

<a name="table395825872218"></a>
<table><thead align="left"><tr id="row15122195992213"><th class="cellrowborder" valign="top" width="15.381538153815383%" id="mcps1.2.4.1.1"><p id="p1612211591220"><a name="p1612211591220"></a><a name="p1612211591220"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="23.072307230723073%" id="mcps1.2.4.1.2"><p id="p7122185916226"><a name="p7122185916226"></a><a name="p7122185916226"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="61.546154615461546%" id="mcps1.2.4.1.3"><p id="p512212594226"><a name="p512212594226"></a><a name="p512212594226"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row412225982219"><td class="cellrowborder" valign="top" width="15.381538153815383%" headers="mcps1.2.4.1.1 "><p id="p3122155914223"><a name="p3122155914223"></a><a name="p3122155914223"></a>floatingips</p>
</td>
<td class="cellrowborder" valign="top" width="23.072307230723073%" headers="mcps1.2.4.1.2 "><p id="p1112214593223"><a name="p1112214593223"></a><a name="p1112214593223"></a>Array of <a href="#table129961748135412">floatingip</a> objects</p>
</td>
<td class="cellrowborder" valign="top" width="61.546154615461546%" headers="mcps1.2.4.1.3 "><p id="p10123059152213"><a name="p10123059152213"></a><a name="p10123059152213"></a>Specifies the floating IP address list. For details, see <a href="#table129961748135412">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **floatingip**  objects

<a name="table129961748135412"></a>
<table><thead align="left"><tr id="row5993648185411"><th class="cellrowborder" valign="top" width="24.452445244524455%" id="mcps1.2.4.1.1"><p id="p9993174855413"><a name="p9993174855413"></a><a name="p9993174855413"></a><strong id="b727017471321"><a name="b727017471321"></a><a name="b727017471321"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.931793179317932%" id="mcps1.2.4.1.2"><p id="p16993194812541"><a name="p16993194812541"></a><a name="p16993194812541"></a><strong id="b146834910215"><a name="b146834910215"></a><a name="b146834910215"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="57.615761576157624%" id="mcps1.2.4.1.3"><p id="p99938485541"><a name="p99938485541"></a><a name="p99938485541"></a><strong id="b150314501422"><a name="b150314501422"></a><a name="b150314501422"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row399444818546"><td class="cellrowborder" valign="top" width="24.452445244524455%" headers="mcps1.2.4.1.1 "><p id="p109931248105412"><a name="p109931248105412"></a><a name="p109931248105412"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="17.931793179317932%" headers="mcps1.2.4.1.2 "><p id="p209935484543"><a name="p209935484543"></a><a name="p209935484543"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.615761576157624%" headers="mcps1.2.4.1.3 "><p id="p1099384811549"><a name="p1099384811549"></a><a name="p1099384811549"></a>Specifies the floating IP address status. The value can be <strong id="b81252317598"><a name="b81252317598"></a><a name="b81252317598"></a>ACTIVE</strong>, <strong id="b61280316597"><a name="b61280316597"></a><a name="b61280316597"></a>DOWN</strong>, or <strong id="b31301031175917"><a name="b31301031175917"></a><a name="b31301031175917"></a>ERROR</strong>.</p>
<a name="ul10994124825413"></a><a name="ul10994124825413"></a><ul id="ul10994124825413"><li><strong id="b1416416131052"><a name="b1416416131052"></a><a name="b1416416131052"></a>ACTIVE</strong> indicates that the floating IP address has been bound.</li><li><strong id="b377055614519"><a name="b377055614519"></a><a name="b377055614519"></a>ERROR</strong> indicates that the floating IP address is abnormal.</li><li><strong id="b165241699718"><a name="b165241699718"></a><a name="b165241699718"></a>DOWN</strong> indicates that the floating IP address has not been bound.</li></ul>
</td>
</tr>
<tr id="row209948489541"><td class="cellrowborder" valign="top" width="24.452445244524455%" headers="mcps1.2.4.1.1 "><p id="p6994144818541"><a name="p6994144818541"></a><a name="p6994144818541"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="17.931793179317932%" headers="mcps1.2.4.1.2 "><p id="p1399416486549"><a name="p1399416486549"></a><a name="p1399416486549"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.615761576157624%" headers="mcps1.2.4.1.3 "><p id="p1899418480541"><a name="p1899418480541"></a><a name="p1899418480541"></a>Specifies the floating IP address ID.</p>
</td>
</tr>
<tr id="row99941448115418"><td class="cellrowborder" valign="top" width="24.452445244524455%" headers="mcps1.2.4.1.1 "><p id="p29942484542"><a name="p29942484542"></a><a name="p29942484542"></a>floating_ip_address</p>
</td>
<td class="cellrowborder" valign="top" width="17.931793179317932%" headers="mcps1.2.4.1.2 "><p id="p9994348155412"><a name="p9994348155412"></a><a name="p9994348155412"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.615761576157624%" headers="mcps1.2.4.1.3 "><p id="p8994174818549"><a name="p8994174818549"></a><a name="p8994174818549"></a>Specifies the floating IPv6 address.</p>
</td>
</tr>
<tr id="row1499474865414"><td class="cellrowborder" valign="top" width="24.452445244524455%" headers="mcps1.2.4.1.1 "><p id="p119948483548"><a name="p119948483548"></a><a name="p119948483548"></a>floating_network_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.931793179317932%" headers="mcps1.2.4.1.2 "><p id="p89942482546"><a name="p89942482546"></a><a name="p89942482546"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.615761576157624%" headers="mcps1.2.4.1.3 "><p id="p59942486544"><a name="p59942486544"></a><a name="p59942486544"></a>Specifies the external network ID.</p>
</td>
</tr>
<tr id="row89951548125411"><td class="cellrowborder" valign="top" width="24.452445244524455%" headers="mcps1.2.4.1.1 "><p id="p99954487543"><a name="p99954487543"></a><a name="p99954487543"></a>router_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.931793179317932%" headers="mcps1.2.4.1.2 "><p id="p1999574817544"><a name="p1999574817544"></a><a name="p1999574817544"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.615761576157624%" headers="mcps1.2.4.1.3 "><p id="p1199594812543"><a name="p1199594812543"></a><a name="p1199594812543"></a>Specifies the ID of the belonged router.</p>
</td>
</tr>
<tr id="row1699515482547"><td class="cellrowborder" valign="top" width="24.452445244524455%" headers="mcps1.2.4.1.1 "><p id="p399515488546"><a name="p399515488546"></a><a name="p399515488546"></a>port_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.931793179317932%" headers="mcps1.2.4.1.2 "><p id="p499534814543"><a name="p499534814543"></a><a name="p499534814543"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.615761576157624%" headers="mcps1.2.4.1.3 "><p id="p16995248135411"><a name="p16995248135411"></a><a name="p16995248135411"></a>Specifies the port ID.</p>
</td>
</tr>
<tr id="row15995124813546"><td class="cellrowborder" valign="top" width="24.452445244524455%" headers="mcps1.2.4.1.1 "><p id="p2099514875417"><a name="p2099514875417"></a><a name="p2099514875417"></a>fixed_ip_address</p>
</td>
<td class="cellrowborder" valign="top" width="17.931793179317932%" headers="mcps1.2.4.1.2 "><p id="p1599514484541"><a name="p1599514484541"></a><a name="p1599514484541"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.615761576157624%" headers="mcps1.2.4.1.3 "><p id="p6995134819542"><a name="p6995134819542"></a><a name="p6995134819542"></a>Specifies the private IP address of the associated port.</p>
</td>
</tr>
<tr id="row8996124875412"><td class="cellrowborder" valign="top" width="24.452445244524455%" headers="mcps1.2.4.1.1 "><p id="p139951748155418"><a name="p139951748155418"></a><a name="p139951748155418"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.931793179317932%" headers="mcps1.2.4.1.2 "><p id="p209957480545"><a name="p209957480545"></a><a name="p209957480545"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.615761576157624%" headers="mcps1.2.4.1.3 "><p id="p12687170546"><a name="p12687170546"></a><a name="p12687170546"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row4719141983620"><td class="cellrowborder" valign="top" width="24.452445244524455%" headers="mcps1.2.4.1.1 "><p id="p7719171912368"><a name="p7719171912368"></a><a name="p7719171912368"></a>floatingips_links</p>
</td>
<td class="cellrowborder" valign="top" width="17.931793179317932%" headers="mcps1.2.4.1.2 "><p id="p20720819203612"><a name="p20720819203612"></a><a name="p20720819203612"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="57.615761576157624%" headers="mcps1.2.4.1.3 "><p id="p15720419103617"><a name="p15720419103617"></a><a name="p15720419103617"></a>Specifies the request URL.</p>
</td>
</tr>
</tbody>
</table>

-   Example response

    ```
    {
      "floatingips": [
        {
          "id": "861a4c5b-b17b-4a1d-b653-f3e95dcb3345",
          "status": "DOWN",
          "router_id": null,
          "tenant_id": "26ae5181a416420998eb2093aaed84d9",
          "project_id": "26ae5181a416420998eb2093aaed84d9",
          "floating_network_id": "0a2228f2-7f8a-45f1-8e09-9039e1d09975",
          "fixed_ip_address": null,
          "floating_ip_address": "cdcd:910a:2222:5498:8475:1111:c613:16e3",
          "port_id": null,
          "created_at": "2019-03-26T09:52:41",
          "updated_at": "2019-03-26T09:52:45"
        }
      ],
      "floatingips_links": [
        {
          "href": "https://network.region.cn-southwest-2.hwclouds.com/v2.0/floatingips_v6?marker=861a4c5b-b17b-4a1d-b653-f3e95dcb3345&page_reverse=true&page_reverse=True",
          "rel": "previous"
        }
      ]
    }
    ```


## Status Code<a name="section31981619"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

