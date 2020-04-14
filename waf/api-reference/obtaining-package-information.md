# Obtaining Package Information<a name="EN-US_TOPIC_0193630655"></a>

## Function Description<a name="section31323448"></a>

This API is used to obtain package information of a user.

## URI<a name="section13475579"></a>

-   URI format

    GET  /v1/\{project\_id\}/waf/bundle

-   Parameter description

    **Table  1**  Path parameters

    <a name="table590614272575"></a>
    <table><thead align="left"><tr id="row1590692719576"><th class="cellrowborder" valign="top" width="23.377662233776622%" id="mcps1.2.5.1.1"><p id="p169061827105716"><a name="p169061827105716"></a><a name="p169061827105716"></a><strong id="b16868111153218"><a name="b16868111153218"></a><a name="b16868111153218"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.478052194780524%" id="mcps1.2.5.1.2"><p id="p39061127155712"><a name="p39061127155712"></a><a name="p39061127155712"></a><strong id="b991913123215"><a name="b991913123215"></a><a name="b991913123215"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.3"><p id="p6906132705711"><a name="p6906132705711"></a><a name="p6906132705711"></a><strong id="b5103161513217"><a name="b5103161513217"></a><a name="b5103161513217"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.5.1.4"><p id="p19906127145715"><a name="p19906127145715"></a><a name="p19906127145715"></a><strong id="b136261817143217"><a name="b136261817143217"></a><a name="b136261817143217"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row990610275575"><td class="cellrowborder" valign="top" width="23.377662233776622%" headers="mcps1.2.5.1.1 "><p id="p5906427155710"><a name="p5906427155710"></a><a name="p5906427155710"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.478052194780524%" headers="mcps1.2.5.1.2 "><p id="p2906202765712"><a name="p2906202765712"></a><a name="p2906202765712"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p1906112775712"><a name="p1906112775712"></a><a name="p1906112775712"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p790652765714"><a name="p790652765714"></a><a name="p790652765714"></a>Specifies the project ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section54171348"></a>

Request parameters

None

## Response<a name="section17780084"></a>

Response parameters

**Table  2**  Parameter description

<a name="table30058"></a>
<table><thead align="left"><tr id="row2435615"><th class="cellrowborder" valign="top" width="30.316968303169684%" id="mcps1.2.4.1.1"><p id="p63067149"><a name="p63067149"></a><a name="p63067149"></a><strong id="b6490135318323"><a name="b6490135318323"></a><a name="b6490135318323"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="24.787521247875212%" id="mcps1.2.4.1.2"><p id="p8165419"><a name="p8165419"></a><a name="p8165419"></a><strong id="b52914563325"><a name="b52914563325"></a><a name="b52914563325"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="44.89551044895511%" id="mcps1.2.4.1.3"><p id="p57419169"><a name="p57419169"></a><a name="p57419169"></a><strong id="b1915475719329"><a name="b1915475719329"></a><a name="b1915475719329"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row47010477"><td class="cellrowborder" valign="top" width="30.316968303169684%" headers="mcps1.2.4.1.1 "><p id="p49752283"><a name="p49752283"></a><a name="p49752283"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="24.787521247875212%" headers="mcps1.2.4.1.2 "><p id="p3403126"><a name="p3403126"></a><a name="p3403126"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="44.89551044895511%" headers="mcps1.2.4.1.3 "><p id="p7217765"><a name="p7217765"></a><a name="p7217765"></a>Specifies version information.</p>
</td>
</tr>
<tr id="row64959888"><td class="cellrowborder" valign="top" width="30.316968303169684%" headers="mcps1.2.4.1.1 "><p id="p27259545"><a name="p27259545"></a><a name="p27259545"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="24.787521247875212%" headers="mcps1.2.4.1.2 "><p id="p60539498"><a name="p60539498"></a><a name="p60539498"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.89551044895511%" headers="mcps1.2.4.1.3 "><p id="p4752300"><a name="p4752300"></a><a name="p4752300"></a>Specifies the package name.</p>
</td>
</tr>
<tr id="row42770702"><td class="cellrowborder" valign="top" width="30.316968303169684%" headers="mcps1.2.4.1.1 "><p id="p41874876"><a name="p41874876"></a><a name="p41874876"></a>options</p>
</td>
<td class="cellrowborder" valign="top" width="24.787521247875212%" headers="mcps1.2.4.1.2 "><p id="p36421806"><a name="p36421806"></a><a name="p36421806"></a><a href="#table1272813819259">Table 3</a></p>
</td>
<td class="cellrowborder" valign="top" width="44.89551044895511%" headers="mcps1.2.4.1.3 "><p id="p64485197"><a name="p64485197"></a><a name="p64485197"></a>Specifies the protection switches.</p>
</td>
</tr>
<tr id="row11655887"><td class="cellrowborder" valign="top" width="30.316968303169684%" headers="mcps1.2.4.1.1 "><p id="p4602773"><a name="p4602773"></a><a name="p4602773"></a>rule</p>
</td>
<td class="cellrowborder" valign="top" width="24.787521247875212%" headers="mcps1.2.4.1.2 "><p id="p37280369"><a name="p37280369"></a><a name="p37280369"></a><a href="#table16103191716381">Table 4</a></p>
</td>
<td class="cellrowborder" valign="top" width="44.89551044895511%" headers="mcps1.2.4.1.3 "><p id="p66919880"><a name="p66919880"></a><a name="p66919880"></a>Specifies the maximum number of rules in a policy.</p>
</td>
</tr>
<tr id="row63762611"><td class="cellrowborder" valign="top" width="30.316968303169684%" headers="mcps1.2.4.1.1 "><p id="p64497889"><a name="p64497889"></a><a name="p64497889"></a>host</p>
</td>
<td class="cellrowborder" valign="top" width="24.787521247875212%" headers="mcps1.2.4.1.2 "><p id="p56946495"><a name="p56946495"></a><a name="p56946495"></a><a href="#table951693116344">Table 5</a></p>
</td>
<td class="cellrowborder" valign="top" width="44.89551044895511%" headers="mcps1.2.4.1.3 "><p id="p49263349"><a name="p49263349"></a><a name="p49263349"></a>Specifies the maximum number of domain names in a policy.</p>
</td>
</tr>
<tr id="row14470105310144"><td class="cellrowborder" valign="top" width="30.316968303169684%" headers="mcps1.2.4.1.1 "><p id="p17472155312146"><a name="p17472155312146"></a><a name="p17472155312146"></a>other</p>
</td>
<td class="cellrowborder" valign="top" width="24.787521247875212%" headers="mcps1.2.4.1.2 "><p id="p1947255314147"><a name="p1947255314147"></a><a name="p1947255314147"></a><a href="#table027365911177">Table 6</a></p>
</td>
<td class="cellrowborder" valign="top" width="44.89551044895511%" headers="mcps1.2.4.1.3 "><p id="p1247210535142"><a name="p1247210535142"></a><a name="p1247210535142"></a>Specifies other restrictions in the package.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **options**

