# Changing DB Instance Volume<a name="en-us_topic_0056890049"></a>

## Function<a name="section39107512101854"></a>

This API is used to change the DB instance volume.

## URI<a name="section55218585101854"></a>

-   URI format

    PATH: /v1.0/\{project\_id\}/instances/\{instanceId\}/action

    Method: POST

-   Parameter description

    **Table  1**  Parameter description

    <a name="table36318895101854"></a>
    <table><thead align="left"><tr id="row51305511101854"><th class="cellrowborder" valign="top" width="21.07%" id="mcps1.2.4.1.1"><p id="p62105732101854"><a name="p62105732101854"></a><a name="p62105732101854"></a><strong id="b84235270691445_1"><a name="b84235270691445_1"></a><a name="b84235270691445_1"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="29.25%" id="mcps1.2.4.1.2"><p id="p64508414101854"><a name="p64508414101854"></a><a name="p64508414101854"></a><strong id="b842352706102346_1"><a name="b842352706102346_1"></a><a name="b842352706102346_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="49.68%" id="mcps1.2.4.1.3"><p id="p57799036101854"><a name="p57799036101854"></a><a name="p57799036101854"></a><strong id="b842352706163417_1"><a name="b842352706163417_1"></a><a name="b842352706163417_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row51210343101854"><td class="cellrowborder" valign="top" width="21.07%" headers="mcps1.2.4.1.1 "><p id="p54397094101854"><a name="p54397094101854"></a><a name="p54397094101854"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.25%" headers="mcps1.2.4.1.2 "><p id="p44088482101854"><a name="p44088482101854"></a><a name="p44088482101854"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.68%" headers="mcps1.2.4.1.3 "><p id="p14397250101854"><a name="p14397250101854"></a><a name="p14397250101854"></a>Specifies the project ID of a tenant in a region.</p>
    </td>
    </tr>
    <tr id="row62466387101854"><td class="cellrowborder" valign="top" width="21.07%" headers="mcps1.2.4.1.1 "><p id="p26612581101854"><a name="p26612581101854"></a><a name="p26612581101854"></a>instanceId</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.25%" headers="mcps1.2.4.1.2 "><p id="p8135439101854"><a name="p8135439101854"></a><a name="p8135439101854"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.68%" headers="mcps1.2.4.1.3 "><p id="p54990842101854"><a name="p54990842101854"></a><a name="p54990842101854"></a>Specifies the DB instance ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Restrictions
    1.  The adjusted volume size must be greater than the original one and the desired volume size must be a multiple of 10.
    2.  The sizes of the primary and standby DB instances are the same. When you scale the primary DB instance, its standby DB instance is also scaled.
    3.  The DB instances can be scaled when they are in the  **Available**  state.
    4.  Currently, only the DB engines MySQL and PostgreSQL are supported by the API.


