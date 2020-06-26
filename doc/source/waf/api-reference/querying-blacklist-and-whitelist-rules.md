# Querying Blacklist and Whitelist Rules<a name="EN-US_TOPIC_0193631113"></a>

## Function Description<a name="section32792555"></a>

This API is used to query all blacklist and whitelist rules.

## URI<a name="section26697540"></a>

-   URI format

    GET  /v1/\{project\_id\}/waf/policy/\{policy\_id\}/whiteblackip?offset=\{offset\}&limit=\{limit\}

-   Parameter description

    **Table  1**  Path parameters

    <a name="table9786546"></a>
    <table><thead align="left"><tr id="row45293161"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p44867418"><a name="p44867418"></a><a name="p44867418"></a><strong id="b10123171355118"><a name="b10123171355118"></a><a name="b10123171355118"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.2"><p id="p10382207"><a name="p10382207"></a><a name="p10382207"></a><strong id="b78891413115115"><a name="b78891413115115"></a><a name="b78891413115115"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.3"><p id="p35652416"><a name="p35652416"></a><a name="p35652416"></a><strong id="b1382771412515"><a name="b1382771412515"></a><a name="b1382771412515"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.5.1.4"><p id="p2164615"><a name="p2164615"></a><a name="p2164615"></a><strong id="b135811516512"><a name="b135811516512"></a><a name="b135811516512"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row41116089"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p42068928"><a name="p42068928"></a><a name="p42068928"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p52140036"><a name="p52140036"></a><a name="p52140036"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p62593388"><a name="p62593388"></a><a name="p62593388"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p36899681"><a name="p36899681"></a><a name="p36899681"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row63661675"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p56322078"><a name="p56322078"></a><a name="p56322078"></a>policy_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p65794449"><a name="p65794449"></a><a name="p65794449"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p27750124"><a name="p27750124"></a><a name="p27750124"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p33167576"><a name="p33167576"></a><a name="p33167576"></a>Specifies the policy ID.</p>
    </td>
    </tr>
    <tr id="row30072732"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p19972195"><a name="p19972195"></a><a name="p19972195"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p7135119"><a name="p7135119"></a><a name="p7135119"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p41073800"><a name="p41073800"></a><a name="p41073800"></a>Long</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p21617533"><a name="p21617533"></a><a name="p21617533"></a>Specifies the number of returned pages. Its value ranges from <strong id="b19630114363320"><a name="b19630114363320"></a><a name="b19630114363320"></a>0</strong> to <strong id="b863834393319"><a name="b863834393319"></a><a name="b863834393319"></a>65535</strong>. The default value is <strong id="b563815436331"><a name="b563815436331"></a><a name="b563815436331"></a>0</strong>.</p>
    </td>
    </tr>
    <tr id="row12247267"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p52504570"><a name="p52504570"></a><a name="p52504570"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p25011769"><a name="p25011769"></a><a name="p25011769"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p12687433"><a name="p12687433"></a><a name="p12687433"></a>Long</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p25357967"><a name="p25357967"></a><a name="p25357967"></a>Specifies the maximum number of records displayed on each page. Its value ranges from <strong id="b1752010453331"><a name="b1752010453331"></a><a name="b1752010453331"></a>0</strong> to <strong id="b1528124514337"><a name="b1528124514337"></a><a name="b1528124514337"></a>50</strong>. The default value is <strong id="b352854533316"><a name="b352854533316"></a><a name="b352854533316"></a>10</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section38951274"></a>

Request parameters

None

## Response<a name="section15017149"></a>

Response parameters

**Table  2**  Parameter description

<a name="table15472974"></a>
<table><thead align="left"><tr id="row56736167"><th class="cellrowborder" valign="top" width="42.85571442855714%" id="mcps1.2.4.1.1"><p id="p32226778"><a name="p32226778"></a><a name="p32226778"></a><strong id="b369075835211"><a name="b369075835211"></a><a name="b369075835211"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.4.1.2"><p id="p60232263"><a name="p60232263"></a><a name="p60232263"></a><strong id="b86271959175219"><a name="b86271959175219"></a><a name="b86271959175219"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.4.1.3"><p id="p46975124"><a name="p46975124"></a><a name="p46975124"></a><strong id="b18181503532"><a name="b18181503532"></a><a name="b18181503532"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row20122934"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p19344951"><a name="p19344951"></a><a name="p19344951"></a>total</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p23437164"><a name="p23437164"></a><a name="p23437164"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p19362109"><a name="p19362109"></a><a name="p19362109"></a>Specifies the total number of rules.</p>
</td>
</tr>
<tr id="row40041260"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p22116660"><a name="p22116660"></a><a name="p22116660"></a>items</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p46619020"><a name="p46619020"></a><a name="p46619020"></a><a href="#table16394183011019">Table 3</a></p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p1603648"><a name="p1603648"></a><a name="p1603648"></a>Specifies the blacklist or whitelist rule objects.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **items**

