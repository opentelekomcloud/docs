# Querying AZs<a name="EN-US_TOPIC_0065817728"></a>

## Function<a name="en-us_topic_0057973206_section60955817"></a>

This API is used to query AZs.

## URI<a name="en-us_topic_0057973206_section11731442"></a>

GET /v2/\{project\_id\}/os-availability-zone

GET /v2.1/\{project\_id\}/os-availability-zone

[Table 1](#en-us_topic_0057973206_table2814978410562)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="en-us_topic_0057973206_table2814978410562"></a>
<table><thead align="left"><tr id="en-us_topic_0057973206_row4149654710562"><th class="cellrowborder" valign="top" width="16.830000000000002%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.549999999999997%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.62%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973206_row3491217610562"><td class="cellrowborder" valign="top" width="16.830000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973206_p931403110562"><a name="en-us_topic_0057973206_p931403110562"></a><a name="en-us_topic_0057973206_p931403110562"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.549999999999997%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973206_p1623904210562"><a name="en-us_topic_0057973206_p1623904210562"></a><a name="en-us_topic_0057973206_p1623904210562"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.62%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="en-us_topic_0057973206_section63234676"></a>

[Table 2](#en-us_topic_0057973206_table34970028)  describes the response parameters.

**Table  2**  Response parameters

<a name="en-us_topic_0057973206_table34970028"></a>
<table><thead align="left"><tr id="en-us_topic_0057973206_row39112085"><th class="cellrowborder" valign="top" width="16.900000000000002%" id="mcps1.2.4.1.1"><p id="en-us_topic_0057972670_p57733603"><a name="en-us_topic_0057972670_p57733603"></a><a name="en-us_topic_0057972670_p57733603"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15.65%" id="mcps1.2.4.1.2"><p id="en-us_topic_0057972670_p45910260"><a name="en-us_topic_0057972670_p45910260"></a><a name="en-us_topic_0057972670_p45910260"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="67.45%" id="mcps1.2.4.1.3"><p id="en-us_topic_0057972670_p32634650"><a name="en-us_topic_0057972670_p32634650"></a><a name="en-us_topic_0057972670_p32634650"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973206_row37957477"><td class="cellrowborder" valign="top" width="16.900000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973206_p54656798"><a name="en-us_topic_0057973206_p54656798"></a><a name="en-us_topic_0057973206_p54656798"></a>availabilityZoneInfo</p>
</td>
<td class="cellrowborder" valign="top" width="15.65%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973206_p65124552"><a name="en-us_topic_0057973206_p65124552"></a><a name="en-us_topic_0057973206_p65124552"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="67.45%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973206_p54030"><a name="en-us_topic_0057973206_p54030"></a><a name="en-us_topic_0057973206_p54030"></a>Specifies the AZ information.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  AvailabilityZoneInfo parameter information

<a name="en-us_topic_0057973206_table4376441"></a>
<table><thead align="left"><tr id="en-us_topic_0057973206_row55834932"><th class="cellrowborder" valign="top" width="16.900000000000002%" id="mcps1.2.4.1.1"><p id="p044879102811"><a name="p044879102811"></a><a name="p044879102811"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15.65%" id="mcps1.2.4.1.2"><p id="p74488912281"><a name="p74488912281"></a><a name="p74488912281"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="67.45%" id="mcps1.2.4.1.3"><p id="p846317913288"><a name="p846317913288"></a><a name="p846317913288"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973206_row62745414"><td class="cellrowborder" valign="top" width="16.900000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973206_p49213798"><a name="en-us_topic_0057973206_p49213798"></a><a name="en-us_topic_0057973206_p49213798"></a>zoneState</p>
</td>
<td class="cellrowborder" valign="top" width="15.65%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973206_p26894719"><a name="en-us_topic_0057973206_p26894719"></a><a name="en-us_topic_0057973206_p26894719"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="67.45%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973206_p27048633"><a name="en-us_topic_0057973206_p27048633"></a><a name="en-us_topic_0057973206_p27048633"></a>Specifies the AZ status.</p>
</td>
</tr>
<tr id="en-us_topic_0057973206_row42111108"><td class="cellrowborder" valign="top" width="16.900000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973206_p55556613"><a name="en-us_topic_0057973206_p55556613"></a><a name="en-us_topic_0057973206_p55556613"></a>hosts</p>
</td>
<td class="cellrowborder" valign="top" width="15.65%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973206_p3791843"><a name="en-us_topic_0057973206_p3791843"></a><a name="en-us_topic_0057973206_p3791843"></a>List</p>
</td>
<td class="cellrowborder" valign="top" width="67.45%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973206_p48006356"><a name="en-us_topic_0057973206_p48006356"></a><a name="en-us_topic_0057973206_p48006356"></a>The parameter is set to <strong id="en-us_topic_0057973206_b54095206"><a name="en-us_topic_0057973206_b54095206"></a><a name="en-us_topic_0057973206_b54095206"></a>null</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0057973206_row29404023"><td class="cellrowborder" valign="top" width="16.900000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973206_p32915700"><a name="en-us_topic_0057973206_p32915700"></a><a name="en-us_topic_0057973206_p32915700"></a>zoneName</p>
</td>
<td class="cellrowborder" valign="top" width="15.65%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973206_p48926033"><a name="en-us_topic_0057973206_p48926033"></a><a name="en-us_topic_0057973206_p48926033"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67.45%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973206_p22007756"><a name="en-us_topic_0057973206_p22007756"></a><a name="en-us_topic_0057973206_p22007756"></a>Specifies the AZ name.</p>
</td>
</tr>
</tbody>
</table>

**Table  4**  zoneState parameter information

<a name="en-us_topic_0057973206_table37797818"></a>
<table><thead align="left"><tr id="en-us_topic_0057973206_row19790066"><th class="cellrowborder" valign="top" width="16.93%" id="mcps1.2.4.1.1"><p id="p19223713172814"><a name="p19223713172814"></a><a name="p19223713172814"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15.620000000000001%" id="mcps1.2.4.1.2"><p id="p7223213122812"><a name="p7223213122812"></a><a name="p7223213122812"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="67.45%" id="mcps1.2.4.1.3"><p id="p17223111314282"><a name="p17223111314282"></a><a name="p17223111314282"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973206_row56786272"><td class="cellrowborder" valign="top" width="16.93%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973206_p36285299"><a name="en-us_topic_0057973206_p36285299"></a><a name="en-us_topic_0057973206_p36285299"></a>available</p>
</td>
<td class="cellrowborder" valign="top" width="15.620000000000001%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973206_p53428078"><a name="en-us_topic_0057973206_p53428078"></a><a name="en-us_topic_0057973206_p53428078"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="67.45%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973206_p32026686"><a name="en-us_topic_0057973206_p32026686"></a><a name="en-us_topic_0057973206_p32026686"></a>Specifies the AZ status.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="en-us_topic_0057973206_section32241172"></a>

```
GET https://{endpoint}/v2/9c53a566cb3443ab910cf0daebca90c4/os-availability-zone
GET https://{endpoint}/v2.1/9c53a566cb3443ab910cf0daebca90c4/os-availability-zone
```

## Example Response<a name="section19399181019572"></a>

```
{
	"availabilityZoneInfo": [{
		"zoneState": {
			"available": true
		},
		"hosts": null,
		"zoneName": "az1.dc1"
	},
	{
		"zoneState": {
			"available": true
		},
		"hosts": null,
		"zoneName": "vmware.az1"
	}]
}
```

## Returned Values<a name="en-us_topic_0057973206_en-us_topic_0020212692_section22960139"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

