# Obtaining a Parameter Template<a name="en-us_topic_0056890261"></a>

## Function<a name="section34190215102747"></a>

This API is used to obtain information about a specified parameter template.

## URI<a name="section27278260102747"></a>

-   URI format

    PATH: /v1.0/\{project\_id\}/configurations/\{id\}

    Method: GET

-   Parameter description

    **Table  1**  Parameter description

    <a name="table35502362102747"></a>
    <table><thead align="left"><tr id="row66354709102747"><th class="cellrowborder" valign="top" width="21.25%" id="mcps1.2.4.1.1"><p id="p6022318102747"><a name="p6022318102747"></a><a name="p6022318102747"></a><strong id="b84235270691445_1"><a name="b84235270691445_1"></a><a name="b84235270691445_1"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="29.060000000000002%" id="mcps1.2.4.1.2"><p id="p18045711102747"><a name="p18045711102747"></a><a name="p18045711102747"></a><strong id="b842352706102346_1"><a name="b842352706102346_1"></a><a name="b842352706102346_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="49.69%" id="mcps1.2.4.1.3"><p id="p52416481102747"><a name="p52416481102747"></a><a name="p52416481102747"></a><strong id="b842352706163417_1"><a name="b842352706163417_1"></a><a name="b842352706163417_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row51827069142142"><td class="cellrowborder" valign="top" width="21.25%" headers="mcps1.2.4.1.1 "><p id="p11503042145314"><a name="p11503042145314"></a><a name="p11503042145314"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.060000000000002%" headers="mcps1.2.4.1.2 "><p id="p34002696145314"><a name="p34002696145314"></a><a name="p34002696145314"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.69%" headers="mcps1.2.4.1.3 "><p id="p57786187145314"><a name="p57786187145314"></a><a name="p57786187145314"></a>Specifies the project ID of a tenant in a region.</p>
    </td>
    </tr>
    <tr id="row17876555102747"><td class="cellrowborder" valign="top" width="21.25%" headers="mcps1.2.4.1.1 "><p id="p16441776145314"><a name="p16441776145314"></a><a name="p16441776145314"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.060000000000002%" headers="mcps1.2.4.1.2 "><p id="p57953286145314"><a name="p57953286145314"></a><a name="p57953286145314"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.69%" headers="mcps1.2.4.1.3 "><p id="p37254701163522"><a name="p37254701163522"></a><a name="p37254701163522"></a>Indicates the parameter template ID.</p>
    <p id="p6051340145314"><a name="p6051340145314"></a><a name="p6051340145314"></a>When this parameter is empty (not space), the URL of the parameter template list is obtained. For details, see <a href="obtaining-a-parameter-template-list-23.md">Obtaining a Parameter Template List</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Restrictions

    Currently, the DB engines MySQL and PostgreSQL support obtaining parameter templates.


## Request<a name="section32509473102747"></a>

None

