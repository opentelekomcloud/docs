# Querying Backend ECSs<a name="EN-US_TOPIC_0096561519"></a>

## Function<a name="en-us_topic_0020100172_section1286929"></a>

This API is used to query backend ECSs added to a listener. If you are an administrator tenant, the backend ECS list will be empty.

## URI<a name="en-us_topic_0020100172_section11582368"></a>

GET /v1.0/\{project\_id\}/elbaas/listeners/\{listener\_id\}/members?limit=10&marker=0

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>Enter a question mark \(?\) and an ampersand \(&\) at the end of the URI to define multiple search criteria. This interface supports backend ECS filtering by each parameter in the response message except  **listeners**,  **server\_name**,  **update\_time**, and  **create\_time**.  

**Table  1**  Parameter description

<a name="en-us_topic_0020100172_table53268321"></a>
<table><thead align="left"><tr id="en-us_topic_0020100172_row35093725"><th class="cellrowborder" valign="top" width="30.826917308269174%" id="mcps1.2.5.1.1"><p id="en-us_topic_0020100172_p24019444"><a name="en-us_topic_0020100172_p24019444"></a><a name="en-us_topic_0020100172_p24019444"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20.677932206779325%" id="mcps1.2.5.1.2"><p id="en-us_topic_0020100172_p66526832"><a name="en-us_topic_0020100172_p66526832"></a><a name="en-us_topic_0020100172_p66526832"></a><strong id="b842352706192244"><a name="b842352706192244"></a><a name="b842352706192244"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.66823317668233%" id="mcps1.2.5.1.3"><p id="en-us_topic_0020100172_p56565956115952"><a name="en-us_topic_0020100172_p56565956115952"></a><a name="en-us_topic_0020100172_p56565956115952"></a><strong id="b842352706145623"><a name="b842352706145623"></a><a name="b842352706145623"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="30.826917308269174%" id="mcps1.2.5.1.4"><p id="p953301310198"><a name="p953301310198"></a><a name="p953301310198"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0020100172_row66859549115912"><td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.1 "><p id="p283081461212"><a name="p283081461212"></a><a name="p283081461212"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="20.677932206779325%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100172_p35726093115917"><a name="en-us_topic_0020100172_p35726093115917"></a><a name="en-us_topic_0020100172_p35726093115917"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.66823317668233%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100172_p17221766115952"><a name="en-us_topic_0020100172_p17221766115952"></a><a name="en-us_topic_0020100172_p17221766115952"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020100172_p8132410115917"><a name="en-us_topic_0020100172_p8132410115917"></a><a name="en-us_topic_0020100172_p8132410115917"></a>Specifies the project ID of the operator.</p>
</td>
</tr>
<tr id="en-us_topic_0020100172_row6499254"><td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100172_p56677584"><a name="en-us_topic_0020100172_p56677584"></a><a name="en-us_topic_0020100172_p56677584"></a>listener_id</p>
</td>
<td class="cellrowborder" valign="top" width="20.677932206779325%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100172_p27481582"><a name="en-us_topic_0020100172_p27481582"></a><a name="en-us_topic_0020100172_p27481582"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.66823317668233%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100172_p5310337115952"><a name="en-us_topic_0020100172_p5310337115952"></a><a name="en-us_topic_0020100172_p5310337115952"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020100172_p11415673"><a name="en-us_topic_0020100172_p11415673"></a><a name="en-us_topic_0020100172_p11415673"></a>Specifies the listener ID.</p>
</td>
</tr>
<tr id="en-us_topic_0020100172_row27442201103218"><td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100172_p45404342103218"><a name="en-us_topic_0020100172_p45404342103218"></a><a name="en-us_topic_0020100172_p45404342103218"></a>marker</p>
</td>
<td class="cellrowborder" valign="top" width="20.677932206779325%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100172_p53873055103218"><a name="en-us_topic_0020100172_p53873055103218"></a><a name="en-us_topic_0020100172_p53873055103218"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.66823317668233%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100172_p1641296103218"><a name="en-us_topic_0020100172_p1641296103218"></a><a name="en-us_topic_0020100172_p1641296103218"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020100172_p65836146103218"><a name="en-us_topic_0020100172_p65836146103218"></a><a name="en-us_topic_0020100172_p65836146103218"></a>Specifies the resource ID of pagination query. If the parameter is left blank, only resources on the first page are queried.</p>
</td>
</tr>
<tr id="en-us_topic_0020100172_row32875295103218"><td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100172_p11712914103218"><a name="en-us_topic_0020100172_p11712914103218"></a><a name="en-us_topic_0020100172_p11712914103218"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="20.677932206779325%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100172_p9221988103218"><a name="en-us_topic_0020100172_p9221988103218"></a><a name="en-us_topic_0020100172_p9221988103218"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.66823317668233%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100172_p8783587103218"><a name="en-us_topic_0020100172_p8783587103218"></a><a name="en-us_topic_0020100172_p8783587103218"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100172_ul6229064492949"></a><a name="en-us_topic_0020100172_ul6229064492949"></a><ul id="en-us_topic_0020100172_ul6229064492949"><li>Specifies the number of records on each page.</li><li>The value ranges from <strong>0</strong> to <strong>intmax</strong>.</li></ul>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0020100172_section37132456"></a>

