# Updating a Router<a name="vpc_router_0004"></a>

## Function<a name="section2668865720589"></a>

This API is used to update a router.

## URI<a name="section6156926920589"></a>

PUT /v2.0/routers/\{router\_id\}

## Request Message<a name="section3272152320589"></a>

**Table  1**  Request parameter

<a name="table3319773520589"></a>
<table><thead align="left"><tr id="row680247320589"><th class="cellrowborder" valign="top" width="14.44%" id="mcps1.2.5.1.1"><p id="p1412942020589"><a name="p1412942020589"></a><a name="p1412942020589"></a><strong id="b1873082515612"><a name="b1873082515612"></a><a name="b1873082515612"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="13.5%" id="mcps1.2.5.1.2"><p id="p2578437120589"><a name="p2578437120589"></a><a name="p2578437120589"></a><strong id="b1357123205610"><a name="b1357123205610"></a><a name="b1357123205610"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="10.36%" id="mcps1.2.5.1.3"><p id="p363234320589"><a name="p363234320589"></a><a name="p363234320589"></a><strong id="b15446102820561"><a name="b15446102820561"></a><a name="b15446102820561"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="61.7%" id="mcps1.2.5.1.4"><p id="p815930320589"><a name="p815930320589"></a><a name="p815930320589"></a><strong id="b1280203035618"><a name="b1280203035618"></a><a name="b1280203035618"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row5692383620589"><td class="cellrowborder" valign="top" width="14.44%" headers="mcps1.2.5.1.1 "><p id="p4742802620589"><a name="p4742802620589"></a><a name="p4742802620589"></a>router</p>
</td>
<td class="cellrowborder" valign="top" width="13.5%" headers="mcps1.2.5.1.2 "><p id="p5858622220589"><a name="p5858622220589"></a><a name="p5858622220589"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="10.36%" headers="mcps1.2.5.1.3 "><p id="p1646487220589"><a name="p1646487220589"></a><a name="p1646487220589"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="61.7%" headers="mcps1.2.5.1.4 "><p id="p63022381205744"><a name="p63022381205744"></a><a name="p63022381205744"></a>Specifies the router list. For details, see <a href="#table128801154104715">Table 2</a>.</p>
<p id="p2811868820589"><a name="p2811868820589"></a><a name="p2811868820589"></a>You must specify at least one attribute when updating a router.</p>
</td>
</tr>
</tbody>
</table>

**Table  2** **router**  objects

