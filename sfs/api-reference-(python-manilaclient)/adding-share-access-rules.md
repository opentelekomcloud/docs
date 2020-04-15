# Adding Share Access Rules<a name="EN-US_TOPIC_0090543959"></a>

## Function<a name="section37770681153559"></a>

This interface is used to add share access rules.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>-   This interface is an asynchronous interface. After the command is successfully executed, information about share access rules is displayed but this only indicates that the command is successfully delivered. Later, you can refer to  [Querying Share Access Rules](querying-share-access-rules.md)  to identify whether the rule adding is complete and successful.  
>-   APIs whose microversion is 2.28 or later can ignore error statuses of existing share access rules during rule adding. This function takes effect only when python-manilaclient version is 1.12.0 or later and  **--os-share-api-version**  is set to a value greater than or equal to 2.28. An example of sending a request by using a command is as follows:  **manila --os-share-api-version 2.28 access-allow 859059fa-dcb0-47c5-876e-f5a88a8636da cert 0157b53f-4974-4e80-91c9-098532bcaf00**  

## Command<a name="section20192768153559"></a>

-   Usage

    ```
    manila access-allow [--access-level <access_level>]
                        <share> <access_type> <access_to>
    ```

-   Parameter description

    <a name="table20894149153559"></a>
    <table><thead align="left"><tr id="row32257843153559"><th class="cellrowborder" valign="top" width="16.16161616161616%" id="mcps1.1.5.1.1"><p id="p62748452153559"><a name="p62748452153559"></a><a name="p62748452153559"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.21212121212121%" id="mcps1.1.5.1.2"><p id="p49459846153559"><a name="p49459846153559"></a><a name="p49459846153559"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.13131313131313%" id="mcps1.1.5.1.3"><p id="p46824576153559"><a name="p46824576153559"></a><a name="p46824576153559"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="49.494949494949495%" id="mcps1.1.5.1.4"><p id="p34694331153559"><a name="p34694331153559"></a><a name="p34694331153559"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row58777439153559"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p63352082153559"><a name="p63352082153559"></a><a name="p63352082153559"></a>share</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.2 "><p id="p31245055153559"><a name="p31245055153559"></a><a name="p31245055153559"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.5.1.3 "><p id="p47821516153559"><a name="p47821516153559"></a><a name="p47821516153559"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.1.5.1.4 "><p id="p48337569153559"><a name="p48337569153559"></a><a name="p48337569153559"></a>Specifies the UUID or name of the shared file system.</p>
    </td>
    </tr>
    <tr id="row32384943153559"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p5934692153559"><a name="p5934692153559"></a><a name="p5934692153559"></a>access_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.2 "><p id="p10948021153559"><a name="p10948021153559"></a><a name="p10948021153559"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.5.1.3 "><p id="p14374540153559"><a name="p14374540153559"></a><a name="p14374540153559"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.1.5.1.4 "><p id="p20062088114427"><a name="p20062088114427"></a><a name="p20062088114427"></a>Specifies the type of the share access rule. For NFS shared file systems, the value can only be <strong id="b11745369194713"><a name="b11745369194713"></a><a name="b11745369194713"></a>cert</strong>. When this parameter is set to <strong id="b180824665194725"><a name="b180824665194725"></a><a name="b180824665194725"></a>cert</strong> for NFS shared file systems, set <strong id="b207147105894725"><a name="b207147105894725"></a><a name="b207147105894725"></a>access_to</strong> to the VPC ID.</p>
    </td>
    </tr>
    <tr id="row10056900153559"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p9302548153559"><a name="p9302548153559"></a><a name="p9302548153559"></a>access_to</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.2 "><p id="p15308933153559"><a name="p15308933153559"></a><a name="p15308933153559"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.5.1.3 "><p id="p32064062153559"><a name="p32064062153559"></a><a name="p32064062153559"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.1.5.1.4 "><p id="p815612772610"><a name="p815612772610"></a><a name="p815612772610"></a>Specifies the value of the access rule. When the access rule type of the NFS share is cert, the value contains 1 to 64 characters and can only be the VPC ID.</p>
    <div class="note" id="note1379810719612"><a name="note1379810719612"></a><a name="note1379810719612"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p379911712616"><a name="p379911712616"></a><a name="p379911712616"></a>The python-manilaclient tool and command lines support only VPC authorization and does not support IP address authorization. Use the RESTful API to create an access rule for IP address authorization.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row20817199153559"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p8471557153559"><a name="p8471557153559"></a><a name="p8471557153559"></a>access_level</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.2 "><p id="p15107487153559"><a name="p15107487153559"></a><a name="p15107487153559"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.5.1.3 "><p id="p15746917153559"><a name="p15746917153559"></a><a name="p15746917153559"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.1.5.1.4 "><p id="p431937153559"><a name="p431937153559"></a><a name="p431937153559"></a>Specifies the access level of the shared file system. Possible values are <strong id="b327976527114855"><a name="b327976527114855"></a><a name="b327976527114855"></a>ro</strong> (read-only) and <strong id="b360052986114855"><a name="b360052986114855"></a><a name="b360052986114855"></a>rw</strong> (read-write). The default value is <strong id="b842352706174646"><a name="b842352706174646"></a><a name="b842352706174646"></a>rw</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example command

    ```
    manila access-allow 416112b6-e5c9-4a46-8dd1-80749fc09336 cert 996357e2-ecf4-4b60-afc5-89001ee224d6
    ```


