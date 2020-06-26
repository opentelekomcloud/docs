# Querying a Firewall Policy<a name="vpc_firewall_0007"></a>

## Function<a name="section915947313242"></a>

This API is used to query details about a specific firewall policy.

## URI<a name="section2518841213242"></a>

GET /v2.0/fwaas/firewall\_policies/\{firewall\_policy\_id\}

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
<tbody><tr id="row19681041189"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p1682422682817"><a name="p1682422682817"></a><a name="p1682422682817"></a>firewall_policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.2 "><p id="p1797015416817"><a name="p1797015416817"></a><a name="p1797015416817"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.5.1.3 "><p id="p19701411813"><a name="p19701411813"></a><a name="p19701411813"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.5.1.4 "><p id="p109701641488"><a name="p109701641488"></a><a name="p109701641488"></a>Specifies the firewall policy ID, which uniquely identifies the firewall policy. The <strong id="b12400133185915"><a name="b12400133185915"></a><a name="b12400133185915"></a>firewall_policy_id</strong> value is used as the filter.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section5030939813242"></a>

None

## Response Message<a name="section2488003713242"></a>

**Table  2**  Response parameter

<a name="table6694832013242"></a>
<table><thead align="left"><tr id="row6068200913242"><th class="cellrowborder" valign="top" width="21.349999999999998%" id="mcps1.2.4.1.1"><p id="p963376713242"><a name="p963376713242"></a><a name="p963376713242"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.11%" id="mcps1.2.4.1.2"><p id="p303129213242"><a name="p303129213242"></a><a name="p303129213242"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="59.540000000000006%" id="mcps1.2.4.1.3"><p id="p1024114813242"><a name="p1024114813242"></a><a name="p1024114813242"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row4115792613242"><td class="cellrowborder" valign="top" width="21.349999999999998%" headers="mcps1.2.4.1.1 "><p id="p1605288813242"><a name="p1605288813242"></a><a name="p1605288813242"></a>firewall_policy</p>
</td>
<td class="cellrowborder" valign="top" width="19.11%" headers="mcps1.2.4.1.2 "><p id="p2885681613242"><a name="p2885681613242"></a><a name="p2885681613242"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="59.540000000000006%" headers="mcps1.2.4.1.3 "><p id="p6121237313242"><a name="p6121237313242"></a><a name="p6121237313242"></a>Specifies the firewall policy list. For details, see <a href="#table17002720121127">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **Firewall Policy**  objects

