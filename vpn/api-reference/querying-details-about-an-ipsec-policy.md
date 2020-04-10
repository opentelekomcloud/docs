# Querying Details About an IPsec Policy<a name="en_topic_0093011505"></a>

## **Function**<a name="section46564252"></a>

This interface is used to query details about an IPsec policy.

## URI<a name="section16425092"></a>

GET /v2.0/vpn/ipsecpolicies/\{ipsecpolicy\_id\}

**Table  1**  Parameter description

<a name="table1825652715511"></a>
<table><thead align="left"><tr id="row12264132715556"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p102643279555"><a name="p102643279555"></a><a name="p102643279555"></a><strong id="b842352706172115"><a name="b842352706172115"></a><a name="b842352706172115"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p82641027125511"><a name="p82641027125511"></a><a name="p82641027125511"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p1927219279559"><a name="p1927219279559"></a><a name="p1927219279559"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p427219276555"><a name="p427219276555"></a><a name="p427219276555"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row132721527165517"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p1627212278556"><a name="p1627212278556"></a><a name="p1627212278556"></a>ipsecpolicy_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p10272827185512"><a name="p10272827185512"></a><a name="p10272827185512"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p13280427125520"><a name="p13280427125520"></a><a name="p13280427125520"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p32801027195514"><a name="p32801027195514"></a><a name="p32801027195514"></a>Specifies the IPsec policy ID.</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>1.  The  **project\_id**  parameter is not supported.  
>2.  The  **ipsecpolicy\_id**  parameter must be specified.  

## Request Message<a name="section55364084"></a>

None

## Response Message<a name="section28514710"></a>

