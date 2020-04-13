# Creating a Firewall Group<a name="vpc_firewall_0015"></a>

## Function<a name="section28317954132753"></a>

This API is used to create a firewall group.

## URI<a name="section55587849132753"></a>

POST /v2.0/fwaas/firewall\_groups

## Request Message<a name="section28981251132753"></a>

**Table  1**  Request parameter

<a name="table23322114132753"></a>
<table><thead align="left"><tr id="row65935357132753"><th class="cellrowborder" valign="top" width="19.39%" id="mcps1.2.5.1.1"><p id="p47877448132753"><a name="p47877448132753"></a><a name="p47877448132753"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.29%" id="mcps1.2.5.1.2"><p id="p52491337132753"><a name="p52491337132753"></a><a name="p52491337132753"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="20.46%" id="mcps1.2.5.1.3"><p id="p45667362132753"><a name="p45667362132753"></a><a name="p45667362132753"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="42.86%" id="mcps1.2.5.1.4"><p id="p17633266132753"><a name="p17633266132753"></a><a name="p17633266132753"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row8939225132753"><td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.2.5.1.1 "><p id="p59896822132753"><a name="p59896822132753"></a><a name="p59896822132753"></a>firewall_group</p>
</td>
<td class="cellrowborder" valign="top" width="17.29%" headers="mcps1.2.5.1.2 "><p id="p49917547132753"><a name="p49917547132753"></a><a name="p49917547132753"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="20.46%" headers="mcps1.2.5.1.3 "><p id="p64285015132753"><a name="p64285015132753"></a><a name="p64285015132753"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="42.86%" headers="mcps1.2.5.1.4 "><p id="p48871362132652"><a name="p48871362132652"></a><a name="p48871362132652"></a>Specifies the firewall group list. For details, see <a href="#table31629250121127">Table 2</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  2** **Firewall Group**  objects

