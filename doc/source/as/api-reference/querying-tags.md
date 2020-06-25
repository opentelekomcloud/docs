# Querying Tags<a name="EN-US_TOPIC_0066763617"></a>

## Function<a name="section35616396114129"></a>

This interface is used to query tags by project ID.

## URI<a name="section60331580114129"></a>

GET /autoscaling-api/v1/\{project\_id\}/\{resource\_type\}/tags

**Table  1**  Parameter description

<a name="table6195496114129"></a>
<table><thead align="left"><tr id="row9584089114129"><th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.1"><p id="p38113769114129"><a name="p38113769114129"></a><a name="p38113769114129"></a><strong id="b463111614417"><a name="b463111614417"></a><a name="b463111614417"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.2"><p id="p207602114129"><a name="p207602114129"></a><a name="p207602114129"></a><strong id="b842352706141528"><a name="b842352706141528"></a><a name="b842352706141528"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p16815771114129"><a name="p16815771114129"></a><a name="p16815771114129"></a><strong id="b84235270693914"><a name="b84235270693914"></a><a name="b84235270693914"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="47%" id="mcps1.2.5.1.4"><p id="p19900172114129"><a name="p19900172114129"></a><a name="p19900172114129"></a><strong id="b7997138164415"><a name="b7997138164415"></a><a name="b7997138164415"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1301230114129"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.1 "><p id="p09771712145519"><a name="p09771712145519"></a><a name="p09771712145519"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p159771212125512"><a name="p159771212125512"></a><a name="p159771212125512"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p297761225514"><a name="p297761225514"></a><a name="p297761225514"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.4 "><p id="p36520930"><a name="p36520930"></a><a name="p36520930"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row28017490114129"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.1 "><p id="p297711225519"><a name="p297711225519"></a><a name="p297711225519"></a>resource_type</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p1797713126559"><a name="p1797713126559"></a><a name="p1797713126559"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p10977712195517"><a name="p10977712195517"></a><a name="p10977712195517"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.4 "><p id="p79351742201718"><a name="p79351742201718"></a><a name="p79351742201718"></a>Specifies the resource type. The option is as follows:</p>
<p id="p197701245516"><a name="p197701245516"></a><a name="p197701245516"></a><strong id="b84235270620951"><a name="b84235270620951"></a><a name="b84235270620951"></a>scaling_group_tag</strong>: indicates that the resource type is an AS group.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section45408733114129"></a>

-   Request parameters

    None

-   Example request

    This example shows how to query resource tags of an AS group.

    ```
    GET https://{Endpoint}/autoscaling-api/v1/{project_id}/scaling_group_tag/tags
    ```


## Response Message<a name="section18297044114129"></a>

