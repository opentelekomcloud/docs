# Updating the Connection<a name="en-dc_topic_0055025319"></a>

## Function<a name="section10267951"></a>

This API is used to update a connection.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>1.  You can only increase the bandwidth.  
>2.  Bandwidths of the hosting connections cannot be updated.  

## URI<a name="section25302698"></a>

PUT /v2.0/dcaas/direct-connects/\{direct\_connect\_id\}

**Table  1**  Parameter description

<a name="table183245150407"></a>
<table><thead align="left"><tr id="row1329191584012"><th class="cellrowborder" valign="top" width="26.52734726527347%" id="mcps1.2.5.1.1"><p id="p8332215134011"><a name="p8332215134011"></a><a name="p8332215134011"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p153354156404"><a name="p153354156404"></a><a name="p153354156404"></a><strong id="b842352706165439"><a name="b842352706165439"></a><a name="b842352706165439"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.328367163283673%" id="mcps1.2.5.1.3"><p id="p2339151519405"><a name="p2339151519405"></a><a name="p2339151519405"></a><strong id="b842352706192549"><a name="b842352706192549"></a><a name="b842352706192549"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="42.85571442855714%" id="mcps1.2.5.1.4"><p id="p3341141516405"><a name="p3341141516405"></a><a name="p3341141516405"></a><strong id="b84235270615331"><a name="b84235270615331"></a><a name="b84235270615331"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row7342191504013"><td class="cellrowborder" valign="top" width="26.52734726527347%" headers="mcps1.2.5.1.1 "><p id="p2344315174014"><a name="p2344315174014"></a><a name="p2344315174014"></a>direct_connect_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p234713152402"><a name="p234713152402"></a><a name="p234713152402"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p13511015184019"><a name="p13511015184019"></a><a name="p13511015184019"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.5.1.4 "><p id="p143531415154018"><a name="p143531415154018"></a><a name="p143531415154018"></a>Indicates the connection ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section36252627"></a>

