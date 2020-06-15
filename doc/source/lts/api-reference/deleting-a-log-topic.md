# Deleting a Log Topic<a name="lts_02_0009"></a>

## Function<a name="section47241003"></a>

This function describes how to delete a log topic that will not be used.

>![](/images/icon-note.gif) **NOTE:**   
>Before deleting a log topic, ensure that the log topic has no log transfer task. Deleted log topics cannot be recovered. Therefore, exercise caution when performing this deletion operation.  

## URI<a name="section22515847"></a>

-   URI format

    DELETE /v2.0/\{project\_id\}/log-groups/\{group\_id\}/log-topics/\{topic\_id\}


-   Parameter description

    **Table  1**  Parameter description

    <a name="table4681258"></a>
    <table><thead align="left"><tr id="row27052584"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p43775699"><a name="p43775699"></a><a name="p43775699"></a><strong id="b128317754613"><a name="b128317754613"></a><a name="b128317754613"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p56170706"><a name="p56170706"></a><a name="p56170706"></a><strong id="b1819188124617"><a name="b1819188124617"></a><a name="b1819188124617"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p53533326"><a name="p53533326"></a><a name="p53533326"></a><strong id="b12937918465"><a name="b12937918465"></a><a name="b12937918465"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p41232110"><a name="p41232110"></a><a name="p41232110"></a><strong id="b1287389104610"><a name="b1287389104610"></a><a name="b1287389104610"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row51466586"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p8043963"><a name="p8043963"></a><a name="p8043963"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p47581305"><a name="p47581305"></a><a name="p47581305"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p28880507"><a name="p28880507"></a><a name="p28880507"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p57619754"><a name="p57619754"></a><a name="p57619754"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row48815741"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p61760986"><a name="p61760986"></a><a name="p61760986"></a>group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p36583959"><a name="p36583959"></a><a name="p36583959"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p10510684"><a name="p10510684"></a><a name="p10510684"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p46059090"><a name="p46059090"></a><a name="p46059090"></a>Specifies the ID of the created log group.</p>
    </td>
    </tr>
    <tr id="row11878631"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p22645032"><a name="p22645032"></a><a name="p22645032"></a>topic_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p22308335"><a name="p22308335"></a><a name="p22308335"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p62144673"><a name="p62144673"></a><a name="p62144673"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p553768"><a name="p553768"></a><a name="p553768"></a>Specifies the ID of the created log topic.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section1316036"></a>

-   Request parameters

    None

-   Example request

    ```
    DELETE /v2.0/{project_id}/log-groups/{group_id}/log-topics/{topic_id}
    ```


## Response<a name="section11844332"></a>

-   Parameter description

    None

-   Example response

    None


## Returned Value<a name="section39490126"></a>

-   Normal

    204

-   Abnormal

    For details about status code, see  [Status Code](status-code.md).


