# Querying Request Statistics and Attack Statistics in a Specified Time Range<a name="EN-US_TOPIC_0193630657"></a>

## Function Description<a name="section272892"></a>

This API is used to query request statistics and attack statistics in a specified time range.

## URI<a name="section22104283"></a>

-   URI format

    GET  /v1/\{project\_id\}/waf/event/timeline?from=\{from\}&to=\{to\}&timezone=\{timezone\}&hosts=\{hostids\}

    >![](/images/icon-note.gif) **NOTE:**   
    >An example of a URI is as follows:  
    >GET  /v1/3ac26c59e15a4a11bb680a103a29ddb6/waf/event/attack/type?from=1543976973635&to=1563976973635&hosts=3211757cafa3437aae24d760022e79ba&hosts=93029844064b43739b51ca63036fbc4b&hosts=34fe5f5c60ef4e43a9975296765d1217  

-   Parameter description

    **Table  1**  Path parameters

    <a name="table23456073"></a>
    <table><thead align="left"><tr id="row24209096"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p14779753"><a name="p14779753"></a><a name="p14779753"></a><strong id="b181631731111111"><a name="b181631731111111"></a><a name="b181631731111111"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.2"><p id="p56309310"><a name="p56309310"></a><a name="p56309310"></a><strong id="b9628338114"><a name="b9628338114"></a><a name="b9628338114"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.33826617338266%" id="mcps1.2.5.1.3"><p id="p64760239"><a name="p64760239"></a><a name="p64760239"></a><strong id="b170120342111"><a name="b170120342111"></a><a name="b170120342111"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.806019398060194%" id="mcps1.2.5.1.4"><p id="p11088038"><a name="p11088038"></a><a name="p11088038"></a><strong id="b1731413610112"><a name="b1731413610112"></a><a name="b1731413610112"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row25715848"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p2608959"><a name="p2608959"></a><a name="p2608959"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p9999155"><a name="p9999155"></a><a name="p9999155"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.33826617338266%" headers="mcps1.2.5.1.3 "><p id="p4625227"><a name="p4625227"></a><a name="p4625227"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.806019398060194%" headers="mcps1.2.5.1.4 "><p id="p39099120"><a name="p39099120"></a><a name="p39099120"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row16347762"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p49100373"><a name="p49100373"></a><a name="p49100373"></a>from</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p17707256"><a name="p17707256"></a><a name="p17707256"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.33826617338266%" headers="mcps1.2.5.1.3 "><p id="p25001603"><a name="p25001603"></a><a name="p25001603"></a>Long</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.806019398060194%" headers="mcps1.2.5.1.4 "><p id="p18857034"><a name="p18857034"></a><a name="p18857034"></a>Specifies the start time (UTC) in milliseconds. For example, <strong id="b102003575485"><a name="b102003575485"></a><a name="b102003575485"></a>1548172800000</strong>.</p>
    </td>
    </tr>
    <tr id="row3762181511574"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p1076241518579"><a name="p1076241518579"></a><a name="p1076241518579"></a>to</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p11762171595720"><a name="p11762171595720"></a><a name="p11762171595720"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.33826617338266%" headers="mcps1.2.5.1.3 "><p id="p18762131575715"><a name="p18762131575715"></a><a name="p18762131575715"></a>Long</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.806019398060194%" headers="mcps1.2.5.1.4 "><p id="p676211156578"><a name="p676211156578"></a><a name="p676211156578"></a>Specifies the end time (UTC) in milliseconds. For example, <strong id="b10419170144910"><a name="b10419170144910"></a><a name="b10419170144910"></a>1548431999000</strong>.</p>
    </td>
    </tr>
    <tr id="row15254518105719"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p192549185578"><a name="p192549185578"></a><a name="p192549185578"></a>timezone</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p8254151819574"><a name="p8254151819574"></a><a name="p8254151819574"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.33826617338266%" headers="mcps1.2.5.1.3 "><p id="p1525415181578"><a name="p1525415181578"></a><a name="p1525415181578"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.806019398060194%" headers="mcps1.2.5.1.4 "><p id="p162541618145710"><a name="p162541618145710"></a><a name="p162541618145710"></a>Specifies the time zone. For example, the time zone of London is <strong id="b117301023184915"><a name="b117301023184915"></a><a name="b117301023184915"></a>+00:00</strong> and that of Beijing is <strong id="b474762724910"><a name="b474762724910"></a><a name="b474762724910"></a>+08:00</strong>. The default value is <strong id="b224718353496"><a name="b224718353496"></a><a name="b224718353496"></a>+00:00</strong>.</p>
    </td>
    </tr>
    <tr id="row39666843"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p58897682"><a name="p58897682"></a><a name="p58897682"></a>hosts</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p5982958"><a name="p5982958"></a><a name="p5982958"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.33826617338266%" headers="mcps1.2.5.1.3 "><p id="p14857623"><a name="p14857623"></a><a name="p14857623"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.806019398060194%" headers="mcps1.2.5.1.4 "><p id="p62616820"><a name="p62616820"></a><a name="p62616820"></a>Specifies the domain IDs.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section64720826"></a>

