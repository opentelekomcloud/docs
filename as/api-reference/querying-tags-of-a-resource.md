# Querying Tags of a Resource<a name="EN-US_TOPIC_0066763618"></a>

## Function<a name="section29924782114441"></a>

This interface is used to query tags of a specified resource by project ID and resource ID.

## URI<a name="section4785746114441"></a>

GET /autoscaling-api/v1/\{project\_id\}/\{resource\_type\}/\{resource\_id\}/tags

**Table  1**  Parameter description

<a name="table50145657114441"></a>
<table><thead align="left"><tr id="row58197975114441"><th class="cellrowborder" valign="top" width="19.191919191919194%" id="mcps1.2.5.1.1"><p id="p16415567114441"><a name="p16415567114441"></a><a name="p16415567114441"></a><strong id="b16639103319446"><a name="b16639103319446"></a><a name="b16639103319446"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="19.191919191919194%" id="mcps1.2.5.1.2"><p id="p54592535114441"><a name="p54592535114441"></a><a name="p54592535114441"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.141414141414144%" id="mcps1.2.5.1.3"><p id="p59919191114441"><a name="p59919191114441"></a><a name="p59919191114441"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="47.474747474747474%" id="mcps1.2.5.1.4"><p id="p21616312114441"><a name="p21616312114441"></a><a name="p21616312114441"></a><strong id="b116023414446"><a name="b116023414446"></a><a name="b116023414446"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row6090849114441"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.1 "><p id="p23596795114441"><a name="p23596795114441"></a><a name="p23596795114441"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.2 "><p id="p32292270114441"><a name="p32292270114441"></a><a name="p32292270114441"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.3 "><p id="p65537057114441"><a name="p65537057114441"></a><a name="p65537057114441"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.474747474747474%" headers="mcps1.2.5.1.4 "><p id="p36520930"><a name="p36520930"></a><a name="p36520930"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row62112352114441"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.1 "><p id="p65044652114441"><a name="p65044652114441"></a><a name="p65044652114441"></a>resource_type</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.2 "><p id="p34125427114441"><a name="p34125427114441"></a><a name="p34125427114441"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.3 "><p id="p12696223114441"><a name="p12696223114441"></a><a name="p12696223114441"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.474747474747474%" headers="mcps1.2.5.1.4 "><p id="p8757171112548"><a name="p8757171112548"></a><a name="p8757171112548"></a>Specifies the resource type. The option is as follows:</p>
<p id="p92021825131918"><a name="p92021825131918"></a><a name="p92021825131918"></a><strong id="b109172918416"><a name="b109172918416"></a><a name="b109172918416"></a>scaling_group_tag</strong>: indicates that the resource type is an AS group.</p>
</td>
</tr>
<tr id="row61632861114441"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.1 "><p id="p26205811114441"><a name="p26205811114441"></a><a name="p26205811114441"></a>resource_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.2 "><p id="p42295946114441"><a name="p42295946114441"></a><a name="p42295946114441"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.3 "><p id="p3419593114441"><a name="p3419593114441"></a><a name="p3419593114441"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.474747474747474%" headers="mcps1.2.5.1.4 "><p id="p8551641114441"><a name="p8551641114441"></a><a name="p8551641114441"></a>Specifies the resource ID.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section21594338114441"></a>

-   Request parameters

    None

-   Example request

    This example shows how to query the resource tags of the AS group with ID  **e5d27f5c-dd76-4a61-b4bc-a67c5686719a**.

    ```
    GET https://{Endpoint}/autoscaling-api/v1/{project_id}/scaling_group_tag/e5d27f5c-dd76-4a61-b4bc-a67c5686719a/tags
    ```


## Response Message<a name="section38798307114441"></a>

