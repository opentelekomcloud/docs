# Creating or Deleting a Tag<a name="EN-US_TOPIC_0066763619"></a>

## Function<a name="section54294980114716"></a>

This interface is used to create or delete a resource tag.

Each AS group can have a maximum of 10 tags added to it.

## URI<a name="section53919650114716"></a>

POST /autoscaling-api/v1/\{project\_id\}/\{resource\_type\}/\{resource\_id\}/tags/action

**Table  1**  Parameter description

<a name="table30823845114716"></a>
<table><thead align="left"><tr id="row45946273114716"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.5.1.1"><p id="p30660627114716"><a name="p30660627114716"></a><a name="p30660627114716"></a><strong id="b174891716459"><a name="b174891716459"></a><a name="b174891716459"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="p482845114716"><a name="p482845114716"></a><a name="p482845114716"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p39110504114716"><a name="p39110504114716"></a><a name="p39110504114716"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="48%" id="mcps1.2.5.1.4"><p id="p13834268114716"><a name="p13834268114716"></a><a name="p13834268114716"></a><strong id="b157324455"><a name="b157324455"></a><a name="b157324455"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row46833887114716"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.1 "><p id="p35448540114716"><a name="p35448540114716"></a><a name="p35448540114716"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p52759481114716"><a name="p52759481114716"></a><a name="p52759481114716"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p45659550114716"><a name="p45659550114716"></a><a name="p45659550114716"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.5.1.4 "><p id="p36520930"><a name="p36520930"></a><a name="p36520930"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row66924761114716"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.1 "><p id="p52196538114716"><a name="p52196538114716"></a><a name="p52196538114716"></a>resource_type</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p61217114716"><a name="p61217114716"></a><a name="p61217114716"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p4958579114716"><a name="p4958579114716"></a><a name="p4958579114716"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.5.1.4 "><p id="p75841038195410"><a name="p75841038195410"></a><a name="p75841038195410"></a>Specifies the resource type. The option is as follows:</p>
<p id="p1338315305567"><a name="p1338315305567"></a><a name="p1338315305567"></a><strong id="b84235270620951"><a name="b84235270620951"></a><a name="b84235270620951"></a>scaling_group_tag</strong>: indicates that the resource type is an AS group.</p>
</td>
</tr>
<tr id="row58034801114716"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.1 "><p id="p3198450114716"><a name="p3198450114716"></a><a name="p3198450114716"></a>resource_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p57747899114716"><a name="p57747899114716"></a><a name="p57747899114716"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p47068277114716"><a name="p47068277114716"></a><a name="p47068277114716"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.5.1.4 "><p id="p54434120114716"><a name="p54434120114716"></a><a name="p54434120114716"></a>Resource ID</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section47087579114716"></a>

