# Querying Details of a Disk Transfer<a name="evs_04_3072"></a>

## Function<a name="en-us_topic_0092902035_section44805042171914"></a>

This API is used to query the details of a disk transfer, including the transfer creation time, transfer ID, and transfer name.

## URI<a name="en-us_topic_0092887872_section21748494171940"></a>

-   URI format

    GET /v3/\{project\_id\}/os-volume-transfer/\{transfer\_id\}

-   Parameter description

    <a name="table5162674110529"></a>
    <table><thead align="left"><tr id="row4741724810529"><th class="cellrowborder" valign="top" width="28.57%" id="mcps1.1.4.1.1"><p id="p1559190910529"><a name="p1559190910529"></a><a name="p1559190910529"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="26.529999999999998%" id="mcps1.1.4.1.2"><p id="p5498513910529"><a name="p5498513910529"></a><a name="p5498513910529"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="44.9%" id="mcps1.1.4.1.3"><p id="p2461124910529"><a name="p2461124910529"></a><a name="p2461124910529"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4735411910529"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p1047843010529"><a name="p1047843010529"></a><a name="p1047843010529"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.1.4.1.2 "><p id="p4344649310529"><a name="p4344649310529"></a><a name="p4344649310529"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.9%" headers="mcps1.1.4.1.3 "><p id="p2950506910529"><a name="p2950506910529"></a><a name="p2950506910529"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row22943135111210"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p53024664151925"><a name="p53024664151925"></a><a name="p53024664151925"></a>transfer_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.1.4.1.2 "><p id="p30503151925"><a name="p30503151925"></a><a name="p30503151925"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.9%" headers="mcps1.1.4.1.3 "><p id="p2470771151925"><a name="p2470771151925"></a><a name="p2470771151925"></a>Specifies the disk transfer ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="en-us_topic_0092902035_section3832507172056"></a>

-   Example request

    ```
    GET  https://{endpoint}/v3/{project_id}/os-volume-transfer/cac5c677-73a9-4288-bb9c-b2ebfb547377
    ```


## Response<a name="section5804104214399"></a>

