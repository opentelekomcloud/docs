# Querying False Alarm Masking Rules<a name="EN-US_TOPIC_0193631185"></a>

## Function Description<a name="section2094778"></a>

This API is used to query all false alarm masking rules in a policy.

## URI<a name="section18853009"></a>

-   URI format

    GET  /v1/\{project\_id\}/waf/policy/\{policy\_id\}/ignore?path=\{path\}&offset=\{offset\}&limit=\{limit\}

-   Parameter description

    **Table  1**  Path parameters

    <a name="table42601887"></a>
    <table><thead align="left"><tr id="row58492696"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p40287960"><a name="p40287960"></a><a name="p40287960"></a><strong id="b5785182114327"><a name="b5785182114327"></a><a name="b5785182114327"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.2"><p id="p42099345"><a name="p42099345"></a><a name="p42099345"></a><strong id="b19808946163216"><a name="b19808946163216"></a><a name="b19808946163216"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.3"><p id="p54603754"><a name="p54603754"></a><a name="p54603754"></a><strong id="b9113348153212"><a name="b9113348153212"></a><a name="b9113348153212"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.5.1.4"><p id="p60827915"><a name="p60827915"></a><a name="p60827915"></a><strong id="b3474184973216"><a name="b3474184973216"></a><a name="b3474184973216"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row28114077"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p62647751"><a name="p62647751"></a><a name="p62647751"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p41303090"><a name="p41303090"></a><a name="p41303090"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p57216006"><a name="p57216006"></a><a name="p57216006"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p3984873"><a name="p3984873"></a><a name="p3984873"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row35863865"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p19291961"><a name="p19291961"></a><a name="p19291961"></a>policy_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p19144989"><a name="p19144989"></a><a name="p19144989"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p7240270"><a name="p7240270"></a><a name="p7240270"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p49590963"><a name="p49590963"></a><a name="p49590963"></a>Specifies the policy ID.</p>
    </td>
    </tr>
    <tr id="row1212015781017"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p812119579109"><a name="p812119579109"></a><a name="p812119579109"></a>path</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p2012215710106"><a name="p2012215710106"></a><a name="p2012215710106"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p131221457101018"><a name="p131221457101018"></a><a name="p131221457101018"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p8122105771015"><a name="p8122105771015"></a><a name="p8122105771015"></a>Specifies the misreported URL.</p>
    </td>
    </tr>
    <tr id="row43665484"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p47243355"><a name="p47243355"></a><a name="p47243355"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p1506579"><a name="p1506579"></a><a name="p1506579"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p54924059"><a name="p54924059"></a><a name="p54924059"></a>Long</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p21617533"><a name="p21617533"></a><a name="p21617533"></a>Specifies the number of returned pages. Its value ranges from <strong id="b9433145510342"><a name="b9433145510342"></a><a name="b9433145510342"></a>0</strong> to <strong id="b124331255123413"><a name="b124331255123413"></a><a name="b124331255123413"></a>65535</strong>. The default value is <strong id="b1243465511344"><a name="b1243465511344"></a><a name="b1243465511344"></a>0</strong>.</p>
    </td>
    </tr>
    <tr id="row42756216"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p875914720329"><a name="p875914720329"></a><a name="p875914720329"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p8484949"><a name="p8484949"></a><a name="p8484949"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p16192254"><a name="p16192254"></a><a name="p16192254"></a>Long</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p25357967"><a name="p25357967"></a><a name="p25357967"></a>Specifies the maximum number of records displayed on each page. Its value ranges from <strong id="b1826619571342"><a name="b1826619571342"></a><a name="b1826619571342"></a>0</strong> to <strong id="b1826645714341"><a name="b1826645714341"></a><a name="b1826645714341"></a>50</strong>. The default value is <strong id="b42661957103416"><a name="b42661957103416"></a><a name="b42661957103416"></a>10</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section35459357"></a>

Request parameters

None

## Response<a name="section50698759"></a>

Response parameters

**Table  2**  Parameter description

<a name="table63197648"></a>
<table><thead align="left"><tr id="row49462140"><th class="cellrowborder" valign="top" width="33.086691330866906%" id="mcps1.2.4.1.1"><p id="p47010409"><a name="p47010409"></a><a name="p47010409"></a><strong id="b1063472920333"><a name="b1063472920333"></a><a name="b1063472920333"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.117288271172878%" id="mcps1.2.4.1.2"><p id="p49746803"><a name="p49746803"></a><a name="p49746803"></a><strong id="b43971731123318"><a name="b43971731123318"></a><a name="b43971731123318"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.4.1.3"><p id="p2959233"><a name="p2959233"></a><a name="p2959233"></a><strong id="b338463253320"><a name="b338463253320"></a><a name="b338463253320"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row26633101"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p9797597"><a name="p9797597"></a><a name="p9797597"></a>total</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p55407910"><a name="p55407910"></a><a name="p55407910"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p58855695"><a name="p58855695"></a><a name="p58855695"></a>Specifies the total number of policies.</p>
</td>
</tr>
<tr id="row59939207"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p23237571"><a name="p23237571"></a><a name="p23237571"></a>items</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p3195124"><a name="p3195124"></a><a name="p3195124"></a><a href="#table16394183011019">Table 3</a></p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p57478530"><a name="p57478530"></a><a name="p57478530"></a>Specifies the false alarm masking rule objects.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **items**