<a name="table1272813819259"></a>
<table><thead align="left"><tr id="row14733082258"><th class="cellrowborder" valign="top" width="33.086691330866906%" id="mcps1.2.4.1.1"><p id="p873817812512"><a name="p873817812512"></a><a name="p873817812512"></a><strong id="b499591720317"><a name="b499591720317"></a><a name="b499591720317"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.117288271172878%" id="mcps1.2.4.1.2"><p id="p137404817256"><a name="p137404817256"></a><a name="p137404817256"></a><strong id="b1123088072"><a name="b1123088072"></a><a name="b1123088072"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.4.1.3"><p id="p6742198152512"><a name="p6742198152512"></a><a name="p6742198152512"></a><strong id="b67531120113113"><a name="b67531120113113"></a><a name="b67531120113113"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1177747172812"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p1309133143019"><a name="p1309133143019"></a><a name="p1309133143019"></a>webattack</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p23102317308"><a name="p23102317308"></a><a name="p23102317308"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p931383133011"><a name="p931383133011"></a><a name="p931383133011"></a>Specifies whether Basic Web Protection is enabled.</p>
<a name="ul1531533123020"></a><a name="ul1531533123020"></a><ul id="ul1531533123020"><li><strong id="b325342614344"><a name="b325342614344"></a><a name="b325342614344"></a>true</strong>: enabled.</li><li><strong id="b842352706104143"><a name="b842352706104143"></a><a name="b842352706104143"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row1577720732819"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p1732783153010"><a name="p1732783153010"></a><a name="p1732783153010"></a>common</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p113301531193019"><a name="p113301531193019"></a><a name="p113301531193019"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p1533333123014"><a name="p1533333123014"></a><a name="p1533333123014"></a>Specifies whether General Check in Basic Web Protection is enabled.</p>
<a name="ul7286143519589"></a><a name="ul7286143519589"></a><ul id="ul7286143519589"><li><strong id="b16615165711343"><a name="b16615165711343"></a><a name="b16615165711343"></a>true</strong>: enabled.</li><li><strong id="b01500143516"><a name="b01500143516"></a><a name="b01500143516"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row8777157112811"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p534493120300"><a name="p534493120300"></a><a name="p534493120300"></a>crawler</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p5346931163011"><a name="p5346931163011"></a><a name="p5346931163011"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p53504313302"><a name="p53504313302"></a><a name="p53504313302"></a>Specifies whether the master crawler detection switch in Basic Web Protection is enabled.</p>
<a name="ul13611195016585"></a><a name="ul13611195016585"></a><ul id="ul13611195016585"><li><strong id="b4222136354"><a name="b4222136354"></a><a name="b4222136354"></a>true</strong>: enabled.</li><li><strong id="b46408149350"><a name="b46408149350"></a><a name="b46408149350"></a>false</strong>: disabled.</li></ul>
<div class="note" id="note4801149113110"><a name="note4801149113110"></a><a name="note4801149113110"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p581144914316"><a name="p581144914316"></a><a name="p581144914316"></a>If <strong id="b34721035161715"><a name="b34721035161715"></a><a name="b34721035161715"></a>crawler</strong> is <strong id="b138521338101718"><a name="b138521338101718"></a><a name="b138521338101718"></a>false</strong>, all the subswitches, <strong id="b19498729194315"><a name="b19498729194315"></a><a name="b19498729194315"></a>crawler_engine</strong>, <strong id="b731003374316"><a name="b731003374316"></a><a name="b731003374316"></a>crawler_scanner</strong>, <strong id="b1621637124317"><a name="b1621637124317"></a><a name="b1621637124317"></a>crawler_script</strong>, and <strong id="b1761554015438"><a name="b1761554015438"></a><a name="b1761554015438"></a>crawler_other</strong> are invalid.</p>
</div></div>
</td>
</tr>
<tr id="row1177515762814"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p6362131113014"><a name="p6362131113014"></a><a name="p6362131113014"></a>crawler_engine</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p336673193011"><a name="p336673193011"></a><a name="p336673193011"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p153691131113017"><a name="p153691131113017"></a><a name="p153691131113017"></a>Specifies whether the Search Engine switch in Basic Web Protection is enabled.</p>
<a name="ul65306544586"></a><a name="ul65306544586"></a><ul id="ul65306544586"><li><strong id="b188901225123512"><a name="b188901225123512"></a><a name="b188901225123512"></a>true</strong>: enabled.</li><li><strong id="b5726142616358"><a name="b5726142616358"></a><a name="b5726142616358"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row177751776289"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p93831231163015"><a name="p93831231163015"></a><a name="p93831231163015"></a>crawler_scanner</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p153871531163016"><a name="p153871531163016"></a><a name="p153871531163016"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p15390193111303"><a name="p15390193111303"></a><a name="p15390193111303"></a>Specifies whether the Scanner switch in Basic Web Protection is enabled.</p>
<a name="ul98014100599"></a><a name="ul98014100599"></a><ul id="ul98014100599"><li><strong id="b137981013123615"><a name="b137981013123615"></a><a name="b137981013123615"></a>true</strong>: enabled.</li><li><strong id="b131664012415"><a name="b131664012415"></a><a name="b131664012415"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row177577172811"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p13401231163013"><a name="p13401231163013"></a><a name="p13401231163013"></a>crawler_script</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p8404031183014"><a name="p8404031183014"></a><a name="p8404031183014"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p154071731173012"><a name="p154071731173012"></a><a name="p154071731173012"></a>Specifies whether the Script Tool switch in Basic Web Protection is enabled.</p>
<a name="ul1248751619599"></a><a name="ul1248751619599"></a><ul id="ul1248751619599"><li><strong id="b62681956144115"><a name="b62681956144115"></a><a name="b62681956144115"></a>true</strong>: enabled.</li><li><strong id="b9971205744119"><a name="b9971205744119"></a><a name="b9971205744119"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row1773576281"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p14424131193020"><a name="p14424131193020"></a><a name="p14424131193020"></a>crawler_other</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p1542943163011"><a name="p1542943163011"></a><a name="p1542943163011"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p2434203115301"><a name="p2434203115301"></a><a name="p2434203115301"></a>Specifies whether detection of other crawlers in Basic Web Protection is enabled.</p>
<a name="ul246082345914"></a><a name="ul246082345914"></a><ul id="ul246082345914"><li><strong id="b20257152384217"><a name="b20257152384217"></a><a name="b20257152384217"></a>true</strong>: enabled.</li><li><strong id="b175742510429"><a name="b175742510429"></a><a name="b175742510429"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row1177357102817"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p844733163014"><a name="p844733163014"></a><a name="p844733163014"></a>webshell</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p18449173118309"><a name="p18449173118309"></a><a name="p18449173118309"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p134531631193015"><a name="p134531631193015"></a><a name="p134531631193015"></a>Specifies whether webshell detection is enabled.</p>
<a name="ul10624333596"></a><a name="ul10624333596"></a><ul id="ul10624333596"><li><strong id="b1672614367429"><a name="b1672614367429"></a><a name="b1672614367429"></a>true</strong>: enabled.</li><li><strong id="b18367153813423"><a name="b18367153813423"></a><a name="b18367153813423"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row47721722816"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p19470173143016"><a name="p19470173143016"></a><a name="p19470173143016"></a>cc</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p7472123113305"><a name="p7472123113305"></a><a name="p7472123113305"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p10475131183010"><a name="p10475131183010"></a><a name="p10475131183010"></a>Specifies whether CC Attack Protection is enabled.</p>
<a name="ul197223825911"></a><a name="ul197223825911"></a><ul id="ul197223825911"><li><strong id="b134957573427"><a name="b134957573427"></a><a name="b134957573427"></a>true</strong>: enabled.</li><li><strong id="b19706135814214"><a name="b19706135814214"></a><a name="b19706135814214"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row1977218711283"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p12487133193013"><a name="p12487133193013"></a><a name="p12487133193013"></a>custom</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p14492931113018"><a name="p14492931113018"></a><a name="p14492931113018"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p9494331203016"><a name="p9494331203016"></a><a name="p9494331203016"></a>Specifies whether Precise Protection is enabled.</p>
<a name="ul91403452599"></a><a name="ul91403452599"></a><ul id="ul91403452599"><li><strong id="b04841674435"><a name="b04841674435"></a><a name="b04841674435"></a>true</strong>: enabled.</li><li><strong id="b17436834315"><a name="b17436834315"></a><a name="b17436834315"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row97728782819"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p1550620319308"><a name="p1550620319308"></a><a name="p1550620319308"></a>whiteblackip</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p05107316305"><a name="p05107316305"></a><a name="p05107316305"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p10513133183013"><a name="p10513133183013"></a><a name="p10513133183013"></a>Specifies whether Blacklist and Whitelist is enabled.</p>
<a name="ul1107195118596"></a><a name="ul1107195118596"></a><ul id="ul1107195118596"><li><strong id="b2046920205436"><a name="b2046920205436"></a><a name="b2046920205436"></a>true</strong>: enabled.</li><li><strong id="b5696102211434"><a name="b5696102211434"></a><a name="b5696102211434"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row10772157172818"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p752533163014"><a name="p752533163014"></a><a name="p752533163014"></a>privacy</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p175288318301"><a name="p175288318301"></a><a name="p175288318301"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p453218314302"><a name="p453218314302"></a><a name="p453218314302"></a>Specifies whether Data Masking is enabled.</p>
<a name="ul1402205735918"></a><a name="ul1402205735918"></a><ul id="ul1402205735918"><li><strong id="b126495318439"><a name="b126495318439"></a><a name="b126495318439"></a>true</strong>: enabled.</li><li><strong id="b1644141848"><a name="b1644141848"></a><a name="b1644141848"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row14770678287"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p18543163163010"><a name="p18543163163010"></a><a name="p18543163163010"></a>Ignore</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p12546103111306"><a name="p12546103111306"></a><a name="p12546103111306"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p16551731203011"><a name="p16551731203011"></a><a name="p16551731203011"></a>Specifies whether False Alarm Masking is enabled.</p>
<a name="ul1756132300"></a><a name="ul1756132300"></a><ul id="ul1756132300"><li><strong id="b112451419104518"><a name="b112451419104518"></a><a name="b112451419104518"></a>true</strong>: enabled.</li><li><strong id="b113851205458"><a name="b113851205458"></a><a name="b113851205458"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row167707717287"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p55631931163010"><a name="p55631931163010"></a><a name="p55631931163010"></a>antitamper</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p1656653112309"><a name="p1656653112309"></a><a name="p1656653112309"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p1556923113303"><a name="p1556923113303"></a><a name="p1556923113303"></a>Specifies whether Web Tamper Protection is enabled.</p>
<a name="ul9103887012"></a><a name="ul9103887012"></a><ul id="ul9103887012"><li><strong id="b161121129154510"><a name="b161121129154510"></a><a name="b161121129154510"></a>true</strong>: enabled.</li><li><strong id="b6213130184514"><a name="b6213130184514"></a><a name="b6213130184514"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row2033919133325"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p1262181293212"><a name="p1262181293212"></a><a name="p1262181293212"></a>full_detection</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p865312113218"><a name="p865312113218"></a><a name="p865312113218"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p868712193215"><a name="p868712193215"></a><a name="p868712193215"></a>Specifies whether the full detection mode in Precise Protection is enabled.</p>
<a name="ul18716127326"></a><a name="ul18716127326"></a><ul id="ul18716127326"><li><strong id="en-us_topic_0193631159_b1755019491619"><a name="en-us_topic_0193631159_b1755019491619"></a><a name="en-us_topic_0193631159_b1755019491619"></a>true</strong>: full detection. Full detection finishes all threat detections before blocking requests that meet Precise Protection specified conditions.</li><li><strong id="en-us_topic_0193631159_b17686122792016"><a name="en-us_topic_0193631159_b17686122792016"></a><a name="en-us_topic_0193631159_b17686122792016"></a>false</strong>: instant detection. Instant detection immediately ends threat detection after blocking a request that meets Precise Protection specified conditions.</li></ul>
</td>
</tr>
<tr id="row10338181343213"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p1687191243212"><a name="p1687191243212"></a><a name="p1687191243212"></a>log_download</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p591512183213"><a name="p591512183213"></a><a name="p591512183213"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p1895412113214"><a name="p1895412113214"></a><a name="p1895412113214"></a>Specifies whether log download is available.</p>
<a name="ul11971912173216"></a><a name="ul11971912173216"></a><ul id="ul11971912173216"><li><strong id="b443572044716"><a name="b443572044716"></a><a name="b443572044716"></a>true</strong>: available.</li><li><strong id="b3615163018479"><a name="b3615163018479"></a><a name="b3615163018479"></a>false</strong>: unavailable.</li></ul>
</td>
</tr>
</tbody>
</table>

