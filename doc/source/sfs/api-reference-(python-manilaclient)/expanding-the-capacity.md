# Expanding the Capacity<a name="EN-US_TOPIC_0090543965"></a>

## Function<a name="section28874420153615"></a>

Expanding the capacity of a shared file system.

>![](/images/icon-note.gif) **NOTE:**   
>This interface is an asynchronous interface. Successful command execution only indicates that the command is successfully delivered. Later, you can refer to  [Querying Details About a Shared File System](querying-details-about-a-shared-file-system.md)  to identify whether capacity expansion is complete and successful.  

## Command<a name="section44378387153615"></a>

-   Usage

    ```
    manila extend <share> <new_size>
    ```

-   Parameter description

    <a name="table23795772153615"></a>
    <table><thead align="left"><tr id="row23531140153615"><th class="cellrowborder" valign="top" width="16.16161616161616%" id="mcps1.1.5.1.1"><p id="p26974158153615"><a name="p26974158153615"></a><a name="p26974158153615"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.21212121212121%" id="mcps1.1.5.1.2"><p id="p37423172153615"><a name="p37423172153615"></a><a name="p37423172153615"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.13131313131313%" id="mcps1.1.5.1.3"><p id="p11378128153615"><a name="p11378128153615"></a><a name="p11378128153615"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="49.494949494949495%" id="mcps1.1.5.1.4"><p id="p49213143153615"><a name="p49213143153615"></a><a name="p49213143153615"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row26841667153615"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p5723273142142"><a name="p5723273142142"></a><a name="p5723273142142"></a>share</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.2 "><p id="p60932008142142"><a name="p60932008142142"></a><a name="p60932008142142"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.5.1.3 "><p id="p36545648142142"><a name="p36545648142142"></a><a name="p36545648142142"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.1.5.1.4 "><p id="p7407496142142"><a name="p7407496142142"></a><a name="p7407496142142"></a>Specifies the UUID or name of the shared file system.</p>
    </td>
    </tr>
    <tr id="row44076941153615"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p11750691134012"><a name="p11750691134012"></a><a name="p11750691134012"></a>new_size</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.2 "><p id="p56776725142142"><a name="p56776725142142"></a><a name="p56776725142142"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.5.1.3 "><p id="p35512026142142"><a name="p35512026142142"></a><a name="p35512026142142"></a>integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.1.5.1.4 "><p id="p57901843142142"><a name="p57901843142142"></a><a name="p57901843142142"></a>Specifies the post-expansion capacity of the shared file system in GB.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example command

    ```
    manila extend 416112b6-e5c9-4a46-8dd1-80749fc09336 10
    ```


## Response<a name="section35893912153615"></a>

-   Parameter description

    None


-   Example response

    None


