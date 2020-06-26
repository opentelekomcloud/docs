# Querying Share Access Rules<a name="EN-US_TOPIC_0090543961"></a>

## Function<a name="section4617656515366"></a>

This interface is used to query share access rules.

## Command<a name="section4117552315366"></a>

-   Usage

    ```
    manila access-list [--columns <columns>] <share>
    ```

-   Parameter description

    <a name="table3994131915366"></a>
    <table><thead align="left"><tr id="row2961505215366"><th class="cellrowborder" valign="top" width="16.16161616161616%" id="mcps1.1.5.1.1"><p id="p5000904815366"><a name="p5000904815366"></a><a name="p5000904815366"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.21212121212121%" id="mcps1.1.5.1.2"><p id="p2420105515366"><a name="p2420105515366"></a><a name="p2420105515366"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.13131313131313%" id="mcps1.1.5.1.3"><p id="p1412845915366"><a name="p1412845915366"></a><a name="p1412845915366"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="49.494949494949495%" id="mcps1.1.5.1.4"><p id="p355456415366"><a name="p355456415366"></a><a name="p355456415366"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1948427315366"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p3472229915366"><a name="p3472229915366"></a><a name="p3472229915366"></a>share</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.2 "><p id="p6104282515366"><a name="p6104282515366"></a><a name="p6104282515366"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.5.1.3 "><p id="p4552179615366"><a name="p4552179615366"></a><a name="p4552179615366"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.1.5.1.4 "><p id="p6338683515366"><a name="p6338683515366"></a><a name="p6338683515366"></a>Specifies the UUID or name of the shared file system.</p>
    </td>
    </tr>
    <tr id="row3361060615366"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p3810453515366"><a name="p3810453515366"></a><a name="p3810453515366"></a>columns</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.2 "><p id="p6656845615366"><a name="p6656845615366"></a><a name="p6656845615366"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.5.1.3 "><p id="p2333585015366"><a name="p2333585015366"></a><a name="p2333585015366"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.1.5.1.4 "><p id="p65644562112533"><a name="p65644562112533"></a><a name="p65644562112533"></a>Specifies the queried columns, which are separated by commas (,).</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example command

    ```
    manila access-list 416112b6-e5c9-4a46-8dd1-80749fc09336
    ```


## Response<a name="section3772782815366"></a>

-   Parameter description

    <a name="table3479226615366"></a>
    <table><thead align="left"><tr id="row1371567615366"><th class="cellrowborder" valign="top" width="16.73%" id="mcps1.1.5.1.1"><p id="p3722794415366"><a name="p3722794415366"></a><a name="p3722794415366"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.75%" id="mcps1.1.5.1.2"><p id="p6267351315366"><a name="p6267351315366"></a><a name="p6267351315366"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.51%" id="mcps1.1.5.1.3"><p id="p4338983115366"><a name="p4338983115366"></a><a name="p4338983115366"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="51.01%" id="mcps1.1.5.1.4"><p id="p2491543315366"><a name="p2491543315366"></a><a name="p2491543315366"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row488421615366"><td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.1.5.1.1 "><p id="p6007721115366"><a name="p6007721115366"></a><a name="p6007721115366"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.75%" headers="mcps1.1.5.1.2 "><p id="p3441593115366"><a name="p3441593115366"></a><a name="p3441593115366"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.51%" headers="mcps1.1.5.1.3 "><p id="p3622700715366"><a name="p3622700715366"></a><a name="p3622700715366"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p49341375113210"><a name="p49341375113210"></a><a name="p49341375113210"></a>Specifies the UUID of the share access rule.</p>
    </td>
    </tr>
    <tr id="row5770424615366"><td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.1.5.1.1 "><p id="p4353238115366"><a name="p4353238115366"></a><a name="p4353238115366"></a>access_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.75%" headers="mcps1.1.5.1.2 "><p id="p3646193515366"><a name="p3646193515366"></a><a name="p3646193515366"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.51%" headers="mcps1.1.5.1.3 "><p id="p62677415366"><a name="p62677415366"></a><a name="p62677415366"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p1975583111347"><a name="p1975583111347"></a><a name="p1975583111347"></a>Specifies the type of the share access rule.</p>
    </td>
    </tr>
    <tr id="row5426567815366"><td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.1.5.1.1 "><p id="p3344379915366"><a name="p3344379915366"></a><a name="p3344379915366"></a>access_to</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.75%" headers="mcps1.1.5.1.2 "><p id="p2459323315366"><a name="p2459323315366"></a><a name="p2459323315366"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.51%" headers="mcps1.1.5.1.3 "><p id="p4589488415366"><a name="p4589488415366"></a><a name="p4589488415366"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p54105076113353"><a name="p54105076113353"></a><a name="p54105076113353"></a>Specifies the access that the back end grants or denies.</p>
    </td>
    </tr>
    <tr id="row3715633615366"><td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.1.5.1.1 "><p id="p5687322215366"><a name="p5687322215366"></a><a name="p5687322215366"></a>access_level</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.75%" headers="mcps1.1.5.1.2 "><p id="p4332830615366"><a name="p4332830615366"></a><a name="p4332830615366"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.51%" headers="mcps1.1.5.1.3 "><p id="p1993186515366"><a name="p1993186515366"></a><a name="p1993186515366"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p33162067113336"><a name="p33162067113336"></a><a name="p33162067113336"></a>Specifies the level of the access rule.</p>
    </td>
    </tr>
    <tr id="row3481550915366"><td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.1.5.1.1 "><p id="p148395515366"><a name="p148395515366"></a><a name="p148395515366"></a>state</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.75%" headers="mcps1.1.5.1.2 "><p id="p5309149715366"><a name="p5309149715366"></a><a name="p5309149715366"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.51%" headers="mcps1.1.5.1.3 "><p id="p544400015366"><a name="p544400015366"></a><a name="p544400015366"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p65593034113235"><a name="p65593034113235"></a><a name="p65593034113235"></a>Specifies the status of the access rule. Possible values are <strong id="b176117763095350"><a name="b176117763095350"></a><a name="b176117763095350"></a>active</strong> and <strong id="b163204291095350"><a name="b163204291095350"></a><a name="b163204291095350"></a>error</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    +--------------------------------------+-------------+--------------------------------------+--------------+--------+------------+
    | id                                   | access_type | access_to                            | access_level | state  | access_key |
    +--------------------------------------+-------------+--------------------------------------+--------------+-------+------------+
    | e0347b5c-8aec-402c-af83-775c3b5e0ad0 | cert        | 996357e2-ecf4-4b60-afc5-89001ee224d6 | rw           | active |            |
    | c503ae9d-9ba5-4d1d-9897-e37b1b043fc0 | cert        | 0157b53f-4974-4e80-91c9-098532bcaf00 | rw           | active |            |
    +--------------------------------------+-------------+--------------------------------------+--------------+--------+------------+
    ```


