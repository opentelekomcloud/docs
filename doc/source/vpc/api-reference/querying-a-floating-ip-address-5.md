# Querying a Floating IP Address<a name="vpc_floatingiP_0002"></a>

## Function<a name="section433032482159"></a>

This API is used to query details about a specified floating IP address, including the floating IP address status, ID of the router to which the floating IP address belongs, and external network ID of the floating IP address.

## URI<a name="section269019862159"></a>

GET /v2.0/floatingips/\{floatingip\_id\}

## Request Message<a name="section513321362159"></a>

None

## Response Message<a name="section414903182159"></a>

**Table  1**  Response parameter

<a name="table52726292159"></a>
<table><thead align="left"><tr id="row483206142159"><th class="cellrowborder" valign="top" width="21.349999999999998%" id="mcps1.2.4.1.1"><p id="p216556632159"><a name="p216556632159"></a><a name="p216556632159"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="8.99%" id="mcps1.2.4.1.2"><p id="p92783132159"><a name="p92783132159"></a><a name="p92783132159"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="69.66%" id="mcps1.2.4.1.3"><p id="p72773912159"><a name="p72773912159"></a><a name="p72773912159"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row525977702159"><td class="cellrowborder" valign="top" width="21.349999999999998%" headers="mcps1.2.4.1.1 "><p id="p325609822159"><a name="p325609822159"></a><a name="p325609822159"></a>floatingip</p>
</td>
<td class="cellrowborder" valign="top" width="8.99%" headers="mcps1.2.4.1.2 "><p id="p201938822159"><a name="p201938822159"></a><a name="p201938822159"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="69.66%" headers="mcps1.2.4.1.3 "><p id="p191679172159"><a name="p191679172159"></a><a name="p191679172159"></a>Specifies the floating IP address list. For details, see <a href="#table8139247714">Table 2</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  2** **floatingip**  objects

