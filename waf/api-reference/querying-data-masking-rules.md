# Querying Data Masking Rules<a name="EN-US_TOPIC_0193630653"></a>

## Function Description<a name="section39390906"></a>

This API is used to query all data masking rules in a policy.

## URI<a name="section18973837"></a>

-   URI format

    GET  /v1/\{project\_id\}/waf/policy/\{policy\_id\}/privacy?offset=\{offset\}&limit=\{limit\}

-   Parameter description

    **Table  1**  Path parameters

    <a name="table25306260"></a>
    <table><thead align="left"><tr id="row35532954"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p59597058"><a name="p59597058"></a><a name="p59597058"></a><strong id="b1875961614214"><a name="b1875961614214"></a><a name="b1875961614214"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.2"><p id="p62632378"><a name="p62632378"></a><a name="p62632378"></a><strong id="b16157151911217"><a name="b16157151911217"></a><a name="b16157151911217"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.3"><p id="p40057834"><a name="p40057834"></a><a name="p40057834"></a><strong id="b654821162119"><a name="b654821162119"></a><a name="b654821162119"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.5.1.4"><p id="p23459131"><a name="p23459131"></a><a name="p23459131"></a><strong id="b1353922382111"><a name="b1353922382111"></a><a name="b1353922382111"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row21141460"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p34736734"><a name="p34736734"></a><a name="p34736734"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p62212097"><a name="p62212097"></a><a name="p62212097"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p6015076"><a name="p6015076"></a><a name="p6015076"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p17459119"><a name="p17459119"></a><a name="p17459119"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row22914347"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p44122855"><a name="p44122855"></a><a name="p44122855"></a>policy_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p17181470"><a name="p17181470"></a><a name="p17181470"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p49521850"><a name="p49521850"></a><a name="p49521850"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p51846947"><a name="p51846947"></a><a name="p51846947"></a>Specifies the policy ID.</p>
    </td>
    </tr>
    <tr id="row63969344"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p14134342"><a name="p14134342"></a><a name="p14134342"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p4031053"><a name="p4031053"></a><a name="p4031053"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p58079868"><a name="p58079868"></a><a name="p58079868"></a>Long</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p21617533"><a name="p21617533"></a><a name="p21617533"></a>Specifies the number of returned pages. Its value ranges from <strong id="b116231631103417"><a name="b116231631103417"></a><a name="b116231631103417"></a>0</strong> to <strong id="b76231931143411"><a name="b76231931143411"></a><a name="b76231931143411"></a>65535</strong>. The default value is <strong id="b6623123113417"><a name="b6623123113417"></a><a name="b6623123113417"></a>0</strong>.</p>
    </td>
    </tr>
    <tr id="row61640034"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p26786846"><a name="p26786846"></a><a name="p26786846"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p22250878"><a name="p22250878"></a><a name="p22250878"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p57490666"><a name="p57490666"></a><a name="p57490666"></a>Long</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p25357967"><a name="p25357967"></a><a name="p25357967"></a>Specifies the maximum number of records displayed on each page. Its value ranges from <strong id="b3623143315349"><a name="b3623143315349"></a><a name="b3623143315349"></a>0</strong> to <strong id="b17623833193420"><a name="b17623833193420"></a><a name="b17623833193420"></a>50</strong>. The default value is <strong id="b1662343310341"><a name="b1662343310341"></a><a name="b1662343310341"></a>10</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section36546812"></a>

Request parameters

None

## Response<a name="section60485854"></a>

Response parameters

**Table  2**  Parameter description

<a name="table43775162"></a>
<table><thead align="left"><tr id="row24416609"><th class="cellrowborder" valign="top" width="33.186681331866815%" id="mcps1.2.4.1.1"><p id="p31588306"><a name="p31588306"></a><a name="p31588306"></a><strong id="b12787162372211"><a name="b12787162372211"></a><a name="b12787162372211"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.017298270172986%" id="mcps1.2.4.1.2"><p id="p8515959"><a name="p8515959"></a><a name="p8515959"></a><strong id="b1012718272225"><a name="b1012718272225"></a><a name="b1012718272225"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.4.1.3"><p id="p18704056"><a name="p18704056"></a><a name="p18704056"></a><strong id="b1781622832220"><a name="b1781622832220"></a><a name="b1781622832220"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row34118783"><td class="cellrowborder" valign="top" width="33.186681331866815%" headers="mcps1.2.4.1.1 "><p id="p12158071"><a name="p12158071"></a><a name="p12158071"></a>total</p>
</td>
<td class="cellrowborder" valign="top" width="27.017298270172986%" headers="mcps1.2.4.1.2 "><p id="p45279679"><a name="p45279679"></a><a name="p45279679"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p43775359"><a name="p43775359"></a><a name="p43775359"></a>Specifies the total number of rules.</p>
</td>
</tr>
<tr id="row58433916"><td class="cellrowborder" valign="top" width="33.186681331866815%" headers="mcps1.2.4.1.1 "><p id="p35526756"><a name="p35526756"></a><a name="p35526756"></a>items</p>
</td>
<td class="cellrowborder" valign="top" width="27.017298270172986%" headers="mcps1.2.4.1.2 "><p id="p59095001"><a name="p59095001"></a><a name="p59095001"></a><a href="#table16394183011019">Table 3</a></p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p1603648"><a name="p1603648"></a><a name="p1603648"></a>Specifies the data masking rule objects.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **items**