-   Request parameters

    **Table  2**  Request parameters

    <a name="table39505762114716"></a>
    <table><thead align="left"><tr id="row32657858114716"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.1"><p id="p28040847114716"><a name="p28040847114716"></a><a name="p28040847114716"></a><strong id="b12141532455"><a name="b12141532455"></a><a name="b12141532455"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.2"><p id="p56716153114716"><a name="p56716153114716"></a><a name="p56716153114716"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="18%" id="mcps1.2.5.1.3"><p id="p30605671114716"><a name="p30605671114716"></a><a name="p30605671114716"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="41%" id="mcps1.2.5.1.4"><p id="p63140290114716"><a name="p63140290114716"></a><a name="p63140290114716"></a><strong id="b1478843164517"><a name="b1478843164517"></a><a name="b1478843164517"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row14089841114716"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p4522712205810"><a name="p4522712205810"></a><a name="p4522712205810"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p45225124580"><a name="p45225124580"></a><a name="p45225124580"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.3 "><p id="p6339193387"><a name="p6339193387"></a><a name="p6339193387"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="41%" headers="mcps1.2.5.1.4 "><p id="p1952218123585"><a name="p1952218123585"></a><a name="p1952218123585"></a>Specifies the tag list. For details, see <a href="#table64069331114716">Table 3</a>.</p>
    <p id="p552221225811"><a name="p552221225811"></a><a name="p552221225811"></a>If <strong id="b842352706104838"><a name="b842352706104838"></a><a name="b842352706104838"></a>action</strong> is set to <strong id="b842352706104848"><a name="b842352706104848"></a><a name="b842352706104848"></a>delete</strong>, the tag structure cannot be missing, and the key cannot be left blank or an empty string.</p>
    </td>
    </tr>
    <tr id="row42939634114716"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p452218127585"><a name="p452218127585"></a><a name="p452218127585"></a>action</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p16522012145815"><a name="p16522012145815"></a><a name="p16522012145815"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.3 "><p id="p152241235813"><a name="p152241235813"></a><a name="p152241235813"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41%" headers="mcps1.2.5.1.4 "><p id="p1152219121582"><a name="p1152219121582"></a><a name="p1152219121582"></a>Operation ID (case sensitive)</p>
    <a name="ul181663201195"></a><a name="ul181663201195"></a><ul id="ul181663201195"><li><strong id="b842352706135945"><a name="b842352706135945"></a><a name="b842352706135945"></a>delete</strong>: indicates deleting a tag.</li><li><strong id="b842352706104918"><a name="b842352706104918"></a><a name="b842352706104918"></a>create</strong>: indicates creating a tag. If the same key value already exists, it will be overwritten.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **ResourceTag**  field description

    <a name="table64069331114716"></a>
    <table><thead align="left"><tr id="row5644334114716"><th class="cellrowborder" valign="top" width="20.588235294117645%" id="mcps1.2.5.1.1"><p id="p54537872114716"><a name="p54537872114716"></a><a name="p54537872114716"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.607843137254903%" id="mcps1.2.5.1.2"><p id="p55491527114716"><a name="p55491527114716"></a><a name="p55491527114716"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.607843137254903%" id="mcps1.2.5.1.3"><p id="p65628731114716"><a name="p65628731114716"></a><a name="p65628731114716"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="40.19607843137255%" id="mcps1.2.5.1.4"><p id="p14326995114716"><a name="p14326995114716"></a><a name="p14326995114716"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row19635960114716"><td class="cellrowborder" valign="top" width="20.588235294117645%" headers="mcps1.2.5.1.1 "><p id="p1224383015599"><a name="p1224383015599"></a><a name="p1224383015599"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.607843137254903%" headers="mcps1.2.5.1.2 "><p id="p62441630155916"><a name="p62441630155916"></a><a name="p62441630155916"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.607843137254903%" headers="mcps1.2.5.1.3 "><p id="p02441330195919"><a name="p02441330195919"></a><a name="p02441330195919"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.19607843137255%" headers="mcps1.2.5.1.4 "><p id="p4781631122336"><a name="p4781631122336"></a><a name="p4781631122336"></a>Specifies the resource tag key. Tag keys of a resource must be unique.</p>
    <a name="ul16323643185717"></a><a name="ul16323643185717"></a><ul id="ul16323643185717"><li>A tag key contains a maximum of 36 Unicode characters and cannot be left blank. It can contain only digits, letters, hyphens (-), underscores (_), and at signs (@).</li><li>When <strong id="b842352706105024"><a name="b842352706105024"></a><a name="b842352706105024"></a>action</strong> is set to <strong id="b842352706105027"><a name="b842352706105027"></a><a name="b842352706105027"></a>delete</strong>, the tag character set is not verified, and a key contains a maximum of 127 Unicode characters.</li></ul>
    </td>
    </tr>
    <tr id="row33928679114716"><td class="cellrowborder" valign="top" width="20.588235294117645%" headers="mcps1.2.5.1.1 "><p id="p4244143010594"><a name="p4244143010594"></a><a name="p4244143010594"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.607843137254903%" headers="mcps1.2.5.1.2 "><p id="p1624483018599"><a name="p1624483018599"></a><a name="p1624483018599"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.607843137254903%" headers="mcps1.2.5.1.3 "><p id="p4245530165910"><a name="p4245530165910"></a><a name="p4245530165910"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.19607843137255%" headers="mcps1.2.5.1.4 "><p id="p45707304223349"><a name="p45707304223349"></a><a name="p45707304223349"></a>Specifies the resource tag value.</p>
    <a name="ul944659195818"></a><a name="ul944659195818"></a><ul id="ul944659195818"><li>A tag value contains a maximum of 43 Unicode characters and can be left blank. It can contain only digits, letters, hyphens (-), underscores (_), and at signs (@).</li><li>When <strong id="b1192335526"><a name="b1192335526"></a><a name="b1192335526"></a>action</strong> is set to <strong id="b19848726"><a name="b19848726"></a><a name="b19848726"></a>delete</strong>, the tag character set is not verified, and a value contains a maximum of 255 Unicode characters. If <strong id="b84235270611421"><a name="b84235270611421"></a><a name="b84235270611421"></a>value</strong> is specified, tags are deleted by key and value. If <strong id="b842352706114252"><a name="b842352706114252"></a><a name="b842352706114252"></a>value</strong> is not specified, tags are deleted by key.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    This example shows how to create two resource tags \(key =  **ENV15**  and value =  **ENV15**\) and \(key =  **ENV151**  and value =  **ENV151**\) in the AS group with ID  **e5d27f5c-dd76-4a61-b4bc-a67c5686719a**.

    ```
    POST https://{Endpoint}/autoscaling-api/v1/{project_id}/scaling_group_tag/e5d27f5c-dd76-4a61-b4bc-a67c5686719a/tags/action
    
    { 
      "tags": [
        { 
            "key": "ENV15", 
            "value": "ENV15" 
        }, 
        { 
            "key": "ENV151", 
            "value": "ENV151" 
        }
        ], 
      "action": "create" 
    }
    ```


