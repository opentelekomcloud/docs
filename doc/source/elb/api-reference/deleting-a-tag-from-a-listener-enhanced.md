# Deleting a Tag from a Listener<a name="EN-US_TOPIC_0112614720"></a>

## Function<a name="section1282617501147"></a>

This API is used to delete a tag with a specific key from a listener.

## URI<a name="section98272050161416"></a>

DELETE /v2.0/\{project\_id\}/listeners/\{listener\_id\}/tags/\{key\}

**Table  1**  Parameter description

<a name="table33323423"></a>
<table><thead align="left"><tr id="row8420641"><th class="cellrowborder" valign="top" width="13.131313131313133%" id="mcps1.2.5.1.1"><p id="p10983320"><a name="p10983320"></a><a name="p10983320"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13.131313131313133%" id="mcps1.2.5.1.2"><p id="p17233719"><a name="p17233719"></a><a name="p17233719"></a><strong id="b842352706192244"><a name="b842352706192244"></a><a name="b842352706192244"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="11.111111111111112%" id="mcps1.2.5.1.3"><p id="p4164548117122"><a name="p4164548117122"></a><a name="p4164548117122"></a><strong id="b842352706145623"><a name="b842352706145623"></a><a name="b842352706145623"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="62.62626262626263%" id="mcps1.2.5.1.4"><p id="p53754023"><a name="p53754023"></a><a name="p53754023"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row53906008171138"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.1 "><p id="p16126074171144"><a name="p16126074171144"></a><a name="p16126074171144"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.2 "><p id="p31143627171144"><a name="p31143627171144"></a><a name="p31143627171144"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.2.5.1.3 "><p id="p39605860171144"><a name="p39605860171144"></a><a name="p39605860171144"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.62626262626263%" headers="mcps1.2.5.1.4 "><p id="p11184131"><a name="p11184131"></a><a name="p11184131"></a>Specifies the ID of the project where the tag is used. </p>
</td>
</tr>
<tr id="row6239103417284"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.1 "><p id="p17239163472818"><a name="p17239163472818"></a><a name="p17239163472818"></a>listener_id</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.2 "><p id="p17239173410285"><a name="p17239173410285"></a><a name="p17239173410285"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.2.5.1.3 "><p id="p77952291156"><a name="p77952291156"></a><a name="p77952291156"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.62626262626263%" headers="mcps1.2.5.1.4 "><p id="p8239434172817"><a name="p8239434172817"></a><a name="p8239434172817"></a>Specifies the ID of the listener from which a tag is to be deleted.</p>
</td>
</tr>
</tbody>
</table>

## Constraints<a name="section18394500145"></a>

None

## Request<a name="section8841850131418"></a>

None

## Response<a name="section118441550181415"></a>

None

## Example<a name="section205541643163117"></a>

-   Example request

    ```
    DELETE https://{Endpoint}/v2.0/6a0de1c3-7d74-4f4a-b75e-e57135bd2b97/listeners/7add33ad-11dc-4ab9-a50f-419703f13163/tags/key1
    ```


-   Example response

    None


## Status Code<a name="section12846175015145"></a>

For details, see  [Status Codes](status-codes-enhanced.md).

