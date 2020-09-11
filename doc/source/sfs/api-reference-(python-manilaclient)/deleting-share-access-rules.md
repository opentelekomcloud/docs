# Deleting Share Access Rules<a name="EN-US_TOPIC_0090543960"></a>

## Function<a name="section3989864615362"></a>

This interface is used to delete share access rules.

>![](/images/icon-note.gif) **NOTE:**   
>This interface is an asynchronous interface. Successful command execution only indicates that the command is successfully delivered. Later, you can refer to  [Querying Share Access Rules](querying-share-access-rules.md)  to identify whether the rule deletion is complete and successful.  

## Command<a name="section2797522215362"></a>

-   Usage

    ```
    manila access-deny <share> <id>
    ```

-   Parameter description

    <a name="table1649293015362"></a>
    <table><thead align="left"><tr id="row4815421115362"><th class="cellrowborder" valign="top" width="16.16161616161616%" id="mcps1.1.5.1.1"><p id="p817704315362"><a name="p817704315362"></a><a name="p817704315362"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.21212121212121%" id="mcps1.1.5.1.2"><p id="p5836076415362"><a name="p5836076415362"></a><a name="p5836076415362"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.13131313131313%" id="mcps1.1.5.1.3"><p id="p2960141315362"><a name="p2960141315362"></a><a name="p2960141315362"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="49.494949494949495%" id="mcps1.1.5.1.4"><p id="p4890421415362"><a name="p4890421415362"></a><a name="p4890421415362"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row181839215362"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p1307205015362"><a name="p1307205015362"></a><a name="p1307205015362"></a>share</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.2 "><p id="p5220314915362"><a name="p5220314915362"></a><a name="p5220314915362"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.5.1.3 "><p id="p59668915362"><a name="p59668915362"></a><a name="p59668915362"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.1.5.1.4 "><p id="p4833181215362"><a name="p4833181215362"></a><a name="p4833181215362"></a>Specifies the UUID or name of the shared file system.</p>
    </td>
    </tr>
    <tr id="row3233313215362"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p173804415362"><a name="p173804415362"></a><a name="p173804415362"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.2 "><p id="p656385615362"><a name="p656385615362"></a><a name="p656385615362"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.5.1.3 "><p id="p6191032115362"><a name="p6191032115362"></a><a name="p6191032115362"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.1.5.1.4 "><p id="p4868007015362"><a name="p4868007015362"></a><a name="p4868007015362"></a>Specifies the share rule ID.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example command

    ```
    manila access-deny 416112b6-e5c9-4a46-8dd1-80749fc09336 e0347b5c-8aec-402c-af83-775c3b5e0ad0
    ```


## Response<a name="section2799341515362"></a>

-   Parameter description

    None


-   Example response

    None