## Normal Response<a name="section9977339102747"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table30178791102747"></a>
    <table><thead align="left"><tr id="row38563839102747"><th class="cellrowborder" valign="top" width="25.509999999999998%" id="mcps1.2.4.1.1"><p id="p36663218102747"><a name="p36663218102747"></a><a name="p36663218102747"></a><strong id="b84235270691445_5"><a name="b84235270691445_5"></a><a name="b84235270691445_5"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="40.82%" id="mcps1.2.4.1.2"><p id="p16930719102747"><a name="p16930719102747"></a><a name="p16930719102747"></a><strong id="b842352706164541_1"><a name="b842352706164541_1"></a><a name="b842352706164541_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.67%" id="mcps1.2.4.1.3"><p id="p29210988102747"><a name="p29210988102747"></a><a name="p29210988102747"></a><strong id="b842352706163417_5"><a name="b842352706163417_5"></a><a name="b842352706163417_5"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row17279809102747"><td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.4.1.1 "><p id="p57487303102747"><a name="p57487303102747"></a><a name="p57487303102747"></a>configuration</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.82%" headers="mcps1.2.4.1.2 "><p id="p25959973102747"><a name="p25959973102747"></a><a name="p25959973102747"></a>List data structure. For details, see <a href="#table1092492102747">Table 3</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.67%" headers="mcps1.2.4.1.3 "><p id="p121388102747"><a name="p121388102747"></a><a name="p121388102747"></a>Indicates the parameter template.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  configuration field data structure description

    <a name="table1092492102747"></a>
    <table><thead align="left"><tr id="row59320401102747"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p40223190102747"><a name="p40223190102747"></a><a name="p40223190102747"></a><strong id="b84235270691445_7"><a name="b84235270691445_7"></a><a name="b84235270691445_7"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p36852943102747"><a name="p36852943102747"></a><a name="p36852943102747"></a><strong id="b842352706164541_3"><a name="b842352706164541_3"></a><a name="b842352706164541_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p32298405102747"><a name="p32298405102747"></a><a name="p32298405102747"></a><strong id="b842352706163417_7"><a name="b842352706163417_7"></a><a name="b842352706163417_7"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row66033983102747"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p47152389102747"><a name="p47152389102747"></a><a name="p47152389102747"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p61247201102747"><a name="p61247201102747"></a><a name="p61247201102747"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p62076216102747"><a name="p62076216102747"></a><a name="p62076216102747"></a>Indicates the parameter template ID.</p>
    </td>
    </tr>
    <tr id="row21815038102747"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p22187676102747"><a name="p22187676102747"></a><a name="p22187676102747"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p52371306102747"><a name="p52371306102747"></a><a name="p52371306102747"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p14217360102747"><a name="p14217360102747"></a><a name="p14217360102747"></a>Indicates the parameter template name.</p>
    </td>
    </tr>
    <tr id="row60847380102747"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p29690738102747"><a name="p29690738102747"></a><a name="p29690738102747"></a>datastore_version_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p56139581102747"><a name="p56139581102747"></a><a name="p56139581102747"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p51012188102747"><a name="p51012188102747"></a><a name="p51012188102747"></a>Indicates the database version ID.</p>
    </td>
    </tr>
    <tr id="row56456511102747"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p9574648102747"><a name="p9574648102747"></a><a name="p9574648102747"></a>datastore_version_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p37348985102747"><a name="p37348985102747"></a><a name="p37348985102747"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p5368939102747"><a name="p5368939102747"></a><a name="p5368939102747"></a>Indicates the database version name.</p>
    </td>
    </tr>
    <tr id="row48320453102747"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p21642659102747"><a name="p21642659102747"></a><a name="p21642659102747"></a>datastore_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p8224965102747"><a name="p8224965102747"></a><a name="p8224965102747"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p62242452102747"><a name="p62242452102747"></a><a name="p62242452102747"></a>Indicates the database name.</p>
    </td>
    </tr>
    <tr id="row23311159102747"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p9155764102747"><a name="p9155764102747"></a><a name="p9155764102747"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p3419409102747"><a name="p3419409102747"></a><a name="p3419409102747"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p8536694102747"><a name="p8536694102747"></a><a name="p8536694102747"></a>Indicates the parameter template description.</p>
    </td>
    </tr>
    <tr id="row9721388102747"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p49234929102747"><a name="p49234929102747"></a><a name="p49234929102747"></a>instance_count</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p28606290102747"><a name="p28606290102747"></a><a name="p28606290102747"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p35408185102747"><a name="p35408185102747"></a><a name="p35408185102747"></a>Indicates the number of associated DB instances.</p>
    </td>
    </tr>
    <tr id="row50238209102747"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p42763113102747"><a name="p42763113102747"></a><a name="p42763113102747"></a>created</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p41260105102747"><a name="p41260105102747"></a><a name="p41260105102747"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p53734218102747"><a name="p53734218102747"></a><a name="p53734218102747"></a>Indicates the parameter template creation time in the following format: yyyy-MM-dd THH:mm:ss.</p>
    </td>
    </tr>
    <tr id="row13845918102747"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p47777587102747"><a name="p47777587102747"></a><a name="p47777587102747"></a>updated</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p44779324102747"><a name="p44779324102747"></a><a name="p44779324102747"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p3246626102747"><a name="p3246626102747"></a><a name="p3246626102747"></a>Indicates the parameter template updated time in the following format: yyyy-MM-dd THH:mm:ss.</p>
    </td>
    </tr>
    <tr id="row29219635102747"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p17980206102747"><a name="p17980206102747"></a><a name="p17980206102747"></a>values</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p47110586102747"><a name="p47110586102747"></a><a name="p47110586102747"></a>Dictionary data structure. For details, see <a href="#table24714908102747">Table 4</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p50988021102747"><a name="p50988021102747"></a><a name="p50988021102747"></a>Indicates the parameter values defined by users based on the default parameter template.</p>
    </td>
    </tr>
    <tr id="row56239011102747"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p59066065102747"><a name="p59066065102747"></a><a name="p59066065102747"></a>parameters</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p19621935102747"><a name="p19621935102747"></a><a name="p19621935102747"></a>List data structure. For details, see <a href="#table42519518102747">Table 5</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p10202641102747"><a name="p10202641102747"></a><a name="p10202641102747"></a>Indicates the parameter list.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  values field data structure description

    <a name="table24714908102747"></a>
    <table><thead align="left"><tr id="row54465141102747"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p49600261102747"><a name="p49600261102747"></a><a name="p49600261102747"></a><strong id="b84235270691445_9"><a name="b84235270691445_9"></a><a name="b84235270691445_9"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p58198177102747"><a name="p58198177102747"></a><a name="p58198177102747"></a><strong id="b842352706164541_5"><a name="b842352706164541_5"></a><a name="b842352706164541_5"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p16431922102747"><a name="p16431922102747"></a><a name="p16431922102747"></a><strong id="b842352706163417_9"><a name="b842352706163417_9"></a><a name="b842352706163417_9"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row55917344102747"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p33011026102747"><a name="p33011026102747"></a><a name="p33011026102747"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p56647473102747"><a name="p56647473102747"></a><a name="p56647473102747"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p25042596102747"><a name="p25042596102747"></a><a name="p25042596102747"></a>Indicates the parameter name. For example, in <strong id="b84235270621563"><a name="b84235270621563"></a><a name="b84235270621563"></a>"xp_cmdshell": "0"</strong>, the key is <strong id="b842352706215241"><a name="b842352706215241"></a><a name="b842352706215241"></a>xp_cmdshell</strong>.</p>
    </td>
    </tr>
    <tr id="row24056777102747"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p2441910102747"><a name="p2441910102747"></a><a name="p2441910102747"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p63577003102747"><a name="p63577003102747"></a><a name="p63577003102747"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p49463633102747"><a name="p49463633102747"></a><a name="p49463633102747"></a>Indicates the parameter value. For example, in <strong id="b23796865222950"><a name="b23796865222950"></a><a name="b23796865222950"></a>"xp_cmdshell": "0"</strong>, the value is <strong id="b84687391422950"><a name="b84687391422950"></a><a name="b84687391422950"></a>0</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5**  parameters field data structure description

    <a name="table42519518102747"></a>
    <table><thead align="left"><tr id="row17506670102747"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p8754142102747"><a name="p8754142102747"></a><a name="p8754142102747"></a><strong id="b84235270691445_11"><a name="b84235270691445_11"></a><a name="b84235270691445_11"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p37996911102747"><a name="p37996911102747"></a><a name="p37996911102747"></a><strong id="b842352706164541_7"><a name="b842352706164541_7"></a><a name="b842352706164541_7"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p57850952102747"><a name="p57850952102747"></a><a name="p57850952102747"></a><strong id="b842352706163417_11"><a name="b842352706163417_11"></a><a name="b842352706163417_11"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row55415570102747"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p59476213102747"><a name="p59476213102747"></a><a name="p59476213102747"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p52843928102747"><a name="p52843928102747"></a><a name="p52843928102747"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p52499747102747"><a name="p52499747102747"></a><a name="p52499747102747"></a>Indicates the parameter name.</p>
    </td>
    </tr>
    <tr id="row2735679102747"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p20263483102747"><a name="p20263483102747"></a><a name="p20263483102747"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p30729394102747"><a name="p30729394102747"></a><a name="p30729394102747"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p6053006102747"><a name="p6053006102747"></a><a name="p6053006102747"></a>Indicates the value.</p>
    </td>
    </tr>
    <tr id="row54477062102747"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p50565876102747"><a name="p50565876102747"></a><a name="p50565876102747"></a>needRestart</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p2195258102747"><a name="p2195258102747"></a><a name="p2195258102747"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p55371750144011"><a name="p55371750144011"></a><a name="p55371750144011"></a>Indicates whether the DB instance needs to be rebooted.</p>
    <a name="ul22419839144020"></a><a name="ul22419839144020"></a><ul id="ul22419839144020"><li><strong id="b842352706214352_1"><a name="b842352706214352_1"></a><a name="b842352706214352_1"></a>0</strong> indicates that the DB instance does not need to be rebooted.</li><li><strong id="b84235270621449_1"><a name="b84235270621449_1"></a><a name="b84235270621449_1"></a>1</strong> indicates that the DB instance needs to be rebooted.</li></ul>
    </td>
    </tr>
    <tr id="row56839564102747"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p40601975102747"><a name="p40601975102747"></a><a name="p40601975102747"></a>readonly</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p425654102747"><a name="p425654102747"></a><a name="p425654102747"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p155410144045"><a name="p155410144045"></a><a name="p155410144045"></a>Indicates whether the parameter template is read-only.</p>
    <a name="ul29923318144055"></a><a name="ul29923318144055"></a><ul id="ul29923318144055"><li><strong id="b842352706214352_3"><a name="b842352706214352_3"></a><a name="b842352706214352_3"></a>0</strong> indicates that the parameter template is not read-only.</li><li><strong id="b84235270621449_3"><a name="b84235270621449_3"></a><a name="b84235270621449_3"></a>1</strong> indicates that the parameter template is read-only.</li></ul>
    </td>
    </tr>
    <tr id="row41866562102747"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p35748323102747"><a name="p35748323102747"></a><a name="p35748323102747"></a>valueRange</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p9933045102747"><a name="p9933045102747"></a><a name="p9933045102747"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p66379167102747"><a name="p66379167102747"></a><a name="p66379167102747"></a>Indicates the value range, such as 0-1.</p>
    </td>
    </tr>
    <tr id="row60541597102747"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p4922335102747"><a name="p4922335102747"></a><a name="p4922335102747"></a>datatype</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p63164878102747"><a name="p63164878102747"></a><a name="p63164878102747"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p16081489102747"><a name="p16081489102747"></a><a name="p16081489102747"></a>Indicates the parameter type, which can be <strong id="b317172548174558"><a name="b317172548174558"></a><a name="b317172548174558"></a>integer</strong>, <strong id="b842352706174612"><a name="b842352706174612"></a><a name="b842352706174612"></a>string</strong>, <strong id="b842352706174617"><a name="b842352706174617"></a><a name="b842352706174617"></a>boolean</strong>, <strong id="b842352706171731"><a name="b842352706171731"></a><a name="b842352706171731"></a>list</strong>, or <strong id="b842352706171734"><a name="b842352706171734"></a><a name="b842352706171734"></a>float</strong>.</p>
    </td>
    </tr>
    <tr id="row10515678102747"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p46463579102747"><a name="p46463579102747"></a><a name="p46463579102747"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p5453536102747"><a name="p5453536102747"></a><a name="p5453536102747"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p39083286102747"><a name="p39083286102747"></a><a name="p39083286102747"></a>Indicates the descriptions of parameters.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Response example

    ```
    {
      "configuration": {
        "id": "07fc12a8e0e94df7a3fcf53d0b5e1605pr01",
        "name": "default-mysql-5.6",
        "datastore_version_id": "",
        "datastore_version_name": "5.6",
        "datastore_name": "mysql",
        "description": "Default parameter group for mysql 5.6",
        "instance_count": 0,
        "created": "2017-05-05T04:40:51",
        "updated": "2017-05-05T04:40:51",
    "values": {
          "autocommit": "ON"
        },
        "parameters": [
          {
            "name": "auto_increment_increment",
            "value": "1",
            "needRestart": "0",
            "readonly": "1",
            "valueRange": "1-65535",
            "datatype": "integer",
            "description": "auto_increment_increment and auto_increment_offset are intended for use with master-to-master replication, and can be used to control the operation of AUTO_INCREMENT columns."
          },
          {
            "name": "autocommit",
            "value": "ON",
            "needRestart": "0",
            "readonly": "1",
            "valueRange": "ON|OFF",
            "datatype": "boolean",
            "description": "The autocommit mode. If set to ON, all changes to a table take effect immediately. If set to OFF, you must use COMMIT to accept a transaction or ROLLBACK to cancel it. "
          }
        ]
      }
    }
    ```


## Abnormal Response<a name="section44860981102747"></a>

For details, see  [Abnormal Request Results](abnormal-request-results.md).

