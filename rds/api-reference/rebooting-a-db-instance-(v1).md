# Rebooting a DB Instance<a name="en-us_topic_0056890051"></a>

## Function<a name="section36524518102048"></a>

This API is used to reboot a DB instance.

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>The RDS DB instance will be unavailable during the reboot process. Exercise caution when performing this operation.  

## URI<a name="section51263775102048"></a>

-   URI format

    PATH: /v1.0/\{project\_id\}/instances/\{instanceId\}/action

    Method: POST

-   Parameter description

    **Table  1**  Parameter description

    <a name="table10271366102048"></a>
    <table><thead align="left"><tr id="row47701174102048"><th class="cellrowborder" valign="top" width="20.97%" id="mcps1.2.4.1.1"><p id="p38589920102048"><a name="p38589920102048"></a><a name="p38589920102048"></a><strong id="b84235270691445"><a name="b84235270691445"></a><a name="b84235270691445"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="29.110000000000003%" id="mcps1.2.4.1.2"><p id="p38775843102048"><a name="p38775843102048"></a><a name="p38775843102048"></a><strong id="b842352706102346"><a name="b842352706102346"></a><a name="b842352706102346"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="49.919999999999995%" id="mcps1.2.4.1.3"><p id="p53835558102048"><a name="p53835558102048"></a><a name="p53835558102048"></a><strong id="b842352706163417"><a name="b842352706163417"></a><a name="b842352706163417"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row65712913102048"><td class="cellrowborder" valign="top" width="20.97%" headers="mcps1.2.4.1.1 "><p id="p21145741102048"><a name="p21145741102048"></a><a name="p21145741102048"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.110000000000003%" headers="mcps1.2.4.1.2 "><p id="p35083457102048"><a name="p35083457102048"></a><a name="p35083457102048"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.919999999999995%" headers="mcps1.2.4.1.3 "><p id="p23187798102048"><a name="p23187798102048"></a><a name="p23187798102048"></a>Specifies the project ID of a tenant in a region.</p>
    </td>
    </tr>
    <tr id="row7363596102048"><td class="cellrowborder" valign="top" width="20.97%" headers="mcps1.2.4.1.1 "><p id="p59580437102048"><a name="p59580437102048"></a><a name="p59580437102048"></a>instanceId</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.110000000000003%" headers="mcps1.2.4.1.2 "><p id="p61286098102048"><a name="p61286098102048"></a><a name="p61286098102048"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.919999999999995%" headers="mcps1.2.4.1.3 "><p id="p65226924102048"><a name="p65226924102048"></a><a name="p65226924102048"></a>Specifies the DB instance ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Restrictions

    The DB instance cannot reboot when it is being created, scaled, backed up, restored, or its instance class is being changed.

    Currently, only the DB engines MySQL and PostgreSQL are supported by the API.


## Request<a name="section49690149102048"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table2211723102048"></a>
    <table><thead align="left"><tr id="row16582139102048"><th class="cellrowborder" valign="top" width="21.242124212421242%" id="mcps1.2.5.1.1"><p id="p976041102048"><a name="p976041102048"></a><a name="p976041102048"></a><strong id="b1940286026"><a name="b1940286026"></a><a name="b1940286026"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.192819281928188%" id="mcps1.2.5.1.2"><p id="p11950471102048"><a name="p11950471102048"></a><a name="p11950471102048"></a><strong id="b2105518919"><a name="b2105518919"></a><a name="b2105518919"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25.562556255625562%" id="mcps1.2.5.1.3"><p id="p28464061102048"><a name="p28464061102048"></a><a name="p28464061102048"></a><strong id="b842352706164541"><a name="b842352706164541"></a><a name="b842352706164541"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25.002500250025%" id="mcps1.2.5.1.4"><p id="p23887604102048"><a name="p23887604102048"></a><a name="p23887604102048"></a><strong id="b1294264075"><a name="b1294264075"></a><a name="b1294264075"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row55847763102048"><td class="cellrowborder" valign="top" width="21.242124212421242%" headers="mcps1.2.5.1.1 "><p id="p27374979102048"><a name="p27374979102048"></a><a name="p27374979102048"></a>restart</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.192819281928188%" headers="mcps1.2.5.1.2 "><p id="p2780844102048"><a name="p2780844102048"></a><a name="p2780844102048"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.562556255625562%" headers="mcps1.2.5.1.3 "><p id="p23921781102048"><a name="p23921781102048"></a><a name="p23921781102048"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.002500250025%" headers="mcps1.2.5.1.4 "><p id="p58616070102048"><a name="p58616070102048"></a><a name="p58616070102048"></a>This parameter is left blank.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Request example

    ```
    {
          "restart": {} 
    }
    ```


## Normal Response<a name="section13572792102048"></a>

None

## Abnormal Response<a name="section64738761102048"></a>

For details, see  [Abnormal Request Results](abnormal-request-results.md).