-   Response parameters

    **Table  2**  Response parameters

    <a name="table11772112114441"></a>
    <table><thead align="left"><tr id="row26751727114441"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.1"><p id="p19406274114441"><a name="p19406274114441"></a><a name="p19406274114441"></a><strong id="b1344643534416"><a name="b1344643534416"></a><a name="b1344643534416"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27%" id="mcps1.2.4.1.2"><p id="p28404370114441"><a name="p28404370114441"></a><a name="p28404370114441"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53%" id="mcps1.2.4.1.3"><p id="p19052614114441"><a name="p19052614114441"></a><a name="p19052614114441"></a><strong id="b82901636154418"><a name="b82901636154418"></a><a name="b82901636154418"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row66866759114441"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p47498364114441"><a name="p47498364114441"></a><a name="p47498364114441"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.2 "><p id="p6339193387"><a name="p6339193387"></a><a name="p6339193387"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.4.1.3 "><p id="p50312100114441"><a name="p50312100114441"></a><a name="p50312100114441"></a>Specifies resource tags. For details, see <a href="#table64069331114716">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="row4141311201216"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p414118114121"><a name="p414118114121"></a><a name="p414118114121"></a>sys_tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.2 "><p id="p791520713534"><a name="p791520713534"></a><a name="p791520713534"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.4.1.3 "><p id="p1514111131210"><a name="p1514111131210"></a><a name="p1514111131210"></a>Specifies system resource tags. For details, see <a href="#table64069331114716">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **ResourceTag**  field description

    <a name="table64069331114716"></a>
    <table><thead align="left"><tr id="row5644334114716"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.1"><p id="p54537872114716"><a name="p54537872114716"></a><a name="p54537872114716"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="26%" id="mcps1.2.4.1.2"><p id="p65628731114716"><a name="p65628731114716"></a><a name="p65628731114716"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="54%" id="mcps1.2.4.1.3"><p id="p14326995114716"><a name="p14326995114716"></a><a name="p14326995114716"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row19635960114716"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p1282573185716"><a name="p1282573185716"></a><a name="p1282573185716"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="p982511316573"><a name="p982511316573"></a><a name="p982511316573"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="p168251231185711"><a name="p168251231185711"></a><a name="p168251231185711"></a>Specifies the resource tag key.</p>
    </td>
    </tr>
    <tr id="row33928679114716"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p1882573110576"><a name="p1882573110576"></a><a name="p1882573110576"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="p482583120570"><a name="p482583120570"></a><a name="p482583120570"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="p1882573111573"><a name="p1882573111573"></a><a name="p1882573111573"></a>Specifies the resource tag value.</p>
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
                "value": "ENV15"
            },
            {
                "key": "ENV151",
                "value": "ENV151"
            },
            {
                "key": "ENV152",
                "value": "ENV152"
            }
        ],
        "sys_tags": null 
    } 
    ```


## Returned Values<a name="section18464239114441"></a>

-   Normal

    200

-   Abnormal

    <a name="table63160750114441"></a>
    <table><thead align="left"><tr id="row4049738114441"><th class="cellrowborder" valign="top" width="43.69%" id="mcps1.1.3.1.1"><p id="p59593393114441"><a name="p59593393114441"></a><a name="p59593393114441"></a><strong id="b842352706175024"><a name="b842352706175024"></a><a name="b842352706175024"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="56.31%" id="mcps1.1.3.1.2"><p id="p62335491114441"><a name="p62335491114441"></a><a name="p62335491114441"></a><strong id="b84235270616929"><a name="b84235270616929"></a><a name="b84235270616929"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row16010026114441"><td class="cellrowborder" valign="top" width="43.69%" headers="mcps1.1.3.1.1 "><p id="p21743758114441"><a name="p21743758114441"></a><a name="p21743758114441"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.31%" headers="mcps1.1.3.1.2 "><p id="p16413974114441"><a name="p16413974114441"></a><a name="p16413974114441"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row13508043114441"><td class="cellrowborder" valign="top" width="43.69%" headers="mcps1.1.3.1.1 "><p id="p20409733114441"><a name="p20409733114441"></a><a name="p20409733114441"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.31%" headers="mcps1.1.3.1.2 "><p id="p42575704114441"><a name="p42575704114441"></a><a name="p42575704114441"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row47637018114441"><td class="cellrowborder" valign="top" width="43.69%" headers="mcps1.1.3.1.1 "><p id="p33393220114441"><a name="p33393220114441"></a><a name="p33393220114441"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.31%" headers="mcps1.1.3.1.2 "><p id="p20496282114441"><a name="p20496282114441"></a><a name="p20496282114441"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row50248818114441"><td class="cellrowborder" valign="top" width="43.69%" headers="mcps1.1.3.1.1 "><p id="p43622454114441"><a name="p43622454114441"></a><a name="p43622454114441"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.31%" headers="mcps1.1.3.1.2 "><p id="p43757915114441"><a name="p43757915114441"></a><a name="p43757915114441"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row58276921114441"><td class="cellrowborder" valign="top" width="43.69%" headers="mcps1.1.3.1.1 "><p id="p22810194114441"><a name="p22810194114441"></a><a name="p22810194114441"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.31%" headers="mcps1.1.3.1.2 "><p id="p35686431114441"><a name="p35686431114441"></a><a name="p35686431114441"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row52742429114441"><td class="cellrowborder" valign="top" width="43.69%" headers="mcps1.1.3.1.1 "><p id="p44278356114441"><a name="p44278356114441"></a><a name="p44278356114441"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.31%" headers="mcps1.1.3.1.2 "><p id="p29777075114441"><a name="p29777075114441"></a><a name="p29777075114441"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row66667090114441"><td class="cellrowborder" valign="top" width="43.69%" headers="mcps1.1.3.1.1 "><p id="p31325185114441"><a name="p31325185114441"></a><a name="p31325185114441"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.31%" headers="mcps1.1.3.1.2 "><p id="p54312045114441"><a name="p54312045114441"></a><a name="p54312045114441"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row19046357114441"><td class="cellrowborder" valign="top" width="43.69%" headers="mcps1.1.3.1.1 "><p id="p66359910114441"><a name="p66359910114441"></a><a name="p66359910114441"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.31%" headers="mcps1.1.3.1.2 "><p id="p6443624114441"><a name="p6443624114441"></a><a name="p6443624114441"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row57992618114441"><td class="cellrowborder" valign="top" width="43.69%" headers="mcps1.1.3.1.1 "><p id="p66890520114441"><a name="p66890520114441"></a><a name="p66890520114441"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.31%" headers="mcps1.1.3.1.2 "><p id="p49423050114441"><a name="p49423050114441"></a><a name="p49423050114441"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row42154273114441"><td class="cellrowborder" valign="top" width="43.69%" headers="mcps1.1.3.1.1 "><p id="p59052916114441"><a name="p59052916114441"></a><a name="p59052916114441"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.31%" headers="mcps1.1.3.1.2 "><p id="p18556929114441"><a name="p18556929114441"></a><a name="p18556929114441"></a>Failed to complete the request because an internal service error occurred.</p>
    </td>
    </tr>
    <tr id="row32794636114441"><td class="cellrowborder" valign="top" width="43.69%" headers="mcps1.1.3.1.1 "><p id="p39119840114441"><a name="p39119840114441"></a><a name="p39119840114441"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.31%" headers="mcps1.1.3.1.2 "><p id="p14590465114441"><a name="p14590465114441"></a><a name="p14590465114441"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row64205321114441"><td class="cellrowborder" valign="top" width="43.69%" headers="mcps1.1.3.1.1 "><p id="p33248519114441"><a name="p33248519114441"></a><a name="p33248519114441"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.31%" headers="mcps1.1.3.1.2 "><p id="p8775558114441"><a name="p8775558114441"></a><a name="p8775558114441"></a>Failed to complete the request because the server has received an invalid response.</p>
    </td>
    </tr>
    <tr id="row11871166114441"><td class="cellrowborder" valign="top" width="43.69%" headers="mcps1.1.3.1.1 "><p id="p22040352114441"><a name="p22040352114441"></a><a name="p22040352114441"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.31%" headers="mcps1.1.3.1.2 "><p id="p40438103114441"><a name="p40438103114441"></a><a name="p40438103114441"></a>Failed to complete the request because the system is currently unavailable.</p>
    </td>
    </tr>
    <tr id="row28398614114441"><td class="cellrowborder" valign="top" width="43.69%" headers="mcps1.1.3.1.1 "><p id="p18586407114441"><a name="p18586407114441"></a><a name="p18586407114441"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.31%" headers="mcps1.1.3.1.2 "><p id="p29104000114441"><a name="p29104000114441"></a><a name="p29104000114441"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section17669131616110"></a>

See  [Error Codes](error-codes.md).