<a name="table128801154104715"></a>
<table><thead align="left"><tr id="row138801854134716"><th class="cellrowborder" valign="top" width="23.54%" id="mcps1.2.5.1.1"><p id="p20880145424714"><a name="p20880145424714"></a><a name="p20880145424714"></a><strong id="b1260154712588"><a name="b1260154712588"></a><a name="b1260154712588"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="11.72%" id="mcps1.2.5.1.2"><p id="p981918394815"><a name="p981918394815"></a><a name="p981918394815"></a><strong id="b460317035914"><a name="b460317035914"></a><a name="b460317035914"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.599999999999998%" id="mcps1.2.5.1.3"><p id="p5881754124714"><a name="p5881754124714"></a><a name="p5881754124714"></a><strong id="b123731816596"><a name="b123731816596"></a><a name="b123731816596"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="44.14%" id="mcps1.2.5.1.4"><p id="p10881175424718"><a name="p10881175424718"></a><a name="p10881175424718"></a><strong id="b31621322596"><a name="b31621322596"></a><a name="b31621322596"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row118821154134714"><td class="cellrowborder" valign="top" width="23.54%" headers="mcps1.2.5.1.1 "><p id="p288212543477"><a name="p288212543477"></a><a name="p288212543477"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="11.72%" headers="mcps1.2.5.1.2 "><p id="p1881923164818"><a name="p1881923164818"></a><a name="p1881923164818"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.599999999999998%" headers="mcps1.2.5.1.3 "><p id="p588205464712"><a name="p588205464712"></a><a name="p588205464712"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.14%" headers="mcps1.2.5.1.4 "><p id="p98821554104719"><a name="p98821554104719"></a><a name="p98821554104719"></a>Specifies the router name.</p>
<p id="p133126255124"><a name="p133126255124"></a><a name="p133126255124"></a>Instructions:</p>
<p id="p5882354114711"><a name="p5882354114711"></a><a name="p5882354114711"></a>The name can contain only letters, digits, underscores (_), hyphens (-), and periods (.).</p>
</td>
</tr>
<tr id="row68821454104717"><td class="cellrowborder" valign="top" width="23.54%" headers="mcps1.2.5.1.1 "><p id="p2882155464710"><a name="p2882155464710"></a><a name="p2882155464710"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="11.72%" headers="mcps1.2.5.1.2 "><p id="p9819193104813"><a name="p9819193104813"></a><a name="p9819193104813"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.599999999999998%" headers="mcps1.2.5.1.3 "><p id="p288265464716"><a name="p288265464716"></a><a name="p288265464716"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="44.14%" headers="mcps1.2.5.1.4 "><p id="p19882175411474"><a name="p19882175411474"></a><a name="p19882175411474"></a>Specifies the administrative status.</p>
<p id="p48828543474"><a name="p48828543474"></a><a name="p48828543474"></a>The value can only be <strong id="b20922162125912"><a name="b20922162125912"></a><a name="b20922162125912"></a>true</strong>.</p>
</td>
</tr>
<tr id="row17883115417475"><td class="cellrowborder" valign="top" width="23.54%" headers="mcps1.2.5.1.1 "><p id="p12883175494713"><a name="p12883175494713"></a><a name="p12883175494713"></a>external_gateway_info</p>
</td>
<td class="cellrowborder" valign="top" width="11.72%" headers="mcps1.2.5.1.2 "><p id="p1281914344820"><a name="p1281914344820"></a><a name="p1281914344820"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.599999999999998%" headers="mcps1.2.5.1.3 "><p id="p128831054134710"><a name="p128831054134710"></a><a name="p128831054134710"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="44.14%" headers="mcps1.2.5.1.4 "><p id="p6883115404715"><a name="p6883115404715"></a><a name="p6883115404715"></a>Specifies the external gateway. This is an extended attribute. For details, see the <strong id="b13739624207"><a name="b13739624207"></a><a name="b13739624207"></a>external_gateway_info</strong> objects.</p>
</td>
</tr>
<tr id="row14883145434716"><td class="cellrowborder" valign="top" width="23.54%" headers="mcps1.2.5.1.1 "><p id="p14883195410473"><a name="p14883195410473"></a><a name="p14883195410473"></a>routes</p>
</td>
<td class="cellrowborder" valign="top" width="11.72%" headers="mcps1.2.5.1.2 "><p id="p12819143204816"><a name="p12819143204816"></a><a name="p12819143204816"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.599999999999998%" headers="mcps1.2.5.1.3 "><p id="p12541618133215"><a name="p12541618133215"></a><a name="p12541618133215"></a>Array of <a href="#table5893155464718">route</a> objects</p>
</td>
<td class="cellrowborder" valign="top" width="44.14%" headers="mcps1.2.5.1.4 "><p id="p10884125412477"><a name="p10884125412477"></a><a name="p10884125412477"></a>Specifies a route list. This is an extended attribute. For details, see <a href="#table5893155464718">Table 4</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **external\_gateway\_info**  objects

