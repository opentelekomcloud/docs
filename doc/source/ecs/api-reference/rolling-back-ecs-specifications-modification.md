# Rolling Back ECS Specifications Modification<a name="EN-US_TOPIC_0028714263"></a>

## Function<a name="section53922917165259"></a>

This API is used to roll back the specifications modification of an ECS.

## Constraints<a name="section64211377173223"></a>

After the rollback, the data modified during migration will be lost.

Before calling this API, ensure that the ECS status \(which can be queried using the API for querying details about the ECS\) meets the following requirements:

OS-EXT-STS:vm\_state=resized

status=VERIFY\_RESIZE

## URI<a name="section51121191165259"></a>

POST /v2/\{project\_id\}/servers/\{server\_id\}/action

POST /v2.1/\{project\_id\}/servers/\{server\_id\}/action

[Table 1](#table60562285165259)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table60562285165259"></a>
<table><thead align="left"><tr id="row4861884165259"><th class="cellrowborder" valign="top" width="16.98%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.36%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.66%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row63809876165259"><td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.1 "><p id="p1217433165259"><a name="p1217433165259"></a><a name="p1217433165259"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.2 "><p id="p31503226165259"><a name="p31503226165259"></a><a name="p31503226165259"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.66%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row14620905165259"><td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.1 "><p id="p43442641165259"><a name="p43442641165259"></a><a name="p43442641165259"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.2 "><p id="p29193009165259"><a name="p29193009165259"></a><a name="p29193009165259"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.66%" headers="mcps1.2.4.1.3 "><p id="p15823538165259"><a name="p15823538165259"></a><a name="p15823538165259"></a>Specifies the ECS ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section8194118165259"></a>

[Table 2](#table7412452165259)  describes the request parameters.

**Table  2**  Request parameters

<a name="table7412452165259"></a>
<table><thead align="left"><tr id="row51747874165259"><th class="cellrowborder" valign="top" width="16.89%" id="mcps1.2.5.1.1"><p id="en-us_topic_0057973030_p1494644"><a name="en-us_topic_0057973030_p1494644"></a><a name="en-us_topic_0057973030_p1494644"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.42%" id="mcps1.2.5.1.2"><p id="p4412161712114"><a name="p4412161712114"></a><a name="p4412161712114"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.340000000000003%" id="mcps1.2.5.1.3"><p id="en-us_topic_0057973030_p53957349"><a name="en-us_topic_0057973030_p53957349"></a><a name="en-us_topic_0057973030_p53957349"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51.35000000000001%" id="mcps1.2.5.1.4"><p id="en-us_topic_0057973030_p14912584"><a name="en-us_topic_0057973030_p14912584"></a><a name="en-us_topic_0057973030_p14912584"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row57740237165259"><td class="cellrowborder" valign="top" width="16.89%" headers="mcps1.2.5.1.1 "><p id="p46447620165259"><a name="p46447620165259"></a><a name="p46447620165259"></a>revertResize</p>
</td>
<td class="cellrowborder" valign="top" width="17.42%" headers="mcps1.2.5.1.2 "><p id="p14412121762111"><a name="p14412121762111"></a><a name="p14412121762111"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.340000000000003%" headers="mcps1.2.5.1.3 "><p id="p4160867165259"><a name="p4160867165259"></a><a name="p4160867165259"></a>Null</p>
</td>
<td class="cellrowborder" valign="top" width="51.35000000000001%" headers="mcps1.2.5.1.4 "><p id="p9531549165259"><a name="p9531549165259"></a><a name="p9531549165259"></a>Confirms the rollback of the ECS specification modification.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section58140617165259"></a>

None

## Example Request<a name="section13101131612713"></a>

```
POST https://{endpoint}/v2/{project_id}/servers/{server_id}/action
POST https://{endpoint}/v2.1/{project_id}/servers/{server_id}/action
```

```
{
    "revertResize" : null
}
```

## Example Response<a name="section6944191611111"></a>

None

## Returned Values<a name="section38817202165259"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

