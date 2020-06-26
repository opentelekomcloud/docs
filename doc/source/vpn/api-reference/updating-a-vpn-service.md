# Updating a VPN Service<a name="en_topic_0093011501"></a>

## **Function**<a name="section25709437"></a>

This interface is used to update a VPN service.

## URI<a name="section30058349"></a>

PUT /v2.0/vpn/vpnservices/\{service\_id\}

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

## Request Message<a name="section18807190"></a>

[Table 2](#table24429894)  describes the request parameters.

**Table  2**  Request parameters

<a name="table24429894"></a>
<table><thead align="left"><tr id="row26383427"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p56682808"><a name="p56682808"></a><a name="p56682808"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p27904713"><a name="p27904713"></a><a name="p27904713"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p45689312"><a name="p45689312"></a><a name="p45689312"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p9846754"><a name="p9846754"></a><a name="p9846754"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row9359903"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p19954658"><a name="p19954658"></a><a name="p19954658"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p5714573"><a name="p5714573"></a><a name="p5714573"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p60227273"><a name="p60227273"></a><a name="p60227273"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p46570941"><a name="p46570941"></a><a name="p46570941"></a>Provides supplementary information about the VPN service.</p>
</td>
</tr>
<tr id="row16485292"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p60240296"><a name="p60240296"></a><a name="p60240296"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p47625841"><a name="p47625841"></a><a name="p47625841"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p32487918"><a name="p32487918"></a><a name="p32487918"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p14275720"><a name="p14275720"></a><a name="p14275720"></a>Specifies the VPN service name.</p>
</td>
</tr>
<tr id="row61372619"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p5126234"><a name="p5126234"></a><a name="p5126234"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p12571834"><a name="p12571834"></a><a name="p12571834"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p11685651"><a name="p11685651"></a><a name="p11685651"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p7013644"><a name="p7013644"></a><a name="p7013644"></a>Specifies the administrative status. The value can be <strong id="b842352706221557"><a name="b842352706221557"></a><a name="b842352706221557"></a>true</strong>&nbsp;or&nbsp;<strong id="b84235270622160"><a name="b84235270622160"></a><a name="b84235270622160"></a>false</strong>.</p>
</td>
</tr>
<tr id="row62741064"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p48861387"><a name="p48861387"></a><a name="p48861387"></a>vpnservice</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p65458312"><a name="p65458312"></a><a name="p65458312"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p523045"><a name="p523045"></a><a name="p523045"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p42366666"><a name="p42366666"></a><a name="p42366666"></a>Specifies the VPN service object.</p>
</td>
</tr>
</tbody>
</table>

>![](/images/icon-note.gif) **NOTE:**   
>1.  The  **project\_id**  parameter is not supported.  
>2.  The value of  **name**  can contain 1 to 64 characters.  
>3.  The value of  **description**  can contain a maximum of 255 characters.  
>4.  The value of  **admin\_state\_up** can only be **true**.  
>5.  The  **subnet\_id**  parameter is unconfigurable.  

## Response Message<a name="section35046986"></a>

[Table 3](#table9147936)  describes the response parameters.

**Table  3**  Response parameters

<a name="table9147936"></a>
<table><thead align="left"><tr id="row55945983"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p35330790"><a name="p35330790"></a><a name="p35330790"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p43221770"><a name="p43221770"></a><a name="p43221770"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p11302482"><a name="p11302482"></a><a name="p11302482"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p43085863"><a name="p43085863"></a><a name="p43085863"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row294000"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p23814038"><a name="p23814038"></a><a name="p23814038"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p49888896"><a name="p49888896"></a><a name="p49888896"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p14468758"><a name="p14468758"></a><a name="p14468758"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p31118786"><a name="p31118786"></a><a name="p31118786"></a>Specifies the VPN service ID.</p>
</td>
</tr>
<tr id="row11633618"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p2799031"><a name="p2799031"></a><a name="p2799031"></a>router_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p25394981"><a name="p25394981"></a><a name="p25394981"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p43727555"><a name="p43727555"></a><a name="p43727555"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p52271033"><a name="p52271033"></a><a name="p52271033"></a>Specifies the router ID.</p>
</td>
</tr>
<tr id="row677253"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p54857523"><a name="p54857523"></a><a name="p54857523"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p14274382"><a name="p14274382"></a><a name="p14274382"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p15374269"><a name="p15374269"></a><a name="p15374269"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p37356265"><a name="p37356265"></a><a name="p37356265"></a>Specifies the VPN service status. The value can be <strong id="b842352706212822"><a name="b842352706212822"></a><a name="b842352706212822"></a>ACTIVE</strong>,&nbsp;<strong id="b842352706212827"><a name="b842352706212827"></a><a name="b842352706212827"></a>DOWN</strong>,&nbsp;<strong id="b842352706212832"><a name="b842352706212832"></a><a name="b842352706212832"></a>BUILD</strong>,&nbsp;<strong id="b842352706212835"><a name="b842352706212835"></a><a name="b842352706212835"></a>ERROR</strong>,&nbsp;<strong id="b842352706212840"><a name="b842352706212840"></a><a name="b842352706212840"></a>PENDING_UPDATE</strong>, or&nbsp;<strong id="b842352706212850"><a name="b842352706212850"></a><a name="b842352706212850"></a>PENDING_DELETE</strong>.</p>
</td>
</tr>
<tr id="row662065"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p53627266"><a name="p53627266"></a><a name="p53627266"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p48841284"><a name="p48841284"></a><a name="p48841284"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p63829918"><a name="p63829918"></a><a name="p63829918"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p2840889"><a name="p2840889"></a><a name="p2840889"></a>Specifies the VPN service name.</p>
</td>
</tr>
<tr id="row25568006"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p57742629"><a name="p57742629"></a><a name="p57742629"></a>external_v6_ip</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p46641368"><a name="p46641368"></a><a name="p46641368"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p19854472"><a name="p19854472"></a><a name="p19854472"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p64708380"><a name="p64708380"></a><a name="p64708380"></a>Specifies the IPv6 address of the VPN service external gateway.</p>
</td>
</tr>
<tr id="row45504511"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p61986789"><a name="p61986789"></a><a name="p61986789"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p54874019"><a name="p54874019"></a><a name="p54874019"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p15610594"><a name="p15610594"></a><a name="p15610594"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p56498634"><a name="p56498634"></a><a name="p56498634"></a>Specifies the administrative status. The value can be <strong id="b842352706221557_2"><a name="b842352706221557_2"></a><a name="b842352706221557_2"></a>true</strong>&nbsp;or&nbsp;<strong id="b84235270622160_2"><a name="b84235270622160_2"></a><a name="b84235270622160_2"></a>false</strong>.</p>
</td>
</tr>
<tr id="row38725660"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p49770771"><a name="p49770771"></a><a name="p49770771"></a>subnet_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p4900679"><a name="p4900679"></a><a name="p4900679"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p61410719"><a name="p61410719"></a><a name="p61410719"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p8212356"><a name="p8212356"></a><a name="p8212356"></a>Specifies the subnet ID.</p>
</td>
</tr>
<tr id="row6802342"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p14118857"><a name="p14118857"></a><a name="p14118857"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p2776748"><a name="p2776748"></a><a name="p2776748"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p23590007"><a name="p23590007"></a><a name="p23590007"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p31742419"><a name="p31742419"></a><a name="p31742419"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row17246319"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p54774566"><a name="p54774566"></a><a name="p54774566"></a>external_v4_ip</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p7554882"><a name="p7554882"></a><a name="p7554882"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p7965739"><a name="p7965739"></a><a name="p7965739"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p41245128"><a name="p41245128"></a><a name="p41245128"></a>Specifies the IPv4 address of the VPN service external gateway.</p>
</td>
</tr>
<tr id="row35661838"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p2927765"><a name="p2927765"></a><a name="p2927765"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p35822404"><a name="p35822404"></a><a name="p35822404"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p15933636"><a name="p15933636"></a><a name="p15933636"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p15556157"><a name="p15556157"></a><a name="p15556157"></a>Provides supplementary information about the VPN service.</p>
</td>
</tr>
<tr id="row5787686"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p66149382"><a name="p66149382"></a><a name="p66149382"></a>vpnservice</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p56499698"><a name="p56499698"></a><a name="p56499698"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p13072851"><a name="p13072851"></a><a name="p13072851"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p52268049"><a name="p52268049"></a><a name="p52268049"></a>Specifies the VPN service object.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section46987420"></a>

-   Example Request

    ```
    PUT /v2.0/vpn/vpnservices/{service_id}
    {
      "vpnservice" : {
        "description" : "Updated description"
      }
    }
    ```


-   Example Response

    ```
    {
        "vpnservice": {
            "router_id": "881b7b30-4efb-407e-a162-5630a7af3595",
            "status": "ACTIVE",
            "name": "myvpn",
            "admin_state_up": true,
            "subnet_id": null,
            "project_id": "26de9cd6cae94c8cb9f79d660d628e1f",
            "tenant_id": "26de9cd6cae94c8cb9f79d660d628e1f",
            "id": "41bfef97-af4e-4f6b-a5d3-4678859d2485",
            "description": "Updated description",
        }
    }
    ```


## Returned Values<a name="section6578292"></a>

For details, see section  [Common Returned Values](common-returned-values.md).