<a name="table8139247714"></a>
<table><thead align="left"><tr id="row18132240714"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p101201250870"><a name="p101201250870"></a><a name="p101201250870"></a><strong id="b883917243138"><a name="b883917243138"></a><a name="b883917243138"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p161211850674"><a name="p161211850674"></a><a name="p161211850674"></a><strong id="b116546278139"><a name="b116546278139"></a><a name="b116546278139"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p41217502719"><a name="p41217502719"></a><a name="p41217502719"></a><strong id="b1350518288137"><a name="b1350518288137"></a><a name="b1350518288137"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row2014192410713"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p6028218019164"><a name="p6028218019164"></a><a name="p6028218019164"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p5101843519164"><a name="p5101843519164"></a><a name="p5101843519164"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p6000412319164"><a name="p6000412319164"></a><a name="p6000412319164"></a>Specifies the floating IP address status. The value can be <strong id="b5686832141314"><a name="b5686832141314"></a><a name="b5686832141314"></a>ACTIVE</strong>, <strong id="b668614321137"><a name="b668614321137"></a><a name="b668614321137"></a>DOWN</strong>, or <strong id="b668723211135"><a name="b668723211135"></a><a name="b668723211135"></a>ERROR</strong>.</p>
<a name="ul10603143175810"></a><a name="ul10603143175810"></a><ul id="ul10603143175810"><li><strong id="b69115394136"><a name="b69115394136"></a><a name="b69115394136"></a>DOWN</strong> indicates that the floating IP address has not been bound.</li><li><strong id="b248155261312"><a name="b248155261312"></a><a name="b248155261312"></a>ACTIVE</strong> indicates that the floating IP address has been bound.</li><li><strong id="b1564525313138"><a name="b1564525313138"></a><a name="b1564525313138"></a>ERROR</strong> indicates that the floating IP address is abnormal. </li></ul>
</td>
</tr>
<tr id="row4141241070"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p5513524919164"><a name="p5513524919164"></a><a name="p5513524919164"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p212111505713"><a name="p212111505713"></a><a name="p212111505713"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p4121850371"><a name="p4121850371"></a><a name="p4121850371"></a>Specifies the floating IP address ID.</p>
</td>
</tr>
<tr id="row614132416712"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1912112509713"><a name="p1912112509713"></a><a name="p1912112509713"></a>floating_ip_address</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p11211850072"><a name="p11211850072"></a><a name="p11211850072"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p16122205017713"><a name="p16122205017713"></a><a name="p16122205017713"></a>Specifies the floating IP address.</p>
</td>
</tr>
<tr id="row115102414717"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p61223503712"><a name="p61223503712"></a><a name="p61223503712"></a>floating_network_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1812220507714"><a name="p1812220507714"></a><a name="p1812220507714"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p16122550274"><a name="p16122550274"></a><a name="p16122550274"></a>Specifies the external network ID.</p>
</td>
</tr>
<tr id="row19155241277"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p201223504719"><a name="p201223504719"></a><a name="p201223504719"></a>router_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1122155015714"><a name="p1122155015714"></a><a name="p1122155015714"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p812212506713"><a name="p812212506713"></a><a name="p812212506713"></a>Specifies the ID of the belonged router.</p>
</td>
</tr>
<tr id="row101514247714"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p412218502718"><a name="p412218502718"></a><a name="p412218502718"></a>port_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p612213506716"><a name="p612213506716"></a><a name="p612213506716"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p141228504716"><a name="p141228504716"></a><a name="p141228504716"></a>Specifies the port ID.</p>
</td>
</tr>
<tr id="row3164249715"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p01237508720"><a name="p01237508720"></a><a name="p01237508720"></a>fixed_ip_address</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p111239501770"><a name="p111239501770"></a><a name="p111239501770"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1712316501972"><a name="p1712316501972"></a><a name="p1712316501972"></a>Specifies the private IP address of the associated port.</p>
</td>
</tr>
<tr id="row21662416711"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p812355018717"><a name="p812355018717"></a><a name="p812355018717"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p612316509712"><a name="p612316509712"></a><a name="p612316509712"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID.</p>
<p id="p51231950174"><a name="p51231950174"></a><a name="p51231950174"></a></p>
</td>
</tr>
<tr id="row11176241720"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p11222111885214"><a name="p11222111885214"></a><a name="p11222111885214"></a>dns_name</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p122232018115215"><a name="p122232018115215"></a><a name="p122232018115215"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p18223161825216"><a name="p18223161825216"></a><a name="p18223161825216"></a>Specifies the DNS name.</p>
</td>
</tr>
<tr id="row17174241670"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p492133065713"><a name="p492133065713"></a><a name="p492133065713"></a>dns_domain</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p16929300573"><a name="p16929300573"></a><a name="p16929300573"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p3921230175711"><a name="p3921230175711"></a><a name="p3921230175711"></a>Specifies the DNS domain.</p>
</td>
</tr>
<tr id="row1418142410714"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1953114119914"><a name="p1953114119914"></a><a name="p1953114119914"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p595318416919"><a name="p595318416919"></a><a name="p595318416919"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1395374115919"><a name="p1395374115919"></a><a name="p1395374115919"></a>Specifies the time when the floating IP address was created.</p>
<p id="p1232884613478"><a name="p1232884613478"></a><a name="p1232884613478"></a>UTC time is used.</p>
<p id="p2070141994713"><a name="p2070141994713"></a><a name="p2070141994713"></a>Format: <em id="i542193342011"><a name="i542193342011"></a><a name="i542193342011"></a>yyyy-MM-ddTHH:mm:ss</em></p>
</td>
</tr>
<tr id="row1188246714"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p139719548912"><a name="p139719548912"></a><a name="p139719548912"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p53971154594"><a name="p53971154594"></a><a name="p53971154594"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1339713549918"><a name="p1339713549918"></a><a name="p1339713549918"></a>Specifies the time when the floating IP address was updated.</p>
<p id="p876511114816"><a name="p876511114816"></a><a name="p876511114816"></a>UTC time is used.</p>
<p id="p137222218476"><a name="p137222218476"></a><a name="p137222218476"></a>Format: <em id="i149104882218"><a name="i149104882218"></a><a name="i149104882218"></a>yyyy-MM-ddTHH:mm:ss</em></p>
</td>
</tr>
</tbody>
</table>

## Example:<a name="section382935262159"></a>

Example request

```
GET https://{Endpoint}/v2.0/floatingips/1a3a2818-d9b4-4a9c-8a19-5252c499d1cd
```

Example response

```
{
    "floatingip": {
        "id": "1a3a2818-d9b4-4a9c-8a19-5252c499d1cd",
        "status": "DOWN",
        "router_id": null,
        "tenant_id": "bbfe8c41dd034a07bebd592bf03b4b0c",
        "project_id": "bbfe8c41dd034a07bebd592bf03b4b0c",
        "floating_network_id": "0a2228f2-7f8a-45f1-8e09-9039e1d09975",
        "fixed_ip_address": null,
        "floating_ip_address": "99.99.99.84",
        "port_id": null,
        "created_at": "2017-10-19T12:21:28",
        "updated_at": "2018-07-30T12:52:13"
    }
}
```

## Status Code<a name="section10470352390"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