<a name="table16394183011019"></a>
<table><thead align="left"><tr id="row939613301015"><th class="cellrowborder" valign="top" width="33.086691330866906%" id="mcps1.2.4.1.1"><p id="p039873016013"><a name="p039873016013"></a><a name="p039873016013"></a><strong id="b1142929165215"><a name="b1142929165215"></a><a name="b1142929165215"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.117288271172878%" id="mcps1.2.4.1.2"><p id="p183997301406"><a name="p183997301406"></a><a name="p183997301406"></a><strong id="b1012718272225_1"><a name="b1012718272225_1"></a><a name="b1012718272225_1"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.4.1.3"><p id="p839973013010"><a name="p839973013010"></a><a name="p839973013010"></a><strong id="b1280733115213"><a name="b1280733115213"></a><a name="b1280733115213"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row74801364143"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p63770514142"><a name="p63770514142"></a><a name="p63770514142"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p11378155131414"><a name="p11378155131414"></a><a name="p11378155131414"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p837920531414"><a name="p837920531414"></a><a name="p837920531414"></a>Specifies the ID of a data masking rule.</p>
</td>
</tr>
<tr id="row19480661145"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p173802510146"><a name="p173802510146"></a><a name="p173802510146"></a>policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p638316519142"><a name="p638316519142"></a><a name="p638316519142"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p63841753146"><a name="p63841753146"></a><a name="p63841753146"></a>Specifies the policy ID.</p>
</td>
</tr>
<tr id="row14795618141"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p0385135191417"><a name="p0385135191417"></a><a name="p0385135191417"></a>path</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p12385105161417"><a name="p12385105161417"></a><a name="p12385105161417"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p123871254144"><a name="p123871254144"></a><a name="p123871254144"></a>Specifies the URL to which the data masking rule applies (exact match by default).</p>
</td>
</tr>
<tr id="row1747913615148"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p938919511416"><a name="p938919511416"></a><a name="p938919511416"></a>category</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p63905541418"><a name="p63905541418"></a><a name="p63905541418"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p439010571416"><a name="p439010571416"></a><a name="p439010571416"></a>Specifies the masked field. The options are <strong id="b633918430135"><a name="b633918430135"></a><a name="b633918430135"></a>params</strong> and <strong id="b63391343111310"><a name="b63391343111310"></a><a name="b63391343111310"></a>header</strong>.</p>
</td>
</tr>
<tr id="row10479146161415"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p3392957141"><a name="p3392957141"></a><a name="p3392957141"></a>index</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p12393454141"><a name="p12393454141"></a><a name="p12393454141"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p123945531414"><a name="p123945531414"></a><a name="p123945531414"></a>Specifies the masked subfield.</p>
</td>
</tr>
<tr id="row1247806121411"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p1839525101413"><a name="p1839525101413"></a><a name="p1839525101413"></a>timestamp</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p93978511148"><a name="p93978511148"></a><a name="p93978511148"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p63984521418"><a name="p63984521418"></a><a name="p63984521418"></a>Specifies the time when a data masking rule is added.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section2080711469572"></a>

**total**  with a value of  **2**  is used as an example.

Response example

```
{
  "total": 2,
  "items": [{
      "id": "e1c0e55865544d1f8c95cf71df108c6b",
      "policy_id": "yuc0e55865544d1f8c95cf71df108c6b",
      "path": "/login",
      "category": "params",
      "index": "password",
      "timestamp": 123243414132
    }, {
      "id": "d947d31c3e794b70a25e5e2057997f8e",
      "policy_id": "yuc0e55865544d1f8c95cf71df108c89",
      "path": "/register",
      "category": "header",
      "index": "x-auth-token",
      "timestamp": 1343243243123
    }
  ]
}

```

## Status Code<a name="section7501782"></a>

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

