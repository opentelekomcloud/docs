# Querying Statistics of All Running Instances<a name="dcs-api-0312014"></a>

## Function<a name="section03501119195511"></a>

This API is used to query the statistics of all DCS instances that are in the  **Running**  state.

## URI<a name="section678380145219"></a>

GET /v1.0/\{project\_id\}/instances/statistic

[Table 1](#table8593726183514)  describes the parameter.

**Table  1**  Parameter description

<a name="table8593726183514"></a>
<table><thead align="left"><tr id="row1759392653515"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p65922269352"><a name="p65922269352"></a><a name="p65922269352"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p10592172653513"><a name="p10592172653513"></a><a name="p10592172653513"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p35931926163513"><a name="p35931926163513"></a><a name="p35931926163513"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p1259392633512"><a name="p1259392633512"></a><a name="p1259392633512"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1593202653513"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p959392614353"><a name="p959392614353"></a><a name="p959392614353"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p6593126103516"><a name="p6593126103516"></a><a name="p6593126103516"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p1759342693511"><a name="p1759342693511"></a><a name="p1759342693511"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p1359302623515"><a name="p1359302623515"></a><a name="p1359302623515"></a>Project ID</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section525620116529"></a>

**Request parameters**

None.

**Example request**

```
GET https://{dcs_endpoint}/v1.0/{project_id}/instances/statistic
```

## Response<a name="section1076710320527"></a>

**Response parameters**

[Table 2](#table254823012351)  describes the response parameter.

**Table  2**  Parameter description

<a name="table254823012351"></a>
<table><thead align="left"><tr id="row454823033518"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p19271145132518"><a name="p19271145132518"></a><a name="p19271145132518"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p2548173053511"><a name="p2548173053511"></a><a name="p2548173053511"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p19548183083519"><a name="p19548183083519"></a><a name="p19548183083519"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row8548630153516"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p654873018353"><a name="p654873018353"></a><a name="p654873018353"></a>statistics</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p0548153093512"><a name="p0548153093512"></a><a name="p0548153093512"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p205488301359"><a name="p205488301359"></a><a name="p205488301359"></a>Statistics of all instances in the <strong id="b2526205910520"><a name="b2526205910520"></a><a name="b2526205910520"></a>Running</strong> state. For details, see <a href="#table7914256164">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  statistics parameter description

<a name="table7914256164"></a>
<table><thead align="left"><tr id="row6914195611613"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.4.1.1"><p id="p1191417569612"><a name="p1191417569612"></a><a name="p1191417569612"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.4.1.2"><p id="p1191415613619"><a name="p1191415613619"></a><a name="p1191415613619"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="53%" id="mcps1.2.4.1.3"><p id="p691414560620"><a name="p691414560620"></a><a name="p691414560620"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1491513561461"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="p19915195614617"><a name="p19915195614617"></a><a name="p19915195614617"></a>keys</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p17915125620619"><a name="p17915125620619"></a><a name="p17915125620619"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.4.1.3 "><p id="p79151056865"><a name="p79151056865"></a><a name="p79151056865"></a>Number of cached data records</p>
</td>
</tr>
<tr id="row19698149103520"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="p1114765163510"><a name="p1114765163510"></a><a name="p1114765163510"></a>instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p1714815193511"><a name="p1714815193511"></a><a name="p1714815193511"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.4.1.3 "><p id="p141482051103516"><a name="p141482051103516"></a><a name="p141482051103516"></a>DCS instance ID</p>
</td>
</tr>
<tr id="row1191516561968"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="p18915656968"><a name="p18915656968"></a><a name="p18915656968"></a>used_memory</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p14915145615610"><a name="p14915145615610"></a><a name="p14915145615610"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.4.1.3 "><p id="p291565620618"><a name="p291565620618"></a><a name="p291565620618"></a>Size of the used memory in MB</p>
</td>
</tr>
<tr id="row59151956264"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="p13915185611615"><a name="p13915185611615"></a><a name="p13915185611615"></a>max_memory</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p891517562062"><a name="p891517562062"></a><a name="p891517562062"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.4.1.3 "><p id="p1991517561466"><a name="p1991517561466"></a><a name="p1991517561466"></a>Overall memory size in MB.</p>
</td>
</tr>
<tr id="row8915156766"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="p49151856163"><a name="p49151856163"></a><a name="p49151856163"></a>cmd_get_count</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p1691515561068"><a name="p1691515561068"></a><a name="p1691515561068"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.4.1.3 "><p id="p39157564612"><a name="p39157564612"></a><a name="p39157564612"></a>Number of times the GET command is run</p>
</td>
</tr>
<tr id="row139151356469"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="p149156569611"><a name="p149156569611"></a><a name="p149156569611"></a>cmd_set_count</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p1091525613614"><a name="p1091525613614"></a><a name="p1091525613614"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.4.1.3 "><p id="p09157568619"><a name="p09157568619"></a><a name="p09157568619"></a>Number of times the SET command is run</p>
</td>
</tr>
<tr id="row139151156268"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="p14915115616613"><a name="p14915115616613"></a><a name="p14915115616613"></a>used_cpu</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p69151656567"><a name="p69151656567"></a><a name="p69151656567"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.4.1.3 "><p id="p391520565615"><a name="p391520565615"></a><a name="p391520565615"></a>Percentage of CPU usage</p>
</td>
</tr>
<tr id="row6915356665"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="p1591512568616"><a name="p1591512568616"></a><a name="p1591512568616"></a>input_kbps</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p17916856466"><a name="p17916856466"></a><a name="p17916856466"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.4.1.3 "><p id="p391665616610"><a name="p391665616610"></a><a name="p391665616610"></a>Incoming traffic (kbit/s) of the DCS instance</p>
</td>
</tr>
<tr id="row159161561669"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="p391625614617"><a name="p391625614617"></a><a name="p391625614617"></a>output_kbps</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p149163561619"><a name="p149163561619"></a><a name="p149163561619"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.4.1.3 "><p id="p159161356362"><a name="p159161356362"></a><a name="p159161356362"></a>Outgoing traffic (kbit/s) of the DCS instance</p>
</td>
</tr>
</tbody>
</table>

**Example response**

```
{
    "statistics" : [{
            "keys" : 0,
            "instance_id" : "e008652d-18e0-43ff-924e-072261e0372a",
            "used_memory" : 0,
            "max_memory" : 460,
            "cmd_get_count" : 0,
            "cmd_set_count" : 0,
            "used_cpu" : "0.0",
            "input_kbps" : "0.0",
            "output_kbps" : "0.0"
        }, {
            "keys" : 0,
            "instance_id" : "c577a1eb-33b7-42c7-8231-ad32358599ac",
            "used_memory" : 0,
            "max_memory" : 460,
            "cmd_get_count" : 0,
            "cmd_set_count" : 0,
            "used_cpu" : "0.0",
            "input_kbps" : "0.0",
            "output_kbps" : "0.0"
        }, {
            "keys" : 0,
            "instance_id" : "e8b98471-55d5-4695-b0bb-8f336a98e207",
            "used_memory" : 0,
            "max_memory" : 460,
            "cmd_get_count" : 0,
            "cmd_set_count" : 0,
            "used_cpu" : "0.0",
            "input_kbps" : "0.03",
            "output_kbps" : "1.19"
        }, {
            "keys" : 0,
            "instance_id" : "bc61c690-4b34-4cbe-9ce3-11246aea7aba",
            "used_memory" : 0,
            "max_memory" : 6963,
            "cmd_get_count" : 0,
            "cmd_set_count" : 0,
            "used_cpu" : "0.0",
            "input_kbps" : "0.0",
            "output_kbps" : "0.0"
        }
    ]
}
```

## Status Code<a name="section143993303124"></a>

[Table 4](#table63992308123)  describes the status code of successful operations. For details about other status codes, see  [Table 1](status-codes.md#table5210141351517).

**Table  4**  Status code

<a name="table63992308123"></a>
<table><thead align="left"><tr id="row1400230201218"><th class="cellrowborder" valign="top" width="15.98%" id="mcps1.2.3.1.1"><p id="p14009308126"><a name="p14009308126"></a><a name="p14009308126"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="84.02%" id="mcps1.2.3.1.2"><p id="p13400203001219"><a name="p13400203001219"></a><a name="p13400203001219"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row540016305125"><td class="cellrowborder" valign="top" width="15.98%" headers="mcps1.2.3.1.1 "><p id="p3400163015122"><a name="p3400163015122"></a><a name="p3400163015122"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="84.02%" headers="mcps1.2.3.1.2 "><p id="p24001308129"><a name="p24001308129"></a><a name="p24001308129"></a>Statistics of all instances queried successfully.</p>
</td>
</tr>
</tbody>
</table>

