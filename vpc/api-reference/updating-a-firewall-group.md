# Updating a Firewall Group<a name="vpc_firewall_0016"></a>

## Function<a name="section61945363132813"></a>

This API is used to update a firewall group.

## URI<a name="section27354345132813"></a>

PUT /v2.0/fwaas/firewall\_groups/\{firewall\_group\_id\}

## Request Message<a name="section27893714132813"></a>

**Table  1**  Request parameter

<a name="table28101199132813"></a>
<table><thead align="left"><tr id="row55825911132813"><th class="cellrowborder" valign="top" width="19.388061193880613%" id="mcps1.2.5.1.1"><p id="p10707943132813"><a name="p10707943132813"></a><a name="p10707943132813"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18.60813918608139%" id="mcps1.2.5.1.2"><p id="p28975582132813"><a name="p28975582132813"></a><a name="p28975582132813"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="19.148085191480853%" id="mcps1.2.5.1.3"><p id="p18050301132813"><a name="p18050301132813"></a><a name="p18050301132813"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="42.85571442855714%" id="mcps1.2.5.1.4"><p id="p32456290132813"><a name="p32456290132813"></a><a name="p32456290132813"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row37137198132813"><td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.2.5.1.1 "><p id="p13657217132813"><a name="p13657217132813"></a><a name="p13657217132813"></a>firewall_group</p>
</td>
<td class="cellrowborder" valign="top" width="18.60813918608139%" headers="mcps1.2.5.1.2 "><p id="p40187772132813"><a name="p40187772132813"></a><a name="p40187772132813"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="19.148085191480853%" headers="mcps1.2.5.1.3 "><p id="p43289917132813"><a name="p43289917132813"></a><a name="p43289917132813"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.5.1.4 "><p id="p5159094411463"><a name="p5159094411463"></a><a name="p5159094411463"></a>Specifies the firewall group list. For details, see <a href="#table1368812022812">Table 2</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  2** **Firewall Group**  objects

