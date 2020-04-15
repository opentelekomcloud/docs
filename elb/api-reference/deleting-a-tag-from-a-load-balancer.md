# Deleting a Tag from a Load Balancer<a name="EN-US_TOPIC_0109852831"></a>

## Function<a name="en-us_topic_0102000761_section5459564712243"></a>

This API is used to delete a tag with a specific key from a load balancer.

## URI<a name="en-us_topic_0102000761_section467068812243"></a>

DELETE /v2.0/\{project\_id\}/loadbalancers/\{loadbalancer\_id\}/tags/\{key\}

**Table  1**  Parameter description

<a name="table33323423"></a>
<table><thead align="left"><tr id="row8420641"><th class="cellrowborder" valign="top" width="13.131313131313133%" id="mcps1.2.5.1.1"><p id="p10983320"><a name="p10983320"></a><a name="p10983320"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.141414141414144%" id="mcps1.2.5.1.2"><p id="p17233719"><a name="p17233719"></a><a name="p17233719"></a><strong id="b842352706192244"><a name="b842352706192244"></a><a name="b842352706192244"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="13.131313131313133%" id="mcps1.2.5.1.3"><p id="p4164548117122"><a name="p4164548117122"></a><a name="p4164548117122"></a><strong id="b842352706145623"><a name="b842352706145623"></a><a name="b842352706145623"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="59.59595959595959%" id="mcps1.2.5.1.4"><p id="p53754023"><a name="p53754023"></a><a name="p53754023"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row53906008171138"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.1 "><p id="p16126074171144"><a name="p16126074171144"></a><a name="p16126074171144"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.2 "><p id="p31143627171144"><a name="p31143627171144"></a><a name="p31143627171144"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.3 "><p id="p39605860171144"><a name="p39605860171144"></a><a name="p39605860171144"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.59595959595959%" headers="mcps1.2.5.1.4 "><p id="p11184131"><a name="p11184131"></a><a name="p11184131"></a>Specifies the ID of the project where the tag is used.</p>
<p id="p8222164914610"><a name="p8222164914610"></a><a name="p8222164914610"></a></p>
</td>
</tr>
<tr id="row1686321181111"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.1 "><p id="p15863201114114"><a name="p15863201114114"></a><a name="p15863201114114"></a>loadbalancer_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.2 "><p id="p486381113115"><a name="p486381113115"></a><a name="p486381113115"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.3 "><p id="p168781411121112"><a name="p168781411121112"></a><a name="p168781411121112"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.59595959595959%" headers="mcps1.2.5.1.4 "><p id="p1220014383149"><a name="p1220014383149"></a><a name="p1220014383149"></a>Specifies the ID of the load balancer from which a tag is to be deleted.</p>
</td>
</tr>
</tbody>
</table>

## Constraints<a name="en-us_topic_0102000761_section847718412243"></a>

None

## Request<a name="en-us_topic_0102000761_section5274212712243"></a>

None

## Response<a name="en-us_topic_0102000761_section6274108212243"></a>

None

## Example<a name="section477834010264"></a>

-   Example request

    ```
    DELETE https://{Endpoint}/v2.0/6a0de1c3-7d74-4f4a-b75e-e57135bd2b97/loadbalancers/7add33ad-11dc-4ab9-a50f-419703f13163/tags/key1
    ```


-   Example response

    None


## Status Code<a name="en-us_topic_0102000761_section1040452612243"></a>

For details, see  [Status Codes](status-codes.md).

