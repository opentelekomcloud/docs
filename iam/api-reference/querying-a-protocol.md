# Querying a Protocol<a name="en-us_topic_0057845616"></a>

## Function Description<a name="section41911953102858"></a>

This interface is used to query the information about a protocol.

## URI<a name="section19280869102858"></a>

-   URI format

    GET /v3/OS-FEDERATION/identity\_providers/\{idp\_id\}/protocols/\{protocol\_id\}


-   URI parameter description

    <a name="table5854888102858"></a>
    <table><thead align="left"><tr id="row27160337102858"><th class="cellrowborder" valign="top" width="21.02%" id="mcps1.1.5.1.1"><p id="p52503678102858"><a name="p52503678102858"></a><a name="p52503678102858"></a><strong id="b37426530113629"><a name="b37426530113629"></a><a name="b37426530113629"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.7%" id="mcps1.1.5.1.2"><p id="p24939507102858"><a name="p24939507102858"></a><a name="p24939507102858"></a><strong id="b842352706112524"><a name="b842352706112524"></a><a name="b842352706112524"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.43%" id="mcps1.1.5.1.3"><p id="p6834201102858"><a name="p6834201102858"></a><a name="p6834201102858"></a><strong id="b84235270615026"><a name="b84235270615026"></a><a name="b84235270615026"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43.85%" id="mcps1.1.5.1.4"><p id="p16699415102858"><a name="p16699415102858"></a><a name="p16699415102858"></a><strong id="b14438018113629"><a name="b14438018113629"></a><a name="b14438018113629"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row10475414102858"><td class="cellrowborder" valign="top" width="21.02%" headers="mcps1.1.5.1.1 "><p id="p43202238102858"><a name="p43202238102858"></a><a name="p43202238102858"></a>idp_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.7%" headers="mcps1.1.5.1.2 "><p id="p9720374102858"><a name="p9720374102858"></a><a name="p9720374102858"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.43%" headers="mcps1.1.5.1.3 "><p id="p49152806102858"><a name="p49152806102858"></a><a name="p49152806102858"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.85%" headers="mcps1.1.5.1.4 "><p id="p21954359102858"><a name="p21954359102858"></a><a name="p21954359102858"></a>ID of an identity provider.</p>
    </td>
    </tr>
    <tr id="row63371507102858"><td class="cellrowborder" valign="top" width="21.02%" headers="mcps1.1.5.1.1 "><p id="p32818456102858"><a name="p32818456102858"></a><a name="p32818456102858"></a>protocol _id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.7%" headers="mcps1.1.5.1.2 "><p id="p41049265102858"><a name="p41049265102858"></a><a name="p41049265102858"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.43%" headers="mcps1.1.5.1.3 "><p id="p36656167102858"><a name="p36656167102858"></a><a name="p36656167102858"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.85%" headers="mcps1.1.5.1.4 "><p id="p16359521102858"><a name="p16359521102858"></a><a name="p16359521102858"></a>ID of a protocol.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section50052807102858"></a>

