# Adding an NIC to an ECS<a name="EN-US_TOPIC_0020212664"></a>

## Function<a name="section10723444"></a>

This API is used to add a single NIC to an ECS.

## URI<a name="section29402138"></a>

POST /v2/\{project\_id\}/servers/\{server\_id\}/os-interface

POST /v2.1/\{project\_id\}/servers/\{server\_id\}/os-interface

[Table 1](#table55925239)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table55925239"></a>
<table><thead align="left"><tr id="row60011419"><th class="cellrowborder" valign="top" width="16.6%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.169999999999998%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="66.23%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row61407752"><td class="cellrowborder" valign="top" width="16.6%" headers="mcps1.2.4.1.1 "><p id="p7972012"><a name="p7972012"></a><a name="p7972012"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p41753265"><a name="p41753265"></a><a name="p41753265"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row37815352"><td class="cellrowborder" valign="top" width="16.6%" headers="mcps1.2.4.1.1 "><p id="p43144677"><a name="p43144677"></a><a name="p43144677"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p5057967"><a name="p5057967"></a><a name="p5057967"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.2.4.1.3 "><p id="p7042173"><a name="p7042173"></a><a name="p7042173"></a>Specifies the ECS ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section63292653"></a>

[Table 2](#table21989419)  describes the request parameters.

**Table  2**  Request parameters

<a name="table21989419"></a>
<table><thead align="left"><tr id="row20106686"><th class="cellrowborder" valign="top" width="16.41%" id="mcps1.2.5.1.1"><p id="p18028880"><a name="p18028880"></a><a name="p18028880"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.560000000000002%" id="mcps1.2.5.1.2"><p id="p51053199"><a name="p51053199"></a><a name="p51053199"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16.14%" id="mcps1.2.5.1.3"><p id="p41668450"><a name="p41668450"></a><a name="p41668450"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49.89%" id="mcps1.2.5.1.4"><p id="p19701298"><a name="p19701298"></a><a name="p19701298"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row52301286"><td class="cellrowborder" valign="top" width="16.41%" headers="mcps1.2.5.1.1 "><p id="p8545767"><a name="p8545767"></a><a name="p8545767"></a>interfaceAttachment</p>
</td>
<td class="cellrowborder" valign="top" width="17.560000000000002%" headers="mcps1.2.5.1.2 "><p id="p21118492"><a name="p21118492"></a><a name="p21118492"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.14%" headers="mcps1.2.5.1.3 "><p id="p32876269"><a name="p32876269"></a><a name="p32876269"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="49.89%" headers="mcps1.2.5.1.4 "><p id="p8936292"><a name="p8936292"></a><a name="p8936292"></a>Specifies the NICs to be added. For details, see <a href="#table44975500">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **interfaceAttachment**  field description

<a name="table44975500"></a>
<table><thead align="left"><tr id="row35373287"><th class="cellrowborder" valign="top" width="16.35%" id="mcps1.2.5.1.1"><p id="p163671873419"><a name="p163671873419"></a><a name="p163671873419"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.669999999999998%" id="mcps1.2.5.1.2"><p id="p1136121853418"><a name="p1136121853418"></a><a name="p1136121853418"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="13.719999999999999%" id="mcps1.2.5.1.3"><p id="p15361118183411"><a name="p15361118183411"></a><a name="p15361118183411"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="52.26%" id="mcps1.2.5.1.4"><p id="p183691812344"><a name="p183691812344"></a><a name="p183691812344"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row19920592"><td class="cellrowborder" valign="top" width="16.35%" headers="mcps1.2.5.1.1 "><p id="p2955276"><a name="p2955276"></a><a name="p2955276"></a>port_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.669999999999998%" headers="mcps1.2.5.1.2 "><p id="p38050837"><a name="p38050837"></a><a name="p38050837"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.719999999999999%" headers="mcps1.2.5.1.3 "><p id="p23099752"><a name="p23099752"></a><a name="p23099752"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.26%" headers="mcps1.2.5.1.4 "><p id="p62503562"><a name="p62503562"></a><a name="p62503562"></a>Specifies the port ID.</p>
<p id="p1735084713332"><a name="p1735084713332"></a><a name="p1735084713332"></a>Either <strong id="b842352706164230"><a name="b842352706164230"></a><a name="b842352706164230"></a>port_id</strong> or <strong id="b842352706164234"><a name="b842352706164234"></a><a name="b842352706164234"></a>net_id</strong> is used each time.</p>
</td>
</tr>
<tr id="row65287294"><td class="cellrowborder" valign="top" width="16.35%" headers="mcps1.2.5.1.1 "><p id="p53779479"><a name="p53779479"></a><a name="p53779479"></a>net_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.669999999999998%" headers="mcps1.2.5.1.2 "><p id="p61170512"><a name="p61170512"></a><a name="p61170512"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.719999999999999%" headers="mcps1.2.5.1.3 "><p id="p33017564"><a name="p33017564"></a><a name="p33017564"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.26%" headers="mcps1.2.5.1.4 "><p id="p44831437"><a name="p44831437"></a><a name="p44831437"></a>Specifies the network ID.</p>
<p id="p19593329161444"><a name="p19593329161444"></a><a name="p19593329161444"></a>This parameter is invalid if parameter <strong>port_id</strong> is specified.</p>
</td>
</tr>
<tr id="row6769295"><td class="cellrowborder" valign="top" width="16.35%" headers="mcps1.2.5.1.1 "><p id="p11442060"><a name="p11442060"></a><a name="p11442060"></a>fixed_ips</p>
</td>
<td class="cellrowborder" valign="top" width="17.669999999999998%" headers="mcps1.2.5.1.2 "><p id="p54391657"><a name="p54391657"></a><a name="p54391657"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.719999999999999%" headers="mcps1.2.5.1.3 "><p id="p57288388"><a name="p57288388"></a><a name="p57288388"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="52.26%" headers="mcps1.2.5.1.4 "><p id="p21521490"><a name="p21521490"></a><a name="p21521490"></a>Specifies a private IP address.</p>
<p id="p52801617"><a name="p52801617"></a><a name="p52801617"></a>This parameter is invalid if <strong id="b64072134154929"><a name="b64072134154929"></a><a name="b64072134154929"></a>port_id</strong> has been specified. This parameter must be specified together with <strong id="b40981553154929"><a name="b40981553154929"></a><a name="b40981553154929"></a>net_id</strong>.</p>
<p id="p6399032017506"><a name="p6399032017506"></a><a name="p6399032017506"></a>Only the first element in the list is valid. If two or more elements are used, an error will be reported. For details, see <a href="#table26224215175117">Table 4</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **fixed\_ips**  field description

<a name="table26224215175117"></a>
<table><thead align="left"><tr id="row58580904175117"><th class="cellrowborder" valign="top" width="16.33%" id="mcps1.2.5.1.1"><p id="p141684386346"><a name="p141684386346"></a><a name="p141684386346"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.25%" id="mcps1.2.5.1.2"><p id="p19168133812341"><a name="p19168133812341"></a><a name="p19168133812341"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.099999999999998%" id="mcps1.2.5.1.3"><p id="p17168538103412"><a name="p17168538103412"></a><a name="p17168538103412"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="52.32%" id="mcps1.2.5.1.4"><p id="p1818353816344"><a name="p1818353816344"></a><a name="p1818353816344"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row38687294175117"><td class="cellrowborder" valign="top" width="16.33%" headers="mcps1.2.5.1.1 "><p id="p58156055175144"><a name="p58156055175144"></a><a name="p58156055175144"></a>ip_address</p>
</td>
<td class="cellrowborder" valign="top" width="17.25%" headers="mcps1.2.5.1.2 "><p id="p1214420331348"><a name="p1214420331348"></a><a name="p1214420331348"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.099999999999998%" headers="mcps1.2.5.1.3 "><p id="p21614964175117"><a name="p21614964175117"></a><a name="p21614964175117"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.32%" headers="mcps1.2.5.1.4 "><p id="p5981637175117"><a name="p5981637175117"></a><a name="p5981637175117"></a>Specifies the IP address.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section32762966"></a>

[Table 5](#table60398192112020)  describes the response parameters.

**Table  5**  Response parameters

<a name="table60398192112020"></a>
<table><thead align="left"><tr id="row40180364112020"><th class="cellrowborder" valign="top" width="16.509999999999998%" id="mcps1.2.4.1.1"><p id="p33384038112020"><a name="p33384038112020"></a><a name="p33384038112020"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.2%" id="mcps1.2.4.1.2"><p id="p19752577112020"><a name="p19752577112020"></a><a name="p19752577112020"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="67.29%" id="mcps1.2.4.1.3"><p id="p56454917112020"><a name="p56454917112020"></a><a name="p56454917112020"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row9445528112020"><td class="cellrowborder" valign="top" width="16.509999999999998%" headers="mcps1.2.4.1.1 "><p id="p26890341112020"><a name="p26890341112020"></a><a name="p26890341112020"></a>interfaceAttachment</p>
</td>
<td class="cellrowborder" valign="top" width="16.2%" headers="mcps1.2.4.1.2 "><p id="p30634002112020"><a name="p30634002112020"></a><a name="p30634002112020"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="67.29%" headers="mcps1.2.4.1.3 "><p id="p52044805112020"><a name="p52044805112020"></a><a name="p52044805112020"></a>Specifies ECS NICs. For details, see <a href="#table49017803">Table 6</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  6** **interfaceAttachment**  field description

<a name="table49017803"></a>
<table><thead align="left"><tr id="row45954822"><th class="cellrowborder" valign="top" width="16.669999999999998%" id="mcps1.2.4.1.1"><p id="p1838855864417"><a name="p1838855864417"></a><a name="p1838855864417"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15.9%" id="mcps1.2.4.1.2"><p id="p7388958164410"><a name="p7388958164410"></a><a name="p7388958164410"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="67.43%" id="mcps1.2.4.1.3"><p id="p4404858174411"><a name="p4404858174411"></a><a name="p4404858174411"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row50443655"><td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p59404221"><a name="p59404221"></a><a name="p59404221"></a>port_state</p>
</td>
<td class="cellrowborder" valign="top" width="15.9%" headers="mcps1.2.4.1.2 "><p id="p49923923"><a name="p49923923"></a><a name="p49923923"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67.43%" headers="mcps1.2.4.1.3 "><p id="p17305987"><a name="p17305987"></a><a name="p17305987"></a>Specifies the port state.</p>
</td>
</tr>
<tr id="row21536161"><td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p66707469"><a name="p66707469"></a><a name="p66707469"></a>fixed_ips</p>
</td>
<td class="cellrowborder" valign="top" width="15.9%" headers="mcps1.2.4.1.2 "><p id="p50801977"><a name="p50801977"></a><a name="p50801977"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="67.43%" headers="mcps1.2.4.1.3 "><p id="p57657762"><a name="p57657762"></a><a name="p57657762"></a>Specifies IP addresses for NICs. For details, see <a href="#table35098076112057">Table 7</a>.</p>
</td>
</tr>
<tr id="row49157816"><td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p22360170"><a name="p22360170"></a><a name="p22360170"></a>port_id</p>
</td>
<td class="cellrowborder" valign="top" width="15.9%" headers="mcps1.2.4.1.2 "><p id="p5103804"><a name="p5103804"></a><a name="p5103804"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67.43%" headers="mcps1.2.4.1.3 "><p id="p29686030"><a name="p29686030"></a><a name="p29686030"></a>Specifies the port ID.</p>
</td>
</tr>
<tr id="row65847680"><td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p32061857"><a name="p32061857"></a><a name="p32061857"></a>net_id</p>
</td>
<td class="cellrowborder" valign="top" width="15.9%" headers="mcps1.2.4.1.2 "><p id="p38664423"><a name="p38664423"></a><a name="p38664423"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67.43%" headers="mcps1.2.4.1.3 "><p id="p642126"><a name="p642126"></a><a name="p642126"></a>Specifies the network ID.</p>
</td>
</tr>
<tr id="row5779136"><td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p65456887"><a name="p65456887"></a><a name="p65456887"></a>mac_addr</p>
</td>
<td class="cellrowborder" valign="top" width="15.9%" headers="mcps1.2.4.1.2 "><p id="p33020419"><a name="p33020419"></a><a name="p33020419"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67.43%" headers="mcps1.2.4.1.3 "><p id="p57408296"><a name="p57408296"></a><a name="p57408296"></a>Specifies the MAC address.</p>
</td>
</tr>
</tbody>
</table>

**Table  7** **fixed\_ips**  field description

<a name="table35098076112057"></a>
<table><thead align="left"><tr id="row50961341112057"><th class="cellrowborder" valign="top" width="16.6%" id="mcps1.2.4.1.1"><p id="p1214910115455"><a name="p1214910115455"></a><a name="p1214910115455"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15.85%" id="mcps1.2.4.1.2"><p id="p214914120458"><a name="p214914120458"></a><a name="p214914120458"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="67.55%" id="mcps1.2.4.1.3"><p id="p1514921174516"><a name="p1514921174516"></a><a name="p1514921174516"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row5951916112057"><td class="cellrowborder" valign="top" width="16.6%" headers="mcps1.2.4.1.1 "><p id="p12343224112057"><a name="p12343224112057"></a><a name="p12343224112057"></a>subnet_id</p>
</td>
<td class="cellrowborder" valign="top" width="15.85%" headers="mcps1.2.4.1.2 "><p id="p60277055112057"><a name="p60277055112057"></a><a name="p60277055112057"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67.55%" headers="mcps1.2.4.1.3 "><p id="p52776587112057"><a name="p52776587112057"></a><a name="p52776587112057"></a>Specifies the ID of the subnet used by the NIC.</p>
</td>
</tr>
<tr id="row5227236112057"><td class="cellrowborder" valign="top" width="16.6%" headers="mcps1.2.4.1.1 "><p id="p20752977112057"><a name="p20752977112057"></a><a name="p20752977112057"></a>ip_address</p>
</td>
<td class="cellrowborder" valign="top" width="15.85%" headers="mcps1.2.4.1.2 "><p id="p3269595112057"><a name="p3269595112057"></a><a name="p3269595112057"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67.55%" headers="mcps1.2.4.1.3 "><p id="p34724789112057"><a name="p34724789112057"></a><a name="p34724789112057"></a>Specifies the NIC IP address.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="section1478176134514"></a>

```
POST https://{endpoint}/v2/{project_id}/servers/{server_id}/os-interface
POST https://{endpoint}/v2.1/{project_id}/servers/{server_id}/os-interface
```

```
{
    "interfaceAttachment" : {
        "fixed_ips" : [ 
            {
                "ip_address" : "192.168.1.3"
            } 
         ],
    "net_id" : "3cb9bc59-5699-4588-a4b1-b87f96708bc6"
    }
}
```

```
{
    "interfaceAttachment" : {
    "port_id" : "ce531f90-199f-48c0-816c-13e38010b442"
    }
}
```

## Example Response<a name="section247111511352"></a>

```
{
    "interfaceAttachment": {
        "port_state": "DOWN",
        "fixed_ips": [
            {
                "subnet_id": "d9cfef77-0151-4c2a-9ed5-d951ada8adf3",
                "ip_address": "10.0.1.11"
            }
        ],
        "port_id": " ce531f90-199f-48c0-816c-13e38010b442",
        "net_id": "0dc714fa-9022-4a03-bb22-9821a396bb9d",
        "mac_addr": "fa:16:3e:63:75:b2"
    }
}
```

## Returned Values<a name="section26431238"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