**Table  4** **rule**

<a name="table16103191716381"></a>
<table><thead align="left"><tr id="row412051711381"><th class="cellrowborder" valign="top" width="33.05669433056694%" id="mcps1.2.4.1.1"><p id="p112571753818"><a name="p112571753818"></a><a name="p112571753818"></a><strong id="b1438385013488"><a name="b1438385013488"></a><a name="b1438385013488"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.117288271172885%" id="mcps1.2.4.1.2"><p id="p12132217113814"><a name="p12132217113814"></a><a name="p12132217113814"></a><strong id="b1072871189"><a name="b1072871189"></a><a name="b1072871189"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.82601739826017%" id="mcps1.2.4.1.3"><p id="p11137217193810"><a name="p11137217193810"></a><a name="p11137217193810"></a><strong id="b2021917536484"><a name="b2021917536484"></a><a name="b2021917536484"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row10774162333816"><td class="cellrowborder" valign="top" width="33.05669433056694%" headers="mcps1.2.4.1.1 "><p id="p77741423163813"><a name="p77741423163813"></a><a name="p77741423163813"></a>antitamper</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172885%" headers="mcps1.2.4.1.2 "><p id="p8774122363815"><a name="p8774122363815"></a><a name="p8774122363815"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="39.82601739826017%" headers="mcps1.2.4.1.3 "><p id="p5774172303816"><a name="p5774172303816"></a><a name="p5774172303816"></a>Specifies the total number of web tamper protection rules. The maximum value is <strong id="b1658335713527"><a name="b1658335713527"></a><a name="b1658335713527"></a>100</strong>.</p>
</td>
</tr>
<tr id="row64614346386"><td class="cellrowborder" valign="top" width="33.05669433056694%" headers="mcps1.2.4.1.1 "><p id="p12294333103816"><a name="p12294333103816"></a><a name="p12294333103816"></a>cc</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172885%" headers="mcps1.2.4.1.2 "><p id="p11298143315385"><a name="p11298143315385"></a><a name="p11298143315385"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="39.82601739826017%" headers="mcps1.2.4.1.3 "><p id="p4301203393811"><a name="p4301203393811"></a><a name="p4301203393811"></a>Specifies the total number of CC attack protection rules. The maximum value is <strong id="b84235270611527"><a name="b84235270611527"></a><a name="b84235270611527"></a>100</strong>.</p>
</td>
</tr>
<tr id="row5112194115382"><td class="cellrowborder" valign="top" width="33.05669433056694%" headers="mcps1.2.4.1.1 "><p id="p94246405388"><a name="p94246405388"></a><a name="p94246405388"></a>custom</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172885%" headers="mcps1.2.4.1.2 "><p id="p124271940123816"><a name="p124271940123816"></a><a name="p124271940123816"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="39.82601739826017%" headers="mcps1.2.4.1.3 "><p id="p1543110409386"><a name="p1543110409386"></a><a name="p1543110409386"></a>Specifies the total number of precise protection rules. The maximum value is <strong id="b15769215164110"><a name="b15769215164110"></a><a name="b15769215164110"></a>100</strong>.</p>
</td>
</tr>
<tr id="row1247104343819"><td class="cellrowborder" valign="top" width="33.05669433056694%" headers="mcps1.2.4.1.1 "><p id="p198271542163817"><a name="p198271542163817"></a><a name="p198271542163817"></a>ignore</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172885%" headers="mcps1.2.4.1.2 "><p id="p198319422381"><a name="p198319422381"></a><a name="p198319422381"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="39.82601739826017%" headers="mcps1.2.4.1.3 "><p id="p1683544220389"><a name="p1683544220389"></a><a name="p1683544220389"></a>Specifies the total number of false alarm masking rules. The maximum value is <strong id="b162771647174111"><a name="b162771647174111"></a><a name="b162771647174111"></a>1000</strong>.</p>
</td>
</tr>
<tr id="row415724563812"><td class="cellrowborder" valign="top" width="33.05669433056694%" headers="mcps1.2.4.1.1 "><p id="p13549154473811"><a name="p13549154473811"></a><a name="p13549154473811"></a>privacy</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172885%" headers="mcps1.2.4.1.2 "><p id="p17553124403811"><a name="p17553124403811"></a><a name="p17553124403811"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="39.82601739826017%" headers="mcps1.2.4.1.3 "><p id="p17557944103819"><a name="p17557944103819"></a><a name="p17557944103819"></a>Specifies the total number of data masking rules. The maximum value is <strong id="b973671864213"><a name="b973671864213"></a><a name="b973671864213"></a>1000</strong>.</p>
</td>
</tr>
<tr id="row489864612384"><td class="cellrowborder" valign="top" width="33.05669433056694%" headers="mcps1.2.4.1.1 "><p id="p12295104693820"><a name="p12295104693820"></a><a name="p12295104693820"></a>whiteblackip</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172885%" headers="mcps1.2.4.1.2 "><p id="p6299746193817"><a name="p6299746193817"></a><a name="p6299746193817"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="39.82601739826017%" headers="mcps1.2.4.1.3 "><p id="p4304446103812"><a name="p4304446103812"></a><a name="p4304446103812"></a>Specifies the total number of blacklist and whitelist rules. The maximum value is <strong id="b56731952124218"><a name="b56731952124218"></a><a name="b56731952124218"></a>100</strong>.</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>Contact the administrator to increase the maximum values in  [Table 4](#table16103191716381).  