Request parameters

None

## Response<a name="section45616523"></a>

Response parameters

**Table  2**  Parameter description

<a name="table7646679"></a>
<table><thead align="left"><tr id="row48684466"><th class="cellrowborder" valign="top" width="32.46675332466753%" id="mcps1.2.4.1.1"><p id="p51127646"><a name="p51127646"></a><a name="p51127646"></a><strong id="b15679918171220"><a name="b15679918171220"></a><a name="b15679918171220"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.73722627737226%" id="mcps1.2.4.1.2"><p id="p47698687"><a name="p47698687"></a><a name="p47698687"></a><strong id="b1444121181310"><a name="b1444121181310"></a><a name="b1444121181310"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.4.1.3"><p id="p38388477"><a name="p38388477"></a><a name="p38388477"></a><strong id="b149423223136"><a name="b149423223136"></a><a name="b149423223136"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row9951978"><td class="cellrowborder" valign="top" width="32.46675332466753%" headers="mcps1.2.4.1.1 "><p id="p803902"><a name="p803902"></a><a name="p803902"></a>requests</p>
</td>
<td class="cellrowborder" valign="top" width="27.73722627737226%" headers="mcps1.2.4.1.2 "><p id="p65116065"><a name="p65116065"></a><a name="p65116065"></a><a href="#table1864743120361">Table 3</a></p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p39909950"><a name="p39909950"></a><a name="p39909950"></a>Specifies request statistics.</p>
</td>
</tr>
<tr id="row59543404"><td class="cellrowborder" valign="top" width="32.46675332466753%" headers="mcps1.2.4.1.1 "><p id="p58286448"><a name="p58286448"></a><a name="p58286448"></a>attacks</p>
</td>
<td class="cellrowborder" valign="top" width="27.73722627737226%" headers="mcps1.2.4.1.2 "><p id="p23581848"><a name="p23581848"></a><a name="p23581848"></a><a href="#table1441245463618">Table 4</a></p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p31081549"><a name="p31081549"></a><a name="p31081549"></a>Specifies attack statistics.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **requests**

