# Deleting a Forwarding Policy<a name="EN-US_TOPIC_0136295319"></a>

## Function<a name="section1569947195915"></a>

This API is used to delete a specific forwarding policy.

## URI<a name="section1131040245"></a>

DELETE /v2.0/lbaas/l7policies/\{l7policy\_id\}

**Table  1**  Parameter description

<a name="table158419166402"></a>
<table><thead align="left"><tr id="row19584716114011"><th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.1"><p id="p15841916124016"><a name="p15841916124016"></a><a name="p15841916124016"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.2"><p id="p447718103185"><a name="p447718103185"></a><a name="p447718103185"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.3"><p id="p75841316164014"><a name="p75841316164014"></a><a name="p75841316164014"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="54%" id="mcps1.2.5.1.4"><p id="p14584151674011"><a name="p14584151674011"></a><a name="p14584151674011"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row17158113918463"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.1 "><p id="p6789122710454"><a name="p6789122710454"></a><a name="p6789122710454"></a>l7policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p14476710191816"><a name="p14476710191816"></a><a name="p14476710191816"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p10789627154513"><a name="p10789627154513"></a><a name="p10789627154513"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.5.1.4 "><p id="p182291832134920"><a name="p182291832134920"></a><a name="p182291832134920"></a>Specifies the forwarding policy ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section936817221503"></a>

None

## Response<a name="section243715298217"></a>

None

## Example<a name="section189883236519"></a>

-   Example request: Deleting a forwarding policy

    ```
    DELETE https://{Endpoint}/v2.0/lbaas/l7policies/5ae0e1e7-5f0f-47a1-b39f-5d4c428a1586
    ```

-   Example response

    None


## Status Code<a name="section6200237145116"></a>

For details, see  [HTTP Status Codes for Enhanced Load Balancers](http-status-codes-for-enhanced-load-balancers.md).

