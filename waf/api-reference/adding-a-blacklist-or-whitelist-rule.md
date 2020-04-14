# Adding a Blacklist or Whitelist Rule<a name="EN-US_TOPIC_0193631189"></a>

## Function Description<a name="section3580440"></a>

This API is used to add a blacklist or whitelist rule.

## URI<a name="section32223962"></a>

-   URI format

    POST  /v1/\{project\_id\}/waf/policy/\{policy\_id\}/whiteblackip

-   Parameter description

    **Table  1**  Path parameters

    <a name="table55185573"></a>
    <table><thead align="left"><tr id="row48252727"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p16156794"><a name="p16156794"></a><a name="p16156794"></a><strong id="b17547122985512"><a name="b17547122985512"></a><a name="b17547122985512"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.2"><p id="p33631909"><a name="p33631909"></a><a name="p33631909"></a><strong id="b1484893425518"><a name="b1484893425518"></a><a name="b1484893425518"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.3"><p id="p39830113"><a name="p39830113"></a><a name="p39830113"></a><strong id="b193819366552"><a name="b193819366552"></a><a name="b193819366552"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.5.1.4"><p id="p5013717"><a name="p5013717"></a><a name="p5013717"></a><strong id="b8445153815513"><a name="b8445153815513"></a><a name="b8445153815513"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3457962"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p11659528"><a name="p11659528"></a><a name="p11659528"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p4897686"><a name="p4897686"></a><a name="p4897686"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p61168252"><a name="p61168252"></a><a name="p61168252"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p55681379"><a name="p55681379"></a><a name="p55681379"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row31370366"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p57971721"><a name="p57971721"></a><a name="p57971721"></a>policy_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p65197800"><a name="p65197800"></a><a name="p65197800"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p46530436"><a name="p46530436"></a><a name="p46530436"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p10868932"><a name="p10868932"></a><a name="p10868932"></a>Specifies the policy ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section21580205"></a>

Request parameters

**Table  2**  Parameter description

<a name="table41450321"></a>
<table><thead align="left"><tr id="row48860259"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p65366944"><a name="p65366944"></a><a name="p65366944"></a><strong id="b6553152317584"><a name="b6553152317584"></a><a name="b6553152317584"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.2"><p id="p60231101"><a name="p60231101"></a><a name="p60231101"></a><strong id="b12916324105817"><a name="b12916324105817"></a><a name="b12916324105817"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.3"><p id="p46880994"><a name="p46880994"></a><a name="p46880994"></a><strong id="b1867627155810"><a name="b1867627155810"></a><a name="b1867627155810"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.5.1.4"><p id="p39264184"><a name="p39264184"></a><a name="p39264184"></a><strong id="b271892815817"><a name="b271892815817"></a><a name="b271892815817"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row26282342"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p48494997"><a name="p48494997"></a><a name="p48494997"></a>addr</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p35780717"><a name="p35780717"></a><a name="p35780717"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p12556949"><a name="p12556949"></a><a name="p12556949"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p10479925"><a name="p10479925"></a><a name="p10479925"></a>Specifies the public IP address or range (IP address and subnet mask). For example, <em id="i164311921102413"><a name="i164311921102413"></a><a name="i164311921102413"></a>X.X.</em><strong id="b10431621162410"><a name="b10431621162410"></a><a name="b10431621162410"></a>0.125</strong> or <em id="i9431621142417"><a name="i9431621142417"></a><a name="i9431621142417"></a>X.X.</em><strong id="b17431192142417"><a name="b17431192142417"></a><a name="b17431192142417"></a>6.0/24</strong>.</p>
</td>
</tr>
<tr id="row27210466"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p56564138"><a name="p56564138"></a><a name="p56564138"></a>white</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p18292479"><a name="p18292479"></a><a name="p18292479"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p5295816"><a name="p5295816"></a><a name="p5295816"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p131673177539"><a name="p131673177539"></a><a name="p131673177539"></a>Specifies the IP address type.</p>
<a name="ul3374102111535"></a><a name="ul3374102111535"></a><ul id="ul3374102111535"><li><strong id="b12249191451113"><a name="b12249191451113"></a><a name="b12249191451113"></a>1</strong>: <strong id="b3249121421117"><a name="b3249121421117"></a><a name="b3249121421117"></a>Whitelist</strong></li><li><strong id="b158811021111114"><a name="b158811021111114"></a><a name="b158811021111114"></a>0</strong>: <strong id="b118815212112"><a name="b118815212112"></a><a name="b118815212112"></a>Blacklist</strong> </li></ul>
<p id="p26307950"><a name="p26307950"></a><a name="p26307950"></a>If you do not configure the <strong id="b68703121776"><a name="b68703121776"></a><a name="b68703121776"></a>white</strong> parameter, the value is <strong id="b162551040274"><a name="b162551040274"></a><a name="b162551040274"></a>Blacklist</strong> by default.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section60004123"></a>

