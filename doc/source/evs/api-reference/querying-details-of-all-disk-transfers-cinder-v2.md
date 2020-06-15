# Querying Details of All Disk Transfers<a name="evs_04_2111"></a>

## Function<a name="en-us_topic_0092902037_section44805042171914"></a>

This API is used to query the details of all disk transfers, including the transfer creation time, transfer IDs, and transfer names.

## URI<a name="en-us_topic_0092887872_section21748494171940"></a>

-   URI format

    GET /v2/\{project\_id\}/os-volume-transfer/detail

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
    </tbody>
    </table>

-   Request filter parameters

    <a name="evs_04_2110_table114096539515"></a>
    <table><thead align="left"><tr id="evs_04_2110_row64913538519"><th class="cellrowborder" valign="top" width="17.82178217821782%" id="mcps1.1.5.1.1"><p id="evs_04_2110_p14491115311514"><a name="evs_04_2110_p14491115311514"></a><a name="evs_04_2110_p14491115311514"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.82178217821782%" id="mcps1.1.5.1.2"><p id="evs_04_2110_p54911753125116"><a name="evs_04_2110_p54911753125116"></a><a name="evs_04_2110_p54911753125116"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.772277227722775%" id="mcps1.1.5.1.3"><p id="evs_04_2110_p10491105315113"><a name="evs_04_2110_p10491105315113"></a><a name="evs_04_2110_p10491105315113"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="41.584158415841586%" id="mcps1.1.5.1.4"><p id="evs_04_2110_p16491553125110"><a name="evs_04_2110_p16491553125110"></a><a name="evs_04_2110_p16491553125110"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2110_row64916530515"><td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.5.1.1 "><p id="evs_04_2110_p14491953135112"><a name="evs_04_2110_p14491953135112"></a><a name="evs_04_2110_p14491953135112"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.5.1.2 "><p id="evs_04_2110_p15491185365111"><a name="evs_04_2110_p15491185365111"></a><a name="evs_04_2110_p15491185365111"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.772277227722775%" headers="mcps1.1.5.1.3 "><p id="evs_04_2110_p349155345117"><a name="evs_04_2110_p349155345117"></a><a name="evs_04_2110_p349155345117"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.584158415841586%" headers="mcps1.1.5.1.4 "><p id="evs_04_2110_p12491175314513"><a name="evs_04_2110_p12491175314513"></a><a name="evs_04_2110_p12491175314513"></a>Specifies the maximum number of query results that can be returned.</p>
    <p id="evs_04_2110_p116095293163"><a name="evs_04_2110_p116095293163"></a><a name="evs_04_2110_p116095293163"></a><span id="evs_04_2110_text138349551887"><a name="evs_04_2110_text138349551887"></a><a name="evs_04_2110_text138349551887"></a>The value ranges from 1 to 1000, and the default value is 1000. The returned value cannot exceed this limit.</span></p>
    </td>
    </tr>
    <tr id="evs_04_2110_row12491135365118"><td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.5.1.1 "><p id="evs_04_2110_p54911153165115"><a name="evs_04_2110_p54911153165115"></a><a name="evs_04_2110_p54911153165115"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.5.1.2 "><p id="evs_04_2110_p0491145315116"><a name="evs_04_2110_p0491145315116"></a><a name="evs_04_2110_p0491145315116"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.772277227722775%" headers="mcps1.1.5.1.3 "><p id="evs_04_2110_p549165318518"><a name="evs_04_2110_p549165318518"></a><a name="evs_04_2110_p549165318518"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.584158415841586%" headers="mcps1.1.5.1.4 "><p id="evs_04_2110_p164913532515"><a name="evs_04_2110_p164913532515"></a><a name="evs_04_2110_p164913532515"></a>Specifies the offset. All disk transfers after this offset will be queried. The value must be an integer greater than 0 but less than the number of disk transfers.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section45527389"></a>

The following example shows how to query details of the disk transfers whose limit is no more than 50.

-   Example request

    ```
    GET https://{endpoint}/v2/{project_id}/os-volume-transfer/detail?limit=50
    ```


## Parameter description<a name="en-us_topic_0092902037_section23586530172122"></a>