-   Request header parameter description

    <a name="table32801338102858"></a>
    <table><thead align="left"><tr id="row13061250102858"><th class="cellrowborder" valign="top" width="21.052105210521052%" id="mcps1.1.5.1.1"><p id="p51328329102858"><a name="p51328329102858"></a><a name="p51328329102858"></a><strong id="b4912712714504"><a name="b4912712714504"></a><a name="b4912712714504"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.6017601760176%" id="mcps1.1.5.1.2"><p id="p63953976102858"><a name="p63953976102858"></a><a name="p63953976102858"></a><strong id="b29624837144946_1"><a name="b29624837144946_1"></a><a name="b29624837144946_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.45174517451745%" id="mcps1.1.5.1.3"><p id="p12889592102858"><a name="p12889592102858"></a><a name="p12889592102858"></a><strong id="b41850847145016"><a name="b41850847145016"></a><a name="b41850847145016"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43.89438943894389%" id="mcps1.1.5.1.4"><p id="p37424049102858"><a name="p37424049102858"></a><a name="p37424049102858"></a><strong id="b46355523145025"><a name="b46355523145025"></a><a name="b46355523145025"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row11449098102858"><td class="cellrowborder" valign="top" width="21.052105210521052%" headers="mcps1.1.5.1.1 "><p id="p54961707102858"><a name="p54961707102858"></a><a name="p54961707102858"></a>Content-Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.6017601760176%" headers="mcps1.1.5.1.2 "><p id="p22713277102858"><a name="p22713277102858"></a><a name="p22713277102858"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.45174517451745%" headers="mcps1.1.5.1.3 "><p id="p27836135102858"><a name="p27836135102858"></a><a name="p27836135102858"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.89438943894389%" headers="mcps1.1.5.1.4 "><p id="p40134482102858"><a name="p40134482102858"></a><a name="p40134482102858"></a>Fill <strong id="b842352706161331"><a name="b842352706161331"></a><a name="b842352706161331"></a>application/json;charset=utf8</strong> in this field.</p>
    </td>
    </tr>
    <tr id="row25666023102858"><td class="cellrowborder" valign="top" width="21.052105210521052%" headers="mcps1.1.5.1.1 "><p id="p65682006102858"><a name="p65682006102858"></a><a name="p65682006102858"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.6017601760176%" headers="mcps1.1.5.1.2 "><p id="p18642265102858"><a name="p18642265102858"></a><a name="p18642265102858"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.45174517451745%" headers="mcps1.1.5.1.3 "><p id="p33628505102858"><a name="p33628505102858"></a><a name="p33628505102858"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.89438943894389%" headers="mcps1.1.5.1.4 "><p id="p51645192143514"><a name="p51645192143514"></a><a name="p51645192143514"></a>Authenticated token.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Sample request

    ```
    curl -i -k -H 'Accept:application/json' -H 'Content-Type:application/json;charset=utf8' -H "X-Auth-Token:$token" -X GET https://10.185.190.118:31943/v3/OS-FEDERATION/identity_providers/ACME/protocols/saml
    ```


## Response<a name="section49786990102858"></a>

-   Response body parameter description

    <a name="table33600724102858"></a>
    <table><thead align="left"><tr id="row58807483102858"><th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.5.1.1"><p id="p65785692102858"><a name="p65785692102858"></a><a name="p65785692102858"></a><strong id="b61512370145115"><a name="b61512370145115"></a><a name="b61512370145115"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.708229177082295%" id="mcps1.1.5.1.2"><p id="p27040837102858"><a name="p27040837102858"></a><a name="p27040837102858"></a><strong id="b29624837144946_3"><a name="b29624837144946_3"></a><a name="b29624837144946_3"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.328267173282672%" id="mcps1.1.5.1.3"><p id="p42824223102858"><a name="p42824223102858"></a><a name="p42824223102858"></a><strong id="b34844838145052"><a name="b34844838145052"></a><a name="b34844838145052"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43.785621437856214%" id="mcps1.1.5.1.4"><p id="p46210066102858"><a name="p46210066102858"></a><a name="p46210066102858"></a><strong id="b2854729314514"><a name="b2854729314514"></a><a name="b2854729314514"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row52027845102858"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.5.1.1 "><p id="p53505888102858"><a name="p53505888102858"></a><a name="p53505888102858"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.708229177082295%" headers="mcps1.1.5.1.2 "><p id="p39009676102858"><a name="p39009676102858"></a><a name="p39009676102858"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.328267173282672%" headers="mcps1.1.5.1.3 "><p id="p5667184102858"><a name="p5667184102858"></a><a name="p5667184102858"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.785621437856214%" headers="mcps1.1.5.1.4 "><p id="p56388789102858"><a name="p56388789102858"></a><a name="p56388789102858"></a>ID of a protocol.</p>
    </td>
    </tr>
    <tr id="row37737059102858"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.5.1.1 "><p id="p36802972102858"><a name="p36802972102858"></a><a name="p36802972102858"></a>mapping_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.708229177082295%" headers="mcps1.1.5.1.2 "><p id="p28250761102858"><a name="p28250761102858"></a><a name="p28250761102858"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.328267173282672%" headers="mcps1.1.5.1.3 "><p id="p6610323102858"><a name="p6610323102858"></a><a name="p6610323102858"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.785621437856214%" headers="mcps1.1.5.1.4 "><p id="p65674145102858"><a name="p65674145102858"></a><a name="p65674145102858"></a>Mapping ID.</p>
    </td>
    </tr>
    <tr id="row54196397102858"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.5.1.1 "><p id="p27832061102858"><a name="p27832061102858"></a><a name="p27832061102858"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.708229177082295%" headers="mcps1.1.5.1.2 "><p id="p39804486102858"><a name="p39804486102858"></a><a name="p39804486102858"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.328267173282672%" headers="mcps1.1.5.1.3 "><p id="p2937903102858"><a name="p2937903102858"></a><a name="p2937903102858"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.785621437856214%" headers="mcps1.1.5.1.4 "><p id="p36643552102858"><a name="p36643552102858"></a><a name="p36643552102858"></a>Resource links of a protocol.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Sample response

    ```
    {
        "protocol": {
            "id": "saml",
            "links": {
                "identity_provider": "https://example.com/v3/OS-FEDERATION/identity_providers/ACME",
                "self": "https://example.com/v3/OS-FEDERATION/identity_providers/ACME/protocols/saml"
            },
            "mapping_id": "ACME"
        }
    }
    ```


