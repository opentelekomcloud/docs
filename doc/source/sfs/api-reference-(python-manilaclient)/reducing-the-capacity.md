# Reducing the Capacity<a name="EN-US_TOPIC_0090543966"></a>

## Function<a name="section48498427153619"></a>

This interface is used to reduce the capacity of a shared file system.

>![](/images/icon-note.gif) **NOTE:**   
>This interface is an asynchronous interface. Successful command execution only indicates that the command is successfully delivered. Later, you can refer to  [Querying Details About a Shared File System](querying-details-about-a-shared-file-system.md)  to identify whether capacity reducing is complete and successful.  

## Command<a name="section56091105153619"></a>

-   Usage

    ```
    manila shrink <share> <new_size>
    ```

-   Parameter description

    <a name="table26732828153619"></a>
    <table><thead align="left"><tr id="row38219268153619"><th class="cellrowborder" valign="top" width="16.16161616161616%" id="mcps1.1.5.1.1"><p id="p8753016153619"><a name="p8753016153619"></a><a name="p8753016153619"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.21212121212121%" id="mcps1.1.5.1.2"><p id="p37905659153619"><a name="p37905659153619"></a><a name="p37905659153619"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.13131313131313%" id="mcps1.1.5.1.3"><p id="p50459576153619"><a name="p50459576153619"></a><a name="p50459576153619"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="49.494949494949495%" id="mcps1.1.5.1.4"><p id="p60693845153619"><a name="p60693845153619"></a><a name="p60693845153619"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row17254394153619"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p55428688153619"><a name="p55428688153619"></a><a name="p55428688153619"></a>share</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.2 "><p id="p60538750153619"><a name="p60538750153619"></a><a name="p60538750153619"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.5.1.3 "><p id="p4691757153619"><a name="p4691757153619"></a><a name="p4691757153619"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.1.5.1.4 "><p id="p44488069153619"><a name="p44488069153619"></a><a name="p44488069153619"></a>Specifies the UUID or name of the shared file system.</p>
    </td>
    </tr>
    <tr id="row64848303153619"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p18221206153619"><a name="p18221206153619"></a><a name="p18221206153619"></a>new_size</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.2 "><p id="p66631610153619"><a name="p66631610153619"></a><a name="p66631610153619"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.5.1.3 "><p id="p41171302142119"><a name="p41171302142119"></a><a name="p41171302142119"></a>integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.1.5.1.4 "><p id="p4444221514210"><a name="p4444221514210"></a><a name="p4444221514210"></a>Specifies the post-reduction capacity of the shared file system in GB.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example command

    ```
    manila shrink 52820f82-1419-4f4c-a032-e97e310f5505 5
    ```


## Response<a name="section4739757153619"></a>

-   Parameter description

    None


-   Example response

    None


