# Updating a Firewall Policy<a name="vpc_firewall_0009"></a>

## Function<a name="section19593265132522"></a>

This API is used to update a firewall policy.

## URI<a name="section46147480132522"></a>

PUT /v2.0/fwaas/firewall\_policies/\{firewall\_policy\_id\}

## Request Message<a name="section36048911132522"></a>

**Table  1**  Request parameter

<a name="table8852370132522"></a>
<table><thead align="left"><tr id="row32357095132522"><th class="cellrowborder" valign="top" width="19.388061193880613%" id="mcps1.2.5.1.1"><p id="p45580669132522"><a name="p45580669132522"></a><a name="p45580669132522"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18.7981201879812%" id="mcps1.2.5.1.2"><p id="p51498842132522"><a name="p51498842132522"></a><a name="p51498842132522"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="18.95810418958104%" id="mcps1.2.5.1.3"><p id="p56072606132522"><a name="p56072606132522"></a><a name="p56072606132522"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="42.85571442855714%" id="mcps1.2.5.1.4"><p id="p6648170132522"><a name="p6648170132522"></a><a name="p6648170132522"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row64881628132522"><td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.2.5.1.1 "><p id="p14588437132522"><a name="p14588437132522"></a><a name="p14588437132522"></a>firewall_policy</p>
</td>
<td class="cellrowborder" valign="top" width="18.7981201879812%" headers="mcps1.2.5.1.2 "><p id="p52664630132522"><a name="p52664630132522"></a><a name="p52664630132522"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="18.95810418958104%" headers="mcps1.2.5.1.3 "><p id="p43844189132522"><a name="p43844189132522"></a><a name="p43844189132522"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.5.1.4 "><p id="p50197883132340"><a name="p50197883132340"></a><a name="p50197883132340"></a>Specifies the firewall policy objects. For details, see <a href="#table17002720121127">Table 2</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  2** **Firewall Policy**  objects

<a name="table17002720121127"></a>
<table><thead align="left"><tr id="row16929792121127"><th class="cellrowborder" valign="top" width="23.21%" id="mcps1.2.5.1.1"><p id="p18873879121127"><a name="p18873879121127"></a><a name="p18873879121127"></a><strong id="b1087743721713"><a name="b1087743721713"></a><a name="b1087743721713"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="13.98%" id="mcps1.2.5.1.2"><p id="p1187191018576"><a name="p1187191018576"></a><a name="p1187191018576"></a><strong id="b764633831718"><a name="b764633831718"></a><a name="b764633831718"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.93%" id="mcps1.2.5.1.3"><p id="p12638309121127"><a name="p12638309121127"></a><a name="p12638309121127"></a><strong id="b05891639121718"><a name="b05891639121718"></a><a name="b05891639121718"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="41.88%" id="mcps1.2.5.1.4"><p id="p61199938121127"><a name="p61199938121127"></a><a name="p61199938121127"></a><strong id="b192981540181716"><a name="b192981540181716"></a><a name="b192981540181716"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row9858171121127"><td class="cellrowborder" valign="top" width="23.21%" headers="mcps1.2.5.1.1 "><p id="p49865700121127"><a name="p49865700121127"></a><a name="p49865700121127"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="13.98%" headers="mcps1.2.5.1.2 "><p id="p287210165719"><a name="p287210165719"></a><a name="p287210165719"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.93%" headers="mcps1.2.5.1.3 "><p id="p6225460121127"><a name="p6225460121127"></a><a name="p6225460121127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="41.88%" headers="mcps1.2.5.1.4 "><p id="p40337147121127"><a name="p40337147121127"></a><a name="p40337147121127"></a>Specifies the name of the firewall policy.</p>
<p id="p1606122895617"><a name="p1606122895617"></a><a name="p1606122895617"></a>The value can contain a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row61803802121127"><td class="cellrowborder" valign="top" width="23.21%" headers="mcps1.2.5.1.1 "><p id="p39621949121127"><a name="p39621949121127"></a><a name="p39621949121127"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="13.98%" headers="mcps1.2.5.1.2 "><p id="p087191011575"><a name="p087191011575"></a><a name="p087191011575"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.93%" headers="mcps1.2.5.1.3 "><p id="p66053143121127"><a name="p66053143121127"></a><a name="p66053143121127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="41.88%" headers="mcps1.2.5.1.4 "><p id="p15357220121127"><a name="p15357220121127"></a><a name="p15357220121127"></a>Provides supplementary information about the firewall policy.</p>
<p id="p1267612575565"><a name="p1267612575565"></a><a name="p1267612575565"></a>The value can contain a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row33369184121127"><td class="cellrowborder" valign="top" width="23.21%" headers="mcps1.2.5.1.1 "><p id="p16940942121127"><a name="p16940942121127"></a><a name="p16940942121127"></a>firewall_rules</p>
</td>
<td class="cellrowborder" valign="top" width="13.98%" headers="mcps1.2.5.1.2 "><p id="p7871410165711"><a name="p7871410165711"></a><a name="p7871410165711"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.93%" headers="mcps1.2.5.1.3 "><p id="p27024915121127"><a name="p27024915121127"></a><a name="p27024915121127"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="41.88%" headers="mcps1.2.5.1.4 "><p id="p53455884121127"><a name="p53455884121127"></a><a name="p53455884121127"></a>Specifies the firewall rules referenced by the firewall policy.</p>
</td>
</tr>
<tr id="row717167121127"><td class="cellrowborder" valign="top" width="23.21%" headers="mcps1.2.5.1.1 "><p id="p30704110121127"><a name="p30704110121127"></a><a name="p30704110121127"></a>audited</p>
</td>
<td class="cellrowborder" valign="top" width="13.98%" headers="mcps1.2.5.1.2 "><p id="p17871310145717"><a name="p17871310145717"></a><a name="p17871310145717"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.93%" headers="mcps1.2.5.1.3 "><p id="p10804884121127"><a name="p10804884121127"></a><a name="p10804884121127"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="41.88%" headers="mcps1.2.5.1.4 "><p id="p3925300121127"><a name="p3925300121127"></a><a name="p3925300121127"></a>Specifies the audit flag.</p>
<p id="p172123197567"><a name="p172123197567"></a><a name="p172123197567"></a>The value can be <strong id="b12839191619228"><a name="b12839191619228"></a><a name="b12839191619228"></a>true</strong> or <strong id="b16840161613221"><a name="b16840161613221"></a><a name="b16840161613221"></a>false</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Response Message<a name="section41558848132522"></a>

