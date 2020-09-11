# Querying Basic Information of a VPC Endpoint Service<a name="vpcep_06_0302"></a>

## Function<a name="section29800032"></a>

This API is used to query basic information of a target VPC endpoint service. You can use this API to query the target VPC endpoint service to be accessed. This API can also be used by other users to query basic information of your VPC endpoint service, without exposing your server information.

## URI<a name="section66873698"></a>

GET /v1/\{project\_id\}/vpc-endpoint-services/describe?endpoint\_service\_name=\{endpoint\_service\_name\}&id=\{endpoint\_service\_id\}

[Table 1](#table19259243)  describes the required parameters.

**Table  1**  Parameters

<a name="table19259243"></a>
<table><thead align="left"><tr id="row55868958"><th class="cellrowborder" valign="top" width="28.999999999999996%" id="mcps1.2.4.1.1"><p id="p29091726"><a name="p29091726"></a><a name="p29091726"></a><strong id="b87145213519"><a name="b87145213519"></a><a name="b87145213519"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="30%" id="mcps1.2.4.1.2"><p id="p7619615"><a name="p7619615"></a><a name="p7619615"></a><strong id="b1019813256516"><a name="b1019813256516"></a><a name="b1019813256516"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="41%" id="mcps1.2.4.1.3"><p id="p13209080"><a name="p13209080"></a><a name="p13209080"></a><strong id="b145216267515"><a name="b145216267515"></a><a name="b145216267515"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row63302594"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.4.1.1 "><p id="p27236517"><a name="p27236517"></a><a name="p27236517"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.2 "><p id="p58674248"><a name="p58674248"></a><a name="p58674248"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="41%" headers="mcps1.2.4.1.3 "><p id="p54993619"><a name="p54993619"></a><a name="p54993619"></a>Specifies the project ID. For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section64992378"></a>

-   Parameter description

    **Table  2**  Request parameters

    <a name="table16494874"></a>
    <table><thead align="left"><tr id="row60344611"><th class="cellrowborder" valign="top" width="27%" id="mcps1.2.5.1.1"><p id="p56075332"><a name="p56075332"></a><a name="p56075332"></a><strong id="b2363133813519"><a name="b2363133813519"></a><a name="b2363133813519"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.2"><p id="p45808045"><a name="p45808045"></a><a name="p45808045"></a><strong id="b538893721"><a name="b538893721"></a><a name="b538893721"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.3"><p id="p04912812293"><a name="p04912812293"></a><a name="p04912812293"></a><strong id="b10280928868"><a name="b10280928868"></a><a name="b10280928868"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="37%" id="mcps1.2.5.1.4"><p id="p19464199"><a name="p19464199"></a><a name="p19464199"></a><strong id="b1233643617"><a name="b1233643617"></a><a name="b1233643617"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row33096314"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.5.1.1 "><p id="p63555757"><a name="p63555757"></a><a name="p63555757"></a>endpoint_service_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p47742664"><a name="p47742664"></a><a name="p47742664"></a>No</p>
    <div class="note" id="note20155193717514"><a name="note20155193717514"></a><a name="note20155193717514"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p215517374511"><a name="p215517374511"></a><a name="p215517374511"></a>Either this parameter or the <strong id="b17561151485814"><a name="b17561151485814"></a><a name="b17561151485814"></a>id</strong> parameter must be selected.</p>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p349168152917"><a name="p349168152917"></a><a name="p349168152917"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.5.1.4 "><p id="p41950580"><a name="p41950580"></a><a name="p41950580"></a>Specifies the name of the VPC endpoint service.</p>
    </td>
    </tr>
    <tr id="row42010904"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.5.1.1 "><p id="p47440031"><a name="p47440031"></a><a name="p47440031"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p17437323"><a name="p17437323"></a><a name="p17437323"></a>No</p>
    <div class="note" id="note97636123717"><a name="note97636123717"></a><a name="note97636123717"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p4763141212711"><a name="p4763141212711"></a><a name="p4763141212711"></a>Either this parameter or the <strong id="b9151174495816"><a name="b9151174495816"></a><a name="b9151174495816"></a>endpoint_service_name</strong> parameter must be selected.</p>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p249113872912"><a name="p249113872912"></a><a name="p249113872912"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.5.1.4 "><p id="p5301108164415"><a name="p5301108164415"></a><a name="p5301108164415"></a>Specifies the unique ID of the VPC endpoint service.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    GET https://{endpoint}/v1/{project_id}/vpc-endpoint-services/describe?id={4189d3c2-8882-4871-a3c2-d380272eed83}
    ```


## Response<a name="section29891285"></a>

-   Parameter description

    **Table  3**  Response parameters

    <a name="table14236141"></a>
    <table><thead align="left"><tr id="row33026327"><th class="cellrowborder" valign="top" width="24.242424242424242%" id="mcps1.2.4.1.1"><p id="p57886792"><a name="p57886792"></a><a name="p57886792"></a><strong id="b605688002"><a name="b605688002"></a><a name="b605688002"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="29.292929292929294%" id="mcps1.2.4.1.2"><p id="p58318570"><a name="p58318570"></a><a name="p58318570"></a><strong id="b1114705684"><a name="b1114705684"></a><a name="b1114705684"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="46.464646464646464%" id="mcps1.2.4.1.3"><p id="p26183716"><a name="p26183716"></a><a name="p26183716"></a><strong id="b1072510847"><a name="b1072510847"></a><a name="b1072510847"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row40506271"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p59782531"><a name="p59782531"></a><a name="p59782531"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="p10546806"><a name="p10546806"></a><a name="p10546806"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.4.1.3 "><p id="p48984995"><a name="p48984995"></a><a name="p48984995"></a>Specifies the unique ID of the VPC endpoint service.</p>
    </td>
    </tr>
    <tr id="row38211774"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p8145970"><a name="p8145970"></a><a name="p8145970"></a>service_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="p55843827"><a name="p55843827"></a><a name="p55843827"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.4.1.3 "><p id="p27056104"><a name="p27056104"></a><a name="p27056104"></a>Specifies the name of the VPC endpoint service.</p>
    </td>
    </tr>
    <tr id="row42178345"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p61002824"><a name="p61002824"></a><a name="p61002824"></a>service_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="p42281744"><a name="p42281744"></a><a name="p42281744"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.4.1.3 "><p id="p135911520141219"><a name="p135911520141219"></a><a name="p135911520141219"></a>Specifies the type of the VPC endpoint service. Only your private services can be configured into interface VPC endpoint services.</p>
    <a name="ul649612552553"></a><a name="ul649612552553"></a><ul id="ul649612552553"><li>Gateway: VPC endpoint services of this type are configured by operations people. You can use them directly without the need to create one by yourselves.</li><li>Interface: VPC endpoint services of this type include cloud services configured by operations people and private services created by yourselves. You cannot configure these cloud services, but can use them.</li></ul>
    <p id="p941115410718"><a name="p941115410718"></a><a name="p941115410718"></a>You can perform the operations in <a href="creating-a-vpc-endpoint.md">Creating a VPC Endpoint</a> to create VPC endpoints for accessing VPC endpoints of the gateway and interface types.</p>
    </td>
    </tr>
    <tr id="row20423017"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p43651709"><a name="p43651709"></a><a name="p43651709"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="p46127541"><a name="p46127541"></a><a name="p46127541"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.4.1.3 "><p id="p22890001"><a name="p22890001"></a><a name="p22890001"></a>Specifies the creation time of the VPC endpoint service.</p>
    <p id="p871616113394"><a name="p871616113394"></a><a name="p871616113394"></a>The UTC time format is used: YYYY-MM-DDTHH:MM:SSZ.</p>
    </td>
    </tr>
    <tr id="row389811654114"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p2089991612413"><a name="p2089991612413"></a><a name="p2089991612413"></a>is_charge</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="p68996168416"><a name="p68996168416"></a><a name="p68996168416"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.4.1.3 "><p id="p1389951614111"><a name="p1389951614111"></a><a name="p1389951614111"></a>Specifies whether the associated VPC endpoint carries a charge.</p>
    <a name="ul4942193713444"></a><a name="ul4942193713444"></a><ul id="ul4942193713444"><li><strong id="vpcep_06_0301_b19200830195415"><a name="vpcep_06_0301_b19200830195415"></a><a name="vpcep_06_0301_b19200830195415"></a>true</strong>: indicates that the associated VPC endpoint carries a charge.</li><li><strong id="vpcep_06_0301_b950713385556"><a name="vpcep_06_0301_b950713385556"></a><a name="vpcep_06_0301_b950713385556"></a>false</strong>: indicates that the associated VPC endpoint does not a charge.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
      "id": "9d4c1028-1336-4556-9881-b5d807c1b8a8",
      "service_name": "test123",
      "service_type": "interface",
      "created_at": "2018-09-17T07:28:31Z",
      "is_charge": "true"
    }
    ```


## Status Code<a name="section5275033"></a>

For details about status codes, see  [Status Code](/vpcep/api-reference/common/status-code.md).

