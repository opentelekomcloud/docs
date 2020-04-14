# Deleting a Load Balancer<a name="EN-US_TOPIC_0141008275"></a>

## Function<a name="en-us_topic_0096561537_en-us_topic_0049139636_section15222565"></a>

This API is used to delete a specific load balancer. When you select cascade delete, listeners, backend server groups, backend servers, health checks, forwarding policies, forwarding rules, whitelists, and tags associated with the load balancer will be deleted.

## URI<a name="en-us_topic_0096561537_en-us_topic_0049139636_section2785358"></a>

DELETE /v2.0/lbaas/loadbalancers/\{loadbalancer\_id\}

**Table  1**  Parameter description

<a name="en-us_topic_0096561537_table1022794920394"></a>
<table><thead align="left"><tr id="en-us_topic_0096561537_row12260114916392"><th class="cellrowborder" valign="top" width="26.442644264426445%" id="mcps1.2.5.1.1"><p id="en-us_topic_0096561537_p1226015492392"><a name="en-us_topic_0096561537_p1226015492392"></a><a name="en-us_topic_0096561537_p1226015492392"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="12.861286128612862%" id="mcps1.2.5.1.2"><p id="en-us_topic_0096561537_p12260649173914"><a name="en-us_topic_0096561537_p12260649173914"></a><a name="en-us_topic_0096561537_p12260649173914"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="12.401240124012402%" id="mcps1.2.5.1.3"><p id="en-us_topic_0096561537_p1226018498394"><a name="en-us_topic_0096561537_p1226018498394"></a><a name="en-us_topic_0096561537_p1226018498394"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="48.294829482948295%" id="mcps1.2.5.1.4"><p id="en-us_topic_0096561537_p1926013494393"><a name="en-us_topic_0096561537_p1926013494393"></a><a name="en-us_topic_0096561537_p1926013494393"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0096561537_row22601349183910"><td class="cellrowborder" valign="top" width="26.442644264426445%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0096561537_p1726024910396"><a name="en-us_topic_0096561537_p1726024910396"></a><a name="en-us_topic_0096561537_p1726024910396"></a>loadbalancer_id</p>
</td>
<td class="cellrowborder" valign="top" width="12.861286128612862%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0096561537_p1726017494395"><a name="en-us_topic_0096561537_p1726017494395"></a><a name="en-us_topic_0096561537_p1726017494395"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="12.401240124012402%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0096561537_p7260849143916"><a name="en-us_topic_0096561537_p7260849143916"></a><a name="en-us_topic_0096561537_p7260849143916"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.294829482948295%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0096561537_p126074963916"><a name="en-us_topic_0096561537_p126074963916"></a><a name="en-us_topic_0096561537_p126074963916"></a>Specifies the load balancer ID.</p>
</td>
</tr>
</tbody>
</table>

## Constraints<a name="en-us_topic_0096561537_en-us_topic_0049139636_section25068230"></a>

All listeners added to the load balancer must be deleted before the load balancer is deleted.

## Request<a name="en-us_topic_0096561537_section2772124744415"></a>

None

## Response<a name="en-us_topic_0096561537_section144379436451"></a>

None

## Example<a name="section251523714195"></a>

-   Example request: Deleting a load balancer

    ```
    DELETE https://{endpoint}/v2.0/lbaas/loadbalancers/90f7c765-0bc9-47c4-8513-4cc0c264c8f8
    ```

-   Example response

    None


## Status Code<a name="en-us_topic_0096561537_en-us_topic_0049139636_section33751805"></a>

For details, see  [HTTP Status Codes for Enhanced Load Balancers](http-status-codes-for-enhanced-load-balancers.md).

