# Deleting a Backend Server Group<a name="EN-US_TOPIC_0096561551"></a>

## Function<a name="section18751829131716"></a>

This API is used to delete a backend server group.

## URI<a name="section88952419175"></a>

DELETE /v2.0/lbaas/pools/\{pool\_id\}

**Table  1**  Parameter description

<a name="table1327914504712"></a>
<table><thead align="left"><tr id="row9312105012710"><th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.1"><p id="p103127504710"><a name="p103127504710"></a><a name="p103127504710"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.5.1.2"><p id="p83122050276"><a name="p83122050276"></a><a name="p83122050276"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p93129509712"><a name="p93129509712"></a><a name="p93129509712"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="60%" id="mcps1.2.5.1.4"><p id="p1345194632614"><a name="p1345194632614"></a><a name="p1345194632614"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row5312145018717"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="p1131211505714"><a name="p1131211505714"></a><a name="p1131211505714"></a>pool_id</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.2 "><p id="p53129507720"><a name="p53129507720"></a><a name="p53129507720"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p53121850773"><a name="p53121850773"></a><a name="p53121850773"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.5.1.4 "><p id="p1331285012713"><a name="p1331285012713"></a><a name="p1331285012713"></a>Specifies the backend server group ID.</p>
</td>
</tr>
</tbody>
</table>

## Constraints<a name="en-us_topic_0049139652_section43896488"></a>

Before deleting a backend server group, remove all backend servers, delete the health check, and disassociate forwarding policies from the backend server group by changing the value of  **redirect\_pool\_id**  to  **null**. For details, see  [Updating a Forwarding Policy](updating-a-forwarding-policy.md).

## Request<a name="section14802182381816"></a>

None

## Response<a name="section682186111916"></a>

None

## Example<a name="section8984194341912"></a>

-   Example request: Deleting a backend server group

    ```
    DELETE  /v2.0/lbaas/pools/5a9a3e9e-d1aa-448e-af37-a70171f2a332
    ```


-   Example response

    None


## Status Code<a name="en-us_topic_0049139652_section30985493"></a>

For details, see  [HTTP Status Codes for Enhanced Load Balancers](http-status-codes-for-enhanced-load-balancers.md).

