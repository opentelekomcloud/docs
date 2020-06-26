# Updating a Floating IP Address<a name="vpc_floatingiP_0004"></a>

## Function<a name="section6285365021641"></a>

This API is used to update a floating IP address.

During the update, the ID of the floating IP address must be provided in the URL.

If  **port\_id**  is left blank, the floating IP address has been unbound from the port.

Restrictions

When you bind a floating IP address, if the floating IP address is in the  **error**  state, try unbinding the address first.

You are not allowed to bind a floating IP address that has been bound to a port to another port. You must first unbind the IP address from its original port and bind it to the required port.

## URI<a name="section5206576221641"></a>

PUT /v2.0/floatingips/\{floatingip\_id\}

[Table 1](#table5388109319164)  describes the parameters.

**Table  1**  Parameter description

<a name="table5388109319164"></a>
<table><thead align="left"><tr id="row6462628919164"><th class="cellrowborder" valign="top" width="23.169999999999998%" id="mcps1.2.5.1.1"><p id="p23806019164"><a name="p23806019164"></a><a name="p23806019164"></a><strong id="b78917553286"><a name="b78917553286"></a><a name="b78917553286"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="11.66%" id="mcps1.2.5.1.2"><p id="p868823916540"><a name="p868823916540"></a><a name="p868823916540"></a><strong id="b119011056102810"><a name="b119011056102810"></a><a name="b119011056102810"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.28%" id="mcps1.2.5.1.3"><p id="p1928287519164"><a name="p1928287519164"></a><a name="p1928287519164"></a><strong id="b180005719282"><a name="b180005719282"></a><a name="b180005719282"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="44.89%" id="mcps1.2.5.1.4"><p id="p4943306019164"><a name="p4943306019164"></a><a name="p4943306019164"></a><strong id="b585785862817"><a name="b585785862817"></a><a name="b585785862817"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row316619519164"><td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.2.5.1.1 "><p id="p115515499553"><a name="p115515499553"></a><a name="p115515499553"></a>floatingip_id</p>
</td>
<td class="cellrowborder" valign="top" width="11.66%" headers="mcps1.2.5.1.2 "><p id="p0689103915411"><a name="p0689103915411"></a><a name="p0689103915411"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="20.28%" headers="mcps1.2.5.1.3 "><p id="p3677022419164"><a name="p3677022419164"></a><a name="p3677022419164"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.89%" headers="mcps1.2.5.1.4 "><p id="p2690811319164"><a name="p2690811319164"></a><a name="p2690811319164"></a>Specifies the floating IP address ID.</p>
<p id="p6641157838"><a name="p6641157838"></a><a name="p6641157838"></a>This parameter is not required when you assign a floating IP address. This parameter is mandatory when you query, update, or delete a floating IP address.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section2938074421641"></a>

**Table  2**  Request parameter

<a name="table3103003021641"></a>
<table><thead align="left"><tr id="row5907300221641"><th class="cellrowborder" valign="top" width="19.59%" id="mcps1.2.5.1.1"><p id="p2018384621641"><a name="p2018384621641"></a><a name="p2018384621641"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.03%" id="mcps1.2.5.1.2"><p id="p2427879021641"><a name="p2427879021641"></a><a name="p2427879021641"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="18.4%" id="mcps1.2.5.1.3"><p id="p2042494621641"><a name="p2042494621641"></a><a name="p2042494621641"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="45.98%" id="mcps1.2.5.1.4"><p id="p4380795521641"><a name="p4380795521641"></a><a name="p4380795521641"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row5878350521641"><td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.5.1.1 "><p id="p6384347521641"><a name="p6384347521641"></a><a name="p6384347521641"></a>floatingip</p>
</td>
<td class="cellrowborder" valign="top" width="16.03%" headers="mcps1.2.5.1.2 "><p id="p393901021641"><a name="p393901021641"></a><a name="p393901021641"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="18.4%" headers="mcps1.2.5.1.3 "><p id="p5062438921641"><a name="p5062438921641"></a><a name="p5062438921641"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.98%" headers="mcps1.2.5.1.4 "><p id="p557124874610"><a name="p557124874610"></a><a name="p557124874610"></a>Specifies the floating IP address list. For details, see <a href="#table547993685510">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **floatingip**  objects

<a name="table547993685510"></a>
<table><thead align="left"><tr id="row966719362553"><th class="cellrowborder" valign="top" width="19.878012198780123%" id="mcps1.2.5.1.1"><p id="p0685313416"><a name="p0685313416"></a><a name="p0685313416"></a><strong id="b14322115343414"><a name="b14322115343414"></a><a name="b14322115343414"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="12.938706129387059%" id="mcps1.2.5.1.2"><p id="p768561134110"><a name="p768561134110"></a><a name="p768561134110"></a><strong id="b3756754163410"><a name="b3756754163410"></a><a name="b3756754163410"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="12.84871512848715%" id="mcps1.2.5.1.3"><p id="p368681134120"><a name="p368681134120"></a><a name="p368681134120"></a><strong id="b85211556143419"><a name="b85211556143419"></a><a name="b85211556143419"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="54.334566543345666%" id="mcps1.2.5.1.4"><p id="p668612124119"><a name="p668612124119"></a><a name="p668612124119"></a><strong id="b12100759133410"><a name="b12100759133410"></a><a name="b12100759133410"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1667163613554"><td class="cellrowborder" valign="top" width="19.878012198780123%" headers="mcps1.2.5.1.1 "><p id="p1868717104113"><a name="p1868717104113"></a><a name="p1868717104113"></a>port_id</p>
</td>
<td class="cellrowborder" valign="top" width="12.938706129387059%" headers="mcps1.2.5.1.2 "><p id="p26871119419"><a name="p26871119419"></a><a name="p26871119419"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.84871512848715%" headers="mcps1.2.5.1.3 "><p id="p66889116414"><a name="p66889116414"></a><a name="p66889116414"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.334566543345666%" headers="mcps1.2.5.1.4 "><p id="p14688213413"><a name="p14688213413"></a><a name="p14688213413"></a>Specifies the port ID. </p>
</td>
</tr>
</tbody>
</table>

## Response Message<a name="section2485220121641"></a>

**Table  4**  Response parameter

<a name="table6687125821641"></a>
<table><thead align="left"><tr id="row2678790321641"><th class="cellrowborder" valign="top" width="21.349999999999998%" id="mcps1.2.4.1.1"><p id="p2233651921641"><a name="p2233651921641"></a><a name="p2233651921641"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.11%" id="mcps1.2.4.1.2"><p id="p6442759121641"><a name="p6442759121641"></a><a name="p6442759121641"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="59.540000000000006%" id="mcps1.2.4.1.3"><p id="p5780308921641"><a name="p5780308921641"></a><a name="p5780308921641"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row5153866721641"><td class="cellrowborder" valign="top" width="21.349999999999998%" headers="mcps1.2.4.1.1 "><p id="p1388252621641"><a name="p1388252621641"></a><a name="p1388252621641"></a>floatingip</p>
</td>
<td class="cellrowborder" valign="top" width="19.11%" headers="mcps1.2.4.1.2 "><p id="p5074280121641"><a name="p5074280121641"></a><a name="p5074280121641"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="59.540000000000006%" headers="mcps1.2.4.1.3 "><p id="p6355285621641"><a name="p6355285621641"></a><a name="p6355285621641"></a>Specifies the floating IP address list. For details, see <a href="#table8139247714">Table 5</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  5** **floatingip**  objects

<a name="table8139247714"></a>
<table><thead align="left"><tr id="row18132240714"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p101201250870"><a name="p101201250870"></a><a name="p101201250870"></a><strong id="b4848194719387"><a name="b4848194719387"></a><a name="b4848194719387"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p161211850674"><a name="p161211850674"></a><a name="p161211850674"></a><strong id="b5423951113817"><a name="b5423951113817"></a><a name="b5423951113817"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p41217502719"><a name="p41217502719"></a><a name="p41217502719"></a><strong id="b047975220387"><a name="b047975220387"></a><a name="b047975220387"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row2014192410713"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p6028218019164"><a name="p6028218019164"></a><a name="p6028218019164"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p5101843519164"><a name="p5101843519164"></a><a name="p5101843519164"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p6000412319164"><a name="p6000412319164"></a><a name="p6000412319164"></a>Specifies the floating IP address status. The value can be <strong id="b347325413814"><a name="b347325413814"></a><a name="b347325413814"></a>ACTIVE</strong>, <strong id="b547445453819"><a name="b547445453819"></a><a name="b547445453819"></a>DOWN</strong>, or <strong id="b19474135473816"><a name="b19474135473816"></a><a name="b19474135473816"></a>ERROR</strong>.</p>
<a name="ul10603143175810"></a><a name="ul10603143175810"></a><ul id="ul10603143175810"><li><strong id="b148291056183815"><a name="b148291056183815"></a><a name="b148291056183815"></a>DOWN</strong> indicates that the floating IP address has not been bound.</li><li><strong id="b105673119392"><a name="b105673119392"></a><a name="b105673119392"></a>ACTIVE</strong> indicates that the floating IP address has been bound.</li><li><strong id="b250519383917"><a name="b250519383917"></a><a name="b250519383917"></a>ERROR</strong> indicates that the floating IP address is abnormal. </li></ul>
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
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1395374115919"><a name="p1395374115919"></a><a name="p1395374115919"></a>Specifies the time (UTC) when the floating IP address is created.</p>
<p id="p2070141994713"><a name="p2070141994713"></a><a name="p2070141994713"></a>Format: <em id="i1163119166405"><a name="i1163119166405"></a><a name="i1163119166405"></a>yyyy-MM-ddTHH:mm:ss</em></p>
</td>
</tr>
<tr id="row1188246714"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p139719548912"><a name="p139719548912"></a><a name="p139719548912"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p53971154594"><a name="p53971154594"></a><a name="p53971154594"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1339713549918"><a name="p1339713549918"></a><a name="p1339713549918"></a>Specifies the time (UTC) when the floating IP address is updated.</p>
<p id="p137222218476"><a name="p137222218476"></a><a name="p137222218476"></a>Format: <em id="i64778275404"><a name="i64778275404"></a><a name="i64778275404"></a>yyyy-MM-ddTHH:mm:ss</em></p>
</td>
</tr>
</tbody>
</table>

## Example:<a name="section3510479621641"></a>

Example request 1 \(Binding a floating IP address to a port\)

```
PUT https://{Endpoint}/v2.0/floatingips/b997e0d4-3359-4c74-8f88-bc0af81cd5a2 
 
{
    "floatingip": {
           "port_id": "f91f5763-c5a2-4458-979d-61e48b3c3fac"
    }
}
```

Example response 1 \(Binding a floating IP address to a port\)

```
{
    "floatingip": {
        "id": "b997e0d4-3359-4c74-8f88-bc0af81cd5a2",
        "status": "DOWN",
        "router_id": null,
        "tenant_id": "bbfe8c41dd034a07bebd592bf03b4b0c",
        "project_id": "bbfe8c41dd034a07bebd592bf03b4b0c",
        "floating_network_id": "0a2228f2-7f8a-45f1-8e09-9039e1d09975",
        "fixed_ip_address": "192.168.10.3",
        "floating_ip_address": "88.88.215.205",
        "port_id": 00587256-27e3-489b-96bf-ea80c1da4aeb,
        "created_at": "2018-09-20T02:10:02",
        "updated_at": "2018-09-20T02:10:07"
    }
}
```

Example request 2 \(Unbinding a floating IP address from a port\)

```
PUT https://{Endpoint}/v2.0/floatingips/b997e0d4-3359-4c74-8f88-bc0af81cd5a2

{
    "floatingip": {
        "port_id": null
    }
}
```

Example response 2 \(Unbinding a floating IP address from a port\)

```
{
    "floatingip": {
        "id": "b997e0d4-3359-4c74-8f88-bc0af81cd5a2",
        "status": "DOWN",
        "router_id": null,
        "tenant_id": "bbfe8c41dd034a07bebd592bf03b4b0c",
        "project_id": "bbfe8c41dd034a07bebd592bf03b4b0c",
        "floating_network_id": "0a2228f2-7f8a-45f1-8e09-9039e1d09975",
        "fixed_ip_address": null,
        "floating_ip_address": "88.88.215.205",
        "port_id": null,
        "created_at": "2018-09-20T02:10:02",
        "updated_at": "2018-09-20T02:10:07"
    }
}
```

## Status Code<a name="section10470352390"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

