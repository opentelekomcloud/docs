# Creating a Router<a name="vpc_router_0003"></a>

## Function<a name="section54866008205757"></a>

This API is used to create a router.

## URI<a name="section437105205757"></a>

POST /v2.0/routers

## Request Message<a name="section56558784205757"></a>

**Table  1**  Request parameter

<a name="table17858782205757"></a>
<table><thead align="left"><tr id="row29195524205757"><th class="cellrowborder" valign="top" width="19.388061193880613%" id="mcps1.2.5.1.1"><p id="p16027205205757"><a name="p16027205205757"></a><a name="p16027205205757"></a><strong id="b1457511119615"><a name="b1457511119615"></a><a name="b1457511119615"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="19.548045195480455%" id="mcps1.2.5.1.2"><p id="p23135223205757"><a name="p23135223205757"></a><a name="p23135223205757"></a><strong id="b410113363"><a name="b410113363"></a><a name="b410113363"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="18.208179182081793%" id="mcps1.2.5.1.3"><p id="p62013761205757"><a name="p62013761205757"></a><a name="p62013761205757"></a><strong id="b13919165610517"><a name="b13919165610517"></a><a name="b13919165610517"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="42.85571442855714%" id="mcps1.2.5.1.4"><p id="p57058764205757"><a name="p57058764205757"></a><a name="p57058764205757"></a><strong id="b102221816261"><a name="b102221816261"></a><a name="b102221816261"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row58357184205757"><td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.2.5.1.1 "><p id="p29311427205757"><a name="p29311427205757"></a><a name="p29311427205757"></a>router</p>
</td>
<td class="cellrowborder" valign="top" width="19.548045195480455%" headers="mcps1.2.5.1.2 "><p id="p25415424205757"><a name="p25415424205757"></a><a name="p25415424205757"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="18.208179182081793%" headers="mcps1.2.5.1.3 "><p id="p45383453205757"><a name="p45383453205757"></a><a name="p45383453205757"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.5.1.4 "><p id="p52181058205757"><a name="p52181058205757"></a><a name="p52181058205757"></a>Specifies the router list. For details, see <a href="#table24153696181443">Table 2</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  2** **router**  objects