<a name="table189345484710"></a>
<table><thead align="left"><tr id="row1989315411471"><th class="cellrowborder" valign="top" width="19.21192119211921%" id="mcps1.2.5.1.1"><p id="p8893654144716"><a name="p8893654144716"></a><a name="p8893654144716"></a><strong id="b1740664117012"><a name="b1740664117012"></a><a name="b1740664117012"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="18.04180418041804%" id="mcps1.2.5.1.2"><p id="p9914193519213"><a name="p9914193519213"></a><a name="p9914193519213"></a><strong id="b168870421205"><a name="b168870421205"></a><a name="b168870421205"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.51165116511651%" id="mcps1.2.5.1.3"><p id="p0893154164719"><a name="p0893154164719"></a><a name="p0893154164719"></a><strong id="b1213818468018"><a name="b1213818468018"></a><a name="b1213818468018"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="46.23462346234623%" id="mcps1.2.5.1.4"><p id="p3893135414472"><a name="p3893135414472"></a><a name="p3893135414472"></a><strong id="b4688104611013"><a name="b4688104611013"></a><a name="b4688104611013"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row19893154184710"><td class="cellrowborder" valign="top" width="19.21192119211921%" headers="mcps1.2.5.1.1 "><p id="p1289385414477"><a name="p1289385414477"></a><a name="p1289385414477"></a>network_id</p>
</td>
<td class="cellrowborder" valign="top" width="18.04180418041804%" headers="mcps1.2.5.1.2 "><p id="p1891463572117"><a name="p1891463572117"></a><a name="p1891463572117"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16.51165116511651%" headers="mcps1.2.5.1.3 "><p id="p16893654154714"><a name="p16893654154714"></a><a name="p16893654154714"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.23462346234623%" headers="mcps1.2.5.1.4 "><p id="p15893135454716"><a name="p15893135454716"></a><a name="p15893135454716"></a>Specifies the UUID of the external network.</p>
<p id="p3893105412472"><a name="p3893105412472"></a><a name="p3893105412472"></a>You can use <strong id="b1285355418010"><a name="b1285355418010"></a><a name="b1285355418010"></a>GET /v2.0/networks?router:external=True</strong> or run the <strong id="b148551541105"><a name="b148551541105"></a><a name="b148551541105"></a>neutron net-external-list</strong> command to query information about the external network.</p>
</td>
</tr>
<tr id="row1689395415476"><td class="cellrowborder" valign="top" width="19.21192119211921%" headers="mcps1.2.5.1.1 "><p id="p2893185414475"><a name="p2893185414475"></a><a name="p2893185414475"></a>enable_snat</p>
</td>
<td class="cellrowborder" valign="top" width="18.04180418041804%" headers="mcps1.2.5.1.2 "><p id="p1891414355218"><a name="p1891414355218"></a><a name="p1891414355218"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16.51165116511651%" headers="mcps1.2.5.1.3 "><p id="p168931154164710"><a name="p168931154164710"></a><a name="p168931154164710"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="46.23462346234623%" headers="mcps1.2.5.1.4 "><p id="p88931354164710"><a name="p88931354164710"></a><a name="p88931354164710"></a>Specifies whether the SNAT function is enabled.</p>
<p id="p1889316541471"><a name="p1889316541471"></a><a name="p1889316541471"></a>The default value is <strong id="b024415341014"><a name="b024415341014"></a><a name="b024415341014"></a>false</strong>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **route**  objects

<a name="table5893155464718"></a>
<table><thead align="left"><tr id="row989335411471"><th class="cellrowborder" valign="top" width="19.321932193219325%" id="mcps1.2.5.1.1"><p id="p0894105494711"><a name="p0894105494711"></a><a name="p0894105494711"></a><strong id="b14424153612114"><a name="b14424153612114"></a><a name="b14424153612114"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.931793179317932%" id="mcps1.2.5.1.2"><p id="p1963454216214"><a name="p1963454216214"></a><a name="p1963454216214"></a><strong id="b57491137816"><a name="b57491137816"></a><a name="b57491137816"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.51165116511651%" id="mcps1.2.5.1.3"><p id="p38941548472"><a name="p38941548472"></a><a name="p38941548472"></a><strong id="b145700381413"><a name="b145700381413"></a><a name="b145700381413"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="46.23462346234623%" id="mcps1.2.5.1.4"><p id="p789445444713"><a name="p789445444713"></a><a name="p789445444713"></a><strong id="b934416391410"><a name="b934416391410"></a><a name="b934416391410"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1589455404711"><td class="cellrowborder" valign="top" width="19.321932193219325%" headers="mcps1.2.5.1.1 "><p id="p7894185418479"><a name="p7894185418479"></a><a name="p7894185418479"></a>destination</p>
</td>
<td class="cellrowborder" valign="top" width="17.931793179317932%" headers="mcps1.2.5.1.2 "><p id="p14634164217211"><a name="p14634164217211"></a><a name="p14634164217211"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16.51165116511651%" headers="mcps1.2.5.1.3 "><p id="p118941554144712"><a name="p118941554144712"></a><a name="p118941554144712"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.23462346234623%" headers="mcps1.2.5.1.4 "><p id="p689515415471"><a name="p689515415471"></a><a name="p689515415471"></a>Specifies the IP address range.</p>
<p id="p15350341121316"><a name="p15350341121316"></a><a name="p15350341121316"></a>Instructions:</p>
<p id="p634312501138"><a name="p634312501138"></a><a name="p634312501138"></a>The prefix cannot be the same as that of a direct route.</p>
</td>
</tr>
<tr id="row20895175444713"><td class="cellrowborder" valign="top" width="19.321932193219325%" headers="mcps1.2.5.1.1 "><p id="p1889515444716"><a name="p1889515444716"></a><a name="p1889515444716"></a>nexthop</p>
</td>
<td class="cellrowborder" valign="top" width="17.931793179317932%" headers="mcps1.2.5.1.2 "><p id="p13634142202117"><a name="p13634142202117"></a><a name="p13634142202117"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16.51165116511651%" headers="mcps1.2.5.1.3 "><p id="p208951854184713"><a name="p208951854184713"></a><a name="p208951854184713"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.23462346234623%" headers="mcps1.2.5.1.4 "><p id="p12895654184714"><a name="p12895654184714"></a><a name="p12895654184714"></a>Specifies the next hop IP address. The IP address can only be one in the subnet associated with the router.</p>
</td>
</tr>
</tbody>
</table>

