# Adding a Web Tamper Protection Rule<a name="EN-US_TOPIC_0193631172"></a>

## Function Description<a name="section54735234"></a>

This API is used to add a web tamper protection rule.

## URI<a name="section22855062"></a>

-   URI format

    POST  /v1/\{project\_id\}/waf/policy/\{policy\_id\}/antitamper

-   Parameter description

    **Table  1**  Path parameters

    <a name="table37563472"></a>
    <table><thead align="left"><tr id="row739175"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p59873195"><a name="p59873195"></a><a name="p59873195"></a><strong id="b11541183134310"><a name="b11541183134310"></a><a name="b11541183134310"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.2"><p id="p17890620"><a name="p17890620"></a><a name="p17890620"></a><strong id="b320693334313"><a name="b320693334313"></a><a name="b320693334313"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.3"><p id="p39854081"><a name="p39854081"></a><a name="p39854081"></a><strong id="b783823474313"><a name="b783823474313"></a><a name="b783823474313"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.5.1.4"><p id="p6955106"><a name="p6955106"></a><a name="p6955106"></a><strong id="b139843369430"><a name="b139843369430"></a><a name="b139843369430"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row26492745"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p65537563"><a name="p65537563"></a><a name="p65537563"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p6942402"><a name="p6942402"></a><a name="p6942402"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p25463718"><a name="p25463718"></a><a name="p25463718"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p49295278"><a name="p49295278"></a><a name="p49295278"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row41004323"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p33015901"><a name="p33015901"></a><a name="p33015901"></a>policy_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p57042352"><a name="p57042352"></a><a name="p57042352"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p57027779"><a name="p57027779"></a><a name="p57027779"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p55847358"><a name="p55847358"></a><a name="p55847358"></a>Specifies the policy ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section4368973"></a>

Request parameters

**Table  2**  Parameter description

<a name="table121998"></a>
<table><thead align="left"><tr id="row5199287"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p18489121"><a name="p18489121"></a><a name="p18489121"></a><strong id="b183281556164312"><a name="b183281556164312"></a><a name="b183281556164312"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.2"><p id="p21223823"><a name="p21223823"></a><a name="p21223823"></a><strong id="b195810586436"><a name="b195810586436"></a><a name="b195810586436"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.3"><p id="p41408106"><a name="p41408106"></a><a name="p41408106"></a><strong id="b9414615441"><a name="b9414615441"></a><a name="b9414615441"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.5.1.4"><p id="p65722265"><a name="p65722265"></a><a name="p65722265"></a><strong id="b38981625445"><a name="b38981625445"></a><a name="b38981625445"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row21903237"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p29331733"><a name="p29331733"></a><a name="p29331733"></a>hostname</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p27060145"><a name="p27060145"></a><a name="p27060145"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p44388162"><a name="p44388162"></a><a name="p44388162"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p38671408"><a name="p38671408"></a><a name="p38671408"></a>Specifies the domain name.</p>
</td>
</tr>
<tr id="row12498357"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p5734009"><a name="p5734009"></a><a name="p5734009"></a>path</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p61801548"><a name="p61801548"></a><a name="p61801548"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p39869529"><a name="p39869529"></a><a name="p39869529"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p8206406"><a name="p8206406"></a><a name="p8206406"></a>Specifies the URL protected by the web tamper protection rule, excluding a domain name.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section39320758"></a>

Response parameters

**Table  3**  Parameter description

<a name="table49584952"></a>
<table><thead align="left"><tr id="row40541947"><th class="cellrowborder" valign="top" width="31.736826317368262%" id="mcps1.2.4.1.1"><p id="p62672288"><a name="p62672288"></a><a name="p62672288"></a><strong id="b961314219458"><a name="b961314219458"></a><a name="b961314219458"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="28.467153284671525%" id="mcps1.2.4.1.2"><p id="p43290553"><a name="p43290553"></a><a name="p43290553"></a><strong id="b8801204434515"><a name="b8801204434515"></a><a name="b8801204434515"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.4.1.3"><p id="p16873903"><a name="p16873903"></a><a name="p16873903"></a><strong id="b16987046204514"><a name="b16987046204514"></a><a name="b16987046204514"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row17647400"><td class="cellrowborder" valign="top" width="31.736826317368262%" headers="mcps1.2.4.1.1 "><p id="p20153267"><a name="p20153267"></a><a name="p20153267"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="28.467153284671525%" headers="mcps1.2.4.1.2 "><p id="p21801935"><a name="p21801935"></a><a name="p21801935"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p21126307"><a name="p21126307"></a><a name="p21126307"></a>Specifies the ID of a web tamper protection rule.</p>
</td>
</tr>
<tr id="row55919042"><td class="cellrowborder" valign="top" width="31.736826317368262%" headers="mcps1.2.4.1.1 "><p id="p33148574"><a name="p33148574"></a><a name="p33148574"></a>policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="28.467153284671525%" headers="mcps1.2.4.1.2 "><p id="p680007"><a name="p680007"></a><a name="p680007"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p55080612"><a name="p55080612"></a><a name="p55080612"></a>Specifies the policy ID.</p>
</td>
</tr>
<tr id="row25963466"><td class="cellrowborder" valign="top" width="31.736826317368262%" headers="mcps1.2.4.1.1 "><p id="p22666001"><a name="p22666001"></a><a name="p22666001"></a>hostname</p>
</td>
<td class="cellrowborder" valign="top" width="28.467153284671525%" headers="mcps1.2.4.1.2 "><p id="p24006784"><a name="p24006784"></a><a name="p24006784"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p65501376"><a name="p65501376"></a><a name="p65501376"></a>Specifies the domain name.</p>
</td>
</tr>
<tr id="row52641478"><td class="cellrowborder" valign="top" width="31.736826317368262%" headers="mcps1.2.4.1.1 "><p id="p36101314"><a name="p36101314"></a><a name="p36101314"></a>path</p>
</td>
<td class="cellrowborder" valign="top" width="28.467153284671525%" headers="mcps1.2.4.1.2 "><p id="p38525282"><a name="p38525282"></a><a name="p38525282"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p33540110"><a name="p33540110"></a><a name="p33540110"></a>Specifies the URL protected by the web tamper protection rule, excluding a domain name.</p>
</td>
</tr>
<tr id="row33425541"><td class="cellrowborder" valign="top" width="31.736826317368262%" headers="mcps1.2.4.1.1 "><p id="p23114287"><a name="p23114287"></a><a name="p23114287"></a>timestamp</p>
</td>
<td class="cellrowborder" valign="top" width="28.467153284671525%" headers="mcps1.2.4.1.2 "><p id="p60317978"><a name="p60317978"></a><a name="p60317978"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p12128762"><a name="p12128762"></a><a name="p12128762"></a>Specifies the time when the cache is refreshed.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="section11924143811316"></a>

Domain name  **www.abc.com**  is used as an example.

-   Request example

    ```
    {
      "hostname": "www.abc.com",
      "path": "/a"
    }
    ```


-   Response example

    ```
    {
          "id": "3a9b5c0f96784ec8abd8ba61a98064ef",
          "policyid": "yuc0e55865544d1f8c95cf71df108c6b",
          "hostname": "www.abc.com",
          "path": "/a",
          "timestamp": 1499817600
    }
    ```


## Status Code<a name="section18342508"></a>

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