**Table  5** **host**

<a name="table951693116344"></a>
<table><thead align="left"><tr id="row18532153110346"><th class="cellrowborder" valign="top" width="33.05669433056694%" id="mcps1.2.4.1.1"><p id="p15539123133411"><a name="p15539123133411"></a><a name="p15539123133411"></a><strong id="b175951730431"><a name="b175951730431"></a><a name="b175951730431"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.14728527147285%" id="mcps1.2.4.1.2"><p id="p954443113343"><a name="p954443113343"></a><a name="p954443113343"></a><strong id="b1287620190"><a name="b1287620190"></a><a name="b1287620190"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.4.1.3"><p id="p1551123120344"><a name="p1551123120344"></a><a name="p1551123120344"></a><strong id="b13758138174318"><a name="b13758138174318"></a><a name="b13758138174318"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row104981154161"><td class="cellrowborder" valign="top" width="33.05669433056694%" headers="mcps1.2.4.1.1 "><p id="p9620105545214"><a name="p9620105545214"></a><a name="p9620105545214"></a>wildcard</p>
</td>
<td class="cellrowborder" valign="top" width="27.14728527147285%" headers="mcps1.2.4.1.2 "><p id="p26201955155218"><a name="p26201955155218"></a><a name="p26201955155218"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p062155510522"><a name="p062155510522"></a><a name="p062155510522"></a>Specifies whether a wildcard domain is supported.</p>
<a name="ul1261915521864"></a><a name="ul1261915521864"></a><ul id="ul1261915521864"><li><strong id="b10165122734319"><a name="b10165122734319"></a><a name="b10165122734319"></a>true</strong>: supported.</li><li><strong id="b190010364435"><a name="b190010364435"></a><a name="b190010364435"></a>false</strong>: unsupported.</li></ul>
</td>
</tr>
<tr id="row74963547617"><td class="cellrowborder" valign="top" width="33.05669433056694%" headers="mcps1.2.4.1.1 "><p id="p91814533618"><a name="p91814533618"></a><a name="p91814533618"></a>ports</p>
</td>
<td class="cellrowborder" valign="top" width="27.14728527147285%" headers="mcps1.2.4.1.2 "><p id="p78158351142"><a name="p78158351142"></a><a name="p78158351142"></a><a href="#table512720205117">Table 7</a></p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p0191185313613"><a name="p0191185313613"></a><a name="p0191185313613"></a>Specifies the range of ports supported.</p>
</td>
</tr>
<tr id="row04964543614"><td class="cellrowborder" valign="top" width="33.05669433056694%" headers="mcps1.2.4.1.1 "><p id="p1290716616169"><a name="p1290716616169"></a><a name="p1290716616169"></a>protocol</p>
</td>
<td class="cellrowborder" valign="top" width="27.14728527147285%" headers="mcps1.2.4.1.2 "><p id="p1845341665719"><a name="p1845341665719"></a><a name="p1845341665719"></a><a href="#table587623519166">Table 8</a></p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p321185312613"><a name="p321185312613"></a><a name="p321185312613"></a>Specifies the client protocol.</p>
</td>
</tr>
<tr id="row6495554264"><td class="cellrowborder" valign="top" width="33.05669433056694%" headers="mcps1.2.4.1.1 "><p id="p10220135311617"><a name="p10220135311617"></a><a name="p10220135311617"></a>server</p>
</td>
<td class="cellrowborder" valign="top" width="27.14728527147285%" headers="mcps1.2.4.1.2 "><p id="p12261653660"><a name="p12261653660"></a><a name="p12261653660"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p62321453769"><a name="p62321453769"></a><a name="p62321453769"></a>Specifies the number of backend servers supported. The maximum value is <strong id="b1216619120183"><a name="b1216619120183"></a><a name="b1216619120183"></a>30</strong>.</p>
</td>
</tr>
<tr id="row549535418612"><td class="cellrowborder" valign="top" width="33.05669433056694%" headers="mcps1.2.4.1.1 "><p id="p92391653264"><a name="p92391653264"></a><a name="p92391653264"></a>host</p>
</td>
<td class="cellrowborder" valign="top" width="27.14728527147285%" headers="mcps1.2.4.1.2 "><p id="p6243115314618"><a name="p6243115314618"></a><a name="p6243115314618"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p525018536619"><a name="p525018536619"></a><a name="p525018536619"></a>Specifies the number of subdomain names supported. The maximum value is <strong id="b818231341820"><a name="b818231341820"></a><a name="b818231341820"></a>100</strong>.</p>
</td>
</tr>
<tr id="row124931654765"><td class="cellrowborder" valign="top" width="33.05669433056694%" headers="mcps1.2.4.1.1 "><p id="p726045316612"><a name="p726045316612"></a><a name="p726045316612"></a>domain</p>
</td>
<td class="cellrowborder" valign="top" width="27.14728527147285%" headers="mcps1.2.4.1.2 "><p id="p202658531563"><a name="p202658531563"></a><a name="p202658531563"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p112719533611"><a name="p112719533611"></a><a name="p112719533611"></a>Specifies the number of domain names supported. The maximum value is <strong id="b1561612775"><a name="b1561612775"></a><a name="b1561612775"></a>100</strong>.</p>
</td>
</tr>
<tr id="row141471218165318"><td class="cellrowborder" valign="top" width="33.05669433056694%" headers="mcps1.2.4.1.1 "><p id="p27812174539"><a name="p27812174539"></a><a name="p27812174539"></a>cert_num</p>
</td>
<td class="cellrowborder" valign="top" width="27.14728527147285%" headers="mcps1.2.4.1.2 "><p id="p188315178539"><a name="p188315178539"></a><a name="p188315178539"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p48911178532"><a name="p48911178532"></a><a name="p48911178532"></a>Specifies the number of certificates supported. The maximum value is <strong id="b66066426434"><a name="b66066426434"></a><a name="b66066426434"></a>100</strong>.</p>
</td>
</tr>
<tr id="row1154185195310"><td class="cellrowborder" valign="top" width="33.05669433056694%" headers="mcps1.2.4.1.1 "><p id="p1161795055319"><a name="p1161795055319"></a><a name="p1161795055319"></a>policy_apply_to</p>
</td>
<td class="cellrowborder" valign="top" width="27.14728527147285%" headers="mcps1.2.4.1.2 "><p id="p56211750145310"><a name="p56211750145310"></a><a name="p56211750145310"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p19631155015314"><a name="p19631155015314"></a><a name="p19631155015314"></a>Specifies whether a policy can be applied to multiple domain names.</p>
<a name="ul9647441165118"></a><a name="ul9647441165118"></a><ul id="ul9647441165118"><li><strong id="b16535802569"><a name="b16535802569"></a><a name="b16535802569"></a>true</strong>: A policy can be applied to multiple domain names.</li><li><strong id="b134341251135719"><a name="b134341251135719"></a><a name="b134341251135719"></a>false</strong>: A policy cannot be applied to multiple domain names.</li></ul>
</td>
</tr>
<tr id="row1687413535533"><td class="cellrowborder" valign="top" width="33.05669433056694%" headers="mcps1.2.4.1.1 "><p id="p135917531533"><a name="p135917531533"></a><a name="p135917531533"></a>policy_num</p>
</td>
<td class="cellrowborder" valign="top" width="27.14728527147285%" headers="mcps1.2.4.1.2 "><p id="p106710533531"><a name="p106710533531"></a><a name="p106710533531"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p157385317533"><a name="p157385317533"></a><a name="p157385317533"></a>Specifies the number of policies supported. The maximum value is <strong id="b12825101735817"><a name="b12825101735817"></a><a name="b12825101735817"></a>5000</strong>.</p>
</td>
</tr>
</tbody>
</table>