<a name="table31629250121127"></a>
<table><thead align="left"><tr id="row45711693121127"><th class="cellrowborder" valign="top" width="26.897310268973108%" id="mcps1.2.5.1.1"><p id="p46819705121127"><a name="p46819705121127"></a><a name="p46819705121127"></a><strong id="b5241633192214"><a name="b5241633192214"></a><a name="b5241633192214"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="13.268673132686734%" id="mcps1.2.5.1.2"><p id="p8500055165416"><a name="p8500055165416"></a><a name="p8500055165416"></a><strong id="b4555347222"><a name="b4555347222"></a><a name="b4555347222"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="19.948005199480054%" id="mcps1.2.5.1.3"><p id="p35064605121127"><a name="p35064605121127"></a><a name="p35064605121127"></a><strong id="b242163517223"><a name="b242163517223"></a><a name="b242163517223"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.88601139886011%" id="mcps1.2.5.1.4"><p id="p11952850121127"><a name="p11952850121127"></a><a name="p11952850121127"></a><strong id="b198383582216"><a name="b198383582216"></a><a name="b198383582216"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row34896104121127"><td class="cellrowborder" valign="top" width="26.897310268973108%" headers="mcps1.2.5.1.1 "><p id="p52608071121127"><a name="p52608071121127"></a><a name="p52608071121127"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="13.268673132686734%" headers="mcps1.2.5.1.2 "><p id="p1500355195417"><a name="p1500355195417"></a><a name="p1500355195417"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="19.948005199480054%" headers="mcps1.2.5.1.3 "><p id="p59846605121127"><a name="p59846605121127"></a><a name="p59846605121127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.88601139886011%" headers="mcps1.2.5.1.4 "><p id="p28604909121127"><a name="p28604909121127"></a><a name="p28604909121127"></a>Specifies the name of the firewall group.</p>
<p id="p83231610195414"><a name="p83231610195414"></a><a name="p83231610195414"></a>The value can contain a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row11129246121127"><td class="cellrowborder" valign="top" width="26.897310268973108%" headers="mcps1.2.5.1.1 "><p id="p39887063121127"><a name="p39887063121127"></a><a name="p39887063121127"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="13.268673132686734%" headers="mcps1.2.5.1.2 "><p id="p1450085505420"><a name="p1450085505420"></a><a name="p1450085505420"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="19.948005199480054%" headers="mcps1.2.5.1.3 "><p id="p28745735121127"><a name="p28745735121127"></a><a name="p28745735121127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.88601139886011%" headers="mcps1.2.5.1.4 "><p id="p35639020121127"><a name="p35639020121127"></a><a name="p35639020121127"></a>Provides supplementary information about the firewall group.</p>
<p id="p11817162215413"><a name="p11817162215413"></a><a name="p11817162215413"></a>The value can contain a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row38137474121127"><td class="cellrowborder" valign="top" width="26.897310268973108%" headers="mcps1.2.5.1.1 "><p id="p35500294121127"><a name="p35500294121127"></a><a name="p35500294121127"></a>ingress_firewall_policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="13.268673132686734%" headers="mcps1.2.5.1.2 "><p id="p3500155520543"><a name="p3500155520543"></a><a name="p3500155520543"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="19.948005199480054%" headers="mcps1.2.5.1.3 "><p id="p49995809121127"><a name="p49995809121127"></a><a name="p49995809121127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.88601139886011%" headers="mcps1.2.5.1.4 "><p id="p56499442121127"><a name="p56499442121127"></a><a name="p56499442121127"></a>Specifies the firewall policy for inbound traffic.</p>
</td>
</tr>
<tr id="row9094936121127"><td class="cellrowborder" valign="top" width="26.897310268973108%" headers="mcps1.2.5.1.1 "><p id="p34911245121127"><a name="p34911245121127"></a><a name="p34911245121127"></a>egress_firewall_policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="13.268673132686734%" headers="mcps1.2.5.1.2 "><p id="p1950085514546"><a name="p1950085514546"></a><a name="p1950085514546"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="19.948005199480054%" headers="mcps1.2.5.1.3 "><p id="p44624490121127"><a name="p44624490121127"></a><a name="p44624490121127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.88601139886011%" headers="mcps1.2.5.1.4 "><p id="p37100641121127"><a name="p37100641121127"></a><a name="p37100641121127"></a>Specifies the firewall policy for outbound traffic.</p>
</td>
</tr>
<tr id="row31622902121127"><td class="cellrowborder" valign="top" width="26.897310268973108%" headers="mcps1.2.5.1.1 "><p id="p65911012121127"><a name="p65911012121127"></a><a name="p65911012121127"></a>ports</p>
</td>
<td class="cellrowborder" valign="top" width="13.268673132686734%" headers="mcps1.2.5.1.2 "><p id="p8500855175412"><a name="p8500855175412"></a><a name="p8500855175412"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="19.948005199480054%" headers="mcps1.2.5.1.3 "><p id="p5459978121127"><a name="p5459978121127"></a><a name="p5459978121127"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="39.88601139886011%" headers="mcps1.2.5.1.4 "><p id="p61002567121127"><a name="p61002567121127"></a><a name="p61002567121127"></a>Specifies the list of ports bound with the firewall group.</p>
<p id="p10668102685116"><a name="p10668102685116"></a><a name="p10668102685116"></a>The value must be the port ID of the distributed router.</p>
</td>
</tr>
<tr id="row59833296121127"><td class="cellrowborder" valign="top" width="26.897310268973108%" headers="mcps1.2.5.1.1 "><p id="p44051842121127"><a name="p44051842121127"></a><a name="p44051842121127"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="13.268673132686734%" headers="mcps1.2.5.1.2 "><p id="p3500455195415"><a name="p3500455195415"></a><a name="p3500455195415"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="19.948005199480054%" headers="mcps1.2.5.1.3 "><p id="p58587899121127"><a name="p58587899121127"></a><a name="p58587899121127"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.88601139886011%" headers="mcps1.2.5.1.4 "><p id="p3428646121127"><a name="p3428646121127"></a><a name="p3428646121127"></a>Specifies whether the firewall is controlled by the administrator.</p>
<p id="p19344243185411"><a name="p19344243185411"></a><a name="p19344243185411"></a>The value can be <strong id="b1138151814315"><a name="b1138151814315"></a><a name="b1138151814315"></a>true</strong> or <strong id="b5152161834312"><a name="b5152161834312"></a><a name="b5152161834312"></a>false</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Response Message<a name="section47249684132753"></a>