## Response Message<a name="section6302125920589"></a>

**Table  5**  Response parameter

<a name="table444833020589"></a>
<table><thead align="left"><tr id="row3190269720589"><th class="cellrowborder" valign="top" width="15.73%" id="mcps1.2.4.1.1"><p id="p3398165120589"><a name="p3398165120589"></a><a name="p3398165120589"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="8.99%" id="mcps1.2.4.1.2"><p id="p105036620589"><a name="p105036620589"></a><a name="p105036620589"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="75.28%" id="mcps1.2.4.1.3"><p id="p4635141320589"><a name="p4635141320589"></a><a name="p4635141320589"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row6347701020589"><td class="cellrowborder" valign="top" width="15.73%" headers="mcps1.2.4.1.1 "><p id="p4136417520589"><a name="p4136417520589"></a><a name="p4136417520589"></a>router</p>
</td>
<td class="cellrowborder" valign="top" width="8.99%" headers="mcps1.2.4.1.2 "><p id="p6216386020589"><a name="p6216386020589"></a><a name="p6216386020589"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="75.28%" headers="mcps1.2.4.1.3 "><p id="p3652335220589"><a name="p3652335220589"></a><a name="p3652335220589"></a>Specifies the router list. For details, see <a href="#table24153696181443">Table 6</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  6** **router**  objects

