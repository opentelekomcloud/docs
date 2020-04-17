# Accepting a Disk Transfer<a name="evs_04_2107"></a>

## Function<a name="en-us_topic_0092901819_section44805042171914"></a>

This API is used to accept a disk transfer through the transfer ID and authentication key.

## Constraints<a name="en-us_topic_0092901819_section47607821172029"></a>

-   Encrypted EVS disks cannot be transferred.
-   EVS disks with backups and snapshots available cannot be transferred.
-   EVS disks associated with backup policies cannot be transferred.
-   EVS disks used as system disks cannot be transferred.
-   EVS disks in EVS replication pairs cannot be transferred.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>If the disk transfer is created using one of the unsupported disks, error code 400 will be returned.  

## URI<a name="section1165125022416"></a>

-   URI format

    POST /v2/\{project\_id\}/os-volume-transfer/\{transfer\_id\}/accept

-   Parameter description

    <a name="table2027517263253"></a>
    <table><thead align="left"><tr id="row102761226182515"><th class="cellrowborder" valign="top" width="28.57%" id="mcps1.1.4.1.1"><p id="p162762026162519"><a name="p162762026162519"></a><a name="p162762026162519"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="26.529999999999998%" id="mcps1.1.4.1.2"><p id="p127642622515"><a name="p127642622515"></a><a name="p127642622515"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="44.9%" id="mcps1.1.4.1.3"><p id="p8276926112511"><a name="p8276926112511"></a><a name="p8276926112511"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row18276426132517"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p7276126172516"><a name="p7276126172516"></a><a name="p7276126172516"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.1.4.1.2 "><p id="p122761326192517"><a name="p122761326192517"></a><a name="p122761326192517"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.9%" headers="mcps1.1.4.1.3 "><p id="p827712613258"><a name="p827712613258"></a><a name="p827712613258"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row127732632517"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p12277192622513"><a name="p12277192622513"></a><a name="p12277192622513"></a>transfer_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.1.4.1.2 "><p id="p927792682512"><a name="p927792682512"></a><a name="p927792682512"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.9%" headers="mcps1.1.4.1.3 "><p id="p19277626182515"><a name="p19277626182515"></a><a name="p19277626182515"></a>Specifies the disk transfer ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="en-us_topic_0092901819_section3832507172056"></a>