-   Response parameters

    **Table  2**  Response parameters

    <a name="table56258812114129"></a>
    <table><thead align="left"><tr id="row32761424114129"><th class="cellrowborder" valign="top" width="24.07%" id="mcps1.2.4.1.1"><p id="p36429715114129"><a name="p36429715114129"></a><a name="p36429715114129"></a><strong id="b810581220440"><a name="b810581220440"></a><a name="b810581220440"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.38%" id="mcps1.2.4.1.2"><p id="p65125782114129"><a name="p65125782114129"></a><a name="p65125782114129"></a><strong id="b2139755460"><a name="b2139755460"></a><a name="b2139755460"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="54.55%" id="mcps1.2.4.1.3"><p id="p40696961114129"><a name="p40696961114129"></a><a name="p40696961114129"></a><strong id="b4642813114413"><a name="b4642813114413"></a><a name="b4642813114413"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8119549114129"><td class="cellrowborder" valign="top" width="24.07%" headers="mcps1.2.4.1.1 "><p id="p53703729114129"><a name="p53703729114129"></a><a name="p53703729114129"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.38%" headers="mcps1.2.4.1.2 "><p id="p6339193387"><a name="p6339193387"></a><a name="p6339193387"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.55%" headers="mcps1.2.4.1.3 "><p id="p28635620114129"><a name="p28635620114129"></a><a name="p28635620114129"></a>Specifies the resource tag.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **Tag**  field description

    <a name="table40593624114129"></a>
    <table><thead align="left"><tr id="row32533742114129"><th class="cellrowborder" valign="top" width="24.07%" id="mcps1.2.4.1.1"><p id="p17987463114129"><a name="p17987463114129"></a><a name="p17987463114129"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.38%" id="mcps1.2.4.1.2"><p id="p47698368114129"><a name="p47698368114129"></a><a name="p47698368114129"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="54.55%" id="mcps1.2.4.1.3"><p id="p38362561114129"><a name="p38362561114129"></a><a name="p38362561114129"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row20359731114129"><td class="cellrowborder" valign="top" width="24.07%" headers="mcps1.2.4.1.1 "><p id="p123961037115511"><a name="p123961037115511"></a><a name="p123961037115511"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.38%" headers="mcps1.2.4.1.2 "><p id="p123961371557"><a name="p123961371557"></a><a name="p123961371557"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.55%" headers="mcps1.2.4.1.3 "><p id="p173961537205510"><a name="p173961537205510"></a><a name="p173961537205510"></a>Specifies the resource tag key.</p>
    </td>
    </tr>
    <tr id="row36080156114129"><td class="cellrowborder" valign="top" width="24.07%" headers="mcps1.2.4.1.1 "><p id="p1396103711552"><a name="p1396103711552"></a><a name="p1396103711552"></a>values</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.38%" headers="mcps1.2.4.1.2 "><p id="p1233617371524"><a name="p1233617371524"></a><a name="p1233617371524"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.55%" headers="mcps1.2.4.1.3 "><p id="p1339619370557"><a name="p1339619370557"></a><a name="p1339619370557"></a>Specifies the resource tag values.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
     {
        "tags": [
            {
                "key": "ENV15",
                "values": [
                    "ENV15"
                ]
            },
            {
                "key": "111",
                "values": [
                    ""
                ]
            },
            {
                "key": "environment",
                "values": [
                    "DEV"
                ]
            },
            {
                "key": "ENV151",
                "values": [
                    "ENV151"
                ]
            },
            {
                "key": "ENV152",
                "values": [
                    "ENV152"
                ]
            }
         ]
     }
    ```


## Returned Values<a name="section16422356114129"></a>

-   Normal

    200

-   Abnormal

    <a name="table5682301114129"></a>
    <table><thead align="left"><tr id="row57025015114129"><th class="cellrowborder" valign="top" width="44.440000000000005%" id="mcps1.1.3.1.1"><p id="p55623469114129"><a name="p55623469114129"></a><a name="p55623469114129"></a><strong id="b842352706175024"><a name="b842352706175024"></a><a name="b842352706175024"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="55.559999999999995%" id="mcps1.1.3.1.2"><p id="p9207140114129"><a name="p9207140114129"></a><a name="p9207140114129"></a><strong id="b84235270616929"><a name="b84235270616929"></a><a name="b84235270616929"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row7580867114129"><td class="cellrowborder" valign="top" width="44.440000000000005%" headers="mcps1.1.3.1.1 "><p id="p10070515114129"><a name="p10070515114129"></a><a name="p10070515114129"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.559999999999995%" headers="mcps1.1.3.1.2 "><p id="p10405404114129"><a name="p10405404114129"></a><a name="p10405404114129"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row26539773114129"><td class="cellrowborder" valign="top" width="44.440000000000005%" headers="mcps1.1.3.1.1 "><p id="p2237965114129"><a name="p2237965114129"></a><a name="p2237965114129"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.559999999999995%" headers="mcps1.1.3.1.2 "><p id="p47057449114129"><a name="p47057449114129"></a><a name="p47057449114129"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row20863864114129"><td class="cellrowborder" valign="top" width="44.440000000000005%" headers="mcps1.1.3.1.1 "><p id="p12251410114129"><a name="p12251410114129"></a><a name="p12251410114129"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.559999999999995%" headers="mcps1.1.3.1.2 "><p id="p52840173114129"><a name="p52840173114129"></a><a name="p52840173114129"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row5799514114129"><td class="cellrowborder" valign="top" width="44.440000000000005%" headers="mcps1.1.3.1.1 "><p id="p67107513114129"><a name="p67107513114129"></a><a name="p67107513114129"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.559999999999995%" headers="mcps1.1.3.1.2 "><p id="p66999468114129"><a name="p66999468114129"></a><a name="p66999468114129"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row66124305114129"><td class="cellrowborder" valign="top" width="44.440000000000005%" headers="mcps1.1.3.1.1 "><p id="p54468478114129"><a name="p54468478114129"></a><a name="p54468478114129"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.559999999999995%" headers="mcps1.1.3.1.2 "><p id="p49870579114129"><a name="p49870579114129"></a><a name="p49870579114129"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row46182033114129"><td class="cellrowborder" valign="top" width="44.440000000000005%" headers="mcps1.1.3.1.1 "><p id="p49757158114129"><a name="p49757158114129"></a><a name="p49757158114129"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.559999999999995%" headers="mcps1.1.3.1.2 "><p id="p3797975114129"><a name="p3797975114129"></a><a name="p3797975114129"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row34181782114129"><td class="cellrowborder" valign="top" width="44.440000000000005%" headers="mcps1.1.3.1.1 "><p id="p17260990114129"><a name="p17260990114129"></a><a name="p17260990114129"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.559999999999995%" headers="mcps1.1.3.1.2 "><p id="p55962934114129"><a name="p55962934114129"></a><a name="p55962934114129"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row33904359114129"><td class="cellrowborder" valign="top" width="44.440000000000005%" headers="mcps1.1.3.1.1 "><p id="p61898587114129"><a name="p61898587114129"></a><a name="p61898587114129"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.559999999999995%" headers="mcps1.1.3.1.2 "><p id="p47729651114129"><a name="p47729651114129"></a><a name="p47729651114129"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row26913680114129"><td class="cellrowborder" valign="top" width="44.440000000000005%" headers="mcps1.1.3.1.1 "><p id="p32524506114129"><a name="p32524506114129"></a><a name="p32524506114129"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.559999999999995%" headers="mcps1.1.3.1.2 "><p id="p17239357114129"><a name="p17239357114129"></a><a name="p17239357114129"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row20936487114129"><td class="cellrowborder" valign="top" width="44.440000000000005%" headers="mcps1.1.3.1.1 "><p id="p18133857114129"><a name="p18133857114129"></a><a name="p18133857114129"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.559999999999995%" headers="mcps1.1.3.1.2 "><p id="p59556295114129"><a name="p59556295114129"></a><a name="p59556295114129"></a>Failed to complete the request because an internal service error occurred.</p>
    </td>
    </tr>
    <tr id="row66244615114129"><td class="cellrowborder" valign="top" width="44.440000000000005%" headers="mcps1.1.3.1.1 "><p id="p64213595114129"><a name="p64213595114129"></a><a name="p64213595114129"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.559999999999995%" headers="mcps1.1.3.1.2 "><p id="p33918736114129"><a name="p33918736114129"></a><a name="p33918736114129"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row36833174114129"><td class="cellrowborder" valign="top" width="44.440000000000005%" headers="mcps1.1.3.1.1 "><p id="p30697151114129"><a name="p30697151114129"></a><a name="p30697151114129"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.559999999999995%" headers="mcps1.1.3.1.2 "><p id="p3441308114129"><a name="p3441308114129"></a><a name="p3441308114129"></a>Failed to complete the request because the server has received an invalid response.</p>
    </td>
    </tr>
    <tr id="row30971778114129"><td class="cellrowborder" valign="top" width="44.440000000000005%" headers="mcps1.1.3.1.1 "><p id="p25686089114129"><a name="p25686089114129"></a><a name="p25686089114129"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.559999999999995%" headers="mcps1.1.3.1.2 "><p id="p198456114129"><a name="p198456114129"></a><a name="p198456114129"></a>Failed to complete the request because the system is currently unavailable.</p>
    </td>
    </tr>
    <tr id="row1786111114129"><td class="cellrowborder" valign="top" width="44.440000000000005%" headers="mcps1.1.3.1.1 "><p id="p10457278114129"><a name="p10457278114129"></a><a name="p10457278114129"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.559999999999995%" headers="mcps1.1.3.1.2 "><p id="p41733178114129"><a name="p41733178114129"></a><a name="p41733178114129"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section17669131616110"></a>

See  [Error Codes](error-codes.md).

