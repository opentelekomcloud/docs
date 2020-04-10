# Querying Details About an IKE Policy<a name="en_topic_0093011511"></a>

## **Function**<a name="section11984159"></a>

This interface is used to query details about an IKE policy.

## URI<a name="section40748571"></a>

GET /v2.0/vpn/ikepolicies/\{ikepolicy\_id\}

**Table  1**  Parameter description

<a name="table6239218796"></a>
<table><thead align="left"><tr id="row723918188913"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p10239918692"><a name="p10239918692"></a><a name="p10239918692"></a><strong id="b842352706172115"><a name="b842352706172115"></a><a name="b842352706172115"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p92472018296"><a name="p92472018296"></a><a name="p92472018296"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p192477181092"><a name="p192477181092"></a><a name="p192477181092"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p22471818494"><a name="p22471818494"></a><a name="p22471818494"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row72472185920"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p22551718093"><a name="p22551718093"></a><a name="p22551718093"></a>ikepolicy_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p525541811914"><a name="p525541811914"></a><a name="p525541811914"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p16255101814915"><a name="p16255101814915"></a><a name="p16255101814915"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p626314181394"><a name="p626314181394"></a><a name="p626314181394"></a>Specifies the IKE policy ID.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section12299945"></a>

None

## Response Message<a name="section43590645"></a>