<a name="table17002720121127"></a>
<table><thead align="left"><tr id="row16929792121127"><th class="cellrowborder" valign="top" width="32.083208320832085%" id="mcps1.2.4.1.1"><p id="p18873879121127"><a name="p18873879121127"></a><a name="p18873879121127"></a><strong id="b2095220401262"><a name="b2095220401262"></a><a name="b2095220401262"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="22.632263226322635%" id="mcps1.2.4.1.2"><p id="p12638309121127"><a name="p12638309121127"></a><a name="p12638309121127"></a><strong id="b823616426612"><a name="b823616426612"></a><a name="b823616426612"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="45.28452845284529%" id="mcps1.2.4.1.3"><p id="p61199938121127"><a name="p61199938121127"></a><a name="p61199938121127"></a><strong id="b15115144319610"><a name="b15115144319610"></a><a name="b15115144319610"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row46402691121127"><td class="cellrowborder" valign="top" width="32.083208320832085%" headers="mcps1.2.4.1.1 "><p id="p11805115121127"><a name="p11805115121127"></a><a name="p11805115121127"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="22.632263226322635%" headers="mcps1.2.4.1.2 "><p id="p13006089121127"><a name="p13006089121127"></a><a name="p13006089121127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.28452845284529%" headers="mcps1.2.4.1.3 "><p id="p13152683121127"><a name="p13152683121127"></a><a name="p13152683121127"></a>Specifies the UUID of the firewall policy.</p>
</td>
</tr>
<tr id="row9858171121127"><td class="cellrowborder" valign="top" width="32.083208320832085%" headers="mcps1.2.4.1.1 "><p id="p49865700121127"><a name="p49865700121127"></a><a name="p49865700121127"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="22.632263226322635%" headers="mcps1.2.4.1.2 "><p id="p6225460121127"><a name="p6225460121127"></a><a name="p6225460121127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.28452845284529%" headers="mcps1.2.4.1.3 "><p id="p40337147121127"><a name="p40337147121127"></a><a name="p40337147121127"></a>Specifies the name of the firewall policy.</p>
</td>
</tr>
<tr id="row61803802121127"><td class="cellrowborder" valign="top" width="32.083208320832085%" headers="mcps1.2.4.1.1 "><p id="p39621949121127"><a name="p39621949121127"></a><a name="p39621949121127"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="22.632263226322635%" headers="mcps1.2.4.1.2 "><p id="p66053143121127"><a name="p66053143121127"></a><a name="p66053143121127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.28452845284529%" headers="mcps1.2.4.1.3 "><p id="p15357220121127"><a name="p15357220121127"></a><a name="p15357220121127"></a>Provides supplementary information about the firewall policy.</p>
</td>
</tr>
<tr id="row57644277121127"><td class="cellrowborder" valign="top" width="32.083208320832085%" headers="mcps1.2.4.1.1 "><p id="p9761241121127"><a name="p9761241121127"></a><a name="p9761241121127"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="22.632263226322635%" headers="mcps1.2.4.1.2 "><p id="p20138053121127"><a name="p20138053121127"></a><a name="p20138053121127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.28452845284529%" headers="mcps1.2.4.1.3 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row33369184121127"><td class="cellrowborder" valign="top" width="32.083208320832085%" headers="mcps1.2.4.1.1 "><p id="p16940942121127"><a name="p16940942121127"></a><a name="p16940942121127"></a>firewall_rules</p>
</td>
<td class="cellrowborder" valign="top" width="22.632263226322635%" headers="mcps1.2.4.1.2 "><p id="p1916011339370"><a name="p1916011339370"></a><a name="p1916011339370"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="45.28452845284529%" headers="mcps1.2.4.1.3 "><p id="p53455884121127"><a name="p53455884121127"></a><a name="p53455884121127"></a>Specifies the firewall rules referenced by the firewall policy.</p>
</td>
</tr>
<tr id="row717167121127"><td class="cellrowborder" valign="top" width="32.083208320832085%" headers="mcps1.2.4.1.1 "><p id="p30704110121127"><a name="p30704110121127"></a><a name="p30704110121127"></a>audited</p>
</td>
<td class="cellrowborder" valign="top" width="22.632263226322635%" headers="mcps1.2.4.1.2 "><p id="p10804884121127"><a name="p10804884121127"></a><a name="p10804884121127"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="45.28452845284529%" headers="mcps1.2.4.1.3 "><p id="p3925300121127"><a name="p3925300121127"></a><a name="p3925300121127"></a>Specifies the audit flag.</p>
</td>
</tr>
<tr id="row40905717121127"><td class="cellrowborder" valign="top" width="32.083208320832085%" headers="mcps1.2.4.1.1 "><p id="p16821838121127"><a name="p16821838121127"></a><a name="p16821838121127"></a>public</p>
</td>
<td class="cellrowborder" valign="top" width="22.632263226322635%" headers="mcps1.2.4.1.2 "><p id="p49691806121127"><a name="p49691806121127"></a><a name="p49691806121127"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="45.28452845284529%" headers="mcps1.2.4.1.3 "><p id="p31604739121127"><a name="p31604739121127"></a><a name="p31604739121127"></a>Specifies whether the firewall policy can be shared by different tenants.</p>
</td>
</tr>
<tr id="row109594223354"><td class="cellrowborder" valign="top" width="32.083208320832085%" headers="mcps1.2.4.1.1 "><p id="p870051413911"><a name="p870051413911"></a><a name="p870051413911"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="22.632263226322635%" headers="mcps1.2.4.1.2 "><p id="p17700201411911"><a name="p17700201411911"></a><a name="p17700201411911"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.28452845284529%" headers="mcps1.2.4.1.3 "><p id="p20137347142815"><a name="p20137347142815"></a><a name="p20137347142815"></a>Specifies the project ID. </p>
</td>
</tr>
</tbody>
</table>

## Example:<a name="section478525713242"></a>

Example request

```
GET https://{Endpoint}/v2.0/fwaas/firewall_policies/fed2d88f-d0e7-4cc5-bd7e-c495f67037b6
```

Example response

```
{
    "firewall_policy": {
        "description": "", 
        "firewall_rules": [
            "3c0e6267-73df-4d9a-87a6-e226f2db2036"
        ], 
        "tenant_id": "23c8a121505047b6869edf39f3062712", 
        "public": false, 
        "id": "fed2d88f-d0e7-4cc5-bd7e-c495f67037b6", 
        "audited": false, 
        "name": "bobby_fwp1",
        "project_id": "23c8a121505047b6869edf39f3062712"
    }
}
```

## Status Code<a name="section10470352390"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

