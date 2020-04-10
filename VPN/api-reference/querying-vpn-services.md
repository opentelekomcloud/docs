# Querying VPN Services<a name="en_topic_0093011500"></a>

## **Function**<a name="section43036322"></a>

This interface is used to query VPN services.

## URI<a name="ole_link150"></a>

GET /v2.0/vpn/vpnservices

## Request Message<a name="section33639718"></a>

[Table 1](#table57678784)  describes the request parameters.

**Table  1**  Request parameters

<a name="table57678784"></a>
<table><thead align="left"><tr id="row24197721"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p13858403"><a name="p13858403"></a><a name="p13858403"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p48788849"><a name="p48788849"></a><a name="p48788849"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p59582700"><a name="p59582700"></a><a name="p59582700"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p61469371"><a name="p61469371"></a><a name="p61469371"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row12963143"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p43381623"><a name="p43381623"></a><a name="p43381623"></a>fields</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p24250547"><a name="p24250547"></a><a name="p24250547"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p18137316"><a name="p18137316"></a><a name="p18137316"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p59836530"><a name="p59836530"></a><a name="p59836530"></a>Controls which parameters are returned. If this parameter is not specified, all parameters will be returned.</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>The  **project\_id**  parameter is not supported.  

## Response Message<a name="section34322009"></a>

[Table 2](#table14920772)  describes the response parameters.

**Table  2**  Response parameters

<a name="table14920772"></a>
<table><thead align="left"><tr id="row14434584"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p28350637"><a name="p28350637"></a><a name="p28350637"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p14700275"><a name="p14700275"></a><a name="p14700275"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p49871633"><a name="p49871633"></a><a name="p49871633"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p13070512"><a name="p13070512"></a><a name="p13070512"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row52078584"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p57615760"><a name="p57615760"></a><a name="p57615760"></a>vpnservices</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p36364960"><a name="p36364960"></a><a name="p36364960"></a>List&lt;Object&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p59880657"><a name="p59880657"></a><a name="p59880657"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p18495050"><a name="p18495050"></a><a name="p18495050"></a>Specifies the VPN service object.</p>
</td>
</tr>
<tr id="row32237730"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p61119323"><a name="p61119323"></a><a name="p61119323"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p51718129"><a name="p51718129"></a><a name="p51718129"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p28418891"><a name="p28418891"></a><a name="p28418891"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p20228817"><a name="p20228817"></a><a name="p20228817"></a>Specifies whether the VPN service is currently operational. The value can be <strong id="b842352706212822"><a name="b842352706212822"></a><a name="b842352706212822"></a>ACTIVE</strong>,&nbsp;<strong id="b842352706212827"><a name="b842352706212827"></a><a name="b842352706212827"></a>DOWN</strong>,&nbsp;<strong id="b842352706212832"><a name="b842352706212832"></a><a name="b842352706212832"></a>BUILD</strong>,&nbsp;<strong id="b842352706212835"><a name="b842352706212835"></a><a name="b842352706212835"></a>ERROR</strong>,&nbsp;<strong id="b842352706212840"><a name="b842352706212840"></a><a name="b842352706212840"></a>PENDING_CREATE</strong>,&nbsp;<strong id="b842352706212845"><a name="b842352706212845"></a><a name="b842352706212845"></a>PENDING_UPDATE</strong>, or&nbsp;<strong id="b842352706212850"><a name="b842352706212850"></a><a name="b842352706212850"></a>PENDING_DELETE</strong>.</p>
</td>
</tr>
<tr id="row47841633"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p49967061"><a name="p49967061"></a><a name="p49967061"></a>router_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p20800170"><a name="p20800170"></a><a name="p20800170"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p7092232"><a name="p7092232"></a><a name="p7092232"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p37599894"><a name="p37599894"></a><a name="p37599894"></a>Specifies the router ID.</p>
</td>
</tr>
<tr id="row2854726"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p29906272"><a name="p29906272"></a><a name="p29906272"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p6488958"><a name="p6488958"></a><a name="p6488958"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p55843593"><a name="p55843593"></a><a name="p55843593"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p27037160"><a name="p27037160"></a><a name="p27037160"></a>Specifies the VPN service name.</p>
</td>
</tr>
<tr id="row42007851"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p47192740"><a name="p47192740"></a><a name="p47192740"></a>external_v6_ip</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p64515557"><a name="p64515557"></a><a name="p64515557"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p58377623"><a name="p58377623"></a><a name="p58377623"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p30967009"><a name="p30967009"></a><a name="p30967009"></a>Specifies the IPv6 address of the VPN service external gateway.</p>
</td>
</tr>
<tr id="row10267631"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p26371793"><a name="p26371793"></a><a name="p26371793"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p55740512"><a name="p55740512"></a><a name="p55740512"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p18687619"><a name="p18687619"></a><a name="p18687619"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p37302179"><a name="p37302179"></a><a name="p37302179"></a>Specifies the administrative status. The value can be <strong id="b842352706221557"><a name="b842352706221557"></a><a name="b842352706221557"></a>true</strong>&nbsp;or&nbsp;<strong id="b84235270622160"><a name="b84235270622160"></a><a name="b84235270622160"></a>false</strong>.</p>
</td>
</tr>
<tr id="row175293"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p14198754"><a name="p14198754"></a><a name="p14198754"></a>subnet_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p9248440"><a name="p9248440"></a><a name="p9248440"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p10926182"><a name="p10926182"></a><a name="p10926182"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p12605589"><a name="p12605589"></a><a name="p12605589"></a>Specifies the subnet ID.</p>
</td>
</tr>
<tr id="row46341445"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p62669527"><a name="p62669527"></a><a name="p62669527"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p43066942"><a name="p43066942"></a><a name="p43066942"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p65870306"><a name="p65870306"></a><a name="p65870306"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p33894570"><a name="p33894570"></a><a name="p33894570"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row36615679"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p13080057"><a name="p13080057"></a><a name="p13080057"></a>external_v4_ip</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p52851724"><a name="p52851724"></a><a name="p52851724"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p53131231"><a name="p53131231"></a><a name="p53131231"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p8662426"><a name="p8662426"></a><a name="p8662426"></a>Specifies the IPv4 address of the VPN service external gateway.</p>
</td>
</tr>
<tr id="row10852974"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p6675738"><a name="p6675738"></a><a name="p6675738"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p3863873"><a name="p3863873"></a><a name="p3863873"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p44538317"><a name="p44538317"></a><a name="p44538317"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p50833958"><a name="p50833958"></a><a name="p50833958"></a>Specifies the VPN service ID.</p>
</td>
</tr>
<tr id="row54852443"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p13862865"><a name="p13862865"></a><a name="p13862865"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p49150280"><a name="p49150280"></a><a name="p49150280"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p21749735"><a name="p21749735"></a><a name="p21749735"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p16898135"><a name="p16898135"></a><a name="p16898135"></a>Provides supplementary information about the VPN service.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section40462633"></a>

-   Request Example

```
GET /v2.0/vpn/vpnservices
```

-   Example Response

    ```
    {
        "vpnservices": [
            {
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
        ]
    }
    ```


## Returned Values<a name="section6578292"></a>

For details, see section  [Common Returned Values](common-returned-values.md).

