# Updating a Data Masking Rule<a name="EN-US_TOPIC_0193631156"></a>

## Function Description<a name="section10612703"></a>

This API is used to update a data masking rule.

## URI<a name="section28405467"></a>

-   URI format

    PUT  /v1/\{project\_id\}/waf/policy/\{policy\_id\}/privacy/\{privacy\_rule\_id\}

-   Parameter description

    **Table  1**  Path parameters

    <a name="table37956514"></a>
    <table><thead align="left"><tr id="row55465642"><th class="cellrowborder" valign="top" width="30.930000000000003%" id="mcps1.2.5.1.1"><p id="p63532017"><a name="p63532017"></a><a name="p63532017"></a><strong id="b5946135333816"><a name="b5946135333816"></a><a name="b5946135333816"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.62%" id="mcps1.2.5.1.2"><p id="p45819744"><a name="p45819744"></a><a name="p45819744"></a><strong id="b12608756193818"><a name="b12608756193818"></a><a name="b12608756193818"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.430000000000001%" id="mcps1.2.5.1.3"><p id="p20411808"><a name="p20411808"></a><a name="p20411808"></a><strong id="b0668205873812"><a name="b0668205873812"></a><a name="b0668205873812"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="34.02%" id="mcps1.2.5.1.4"><p id="p42743769"><a name="p42743769"></a><a name="p42743769"></a><strong id="b31453083911"><a name="b31453083911"></a><a name="b31453083911"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row39693234"><td class="cellrowborder" valign="top" width="30.930000000000003%" headers="mcps1.2.5.1.1 "><p id="p61035347"><a name="p61035347"></a><a name="p61035347"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.5.1.2 "><p id="p44916069"><a name="p44916069"></a><a name="p44916069"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.430000000000001%" headers="mcps1.2.5.1.3 "><p id="p14322959"><a name="p14322959"></a><a name="p14322959"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.5.1.4 "><p id="p19309050"><a name="p19309050"></a><a name="p19309050"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row39563727"><td class="cellrowborder" valign="top" width="30.930000000000003%" headers="mcps1.2.5.1.1 "><p id="p50545342"><a name="p50545342"></a><a name="p50545342"></a>policy_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.5.1.2 "><p id="p532033"><a name="p532033"></a><a name="p532033"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.430000000000001%" headers="mcps1.2.5.1.3 "><p id="p43094721"><a name="p43094721"></a><a name="p43094721"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.5.1.4 "><p id="p1011493"><a name="p1011493"></a><a name="p1011493"></a>Specifies the policy ID.</p>
    </td>
    </tr>
    <tr id="row9103440"><td class="cellrowborder" valign="top" width="30.930000000000003%" headers="mcps1.2.5.1.1 "><p id="p66290054"><a name="p66290054"></a><a name="p66290054"></a>privacy_rule_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.5.1.2 "><p id="p785300"><a name="p785300"></a><a name="p785300"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.430000000000001%" headers="mcps1.2.5.1.3 "><p id="p63609379"><a name="p63609379"></a><a name="p63609379"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.5.1.4 "><p id="p52086107"><a name="p52086107"></a><a name="p52086107"></a>Specifies the ID of a data masking rule.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section54322616"></a>

Request parameters

**Table  2**  Parameter description

<a name="table18614499"></a>
<table><thead align="left"><tr id="row50029062"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p25822220"><a name="p25822220"></a><a name="p25822220"></a><strong id="b15545152714390"><a name="b15545152714390"></a><a name="b15545152714390"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.2"><p id="p11225046"><a name="p11225046"></a><a name="p11225046"></a><strong id="b1588832571516"><a name="b1588832571516"></a><a name="b1588832571516"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.3"><p id="p36813516"><a name="p36813516"></a><a name="p36813516"></a><strong id="b4719192712158"><a name="b4719192712158"></a><a name="b4719192712158"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.5.1.4"><p id="p29104856"><a name="p29104856"></a><a name="p29104856"></a><strong id="b154353301150"><a name="b154353301150"></a><a name="b154353301150"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row8683103"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p32242763"><a name="p32242763"></a><a name="p32242763"></a>path</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p61527044"><a name="p61527044"></a><a name="p61527044"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p17634673"><a name="p17634673"></a><a name="p17634673"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p19122427"><a name="p19122427"></a><a name="p19122427"></a>Specifies the URL to which the data masking rule applies (exact match by default).</p>
</td>
</tr>
<tr id="row37884118"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p48714709"><a name="p48714709"></a><a name="p48714709"></a>category</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p53577381"><a name="p53577381"></a><a name="p53577381"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p44800622"><a name="p44800622"></a><a name="p44800622"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p4971735"><a name="p4971735"></a><a name="p4971735"></a>Specifies the masked field. The options are <strong id="b68951722143310"><a name="b68951722143310"></a><a name="b68951722143310"></a>params</strong> and <strong id="b1895152253316"><a name="b1895152253316"></a><a name="b1895152253316"></a>header</strong>.</p>
</td>
</tr>
<tr id="row44745615"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p516171"><a name="p516171"></a><a name="p516171"></a>index</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p41809916"><a name="p41809916"></a><a name="p41809916"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p31160074"><a name="p31160074"></a><a name="p31160074"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p40938076"><a name="p40938076"></a><a name="p40938076"></a>Specifies the masked subfield.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section19141504"></a>

