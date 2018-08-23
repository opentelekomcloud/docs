# Deleting a Load Balancer<a name="EN-US_TOPIC_0096561537"></a>

## Function<a name="en-us_topic_0049139636_section15222565"></a>

This API is used to delete a load balancer.

## API Format<a name="en-us_topic_0049139636_section2785358"></a>

<a name="en-us_topic_0049139636_table52658651111138"></a><table><thead align="left"><tr id="en-us_topic_0049139636_row29654238111138"><th class="cellrowborder" valign="top" width="14.35%" id="mcps1.1.4.1.1"><p id="en-us_topic_0049139636_p40874042111143"><a name="en-us_topic_0049139636_p40874042111143"></a><a name="en-us_topic_0049139636_p40874042111143"></a><strong id="en-us_topic_0049139636_b842352706111926"><a name="en-us_topic_0049139636_b842352706111926"></a><a name="en-us_topic_0049139636_b842352706111926"></a>Method</strong></p>
</th>
<th class="cellrowborder" valign="top" width="32.4%" id="mcps1.1.4.1.2"><p id="en-us_topic_0049139636_p22463138111143"><a name="en-us_topic_0049139636_p22463138111143"></a><a name="en-us_topic_0049139636_p22463138111143"></a>URI</p>
</th>
<th class="cellrowborder" valign="top" width="53.25%" id="mcps1.1.4.1.3"><p id="en-us_topic_0049139636_p7574874111143"><a name="en-us_topic_0049139636_p7574874111143"></a><a name="en-us_topic_0049139636_p7574874111143"></a><strong id="en-us_topic_0049139636_b84235270695939"><a name="en-us_topic_0049139636_b84235270695939"></a><a name="en-us_topic_0049139636_b84235270695939"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0049139636_row53084845111138"><td class="cellrowborder" valign="top" width="14.35%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0049139636_p38190299111143"><a name="en-us_topic_0049139636_p38190299111143"></a><a name="en-us_topic_0049139636_p38190299111143"></a>DELETE</p>
</td>
<td class="cellrowborder" valign="top" width="32.4%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0049139636_p6406516111143"><a name="en-us_topic_0049139636_p6406516111143"></a><a name="en-us_topic_0049139636_p6406516111143"></a>/v2.0/lbaas/loadbalancers/{loadbalancer_id}</p>
</td>
<td class="cellrowborder" valign="top" width="53.25%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0049139636_p49165822111143"><a name="en-us_topic_0049139636_p49165822111143"></a><a name="en-us_topic_0049139636_p49165822111143"></a>Deletes a load balancer.</p>
</td>
</tr>
</tbody>
</table>

## Restrictions<a name="en-us_topic_0049139636_section25068230"></a>

Before a load balancer is deleted, all listeners associated with the load balancer must be deleted.

## Request<a name="section2772124744415"></a>

-   Parameter description

    None

-   Example request

    ```
    DELETE  /v2.0/lbaas/loadbalancers/90f7c765-0bc9-47c4-8513-4cc0c264c8f8
    ```


## Response<a name="section144379436451"></a>

None

## Error Codes<a name="en-us_topic_0049139636_section33751805"></a>

For details, see section  [Error Codes for Enhanced Load Balancers](error-codes-for-enhanced-load-balancers.md).

