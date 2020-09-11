# Querying All DCS Instances of a Tenant<a name="EN-US_TOPIC_0237964375"></a>

## Function<a name="section20085343"></a>

This API is used to query DCS instances of a tenant, and allows you to specify query criteria.

## URI<a name="section46550364"></a>

-   URI format:

    GET /v1.0/\{project\_id\}/instances?start=\{start\}&limit=\{limit\}&name=\{name\}&status=\{status\}&id=\{id\}&includeFailure=\{includeFailure\}&isExactMatchName=\{isExactMatchName\}

-   Parameter description:

    [Table 1](#table31915390)  describes the parameters of this API.


**Table  1**  Parameter description

<a name="table31915390"></a>
<table><thead align="left"><tr id="row46521641"><th class="cellrowborder" valign="top" width="17.17171717171717%" id="mcps1.2.5.1.1"><p id="p10156578"><a name="p10156578"></a><a name="p10156578"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="21.21212121212121%" id="mcps1.2.5.1.2"><p id="p17376524"><a name="p17376524"></a><a name="p17376524"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="19.19191919191919%" id="mcps1.2.5.1.3"><p id="p65321231"><a name="p65321231"></a><a name="p65321231"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="42.42424242424242%" id="mcps1.2.5.1.4"><p id="p56528338"><a name="p56528338"></a><a name="p56528338"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row15392637"><td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.2.5.1.1 "><p id="p38844089"><a name="p38844089"></a><a name="p38844089"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.5.1.2 "><p id="p59363501"><a name="p59363501"></a><a name="p59363501"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.5.1.3 "><p id="p43714306"><a name="p43714306"></a><a name="p43714306"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.5.1.4 "><p id="p51197920"><a name="p51197920"></a><a name="p51197920"></a>Project ID.</p>
</td>
</tr>
<tr id="row58128097"><td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.2.5.1.1 "><p id="p10755422"><a name="p10755422"></a><a name="p10755422"></a>start</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.5.1.2 "><p id="p65882872"><a name="p65882872"></a><a name="p65882872"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.5.1.3 "><p id="p34912406"><a name="p34912406"></a><a name="p34912406"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.5.1.4 "><p id="p9332641"><a name="p9332641"></a><a name="p9332641"></a>Start number for querying DCS instances. It cannot be lower than 1.</p>
<p id="p16884906"><a name="p16884906"></a><a name="p16884906"></a>By default, the start number is 1.</p>
</td>
</tr>
<tr id="row17746432"><td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.2.5.1.1 "><p id="p28174876"><a name="p28174876"></a><a name="p28174876"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.5.1.2 "><p id="p463580"><a name="p463580"></a><a name="p463580"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.5.1.3 "><p id="p37549992"><a name="p37549992"></a><a name="p37549992"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.5.1.4 "><p id="p21650537"><a name="p21650537"></a><a name="p21650537"></a>Maximum number of DCS instances displayed on each page.</p>
<p id="p60637113"><a name="p60637113"></a><a name="p60637113"></a>Minimum value: 1</p>
<p id="p8863111"><a name="p8863111"></a><a name="p8863111"></a>If this parameter is left unspecified, there is no limit on the maximum number of DCS instances displayed on each page.</p>
</td>
</tr>
<tr id="row12659140"><td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.2.5.1.1 "><p id="p18757432"><a name="p18757432"></a><a name="p18757432"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.5.1.2 "><p id="p42956987"><a name="p42956987"></a><a name="p42956987"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.5.1.3 "><p id="p56963960"><a name="p56963960"></a><a name="p56963960"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.5.1.4 "><p id="p50678037"><a name="p50678037"></a><a name="p50678037"></a>DCS instance name.</p>
</td>
</tr>
<tr id="row53449151"><td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.2.5.1.1 "><p id="p34413968"><a name="p34413968"></a><a name="p34413968"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.5.1.2 "><p id="p36067989"><a name="p36067989"></a><a name="p36067989"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.5.1.3 "><p id="p35825974"><a name="p35825974"></a><a name="p35825974"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.5.1.4 "><p id="p16222813"><a name="p16222813"></a><a name="p16222813"></a>DCS instance status. For details about status, see <a href="dcs-instance-statuses.md">DCS Instance Statuses</a>.</p>
</td>
</tr>
<tr id="row38979439"><td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.2.5.1.1 "><p id="p3218006"><a name="p3218006"></a><a name="p3218006"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.5.1.2 "><p id="p59331962"><a name="p59331962"></a><a name="p59331962"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.5.1.3 "><p id="p41159618"><a name="p41159618"></a><a name="p41159618"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.5.1.4 "><p id="p45594775"><a name="p45594775"></a><a name="p45594775"></a>Instance ID.</p>
</td>
</tr>
<tr id="row7699793"><td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.2.5.1.1 "><p id="p19703524"><a name="p19703524"></a><a name="p19703524"></a>includeFailure</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.5.1.2 "><p id="p52481591"><a name="p52481591"></a><a name="p52481591"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.5.1.3 "><p id="p23150450"><a name="p23150450"></a><a name="p23150450"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.5.1.4 "><p id="p63247166"><a name="p63247166"></a><a name="p63247166"></a>An indicator of whether the number of DCS instances that failed to be created will be returned to the API caller.</p>
<p id="p32353586"><a name="p32353586"></a><a name="p32353586"></a>Options:</p>
<a name="ul22746818"></a><a name="ul22746818"></a><ul id="ul22746818"><li><strong id="b30552999"><a name="b30552999"></a><a name="b30552999"></a>true</strong>: The number of DCS instances that failed to be created will be returned to the API caller.</li><li><strong id="b58873877"><a name="b58873877"></a><a name="b58873877"></a>false</strong> or others: The number of DCS instances that failed to be created will not be returned to the API caller.</li></ul>
</td>
</tr>
<tr id="row60102846"><td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.2.5.1.1 "><p id="p36492363"><a name="p36492363"></a><a name="p36492363"></a>isExactMatchName</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.5.1.2 "><p id="p3091445"><a name="p3091445"></a><a name="p3091445"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.5.1.3 "><p id="p49080483"><a name="p49080483"></a><a name="p49080483"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.5.1.4 "><p id="p16096190"><a name="p16096190"></a><a name="p16096190"></a>An indicator of whether to perform an exact or fuzzy match based on instance name.</p>
<p id="p10647983"><a name="p10647983"></a><a name="p10647983"></a>Options:</p>
<a name="ul28722989"></a><a name="ul28722989"></a><ul id="ul28722989"><li><strong id="b44860761"><a name="b44860761"></a><a name="b44860761"></a>true</strong>: exact match</li><li><strong id="b9842985"><a name="b9842985"></a><a name="b9842985"></a>false</strong>: fuzzy match</li></ul>
<p id="p21478002"><a name="p21478002"></a><a name="p21478002"></a>Default value: <strong id="b59084293"><a name="b59084293"></a><a name="b59084293"></a>false</strong></p>
</td>
</tr>
</tbody>
</table>

-   Example response:

    ```
    GET /v1.0/bd6b78e2ff9e4e47bc260803ddcc7a21/instances?start=1&limit=10&name=&status=&id=&includeFailure=true&isExactMatchName=false
    ```


## Request<a name="section16300099"></a>

None.

## Response<a name="section12483163"></a>

-   Status code:

    If status code "200 OK" is returned, this request is fulfilled. For description of other status codes, see  [API Usage Guidelines](api-usage-guidelines.md).

-   Response parameter:

    [Table 2](#table18803055)  describes response parameters.


**Table  2**  Parameter description

<a name="table18803055"></a>
<table><thead align="left"><tr id="row53472466"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.1"><p id="p36302522"><a name="p36302522"></a><a name="p36302522"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="36%" id="mcps1.2.4.1.2"><p id="p54823154"><a name="p54823154"></a><a name="p54823154"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="43%" id="mcps1.2.4.1.3"><p id="p11490466"><a name="p11490466"></a><a name="p11490466"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row58312563"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p25697164"><a name="p25697164"></a><a name="p25697164"></a>instance_num</p>
</td>
<td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.2 "><p id="p1095574"><a name="p1095574"></a><a name="p1095574"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.4.1.3 "><p id="p21632697"><a name="p21632697"></a><a name="p21632697"></a>Number of DCS instances.</p>
</td>
</tr>
<tr id="row60476547"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p66762109"><a name="p66762109"></a><a name="p66762109"></a>instances</p>
</td>
<td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.2 "><p id="p39021731"><a name="p39021731"></a><a name="p39021731"></a>Array.</p>
<p id="p15651267"><a name="p15651267"></a><a name="p15651267"></a>For details, see <a href="#ref478579959">Table 3</a>.</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.4.1.3 "><p id="p1267094"><a name="p1267094"></a><a name="p1267094"></a>Array of DCS instance details.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Parameter description of the instances array

<a name="ref478579959"></a>
<table><thead align="left"><tr id="row1548018"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="p58280624"><a name="p58280624"></a><a name="p58280624"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.4.1.2"><p id="p23110107"><a name="p23110107"></a><a name="p23110107"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="65%" id="mcps1.2.4.1.3"><p id="p59979354"><a name="p59979354"></a><a name="p59979354"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row26489494"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p65274230"><a name="p65274230"></a><a name="p65274230"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p52721250"><a name="p52721250"></a><a name="p52721250"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p42562883"><a name="p42562883"></a><a name="p42562883"></a>DCS instance name.</p>
</td>
</tr>
<tr id="row47521635"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p24047246"><a name="p24047246"></a><a name="p24047246"></a>engine</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p1669922"><a name="p1669922"></a><a name="p1669922"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p1045957"><a name="p1045957"></a><a name="p1045957"></a>Cache engine.</p>
</td>
</tr>
<tr id="row9413621"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p24305845"><a name="p24305845"></a><a name="p24305845"></a>capacity</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p22616409"><a name="p22616409"></a><a name="p22616409"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p19989834"><a name="p19989834"></a><a name="p19989834"></a>Cache capacity.</p>
<p id="p45690778"><a name="p45690778"></a><a name="p45690778"></a>Unit: GB.</p>
</td>
</tr>
<tr id="row8563823"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p22581040"><a name="p22581040"></a><a name="p22581040"></a>ip</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p17124983"><a name="p17124983"></a><a name="p17124983"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p44946345"><a name="p44946345"></a><a name="p44946345"></a>Cache node's IP address in tenant's VPC.</p>
</td>
</tr>
<tr id="row1863927"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p16760375"><a name="p16760375"></a><a name="p16760375"></a>port</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p15413144"><a name="p15413144"></a><a name="p15413144"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p40505153"><a name="p40505153"></a><a name="p40505153"></a>Port of the cache node.</p>
</td>
</tr>
<tr id="row29002065"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p357050"><a name="p357050"></a><a name="p357050"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p28921088"><a name="p28921088"></a><a name="p28921088"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p60906762"><a name="p60906762"></a><a name="p60906762"></a>Cache instance status. For details about status, see <a href="dcs-instance-statuses.md">DCS Instance Statuses</a>.</p>
</td>
</tr>
<tr id="row34500672"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p43091084"><a name="p43091084"></a><a name="p43091084"></a>max_memory</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p716883"><a name="p716883"></a><a name="p716883"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p58067583"><a name="p58067583"></a><a name="p58067583"></a>Overall memory size.</p>
<p id="p52846207"><a name="p52846207"></a><a name="p52846207"></a>Unit: MB.</p>
</td>
</tr>
<tr id="row5853816"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p4397093"><a name="p4397093"></a><a name="p4397093"></a>used_memory</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p20620271"><a name="p20620271"></a><a name="p20620271"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p59629245"><a name="p59629245"></a><a name="p59629245"></a>Size of the used memory.</p>
<p id="p66901161"><a name="p66901161"></a><a name="p66901161"></a>Unit: MB.</p>
</td>
</tr>
<tr id="row65239544"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p49911687"><a name="p49911687"></a><a name="p49911687"></a>instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p16314835"><a name="p16314835"></a><a name="p16314835"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p46433219"><a name="p46433219"></a><a name="p46433219"></a>DCS instance ID.</p>
</td>
</tr>
<tr id="row15245788"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p26949310"><a name="p26949310"></a><a name="p26949310"></a>resource_spec_code</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p35410488"><a name="p35410488"></a><a name="p35410488"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p49677299"><a name="p49677299"></a><a name="p49677299"></a>Resource specifications.</p>
<a name="ul44442512"></a><a name="ul44442512"></a><ul id="ul44442512"><li><strong id="b43073743"><a name="b43073743"></a><a name="b43073743"></a>dcs.single_node</strong>: indicates a DCS instance in single-node mode.</li><li><strong id="b66421154"><a name="b66421154"></a><a name="b66421154"></a>dcs.master_standby</strong>: indicates a DCS instance in master/standby mode.</li><li><strong id="b11404402"><a name="b11404402"></a><a name="b11404402"></a>dcs.cluster</strong>: indicates a DCS instance in cluster mode.</li></ul>
</td>
</tr>
<tr id="row35530756"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p59418969"><a name="p59418969"></a><a name="p59418969"></a>engine_version</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p48207199"><a name="p48207199"></a><a name="p48207199"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p12469053"><a name="p12469053"></a><a name="p12469053"></a>Cache engine version.</p>
</td>
</tr>
<tr id="row45112621"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p30243716"><a name="p30243716"></a><a name="p30243716"></a>internal_version</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p33821894"><a name="p33821894"></a><a name="p33821894"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p55218909"><a name="p55218909"></a><a name="p55218909"></a>Internal DCS version.</p>
</td>
</tr>
<tr id="row27208140"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p56375741"><a name="p56375741"></a><a name="p56375741"></a>charging_mode</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p3032310"><a name="p3032310"></a><a name="p3032310"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p44290592"><a name="p44290592"></a><a name="p44290592"></a>Billing mode.</p>
<p id="p63071015"><a name="p63071015"></a><a name="p63071015"></a><strong id="b30768227"><a name="b30768227"></a><a name="b30768227"></a>0</strong> indicates that users only pay for what they use.</p>
</td>
</tr>
<tr id="row8478589"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p15677079"><a name="p15677079"></a><a name="p15677079"></a>capacity_minor</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p61883869"><a name="p61883869"></a><a name="p61883869"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p46537529"><a name="p46537529"></a><a name="p46537529"></a>Small-scale cache capacity. Unit: GB.</p>
</td>
</tr>
<tr id="row16184577"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p35882390"><a name="p35882390"></a><a name="p35882390"></a>vpc_id</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p20792500"><a name="p20792500"></a><a name="p20792500"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p6470914"><a name="p6470914"></a><a name="p6470914"></a>VPC ID.</p>
</td>
</tr>
<tr id="row58238226"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p19675884"><a name="p19675884"></a><a name="p19675884"></a>vpc_name</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p50242762"><a name="p50242762"></a><a name="p50242762"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p43131925"><a name="p43131925"></a><a name="p43131925"></a>VPC name.</p>
</td>
</tr>
<tr id="row52643006"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p36225111"><a name="p36225111"></a><a name="p36225111"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p48552848"><a name="p48552848"></a><a name="p48552848"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p40466577"><a name="p40466577"></a><a name="p40466577"></a>Time at which the DCS instance is created.</p>
<p id="p28654876"><a name="p28654876"></a><a name="p28654876"></a>For example, 2017-03-31<strong id="b56567299"><a name="b56567299"></a><a name="b56567299"></a>T</strong>12:24:46.297<strong id="b39343645"><a name="b39343645"></a><a name="b39343645"></a>Z</strong>.</p>
</td>
</tr>
<tr id="row18548493"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p26032984"><a name="p26032984"></a><a name="p26032984"></a>error_code</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p28296972"><a name="p28296972"></a><a name="p28296972"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p10353359"><a name="p10353359"></a><a name="p10353359"></a>Error code returned when the DCS instance fails to be created or is in abnormal status.</p>
<p id="p26071375"><a name="p26071375"></a><a name="p26071375"></a>For details about error codes, see <a href="querying-a-dcs-instance.md#table45484537">Table 3</a>.</p>
</td>
</tr>
<tr id="row31406639"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p60909811"><a name="p60909811"></a><a name="p60909811"></a>user_id</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p34747652"><a name="p34747652"></a><a name="p34747652"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p63096393"><a name="p63096393"></a><a name="p63096393"></a>User ID.</p>
</td>
</tr>
<tr id="row30996626"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p27698817"><a name="p27698817"></a><a name="p27698817"></a>user_name</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p29011737"><a name="p29011737"></a><a name="p29011737"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p1140481"><a name="p1140481"></a><a name="p1140481"></a>Username.</p>
</td>
</tr>
<tr id="row10264330"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p26104430"><a name="p26104430"></a><a name="p26104430"></a>maintain_begin</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p34084086"><a name="p34084086"></a><a name="p34084086"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p9347595"><a name="p9347595"></a><a name="p9347595"></a>Time at which the maintenance time window starts.</p>
<p id="p17019493"><a name="p17019493"></a><a name="p17019493"></a>Format: HH:mm:ss.</p>
</td>
</tr>
<tr id="row18957716"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p59180026"><a name="p59180026"></a><a name="p59180026"></a>maintain_end</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p28852772"><a name="p28852772"></a><a name="p28852772"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p55373178"><a name="p55373178"></a><a name="p55373178"></a>Time at which the maintenance time window ends.</p>
<p id="p28596562"><a name="p28596562"></a><a name="p28596562"></a>Format: HH:mm:ss.</p>
</td>
</tr>
<tr id="row56042470"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p43146189"><a name="p43146189"></a><a name="p43146189"></a>no_password_access</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p5180441"><a name="p5180441"></a><a name="p5180441"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p16962610"><a name="p16962610"></a><a name="p16962610"></a>An indicator of whether a DCS instance can be accessed in password-free mode.</p>
<a name="ul18445767"></a><a name="ul18445767"></a><ul id="ul18445767"><li><strong id="b17712125"><a name="b17712125"></a><a name="b17712125"></a>true</strong>: indicates that a DCS instance can be accessed without a password.</li><li><strong id="b25396020"><a name="b25396020"></a><a name="b25396020"></a>false</strong>: indicates that a DCS instance can be accessed only after password authentication.</li></ul>
</td>
</tr>
<tr id="row27237591"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p58761266"><a name="p58761266"></a><a name="p58761266"></a>access_user</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p62042081"><a name="p62042081"></a><a name="p62042081"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p59352653"><a name="p59352653"></a><a name="p59352653"></a>Username used for accessing a DCS instance after password authentication.</p>
</td>
</tr>
<tr id="row64411829"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p49975622"><a name="p49975622"></a><a name="p49975622"></a>enable_publicip</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p21493576"><a name="p21493576"></a><a name="p21493576"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p63258082"><a name="p63258082"></a><a name="p63258082"></a>An indicator of whether public access is enabled for a DCS Redis instance.</p>
<a name="ul32451832"></a><a name="ul32451832"></a><ul id="ul32451832"><li><strong id="b11352746"><a name="b11352746"></a><a name="b11352746"></a>true</strong>: enabled.</li><li><strong id="b47157257"><a name="b47157257"></a><a name="b47157257"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row21762132"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p17902305"><a name="p17902305"></a><a name="p17902305"></a>publicip_id</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p40800590"><a name="p40800590"></a><a name="p40800590"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p16513475"><a name="p16513475"></a><a name="p16513475"></a>ID of the elastic IP address bound to a DCS Redis instance.</p>
<p id="p14403553"><a name="p14403553"></a><a name="p14403553"></a>The parameter value is <strong id="b62523113"><a name="b62523113"></a><a name="b62523113"></a>null</strong> if public access is disabled.</p>
</td>
</tr>
<tr id="row25837110"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p12431143"><a name="p12431143"></a><a name="p12431143"></a>publicip_address</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p289694"><a name="p289694"></a><a name="p289694"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p23465216"><a name="p23465216"></a><a name="p23465216"></a>Elastic IP address bound to a DCS Redis instance.</p>
<p id="p9860358"><a name="p9860358"></a><a name="p9860358"></a>The parameter value is <strong id="b21634359"><a name="b21634359"></a><a name="b21634359"></a>null</strong> if public access is disabled.</p>
</td>
</tr>
<tr id="row60491510"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p865287"><a name="p865287"></a><a name="p865287"></a>enable_ssl</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p2979424"><a name="p2979424"></a><a name="p2979424"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p40006826"><a name="p40006826"></a><a name="p40006826"></a>An indicator of whether to enable SSL for public access to a DCS Redis instance.</p>
<a name="ul24517121"></a><a name="ul24517121"></a><ul id="ul24517121"><li><strong id="b39729783"><a name="b39729783"></a><a name="b39729783"></a>true</strong>: enabled.</li><li><strong id="b63995825"><a name="b63995825"></a><a name="b63995825"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row39091515"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p12296151"><a name="p12296151"></a><a name="p12296151"></a>service_upgrade</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p56464171"><a name="p56464171"></a><a name="p56464171"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p10195168"><a name="p10195168"></a><a name="p10195168"></a>An indicator of whether an upgrade task has been created for a DCS instance.</p>
<a name="ul24647654"></a><a name="ul24647654"></a><ul id="ul24647654"><li><strong id="b50302991"><a name="b50302991"></a><a name="b50302991"></a>true</strong>: yes.</li><li><strong id="b48010476"><a name="b48010476"></a><a name="b48010476"></a>false</strong>: no.</li></ul>
</td>
</tr>
<tr id="row29441106"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p35919385"><a name="p35919385"></a><a name="p35919385"></a>service_task_id</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p23789064"><a name="p23789064"></a><a name="p23789064"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p47866056"><a name="p47866056"></a><a name="p47866056"></a>Upgrade task ID.</p>
<a name="ul28141326"></a><a name="ul28141326"></a><ul id="ul28141326"><li>If the value of <strong id="b64854922"><a name="b64854922"></a><a name="b64854922"></a>service_upgrade</strong> is set to <strong id="b46823386"><a name="b46823386"></a><a name="b46823386"></a>true</strong>, the value of this parameter is the ID of the upgrade task.</li><li>If the value of <strong id="b34597883"><a name="b34597883"></a><a name="b34597883"></a>service_upgrade</strong> is set to <strong id="b42945494"><a name="b42945494"></a><a name="b42945494"></a>false</strong>, the value of this parameter is empty.</li></ul>
</td>
</tr>
</tbody>
</table>

-   Example response:

    ```
    { 
     "instances": [ 
            { 
                "name": "dcs-single-test-1", 
                "engine": "Redis", 
                "capacity": 2, 
                "ip": "192.168.0.82", 
                "port": 6379, 
                "status": "RUNNING", 
                "max_memory": 1536, 
                "used_memory": 1, 
                "instance_id": "12073516-dab2-40a8-a285-4c5da07891ae", 
                "resource_spec_code": "dcs.single_node", 
                "engine_version": "3.0.7", 
                "internal_version": null, 
                "charging_mode": 0, 
                "capacity_minor": null, 
                "vpc_id": "f963ebe1-0346-4ab6-ad35-4d56154fb4ab", 
                "vpc_name": "vpc-weihuazu", 
                "created_at": "2019-05-31T03:15:40.631Z", 
                "error_code": null, 
                "user_id": "d53977d1adfb49c5b025ba7d33a13fd7", 
                "user_name": "paas_dcs_a00421997_02", 
                "maintain_begin": "02:00:00", 
                "maintain_end": "06:00:00", 
                "no_password_access": "false", 
                "access_user": null, 
                "enable_publicip": false, 
                "publicip_id": null, 
                "publicip_address": null, 
                "enable_ssl": false, 
                "service_upgrade": false, 
                "service_task_id": "" 
            } 
     ], 
     "instance_num": 1 
    }
    ```