<a name="table1864743120361"></a>
<table><thead align="left"><tr id="row11651123193616"><th class="cellrowborder" valign="top" width="32.46675332466753%" id="mcps1.2.4.1.1"><p id="p8652331123610"><a name="p8652331123610"></a><a name="p8652331123610"></a><strong id="b19344135922013"><a name="b19344135922013"></a><a name="b19344135922013"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.73722627737226%" id="mcps1.2.4.1.2"><p id="p16653173163614"><a name="p16653173163614"></a><a name="p16653173163614"></a><strong id="b1924208323"><a name="b1924208323"></a><a name="b1924208323"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.4.1.3"><p id="p1765414316365"><a name="p1765414316365"></a><a name="p1765414316365"></a><strong id="b1273133172116"><a name="b1273133172116"></a><a name="b1273133172116"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row14369133920360"><td class="cellrowborder" valign="top" width="32.46675332466753%" headers="mcps1.2.4.1.1 "><p id="p586543743614"><a name="p586543743614"></a><a name="p586543743614"></a>time</p>
</td>
<td class="cellrowborder" valign="top" width="27.73722627737226%" headers="mcps1.2.4.1.2 "><p id="p4865133733611"><a name="p4865133733611"></a><a name="p4865133733611"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p58661537163619"><a name="p58661537163619"></a><a name="p58661537163619"></a>Specifies the end time since Unix Epoch in milliseconds.</p>
</td>
</tr>
<tr id="row33681839143618"><td class="cellrowborder" valign="top" width="32.46675332466753%" headers="mcps1.2.4.1.1 "><p id="p586810376369"><a name="p586810376369"></a><a name="p586810376369"></a>num</p>
</td>
<td class="cellrowborder" valign="top" width="27.73722627737226%" headers="mcps1.2.4.1.2 "><p id="p1086973783615"><a name="p1086973783615"></a><a name="p1086973783615"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p4871143716361"><a name="p4871143716361"></a><a name="p4871143716361"></a>Specifies the number of requests.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **attacks**

<a name="table1441245463618"></a>
<table><thead align="left"><tr id="row1241695410366"><th class="cellrowborder" valign="top" width="32.46675332466753%" id="mcps1.2.4.1.1"><p id="p641715493612"><a name="p641715493612"></a><a name="p641715493612"></a><strong id="b1393228922"><a name="b1393228922"></a><a name="b1393228922"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.73722627737226%" id="mcps1.2.4.1.2"><p id="p14419115433618"><a name="p14419115433618"></a><a name="p14419115433618"></a><strong id="b1878758360"><a name="b1878758360"></a><a name="b1878758360"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.4.1.3"><p id="p942015493613"><a name="p942015493613"></a><a name="p942015493613"></a><strong id="b1430832337"><a name="b1430832337"></a><a name="b1430832337"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row742115443618"><td class="cellrowborder" valign="top" width="32.46675332466753%" headers="mcps1.2.4.1.1 "><p id="p0422254153613"><a name="p0422254153613"></a><a name="p0422254153613"></a>time</p>
</td>
<td class="cellrowborder" valign="top" width="27.73722627737226%" headers="mcps1.2.4.1.2 "><p id="p0423115443611"><a name="p0423115443611"></a><a name="p0423115443611"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p542415544363"><a name="p542415544363"></a><a name="p542415544363"></a>Specifies the end time since Unix Epoch in milliseconds.</p>
</td>
</tr>
<tr id="row1342565413362"><td class="cellrowborder" valign="top" width="32.46675332466753%" headers="mcps1.2.4.1.1 "><p id="p10426754133613"><a name="p10426754133613"></a><a name="p10426754133613"></a>num</p>
</td>
<td class="cellrowborder" valign="top" width="27.73722627737226%" headers="mcps1.2.4.1.2 "><p id="p642775493614"><a name="p642775493614"></a><a name="p642775493614"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p1342810548364"><a name="p1342810548364"></a><a name="p1342810548364"></a>Specifies the number of attacks.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section6158236101217"></a>

Response example

```
{
  "requests": [
        {"time": 1499817600, "num": 123400},
        {"time": 1499817601, "num": 123401},
        {"time": 1499817602, "num": 123402}
  ],
  "attacks": [
        {"time": 1499817600, "num": 1234},
        {"time": 1499817601, "num": 1235},
        {"time": 1499817602, "num": 1236}
  ]
}
```

## Status Code<a name="section7895529"></a>

[Table 5](#en-us_topic_0193631139_t82c3440f3efb42a38b9d4dc4011a33d0)  describes the normal status code returned by the API.

**Table  5**  Status code

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

