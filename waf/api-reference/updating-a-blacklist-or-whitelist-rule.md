# Updating a Blacklist or Whitelist Rule<a name="EN-US_TOPIC_0193631129"></a>

## Function Description<a name="section53455492"></a>

This API is used to update a blacklist or whitelist rule.

## URI<a name="section11337384"></a>

-   URI format

    PUT  /v1/\{project\_id\}/waf/policy/\{policy\_id\}/whiteblackip/\{whiteblackip\_rule\_id\}

-   Parameter description

    **Table  1**  Path parameters

    <a name="table40734402"></a>
    <table><thead align="left"><tr id="row58692937"><th class="cellrowborder" valign="top" width="30.930000000000003%" id="mcps1.2.5.1.1"><p id="p56507437"><a name="p56507437"></a><a name="p56507437"></a><strong id="b269068184420"><a name="b269068184420"></a><a name="b269068184420"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.62%" id="mcps1.2.5.1.2"><p id="p13699678"><a name="p13699678"></a><a name="p13699678"></a><strong id="b12633393444"><a name="b12633393444"></a><a name="b12633393444"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.430000000000001%" id="mcps1.2.5.1.3"><p id="p35932099"><a name="p35932099"></a><a name="p35932099"></a><strong id="b5580131011442"><a name="b5580131011442"></a><a name="b5580131011442"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="34.02%" id="mcps1.2.5.1.4"><p id="p24818884"><a name="p24818884"></a><a name="p24818884"></a><strong id="b2052871144420"><a name="b2052871144420"></a><a name="b2052871144420"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row64172619"><td class="cellrowborder" valign="top" width="30.930000000000003%" headers="mcps1.2.5.1.1 "><p id="p30599613"><a name="p30599613"></a><a name="p30599613"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.5.1.2 "><p id="p62649604"><a name="p62649604"></a><a name="p62649604"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.430000000000001%" headers="mcps1.2.5.1.3 "><p id="p41453192"><a name="p41453192"></a><a name="p41453192"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.5.1.4 "><p id="p2265392"><a name="p2265392"></a><a name="p2265392"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row20388533"><td class="cellrowborder" valign="top" width="30.930000000000003%" headers="mcps1.2.5.1.1 "><p id="p40858511"><a name="p40858511"></a><a name="p40858511"></a>policy_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.5.1.2 "><p id="p21205122"><a name="p21205122"></a><a name="p21205122"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.430000000000001%" headers="mcps1.2.5.1.3 "><p id="p39893301"><a name="p39893301"></a><a name="p39893301"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.5.1.4 "><p id="p10131920"><a name="p10131920"></a><a name="p10131920"></a>Specifies the policy ID.</p>
    </td>
    </tr>
    <tr id="row24078420"><td class="cellrowborder" valign="top" width="30.930000000000003%" headers="mcps1.2.5.1.1 "><p id="p4195040"><a name="p4195040"></a><a name="p4195040"></a>whiteblackip_rule_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.5.1.2 "><p id="p4253927"><a name="p4253927"></a><a name="p4253927"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.430000000000001%" headers="mcps1.2.5.1.3 "><p id="p9023827"><a name="p9023827"></a><a name="p9023827"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.5.1.4 "><p id="p59841420"><a name="p59841420"></a><a name="p59841420"></a>Specifies the ID of a blacklist or whitelist rule.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section34927599"></a>

Request parameters

**Table  2**  Parameter description

<a name="table32705923"></a>
<table><thead align="left"><tr id="row51664566"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p24080287"><a name="p24080287"></a><a name="p24080287"></a><strong id="b81585554415"><a name="b81585554415"></a><a name="b81585554415"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.2"><p id="p4346192"><a name="p4346192"></a><a name="p4346192"></a><strong id="b597325554416"><a name="b597325554416"></a><a name="b597325554416"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.3"><p id="p16497266"><a name="p16497266"></a><a name="p16497266"></a><strong id="b1185965664420"><a name="b1185965664420"></a><a name="b1185965664420"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.5.1.4"><p id="p61210156"><a name="p61210156"></a><a name="p61210156"></a><strong id="b168633572440"><a name="b168633572440"></a><a name="b168633572440"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row59075623"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p20396171"><a name="p20396171"></a><a name="p20396171"></a>addr</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p41477118"><a name="p41477118"></a><a name="p41477118"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p4203435"><a name="p4203435"></a><a name="p4203435"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p4933944"><a name="p4933944"></a><a name="p4933944"></a>Specifies the public IP address or range (IP address and subnet mask). For example, <em id="i15610112217277"><a name="i15610112217277"></a><a name="i15610112217277"></a>X.X.</em><strong id="b156251722172710"><a name="b156251722172710"></a><a name="b156251722172710"></a>0.125</strong> or <em id="i4625822152714"><a name="i4625822152714"></a><a name="i4625822152714"></a>X.X.</em><strong id="b12625182222714"><a name="b12625182222714"></a><a name="b12625182222714"></a>6.0/24</strong>.</p>
</td>
</tr>
<tr id="row83631647193016"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p736354716300"><a name="p736354716300"></a><a name="p736354716300"></a>white</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p1836317478309"><a name="p1836317478309"></a><a name="p1836317478309"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p44337548"><a name="p44337548"></a><a name="p44337548"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p131673177539"><a name="p131673177539"></a><a name="p131673177539"></a>Specifies the IP address type.</p>
<a name="ul3374102111535"></a><a name="ul3374102111535"></a><ul id="ul3374102111535"><li><strong id="b207811484455"><a name="b207811484455"></a><a name="b207811484455"></a>1</strong>: <strong id="b117821348124517"><a name="b117821348124517"></a><a name="b117821348124517"></a>Whitelist</strong></li><li><strong id="b020875084510"><a name="b020875084510"></a><a name="b020875084510"></a>0</strong>: <strong id="b1421014506454"><a name="b1421014506454"></a><a name="b1421014506454"></a>Blacklist</strong></li></ul>
</td>
</tr>
</tbody>
</table>

