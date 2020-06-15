# Querying DeHs<a name="EN-US_TOPIC_0087389316"></a>

## Function<a name="section7659482"></a>

This API is used to query the DeH list.

## URI<a name="section1826478"></a>

GET /v1.0/\{project\_id\}/dedicated-hosts

[Table 1](#table572214121015)  describes the parameters.

**Table  1**  Parameters description

<a name="table572214121015"></a>
<table><thead align="left"><tr id="row572516410109"><th class="cellrowborder" valign="top" width="21.23787621237876%" id="mcps1.2.5.1.1"><p id="p107252049107"><a name="p107252049107"></a><a name="p107252049107"></a><strong id="b19178110561"><a name="b19178110561"></a><a name="b19178110561"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="23.44765523447655%" id="mcps1.2.5.1.2"><p id="p726975522919"><a name="p726975522919"></a><a name="p726975522919"></a><strong id="b11731311266"><a name="b11731311266"></a><a name="b11731311266"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="24.48755124487551%" id="mcps1.2.5.1.3"><p id="p072564201017"><a name="p072564201017"></a><a name="p072564201017"></a><strong id="b17785141967"><a name="b17785141967"></a><a name="b17785141967"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="30.826917308269174%" id="mcps1.2.5.1.4"><p id="p47253421017"><a name="p47253421017"></a><a name="p47253421017"></a><strong id="b472831512610"><a name="b472831512610"></a><a name="b472831512610"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row107256481017"><td class="cellrowborder" valign="top" width="21.23787621237876%" headers="mcps1.2.5.1.1 "><p id="p1872514451016"><a name="p1872514451016"></a><a name="p1872514451016"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="23.44765523447655%" headers="mcps1.2.5.1.2 "><p id="p12269175511291"><a name="p12269175511291"></a><a name="p12269175511291"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="24.48755124487551%" headers="mcps1.2.5.1.3 "><p id="p147251646108"><a name="p147251646108"></a><a name="p147251646108"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.4 "><p id="p6725747104"><a name="p6725747104"></a><a name="p6725747104"></a>Specifies the project ID.</p>
<p id="p7376194915119"><a name="p7376194915119"></a><a name="p7376194915119"></a>For details about how to obtain the project ID, see <a href="https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328009.html" target="_blank" rel="noopener noreferrer">Obtaining Required Information</a>.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section56434525"></a>

-   Request parameters

    You can add parameters  **host\_type**,  **host\_type\_name**,  **flavor**,  **dedicated\_host\_id**,  **state**,  **tenant**,  **availability\_zone**,  **name**,  **limit**,  **marker**,  **tags**,  **instance\_uuid**,  **released\_at**, or  **changes-since**  to the URI to filter the search result, 

    for example,  **/v1.0/\{project\_id\}/dedicated-hosts?host\_type=\{host\_type\}&state=\{state\}**.

    <a name="table64553311"></a>
    <table><thead align="left"><tr id="row66070243"><th class="cellrowborder" valign="top" width="16%" id="mcps1.1.6.1.1"><p id="p34232944"><a name="p34232944"></a><a name="p34232944"></a><strong id="b107181121203115"><a name="b107181121203115"></a><a name="b107181121203115"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="13%" id="mcps1.1.6.1.2"><p id="p21405046"><a name="p21405046"></a><a name="p21405046"></a><strong id="b183360231313"><a name="b183360231313"></a><a name="b183360231313"></a>In</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="13%" id="mcps1.1.6.1.3"><p id="p56087165"><a name="p56087165"></a><a name="p56087165"></a><strong id="b12197266312"><a name="b12197266312"></a><a name="b12197266312"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17%" id="mcps1.1.6.1.4"><p id="p46766508"><a name="p46766508"></a><a name="p46766508"></a><strong id="b0572154053212"><a name="b0572154053212"></a><a name="b0572154053212"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="41%" id="mcps1.1.6.1.5"><p id="p29990828"><a name="p29990828"></a><a name="p29990828"></a><strong id="b871013415329"><a name="b871013415329"></a><a name="b871013415329"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row27788708"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.6.1.1 "><p id="p36292894"><a name="p36292894"></a><a name="p36292894"></a>dedicated_host_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.2 "><p id="p54043292"><a name="p54043292"></a><a name="p54043292"></a>query</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.3 "><p id="p15430535"><a name="p15430535"></a><a name="p15430535"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.6.1.4 "><p id="p41913798"><a name="p41913798"></a><a name="p41913798"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="41%" headers="mcps1.1.6.1.5 "><p id="p39574466"><a name="p39574466"></a><a name="p39574466"></a>Specifies the DeH ID.</p>
    </td>
    </tr>
    <tr id="row20625874"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.6.1.1 "><p id="p60083059"><a name="p60083059"></a><a name="p60083059"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.2 "><p id="p34889605"><a name="p34889605"></a><a name="p34889605"></a>query</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.3 "><p id="p7485743"><a name="p7485743"></a><a name="p7485743"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.6.1.4 "><p id="p2365466"><a name="p2365466"></a><a name="p2365466"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="41%" headers="mcps1.1.6.1.5 "><p id="p57385070"><a name="p57385070"></a><a name="p57385070"></a>Specifies the DeH name.</p>
    </td>
    </tr>
    <tr id="row46703582"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.6.1.1 "><p id="p24893793"><a name="p24893793"></a><a name="p24893793"></a>host_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.2 "><p id="p3131361"><a name="p3131361"></a><a name="p3131361"></a>query</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.3 "><p id="p52313669"><a name="p52313669"></a><a name="p52313669"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.6.1.4 "><p id="p9548790"><a name="p9548790"></a><a name="p9548790"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="41%" headers="mcps1.1.6.1.5 "><p id="p35254491"><a name="p35254491"></a><a name="p35254491"></a>Specifies the DeH type.</p>
    </td>
    </tr>
    <tr id="row48854964"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.6.1.1 "><p id="p64938051"><a name="p64938051"></a><a name="p64938051"></a>host_type_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.2 "><p id="p25490811"><a name="p25490811"></a><a name="p25490811"></a>query</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.3 "><p id="p51489795"><a name="p51489795"></a><a name="p51489795"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.6.1.4 "><p id="p9923843"><a name="p9923843"></a><a name="p9923843"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="41%" headers="mcps1.1.6.1.5 "><p id="p65633828"><a name="p65633828"></a><a name="p65633828"></a>Specifies the name of the DeH type.</p>
    </td>
    </tr>
    <tr id="row53833544"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.6.1.1 "><p id="p65549821"><a name="p65549821"></a><a name="p65549821"></a>flavor</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.2 "><p id="p7935270"><a name="p7935270"></a><a name="p7935270"></a>query</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.3 "><p id="p38777132"><a name="p38777132"></a><a name="p38777132"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.6.1.4 "><p id="p53939958"><a name="p53939958"></a><a name="p53939958"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="41%" headers="mcps1.1.6.1.5 "><p id="p7060460"><a name="p7060460"></a><a name="p7060460"></a>Specifies the flavor ID.</p>
    </td>
    </tr>
    <tr id="row63544148"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.6.1.1 "><p id="p46802360"><a name="p46802360"></a><a name="p46802360"></a>state</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.2 "><p id="p32894845"><a name="p32894845"></a><a name="p32894845"></a>query</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.3 "><p id="p47236811"><a name="p47236811"></a><a name="p47236811"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.6.1.4 "><p id="p976457"><a name="p976457"></a><a name="p976457"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="41%" headers="mcps1.1.6.1.5 "><p id="OLE_LINK108"><a name="OLE_LINK108"></a><a name="OLE_LINK108"></a>Specifies the DeH status.</p>
    <p id="p40748571"><a name="p40748571"></a><a name="p40748571"></a>The value can be <strong id="b14028407345"><a name="b14028407345"></a><a name="b14028407345"></a>available</strong>, <strong id="b1353944212349"><a name="b1353944212349"></a><a name="b1353944212349"></a>fault</strong>, or <strong id="b3528194483410"><a name="b3528194483410"></a><a name="b3528194483410"></a>released</strong>.</p>
    </td>
    </tr>
    <tr id="row56771492"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.6.1.1 "><p id="p35088115"><a name="p35088115"></a><a name="p35088115"></a>tenant</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.2 "><p id="p23565055"><a name="p23565055"></a><a name="p23565055"></a>query</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.3 "><p id="p29721263"><a name="p29721263"></a><a name="p29721263"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.6.1.4 "><p id="p58612075"><a name="p58612075"></a><a name="p58612075"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="41%" headers="mcps1.1.6.1.5 "><p id="p49957660"><a name="p49957660"></a><a name="p49957660"></a>The value can be a tenant ID or <strong id="b178511162357"><a name="b178511162357"></a><a name="b178511162357"></a>all</strong>.</p>
    <p id="p46130559"><a name="p46130559"></a><a name="p46130559"></a>Only the administrator can specify this parameter.</p>
    </td>
    </tr>
    <tr id="row12521852"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.6.1.1 "><p id="p7637115"><a name="p7637115"></a><a name="p7637115"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.2 "><p id="p14626574"><a name="p14626574"></a><a name="p14626574"></a>query</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.3 "><p id="p43901854"><a name="p43901854"></a><a name="p43901854"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.6.1.4 "><p id="p66389266"><a name="p66389266"></a><a name="p66389266"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="41%" headers="mcps1.1.6.1.5 "><p id="p8821459"><a name="p8821459"></a><a name="p8821459"></a>Specifies the AZ to which the DeH belongs.</p>
    </td>
    </tr>
    <tr id="row12284267"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.6.1.1 "><p id="p55501577"><a name="p55501577"></a><a name="p55501577"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.2 "><p id="p66442792"><a name="p66442792"></a><a name="p66442792"></a>query</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.3 "><p id="p13157104"><a name="p13157104"></a><a name="p13157104"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.6.1.4 "><p id="p59092488"><a name="p59092488"></a><a name="p59092488"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="41%" headers="mcps1.1.6.1.5 "><p id="OLE_LINK48"><a name="OLE_LINK48"></a><a name="OLE_LINK48"></a>Specifies the number of records displayed per page.</p>
    </td>
    </tr>
    <tr id="row61642077"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.6.1.1 "><p id="p26952341"><a name="p26952341"></a><a name="p26952341"></a>marker</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.2 "><p id="p35656026"><a name="p35656026"></a><a name="p35656026"></a>query</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.3 "><p id="p2456979"><a name="p2456979"></a><a name="p2456979"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.6.1.4 "><p id="p64797609"><a name="p64797609"></a><a name="p64797609"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="41%" headers="mcps1.1.6.1.5 "><p id="p14114947"><a name="p14114947"></a><a name="p14114947"></a>Specifies the ID of the last record on the previous page. If the <strong id="b262311553354"><a name="b262311553354"></a><a name="b262311553354"></a>marker</strong> value is invalid, status code 400 is returned.</p>
    </td>
    </tr>
    <tr id="row2797283145"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.6.1.1 "><p id="p1080102821419"><a name="p1080102821419"></a><a name="p1080102821419"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.2 "><p id="p1986024331412"><a name="p1986024331412"></a><a name="p1986024331412"></a>query</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.3 "><p id="p8123114713148"><a name="p8123114713148"></a><a name="p8123114713148"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.6.1.4 "><p id="p496735014140"><a name="p496735014140"></a><a name="p496735014140"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="41%" headers="mcps1.1.6.1.5 "><p id="p168012812142"><a name="p168012812142"></a><a name="p168012812142"></a>Specifies the DeH tags.</p>
    </td>
    </tr>
    <tr id="row123401713157"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.6.1.1 "><p id="p876415012165"><a name="p876415012165"></a><a name="p876415012165"></a>instance_uuid</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.2 "><p id="p334011191518"><a name="p334011191518"></a><a name="p334011191518"></a>query</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.3 "><p id="p934017113151"><a name="p934017113151"></a><a name="p934017113151"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.6.1.4 "><p id="p16952102715157"><a name="p16952102715157"></a><a name="p16952102715157"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="41%" headers="mcps1.1.6.1.5 "><p id="p193407116156"><a name="p193407116156"></a><a name="p193407116156"></a>Specifies the ID of the ECS on the DeH.</p>
    </td>
    </tr>
    <tr id="row12995615131612"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.6.1.1 "><p id="p5996161513169"><a name="p5996161513169"></a><a name="p5996161513169"></a>released_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.2 "><p id="p13122142911614"><a name="p13122142911614"></a><a name="p13122142911614"></a>query</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.3 "><p id="p13375173216165"><a name="p13375173216165"></a><a name="p13375173216165"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.6.1.4 "><p id="p15692123510165"><a name="p15692123510165"></a><a name="p15692123510165"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="41%" headers="mcps1.1.6.1.5 "><p id="p39963155166"><a name="p39963155166"></a><a name="p39963155166"></a>Specifies the time when the DeH is released.</p>
    </td>
    </tr>
    <tr id="row2460041"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.6.1.1 "><p id="p65045669"><a name="p65045669"></a><a name="p65045669"></a>changes-since</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.2 "><p id="p34207804"><a name="p34207804"></a><a name="p34207804"></a>query</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.3 "><p id="p19368760"><a name="p19368760"></a><a name="p19368760"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.6.1.4 "><p id="p25365761"><a name="p25365761"></a><a name="p25365761"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="41%" headers="mcps1.1.6.1.5 "><p id="p41360766"><a name="p41360766"></a><a name="p41360766"></a>Filters the response by date and timestamp when the DeH status changes. To help keep track of changes, this parameter may also display recently deleted DeHs.</p>
    <p id="p61887768"><a name="p61887768"></a><a name="p61887768"></a>The format of the date and timestamp is ISO 8601:</p>
    <pre class="screen" id="screen65181839195018"><a name="screen65181839195018"></a><a name="screen65181839195018"></a>CCYY-MM-DDThh:mm:ss&plusmn;hh:mm</pre>
    <p id="p37021121"><a name="p37021121"></a><a name="p37021121"></a>If the <strong id="b149981536172319"><a name="b149981536172319"></a><a name="b149981536172319"></a>hh:mm</strong> value is included, the time zone is returned as the UTC offset, for example, <strong id="b1337186162410"><a name="b1337186162410"></a><a name="b1337186162410"></a>2015-08-27T09:49:58-05:00</strong>. If you omit the time zone, the UTC time zone is assumed.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    GET https://{Endpoint}/v1.0/9c53a566cb3443ab910cf0daebca90c4/dedicated-hosts?state=available
    ```


## Response<a name="section38148684"></a>

-   Response parameters

    <a name="table28597308"></a>
    <table><thead align="left"><tr id="row33757095"><th class="cellrowborder" valign="top" width="19.52%" id="mcps1.1.5.1.1"><p id="p49970185"><a name="p49970185"></a><a name="p49970185"></a><strong id="b1086017543347"><a name="b1086017543347"></a><a name="b1086017543347"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.27%" id="mcps1.1.5.1.2"><p id="p21053208"><a name="p21053208"></a><a name="p21053208"></a><strong id="b15244562349"><a name="b15244562349"></a><a name="b15244562349"></a>In</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.78%" id="mcps1.1.5.1.3"><p id="p27588283"><a name="p27588283"></a><a name="p27588283"></a><strong id="b38174570340"><a name="b38174570340"></a><a name="b38174570340"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="42.43%" id="mcps1.1.5.1.4"><p id="p14122463"><a name="p14122463"></a><a name="p14122463"></a><strong id="b68691358153414"><a name="b68691358153414"></a><a name="b68691358153414"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row59993306"><td class="cellrowborder" valign="top" width="19.52%" headers="mcps1.1.5.1.1 "><p id="p27619632"><a name="p27619632"></a><a name="p27619632"></a>dedicated_hosts</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.27%" headers="mcps1.1.5.1.2 "><p id="p22597726"><a name="p22597726"></a><a name="p22597726"></a>body</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.78%" headers="mcps1.1.5.1.3 "><p id="p178961686344"><a name="p178961686344"></a><a name="p178961686344"></a>Array of objects</p>
    <p id="p18476557"><a name="p18476557"></a><a name="p18476557"></a>For details, see <a href="object-models.md#dedicated_host">Table 1</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.43%" headers="mcps1.1.5.1.4 "><p id="p33464950"><a name="p33464950"></a><a name="p33464950"></a>Specifies the DeHs that meet the search criteria.</p>
    </td>
    </tr>
    <tr id="row32749101"><td class="cellrowborder" valign="top" width="19.52%" headers="mcps1.1.5.1.1 "><p id="p35431534"><a name="p35431534"></a><a name="p35431534"></a>total</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.27%" headers="mcps1.1.5.1.2 "><p id="p51382007"><a name="p51382007"></a><a name="p51382007"></a>body</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.78%" headers="mcps1.1.5.1.3 "><p id="p1193073"><a name="p1193073"></a><a name="p1193073"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.43%" headers="mcps1.1.5.1.4 "><p id="OLE_LINK50"><a name="OLE_LINK50"></a><a name="OLE_LINK50"></a>Specifies the quantity of DeHs that meet the search criteria.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "dedicated_hosts": [
            {
                "dedicated_host_id": "ab910cf0daebca90c4001",
                "name": "high performance servers1",
                "auto_placement": "off",
                "availability_zone": "az1",
                "host_properties": {
                    "vcpus": 36,
                    "cores": 12,
                    "sockets": 2,
                    "memory": 1073741824,
                    "host_type": "h1",
                    "host_type_name": "High performance",
                    "available_instance_capacities": [
                        {
                            "flavor": "h1.large"
                        },
                        {
                            "flavor": "h1.2large"
                        },
                        {
                            "flavor": "h1.4large"
                        },
                        {
                            "flavor": "h1.8large"
                        }
                    ]
                },
                "state": "available",
                "project_id": "9c53a566cb3443ab910cf0daebca90c4",
                "available_vcpus": 20,
                "available_memory": 1073201821,
                "instance_total": 2,
                "allocated_at": "2016-10-10T14:35:47Z",
                "released_at": null
                },
            {
                "dedicated_host_id": "ab910cf0daebca90c4002",
                "name": "high performance servers2",
                "auto_placement": "off",
                "availability_zone": "az1",
                "host_properties": {
                    "vcpus": 36,
                    "cores": 12,
                    "sockets": 2,
                    "host_type": "h1",
                    "host_type_name": "High performance",
                    "memory": 1073741824,
                    "available_instance_capacities": [
                        {
                            "flavor": "h1.large"
                        },
                        {
                            "flavor": "h1.2large"
                        },
                        {
                            "flavor": "h1.4large"
                        },
                        {
                            "flavor": "h1.8large"
                        }
                    ]
                },
                "state": "available",
                "project_id": "9c53a566cb3443ab910cf0daebca90c4",
                "available_vcpus": 20,
                "available_memory": 1073101821,
                "instance_total": 3,
                "allocated_at": "2016-10-10T14:35:47Z",
                "released_at": null
                },
            ...
        ],
        "total": 25
    }
    ```


## Status Code<a name="section27321283"></a>

See  [Status Codes](status-codes.md).

