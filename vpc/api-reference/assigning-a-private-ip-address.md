# Assigning a Private IP Address<a name="vpc_privateip_0001"></a>

## Function<a name="section31644779"></a>

This API is used to assign a private IP address.

## URI<a name="section16367560"></a>

POST /v1/\{project\_id\}/privateips

[Table 1](#table57906226)  describes the parameters.

**Table  1**  Parameter description

<a name="table57906226"></a>
<table><thead align="left"><tr id="row33939988"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p64784526"><a name="p64784526"></a><a name="p64784526"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p13055244"><a name="p13055244"></a><a name="p13055244"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p50841847"><a name="p50841847"></a><a name="p50841847"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row24548918"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p42305330"><a name="p42305330"></a><a name="p42305330"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p4179666"><a name="p4179666"></a><a name="p4179666"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section13090320"></a>

-   Request parameter

    **Table  2**  Request parameter

    <a name="table6906072155755"></a>
    <table><thead align="left"><tr id="row11778955155755"><th class="cellrowborder" valign="top" width="15.409999999999998%" id="mcps1.2.5.1.1"><p id="p14571261155755"><a name="p14571261155755"></a><a name="p14571261155755"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.86%" id="mcps1.2.5.1.2"><p id="p39421508155755"><a name="p39421508155755"></a><a name="p39421508155755"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.55%" id="mcps1.2.5.1.3"><p id="p39025608155755"><a name="p39025608155755"></a><a name="p39025608155755"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="47.18%" id="mcps1.2.5.1.4"><p id="p6957680155755"><a name="p6957680155755"></a><a name="p6957680155755"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row26701221155755"><td class="cellrowborder" valign="top" width="15.409999999999998%" headers="mcps1.2.5.1.1 "><p id="p15315278155755"><a name="p15315278155755"></a><a name="p15315278155755"></a>privateips</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.2.5.1.2 "><p id="p32578004155755"><a name="p32578004155755"></a><a name="p32578004155755"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.55%" headers="mcps1.2.5.1.3 "><p id="p21572638155755"><a name="p21572638155755"></a><a name="p21572638155755"></a>Array of <a href="#table45335391">privateip</a> objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.18%" headers="mcps1.2.5.1.4 "><p id="p22979132155755"><a name="p22979132155755"></a><a name="p22979132155755"></a>Specifies the private IP address objects. For details, see <a href="#table45335391">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Description of the  **privateip**  field

    <a name="table45335391"></a>
    <table><thead align="left"><tr id="row64244561"><th class="cellrowborder" valign="top" width="16.91830816918308%" id="mcps1.2.5.1.1"><p id="p36426933"><a name="p36426933"></a><a name="p36426933"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.478252174782526%" id="mcps1.2.5.1.2"><p id="p64900454"><a name="p64900454"></a><a name="p64900454"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.04819518048195%" id="mcps1.2.5.1.3"><p id="p2779229717298"><a name="p2779229717298"></a><a name="p2779229717298"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="47.55524447555245%" id="mcps1.2.5.1.4"><p id="p22445387"><a name="p22445387"></a><a name="p22445387"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6137036"><td class="cellrowborder" valign="top" width="16.91830816918308%" headers="mcps1.2.5.1.1 "><p id="p27337939"><a name="p27337939"></a><a name="p27337939"></a>subnet_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.478252174782526%" headers="mcps1.2.5.1.2 "><p id="p66889413"><a name="p66889413"></a><a name="p66889413"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.04819518048195%" headers="mcps1.2.5.1.3 "><p id="p3658359317298"><a name="p3658359317298"></a><a name="p3658359317298"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.55524447555245%" headers="mcps1.2.5.1.4 "><p id="p41347315"><a name="p41347315"></a><a name="p41347315"></a>Specifies the ID of the subnet from which IP addresses are assigned.</p>
    </td>
    </tr>
    <tr id="row36581520"><td class="cellrowborder" valign="top" width="16.91830816918308%" headers="mcps1.2.5.1.1 "><p id="p10313144"><a name="p10313144"></a><a name="p10313144"></a>ip_address</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.478252174782526%" headers="mcps1.2.5.1.2 "><p id="p30058349"><a name="p30058349"></a><a name="p30058349"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.04819518048195%" headers="mcps1.2.5.1.3 "><p id="p1048103717298"><a name="p1048103717298"></a><a name="p1048103717298"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.55524447555245%" headers="mcps1.2.5.1.4 "><a name="ul10782731123015"></a><a name="ul10782731123015"></a><ul id="ul10782731123015"><li>Specifies the target IP address.</li><li>The value can be an available IP address in the subnet. If it is not specified, the system automatically assigns an IP address.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    POST https://{Endpoint}/v1/{project_id}/privateips
    
    {
      "privateips": 
       [ 
        {
            "subnet_id": "531dec0f-3116-411b-a21b-e612e42349fd"
        },
        {
            "subnet_id": "531dec0f-3116-411b-a21b-e612e42349fd",
             "ip_address": "192.168.1.17"
        }
       ]
    }
    ```


## Response Message<a name="section50704018"></a>

-   Response parameter

    **Table  4**  Response parameter

    <a name="table38560739155852"></a>
    <table><thead align="left"><tr id="row1158370155852"><th class="cellrowborder" valign="top" width="18.34%" id="mcps1.2.4.1.1"><p id="p26719126155852"><a name="p26719126155852"></a><a name="p26719126155852"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="25.509999999999998%" id="mcps1.2.4.1.2"><p id="p15835596155852"><a name="p15835596155852"></a><a name="p15835596155852"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.15%" id="mcps1.2.4.1.3"><p id="p7614877155852"><a name="p7614877155852"></a><a name="p7614877155852"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row12825332155852"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.2.4.1.1 "><p id="p32218934155852"><a name="p32218934155852"></a><a name="p32218934155852"></a>privateips</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.4.1.2 "><p id="p26395826172022"><a name="p26395826172022"></a><a name="p26395826172022"></a>Array of <a href="#table34571880">privateip</a> objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.15%" headers="mcps1.2.4.1.3 "><p id="p14320614155852"><a name="p14320614155852"></a><a name="p14320614155852"></a>Specifies the private IP address objects. For details, see <a href="#table34571880">Table 5</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5**  Description of the  **privateip**  field

    <a name="table34571880"></a>
    <table><thead align="left"><tr id="row51070612"><th class="cellrowborder" valign="top" width="22.222222222222225%" id="mcps1.2.4.1.1"><p id="p43078913"><a name="p43078913"></a><a name="p43078913"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="28.132813281328133%" id="mcps1.2.4.1.2"><p id="p42083530172955"><a name="p42083530172955"></a><a name="p42083530172955"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="49.644964496449646%" id="mcps1.2.4.1.3"><p id="p45326617"><a name="p45326617"></a><a name="p45326617"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row47577364"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.4.1.1 "><p id="p28561251"><a name="p28561251"></a><a name="p28561251"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.132813281328133%" headers="mcps1.2.4.1.2 "><p id="p53322749172955"><a name="p53322749172955"></a><a name="p53322749172955"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.644964496449646%" headers="mcps1.2.4.1.3 "><a name="ul13978236183119"></a><a name="ul13978236183119"></a><ul id="ul13978236183119"><li>Specifies the status of the private IP address.</li><li>Possible values are as follows:<a name="ul948092312377"></a><a name="ul948092312377"></a><ul id="ul948092312377"><li><strong id="b113207483149"><a name="b113207483149"></a><a name="b113207483149"></a>ACTIVE</strong></li><li><strong id="b842352706162411"><a name="b842352706162411"></a><a name="b842352706162411"></a>DOWN</strong></li></ul>
    </li></ul>
    </td>
    </tr>
    <tr id="row38031802"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.4.1.1 "><p id="p60677108"><a name="p60677108"></a><a name="p60677108"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.132813281328133%" headers="mcps1.2.4.1.2 "><p id="p24175384172955"><a name="p24175384172955"></a><a name="p24175384172955"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.644964496449646%" headers="mcps1.2.4.1.3 "><p id="p47453675"><a name="p47453675"></a><a name="p47453675"></a>Specifies the ID of the private IP address, which uniquely identifies the private IP address.</p>
    </td>
    </tr>
    <tr id="row24429894"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.4.1.1 "><p id="p32664435"><a name="p32664435"></a><a name="p32664435"></a>subnet_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.132813281328133%" headers="mcps1.2.4.1.2 "><p id="p12049092172955"><a name="p12049092172955"></a><a name="p12049092172955"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.644964496449646%" headers="mcps1.2.4.1.3 "><p id="p26383427"><a name="p26383427"></a><a name="p26383427"></a>Specifies the ID of the subnet from which IP addresses are assigned.</p>
    </td>
    </tr>
    <tr id="row1899134118131"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.4.1.1 "><p id="p6190364318131"><a name="p6190364318131"></a><a name="p6190364318131"></a>tenant_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.132813281328133%" headers="mcps1.2.4.1.2 "><p id="p696029318131"><a name="p696029318131"></a><a name="p696029318131"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.644964496449646%" headers="mcps1.2.4.1.3 "><p id="p1071642181111"><a name="p1071642181111"></a><a name="p1071642181111"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row36124251"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.4.1.1 "><p id="p40383225"><a name="p40383225"></a><a name="p40383225"></a>device_owner</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.132813281328133%" headers="mcps1.2.4.1.2 "><p id="p36452392172955"><a name="p36452392172955"></a><a name="p36452392172955"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.644964496449646%" headers="mcps1.2.4.1.3 "><a name="ul1878734133215"></a><a name="ul1878734133215"></a><ul id="ul1878734133215"><li>Specifies the resource using the private IP address. The parameter is left blank if it is not used.</li><li>The value can be <strong id="b2857432319423"><a name="b2857432319423"></a><a name="b2857432319423"></a>network:dhcp</strong>, <strong id="b145221618319423"><a name="b145221618319423"></a><a name="b145221618319423"></a>network:router_interface_distributed</strong>, <strong id="b8232141419423"><a name="b8232141419423"></a><a name="b8232141419423"></a>compute:xxx</strong>, or <strong id="b842352706191337"><a name="b842352706191337"></a><a name="b842352706191337"></a>neutron:VIP_PORT</strong>. (In value <strong id="b84235270619147"><a name="b84235270619147"></a><a name="b84235270619147"></a>compute:xxx</strong>, <strong id="b168050156819423"><a name="b168050156819423"></a><a name="b168050156819423"></a>xxx</strong> specifies the AZ name, for example, <strong id="b55046298619423"><a name="b55046298619423"></a><a name="b55046298619423"></a>compute:aa-bb-cc</strong> indicates that the private IP address is used by an ECS in the <strong id="b160041186519423"><a name="b160041186519423"></a><a name="b160041186519423"></a>aa-bb-cc</strong> AZ).</li><li>The value range specifies only the type of private IP addresses supported by the current service.</li></ul>
    </td>
    </tr>
    <tr id="row64744584"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.4.1.1 "><p id="p9819961"><a name="p9819961"></a><a name="p9819961"></a>ip_address</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.132813281328133%" headers="mcps1.2.4.1.2 "><p id="p66962669172955"><a name="p66962669172955"></a><a name="p66962669172955"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.644964496449646%" headers="mcps1.2.4.1.3 "><p id="p38322691"><a name="p38322691"></a><a name="p38322691"></a>Specifies the assigned private IP address.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "privateips": [
            {
                "status": "DOWN",
                "id": "c60c2ce1-1e73-44bd-bf48-fd688448ff7b",
                "subnet_id": "531dec0f-3116-411b-a21b-e612e42349fd",
                "tenant_id": "8b7e35ad379141fc9df3e178bd64f55c",
                "device_owner": "",
                "ip_address": "192.168.1.10"
            },
            {
                "status": "DOWN",
                "id": "4b123c18-ae92-4dfa-92cd-d44002359aa1",
                "subnet_id": "531dec0f-3116-411b-a21b-e612e42349fd",
                "tenant_id": "8b7e35ad379141fc9df3e178bd64f55c",
                "device_owner": "",
                "ip_address": "192.168.1.17"
            }
        ]
    }
    ```


## Status Code<a name="section31981619"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

