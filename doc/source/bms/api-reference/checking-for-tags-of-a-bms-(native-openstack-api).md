# Checking for Tags of a BMS \(Native OpenStack API\)<a name="EN-US_TOPIC_0060410930"></a>

## Function<a name="section66970384144623"></a>

This API is used to check whether a BMS has a specified tag.

You are required to use the HTTP header  **X-OpenStack-Nova-API-Version: 2.26**  to specify the micro version on the client.

## URI<a name="section20295111144623"></a>

GET /v2.1/\{project\_id\}/servers/\{server\_id\}/tags/\{tag\}

[Table 1](#table6300135020116)  lists the parameters.

**Table  1**  Parameter description

<a name="table6300135020116"></a>
<table><thead align="left"><tr id="row6301650413"><th class="cellrowborder" valign="top" width="24.892489248924893%" id="mcps1.2.4.1.1"><p id="p29933752144623"><a name="p29933752144623"></a><a name="p29933752144623"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="24.892489248924893%" id="mcps1.2.4.1.2"><p id="p8714817144623"><a name="p8714817144623"></a><a name="p8714817144623"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="50.215021502150215%" id="mcps1.2.4.1.3"><p id="p34811538144623"><a name="p34811538144623"></a><a name="p34811538144623"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1830145014117"><td class="cellrowborder" valign="top" width="24.892489248924893%" headers="mcps1.2.4.1.1 "><p id="p27039406144623"><a name="p27039406144623"></a><a name="p27039406144623"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="24.892489248924893%" headers="mcps1.2.4.1.2 "><p id="p42708297144623"><a name="p42708297144623"></a><a name="p42708297144623"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="50.215021502150215%" headers="mcps1.2.4.1.3 "><p id="p36820045144623"><a name="p36820045144623"></a><a name="p36820045144623"></a>Specifies the project ID.</p>
<p id="p9141450142010"><a name="p9141450142010"></a><a name="p9141450142010"></a>For how to obtain the project ID, see <a href="https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328009.html" target="_blank" rel="noopener noreferrer">Obtaining Required Information</a>.</p>
</td>
</tr>
<tr id="row030112504112"><td class="cellrowborder" valign="top" width="24.892489248924893%" headers="mcps1.2.4.1.1 "><p id="p65376104144623"><a name="p65376104144623"></a><a name="p65376104144623"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="24.892489248924893%" headers="mcps1.2.4.1.2 "><p id="p60973080144623"><a name="p60973080144623"></a><a name="p60973080144623"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="50.215021502150215%" headers="mcps1.2.4.1.3 "><p id="p39872428144623"><a name="p39872428144623"></a><a name="p39872428144623"></a>Specifies the <span id="text166801037185316"><a name="text166801037185316"></a><a name="text166801037185316"></a>BMS</span><span id="text96808374535"><a name="text96808374535"></a><a name="text96808374535"></a></span> ID.</p>
<p id="p29791113277"><a name="p29791113277"></a><a name="p29791113277"></a>You can obtain the BMS ID from the <span id="en-us_topic_0113746489_text013014803615"><a name="en-us_topic_0113746489_text013014803615"></a><a name="en-us_topic_0113746489_text013014803615"></a>BMS</span><span id="en-us_topic_0113746489_text10131448133612"><a name="en-us_topic_0113746489_text10131448133612"></a><a name="en-us_topic_0113746489_text10131448133612"></a></span> console or using the <a href="querying-bmss-(native-openstack-api).md">Querying BMSs (Native OpenStack API)</a> API.</p>
</td>
</tr>
<tr id="row33016506115"><td class="cellrowborder" valign="top" width="24.892489248924893%" headers="mcps1.2.4.1.1 "><p id="p8862197144623"><a name="p8862197144623"></a><a name="p8862197144623"></a>tag</p>
</td>
<td class="cellrowborder" valign="top" width="24.892489248924893%" headers="mcps1.2.4.1.2 "><p id="p46749363144623"><a name="p46749363144623"></a><a name="p46749363144623"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="50.215021502150215%" headers="mcps1.2.4.1.3 "><p id="p28602098144623"><a name="p28602098144623"></a><a name="p28602098144623"></a>Specifies the key of the tag to be queried.</p>
<p id="p15688120112814"><a name="p15688120112814"></a><a name="p15688120112814"></a>Constraints:</p>
<a name="ul926591942418"></a><a name="ul926591942418"></a><ul id="ul926591942418"><li>URL encoding is required for special characters.</li><li>If no tag key is specified, all tags of the <span id="text1873714012533"><a name="text1873714012533"></a><a name="text1873714012533"></a>BMS</span><span id="text197378408537"><a name="text197378408537"></a><a name="text197378408537"></a></span> are displayed.</li></ul>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section56092298144623"></a>

-   Request parameters

    None

-   Example request

    ```
    GET https://{ECS Endpoint}/v2.1/bbf1946d374b44a0a2a95533562ba954/servers/2d85af7c-cbfe-40c5-a378-4d03b42fb0e2/tags/{tag}
    ```


## Response Message<a name="section21987090144623"></a>

If the specified tag exists, no response is returned.

If the specified tag does not exist, the response is as follows:

```
{
    "itemNotFound": {
        "message": "Server 2d85af7c-cbfe-40c5-a378-4d03b42fb0e2 has no tag 'abc'",
        "code": 404
    }
}
```

## Returned Values<a name="section27037160"></a>

Normal values

<a name="en-us_topic_0053158659_table753804619176"></a>
<table><thead align="left"><tr id="en-us_topic_0053158659_row10735134615172"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="en-us_topic_0053158659_p19735204616177"><a name="en-us_topic_0053158659_p19735204616177"></a><a name="en-us_topic_0053158659_p19735204616177"></a>Returned Values</p>
</th>
<th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="en-us_topic_0053158659_p207355465176"><a name="en-us_topic_0053158659_p207355465176"></a><a name="en-us_topic_0053158659_p207355465176"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0053158659_row1473514621713"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0053158659_p13735144611178"><a name="en-us_topic_0053158659_p13735144611178"></a><a name="en-us_topic_0053158659_p13735144611178"></a>204</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0053158659_p81516575011"><a name="en-us_topic_0053158659_p81516575011"></a><a name="en-us_topic_0053158659_p81516575011"></a>The server has processed the request but did not return any content.</p>
</td>
</tr>
</tbody>
</table>

For details about other returned values, see  [Status Codes](status-codes.md).

## Error Codes<a name="section14752650154917"></a>

See  [Error Codes](error-codes.md).

