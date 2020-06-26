# Querying Routers<a name="vpc_router_0001"></a>

## Function<a name="section55573059205730"></a>

This API is used to query all routers accessible to the tenant submitting the request. 

## URI<a name="section46115681205730"></a>

GET /v2.0/routers

Example:

```
GET https://{Endpoint}/v2.0/routers?id={id}&name={name}&admin_state_up={admin_state_up}&tenant_id={tenant_id}&status={status}
```

Example of querying routers by page

```
GET https://{Endpoint}/v2.0/routers?limit=2&marker=01ab4be1-4447-45fb-94be-3ee787ed4ebe&page_reverse=False
```

[Table 1](#table966161441716)  describes the parameters.

**Table  1**  Parameter description

<a name="table966161441716"></a>
<table><thead align="left"><tr id="row57831214171715"><th class="cellrowborder" valign="top" width="22.222222222222225%" id="mcps1.2.5.1.1"><p id="p1478361451716"><a name="p1478361451716"></a><a name="p1478361451716"></a><strong id="b156013111152"><a name="b156013111152"></a><a name="b156013111152"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="12.91129112911291%" id="mcps1.2.5.1.2"><p id="p57832145174"><a name="p57832145174"></a><a name="p57832145174"></a><strong id="b6828131410513"><a name="b6828131410513"></a><a name="b6828131410513"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="13.211321132113211%" id="mcps1.2.5.1.3"><p id="p167831314131711"><a name="p167831314131711"></a><a name="p167831314131711"></a><strong id="b107808151453"><a name="b107808151453"></a><a name="b107808151453"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51.65516551655165%" id="mcps1.2.5.1.4"><p id="p137831144177"><a name="p137831144177"></a><a name="p137831144177"></a><strong id="b132837171353"><a name="b132837171353"></a><a name="b132837171353"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1078441451720"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p1778416144170"><a name="p1778416144170"></a><a name="p1778416144170"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="12.91129112911291%" headers="mcps1.2.5.1.2 "><p id="p67842143178"><a name="p67842143178"></a><a name="p67842143178"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.211321132113211%" headers="mcps1.2.5.1.3 "><p id="p15784191431717"><a name="p15784191431717"></a><a name="p15784191431717"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.65516551655165%" headers="mcps1.2.5.1.4 "><p id="p1478441481719"><a name="p1478441481719"></a><a name="p1478441481719"></a>Specifies that the router ID is used as the filtering condition.</p>
</td>
</tr>
<tr id="row14784101461711"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p207841314171712"><a name="p207841314171712"></a><a name="p207841314171712"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="12.91129112911291%" headers="mcps1.2.5.1.2 "><p id="p107841014181716"><a name="p107841014181716"></a><a name="p107841014181716"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.211321132113211%" headers="mcps1.2.5.1.3 "><p id="p878418146174"><a name="p878418146174"></a><a name="p878418146174"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="51.65516551655165%" headers="mcps1.2.5.1.4 "><p id="p1476743711713"><a name="p1476743711713"></a><a name="p1476743711713"></a>Specifies that the admin state is used as the filtering condition.</p>
<p id="p1078421441710"><a name="p1078421441710"></a><a name="p1078421441710"></a>The value can be <strong id="b45964291519"><a name="b45964291519"></a><a name="b45964291519"></a>true</strong> or <strong id="b125961629055"><a name="b125961629055"></a><a name="b125961629055"></a>false</strong>.</p>
</td>
</tr>
<tr id="row078411140178"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p187841514141717"><a name="p187841514141717"></a><a name="p187841514141717"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="12.91129112911291%" headers="mcps1.2.5.1.2 "><p id="p1578417147173"><a name="p1578417147173"></a><a name="p1578417147173"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.211321132113211%" headers="mcps1.2.5.1.3 "><p id="p10784151415173"><a name="p10784151415173"></a><a name="p10784151415173"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.65516551655165%" headers="mcps1.2.5.1.4 "><p id="p16910184011710"><a name="p16910184011710"></a><a name="p16910184011710"></a>Specifies that the router status is used as the filtering condition.</p>
<p id="p478431431718"><a name="p478431431718"></a><a name="p478431431718"></a>The value can be <strong id="b18546440858"><a name="b18546440858"></a><a name="b18546440858"></a>ACTIVE</strong>, <strong id="b195691114612"><a name="b195691114612"></a><a name="b195691114612"></a>DOWN</strong>, or <strong id="b154616401456"><a name="b154616401456"></a><a name="b154616401456"></a>DOWN</strong>.</p>
</td>
</tr>
<tr id="row87841014181710"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p37841149177"><a name="p37841149177"></a><a name="p37841149177"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="12.91129112911291%" headers="mcps1.2.5.1.2 "><p id="p13784151421713"><a name="p13784151421713"></a><a name="p13784151421713"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.211321132113211%" headers="mcps1.2.5.1.3 "><p id="p12784161411177"><a name="p12784161411177"></a><a name="p12784161411177"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.65516551655165%" headers="mcps1.2.5.1.4 "><p id="p6784131461718"><a name="p6784131461718"></a><a name="p6784131461718"></a>Specifies that the project ID is used as the filtering condition.</p>
</td>
</tr>
<tr id="row37841314121714"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p14784191491715"><a name="p14784191491715"></a><a name="p14784191491715"></a>marker</p>
</td>
<td class="cellrowborder" valign="top" width="12.91129112911291%" headers="mcps1.2.5.1.2 "><p id="p8784141471714"><a name="p8784141471714"></a><a name="p8784141471714"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.211321132113211%" headers="mcps1.2.5.1.3 "><p id="p13784161412171"><a name="p13784161412171"></a><a name="p13784161412171"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.65516551655165%" headers="mcps1.2.5.1.4 "><p id="p97841914171711"><a name="p97841914171711"></a><a name="p97841914171711"></a>Specifies the start resource ID of pagination query. If the parameter is left blank, only resources on the first page are queried.</p>
</td>
</tr>
<tr id="row7784191491713"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p278491421719"><a name="p278491421719"></a><a name="p278491421719"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="12.91129112911291%" headers="mcps1.2.5.1.2 "><p id="p278431415173"><a name="p278431415173"></a><a name="p278431415173"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.211321132113211%" headers="mcps1.2.5.1.3 "><p id="p7784201411173"><a name="p7784201411173"></a><a name="p7784201411173"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="51.65516551655165%" headers="mcps1.2.5.1.4 "><p id="p4930114216172"><a name="p4930114216172"></a><a name="p4930114216172"></a>Specifies the number of records on each page.</p>
<p id="p1778421417179"><a name="p1778421417179"></a><a name="p1778421417179"></a>The value ranges from 0 to intmax.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section22539803205730"></a>

None

## Response Message<a name="section56953834205730"></a>

**Table  2**  Response parameter

<a name="table49857835205730"></a>
<table><thead align="left"><tr id="row16977544205730"><th class="cellrowborder" valign="top" width="21.349999999999998%" id="mcps1.2.4.1.1"><p id="p33003808205730"><a name="p33003808205730"></a><a name="p33003808205730"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.11%" id="mcps1.2.4.1.2"><p id="p56062768205730"><a name="p56062768205730"></a><a name="p56062768205730"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="59.540000000000006%" id="mcps1.2.4.1.3"><p id="p4141274205730"><a name="p4141274205730"></a><a name="p4141274205730"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row67007812205730"><td class="cellrowborder" valign="top" width="21.349999999999998%" headers="mcps1.2.4.1.1 "><p id="p58923719205730"><a name="p58923719205730"></a><a name="p58923719205730"></a>routers</p>
</td>
<td class="cellrowborder" valign="top" width="19.11%" headers="mcps1.2.4.1.2 "><p id="p166911588244"><a name="p166911588244"></a><a name="p166911588244"></a>Array of <a href="#table24153696181443">router</a> objects</p>
</td>
<td class="cellrowborder" valign="top" width="59.540000000000006%" headers="mcps1.2.4.1.3 "><p id="p7937265205730"><a name="p7937265205730"></a><a name="p7937265205730"></a>Specifies the router list. For details, see <a href="#table24153696181443">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **router**  objects

<a name="table24153696181443"></a>
<table><thead align="left"><tr id="row11861342181443"><th class="cellrowborder" valign="top" width="26.669999999999998%" id="mcps1.2.4.1.1"><p id="p21244677181443"><a name="p21244677181443"></a><a name="p21244677181443"></a><strong id="b12596154575614"><a name="b12596154575614"></a><a name="b12596154575614"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="23.330000000000002%" id="mcps1.2.4.1.2"><p id="p43097239181443"><a name="p43097239181443"></a><a name="p43097239181443"></a><strong id="b3295101414315"><a name="b3295101414315"></a><a name="b3295101414315"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p36728767181443"><a name="p36728767181443"></a><a name="p36728767181443"></a><strong id="b1976615636"><a name="b1976615636"></a><a name="b1976615636"></a>Description</strong></p>
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
<p id="p35120501181443"><a name="p35120501181443"></a><a name="p35120501181443"></a>The value can only be <strong id="b9364330194116"><a name="b9364330194116"></a><a name="b9364330194116"></a>true</strong>.</p>
</td>
</tr>
<tr id="row47649056181443"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p34368308181443"><a name="p34368308181443"></a><a name="p34368308181443"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p32369557181443"><a name="p32369557181443"></a><a name="p32369557181443"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p4016564181443"><a name="p4016564181443"></a><a name="p4016564181443"></a>Specifies the router status. The value can be <strong id="b842352706144324"><a name="b842352706144324"></a><a name="b842352706144324"></a>ACTIVE</strong>, <strong id="b842352706144328"><a name="b842352706144328"></a><a name="b842352706144328"></a>DOWN</strong>, or <strong id="b842352706144332"><a name="b842352706144332"></a><a name="b842352706144332"></a>ERROR</strong>.</p>
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
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p12911840181443"><a name="p12911840181443"></a><a name="p12911840181443"></a>Specifies the external gateway. This is an extended attribute. For details, see the <strong id="b842352706144447"><a name="b842352706144447"></a><a name="b842352706144447"></a>external_gateway_info</strong> objects.</p>
</td>
</tr>
<tr id="row49097702181443"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p17490925181443"><a name="p17490925181443"></a><a name="p17490925181443"></a>routes</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p7478812181443"><a name="p7478812181443"></a><a name="p7478812181443"></a>Array of <a href="#table18829650181443">route</a> objects</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p5122123194853"><a name="p5122123194853"></a><a name="p5122123194853"></a>Specifies a route list. This is an extended attribute. For details, see <a href="#table18829650181443">Table 5</a>.</p>
</td>
</tr>
<tr id="row7278189151614"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p870051413911"><a name="p870051413911"></a><a name="p870051413911"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p15700614790"><a name="p15700614790"></a><a name="p15700614790"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p960410518269"><a name="p960410518269"></a><a name="p960410518269"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row172292215166"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p1953114119914"><a name="p1953114119914"></a><a name="p1953114119914"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p595318416919"><a name="p595318416919"></a><a name="p595318416919"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1395374115919"><a name="p1395374115919"></a><a name="p1395374115919"></a>Specifies the time (UTC) when the router is created.</p>
<p id="p65980291419"><a name="p65980291419"></a><a name="p65980291419"></a>Format: <em id="i1191819548534"><a name="i1191819548534"></a><a name="i1191819548534"></a>yyyy-MM-ddTHH:mm:ss</em></p>
</td>
</tr>
<tr id="row106341917161611"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p139719548912"><a name="p139719548912"></a><a name="p139719548912"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p53971154594"><a name="p53971154594"></a><a name="p53971154594"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1339713549918"><a name="p1339713549918"></a><a name="p1339713549918"></a>Specifies the time (UTC) when the router is updated.</p>
<p id="p318184844718"><a name="p318184844718"></a><a name="p318184844718"></a>Format: <em id="i1065865135417"><a name="i1065865135417"></a><a name="i1065865135417"></a>yyyy-MM-ddTHH:mm:ss</em></p>
</td>
</tr>
</tbody>
</table>

**Table  4** **external\_gateway\_info**  objects

<a name="table11448068181443"></a>
<table><thead align="left"><tr id="row58732356181443"><th class="cellrowborder" valign="top" width="26.669999999999998%" id="mcps1.2.4.1.1"><p id="p59700400181443"><a name="p59700400181443"></a><a name="p59700400181443"></a><strong id="b11687111547"><a name="b11687111547"></a><a name="b11687111547"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="23.34%" id="mcps1.2.4.1.2"><p id="p3894228181443"><a name="p3894228181443"></a><a name="p3894228181443"></a><strong id="b1215717126545"><a name="b1215717126545"></a><a name="b1215717126545"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="49.99%" id="mcps1.2.4.1.3"><p id="p1781307181443"><a name="p1781307181443"></a><a name="p1781307181443"></a><strong id="b7181151310541"><a name="b7181151310541"></a><a name="b7181151310541"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row10068178181443"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p10216081181443"><a name="p10216081181443"></a><a name="p10216081181443"></a>network_id</p>
</td>
<td class="cellrowborder" valign="top" width="23.34%" headers="mcps1.2.4.1.2 "><p id="p22196257181443"><a name="p22196257181443"></a><a name="p22196257181443"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.99%" headers="mcps1.2.4.1.3 "><p id="p38375206181443"><a name="p38375206181443"></a><a name="p38375206181443"></a>Specifies the UUID of the external network.</p>
<p id="p21383968181443"><a name="p21383968181443"></a><a name="p21383968181443"></a>You can use <strong id="b842352706145825"><a name="b842352706145825"></a><a name="b842352706145825"></a>GET /v2.0/networks?router:external=True</strong> or run the <strong id="b842352706145839"><a name="b842352706145839"></a><a name="b842352706145839"></a>neutron net-external-list</strong> command to query information about the external network.</p>
</td>
</tr>
<tr id="row58237990181443"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p19656760181443"><a name="p19656760181443"></a><a name="p19656760181443"></a>enable_snat</p>
</td>
<td class="cellrowborder" valign="top" width="23.34%" headers="mcps1.2.4.1.2 "><p id="p48693751181443"><a name="p48693751181443"></a><a name="p48693751181443"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="49.99%" headers="mcps1.2.4.1.3 "><p id="p22976335181443"><a name="p22976335181443"></a><a name="p22976335181443"></a>Specifies whether the SNAT function is enabled.</p>
<p id="p49143812181443"><a name="p49143812181443"></a><a name="p49143812181443"></a>The default value is <strong id="b1611643349143731"><a name="b1611643349143731"></a><a name="b1611643349143731"></a>false</strong>.</p>
</td>
</tr>
</tbody>
</table>

**Table  5** **route**  objects

<a name="table18829650181443"></a>
<table><thead align="left"><tr id="row60542282181443"><th class="cellrowborder" valign="top" width="26.669999999999998%" id="mcps1.2.4.1.1"><p id="p4977811181443"><a name="p4977811181443"></a><a name="p4977811181443"></a><strong id="b191835017558"><a name="b191835017558"></a><a name="b191835017558"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="23.34%" id="mcps1.2.4.1.2"><p id="p549581181443"><a name="p549581181443"></a><a name="p549581181443"></a><strong id="b153689135515"><a name="b153689135515"></a><a name="b153689135515"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="49.99%" id="mcps1.2.4.1.3"><p id="p9206714181443"><a name="p9206714181443"></a><a name="p9206714181443"></a><strong id="b124611220553"><a name="b124611220553"></a><a name="b124611220553"></a>Description</strong></p>
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

## Example:<a name="section4326525205730"></a>

Example request

```
GET https://{Endpoint}/v2.0/routers?limit=1
```

Example response

```
{
    "routers": [
        {
            "id": "01ab4be1-4447-45fb-94be-3ee787ed4ebe",
            "name": "xiaoleizi-tag",
            "status": "ACTIVE",
            "tenant_id": "bbfe8c41dd034a07bebd592bf03b4b0c",
            "project_id": "bbfe8c41dd034a07bebd592bf03b4b0c",
            "admin_state_up": true,
            "external_gateway_info": {
                "network_id": "0a2228f2-7f8a-45f1-8e09-9039e1d09975",
                "enable_snat": false
            },
            "routes": [
                {
                    "destination": "0.0.0.0/0",
                    "nexthop": "172.16.0.124"
                }
            ],
            "created_at": "2018-03-23T09:26:08",
            "updated_at": "2018-08-24T08:49:53"
        }
    ]
}
```

## Status Code<a name="section10470352390"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

