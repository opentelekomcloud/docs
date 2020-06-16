# Querying Mount Locations of a Shared File System<a name="EN-US_TOPIC_0090543956"></a>

## Function<a name="section39253738153537"></a>

Querying Mount path of a shared file system.

>![](/images/icon-note.gif) **NOTE:**   
>In the command, the value of  **--os-share-api-version**  must be larger than or equal to 2.9.   

## Command<a name="section27599497153537"></a>

-   Usage

    ```
    manila share-export-location-list [--columns <columns>] <share>
    ```

-   Parameter description

    <a name="table57051582153537"></a>
    <table><thead align="left"><tr id="row35344100153537"><th class="cellrowborder" valign="top" width="16.16161616161616%" id="mcps1.1.5.1.1"><p id="p44299813153537"><a name="p44299813153537"></a><a name="p44299813153537"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.21212121212121%" id="mcps1.1.5.1.2"><p id="p31515095153537"><a name="p31515095153537"></a><a name="p31515095153537"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.13131313131313%" id="mcps1.1.5.1.3"><p id="p2585889153537"><a name="p2585889153537"></a><a name="p2585889153537"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="49.494949494949495%" id="mcps1.1.5.1.4"><p id="p8130476153537"><a name="p8130476153537"></a><a name="p8130476153537"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row52842808153537"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p52409021153537"><a name="p52409021153537"></a><a name="p52409021153537"></a>share</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.2 "><p id="p17272286153537"><a name="p17272286153537"></a><a name="p17272286153537"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.5.1.3 "><p id="p56877957153537"><a name="p56877957153537"></a><a name="p56877957153537"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.1.5.1.4 "><p id="p43711767153537"><a name="p43711767153537"></a><a name="p43711767153537"></a>Specifies name or UUID for the shared file system.</p>
    </td>
    </tr>
    <tr id="row61272067104944"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p1705895104947"><a name="p1705895104947"></a><a name="p1705895104947"></a>columns</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.2 "><p id="p3959839104947"><a name="p3959839104947"></a><a name="p3959839104947"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.5.1.3 "><p id="p52311527104947"><a name="p52311527104947"></a><a name="p52311527104947"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.1.5.1.4 "><p id="p9375271104947"><a name="p9375271104947"></a><a name="p9375271104947"></a>Specifies the queried columns, which are separated by commas (,).</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example command

    ```
    manila --os-share-api-version 2.9 share-export-location-list 416112b6-e5c9-4a46-8dd1-80749fc09336
    ```


## Response<a name="section65600317153537"></a>

-   Parameter description

    <a name="table34537888153537"></a>
    <table><thead align="left"><tr id="row12716027153537"><th class="cellrowborder" valign="top" width="14.29%" id="mcps1.1.5.1.1"><p id="p23365306153537"><a name="p23365306153537"></a><a name="p23365306153537"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.310000000000002%" id="mcps1.1.5.1.2"><p id="p13541666153537"><a name="p13541666153537"></a><a name="p13541666153537"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.39%" id="mcps1.1.5.1.3"><p id="p23133146153537"><a name="p23133146153537"></a><a name="p23133146153537"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="51.01%" id="mcps1.1.5.1.4"><p id="p61845514153537"><a name="p61845514153537"></a><a name="p61845514153537"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row43430747153537"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p28229620153537"><a name="p28229620153537"></a><a name="p28229620153537"></a>ID</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p4897918153537"><a name="p4897918153537"></a><a name="p4897918153537"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p61187105153537"><a name="p61187105153537"></a><a name="p61187105153537"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p4501833810547"><a name="p4501833810547"></a><a name="p4501833810547"></a>Specifies the UUID of the mount path of the shared file system.</p>
    </td>
    </tr>
    <tr id="row4778155153537"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p51486271153537"><a name="p51486271153537"></a><a name="p51486271153537"></a>Path</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p9638452153537"><a name="p9638452153537"></a><a name="p9638452153537"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p42517170153537"><a name="p42517170153537"></a><a name="p42517170153537"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p8264171105350"><a name="p8264171105350"></a><a name="p8264171105350"></a>Specifies the path to which the shared file system will be mounted.</p>
    </td>
    </tr>
    <tr id="row57830752153537"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p53779354153537"><a name="p53779354153537"></a><a name="p53779354153537"></a>Preferred</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p61160408153537"><a name="p61160408153537"></a><a name="p61160408153537"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p11703634105555"><a name="p11703634105555"></a><a name="p11703634105555"></a>boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p6385827710567"><a name="p6385827710567"></a><a name="p6385827710567"></a>(Since API v2.14) Identifies which mount locations are most efficient and are used preferentially when multiple mount locations exist. This parameter is reserved, because this feature is not supported currently.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    +--------------------------------------+--------------------------------------------------+-----------+
    | ID                                   | Path                                             | Preferred |
    +--------------------------------------+--------------------------------------------------+-----------+
    | 6014f802-7b74-4fb2-8436-a58c94f86e84 | sfs-nas1.eu-de.otc.t-systems.com:/share-cff11cb8 |           |
    +--------------------------------------+--------------------------------------------------+-----------+
    ```


