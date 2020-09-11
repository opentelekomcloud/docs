# Querying Event Distribution<a name="EN-US_TOPIC_0193631133"></a>

## Function Description<a name="section50563647"></a>

This API is used to query event distribution.

## URI<a name="section2014776"></a>

-   URI format

    GET  /v1/\{project\_id\}/waf/event/attack/type?from=\{from\}&to=\{to\}&hosts=\{hostids\}

    >![](/images/icon-note.gif) **NOTE:**   
    >An example of a URI is as follows:  
    >GET  /v1/3ac26c59e15a4a11bb680a103a29ddb6/waf/event/attack/type?from=1543976973635&to=1563976973635&hosts=3211757cafa3437aae24d760022e79ba&hosts=93029844064b43739b51ca63036fbc4b&hosts=34fe5f5c60ef4e43a9975296765d1217  

-   Parameter description

    **Table  1**  Path parameters

    <a name="table54623359"></a>
    <table><thead align="left"><tr id="row49794519"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p6824202"><a name="p6824202"></a><a name="p6824202"></a><strong id="b128864178450"><a name="b128864178450"></a><a name="b128864178450"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.2"><p id="p15889527"><a name="p15889527"></a><a name="p15889527"></a><strong id="b9149112019454"><a name="b9149112019454"></a><a name="b9149112019454"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.3"><p id="p11983300"><a name="p11983300"></a><a name="p11983300"></a><strong id="b11399162194512"><a name="b11399162194512"></a><a name="b11399162194512"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.5.1.4"><p id="p31123225"><a name="p31123225"></a><a name="p31123225"></a><strong id="b1859762374514"><a name="b1859762374514"></a><a name="b1859762374514"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row37953311"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p54319357"><a name="p54319357"></a><a name="p54319357"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p37791836"><a name="p37791836"></a><a name="p37791836"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p41239908"><a name="p41239908"></a><a name="p41239908"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p52098236"><a name="p52098236"></a><a name="p52098236"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row66230941"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p63106033"><a name="p63106033"></a><a name="p63106033"></a>from</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p11315049"><a name="p11315049"></a><a name="p11315049"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p44103790"><a name="p44103790"></a><a name="p44103790"></a>Long</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p18857034"><a name="p18857034"></a><a name="p18857034"></a>Specifies the start time (UTC) in milliseconds. For example, <strong id="b846033624812"><a name="b846033624812"></a><a name="b846033624812"></a>1548172800000</strong>.</p>
    </td>
    </tr>
    <tr id="row099415339557"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p199961933195515"><a name="p199961933195515"></a><a name="p199961933195515"></a>to</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p179961533135510"><a name="p179961533135510"></a><a name="p179961533135510"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p1799663325516"><a name="p1799663325516"></a><a name="p1799663325516"></a>Long</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p28177917"><a name="p28177917"></a><a name="p28177917"></a>Specifies the end time (UTC) in milliseconds. For example, <strong id="b85071742184812"><a name="b85071742184812"></a><a name="b85071742184812"></a>1548431999000</strong>.</p>
    </td>
    </tr>
    <tr id="row6517283"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p58137894"><a name="p58137894"></a><a name="p58137894"></a>hosts</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p11548945"><a name="p11548945"></a><a name="p11548945"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p63049357"><a name="p63049357"></a><a name="p63049357"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p6724289"><a name="p6724289"></a><a name="p6724289"></a>Specifies the domain IDs.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section18132989"></a>

Request parameters

None

## Response<a name="section28979173"></a>

Response parameters

**Table  2**  Parameter description