-   Parameter description

    <a name="table44421424377"></a>
    <table><thead align="left"><tr id="row16442202183720"><th class="cellrowborder" valign="top" width="23.377662233776622%" id="mcps1.1.4.1.1"><p id="p044210213713"><a name="p044210213713"></a><a name="p044210213713"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="23.377662233776622%" id="mcps1.1.4.1.2"><p id="p1944232103719"><a name="p1944232103719"></a><a name="p1944232103719"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.24467553244675%" id="mcps1.1.4.1.3"><p id="p104421529376"><a name="p104421529376"></a><a name="p104421529376"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1944316223713"><td class="cellrowborder" valign="top" width="23.377662233776622%" headers="mcps1.1.4.1.1 "><p id="p124437213370"><a name="p124437213370"></a><a name="p124437213370"></a>transfers</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.377662233776622%" headers="mcps1.1.4.1.2 "><p id="p1944332193718"><a name="p1944332193718"></a><a name="p1944332193718"></a>List&lt;Transfer&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.24467553244675%" headers="mcps1.1.4.1.3 "><p id="p124439263715"><a name="p124439263715"></a><a name="p124439263715"></a>Specifies the disk transfer details. For details, see <a href="#li39411666114933">Parameters in the transfers field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   <a name="li39411666114933"></a>Parameters in the  **transfers**  field

    <a name="en-us_topic_0092902037_table6685576181553"></a>
    <table><thead align="left"><tr id="en-us_topic_0092902037_row1296752181553"><th class="cellrowborder" valign="top" width="23.377662233776622%" id="mcps1.1.4.1.1"><p id="p6080130411503"><a name="p6080130411503"></a><a name="p6080130411503"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="23.377662233776622%" id="mcps1.1.4.1.2"><p id="p2595862911503"><a name="p2595862911503"></a><a name="p2595862911503"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.24467553244675%" id="mcps1.1.4.1.3"><p id="p5937927111503"><a name="p5937927111503"></a><a name="p5937927111503"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0092902037_row12974480107"><td class="cellrowborder" valign="top" width="23.377662233776622%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0092902037_p1097410819109"><a name="en-us_topic_0092902037_p1097410819109"></a><a name="en-us_topic_0092902037_p1097410819109"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.377662233776622%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0092902037_p797448121011"><a name="en-us_topic_0092902037_p797448121011"></a><a name="en-us_topic_0092902037_p797448121011"></a>List&lt; Dict &gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.24467553244675%" headers="mcps1.1.4.1.3 "><p id="p62103920115039"><a name="p62103920115039"></a><a name="p62103920115039"></a>Specifies the links of the disk transfer.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0092902037_row862121220101"><td class="cellrowborder" valign="top" width="23.377662233776622%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0092902037_p1762112141010"><a name="en-us_topic_0092902037_p1762112141010"></a><a name="en-us_topic_0092902037_p1762112141010"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.377662233776622%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0092902037_p4623123109"><a name="en-us_topic_0092902037_p4623123109"></a><a name="en-us_topic_0092902037_p4623123109"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.24467553244675%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0092902037_p186221213104"><a name="en-us_topic_0092902037_p186221213104"></a><a name="en-us_topic_0092902037_p186221213104"></a>Specifies the time when the disk transfer was created.</p>
    <p id="p418335273815"><a name="p418335273815"></a><a name="p418335273815"></a><span id="text164869573817"><a name="text164869573817"></a><a name="text164869573817"></a>Time format: UTC YYYY-MM-DDTHH:MM:SS.XXXXXX</span></p>
    </td>
    </tr>
    <tr id="en-us_topic_0092902037_row569771417102"><td class="cellrowborder" valign="top" width="23.377662233776622%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0092902037_p369761461010"><a name="en-us_topic_0092902037_p369761461010"></a><a name="en-us_topic_0092902037_p369761461010"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.377662233776622%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0092902037_p769712143104"><a name="en-us_topic_0092902037_p769712143104"></a><a name="en-us_topic_0092902037_p769712143104"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.24467553244675%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0092902037_p56979145107"><a name="en-us_topic_0092902037_p56979145107"></a><a name="en-us_topic_0092902037_p56979145107"></a>Specifies the disk ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0092902037_row2457217151019"><td class="cellrowborder" valign="top" width="23.377662233776622%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0092902037_p94571174106"><a name="en-us_topic_0092902037_p94571174106"></a><a name="en-us_topic_0092902037_p94571174106"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.377662233776622%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0092902037_p174577172105"><a name="en-us_topic_0092902037_p174577172105"></a><a name="en-us_topic_0092902037_p174577172105"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.24467553244675%" headers="mcps1.1.4.1.3 "><p id="p20497649115033"><a name="p20497649115033"></a><a name="p20497649115033"></a>Specifies the disk transfer ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0092902037_row527752431012"><td class="cellrowborder" valign="top" width="23.377662233776622%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0092902037_p10277112415105"><a name="en-us_topic_0092902037_p10277112415105"></a><a name="en-us_topic_0092902037_p10277112415105"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.377662233776622%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0092902037_p4277132441017"><a name="en-us_topic_0092902037_p4277132441017"></a><a name="en-us_topic_0092902037_p4277132441017"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.24467553244675%" headers="mcps1.1.4.1.3 "><p id="p44618758115033"><a name="p44618758115033"></a><a name="p44618758115033"></a>Specifies the name of the disk transfer.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "transfers": [
            {
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
            }, 
            {
                "id": "f26c0dee-d20d-4e80-8dee-a8d91b9742a1", 
                "created_at": "2015-03-25T03:56:53.081642", 
                "name": "second volume transfer", 
                "volume_id": "673db275-379f-41af-8371-e1652132b4c1", 
                "links": [
                    {
                        "href": "https://localhost/v2/firstproject/os-volume-transfer/2", 
                        "rel": "self"
                    }, 
                    {
                        "href": "https://localhost/firstproject/os-volume-transfer/2", 
                        "rel": "bookmark"
                    }
                ]
            }
        ]
    }
    ```


## Status Codes<a name="en-us_topic_0092902037_section10353980172239"></a>

-   Normal

    200


## Error Codes<a name="section431317151242"></a>

For details, see  [Error Codes](error-codes.md).