<a name="table16394183011019"></a>
<table><thead align="left"><tr id="row939613301015"><th class="cellrowborder" valign="top" width="33.086691330866906%" id="mcps1.2.4.1.1"><p id="p039873016013"><a name="p039873016013"></a><a name="p039873016013"></a><strong id="b173931822155314"><a name="b173931822155314"></a><a name="b173931822155314"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.117288271172878%" id="mcps1.2.4.1.2"><p id="p183997301406"><a name="p183997301406"></a><a name="p183997301406"></a><strong id="b1154856325"><a name="b1154856325"></a><a name="b1154856325"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.4.1.3"><p id="p839973013010"><a name="p839973013010"></a><a name="p839973013010"></a><strong id="b13111162515310"><a name="b13111162515310"></a><a name="b13111162515310"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row71355371705"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p1031011361902"><a name="p1031011361902"></a><a name="p1031011361902"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p1631217361200"><a name="p1631217361200"></a><a name="p1631217361200"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p12313536306"><a name="p12313536306"></a><a name="p12313536306"></a>Specifies the ID of a false alarm masking rule.</p>
</td>
</tr>
<tr id="row21351837608"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p43141936203"><a name="p43141936203"></a><a name="p43141936203"></a>policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p13316436805"><a name="p13316436805"></a><a name="p13316436805"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p183181836204"><a name="p183181836204"></a><a name="p183181836204"></a>Specifies the policy ID.</p>
</td>
</tr>
<tr id="row613319371801"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p8320136807"><a name="p8320136807"></a><a name="p8320136807"></a>path</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p93202036804"><a name="p93202036804"></a><a name="p93202036804"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p1532173610010"><a name="p1532173610010"></a><a name="p1532173610010"></a>Specifies a misreported URL excluding a domain name.</p>
</td>
</tr>
<tr id="row73641132163610"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p193651632203614"><a name="p193651632203614"></a><a name="p193651632203614"></a>event_id</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p1836593273612"><a name="p1836593273612"></a><a name="p1836593273612"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p113654323369"><a name="p113654323369"></a><a name="p113654323369"></a>Specifies the event ID.</p>
</td>
</tr>
<tr id="row3844271371"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p88441673372"><a name="p88441673372"></a><a name="p88441673372"></a>event_type</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p198441872374"><a name="p198441872374"></a><a name="p198441872374"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p5844107103719"><a name="p5844107103719"></a><a name="p5844107103719"></a>Specifies the event type.</p>
</td>
</tr>
<tr id="row201327371306"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p6322133618019"><a name="p6322133618019"></a><a name="p6322133618019"></a>rule</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p632311361307"><a name="p632311361307"></a><a name="p632311361307"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p143255361501"><a name="p143255361501"></a><a name="p143255361501"></a>Specifies the rule ID, which consists of six digits and cannot be empty.</p>
</td>
</tr>
<tr id="row9131113720015"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p173278362004"><a name="p173278362004"></a><a name="p173278362004"></a>timestamp</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p1329173611017"><a name="p1329173611017"></a><a name="p1329173611017"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p1332911361107"><a name="p1332911361107"></a><a name="p1332911361107"></a>Specifies the time when a false alarm masking rule is added.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section586416610719"></a>

**total**  with a value of  **2**  is used as an example.

Response example

```
{
  "total": 2,
  "items": [{
      "id": "3a9b5c0f96784ec8abd8ba61a98064ef",
      "policy_id": "yuc0e55865544d1f8c95cf71df108c6b",
      "event_id": "02d3ac3cd99f440daf8d38e03cf0e2a6",
      "event_type": "xss",
      "rule": "100001",
      "timestamp": 1499817600,
      "path": "/a"
    }, {
      "id": "44d887434169475794b2717438f7fa78",
      "policy_id": "yuc0e55865544d1f8c95cf71df108c6b",
      "event_id": "f8c74b656a9d4d329dbcefe0969cc427",
      "event_type": "sqli"
      "rule": "100002",
      "timestamp": 1499817600,
      "path": "/a"
    }
  ]
}
```

## Status Code<a name="section53635648"></a>

[Table 4](#en-us_topic_0193631139_t82c3440f3efb42a38b9d4dc4011a33d0)  describes the normal status code returned by the API.

**Table  4**  Status code

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

