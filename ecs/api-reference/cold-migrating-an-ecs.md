# Cold Migrating an ECS<a name="EN-US_TOPIC_0132905656"></a>

## Function<a name="en-us_topic_0092803065_en-us_topic_0067161469_en-us_topic_0057973179_section16588975"></a>

-   An ECS deployed on a DeH can be migrated to another DeH.
-   An ECS deployed on a DeH can be migrated to a public resource pool.
-   An ECS deployed in a public resource pool can be migrated to a DeH.

## Constraints<a name="section10197106104013"></a>

-   This API is supported by DeHs only.
-   Only a stopped ECS can be cold migrated.
-   Existing constraints of the native cold migration API are inherited.

## URI<a name="section48412952"></a>

POST /v1/\{project\_id\}/cloudservers/\{server\_id\}/migrate

[Table 1](#table29396722)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table29396722"></a>
<table><thead align="left"><tr id="row15658103"><th class="cellrowborder" valign="top" width="16.79%" id="mcps1.2.4.1.1"><p id="p60346796"><a name="p60346796"></a><a name="p60346796"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.16%" id="mcps1.2.4.1.2"><p id="p56252285"><a name="p56252285"></a><a name="p56252285"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="66.05%" id="mcps1.2.4.1.3"><p id="p60141268"><a name="p60141268"></a><a name="p60141268"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row39604502"><td class="cellrowborder" valign="top" width="16.79%" headers="mcps1.2.4.1.1 "><p id="p53848109"><a name="p53848109"></a><a name="p53848109"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.16%" headers="mcps1.2.4.1.2 "><p id="p66729601"><a name="p66729601"></a><a name="p66729601"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.05%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row59061958"><td class="cellrowborder" valign="top" width="16.79%" headers="mcps1.2.4.1.1 "><p id="p19289328"><a name="p19289328"></a><a name="p19289328"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.16%" headers="mcps1.2.4.1.2 "><p id="p18931763"><a name="p18931763"></a><a name="p18931763"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.05%" headers="mcps1.2.4.1.3 "><p id="p57077814"><a name="p57077814"></a><a name="p57077814"></a>Specifies the ECS ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section33063388"></a>

[Table 2](#table6742880)  describes the request parameters.

**Table  2**  Request parameters

<a name="table6742880"></a>
<table><thead align="left"><tr id="row13072760"><th class="cellrowborder" valign="top" width="16.73%" id="mcps1.2.5.1.1"><p id="p52260639"><a name="p52260639"></a><a name="p52260639"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.29%" id="mcps1.2.5.1.2"><p id="p5253358"><a name="p5253358"></a><a name="p5253358"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15.98%" id="mcps1.2.5.1.3"><p id="p22868878"><a name="p22868878"></a><a name="p22868878"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="p40439847"><a name="p40439847"></a><a name="p40439847"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row54402144"><td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.1 "><p id="p44497505"><a name="p44497505"></a><a name="p44497505"></a>migrate</p>
</td>
<td class="cellrowborder" valign="top" width="17.29%" headers="mcps1.2.5.1.2 "><p id="p47528147"><a name="p47528147"></a><a name="p47528147"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.98%" headers="mcps1.2.5.1.3 "><p id="p24574685"><a name="p24574685"></a><a name="p24574685"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="p63988077"><a name="p63988077"></a><a name="p63988077"></a>Specifies the ECS to be migrated. For details, see <a href="#table7657338">Table 3</a>.</p>
<p id="p069552312476"><a name="p069552312476"></a><a name="p069552312476"></a>When migrating an ECS from a DeH to a public resource pool, the <strong id="b842352706211555"><a name="b842352706211555"></a><a name="b842352706211555"></a>migrate</strong> value is null.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **migrate**  field description

<a name="table7657338"></a>
<table><thead align="left"><tr id="row17725233"><th class="cellrowborder" valign="top" width="19.3%" id="mcps1.2.5.1.1"><p id="p212320319517"><a name="p212320319517"></a><a name="p212320319517"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.62%" id="mcps1.2.5.1.2"><p id="p141231538517"><a name="p141231538517"></a><a name="p141231538517"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="13.19%" id="mcps1.2.5.1.3"><p id="p01231137517"><a name="p01231137517"></a><a name="p01231137517"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49.89%" id="mcps1.2.5.1.4"><p id="p101231038519"><a name="p101231038519"></a><a name="p101231038519"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row4862529914328"><td class="cellrowborder" valign="top" width="19.3%" headers="mcps1.2.5.1.1 "><p id="p39963283143216"><a name="p39963283143216"></a><a name="p39963283143216"></a>dedicated_host_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.62%" headers="mcps1.2.5.1.2 "><p id="p6216169514328"><a name="p6216169514328"></a><a name="p6216169514328"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.19%" headers="mcps1.2.5.1.3 "><p id="p193254814328"><a name="p193254814328"></a><a name="p193254814328"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.89%" headers="mcps1.2.5.1.4 "><p id="p10407151510462"><a name="p10407151510462"></a><a name="p10407151510462"></a>Specifies the DeH ID.</p>
<p id="p2231868514328"><a name="p2231868514328"></a><a name="p2231868514328"></a>This parameter takes effect when an ECS is migrated from a public resource pool to a DeH or when an ECS is migrated between DeHs.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section29135036"></a>

See  [Responses \(Task\)](responses-(task).md).

## Example Request<a name="section1791154205019"></a>

```
POST https://{endpoint}/v1/{project_id}/cloudservers/{server_id}/migrate
```

```
{
    "migrate": {
        "dedicated_host_id": "459a2b9d-804a-4745-ab19-a113bb1b4ddc"
    }
}
Or
{
    "migrate": null
}
```

## Example Response<a name="section20192755104713"></a>

None

## Returned Values<a name="section27037160"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

## Error Codes<a name="section85821649202813"></a>

See  [Error Code Description](error-code-description.md).