<a name="table24153696181443"></a>
<table><thead align="left"><tr id="row11861342181443"><th class="cellrowborder" valign="top" width="26.669999999999998%" id="mcps1.2.4.1.1"><p id="p21244677181443"><a name="p21244677181443"></a><a name="p21244677181443"></a><strong id="b239191519211"><a name="b239191519211"></a><a name="b239191519211"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="23.330000000000002%" id="mcps1.2.4.1.2"><p id="p43097239181443"><a name="p43097239181443"></a><a name="p43097239181443"></a><strong id="b22156166218"><a name="b22156166218"></a><a name="b22156166218"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p36728767181443"><a name="p36728767181443"></a><a name="p36728767181443"></a><strong id="b1687710161027"><a name="b1687710161027"></a><a name="b1687710161027"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row22240136181443"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p56620590181443"><a name="p56620590181443"></a><a name="p56620590181443"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p22865048181443"><a name="p22865048181443"></a><a name="p22865048181443"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p46905229181443"><a name="p46905229181443"></a><a name="p46905229181443"></a>Specifies the router ID.</p>
<p id="p121142486504"><a name="p121142486504"></a><a name="p121142486504"></a>This parameter is not mandatory when you query routers.</p>
</td>
</tr>
<tr id="row19493885181443"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p35500827181443"><a name="p35500827181443"></a><a name="p35500827181443"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p56994705181443"><a name="p56994705181443"></a><a name="p56994705181443"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p11978624181443"><a name="p11978624181443"></a><a name="p11978624181443"></a>Specifies the router name.</p>
<p id="p30744457181443"><a name="p30744457181443"></a><a name="p30744457181443"></a>The name can contain only letters, digits, underscores (_), hyphens (-), and periods (.).</p>
</td>
</tr>
<tr id="row8264657181443"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p65457453181443"><a name="p65457453181443"></a><a name="p65457453181443"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p453502181443"><a name="p453502181443"></a><a name="p453502181443"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p48641520181443"><a name="p48641520181443"></a><a name="p48641520181443"></a>Specifies the administrative status.</p>
<p id="p35120501181443"><a name="p35120501181443"></a><a name="p35120501181443"></a>The value can only be <strong id="b073217511625"><a name="b073217511625"></a><a name="b073217511625"></a>true</strong>.</p>
</td>
</tr>
<tr id="row47649056181443"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p34368308181443"><a name="p34368308181443"></a><a name="p34368308181443"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p32369557181443"><a name="p32369557181443"></a><a name="p32369557181443"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p4016564181443"><a name="p4016564181443"></a><a name="p4016564181443"></a>Specifies the router status. The value can be <strong id="b934555926"><a name="b934555926"></a><a name="b934555926"></a>ACTIVE</strong>, <strong id="b193615558215"><a name="b193615558215"></a><a name="b193615558215"></a>DOWN</strong>, or <strong id="b53818559218"><a name="b53818559218"></a><a name="b53818559218"></a>ERROR</strong>.</p>
</td>
</tr>
<tr id="row36149082181443"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p42394506181443"><a name="p42394506181443"></a><a name="p42394506181443"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p11402971181443"><a name="p11402971181443"></a><a name="p11402971181443"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row26765861181443"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p20551115181443"><a name="p20551115181443"></a><a name="p20551115181443"></a>external_gateway_info</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p54027655181443"><a name="p54027655181443"></a><a name="p54027655181443"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p12911840181443"><a name="p12911840181443"></a><a name="p12911840181443"></a>Specifies the external gateway. This is an extended attribute. For details, see the <strong id="b169971641318"><a name="b169971641318"></a><a name="b169971641318"></a>external_gateway_info</strong> objects.</p>
</td>
</tr>
<tr id="row49097702181443"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p17490925181443"><a name="p17490925181443"></a><a name="p17490925181443"></a>routes</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p7478812181443"><a name="p7478812181443"></a><a name="p7478812181443"></a>Array of <a href="#table18829650181443">route</a> objects</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p5122123194853"><a name="p5122123194853"></a><a name="p5122123194853"></a>Specifies a route list. This is an extended attribute. For details, see <a href="#table18829650181443">Table 8</a>.</p>
</td>
</tr>
<tr id="row7278189151614"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p870051413911"><a name="p870051413911"></a><a name="p870051413911"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p15700614790"><a name="p15700614790"></a><a name="p15700614790"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p0236436142611"><a name="p0236436142611"></a><a name="p0236436142611"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row172292215166"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p1953114119914"><a name="p1953114119914"></a><a name="p1953114119914"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p595318416919"><a name="p595318416919"></a><a name="p595318416919"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1395374115919"><a name="p1395374115919"></a><a name="p1395374115919"></a>Specifies the time (UTC) when the router is created.</p>
<p id="p65980291419"><a name="p65980291419"></a><a name="p65980291419"></a>Format: <em id="i11531202913314"><a name="i11531202913314"></a><a name="i11531202913314"></a>yyyy-MM-ddTHH:mm:ss</em></p>
</td>
</tr>
<tr id="row106341917161611"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p139719548912"><a name="p139719548912"></a><a name="p139719548912"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p53971154594"><a name="p53971154594"></a><a name="p53971154594"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1339713549918"><a name="p1339713549918"></a><a name="p1339713549918"></a>Specifies the time (UTC) when the router is updated.</p>
<p id="p73282255586"><a name="p73282255586"></a><a name="p73282255586"></a>Format: <em id="i52401346310"><a name="i52401346310"></a><a name="i52401346310"></a>yyyy-MM-ddTHH:mm:ss</em></p>
</td>
</tr>
</tbody>
</table>

**Table  7** **external\_gateway\_info**  objects