<a name="table24153696181443"></a>
<table><thead align="left"><tr id="row11861342181443"><th class="cellrowborder" valign="top" width="23.54%" id="mcps1.2.5.1.1"><p id="p21244677181443"><a name="p21244677181443"></a><a name="p21244677181443"></a><strong id="b4526018986"><a name="b4526018986"></a><a name="b4526018986"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.740000000000002%" id="mcps1.2.5.1.2"><p id="p981918394815"><a name="p981918394815"></a><a name="p981918394815"></a><strong id="b597871915812"><a name="b597871915812"></a><a name="b597871915812"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.31%" id="mcps1.2.5.1.3"><p id="p43097239181443"><a name="p43097239181443"></a><a name="p43097239181443"></a><strong id="b167571520187"><a name="b167571520187"></a><a name="b167571520187"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="42.41%" id="mcps1.2.5.1.4"><p id="p36728767181443"><a name="p36728767181443"></a><a name="p36728767181443"></a><strong id="b1033117219813"><a name="b1033117219813"></a><a name="b1033117219813"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row19493885181443"><td class="cellrowborder" valign="top" width="23.54%" headers="mcps1.2.5.1.1 "><p id="p35500827181443"><a name="p35500827181443"></a><a name="p35500827181443"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="17.740000000000002%" headers="mcps1.2.5.1.2 "><p id="p1881923164818"><a name="p1881923164818"></a><a name="p1881923164818"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16.31%" headers="mcps1.2.5.1.3 "><p id="p56994705181443"><a name="p56994705181443"></a><a name="p56994705181443"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.41%" headers="mcps1.2.5.1.4 "><p id="p11978624181443"><a name="p11978624181443"></a><a name="p11978624181443"></a>Specifies the router name.</p>
<p id="p15156189113"><a name="p15156189113"></a><a name="p15156189113"></a>Instructions:</p>
<p id="p30744457181443"><a name="p30744457181443"></a><a name="p30744457181443"></a>The name can contain only letters, digits, underscores (_), hyphens (-), and periods (.).</p>
</td>
</tr>
<tr id="row8264657181443"><td class="cellrowborder" valign="top" width="23.54%" headers="mcps1.2.5.1.1 "><p id="p65457453181443"><a name="p65457453181443"></a><a name="p65457453181443"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="17.740000000000002%" headers="mcps1.2.5.1.2 "><p id="p9819193104813"><a name="p9819193104813"></a><a name="p9819193104813"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16.31%" headers="mcps1.2.5.1.3 "><p id="p453502181443"><a name="p453502181443"></a><a name="p453502181443"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="42.41%" headers="mcps1.2.5.1.4 "><p id="p48641520181443"><a name="p48641520181443"></a><a name="p48641520181443"></a>Specifies the administrative status.</p>
<p id="p35120501181443"><a name="p35120501181443"></a><a name="p35120501181443"></a>The value can only be <strong id="b159184241396"><a name="b159184241396"></a><a name="b159184241396"></a>true</strong>.</p>
</td>
</tr>
<tr id="row26765861181443"><td class="cellrowborder" valign="top" width="23.54%" headers="mcps1.2.5.1.1 "><p id="p20551115181443"><a name="p20551115181443"></a><a name="p20551115181443"></a>external_gateway_info</p>
</td>
<td class="cellrowborder" valign="top" width="17.740000000000002%" headers="mcps1.2.5.1.2 "><p id="p1281914344820"><a name="p1281914344820"></a><a name="p1281914344820"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16.31%" headers="mcps1.2.5.1.3 "><p id="p54027655181443"><a name="p54027655181443"></a><a name="p54027655181443"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="42.41%" headers="mcps1.2.5.1.4 "><p id="p12911840181443"><a name="p12911840181443"></a><a name="p12911840181443"></a>Specifies the external gateway. This is an extended attribute. For details, see the <strong id="b799745419471"><a name="b799745419471"></a><a name="b799745419471"></a>external_gateway_info</strong> objects.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **external\_gateway\_info**  objects

<a name="table11448068181443"></a>
<table><thead align="left"><tr id="row58732356181443"><th class="cellrowborder" valign="top" width="23.522352235223522%" id="mcps1.2.5.1.1"><p id="p59700400181443"><a name="p59700400181443"></a><a name="p59700400181443"></a><strong id="b355115917476"><a name="b355115917476"></a><a name="b355115917476"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.22172217221722%" id="mcps1.2.5.1.2"><p id="p1127212151208"><a name="p1127212151208"></a><a name="p1127212151208"></a><strong id="b656415064819"><a name="b656415064819"></a><a name="b656415064819"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="13.021302130213023%" id="mcps1.2.5.1.3"><p id="p3894228181443"><a name="p3894228181443"></a><a name="p3894228181443"></a><strong id="b66481116486"><a name="b66481116486"></a><a name="b66481116486"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="46.23462346234623%" id="mcps1.2.5.1.4"><p id="p1781307181443"><a name="p1781307181443"></a><a name="p1781307181443"></a><strong id="b1471428481"><a name="b1471428481"></a><a name="b1471428481"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row10068178181443"><td class="cellrowborder" valign="top" width="23.522352235223522%" headers="mcps1.2.5.1.1 "><p id="p10216081181443"><a name="p10216081181443"></a><a name="p10216081181443"></a>network_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.22172217221722%" headers="mcps1.2.5.1.2 "><p id="p7272191582015"><a name="p7272191582015"></a><a name="p7272191582015"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.021302130213023%" headers="mcps1.2.5.1.3 "><p id="p22196257181443"><a name="p22196257181443"></a><a name="p22196257181443"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.23462346234623%" headers="mcps1.2.5.1.4 "><p id="p38375206181443"><a name="p38375206181443"></a><a name="p38375206181443"></a>Specifies the UUID of the external network.</p>
<p id="p21383968181443"><a name="p21383968181443"></a><a name="p21383968181443"></a>You can use <strong id="b1735498134816"><a name="b1735498134816"></a><a name="b1735498134816"></a>GET /v2.0/networks?router:external=True</strong> or run the <strong id="b1635514854810"><a name="b1635514854810"></a><a name="b1635514854810"></a>neutron net-external-list</strong> command to query information about the external network.</p>
</td>
</tr>
<tr id="row58237990181443"><td class="cellrowborder" valign="top" width="23.522352235223522%" headers="mcps1.2.5.1.1 "><p id="p19656760181443"><a name="p19656760181443"></a><a name="p19656760181443"></a>enable_snat</p>
</td>
<td class="cellrowborder" valign="top" width="17.22172217221722%" headers="mcps1.2.5.1.2 "><p id="p132731315162019"><a name="p132731315162019"></a><a name="p132731315162019"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.021302130213023%" headers="mcps1.2.5.1.3 "><p id="p48693751181443"><a name="p48693751181443"></a><a name="p48693751181443"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="46.23462346234623%" headers="mcps1.2.5.1.4 "><p id="p22976335181443"><a name="p22976335181443"></a><a name="p22976335181443"></a>Specifies whether the SNAT function is enabled.</p>
<p id="p49143812181443"><a name="p49143812181443"></a><a name="p49143812181443"></a>The default value is <strong id="b17245105811501"><a name="b17245105811501"></a><a name="b17245105811501"></a>false</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Response Message<a name="section56374749205757"></a>

