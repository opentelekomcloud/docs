# Modifying the Specifications of an ECS<a name="EN-US_TOPIC_0028714261"></a>

## Function<a name="section5763990416457"></a>

This API is used to modify the specifications of an ECS.

For a running ECS, the system will automatically stop the ECS, copy the ECS data to the target node which can be the source node, and then restart the ECS.

This API supports automatic rollback if the underlying resources are insufficient.

This API must be used with the API for verifying ECS specifications modification \(POST /v2/\{project\_id\}/servers/\{server\_id\}/action\) or the API for rolling back ECS specifications modification \(POST /v2/\{project\_id\}/servers/\{server\_id\}/action\) if an ECS is detected to be in  **VERIFY\_RESIZE**  state and its  **OS-EXT-STS:vm\_state**  is  **RESIZED**.

## URI<a name="section934152916457"></a>

POST /v2/\{project\_id\}/servers/\{server\_id\}/action

POST /v2.1/\{project\_id\}/servers/\{server\_id\}/action

[Table 1](#table3588765216457)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table3588765216457"></a>
<table><thead align="left"><tr id="row3213599316457"><th class="cellrowborder" valign="top" width="16.61%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.169999999999998%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="66.22%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row5283576216457"><td class="cellrowborder" valign="top" width="16.61%" headers="mcps1.2.4.1.1 "><p id="p5183832116457"><a name="p5183832116457"></a><a name="p5183832116457"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p3815449716457"><a name="p3815449716457"></a><a name="p3815449716457"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.22%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row3155913116457"><td class="cellrowborder" valign="top" width="16.61%" headers="mcps1.2.4.1.1 "><p id="p615277916457"><a name="p615277916457"></a><a name="p615277916457"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p2861306316457"><a name="p2861306316457"></a><a name="p2861306316457"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.22%" headers="mcps1.2.4.1.3 "><p id="p3595679216457"><a name="p3595679216457"></a><a name="p3595679216457"></a>Specifies the ECS ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section5517568016457"></a>

[Table 2](#table2242889516457)  describes the request parameters.

**Table  2**  Request parameters

<a name="table2242889516457"></a>
<table><thead align="left"><tr id="row3650219016457"><th class="cellrowborder" valign="top" width="16.648335166483353%" id="mcps1.2.5.1.1"><p id="en-us_topic_0057973030_p1494644"><a name="en-us_topic_0057973030_p1494644"></a><a name="en-us_topic_0057973030_p1494644"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.24827517248275%" id="mcps1.2.5.1.2"><p id="en-us_topic_0057973030_p8469150"><a name="en-us_topic_0057973030_p8469150"></a><a name="en-us_topic_0057973030_p8469150"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.258574142585742%" id="mcps1.2.5.1.3"><p id="en-us_topic_0057973030_p53957349"><a name="en-us_topic_0057973030_p53957349"></a><a name="en-us_topic_0057973030_p53957349"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51.84481551844815%" id="mcps1.2.5.1.4"><p id="en-us_topic_0057973030_p14912584"><a name="en-us_topic_0057973030_p14912584"></a><a name="en-us_topic_0057973030_p14912584"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1418337416457"><td class="cellrowborder" valign="top" width="16.648335166483353%" headers="mcps1.2.5.1.1 "><p id="p800266116457"><a name="p800266116457"></a><a name="p800266116457"></a>flavorRef</p>
</td>
<td class="cellrowborder" valign="top" width="17.24827517248275%" headers="mcps1.2.5.1.2 "><p id="p2633272116457"><a name="p2633272116457"></a><a name="p2633272116457"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.258574142585742%" headers="mcps1.2.5.1.3 "><p id="p4423583316457"><a name="p4423583316457"></a><a name="p4423583316457"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="51.84481551844815%" headers="mcps1.2.5.1.4 "><p id="p341898416457"><a name="p341898416457"></a><a name="p341898416457"></a>Specifies the new flavor ID or URI.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section1759889416457"></a>

None

## Example Request<a name="section1264820314241"></a>

```
POST https://{endpoint}/v2/{project_id}/servers/{server_id}/action
POST https://{endpoint}/v2.1/{project_id}/servers/{server_id}/action
```

```
{
    "resize" : {
        "flavorRef" : "4",
        "dedicated_host_id": "459a2b9d-804a-4745-ab19-a113bb1b4ddc"
    }
}
```

## Example Response<a name="section47159401499"></a>

None

## Returned Values<a name="section1180080516457"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

