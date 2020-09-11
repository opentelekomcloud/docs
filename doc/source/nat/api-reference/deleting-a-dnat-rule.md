# Deleting a DNAT Rule<a name="nat_api_0014"></a>

## Function<a name="section133765317113"></a>

This API is used to delete a DNAT rule.

## URI<a name="section57269908171124"></a>

DELETE /v2.0/dnat\_rules/\{dnat\_rule\_id\}

**Table  1**  Parameter description

<a name="table41603310017"></a>
<table><thead align="left"><tr id="row323012314017"><th class="cellrowborder" valign="top" width="23.54%" id="mcps1.2.5.1.1"><p id="p1023043508"><a name="p1023043508"></a><a name="p1023043508"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.939999999999998%" id="mcps1.2.5.1.2"><p id="p52301036011"><a name="p52301036011"></a><a name="p52301036011"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="18.029999999999998%" id="mcps1.2.5.1.3"><p id="p1823017318015"><a name="p1823017318015"></a><a name="p1823017318015"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="38.49%" id="mcps1.2.5.1.4"><p id="p7230330014"><a name="p7230330014"></a><a name="p7230330014"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row9230031106"><td class="cellrowborder" valign="top" width="23.54%" headers="mcps1.2.5.1.1 "><p id="p1823033907"><a name="p1823033907"></a><a name="p1823033907"></a>dnat_rule_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.939999999999998%" headers="mcps1.2.5.1.2 "><p id="p623013311018"><a name="p623013311018"></a><a name="p623013311018"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.029999999999998%" headers="mcps1.2.5.1.3 "><p id="p42301335017"><a name="p42301335017"></a><a name="p42301335017"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="38.49%" headers="mcps1.2.5.1.4 "><p id="p5230735019"><a name="p5230735019"></a><a name="p5230735019"></a>Specifies the ID of the DNAT rule.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section57861162171148"></a>

None

## Response<a name="section1248980417125"></a>

None

## Examples<a name="section16888175171218"></a>

-   Example request

    ```
    DELETE https://{Endpoint}/v2.0/dnat_rules/a78fb3eb-1654-4710-8742-3fc49d5f04f8
    ```


-   Example response

    ```
    None (STATUS CODE 204)
    ```


## Status Code<a name="section21780566171318"></a>

See  [Status Codes](status-codes.md).

