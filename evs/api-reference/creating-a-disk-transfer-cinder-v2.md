# Creating a Disk Transfer<a name="evs_04_2106"></a>

## Function<a name="en-us_topic_0092887872_section44805042171914"></a>

This API is used to create a disk transfer. After the transfer has been created, a transfer ID and an authentication key are returned.

After a disk transfer is created, the disk status changes from  **available**  to  **awaiting-transfer**. Once the disk transfer is accepted, the disk status changes to  **available**  again.

## Constraints<a name="en-us_topic_0092887872_section47607821172029"></a>

A disk transfer can be created only when the disk status is  **available**. The detailed constraints are as follows:

-   Encrypted EVS disks cannot be transferred.
-   EVS disks with backups and snapshots available cannot be transferred.
-   EVS disks associated with backup policies cannot be transferred.
-   EVS disks used as system disks cannot be transferred.
-   EVS disks in EVS replication pairs cannot be transferred.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>If the disk transfer is created using one of the unsupported disks, error code 400 will be returned.  

## URI<a name="section1351917332235"></a>

-   URI format

    POST /v2/\{project\_id\}/os-volume-transfer

-   Parameter description

    <a name="table12146232414"></a>
    <table><thead align="left"><tr id="row1221412122414"><th class="cellrowborder" valign="top" width="28.57%" id="mcps1.1.4.1.1"><p id="p17214424242"><a name="p17214424242"></a><a name="p17214424242"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="26.529999999999998%" id="mcps1.1.4.1.2"><p id="p7214122102419"><a name="p7214122102419"></a><a name="p7214122102419"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="44.9%" id="mcps1.1.4.1.3"><p id="p1021542202417"><a name="p1021542202417"></a><a name="p1021542202417"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row202151428245"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p32155212418"><a name="p32155212418"></a><a name="p32155212418"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.1.4.1.2 "><p id="p721519211241"><a name="p721519211241"></a><a name="p721519211241"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.9%" headers="mcps1.1.4.1.3 "><p id="p6215122152416"><a name="p6215122152416"></a><a name="p6215122152416"></a>Specifies the project ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="en-us_topic_0092887872_section3832507172056"></a>

