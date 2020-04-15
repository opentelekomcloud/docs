# Unlocking an ECS<a name="EN-US_TOPIC_0065817691"></a>

## Function<a name="en-us_topic_0057973176_section38263289"></a>

This API is used to unlock an ECS.

After an ECS is unlocked, common users are allowed to manage the ECS.

## URI<a name="en-us_topic_0057973176_section8825287"></a>

POST /v2/\{project\_id\}/servers/\{server\_id\}/action

POST /v2.1/\{project\_id\}/servers/\{server\_id\}/action

[Table 1](#en-us_topic_0057973176_table32475667)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="en-us_topic_0057973176_table32475667"></a>
<table><thead align="left"><tr id="en-us_topic_0057973176_row44937496"><th class="cellrowborder" valign="top" width="16.41%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.549999999999997%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="66.03999999999999%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973176_row1664874"><td class="cellrowborder" valign="top" width="16.41%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973176_p637140"><a name="en-us_topic_0057973176_p637140"></a><a name="en-us_topic_0057973176_p637140"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.549999999999997%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973176_p51608407"><a name="en-us_topic_0057973176_p51608407"></a><a name="en-us_topic_0057973176_p51608407"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.03999999999999%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0057973176_row41565035"><td class="cellrowborder" valign="top" width="16.41%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973176_p11324657"><a name="en-us_topic_0057973176_p11324657"></a><a name="en-us_topic_0057973176_p11324657"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.549999999999997%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973176_p44882061"><a name="en-us_topic_0057973176_p44882061"></a><a name="en-us_topic_0057973176_p44882061"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.03999999999999%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973176_p11568292"><a name="en-us_topic_0057973176_p11568292"></a><a name="en-us_topic_0057973176_p11568292"></a>Specifies the ECS ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0057973176_section58292189"></a>

[Table 2](#en-us_topic_0057973176_table65978805)  describes the request parameters.

**Table  2**  Request parameters

<a name="en-us_topic_0057973176_table65978805"></a>
<table><thead align="left"><tr id="en-us_topic_0057973176_row45865265"><th class="cellrowborder" valign="top" width="16.39%" id="mcps1.2.5.1.1"><p id="en-us_topic_0057973176_p24098979"><a name="en-us_topic_0057973176_p24098979"></a><a name="en-us_topic_0057973176_p24098979"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.599999999999998%" id="mcps1.2.5.1.2"><p id="p6342334101715"><a name="p6342334101715"></a><a name="p6342334101715"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15.129999999999999%" id="mcps1.2.5.1.3"><p id="en-us_topic_0057973176_p5860269"><a name="en-us_topic_0057973176_p5860269"></a><a name="en-us_topic_0057973176_p5860269"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50.88%" id="mcps1.2.5.1.4"><p id="en-us_topic_0057973176_p62959532"><a name="en-us_topic_0057973176_p62959532"></a><a name="en-us_topic_0057973176_p62959532"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973176_row66557295"><td class="cellrowborder" valign="top" width="16.39%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973176_p22431852"><a name="en-us_topic_0057973176_p22431852"></a><a name="en-us_topic_0057973176_p22431852"></a>unlock</p>
</td>
<td class="cellrowborder" valign="top" width="17.599999999999998%" headers="mcps1.2.5.1.2 "><p id="p1434216345178"><a name="p1434216345178"></a><a name="p1434216345178"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.129999999999999%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973176_p5040713"><a name="en-us_topic_0057973176_p5040713"></a><a name="en-us_topic_0057973176_p5040713"></a>Null</p>
</td>
<td class="cellrowborder" valign="top" width="50.88%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973176_p54558660"><a name="en-us_topic_0057973176_p54558660"></a><a name="en-us_topic_0057973176_p54558660"></a>Unlocks an ECS.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="en-us_topic_0057973176_section1628434413713"></a>

None

## Example Request<a name="en-us_topic_0057973176_section14285144433715"></a>

```
POST https://{endpoint}/v2/{project_id}/servers/{server_id}/action
POST https://{endpoint}/v2.1/{project_id}/servers/{server_id}/action
```

```
{
   "unlock": null 
}
```

## Example Response<a name="section177213225519"></a>

None

## Returned Values<a name="en-us_topic_0057973176_section1642564"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

