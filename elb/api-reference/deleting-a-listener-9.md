# Deleting a Listener<a name="EN-US_TOPIC_0096561543"></a>

## Function<a name="en-us_topic_0049139644_section30386741"></a>

This API is used to delete a specific listener. If you select cascade delete, backend servers and backend servers groups will be disassociated from the listener, and forwarding policies, forwarding rules, whitelists, and tags associated with the listener will be deleted.

## URI<a name="en-us_topic_0049139644_section5045213"></a>

DELETE /v2.0/lbaas/listeners/\{listener\_id\}

**Table  1**  Parameter description

<a name="table20248962551"></a>
<table><thead align="left"><tr id="row1028619635515"><th class="cellrowborder" valign="top" width="26.442644264426445%" id="mcps1.2.5.1.1"><p id="p028646185519"><a name="p028646185519"></a><a name="p028646185519"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="10.741074107410741%" id="mcps1.2.5.1.2"><p id="p1628613625510"><a name="p1628613625510"></a><a name="p1628613625510"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.52145214521452%" id="mcps1.2.5.1.3"><p id="p22866675511"><a name="p22866675511"></a><a name="p22866675511"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="48.294829482948295%" id="mcps1.2.5.1.4"><p id="p528626165515"><a name="p528626165515"></a><a name="p528626165515"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row028696145515"><td class="cellrowborder" valign="top" width="26.442644264426445%" headers="mcps1.2.5.1.1 "><p id="p72868675519"><a name="p72868675519"></a><a name="p72868675519"></a>listener_id</p>
</td>
<td class="cellrowborder" valign="top" width="10.741074107410741%" headers="mcps1.2.5.1.2 "><p id="p42864614551"><a name="p42864614551"></a><a name="p42864614551"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.52145214521452%" headers="mcps1.2.5.1.3 "><p id="p11286156135517"><a name="p11286156135517"></a><a name="p11286156135517"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.294829482948295%" headers="mcps1.2.5.1.4 "><p id="p1028636105515"><a name="p1028636105515"></a><a name="p1028636105515"></a>Specifies the listener ID.</p>
</td>
</tr>
</tbody>
</table>

## Constraints<a name="en-us_topic_0049139644_section45406920"></a>

All backend server groups associated with the listener must be deleted before the listener is deleted.

## Request<a name="section95756481931"></a>

None

## Response<a name="section19304559449"></a>

None

## Example<a name="section122114835814"></a>

-   Example request: Deleting a listener

    ```
    DELETE https://{Endpoint}/v2.0/lbaas/listeners/35cb8516-1173-4035-8dae-0dae3453f37f
    ```

-   Example response

    None


## Status Code<a name="en-us_topic_0049139644_section32832084"></a>

For details, see  [HTTP Status Codes for Enhanced Load Balancers](http-status-codes-for-enhanced-load-balancers.md).

