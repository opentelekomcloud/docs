# Adding a Data Masking Rule<a name="EN-US_TOPIC_0193631169"></a>

## Function Description<a name="section59927491"></a>

This API is used to add a data masking rule.

## URI<a name="section2476512"></a>

-   URI format

    POST  /v1/\{project\_id\}/waf/policy/\{policy\_id\}/privacy

-   Parameter description

    **Table  1**  Path parameters

    <a name="table6459064"></a>
    <table><thead align="left"><tr id="row4905225"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p61778911"><a name="p61778911"></a><a name="p61778911"></a><strong id="b3820456104216"><a name="b3820456104216"></a><a name="b3820456104216"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.2"><p id="p38035894"><a name="p38035894"></a><a name="p38035894"></a><strong id="b1123845811426"><a name="b1123845811426"></a><a name="b1123845811426"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.3"><p id="p61008565"><a name="p61008565"></a><a name="p61008565"></a><strong id="b5623165934211"><a name="b5623165934211"></a><a name="b5623165934211"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.5.1.4"><p id="p42746757"><a name="p42746757"></a><a name="p42746757"></a><strong id="b910316124312"><a name="b910316124312"></a><a name="b910316124312"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row39935310"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p13534647"><a name="p13534647"></a><a name="p13534647"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p22564584"><a name="p22564584"></a><a name="p22564584"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p15792010"><a name="p15792010"></a><a name="p15792010"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p4084420"><a name="p4084420"></a><a name="p4084420"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row36759786"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p24752700"><a name="p24752700"></a><a name="p24752700"></a>policy_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p58811707"><a name="p58811707"></a><a name="p58811707"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p66127822"><a name="p66127822"></a><a name="p66127822"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p54753374"><a name="p54753374"></a><a name="p54753374"></a>Specifies the policy ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section22288612"></a>

Request parameters

**Table  2**  Parameter description

<a name="table3139475"></a>
<table><thead align="left"><tr id="row936368"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p8736968"><a name="p8736968"></a><a name="p8736968"></a><strong id="b3900161615438"><a name="b3900161615438"></a><a name="b3900161615438"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.2"><p id="p36605784"><a name="p36605784"></a><a name="p36605784"></a><strong id="b519819187438"><a name="b519819187438"></a><a name="b519819187438"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.3"><p id="p12278537"><a name="p12278537"></a><a name="p12278537"></a><strong id="b572132054311"><a name="b572132054311"></a><a name="b572132054311"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.5.1.4"><p id="p55037442"><a name="p55037442"></a><a name="p55037442"></a><strong id="b6223023104316"><a name="b6223023104316"></a><a name="b6223023104316"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row28847852"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p54974703"><a name="p54974703"></a><a name="p54974703"></a>path</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p23765938"><a name="p23765938"></a><a name="p23765938"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p45992797"><a name="p45992797"></a><a name="p45992797"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p34429081"><a name="p34429081"></a><a name="p34429081"></a>Specifies the URL to which the data masking rule applies (exact match by default).</p>
</td>
</tr>
<tr id="row41426277"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p85244"><a name="p85244"></a><a name="p85244"></a>category</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p6904824"><a name="p6904824"></a><a name="p6904824"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p22419905"><a name="p22419905"></a><a name="p22419905"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p4073022"><a name="p4073022"></a><a name="p4073022"></a>Specifies the masked field. The options are <strong id="b178611332123212"><a name="b178611332123212"></a><a name="b178611332123212"></a>params</strong> and <strong id="b17861173215329"><a name="b17861173215329"></a><a name="b17861173215329"></a>header</strong>.</p>
</td>
</tr>
<tr id="row36657204"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p16443547"><a name="p16443547"></a><a name="p16443547"></a>index</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p56858922"><a name="p56858922"></a><a name="p56858922"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p42169994"><a name="p42169994"></a><a name="p42169994"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p60326371"><a name="p60326371"></a><a name="p60326371"></a>Specifies the masked subfield.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section66379784"></a>

Response parameters

**Table  3**  Parameter description

