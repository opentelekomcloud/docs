# Deleting a Health Check<a name="EN-US_TOPIC_0096561565"></a>

## Function<a name="en-us_topic_0049139667_section61062380"></a>

This API is used to delete a specific health check.

## URI<a name="en-us_topic_0049139667_section12690509"></a>

DELETE /v2.0/lbaas/healthmonitors/\{healthmonitor\_id\}

**Table  1**  Parameter description

<a name="table132418563309"></a>
<table><thead align="left"><tr id="row62797564309"><th class="cellrowborder" valign="top" width="18.181818181818183%" id="mcps1.2.5.1.1"><p id="p5279105619300"><a name="p5279105619300"></a><a name="p5279105619300"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.141414141414144%" id="mcps1.2.5.1.2"><p id="p1527985619309"><a name="p1527985619309"></a><a name="p1527985619309"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16.161616161616163%" id="mcps1.2.5.1.3"><p id="p11279556143016"><a name="p11279556143016"></a><a name="p11279556143016"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51.515151515151516%" id="mcps1.2.5.1.4"><p id="p427905643013"><a name="p427905643013"></a><a name="p427905643013"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row10279105613013"><td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.1 "><p id="p112791156163015"><a name="p112791156163015"></a><a name="p112791156163015"></a>healthmonitor_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.2 "><p id="p9279956183020"><a name="p9279956183020"></a><a name="p9279956183020"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.3 "><p id="p112054816338"><a name="p112054816338"></a><a name="p112054816338"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.2.5.1.4 "><p id="p227913566302"><a name="p227913566302"></a><a name="p227913566302"></a>Specifies the health check ID.</p>
</td>
</tr>
</tbody>
</table>

## Constraints<a name="en-us_topic_0049139667_section47105724"></a>

If  **provisioning\_status**  of the load balancer for which the health check is configured is not  **ACTIVE**, the health check cannot be deleted.

## Request<a name="en-us_topic_0049139667_section47443737"></a>

None

## Response<a name="en-us_topic_0049139667_section24340454"></a>

None

## Example<a name="section16819144115533"></a>

-   Example request: Deleting a health check

    ```
    DELETE https://{Endpoint}/v2.0/lbaas/healthmonitors/b7633ade-24dc-4d72-8475-06aa22be5412
    ```

-   Example response

    None


## Status Code<a name="en-us_topic_0049139655_section64643717"></a>

For details, see  [HTTP Status Codes for Enhanced Load Balancers](http-status-codes-for-enhanced-load-balancers.md).

