# Querying Details About a VPN Service<a name="en_topic_0093011499"></a>

## **Function**<a name="section28631516"></a>

This interface is used to query details about a VPN service.

## URI<a name="section56357057"></a>

GET /v2.0/vpn/vpnservices/\{service\_id\}

**Table  1**  Parameter description

<a name="table184162115335"></a>
<table><thead align="left"><tr id="row984914219336"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p8849921163313"><a name="p8849921163313"></a><a name="p8849921163313"></a><strong id="b842352706172115"><a name="b842352706172115"></a><a name="b842352706172115"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p384918214339"><a name="p384918214339"></a><a name="p384918214339"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p208493212330"><a name="p208493212330"></a><a name="p208493212330"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p1185732118339"><a name="p1185732118339"></a><a name="p1185732118339"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row10857162110332"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p17857142117336"><a name="p17857142117336"></a><a name="p17857142117336"></a>service_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p18857152173311"><a name="p18857152173311"></a><a name="p18857152173311"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p385772133310"><a name="p385772133310"></a><a name="p385772133310"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p28642214334"><a name="p28642214334"></a><a name="p28642214334"></a>Specifies the VPN service ID.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section1518871"></a>

None

## Response Message<a name="section13669843"></a>

[Table 2](#table6499254)  describes the response parameters.

**Table  2**  Response parameters

<a name="table6499254"></a>
<table><thead align="left"><tr id="row35632194"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p526619"><a name="p526619"></a><a name="p526619"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p42656148"><a name="p42656148"></a><a name="p42656148"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p32595925"><a name="p32595925"></a><a name="p32595925"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p23024263"><a name="p23024263"></a><a name="p23024263"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row53026001"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p138844"><a name="p138844"></a><a name="p138844"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p11246416"><a name="p11246416"></a><a name="p11246416"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p38544467"><a name="p38544467"></a><a name="p38544467"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p35094160"><a name="p35094160"></a><a name="p35094160"></a>Specifies whether the VPN service is currently operational. The value can be <strong id="b842352706212822"><a name="b842352706212822"></a><a name="b842352706212822"></a>ACTIVE</strong>,&nbsp;<strong id="b842352706212827"><a name="b842352706212827"></a><a name="b842352706212827"></a>DOWN</strong>,&nbsp;<strong id="b842352706212832"><a name="b842352706212832"></a><a name="b842352706212832"></a>BUILD</strong>,&nbsp;<strong id="b842352706212835"><a name="b842352706212835"></a><a name="b842352706212835"></a>ERROR</strong>,&nbsp;<strong id="b842352706212840"><a name="b842352706212840"></a><a name="b842352706212840"></a>PENDING_CREATE</strong>,&nbsp;<strong id="b842352706212845"><a name="b842352706212845"></a><a name="b842352706212845"></a>PENDING_UPDATE</strong>, or&nbsp;<strong id="b842352706212850"><a name="b842352706212850"></a><a name="b842352706212850"></a>PENDING_DELETE</strong>.</p>
</td>
</tr>
<tr id="row47411987"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p15165719"><a name="p15165719"></a><a name="p15165719"></a>router_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p20463720"><a name="p20463720"></a><a name="p20463720"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p46948589"><a name="p46948589"></a><a name="p46948589"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p44739342"><a name="p44739342"></a><a name="p44739342"></a>Specifies the router ID.</p>
</td>
</tr>
<tr id="row901"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p73053"><a name="p73053"></a><a name="p73053"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p5917317"><a name="p5917317"></a><a name="p5917317"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p9540645"><a name="p9540645"></a><a name="p9540645"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p34594790"><a name="p34594790"></a><a name="p34594790"></a>Specifies the VPN service name.</p>
</td>
</tr>
<tr id="row42917658"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p53778287"><a name="p53778287"></a><a name="p53778287"></a>external_v6_ip</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p61073976"><a name="p61073976"></a><a name="p61073976"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p48045022"><a name="p48045022"></a><a name="p48045022"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p66441544"><a name="p66441544"></a><a name="p66441544"></a>Specifies the IPv6 address of the VPN service external gateway.</p>
</td>
</tr>
<tr id="row61102986"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p50394838"><a name="p50394838"></a><a name="p50394838"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p55450074"><a name="p55450074"></a><a name="p55450074"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p62271039"><a name="p62271039"></a><a name="p62271039"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p10789421"><a name="p10789421"></a><a name="p10789421"></a>Specifies the administrative status. The value can be <strong id="b842352706221557"><a name="b842352706221557"></a><a name="b842352706221557"></a>true</strong>&nbsp;or&nbsp;<strong id="b84235270622160"><a name="b84235270622160"></a><a name="b84235270622160"></a>false</strong>.</p>
</td>
</tr>
<tr id="row29995926"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p13750947"><a name="p13750947"></a><a name="p13750947"></a>subnet_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p40084941"><a name="p40084941"></a><a name="p40084941"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p25654779"><a name="p25654779"></a><a name="p25654779"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p64771222"><a name="p64771222"></a><a name="p64771222"></a>Specifies the subnet ID.</p>
</td>
</tr>
<tr id="row46070087"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p40689584"><a name="p40689584"></a><a name="p40689584"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p7521977"><a name="p7521977"></a><a name="p7521977"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p5300362"><a name="p5300362"></a><a name="p5300362"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p26676172"><a name="p26676172"></a><a name="p26676172"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row38758958"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p52467932"><a name="p52467932"></a><a name="p52467932"></a>external_v4_ip</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p22044110"><a name="p22044110"></a><a name="p22044110"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p40742509"><a name="p40742509"></a><a name="p40742509"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p11808928"><a name="p11808928"></a><a name="p11808928"></a>Specifies the IPv4 address of the VPN service external gateway.</p>
</td>
</tr>
<tr id="row39171493"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p18774354"><a name="p18774354"></a><a name="p18774354"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p44327687"><a name="p44327687"></a><a name="p44327687"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p33772909"><a name="p33772909"></a><a name="p33772909"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p51251115"><a name="p51251115"></a><a name="p51251115"></a>Specifies the VPN service ID.</p>
</td>
</tr>
<tr id="row58606859"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p49535170"><a name="p49535170"></a><a name="p49535170"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p52925796"><a name="p52925796"></a><a name="p52925796"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p59131099"><a name="p59131099"></a><a name="p59131099"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p24889743"><a name="p24889743"></a><a name="p24889743"></a>Provides supplementary information about the VPN service.</p>
</td>
</tr>
<tr id="row22681099"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p25229732"><a name="p25229732"></a><a name="p25229732"></a>vpnservice</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p30342446"><a name="p30342446"></a><a name="p30342446"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p41819089"><a name="p41819089"></a><a name="p41819089"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p31903028"><a name="p31903028"></a><a name="p31903028"></a>Specifies the VPN service object.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section55919726"></a>

-   Example Request

    ```
    GET /v2.0/vpn/vpnservices/{service_id}
    ```


-   Example Response

    ```
    {
        "vpnservice": {
            "router_id": "66e3b16c-8ce5-40fb-bb49-ab6d8dc3f2aa",
            "status": "PENDING_CREATE",
            "name": "myservice",
            "external_v6_ip": "2001:db8::1",
            "admin_state_up": true,
            "subnet_id": null,
            "project_id": "10039663455a446d8ba2cbb058b0f578",
            "tenant_id": "10039663455a446d8ba2cbb058b0f578",
            "external_v4_ip": "172.32.1.11",
            "id": "5c561d9d-eaea-45f6-ae3e-08d1a7080828",
            "description": "",
        }
    }
    ```


## Returned Values<a name="section6578292"></a>

For details, see section  [Common Returned Values](common-returned-values.md).

