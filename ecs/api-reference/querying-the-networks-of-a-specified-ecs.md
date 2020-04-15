# Querying the Networks of a Specified ECS<a name="EN-US_TOPIC_0031169058"></a>

## Function<a name="section53922917165259"></a>

This API is used to query the networks of an ECS.

## Constraints<a name="section64211377173223"></a>

None

## URI<a name="section51121191165259"></a>

GET /v2/\{project\_id\}/servers/\{server\_id\}/ips

GET /v2.1/\{project\_id\}/servers/\{server\_id\}/ips

[Table 1](#table60562285165259)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table60562285165259"></a>
<table><thead align="left"><tr id="row4861884165259"><th class="cellrowborder" valign="top" width="16.6%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.349999999999998%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="66.05%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row63809876165259"><td class="cellrowborder" valign="top" width="16.6%" headers="mcps1.2.4.1.1 "><p id="p1217433165259"><a name="p1217433165259"></a><a name="p1217433165259"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p31503226165259"><a name="p31503226165259"></a><a name="p31503226165259"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.05%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row14620905165259"><td class="cellrowborder" valign="top" width="16.6%" headers="mcps1.2.4.1.1 "><p id="p43442641165259"><a name="p43442641165259"></a><a name="p43442641165259"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p29193009165259"><a name="p29193009165259"></a><a name="p29193009165259"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.05%" headers="mcps1.2.4.1.3 "><p id="p15823538165259"><a name="p15823538165259"></a><a name="p15823538165259"></a>Specifies the ECS ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section8194118165259"></a>

None

## Response<a name="section58140617165259"></a>

[Table 2](#table53480673143936)  describes the response parameters.

**Table  2**  Response parameters

<a name="table53480673143936"></a>
<table><thead align="left"><tr id="row28382388143936"><th class="cellrowborder" valign="top" width="18.75%" id="mcps1.2.5.1.1"><p id="p17272131143936"><a name="p17272131143936"></a><a name="p17272131143936"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.4%" id="mcps1.2.5.1.2"><p id="p5907101717224"><a name="p5907101717224"></a><a name="p5907101717224"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15.629999999999999%" id="mcps1.2.5.1.3"><p id="p56865403143936"><a name="p56865403143936"></a><a name="p56865403143936"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="48.22%" id="mcps1.2.5.1.4"><p id="p35736067143936"><a name="p35736067143936"></a><a name="p35736067143936"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row8940324143936"><td class="cellrowborder" valign="top" width="18.75%" headers="mcps1.2.5.1.1 "><p id="p53077645143936"><a name="p53077645143936"></a><a name="p53077645143936"></a>addresses</p>
</td>
<td class="cellrowborder" valign="top" width="17.4%" headers="mcps1.2.5.1.2 "><p id="p390718172226"><a name="p390718172226"></a><a name="p390718172226"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.629999999999999%" headers="mcps1.2.5.1.3 "><p id="p4322023143936"><a name="p4322023143936"></a><a name="p4322023143936"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="48.22%" headers="mcps1.2.5.1.4 "><p id="p36857741143936"><a name="p36857741143936"></a><a name="p36857741143936"></a>Specifies the ECS network information.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **addresses**  parameter structure description

<a name="table56891490143956"></a>
<table><thead align="left"><tr id="row33903869143956"><th class="cellrowborder" valign="top" width="18.77812218778122%" id="mcps1.2.5.1.1"><p id="p4503028171311"><a name="p4503028171311"></a><a name="p4503028171311"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.308269173082692%" id="mcps1.2.5.1.2"><p id="p107641620192214"><a name="p107641620192214"></a><a name="p107641620192214"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15.688431156884313%" id="mcps1.2.5.1.3"><p id="p1150310281135"><a name="p1150310281135"></a><a name="p1150310281135"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="48.22517748225177%" id="mcps1.2.5.1.4"><p id="p205181728131313"><a name="p205181728131313"></a><a name="p205181728131313"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row33776430143956"><td class="cellrowborder" valign="top" width="18.77812218778122%" headers="mcps1.2.5.1.1 "><p id="p51536339143956"><a name="p51536339143956"></a><a name="p51536339143956"></a>Name of the network where the ECS accesses</p>
</td>
<td class="cellrowborder" valign="top" width="17.308269173082692%" headers="mcps1.2.5.1.2 "><p id="p8764182011227"><a name="p8764182011227"></a><a name="p8764182011227"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.688431156884313%" headers="mcps1.2.5.1.3 "><p id="p13693953143956"><a name="p13693953143956"></a><a name="p13693953143956"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="48.22517748225177%" headers="mcps1.2.5.1.4 "><p id="p54366741143956"><a name="p54366741143956"></a><a name="p54366741143956"></a>Specifies the network where the ECS accesses. For details about the network, see <a href="#table22651992144025">Table 4</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4**  ECS network parameter structure description

<a name="table22651992144025"></a>
<table><thead align="left"><tr id="row15576094144025"><th class="cellrowborder" valign="top" width="14.85148514851485%" id="mcps1.2.7.1.1"><p id="p53704088144025"><a name="p53704088144025"></a><a name="p53704088144025"></a>Attribute</p>
</th>
<th class="cellrowborder" valign="top" width="9.770977097709771%" id="mcps1.2.7.1.2"><p id="p55063891144025"><a name="p55063891144025"></a><a name="p55063891144025"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="10.911091109110911%" id="mcps1.2.7.1.3"><p id="p30990199144025"><a name="p30990199144025"></a><a name="p30990199144025"></a>CRUD</p>
</th>
<th class="cellrowborder" valign="top" width="12.411241124112411%" id="mcps1.2.7.1.4"><p id="p27178154144025"><a name="p27178154144025"></a><a name="p27178154144025"></a>Default Value</p>
</th>
<th class="cellrowborder" valign="top" width="15.981598159815983%" id="mcps1.2.7.1.5"><p id="p53946903144025"><a name="p53946903144025"></a><a name="p53946903144025"></a>Constraint</p>
</th>
<th class="cellrowborder" valign="top" width="36.07360736073608%" id="mcps1.2.7.1.6"><p id="p7623012144025"><a name="p7623012144025"></a><a name="p7623012144025"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row1498246144025"><td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.7.1.1 "><p id="p54249095144025"><a name="p54249095144025"></a><a name="p54249095144025"></a>version</p>
</td>
<td class="cellrowborder" valign="top" width="9.770977097709771%" headers="mcps1.2.7.1.2 "><p id="p32100540144025"><a name="p32100540144025"></a><a name="p32100540144025"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="10.911091109110911%" headers="mcps1.2.7.1.3 "><p id="p50006925144025"><a name="p50006925144025"></a><a name="p50006925144025"></a>R</p>
</td>
<td class="cellrowborder" valign="top" width="12.411241124112411%" headers="mcps1.2.7.1.4 "><p id="p24029156144025"><a name="p24029156144025"></a><a name="p24029156144025"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="15.981598159815983%" headers="mcps1.2.7.1.5 "><p id="p204582144025"><a name="p204582144025"></a><a name="p204582144025"></a>4 or 6</p>
</td>
<td class="cellrowborder" valign="top" width="36.07360736073608%" headers="mcps1.2.7.1.6 "><p id="p16571197144025"><a name="p16571197144025"></a><a name="p16571197144025"></a>Specifies the IP address version. The value of this parameter can be <strong id="b50100560143815"><a name="b50100560143815"></a><a name="b50100560143815"></a>4</strong> or <strong id="b62274100143818"><a name="b62274100143818"></a><a name="b62274100143818"></a>6</strong>.</p>
</td>
</tr>
<tr id="row14923052144025"><td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.7.1.1 "><p id="p807709144025"><a name="p807709144025"></a><a name="p807709144025"></a>addr</p>
</td>
<td class="cellrowborder" valign="top" width="9.770977097709771%" headers="mcps1.2.7.1.2 "><p id="p65424470144025"><a name="p65424470144025"></a><a name="p65424470144025"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="10.911091109110911%" headers="mcps1.2.7.1.3 "><p id="p64890752144025"><a name="p64890752144025"></a><a name="p64890752144025"></a>R</p>
</td>
<td class="cellrowborder" valign="top" width="12.411241124112411%" headers="mcps1.2.7.1.4 "><p id="p21659587144025"><a name="p21659587144025"></a><a name="p21659587144025"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="15.981598159815983%" headers="mcps1.2.7.1.5 "><p id="p9596102144025"><a name="p9596102144025"></a><a name="p9596102144025"></a>IP address format</p>
</td>
<td class="cellrowborder" valign="top" width="36.07360736073608%" headers="mcps1.2.7.1.6 "><p id="p39086769144025"><a name="p39086769144025"></a><a name="p39086769144025"></a>Specifies the IP address.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="section852143516136"></a>

```
GET https://{endpoint}/v2/{project_id}/servers/{server_id}/ips
GET https://{endpoint}/v2.1/{project_id}/servers/{server_id}/ips
```

## Example Response<a name="section101711934134020"></a>

```
{
    "addresses": {
        "demo_net": [
            {
                "version": 4,
                "addr": "10.0.0.4"
            },
            {
                "version": 4,
                "addr": "192.150.73.132"
            }
        ],
        "private_net": [
            {
                "version": 4,
                "addr": "10.176.42.16"
            },
            {
                "version": 6,
                "addr": "::babe:10.176.42.16"
            }
        ]
    }
}
```

## Returned Values<a name="section38817202165259"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

