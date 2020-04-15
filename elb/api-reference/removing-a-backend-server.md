# Removing a Backend Server<a name="EN-US_TOPIC_0096561558"></a>

## Function<a name="en-us_topic_0049139659_section26102093"></a>

This API is used to remove a backend server by its ID.

## URI<a name="section130145411433"></a>

DELETE /v2.0/lbaas/pools/\{pool\_id\}/members/\{member\_id\}

**Table  1**  Parameter description

<a name="table051172614182"></a>
<table><thead align="left"><tr id="row1311718267180"><th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.1"><p id="p611782612183"><a name="p611782612183"></a><a name="p611782612183"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.2"><p id="p171175268189"><a name="p171175268189"></a><a name="p171175268189"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.2.5.1.3"><p id="p7117192641812"><a name="p7117192641812"></a><a name="p7117192641812"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="54%" id="mcps1.2.5.1.4"><p id="p211762661812"><a name="p211762661812"></a><a name="p211762661812"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row711782621810"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="p61171126181819"><a name="p61171126181819"></a><a name="p61171126181819"></a>pool_id</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p11175262186"><a name="p11175262186"></a><a name="p11175262186"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.3 "><p id="p3118172691814"><a name="p3118172691814"></a><a name="p3118172691814"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.5.1.4 "><p id="p4118132613185"><a name="p4118132613185"></a><a name="p4118132613185"></a>Specifies the backend server group ID.</p>
</td>
</tr>
<tr id="row1011872641818"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="p18118142615182"><a name="p18118142615182"></a><a name="p18118142615182"></a>member_id</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p31181926141810"><a name="p31181926141810"></a><a name="p31181926141810"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.3 "><p id="p061711023719"><a name="p061711023719"></a><a name="p061711023719"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.5.1.4 "><p id="p13118142691814"><a name="p13118142691814"></a><a name="p13118142691814"></a>Specifies the backend server ID.</p>
</td>
</tr>
</tbody>
</table>

## Constraints<a name="en-us_topic_0049139659_section33894784"></a>

After you delete a backend server, new connections to this server will not be established. However, long connections that have been established will be maintained.

## Request<a name="en-us_topic_0049139659_section13236018"></a>

None

## Response<a name="en-us_topic_0049139659_section52015300"></a>

None

## Example<a name="section13626216188"></a>

-   Example request: Removing a backend server

    ```
    DELETE https://{Endpoint}/v2.0/lbaas/pools/5a9a3e9e-d1aa-448e-af37-a70171f2a332/members/cf024846-7516-4e3a-b0fb-6590322c836f
    ```


-   Example response

    None


## Status Code<a name="en-us_topic_0049139655_section64643717"></a>

For details, see  [HTTP Status Codes for Enhanced Load Balancers](http-status-codes-for-enhanced-load-balancers.md).

