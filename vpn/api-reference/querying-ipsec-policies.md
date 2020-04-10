# Querying IPsec Policies<a name="en_topic_0093011506"></a>

## **Function**<a name="section18389930"></a>

This interface is used to query IPsec policies.

## URI<a name="section31291646"></a>

GET /v2.0/vpn/ipsecpolicies

## Request Message<a name="section51595365"></a>

[Table 1](#table47787675)  describes the request parameters.

**Table  1**  Request parameters

<a name="table47787675"></a>
<table><thead align="left"><tr id="row19017142"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p63993496"><a name="p63993496"></a><a name="p63993496"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p16090703"><a name="p16090703"></a><a name="p16090703"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p28278595"><a name="p28278595"></a><a name="p28278595"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p8864859"><a name="p8864859"></a><a name="p8864859"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row46964992"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p46067993"><a name="p46067993"></a><a name="p46067993"></a>fields</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p40519951"><a name="p40519951"></a><a name="p40519951"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p60890569"><a name="p60890569"></a><a name="p60890569"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p33189039"><a name="p33189039"></a><a name="p33189039"></a>Controls which parameters are returned. If this parameter is not specified, all parameters will be returned.</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>The  **project\_id**  parameter is not supported.  

## Response Message<a name="section61705107"></a>

[Table 2](#table3957675)  describes the response parameters.

**Table  2**  Response parameters

<a name="table3957675"></a>
<table><thead align="left"><tr id="row40026340"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p20908074"><a name="p20908074"></a><a name="p20908074"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p15832433"><a name="p15832433"></a><a name="p15832433"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p59182880"><a name="p59182880"></a><a name="p59182880"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row29083993"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p6993202"><a name="p6993202"></a><a name="p6993202"></a>transform_protocol</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p29578451"><a name="p29578451"></a><a name="p29578451"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p52493967"><a name="p52493967"></a><a name="p52493967"></a>Specifies the transform protocol used. The value can be <strong id="b842352706214431"><a name="b842352706214431"></a><a name="b842352706214431"></a>esp</strong>, <strong id="b842352706214435"><a name="b842352706214435"></a><a name="b842352706214435"></a>ah</strong>, or <strong id="b842352706214439"><a name="b842352706214439"></a><a name="b842352706214439"></a>ah-esp</strong>. The default value is <strong id="b842352706185243"><a name="b842352706185243"></a><a name="b842352706185243"></a>esp</strong>.</p>
</td>
</tr>
<tr id="row2683661"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p16049999"><a name="p16049999"></a><a name="p16049999"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p24981566"><a name="p24981566"></a><a name="p24981566"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p24211521"><a name="p24211521"></a><a name="p24211521"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row16577099"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p567760"><a name="p567760"></a><a name="p567760"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p45988614"><a name="p45988614"></a><a name="p45988614"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p9847715"><a name="p9847715"></a><a name="p9847715"></a>Specifies the IPsec policy ID.</p>
</td>
</tr>
<tr id="row21520579"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p65445301"><a name="p65445301"></a><a name="p65445301"></a>encapsulation_mode</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p66578044"><a name="p66578044"></a><a name="p66578044"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p6956456"><a name="p6956456"></a><a name="p6956456"></a>Specifies the encapsulation mode. The default value is <strong id="b84235270617116"><a name="b84235270617116"></a><a name="b84235270617116"></a>tunnel</strong>.</p>
</td>
</tr>
<tr id="row62608109"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p38092103"><a name="p38092103"></a><a name="p38092103"></a>pfs</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p65561530"><a name="p65561530"></a><a name="p65561530"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p6588145672511"><a name="p6588145672511"></a><a name="p6588145672511"></a>Specifies the PFS. The value can be <strong id="b17777143023410"><a name="b17777143023410"></a><a name="b17777143023410"></a>group1</strong>, <strong id="b14778113093410"><a name="b14778113093410"></a><a name="b14778113093410"></a>group2</strong>, <strong id="b877812302349"><a name="b877812302349"></a><a name="b877812302349"></a>group5</strong>, <strong id="b3778143053414"><a name="b3778143053414"></a><a name="b3778143053414"></a>group14</strong>, <strong id="b37785307341"><a name="b37785307341"></a><a name="b37785307341"></a>group15</strong>, <strong id="b16779630123415"><a name="b16779630123415"></a><a name="b16779630123415"></a>group16</strong>, <strong id="b6780193053410"><a name="b6780193053410"></a><a name="b6780193053410"></a>group19</strong>, <strong id="b12780143053418"><a name="b12780143053418"></a><a name="b12780143053418"></a>group20</strong>, <strong id="b147823300346"><a name="b147823300346"></a><a name="b147823300346"></a>group21</strong>, or <strong id="b147822030143411"><a name="b147822030143411"></a><a name="b147822030143411"></a>disable</strong>.</p>
<p id="p489023122614"><a name="p489023122614"></a><a name="p489023122614"></a>The default value is <strong id="b912323216347"><a name="b912323216347"></a><a name="b912323216347"></a>group5</strong>.</p>
<p id="p2048184412287"><a name="p2048184412287"></a><a name="p2048184412287"></a>The value <strong id="b29481933163419"><a name="b29481933163419"></a><a name="b29481933163419"></a>disable</strong> indicates that the PFS function is disabled.</p>
</td>
</tr>
<tr id="row33761356"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p50315352"><a name="p50315352"></a><a name="p50315352"></a>lifetime</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p49011679"><a name="p49011679"></a><a name="p49011679"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p47063428"><a name="p47063428"></a><a name="p47063428"></a>Specifies the lifetime object of SA.</p>
</td>
</tr>
<tr id="row20917673"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p16609919"><a name="p16609919"></a><a name="p16609919"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p3226198"><a name="p3226198"></a><a name="p3226198"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p27795493"><a name="p27795493"></a><a name="p27795493"></a>Specifies the IPsec policy name.</p>
</td>
</tr>
<tr id="row48832851"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p63146847"><a name="p63146847"></a><a name="p63146847"></a>auth_algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p14620943"><a name="p14620943"></a><a name="p14620943"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p29441404"><a name="p29441404"></a><a name="p29441404"></a>Specifies the authentication hash algorithm. The value can be <strong id="b842352706165820"><a name="b842352706165820"></a><a name="b842352706165820"></a>md5</strong>, <strong id="b842352706165823"><a name="b842352706165823"></a><a name="b842352706165823"></a>sha1</strong>, <strong id="b842352706165833"><a name="b842352706165833"></a><a name="b842352706165833"></a>sha2-256</strong>, <strong id="b842352706165840"><a name="b842352706165840"></a><a name="b842352706165840"></a>sha2-384</strong>, or <strong id="b842352706165851"><a name="b842352706165851"></a><a name="b842352706165851"></a>sha2-512</strong>.</p>
</td>
</tr>
<tr id="row63646052"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p55056607"><a name="p55056607"></a><a name="p55056607"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p30400195"><a name="p30400195"></a><a name="p30400195"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p8135907"><a name="p8135907"></a><a name="p8135907"></a>Provides supplementary information about the IPsec policy.</p>
</td>
</tr>
<tr id="row6114302"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p25496434"><a name="p25496434"></a><a name="p25496434"></a>ipsecpolicies</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p51945267"><a name="p51945267"></a><a name="p51945267"></a>List&lt;Object&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p34085817"><a name="p34085817"></a><a name="p34085817"></a>Specifies the IPsec policy list.</p>
</td>
</tr>
<tr id="row66697461"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p33785274"><a name="p33785274"></a><a name="p33785274"></a>encryption_algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p52252659"><a name="p52252659"></a><a name="p52252659"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p37621475"><a name="p37621475"></a><a name="p37621475"></a>Specifies the encryption algorithm. The value can be <strong id="b8423527061721"><a name="b8423527061721"></a><a name="b8423527061721"></a>3des</strong>, <strong id="b84235270617211"><a name="b84235270617211"></a><a name="b84235270617211"></a>aes-128</strong>, <strong id="b84235270617219"><a name="b84235270617219"></a><a name="b84235270617219"></a>aes-192</strong>, or <strong id="b84235270617227"><a name="b84235270617227"></a><a name="b84235270617227"></a>aes-256</strong>. The default value is <strong id="b84235270617239"><a name="b84235270617239"></a><a name="b84235270617239"></a>aes-128</strong>.</p>
</td>
</tr>
<tr id="row3048957"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p45638969"><a name="p45638969"></a><a name="p45638969"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p5769005"><a name="p5769005"></a><a name="p5769005"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p1048160"><a name="p1048160"></a><a name="p1048160"></a>Specifies the lifetime value of the SA. The default unit is <strong id="b842352706101036"><a name="b842352706101036"></a><a name="b842352706101036"></a>seconds.</strong> The default value is <strong id="b842352706101040"><a name="b842352706101040"></a><a name="b842352706101040"></a>3600</strong>.</p>
</td>
</tr>
<tr id="row9433441"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p25911262"><a name="p25911262"></a><a name="p25911262"></a>units</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p18437496"><a name="p18437496"></a><a name="p18437496"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p38240801"><a name="p38240801"></a><a name="p38240801"></a>Specifies the lifecycle unit. The default value is <strong id="b842352706101045"><a name="b842352706101045"></a><a name="b842352706101045"></a>seconds</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section18475057"></a>

-   Example Request

    ```
    GET /v2.0/vpn/ipsecpolicies
    ```


-   Example Response

    ```
    {
      "ipsecpolicies" : [ {
        "name" : "ipsecpolicy1",
        "transform_protocol" : "esp",
        "auth_algorithm" : "sha1",
        "encapsulation_mode" : "tunnel",
        "encryption_algorithm" : "aes-128",
        "pfs" : "group14",
        "project_id" : "ccb81365fe36411a9011e90491fe1330",
        "tenant_id" : "ccb81365fe36411a9011e90491fe1330",
        "lifetime" : {
          "units" : "seconds",
          "value" : 3600
        },
        "id" : "5291b189-fd84-46e5-84bd-78f40c05d69c",
        "description" : ""
      } ]
    }
    ```


## Returned Values<a name="section6578292"></a>

For details, see section  [Common Returned Values](common-returned-values.md).

