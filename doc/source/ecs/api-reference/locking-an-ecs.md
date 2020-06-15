# Locking an ECS<a name="EN-US_TOPIC_0065817690"></a>

## Function<a name="en-us_topic_0057973175_section39224329"></a>

This API is used to lock an ECS.

Tenants are only allowed to lock their own ECSs. After their ECSs are locked, tenants are not allowed to manage the ECSs.

## URI<a name="en-us_topic_0057973175_section17474649"></a>

POST /v2/\{project\_id\}/servers/\{server\_id\}/action

POST /v2.1/\{project\_id\}/servers/\{server\_id\}/action

[Table 1](#en-us_topic_0057973175_table32475667)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="en-us_topic_0057973175_table32475667"></a>
<table><thead align="left"><tr id="en-us_topic_0057973175_row44937496"><th class="cellrowborder" valign="top" width="16.79%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.169999999999998%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="66.03999999999999%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973175_row1664874"><td class="cellrowborder" valign="top" width="16.79%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973175_p637140"><a name="en-us_topic_0057973175_p637140"></a><a name="en-us_topic_0057973175_p637140"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973175_p51608407"><a name="en-us_topic_0057973175_p51608407"></a><a name="en-us_topic_0057973175_p51608407"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.03999999999999%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0057973175_row41565035"><td class="cellrowborder" valign="top" width="16.79%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973175_p11324657"><a name="en-us_topic_0057973175_p11324657"></a><a name="en-us_topic_0057973175_p11324657"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973175_p44882061"><a name="en-us_topic_0057973175_p44882061"></a><a name="en-us_topic_0057973175_p44882061"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.03999999999999%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973175_p11568292"><a name="en-us_topic_0057973175_p11568292"></a><a name="en-us_topic_0057973175_p11568292"></a>Specifies the ECS ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0057973175_section55444361"></a>

[Table 2](#en-us_topic_0057973175_table18228066)  describes the request parameters.

**Table  2**  Request parameters

<a name="en-us_topic_0057973175_table18228066"></a>
<table><thead align="left"><tr id="en-us_topic_0057973175_row66497515"><th class="cellrowborder" valign="top" width="16.73%" id="mcps1.2.5.1.1"><p id="en-us_topic_0057973175_p17589653"><a name="en-us_topic_0057973175_p17589653"></a><a name="en-us_topic_0057973175_p17589653"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.66%" id="mcps1.2.5.1.2"><p id="en-us_topic_0057973175_p15475779"><a name="en-us_topic_0057973175_p15475779"></a><a name="en-us_topic_0057973175_p15475779"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="18.05%" id="mcps1.2.5.1.3"><p id="en-us_topic_0057973175_p45578590"><a name="en-us_topic_0057973175_p45578590"></a><a name="en-us_topic_0057973175_p45578590"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="50.56%" id="mcps1.2.5.1.4"><p id="en-us_topic_0057973175_p878285"><a name="en-us_topic_0057973175_p878285"></a><a name="en-us_topic_0057973175_p878285"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973175_row4032249"><td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973175_p58176713"><a name="en-us_topic_0057973175_p58176713"></a><a name="en-us_topic_0057973175_p58176713"></a>lock</p>
</td>
<td class="cellrowborder" valign="top" width="14.66%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057973175_p14693285"><a name="en-us_topic_0057973175_p14693285"></a><a name="en-us_topic_0057973175_p14693285"></a>Null</p>
</td>
<td class="cellrowborder" valign="top" width="18.05%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973175_p49305462"><a name="en-us_topic_0057973175_p49305462"></a><a name="en-us_topic_0057973175_p49305462"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="50.56%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973175_p34319524"><a name="en-us_topic_0057973175_p34319524"></a><a name="en-us_topic_0057973175_p34319524"></a>Locks an ECS.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="en-us_topic_0057973175_section7967191653319"></a>

None

## Example Request<a name="en-us_topic_0057973175_section1296841643314"></a>

```
POST https://{endpoint}/v2/{project_id}/servers/{server_id}/action
POST https://{endpoint}/v2.1/{project_id}/servers/{server_id}/action
```

```
{
    "lock": null
}
```

## Example Response<a name="section243517360410"></a>

None

## Returned Values<a name="en-us_topic_0057973175_section40414779"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

