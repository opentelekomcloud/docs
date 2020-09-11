# Querying the extra\_specs Value for an ECS Flavor<a name="EN-US_TOPIC_0065817706"></a>

## Function<a name="en-us_topic_0057973064_section33891944"></a>

This API is used to query the  **extra\_specs**  value for a specified ECS flavor.

## URI<a name="en-us_topic_0057973064_section36592045"></a>

GET /v2/\{project\_id\}/flavors/\{flavors\_id\}/os-extra\_specs

GET /v2.1/\{project\_id\}/flavors/\{flavors\_id\}/os-extra\_specs

[Table 1](#en-us_topic_0057973064_table47154420)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="en-us_topic_0057973064_table47154420"></a>
<table><thead align="left"><tr id="en-us_topic_0057973064_row324668"><th class="cellrowborder" valign="top" width="16.6%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.36%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="66.03999999999999%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973064_row17004965"><td class="cellrowborder" valign="top" width="16.6%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973064_p35224963"><a name="en-us_topic_0057973064_p35224963"></a><a name="en-us_topic_0057973064_p35224963"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973064_p34649765"><a name="en-us_topic_0057973064_p34649765"></a><a name="en-us_topic_0057973064_p34649765"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.03999999999999%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0057973064_row26746391"><td class="cellrowborder" valign="top" width="16.6%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973064_p18974100"><a name="en-us_topic_0057973064_p18974100"></a><a name="en-us_topic_0057973064_p18974100"></a>flavors_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973064_p60507121"><a name="en-us_topic_0057973064_p60507121"></a><a name="en-us_topic_0057973064_p60507121"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.03999999999999%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973064_p2129750"><a name="en-us_topic_0057973064_p2129750"></a><a name="en-us_topic_0057973064_p2129750"></a>Specifies the flavor ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0057973064_section33381957"></a>

None

## Response<a name="en-us_topic_0057973064_section32002165"></a>

[Table 2](#en-us_topic_0057973064_table28168569)  describes the response parameters.

**Table  2**  Response parameters

<a name="en-us_topic_0057973064_table28168569"></a>
<table><thead align="left"><tr id="en-us_topic_0057973064_row26406300"><th class="cellrowborder" valign="top" width="16.88%" id="mcps1.2.4.1.1"><p id="p110452114597"><a name="p110452114597"></a><a name="p110452114597"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.180000000000001%" id="mcps1.2.4.1.2"><p id="p71044217595"><a name="p71044217595"></a><a name="p71044217595"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="68.94%" id="mcps1.2.4.1.3"><p id="p15104102175910"><a name="p15104102175910"></a><a name="p15104102175910"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973064_row46433444"><td class="cellrowborder" valign="top" width="16.88%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973064_p3012613"><a name="en-us_topic_0057973064_p3012613"></a><a name="en-us_topic_0057973064_p3012613"></a>extra_specs</p>
</td>
<td class="cellrowborder" valign="top" width="14.180000000000001%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973064_p42695066"><a name="en-us_topic_0057973064_p42695066"></a><a name="en-us_topic_0057973064_p42695066"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="68.94%" headers="mcps1.2.4.1.3 "><p id="p1679511281174"><a name="p1679511281174"></a><a name="p1679511281174"></a>Specifies the key-value pair of an ECS flavor.</p>
<p id="p166420315234"><a name="p166420315234"></a><a name="p166420315234"></a>For details about the returned fields, see the <strong id="b1741454723911"><a name="b1741454723911"></a><a name="b1741454723911"></a>os_extra_specs</strong> field description in "Querying Details About Flavors and Extended Flavor Information".</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="en-us_topic_0057973064_section19584029"></a>

```
GET https://{endpoint}/v2/743b4c0428d94531b9f2add666642e6b/flavors/c3.2xlarge.2/os-extra_specs
GET https://{endpoint}/v2.1/743b4c0428d94531b9f2add666642e6b/flavors/c3.2xlarge.2/os-extra_specs
```

## Example Response<a name="section1679819123313"></a>

```
{
    "extra_specs": {
        "ecs:performancetype": "computingv3",
        "resource_type": "IOoptimizedC3_2"
    }
}
```

## Returned Values<a name="en-us_topic_0057973064_en-us_topic_0020212692_section22960139"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