**Table  4**  Response parameter

<a name="table2951934205757"></a>
<table><thead align="left"><tr id="row46218389205757"><th class="cellrowborder" valign="top" width="23.169999999999998%" id="mcps1.2.4.1.1"><p id="p52702038205757"><a name="p52702038205757"></a><a name="p52702038205757"></a><strong id="b842352706182020"><a name="b842352706182020"></a><a name="b842352706182020"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25.61%" id="mcps1.2.4.1.2"><p id="p41006687205757"><a name="p41006687205757"></a><a name="p41006687205757"></a><strong id="b842352706115456"><a name="b842352706115456"></a><a name="b842352706115456"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51.22%" id="mcps1.2.4.1.3"><p id="p5443692205757"><a name="p5443692205757"></a><a name="p5443692205757"></a><strong id="b84235270691717"><a name="b84235270691717"></a><a name="b84235270691717"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row38285887205757"><td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p14149114205757"><a name="p14149114205757"></a><a name="p14149114205757"></a>router</p>
</td>
<td class="cellrowborder" valign="top" width="25.61%" headers="mcps1.2.4.1.2 "><p id="p5227590205757"><a name="p5227590205757"></a><a name="p5227590205757"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.2.4.1.3 "><p id="p5591471205757"><a name="p5591471205757"></a><a name="p5591471205757"></a>Specifies the router. For details, see <a href="#table1923815121475">Table 5</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  5** **router**  objects