**Table  3**  Response parameter

<a name="table35154237132522"></a>
<table><thead align="left"><tr id="row52261665132522"><th class="cellrowborder" valign="top" width="23.169999999999998%" id="mcps1.2.4.1.1"><p id="p65769625132522"><a name="p65769625132522"></a><a name="p65769625132522"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25.61%" id="mcps1.2.4.1.2"><p id="p12018727132522"><a name="p12018727132522"></a><a name="p12018727132522"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51.22%" id="mcps1.2.4.1.3"><p id="p17036810132522"><a name="p17036810132522"></a><a name="p17036810132522"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row43204254132522"><td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p40260041132522"><a name="p40260041132522"></a><a name="p40260041132522"></a>firewall_policy</p>
</td>
<td class="cellrowborder" valign="top" width="25.61%" headers="mcps1.2.4.1.2 "><p id="p26565290132522"><a name="p26565290132522"></a><a name="p26565290132522"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.2.4.1.3 "><p id="p59164179132522"><a name="p59164179132522"></a><a name="p59164179132522"></a>Specifies the firewall policy objects. For details, see <a href="#table6763048152111">Table 4</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **Firewall Policy**  objects

<a name="table6763048152111"></a>
<table><thead align="left"><tr id="row18764194892115"><th class="cellrowborder" valign="top" width="32.083208320832085%" id="mcps1.2.4.1.1"><p id="p3764194815213"><a name="p3764194815213"></a><a name="p3764194815213"></a><strong id="b128516206257"><a name="b128516206257"></a><a name="b128516206257"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="22.632263226322635%" id="mcps1.2.4.1.2"><p id="p876474817212"><a name="p876474817212"></a><a name="p876474817212"></a><strong id="b139481921202520"><a name="b139481921202520"></a><a name="b139481921202520"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="45.28452845284529%" id="mcps1.2.4.1.3"><p id="p1876484815214"><a name="p1876484815214"></a><a name="p1876484815214"></a><strong id="b16746822172514"><a name="b16746822172514"></a><a name="b16746822172514"></a>Description</strong></p>
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
<tr id="row376464814211"><td class="cellrowborder" valign="top" width="32.083208320832085%" headers="mcps1.2.4.1.1 "><p id="p19764204872112"><a name="p19764204872112"></a><a name="p19764204872112"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="22.632263226322635%" headers="mcps1.2.4.1.2 "><p id="p2764154815210"><a name="p2764154815210"></a><a name="p2764154815210"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.28452845284529%" headers="mcps1.2.4.1.3 "><p id="p676474842118"><a name="p676474842118"></a><a name="p676474842118"></a>Specifies the name of the firewall policy.</p>
</td>
</tr>
<tr id="row5764144892115"><td class="cellrowborder" valign="top" width="32.083208320832085%" headers="mcps1.2.4.1.1 "><p id="p476424842118"><a name="p476424842118"></a><a name="p476424842118"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="22.632263226322635%" headers="mcps1.2.4.1.2 "><p id="p147654481219"><a name="p147654481219"></a><a name="p147654481219"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.28452845284529%" headers="mcps1.2.4.1.3 "><p id="p18765204812117"><a name="p18765204812117"></a><a name="p18765204812117"></a>Provides supplementary information about the firewall policy.</p>
</td>
</tr>
<tr id="row3765184815214"><td class="cellrowborder" valign="top" width="32.083208320832085%" headers="mcps1.2.4.1.1 "><p id="p11765848162113"><a name="p11765848162113"></a><a name="p11765848162113"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="22.632263226322635%" headers="mcps1.2.4.1.2 "><p id="p4765548162116"><a name="p4765548162116"></a><a name="p4765548162116"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.28452845284529%" headers="mcps1.2.4.1.3 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row7766248182119"><td class="cellrowborder" valign="top" width="32.083208320832085%" headers="mcps1.2.4.1.1 "><p id="p376624822116"><a name="p376624822116"></a><a name="p376624822116"></a>firewall_rules</p>
</td>
<td class="cellrowborder" valign="top" width="22.632263226322635%" headers="mcps1.2.4.1.2 "><p id="p2070691313818"><a name="p2070691313818"></a><a name="p2070691313818"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="45.28452845284529%" headers="mcps1.2.4.1.3 "><p id="p076694811218"><a name="p076694811218"></a><a name="p076694811218"></a>Specifies the firewall rules referenced by the firewall policy.</p>
</td>
</tr>
<tr id="row376664817218"><td class="cellrowborder" valign="top" width="32.083208320832085%" headers="mcps1.2.4.1.1 "><p id="p1376624892119"><a name="p1376624892119"></a><a name="p1376624892119"></a>audited</p>
</td>
<td class="cellrowborder" valign="top" width="22.632263226322635%" headers="mcps1.2.4.1.2 "><p id="p197661748132118"><a name="p197661748132118"></a><a name="p197661748132118"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="45.28452845284529%" headers="mcps1.2.4.1.3 "><p id="p1676694811214"><a name="p1676694811214"></a><a name="p1676694811214"></a>Specifies the audit flag.</p>
</td>
</tr>
<tr id="row1976619489210"><td class="cellrowborder" valign="top" width="32.083208320832085%" headers="mcps1.2.4.1.1 "><p id="p1376694818214"><a name="p1376694818214"></a><a name="p1376694818214"></a>public</p>
</td>
<td class="cellrowborder" valign="top" width="22.632263226322635%" headers="mcps1.2.4.1.2 "><p id="p576634816213"><a name="p576634816213"></a><a name="p576634816213"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="45.28452845284529%" headers="mcps1.2.4.1.3 "><p id="p19766748192115"><a name="p19766748192115"></a><a name="p19766748192115"></a>Specifies whether the firewall policy can be shared by different tenants.</p>
</td>
</tr>
<tr id="row109594223354"><td class="cellrowborder" valign="top" width="32.083208320832085%" headers="mcps1.2.4.1.1 "><p id="p870051413911"><a name="p870051413911"></a><a name="p870051413911"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="22.632263226322635%" headers="mcps1.2.4.1.2 "><p id="p17700201411911"><a name="p17700201411911"></a><a name="p17700201411911"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.28452845284529%" headers="mcps1.2.4.1.3 "><p id="p28021558142812"><a name="p28021558142812"></a><a name="p28021558142812"></a>Specifies the project ID. </p>
</td>
</tr>
</tbody>
</table>

## Example:<a name="section41774729132522"></a>

Example request

```
PUT https://{Endpoint}/v2.0/fwaas/firewall_policies/2fb0e81f-9f63-44b2-9894-c13a3284594a 

{
    "firewall_policy": {
        "firewall_rules": [
            "0f82b221-8cd6-44bd-9dfc-0e118fa7b6b1"
        ]
    }
}
```

Example response

```
{
    "firewall_policy": {
        "description": "", 
        "firewall_rules": [
            "0f82b221-8cd6-44bd-9dfc-0e118fa7b6b1"
        ], 
        "tenant_id": "23c8a121505047b6869edf39f3062712", 
        "public": false, 
        "id": "2fb0e81f-9f63-44b2-9894-c13a3284594a", 
        "audited": false, 
        "name": "test-policy",
        "project_id": "23c8a121505047b6869edf39f3062712"
    }
}
```

## Status Code<a name="section10470352390"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

