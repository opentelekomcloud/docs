# Binding or Unbinding an EIP<a name="rds_09_0001"></a>

## Function<a name="section36524518102048"></a>

This API is used to bind or unbind an EIP.

## URI<a name="section51263775102048"></a>

-   URI format

    PATH: /rds/v1/\{project\_id\}/instances/\{instanceId\}/action

    Method: POST

-   Parameter description

    **Table  1**  Parameter description

    <a name="table10271366102048"></a>
    <table><thead align="left"><tr id="row47701174102048"><th class="cellrowborder" valign="top" width="20.97%" id="mcps1.2.4.1.1"><p id="p38589920102048"><a name="p38589920102048"></a><a name="p38589920102048"></a><strong id="b84235270691445_1"><a name="b84235270691445_1"></a><a name="b84235270691445_1"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="29.110000000000003%" id="mcps1.2.4.1.2"><p id="p38775843102048"><a name="p38775843102048"></a><a name="p38775843102048"></a><strong id="b842352706102346_1"><a name="b842352706102346_1"></a><a name="b842352706102346_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="49.919999999999995%" id="mcps1.2.4.1.3"><p id="p53835558102048"><a name="p53835558102048"></a><a name="p53835558102048"></a><strong id="b842352706163417_1"><a name="b842352706163417_1"></a><a name="b842352706163417_1"></a>Description</strong></p>
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
    <tr id="row7363596102048"><td class="cellrowborder" valign="top" width="20.97%" headers="mcps1.2.4.1.1 "><p id="p751522153814"><a name="p751522153814"></a><a name="p751522153814"></a>instanceId</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.110000000000003%" headers="mcps1.2.4.1.2 "><p id="p61286098102048"><a name="p61286098102048"></a><a name="p61286098102048"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.919999999999995%" headers="mcps1.2.4.1.3 "><p id="p7417132564016"><a name="p7417132564016"></a><a name="p7417132564016"></a>Specifies the primary node ID of the DB instance.</p>
    <div class="note" id="note18250133224019"><a name="note18250133224019"></a><a name="note18250133224019"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p142501332164011"><a name="p142501332164011"></a><a name="p142501332164011"></a>This field is not the DB instance ID. You are advised to use API v3 and the DB instance ID to perform related operations.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>


-   Restrictions

    First, invoke the VPC API to query EIPs by referring to section "Querying Elastic IP Addresses" in the  _Virtual Private Cloud API Reference_. If no EIP is available for the tenant, invoke the VPC API to create an EIP by referring to section "Applying for an Elastic IP Address" in the  _Virtual Private Cloud API Reference_.

    EIPs cannot be bound to or unbound from primary/standby DB instances of earlier versions.