## Status Codes<a name="section16111048102858"></a>

<a name="table29926493102858"></a>
<table><thead align="left"><tr id="row18918097102858"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p55970920102858"><a name="p55970920102858"></a><a name="p55970920102858"></a><strong id="b37151362163018"><a name="b37151362163018"></a><a name="b37151362163018"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p37350634102858"><a name="p37350634102858"></a><a name="p37350634102858"></a><strong id="b38470707163018"><a name="b38470707163018"></a><a name="b38470707163018"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row5502529102858"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p43051733102858"><a name="p43051733102858"></a><a name="p43051733102858"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p64638349102858"><a name="p64638349102858"></a><a name="p64638349102858"></a>The request is successful.</p>
</td>
</tr>
<tr id="row44874234102858"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p10934372102858"><a name="p10934372102858"></a><a name="p10934372102858"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p13268967102858"><a name="p13268967102858"></a><a name="p13268967102858"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="row52311841102858"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p9400699102858"><a name="p9400699102858"></a><a name="p9400699102858"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p23259137102858"><a name="p23259137102858"></a><a name="p23259137102858"></a>You must enter a username and password to access the requested page.</p>
</td>
</tr>
<tr id="row8005649102858"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p44477829102858"><a name="p44477829102858"></a><a name="p44477829102858"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p45934426102858"><a name="p45934426102858"></a><a name="p45934426102858"></a>You are forbidden to access the requested page.</p>
</td>
</tr>
<tr id="row10756656102858"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p65982841102858"><a name="p65982841102858"></a><a name="p65982841102858"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p43009910102858"><a name="p43009910102858"></a><a name="p43009910102858"></a>The server could not find the requested page.</p>
</td>
</tr>
<tr id="row51544876102858"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p14385427102858"><a name="p14385427102858"></a><a name="p14385427102858"></a>405</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p24368930102858"><a name="p24368930102858"></a><a name="p24368930102858"></a>You are not allowed to use the method specified in the request.</p>
</td>
</tr>
<tr id="row17993785102858"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p48210456102858"><a name="p48210456102858"></a><a name="p48210456102858"></a>413</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p12732852102858"><a name="p12732852102858"></a><a name="p12732852102858"></a>The request entity is too large.</p>
</td>
</tr>
<tr id="row47486804102858"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p21225877102858"><a name="p21225877102858"></a><a name="p21225877102858"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p41574471102858"><a name="p41574471102858"></a><a name="p41574471102858"></a>Failed to complete the request because of an internal service error.</p>
</td>
</tr>
<tr id="row38625921102858"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p41691935102858"><a name="p41691935102858"></a><a name="p41691935102858"></a>503</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p21603585102858"><a name="p21603585102858"></a><a name="p21603585102858"></a>Failed to complete the request because the service is unavailable.</p>
</td>
</tr>
</tbody>
</table>

