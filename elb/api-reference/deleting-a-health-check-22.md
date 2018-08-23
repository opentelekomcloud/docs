# Deleting a Health Check<a name="EN-US_TOPIC_0096561565"></a>

## Function<a name="en-us_topic_0049139667_section61062380"></a>

This API is used to delete a health check.

## API Format<a name="en-us_topic_0049139667_section12690509"></a>

<a name="en-us_topic_0049139667_table4236262113420"></a><table><thead align="left"><tr id="en-us_topic_0049139667_row6603281513420"><th class="cellrowborder" valign="top" width="14.719999999999999%" id="mcps1.1.4.1.1"><p id="en-us_topic_0049139667_p422569313426"><a name="en-us_topic_0049139667_p422569313426"></a><a name="en-us_topic_0049139667_p422569313426"></a><strong id="b842352706172312"><a name="b842352706172312"></a><a name="b842352706172312"></a>Method</strong></p>
</th>
<th class="cellrowborder" valign="top" width="55.88999999999999%" id="mcps1.1.4.1.2"><p id="en-us_topic_0049139667_p673686813426"><a name="en-us_topic_0049139667_p673686813426"></a><a name="en-us_topic_0049139667_p673686813426"></a>URI</p>
</th>
<th class="cellrowborder" valign="top" width="29.39%" id="mcps1.1.4.1.3"><p id="en-us_topic_0049139667_p881546413426"><a name="en-us_topic_0049139667_p881546413426"></a><a name="en-us_topic_0049139667_p881546413426"></a><strong id="b842352706192251"><a name="b842352706192251"></a><a name="b842352706192251"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0049139667_row989978013420"><td class="cellrowborder" valign="top" width="14.719999999999999%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0049139667_p5753069313426"><a name="en-us_topic_0049139667_p5753069313426"></a><a name="en-us_topic_0049139667_p5753069313426"></a>DELETE</p>
</td>
<td class="cellrowborder" valign="top" width="55.88999999999999%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0049139667_p2947454213426"><a name="en-us_topic_0049139667_p2947454213426"></a><a name="en-us_topic_0049139667_p2947454213426"></a>/v2.0/lbaas/healthmonitors/{healthmonitor_id}</p>
</td>
<td class="cellrowborder" valign="top" width="29.39%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0049139667_p3862770013426"><a name="en-us_topic_0049139667_p3862770013426"></a><a name="en-us_topic_0049139667_p3862770013426"></a>Deletes a specific health check.</p>
</td>
</tr>
</tbody>
</table>

## Restrictions<a name="en-us_topic_0049139667_section47105724"></a>

If  **provisioning\_status** of the load balancer for which the health check is configured is not **ACTIVE**, the health check cannot be deleted.

## Request<a name="en-us_topic_0049139667_section47443737"></a>

-   Parameter description

    None

-   Example request

    ```
    DELETE  /v2.0/lbaas/healthmonitors/b7633ade-24dc-4d72-8475-06aa22be5412
    ```


## Response<a name="en-us_topic_0049139667_section24340454"></a>

None

## Error Codes<a name="en-us_topic_0049139655_section64643717"></a>

For details, see section  [Error Codes for Enhanced Load Balancers](error-codes-for-enhanced-load-balancers.md).

