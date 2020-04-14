# Querying Firewall Policies<a name="vpc_firewall_0006"></a>

## Function<a name="section836818132340"></a>

This API is used to query all firewall policies accessible to the tenant submitting the request. 

## URI<a name="section20177217132340"></a>

GET /v2.0/fwaas/firewall\_policies

Example of querying policies by page

```
GET https://{Endpoint}/v2.0/fwaas/firewall_policies?limit=2&marker=6b70e321-0c21-4b83-bb8a-a886d1414a5f&page_reverse=False
```

[Table 1](#table2168229184411)  describes the parameters.

**Table  1**  Parameter description

<a name="table2168229184411"></a>
<table><thead align="left"><tr id="row62731129194416"><th class="cellrowborder" valign="top" width="22.222222222222225%" id="mcps1.2.5.1.1"><p id="p202731029194414"><a name="p202731029194414"></a><a name="p202731029194414"></a><strong id="b74701044111517"><a name="b74701044111517"></a><a name="b74701044111517"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.14141414141414%" id="mcps1.2.5.1.2"><p id="p827332934419"><a name="p827332934419"></a><a name="p827332934419"></a><strong id="b164541245171517"><a name="b164541245171517"></a><a name="b164541245171517"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.27272727272727%" id="mcps1.2.5.1.3"><p id="p3273829124411"><a name="p3273829124411"></a><a name="p3273829124411"></a><strong id="b1837313462151"><a name="b1837313462151"></a><a name="b1837313462151"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="36.36363636363636%" id="mcps1.2.5.1.4"><p id="p18273529184418"><a name="p18273529184418"></a><a name="p18273529184418"></a><strong id="b097104714155"><a name="b097104714155"></a><a name="b097104714155"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row2027311294446"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p227317292447"><a name="p227317292447"></a><a name="p227317292447"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.2 "><p id="p1273192914419"><a name="p1273192914419"></a><a name="p1273192914419"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.5.1.3 "><p id="p192737290449"><a name="p192737290449"></a><a name="p192737290449"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.5.1.4 "><p id="p172735292445"><a name="p172735292445"></a><a name="p172735292445"></a>Specifies that the ID is used as the filtering condition.</p>
</td>
</tr>
<tr id="row1327314298444"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p18273102911445"><a name="p18273102911445"></a><a name="p18273102911445"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.2 "><p id="p1327342914412"><a name="p1327342914412"></a><a name="p1327342914412"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.5.1.3 "><p id="p1273112954414"><a name="p1273112954414"></a><a name="p1273112954414"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.5.1.4 "><p id="p1627318299444"><a name="p1627318299444"></a><a name="p1627318299444"></a>Specifies that the name is used as the filtering condition.</p>
</td>
</tr>
<tr id="row227382915449"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p1627342919446"><a name="p1627342919446"></a><a name="p1627342919446"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.2 "><p id="p02741429174411"><a name="p02741429174411"></a><a name="p02741429174411"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.5.1.3 "><p id="p1727442911446"><a name="p1727442911446"></a><a name="p1727442911446"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.5.1.4 "><p id="p16274429204415"><a name="p16274429204415"></a><a name="p16274429204415"></a>Specifies that the description is used as the filtering condition.</p>
</td>
</tr>
<tr id="row22741329104419"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p52741929134414"><a name="p52741929134414"></a><a name="p52741929134414"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.2 "><p id="p1227415292446"><a name="p1227415292446"></a><a name="p1227415292446"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.5.1.3 "><p id="p18274429154412"><a name="p18274429154412"></a><a name="p18274429154412"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.5.1.4 "><p id="p1227413297440"><a name="p1227413297440"></a><a name="p1227413297440"></a>Specifies that the project ID is used as the filtering condition.</p>
</td>
</tr>
<tr id="row192740294443"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p192741229104418"><a name="p192741229104418"></a><a name="p192741229104418"></a>marker</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.2 "><p id="p152741298443"><a name="p152741298443"></a><a name="p152741298443"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.5.1.3 "><p id="p13274229194419"><a name="p13274229194419"></a><a name="p13274229194419"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.5.1.4 "><p id="p2027415296449"><a name="p2027415296449"></a><a name="p2027415296449"></a>Specifies the start resource ID of pagination query. If the parameter is left blank, only resources on the first page are queried.</p>
</td>
</tr>
<tr id="row112741929134413"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p727492918445"><a name="p727492918445"></a><a name="p727492918445"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.2 "><p id="p72746298445"><a name="p72746298445"></a><a name="p72746298445"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.5.1.3 "><p id="p327413298441"><a name="p327413298441"></a><a name="p327413298441"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.5.1.4 "><p id="p8274329174411"><a name="p8274329174411"></a><a name="p8274329174411"></a>Specifies the number of records on each page. The value ranges from 0 to intmax.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section49464339132340"></a>

None

## Response Message<a name="section60203718132340"></a>

**Table  2**  Response parameter

<a name="table9250393132340"></a>
<table><thead align="left"><tr id="row50269734132340"><th class="cellrowborder" valign="top" width="23.330000000000002%" id="mcps1.2.4.1.1"><p id="p65065932132340"><a name="p65065932132340"></a><a name="p65065932132340"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.78%" id="mcps1.2.4.1.2"><p id="p19160762132340"><a name="p19160762132340"></a><a name="p19160762132340"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="58.89%" id="mcps1.2.4.1.3"><p id="p8860905132340"><a name="p8860905132340"></a><a name="p8860905132340"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row66469484132340"><td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.1 "><p id="p23038389132340"><a name="p23038389132340"></a><a name="p23038389132340"></a>firewall_policies</p>
</td>
<td class="cellrowborder" valign="top" width="17.78%" headers="mcps1.2.4.1.2 "><p id="p39042021132340"><a name="p39042021132340"></a><a name="p39042021132340"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="58.89%" headers="mcps1.2.4.1.3 "><p id="p50197883132340"><a name="p50197883132340"></a><a name="p50197883132340"></a>Specifies the firewall policy objects. For details, see <a href="#table17002720121127">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **Firewall Policy**  objects

<a name="table17002720121127"></a>
<table><thead align="left"><tr id="row16929792121127"><th class="cellrowborder" valign="top" width="32.083208320832085%" id="mcps1.2.4.1.1"><p id="p18873879121127"><a name="p18873879121127"></a><a name="p18873879121127"></a><strong id="b1188204513296"><a name="b1188204513296"></a><a name="b1188204513296"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="22.632263226322635%" id="mcps1.2.4.1.2"><p id="p12638309121127"><a name="p12638309121127"></a><a name="p12638309121127"></a><strong id="b1885612464296"><a name="b1885612464296"></a><a name="b1885612464296"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="45.28452845284529%" id="mcps1.2.4.1.3"><p id="p61199938121127"><a name="p61199938121127"></a><a name="p61199938121127"></a><strong id="b2576144719292"><a name="b2576144719292"></a><a name="b2576144719292"></a>Description</strong></p>
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
<td class="cellrowborder" valign="top" width="22.632263226322635%" headers="mcps1.2.4.1.2 "><p id="p122792241376"><a name="p122792241376"></a><a name="p122792241376"></a>Array of strings</p>
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
<td class="cellrowborder" valign="top" width="45.28452845284529%" headers="mcps1.2.4.1.3 "><p id="p763154142816"><a name="p763154142816"></a><a name="p763154142816"></a>Specifies the project ID. </p>
</td>
</tr>
</tbody>
</table>

## Example:<a name="section35216218132340"></a>

Example request

```
GET https://{Endpoint}/v2.0/fwaas/firewall_policies
```

Example response

```
{
    "firewall_policies": [
        {
            "description": "", 
            "firewall_rules": [
                "6c6803e0-ca8c-4aa9-afb3-4f89275b6c32"
            ], 
            "tenant_id": "23c8a121505047b6869edf39f3062712", 
            "public": false, 
            "id": "6b70e321-0c21-4b83-bb8a-a886d1414a5f", 
            "audited": false, 
            "name": "fwp1",
            "project_id": "23c8a121505047b6869edf39f3062712"
        }, 
        {
            "description": "", 
            "firewall_rules": [
                "6c6803e0-ca8c-4aa9-afb3-4f89275b6c32"
            ], 
            "tenant_id": "23c8a121505047b6869edf39f3062712", 
            "public": false, 
            "id": "fce92002-5a15-465d-aaca-9b44453bb738", 
            "audited": false, 
            "name": "fwp2",
            "project_id": "23c8a121505047b6869edf39f3062712"
        }
    ]
}
```

## Status Code<a name="section10470352390"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