## Request<a name="section30129545101854"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table44343763101854"></a>
    <table><thead align="left"><tr id="row32217258101854"><th class="cellrowborder" valign="top" width="24.242424242424242%" id="mcps1.2.4.1.1"><p id="p59461092101854"><a name="p59461092101854"></a><a name="p59461092101854"></a><strong id="b84235270691445_5"><a name="b84235270691445_5"></a><a name="b84235270691445_5"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="42.42424242424242%" id="mcps1.2.4.1.2"><p id="p51619167101854"><a name="p51619167101854"></a><a name="p51619167101854"></a><strong id="b842352706164541_1"><a name="b842352706164541_1"></a><a name="b842352706164541_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p20403011101854"><a name="p20403011101854"></a><a name="p20403011101854"></a><strong id="b842352706163417_5"><a name="b842352706163417_5"></a><a name="b842352706163417_5"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row42031158101854"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p49080675101854"><a name="p49080675101854"></a><a name="p49080675101854"></a>resize</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.2 "><p id="p16111728101854"><a name="p16111728101854"></a><a name="p16111728101854"></a>Dictionary data structure. For details, see <a href="#table46186408101854">Table 3</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1398707101854"><a name="p1398707101854"></a><a name="p1398707101854"></a>Specifies the information about the returned parameter <strong id="b842352706113940_1"><a name="b842352706113940_1"></a><a name="b842352706113940_1"></a>volume</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  resize field data structure description

    <a name="table46186408101854"></a>
    <table><thead align="left"><tr id="row5532136101854"><th class="cellrowborder" valign="top" width="23.47%" id="mcps1.2.4.1.1"><p id="p45449848101854"><a name="p45449848101854"></a><a name="p45449848101854"></a><strong id="b84235270691445_7"><a name="b84235270691445_7"></a><a name="b84235270691445_7"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="42.86%" id="mcps1.2.4.1.2"><p id="p57559081101854"><a name="p57559081101854"></a><a name="p57559081101854"></a><strong id="b842352706164541_3"><a name="b842352706164541_3"></a><a name="b842352706164541_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.67%" id="mcps1.2.4.1.3"><p id="p31773986101854"><a name="p31773986101854"></a><a name="p31773986101854"></a><strong id="b842352706163417_7"><a name="b842352706163417_7"></a><a name="b842352706163417_7"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row23556108101854"><td class="cellrowborder" valign="top" width="23.47%" headers="mcps1.2.4.1.1 "><p id="p28996623101854"><a name="p28996623101854"></a><a name="p28996623101854"></a>volume</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.86%" headers="mcps1.2.4.1.2 "><p id="p67025106101854"><a name="p67025106101854"></a><a name="p67025106101854"></a>Dictionary data structure. For details, see <a href="#table20238213101854">Table 4</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.67%" headers="mcps1.2.4.1.3 "><p id="p6049385101854"><a name="p6049385101854"></a><a name="p6049385101854"></a>Specifies the information about the returned parameter <strong id="b842352706113940_3"><a name="b842352706113940_3"></a><a name="b842352706113940_3"></a>size</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  volume field data structure description

    <a name="table20238213101854"></a>
    <table><thead align="left"><tr id="row48003310101854"><th class="cellrowborder" valign="top" width="23.369999999999997%" id="mcps1.2.4.1.1"><p id="p63062868101854"><a name="p63062868101854"></a><a name="p63062868101854"></a><strong id="b84235270691445_9"><a name="b84235270691445_9"></a><a name="b84235270691445_9"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43.3%" id="mcps1.2.4.1.2"><p id="p7818683101854"><a name="p7818683101854"></a><a name="p7818683101854"></a><strong id="b842352706164541_5"><a name="b842352706164541_5"></a><a name="b842352706164541_5"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33%" id="mcps1.2.4.1.3"><p id="p29333578101854"><a name="p29333578101854"></a><a name="p29333578101854"></a><strong id="b842352706163417_9"><a name="b842352706163417_9"></a><a name="b842352706163417_9"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row27209642101854"><td class="cellrowborder" valign="top" width="23.369999999999997%" headers="mcps1.2.4.1.1 "><p id="p56497411101854"><a name="p56497411101854"></a><a name="p56497411101854"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.3%" headers="mcps1.2.4.1.2 "><p id="p12887548101854"><a name="p12887548101854"></a><a name="p12887548101854"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p37258429101854"><a name="p37258429101854"></a><a name="p37258429101854"></a>Specifies the volume size after scaling up. The value must a multiple of 10.</p>
    <p id="p66890408101854"><a name="p66890408101854"></a><a name="p66890408101854"></a>Its value range is from 50 GB to 4000 GB.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Request example

    ```
    {     
    "resize": { 
            "volume": { 
                "size": 400  
            } 
        } 
    }
    ```


## Normal Response<a name="section52450500101854"></a>

None

## Abnormal Response<a name="section60588987101854"></a>

For details, see  [Abnormal Request Results](abnormal-request-results.md).

