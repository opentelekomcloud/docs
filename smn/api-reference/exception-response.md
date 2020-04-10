# Exception Response<a name="smn_api_63001"></a>

-   Parameter description

    <a name="table53326251195228"></a>
    <table><thead align="left"><tr id="row18693265195228"><th class="cellrowborder" valign="top" width="15.310000000000002%" id="mcps1.1.4.1.1"><p id="p37759514195228"><a name="p37759514195228"></a><a name="p37759514195228"></a><strong id="b842352706191030"><a name="b842352706191030"></a><a name="b842352706191030"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="26.529999999999998%" id="mcps1.1.4.1.2"><p id="p38621763195228"><a name="p38621763195228"></a><a name="p38621763195228"></a><strong id="b84235270619112"><a name="b84235270619112"></a><a name="b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="58.160000000000004%" id="mcps1.1.4.1.3"><p id="p41355060195228"><a name="p41355060195228"></a><a name="p41355060195228"></a><strong id="b84235270619115"><a name="b84235270619115"></a><a name="b84235270619115"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row61425558195228"><td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.4.1.1 "><p id="p9414288195228"><a name="p9414288195228"></a><a name="p9414288195228"></a>request_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.1.4.1.2 "><p id="p24359883195228"><a name="p24359883195228"></a><a name="p24359883195228"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.1.4.1.3 "><p id="p26993519195228"><a name="p26993519195228"></a><a name="p26993519195228"></a>Request ID</p>
    </td>
    </tr>
    <tr id="row41615079195228"><td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.4.1.1 "><p id="p15378234195228"><a name="p15378234195228"></a><a name="p15378234195228"></a>code</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.1.4.1.2 "><p id="p37677450195228"><a name="p37677450195228"></a><a name="p37677450195228"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.1.4.1.3 "><p id="p31974590195228"><a name="p31974590195228"></a><a name="p31974590195228"></a>See section <a href="error-code.md">Error Code</a>.</p>
    </td>
    </tr>
    <tr id="row19335857195228"><td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.4.1.1 "><p id="p22700599195228"><a name="p22700599195228"></a><a name="p22700599195228"></a>message</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.1.4.1.2 "><p id="p26809237195228"><a name="p26809237195228"></a><a name="p26809237195228"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.1.4.1.3 "><p id="p24064628195228"><a name="p24064628195228"></a><a name="p24064628195228"></a>See section <a href="error-code.md">Error Code</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example

    ```
    {
        "request_id": "aad0860d089c482b943971f802a6718e",
        "code": "SMN.0006",
        "message": "Topic not found."
    }
    ```


