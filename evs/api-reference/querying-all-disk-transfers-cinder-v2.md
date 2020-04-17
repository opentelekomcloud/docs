# Querying All Disk Transfers<a name="evs_04_2110"></a>

## Function<a name="en-us_topic_0092902036_section44805042171914"></a>

This API is used to query all disk transfers of the current tenant.

## URI<a name="en-us_topic_0092887872_section21748494171940"></a>

-   URI format

    GET /v2/\{project\_id\}/os-volume-transfer

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

    <a name="table114096539515"></a>
    <table><thead align="left"><tr id="row64913538519"><th class="cellrowborder" valign="top" width="17.82178217821782%" id="mcps1.1.5.1.1"><p id="p14491115311514"><a name="p14491115311514"></a><a name="p14491115311514"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.82178217821782%" id="mcps1.1.5.1.2"><p id="p54911753125116"><a name="p54911753125116"></a><a name="p54911753125116"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.772277227722775%" id="mcps1.1.5.1.3"><p id="p10491105315113"><a name="p10491105315113"></a><a name="p10491105315113"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="41.584158415841586%" id="mcps1.1.5.1.4"><p id="p16491553125110"><a name="p16491553125110"></a><a name="p16491553125110"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row64916530515"><td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.5.1.1 "><p id="p14491953135112"><a name="p14491953135112"></a><a name="p14491953135112"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.5.1.2 "><p id="p15491185365111"><a name="p15491185365111"></a><a name="p15491185365111"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.772277227722775%" headers="mcps1.1.5.1.3 "><p id="p349155345117"><a name="p349155345117"></a><a name="p349155345117"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.584158415841586%" headers="mcps1.1.5.1.4 "><p id="p12491175314513"><a name="p12491175314513"></a><a name="p12491175314513"></a>Specifies the maximum number of query results that can be returned.</p>
    <p id="p116095293163"><a name="p116095293163"></a><a name="p116095293163"></a><span id="text138349551887"><a name="text138349551887"></a><a name="text138349551887"></a>The value ranges from 1 to 1000, and the default value is 1000. The returned value cannot exceed this limit.</span></p>
    </td>
    </tr>
    <tr id="row12491135365118"><td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.5.1.1 "><p id="p54911153165115"><a name="p54911153165115"></a><a name="p54911153165115"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.5.1.2 "><p id="p0491145315116"><a name="p0491145315116"></a><a name="p0491145315116"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.772277227722775%" headers="mcps1.1.5.1.3 "><p id="p549165318518"><a name="p549165318518"></a><a name="p549165318518"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.584158415841586%" headers="mcps1.1.5.1.4 "><p id="p164913532515"><a name="p164913532515"></a><a name="p164913532515"></a>Specifies the offset. All disk transfers after this offset will be queried. The value must be an integer greater than 0 but less than the number of disk transfers.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section45527389"></a>

The following example shows how to query details of the disk transfers whose limit is no more than 50.

-   Example request

    ```
    GET https://{endpoint}/v2/{project_id}/os-volume-transfer?limit=50
    ```


## Response<a name="en-us_topic_0092902036_section23586530172122"></a>