[Table 2](#table7364283175427)  lists the request parameter.

**Table  2**  Request parameter

<a name="table7364283175427"></a>
<table><thead align="left"><tr id="row28171119175427"><th class="cellrowborder" valign="top" width="23.897610238976103%" id="mcps1.2.5.1.1"><p id="p8323660175427"><a name="p8323660175427"></a><a name="p8323660175427"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.91830816918308%" id="mcps1.2.5.1.2"><p id="p46855411175427"><a name="p46855411175427"></a><a name="p46855411175427"></a><strong id="b842352706165439_1"><a name="b842352706165439_1"></a><a name="b842352706165439_1"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.328367163283673%" id="mcps1.2.5.1.3"><p id="p60815106175427"><a name="p60815106175427"></a><a name="p60815106175427"></a><strong id="b842352706192549_1"><a name="b842352706192549_1"></a><a name="b842352706192549_1"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="42.85571442855714%" id="mcps1.2.5.1.4"><p id="p43025320175427"><a name="p43025320175427"></a><a name="p43025320175427"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row49466658175427"><td class="cellrowborder" valign="top" width="23.897610238976103%" headers="mcps1.2.5.1.1 "><p id="p4415550175427"><a name="p4415550175427"></a><a name="p4415550175427"></a>direct_connect</p>
</td>
<td class="cellrowborder" valign="top" width="16.91830816918308%" headers="mcps1.2.5.1.2 "><p id="p1100763175427"><a name="p1100763175427"></a><a name="p1100763175427"></a>Dictionary data structure</p>
</td>
<td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p15674469175427"><a name="p15674469175427"></a><a name="p15674469175427"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.5.1.4 "><p id="p228188175427"><a name="p228188175427"></a><a name="p228188175427"></a>Indicates the <strong id="b842352706172852"><a name="b842352706172852"></a><a name="b842352706172852"></a>direct_connect</strong> object.</p>
</td>
</tr>
</tbody>
</table>

Description of field  **direct\_connect**

<a name="table125648759846"></a>
<table><thead align="left"><tr id="row265942339846"><th class="cellrowborder" valign="top" width="23.71%" id="mcps1.1.5.1.1"><p id="p351661709915"><a name="p351661709915"></a><a name="p351661709915"></a><strong id="b8423527069918"><a name="b8423527069918"></a><a name="b8423527069918"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="12.78%" id="mcps1.1.5.1.2"><p id="p89913189915"><a name="p89913189915"></a><a name="p89913189915"></a><strong id="b842352706165439_2"><a name="b842352706165439_2"></a><a name="b842352706165439_2"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.28%" id="mcps1.1.5.1.3"><p id="p209180099915"><a name="p209180099915"></a><a name="p209180099915"></a><strong id="b842352706192549_2"><a name="b842352706192549_2"></a><a name="b842352706192549_2"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="43.230000000000004%" id="mcps1.1.5.1.4"><p id="p132751689915"><a name="p132751689915"></a><a name="p132751689915"></a><strong id="b84235270615331_1"><a name="b84235270615331_1"></a><a name="b84235270615331_1"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row17370369846"><td class="cellrowborder" valign="top" width="23.71%" headers="mcps1.1.5.1.1 "><p id="p444303839854"><a name="p444303839854"></a><a name="p444303839854"></a>direct_connect_id</p>
</td>
<td class="cellrowborder" valign="top" width="12.78%" headers="mcps1.1.5.1.2 "><p id="p456497459854"><a name="p456497459854"></a><a name="p456497459854"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="20.28%" headers="mcps1.1.5.1.3 "><p id="p318295119854"><a name="p318295119854"></a><a name="p318295119854"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="43.230000000000004%" headers="mcps1.1.5.1.4 "><p id="p302511269854"><a name="p302511269854"></a><a name="p302511269854"></a>Indicates the connection ID.</p>
</td>
</tr>
<tr id="row5271981314254"><td class="cellrowborder" valign="top" width="23.71%" headers="mcps1.1.5.1.1 "><p id="p5257963714254"><a name="p5257963714254"></a><a name="p5257963714254"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="12.78%" headers="mcps1.1.5.1.2 "><p id="p3109221814254"><a name="p3109221814254"></a><a name="p3109221814254"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="20.28%" headers="mcps1.1.5.1.3 "><p id="p3544171514254"><a name="p3544171514254"></a><a name="p3544171514254"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="43.230000000000004%" headers="mcps1.1.5.1.4 "><p id="p5220666514254"><a name="p5220666514254"></a><a name="p5220666514254"></a>Provides supplementary information about the connection.</p>
</td>
</tr>
<tr id="row2822737814254"><td class="cellrowborder" valign="top" width="23.71%" headers="mcps1.1.5.1.1 "><p id="p793298914254"><a name="p793298914254"></a><a name="p793298914254"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="12.78%" headers="mcps1.1.5.1.2 "><p id="p3859237714254"><a name="p3859237714254"></a><a name="p3859237714254"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="20.28%" headers="mcps1.1.5.1.3 "><p id="p3897482914254"><a name="p3897482914254"></a><a name="p3897482914254"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="43.230000000000004%" headers="mcps1.1.5.1.4 "><p id="p284461014254"><a name="p284461014254"></a><a name="p284461014254"></a>Indicates the connection name.</p>
</td>
</tr>
<tr id="row24309452205237"><td class="cellrowborder" valign="top" width="23.71%" headers="mcps1.1.5.1.1 "><p id="p46653157205251"><a name="p46653157205251"></a><a name="p46653157205251"></a>bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="12.78%" headers="mcps1.1.5.1.2 "><p id="p20809410205251"><a name="p20809410205251"></a><a name="p20809410205251"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="20.28%" headers="mcps1.1.5.1.3 "><p id="p7840639205251"><a name="p7840639205251"></a><a name="p7840639205251"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="43.230000000000004%" headers="mcps1.1.5.1.4 "><p id="p31112004205251"><a name="p31112004205251"></a><a name="p31112004205251"></a>Indicates the bandwidth used by the connection (unit: Mbit/s).</p>
</td>
</tr>
<tr id="row21061467142619"><td class="cellrowborder" valign="top" width="23.71%" headers="mcps1.1.5.1.1 "><p id="p26051377142619"><a name="p26051377142619"></a><a name="p26051377142619"></a>provider_status</p>
</td>
<td class="cellrowborder" valign="top" width="12.78%" headers="mcps1.1.5.1.2 "><p id="p29786826142619"><a name="p29786826142619"></a><a name="p29786826142619"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="20.28%" headers="mcps1.1.5.1.3 "><p id="p63922711142619"><a name="p63922711142619"></a><a name="p63922711142619"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="43.230000000000004%" headers="mcps1.1.5.1.4 "><p id="p7663085204619"><a name="p7663085204619"></a><a name="p7663085204619"></a>Indicates the status of the provider's connection.</p>
<p id="p10357121142619"><a name="p10357121142619"></a><a name="p10357121142619"></a>The value can be <strong id="b842352706171439"><a name="b842352706171439"></a><a name="b842352706171439"></a>ACTIVE</strong>&nbsp;or&nbsp;<strong id="b842352706171443"><a name="b842352706171443"></a><a name="b842352706171443"></a>DOWN</strong>.</p>
</td>
</tr>
<tr id="row23638404155151"><td class="cellrowborder" valign="top" width="23.71%" headers="mcps1.1.5.1.1 "><p id="p28145070155158"><a name="p28145070155158"></a><a name="p28145070155158"></a>order_id</p>
</td>
<td class="cellrowborder" valign="top" width="12.78%" headers="mcps1.1.5.1.2 "><p id="p65158236155158"><a name="p65158236155158"></a><a name="p65158236155158"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="20.28%" headers="mcps1.1.5.1.3 "><p id="p43325774155158"><a name="p43325774155158"></a><a name="p43325774155158"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="43.230000000000004%" headers="mcps1.1.5.1.4 "><p id="p19726829155158"><a name="p19726829155158"></a><a name="p19726829155158"></a>Indicates the order number of a connection.</p>
</td>
</tr>
<tr id="row48447356155155"><td class="cellrowborder" valign="top" width="23.71%" headers="mcps1.1.5.1.1 "><p id="p19561765155158"><a name="p19561765155158"></a><a name="p19561765155158"></a>product_id</p>
</td>
<td class="cellrowborder" valign="top" width="12.78%" headers="mcps1.1.5.1.2 "><p id="p40999122155158"><a name="p40999122155158"></a><a name="p40999122155158"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="20.28%" headers="mcps1.1.5.1.3 "><p id="p32594567155158"><a name="p32594567155158"></a><a name="p32594567155158"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="43.230000000000004%" headers="mcps1.1.5.1.4 "><p id="p22914285155158"><a name="p22914285155158"></a><a name="p22914285155158"></a>Indicates the product ID corresponding to a connection order.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section57838187"></a>

[Table 3](#table49073182143140)  lists the response parameter.

**Table  3**  Response parameter

<a name="table49073182143140"></a>
<table><thead align="left"><tr id="row41888921143140"><th class="cellrowborder" valign="top" width="30.76307630763076%" id="mcps1.2.4.1.1"><p id="p37559451143140"><a name="p37559451143140"></a><a name="p37559451143140"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.34193419341934%" id="mcps1.2.4.1.2"><p id="p3814541143140"><a name="p3814541143140"></a><a name="p3814541143140"></a><strong id="b84235270693914"><a name="b84235270693914"></a><a name="b84235270693914"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="49.89498949894989%" id="mcps1.2.4.1.3"><p id="p40542413143140"><a name="p40542413143140"></a><a name="p40542413143140"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row62710001143140"><td class="cellrowborder" valign="top" width="30.76307630763076%" headers="mcps1.2.4.1.1 "><p id="p46345314143140"><a name="p46345314143140"></a><a name="p46345314143140"></a>direct_connect</p>
</td>
<td class="cellrowborder" valign="top" width="19.34193419341934%" headers="mcps1.2.4.1.2 "><p id="p1342792143140"><a name="p1342792143140"></a><a name="p1342792143140"></a>Dictionary data structure</p>
</td>
<td class="cellrowborder" valign="top" width="49.89498949894989%" headers="mcps1.2.4.1.3 "><p id="p39371911143140"><a name="p39371911143140"></a><a name="p39371911143140"></a>Indicates the <strong id="b842352706172942"><a name="b842352706172942"></a><a name="b842352706172942"></a>direct_connect</strong> object.</p>
</td>
</tr>
</tbody>
</table>

Description of field  **direct\_connect**

<a name="table49261880"></a>
<table><thead align="left"><tr id="row31386613"><th class="cellrowborder" valign="top" width="31.7%" id="mcps1.1.4.1.1"><p id="p59287744"><a name="p59287744"></a><a name="p59287744"></a><strong id="b8423527069918_1"><a name="b8423527069918_1"></a><a name="b8423527069918_1"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.080000000000002%" id="mcps1.1.4.1.2"><p id="p37577972"><a name="p37577972"></a><a name="p37577972"></a><strong id="b842352706165439_3"><a name="b842352706165439_3"></a><a name="b842352706165439_3"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51.22%" id="mcps1.1.4.1.3"><p id="p58217140"><a name="p58217140"></a><a name="p58217140"></a><strong id="b84235270615331_2"><a name="b84235270615331_2"></a><a name="b84235270615331_2"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row22599309142540"><td class="cellrowborder" valign="top" width="31.7%" headers="mcps1.1.4.1.1 "><p id="p65683489142540"><a name="p65683489142540"></a><a name="p65683489142540"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="17.080000000000002%" headers="mcps1.1.4.1.2 "><p id="p18762424142540"><a name="p18762424142540"></a><a name="p18762424142540"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.1.4.1.3 "><p id="p22607505142540"><a name="p22607505142540"></a><a name="p22607505142540"></a>Indicates the connection ID.</p>
</td>
</tr>
<tr id="row2511034142540"><td class="cellrowborder" valign="top" width="31.7%" headers="mcps1.1.4.1.1 "><p id="p39200081142540"><a name="p39200081142540"></a><a name="p39200081142540"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.080000000000002%" headers="mcps1.1.4.1.2 "><p id="p21089994142540"><a name="p21089994142540"></a><a name="p21089994142540"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.1.4.1.3 "><p id="p60087991142540"><a name="p60087991142540"></a><a name="p60087991142540"></a>Indicates the project ID.</p>
</td>
</tr>
<tr id="row59931327142540"><td class="cellrowborder" valign="top" width="31.7%" headers="mcps1.1.4.1.1 "><p id="p49166283142540"><a name="p49166283142540"></a><a name="p49166283142540"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="17.080000000000002%" headers="mcps1.1.4.1.2 "><p id="p23045969142540"><a name="p23045969142540"></a><a name="p23045969142540"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.1.4.1.3 "><p id="p8338180142540"><a name="p8338180142540"></a><a name="p8338180142540"></a>Indicates the connection name.</p>
</td>
</tr>
<tr id="row58854819142540"><td class="cellrowborder" valign="top" width="31.7%" headers="mcps1.1.4.1.1 "><p id="p38736008142540"><a name="p38736008142540"></a><a name="p38736008142540"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="17.080000000000002%" headers="mcps1.1.4.1.2 "><p id="p50608918142540"><a name="p50608918142540"></a><a name="p50608918142540"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.1.4.1.3 "><p id="p57561315142540"><a name="p57561315142540"></a><a name="p57561315142540"></a>Provides supplementary information about the connection.</p>
</td>
</tr>
<tr id="row28909045142540"><td class="cellrowborder" valign="top" width="31.7%" headers="mcps1.1.4.1.1 "><p id="p19158921142540"><a name="p19158921142540"></a><a name="p19158921142540"></a>port_type</p>
</td>
<td class="cellrowborder" valign="top" width="17.080000000000002%" headers="mcps1.1.4.1.2 "><p id="p8368744142540"><a name="p8368744142540"></a><a name="p8368744142540"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.1.4.1.3 "><p id="p3460603522620"><a name="p3460603522620"></a><a name="p3460603522620"></a>Indicates the type of the port used by the connection. The value can be <strong id="b370581214151058"><a name="b370581214151058"></a><a name="b370581214151058"></a>1G</strong>&nbsp;or&nbsp;<strong id="b263825441151058"><a name="b263825441151058"></a><a name="b263825441151058"></a>10G</strong>.</p>
</td>
</tr>
<tr id="row18125197142540"><td class="cellrowborder" valign="top" width="31.7%" headers="mcps1.1.4.1.1 "><p id="p57768785142540"><a name="p57768785142540"></a><a name="p57768785142540"></a>bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="17.080000000000002%" headers="mcps1.1.4.1.2 "><p id="p48760032142540"><a name="p48760032142540"></a><a name="p48760032142540"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.1.4.1.3 "><p id="p6618147142540"><a name="p6618147142540"></a><a name="p6618147142540"></a>Indicates the bandwidth used by the connection (unit: Mbit/s).</p>
</td>
</tr>
<tr id="row31840072142540"><td class="cellrowborder" valign="top" width="31.7%" headers="mcps1.1.4.1.1 "><p id="p59900002142540"><a name="p59900002142540"></a><a name="p59900002142540"></a>location</p>
</td>
<td class="cellrowborder" valign="top" width="17.080000000000002%" headers="mcps1.1.4.1.2 "><p id="p20062008142540"><a name="p20062008142540"></a><a name="p20062008142540"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.1.4.1.3 "><p id="p26355989142540"><a name="p26355989142540"></a><a name="p26355989142540"></a>Indicates the connection access location.</p>
</td>
</tr>
<tr id="row25907407142540"><td class="cellrowborder" valign="top" width="31.7%" headers="mcps1.1.4.1.1 "><p id="p20381527142540"><a name="p20381527142540"></a><a name="p20381527142540"></a>peer_location</p>
</td>
<td class="cellrowborder" valign="top" width="17.080000000000002%" headers="mcps1.1.4.1.2 "><p id="p40291006142540"><a name="p40291006142540"></a><a name="p40291006142540"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.1.4.1.3 "><p id="p7480618142540"><a name="p7480618142540"></a><a name="p7480618142540"></a>Indicates the physical location of the peer device accessed by the connection. The value can be a street, city, and province, or an IDC.</p>
</td>
</tr>
<tr id="row55074383142540"><td class="cellrowborder" valign="top" width="31.7%" headers="mcps1.1.4.1.1 "><p id="p17553017142540"><a name="p17553017142540"></a><a name="p17553017142540"></a>device_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.080000000000002%" headers="mcps1.1.4.1.2 "><p id="p12508300142540"><a name="p12508300142540"></a><a name="p12508300142540"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.1.4.1.3 "><p id="p59926042142540"><a name="p59926042142540"></a><a name="p59926042142540"></a>Indicates the gateway device ID of the connection.</p>
</td>
</tr>
<tr id="row35945537142540"><td class="cellrowborder" valign="top" width="31.7%" headers="mcps1.1.4.1.1 "><p id="p65323418142540"><a name="p65323418142540"></a><a name="p65323418142540"></a>interface_name</p>
</td>
<td class="cellrowborder" valign="top" width="17.080000000000002%" headers="mcps1.1.4.1.2 "><p id="p56705473142540"><a name="p56705473142540"></a><a name="p56705473142540"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.1.4.1.3 "><p id="p60180134142540"><a name="p60180134142540"></a><a name="p60180134142540"></a>Indicates the name of the interface accessed by the connection.</p>
</td>
</tr>
<tr id="row55182886203023"><td class="cellrowborder" valign="top" width="31.7%" headers="mcps1.1.4.1.1 "><p id="p19964412203025"><a name="p19964412203025"></a><a name="p19964412203025"></a>redundant_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.080000000000002%" headers="mcps1.1.4.1.2 "><p id="p6504657203025"><a name="p6504657203025"></a><a name="p6504657203025"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.1.4.1.3 "><p id="p62930357203025"><a name="p62930357203025"></a><a name="p62930357203025"></a>Indicates the ID of the redundant connection using the same gateway.</p>
</td>
</tr>
<tr id="row56189731142540"><td class="cellrowborder" valign="top" width="31.7%" headers="mcps1.1.4.1.1 "><p id="p49229905142540"><a name="p49229905142540"></a><a name="p49229905142540"></a>provider</p>
</td>
<td class="cellrowborder" valign="top" width="17.080000000000002%" headers="mcps1.1.4.1.2 "><p id="p28199368142540"><a name="p28199368142540"></a><a name="p28199368142540"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.1.4.1.3 "><p id="p29079571213632"><a name="p29079571213632"></a><a name="p29079571213632"></a>Indicates the connection provider.</p>
</td>
</tr>
<tr id="row28612924142540"><td class="cellrowborder" valign="top" width="31.7%" headers="mcps1.1.4.1.1 "><p id="p25972590145747"><a name="p25972590145747"></a><a name="p25972590145747"></a>provider_status</p>
</td>
<td class="cellrowborder" valign="top" width="17.080000000000002%" headers="mcps1.1.4.1.2 "><p id="p45405558145747"><a name="p45405558145747"></a><a name="p45405558145747"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.1.4.1.3 "><p id="p65643981145747"><a name="p65643981145747"></a><a name="p65643981145747"></a>Indicates the status of the provider's connection. The value can be <strong id="b842352706171439_1"><a name="b842352706171439_1"></a><a name="b842352706171439_1"></a>ACTIVE</strong>&nbsp;or&nbsp;<strong id="b842352706171443_1"><a name="b842352706171443_1"></a><a name="b842352706171443_1"></a>DOWN</strong>.</p>
</td>
</tr>
<tr id="row47589257115128"><td class="cellrowborder" valign="top" width="31.7%" headers="mcps1.1.4.1.1 "><p id="p5179354011524"><a name="p5179354011524"></a><a name="p5179354011524"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="17.080000000000002%" headers="mcps1.1.4.1.2 "><p id="p3452724911524"><a name="p3452724911524"></a><a name="p3452724911524"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.1.4.1.3 "><p id="p1322174519119"><a name="p1322174519119"></a><a name="p1322174519119"></a>Indicates the connection type. The value can be <strong id="b842352706152446"><a name="b842352706152446"></a><a name="b842352706152446"></a>hosted</strong>.</p>
</td>
</tr>
<tr id="row5044245115125"><td class="cellrowborder" valign="top" width="31.7%" headers="mcps1.1.4.1.1 "><p id="p6285975011524"><a name="p6285975011524"></a><a name="p6285975011524"></a>hosting_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.080000000000002%" headers="mcps1.1.4.1.2 "><p id="p5847496711524"><a name="p5847496711524"></a><a name="p5847496711524"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.1.4.1.3 "><p id="p5999761611524"><a name="p5999761611524"></a><a name="p5999761611524"></a>Indicates the ID of the hosting connection mapped to the hosted connection.</p>
</td>
</tr>
<tr id="row40288765115138"><td class="cellrowborder" valign="top" width="31.7%" headers="mcps1.1.4.1.1 "><p id="p5039210211524"><a name="p5039210211524"></a><a name="p5039210211524"></a>vlan</p>
</td>
<td class="cellrowborder" valign="top" width="17.080000000000002%" headers="mcps1.1.4.1.2 "><p id="p5522847111524"><a name="p5522847111524"></a><a name="p5522847111524"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.1.4.1.3 "><p id="p3324489011524"><a name="p3324489011524"></a><a name="p3324489011524"></a>Indicates the pre-allocated VLAN to the hosted connection.</p>
</td>
</tr>
<tr id="row22890687115136"><td class="cellrowborder" valign="top" width="31.7%" headers="mcps1.1.4.1.1 "><p id="p6349203911524"><a name="p6349203911524"></a><a name="p6349203911524"></a>charge_mode</p>
</td>
<td class="cellrowborder" valign="top" width="17.080000000000002%" headers="mcps1.1.4.1.2 "><p id="p4258157111524"><a name="p4258157111524"></a><a name="p4258157111524"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.1.4.1.3 "><p id="p348712611524"><a name="p348712611524"></a><a name="p348712611524"></a>Indicates the billing mode. The value can be <strong id="b842352706153349"><a name="b842352706153349"></a><a name="b842352706153349"></a>prepayment</strong>,&nbsp;<strong id="b842352706153353"><a name="b842352706153353"></a><a name="b842352706153353"></a>bandwidth</strong>, or&nbsp;<strong id="b842352706153357"><a name="b842352706153357"></a><a name="b842352706153357"></a>traffic</strong>.</p>
</td>
</tr>
<tr id="row27967388115133"><td class="cellrowborder" valign="top" width="31.7%" headers="mcps1.1.4.1.1 "><p id="p5908754811524"><a name="p5908754811524"></a><a name="p5908754811524"></a>apply_time</p>
</td>
<td class="cellrowborder" valign="top" width="17.080000000000002%" headers="mcps1.1.4.1.2 "><p id="p2136205011524"><a name="p2136205011524"></a><a name="p2136205011524"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.1.4.1.3 "><p id="p3310520811524"><a name="p3310520811524"></a><a name="p3310520811524"></a>Indicates the time when the connection is applied for.</p>
</td>
</tr>
<tr id="row45018349115130"><td class="cellrowborder" valign="top" width="31.7%" headers="mcps1.1.4.1.1 "><p id="p4161503811524"><a name="p4161503811524"></a><a name="p4161503811524"></a>create_time</p>
</td>
<td class="cellrowborder" valign="top" width="17.080000000000002%" headers="mcps1.1.4.1.2 "><p id="p1537490611524"><a name="p1537490611524"></a><a name="p1537490611524"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.1.4.1.3 "><p id="p1013568611524"><a name="p1013568611524"></a><a name="p1013568611524"></a>Indicates the time when the connection is created.</p>
</td>
</tr>
<tr id="row46380176115122"><td class="cellrowborder" valign="top" width="31.7%" headers="mcps1.1.4.1.1 "><p id="p694064711524"><a name="p694064711524"></a><a name="p694064711524"></a>delete_time</p>
</td>
<td class="cellrowborder" valign="top" width="17.080000000000002%" headers="mcps1.1.4.1.2 "><p id="p2532155411524"><a name="p2532155411524"></a><a name="p2532155411524"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.1.4.1.3 "><p id="p4028160911524"><a name="p4028160911524"></a><a name="p4028160911524"></a>Indicates the time when the connection is deleted.</p>
</td>
</tr>
<tr id="row56810208155212"><td class="cellrowborder" valign="top" width="31.7%" headers="mcps1.1.4.1.1 "><p id="p53102936155216"><a name="p53102936155216"></a><a name="p53102936155216"></a>order_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.080000000000002%" headers="mcps1.1.4.1.2 "><p id="p6370564155216"><a name="p6370564155216"></a><a name="p6370564155216"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.1.4.1.3 "><p id="p55559981155216"><a name="p55559981155216"></a><a name="p55559981155216"></a>Indicates the order number of a connection.</p>
</td>
</tr>
<tr id="row49611415529"><td class="cellrowborder" valign="top" width="31.7%" headers="mcps1.1.4.1.1 "><p id="p36581716155216"><a name="p36581716155216"></a><a name="p36581716155216"></a>product_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.080000000000002%" headers="mcps1.1.4.1.2 "><p id="p10329025155216"><a name="p10329025155216"></a><a name="p10329025155216"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.1.4.1.3 "><p id="p55893977155216"><a name="p55893977155216"></a><a name="p55893977155216"></a>Indicates the product ID corresponding to a connection order.</p>
</td>
</tr>
<tr id="row40461916142540"><td class="cellrowborder" valign="top" width="31.7%" headers="mcps1.1.4.1.1 "><p id="p28875525145747"><a name="p28875525145747"></a><a name="p28875525145747"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="17.080000000000002%" headers="mcps1.1.4.1.2 "><p id="p50531229145747"><a name="p50531229145747"></a><a name="p50531229145747"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.1.4.1.3 "><p id="p9078857145747"><a name="p9078857145747"></a><a name="p9078857145747"></a>Indicates the connection status. The value can be <strong id="b84235270617169"><a name="b84235270617169"></a><a name="b84235270617169"></a>ACTIVE</strong>,&nbsp;<strong id="b842352706171613"><a name="b842352706171613"></a><a name="b842352706171613"></a>DOWN</strong>,&nbsp;<strong id="b842352706171618"><a name="b842352706171618"></a><a name="b842352706171618"></a>BUILD</strong>,&nbsp;<strong id="b842352706171622"><a name="b842352706171622"></a><a name="b842352706171622"></a>ERROR</strong>,&nbsp;<strong id="b573557709231737"><a name="b573557709231737"></a><a name="b573557709231737"></a>PENDING_DELETE</strong>,&nbsp;<strong id="b810642512231737"><a name="b810642512231737"></a><a name="b810642512231737"></a>DELETED</strong>,&nbsp;<strong id="b17872564231737"><a name="b17872564231737"></a><a name="b17872564231737"></a>APPLY</strong>,&nbsp;<strong id="b1765160533231737"><a name="b1765160533231737"></a><a name="b1765160533231737"></a>DENY</strong>,&nbsp;<strong id="b1723423809231737"><a name="b1723423809231737"></a><a name="b1723423809231737"></a>PENDING_PAY</strong>,&nbsp;<strong id="b733428447231737"><a name="b733428447231737"></a><a name="b733428447231737"></a>PAID</strong>,&nbsp;<strong id="b1888084103231737"><a name="b1888084103231737"></a><a name="b1888084103231737"></a>ORDERING</strong>,&nbsp;<strong id="b842352706151915"><a name="b842352706151915"></a><a name="b842352706151915"></a>ACCEPT</strong>, or&nbsp;<strong id="b1504845468231737"><a name="b1504845468231737"></a><a name="b1504845468231737"></a>REJECTED</strong>.</p>
</td>
</tr>
<tr id="row4495768142540"><td class="cellrowborder" valign="top" width="31.7%" headers="mcps1.1.4.1.1 "><p id="p59711547142540"><a name="p59711547142540"></a><a name="p59711547142540"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="17.080000000000002%" headers="mcps1.1.4.1.2 "><p id="p4797178142540"><a name="p4797178142540"></a><a name="p4797178142540"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.1.4.1.3 "><p id="p11577326204655"><a name="p11577326204655"></a><a name="p11577326204655"></a>Indicates the administrative state of the connection.</p>
<p id="p233498142540"><a name="p233498142540"></a><a name="p233498142540"></a>The value can be <strong id="b842352706154840"><a name="b842352706154840"></a><a name="b842352706154840"></a>true</strong>&nbsp;or&nbsp;<strong id="b842352706154844"><a name="b842352706154844"></a><a name="b842352706154844"></a>false</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="section5055526711495"></a>

-   Example request

    ```
    PUT /v2.0/dcaas/direct-connects/{direct_connect_id}
    {
        "direct_connect" : {
            "name" : "direct connect1",
            "description" : "New description"
        }
    }
    ```


-   Example response

    ```
    {
        "direct_connect" : {
            "id" : "6ecd9cf3-ca64-46c7-863f-f2eb1b9e838a",        
            "tenant_id" : "6fbe9263116a4b68818cf1edce16bc4f",
            "name" : "direct connect1",
            "description" : "",
            "port_type" : "10G",
            "bandwidth" : 100,
            "location" : "Biere", 
            "device_id" : "172.16.40.2", 
            "provider" : "OTC"
        }
    }
    ```


## Returned Value<a name="section178941713364"></a>

For details, see section  [Common Returned Values](common-returned-values.md).