## Response Message<a name="section11862673114716"></a>

-   Response parameters

    None

-   Example response

    None


## Returned Values<a name="section57954106114716"></a>

-   Normal

    204

-   Abnormal

    <a name="table44760069114716"></a>
    <table><thead align="left"><tr id="row21851625114716"><th class="cellrowborder" valign="top" width="43.5%" id="mcps1.1.3.1.1"><p id="p25151238114716"><a name="p25151238114716"></a><a name="p25151238114716"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.49999999999999%" id="mcps1.1.3.1.2"><p id="p23984387114716"><a name="p23984387114716"></a><a name="p23984387114716"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row63687176114716"><td class="cellrowborder" valign="top" width="43.5%" headers="mcps1.1.3.1.1 "><p id="p58387646114716"><a name="p58387646114716"></a><a name="p58387646114716"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.49999999999999%" headers="mcps1.1.3.1.2 "><p id="p31778892114716"><a name="p31778892114716"></a><a name="p31778892114716"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row17574580114716"><td class="cellrowborder" valign="top" width="43.5%" headers="mcps1.1.3.1.1 "><p id="p14254907114716"><a name="p14254907114716"></a><a name="p14254907114716"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.49999999999999%" headers="mcps1.1.3.1.2 "><p id="p13796781114716"><a name="p13796781114716"></a><a name="p13796781114716"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row57062171114716"><td class="cellrowborder" valign="top" width="43.5%" headers="mcps1.1.3.1.1 "><p id="p58633115114716"><a name="p58633115114716"></a><a name="p58633115114716"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.49999999999999%" headers="mcps1.1.3.1.2 "><p id="p51661884114716"><a name="p51661884114716"></a><a name="p51661884114716"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row62303776114716"><td class="cellrowborder" valign="top" width="43.5%" headers="mcps1.1.3.1.1 "><p id="p13441109114716"><a name="p13441109114716"></a><a name="p13441109114716"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.49999999999999%" headers="mcps1.1.3.1.2 "><p id="p14988030114716"><a name="p14988030114716"></a><a name="p14988030114716"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row674546114716"><td class="cellrowborder" valign="top" width="43.5%" headers="mcps1.1.3.1.1 "><p id="p54638245114716"><a name="p54638245114716"></a><a name="p54638245114716"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.49999999999999%" headers="mcps1.1.3.1.2 "><p id="p63621696114716"><a name="p63621696114716"></a><a name="p63621696114716"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row35724356114716"><td class="cellrowborder" valign="top" width="43.5%" headers="mcps1.1.3.1.1 "><p id="p7991760114716"><a name="p7991760114716"></a><a name="p7991760114716"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.49999999999999%" headers="mcps1.1.3.1.2 "><p id="p43352791114716"><a name="p43352791114716"></a><a name="p43352791114716"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row54630805114716"><td class="cellrowborder" valign="top" width="43.5%" headers="mcps1.1.3.1.1 "><p id="p63019107114716"><a name="p63019107114716"></a><a name="p63019107114716"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.49999999999999%" headers="mcps1.1.3.1.2 "><p id="p4274017114716"><a name="p4274017114716"></a><a name="p4274017114716"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row38466153114716"><td class="cellrowborder" valign="top" width="43.5%" headers="mcps1.1.3.1.1 "><p id="p28750707114716"><a name="p28750707114716"></a><a name="p28750707114716"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.49999999999999%" headers="mcps1.1.3.1.2 "><p id="p47105921114716"><a name="p47105921114716"></a><a name="p47105921114716"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row21300109114716"><td class="cellrowborder" valign="top" width="43.5%" headers="mcps1.1.3.1.1 "><p id="p47587293114716"><a name="p47587293114716"></a><a name="p47587293114716"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.49999999999999%" headers="mcps1.1.3.1.2 "><p id="p29365542114716"><a name="p29365542114716"></a><a name="p29365542114716"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row62963287114716"><td class="cellrowborder" valign="top" width="43.5%" headers="mcps1.1.3.1.1 "><p id="p66861447114716"><a name="p66861447114716"></a><a name="p66861447114716"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.49999999999999%" headers="mcps1.1.3.1.2 "><p id="p47068099114716"><a name="p47068099114716"></a><a name="p47068099114716"></a>Failed to complete the request because an internal service error occurred.</p>
    </td>
    </tr>
    <tr id="row20959714114716"><td class="cellrowborder" valign="top" width="43.5%" headers="mcps1.1.3.1.1 "><p id="p20015260114716"><a name="p20015260114716"></a><a name="p20015260114716"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.49999999999999%" headers="mcps1.1.3.1.2 "><p id="p10623383114716"><a name="p10623383114716"></a><a name="p10623383114716"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row28501588114716"><td class="cellrowborder" valign="top" width="43.5%" headers="mcps1.1.3.1.1 "><p id="p26927315114716"><a name="p26927315114716"></a><a name="p26927315114716"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.49999999999999%" headers="mcps1.1.3.1.2 "><p id="p33628902114716"><a name="p33628902114716"></a><a name="p33628902114716"></a>Failed to complete the request because the server has received an invalid response.</p>
    </td>
    </tr>
    <tr id="row34224667114716"><td class="cellrowborder" valign="top" width="43.5%" headers="mcps1.1.3.1.1 "><p id="p20734632114716"><a name="p20734632114716"></a><a name="p20734632114716"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.49999999999999%" headers="mcps1.1.3.1.2 "><p id="p1783613114716"><a name="p1783613114716"></a><a name="p1783613114716"></a>Failed to complete the request because the system is currently unavailable.</p>
    </td>
    </tr>
    <tr id="row16052523114716"><td class="cellrowborder" valign="top" width="43.5%" headers="mcps1.1.3.1.1 "><p id="p25185952114716"><a name="p25185952114716"></a><a name="p25185952114716"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.49999999999999%" headers="mcps1.1.3.1.2 "><p id="p26796209114716"><a name="p26796209114716"></a><a name="p26796209114716"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section17669131616110"></a>

See  [Error Codes](error-codes.md).