[Table 2](#table20119003)  describes the response parameters.

**Table  2**  Response parameters

<a name="table20119003"></a>
<table><thead align="left"><tr id="row28597308"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p34680572"><a name="p34680572"></a><a name="p34680572"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p57662920"><a name="p57662920"></a><a name="p57662920"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p33757095"><a name="p33757095"></a><a name="p33757095"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row49970185"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p21053208"><a name="p21053208"></a><a name="p21053208"></a>ikepolicy</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p27588283"><a name="p27588283"></a><a name="p27588283"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p14122463"><a name="p14122463"></a><a name="p14122463"></a>Specifies the IKE policy object.</p>
</td>
</tr>
<tr id="row47637903"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p33464950"><a name="p33464950"></a><a name="p33464950"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p26306458"><a name="p26306458"></a><a name="p26306458"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p59784887"><a name="p59784887"></a><a name="p59784887"></a>Provides supplementary information about the IKE policy.</p>
</td>
</tr>
<tr id="row1193073"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p29530116"><a name="p29530116"></a><a name="p29530116"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p43129175"><a name="p43129175"></a><a name="p43129175"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p39547486"><a name="p39547486"></a><a name="p39547486"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row21477321"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p61941440"><a name="p61941440"></a><a name="p61941440"></a>auth_algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p51200735"><a name="p51200735"></a><a name="p51200735"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p48163256"><a name="p48163256"></a><a name="p48163256"></a>Specifies the authentication hash algorithm. The value can be <strong id="b842352706221137"><a name="b842352706221137"></a><a name="b842352706221137"></a>md5</strong>, <strong id="b842352706221141"><a name="b842352706221141"></a><a name="b842352706221141"></a>sha1</strong>, <strong id="b842352706221145"><a name="b842352706221145"></a><a name="b842352706221145"></a>sha2-256</strong>, <strong id="b842352706221149"><a name="b842352706221149"></a><a name="b842352706221149"></a>sha2-384</strong>, or <strong id="b842352706221154"><a name="b842352706221154"></a><a name="b842352706221154"></a>sha2-512</strong>.</p>
</td>
</tr>
<tr id="row30816121"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p13077833"><a name="p13077833"></a><a name="p13077833"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p52671525"><a name="p52671525"></a><a name="p52671525"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p34340132"><a name="p34340132"></a><a name="p34340132"></a>Specifies the IKE policy name.</p>
</td>
</tr>
<tr id="row40625737"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p2350413"><a name="p2350413"></a><a name="p2350413"></a>encryption_algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p56165728"><a name="p56165728"></a><a name="p56165728"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p8575450"><a name="p8575450"></a><a name="p8575450"></a>Specifies the encryption algorithm. The value can be <strong id="b8423527061721"><a name="b8423527061721"></a><a name="b8423527061721"></a>3des</strong>, <strong id="b84235270617211"><a name="b84235270617211"></a><a name="b84235270617211"></a>aes-128</strong>, <strong id="b84235270617219"><a name="b84235270617219"></a><a name="b84235270617219"></a>aes-192</strong>, or <strong id="b84235270617227"><a name="b84235270617227"></a><a name="b84235270617227"></a>aes-256</strong>. The default value is <strong id="b84235270617239"><a name="b84235270617239"></a><a name="b84235270617239"></a>aes-128</strong>.</p>
</td>
</tr>
<tr id="row10070188"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p10378893"><a name="p10378893"></a><a name="p10378893"></a>pfs</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p35383970"><a name="p35383970"></a><a name="p35383970"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p6588145672511"><a name="p6588145672511"></a><a name="p6588145672511"></a>Specifies the PFS. The value can be <strong id="b5874112573516"><a name="b5874112573516"></a><a name="b5874112573516"></a>group1</strong>, <strong id="b15874152516358"><a name="b15874152516358"></a><a name="b15874152516358"></a>group2</strong>, <strong id="b1387592593513"><a name="b1387592593513"></a><a name="b1387592593513"></a>group5</strong>, <strong id="b178751525163511"><a name="b178751525163511"></a><a name="b178751525163511"></a>group14</strong>, <strong id="b2087552513357"><a name="b2087552513357"></a><a name="b2087552513357"></a>group15</strong>, <strong id="b087582519352"><a name="b087582519352"></a><a name="b087582519352"></a>group16</strong>, <strong id="b208761125163510"><a name="b208761125163510"></a><a name="b208761125163510"></a>group19</strong>, <strong id="b187617255357"><a name="b187617255357"></a><a name="b187617255357"></a>group20</strong>, <strong id="b168781425193516"><a name="b168781425193516"></a><a name="b168781425193516"></a>group21</strong>, or <strong id="b3878182516358"><a name="b3878182516358"></a><a name="b3878182516358"></a>disable</strong>.</p>
<p id="p489023122614"><a name="p489023122614"></a><a name="p489023122614"></a>The default value is <strong id="b17132763517"><a name="b17132763517"></a><a name="b17132763517"></a>group5</strong>.</p>
</td>
</tr>
<tr id="row20685786"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p64935954"><a name="p64935954"></a><a name="p64935954"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p25320898"><a name="p25320898"></a><a name="p25320898"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p35977388"><a name="p35977388"></a><a name="p35977388"></a>Specifies the lifetime value of the SA. The default unit is <strong id="b842352706101552"><a name="b842352706101552"></a><a name="b842352706101552"></a>seconds</strong>. The default value is <strong id="b842352706101556"><a name="b842352706101556"></a><a name="b842352706101556"></a>3600</strong>.</p>
</td>
</tr>
<tr id="row55361044"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p55059565"><a name="p55059565"></a><a name="p55059565"></a>phase1_negotiation_mode</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p30639779"><a name="p30639779"></a><a name="p30639779"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p36543171"><a name="p36543171"></a><a name="p36543171"></a>Specifies the IKE mode The default value is <strong id="b842352706213613"><a name="b842352706213613"></a><a name="b842352706213613"></a>main</strong>.</p>
</td>
</tr>
<tr id="row60453091"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p64862199"><a name="p64862199"></a><a name="p64862199"></a>units</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p19346796"><a name="p19346796"></a><a name="p19346796"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p31471768"><a name="p31471768"></a><a name="p31471768"></a>Specifies the lifecycle unit. The default value is <strong id="b8423527061079"><a name="b8423527061079"></a><a name="b8423527061079"></a>seconds</strong>.</p>
</td>
</tr>
<tr id="row14810456"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p58796306"><a name="p58796306"></a><a name="p58796306"></a>lifetime</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p64880336"><a name="p64880336"></a><a name="p64880336"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p8363642"><a name="p8363642"></a><a name="p8363642"></a>Specifies the lifetime object of SA.</p>
</td>
</tr>
<tr id="row8163917"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p57297510"><a name="p57297510"></a><a name="p57297510"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p10586695"><a name="p10586695"></a><a name="p10586695"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p1634435"><a name="p1634435"></a><a name="p1634435"></a>Specifies the IKE policy ID.</p>
</td>
</tr>
<tr id="row14709921"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p50652963"><a name="p50652963"></a><a name="p50652963"></a>ike_version</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p9249362"><a name="p9249362"></a><a name="p9249362"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p18653909"><a name="p18653909"></a><a name="p18653909"></a>Specifies the IKE version number. The value can be <strong id="b842352706201636"><a name="b842352706201636"></a><a name="b842352706201636"></a>v1</strong> or <strong id="b842352706201645"><a name="b842352706201645"></a><a name="b842352706201645"></a>v2</strong>. The default value is <strong id="b842352706201018"><a name="b842352706201018"></a><a name="b842352706201018"></a>v1</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section56771492"></a>

-   Example Request

    ```
    GET /v2.0/vpn/ikepolicies/{ikepolicy_id}
    ```


-   Example Response

    ```
    {
      "ikepolicy" : {
        "name" : "ikepolicy1",
        "tenant_id" : "ccb81365fe36411a9011e90491fe1330",
        "auth_algorithm" : "sha1",
        "encryption_algorithm" : "aes-256",
        "pfs" : "group5",
        "phase1_negotiation_mode" : "main",
        "lifetime" : {
          "units" : "seconds",
          "value" : 3600
        },
        "ike_version" : "v1",
        "id" : "5522aff7-1b3c-48dd-9c3c-b50f016b73db",
        "description" : ""
      }
    }
    ```


## Returned Values<a name="section6578292"></a>

For details, see section  [Common Returned Values](common-returned-values.md).

