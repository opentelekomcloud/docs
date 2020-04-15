# Querying ECS NICs<a name="EN-US_TOPIC_0020212661"></a>

## Function<a name="section36073588"></a>

This API is used to query information about ECS NICs.

## URI<a name="section56226836"></a>

GET /v2/\{project\_id\}/servers/\{server\_id\}/os-interface

GET /v2.1/\{project\_id\}/servers/\{server\_id\}/os-interface

[Table 1](#table38523909)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table38523909"></a>
<table><thead align="left"><tr id="row15247616"><th class="cellrowborder" valign="top" width="16.61%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.54%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.85%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row23712525"><td class="cellrowborder" valign="top" width="16.61%" headers="mcps1.2.4.1.1 "><p id="p41666396"><a name="p41666396"></a><a name="p41666396"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.54%" headers="mcps1.2.4.1.2 "><p id="p19534911"><a name="p19534911"></a><a name="p19534911"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.85%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row45459464114812"><td class="cellrowborder" valign="top" width="16.61%" headers="mcps1.2.4.1.1 "><p id="p6481999114812"><a name="p6481999114812"></a><a name="p6481999114812"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.54%" headers="mcps1.2.4.1.2 "><p id="p55279920114812"><a name="p55279920114812"></a><a name="p55279920114812"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.85%" headers="mcps1.2.4.1.3 "><p id="p48488537114812"><a name="p48488537114812"></a><a name="p48488537114812"></a>Specifies the ECS ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section36279478"></a>

None

## Response<a name="section58079852"></a>

[Table 2](#table25276401)  describes the response parameters.

**Table  2**  Response parameters

<a name="table25276401"></a>
<table><thead align="left"><tr id="row30840926"><th class="cellrowborder" valign="top" width="16.57%" id="mcps1.2.4.1.1"><p id="p137113478283"><a name="p137113478283"></a><a name="p137113478283"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15.440000000000001%" id="mcps1.2.4.1.2"><p id="p748676"><a name="p748676"></a><a name="p748676"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="67.99%" id="mcps1.2.4.1.3"><p id="p60642794"><a name="p60642794"></a><a name="p60642794"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row13119252"><td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.2.4.1.1 "><p id="p56026474"><a name="p56026474"></a><a name="p56026474"></a>interfaceAttachments</p>
</td>
<td class="cellrowborder" valign="top" width="15.440000000000001%" headers="mcps1.2.4.1.2 "><p id="p34453949"><a name="p34453949"></a><a name="p34453949"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="67.99%" headers="mcps1.2.4.1.3 "><p id="p18214233"><a name="p18214233"></a><a name="p18214233"></a>Specifies ECS NICs. For details, see <a href="#table49805933">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **interfaceAttachments**  field description

<a name="table49805933"></a>
<table><thead align="left"><tr id="row9026257"><th class="cellrowborder" valign="top" width="16.42%" id="mcps1.2.4.1.1"><p id="p0275155662814"><a name="p0275155662814"></a><a name="p0275155662814"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15.479999999999999%" id="mcps1.2.4.1.2"><p id="p15275145672813"><a name="p15275145672813"></a><a name="p15275145672813"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="68.10000000000001%" id="mcps1.2.4.1.3"><p id="p182751256102814"><a name="p182751256102814"></a><a name="p182751256102814"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row10727144"><td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.1 "><p id="p63592346"><a name="p63592346"></a><a name="p63592346"></a>port_state</p>
</td>
<td class="cellrowborder" valign="top" width="15.479999999999999%" headers="mcps1.2.4.1.2 "><p id="p13579756"><a name="p13579756"></a><a name="p13579756"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="68.10000000000001%" headers="mcps1.2.4.1.3 "><p id="p34639550"><a name="p34639550"></a><a name="p34639550"></a>Specifies the NIC port status.</p>
</td>
</tr>
<tr id="row43320496"><td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.1 "><p id="p19299281"><a name="p19299281"></a><a name="p19299281"></a>fixed_ips</p>
</td>
<td class="cellrowborder" valign="top" width="15.479999999999999%" headers="mcps1.2.4.1.2 "><p id="p55265559"><a name="p55265559"></a><a name="p55265559"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="68.10000000000001%" headers="mcps1.2.4.1.3 "><p id="p23274750"><a name="p23274750"></a><a name="p23274750"></a>Specifies private IP addresses for NICs. For details, see <a href="#table19750463">Table 4</a>.</p>
</td>
</tr>
<tr id="row8146160"><td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.1 "><p id="p55859239"><a name="p55859239"></a><a name="p55859239"></a>net_id</p>
</td>
<td class="cellrowborder" valign="top" width="15.479999999999999%" headers="mcps1.2.4.1.2 "><p id="p10966323"><a name="p10966323"></a><a name="p10966323"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="68.10000000000001%" headers="mcps1.2.4.1.3 "><p id="p8495130"><a name="p8495130"></a><a name="p8495130"></a>Specifies the network ID to which the NIC port belongs.</p>
</td>
</tr>
<tr id="row9347313"><td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.1 "><p id="p18934887"><a name="p18934887"></a><a name="p18934887"></a>port_id</p>
</td>
<td class="cellrowborder" valign="top" width="15.479999999999999%" headers="mcps1.2.4.1.2 "><p id="p13287175"><a name="p13287175"></a><a name="p13287175"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="68.10000000000001%" headers="mcps1.2.4.1.3 "><p id="p22674843"><a name="p22674843"></a><a name="p22674843"></a>Specifies the ID of the NIC port.</p>
</td>
</tr>
<tr id="row2747002"><td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.1 "><p id="p21180630"><a name="p21180630"></a><a name="p21180630"></a>mac_addr</p>
</td>
<td class="cellrowborder" valign="top" width="15.479999999999999%" headers="mcps1.2.4.1.2 "><p id="p50770908"><a name="p50770908"></a><a name="p50770908"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="68.10000000000001%" headers="mcps1.2.4.1.3 "><p id="p35008393"><a name="p35008393"></a><a name="p35008393"></a>Specifies the MAC address of the NIC.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **fixed\_ips**  field description

<a name="table19750463"></a>
<table><thead align="left"><tr id="row60761195"><th class="cellrowborder" valign="top" width="16.35%" id="mcps1.2.4.1.1"><p id="p1495811588288"><a name="p1495811588288"></a><a name="p1495811588288"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15.6%" id="mcps1.2.4.1.2"><p id="p5958105810282"><a name="p5958105810282"></a><a name="p5958105810282"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="68.05%" id="mcps1.2.4.1.3"><p id="p1495816587288"><a name="p1495816587288"></a><a name="p1495816587288"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row61624137"><td class="cellrowborder" valign="top" width="16.35%" headers="mcps1.2.4.1.1 "><p id="p25499238"><a name="p25499238"></a><a name="p25499238"></a>subnet_id</p>
</td>
<td class="cellrowborder" valign="top" width="15.6%" headers="mcps1.2.4.1.2 "><p id="p65213800"><a name="p65213800"></a><a name="p65213800"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="68.05%" headers="mcps1.2.4.1.3 "><p id="p27784979"><a name="p27784979"></a><a name="p27784979"></a>Specifies the subnet of the NIC private IP address.</p>
</td>
</tr>
<tr id="row48738220"><td class="cellrowborder" valign="top" width="16.35%" headers="mcps1.2.4.1.1 "><p id="p55481787"><a name="p55481787"></a><a name="p55481787"></a>ip_address</p>
</td>
<td class="cellrowborder" valign="top" width="15.6%" headers="mcps1.2.4.1.2 "><p id="p17532027"><a name="p17532027"></a><a name="p17532027"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="68.05%" headers="mcps1.2.4.1.3 "><p id="p30163672"><a name="p30163672"></a><a name="p30163672"></a>Specifies the NIC private IP address.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="section10941134193415"></a>

```
GET https://{endpoint}/v2/{project_id}/servers/{server_id}/os-interface
GET https://{endpoint}/v2.1/{project_id}/servers/{server_id}/os-interface
```

## Example Response<a name="section1829831018292"></a>

```
{
    "interfaceAttachments": [
        {
            "port_state": "ACTIVE",
            "fixed_ips": [
                {
                    "subnet_id": "f8a6e8f8-c2ec-497c-9f23-da9616de54ef",
                    "ip_address": "192.168.1.3"
                }
            ],
            "net_id": "3cb9bc59-5699-4588-a4b1-b87f96708bc6",
            "port_id": "ce531f90-199f-48c0-816c-13e38010b442",
            "mac_addr": "fa:16:3e:4c:2c:30"
        }
    ]
}
```

## Returned Values<a name="section52956621"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