-   Parameter description

    <a name="evs_04_2109_table6510124331610"></a>
    <table><thead align="left"><tr id="evs_04_2109_row1751054317165"><th class="cellrowborder" valign="top" width="26.32%" id="mcps1.1.4.1.1"><p id="evs_04_2109_p851014331611"><a name="evs_04_2109_p851014331611"></a><a name="evs_04_2109_p851014331611"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.05%" id="mcps1.1.4.1.2"><p id="evs_04_2109_p5510174319163"><a name="evs_04_2109_p5510174319163"></a><a name="evs_04_2109_p5510174319163"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="52.629999999999995%" id="mcps1.1.4.1.3"><p id="evs_04_2109_p45101438167"><a name="evs_04_2109_p45101438167"></a><a name="evs_04_2109_p45101438167"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2109_row175101243141616"><td class="cellrowborder" valign="top" width="26.32%" headers="mcps1.1.4.1.1 "><p id="evs_04_2109_p5510743171617"><a name="evs_04_2109_p5510743171617"></a><a name="evs_04_2109_p5510743171617"></a>transfer</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.05%" headers="mcps1.1.4.1.2 "><p id="evs_04_2109_p115101943131611"><a name="evs_04_2109_p115101943131611"></a><a name="evs_04_2109_p115101943131611"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.629999999999995%" headers="mcps1.1.4.1.3 "><p id="evs_04_2109_p14510134319169"><a name="evs_04_2109_p14510134319169"></a><a name="evs_04_2109_p14510134319169"></a>Specifies the disk transfer details. For details, see <a href="#evs_04_2109_li61468331112723">Parameters in the transfer field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="evs_04_2109_li61468331112723"></a>Parameters in the  **transfer**  field

    <a name="evs_04_2109_en-us_topic_0092902035_table6685576181553"></a>
    <table><thead align="left"><tr id="evs_04_2109_en-us_topic_0092902035_row1296752181553"><th class="cellrowborder" valign="top" width="26.32%" id="mcps1.1.4.1.1"><p id="evs_04_2109_en-us_topic_0092902035_p37928058181553"><a name="evs_04_2109_en-us_topic_0092902035_p37928058181553"></a><a name="evs_04_2109_en-us_topic_0092902035_p37928058181553"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.05%" id="mcps1.1.4.1.2"><p id="evs_04_2109_en-us_topic_0092902035_p52273840181553"><a name="evs_04_2109_en-us_topic_0092902035_p52273840181553"></a><a name="evs_04_2109_en-us_topic_0092902035_p52273840181553"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="52.629999999999995%" id="mcps1.1.4.1.3"><p id="evs_04_2109_en-us_topic_0092902035_p42375363181553"><a name="evs_04_2109_en-us_topic_0092902035_p42375363181553"></a><a name="evs_04_2109_en-us_topic_0092902035_p42375363181553"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2109_en-us_topic_0092902035_row12974480107"><td class="cellrowborder" valign="top" width="26.32%" headers="mcps1.1.4.1.1 "><p id="evs_04_2109_en-us_topic_0092902035_p1097410819109"><a name="evs_04_2109_en-us_topic_0092902035_p1097410819109"></a><a name="evs_04_2109_en-us_topic_0092902035_p1097410819109"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.05%" headers="mcps1.1.4.1.2 "><p id="evs_04_2109_en-us_topic_0092902035_p797448121011"><a name="evs_04_2109_en-us_topic_0092902035_p797448121011"></a><a name="evs_04_2109_en-us_topic_0092902035_p797448121011"></a>List&lt; Dict &gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.629999999999995%" headers="mcps1.1.4.1.3 "><p id="evs_04_2109_en-us_topic_0092902035_p17974484101"><a name="evs_04_2109_en-us_topic_0092902035_p17974484101"></a><a name="evs_04_2109_en-us_topic_0092902035_p17974484101"></a>Specifies the links of the disk transfer.</p>
    </td>
    </tr>
    <tr id="evs_04_2109_en-us_topic_0092902035_row862121220101"><td class="cellrowborder" valign="top" width="26.32%" headers="mcps1.1.4.1.1 "><p id="evs_04_2109_en-us_topic_0092902035_p1762112141010"><a name="evs_04_2109_en-us_topic_0092902035_p1762112141010"></a><a name="evs_04_2109_en-us_topic_0092902035_p1762112141010"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.05%" headers="mcps1.1.4.1.2 "><p id="evs_04_2109_en-us_topic_0092902035_p4623123109"><a name="evs_04_2109_en-us_topic_0092902035_p4623123109"></a><a name="evs_04_2109_en-us_topic_0092902035_p4623123109"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.629999999999995%" headers="mcps1.1.4.1.3 "><p id="evs_04_2109_en-us_topic_0092902035_p186221213104"><a name="evs_04_2109_en-us_topic_0092902035_p186221213104"></a><a name="evs_04_2109_en-us_topic_0092902035_p186221213104"></a>Specifies the time when the disk transfer was created.</p>
    <p id="evs_04_2109_p8210113613819"><a name="evs_04_2109_p8210113613819"></a><a name="evs_04_2109_p8210113613819"></a><span id="evs_04_2109_text164869573817"><a name="evs_04_2109_text164869573817"></a><a name="evs_04_2109_text164869573817"></a>Time format: UTC YYYY-MM-DDTHH:MM:SS.XXXXXX</span></p>
    </td>
    </tr>
    <tr id="evs_04_2109_en-us_topic_0092902035_row569771417102"><td class="cellrowborder" valign="top" width="26.32%" headers="mcps1.1.4.1.1 "><p id="evs_04_2109_en-us_topic_0092902035_p369761461010"><a name="evs_04_2109_en-us_topic_0092902035_p369761461010"></a><a name="evs_04_2109_en-us_topic_0092902035_p369761461010"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.05%" headers="mcps1.1.4.1.2 "><p id="evs_04_2109_en-us_topic_0092902035_p769712143104"><a name="evs_04_2109_en-us_topic_0092902035_p769712143104"></a><a name="evs_04_2109_en-us_topic_0092902035_p769712143104"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.629999999999995%" headers="mcps1.1.4.1.3 "><p id="evs_04_2109_en-us_topic_0092902035_p56979145107"><a name="evs_04_2109_en-us_topic_0092902035_p56979145107"></a><a name="evs_04_2109_en-us_topic_0092902035_p56979145107"></a>Specifies the disk ID.</p>
    </td>
    </tr>
    <tr id="evs_04_2109_en-us_topic_0092902035_row2457217151019"><td class="cellrowborder" valign="top" width="26.32%" headers="mcps1.1.4.1.1 "><p id="evs_04_2109_en-us_topic_0092902035_p94571174106"><a name="evs_04_2109_en-us_topic_0092902035_p94571174106"></a><a name="evs_04_2109_en-us_topic_0092902035_p94571174106"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.05%" headers="mcps1.1.4.1.2 "><p id="evs_04_2109_en-us_topic_0092902035_p174577172105"><a name="evs_04_2109_en-us_topic_0092902035_p174577172105"></a><a name="evs_04_2109_en-us_topic_0092902035_p174577172105"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.629999999999995%" headers="mcps1.1.4.1.3 "><p id="evs_04_2109_en-us_topic_0092902035_p18457171718107"><a name="evs_04_2109_en-us_topic_0092902035_p18457171718107"></a><a name="evs_04_2109_en-us_topic_0092902035_p18457171718107"></a>Specifies the disk transfer ID.</p>
    </td>
    </tr>
    <tr id="evs_04_2109_en-us_topic_0092902035_row527752431012"><td class="cellrowborder" valign="top" width="26.32%" headers="mcps1.1.4.1.1 "><p id="evs_04_2109_en-us_topic_0092902035_p10277112415105"><a name="evs_04_2109_en-us_topic_0092902035_p10277112415105"></a><a name="evs_04_2109_en-us_topic_0092902035_p10277112415105"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.05%" headers="mcps1.1.4.1.2 "><p id="evs_04_2109_en-us_topic_0092902035_p4277132441017"><a name="evs_04_2109_en-us_topic_0092902035_p4277132441017"></a><a name="evs_04_2109_en-us_topic_0092902035_p4277132441017"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.629999999999995%" headers="mcps1.1.4.1.3 "><p id="evs_04_2109_en-us_topic_0092902035_p827720241108"><a name="evs_04_2109_en-us_topic_0092902035_p827720241108"></a><a name="evs_04_2109_en-us_topic_0092902035_p827720241108"></a>Specifies the name of the disk transfer.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "transfer": {
            "id": "cac5c677-73a9-4288-bb9c-b2ebfb547377", 
            "created_at": "2015-02-25T03:56:53.081642", 
            "name": "first volume transfer", 
            "volume_id": "894623a6-e901-4312-aa06-4275e6321cce", 
            "links": [
                {
                    "href": "https://localhost/v2/firstproject/os-volume-transfer/1", 
                    "rel": "self"
                }, 
                {
                    "href": "https://localhost/firstproject/os-volume-transfer/1", 
                    "rel": "bookmark"
                }
            ]
        }
    }
    ```


## Status Codes<a name="en-us_topic_0092887872_section10353980172239"></a>

-   Normal

    200


## Error Codes<a name="section431317151242"></a>

For details, see  [Error Codes](error-codes.md).

