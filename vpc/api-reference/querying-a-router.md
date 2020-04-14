# Querying a Router<a name="vpc_router_0002"></a>

## Function<a name="section64937351205744"></a>

This API is used to query details about a router.

## URI<a name="section27580478205744"></a>

GET /v2.0/routers/\{router\_id\}

## Request Message<a name="section60819119205744"></a>

None

## Response Message<a name="section45287922205744"></a>

**Table  1**  Response parameter

<a name="table44443065205744"></a>
<table><thead align="left"><tr id="row61398570205744"><th class="cellrowborder" valign="top" width="23.169999999999998%" id="mcps1.2.4.1.1"><p id="p7228234205744"><a name="p7228234205744"></a><a name="p7228234205744"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25.61%" id="mcps1.2.4.1.2"><p id="p48616054205744"><a name="p48616054205744"></a><a name="p48616054205744"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51.22%" id="mcps1.2.4.1.3"><p id="p1505045205744"><a name="p1505045205744"></a><a name="p1505045205744"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row54799831205744"><td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p9601350205744"><a name="p9601350205744"></a><a name="p9601350205744"></a>router</p>
</td>
<td class="cellrowborder" valign="top" width="25.61%" headers="mcps1.2.4.1.2 "><p id="p39511881205744"><a name="p39511881205744"></a><a name="p39511881205744"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.2.4.1.3 "><p id="p63022381205744"><a name="p63022381205744"></a><a name="p63022381205744"></a>Specifies the router list. For details, see <a href="#table24153696181443">Table 2</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  2** **router**  objects

<a name="table24153696181443"></a>
<table><thead align="left"><tr id="row11861342181443"><th class="cellrowborder" valign="top" width="26.669999999999998%" id="mcps1.2.4.1.1"><p id="p21244677181443"><a name="p21244677181443"></a><a name="p21244677181443"></a><strong id="b5165727106"><a name="b5165727106"></a><a name="b5165727106"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="23.330000000000002%" id="mcps1.2.4.1.2"><p id="p43097239181443"><a name="p43097239181443"></a><a name="p43097239181443"></a><strong id="b18186163017016"><a name="b18186163017016"></a><a name="b18186163017016"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p36728767181443"><a name="p36728767181443"></a><a name="p36728767181443"></a><strong id="b126443115017"><a name="b126443115017"></a><a name="b126443115017"></a>Description</strong></p>
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
<p id="p35120501181443"><a name="p35120501181443"></a><a name="p35120501181443"></a>The value can only be <strong id="b171112050111"><a name="b171112050111"></a><a name="b171112050111"></a>true</strong>.</p>
</td>
</tr>
<tr id="row47649056181443"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p34368308181443"><a name="p34368308181443"></a><a name="p34368308181443"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p32369557181443"><a name="p32369557181443"></a><a name="p32369557181443"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p4016564181443"><a name="p4016564181443"></a><a name="p4016564181443"></a>Specifies the router status. The value can be <strong id="b192459531814"><a name="b192459531814"></a><a name="b192459531814"></a>ACTIVE</strong>, <strong id="b1324719531117"><a name="b1324719531117"></a><a name="b1324719531117"></a>DOWN</strong>, or <strong id="b1224915538110"><a name="b1224915538110"></a><a name="b1224915538110"></a>ERROR</strong>.</p>
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
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p12911840181443"><a name="p12911840181443"></a><a name="p12911840181443"></a>Specifies the external gateway. This is an extended attribute. For details, see the <strong id="b19279951920"><a name="b19279951920"></a><a name="b19279951920"></a>external_gateway_info</strong> objects.</p>
</td>
</tr>
<tr id="row49097702181443"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p17490925181443"><a name="p17490925181443"></a><a name="p17490925181443"></a>routes</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p7478812181443"><a name="p7478812181443"></a><a name="p7478812181443"></a>Array of <a href="#table18829650181443">route</a> objects</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p5122123194853"><a name="p5122123194853"></a><a name="p5122123194853"></a>Specifies a route list. This is an extended attribute. For details, see <a href="#table18829650181443">Table 4</a>.</p>
</td>
</tr>
<tr id="row7278189151614"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p870051413911"><a name="p870051413911"></a><a name="p870051413911"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p15700614790"><a name="p15700614790"></a><a name="p15700614790"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1506171582614"><a name="p1506171582614"></a><a name="p1506171582614"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row172292215166"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p1953114119914"><a name="p1953114119914"></a><a name="p1953114119914"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p595318416919"><a name="p595318416919"></a><a name="p595318416919"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1395374115919"><a name="p1395374115919"></a><a name="p1395374115919"></a>Specifies the time (UTC) when the router is created.</p>
<p id="p65980291419"><a name="p65980291419"></a><a name="p65980291419"></a>Format: <em id="i16550616317"><a name="i16550616317"></a><a name="i16550616317"></a>yyyy-MM-ddTHH:mm:ss</em></p>
</td>
</tr>
<tr id="row106341917161611"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p139719548912"><a name="p139719548912"></a><a name="p139719548912"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p53971154594"><a name="p53971154594"></a><a name="p53971154594"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1339713549918"><a name="p1339713549918"></a><a name="p1339713549918"></a>Specifies the time (UTC) when the router is updated.</p>
<p id="p1475019214481"><a name="p1475019214481"></a><a name="p1475019214481"></a>Format: <em id="i72145282310"><a name="i72145282310"></a><a name="i72145282310"></a>yyyy-MM-ddTHH:mm:ss</em></p>
</td>
</tr>
</tbody>
</table>