**Table  6** **other**

<a name="table027365911177"></a>
<table><thead align="left"><tr id="row527425914179"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p3274175911172"><a name="p3274175911172"></a><a name="p3274175911172"></a><strong id="b521954718460"><a name="b521954718460"></a><a name="b521954718460"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p1127425921715"><a name="p1127425921715"></a><a name="p1127425921715"></a><strong id="b1212500948"><a name="b1212500948"></a><a name="b1212500948"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p1727475991713"><a name="p1727475991713"></a><a name="p1727475991713"></a><strong id="b32821450184611"><a name="b32821450184611"></a><a name="b32821450184611"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row132741599175"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p727445951712"><a name="p727445951712"></a><a name="p727445951712"></a>default_cc</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p627415941720"><a name="p627415941720"></a><a name="p627415941720"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p6274205971717"><a name="p6274205971717"></a><a name="p6274205971717"></a>Specifies the maximum number of requests from a web visitor in a default CC attack protection policy.</p>
</td>
</tr>
</tbody>
</table>

**Table  7** **ports**

<a name="table512720205117"></a>
<table><thead align="left"><tr id="row3152102010117"><th class="cellrowborder" valign="top" width="33.05669433056694%" id="mcps1.2.4.1.1"><p id="p15159132011117"><a name="p15159132011117"></a><a name="p15159132011117"></a><strong id="b209648476556"><a name="b209648476556"></a><a name="b209648476556"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.14728527147285%" id="mcps1.2.4.1.2"><p id="p9162152031113"><a name="p9162152031113"></a><a name="p9162152031113"></a><strong id="b1338406935"><a name="b1338406935"></a><a name="b1338406935"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.4.1.3"><p id="p1017182061116"><a name="p1017182061116"></a><a name="p1017182061116"></a><strong id="b8272193475912"><a name="b8272193475912"></a><a name="b8272193475912"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row19265152512117"><td class="cellrowborder" valign="top" width="33.05669433056694%" headers="mcps1.2.4.1.1 "><p id="p2251112411110"><a name="p2251112411110"></a><a name="p2251112411110"></a>http</p>
</td>
<td class="cellrowborder" valign="top" width="27.14728527147285%" headers="mcps1.2.4.1.2 "><p id="p1525832414114"><a name="p1525832414114"></a><a name="p1525832414114"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p11264192414119"><a name="p11264192414119"></a><a name="p11264192414119"></a>Specifies the list of HTTP ports supported.</p>
</td>
</tr>
<tr id="row2026462513116"><td class="cellrowborder" valign="top" width="33.05669433056694%" headers="mcps1.2.4.1.1 "><p id="p132735248119"><a name="p132735248119"></a><a name="p132735248119"></a>https</p>
</td>
<td class="cellrowborder" valign="top" width="27.14728527147285%" headers="mcps1.2.4.1.2 "><p id="p1628015241119"><a name="p1628015241119"></a><a name="p1628015241119"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p1628672441112"><a name="p1628672441112"></a><a name="p1628672441112"></a>Specifies the list of HTTPS ports supported.</p>
</td>
</tr>
<tr id="row185471053111111"><td class="cellrowborder" valign="top" width="33.05669433056694%" headers="mcps1.2.4.1.1 "><p id="p1054814532111"><a name="p1054814532111"></a><a name="p1054814532111"></a>max_num</p>
</td>
<td class="cellrowborder" valign="top" width="27.14728527147285%" headers="mcps1.2.4.1.2 "><p id="p155481453181116"><a name="p155481453181116"></a><a name="p155481453181116"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p16548453151110"><a name="p16548453151110"></a><a name="p16548453151110"></a>Specifies the number of ports supported.</p>
</td>
</tr>
<tr id="row0849170141213"><td class="cellrowborder" valign="top" width="33.05669433056694%" headers="mcps1.2.4.1.1 "><p id="p297885910119"><a name="p297885910119"></a><a name="p297885910119"></a>none_standard</p>
</td>
<td class="cellrowborder" valign="top" width="27.14728527147285%" headers="mcps1.2.4.1.2 "><p id="p098512591118"><a name="p098512591118"></a><a name="p098512591118"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p1989145961113"><a name="p1989145961113"></a><a name="p1989145961113"></a>Specifies whether non-standard ports are supported.</p>
<a name="ul1174514548019"></a><a name="ul1174514548019"></a><ul id="ul1174514548019"><li><strong id="b1740122511014"><a name="b1740122511014"></a><a name="b1740122511014"></a>true</strong>: Non-standard ports are supported.</li><li><strong id="b220019476018"><a name="b220019476018"></a><a name="b220019476018"></a>false</strong>: Non-standard ports are not supported.</li></ul>
</td>
</tr>
</tbody>
</table>

