# Deleting a Listener<a name="EN-US_TOPIC_0096561543"></a>

## Function<a name="en-us_topic_0049139644_section30386741"></a>

This API is used to delete a listener.

## API Format<a name="en-us_topic_0049139644_section5045213"></a>

<a name="en-us_topic_0049139644_table10797997114634"></a><table><thead align="left"><tr id="en-us_topic_0049139644_row43048302114634"><th class="cellrowborder" valign="top" width="18.86%" id="mcps1.1.4.1.1"><p id="en-us_topic_0049139644_p39485450114639"><a name="en-us_topic_0049139644_p39485450114639"></a><a name="en-us_topic_0049139644_p39485450114639"></a><strong id="b842352706172312"><a name="b842352706172312"></a><a name="b842352706172312"></a>Method</strong></p>
</th>
<th class="cellrowborder" valign="top" width="47.81%" id="mcps1.1.4.1.2"><p id="en-us_topic_0049139644_p44204919114639"><a name="en-us_topic_0049139644_p44204919114639"></a><a name="en-us_topic_0049139644_p44204919114639"></a>URI</p>
</th>
<th class="cellrowborder" valign="top" width="33.33%" id="mcps1.1.4.1.3"><p id="en-us_topic_0049139644_p23828676114639"><a name="en-us_topic_0049139644_p23828676114639"></a><a name="en-us_topic_0049139644_p23828676114639"></a><strong id="b842352706192251"><a name="b842352706192251"></a><a name="b842352706192251"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0049139644_row59568308114634"><td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0049139644_p43400735114639"><a name="en-us_topic_0049139644_p43400735114639"></a><a name="en-us_topic_0049139644_p43400735114639"></a>DELETE</p>
</td>
<td class="cellrowborder" valign="top" width="47.81%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0049139644_p25798653114639"><a name="en-us_topic_0049139644_p25798653114639"></a><a name="en-us_topic_0049139644_p25798653114639"></a>/v2.0/lbaas/listeners/{listener_id}</p>
</td>
<td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0049139644_p9316188114639"><a name="en-us_topic_0049139644_p9316188114639"></a><a name="en-us_topic_0049139644_p9316188114639"></a>Deletes a listener specified by the tenant.</p>
</td>
</tr>
</tbody>
</table>

## Restrictions<a name="en-us_topic_0049139644_section45406920"></a>

The associated backend ECS group must be deleted before the listener is deleted.

## Request<a name="section95756481931"></a>

-   Parameter description

    None

-   Example request

    ```
    DELETE  /v2.0/lbaas/listeners/35cb8516-1173-4035-8dae-0dae3453f37f
    ```


## Response<a name="section19304559449"></a>

None

## Error Codes<a name="en-us_topic_0049139644_section32832084"></a>

For details, see section  [Error Codes for Enhanced Load Balancers](error-codes-for-enhanced-load-balancers.md).

