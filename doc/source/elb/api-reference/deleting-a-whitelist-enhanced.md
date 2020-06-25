# Deleting a Whitelist<a name="EN-US_TOPIC_0143878055"></a>

## Function<a name="section35831867"></a>

This API is used to delete a specific whitelist.

## URI<a name="section54051348"></a>

DELETE /v2.0/lbaas/whitelists/\{whitelist\_id\}

**Table  1**  Parameter description

<a name="table39773978"></a>
<table><thead align="left"><tr id="row39242708"><th class="cellrowborder" valign="top" width="17.17171717171717%" id="mcps1.2.5.1.1"><p id="p24542757"><a name="p24542757"></a><a name="p24542757"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.14141414141414%" id="mcps1.2.5.1.2"><p id="p41806332"><a name="p41806332"></a><a name="p41806332"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.14141414141414%" id="mcps1.2.5.1.3"><p id="p30869694"><a name="p30869694"></a><a name="p30869694"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="54.54545454545454%" id="mcps1.2.5.1.4"><p id="p17417301"><a name="p17417301"></a><a name="p17417301"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1515305"><td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.2.5.1.1 "><p id="p55630881"><a name="p55630881"></a><a name="p55630881"></a>whitelist_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.2 "><p id="p9807526"><a name="p9807526"></a><a name="p9807526"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.3 "><p id="p56212127"><a name="p56212127"></a><a name="p56212127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.54545454545454%" headers="mcps1.2.5.1.4 "><p id="p56888437"><a name="p56888437"></a><a name="p56888437"></a>Specifies the whitelist ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section16700087"></a>

None

## Response<a name="section16083062"></a>

None

## Example<a name="section5865123802411"></a>

-   Example request: Deleting a whitelist

    ```
    DELETE https://{Endpoint}/v2.0/lbaas/whitelists/35cb8516-1173-4035-8dae-0dae3453f37f
    ```

-   Example response

    None


## Status Code<a name="section10529832"></a>

For details, see  [HTTP Status Codes for Enhanced Load Balancers](http-status-codes-for-enhanced-load-balancers.md).

