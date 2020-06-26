# Querying Resource Types<a name="EN-US_TOPIC_0084581312"></a>

## Function<a name="en-us_topic_0057973149_section22362409"></a>

This API is used to query resource types.

## URI<a name="en-us_topic_0057973149_section67043958"></a>

GET /v1/\{project\_id\}/resource\_types

For details about the parameters, see  [Table 1](#table1759528275).

**Table  1**  Parameter description

<a name="table1759528275"></a>
<table><thead align="left"><tr id="row26011272716"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p17762534144716"><a name="p17762534144716"></a><a name="p17762534144716"></a><strong id="b103051051101219"><a name="b103051051101219"></a><a name="b103051051101219"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p376433420478"><a name="p376433420478"></a><a name="p376433420478"></a><strong id="b430485215122"><a name="b430485215122"></a><a name="b430485215122"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p15766123474714"><a name="p15766123474714"></a><a name="p15766123474714"></a><strong id="b7654533127"><a name="b7654533127"></a><a name="b7654533127"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p147683349474"><a name="p147683349474"></a><a name="p147683349474"></a><strong id="b12893453141210"><a name="b12893453141210"></a><a name="b12893453141210"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row10601725277"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1765464961019"><a name="p1765464961019"></a><a name="p1765464961019"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p0655184916104"><a name="p0655184916104"></a><a name="p0655184916104"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p865694971017"><a name="p865694971017"></a><a name="p865694971017"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p13658144921010"><a name="p13658144921010"></a><a name="p13658144921010"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

## Request Parameter<a name="en-us_topic_0057973149_section66524715"></a>

N/A

## Response Parameter<a name="en-us_topic_0057973149_section61851530"></a>

<a name="en-us_topic_0057973149_table40331056"></a>
<table><thead align="left"><tr id="en-us_topic_0057973149_row44895264"><th class="cellrowborder" valign="top" width="15.478452154784522%" id="mcps1.1.5.1.1"><p id="p13701251185014"><a name="p13701251185014"></a><a name="p13701251185014"></a><strong id="b539517117139"><a name="b539517117139"></a><a name="b539517117139"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.478452154784522%" id="mcps1.1.5.1.2"><p id="p13704145119507"><a name="p13704145119507"></a><a name="p13704145119507"></a><strong id="b33678216136"><a name="b33678216136"></a><a name="b33678216136"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.478452154784522%" id="mcps1.1.5.1.3"><p id="p3705151185017"><a name="p3705151185017"></a><a name="p3705151185017"></a><strong id="b230317313137"><a name="b230317313137"></a><a name="b230317313137"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="53.564643535646425%" id="mcps1.1.5.1.4"><p id="p1371214511507"><a name="p1371214511507"></a><a name="p1371214511507"></a><strong id="b1621717431313"><a name="b1621717431313"></a><a name="b1621717431313"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973149_row1734575"><td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973149_p6282875"><a name="en-us_topic_0057973149_p6282875"></a><a name="en-us_topic_0057973149_p6282875"></a>resource_types</p>
</td>
<td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.2 "><p id="p9171630123118"><a name="p9171630123118"></a><a name="p9171630123118"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973149_p39150827"><a name="en-us_topic_0057973149_p39150827"></a><a name="en-us_topic_0057973149_p39150827"></a>List &lt;str&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="53.564643535646425%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973149_p42954456"><a name="en-us_topic_0057973149_p42954456"></a><a name="en-us_topic_0057973149_p42954456"></a>Specifies the resource type list.</p>
</td>
</tr>
</tbody>
</table>

## Request Example<a name="en-us_topic_0057973149_section19792858"></a>

```
GET /v1/95d02433133a4c0a87ba6967474a2ad3/resource_types
```

## Response Example<a name="en-us_topic_0057973149_section43917997"></a>

```
{
    "resource_types": [
        "OS::Nova::Server",
        "OS::Neutron::Net",
        "OS::Neutron::Port",
        "OS::Cinder::VolumeAttachment",
        "OS::Neutron::RouterInterface",
        "OS::Neutron::Router"
    ]
}
```

## Return Code<a name="en-us_topic_0057973149_section59717661"></a>

**Table  2**  Normal return code

<a name="table01411862119"></a>
<table><thead align="left"><tr id="en-us_topic_0084581285_en-us_topic_0057973117_row42419326194057"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="en-us_topic_0084581285_en-us_topic_0057973117_p13413377194057"><a name="en-us_topic_0084581285_en-us_topic_0057973117_p13413377194057"></a><a name="en-us_topic_0084581285_en-us_topic_0057973117_p13413377194057"></a><strong id="en-us_topic_0084581285_b14910172512114"><a name="en-us_topic_0084581285_b14910172512114"></a><a name="en-us_topic_0084581285_b14910172512114"></a>Return Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26%" id="mcps1.2.4.1.2"><p id="en-us_topic_0084581285_en-us_topic_0057973117_p12741761194057"><a name="en-us_topic_0084581285_en-us_topic_0057973117_p12741761194057"></a><a name="en-us_topic_0084581285_en-us_topic_0057973117_p12741761194057"></a><strong id="en-us_topic_0084581285_en-us_topic_0057973140_b84235270615814_1"><a name="en-us_topic_0084581285_en-us_topic_0057973140_b84235270615814_1"></a><a name="en-us_topic_0084581285_en-us_topic_0057973140_b84235270615814_1"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51%" id="mcps1.2.4.1.3"><p id="en-us_topic_0084581285_en-us_topic_0057973117_p25449701194057"><a name="en-us_topic_0084581285_en-us_topic_0057973117_p25449701194057"></a><a name="en-us_topic_0084581285_en-us_topic_0057973117_p25449701194057"></a><strong id="en-us_topic_0084581285_en-us_topic_0057973140_b842352706193020"><a name="en-us_topic_0084581285_en-us_topic_0057973140_b842352706193020"></a><a name="en-us_topic_0084581285_en-us_topic_0057973140_b842352706193020"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0084581285_en-us_topic_0057973117_row48159894194057"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0084581285_en-us_topic_0057973117_p8637307194057"><a name="en-us_topic_0084581285_en-us_topic_0057973117_p8637307194057"></a><a name="en-us_topic_0084581285_en-us_topic_0057973117_p8637307194057"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0084581285_en-us_topic_0057973117_p28533244194057"><a name="en-us_topic_0084581285_en-us_topic_0057973117_p28533244194057"></a><a name="en-us_topic_0084581285_en-us_topic_0057973117_p28533244194057"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0084581285_en-us_topic_0057973117_p29491459194057"><a name="en-us_topic_0084581285_en-us_topic_0057973117_p29491459194057"></a><a name="en-us_topic_0084581285_en-us_topic_0057973117_p29491459194057"></a>Request was successful.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Error return code

<a name="table19512103414"></a>
<table><thead align="left"><tr id="row16955110342"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="p129561510144"><a name="p129561510144"></a><a name="p129561510144"></a>Return Code</p>
</th>
<th class="cellrowborder" valign="top" width="26%" id="mcps1.2.4.1.2"><p id="p4959810444"><a name="p4959810444"></a><a name="p4959810444"></a><strong id="b2987612181317"><a name="b2987612181317"></a><a name="b2987612181317"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51%" id="mcps1.2.4.1.3"><p id="p9959161020418"><a name="p9959161020418"></a><a name="p9959161020418"></a><strong id="b105914149137"><a name="b105914149137"></a><a name="b105914149137"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row179609103411"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p896118101840"><a name="p896118101840"></a><a name="p896118101840"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="p1296211015416"><a name="p1296211015416"></a><a name="p1296211015416"></a>Bad Request</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p9963110146"><a name="p9963110146"></a><a name="p9963110146"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="row181330274199"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p18134027201912"><a name="p18134027201912"></a><a name="p18134027201912"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="p1713419274191"><a name="p1713419274191"></a><a name="p1713419274191"></a>Unauthorized</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p11134162718196"><a name="p11134162718196"></a><a name="p11134162718196"></a>Authorization failed.</p>
</td>
</tr>
</tbody>
</table>