Response parameters

**Table  3**  Parameter description

<a name="table47930937"></a>
<table><thead align="left"><tr id="row21156649"><th class="cellrowborder" valign="top" width="42.85571442855714%" id="mcps1.2.4.1.1"><p id="p35967037"><a name="p35967037"></a><a name="p35967037"></a><strong id="b812014281161"><a name="b812014281161"></a><a name="b812014281161"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.4.1.2"><p id="p27648885"><a name="p27648885"></a><a name="p27648885"></a><strong id="b143131830131615"><a name="b143131830131615"></a><a name="b143131830131615"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.4.1.3"><p id="p24967226"><a name="p24967226"></a><a name="p24967226"></a><strong id="b199413241614"><a name="b199413241614"></a><a name="b199413241614"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row23378444"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p14605839"><a name="p14605839"></a><a name="p14605839"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p42222290"><a name="p42222290"></a><a name="p42222290"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p64562301"><a name="p64562301"></a><a name="p64562301"></a>Specifies the ID of a data masking rule.</p>
</td>
</tr>
<tr id="row44189801"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p22604165"><a name="p22604165"></a><a name="p22604165"></a>policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p18998044"><a name="p18998044"></a><a name="p18998044"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p62446616"><a name="p62446616"></a><a name="p62446616"></a>Specifies the policy ID.</p>
</td>
</tr>
<tr id="row25148640"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p23773934"><a name="p23773934"></a><a name="p23773934"></a>path</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p46640468"><a name="p46640468"></a><a name="p46640468"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p19781563"><a name="p19781563"></a><a name="p19781563"></a>Specifies the URL to which the data masking rule applies (exact match by default).</p>
</td>
</tr>
<tr id="row43816342"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p59462817"><a name="p59462817"></a><a name="p59462817"></a>category</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p51758848"><a name="p51758848"></a><a name="p51758848"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p31717148"><a name="p31717148"></a><a name="p31717148"></a>Specifies the masked field. The options are <strong id="b1423102983312"><a name="b1423102983312"></a><a name="b1423102983312"></a>params</strong> and <strong id="b1923192916332"><a name="b1923192916332"></a><a name="b1923192916332"></a>header</strong>.</p>
</td>
</tr>
<tr id="row17018876"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p36351677"><a name="p36351677"></a><a name="p36351677"></a>index</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p58804719"><a name="p58804719"></a><a name="p58804719"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p65561785"><a name="p65561785"></a><a name="p65561785"></a>Specifies the masked subfield.</p>
</td>
</tr>
<tr id="row53185159"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p13030633"><a name="p13030633"></a><a name="p13030633"></a>timestamp</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p48848376"><a name="p48848376"></a><a name="p48848376"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p14882165719150"><a name="p14882165719150"></a><a name="p14882165719150"></a>Specifies the time when a data masking rule is added.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="section117113318216"></a>

-   Request example

    ```
    {
      "path": "/login",
      "category": "params",
      "index": "password"
    }
    ```


-   Response example

    ```
    {
      "id": "e1c0e55865544d1f8c95cf71df108c6b",
      "policy_id": "yuc0e55865544d1f8c95cf71df108c6b",
      "path": "/login",
      "category": "params",
      "index": "password",
      "timestamp": 123434534543
    }
    ```


## Status Code<a name="section38055810"></a>

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