Response parameters

**Table  3**  Parameter description

<a name="table8657213"></a>
<table><thead align="left"><tr id="row15637064"><th class="cellrowborder" valign="top" width="42.85571442855714%" id="mcps1.2.4.1.1"><p id="p58642663"><a name="p58642663"></a><a name="p58642663"></a><strong id="b18629191812212"><a name="b18629191812212"></a><a name="b18629191812212"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.4.1.2"><p id="p52435287"><a name="p52435287"></a><a name="p52435287"></a><strong id="b163410207216"><a name="b163410207216"></a><a name="b163410207216"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.4.1.3"><p id="p19399872"><a name="p19399872"></a><a name="p19399872"></a><strong id="b161135218210"><a name="b161135218210"></a><a name="b161135218210"></a>Description</strong></p>
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
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p27261653"><a name="p27261653"></a><a name="p27261653"></a>Specifies the public IP address or range (IP address and subnet mask). For example, <em id="i1643143082412"><a name="i1643143082412"></a><a name="i1643143082412"></a>X.X.</em><strong id="b04316301241"><a name="b04316301241"></a><a name="b04316301241"></a>0.125</strong> or <em id="i1043153052411"><a name="i1043153052411"></a><a name="i1043153052411"></a>X.X.</em><strong id="b104312030172418"><a name="b104312030172418"></a><a name="b104312030172418"></a>6.0/24</strong>.</p>
</td>
</tr>
<tr id="row44028285"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p9521339"><a name="p9521339"></a><a name="p9521339"></a>white</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p33031034"><a name="p33031034"></a><a name="p33031034"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p2060412271548"><a name="p2060412271548"></a><a name="p2060412271548"></a>Specifies the IP address type.</p>
<a name="ul1460411278541"></a><a name="ul1460411278541"></a><ul id="ul1460411278541"><li><strong id="b240313434116"><a name="b240313434116"></a><a name="b240313434116"></a>1</strong>: <strong id="b104033431117"><a name="b104033431117"></a><a name="b104033431117"></a>Whitelist</strong></li><li><strong id="b335518458113"><a name="b335518458113"></a><a name="b335518458113"></a>0</strong>: <strong id="b93555455116"><a name="b93555455116"></a><a name="b93555455116"></a>Blacklist</strong> </li></ul>
<p id="p58268130"><a name="p58268130"></a><a name="p58268130"></a>If you do not configure the <strong id="b5174172911915"><a name="b5174172911915"></a><a name="b5174172911915"></a>white</strong> parameter, the value is <strong id="b14175132910914"><a name="b14175132910914"></a><a name="b14175132910914"></a>Blacklist</strong> by default.</p>
</td>
</tr>
<tr id="row54651124"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p64664939"><a name="p64664939"></a><a name="p64664939"></a>timestamp</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p3368735"><a name="p3368735"></a><a name="p3368735"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p4432119"><a name="p4432119"></a><a name="p4432119"></a>Specifies the time when a blacklist or whitelist rule is added.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="section13981105484415"></a>

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


## Status Code<a name="section3166195"></a>

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