## Response<a name="section45912936"></a>

Response parameters

**Table  3**  Parameter description

<a name="table8657213"></a>
<table><thead align="left"><tr id="row15637064"><th class="cellrowborder" valign="top" width="42.85571442855714%" id="mcps1.2.4.1.1"><p id="p58642663"><a name="p58642663"></a><a name="p58642663"></a><strong id="b119301536134515"><a name="b119301536134515"></a><a name="b119301536134515"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.4.1.2"><p id="p52435287"><a name="p52435287"></a><a name="p52435287"></a><strong id="b17392143884515"><a name="b17392143884515"></a><a name="b17392143884515"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.4.1.3"><p id="p19399872"><a name="p19399872"></a><a name="p19399872"></a><strong id="b19489139114510"><a name="b19489139114510"></a><a name="b19489139114510"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row40381121"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p49645329"><a name="p49645329"></a><a name="p49645329"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p61848685"><a name="p61848685"></a><a name="p61848685"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p43687614"><a name="p43687614"></a><a name="p43687614"></a>Specifies the ID of a blacklist or whitelist rule.</p>
</td>
</tr>
<tr id="row57644214"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p38669777"><a name="p38669777"></a><a name="p38669777"></a>policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p45244245"><a name="p45244245"></a><a name="p45244245"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p40905192"><a name="p40905192"></a><a name="p40905192"></a>Specifies the policy ID.</p>
</td>
</tr>
<tr id="row32602416"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p23550048"><a name="p23550048"></a><a name="p23550048"></a>addr</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p28505716"><a name="p28505716"></a><a name="p28505716"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p27261653"><a name="p27261653"></a><a name="p27261653"></a>Specifies the public IP address or range (IP address and subnet mask). For example, <em id="i76103441277"><a name="i76103441277"></a><a name="i76103441277"></a>X.X.</em><strong id="b1061010448275"><a name="b1061010448275"></a><a name="b1061010448275"></a>0.125</strong> or <em id="i162519443278"><a name="i162519443278"></a><a name="i162519443278"></a>X.X.</em><strong id="b4625144152718"><a name="b4625144152718"></a><a name="b4625144152718"></a>6.0/24</strong>.</p>
</td>
</tr>
<tr id="row44028285"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p9521339"><a name="p9521339"></a><a name="p9521339"></a>white</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p33031034"><a name="p33031034"></a><a name="p33031034"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p153321832551"><a name="p153321832551"></a><a name="p153321832551"></a>Specifies the IP address type.</p>
<a name="ul7332531553"></a><a name="ul7332531553"></a><ul id="ul7332531553"><li><strong id="b3194951174518"><a name="b3194951174518"></a><a name="b3194951174518"></a>1</strong>: <strong id="b91951751134510"><a name="b91951751134510"></a><a name="b91951751134510"></a>Whitelist</strong></li><li><strong id="b618795217456"><a name="b618795217456"></a><a name="b618795217456"></a>0</strong>: <strong id="b16187175210451"><a name="b16187175210451"></a><a name="b16187175210451"></a>Blacklist</strong></li></ul>
<p id="p58268130"><a name="p58268130"></a><a name="p58268130"></a>If you do not configure the <strong id="b4470573109"><a name="b4470573109"></a><a name="b4470573109"></a>white</strong> parameter, the value is <strong id="b24765719108"><a name="b24765719108"></a><a name="b24765719108"></a>Blacklist</strong> by default.</p>
</td>
</tr>
<tr id="row54651124"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p64664939"><a name="p64664939"></a><a name="p64664939"></a>timestamp</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p3368735"><a name="p3368735"></a><a name="p3368735"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p56661280"><a name="p56661280"></a><a name="p56661280"></a>Specifies the time when a blacklist or whitelist rule is added.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="section12227624124710"></a>

_X.X._**0.125**  is used as an example.

-   Request example

    ```
    {
     "addr": "X.X.0.125",
     "white": 1
    }
    ```


-   Response example

    ```
    {
      "id": "44d887434169475794b2717438f7fa78",
      "policy_id": "ertr45c0f96784ec8abd8ba61a98064ef",
      "addr": "X.X.0.125",
      "white": 1,
      "timestamp": 1499817600
    }
    ```


## Status Code<a name="section10563246"></a>

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