**Table  3** **external\_gateway\_info**  objects

<a name="table11448068181443"></a>
<table><thead align="left"><tr id="row58732356181443"><th class="cellrowborder" valign="top" width="26.669999999999998%" id="mcps1.2.4.1.1"><p id="p59700400181443"><a name="p59700400181443"></a><a name="p59700400181443"></a><strong id="b19991031036"><a name="b19991031036"></a><a name="b19991031036"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="23.34%" id="mcps1.2.4.1.2"><p id="p3894228181443"><a name="p3894228181443"></a><a name="p3894228181443"></a><strong id="b719714335319"><a name="b719714335319"></a><a name="b719714335319"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="49.99%" id="mcps1.2.4.1.3"><p id="p1781307181443"><a name="p1781307181443"></a><a name="p1781307181443"></a><strong id="b1693341135"><a name="b1693341135"></a><a name="b1693341135"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row10068178181443"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p10216081181443"><a name="p10216081181443"></a><a name="p10216081181443"></a>network_id</p>
</td>
<td class="cellrowborder" valign="top" width="23.34%" headers="mcps1.2.4.1.2 "><p id="p22196257181443"><a name="p22196257181443"></a><a name="p22196257181443"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.99%" headers="mcps1.2.4.1.3 "><p id="p38375206181443"><a name="p38375206181443"></a><a name="p38375206181443"></a>Specifies the UUID of the external network.</p>
<p id="p21383968181443"><a name="p21383968181443"></a><a name="p21383968181443"></a>You can use <strong id="b1686716381739"><a name="b1686716381739"></a><a name="b1686716381739"></a>GET /v2.0/networks?router:external=True</strong> or run the <strong id="b1486916381837"><a name="b1486916381837"></a><a name="b1486916381837"></a>neutron net-external-list</strong> command to query information about the external network.</p>
</td>
</tr>
<tr id="row58237990181443"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p19656760181443"><a name="p19656760181443"></a><a name="p19656760181443"></a>enable_snat</p>
</td>
<td class="cellrowborder" valign="top" width="23.34%" headers="mcps1.2.4.1.2 "><p id="p48693751181443"><a name="p48693751181443"></a><a name="p48693751181443"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="49.99%" headers="mcps1.2.4.1.3 "><p id="p22976335181443"><a name="p22976335181443"></a><a name="p22976335181443"></a>Specifies whether the SNAT function is enabled.</p>
<p id="p49143812181443"><a name="p49143812181443"></a><a name="p49143812181443"></a>The default value is <strong id="b2966153841"><a name="b2966153841"></a><a name="b2966153841"></a>false</strong>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **route**  objects

<a name="table18829650181443"></a>
<table><thead align="left"><tr id="row60542282181443"><th class="cellrowborder" valign="top" width="26.669999999999998%" id="mcps1.2.4.1.1"><p id="p4977811181443"><a name="p4977811181443"></a><a name="p4977811181443"></a><strong id="b18596126349"><a name="b18596126349"></a><a name="b18596126349"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="23.34%" id="mcps1.2.4.1.2"><p id="p549581181443"><a name="p549581181443"></a><a name="p549581181443"></a><strong id="b186141573417"><a name="b186141573417"></a><a name="b186141573417"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="49.99%" id="mcps1.2.4.1.3"><p id="p9206714181443"><a name="p9206714181443"></a><a name="p9206714181443"></a><strong id="b18402287420"><a name="b18402287420"></a><a name="b18402287420"></a>Description</strong></p>
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

## Example:<a name="section4539230205744"></a>

Example request

```
GET https://{Endpoint}/v2.0/routers/01ab4be1-4447-45fb-94be-3ee787ed4ebe
```

Example response

```
{
    "router": {
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
}
```

## Status Code<a name="section10470352390"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

