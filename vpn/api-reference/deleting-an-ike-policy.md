# Deleting an IKE Policy<a name="en_topic_0093011514"></a>

## **Function**<a name="section11842506"></a>

This interface is used to delete an IKE policy.

## URI<a name="section39473694"></a>

DELETE /v2.0/vpn/ikepolicies/\{ikepolicy\_id\}

**Table  1**  Parameter description

<a name="table492018108144"></a>
<table><thead align="left"><tr id="row29285105141"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p3928151019147"><a name="p3928151019147"></a><a name="p3928151019147"></a><strong id="b842352706172115"><a name="b842352706172115"></a><a name="b842352706172115"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p69359101144"><a name="p69359101144"></a><a name="p69359101144"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p7935510111417"><a name="p7935510111417"></a><a name="p7935510111417"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p893571013140"><a name="p893571013140"></a><a name="p893571013140"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1294311103147"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p1943141015146"><a name="p1943141015146"></a><a name="p1943141015146"></a>ikepolicy_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p69514103140"><a name="p69514103140"></a><a name="p69514103140"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p179517108141"><a name="p179517108141"></a><a name="p179517108141"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p1595131020148"><a name="p1595131020148"></a><a name="p1595131020148"></a>Specifies the IKE policy ID.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section43252647"></a>

None

## Response Message<a name="section53729511"></a>

None

## Example<a name="section13803553"></a>

-   Example Request

    ```
    DELETE /v2.0/vpn/ikepolicies/{ikepolicy_id}
    ```


-   Example Response

    None


## Returned Values<a name="section6578292"></a>

For details, see section  [Common Returned Values](common-returned-values.md).

