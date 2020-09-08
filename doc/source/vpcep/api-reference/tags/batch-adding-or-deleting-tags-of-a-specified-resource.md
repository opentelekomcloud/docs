# Batch Adding or Deleting Tags of a Specified Resource<a name="vpcep_06_0502"></a>

## Function<a name="section661424813316"></a>

This API is used to batch add or delete tags for a specified VPC endpoint service or VPC endpoint.

-   You can add a maximum of 10 tags to a resource.

## URI<a name="section2061734818319"></a>

POST  /v1/\{project\_id\}/\{resource\_type\}/\{resource\_id\}/tags/action

[Table 1](#table366094812311)  describes the required parameters.

**Table  1**  Parameter description

<a name="table366094812311"></a>
<table><thead align="left"><tr id="row41660491739"><th class="cellrowborder" valign="top" width="25.509999999999998%" id="mcps1.2.5.1.1"><p id="p1416684915316"><a name="p1416684915316"></a><a name="p1416684915316"></a><strong id="b13237153019273"><a name="b13237153019273"></a><a name="b13237153019273"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="21.43%" id="mcps1.2.5.1.2"><p id="p19166154917315"><a name="p19166154917315"></a><a name="p19166154917315"></a><strong id="b8472203112718"><a name="b8472203112718"></a><a name="b8472203112718"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.33%" id="mcps1.2.5.1.3"><p id="p4166249836"><a name="p4166249836"></a><a name="p4166249836"></a><strong id="b1352393210278"><a name="b1352393210278"></a><a name="b1352393210278"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="36.730000000000004%" id="mcps1.2.5.1.4"><p id="p141665498310"><a name="p141665498310"></a><a name="p141665498310"></a><strong id="b14648123312270"><a name="b14648123312270"></a><a name="b14648123312270"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row2166154910312"><td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.5.1.1 "><p id="p11166114916316"><a name="p11166114916316"></a><a name="p11166114916316"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.2.5.1.2 "><p id="p216644910311"><a name="p216644910311"></a><a name="p216644910311"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.33%" headers="mcps1.2.5.1.3 "><p id="p1216614491532"><a name="p1216614491532"></a><a name="p1216614491532"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="36.730000000000004%" headers="mcps1.2.5.1.4 "><p id="p916613492318"><a name="p916613492318"></a><a name="p916613492318"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row916610491316"><td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.5.1.1 "><p id="p131662491537"><a name="p131662491537"></a><a name="p131662491537"></a>resource_type</p>
</td>
<td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.2.5.1.2 "><p id="p91665491736"><a name="p91665491736"></a><a name="p91665491736"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.33%" headers="mcps1.2.5.1.3 "><p id="p31660491332"><a name="p31660491332"></a><a name="p31660491332"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="36.730000000000004%" headers="mcps1.2.5.1.4 "><p id="p201661649630"><a name="p201661649630"></a><a name="p201661649630"></a>Specifies the resource type. The value is <strong id="b325384110279"><a name="b325384110279"></a><a name="b325384110279"></a>endpoint_service</strong> or <strong id="b6254194182714"><a name="b6254194182714"></a><a name="b6254194182714"></a>endpoint</strong>.</p>
</td>
</tr>
<tr id="row016610491139"><td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.5.1.1 "><p id="p216613491315"><a name="p216613491315"></a><a name="p216613491315"></a>resource_id</p>
</td>
<td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.2.5.1.2 "><p id="p181669491533"><a name="p181669491533"></a><a name="p181669491533"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.33%" headers="mcps1.2.5.1.3 "><p id="p1216714490315"><a name="p1216714490315"></a><a name="p1216714490315"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="36.730000000000004%" headers="mcps1.2.5.1.4 "><p id="p1616764911314"><a name="p1616764911314"></a><a name="p1616764911314"></a>Specifies the resource ID, which can be <strong id="b1571013457276"><a name="b1571013457276"></a><a name="b1571013457276"></a>Endpoint Service ID</strong> or <strong id="b671104552715"><a name="b671104552715"></a><a name="b671104552715"></a>Endpoint ID</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section1469314482038"></a>

-   Parameter description

    **Table  2**  Request parameters

    <a name="table463234813314"></a>
    <table><thead align="left"><tr id="row10166949736"><th class="cellrowborder" valign="top" width="20.932093209320936%" id="mcps1.2.5.1.1"><p id="p2016619491136"><a name="p2016619491136"></a><a name="p2016619491136"></a><strong id="b6373105217278"><a name="b6373105217278"></a><a name="b6373105217278"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.4020402040204%" id="mcps1.2.5.1.2"><p id="p316612497317"><a name="p316612497317"></a><a name="p316612497317"></a><strong id="b32511053172710"><a name="b32511053172710"></a><a name="b32511053172710"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.292129212921292%" id="mcps1.2.5.1.3"><p id="p1767832713386"><a name="p1767832713386"></a><a name="p1767832713386"></a><strong id="b356954142717"><a name="b356954142717"></a><a name="b356954142717"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="37.37373737373737%" id="mcps1.2.5.1.4"><p id="p1316614915318"><a name="p1316614915318"></a><a name="p1316614915318"></a><strong id="b168493543272"><a name="b168493543272"></a><a name="b168493543272"></a>Example</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1516610494312"><td class="cellrowborder" valign="top" width="20.932093209320936%" headers="mcps1.2.5.1.1 "><p id="p171667491939"><a name="p171667491939"></a><a name="p171667491939"></a>Content-type</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.4020402040204%" headers="mcps1.2.5.1.2 "><p id="p161661949236"><a name="p161661949236"></a><a name="p161661949236"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.292129212921292%" headers="mcps1.2.5.1.3 "><p id="p12678192713383"><a name="p12678192713383"></a><a name="p12678192713383"></a>Specifies the MIME type of the entity sending the request.</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.37373737373737%" headers="mcps1.2.5.1.4 "><p id="p121669499312"><a name="p121669499312"></a><a name="p121669499312"></a>application/json</p>
    </td>
    </tr>
    <tr id="row7166649834"><td class="cellrowborder" valign="top" width="20.932093209320936%" headers="mcps1.2.5.1.1 "><p id="p1516611492037"><a name="p1516611492037"></a><a name="p1516611492037"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.4020402040204%" headers="mcps1.2.5.1.2 "><p id="p21664491312"><a name="p21664491312"></a><a name="p21664491312"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.292129212921292%" headers="mcps1.2.5.1.3 "><p id="p1167815271382"><a name="p1167815271382"></a><a name="p1167815271382"></a>Specifies the user token.</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.37373737373737%" headers="mcps1.2.5.1.4 "><p id="p1316644912314"><a name="p1316644912314"></a><a name="p1316644912314"></a>N/A</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Parameter description

    <a name="table472134815318"></a>
    <table><thead align="left"><tr id="row2016711493316"><th class="cellrowborder" valign="top" width="24.490000000000002%" id="mcps1.2.5.1.1"><p id="p01671049132"><a name="p01671049132"></a><a name="p01671049132"></a><strong id="b2892888289"><a name="b2892888289"></a><a name="b2892888289"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.43%" id="mcps1.2.5.1.2"><p id="p116711494315"><a name="p116711494315"></a><a name="p116711494315"></a><strong id="b563720132288"><a name="b563720132288"></a><a name="b563720132288"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25.509999999999998%" id="mcps1.2.5.1.3"><p id="p16167549535"><a name="p16167549535"></a><a name="p16167549535"></a><strong id="b12611101611289"><a name="b12611101611289"></a><a name="b12611101611289"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.57%" id="mcps1.2.5.1.4"><p id="p101673495311"><a name="p101673495311"></a><a name="p101673495311"></a><strong id="b15620181762817"><a name="b15620181762817"></a><a name="b15620181762817"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row216713494314"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.5.1.1 "><p id="p016718491237"><a name="p016718491237"></a><a name="p016718491237"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.2.5.1.2 "><p id="p216713495317"><a name="p216713495317"></a><a name="p216713495317"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.5.1.3 "><p id="p19167249330"><a name="p19167249330"></a><a name="p19167249330"></a>List&lt;resource_tag&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.2.5.1.4 "><p id="p7167149832"><a name="p7167149832"></a><a name="p7167149832"></a>Lists the tags.</p>
    <p id="p131674497310"><a name="p131674497310"></a><a name="p131674497310"></a>This parameter is mandatory for common tenants.</p>
    </td>
    </tr>
    <tr id="row7167194920310"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.5.1.1 "><p id="p1416718491037"><a name="p1416718491037"></a><a name="p1416718491037"></a>action</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.2.5.1.2 "><p id="p161679491431"><a name="p161679491431"></a><a name="p161679491431"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.5.1.3 "><p id="p41675493312"><a name="p41675493312"></a><a name="p41675493312"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.2.5.1.4 "><p id="p1316794911313"><a name="p1316794911313"></a><a name="p1316794911313"></a>Specifies the operation to be performed, which can be <strong id="b842352706101829"><a name="b842352706101829"></a><a name="b842352706101829"></a>create</strong> or <strong id="b842352706101833"><a name="b842352706101833"></a><a name="b842352706101833"></a>delete</strong></p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  Data structure of the  **resource\_tag**  field

    <a name="table97481481333"></a>
    <table><thead align="left"><tr id="row2016764915312"><th class="cellrowborder" valign="top" width="24.48755124487551%" id="mcps1.2.5.1.1"><p id="p111679491337"><a name="p111679491337"></a><a name="p111679491337"></a><strong id="b77177216513"><a name="b77177216513"></a><a name="b77177216513"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.42785721427857%" id="mcps1.2.5.1.2"><p id="p616713496313"><a name="p616713496313"></a><a name="p616713496313"></a><strong id="b2676234511"><a name="b2676234511"></a><a name="b2676234511"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p3167649832"><a name="p3167649832"></a><a name="p3167649832"></a><strong id="b176641445111"><a name="b176641445111"></a><a name="b176641445111"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.5.1.4"><p id="p51670493314"><a name="p51670493314"></a><a name="p51670493314"></a><strong id="b3619105185113"><a name="b3619105185113"></a><a name="b3619105185113"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row18167134912310"><td class="cellrowborder" valign="top" width="24.48755124487551%" headers="mcps1.2.5.1.1 "><p id="p1167749537"><a name="p1167749537"></a><a name="p1167749537"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.2 "><p id="p716713491233"><a name="p716713491233"></a><a name="p716713491233"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p9167204919312"><a name="p9167204919312"></a><a name="p9167204919312"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p131679498315"><a name="p131679498315"></a><a name="p131679498315"></a>Specifies the tag key. A tag key contains a maximum of 36 Unicode characters</p>
    <p id="p9167184912313"><a name="p9167184912313"></a><a name="p9167184912313"></a>The key meets the requirements in <a href="tag-character-set-specifications.md">Tag Character Set Specifications</a>.</p>
    </td>
    </tr>
    <tr id="row1116713491835"><td class="cellrowborder" valign="top" width="24.48755124487551%" headers="mcps1.2.5.1.1 "><p id="p91671749238"><a name="p91671749238"></a><a name="p91671749238"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.2 "><p id="p31671249235"><a name="p31671249235"></a><a name="p31671249235"></a>This parameter is mandatory when <strong id="b842352706143922"><a name="b842352706143922"></a><a name="b842352706143922"></a>action</strong> is set to <strong id="b842352706143928"><a name="b842352706143928"></a><a name="b842352706143928"></a>create</strong> and optional when <strong id="b2107046872143949"><a name="b2107046872143949"></a><a name="b2107046872143949"></a>action</strong> is set to <strong id="b1548858455143949"><a name="b1548858455143949"></a><a name="b1548858455143949"></a>delete</strong>.)</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p81670495315"><a name="p81670495315"></a><a name="p81670495315"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p11681491312"><a name="p11681491312"></a><a name="p11681491312"></a>Specifies the tag value. Each value contains a maximum of 43 Unicode characters. If <strong id="b633516399164"><a name="b633516399164"></a><a name="b633516399164"></a>value</strong> is specified, tags are deleted by key and value. If <strong id="b23498393160"><a name="b23498393160"></a><a name="b23498393160"></a>value</strong> is not specified, tags are deleted by key.</p>
    <p id="p191682049733"><a name="p191682049733"></a><a name="p191682049733"></a>The value meets the requirements in <a href="tag-character-set-specifications.md">Tag Character Set Specifications</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    POST https://127.0.0.1:7443/v1/\{project\_id\}/endpoint\_service/\{resource\_id\}/tags/action

    or https://127.0.0.1:7443/v1/\{project\_id\}/endpoint/\{resource\_id\}/tags/action

    POST /v1/\{project\_id\}/\{resource\_type\}/\{resource\_id\}/tags/action 

    ```
    {
        "action": "create",
        "tags": [
            {
                "key": "key1",
                "value": "value1"
            },
            {
                "key": "key",
                "value": "value3"
            }
    ]
    }
    ```

    or

    ```
    {
        "action": "delete",
        "tags": [
            {
                "key": "key1"
             },
            {
                "key": "key2",
                "value": "value3"
            }
    ]
    }
    ```


## Response<a name="section108825481834"></a>

None

## Status Code<a name="section158868481831"></a>

For details about status codes, see  [Status Code](/vpcep/api-reference/common/status-code.md).

