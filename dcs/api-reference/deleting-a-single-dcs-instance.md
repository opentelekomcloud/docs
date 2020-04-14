# Deleting a Single DCS Instance<a name="EN-US_TOPIC_0237964388"></a>

## Function<a name="section9847307"></a>

This API is used to delete a specified DCS instance to free up all resources occupied by the DCS instance.

## URI<a name="section21516907"></a>

-   URI format:

    DELETE /v1.0/\{project\_id\}/instances/\{instance\_id\}

-   Parameter description:

    [Table 1](#d0e1786)  describes the parameters of this API.


**Table  1**  Parameter description

<a name="d0e1786"></a>
<table><thead align="left"><tr id="row39128901"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p15324435"><a name="p15324435"></a><a name="p15324435"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p33319697"><a name="p33319697"></a><a name="p33319697"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p14540903"><a name="p14540903"></a><a name="p14540903"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p36962494"><a name="p36962494"></a><a name="p36962494"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row41172029"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p46600077"><a name="p46600077"></a><a name="p46600077"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p16509910"><a name="p16509910"></a><a name="p16509910"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p62234303"><a name="p62234303"></a><a name="p62234303"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p7813744"><a name="p7813744"></a><a name="p7813744"></a>Project ID.</p>
</td>
</tr>
<tr id="row3214835"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p59075108"><a name="p59075108"></a><a name="p59075108"></a>instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p20354482"><a name="p20354482"></a><a name="p20354482"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p38100356"><a name="p38100356"></a><a name="p38100356"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p66230019"><a name="p66230019"></a><a name="p66230019"></a>DCS instance ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section59434435"></a>

None.

## Response<a name="section65147869"></a>

-   Status code:

    If status code "204 No content" is returned, this request is fulfilled. For description of other status codes, see  [API Usage Guidelines](api-usage-guidelines.md).

-   Response parameter:

    None.

-   Example response:

    None.


