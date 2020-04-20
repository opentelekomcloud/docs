# Adding Custom Parameters<a name="en-us_topic_0056890265"></a>

## Function<a name="section53089284103627"></a>

This API is used to add parameter information to a parameter template identified by a specified ID.

## URI<a name="section47568069103438"></a>

-   URI format

    PATH: /v1.0/\{project\_id\}/configurations/\{id\}

    Method: PATCH

-   Parameter description

    **Table  1**  Parameter description

    <a name="table37593651103438"></a>
    <table><thead align="left"><tr id="row58913670103438"><th class="cellrowborder" valign="top" width="21.240000000000002%" id="mcps1.2.4.1.1"><p id="p7277976103438"><a name="p7277976103438"></a><a name="p7277976103438"></a><strong id="b84235270691445_1"><a name="b84235270691445_1"></a><a name="b84235270691445_1"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.96%" id="mcps1.2.4.1.2"><p id="p52645207103438"><a name="p52645207103438"></a><a name="p52645207103438"></a><strong id="b842352706102346_1"><a name="b842352706102346_1"></a><a name="b842352706102346_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="49.8%" id="mcps1.2.4.1.3"><p id="p36403370103438"><a name="p36403370103438"></a><a name="p36403370103438"></a><strong id="b842352706163417_1"><a name="b842352706163417_1"></a><a name="b842352706163417_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row62991866103438"><td class="cellrowborder" valign="top" width="21.240000000000002%" headers="mcps1.2.4.1.1 "><p id="p902364145258"><a name="p902364145258"></a><a name="p902364145258"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.96%" headers="mcps1.2.4.1.2 "><p id="p5982632145258"><a name="p5982632145258"></a><a name="p5982632145258"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.8%" headers="mcps1.2.4.1.3 "><p id="p14831209145258"><a name="p14831209145258"></a><a name="p14831209145258"></a>Specifies the project ID of a tenant in a region.</p>
    </td>
    </tr>
    <tr id="row12926085103438"><td class="cellrowborder" valign="top" width="21.240000000000002%" headers="mcps1.2.4.1.1 "><p id="p5797490315835"><a name="p5797490315835"></a><a name="p5797490315835"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.96%" headers="mcps1.2.4.1.2 "><p id="p6155576815835"><a name="p6155576815835"></a><a name="p6155576815835"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.8%" headers="mcps1.2.4.1.3 "><p id="p5878971515835"><a name="p5878971515835"></a><a name="p5878971515835"></a>Specifies the parameter template ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Restrictions
    -   Currently, the DB engines MySQL and PostgreSQL support modifying parameter templates.
    -   The values of the newly added parameters must be within the default value range of the specified database version. For details about the range of parameter values, see section "Modifying Parameters in a Parameter Template" in the  _Relational Database Service User Guide_.
    -   Parameter template modifications will take effect for DB instances to which the parameter template applies. Some modifications take effect only after the DB instance reboots.


