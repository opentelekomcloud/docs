# Confirming ECS Specifications Modification<a name="EN-US_TOPIC_0028714262"></a>

## Function<a name="section14742295165029"></a>

This API is used to confirm the specifications modification of an ECS.

## Constraints<a name="section54952513173158"></a>

Before calling this API, ensure that the ECS status \(which can be queried using the API for querying details about the ECS\) meets the following requirements:

OS-EXT-STS:vm\_state=resized

status=VERIFY\_RESIZE

## URI<a name="section9714850165029"></a>

POST /v2/\{project\_id\}/servers/\{server\_id\}/action

POST /v2.1/\{project\_id\}/servers/\{server\_id\}/action

[Table 1](#table54458463165029)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table54458463165029"></a>
<table><thead align="left"><tr id="row24545956165029"><th class="cellrowborder" valign="top" width="16.6%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.16%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="66.24%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row42809334165029"><td class="cellrowborder" valign="top" width="16.6%" headers="mcps1.2.4.1.1 "><p id="p45004064165029"><a name="p45004064165029"></a><a name="p45004064165029"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.16%" headers="mcps1.2.4.1.2 "><p id="p21450595165029"><a name="p21450595165029"></a><a name="p21450595165029"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.24%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row1118615165029"><td class="cellrowborder" valign="top" width="16.6%" headers="mcps1.2.4.1.1 "><p id="p23498973165029"><a name="p23498973165029"></a><a name="p23498973165029"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.16%" headers="mcps1.2.4.1.2 "><p id="p24368697165029"><a name="p24368697165029"></a><a name="p24368697165029"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.24%" headers="mcps1.2.4.1.3 "><p id="p27707408165029"><a name="p27707408165029"></a><a name="p27707408165029"></a>Specifies the ECS ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section48040086165029"></a>

[Table 2](#table47783938165029)  describes the request parameters.

**Table  2**  Request parameters

<a name="table47783938165029"></a>
<table><thead align="left"><tr id="row60288789165029"><th class="cellrowborder" valign="top" width="18.6%" id="mcps1.2.5.1.1"><p id="en-us_topic_0057973030_p1494644"><a name="en-us_topic_0057973030_p1494644"></a><a name="en-us_topic_0057973030_p1494644"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.48%" id="mcps1.2.5.1.2"><p id="p11164206213"><a name="p11164206213"></a><a name="p11164206213"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="12.78%" id="mcps1.2.5.1.3"><p id="en-us_topic_0057973030_p53957349"><a name="en-us_topic_0057973030_p53957349"></a><a name="en-us_topic_0057973030_p53957349"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51.13999999999999%" id="mcps1.2.5.1.4"><p id="en-us_topic_0057973030_p14912584"><a name="en-us_topic_0057973030_p14912584"></a><a name="en-us_topic_0057973030_p14912584"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row50942237165029"><td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.2.5.1.1 "><p id="p32680571165029"><a name="p32680571165029"></a><a name="p32680571165029"></a>confirmResize</p>
</td>
<td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.2.5.1.2 "><p id="p1164140102115"><a name="p1164140102115"></a><a name="p1164140102115"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="12.78%" headers="mcps1.2.5.1.3 "><p id="p29880605165029"><a name="p29880605165029"></a><a name="p29880605165029"></a>Null</p>
</td>
<td class="cellrowborder" valign="top" width="51.13999999999999%" headers="mcps1.2.5.1.4 "><p id="p60747468165029"><a name="p60747468165029"></a><a name="p60747468165029"></a>Confirms the modification to ECS specifications.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section4596622165029"></a>

None

## Example Request<a name="section1194124632513"></a>

```
POST https://{endpoint}/v2/{project_id}/servers/{server_id}/action
POST https://{endpoint}/v2.1/{project_id}/servers/{server_id}/action
```

```
{
    "confirmResize" : null
}
```

## Example Response<a name="section1233763710102"></a>

None

## Returned Values<a name="section62603593165029"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