<a name="table1923815121475"></a>
<table><thead align="left"><tr id="row1723891210478"><th class="cellrowborder" valign="top" width="26.669999999999998%" id="mcps1.2.4.1.1"><p id="p16238151211471"><a name="p16238151211471"></a><a name="p16238151211471"></a><strong id="b117421530195118"><a name="b117421530195118"></a><a name="b117421530195118"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="23.330000000000002%" id="mcps1.2.4.1.2"><p id="p723831234719"><a name="p723831234719"></a><a name="p723831234719"></a><strong id="b7211113395117"><a name="b7211113395117"></a><a name="b7211113395117"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p11238131214710"><a name="p11238131214710"></a><a name="p11238131214710"></a><strong id="b131301734195119"><a name="b131301734195119"></a><a name="b131301734195119"></a>Description</strong></p>
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
<tr id="row112381012204717"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p17238141219479"><a name="p17238141219479"></a><a name="p17238141219479"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p142381412104710"><a name="p142381412104710"></a><a name="p142381412104710"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p52381412104714"><a name="p52381412104714"></a><a name="p52381412104714"></a>Specifies the router name.</p>
<p id="p122389120477"><a name="p122389120477"></a><a name="p122389120477"></a>The name can contain only letters, digits, underscores (_), hyphens (-), and periods (.).</p>
</td>
</tr>
<tr id="row16238101211472"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p123911294714"><a name="p123911294714"></a><a name="p123911294714"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p18239171220477"><a name="p18239171220477"></a><a name="p18239171220477"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p12395124476"><a name="p12395124476"></a><a name="p12395124476"></a>Specifies the administrative status.</p>
<p id="p023921210476"><a name="p023921210476"></a><a name="p023921210476"></a>The value can only be <strong id="b723503013527"><a name="b723503013527"></a><a name="b723503013527"></a>true</strong>.</p>
</td>
</tr>
<tr id="row47649056181443"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p34368308181443"><a name="p34368308181443"></a><a name="p34368308181443"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p32369557181443"><a name="p32369557181443"></a><a name="p32369557181443"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p4016564181443"><a name="p4016564181443"></a><a name="p4016564181443"></a>Specifies the router status. The value can be <strong id="b1278999155817"><a name="b1278999155817"></a><a name="b1278999155817"></a>ACTIVE</strong>, <strong id="b1179015995814"><a name="b1179015995814"></a><a name="b1179015995814"></a>DOWN</strong>, or <strong id="b37921293586"><a name="b37921293586"></a><a name="b37921293586"></a>ERROR</strong>.</p>
</td>
</tr>
<tr id="row36149082181443"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p42394506181443"><a name="p42394506181443"></a><a name="p42394506181443"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p11402971181443"><a name="p11402971181443"></a><a name="p11402971181443"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row5239171218479"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p18239101217478"><a name="p18239101217478"></a><a name="p18239101217478"></a>external_gateway_info</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p1239161213474"><a name="p1239161213474"></a><a name="p1239161213474"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1223916124478"><a name="p1223916124478"></a><a name="p1223916124478"></a>Specifies the external gateway. This is an extended attribute. For details, see the <strong id="b5862143755213"><a name="b5862143755213"></a><a name="b5862143755213"></a>external_gateway_info</strong> objects.</p>
</td>
</tr>
<tr id="row49097702181443"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p17490925181443"><a name="p17490925181443"></a><a name="p17490925181443"></a>routes</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p7478812181443"><a name="p7478812181443"></a><a name="p7478812181443"></a>Array of <a href="#table18829650181443">route</a> objects</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p5122123194853"><a name="p5122123194853"></a><a name="p5122123194853"></a>Specifies a route list. This is an extended attribute. For details, see <a href="#table18829650181443">Table 7</a>.</p>
</td>
</tr>
<tr id="row7278189151614"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p870051413911"><a name="p870051413911"></a><a name="p870051413911"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p15700614790"><a name="p15700614790"></a><a name="p15700614790"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p8813182510263"><a name="p8813182510263"></a><a name="p8813182510263"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row172292215166"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p1953114119914"><a name="p1953114119914"></a><a name="p1953114119914"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p595318416919"><a name="p595318416919"></a><a name="p595318416919"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1395374115919"><a name="p1395374115919"></a><a name="p1395374115919"></a>Specifies the time (UTC) when the router is created.</p>
<p id="p65980291419"><a name="p65980291419"></a><a name="p65980291419"></a>Format: <em id="i92763917535"><a name="i92763917535"></a><a name="i92763917535"></a>yyyy-MM-ddTHH:mm:ss</em></p>
</td>
</tr>
<tr id="row106341917161611"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p139719548912"><a name="p139719548912"></a><a name="p139719548912"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p53971154594"><a name="p53971154594"></a><a name="p53971154594"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1339713549918"><a name="p1339713549918"></a><a name="p1339713549918"></a>Specifies the time (UTC) when the router is updated.</p>
<p id="p1329962217483"><a name="p1329962217483"></a><a name="p1329962217483"></a>Format: <em id="i1748961535317"><a name="i1748961535317"></a><a name="i1748961535317"></a>yyyy-MM-ddTHH:mm:ss</em></p>
</td>
</tr>
</tbody>
</table>

