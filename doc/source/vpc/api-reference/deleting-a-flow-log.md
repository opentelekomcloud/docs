# Deleting a Flow Log<a name="vpc_flow_0005"></a>

## Function<a name="section1699617359406"></a>

This API is used to delete a flow log.

## URI<a name="section69961435104017"></a>

DELETE /v1/\{project\_id\}/fl/flow\_logs/\{flowlog\_id\}

[Table 1](#table19961835154017)  describes the parameters.

**Table  1**  Parameter description

<a name="table19961835154017"></a>
<table><thead align="left"><tr id="row8591036184010"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p1159163654017"><a name="p1159163654017"></a><a name="p1159163654017"></a><strong id="b158059312015"><a name="b158059312015"></a><a name="b158059312015"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p11596363401"><a name="p11596363401"></a><a name="p11596363401"></a><strong id="b17629143210015"><a name="b17629143210015"></a><a name="b17629143210015"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p95913684012"><a name="p95913684012"></a><a name="p95913684012"></a><strong id="b19607123312017"><a name="b19607123312017"></a><a name="b19607123312017"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p15591936144018"><a name="p15591936144018"></a><a name="p15591936144018"></a><strong id="b154558341016"><a name="b154558341016"></a><a name="b154558341016"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row059336104010"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p125943664010"><a name="p125943664010"></a><a name="p125943664010"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p55993644013"><a name="p55993644013"></a><a name="p55993644013"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p95923610406"><a name="p95923610406"></a><a name="p95923610406"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row155917363400"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p259836164017"><a name="p259836164017"></a><a name="p259836164017"></a>flowlog_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p10591836174010"><a name="p10591836174010"></a><a name="p10591836174010"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p1459113614015"><a name="p1459113614015"></a><a name="p1459113614015"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p205912364405"><a name="p205912364405"></a><a name="p205912364405"></a>Specifies the VPC flow log ID.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section499623515407"></a>

-   Request parameter

    None

-   Example request

    ```
    DELETE https://{Endpoint}/v1/b2782e6708b8475c993e6064bc456bf8/fl/flow_logs/60c809cb-6731-45d0-ace8-3bf5626421a9
    ```


## Response Message<a name="section3121736194011"></a>

-   Request parameter

    None

-   Example response

    None


## Status Code<a name="section31981619"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