<a name="table1368812022812"></a>
<table><thead align="left"><tr id="row136881720192815"><th class="cellrowborder" valign="top" width="27.73722627737226%" id="mcps1.2.5.1.1"><p id="p2688620132811"><a name="p2688620132811"></a><a name="p2688620132811"></a><strong id="b4222153517525"><a name="b4222153517525"></a><a name="b4222153517525"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="12.428757124287571%" id="mcps1.2.5.1.2"><p id="p7386171235314"><a name="p7386171235314"></a><a name="p7386171235314"></a><strong id="b427913995219"><a name="b427913995219"></a><a name="b427913995219"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="19.948005199480054%" id="mcps1.2.5.1.3"><p id="p15688220162819"><a name="p15688220162819"></a><a name="p15688220162819"></a><strong id="b156531679547"><a name="b156531679547"></a><a name="b156531679547"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.88601139886011%" id="mcps1.2.5.1.4"><p id="p8688172010288"><a name="p8688172010288"></a><a name="p8688172010288"></a><strong id="b965717805416"><a name="b965717805416"></a><a name="b965717805416"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row26891020122819"><td class="cellrowborder" valign="top" width="27.73722627737226%" headers="mcps1.2.5.1.1 "><p id="p3689520102819"><a name="p3689520102819"></a><a name="p3689520102819"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="12.428757124287571%" headers="mcps1.2.5.1.2 "><p id="p838616129535"><a name="p838616129535"></a><a name="p838616129535"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="19.948005199480054%" headers="mcps1.2.5.1.3 "><p id="p166891720192810"><a name="p166891720192810"></a><a name="p166891720192810"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.88601139886011%" headers="mcps1.2.5.1.4 "><p id="p56891120112816"><a name="p56891120112816"></a><a name="p56891120112816"></a>Specifies the name of the firewall group.</p>
<p id="p3706202115111"><a name="p3706202115111"></a><a name="p3706202115111"></a>The value can contain a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row568972062810"><td class="cellrowborder" valign="top" width="27.73722627737226%" headers="mcps1.2.5.1.1 "><p id="p1768917204281"><a name="p1768917204281"></a><a name="p1768917204281"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="12.428757124287571%" headers="mcps1.2.5.1.2 "><p id="p738618127533"><a name="p738618127533"></a><a name="p738618127533"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="19.948005199480054%" headers="mcps1.2.5.1.3 "><p id="p1368912072817"><a name="p1368912072817"></a><a name="p1368912072817"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.88601139886011%" headers="mcps1.2.5.1.4 "><p id="p1669114206286"><a name="p1669114206286"></a><a name="p1669114206286"></a>Provides supplementary information about the firewall group.</p>
<p id="p131697242517"><a name="p131697242517"></a><a name="p131697242517"></a>The value can contain a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row20691132052816"><td class="cellrowborder" valign="top" width="27.73722627737226%" headers="mcps1.2.5.1.1 "><p id="p86911120202818"><a name="p86911120202818"></a><a name="p86911120202818"></a>ingress_firewall_policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="12.428757124287571%" headers="mcps1.2.5.1.2 "><p id="p11386171215311"><a name="p11386171215311"></a><a name="p11386171215311"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="19.948005199480054%" headers="mcps1.2.5.1.3 "><p id="p769112032811"><a name="p769112032811"></a><a name="p769112032811"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.88601139886011%" headers="mcps1.2.5.1.4 "><p id="p669112205283"><a name="p669112205283"></a><a name="p669112205283"></a>Specifies the firewall policy for inbound traffic.</p>
</td>
</tr>
<tr id="row1169132062820"><td class="cellrowborder" valign="top" width="27.73722627737226%" headers="mcps1.2.5.1.1 "><p id="p156911820172819"><a name="p156911820172819"></a><a name="p156911820172819"></a>egress_firewall_policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="12.428757124287571%" headers="mcps1.2.5.1.2 "><p id="p9386712155316"><a name="p9386712155316"></a><a name="p9386712155316"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="19.948005199480054%" headers="mcps1.2.5.1.3 "><p id="p5691192062810"><a name="p5691192062810"></a><a name="p5691192062810"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.88601139886011%" headers="mcps1.2.5.1.4 "><p id="p1769102016284"><a name="p1769102016284"></a><a name="p1769102016284"></a>Specifies the firewall policy for outbound traffic.</p>
</td>
</tr>
<tr id="row176921220182811"><td class="cellrowborder" valign="top" width="27.73722627737226%" headers="mcps1.2.5.1.1 "><p id="p869212018285"><a name="p869212018285"></a><a name="p869212018285"></a>ports</p>
</td>
<td class="cellrowborder" valign="top" width="12.428757124287571%" headers="mcps1.2.5.1.2 "><p id="p138610126537"><a name="p138610126537"></a><a name="p138610126537"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="19.948005199480054%" headers="mcps1.2.5.1.3 "><p id="p5515105824112"><a name="p5515105824112"></a><a name="p5515105824112"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="39.88601139886011%" headers="mcps1.2.5.1.4 "><p id="p669242018288"><a name="p669242018288"></a><a name="p669242018288"></a>Specifies the list of ports bound with the firewall group.</p>
<p id="p10668102685116"><a name="p10668102685116"></a><a name="p10668102685116"></a>The value must be the port ID of the distributed router.</p>
</td>
</tr>
<tr id="row7693182092815"><td class="cellrowborder" valign="top" width="27.73722627737226%" headers="mcps1.2.5.1.1 "><p id="p19693620122810"><a name="p19693620122810"></a><a name="p19693620122810"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="12.428757124287571%" headers="mcps1.2.5.1.2 "><p id="p123861112155311"><a name="p123861112155311"></a><a name="p123861112155311"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="19.948005199480054%" headers="mcps1.2.5.1.3 "><p id="p669362014284"><a name="p669362014284"></a><a name="p669362014284"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.88601139886011%" headers="mcps1.2.5.1.4 "><p id="p1269311209285"><a name="p1269311209285"></a><a name="p1269311209285"></a>Specifies whether the firewall is controlled by the administrator.</p>
<p id="p76011638135114"><a name="p76011638135114"></a><a name="p76011638135114"></a>The value can be <strong id="b4957120185718"><a name="b4957120185718"></a><a name="b4957120185718"></a>true</strong> or <strong id="b18958122012572"><a name="b18958122012572"></a><a name="b18958122012572"></a>false</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Response Message<a name="section39612821132813"></a>

**Table  3**  Response parameter

