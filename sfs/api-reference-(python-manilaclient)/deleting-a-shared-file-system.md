# Deleting a Shared File System<a name="EN-US_TOPIC_0090543958"></a>

## Function<a name="section26238950153544"></a>

This API is used to delete a shared file system.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>This interface is an asynchronous interface. Successful command execution only indicates that the command is successfully delivered. Later, you can use the interface described in  [Querying Details About a Shared File System](querying-details-about-a-shared-file-system.md)  to check whether the deletion is complete and successful.  

## Command<a name="section2168539153544"></a>

-   Usage

    ```
    manila delete [--consistency-group <consistency-group>]
                  <share> [<share> ...]
    ```

-   Parameter description

    <a name="table57247685153544"></a>
    <table><thead align="left"><tr id="row8948109153544"><th class="cellrowborder" valign="top" width="16.16161616161616%" id="mcps1.1.5.1.1"><p id="p53708234153544"><a name="p53708234153544"></a><a name="p53708234153544"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.21212121212121%" id="mcps1.1.5.1.2"><p id="p55399716153544"><a name="p55399716153544"></a><a name="p55399716153544"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.13131313131313%" id="mcps1.1.5.1.3"><p id="p58192002153544"><a name="p58192002153544"></a><a name="p58192002153544"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="49.494949494949495%" id="mcps1.1.5.1.4"><p id="p15931725153544"><a name="p15931725153544"></a><a name="p15931725153544"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row15401324153544"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p39547720153544"><a name="p39547720153544"></a><a name="p39547720153544"></a>share</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.2 "><p id="p49248712153544"><a name="p49248712153544"></a><a name="p49248712153544"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.5.1.3 "><p id="p29722708153544"><a name="p29722708153544"></a><a name="p29722708153544"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.1.5.1.4 "><p id="p58729173153544"><a name="p58729173153544"></a><a name="p58729173153544"></a>Specifies the UUID or name of the shared file system.</p>
    </td>
    </tr>
    <tr id="row58800517153544"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p65221456153544"><a name="p65221456153544"></a><a name="p65221456153544"></a>consistency-group</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.2 "><p id="p48446596153544"><a name="p48446596153544"></a><a name="p48446596153544"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.5.1.3 "><p id="p31860167153544"><a name="p31860167153544"></a><a name="p31860167153544"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.1.5.1.4 "><p id="p30536772153544"><a name="p30536772153544"></a><a name="p30536772153544"></a>This parameter is reserved, because consistency groups are not supported currently.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example command

    ```
    manila delete b4e1665d-2a63-4056-855a-4902720a2a07
    ```


## Response<a name="section44280676153544"></a>

-   Parameter description

    None


-   Example response

    None