<a name="table13671625"></a>
<table><thead align="left"><tr id="row54208027"><th class="cellrowborder" valign="top" width="30.386961303869608%" id="mcps1.2.4.1.1"><p id="p28774047"><a name="p28774047"></a><a name="p28774047"></a><strong id="b07451564451"><a name="b07451564451"></a><a name="b07451564451"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="29.81701829817018%" id="mcps1.2.4.1.2"><p id="p48996464"><a name="p48996464"></a><a name="p48996464"></a><strong id="b7487688457"><a name="b7487688457"></a><a name="b7487688457"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.4.1.3"><p id="p9290613"><a name="p9290613"></a><a name="p9290613"></a><strong id="b157377911456"><a name="b157377911456"></a><a name="b157377911456"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row16506654"><td class="cellrowborder" valign="top" width="30.386961303869608%" headers="mcps1.2.4.1.1 "><p id="p61970637"><a name="p61970637"></a><a name="p61970637"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="29.81701829817018%" headers="mcps1.2.4.1.2 "><p id="p53565733"><a name="p53565733"></a><a name="p53565733"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p43857101"><a name="p43857101"></a><a name="p43857101"></a>Specifies the ID of a data masking rule.</p>
</td>
</tr>
<tr id="row59169590"><td class="cellrowborder" valign="top" width="30.386961303869608%" headers="mcps1.2.4.1.1 "><p id="p28007514"><a name="p28007514"></a><a name="p28007514"></a>policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="29.81701829817018%" headers="mcps1.2.4.1.2 "><p id="p54016162"><a name="p54016162"></a><a name="p54016162"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p13233015"><a name="p13233015"></a><a name="p13233015"></a>Specifies the policy ID.</p>
</td>
</tr>
<tr id="row51988273"><td class="cellrowborder" valign="top" width="30.386961303869608%" headers="mcps1.2.4.1.1 "><p id="p50300612"><a name="p50300612"></a><a name="p50300612"></a>path</p>
</td>
<td class="cellrowborder" valign="top" width="29.81701829817018%" headers="mcps1.2.4.1.2 "><p id="p47817751"><a name="p47817751"></a><a name="p47817751"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p48032594"><a name="p48032594"></a><a name="p48032594"></a>Specifies the URL to which the data masking rule applies (exact match by default).</p>
</td>
</tr>
<tr id="row29640166"><td class="cellrowborder" valign="top" width="30.386961303869608%" headers="mcps1.2.4.1.1 "><p id="p52043282"><a name="p52043282"></a><a name="p52043282"></a>category</p>
</td>
<td class="cellrowborder" valign="top" width="29.81701829817018%" headers="mcps1.2.4.1.2 "><p id="p54756281"><a name="p54756281"></a><a name="p54756281"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p6073797"><a name="p6073797"></a><a name="p6073797"></a>Specifies the masked field. The options are <strong id="b10165124613211"><a name="b10165124613211"></a><a name="b10165124613211"></a>params</strong> and <strong id="b7165154693217"><a name="b7165154693217"></a><a name="b7165154693217"></a>header</strong>.</p>
</td>
</tr>
<tr id="row54664181"><td class="cellrowborder" valign="top" width="30.386961303869608%" headers="mcps1.2.4.1.1 "><p id="p65722515"><a name="p65722515"></a><a name="p65722515"></a>index</p>
</td>
<td class="cellrowborder" valign="top" width="29.81701829817018%" headers="mcps1.2.4.1.2 "><p id="p21923465"><a name="p21923465"></a><a name="p21923465"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p30970240"><a name="p30970240"></a><a name="p30970240"></a>Specifies the masked subfield.</p>
</td>
</tr>
<tr id="row10296707"><td class="cellrowborder" valign="top" width="30.386961303869608%" headers="mcps1.2.4.1.1 "><p id="p28726942"><a name="p28726942"></a><a name="p28726942"></a>timestamp</p>
</td>
<td class="cellrowborder" valign="top" width="29.81701829817018%" headers="mcps1.2.4.1.2 "><p id="p45180941"><a name="p45180941"></a><a name="p45180941"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p12128762"><a name="p12128762"></a><a name="p12128762"></a>Specifies the time when a data masking rule is added.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="section140302775820"></a>

-   Request example

    ```
    {
      "path": "/login",
      "category": "params",
      "index": "name"
    }
    ```


-   Response example

    ```
    {
          "id": "e1c0e55865544d1f8c95cf71df108c6b",
          "policy_id": "yuc0e55865544d1f8c95cf71df108c6b",
          "path": "/login",
          "category":"params",
          "index": "name",
          "timestamp": 123243414132
    }
    ```


## Status Code<a name="section60547149"></a>

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

