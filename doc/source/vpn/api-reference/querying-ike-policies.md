# Querying IKE Policies<a name="en_topic_0093011512"></a>

## **Function**<a name="section53330552"></a>

This interface is used to query IKE policies.

## URI<a name="section10212927"></a>

GET /v2.0/vpn/ikepolicies

## Request Message<a name="section21940722"></a>

[Table 1](#table61502840)  describes the request parameters.

**Table  1**  Request parameters

<a name="table61502840"></a>
<table><thead align="left"><tr id="row45420240"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p55160823"><a name="p55160823"></a><a name="p55160823"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p38841670"><a name="p38841670"></a><a name="p38841670"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p59167590"><a name="p59167590"></a><a name="p59167590"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p27845503"><a name="p27845503"></a><a name="p27845503"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row40893240"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p24018105"><a name="p24018105"></a><a name="p24018105"></a>fields</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p66418347"><a name="p66418347"></a><a name="p66418347"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p11177013"><a name="p11177013"></a><a name="p11177013"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p32922880"><a name="p32922880"></a><a name="p32922880"></a>Controls which parameters are returned. If this parameter is not specified, all parameters will be returned.</p>
</td>
</tr>
</tbody>
</table>

>![](/images/icon-note.gif) **NOTE:**   
>The  **project\_id**  parameter is not supported.  

## Response Message<a name="section63248778"></a>

[Table 2](#table49507636)  describes the response parameters.

**Table  2**  Response parameters

<a name="table49507636"></a>
<table><thead align="left"><tr id="row63187419"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p17907308"><a name="p17907308"></a><a name="p17907308"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p41205809"><a name="p41205809"></a><a name="p41205809"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p36810105"><a name="p36810105"></a><a name="p36810105"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row28828491"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p53406450"><a name="p53406450"></a><a name="p53406450"></a>ikepolicies</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p30955222"><a name="p30955222"></a><a name="p30955222"></a>List&lt;Object&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p25792371"><a name="p25792371"></a><a name="p25792371"></a>Specifies the IKE policy list.</p>
</td>
</tr>
<tr id="row30804749"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p12156768"><a name="p12156768"></a><a name="p12156768"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p45174131"><a name="p45174131"></a><a name="p45174131"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p34731002"><a name="p34731002"></a><a name="p34731002"></a>Provides supplementary information about the IKE policy.</p>
</td>
</tr>
<tr id="row44143566"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p18859061"><a name="p18859061"></a><a name="p18859061"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p51188993"><a name="p51188993"></a><a name="p51188993"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p38233575"><a name="p38233575"></a><a name="p38233575"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row4485813"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p27806533"><a name="p27806533"></a><a name="p27806533"></a>auth_algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p37736673"><a name="p37736673"></a><a name="p37736673"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p25717600"><a name="p25717600"></a><a name="p25717600"></a>Specifies the authentication hash algorithm. The value can be <strong id="b842352706221137"><a name="b842352706221137"></a><a name="b842352706221137"></a>md5</strong>, <strong id="b842352706221141"><a name="b842352706221141"></a><a name="b842352706221141"></a>sha1</strong>, <strong id="b842352706221145"><a name="b842352706221145"></a><a name="b842352706221145"></a>sha2-256</strong>, <strong id="b842352706221149"><a name="b842352706221149"></a><a name="b842352706221149"></a>sha2-384</strong>, or <strong id="b842352706221154"><a name="b842352706221154"></a><a name="b842352706221154"></a>sha2-512</strong>.</p>
</td>
</tr>
<tr id="row30131813"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p24757801"><a name="p24757801"></a><a name="p24757801"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p59224828"><a name="p59224828"></a><a name="p59224828"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p13780214"><a name="p13780214"></a><a name="p13780214"></a>Specifies the IKE policy name.</p>
</td>
</tr>
<tr id="row56913064"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p46555465"><a name="p46555465"></a><a name="p46555465"></a>encryption_algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p12896286"><a name="p12896286"></a><a name="p12896286"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p55365254"><a name="p55365254"></a><a name="p55365254"></a>Specifies the encryption algorithm. The value can be <strong id="b8423527061721"><a name="b8423527061721"></a><a name="b8423527061721"></a>3des</strong>, <strong id="b84235270617211"><a name="b84235270617211"></a><a name="b84235270617211"></a>aes-128</strong>, <strong id="b84235270617219"><a name="b84235270617219"></a><a name="b84235270617219"></a>aes-192</strong>, or <strong id="b84235270617227"><a name="b84235270617227"></a><a name="b84235270617227"></a>aes-256</strong>. The default value is <strong id="b84235270617239"><a name="b84235270617239"></a><a name="b84235270617239"></a>aes-128</strong>.</p>
</td>
</tr>
<tr id="row28525238"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p28842926"><a name="p28842926"></a><a name="p28842926"></a>pfs</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p54575646"><a name="p54575646"></a><a name="p54575646"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p6588145672511"><a name="p6588145672511"></a><a name="p6588145672511"></a>Specifies the PFS. The value can be <strong id="b698675117355"><a name="b698675117355"></a><a name="b698675117355"></a>group1</strong>, <strong id="b49863518352"><a name="b49863518352"></a><a name="b49863518352"></a>group2</strong>, <strong id="b1987115183511"><a name="b1987115183511"></a><a name="b1987115183511"></a>group5</strong>, <strong id="b0987105103517"><a name="b0987105103517"></a><a name="b0987105103517"></a>group14</strong>, <strong id="b299085111351"><a name="b299085111351"></a><a name="b299085111351"></a>group15</strong>, <strong id="b169918510359"><a name="b169918510359"></a><a name="b169918510359"></a>group16</strong>, <strong id="b699145103514"><a name="b699145103514"></a><a name="b699145103514"></a>group19</strong>, <strong id="b179921517359"><a name="b179921517359"></a><a name="b179921517359"></a>group20</strong>, <strong id="b12992135113511"><a name="b12992135113511"></a><a name="b12992135113511"></a>group21</strong>, or <strong id="b699311511358"><a name="b699311511358"></a><a name="b699311511358"></a>disable</strong>.</p>
<p id="p489023122614"><a name="p489023122614"></a><a name="p489023122614"></a>The default value is <strong id="b772618554356"><a name="b772618554356"></a><a name="b772618554356"></a>group5</strong>.</p>
</td>
</tr>
<tr id="row2598608"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p9160681"><a name="p9160681"></a><a name="p9160681"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p3817695"><a name="p3817695"></a><a name="p3817695"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p16291455"><a name="p16291455"></a><a name="p16291455"></a>Specifies the lifetime value of the SA. The default unit is <strong id="b842352706101627"><a name="b842352706101627"></a><a name="b842352706101627"></a>seconds</strong>. The default value is <strong id="b842352706101631"><a name="b842352706101631"></a><a name="b842352706101631"></a>3600</strong>.</p>
</td>
</tr>
<tr id="row12405375"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p65311315"><a name="p65311315"></a><a name="p65311315"></a>phase1_negotiation_mode</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p55725192"><a name="p55725192"></a><a name="p55725192"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p3898676"><a name="p3898676"></a><a name="p3898676"></a>Specifies the IKE mode The default value is <strong id="b842352706213613"><a name="b842352706213613"></a><a name="b842352706213613"></a>main</strong>.</p>
</td>
</tr>
<tr id="row35088084"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p23562574"><a name="p23562574"></a><a name="p23562574"></a>units</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p29520332"><a name="p29520332"></a><a name="p29520332"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p6720246"><a name="p6720246"></a><a name="p6720246"></a>Specifies the lifecycle unit. The default value is <strong id="b8423527061079"><a name="b8423527061079"></a><a name="b8423527061079"></a>seconds</strong>.</p>
</td>
</tr>
<tr id="row60482217"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p112514"><a name="p112514"></a><a name="p112514"></a>lifetime</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p9113635"><a name="p9113635"></a><a name="p9113635"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p564191"><a name="p564191"></a><a name="p564191"></a>Specifies the lifetime object of SA.</p>
</td>
</tr>
<tr id="row5077725"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p8642591"><a name="p8642591"></a><a name="p8642591"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p28961294"><a name="p28961294"></a><a name="p28961294"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p29858833"><a name="p29858833"></a><a name="p29858833"></a>Specifies the IKE policy ID.</p>
</td>
</tr>
<tr id="row294043"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p23817504"><a name="p23817504"></a><a name="p23817504"></a>ike_version</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p50169686"><a name="p50169686"></a><a name="p50169686"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p61444595"><a name="p61444595"></a><a name="p61444595"></a>Specifies the IKE version. The value can be <strong id="b2123880768213834"><a name="b2123880768213834"></a><a name="b2123880768213834"></a>v1</strong> or <strong id="b499525058213834"><a name="b499525058213834"></a><a name="b499525058213834"></a>v2</strong>. The default value is <strong id="b842352706213844"><a name="b842352706213844"></a><a name="b842352706213844"></a>v1</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section32368095"></a>

-   Example Request

    ```
    GET /v2.0/vpn/ikepolicies
    ```


-   Example Response

    ```
    {
      "ikepolicies" : [ {
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
      } ]
    }
    ```


## Returned Values<a name="section6578292"></a>

For details, see section  [Common Returned Values](common-returned-values.md).

