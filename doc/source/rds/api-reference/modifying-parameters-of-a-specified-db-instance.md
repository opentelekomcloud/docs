# Modifying Parameters of a Specified DB Instance<a name="rds_09_0305"></a>

## Function<a name="section563650143816"></a>

This API is used to modify parameters in the parameter template of a specified DB instance.

-   Learn how to  [authorize and authenticate](authentication.md)  this API before using it.
-   Before calling this API, obtain the required  [region and endpoint](https://docs.otc.t-systems.com/en-us/endpoint/index.html).

## Constraints<a name="section1461493103419"></a>

-   The following DB engines are supported: MySQL, PostgreSQL, and Microsoft SQL Server.
-   For Microsoft SQL Server, only the following editions are supported: Microsoft SQL Server 2014 SE, 2016 SE, and 2016 EE.

-   The values of the edited parameters must be within the default value range of the specified database version. For details about the range of parameter values, see the "Modifying Parameters in a Parameter Template" section in the  _Relational Database Service User Guide_.

## URI<a name="section116519011384"></a>

-   URI format

    PUT https://\{_Endpoint_\}/v3/\{project\_id\}/instances/\{instance\_id\}/configurations

-   Example

    https://rds.eu-de.otc.t-systems.com/v3/0483b6b16e954cb88930a360d2c4e663/instances/dsfae23fsfdsae3435in01/configurations

-   Parameter description

    **Table  1**  Parameter description

    <a name="table156666010383"></a>
    <table><thead align="left"><tr id="row18948107387"><th class="cellrowborder" valign="top" width="21.21%" id="mcps1.2.4.1.1"><p id="p1194880153810"><a name="p1194880153810"></a><a name="p1194880153810"></a><strong id="b84235270691445"><a name="b84235270691445"></a><a name="b84235270691445"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.67%" id="mcps1.2.4.1.2"><p id="p594815053817"><a name="p594815053817"></a><a name="p594815053817"></a><strong>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="51.12%" id="mcps1.2.4.1.3"><p id="p394813018383"><a name="p394813018383"></a><a name="p394813018383"></a><strong id="b842352706163417"><a name="b842352706163417"></a><a name="b842352706163417"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2948130153820"><td class="cellrowborder" valign="top" width="21.21%" headers="mcps1.2.4.1.1 "><p id="p129488015381"><a name="p129488015381"></a><a name="p129488015381"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.67%" headers="mcps1.2.4.1.2 "><p id="p29482006386"><a name="p29482006386"></a><a name="p29482006386"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.12%" headers="mcps1.2.4.1.3 "><p id="p1594814073813"><a name="p1594814073813"></a><a name="p1594814073813"></a>Specifies the project ID of a tenant in a region.</p>
    <p id="p88831119867"><a name="p88831119867"></a><a name="p88831119867"></a>For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row17948707388"><td class="cellrowborder" valign="top" width="21.21%" headers="mcps1.2.4.1.1 "><p id="p1094811012382"><a name="p1094811012382"></a><a name="p1094811012382"></a>instance_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.67%" headers="mcps1.2.4.1.2 "><p id="p4948205386"><a name="p4948205386"></a><a name="p4948205386"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.12%" headers="mcps1.2.4.1.3 "><p id="p194814033815"><a name="p194814033815"></a><a name="p194814033815"></a>Specifies the DB instance ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section37136013381"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table17301053815"></a>
    <table><thead align="left"><tr id="row17964120113817"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.1"><p id="p1296414014382"><a name="p1296414014382"></a><a name="p1296414014382"></a><strong id="b1825700343"><a name="b1825700343"></a><a name="b1825700343"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="26%" id="mcps1.2.5.1.2"><p id="p119641902388"><a name="p119641902388"></a><a name="p119641902388"></a><strong>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="p14964140103819"><a name="p14964140103819"></a><a name="p14964140103819"></a><strong id="b842352706164541"><a name="b842352706164541"></a><a name="b842352706164541"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="37%" id="mcps1.2.5.1.4"><p id="p1596410023814"><a name="p1596410023814"></a><a name="p1596410023814"></a><strong id="b603618804"><a name="b603618804"></a><a name="b603618804"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row7964102380"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p179641309380"><a name="p179641309380"></a><a name="p179641309380"></a>values</p>
    </td>
    <td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.5.1.2 "><p id="p169644053814"><a name="p169644053814"></a><a name="p169644053814"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="p09646073812"><a name="p09646073812"></a><a name="p09646073812"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.5.1.4 "><p id="p09641305389"><a name="p09641305389"></a><a name="p09641305389"></a>Specifies the parameter values defined by users based on the default parameter templates.</p>
    <p id="p128891559123615"><a name="p128891559123615"></a><a name="p128891559123615"></a>For details, see <a href="#table12745180163820">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  values field data structure description

    <a name="table12745180163820"></a>
    <table><thead align="left"><tr id="row19643018386"><th class="cellrowborder" valign="top" width="20.169999999999998%" id="mcps1.2.5.1.1"><p id="p896413010389"><a name="p896413010389"></a><a name="p896413010389"></a><strong id="b1672634051"><a name="b1672634051"></a><a name="b1672634051"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="26.369999999999997%" id="mcps1.2.5.1.2"><p id="p149647093818"><a name="p149647093818"></a><a name="p149647093818"></a><strong>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.73%" id="mcps1.2.5.1.3"><p id="p1096416010381"><a name="p1096416010381"></a><a name="p1096416010381"></a><strong id="b491897444"><a name="b491897444"></a><a name="b491897444"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="36.730000000000004%" id="mcps1.2.5.1.4"><p id="p1964150113810"><a name="p1964150113810"></a><a name="p1964150113810"></a><strong id="b2142018081"><a name="b2142018081"></a><a name="b2142018081"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row696470153811"><td class="cellrowborder" valign="top" width="20.169999999999998%" headers="mcps1.2.5.1.1 "><p id="p17964130193815"><a name="p17964130193815"></a><a name="p17964130193815"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.369999999999997%" headers="mcps1.2.5.1.2 "><p id="p1096417018381"><a name="p1096417018381"></a><a name="p1096417018381"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="p4964100163820"><a name="p4964100163820"></a><a name="p4964100163820"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.730000000000004%" headers="mcps1.2.5.1.4 "><p id="p19642053818"><a name="p19642053818"></a><a name="p19642053818"></a>Specifies the parameter name. For example, in <strong id="b84235270621563"><a name="b84235270621563"></a><a name="b84235270621563"></a>"max_connections": "10"</strong>, the key is <strong id="b842352706215241"><a name="b842352706215241"></a><a name="b842352706215241"></a>max_connections</strong>.</p>
    </td>
    </tr>
    <tr id="row1196415053814"><td class="cellrowborder" valign="top" width="20.169999999999998%" headers="mcps1.2.5.1.1 "><p id="p696411018385"><a name="p696411018385"></a><a name="p696411018385"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.369999999999997%" headers="mcps1.2.5.1.2 "><p id="p9964401383"><a name="p9964401383"></a><a name="p9964401383"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="p09647018388"><a name="p09647018388"></a><a name="p09647018388"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.730000000000004%" headers="mcps1.2.5.1.4 "><p id="p209641004383"><a name="p209641004383"></a><a name="p209641004383"></a>Specifies the parameter value. For example, in <strong id="b953814020215624"><a name="b953814020215624"></a><a name="b953814020215624"></a>"max_connections": "10"</strong>, the value is <strong id="b842352706215633"><a name="b842352706215633"></a><a name="b842352706215633"></a>10</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Request example

    ```
    { 
        "values": { 
           "max_connections": "10", 
           "autocommit": "OFF" 
        }
    }
    ```


## Response<a name="section77762093812"></a>

-   Normal response

    **Table  4**  Parameter description

    <a name="table1477614093818"></a>
    <table><thead align="left"><tr id="row6964308384"><th class="cellrowborder" valign="top" width="25.509999999999998%" id="mcps1.2.4.1.1"><p id="p1096410017380"><a name="p1096410017380"></a><a name="p1096410017380"></a><strong id="b345595144"><a name="b345595144"></a><a name="b345595144"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="40.82%" id="mcps1.2.4.1.2"><p id="p129648023816"><a name="p129648023816"></a><a name="p129648023816"></a><strong id="b392854292"><a name="b392854292"></a><a name="b392854292"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.67%" id="mcps1.2.4.1.3"><p id="p169647014384"><a name="p169647014384"></a><a name="p169647014384"></a><strong id="b1079786441"><a name="b1079786441"></a><a name="b1079786441"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row096412073812"><td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.4.1.1 "><p id="p896419003819"><a name="p896419003819"></a><a name="p896419003819"></a>restart_required</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.82%" headers="mcps1.2.4.1.2 "><p id="p1396417033819"><a name="p1396417033819"></a><a name="p1396417033819"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.67%" headers="mcps1.2.4.1.3 "><p id="p0964100183811"><a name="p0964100183811"></a><a name="p0964100183811"></a>Indicates whether a reboot is required.</p>
    <a name="ul896417073811"></a><a name="ul896417073811"></a><ul id="ul896417073811"><li><strong id="b842352706174226"><a name="b842352706174226"></a><a name="b842352706174226"></a>true</strong>: A reboot is required.</li><li><strong id="b842352706174241"><a name="b842352706174241"></a><a name="b842352706174241"></a>false</strong>: A reboot is not required.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

-   Example normal response

    ```
    {
      "restart_required": false
    }
    ```

-   Abnormal Response

    For details, see  [Abnormal Request Results](abnormal-request-results.md).


## Status Code<a name="section4778540915440"></a>

For details, see  [Status Codes](status-codes.md).

## Error Code<a name="section946032144017"></a>

For details, see  [Error Codes](error-codes.md).

