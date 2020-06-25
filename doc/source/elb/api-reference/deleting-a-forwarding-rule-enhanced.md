# Deleting a Forwarding Rule<a name="EN-US_TOPIC_0116649238"></a>

## Function<a name="en-us_topic_0082661929_section43897986151857"></a>

This API is used to delete a specific forwarding rule.

## URI<a name="en-us_topic_0082661929_section57812656151857"></a>

DELETE /v2.0/lbaas/l7policies/\{l7policy\_id\}/rules/\{l7rule\_id\}

**Table  1**  Parameter description

<a name="table136416168119"></a>
<table><thead align="left"><tr id="row191101161110"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="p8110416114"><a name="p8110416114"></a><a name="p8110416114"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="11%" id="mcps1.2.5.1.2"><p id="p161108168115"><a name="p161108168115"></a><a name="p161108168115"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="p1111013169117"><a name="p1111013169117"></a><a name="p1111013169117"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="56.99999999999999%" id="mcps1.2.5.1.4"><p id="p194124122910"><a name="p194124122910"></a><a name="p194124122910"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row91109162016"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p13110141616118"><a name="p13110141616118"></a><a name="p13110141616118"></a>l7policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.2 "><p id="p311012162111"><a name="p311012162111"></a><a name="p311012162111"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p1611091610113"><a name="p1611091610113"></a><a name="p1611091610113"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.5.1.4 "><p id="p9110131610114"><a name="p9110131610114"></a><a name="p9110131610114"></a>Specifies the forwarding policy ID.</p>
</td>
</tr>
<tr id="row81109166112"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p611019161215"><a name="p611019161215"></a><a name="p611019161215"></a>l7rule_id</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.2 "><p id="p611031615117"><a name="p611031615117"></a><a name="p611031615117"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p176481590288"><a name="p176481590288"></a><a name="p176481590288"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.5.1.4 "><p id="p911016167118"><a name="p911016167118"></a><a name="p911016167118"></a>Specifies the forwarding rule ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0082661929_section38444823151857"></a>

None

## Response<a name="en-us_topic_0082661929_section41879874151857"></a>

None

## Example<a name="section102569429817"></a>

-   Example request: Deleting a forwarding rule

    ```
    DELETE https://{Endpoint}/v2.0/lbaas/l7policies/5ae0e1e7-5f0f-47a1-b39f-5d4c428a1586/rules/c6f457b8-bf6f-45d7-be5c-a3226945b7b1
    ```

-   Example response

    None


## Status Code<a name="section14127191015294"></a>

For details, see  [HTTP Status Codes for Enhanced Load Balancers](http-status-codes-for-enhanced-load-balancers.md).