-   Parameter description

    <a name="table42671863"></a>
    <table><thead align="left"><tr id="row12592542"><th class="cellrowborder" valign="top" width="19.17%" id="mcps1.1.5.1.1"><p id="p13362997"><a name="p13362997"></a><a name="p13362997"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.15%" id="mcps1.1.5.1.2"><p id="p8661001"><a name="p8661001"></a><a name="p8661001"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.380000000000003%" id="mcps1.1.5.1.3"><p id="p30452481"><a name="p30452481"></a><a name="p30452481"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.300000000000004%" id="mcps1.1.5.1.4"><p id="p50731910"><a name="p50731910"></a><a name="p50731910"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5187493615377"><td class="cellrowborder" valign="top" width="19.17%" headers="mcps1.1.5.1.1 "><p id="p4112025815377"><a name="p4112025815377"></a><a name="p4112025815377"></a>transfer</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.15%" headers="mcps1.1.5.1.2 "><p id="p4240658415377"><a name="p4240658415377"></a><a name="p4240658415377"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.380000000000003%" headers="mcps1.1.5.1.3 "><p id="p1238131615377"><a name="p1238131615377"></a><a name="p1238131615377"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.300000000000004%" headers="mcps1.1.5.1.4 "><p id="p6336250715377"><a name="p6336250715377"></a><a name="p6336250715377"></a>Specifies the disk transfer marker. For details, see <a href="#li55316081111336">Parameters in the transfer field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   <a name="li55316081111336"></a>Parameters in the  **transfer**  field

    <a name="en-us_topic_0092887872_table881415614117"></a>
    <table><thead align="left"><tr id="en-us_topic_0092887872_row168152061012"><th class="cellrowborder" valign="top" width="18.181818181818183%" id="mcps1.1.5.1.1"><p id="en-us_topic_0092887872_p17815961816"><a name="en-us_topic_0092887872_p17815961816"></a><a name="en-us_topic_0092887872_p17815961816"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.181818181818183%" id="mcps1.1.5.1.2"><p id="en-us_topic_0092887872_p9815116514"><a name="en-us_topic_0092887872_p9815116514"></a><a name="en-us_topic_0092887872_p9815116514"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.202020202020204%" id="mcps1.1.5.1.3"><p id="en-us_topic_0092887872_p11815176017"><a name="en-us_topic_0092887872_p11815176017"></a><a name="en-us_topic_0092887872_p11815176017"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="43.43434343434344%" id="mcps1.1.5.1.4"><p id="en-us_topic_0092887872_p881596417"><a name="en-us_topic_0092887872_p881596417"></a><a name="en-us_topic_0092887872_p881596417"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0092887872_row6815269119"><td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0092887872_p15774191420418"><a name="en-us_topic_0092887872_p15774191420418"></a><a name="en-us_topic_0092887872_p15774191420418"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0092887872_p11815126917"><a name="en-us_topic_0092887872_p11815126917"></a><a name="en-us_topic_0092887872_p11815126917"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0092887872_p178154611118"><a name="en-us_topic_0092887872_p178154611118"></a><a name="en-us_topic_0092887872_p178154611118"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.43434343434344%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0092887872_p88151664117"><a name="en-us_topic_0092887872_p88151664117"></a><a name="en-us_topic_0092887872_p88151664117"></a>Specifies the disk ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0092887872_row48151561014"><td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0092887872_p1781517616118"><a name="en-us_topic_0092887872_p1781517616118"></a><a name="en-us_topic_0092887872_p1781517616118"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0092887872_p10815136119"><a name="en-us_topic_0092887872_p10815136119"></a><a name="en-us_topic_0092887872_p10815136119"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0092887872_p98151467115"><a name="en-us_topic_0092887872_p98151467115"></a><a name="en-us_topic_0092887872_p98151467115"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.43434343434344%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0092887872_p17815196917"><a name="en-us_topic_0092887872_p17815196917"></a><a name="en-us_topic_0092887872_p17815196917"></a>Specifies the disk transfer name. <span id="text726643673017"><a name="text726643673017"></a><a name="text726643673017"></a>The value can contain a maximum of 255 bytes.</span></p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    {
        "transfer": {
            "volume_id": "c86b9af4-151d-4ead-b62c-5fb967af0e37", 
            "name": "first volume"
        }
    }
    ```


## Response<a name="en-us_topic_0092887872_section23586530172122"></a>

-   Parameter description

    <a name="table367317440212"></a>
    <table><thead align="left"><tr id="row167314412210"><th class="cellrowborder" valign="top" width="24.05%" id="mcps1.1.4.1.1"><p id="p467324415210"><a name="p467324415210"></a><a name="p467324415210"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="24.05%" id="mcps1.1.4.1.2"><p id="p156746441427"><a name="p156746441427"></a><a name="p156746441427"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="51.9%" id="mcps1.1.4.1.3"><p id="p8674134413213"><a name="p8674134413213"></a><a name="p8674134413213"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row196747441326"><td class="cellrowborder" valign="top" width="24.05%" headers="mcps1.1.4.1.1 "><p id="p967411441324"><a name="p967411441324"></a><a name="p967411441324"></a>transfer</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.05%" headers="mcps1.1.4.1.2 "><p id="p106741844324"><a name="p106741844324"></a><a name="p106741844324"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.9%" headers="mcps1.1.4.1.3 "><p id="p1067484418216"><a name="p1067484418216"></a><a name="p1067484418216"></a>Specifies the disk transfer information. For details, see <a href="#li32419762111447">Parameters in the transfer field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li32419762111447"></a>Parameters in the  **transfer**  field

    <a name="en-us_topic_0092887872_table6685576181553"></a>
    <table><thead align="left"><tr id="en-us_topic_0092887872_row1296752181553"><th class="cellrowborder" valign="top" width="24.05%" id="mcps1.1.4.1.1"><p id="en-us_topic_0092887872_p37928058181553"><a name="en-us_topic_0092887872_p37928058181553"></a><a name="en-us_topic_0092887872_p37928058181553"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="24.05%" id="mcps1.1.4.1.2"><p id="en-us_topic_0092887872_p52273840181553"><a name="en-us_topic_0092887872_p52273840181553"></a><a name="en-us_topic_0092887872_p52273840181553"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="51.9%" id="mcps1.1.4.1.3"><p id="en-us_topic_0092887872_p42375363181553"><a name="en-us_topic_0092887872_p42375363181553"></a><a name="en-us_topic_0092887872_p42375363181553"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0092887872_row45833953181553"><td class="cellrowborder" valign="top" width="24.05%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0092887872_p21562735181553"><a name="en-us_topic_0092887872_p21562735181553"></a><a name="en-us_topic_0092887872_p21562735181553"></a>auth_key</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.05%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0092887872_p1751085181553"><a name="en-us_topic_0092887872_p1751085181553"></a><a name="en-us_topic_0092887872_p1751085181553"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.9%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0092887872_p13253466181553"><a name="en-us_topic_0092887872_p13253466181553"></a><a name="en-us_topic_0092887872_p13253466181553"></a>Specifies the authentication key of the disk transfer.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0092887872_row12974480107"><td class="cellrowborder" valign="top" width="24.05%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0092887872_p1097410819109"><a name="en-us_topic_0092887872_p1097410819109"></a><a name="en-us_topic_0092887872_p1097410819109"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.05%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0092887872_p797448121011"><a name="en-us_topic_0092887872_p797448121011"></a><a name="en-us_topic_0092887872_p797448121011"></a>List&lt; Dict &gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.9%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0092887872_p17974484101"><a name="en-us_topic_0092887872_p17974484101"></a><a name="en-us_topic_0092887872_p17974484101"></a>Specifies the links of the disk transfer.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0092887872_row862121220101"><td class="cellrowborder" valign="top" width="24.05%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0092887872_p1762112141010"><a name="en-us_topic_0092887872_p1762112141010"></a><a name="en-us_topic_0092887872_p1762112141010"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.05%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0092887872_p4623123109"><a name="en-us_topic_0092887872_p4623123109"></a><a name="en-us_topic_0092887872_p4623123109"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.9%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0092887872_p186221213104"><a name="en-us_topic_0092887872_p186221213104"></a><a name="en-us_topic_0092887872_p186221213104"></a>Specifies the time when the disk transfer was created.</p>
    <p id="p189414591376"><a name="p189414591376"></a><a name="p189414591376"></a><span id="text164869573817"><a name="text164869573817"></a><a name="text164869573817"></a>Time format: UTC YYYY-MM-DDTHH:MM:SS.XXXXXX</span></p>
    </td>
    </tr>
    <tr id="en-us_topic_0092887872_row569771417102"><td class="cellrowborder" valign="top" width="24.05%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0092887872_p369761461010"><a name="en-us_topic_0092887872_p369761461010"></a><a name="en-us_topic_0092887872_p369761461010"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.05%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0092887872_p769712143104"><a name="en-us_topic_0092887872_p769712143104"></a><a name="en-us_topic_0092887872_p769712143104"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.9%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0092887872_p56979145107"><a name="en-us_topic_0092887872_p56979145107"></a><a name="en-us_topic_0092887872_p56979145107"></a>Specifies the disk ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0092887872_row2457217151019"><td class="cellrowborder" valign="top" width="24.05%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0092887872_p94571174106"><a name="en-us_topic_0092887872_p94571174106"></a><a name="en-us_topic_0092887872_p94571174106"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.05%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0092887872_p174577172105"><a name="en-us_topic_0092887872_p174577172105"></a><a name="en-us_topic_0092887872_p174577172105"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.9%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0092887872_p18457171718107"><a name="en-us_topic_0092887872_p18457171718107"></a><a name="en-us_topic_0092887872_p18457171718107"></a>Specifies the disk transfer ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0092887872_row527752431012"><td class="cellrowborder" valign="top" width="24.05%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0092887872_p10277112415105"><a name="en-us_topic_0092887872_p10277112415105"></a><a name="en-us_topic_0092887872_p10277112415105"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.05%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0092887872_p4277132441017"><a name="en-us_topic_0092887872_p4277132441017"></a><a name="en-us_topic_0092887872_p4277132441017"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.9%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0092887872_p827720241108"><a name="en-us_topic_0092887872_p827720241108"></a><a name="en-us_topic_0092887872_p827720241108"></a>Specifies the name of the disk transfer.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "transfer": {
            "id": "1a7059f5-8ed7-45b7-8d05-2811e5d09f24", 
            "created_at": "2015-02-25T03:56:53.081642", 
            "name": "first volume", 
            "volume_id": "c86b9af4-151d-4ead-b62c-5fb967af0e37", 
            "auth_key": "9266c59563c84664", 
            "links": [
                {
                    "href": "https://localhost/v2/firstproject/os-volume-transfer/3", 
                    "rel": "self"
                }, 
                {
                    "href": "https://localhost/firstproject/os-volume-transfer/3", 
                    "rel": "bookmark"
                }
            ]
        }
    }
    ```


## Status Codes<a name="en-us_topic_0092887872_section10353980172239"></a>

-   Normal

    202


## Error Codes<a name="section431317151242"></a>

For details, see  [Error Codes](error-codes.md).