## Request<a name="section53891412103438"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table3128215103438"></a>
    <table><thead align="left"><tr id="row903148103438"><th class="cellrowborder" valign="top" width="21.43%" id="mcps1.2.5.1.1"><p id="p6046170103438"><a name="p6046170103438"></a><a name="p6046170103438"></a><strong id="b84235270691445_5"><a name="b84235270691445_5"></a><a name="b84235270691445_5"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="24.82%" id="mcps1.2.5.1.2"><p id="p19977801103438"><a name="p19977801103438"></a><a name="p19977801103438"></a><strong id="b842352706102346_5"><a name="b842352706102346_5"></a><a name="b842352706102346_5"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.62%" id="mcps1.2.5.1.3"><p id="p7589217103438"><a name="p7589217103438"></a><a name="p7589217103438"></a><strong id="b842352706164541_1"><a name="b842352706164541_1"></a><a name="b842352706164541_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="26.13%" id="mcps1.2.5.1.4"><p id="p10746825103438"><a name="p10746825103438"></a><a name="p10746825103438"></a><strong id="b842352706163417_5"><a name="b842352706163417_5"></a><a name="b842352706163417_5"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row65186473103438"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.2.5.1.1 "><p id="p45612970103438"><a name="p45612970103438"></a><a name="p45612970103438"></a>configuration</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.82%" headers="mcps1.2.5.1.2 "><p id="p3663091103438"><a name="p3663091103438"></a><a name="p3663091103438"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.62%" headers="mcps1.2.5.1.3 "><p id="p28274989103438"><a name="p28274989103438"></a><a name="p28274989103438"></a>Dictionary data structure. For details, see <a href="#table23308179103438">Table 3</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.13%" headers="mcps1.2.5.1.4 "><p id="p10046338103438"><a name="p10046338103438"></a><a name="p10046338103438"></a>Specifies the parameter template object.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  configuration field data structure description

    <a name="table23308179103438"></a>
    <table><thead align="left"><tr id="row46775637103438"><th class="cellrowborder" valign="top" width="21.237876212378758%" id="mcps1.2.5.1.1"><p id="p4159209515175"><a name="p4159209515175"></a><a name="p4159209515175"></a><strong id="b84235270691445_7"><a name="b84235270691445_7"></a><a name="b84235270691445_7"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="24.817518248175176%" id="mcps1.2.5.1.2"><p id="p3312230415175"><a name="p3312230415175"></a><a name="p3312230415175"></a><strong id="b842352706102346_7"><a name="b842352706102346_7"></a><a name="b842352706102346_7"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.44725527447255%" id="mcps1.2.5.1.3"><p id="p6683254715175"><a name="p6683254715175"></a><a name="p6683254715175"></a><strong id="b842352706164541_3"><a name="b842352706164541_3"></a><a name="b842352706164541_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="26.497350264973495%" id="mcps1.2.5.1.4"><p id="p541855815175"><a name="p541855815175"></a><a name="p541855815175"></a><strong id="b842352706163417_7"><a name="b842352706163417_7"></a><a name="b842352706163417_7"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row36195986103438"><td class="cellrowborder" valign="top" width="21.237876212378758%" headers="mcps1.2.5.1.1 "><p id="p1291584615175"><a name="p1291584615175"></a><a name="p1291584615175"></a>values</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.817518248175176%" headers="mcps1.2.5.1.2 "><p id="p4230526515175"><a name="p4230526515175"></a><a name="p4230526515175"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.44725527447255%" headers="mcps1.2.5.1.3 "><p id="p5058006715175"><a name="p5058006715175"></a><a name="p5058006715175"></a>Dictionary data structure. For details, see <a href="#table25655849103438">Table 4</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.497350264973495%" headers="mcps1.2.5.1.4 "><p id="p4038861415175"><a name="p4038861415175"></a><a name="p4038861415175"></a>Specifies the parameter values defined by users based on the default parameter template.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  values field data structure description

    <a name="table25655849103438"></a>
    <table><thead align="left"><tr id="row24203070103438"><th class="cellrowborder" valign="top" width="21.62%" id="mcps1.2.5.1.1"><p id="p6440743151716"><a name="p6440743151716"></a><a name="p6440743151716"></a><strong id="b84235270691445_9"><a name="b84235270691445_9"></a><a name="b84235270691445_9"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="24.060000000000002%" id="mcps1.2.5.1.2"><p id="p18370235151716"><a name="p18370235151716"></a><a name="p18370235151716"></a><strong id="b842352706102346_9"><a name="b842352706102346_9"></a><a name="b842352706102346_9"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.060000000000002%" id="mcps1.2.5.1.3"><p id="p18748004151716"><a name="p18748004151716"></a><a name="p18748004151716"></a><strong id="b842352706164541_5"><a name="b842352706164541_5"></a><a name="b842352706164541_5"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.26%" id="mcps1.2.5.1.4"><p id="p10716837151716"><a name="p10716837151716"></a><a name="p10716837151716"></a><strong id="b842352706163417_9"><a name="b842352706163417_9"></a><a name="b842352706163417_9"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row46344255103438"><td class="cellrowborder" valign="top" width="21.62%" headers="mcps1.2.5.1.1 "><p id="p46777534151716"><a name="p46777534151716"></a><a name="p46777534151716"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.060000000000002%" headers="mcps1.2.5.1.2 "><p id="p6662534810289"><a name="p6662534810289"></a><a name="p6662534810289"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.060000000000002%" headers="mcps1.2.5.1.3 "><p id="p18273526151716"><a name="p18273526151716"></a><a name="p18273526151716"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.26%" headers="mcps1.2.5.1.4 "><p id="p45015520202335"><a name="p45015520202335"></a><a name="p45015520202335"></a>Specifies the parameter name. For example, in <strong id="b84235270621563"><a name="b84235270621563"></a><a name="b84235270621563"></a>"max_connections": "10"</strong>, the key is <strong id="b842352706215241"><a name="b842352706215241"></a><a name="b842352706215241"></a>max_connections</strong>.</p>
    </td>
    </tr>
    <tr id="row11109234103438"><td class="cellrowborder" valign="top" width="21.62%" headers="mcps1.2.5.1.1 "><p id="p50431049151716"><a name="p50431049151716"></a><a name="p50431049151716"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.060000000000002%" headers="mcps1.2.5.1.2 "><p id="p5017068210289"><a name="p5017068210289"></a><a name="p5017068210289"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.060000000000002%" headers="mcps1.2.5.1.3 "><p id="p66033168151716"><a name="p66033168151716"></a><a name="p66033168151716"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.26%" headers="mcps1.2.5.1.4 "><p id="p79653202335"><a name="p79653202335"></a><a name="p79653202335"></a>Specifies the parameter value. For example, in <strong id="b953814020215624"><a name="b953814020215624"></a><a name="b953814020215624"></a>"max_connections": "10"</strong>, the value is <strong id="b842352706215633"><a name="b842352706215633"></a><a name="b842352706215633"></a>10</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Request example

    ```
    {
      "configuration": {
        "values": {
           "max_connections": "10",
           "autocommit": "OFF"
        }
      }
    }
    ```


## Normal Response<a name="section15351265103438"></a>

```
{
  "errCode": "RDS.0041",
  "externalMessage": "Operation successful."
}
```

## Abnormal Response<a name="section51001047103438"></a>

For details, see  [Abnormal Request Results](abnormal-request-results.md).

