# Querying a Firewall Group<a name="vpc_firewall_0014"></a>

## Function<a name="section39340300132713"></a>

This API is used to query details about a specific firewall group.

## URI<a name="section36516119132713"></a>

GET /v2.0/fwaas/firewall\_groups/\{firewall\_group\_id\}

[Table 1](#table18880184689)  describes the parameters.

**Table  1**  Parameter description

<a name="table18880184689"></a>
<table><thead align="left"><tr id="row13968641385"><th class="cellrowborder" valign="top" width="22.222222222222225%" id="mcps1.2.5.1.1"><p id="p209684410817"><a name="p209684410817"></a><a name="p209684410817"></a><strong id="b842352706195711"><a name="b842352706195711"></a><a name="b842352706195711"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.14141414141414%" id="mcps1.2.5.1.2"><p id="p69681441386"><a name="p69681441386"></a><a name="p69681441386"></a><strong id="b84235270615219"><a name="b84235270615219"></a><a name="b84235270615219"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.27272727272727%" id="mcps1.2.5.1.3"><p id="p1096813412811"><a name="p1096813412811"></a><a name="p1096813412811"></a><strong id="b842352706145623"><a name="b842352706145623"></a><a name="b842352706145623"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="36.36363636363636%" id="mcps1.2.5.1.4"><p id="p139686416813"><a name="p139686416813"></a><a name="p139686416813"></a><strong id="b8423527061645"><a name="b8423527061645"></a><a name="b8423527061645"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row19681041189"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p1682422682817"><a name="p1682422682817"></a><a name="p1682422682817"></a>firewall_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.2 "><p id="p1797015416817"><a name="p1797015416817"></a><a name="p1797015416817"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.5.1.3 "><p id="p19701411813"><a name="p19701411813"></a><a name="p19701411813"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.5.1.4 "><p id="p109701641488"><a name="p109701641488"></a><a name="p109701641488"></a>Specifies the firewall group ID, which uniquely identifies the firewall group. The <strong id="b14161131618224"><a name="b14161131618224"></a><a name="b14161131618224"></a>fire_group_id</strong> value is used as the filter.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section17948186132713"></a>

None

## Response Message<a name="section7113297132713"></a>

**Table  2**  Response parameter

<a name="table31400393132713"></a>
<table><thead align="left"><tr id="row29671115132713"><th class="cellrowborder" valign="top" width="21.349999999999998%" id="mcps1.2.4.1.1"><p id="p40935942132713"><a name="p40935942132713"></a><a name="p40935942132713"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.11%" id="mcps1.2.4.1.2"><p id="p111081132713"><a name="p111081132713"></a><a name="p111081132713"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="59.540000000000006%" id="mcps1.2.4.1.3"><p id="p59152418132713"><a name="p59152418132713"></a><a name="p59152418132713"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row6968505132713"><td class="cellrowborder" valign="top" width="21.349999999999998%" headers="mcps1.2.4.1.1 "><p id="p61606520132713"><a name="p61606520132713"></a><a name="p61606520132713"></a>firewall_group</p>
</td>
<td class="cellrowborder" valign="top" width="19.11%" headers="mcps1.2.4.1.2 "><p id="p13430132393915"><a name="p13430132393915"></a><a name="p13430132393915"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="59.540000000000006%" headers="mcps1.2.4.1.3 "><p id="p14666204132713"><a name="p14666204132713"></a><a name="p14666204132713"></a>Specifies the firewall group list. For details, see <a href="#table31629250121127">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **Firewall Group**  objects

<a name="table31629250121127"></a>
<table><thead align="left"><tr id="row45711693121127"><th class="cellrowborder" valign="top" width="35.3%" id="mcps1.2.4.1.1"><p id="p46819705121127"><a name="p46819705121127"></a><a name="p46819705121127"></a><strong id="b054783493914"><a name="b054783493914"></a><a name="b054783493914"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="21.57%" id="mcps1.2.4.1.2"><p id="p35064605121127"><a name="p35064605121127"></a><a name="p35064605121127"></a><strong id="b0248163517394"><a name="b0248163517394"></a><a name="b0248163517394"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="43.13%" id="mcps1.2.4.1.3"><p id="p11952850121127"><a name="p11952850121127"></a><a name="p11952850121127"></a><strong id="b1590273553919"><a name="b1590273553919"></a><a name="b1590273553919"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row20395689121127"><td class="cellrowborder" valign="top" width="35.3%" headers="mcps1.2.4.1.1 "><p id="p50168503121127"><a name="p50168503121127"></a><a name="p50168503121127"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="21.57%" headers="mcps1.2.4.1.2 "><p id="p47513116121127"><a name="p47513116121127"></a><a name="p47513116121127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.13%" headers="mcps1.2.4.1.3 "><p id="p62072725121127"><a name="p62072725121127"></a><a name="p62072725121127"></a>Specifies the UUID of the firewall group. </p>
</td>
</tr>
<tr id="row34896104121127"><td class="cellrowborder" valign="top" width="35.3%" headers="mcps1.2.4.1.1 "><p id="p52608071121127"><a name="p52608071121127"></a><a name="p52608071121127"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="21.57%" headers="mcps1.2.4.1.2 "><p id="p59846605121127"><a name="p59846605121127"></a><a name="p59846605121127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.13%" headers="mcps1.2.4.1.3 "><p id="p28604909121127"><a name="p28604909121127"></a><a name="p28604909121127"></a>Specifies the name of the firewall group.</p>
</td>
</tr>
<tr id="row11129246121127"><td class="cellrowborder" valign="top" width="35.3%" headers="mcps1.2.4.1.1 "><p id="p39887063121127"><a name="p39887063121127"></a><a name="p39887063121127"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="21.57%" headers="mcps1.2.4.1.2 "><p id="p28745735121127"><a name="p28745735121127"></a><a name="p28745735121127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.13%" headers="mcps1.2.4.1.3 "><p id="p35639020121127"><a name="p35639020121127"></a><a name="p35639020121127"></a>Provides supplementary information about the firewall group.</p>
</td>
</tr>
<tr id="row677472121127"><td class="cellrowborder" valign="top" width="35.3%" headers="mcps1.2.4.1.1 "><p id="p60717947121127"><a name="p60717947121127"></a><a name="p60717947121127"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="21.57%" headers="mcps1.2.4.1.2 "><p id="p65871708121127"><a name="p65871708121127"></a><a name="p65871708121127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.13%" headers="mcps1.2.4.1.3 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row38137474121127"><td class="cellrowborder" valign="top" width="35.3%" headers="mcps1.2.4.1.1 "><p id="p35500294121127"><a name="p35500294121127"></a><a name="p35500294121127"></a>ingress_firewall_policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="21.57%" headers="mcps1.2.4.1.2 "><p id="p49995809121127"><a name="p49995809121127"></a><a name="p49995809121127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.13%" headers="mcps1.2.4.1.3 "><p id="p56499442121127"><a name="p56499442121127"></a><a name="p56499442121127"></a>Specifies the firewall policy for inbound traffic.</p>
</td>
</tr>
<tr id="row9094936121127"><td class="cellrowborder" valign="top" width="35.3%" headers="mcps1.2.4.1.1 "><p id="p34911245121127"><a name="p34911245121127"></a><a name="p34911245121127"></a>egress_firewall_policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="21.57%" headers="mcps1.2.4.1.2 "><p id="p44624490121127"><a name="p44624490121127"></a><a name="p44624490121127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.13%" headers="mcps1.2.4.1.3 "><p id="p37100641121127"><a name="p37100641121127"></a><a name="p37100641121127"></a>Specifies the firewall policy for outbound traffic.</p>
</td>
</tr>
<tr id="row31622902121127"><td class="cellrowborder" valign="top" width="35.3%" headers="mcps1.2.4.1.1 "><p id="p65911012121127"><a name="p65911012121127"></a><a name="p65911012121127"></a>ports</p>
</td>
<td class="cellrowborder" valign="top" width="21.57%" headers="mcps1.2.4.1.2 "><p id="p15651147173911"><a name="p15651147173911"></a><a name="p15651147173911"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="43.13%" headers="mcps1.2.4.1.3 "><p id="p61002567121127"><a name="p61002567121127"></a><a name="p61002567121127"></a>Specifies the list of ports bound with the firewall group.</p>
</td>
</tr>
<tr id="row48186031121127"><td class="cellrowborder" valign="top" width="35.3%" headers="mcps1.2.4.1.1 "><p id="p33368479121127"><a name="p33368479121127"></a><a name="p33368479121127"></a>public</p>
</td>
<td class="cellrowborder" valign="top" width="21.57%" headers="mcps1.2.4.1.2 "><p id="p7938198121127"><a name="p7938198121127"></a><a name="p7938198121127"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="43.13%" headers="mcps1.2.4.1.3 "><p id="p56166201121127"><a name="p56166201121127"></a><a name="p56166201121127"></a>Specifies whether the firewall policy can be shared by different tenants.</p>
</td>
</tr>
<tr id="row60912436121127"><td class="cellrowborder" valign="top" width="35.3%" headers="mcps1.2.4.1.1 "><p id="p66273781121127"><a name="p66273781121127"></a><a name="p66273781121127"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="21.57%" headers="mcps1.2.4.1.2 "><p id="p7141533121127"><a name="p7141533121127"></a><a name="p7141533121127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.13%" headers="mcps1.2.4.1.3 "><p id="p6468335121127"><a name="p6468335121127"></a><a name="p6468335121127"></a>Specifies the status of the firewall policy.</p>
</td>
</tr>
<tr id="row59833296121127"><td class="cellrowborder" valign="top" width="35.3%" headers="mcps1.2.4.1.1 "><p id="p44051842121127"><a name="p44051842121127"></a><a name="p44051842121127"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="21.57%" headers="mcps1.2.4.1.2 "><p id="p58587899121127"><a name="p58587899121127"></a><a name="p58587899121127"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="43.13%" headers="mcps1.2.4.1.3 "><p id="p3428646121127"><a name="p3428646121127"></a><a name="p3428646121127"></a>Specifies whether the firewall is controlled by the administrator.</p>
</td>
</tr>
<tr id="row7228115213486"><td class="cellrowborder" valign="top" width="35.3%" headers="mcps1.2.4.1.1 "><p id="p53071912134918"><a name="p53071912134918"></a><a name="p53071912134918"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="21.57%" headers="mcps1.2.4.1.2 "><p id="p1731011220498"><a name="p1731011220498"></a><a name="p1731011220498"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.13%" headers="mcps1.2.4.1.3 "><p id="p66091240132915"><a name="p66091240132915"></a><a name="p66091240132915"></a>Specifies the project ID. </p>
</td>
</tr>
</tbody>
</table>

## Example:<a name="section46668427132713"></a>

Example request

```
GET https://{Endpoint}/v2.0/fwaas/firewall_groups/a504a4cf-9300-40e0-b2d4-649bd157c55a
```

Example response

```
{
    "firewall_group": {
        "status": "ACTIVE", 
        "public": false, 
        "egress_firewall_policy_id": null, 
        "name": "bobby_fwg1", 
        "admin_state_up": true, 
        "ports": [
            "16e6d779-15e9-48fb-abc5-b86457792a15"
        ], 
        "tenant_id": "23c8a121505047b6869edf39f3062712", 
        "id": "a504a4cf-9300-40e0-b2d4-649bd157c55a", 
        "ingress_firewall_policy_id": "fed2d88f-d0e7-4cc5-bd7e-c495f67037b6", 
        "description": "test",
        "project_id": "23c8a121505047b6869edf39f3062712"
    }
}
```

## Status Code<a name="section10470352390"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