[Table 2](#table38520254)  describes the response parameters.

**Table  2**  Response parameters

<a name="table38520254"></a>
<table><thead align="left"><tr id="row37494699"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p17171756"><a name="p17171756"></a><a name="p17171756"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p48735027"><a name="p48735027"></a><a name="p48735027"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p43884268"><a name="p43884268"></a><a name="p43884268"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row64964848"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p27661336"><a name="p27661336"></a><a name="p27661336"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p25975757"><a name="p25975757"></a><a name="p25975757"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p37538044"><a name="p37538044"></a><a name="p37538044"></a>Specifies the IPsec policy name.</p>
</td>
</tr>
<tr id="row2298077"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p51926520"><a name="p51926520"></a><a name="p51926520"></a>encapsulation_mode</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p45298596"><a name="p45298596"></a><a name="p45298596"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p46041549"><a name="p46041549"></a><a name="p46041549"></a>Specifies the encapsulation mode. The default value is <strong id="b84235270617116"><a name="b84235270617116"></a><a name="b84235270617116"></a>tunnel</strong>.</p>
</td>
</tr>
<tr id="row11720763"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p9857780"><a name="p9857780"></a><a name="p9857780"></a>encryption_algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p60282721"><a name="p60282721"></a><a name="p60282721"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p42401657"><a name="p42401657"></a><a name="p42401657"></a>Specifies the encryption algorithm. The value can be <strong id="b8423527061721"><a name="b8423527061721"></a><a name="b8423527061721"></a>3des</strong>, <strong id="b84235270617211"><a name="b84235270617211"></a><a name="b84235270617211"></a>aes-128</strong>, <strong id="b84235270617219"><a name="b84235270617219"></a><a name="b84235270617219"></a>aes-192</strong>, or <strong id="b84235270617227"><a name="b84235270617227"></a><a name="b84235270617227"></a>aes-256</strong>. The default value is <strong id="b84235270617239"><a name="b84235270617239"></a><a name="b84235270617239"></a>aes-128</strong>.</p>
</td>
</tr>
<tr id="row46070597"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p40730901"><a name="p40730901"></a><a name="p40730901"></a>pfs</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p10868702"><a name="p10868702"></a><a name="p10868702"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p6588145672511"><a name="p6588145672511"></a><a name="p6588145672511"></a>Specifies the PFS. The value can be <strong id="b16631131916346"><a name="b16631131916346"></a><a name="b16631131916346"></a>group1</strong>, <strong id="b15631121920344"><a name="b15631121920344"></a><a name="b15631121920344"></a>group2</strong>, <strong id="b563214194344"><a name="b563214194344"></a><a name="b563214194344"></a>group5</strong>, <strong id="b3632519183410"><a name="b3632519183410"></a><a name="b3632519183410"></a>group14</strong>, <strong id="b16634101920341"><a name="b16634101920341"></a><a name="b16634101920341"></a>group15</strong>, <strong id="b116342019123412"><a name="b116342019123412"></a><a name="b116342019123412"></a>group16</strong>, <strong id="b18635111919344"><a name="b18635111919344"></a><a name="b18635111919344"></a>group19</strong>, <strong id="b3635171993410"><a name="b3635171993410"></a><a name="b3635171993410"></a>group20</strong>, <strong id="b156351319193417"><a name="b156351319193417"></a><a name="b156351319193417"></a>group21</strong>, or <strong id="b86354194344"><a name="b86354194344"></a><a name="b86354194344"></a>disable</strong>.</p>
<p id="p489023122614"><a name="p489023122614"></a><a name="p489023122614"></a>The default value is <strong id="b149071202348"><a name="b149071202348"></a><a name="b149071202348"></a>group5</strong>.</p>
<p id="p1525913569288"><a name="p1525913569288"></a><a name="p1525913569288"></a>The value <strong id="b17842102193418"><a name="b17842102193418"></a><a name="b17842102193418"></a>disable</strong> indicates that the PFS function is disabled.</p>
</td>
</tr>
<tr id="row23924539"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p58839532"><a name="p58839532"></a><a name="p58839532"></a>lifetime</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p121151126299"><a name="p121151126299"></a><a name="p121151126299"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p29516363"><a name="p29516363"></a><a name="p29516363"></a>Specifies the lifetime object of SA.</p>
</td>
</tr>
<tr id="row64320678"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p42592467"><a name="p42592467"></a><a name="p42592467"></a>transform_protocol</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p27437792"><a name="p27437792"></a><a name="p27437792"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p33381819"><a name="p33381819"></a><a name="p33381819"></a>Specifies the transform protocol used. The value can be <strong id="b842352706184452"><a name="b842352706184452"></a><a name="b842352706184452"></a>esp</strong>, <strong id="b842352706184456"><a name="b842352706184456"></a><a name="b842352706184456"></a>ah</strong>, or <strong id="b84235270618456"><a name="b84235270618456"></a><a name="b84235270618456"></a>ah-esp</strong>. The default value is <strong id="b842352706201018"><a name="b842352706201018"></a><a name="b842352706201018"></a>esp</strong>.</p>
</td>
</tr>
<tr id="row32000920"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p41937705"><a name="p41937705"></a><a name="p41937705"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p41510976"><a name="p41510976"></a><a name="p41510976"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p25743641"><a name="p25743641"></a><a name="p25743641"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row30366184"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p43741849"><a name="p43741849"></a><a name="p43741849"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p53428882"><a name="p53428882"></a><a name="p53428882"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p37304191"><a name="p37304191"></a><a name="p37304191"></a>Specifies the IPsec policy ID.</p>
</td>
</tr>
<tr id="row193401"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p15665491"><a name="p15665491"></a><a name="p15665491"></a>auth_algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p60945241"><a name="p60945241"></a><a name="p60945241"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p27120652"><a name="p27120652"></a><a name="p27120652"></a>Specifies the authentication hash algorithm. The value can be <strong id="b842352706165820"><a name="b842352706165820"></a><a name="b842352706165820"></a>md5</strong>, <strong id="b842352706165823"><a name="b842352706165823"></a><a name="b842352706165823"></a>sha1</strong>, <strong id="b842352706165833"><a name="b842352706165833"></a><a name="b842352706165833"></a>sha2-256</strong>, <strong id="b842352706165840"><a name="b842352706165840"></a><a name="b842352706165840"></a>sha2-384</strong>, or <strong id="b842352706165851"><a name="b842352706165851"></a><a name="b842352706165851"></a>sha2-512</strong>.</p>
</td>
</tr>
<tr id="row42759282"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p40949840"><a name="p40949840"></a><a name="p40949840"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p28602718"><a name="p28602718"></a><a name="p28602718"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p26049579"><a name="p26049579"></a><a name="p26049579"></a>Provides supplementary information about the IPsec policy.</p>
</td>
</tr>
<tr id="row57582125"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p33640543"><a name="p33640543"></a><a name="p33640543"></a>ipsecpolicy</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p40529449"><a name="p40529449"></a><a name="p40529449"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p28400552"><a name="p28400552"></a><a name="p28400552"></a>Specifies the IPsec policy object.</p>
</td>
</tr>
<tr id="row56982912"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p52213166"><a name="p52213166"></a><a name="p52213166"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p1408093"><a name="p1408093"></a><a name="p1408093"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p44589661"><a name="p44589661"></a><a name="p44589661"></a>Specifies the lifetime value of the SA. The default unit is <strong id="b84235270610926"><a name="b84235270610926"></a><a name="b84235270610926"></a>seconds</strong>. The default value is <strong id="b84235270610932"><a name="b84235270610932"></a><a name="b84235270610932"></a>3600</strong>.</p>
</td>
</tr>
<tr id="row65762630"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p25172842"><a name="p25172842"></a><a name="p25172842"></a>units</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p25734322"><a name="p25734322"></a><a name="p25734322"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p64098000"><a name="p64098000"></a><a name="p64098000"></a>Specifies the lifecycle unit. The default value is <strong id="b84235270610104"><a name="b84235270610104"></a><a name="b84235270610104"></a>seconds</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section55305800"></a>

-   Example Request

    ```
    GET /v2.0/vpn/ipsecpolicies/{ipsecpolicy_id}
    ```


-   Example Response

    ```
    {
      "ipsecpolicy" : {
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
      }
    }
    ```


## Returned Values<a name="section6578292"></a>

For details, see section  [Common Returned Values](common-returned-values.md).