-   Parameter description

    <a name="table32915012913"></a>
    <table><thead align="left"><tr id="row12296509296"><th class="cellrowborder" valign="top" width="23.080000000000002%" id="mcps1.1.4.1.1"><p id="p9301250202915"><a name="p9301250202915"></a><a name="p9301250202915"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="24.36%" id="mcps1.1.4.1.2"><p id="p5308506296"><a name="p5308506296"></a><a name="p5308506296"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="52.559999999999995%" id="mcps1.1.4.1.3"><p id="p5306501294"><a name="p5306501294"></a><a name="p5306501294"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row830105052917"><td class="cellrowborder" valign="top" width="23.080000000000002%" headers="mcps1.1.4.1.1 "><p id="p163095013293"><a name="p163095013293"></a><a name="p163095013293"></a>transfers</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.36%" headers="mcps1.1.4.1.2 "><p id="p1230195019292"><a name="p1230195019292"></a><a name="p1230195019292"></a>List&lt;Transfer&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.559999999999995%" headers="mcps1.1.4.1.3 "><p id="p163045017299"><a name="p163045017299"></a><a name="p163045017299"></a>Specifies the disk transfers. For details, see <a href="#li6113282511345">Parameters in the transfers field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li6113282511345"></a>Parameters in the  **transfers**  field

    <a name="en-us_topic_0092902036_table6685576181553"></a>
    <table><thead align="left"><tr id="en-us_topic_0092902036_row1296752181553"><th class="cellrowborder" valign="top" width="23.080000000000002%" id="mcps1.1.4.1.1"><p id="en-us_topic_0092902036_p37928058181553"><a name="en-us_topic_0092902036_p37928058181553"></a><a name="en-us_topic_0092902036_p37928058181553"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="24.36%" id="mcps1.1.4.1.2"><p id="en-us_topic_0092902036_p52273840181553"><a name="en-us_topic_0092902036_p52273840181553"></a><a name="en-us_topic_0092902036_p52273840181553"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="52.559999999999995%" id="mcps1.1.4.1.3"><p id="p3215895113223"><a name="p3215895113223"></a><a name="p3215895113223"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0092902036_row12974480107"><td class="cellrowborder" valign="top" width="23.080000000000002%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0092902036_p1097410819109"><a name="en-us_topic_0092902036_p1097410819109"></a><a name="en-us_topic_0092902036_p1097410819109"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.36%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0092902036_p797448121011"><a name="en-us_topic_0092902036_p797448121011"></a><a name="en-us_topic_0092902036_p797448121011"></a>List&lt; Dict &gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.559999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0092902036_p17974484101"><a name="en-us_topic_0092902036_p17974484101"></a><a name="en-us_topic_0092902036_p17974484101"></a>Specifies the links of the disk transfer.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0092902036_row569771417102"><td class="cellrowborder" valign="top" width="23.080000000000002%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0092902036_p369761461010"><a name="en-us_topic_0092902036_p369761461010"></a><a name="en-us_topic_0092902036_p369761461010"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.36%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0092902036_p769712143104"><a name="en-us_topic_0092902036_p769712143104"></a><a name="en-us_topic_0092902036_p769712143104"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.559999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0092902036_p56979145107"><a name="en-us_topic_0092902036_p56979145107"></a><a name="en-us_topic_0092902036_p56979145107"></a>Specifies the disk ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0092902036_row2457217151019"><td class="cellrowborder" valign="top" width="23.080000000000002%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0092902036_p94571174106"><a name="en-us_topic_0092902036_p94571174106"></a><a name="en-us_topic_0092902036_p94571174106"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.36%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0092902036_p174577172105"><a name="en-us_topic_0092902036_p174577172105"></a><a name="en-us_topic_0092902036_p174577172105"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.559999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0092902036_p18457171718107"><a name="en-us_topic_0092902036_p18457171718107"></a><a name="en-us_topic_0092902036_p18457171718107"></a>Specifies the disk transfer ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0092902036_row527752431012"><td class="cellrowborder" valign="top" width="23.080000000000002%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0092902036_p10277112415105"><a name="en-us_topic_0092902036_p10277112415105"></a><a name="en-us_topic_0092902036_p10277112415105"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.36%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0092902036_p4277132441017"><a name="en-us_topic_0092902036_p4277132441017"></a><a name="en-us_topic_0092902036_p4277132441017"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.559999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0092902036_p827720241108"><a name="en-us_topic_0092902036_p827720241108"></a><a name="en-us_topic_0092902036_p827720241108"></a>Specifies the name of the disk transfer.</p>
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


## Status Codes<a name="en-us_topic_0092902036_section10353980172239"></a>

-   Normal

    200


## Error Codes<a name="section431317151242"></a>

For details, see  [Error Codes](error-codes.md).