<a name="table16394183011019"></a>
<table><thead align="left"><tr id="row939613301015"><th class="cellrowborder" valign="top" width="33.08669133086692%" id="mcps1.2.4.1.1"><p id="p039873016013"><a name="p039873016013"></a><a name="p039873016013"></a><strong id="b83195249445"><a name="b83195249445"></a><a name="b83195249445"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26.577342265773424%" id="mcps1.2.4.1.2"><p id="p183997301406"><a name="p183997301406"></a><a name="p183997301406"></a><strong id="b86271959175219_1"><a name="b86271959175219_1"></a><a name="b86271959175219_1"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="40.33596640335966%" id="mcps1.2.4.1.3"><p id="p839973013010"><a name="p839973013010"></a><a name="p839973013010"></a><strong id="b4305123014416"><a name="b4305123014416"></a><a name="b4305123014416"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row6254134620148"><td class="cellrowborder" valign="top" width="33.08669133086692%" headers="mcps1.2.4.1.1 "><p id="p15927154410145"><a name="p15927154410145"></a><a name="p15927154410145"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="26.577342265773424%" headers="mcps1.2.4.1.2 "><p id="p18929194417149"><a name="p18929194417149"></a><a name="p18929194417149"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40.33596640335966%" headers="mcps1.2.4.1.3 "><p id="p8930944171414"><a name="p8930944171414"></a><a name="p8930944171414"></a>Specifies the ID of a blacklist or whitelist rule.</p>
</td>
</tr>
<tr id="row9253144691412"><td class="cellrowborder" valign="top" width="33.08669133086692%" headers="mcps1.2.4.1.1 "><p id="p1493184451410"><a name="p1493184451410"></a><a name="p1493184451410"></a>policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="26.577342265773424%" headers="mcps1.2.4.1.2 "><p id="p17933114491410"><a name="p17933114491410"></a><a name="p17933114491410"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40.33596640335966%" headers="mcps1.2.4.1.3 "><p id="p15934444201410"><a name="p15934444201410"></a><a name="p15934444201410"></a>Specifies the ID of the policy to which the rule belongs.</p>
</td>
</tr>
<tr id="row325324620149"><td class="cellrowborder" valign="top" width="33.08669133086692%" headers="mcps1.2.4.1.1 "><p id="p189361444161416"><a name="p189361444161416"></a><a name="p189361444161416"></a>addr</p>
</td>
<td class="cellrowborder" valign="top" width="26.577342265773424%" headers="mcps1.2.4.1.2 "><p id="p6937144111419"><a name="p6937144111419"></a><a name="p6937144111419"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40.33596640335966%" headers="mcps1.2.4.1.3 "><p id="p169381144191419"><a name="p169381144191419"></a><a name="p169381144191419"></a>Specifies the public IP address or range (IP address and subnet mask). For example, <em id="i155853570228"><a name="i155853570228"></a><a name="i155853570228"></a>X.X.</em><strong id="b13507156132214"><a name="b13507156132214"></a><a name="b13507156132214"></a>0.125</strong> or <em id="i58821941239"><a name="i58821941239"></a><a name="i58821941239"></a>X.X.</em><strong id="b13210109182310"><a name="b13210109182310"></a><a name="b13210109182310"></a>6.0/24</strong>.</p>
</td>
</tr>
<tr id="row8253104617149"><td class="cellrowborder" valign="top" width="33.08669133086692%" headers="mcps1.2.4.1.1 "><p id="p139407442141"><a name="p139407442141"></a><a name="p139407442141"></a>white</p>
</td>
<td class="cellrowborder" valign="top" width="26.577342265773424%" headers="mcps1.2.4.1.2 "><p id="p1494224410148"><a name="p1494224410148"></a><a name="p1494224410148"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="40.33596640335966%" headers="mcps1.2.4.1.3 "><p id="p131673177539"><a name="p131673177539"></a><a name="p131673177539"></a>Specifies the IP address type.</p>
<a name="ul3374102111535"></a><a name="ul3374102111535"></a><ul id="ul3374102111535"><li><strong id="b484418521202"><a name="b484418521202"></a><a name="b484418521202"></a>1</strong>: <strong id="b1844135213206"><a name="b1844135213206"></a><a name="b1844135213206"></a>Whitelist</strong></li><li><strong id="b432165415203"><a name="b432165415203"></a><a name="b432165415203"></a>0</strong>: <strong id="b632110546209"><a name="b632110546209"></a><a name="b632110546209"></a>Blacklist</strong></li></ul>
</td>
</tr>
<tr id="row2025284612149"><td class="cellrowborder" valign="top" width="33.08669133086692%" headers="mcps1.2.4.1.1 "><p id="p17943164411414"><a name="p17943164411414"></a><a name="p17943164411414"></a>timestamp</p>
</td>
<td class="cellrowborder" valign="top" width="26.577342265773424%" headers="mcps1.2.4.1.2 "><p id="p169441144111414"><a name="p169441144111414"></a><a name="p169441144111414"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="40.33596640335966%" headers="mcps1.2.4.1.3 "><p id="p199461944101413"><a name="p199461944101413"></a><a name="p199461944101413"></a>Specifies the time when a blacklist or whitelist rule is added.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section1014014529435"></a>

**total**  with a value of  **2**  is used as an example.

Response example

```
{
  "total": 2,
  "items": [{
      "id": "3a9b5c0f96784ec8abd8ba61a98064ef",
      "policy_id": "ertr45c0f96784ec8abd8ba61a98064ef",
      "addr": "X.X.0.125",
      "white": 1,
      "timestamp": 1499817600
    }, {
      "id": "44d887434169475794b2717438f7fa78",
      "policy_id": "ertr45c0f96784ec8abd8ba61a98064ef",
      "addr": "X.X.0.125",
      "white": 0,
      "timestamp": 1499817601
    }
  ]
}

```

## Status Code<a name="section936614"></a>

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

