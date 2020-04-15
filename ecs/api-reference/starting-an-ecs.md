# Starting an ECS<a name="EN-US_TOPIC_0020212648"></a>

## Function<a name="section5894231"></a>

This API is used to start a single ECS.

## URI<a name="section53048087"></a>

POST /v2/\{project\_id\}/servers/\{server\_id\}/action

POST /v2.1/\{project\_id\}/servers/\{server\_id\}/action

[Table 1](#table48630964)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table48630964"></a>
<table><thead align="left"><tr id="row59481773"><th class="cellrowborder" valign="top" width="16.98%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.169999999999998%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.85%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row2533231"><td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.1 "><p id="p3865173"><a name="p3865173"></a><a name="p3865173"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p44643603"><a name="p44643603"></a><a name="p44643603"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.85%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row64497130"><td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.1 "><p id="p56885004"><a name="p56885004"></a><a name="p56885004"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p44282627"><a name="p44282627"></a><a name="p44282627"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.85%" headers="mcps1.2.4.1.3 "><p id="p30123063"><a name="p30123063"></a><a name="p30123063"></a>Specifies the ECS ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section7670737"></a>

[Table 2](#table48180537)  describes the request parameters.

**Table  2**  Request parameters

<a name="table48180537"></a>
<table><thead align="left"><tr id="row15499871"><th class="cellrowborder" valign="top" width="16.91%" id="mcps1.2.5.1.1"><p id="p47530006"><a name="p47530006"></a><a name="p47530006"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.29%" id="mcps1.2.5.1.2"><p id="p24725298"><a name="p24725298"></a><a name="p24725298"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.860000000000001%" id="mcps1.2.5.1.3"><p id="p56592155"><a name="p56592155"></a><a name="p56592155"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50.94%" id="mcps1.2.5.1.4"><p id="p20561848"><a name="p20561848"></a><a name="p20561848"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row54897010"><td class="cellrowborder" valign="top" width="16.91%" headers="mcps1.2.5.1.1 "><p id="p17472816"><a name="p17472816"></a><a name="p17472816"></a>os-start</p>
</td>
<td class="cellrowborder" valign="top" width="17.29%" headers="mcps1.2.5.1.2 "><p id="p6011995"><a name="p6011995"></a><a name="p6011995"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.860000000000001%" headers="mcps1.2.5.1.3 "><p id="p17209562"><a name="p17209562"></a><a name="p17209562"></a>Null</p>
</td>
<td class="cellrowborder" valign="top" width="50.94%" headers="mcps1.2.5.1.4 "><p id="p63522246"><a name="p63522246"></a><a name="p63522246"></a>Specifies the operation to start the ECS. The data structure is empty.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section1927776"></a>

None

## Example Request<a name="section050015816355"></a>

```
POST https://{endpoint}/v2.1/{project_id}/servers/{server_id}/action
```

```
{
    "os-start": {}
                    }
```

## Example Response<a name="section74690516211"></a>

None

## Returned Values<a name="section17349988"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

