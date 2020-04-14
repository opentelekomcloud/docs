# Querying a Floating IP Address<a name="eip_openstackapi_0007"></a>

## Function<a name="en-us_topic_0201534072_section433032482159"></a>

This API is used to query details about a specified floating IP address, including the floating IP address status, ID of the router to which the floating IP address belongs, and external network ID of the floating IP address.

## URI<a name="en-us_topic_0201534072_section269019862159"></a>

GET /v2.0/floatingips/\{floatingip\_id\}

## Request Message<a name="en-us_topic_0201534072_section513321362159"></a>

None

## Response Message<a name="en-us_topic_0201534072_section414903182159"></a>

**Table  1**  Response parameter

<a name="en-us_topic_0201534072_table52726292159"></a>
<table><thead align="left"><tr id="en-us_topic_0201534072_row483206142159"><th class="cellrowborder" valign="top" width="21.349999999999998%" id="mcps1.2.4.1.1"><p id="en-us_topic_0201534072_p216556632159"><a name="en-us_topic_0201534072_p216556632159"></a><a name="en-us_topic_0201534072_p216556632159"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="8.99%" id="mcps1.2.4.1.2"><p id="en-us_topic_0201534072_p92783132159"><a name="en-us_topic_0201534072_p92783132159"></a><a name="en-us_topic_0201534072_p92783132159"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="69.66%" id="mcps1.2.4.1.3"><p id="en-us_topic_0201534072_p72773912159"><a name="en-us_topic_0201534072_p72773912159"></a><a name="en-us_topic_0201534072_p72773912159"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0201534072_row525977702159"><td class="cellrowborder" valign="top" width="21.349999999999998%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534072_p325609822159"><a name="en-us_topic_0201534072_p325609822159"></a><a name="en-us_topic_0201534072_p325609822159"></a>floatingip</p>
</td>
<td class="cellrowborder" valign="top" width="8.99%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534072_p201938822159"><a name="en-us_topic_0201534072_p201938822159"></a><a name="en-us_topic_0201534072_p201938822159"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="69.66%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534072_p191679172159"><a name="en-us_topic_0201534072_p191679172159"></a><a name="en-us_topic_0201534072_p191679172159"></a>Specifies the floating IP address list. For details, see <a href="#en-us_topic_0201534072_table8139247714">Table 2</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  2** **floatingip**  objects

