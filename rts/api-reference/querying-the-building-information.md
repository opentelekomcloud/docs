# Querying the Building Information<a name="EN-US_TOPIC_0084581314"></a>

## Function<a name="en-us_topic_0057973151_section36500993"></a>

This API is used to query the building information.

## URI<a name="en-us_topic_0057973151_section60073487"></a>

GET /v1/\{project\_id\}/build\_info

For details about the parameters, see  [Table 1](#table1759528275).

**Table  1**  Parameter description

<a name="table1759528275"></a>
<table><thead align="left"><tr id="row26011272716"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p17762534144716"><a name="p17762534144716"></a><a name="p17762534144716"></a><strong id="b33553211349"><a name="b33553211349"></a><a name="b33553211349"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p376433420478"><a name="p376433420478"></a><a name="p376433420478"></a><strong id="b9409142213417"><a name="b9409142213417"></a><a name="b9409142213417"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p15766123474714"><a name="p15766123474714"></a><a name="p15766123474714"></a><strong id="b72321323153410"><a name="b72321323153410"></a><a name="b72321323153410"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p147683349474"><a name="p147683349474"></a><a name="p147683349474"></a><strong id="b19371124173410"><a name="b19371124173410"></a><a name="b19371124173410"></a>Description</strong></p>
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

## Request Parameter<a name="en-us_topic_0057973151_section3790475"></a>

N/A

## Response Parameter<a name="en-us_topic_0057973151_section34114278"></a>

<a name="en-us_topic_0057973151_table63619552"></a>
<table><thead align="left"><tr id="en-us_topic_0057973151_row33690117"><th class="cellrowborder" valign="top" width="16.470000000000002%" id="mcps1.1.5.1.1"><p id="p13701251185014"><a name="p13701251185014"></a><a name="p13701251185014"></a><strong id="b9346153311342"><a name="b9346153311342"></a><a name="b9346153311342"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.470000000000002%" id="mcps1.1.5.1.2"><p id="p13704145119507"><a name="p13704145119507"></a><a name="p13704145119507"></a><strong id="b4415434133414"><a name="b4415434133414"></a><a name="b4415434133414"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.65%" id="mcps1.1.5.1.3"><p id="p3705151185017"><a name="p3705151185017"></a><a name="p3705151185017"></a><strong id="b17332203503416"><a name="b17332203503416"></a><a name="b17332203503416"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="49.41%" id="mcps1.1.5.1.4"><p id="p1371214511507"><a name="p1371214511507"></a><a name="p1371214511507"></a><strong id="b11218183613344"><a name="b11218183613344"></a><a name="b11218183613344"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973151_row50452473"><td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973151_p60118549"><a name="en-us_topic_0057973151_p60118549"></a><a name="en-us_topic_0057973151_p60118549"></a>api</p>
</td>
<td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.1.5.1.2 "><p id="p87428544215"><a name="p87428544215"></a><a name="p87428544215"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.65%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973151_p37764268"><a name="en-us_topic_0057973151_p37764268"></a><a name="en-us_topic_0057973151_p37764268"></a>Dict</p>
</td>
<td class="cellrowborder" valign="top" width="49.41%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973151_p5441393"><a name="en-us_topic_0057973151_p5441393"></a><a name="en-us_topic_0057973151_p5441393"></a>Specifies the API information.</p>
</td>
</tr>
<tr id="en-us_topic_0057973151_row48972542"><td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973151_p7352932"><a name="en-us_topic_0057973151_p7352932"></a><a name="en-us_topic_0057973151_p7352932"></a>engine</p>
</td>
<td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.1.5.1.2 "><p id="p177421853423"><a name="p177421853423"></a><a name="p177421853423"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.65%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973151_p58716619"><a name="en-us_topic_0057973151_p58716619"></a><a name="en-us_topic_0057973151_p58716619"></a>Dict</p>
</td>
<td class="cellrowborder" valign="top" width="49.41%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973151_p34860474"><a name="en-us_topic_0057973151_p34860474"></a><a name="en-us_topic_0057973151_p34860474"></a>Specifies the engine information.</p>
</td>
</tr>
</tbody>
</table>

## Request Example<a name="en-us_topic_0057973151_section38593049"></a>

```
GET /v1/95d02433133a4c0a87ba6967474a2ad3/build_info
```

## Response Example<a name="en-us_topic_0057973151_section11793125"></a>

```
{
    "api": {
        "revision": "{api_build_revision}"
    },
    "engine": {
        "revision": "{engine_build_revision}"
    }
}
```

## **Return Code**<a name="en-us_topic_0057973151_section39029268"></a>

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
<table><thead align="left"><tr id="row16955110342"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="p129561510144"><a name="p129561510144"></a><a name="p129561510144"></a><strong id="b1754611012356"><a name="b1754611012356"></a><a name="b1754611012356"></a>Return Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26%" id="mcps1.2.4.1.2"><p id="p4959810444"><a name="p4959810444"></a><a name="p4959810444"></a><strong id="b14523141133514"><a name="b14523141133514"></a><a name="b14523141133514"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51%" id="mcps1.2.4.1.3"><p id="p9959161020418"><a name="p9959161020418"></a><a name="p9959161020418"></a><strong id="b17343131218354"><a name="b17343131218354"></a><a name="b17343131218354"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row181330274199"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p18134027201912"><a name="p18134027201912"></a><a name="p18134027201912"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="p1713419274191"><a name="p1713419274191"></a><a name="p1713419274191"></a>Unauthorized</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p11134162718196"><a name="p11134162718196"></a><a name="p11134162718196"></a>Authorization failed.</p>
</td>
</tr>
</tbody>
</table>

