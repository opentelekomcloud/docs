# Deleting a Log Group<a name="lts_02_0005"></a>

## Function<a name="section18433281"></a>

This function describes how to delete a log group that will not be used.

>![](/images/icon-note.gif) **NOTE:**   
>Before deleting a log group, ensure that the log group has no log transfer tasks. Deleted log groups cannot be recovered. Therefore, exercise caution when performing this deletion operation.  

## URI<a name="section31681806"></a>

-   URI format

    DELETE /v2.0/\{project\_id\}/log-groups/\{group\_id\}


-   Parameter description

    **Table  1**  Parameter description

    <a name="table805068"></a>
    <table><thead align="left"><tr id="row57933110"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p62070358"><a name="p62070358"></a><a name="p62070358"></a><strong id="b136211338339"><a name="b136211338339"></a><a name="b136211338339"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p61643119"><a name="p61643119"></a><a name="p61643119"></a><strong id="b9482113423316"><a name="b9482113423316"></a><a name="b9482113423316"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p27036712"><a name="p27036712"></a><a name="p27036712"></a><strong id="b18481103510334"><a name="b18481103510334"></a><a name="b18481103510334"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p42490025"><a name="p42490025"></a><a name="p42490025"></a><strong id="b19317163614335"><a name="b19317163614335"></a><a name="b19317163614335"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row19139995"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p6835749"><a name="p6835749"></a><a name="p6835749"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p16824816"><a name="p16824816"></a><a name="p16824816"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p20632868"><a name="p20632868"></a><a name="p20632868"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p60649575"><a name="p60649575"></a><a name="p60649575"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row8975271"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p55908359"><a name="p55908359"></a><a name="p55908359"></a>group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p32283211"><a name="p32283211"></a><a name="p32283211"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p64803292"><a name="p64803292"></a><a name="p64803292"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p14575265"><a name="p14575265"></a><a name="p14575265"></a>Specifies the ID of the created log group.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section16700806"></a>

-   Request parameters

    None

-   Example request

    ```
    DELETE /v2.0/{project_id}/log-groups/{group_id}
    ```


## Response<a name="section16089528"></a>

-   Response parameters

    None

-   Example response

    None


## Returned Value<a name="section10588031"></a>

-   Normal

    204

-   Abnormal

    For details about status code, see  [Status Code](status-code.md).


