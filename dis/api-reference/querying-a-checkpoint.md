# Querying a Checkpoint<a name="dis_02_0404"></a>

## Function<a name="section16103126193046"></a>

This API is used to query a checkpoint.

When querying a checkpoint, you need to specify the stream name, partition ID, and application name.

## URI<a name="section62236792193046"></a>

-   URI format

    GET /v2/\{project\_id\}/checkpoints\{?stream\_name,partition\_id,app\_name,checkpoint\_type\}

-   Parameter description

    None


## Request<a name="section50632090193046"></a>

-   Example request

    ```
    GET https://{ip}{endpoint}/v2/{project_id}/checkpoints?stream_name=stream_name_test&partition_id=0&app_name=app_name&checkpoint_type=LAST_READ
    ```

-   Parameter description

    **Table  1**  Parameter description

    <a name="table65625189193046"></a>
    <table><thead align="left"><tr id="row54859673193046"><th class="cellrowborder" valign="top" width="21.42785721427857%" id="mcps1.2.5.1.1"><p id="p14448509193046"><a name="p14448509193046"></a><a name="p14448509193046"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.308469153084694%" id="mcps1.2.5.1.2"><p id="p29478574193046"><a name="p29478574193046"></a><a name="p29478574193046"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.328367163283673%" id="mcps1.2.5.1.3"><p id="p38954259193046"><a name="p38954259193046"></a><a name="p38954259193046"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.93530646935306%" id="mcps1.2.5.1.4"><p id="p1178388193046"><a name="p1178388193046"></a><a name="p1178388193046"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row28340635193046"><td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.1 "><p id="p13890061193046"><a name="p13890061193046"></a><a name="p13890061193046"></a>stream_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.2 "><p id="p51353172193046"><a name="p51353172193046"></a><a name="p51353172193046"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p65966296193046"><a name="p65966296193046"></a><a name="p65966296193046"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.93530646935306%" headers="mcps1.2.5.1.4 "><p id="p41669760193046"><a name="p41669760193046"></a><a name="p41669760193046"></a>Name of the stream created on the management console.</p>
    <p id="p39483525193046"><a name="p39483525193046"></a><a name="p39483525193046"></a>A stream name is 1 to 64 characters long. Only letters, digits, hyphens (-), and underscores (_) are allowed.</p>
    </td>
    </tr>
    <tr id="row19807413193046"><td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.1 "><p id="p60896606193046"><a name="p60896606193046"></a><a name="p60896606193046"></a>partition_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.2 "><p id="p33678052193046"><a name="p33678052193046"></a><a name="p33678052193046"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p43567662193046"><a name="p43567662193046"></a><a name="p43567662193046"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.93530646935306%" headers="mcps1.2.5.1.4 "><p id="p39319716193046"><a name="p39319716193046"></a><a name="p39319716193046"></a>Unique identifier of the partition.</p>
    </td>
    </tr>
    <tr id="row18333132193046"><td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.1 "><p id="p8588720193046"><a name="p8588720193046"></a><a name="p8588720193046"></a>app_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.2 "><p id="p24597749193046"><a name="p24597749193046"></a><a name="p24597749193046"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p46260675193046"><a name="p46260675193046"></a><a name="p46260675193046"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.93530646935306%" headers="mcps1.2.5.1.4 "><p id="p56127169193046"><a name="p56127169193046"></a><a name="p56127169193046"></a>Unique ID of the consumer application.</p>
    <p id="p667293095437"><a name="p667293095437"></a><a name="p667293095437"></a>An application name is 1 to 50 characters long. Only letters, digits, hyphens (-), and underscores (_) are allowed.</p>
    </td>
    </tr>
    <tr id="row35382473193046"><td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.1 "><p id="p47408083193046"><a name="p47408083193046"></a><a name="p47408083193046"></a>checkpoint_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.2 "><p id="p14849505193046"><a name="p14849505193046"></a><a name="p14849505193046"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p61959260193046"><a name="p61959260193046"></a><a name="p61959260193046"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.93530646935306%" headers="mcps1.2.5.1.4 "><p id="p52644139193046"><a name="p52644139193046"></a><a name="p52644139193046"></a>Type of the checkpoint.</p>
    <p id="p4035206193046"><a name="p4035206193046"></a><a name="p4035206193046"></a>The checkpoint type <strong id="b2989063392321"><a name="b2989063392321"></a><a name="b2989063392321"></a>LAST_READ</strong> indicates that only sequence numbers are recorded into the database.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Response<a name="section36316855193046"></a>

-   Example response

    ```
    { 
      "sequence_number": "10",
      "metadata": "metadata"  
    }
    ```

-   Parameter description

    **Table  2**  Response parameter description

    <a name="table2674146193046"></a>
    <table><thead align="left"><tr id="row14919547193046"><th class="cellrowborder" valign="top" width="22.220000000000002%" id="mcps1.2.4.1.1"><p id="p523784193046"><a name="p523784193046"></a><a name="p523784193046"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.18%" id="mcps1.2.4.1.2"><p id="p42426525193046"><a name="p42426525193046"></a><a name="p42426525193046"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="59.599999999999994%" id="mcps1.2.4.1.3"><p id="p13996515193046"><a name="p13996515193046"></a><a name="p13996515193046"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row59975937193046"><td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.1 "><p id="p26212768193046"><a name="p26212768193046"></a><a name="p26212768193046"></a>sequence_number</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p42859496193046"><a name="p42859496193046"></a><a name="p42859496193046"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.599999999999994%" headers="mcps1.2.4.1.3 "><p id="p49067136193046"><a name="p49067136193046"></a><a name="p49067136193046"></a>Unique sequence number. Each data record has a sequence number that is unique within its partition. </p>
    </td>
    </tr>
    <tr id="row38951041193046"><td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.1 "><p id="p917781193046"><a name="p917781193046"></a><a name="p917781193046"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p7231437193046"><a name="p7231437193046"></a><a name="p7231437193046"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.599999999999994%" headers="mcps1.2.4.1.3 "><p id="p48875538193046"><a name="p48875538193046"></a><a name="p48875538193046"></a>Metadata of the consumer application.</p>
    </td>
    </tr>
    </tbody>
    </table>

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If the checkpoint does not exist or expires, the value of  **sequence\_number**  is  **-1**  and the value of  **metadata**  is empty.  


## Status Code<a name="section37226660193046"></a>

-   Normal

    200 OK

-   Failed

    For more information, see  [Error Codes](error-codes.md).


