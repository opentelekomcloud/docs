# Querying All Major Versions<a name="EN-US_TOPIC_0090581228"></a>

## Function<a name="section28874420153615"></a>

This interface is used to query all major versions.

## Command<a name="section44378387153615"></a>

-   Usage

    ```
    manila api-version
    ```

-   Parameter description

    None

-   Example command

    ```
    manila api-version
    ```


## Response<a name="section35893912153615"></a>

-   Parameter description

    <a name="table26732828153619"></a>
    <table><thead align="left"><tr id="row38219268153619"><th class="cellrowborder" valign="top" width="26.12261226122612%" id="mcps1.1.5.1.1"><p id="p8753016153619"><a name="p8753016153619"></a><a name="p8753016153619"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.861686168616863%" id="mcps1.1.5.1.2"><p id="p37905659153619"><a name="p37905659153619"></a><a name="p37905659153619"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.802180218021803%" id="mcps1.1.5.1.3"><p id="p50459576153619"><a name="p50459576153619"></a><a name="p50459576153619"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="35.21352135213521%" id="mcps1.1.5.1.4"><p id="p60693845153619"><a name="p60693845153619"></a><a name="p60693845153619"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row17254394153619"><td class="cellrowborder" valign="top" width="26.12261226122612%" headers="mcps1.1.5.1.1 "><p id="p55428688153619"><a name="p55428688153619"></a><a name="p55428688153619"></a>ID</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.861686168616863%" headers="mcps1.1.5.1.2 "><p id="p60538750153619"><a name="p60538750153619"></a><a name="p60538750153619"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.802180218021803%" headers="mcps1.1.5.1.3 "><p id="p4691757153619"><a name="p4691757153619"></a><a name="p4691757153619"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.21352135213521%" headers="mcps1.1.5.1.4 "><p id="p44488069153619"><a name="p44488069153619"></a><a name="p44488069153619"></a>Version ID</p>
    </td>
    </tr>
    <tr id="row64848303153619"><td class="cellrowborder" valign="top" width="26.12261226122612%" headers="mcps1.1.5.1.1 "><p id="p18221206153619"><a name="p18221206153619"></a><a name="p18221206153619"></a>Status</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.861686168616863%" headers="mcps1.1.5.1.2 "><p id="p66631610153619"><a name="p66631610153619"></a><a name="p66631610153619"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.802180218021803%" headers="mcps1.1.5.1.3 "><p id="p41171302142119"><a name="p41171302142119"></a><a name="p41171302142119"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.21352135213521%" headers="mcps1.1.5.1.4 "><p id="p4444221514210"><a name="p4444221514210"></a><a name="p4444221514210"></a>Version status The available values are <strong id="b126537594535"><a name="b126537594535"></a><a name="b126537594535"></a>CURRENT</strong>, <strong id="b6140143155415"><a name="b6140143155415"></a><a name="b6140143155415"></a>SUPPORTED</strong>, and <strong id="b4821209115415"><a name="b4821209115415"></a><a name="b4821209115415"></a>DEPRECATED</strong>.</p>
    </td>
    </tr>
    <tr id="row56583452143557"><td class="cellrowborder" valign="top" width="26.12261226122612%" headers="mcps1.1.5.1.1 "><p id="p19856909143557"><a name="p19856909143557"></a><a name="p19856909143557"></a>Version</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.861686168616863%" headers="mcps1.1.5.1.2 "><p id="p64905798143557"><a name="p64905798143557"></a><a name="p64905798143557"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.802180218021803%" headers="mcps1.1.5.1.3 "><p id="p29457285143623"><a name="p29457285143623"></a><a name="p29457285143623"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.21352135213521%" headers="mcps1.1.5.1.4 "><p id="p41204659143557"><a name="p41204659143557"></a><a name="p41204659143557"></a>Version number</p>
    </td>
    </tr>
    <tr id="row4662971614361"><td class="cellrowborder" valign="top" width="26.12261226122612%" headers="mcps1.1.5.1.1 "><p id="p1891066914361"><a name="p1891066914361"></a><a name="p1891066914361"></a>Minimum Version</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.861686168616863%" headers="mcps1.1.5.1.2 "><p id="p5536919014361"><a name="p5536919014361"></a><a name="p5536919014361"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.802180218021803%" headers="mcps1.1.5.1.3 "><p id="p33449951143625"><a name="p33449951143625"></a><a name="p33449951143625"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.21352135213521%" headers="mcps1.1.5.1.4 "><p id="p1697487314361"><a name="p1697487314361"></a><a name="p1697487314361"></a>Minimum version</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    +------+-----------+---------+-----------------+
    | ID   | Status    | Version | Minimum Version |
    +------+-----------+---------+-----------------+
    | v1.0 | SUPPORTED |         |                 |
    | v2.0 | CURRENT   | 2.28    | 2.0             |
    +------+-----------+---------+-----------------+
    ```