**Table  8** **protocol**

<a name="table587623519166"></a>
<table><thead align="left"><tr id="row1690553518164"><th class="cellrowborder" valign="top" width="33.05669433056694%" id="mcps1.2.4.1.1"><p id="p591217352161"><a name="p591217352161"></a><a name="p591217352161"></a><strong id="b13458951703"><a name="b13458951703"></a><a name="b13458951703"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.14728527147285%" id="mcps1.2.4.1.2"><p id="p1092063520163"><a name="p1092063520163"></a><a name="p1092063520163"></a><strong id="b2014352677"><a name="b2014352677"></a><a name="b2014352677"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.4.1.3"><p id="p1592573531612"><a name="p1592573531612"></a><a name="p1592573531612"></a><strong id="b862612591018"><a name="b862612591018"></a><a name="b862612591018"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row20514104119497"><td class="cellrowborder" valign="top" width="33.05669433056694%" headers="mcps1.2.4.1.1 "><p id="p17314174012495"><a name="p17314174012495"></a><a name="p17314174012495"></a>http</p>
</td>
<td class="cellrowborder" valign="top" width="27.14728527147285%" headers="mcps1.2.4.1.2 "><p id="p1232314019494"><a name="p1232314019494"></a><a name="p1232314019494"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p4332124013496"><a name="p4332124013496"></a><a name="p4332124013496"></a>Specifies whether the HTTP protocol is supported.</p>
<a name="ul917015454113"></a><a name="ul917015454113"></a><ul id="ul917015454113"><li><strong id="b2549502117"><a name="b2549502117"></a><a name="b2549502117"></a>true</strong>: The HTTP protocol is supported.</li><li><strong id="b18844952414"><a name="b18844952414"></a><a name="b18844952414"></a>false</strong>: The HTTP protocol is not supported.</li></ul>
</td>
</tr>
<tr id="row451464154913"><td class="cellrowborder" valign="top" width="33.05669433056694%" headers="mcps1.2.4.1.1 "><p id="p1534424094915"><a name="p1534424094915"></a><a name="p1534424094915"></a>https</p>
</td>
<td class="cellrowborder" valign="top" width="27.14728527147285%" headers="mcps1.2.4.1.2 "><p id="p12155171516524"><a name="p12155171516524"></a><a name="p12155171516524"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p16358840164914"><a name="p16358840164914"></a><a name="p16358840164914"></a>Specifies whether the HTTPS protocol is supported.</p>
<a name="ul337713307217"></a><a name="ul337713307217"></a><ul id="ul337713307217"><li><strong id="b1524112200317"><a name="b1524112200317"></a><a name="b1524112200317"></a>true</strong>: The HTTPS protocol is supported.</li><li><strong id="b16506122510320"><a name="b16506122510320"></a><a name="b16506122510320"></a>false</strong>: The HTTPS protocol is not supported.</li></ul>
</td>
</tr>
<tr id="row967213443496"><td class="cellrowborder" valign="top" width="33.05669433056694%" headers="mcps1.2.4.1.1 "><p id="p106381243164913"><a name="p106381243164913"></a><a name="p106381243164913"></a>http_https</p>
</td>
<td class="cellrowborder" valign="top" width="27.14728527147285%" headers="mcps1.2.4.1.2 "><p id="p1664634314499"><a name="p1664634314499"></a><a name="p1664634314499"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p78041921155211"><a name="p78041921155211"></a><a name="p78041921155211"></a>Specifies whether the HTTP and HTTPS protocols are supported.</p>
<a name="ul1321513311639"></a><a name="ul1321513311639"></a><ul id="ul1321513311639"><li><strong id="b44816948"><a name="b44816948"></a><a name="b44816948"></a>true</strong>: Both HTTP and HTTPS are supported.</li><li><strong id="b3479121216416"><a name="b3479121216416"></a><a name="b3479121216416"></a>false</strong>: Neither HTTP nor HTTPS is supported.</li></ul>
</td>
</tr>
</tbody>
</table>