<a name="table16604779132813"></a>
<table><thead align="left"><tr id="row54692786132813"><th class="cellrowborder" valign="top" width="23.169999999999998%" id="mcps1.2.4.1.1"><p id="p37352036132813"><a name="p37352036132813"></a><a name="p37352036132813"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25.61%" id="mcps1.2.4.1.2"><p id="p5454829132813"><a name="p5454829132813"></a><a name="p5454829132813"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51.22%" id="mcps1.2.4.1.3"><p id="p31055875132813"><a name="p31055875132813"></a><a name="p31055875132813"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row6198481132813"><td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p27058422132813"><a name="p27058422132813"></a><a name="p27058422132813"></a>firewall_group</p>
</td>
<td class="cellrowborder" valign="top" width="25.61%" headers="mcps1.2.4.1.2 "><p id="p32561041132813"><a name="p32561041132813"></a><a name="p32561041132813"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.2.4.1.3 "><p id="p2612398132813"><a name="p2612398132813"></a><a name="p2612398132813"></a>Specifies the firewall group list. For details, see <a href="#table31629250121127">Table 4</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **Firewall Group**  objects

<a name="table31629250121127"></a>
<table><thead align="left"><tr id="row45711693121127"><th class="cellrowborder" valign="top" width="23.44%" id="mcps1.2.4.1.1"><p id="p46819705121127"><a name="p46819705121127"></a><a name="p46819705121127"></a><strong id="b2300184512578"><a name="b2300184512578"></a><a name="b2300184512578"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25.55%" id="mcps1.2.4.1.2"><p id="p35064605121127"><a name="p35064605121127"></a><a name="p35064605121127"></a><strong id="b187574675715"><a name="b187574675715"></a><a name="b187574675715"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51.01%" id="mcps1.2.4.1.3"><p id="p11952850121127"><a name="p11952850121127"></a><a name="p11952850121127"></a><strong id="b374013467574"><a name="b374013467574"></a><a name="b374013467574"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row20395689121127"><td class="cellrowborder" valign="top" width="23.44%" headers="mcps1.2.4.1.1 "><p id="p50168503121127"><a name="p50168503121127"></a><a name="p50168503121127"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="25.55%" headers="mcps1.2.4.1.2 "><p id="p47513116121127"><a name="p47513116121127"></a><a name="p47513116121127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.2.4.1.3 "><p id="p62072725121127"><a name="p62072725121127"></a><a name="p62072725121127"></a>Specifies the UUID of the firewall group. </p>
</td>
</tr>
<tr id="row34896104121127"><td class="cellrowborder" valign="top" width="23.44%" headers="mcps1.2.4.1.1 "><p id="p52608071121127"><a name="p52608071121127"></a><a name="p52608071121127"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="25.55%" headers="mcps1.2.4.1.2 "><p id="p59846605121127"><a name="p59846605121127"></a><a name="p59846605121127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.2.4.1.3 "><p id="p28604909121127"><a name="p28604909121127"></a><a name="p28604909121127"></a>Specifies the name of the firewall group.</p>
</td>
</tr>
<tr id="row11129246121127"><td class="cellrowborder" valign="top" width="23.44%" headers="mcps1.2.4.1.1 "><p id="p39887063121127"><a name="p39887063121127"></a><a name="p39887063121127"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="25.55%" headers="mcps1.2.4.1.2 "><p id="p28745735121127"><a name="p28745735121127"></a><a name="p28745735121127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.2.4.1.3 "><p id="p35639020121127"><a name="p35639020121127"></a><a name="p35639020121127"></a>Provides supplementary information about the firewall group.</p>
</td>
</tr>
<tr id="row677472121127"><td class="cellrowborder" valign="top" width="23.44%" headers="mcps1.2.4.1.1 "><p id="p60717947121127"><a name="p60717947121127"></a><a name="p60717947121127"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="25.55%" headers="mcps1.2.4.1.2 "><p id="p65871708121127"><a name="p65871708121127"></a><a name="p65871708121127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.2.4.1.3 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row38137474121127"><td class="cellrowborder" valign="top" width="23.44%" headers="mcps1.2.4.1.1 "><p id="p35500294121127"><a name="p35500294121127"></a><a name="p35500294121127"></a>ingress_firewall_policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="25.55%" headers="mcps1.2.4.1.2 "><p id="p49995809121127"><a name="p49995809121127"></a><a name="p49995809121127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.2.4.1.3 "><p id="p56499442121127"><a name="p56499442121127"></a><a name="p56499442121127"></a>Specifies the firewall policy for inbound traffic.</p>
</td>
</tr>
<tr id="row9094936121127"><td class="cellrowborder" valign="top" width="23.44%" headers="mcps1.2.4.1.1 "><p id="p34911245121127"><a name="p34911245121127"></a><a name="p34911245121127"></a>egress_firewall_policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="25.55%" headers="mcps1.2.4.1.2 "><p id="p44624490121127"><a name="p44624490121127"></a><a name="p44624490121127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.2.4.1.3 "><p id="p37100641121127"><a name="p37100641121127"></a><a name="p37100641121127"></a>Specifies the firewall policy for outbound traffic.</p>
</td>
</tr>
<tr id="row31622902121127"><td class="cellrowborder" valign="top" width="23.44%" headers="mcps1.2.4.1.1 "><p id="p65911012121127"><a name="p65911012121127"></a><a name="p65911012121127"></a>ports</p>
</td>
<td class="cellrowborder" valign="top" width="25.55%" headers="mcps1.2.4.1.2 "><p id="p5459978121127"><a name="p5459978121127"></a><a name="p5459978121127"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.2.4.1.3 "><p id="p61002567121127"><a name="p61002567121127"></a><a name="p61002567121127"></a>Specifies the list of ports bound with the firewall group.</p>
</td>
</tr>
<tr id="row48186031121127"><td class="cellrowborder" valign="top" width="23.44%" headers="mcps1.2.4.1.1 "><p id="p33368479121127"><a name="p33368479121127"></a><a name="p33368479121127"></a>public</p>
</td>
<td class="cellrowborder" valign="top" width="25.55%" headers="mcps1.2.4.1.2 "><p id="p7938198121127"><a name="p7938198121127"></a><a name="p7938198121127"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.2.4.1.3 "><p id="p56166201121127"><a name="p56166201121127"></a><a name="p56166201121127"></a>Specifies whether the firewall policy can be shared by different tenants.</p>
</td>
</tr>
<tr id="row60912436121127"><td class="cellrowborder" valign="top" width="23.44%" headers="mcps1.2.4.1.1 "><p id="p66273781121127"><a name="p66273781121127"></a><a name="p66273781121127"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="25.55%" headers="mcps1.2.4.1.2 "><p id="p7141533121127"><a name="p7141533121127"></a><a name="p7141533121127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.2.4.1.3 "><p id="p6468335121127"><a name="p6468335121127"></a><a name="p6468335121127"></a>Specifies the status of the firewall policy.</p>
</td>
</tr>
<tr id="row59833296121127"><td class="cellrowborder" valign="top" width="23.44%" headers="mcps1.2.4.1.1 "><p id="p44051842121127"><a name="p44051842121127"></a><a name="p44051842121127"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="25.55%" headers="mcps1.2.4.1.2 "><p id="p58587899121127"><a name="p58587899121127"></a><a name="p58587899121127"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.2.4.1.3 "><p id="p3428646121127"><a name="p3428646121127"></a><a name="p3428646121127"></a>Specifies whether the firewall is controlled by the administrator.</p>
</td>
</tr>
<tr id="row7228115213486"><td class="cellrowborder" valign="top" width="23.44%" headers="mcps1.2.4.1.1 "><p id="p53071912134918"><a name="p53071912134918"></a><a name="p53071912134918"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="25.55%" headers="mcps1.2.4.1.2 "><p id="p1731011220498"><a name="p1731011220498"></a><a name="p1731011220498"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.2.4.1.3 "><p id="p1663719453013"><a name="p1663719453013"></a><a name="p1663719453013"></a>Specifies the project ID. </p>
</td>
</tr>
</tbody>
</table>

## Example:<a name="section26765578132813"></a>

Example request

```
PUT https://{Endpoint}/v2.0/fwaas/firewall_groups/2fb0e81f-9f63-44b2-9894-c13a3284594a 

{
    "firewall_group": {
        "egress_firewall_policy_id": "53f36c32-db25-4856-a0ba-e605fd88c5e9"
    }
}
```

Example response

```
{
    "firewall_group": {
        "status": "PENDING_UPDATE", 
        "public": false, 
        "egress_firewall_policy_id": "53f36c32-db25-4856-a0ba-e605fd88c5e9", 
        "name": "", 
        "admin_state_up": true, 
        "ports": [
            "c133f2bf-6937-4416-bb17-012e1be5cd2d"
        ], 
        "tenant_id": "23c8a121505047b6869edf39f3062712", 
        "id": "0415f554-26ed-44e7-a881-bdf4e6216e38", 
        "ingress_firewall_policy_id": "afc52ce9-5305-4ec9-9feb-44feb8330341", 
        "description": "",
        "project_id": "23c8a121505047b6869edf39f3062712"
    }
}
```

## Status Code<a name="section10470352390"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