-   Example command \(ignoring the error status of existing access rules when adding a share access rule\)

    ```
    manila --os-share-api-version 2.28 access-allow c72067bf-9305-4330-852e-5117a0a949f9 cert 0157b53f-4974-4e80-91c9-098532bcaf00
    ```


## Response<a name="section41904372153559"></a>

-   Parameter description

    <a name="table56680631153559"></a>
    <table><thead align="left"><tr id="row11011802153559"><th class="cellrowborder" valign="top" width="17.49%" id="mcps1.1.5.1.1"><p id="p19540809153559"><a name="p19540809153559"></a><a name="p19540809153559"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.120000000000001%" id="mcps1.1.5.1.2"><p id="p39301729153559"><a name="p39301729153559"></a><a name="p39301729153559"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.38%" id="mcps1.1.5.1.3"><p id="p29323465153559"><a name="p29323465153559"></a><a name="p29323465153559"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="51.01%" id="mcps1.1.5.1.4"><p id="p26390441153559"><a name="p26390441153559"></a><a name="p26390441153559"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row37074714153559"><td class="cellrowborder" valign="top" width="17.49%" headers="mcps1.1.5.1.1 "><p id="p5792261012352"><a name="p5792261012352"></a><a name="p5792261012352"></a>share_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.2 "><p id="p44678403153559"><a name="p44678403153559"></a><a name="p44678403153559"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.38%" headers="mcps1.1.5.1.3 "><p id="p62180913153559"><a name="p62180913153559"></a><a name="p62180913153559"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p284448812632"><a name="p284448812632"></a><a name="p284448812632"></a>Specifies the UUID of the shared file system to which the access rule is added.</p>
    </td>
    </tr>
    <tr id="row31402503153559"><td class="cellrowborder" valign="top" width="17.49%" headers="mcps1.1.5.1.1 "><p id="p60574833153559"><a name="p60574833153559"></a><a name="p60574833153559"></a>access_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.2 "><p id="p7614431153559"><a name="p7614431153559"></a><a name="p7614431153559"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.38%" headers="mcps1.1.5.1.3 "><p id="p12789178153559"><a name="p12789178153559"></a><a name="p12789178153559"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p373992411271"><a name="p373992411271"></a><a name="p373992411271"></a>Specifies the type of the share access rule.</p>
    </td>
    </tr>
    <tr id="row62287668153559"><td class="cellrowborder" valign="top" width="17.49%" headers="mcps1.1.5.1.1 "><p id="p12136317153559"><a name="p12136317153559"></a><a name="p12136317153559"></a>access_to</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.2 "><p id="p43517582153559"><a name="p43517582153559"></a><a name="p43517582153559"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.38%" headers="mcps1.1.5.1.3 "><p id="p35263248153559"><a name="p35263248153559"></a><a name="p35263248153559"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p1090922712714"><a name="p1090922712714"></a><a name="p1090922712714"></a>Specifies the access that the back end grants or denies.</p>
    </td>
    </tr>
    <tr id="row4213120153559"><td class="cellrowborder" valign="top" width="17.49%" headers="mcps1.1.5.1.1 "><p id="p5718450153559"><a name="p5718450153559"></a><a name="p5718450153559"></a>access_level</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.2 "><p id="p60541329153559"><a name="p60541329153559"></a><a name="p60541329153559"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.38%" headers="mcps1.1.5.1.3 "><p id="p4900612153559"><a name="p4900612153559"></a><a name="p4900612153559"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p5769481612728"><a name="p5769481612728"></a><a name="p5769481612728"></a>Specifies the access level of the shared file system.</p>
    </td>
    </tr>
    <tr id="row15776790153559"><td class="cellrowborder" valign="top" width="17.49%" headers="mcps1.1.5.1.1 "><p id="p2851595153559"><a name="p2851595153559"></a><a name="p2851595153559"></a>state</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.2 "><p id="p29652657153559"><a name="p29652657153559"></a><a name="p29652657153559"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.38%" headers="mcps1.1.5.1.3 "><p id="p53055023153559"><a name="p53055023153559"></a><a name="p53055023153559"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p121105177474"><a name="p121105177474"></a><a name="p121105177474"></a>Specifies the status of the share access rule. If the API version is earlier than 2.28, the status of the share access rule is <strong id="b842352706205652"><a name="b842352706205652"></a><a name="b842352706205652"></a>new</strong>, <strong id="b84235270620570"><a name="b84235270620570"></a><a name="b84235270620570"></a>active</strong>, or <strong id="b84235270620573"><a name="b84235270620573"></a><a name="b84235270620573"></a>error</strong>. In 2.28 and later versions, the status of the share access rule is <strong id="b842352706205734"><a name="b842352706205734"></a><a name="b842352706205734"></a>queued_to_apply</strong>, <strong id="b842352706205741"><a name="b842352706205741"></a><a name="b842352706205741"></a>applying</strong>, <strong id="b842352706205747"><a name="b842352706205747"></a><a name="b842352706205747"></a>active</strong>, <strong id="b842352706205753"><a name="b842352706205753"></a><a name="b842352706205753"></a>error</strong>, <strong id="b84235270620581"><a name="b84235270620581"></a><a name="b84235270620581"></a>queued_to_deny</strong>, or <strong id="b84235270620586"><a name="b84235270620586"></a><a name="b84235270620586"></a>denying</strong>.</p>
    </td>
    </tr>
    <tr id="row22406822153559"><td class="cellrowborder" valign="top" width="17.49%" headers="mcps1.1.5.1.1 "><p id="p3013256153559"><a name="p3013256153559"></a><a name="p3013256153559"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.2 "><p id="p42747199153559"><a name="p42747199153559"></a><a name="p42747199153559"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.38%" headers="mcps1.1.5.1.3 "><p id="p39971123153559"><a name="p39971123153559"></a><a name="p39971123153559"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p552481841284"><a name="p552481841284"></a><a name="p552481841284"></a>Specifies the UUID of the share access rule.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    root@n-version-client:~/ca# manila access-allow 416112b6-e5c9-4a46-8dd1-80749fc09336 cert 996357e2-ecf4-4b60-afc5-89001ee224d6
    +--------------+--------------------------------------+
    | Property     | Value                                |
    +--------------+--------------------------------------+
    | access_key   | None                                 |
    | share_id     | 416112b6-e5c9-4a46-8dd1-80749fc09336 |
    | access_type  | cert                                 |
    | access_to    | 996357e2-ecf4-4b60-afc5-89001ee224d6 |
    | access_level | rw                                   |
    | state        | new                                  |
    | id           | e0347b5c-8aec-402c-af83-775c3b5e0ad0 |
    +--------------+--------------------------------------+
    ```

-   Example response \(ignoring the error status of existing access rules when adding a share access rule\)

    ```
    root@n-version-client:~/ca# manila --os-share-api-version 2.28 access-allow  c72067bf-9305-4330-852e-5117a0a949f9 cert 0157b53f-4974-4e80-91c9-098532bcaf00
    +--------------+--------------------------------------+
    | Property     | Value                                |
    +--------------+--------------------------------------+
    | access_key   | None                                 |
    | share_id     | c72067bf-9305-4330-852e-5117a0a949f9 |
    | access_type  | cert                                 |
    | access_to    | 0157b53f-4974-4e80-91c9-098532bcaf00 |
    | access_level | rw                                   |
    | state        | queued_to_apply                      |
    | id           | c503ae9d-9ba5-4d1d-9897-e37b1b043fc0 |
    +--------------+--------------------------------------+
    ```


