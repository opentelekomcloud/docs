# Querying NICs of an ECS<a name="EN-US_TOPIC_0020212662"></a>

## Function<a name="section44739342"></a>

This API is used to query information about an ECS NIC based on the NIC ID.

## URI<a name="section901"></a>

GET /v2/\{project\_id\}/servers/\{server\_id\}/os-interface/\{id\}

GET /v2.1/\{project\_id\}/servers/\{server\_id\}/os-interface/\{id\}

[Table 1](#table25654779)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table25654779"></a>
<table><thead align="left"><tr id="row30661937"><th class="cellrowborder" valign="top" width="16.79%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.36%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.85%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row52467932"><td class="cellrowborder" valign="top" width="16.79%" headers="mcps1.2.4.1.1 "><p id="p22044110"><a name="p22044110"></a><a name="p22044110"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.2 "><p id="p40742509"><a name="p40742509"></a><a name="p40742509"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.85%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row3850232617435"><td class="cellrowborder" valign="top" width="16.79%" headers="mcps1.2.4.1.1 "><p id="p3575612917451"><a name="p3575612917451"></a><a name="p3575612917451"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.2 "><p id="p1056536017451"><a name="p1056536017451"></a><a name="p1056536017451"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.85%" headers="mcps1.2.4.1.3 "><p id="p5048782717451"><a name="p5048782717451"></a><a name="p5048782717451"></a>Specifies the ECS ID.</p>
</td>
</tr>
<tr id="row39171493"><td class="cellrowborder" valign="top" width="16.79%" headers="mcps1.2.4.1.1 "><p id="p18774354"><a name="p18774354"></a><a name="p18774354"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.2 "><p id="p44327687"><a name="p44327687"></a><a name="p44327687"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.85%" headers="mcps1.2.4.1.3 "><p id="p21064308"><a name="p21064308"></a><a name="p21064308"></a>Specifies the port ID of the NIC.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section8117"></a>

None

## Response<a name="section73053"></a>

[Table 2](#table59131099)  describes the response parameters.

**Table  2**  Response parameters

<a name="table59131099"></a>
<table><thead align="left"><tr id="row30342446"><th class="cellrowborder" valign="top" width="17.1%" id="mcps1.2.4.1.1"><p id="p41819089"><a name="p41819089"></a><a name="p41819089"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.48%" id="mcps1.2.4.1.2"><p id="p34008447"><a name="p34008447"></a><a name="p34008447"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="65.42%" id="mcps1.2.4.1.3"><p id="p3220827"><a name="p3220827"></a><a name="p3220827"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row59560431"><td class="cellrowborder" valign="top" width="17.1%" headers="mcps1.2.4.1.1 "><p id="p59665636"><a name="p59665636"></a><a name="p59665636"></a>interfaceAttachment</p>
</td>
<td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.2.4.1.2 "><p id="p20239120"><a name="p20239120"></a><a name="p20239120"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="65.42%" headers="mcps1.2.4.1.3 "><p id="p86059257225"><a name="p86059257225"></a><a name="p86059257225"></a>Specifies ECS NICs. For details, see <a href="#table24005299">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **interfaceAttachment**  field description

<a name="table24005299"></a>
<table><thead align="left"><tr id="row46441279"><th class="cellrowborder" valign="top" width="17.04%" id="mcps1.2.4.1.1"><p id="p174601748143018"><a name="p174601748143018"></a><a name="p174601748143018"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.419999999999998%" id="mcps1.2.4.1.2"><p id="p15460748163010"><a name="p15460748163010"></a><a name="p15460748163010"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="65.53999999999999%" id="mcps1.2.4.1.3"><p id="p10460248123010"><a name="p10460248123010"></a><a name="p10460248123010"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row64586077"><td class="cellrowborder" valign="top" width="17.04%" headers="mcps1.2.4.1.1 "><p id="p64089786"><a name="p64089786"></a><a name="p64089786"></a>port_state</p>
</td>
<td class="cellrowborder" valign="top" width="17.419999999999998%" headers="mcps1.2.4.1.2 "><p id="p56055356"><a name="p56055356"></a><a name="p56055356"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="65.53999999999999%" headers="mcps1.2.4.1.3 "><p id="p62165703"><a name="p62165703"></a><a name="p62165703"></a>Specifies the NIC port status.</p>
</td>
</tr>
<tr id="row22620416"><td class="cellrowborder" valign="top" width="17.04%" headers="mcps1.2.4.1.1 "><p id="p20314447"><a name="p20314447"></a><a name="p20314447"></a>fixed_ips</p>
</td>
<td class="cellrowborder" valign="top" width="17.419999999999998%" headers="mcps1.2.4.1.2 "><p id="p4888719"><a name="p4888719"></a><a name="p4888719"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="65.53999999999999%" headers="mcps1.2.4.1.3 "><p id="p7106508"><a name="p7106508"></a><a name="p7106508"></a>Specifies IP addresses for NICs. For details, see <a href="#table53180163">Table 4</a>.</p>
</td>
</tr>
<tr id="row63958576"><td class="cellrowborder" valign="top" width="17.04%" headers="mcps1.2.4.1.1 "><p id="p13262169"><a name="p13262169"></a><a name="p13262169"></a>net_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.419999999999998%" headers="mcps1.2.4.1.2 "><p id="p40009126"><a name="p40009126"></a><a name="p40009126"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="65.53999999999999%" headers="mcps1.2.4.1.3 "><p id="p41406050"><a name="p41406050"></a><a name="p41406050"></a>Specifies the network ID to which the NIC port belongs.</p>
</td>
</tr>
<tr id="row37110132"><td class="cellrowborder" valign="top" width="17.04%" headers="mcps1.2.4.1.1 "><p id="p53130720"><a name="p53130720"></a><a name="p53130720"></a>port_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.419999999999998%" headers="mcps1.2.4.1.2 "><p id="p27217289"><a name="p27217289"></a><a name="p27217289"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="65.53999999999999%" headers="mcps1.2.4.1.3 "><p id="p44289360"><a name="p44289360"></a><a name="p44289360"></a>Specifies the ID of the NIC port.</p>
</td>
</tr>
<tr id="row63059925"><td class="cellrowborder" valign="top" width="17.04%" headers="mcps1.2.4.1.1 "><p id="p7580267"><a name="p7580267"></a><a name="p7580267"></a>mac_addr</p>
</td>
<td class="cellrowborder" valign="top" width="17.419999999999998%" headers="mcps1.2.4.1.2 "><p id="p6466753"><a name="p6466753"></a><a name="p6466753"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="65.53999999999999%" headers="mcps1.2.4.1.3 "><p id="p16643039"><a name="p16643039"></a><a name="p16643039"></a>Specifies the MAC address of the NIC.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **fixed\_ips**  field description

<a name="table53180163"></a>
<table><thead align="left"><tr id="row34896342"><th class="cellrowborder" valign="top" width="17.169999999999998%" id="mcps1.2.4.1.1"><p id="p10906155214308"><a name="p10906155214308"></a><a name="p10906155214308"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.36%" id="mcps1.2.4.1.2"><p id="p1490615524301"><a name="p1490615524301"></a><a name="p1490615524301"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="65.47%" id="mcps1.2.4.1.3"><p id="p129069520307"><a name="p129069520307"></a><a name="p129069520307"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row66523006"><td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p64293480112230"><a name="p64293480112230"></a><a name="p64293480112230"></a>subnet_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.2 "><p id="p40389402112230"><a name="p40389402112230"></a><a name="p40389402112230"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="65.47%" headers="mcps1.2.4.1.3 "><p id="p50192196112230"><a name="p50192196112230"></a><a name="p50192196112230"></a>Specifies the ID of the subnet used by the NIC. </p>
</td>
</tr>
<tr id="row12592542"><td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p15780700112230"><a name="p15780700112230"></a><a name="p15780700112230"></a>ip_address</p>
</td>
<td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.2 "><p id="p3168304112230"><a name="p3168304112230"></a><a name="p3168304112230"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="65.47%" headers="mcps1.2.4.1.3 "><p id="p27992537112230"><a name="p27992537112230"></a><a name="p27992537112230"></a>Specifies the NIC IP address.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="section132471610203513"></a>

```
GET https://{endpoint}/v2/{project_id}/servers/{server_id}/os-interface/{id}
GET https://{endpoint}/v2.1/{project_id}/servers/{server_id}/os-interface/{id}
```

## Example Response<a name="section1032435683014"></a>

```
{
    "interfaceAttachment": 
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
                    }
```

## Returned Values<a name="section657479"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

