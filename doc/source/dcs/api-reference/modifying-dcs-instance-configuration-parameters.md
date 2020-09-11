# Modifying DCS Instance Configuration Parameters<a name="dcs-api-0312017"></a>

## Function<a name="section529181820420"></a>

You can modify the configuration parameters of your DCS instance to optimize DCS performance based on your requirements.

Currently, you can only modify configuration parameters for single-node and master/standby instances in the  **Running**  state.

## URI<a name="section19684271535"></a>

PUT /v1.0/\{project\_id\}/instances/\{instance\_id\}/configs

[Table 1](#table139152015133712)  describes the parameters.

**Table  1**  Parameter description

<a name="table139152015133712"></a>
<table><thead align="left"><tr id="row3914171515371"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p8914171523715"><a name="p8914171523715"></a><a name="p8914171523715"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p14914915103717"><a name="p14914915103717"></a><a name="p14914915103717"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p3914111515373"><a name="p3914111515373"></a><a name="p3914111515373"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p19914201519376"><a name="p19914201519376"></a><a name="p19914201519376"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row109153151378"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p4914415203712"><a name="p4914415203712"></a><a name="p4914415203712"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p59141615193712"><a name="p59141615193712"></a><a name="p59141615193712"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p59141915153719"><a name="p59141915153719"></a><a name="p59141915153719"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p159151715123717"><a name="p159151715123717"></a><a name="p159151715123717"></a>Project ID.</p>
</td>
</tr>
<tr id="row1791581520376"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p9915161523715"><a name="p9915161523715"></a><a name="p9915161523715"></a>instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p7915315203715"><a name="p7915315203715"></a><a name="p7915315203715"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p19915141513716"><a name="p19915141513716"></a><a name="p19915141513716"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p119151015183715"><a name="p119151015183715"></a><a name="p119151015183715"></a>ID of the instance to be modified.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section255981511312"></a>

**Request parameters**

[Table 2](#table16620132063713)  describes the request parameters.

**Table  2**  Parameter description

<a name="table16620132063713"></a>
<table><thead align="left"><tr id="row176191020183713"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p1561942073719"><a name="p1561942073719"></a><a name="p1561942073719"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p1661912013377"><a name="p1661912013377"></a><a name="p1661912013377"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p66191202372"><a name="p66191202372"></a><a name="p66191202372"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p161912206371"><a name="p161912206371"></a><a name="p161912206371"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row8620172073712"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1762011201378"><a name="p1762011201378"></a><a name="p1762011201378"></a>redis_config</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p1620182063719"><a name="p1620182063719"></a><a name="p1620182063719"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p2620420143710"><a name="p2620420143710"></a><a name="p2620420143710"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p36201420203712"><a name="p36201420203712"></a><a name="p36201420203712"></a>Array of configuration items of the DCS instance.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  redis\_config parameter description

<a name="table35215230340"></a>
<table><thead align="left"><tr id="row11517152311346"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p18516112333415"><a name="p18516112333415"></a><a name="p18516112333415"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.2"><p id="p851613233341"><a name="p851613233341"></a><a name="p851613233341"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="11%" id="mcps1.2.5.1.3"><p id="p85171239347"><a name="p85171239347"></a><a name="p85171239347"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="43%" id="mcps1.2.5.1.4"><p id="p351732393412"><a name="p351732393412"></a><a name="p351732393412"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1751811236347"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p13517323193415"><a name="p13517323193415"></a><a name="p13517323193415"></a>param_id</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.2 "><p id="p651718237346"><a name="p651718237346"></a><a name="p651718237346"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.3 "><p id="p1351814237341"><a name="p1351814237341"></a><a name="p1351814237341"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.5.1.4 "><p id="p751818239348"><a name="p751818239348"></a><a name="p751818239348"></a>Configuration item ID.</p>
</td>
</tr>
<tr id="row1151902315341"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p0518923113418"><a name="p0518923113418"></a><a name="p0518923113418"></a>param_name</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.2 "><p id="p165189231344"><a name="p165189231344"></a><a name="p165189231344"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.3 "><p id="p185191823103416"><a name="p185191823103416"></a><a name="p185191823103416"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.5.1.4 "><p id="p10519172320343"><a name="p10519172320343"></a><a name="p10519172320343"></a>Configuration item name.</p>
</td>
</tr>
<tr id="row1352013232346"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p14519122315343"><a name="p14519122315343"></a><a name="p14519122315343"></a>param_value</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.2 "><p id="p19519723193413"><a name="p19519723193413"></a><a name="p19519723193413"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.3 "><p id="p165201023173419"><a name="p165201023173419"></a><a name="p165201023173419"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.5.1.4 "><p id="p105201223193414"><a name="p105201223193414"></a><a name="p105201223193414"></a>Value of the configuration item.</p>
</td>
</tr>
</tbody>
</table>

For possible values of parameters in  [Table 3](#table35215230340), see  [Table 4](querying-dcs-instance-configuration-parameters.md#table1439111281351).

**Example request**

```
PUT https://{dcs_endpoint}/v1.0/{project_id}/instances/{instance_id}/configs
```

```
{ 
    "redis_config": [ 
        { 
            "param_id": "1", 
            "param_name": "timeout", 
            "param_value": "100" 
        } 
    ] 
}
```

## Response<a name="section125024718"></a>

**Response parameters**

None.

**Example response**

None.

## Status Code<a name="section174591750151213"></a>

[Table 4](#table17459195018122)  describes the status code of successful operations. For details about other status codes, see  [Table 1](status-codes.md#table5210141351517).

**Table  4**  Status code

<a name="table17459195018122"></a>
<table><thead align="left"><tr id="row9459350171212"><th class="cellrowborder" valign="top" width="15.98%" id="mcps1.2.3.1.1"><p id="p20460125021214"><a name="p20460125021214"></a><a name="p20460125021214"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="84.02%" id="mcps1.2.3.1.2"><p id="p94604504121"><a name="p94604504121"></a><a name="p94604504121"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1046019506125"><td class="cellrowborder" valign="top" width="15.98%" headers="mcps1.2.3.1.1 "><p id="p446055021214"><a name="p446055021214"></a><a name="p446055021214"></a>204</p>
</td>
<td class="cellrowborder" valign="top" width="84.02%" headers="mcps1.2.3.1.2 "><p id="p646055010129"><a name="p646055010129"></a><a name="p646055010129"></a>DCS instance configurations modified successfully.</p>
</td>
</tr>
</tbody>
</table>