-   Request parameters

    None


-   Example request

    None


## Response<a name="en-us_topic_0020100172_section65756648"></a>

-   Response parameters

    **Table  2**  Response parameters

    <a name="en-us_topic_0020100172_table59854931154845"></a>
    <table><thead align="left"><tr id="en-us_topic_0020100172_row31751075154845"><th class="cellrowborder" valign="top" width="27.060000000000002%" id="mcps1.2.4.1.1"><p id="en-us_topic_0020100172_p21700311154845"><a name="en-us_topic_0020100172_p21700311154845"></a><a name="en-us_topic_0020100172_p21700311154845"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="26.13%" id="mcps1.2.4.1.2"><p id="en-us_topic_0020100172_p28750707194250"><a name="en-us_topic_0020100172_p28750707194250"></a><a name="en-us_topic_0020100172_p28750707194250"></a><strong id="b1176925095"><a name="b1176925095"></a><a name="b1176925095"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="46.81%" id="mcps1.2.4.1.3"><p id="en-us_topic_0020100172_p37843220154845"><a name="en-us_topic_0020100172_p37843220154845"></a><a name="en-us_topic_0020100172_p37843220154845"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0020100172_row45401965154845"><td class="cellrowborder" valign="top" width="27.060000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100172_p53680547154845"><a name="en-us_topic_0020100172_p53680547154845"></a><a name="en-us_topic_0020100172_p53680547154845"></a>server_address</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.13%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100172_p57483260194250"><a name="en-us_topic_0020100172_p57483260194250"></a><a name="en-us_topic_0020100172_p57483260194250"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.81%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100172_p10751427154845"><a name="en-us_topic_0020100172_p10751427154845"></a><a name="en-us_topic_0020100172_p10751427154845"></a>Specifies the private IP address of the backend ECS.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100172_row6821999115139"><td class="cellrowborder" valign="top" width="27.060000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100172_p15711051115139"><a name="en-us_topic_0020100172_p15711051115139"></a><a name="en-us_topic_0020100172_p15711051115139"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.13%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100172_p29365542194250"><a name="en-us_topic_0020100172_p29365542194250"></a><a name="en-us_topic_0020100172_p29365542194250"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.81%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100172_p993492115139"><a name="en-us_topic_0020100172_p993492115139"></a><a name="en-us_topic_0020100172_p993492115139"></a>Specifies the backend ECS ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100172_row29653987154845"><td class="cellrowborder" valign="top" width="27.060000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100172_p53162743154845"><a name="en-us_topic_0020100172_p53162743154845"></a><a name="en-us_topic_0020100172_p53162743154845"></a>address</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.13%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100172_p44555222194246"><a name="en-us_topic_0020100172_p44555222194246"></a><a name="en-us_topic_0020100172_p44555222194246"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.81%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100172_p35996266154845"><a name="en-us_topic_0020100172_p35996266154845"></a><a name="en-us_topic_0020100172_p35996266154845"></a>Specifies the floating IP address assigned to the backend ECS.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100172_row55530939154845"><td class="cellrowborder" valign="top" width="27.060000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100172_p1712216154845"><a name="en-us_topic_0020100172_p1712216154845"></a><a name="en-us_topic_0020100172_p1712216154845"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.13%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100172_p52203199194246"><a name="en-us_topic_0020100172_p52203199194246"></a><a name="en-us_topic_0020100172_p52203199194246"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.81%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100172_p26673616154845"><a name="en-us_topic_0020100172_p26673616154845"></a><a name="en-us_topic_0020100172_p26673616154845"></a>Specifies the status of the backend ECS. The value can be <strong id="b84235270693852"><a name="b84235270693852"></a><a name="b84235270693852"></a>ACTIVE</strong>, <strong id="b84235270693858"><a name="b84235270693858"></a><a name="b84235270693858"></a>PENDING</strong>, or <strong id="b8423527069394"><a name="b8423527069394"></a><a name="b8423527069394"></a>ERROR</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100172_row38735956154845"><td class="cellrowborder" valign="top" width="27.060000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100172_p50604756154845"><a name="en-us_topic_0020100172_p50604756154845"></a><a name="en-us_topic_0020100172_p50604756154845"></a>health_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.13%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100172_p600688194246"><a name="en-us_topic_0020100172_p600688194246"></a><a name="en-us_topic_0020100172_p600688194246"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.81%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100172_p2648081293020"><a name="en-us_topic_0020100172_p2648081293020"></a><a name="en-us_topic_0020100172_p2648081293020"></a>Specifies the health check result. The value is <strong id="b214126053694413"><a name="b214126053694413"></a><a name="b214126053694413"></a>NORMAL</strong>, <strong id="b106173586394413"><a name="b106173586394413"></a><a name="b106173586394413"></a>ABNORMAL</strong>, or <strong id="b123077646394413"><a name="b123077646394413"></a><a name="b123077646394413"></a>UNAVAILABLE</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100172_row66347965203540"><td class="cellrowborder" valign="top" width="27.060000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100172_p20402829203550"><a name="en-us_topic_0020100172_p20402829203550"></a><a name="en-us_topic_0020100172_p20402829203550"></a>update_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.13%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100172_p42016429203550"><a name="en-us_topic_0020100172_p42016429203550"></a><a name="en-us_topic_0020100172_p42016429203550"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.81%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100172_p47887598203550"><a name="en-us_topic_0020100172_p47887598203550"></a><a name="en-us_topic_0020100172_p47887598203550"></a>Specifies the time when the backend ECS was updated.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100172_row34776893203546"><td class="cellrowborder" valign="top" width="27.060000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100172_p13450039203550"><a name="en-us_topic_0020100172_p13450039203550"></a><a name="en-us_topic_0020100172_p13450039203550"></a>create_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.13%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100172_p15711360203550"><a name="en-us_topic_0020100172_p15711360203550"></a><a name="en-us_topic_0020100172_p15711360203550"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.81%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100172_p64660646203550"><a name="en-us_topic_0020100172_p64660646203550"></a><a name="en-us_topic_0020100172_p64660646203550"></a>Specifies the time when the backend ECS was added.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100172_row34036378115335"><td class="cellrowborder" valign="top" width="27.060000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100172_p5483265115335"><a name="en-us_topic_0020100172_p5483265115335"></a><a name="en-us_topic_0020100172_p5483265115335"></a>server_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.13%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100172_p48655762194246"><a name="en-us_topic_0020100172_p48655762194246"></a><a name="en-us_topic_0020100172_p48655762194246"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.81%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100172_p5350778115335"><a name="en-us_topic_0020100172_p5350778115335"></a><a name="en-us_topic_0020100172_p5350778115335"></a>Specifies the backend ECS name.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100172_row440105211565"><td class="cellrowborder" valign="top" width="27.060000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100172_p2094092611565"><a name="en-us_topic_0020100172_p2094092611565"></a><a name="en-us_topic_0020100172_p2094092611565"></a>server_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.13%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100172_p48802636194246"><a name="en-us_topic_0020100172_p48802636194246"></a><a name="en-us_topic_0020100172_p48802636194246"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.81%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100172_p2157304311565"><a name="en-us_topic_0020100172_p2157304311565"></a><a name="en-us_topic_0020100172_p2157304311565"></a>Specifies the backend ECS ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100172_row26882141194356"><td class="cellrowborder" valign="top" width="27.060000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100172_p50308927194359"><a name="en-us_topic_0020100172_p50308927194359"></a><a name="en-us_topic_0020100172_p50308927194359"></a>listeners</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.13%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100172_p60699463194246"><a name="en-us_topic_0020100172_p60699463194246"></a><a name="en-us_topic_0020100172_p60699463194246"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.81%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100172_p35481726194359"><a name="en-us_topic_0020100172_p35481726194359"></a><a name="en-us_topic_0020100172_p35481726194359"></a>Specifies the listener with which the backend ECS is associated.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **listeners**  parameter description

    <a name="en-us_topic_0020100172_table37021658101455"></a>
    <table><thead align="left"><tr id="en-us_topic_0020100172_row65818642101455"><th class="cellrowborder" valign="top" width="27.01%" id="mcps1.2.4.1.1"><p id="en-us_topic_0020100172_p29709814101455"><a name="en-us_topic_0020100172_p29709814101455"></a><a name="en-us_topic_0020100172_p29709814101455"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="26.43%" id="mcps1.2.4.1.2"><p id="en-us_topic_0020100172_p41951891101455"><a name="en-us_topic_0020100172_p41951891101455"></a><a name="en-us_topic_0020100172_p41951891101455"></a><strong id="b1374129164"><a name="b1374129164"></a><a name="b1374129164"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="46.56%" id="mcps1.2.4.1.3"><p id="en-us_topic_0020100172_p42659996101455"><a name="en-us_topic_0020100172_p42659996101455"></a><a name="en-us_topic_0020100172_p42659996101455"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0020100172_row32907650101455"><td class="cellrowborder" valign="top" width="27.01%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100172_p48273964101455"><a name="en-us_topic_0020100172_p48273964101455"></a><a name="en-us_topic_0020100172_p48273964101455"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.43%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100172_p38750446101455"><a name="en-us_topic_0020100172_p38750446101455"></a><a name="en-us_topic_0020100172_p38750446101455"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.56%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100172_p51778389101455"><a name="en-us_topic_0020100172_p51778389101455"></a><a name="en-us_topic_0020100172_p51778389101455"></a>Specifies the listener with which the backend ECS is associated.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    [
        {
            "server_address": "172.16.0.16",
            "id": "4ac8777333bc20777147ab160ea61baf",
            "status": "ACTIVE",
            "address": "100.64.27.96",
            "listeners": [
                {
                    "id": "65093734fb966b3d70f6af26cc63e125"
                },
                {
                    "id": "a659fe780a542e1adf204db767a021a3"
                }
            ],
            "update_time": "2015-12-28 10:35:51",
            "create_time": "2015-12-28 10:35:50",
            "server_name": null,
            "server_id": "97444148-7afb-47cc-b4a3-6e1c94d1ade4",
            "health_status": "NORMAL"
        },
        {
            "server_address": "172.16.0.15",
            "id": "d8a21f107a19d7bd1d05a1f764eb623a",
            "status": "ACTIVE",
            "address": "100.64.27.95",
            "listeners": [
                {
                    "id": "65093734fb966b3d70f6af26cc63e125"
                },
                {
                    "id": "a659fe780a542e1adf204db767a021a3"
                }
            ],
            "update_time": "2015-12-28 10:35:51",
            "create_time": "2015-12-28 10:35:50",
            "server_name": null,
            "server_id": "05b731db-d457-41dc-a824-862daba91a59",
            "health_status": "ABNORMAL"
        }
    ]
    ```


## Status Code<a name="en-us_topic_0020100172_section54938922"></a>

-   Normal

    200

-   Abnormal

    <a name="en-us_topic_0020100172_table50037276151614"></a>
    <table><thead align="left"><tr id="en-us_topic_0020100172_row49170996151614"><th class="cellrowborder" valign="top" width="11.86%" id="mcps1.1.4.1.1"><p id="en-us_topic_0020100172_p23427717151614"><a name="en-us_topic_0020100172_p23427717151614"></a><a name="en-us_topic_0020100172_p23427717151614"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="41.9%" id="mcps1.1.4.1.2"><p id="p294494192017"><a name="p294494192017"></a><a name="p294494192017"></a>Message</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.239999999999995%" id="mcps1.1.4.1.3"><p id="en-us_topic_0020100172_p18596956151614"><a name="en-us_topic_0020100172_p18596956151614"></a><a name="en-us_topic_0020100172_p18596956151614"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0020100172_row29958430151614"><td class="cellrowborder" valign="top" width="11.86%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100172_p10713781151614"><a name="en-us_topic_0020100172_p10713781151614"></a><a name="en-us_topic_0020100172_p10713781151614"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.9%" headers="mcps1.1.4.1.2 "><p id="p783315102020"><a name="p783315102020"></a><a name="p783315102020"></a>badRequest</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100172_p62509961151614"><a name="en-us_topic_0020100172_p62509961151614"></a><a name="en-us_topic_0020100172_p62509961151614"></a>Request error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100172_row25718741151614"><td class="cellrowborder" valign="top" width="11.86%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100172_p2843278151614"><a name="en-us_topic_0020100172_p2843278151614"></a><a name="en-us_topic_0020100172_p2843278151614"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.9%" headers="mcps1.1.4.1.2 "><p id="p11833125118203"><a name="p11833125118203"></a><a name="p11833125118203"></a>unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100172_p28979000151614"><a name="en-us_topic_0020100172_p28979000151614"></a><a name="en-us_topic_0020100172_p28979000151614"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100172_row59484415151614"><td class="cellrowborder" valign="top" width="11.86%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100172_p53508309151614"><a name="en-us_topic_0020100172_p53508309151614"></a><a name="en-us_topic_0020100172_p53508309151614"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.9%" headers="mcps1.1.4.1.2 "><p id="p6833155112200"><a name="p6833155112200"></a><a name="p6833155112200"></a>userDisabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100172_p39205743151614"><a name="en-us_topic_0020100172_p39205743151614"></a><a name="en-us_topic_0020100172_p39205743151614"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100172_row17307369151614"><td class="cellrowborder" valign="top" width="11.86%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100172_p59719653151614"><a name="en-us_topic_0020100172_p59719653151614"></a><a name="en-us_topic_0020100172_p59719653151614"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.9%" headers="mcps1.1.4.1.2 "><p id="p88331151192011"><a name="p88331151192011"></a><a name="p88331151192011"></a>Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100172_p5453721151614"><a name="en-us_topic_0020100172_p5453721151614"></a><a name="en-us_topic_0020100172_p5453721151614"></a>The requested page does not exist.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100172_row49083496151614"><td class="cellrowborder" valign="top" width="11.86%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100172_p16340260151614"><a name="en-us_topic_0020100172_p16340260151614"></a><a name="en-us_topic_0020100172_p16340260151614"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.9%" headers="mcps1.1.4.1.2 "><p id="p15833175119202"><a name="p15833175119202"></a><a name="p15833175119202"></a>authFault</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100172_p48492717151614"><a name="en-us_topic_0020100172_p48492717151614"></a><a name="en-us_topic_0020100172_p48492717151614"></a>System error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100172_row33781274151614"><td class="cellrowborder" valign="top" width="11.86%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100172_p51928640151614"><a name="en-us_topic_0020100172_p51928640151614"></a><a name="en-us_topic_0020100172_p51928640151614"></a>503</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.9%" headers="mcps1.1.4.1.2 "><p id="p383425152015"><a name="p383425152015"></a><a name="p383425152015"></a>serviceUnavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100172_p45470311151614"><a name="en-us_topic_0020100172_p45470311151614"></a><a name="en-us_topic_0020100172_p45470311151614"></a>The service is unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