<a name="table11448068181443"></a>
<table><thead align="left"><tr id="row58732356181443"><th class="cellrowborder" valign="top" width="26.669999999999998%" id="mcps1.2.4.1.1"><p id="p59700400181443"><a name="p59700400181443"></a><a name="p59700400181443"></a><strong id="b793610491739"><a name="b793610491739"></a><a name="b793610491739"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="23.34%" id="mcps1.2.4.1.2"><p id="p3894228181443"><a name="p3894228181443"></a><a name="p3894228181443"></a><strong id="b98107507320"><a name="b98107507320"></a><a name="b98107507320"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="49.99%" id="mcps1.2.4.1.3"><p id="p1781307181443"><a name="p1781307181443"></a><a name="p1781307181443"></a><strong id="b125428511339"><a name="b125428511339"></a><a name="b125428511339"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row10068178181443"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p10216081181443"><a name="p10216081181443"></a><a name="p10216081181443"></a>network_id</p>
</td>
<td class="cellrowborder" valign="top" width="23.34%" headers="mcps1.2.4.1.2 "><p id="p22196257181443"><a name="p22196257181443"></a><a name="p22196257181443"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.99%" headers="mcps1.2.4.1.3 "><p id="p38375206181443"><a name="p38375206181443"></a><a name="p38375206181443"></a>Specifies the UUID of the external network.</p>
<p id="p21383968181443"><a name="p21383968181443"></a><a name="p21383968181443"></a>You can use <strong id="b1717718551933"><a name="b1717718551933"></a><a name="b1717718551933"></a>GET /v2.0/networks?router:external=True</strong> or run the <strong id="b111801551432"><a name="b111801551432"></a><a name="b111801551432"></a>neutron net-external-list</strong> command to query information about the external network.</p>
</td>
</tr>
<tr id="row58237990181443"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p19656760181443"><a name="p19656760181443"></a><a name="p19656760181443"></a>enable_snat</p>
</td>
<td class="cellrowborder" valign="top" width="23.34%" headers="mcps1.2.4.1.2 "><p id="p48693751181443"><a name="p48693751181443"></a><a name="p48693751181443"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="49.99%" headers="mcps1.2.4.1.3 "><p id="p22976335181443"><a name="p22976335181443"></a><a name="p22976335181443"></a>Specifies whether the SNAT function is enabled.</p>
<p id="p49143812181443"><a name="p49143812181443"></a><a name="p49143812181443"></a>The default value is <strong id="b173411501248"><a name="b173411501248"></a><a name="b173411501248"></a>false</strong>.</p>
</td>
</tr>
</tbody>
</table>

**Table  8** **route**  objects

<a name="table18829650181443"></a>
<table><thead align="left"><tr id="row60542282181443"><th class="cellrowborder" valign="top" width="26.669999999999998%" id="mcps1.2.4.1.1"><p id="p4977811181443"><a name="p4977811181443"></a><a name="p4977811181443"></a><strong id="b14963210415"><a name="b14963210415"></a><a name="b14963210415"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="23.34%" id="mcps1.2.4.1.2"><p id="p549581181443"><a name="p549581181443"></a><a name="p549581181443"></a><strong id="b137375315420"><a name="b137375315420"></a><a name="b137375315420"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="49.99%" id="mcps1.2.4.1.3"><p id="p9206714181443"><a name="p9206714181443"></a><a name="p9206714181443"></a><strong id="b177769415419"><a name="b177769415419"></a><a name="b177769415419"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row7546366181443"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p7275939181443"><a name="p7275939181443"></a><a name="p7275939181443"></a>destination</p>
</td>
<td class="cellrowborder" valign="top" width="23.34%" headers="mcps1.2.4.1.2 "><p id="p52480209181443"><a name="p52480209181443"></a><a name="p52480209181443"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.99%" headers="mcps1.2.4.1.3 "><p id="p66892155181443"><a name="p66892155181443"></a><a name="p66892155181443"></a>Specifies the IP address range.</p>
</td>
</tr>
<tr id="row65158490181443"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p43346313181443"><a name="p43346313181443"></a><a name="p43346313181443"></a>nexthop</p>
</td>
<td class="cellrowborder" valign="top" width="23.34%" headers="mcps1.2.4.1.2 "><p id="p21390453181443"><a name="p21390453181443"></a><a name="p21390453181443"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.99%" headers="mcps1.2.4.1.3 "><p id="p17763616181443"><a name="p17763616181443"></a><a name="p17763616181443"></a>Specifies the next hop IP address. The IP address can only be one in the subnet associated with the router.</p>
</td>
</tr>
</tbody>
</table>

## Example:<a name="section6027472020589"></a>

Example request

```
PUT https://{Endpoint}/v2.0/routers/f5dbdfe0-86f9-4b0a-9a32-6be143f0a076  
{
    "router": {
           "name": "router-220"
    }
}
```

Example response

```
{
    "router": {
        "id": "f5dbdfe0-86f9-4b0a-9a32-6be143f0a076",
        "name": "router-220",
        "status": "ACTIVE",
        "tenant_id": "bbfe8c41dd034a07bebd592bf03b4b0c",
        "project_id": "bbfe8c41dd034a07bebd592bf03b4b0c",
        "admin_state_up": true,
        "external_gateway_info": {
            "network_id": "0a2228f2-7f8a-45f1-8e09-9039e1d09975",
            "enable_snat": false
        },
        "routes": [],
        "created_at": "2018-09-20T02:06:07",
        "updated_at": "2018-09-20T02:06:09"
    }
}
```

## Status Code<a name="section10470352390"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