<a name="table10363184164611"></a>
<table><thead align="left"><tr id="row71754174287"><th class="cellrowborder" valign="top" width="33.333333333333336%" id="mcps1.2.4.1.1"><p id="p18175617172815"><a name="p18175617172815"></a><a name="p18175617172815"></a><strong id="b471271633715"><a name="b471271633715"></a><a name="b471271633715"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.333333333333336%" id="mcps1.2.4.1.2"><p id="p131751517202810"><a name="p131751517202810"></a><a name="p131751517202810"></a><strong id="b423135825113"><a name="b423135825113"></a><a name="b423135825113"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.333333333333336%" id="mcps1.2.4.1.3"><p id="p1817541712287"><a name="p1817541712287"></a><a name="p1817541712287"></a><strong id="b1097691883715"><a name="b1097691883715"></a><a name="b1097691883715"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row5175617122810"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p1017561762818"><a name="p1017561762818"></a><a name="p1017561762818"></a>xss</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p417501792816"><a name="p417501792816"></a><a name="p417501792816"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p2017521722812"><a name="p2017521722812"></a><a name="p2017521722812"></a>Specifies the number of XSS attacks detected within the time range.</p>
</td>
</tr>
<tr id="row51751517202817"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p81753172289"><a name="p81753172289"></a><a name="p81753172289"></a>sqli</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p9175141710285"><a name="p9175141710285"></a><a name="p9175141710285"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p81752173285"><a name="p81752173285"></a><a name="p81752173285"></a>Specifies the number of SQL injection attacks detected within the time range.</p>
</td>
</tr>
<tr id="row117511712818"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p111751017172811"><a name="p111751017172811"></a><a name="p111751017172811"></a>cmdi</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p12175131762819"><a name="p12175131762819"></a><a name="p12175131762819"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p417513177284"><a name="p417513177284"></a><a name="p417513177284"></a>Specifies the number of command injection attacks detected within the time range.</p>
</td>
</tr>
<tr id="row1175111710285"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p11765173288"><a name="p11765173288"></a><a name="p11765173288"></a>cc</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p1517691762811"><a name="p1517691762811"></a><a name="p1517691762811"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p1176141722817"><a name="p1176141722817"></a><a name="p1176141722817"></a>Specifies the number of CC attacks detected within the time range.</p>
</td>
</tr>
<tr id="row917614171287"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p417641772815"><a name="p417641772815"></a><a name="p417641772815"></a>custom</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p1517661762815"><a name="p1517661762815"></a><a name="p1517661762815"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p11176151732811"><a name="p11176151732811"></a><a name="p11176151732811"></a>Specifies the number of Precise Protection events detected within the time range.</p>
</td>
</tr>
<tr id="row10176417112813"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p31761417132817"><a name="p31761417132817"></a><a name="p31761417132817"></a>illegal</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p2176191716284"><a name="p2176191716284"></a><a name="p2176191716284"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p61761317172814"><a name="p61761317172814"></a><a name="p61761317172814"></a>Specifies the number of invalid requests detected within the time range.</p>
</td>
</tr>
<tr id="row131761817162814"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p717621718284"><a name="p717621718284"></a><a name="p717621718284"></a>lfi</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p3176517152811"><a name="p3176517152811"></a><a name="p3176517152811"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p360919231290"><a name="p360919231290"></a><a name="p360919231290"></a>Specifies the number of local file inclusion attacks detected within the time range.</p>
</td>
</tr>
<tr id="row11761175286"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p1117611702813"><a name="p1117611702813"></a><a name="p1117611702813"></a>robot</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p1717612178285"><a name="p1717612178285"></a><a name="p1717612178285"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p917614179281"><a name="p917614179281"></a><a name="p917614179281"></a>Specifies the number of malicious crawlers detected within the time range.</p>
</td>
</tr>
<tr id="row181761817112811"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p2176131782811"><a name="p2176131782811"></a><a name="p2176131782811"></a>antitamper</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p1176101719285"><a name="p1176101719285"></a><a name="p1176101719285"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p51760179282"><a name="p51760179282"></a><a name="p51760179282"></a>Specifies the number of webpage tampering attacks detected within the time range.</p>
</td>
</tr>
<tr id="row15176517162810"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p21762176285"><a name="p21762176285"></a><a name="p21762176285"></a>rfi</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p71761317102818"><a name="p71761317102818"></a><a name="p71761317102818"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p1117610171281"><a name="p1117610171281"></a><a name="p1117610171281"></a>Specifies the number of remote file inclusion attacks detected within the time range.</p>
</td>
</tr>
<tr id="row817681710285"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p0176101792815"><a name="p0176101792815"></a><a name="p0176101792815"></a>vuln</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p15176161711283"><a name="p15176161711283"></a><a name="p15176161711283"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p13176317192819"><a name="p13176317192819"></a><a name="p13176317192819"></a>Specifies the number of other attacks detected within the time range.</p>
</td>
</tr>
<tr id="row10176717192811"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p017691711283"><a name="p017691711283"></a><a name="p017691711283"></a>whiteblackip</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p9176151742810"><a name="p9176151742810"></a><a name="p9176151742810"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p20176121742811"><a name="p20176121742811"></a><a name="p20176121742811"></a>Specifies the number of Blacklist and Whitelist events detected within the time range.</p>
</td>
</tr>
<tr id="row1617641711288"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p91760174285"><a name="p91760174285"></a><a name="p91760174285"></a>webshell</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p617621720286"><a name="p617621720286"></a><a name="p617621720286"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p10176201712811"><a name="p10176201712811"></a><a name="p10176201712811"></a>Specifies the number of webshell attacks detected within the time range.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section195321810191219"></a>

Response example

```
{
    "xss": 150,
    "sqli": 321,
    "cmdi": 120,
    "robot": 10,
    "whiteblackip": 30,
    "custom": 50,
    "cc": 60,
    "illegal": 10
}

```

## Status Code<a name="section59485971"></a>

[Table 3](#en-us_topic_0193631139_t82c3440f3efb42a38b9d4dc4011a33d0)  describes the normal status code returned by the API.

**Table  3**  Status code

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