<a name="en-us_topic_0201534072_table8139247714"></a>
<table><thead align="left"><tr id="en-us_topic_0201534072_row18132240714"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="en-us_topic_0201534072_p101201250870"><a name="en-us_topic_0201534072_p101201250870"></a><a name="en-us_topic_0201534072_p101201250870"></a><strong id="en-us_topic_0201534072_b883917243138"><a name="en-us_topic_0201534072_b883917243138"></a><a name="en-us_topic_0201534072_b883917243138"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="en-us_topic_0201534072_p161211850674"><a name="en-us_topic_0201534072_p161211850674"></a><a name="en-us_topic_0201534072_p161211850674"></a><strong id="en-us_topic_0201534072_b116546278139"><a name="en-us_topic_0201534072_b116546278139"></a><a name="en-us_topic_0201534072_b116546278139"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="en-us_topic_0201534072_p41217502719"><a name="en-us_topic_0201534072_p41217502719"></a><a name="en-us_topic_0201534072_p41217502719"></a><strong id="en-us_topic_0201534072_b1350518288137"><a name="en-us_topic_0201534072_b1350518288137"></a><a name="en-us_topic_0201534072_b1350518288137"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0201534072_row2014192410713"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534072_p6028218019164"><a name="en-us_topic_0201534072_p6028218019164"></a><a name="en-us_topic_0201534072_p6028218019164"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534072_p5101843519164"><a name="en-us_topic_0201534072_p5101843519164"></a><a name="en-us_topic_0201534072_p5101843519164"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534072_p6000412319164"><a name="en-us_topic_0201534072_p6000412319164"></a><a name="en-us_topic_0201534072_p6000412319164"></a>Specifies the floating IP address status. The value can be <strong id="en-us_topic_0201534072_b5686832141314"><a name="en-us_topic_0201534072_b5686832141314"></a><a name="en-us_topic_0201534072_b5686832141314"></a>ACTIVE</strong>, <strong id="en-us_topic_0201534072_b668614321137"><a name="en-us_topic_0201534072_b668614321137"></a><a name="en-us_topic_0201534072_b668614321137"></a>DOWN</strong>, or <strong id="en-us_topic_0201534072_b668723211135"><a name="en-us_topic_0201534072_b668723211135"></a><a name="en-us_topic_0201534072_b668723211135"></a>ERROR</strong>.</p>
<a name="en-us_topic_0201534072_ul10603143175810"></a><a name="en-us_topic_0201534072_ul10603143175810"></a><ul id="en-us_topic_0201534072_ul10603143175810"><li><strong id="en-us_topic_0201534072_b69115394136"><a name="en-us_topic_0201534072_b69115394136"></a><a name="en-us_topic_0201534072_b69115394136"></a>DOWN</strong> indicates that the floating IP address has not been bound.</li><li><strong id="en-us_topic_0201534072_b248155261312"><a name="en-us_topic_0201534072_b248155261312"></a><a name="en-us_topic_0201534072_b248155261312"></a>ACTIVE</strong> indicates that the floating IP address has been bound.</li><li><strong id="en-us_topic_0201534072_b1564525313138"><a name="en-us_topic_0201534072_b1564525313138"></a><a name="en-us_topic_0201534072_b1564525313138"></a>ERROR</strong> indicates that the floating IP address is abnormal. </li></ul>
</td>
</tr>
<tr id="en-us_topic_0201534072_row4141241070"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534072_p5513524919164"><a name="en-us_topic_0201534072_p5513524919164"></a><a name="en-us_topic_0201534072_p5513524919164"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534072_p212111505713"><a name="en-us_topic_0201534072_p212111505713"></a><a name="en-us_topic_0201534072_p212111505713"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534072_p4121850371"><a name="en-us_topic_0201534072_p4121850371"></a><a name="en-us_topic_0201534072_p4121850371"></a>Specifies the floating IP address ID.</p>
</td>
</tr>
<tr id="en-us_topic_0201534072_row614132416712"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534072_p1912112509713"><a name="en-us_topic_0201534072_p1912112509713"></a><a name="en-us_topic_0201534072_p1912112509713"></a>floating_ip_address</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534072_p11211850072"><a name="en-us_topic_0201534072_p11211850072"></a><a name="en-us_topic_0201534072_p11211850072"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534072_p16122205017713"><a name="en-us_topic_0201534072_p16122205017713"></a><a name="en-us_topic_0201534072_p16122205017713"></a>Specifies the floating IP address.</p>
</td>
</tr>
<tr id="en-us_topic_0201534072_row115102414717"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534072_p61223503712"><a name="en-us_topic_0201534072_p61223503712"></a><a name="en-us_topic_0201534072_p61223503712"></a>floating_network_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534072_p1812220507714"><a name="en-us_topic_0201534072_p1812220507714"></a><a name="en-us_topic_0201534072_p1812220507714"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534072_p16122550274"><a name="en-us_topic_0201534072_p16122550274"></a><a name="en-us_topic_0201534072_p16122550274"></a>Specifies the external network ID.</p>
</td>
</tr>
<tr id="en-us_topic_0201534072_row19155241277"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534072_p201223504719"><a name="en-us_topic_0201534072_p201223504719"></a><a name="en-us_topic_0201534072_p201223504719"></a>router_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534072_p1122155015714"><a name="en-us_topic_0201534072_p1122155015714"></a><a name="en-us_topic_0201534072_p1122155015714"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534072_p812212506713"><a name="en-us_topic_0201534072_p812212506713"></a><a name="en-us_topic_0201534072_p812212506713"></a>Specifies the ID of the belonged router.</p>
</td>
</tr>
<tr id="en-us_topic_0201534072_row101514247714"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534072_p412218502718"><a name="en-us_topic_0201534072_p412218502718"></a><a name="en-us_topic_0201534072_p412218502718"></a>port_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534072_p612213506716"><a name="en-us_topic_0201534072_p612213506716"></a><a name="en-us_topic_0201534072_p612213506716"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534072_p141228504716"><a name="en-us_topic_0201534072_p141228504716"></a><a name="en-us_topic_0201534072_p141228504716"></a>Specifies the port ID.</p>
</td>
</tr>
<tr id="en-us_topic_0201534072_row3164249715"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534072_p01237508720"><a name="en-us_topic_0201534072_p01237508720"></a><a name="en-us_topic_0201534072_p01237508720"></a>fixed_ip_address</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534072_p111239501770"><a name="en-us_topic_0201534072_p111239501770"></a><a name="en-us_topic_0201534072_p111239501770"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534072_p1712316501972"><a name="en-us_topic_0201534072_p1712316501972"></a><a name="en-us_topic_0201534072_p1712316501972"></a>Specifies the private IP address of the associated port.</p>
</td>
</tr>
<tr id="en-us_topic_0201534072_row21662416711"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534072_p812355018717"><a name="en-us_topic_0201534072_p812355018717"></a><a name="en-us_topic_0201534072_p812355018717"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534072_p612316509712"><a name="en-us_topic_0201534072_p612316509712"></a><a name="en-us_topic_0201534072_p612316509712"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534072_p10487112"><a name="en-us_topic_0201534072_p10487112"></a><a name="en-us_topic_0201534072_p10487112"></a>Specifies the project ID.</p>
<p id="en-us_topic_0201534072_p51231950174"><a name="en-us_topic_0201534072_p51231950174"></a><a name="en-us_topic_0201534072_p51231950174"></a></p>
</td>
</tr>
<tr id="en-us_topic_0201534072_row11176241720"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534072_p11222111885214"><a name="en-us_topic_0201534072_p11222111885214"></a><a name="en-us_topic_0201534072_p11222111885214"></a>dns_name</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534072_p122232018115215"><a name="en-us_topic_0201534072_p122232018115215"></a><a name="en-us_topic_0201534072_p122232018115215"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534072_p18223161825216"><a name="en-us_topic_0201534072_p18223161825216"></a><a name="en-us_topic_0201534072_p18223161825216"></a>Specifies the DNS name.</p>
</td>
</tr>
<tr id="en-us_topic_0201534072_row17174241670"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534072_p492133065713"><a name="en-us_topic_0201534072_p492133065713"></a><a name="en-us_topic_0201534072_p492133065713"></a>dns_domain</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534072_p16929300573"><a name="en-us_topic_0201534072_p16929300573"></a><a name="en-us_topic_0201534072_p16929300573"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534072_p3921230175711"><a name="en-us_topic_0201534072_p3921230175711"></a><a name="en-us_topic_0201534072_p3921230175711"></a>Specifies the DNS domain.</p>
</td>
</tr>
<tr id="en-us_topic_0201534072_row1418142410714"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534072_p1953114119914"><a name="en-us_topic_0201534072_p1953114119914"></a><a name="en-us_topic_0201534072_p1953114119914"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534072_p595318416919"><a name="en-us_topic_0201534072_p595318416919"></a><a name="en-us_topic_0201534072_p595318416919"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534072_p1395374115919"><a name="en-us_topic_0201534072_p1395374115919"></a><a name="en-us_topic_0201534072_p1395374115919"></a>Specifies the time when the floating IP address was created.</p>
<p id="en-us_topic_0201534072_p1232884613478"><a name="en-us_topic_0201534072_p1232884613478"></a><a name="en-us_topic_0201534072_p1232884613478"></a>UTC time is used.</p>
<p id="en-us_topic_0201534072_p2070141994713"><a name="en-us_topic_0201534072_p2070141994713"></a><a name="en-us_topic_0201534072_p2070141994713"></a>Format: <em id="en-us_topic_0201534072_i542193342011"><a name="en-us_topic_0201534072_i542193342011"></a><a name="en-us_topic_0201534072_i542193342011"></a>yyyy-MM-ddTHH:mm:ss</em></p>
</td>
</tr>
<tr id="en-us_topic_0201534072_row1188246714"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534072_p139719548912"><a name="en-us_topic_0201534072_p139719548912"></a><a name="en-us_topic_0201534072_p139719548912"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534072_p53971154594"><a name="en-us_topic_0201534072_p53971154594"></a><a name="en-us_topic_0201534072_p53971154594"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534072_p1339713549918"><a name="en-us_topic_0201534072_p1339713549918"></a><a name="en-us_topic_0201534072_p1339713549918"></a>Specifies the time when the floating IP address was updated.</p>
<p id="en-us_topic_0201534072_p876511114816"><a name="en-us_topic_0201534072_p876511114816"></a><a name="en-us_topic_0201534072_p876511114816"></a>UTC time is used.</p>
<p id="en-us_topic_0201534072_p137222218476"><a name="en-us_topic_0201534072_p137222218476"></a><a name="en-us_topic_0201534072_p137222218476"></a>Format: <em id="en-us_topic_0201534072_i149104882218"><a name="en-us_topic_0201534072_i149104882218"></a><a name="en-us_topic_0201534072_i149104882218"></a>yyyy-MM-ddTHH:mm:ss</em></p>
</td>
</tr>
</tbody>
</table>

## Example:<a name="en-us_topic_0201534072_section382935262159"></a>

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

## Status Code<a name="en-us_topic_0201534072_section10470352390"></a>

See  [Status Codes](status-codes.md#eip_api05_0001).

## Error Code<a name="en-us_topic_0201534072_section85821649202813"></a>

See  [Error Codes](error-codes.md#eip_api05_0002).