## Example<a name="section331618352316"></a>

Response example

```
{
  "type": 1,
  "name": "Basic",
  "options": {
    "webattack": true,
    "common": true,
    "crawler": true,
    "webshell": false,
    "cc": false,
    "custom": false,
    "whiteblackip": true,
    
    "privacy": true,
    "ignore": true,
    "antitamper": false,
"log_download": true,
  },
  "rule": {
    "cc": 0,
    "custom": 0,
    "whiteblackip": 10,
   
    "privacy": 10,
    "ignore": 1000,
"antitamper": 0,
  },
  "host": {
    "wildcard": false,
    "protocol": {
      "http": true,
      "https": false,
      "http_https": false
    },
    "ports": {
      "none_standard": false,
      "http": [],
      "https": [],
      "max_num": 0
    },
    "domain": 1,
    "host": 10,
    "server": 10,
    "route": false
  },
  "other": {
      "default_cc": 25000
    }
}
```

## Status Code<a name="section145221785217"></a>

[Table 9](#en-us_topic_0193631139_t82c3440f3efb42a38b9d4dc4011a33d0)  describes the normal status code returned by the API.

**Table  9**  Status code

<a name="en-us_topic_0193631139_t82c3440f3efb42a38b9d4dc4011a33d0"></a>
<table><thead align="left"><tr id="en-us_topic_0193631139_r3d6e2f205c444705bdbb9daaac74e575"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.1"><p id="en-us_topic_0193631139_af3c4073076f24eca88d94e3fa1effdc6"><a name="en-us_topic_0193631139_af3c4073076f24eca88d94e3fa1effdc6"></a><a name="en-us_topic_0193631139_af3c4073076f24eca88d94e3fa1effdc6"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="19.41%" id="mcps1.2.4.1.2"><p id="en-us_topic_0193631139_en-us_topic_0144911667_p4531342288"><a name="en-us_topic_0193631139_en-us_topic_0144911667_p4531342288"></a><a name="en-us_topic_0193631139_en-us_topic_0144911667_p4531342288"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="58.589999999999996%" id="mcps1.2.4.1.3"><p id="en-us_topic_0193631139_ada185614bba24140995b8123b3e9faa8"><a name="en-us_topic_0193631139_ada185614bba24140995b8123b3e9faa8"></a><a name="en-us_topic_0193631139_ada185614bba24140995b8123b3e9faa8"></a>Meaning</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0193631139_rc7b2adc390904a1ba79e303017797786"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0193631139_a93f3895d44bb4226934cc626ac50e37b"><a name="en-us_topic_0193631139_a93f3895d44bb4226934cc626ac50e37b"></a><a name="en-us_topic_0193631139_a93f3895d44bb4226934cc626ac50e37b"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="19.41%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0193631139_en-us_topic_0144911667_p7538425819"><a name="en-us_topic_0193631139_en-us_topic_0144911667_p7538425819"></a><a name="en-us_topic_0193631139_en-us_topic_0144911667_p7538425819"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0193631139_en-us_topic_0144911667_p369874114414"><a name="en-us_topic_0193631139_en-us_topic_0144911667_p369874114414"></a><a name="en-us_topic_0193631139_en-us_topic_0144911667_p369874114414"></a>The request has succeeded.</p>
</td>
</tr>
</tbody>
</table>

For details about error status codes, see  [Status Codes](status-codes.md).

