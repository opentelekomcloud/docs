# Querying Private IP Address Details<a name="vpc_privateip_0002"></a>

## Function<a name="section9185002"></a>

This API is used to query details about a private IP address using the specified ID.

## URI<a name="section15556157"></a>

GET /v1/\{project\_id\}/privateips/\{privateip\_id\}

[Table 1](#table4378562)  describes the parameters.

**Table  1**  Parameter description

<a name="table4378562"></a>
<table><thead align="left"><tr id="row14851049"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p62084314"><a name="p62084314"></a><a name="p62084314"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p62773503"><a name="p62773503"></a><a name="p62773503"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p51488960"><a name="p51488960"></a><a name="p51488960"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row9856263"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p60159801"><a name="p60159801"></a><a name="p60159801"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p41105728"><a name="p41105728"></a><a name="p41105728"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row35522984"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p58789457"><a name="p58789457"></a><a name="p58789457"></a>privateip_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p64325611"><a name="p64325611"></a><a name="p64325611"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p42992030"><a name="p42992030"></a><a name="p42992030"></a>Specifies the ID of the private IP address, which uniquely identifies the private IP address.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section5787686"></a>

-   Request parameter

    None

-   Example request

    ```
    GET https://{Endpoint}/v1/{project_id}/privateips/d600542a-b231-45ed-af05-e9930cb14f78
    ```


## Response<a name="section52089174"></a>

-   Response parameter

    **Table  2**  Response parameter

    <a name="table66473901155923"></a>
    <table><thead align="left"><tr id="row7115943155923"><th class="cellrowborder" valign="top" width="18.34%" id="mcps1.2.4.1.1"><p id="p39520483155923"><a name="p39520483155923"></a><a name="p39520483155923"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="25.509999999999998%" id="mcps1.2.4.1.2"><p id="p52352674155923"><a name="p52352674155923"></a><a name="p52352674155923"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.15%" id="mcps1.2.4.1.3"><p id="p12708212155923"><a name="p12708212155923"></a><a name="p12708212155923"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row22732275155923"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.2.4.1.1 "><p id="p29374982155923"><a name="p29374982155923"></a><a name="p29374982155923"></a>privateip</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.4.1.2 "><p id="p59712266155923"><a name="p59712266155923"></a><a name="p59712266155923"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.15%" headers="mcps1.2.4.1.3 "><p id="p43698339155923"><a name="p43698339155923"></a><a name="p43698339155923"></a>Specifies the private IP address objects. For details, see <a href="#table23250319">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Description of the  **privateip**  field

    <a name="table23250319"></a>
    <table><thead align="left"><tr id="row21723514"><th class="cellrowborder" valign="top" width="25.28%" id="mcps1.2.4.1.1"><p id="p14774201"><a name="p14774201"></a><a name="p14774201"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.580000000000002%" id="mcps1.2.4.1.2"><p id="p21721490173058"><a name="p21721490173058"></a><a name="p21721490173058"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="54.14%" id="mcps1.2.4.1.3"><p id="p28338386"><a name="p28338386"></a><a name="p28338386"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row13707899"><td class="cellrowborder" valign="top" width="25.28%" headers="mcps1.2.4.1.1 "><p id="p36597996"><a name="p36597996"></a><a name="p36597996"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.580000000000002%" headers="mcps1.2.4.1.2 "><p id="p14610233173058"><a name="p14610233173058"></a><a name="p14610233173058"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.14%" headers="mcps1.2.4.1.3 "><a name="ul13978236183119"></a><a name="ul13978236183119"></a><ul id="ul13978236183119"><li>Specifies the status of the private IP address.</li><li>Possible values are as follows:<a name="ul948092312377"></a><a name="ul948092312377"></a><ul id="ul948092312377"><li><strong id="b38501286192"><a name="b38501286192"></a><a name="b38501286192"></a>ACTIVE</strong></li><li><strong id="b775717296193"><a name="b775717296193"></a><a name="b775717296193"></a>DOWN</strong></li></ul>
    </li></ul>
    </td>
    </tr>
    <tr id="row53064224"><td class="cellrowborder" valign="top" width="25.28%" headers="mcps1.2.4.1.1 "><p id="p3234911"><a name="p3234911"></a><a name="p3234911"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.580000000000002%" headers="mcps1.2.4.1.2 "><p id="p42578245173058"><a name="p42578245173058"></a><a name="p42578245173058"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.14%" headers="mcps1.2.4.1.3 "><p id="p47453675"><a name="p47453675"></a><a name="p47453675"></a>Specifies the ID of the private IP address, which uniquely identifies the private IP address.</p>
    </td>
    </tr>
    <tr id="row36801206"><td class="cellrowborder" valign="top" width="25.28%" headers="mcps1.2.4.1.1 "><p id="p28107703"><a name="p28107703"></a><a name="p28107703"></a>subnet_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.580000000000002%" headers="mcps1.2.4.1.2 "><p id="p26285854173058"><a name="p26285854173058"></a><a name="p26285854173058"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.14%" headers="mcps1.2.4.1.3 "><p id="p26383427"><a name="p26383427"></a><a name="p26383427"></a>Specifies the ID of the subnet from which IP addresses are assigned.</p>
    </td>
    </tr>
    <tr id="row54031349181512"><td class="cellrowborder" valign="top" width="25.28%" headers="mcps1.2.4.1.1 "><p id="p4774073181513"><a name="p4774073181513"></a><a name="p4774073181513"></a>tenant_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.580000000000002%" headers="mcps1.2.4.1.2 "><p id="p49967057181513"><a name="p49967057181513"></a><a name="p49967057181513"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.14%" headers="mcps1.2.4.1.3 "><p id="p167315119118"><a name="p167315119118"></a><a name="p167315119118"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row25113108"><td class="cellrowborder" valign="top" width="25.28%" headers="mcps1.2.4.1.1 "><p id="p20895830"><a name="p20895830"></a><a name="p20895830"></a>device_owner</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.580000000000002%" headers="mcps1.2.4.1.2 "><p id="p48779435173058"><a name="p48779435173058"></a><a name="p48779435173058"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.14%" headers="mcps1.2.4.1.3 "><a name="ul1878734133215"></a><a name="ul1878734133215"></a><ul id="ul1878734133215"><li>Specifies the resource using the private IP address. The parameter is left blank if it is not used.</li><li>The value can be <strong id="b7686105818196"><a name="b7686105818196"></a><a name="b7686105818196"></a>network:dhcp</strong>, <strong id="b3688105813198"><a name="b3688105813198"></a><a name="b3688105813198"></a>network:router_interface_distributed</strong>, <strong id="b1690458161910"><a name="b1690458161910"></a><a name="b1690458161910"></a>compute:xxx</strong>, or <strong id="b76911581197"><a name="b76911581197"></a><a name="b76911581197"></a>neutron:VIP_PORT</strong>. (In value <strong id="b569395881915"><a name="b569395881915"></a><a name="b569395881915"></a>compute:xxx</strong>, <strong id="b1169465811914"><a name="b1169465811914"></a><a name="b1169465811914"></a>xxx</strong> specifies the AZ name, for example, <strong id="b2697758131916"><a name="b2697758131916"></a><a name="b2697758131916"></a>compute:aa-bb-cc</strong> indicates that the private IP address is used by an ECS in the <strong id="b196991258101918"><a name="b196991258101918"></a><a name="b196991258101918"></a>aa-bb-cc</strong> AZ).</li><li>The value range specifies only the type of private IP addresses supported by the current service.</li></ul>
    </td>
    </tr>
    <tr id="row46793790"><td class="cellrowborder" valign="top" width="25.28%" headers="mcps1.2.4.1.1 "><p id="p32200631"><a name="p32200631"></a><a name="p32200631"></a>ip_address</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.580000000000002%" headers="mcps1.2.4.1.2 "><p id="p58820181173058"><a name="p58820181173058"></a><a name="p58820181173058"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.14%" headers="mcps1.2.4.1.3 "><p id="p19644001"><a name="p19644001"></a><a name="p19644001"></a>Specifies the assigned private IP address.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "privateip": 
            {
                "status": "DOWN",
                "id": "d600542a-b231-45ed-af05-e9930cb14f78",
                "subnet_id": "531dec0f-3116-411b-a21b-e612e42349fd",
                "tenant_id": "8b7e35ad379141fc9df3e178bd64f55c",
                "device_owner": "",
                "ip_address": "192.168.1.11"
            }
    }
    ```


## Status Code<a name="section31981619"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