**Table  3**  Response parameter

<a name="table22528036132753"></a>
<table><thead align="left"><tr id="row54420002132753"><th class="cellrowborder" valign="top" width="23.169999999999998%" id="mcps1.2.4.1.1"><p id="p43836262132753"><a name="p43836262132753"></a><a name="p43836262132753"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25.61%" id="mcps1.2.4.1.2"><p id="p57315890132753"><a name="p57315890132753"></a><a name="p57315890132753"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51.22%" id="mcps1.2.4.1.3"><p id="p55101661132753"><a name="p55101661132753"></a><a name="p55101661132753"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row23789310132753"><td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p30981925132753"><a name="p30981925132753"></a><a name="p30981925132753"></a>firewall_group</p>
</td>
<td class="cellrowborder" valign="top" width="25.61%" headers="mcps1.2.4.1.2 "><p id="p1451635132753"><a name="p1451635132753"></a><a name="p1451635132753"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.2.4.1.3 "><p id="p47442693132753"><a name="p47442693132753"></a><a name="p47442693132753"></a>Specifies the firewall group list. For details, see <a href="#table7886851182616">Table 4</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **Firewall Group**  objects

<a name="table7886851182616"></a>
<table><thead align="left"><tr id="row388711511267"><th class="cellrowborder" valign="top" width="35.3%" id="mcps1.2.4.1.1"><p id="p4887205152611"><a name="p4887205152611"></a><a name="p4887205152611"></a><strong id="b11649123714310"><a name="b11649123714310"></a><a name="b11649123714310"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="21.57%" id="mcps1.2.4.1.2"><p id="p288711516264"><a name="p288711516264"></a><a name="p288711516264"></a><strong id="b480163917438"><a name="b480163917438"></a><a name="b480163917438"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="43.13%" id="mcps1.2.4.1.3"><p id="p12887651122618"><a name="p12887651122618"></a><a name="p12887651122618"></a><strong id="b1221240104316"><a name="b1221240104316"></a><a name="b1221240104316"></a>Description</strong></p>
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
<tr id="row788715512269"><td class="cellrowborder" valign="top" width="35.3%" headers="mcps1.2.4.1.1 "><p id="p6887105192617"><a name="p6887105192617"></a><a name="p6887105192617"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="21.57%" headers="mcps1.2.4.1.2 "><p id="p12887175111264"><a name="p12887175111264"></a><a name="p12887175111264"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.13%" headers="mcps1.2.4.1.3 "><p id="p4889105118269"><a name="p4889105118269"></a><a name="p4889105118269"></a>Specifies the name of the firewall group.</p>
</td>
</tr>
<tr id="row1288910518269"><td class="cellrowborder" valign="top" width="35.3%" headers="mcps1.2.4.1.1 "><p id="p148891451162617"><a name="p148891451162617"></a><a name="p148891451162617"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="21.57%" headers="mcps1.2.4.1.2 "><p id="p15889125111262"><a name="p15889125111262"></a><a name="p15889125111262"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.13%" headers="mcps1.2.4.1.3 "><p id="p688975152619"><a name="p688975152619"></a><a name="p688975152619"></a>Provides supplementary information about the firewall group.</p>
</td>
</tr>
<tr id="row677472121127"><td class="cellrowborder" valign="top" width="35.3%" headers="mcps1.2.4.1.1 "><p id="p60717947121127"><a name="p60717947121127"></a><a name="p60717947121127"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="21.57%" headers="mcps1.2.4.1.2 "><p id="p65871708121127"><a name="p65871708121127"></a><a name="p65871708121127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.13%" headers="mcps1.2.4.1.3 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row16889175115261"><td class="cellrowborder" valign="top" width="35.3%" headers="mcps1.2.4.1.1 "><p id="p6889155182616"><a name="p6889155182616"></a><a name="p6889155182616"></a>ingress_firewall_policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="21.57%" headers="mcps1.2.4.1.2 "><p id="p198896511262"><a name="p198896511262"></a><a name="p198896511262"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.13%" headers="mcps1.2.4.1.3 "><p id="p7890105182610"><a name="p7890105182610"></a><a name="p7890105182610"></a>Specifies the firewall policy for inbound traffic.</p>
</td>
</tr>
<tr id="row118901051122618"><td class="cellrowborder" valign="top" width="35.3%" headers="mcps1.2.4.1.1 "><p id="p189075119263"><a name="p189075119263"></a><a name="p189075119263"></a>egress_firewall_policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="21.57%" headers="mcps1.2.4.1.2 "><p id="p1989075152620"><a name="p1989075152620"></a><a name="p1989075152620"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.13%" headers="mcps1.2.4.1.3 "><p id="p489045192610"><a name="p489045192610"></a><a name="p489045192610"></a>Specifies the firewall policy for outbound traffic.</p>
</td>
</tr>
<tr id="row11890165162618"><td class="cellrowborder" valign="top" width="35.3%" headers="mcps1.2.4.1.1 "><p id="p889075115268"><a name="p889075115268"></a><a name="p889075115268"></a>ports</p>
</td>
<td class="cellrowborder" valign="top" width="21.57%" headers="mcps1.2.4.1.2 "><p id="p38902051102616"><a name="p38902051102616"></a><a name="p38902051102616"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="43.13%" headers="mcps1.2.4.1.3 "><p id="p148906511265"><a name="p148906511265"></a><a name="p148906511265"></a>Specifies the list of ports bound with the firewall group.</p>
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
<tr id="row9890155162614"><td class="cellrowborder" valign="top" width="35.3%" headers="mcps1.2.4.1.1 "><p id="p1889085142618"><a name="p1889085142618"></a><a name="p1889085142618"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="21.57%" headers="mcps1.2.4.1.2 "><p id="p10890551152617"><a name="p10890551152617"></a><a name="p10890551152617"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="43.13%" headers="mcps1.2.4.1.3 "><p id="p5890115118263"><a name="p5890115118263"></a><a name="p5890115118263"></a>Specifies whether the firewall is controlled by the administrator.</p>
</td>
</tr>
<tr id="row7228115213486"><td class="cellrowborder" valign="top" width="35.3%" headers="mcps1.2.4.1.1 "><p id="p53071912134918"><a name="p53071912134918"></a><a name="p53071912134918"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="21.57%" headers="mcps1.2.4.1.2 "><p id="p1731011220498"><a name="p1731011220498"></a><a name="p1731011220498"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.13%" headers="mcps1.2.4.1.3 "><p id="p555515419297"><a name="p555515419297"></a><a name="p555515419297"></a>Specifies the project ID. </p>
</td>
</tr>
</tbody>
</table>

## Example:<a name="section59424075132753"></a>

Example request

```
POST https://{Endpoint}/v2.0/fwaas/firewall_groups

{
    "firewall_group": {
        "ingress_firewall_policy_id": "afc52ce9-5305-4ec9-9feb-44feb8330341", 
        "ports": [
            "c133f2bf-6937-4416-bb17-012e1be5cd2d"
        ]
    }
}
```

Example response

```
{
    "firewall_group": {
        "status": "PENDING_CREATE", 
        "public": false, 
        "egress_firewall_policy_id": null, 
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