## Request<a name="section49690149102048"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table2211723102048"></a>
    <table><thead align="left"><tr id="row16582139102048"><th class="cellrowborder" valign="top" width="21.242124212421242%" id="mcps1.2.5.1.1"><p id="p976041102048"><a name="p976041102048"></a><a name="p976041102048"></a><strong id="b84235270691445_5"><a name="b84235270691445_5"></a><a name="b84235270691445_5"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.192819281928188%" id="mcps1.2.5.1.2"><p id="p11950471102048"><a name="p11950471102048"></a><a name="p11950471102048"></a><strong id="b842352706102346_5"><a name="b842352706102346_5"></a><a name="b842352706102346_5"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25.562556255625562%" id="mcps1.2.5.1.3"><p id="p28464061102048"><a name="p28464061102048"></a><a name="p28464061102048"></a><strong id="b842352706164541_1"><a name="b842352706164541_1"></a><a name="b842352706164541_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25.002500250025%" id="mcps1.2.5.1.4"><p id="p23887604102048"><a name="p23887604102048"></a><a name="p23887604102048"></a><strong id="b842352706163417_5"><a name="b842352706163417_5"></a><a name="b842352706163417_5"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row55847763102048"><td class="cellrowborder" valign="top" width="21.242124212421242%" headers="mcps1.2.5.1.1 "><p id="p27374979102048"><a name="p27374979102048"></a><a name="p27374979102048"></a>setPublicIp</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.192819281928188%" headers="mcps1.2.5.1.2 "><p id="p2780844102048"><a name="p2780844102048"></a><a name="p2780844102048"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.562556255625562%" headers="mcps1.2.5.1.3 "><p id="p23921781102048"><a name="p23921781102048"></a><a name="p23921781102048"></a>Dictionary data structure. For details, see <a href="#table16417881161621">Table 3</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.002500250025%" headers="mcps1.2.5.1.4 "><p id="p58616070102048"><a name="p58616070102048"></a><a name="p58616070102048"></a>Returns EIP information.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  setPublicIp field data structure description

    <a name="table16417881161621"></a>
    <table><thead align="left"><tr id="row16337907161621"><th class="cellrowborder" valign="top" width="20.419999999999998%" id="mcps1.2.5.1.1"><p id="p42405005161621"><a name="p42405005161621"></a><a name="p42405005161621"></a><strong id="b84235270691445_7"><a name="b84235270691445_7"></a><a name="b84235270691445_7"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.810000000000002%" id="mcps1.2.5.1.2"><p id="p10953378161621"><a name="p10953378161621"></a><a name="p10953378161621"></a><strong id="b842352706102346_7"><a name="b842352706102346_7"></a><a name="b842352706102346_7"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="26.13%" id="mcps1.2.5.1.3"><p id="p34762175162215"><a name="p34762175162215"></a><a name="p34762175162215"></a><strong id="b842352706164541_3"><a name="b842352706164541_3"></a><a name="b842352706164541_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="24.64%" id="mcps1.2.5.1.4"><p id="p45164760161621"><a name="p45164760161621"></a><a name="p45164760161621"></a><strong id="b842352706163417_7"><a name="b842352706163417_7"></a><a name="b842352706163417_7"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row56422788161621"><td class="cellrowborder" valign="top" width="20.419999999999998%" headers="mcps1.2.5.1.1 "><p id="p52148269161621"><a name="p52148269161621"></a><a name="p52148269161621"></a>action</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.810000000000002%" headers="mcps1.2.5.1.2 "><p id="p58818313161621"><a name="p58818313161621"></a><a name="p58818313161621"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.13%" headers="mcps1.2.5.1.3 "><p id="p10340856162215"><a name="p10340856162215"></a><a name="p10340856162215"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.64%" headers="mcps1.2.5.1.4 "><p id="p37698381163714"><a name="p37698381163714"></a><a name="p37698381163714"></a>If this parameter is <span class="parmvalue" id="parmvalue1792293094213356"><a name="parmvalue1792293094213356"></a><a name="parmvalue1792293094213356"></a><b>enablePublicAccess</b></span>, the EIP is bound to the target DB instance.</p>
    <p id="p3023621616172"><a name="p3023621616172"></a><a name="p3023621616172"></a>If this parameter is <span class="parmvalue" id="parmvalue23207739010939"><a name="parmvalue23207739010939"></a><a name="parmvalue23207739010939"></a><b>disablePublicAccess</b></span>, the EIP is unbound from the target DB instance.</p>
    </td>
    </tr>
    <tr id="row45499856161621"><td class="cellrowborder" valign="top" width="20.419999999999998%" headers="mcps1.2.5.1.1 "><p id="p1877671161621"><a name="p1877671161621"></a><a name="p1877671161621"></a>publicIP</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.810000000000002%" headers="mcps1.2.5.1.2 "><p id="p66741607161621"><a name="p66741607161621"></a><a name="p66741607161621"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.13%" headers="mcps1.2.5.1.3 "><p id="p49060751162215"><a name="p49060751162215"></a><a name="p49060751162215"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.64%" headers="mcps1.2.5.1.4 "><p id="p26919856162049"><a name="p26919856162049"></a><a name="p26919856162049"></a>Specifies the EIP obtained by invoking the VPC API. This parameter is not contained in the request when unbinding the EIP.</p>
    </td>
    </tr>
    <tr id="row8184527161621"><td class="cellrowborder" valign="top" width="20.419999999999998%" headers="mcps1.2.5.1.1 "><p id="p55239882161621"><a name="p55239882161621"></a><a name="p55239882161621"></a>publicIPId</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.810000000000002%" headers="mcps1.2.5.1.2 "><p id="p21739441161621"><a name="p21739441161621"></a><a name="p21739441161621"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.13%" headers="mcps1.2.5.1.3 "><p id="p64203138162215"><a name="p64203138162215"></a><a name="p64203138162215"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.64%" headers="mcps1.2.5.1.4 "><p id="p52500795161621"><a name="p52500795161621"></a><a name="p52500795161621"></a>Specifies the EIP ID obtained by invoking the VPC API. This parameter is not contained in the request when unbinding the EIP.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Request example

    Binding an EIP:

    ```
    {
        "setPublicIp":{
            "action":"enablePublicAccess",
            "publicIP":"10.145.49.92",
            "publicIPId":"4c9c30f5-54fb-4e44-8c6e-df4ea8790e93"
        }
    }
    ```

    Unbinding an EIP:

    ```
    {
        "setPublicIp":{
            "action":"disablePublicAccess"
        }
    }
    ```


## Normal Response<a name="section13572792102048"></a>

```
{}
```

## Abnormal Response<a name="section64738761102048"></a>

For details, see  [Abnormal Request Results](abnormal-request-results.md).