**Table  6** **external\_gateway\_info**  objects

<a name="table5241191216479"></a>
<table><thead align="left"><tr id="row172411312144717"><th class="cellrowborder" valign="top" width="26.669999999999998%" id="mcps1.2.4.1.1"><p id="p1724181214477"><a name="p1724181214477"></a><a name="p1724181214477"></a><strong id="b13911101865312"><a name="b13911101865312"></a><a name="b13911101865312"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="23.34%" id="mcps1.2.4.1.2"><p id="p1024191213473"><a name="p1024191213473"></a><a name="p1024191213473"></a><strong id="b92271620205311"><a name="b92271620205311"></a><a name="b92271620205311"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="49.99%" id="mcps1.2.4.1.3"><p id="p1324121218471"><a name="p1324121218471"></a><a name="p1324121218471"></a><strong id="b123519218539"><a name="b123519218539"></a><a name="b123519218539"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row142411124472"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p19241151274710"><a name="p19241151274710"></a><a name="p19241151274710"></a>network_id</p>
</td>
<td class="cellrowborder" valign="top" width="23.34%" headers="mcps1.2.4.1.2 "><p id="p424101218477"><a name="p424101218477"></a><a name="p424101218477"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.99%" headers="mcps1.2.4.1.3 "><p id="p22411412144715"><a name="p22411412144715"></a><a name="p22411412144715"></a>Specifies the UUID of the external network.</p>
<p id="p4241912204710"><a name="p4241912204710"></a><a name="p4241912204710"></a>You can use <strong id="b17901192415532"><a name="b17901192415532"></a><a name="b17901192415532"></a>GET /v2.0/networks?router:external=True</strong> or run the <strong id="b590362405315"><a name="b590362405315"></a><a name="b590362405315"></a>neutron net-external-list</strong> command to query information about the external network.</p>
</td>
</tr>
<tr id="row1624171218472"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p132411128476"><a name="p132411128476"></a><a name="p132411128476"></a>enable_snat</p>
</td>
<td class="cellrowborder" valign="top" width="23.34%" headers="mcps1.2.4.1.2 "><p id="p1241912124716"><a name="p1241912124716"></a><a name="p1241912124716"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="49.99%" headers="mcps1.2.4.1.3 "><p id="p22411812124711"><a name="p22411812124711"></a><a name="p22411812124711"></a>Specifies whether the SNAT function is enabled.</p>
<p id="p32411120478"><a name="p32411120478"></a><a name="p32411120478"></a>The default value is <strong id="b438813476537"><a name="b438813476537"></a><a name="b438813476537"></a>false</strong>.</p>
</td>
</tr>
</tbody>
</table>

**Table  7** **route**  objects

<a name="table18829650181443"></a>
<table><thead align="left"><tr id="row60542282181443"><th class="cellrowborder" valign="top" width="26.669999999999998%" id="mcps1.2.4.1.1"><p id="p4977811181443"><a name="p4977811181443"></a><a name="p4977811181443"></a><strong id="b854875013535"><a name="b854875013535"></a><a name="b854875013535"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="23.34%" id="mcps1.2.4.1.2"><p id="p549581181443"><a name="p549581181443"></a><a name="p549581181443"></a><strong id="b13431125375315"><a name="b13431125375315"></a><a name="b13431125375315"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="49.99%" id="mcps1.2.4.1.3"><p id="p9206714181443"><a name="p9206714181443"></a><a name="p9206714181443"></a><strong id="b1269932119583"><a name="b1269932119583"></a><a name="b1269932119583"></a>Description</strong></p>
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

## Example:<a name="section50323245205757"></a>

Example request

```
POST https://{Endpoint}/v2.0/routers 
{
    "router": {
           "name": "router-test2",
           "admin_state_up": true
    }
}
```

Example response

```
{
    "router": {
        "id": "f5dbdfe0-86f9-4b0a-9a32-6be143f0a076",
        "name": "router-test2",
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

