# Modifying a Shared File System<a name="EN-US_TOPIC_0090543957"></a>

## Function<a name="section4318564153540"></a>

This interface is used to modify the name and description of a shared file system.

## Command<a name="section61225641153540"></a>

-   Usage

    ```
    manila update [--name <name>] [--description <description>]
                  [--is-public <is_public>]
                  <share>
    ```

-   Parameter description

    <a name="table16185011153540"></a>
    <table><thead align="left"><tr id="row51728907153540"><th class="cellrowborder" valign="top" width="16.16161616161616%" id="mcps1.1.5.1.1"><p id="p29291944153540"><a name="p29291944153540"></a><a name="p29291944153540"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.21212121212121%" id="mcps1.1.5.1.2"><p id="p23837282153540"><a name="p23837282153540"></a><a name="p23837282153540"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.13131313131313%" id="mcps1.1.5.1.3"><p id="p51771680153540"><a name="p51771680153540"></a><a name="p51771680153540"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="49.494949494949495%" id="mcps1.1.5.1.4"><p id="p32756555153540"><a name="p32756555153540"></a><a name="p32756555153540"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row36035274153540"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p33176070153540"><a name="p33176070153540"></a><a name="p33176070153540"></a>share</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.2 "><p id="p2907110153540"><a name="p2907110153540"></a><a name="p2907110153540"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.5.1.3 "><p id="p34149330153540"><a name="p34149330153540"></a><a name="p34149330153540"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.1.5.1.4 "><p id="p14632371153540"><a name="p14632371153540"></a><a name="p14632371153540"></a>Specifies the UUID or name of the shared file system.</p>
    </td>
    </tr>
    <tr id="row64582483153540"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p63798654153540"><a name="p63798654153540"></a><a name="p63798654153540"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.2 "><p id="p308498153540"><a name="p308498153540"></a><a name="p308498153540"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.5.1.3 "><p id="p24988341153540"><a name="p24988341153540"></a><a name="p24988341153540"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.1.5.1.4 "><p id="p582353131135"><a name="p582353131135"></a><a name="p582353131135"></a>Specifies the new name of the shared file system. The value consists of 1 to 255 characters.</p>
    </td>
    </tr>
    <tr id="row29999141153540"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p5307532818516"><a name="p5307532818516"></a><a name="p5307532818516"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.2 "><p id="p1096990818516"><a name="p1096990818516"></a><a name="p1096990818516"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.5.1.3 "><p id="p3332455118516"><a name="p3332455118516"></a><a name="p3332455118516"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.1.5.1.4 "><p id="p165912191151"><a name="p165912191151"></a><a name="p165912191151"></a>Describes the shared file system. The value contains 0 to 255 characters. The default value is <strong id="b1942404712308"><a name="b1942404712308"></a><a name="b1942404712308"></a>None</strong>.</p>
    </td>
    </tr>
    <tr id="row8466343153540"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p3653160318516"><a name="p3653160318516"></a><a name="p3653160318516"></a>is_public</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.2 "><p id="p2569993718516"><a name="p2569993718516"></a><a name="p2569993718516"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.5.1.3 "><p id="p2568549918516"><a name="p2568549918516"></a><a name="p2568549918516"></a>boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.1.5.1.4 "><p id="p40052093102658"><a name="p40052093102658"></a><a name="p40052093102658"></a>(Since API v2.8) Specifies the level of visibility for the shared file system. If this parameter is set to <strong id="b51721838172619"><a name="b51721838172619"></a><a name="b51721838172619"></a>true</strong>, the share can be queried by other tenants using interfaces such as the one in <a href="querying-details-about-a-shared-file-system.md">Querying Details About a Shared File System</a>. If this parameter is set to <strong id="b10174738152618"><a name="b10174738152618"></a><a name="b10174738152618"></a>false</strong>, the share is visible only to the tenant who creates it. The default value is <strong id="b6175143819266"><a name="b6175143819266"></a><a name="b6175143819266"></a>false</strong>.</p>
    <div class="note" id="note484733973710"><a name="note484733973710"></a><a name="note484733973710"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p414515407435"><a name="p414515407435"></a><a name="p414515407435"></a>Share access rules added for different tenants are isolated from each other. Therefore, even if a share is set to be visible to other tenants, the share can only be queried by other tenants using the interface in <a href="querying-details-about-a-shared-file-system.md">Querying Details About a Shared File System</a>. Other tenants are not allowed to mount or use the share.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

-   Example command

    ```
    manila update --name sample1 416112b6-e5c9-4a46-8dd1-80749fc0933
    ```


## Response<a name="section47610802153540"></a>

-   Parameter description

    None

-   Example response

    None