-   Parameter description

    <a name="en-us_topic_0093348348_table42671863"></a>
    <table><thead align="left"><tr id="en-us_topic_0093348348_row12592542"><th class="cellrowborder" valign="top" width="18%" id="mcps1.1.5.1.1"><p id="en-us_topic_0093348348_p13362997"><a name="en-us_topic_0093348348_p13362997"></a><a name="en-us_topic_0093348348_p13362997"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18%" id="mcps1.1.5.1.2"><p id="en-us_topic_0093348348_p8661001"><a name="en-us_topic_0093348348_p8661001"></a><a name="en-us_topic_0093348348_p8661001"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="22%" id="mcps1.1.5.1.3"><p id="en-us_topic_0093348348_p30452481"><a name="en-us_topic_0093348348_p30452481"></a><a name="en-us_topic_0093348348_p30452481"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="42%" id="mcps1.1.5.1.4"><p id="en-us_topic_0093348348_p50731910"><a name="en-us_topic_0093348348_p50731910"></a><a name="en-us_topic_0093348348_p50731910"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0093348348_row5187493615377"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0093348348_p4112025815377"><a name="en-us_topic_0093348348_p4112025815377"></a><a name="en-us_topic_0093348348_p4112025815377"></a>accept</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0093348348_p4240658415377"><a name="en-us_topic_0093348348_p4240658415377"></a><a name="en-us_topic_0093348348_p4240658415377"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0093348348_p1238131615377"><a name="en-us_topic_0093348348_p1238131615377"></a><a name="en-us_topic_0093348348_p1238131615377"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="42%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0093348348_p6336250715377"><a name="en-us_topic_0093348348_p6336250715377"></a><a name="en-us_topic_0093348348_p6336250715377"></a>Specifies the disk transfer acceptance marker. For details, see <a href="#li55316081111336">Parameter in the accept field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   <a name="li55316081111336"></a>Parameter in the  **accept**  field

    <a name="en-us_topic_0092887872_table881415614117"></a>
    <table><thead align="left"><tr id="en-us_topic_0092887872_row168152061012"><th class="cellrowborder" valign="top" width="18%" id="mcps1.1.5.1.1"><p id="en-us_topic_0092887872_p17815961816"><a name="en-us_topic_0092887872_p17815961816"></a><a name="en-us_topic_0092887872_p17815961816"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18%" id="mcps1.1.5.1.2"><p id="en-us_topic_0092887872_p9815116514"><a name="en-us_topic_0092887872_p9815116514"></a><a name="en-us_topic_0092887872_p9815116514"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="23%" id="mcps1.1.5.1.3"><p id="en-us_topic_0092887872_p11815176017"><a name="en-us_topic_0092887872_p11815176017"></a><a name="en-us_topic_0092887872_p11815176017"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="41%" id="mcps1.1.5.1.4"><p id="en-us_topic_0092887872_p881596417"><a name="en-us_topic_0092887872_p881596417"></a><a name="en-us_topic_0092887872_p881596417"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0092887872_row6815269119"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.5.1.1 "><p id="p64366674111553"><a name="p64366674111553"></a><a name="p64366674111553"></a>auth_key</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.5.1.2 "><p id="p46318102111553"><a name="p46318102111553"></a><a name="p46318102111553"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.5.1.3 "><p id="p60778811111553"><a name="p60778811111553"></a><a name="p60778811111553"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="41%" headers="mcps1.1.5.1.4 "><p id="p24136681111553"><a name="p24136681111553"></a><a name="p24136681111553"></a>Specifies the authentication key of the disk transfer.</p>
    <p id="p1338232914415"><a name="p1338232914415"></a><a name="p1338232914415"></a>Specifies the authentication key returned during the disk transfer creation.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    {
        "accept": {
            "auth_key": "9266c59563c84664"
        }
    }
    ```


## Response<a name="en-us_topic_0092901819_section23586530172122"></a>

-   Parameter description

    <a name="table1265065712913"></a>
    <table><thead align="left"><tr id="row565045719919"><th class="cellrowborder" valign="top" width="24.67753224677532%" id="mcps1.1.4.1.1"><p id="p965065715915"><a name="p965065715915"></a><a name="p965065715915"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="24.67753224677532%" id="mcps1.1.4.1.2"><p id="p1465018571910"><a name="p1465018571910"></a><a name="p1465018571910"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="50.64493550644935%" id="mcps1.1.4.1.3"><p id="p14650857797"><a name="p14650857797"></a><a name="p14650857797"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1465012571994"><td class="cellrowborder" valign="top" width="24.67753224677532%" headers="mcps1.1.4.1.1 "><p id="p176508571198"><a name="p176508571198"></a><a name="p176508571198"></a>transfer</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.67753224677532%" headers="mcps1.1.4.1.2 "><p id="p165035718911"><a name="p165035718911"></a><a name="p165035718911"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.64493550644935%" headers="mcps1.1.4.1.3 "><p id="p665065715911"><a name="p665065715911"></a><a name="p665065715911"></a>Specifies the disk transfer information. For details, see <a href="#li12496189111714">Parameters in the transfer field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li12496189111714"></a>Parameters in the  **transfer**  field

    <a name="en-us_topic_0092901819_table6685576181553"></a>
    <table><thead align="left"><tr id="en-us_topic_0092901819_row1296752181553"><th class="cellrowborder" valign="top" width="24.67753224677532%" id="mcps1.1.4.1.1"><p id="en-us_topic_0092901819_p37928058181553"><a name="en-us_topic_0092901819_p37928058181553"></a><a name="en-us_topic_0092901819_p37928058181553"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="24.67753224677532%" id="mcps1.1.4.1.2"><p id="en-us_topic_0092901819_p52273840181553"><a name="en-us_topic_0092901819_p52273840181553"></a><a name="en-us_topic_0092901819_p52273840181553"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="50.64493550644935%" id="mcps1.1.4.1.3"><p id="en-us_topic_0092901819_p42375363181553"><a name="en-us_topic_0092901819_p42375363181553"></a><a name="en-us_topic_0092901819_p42375363181553"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0092901819_row569771417102"><td class="cellrowborder" valign="top" width="24.67753224677532%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0092901819_p369761461010"><a name="en-us_topic_0092901819_p369761461010"></a><a name="en-us_topic_0092901819_p369761461010"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.67753224677532%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0092901819_p769712143104"><a name="en-us_topic_0092901819_p769712143104"></a><a name="en-us_topic_0092901819_p769712143104"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.64493550644935%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0092901819_p56979145107"><a name="en-us_topic_0092901819_p56979145107"></a><a name="en-us_topic_0092901819_p56979145107"></a>Specifies the disk ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0092901819_row2457217151019"><td class="cellrowborder" valign="top" width="24.67753224677532%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0092901819_p94571174106"><a name="en-us_topic_0092901819_p94571174106"></a><a name="en-us_topic_0092901819_p94571174106"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.67753224677532%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0092901819_p174577172105"><a name="en-us_topic_0092901819_p174577172105"></a><a name="en-us_topic_0092901819_p174577172105"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.64493550644935%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0092901819_p18457171718107"><a name="en-us_topic_0092901819_p18457171718107"></a><a name="en-us_topic_0092901819_p18457171718107"></a>Specifies the disk transfer ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0092901819_row527752431012"><td class="cellrowborder" valign="top" width="24.67753224677532%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0092901819_p10277112415105"><a name="en-us_topic_0092901819_p10277112415105"></a><a name="en-us_topic_0092901819_p10277112415105"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.67753224677532%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0092901819_p4277132441017"><a name="en-us_topic_0092901819_p4277132441017"></a><a name="en-us_topic_0092901819_p4277132441017"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.64493550644935%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0092901819_p827720241108"><a name="en-us_topic_0092901819_p827720241108"></a><a name="en-us_topic_0092901819_p827720241108"></a>Specifies the name of the disk transfer.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0092901819_row10511614102910"><td class="cellrowborder" valign="top" width="24.67753224677532%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0092901819_p19144131917296"><a name="en-us_topic_0092901819_p19144131917296"></a><a name="en-us_topic_0092901819_p19144131917296"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.67753224677532%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0092901819_p950720235293"><a name="en-us_topic_0092901819_p950720235293"></a><a name="en-us_topic_0092901819_p950720235293"></a>List&lt; Dict &gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.64493550644935%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0092901819_p184902291294"><a name="en-us_topic_0092901819_p184902291294"></a><a name="en-us_topic_0092901819_p184902291294"></a>Specifies the links of the disk transfer.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "transfer": {
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
        }
    }
    ```


## Status Codes<a name="en-us_topic_0092901819_section10353980172239"></a>

-   Normal

    202


## Error Codes<a name="section431317151242"></a>

For details, see  [Error Codes](error-codes.md).

