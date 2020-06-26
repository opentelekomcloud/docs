# Deleting an IPsec VPN Connection<a name="en_topic_0093011496"></a>

## **Function**<a name="section4400500"></a>

This interface is used to delete an IPsec VPN connection.

## URI<a name="section39604502"></a>

DELETE /v2.0/vpn/ipsec-site-connections/\{connection\_id\}

**Table  1**  Parameter description

<a name="table9861172982416"></a>
<table><thead align="left"><tr id="row19884629102416"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p3884192972412"><a name="p3884192972412"></a><a name="p3884192972412"></a><strong id="b842352706172115"><a name="b842352706172115"></a><a name="b842352706172115"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p13893112952410"><a name="p13893112952410"></a><a name="p13893112952410"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p49011329112410"><a name="p49011329112410"></a><a name="p49011329112410"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p1490112914244"><a name="p1490112914244"></a><a name="p1490112914244"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row139091529142413"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p990917292242"><a name="p990917292242"></a><a name="p990917292242"></a>connection_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p1390982912240"><a name="p1390982912240"></a><a name="p1390982912240"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p12917112917246"><a name="p12917112917246"></a><a name="p12917112917246"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p79171129172411"><a name="p79171129172411"></a><a name="p79171129172411"></a>Specifies the IPsec VPN connection ID.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section53848109"></a>

None

## Response Message<a name="section14870940"></a>

None

## Example<a name="section66729601"></a>

-   Example Request

    ```
    DELETE /v2.0/vpn/ipsec-site-connections/{connection_id}
    ```


-   Example Response

    None


## Returned Values<a name="section6578292"></a>

For details, see section  [Common Returned Values](common-returned-values.md).


