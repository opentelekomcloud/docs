# Switching the WAF Mode<a name="EN-US_TOPIC_0193631127"></a>

## Function Description<a name="section15884400"></a>

This API is used to switch the WAF mode.

## URI<a name="section8741878"></a>

-   URI format

    PUT  /v1/\{project\_id\}/waf/instance/\{instance\_id\}/protect\_status

-   Parameter description

    **Table  1**  Path parameters

    <a name="table3754283"></a>
    <table><thead align="left"><tr id="row34655318"><th class="cellrowborder" valign="top" width="19.388061193880613%" id="mcps1.2.5.1.1"><p id="p55617407"><a name="p55617407"></a><a name="p55617407"></a><strong id="b4639155012380"><a name="b4639155012380"></a><a name="b4639155012380"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p8716124"><a name="p8716124"></a><a name="p8716124"></a><strong id="b10436151183817"><a name="b10436151183817"></a><a name="b10436151183817"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p34917462"><a name="p34917462"></a><a name="p34917462"></a><strong id="b182942525382"><a name="b182942525382"></a><a name="b182942525382"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="52.03479652034796%" id="mcps1.2.5.1.4"><p id="p9742164"><a name="p9742164"></a><a name="p9742164"></a><strong id="b10139195310381"><a name="b10139195310381"></a><a name="b10139195310381"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row50917823"><td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.2.5.1.1 "><p id="p30702974"><a name="p30702974"></a><a name="p30702974"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p3912954"><a name="p3912954"></a><a name="p3912954"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p48513818"><a name="p48513818"></a><a name="p48513818"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.03479652034796%" headers="mcps1.2.5.1.4 "><p id="p37305158"><a name="p37305158"></a><a name="p37305158"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row202109"><td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.2.5.1.1 "><p id="p16370855"><a name="p16370855"></a><a name="p16370855"></a>instance_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p50970898"><a name="p50970898"></a><a name="p50970898"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p35002086"><a name="p35002086"></a><a name="p35002086"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.03479652034796%" headers="mcps1.2.5.1.4 "><p id="p16596681"><a name="p16596681"></a><a name="p16596681"></a>Specifies the instance ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section11568039"></a>

Request parameters

**Table  2**  Parameter description

<a name="table19385625"></a>
<table><thead align="left"><tr id="row16897836"><th class="cellrowborder" valign="top" width="19.388061193880613%" id="mcps1.2.5.1.1"><p id="p26547515"><a name="p26547515"></a><a name="p26547515"></a><strong id="b1295251111392"><a name="b1295251111392"></a><a name="b1295251111392"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p2865139"><a name="p2865139"></a><a name="p2865139"></a><strong id="b1670212129396"><a name="b1670212129396"></a><a name="b1670212129396"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p30749691"><a name="p30749691"></a><a name="p30749691"></a><strong id="b35613163396"><a name="b35613163396"></a><a name="b35613163396"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="52.03479652034796%" id="mcps1.2.5.1.4"><p id="p7697019"><a name="p7697019"></a><a name="p7697019"></a><strong id="b1256021712399"><a name="b1256021712399"></a><a name="b1256021712399"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row19478812"><td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.2.5.1.1 "><p id="p34279941"><a name="p34279941"></a><a name="p34279941"></a>protect_status</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p25211871"><a name="p25211871"></a><a name="p25211871"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p28895698"><a name="p28895698"></a><a name="p28895698"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="52.03479652034796%" headers="mcps1.2.5.1.4 "><p id="p158432573520"><a name="p158432573520"></a><a name="p158432573520"></a>Specifies the WAF mode of a domain name.</p>
<a name="ul484375711526"></a><a name="ul484375711526"></a><ul id="ul484375711526"><li><strong id="b1721153022411"><a name="b1721153022411"></a><a name="b1721153022411"></a>1</strong>: enabled.</li><li><strong id="b10833738192419"><a name="b10833738192419"></a><a name="b10833738192419"></a>0</strong>: disabled.</li><li><strong id="b47318513114"><a name="b47318513114"></a><a name="b47318513114"></a>-1</strong>: bypassed. That is, a client sends a request to the server without passing through WAF.</li></ul>
</td>
</tr>
</tbody>
</table>

## Response<a name="section37003494"></a>

Response parameters

**Table  3**  Parameter description

<a name="table770611248810"></a>
<table><thead align="left"><tr id="row187083241980"><th class="cellrowborder" valign="top" width="19.388061193880613%" id="mcps1.2.5.1.1"><p id="p1170982412812"><a name="p1170982412812"></a><a name="p1170982412812"></a><strong id="b20778821259"><a name="b20778821259"></a><a name="b20778821259"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p117110246819"><a name="p117110246819"></a><a name="p117110246819"></a><strong id="b1644972727"><a name="b1644972727"></a><a name="b1644972727"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p197121324882"><a name="p197121324882"></a><a name="p197121324882"></a><strong id="b534779540"><a name="b534779540"></a><a name="b534779540"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="52.03479652034796%" id="mcps1.2.5.1.4"><p id="p47141224381"><a name="p47141224381"></a><a name="p47141224381"></a><strong id="b1226130538"><a name="b1226130538"></a><a name="b1226130538"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row117157241689"><td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.2.5.1.1 "><p id="p137162024283"><a name="p137162024283"></a><a name="p137162024283"></a>protect_status</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p971718241281"><a name="p971718241281"></a><a name="p971718241281"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p19719192415811"><a name="p19719192415811"></a><a name="p19719192415811"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="52.03479652034796%" headers="mcps1.2.5.1.4 "><p id="p139422072919"><a name="p139422072919"></a><a name="p139422072919"></a>Specifies the WAF mode of a domain name.</p>
<a name="ul63951620192918"></a><a name="ul63951620192918"></a><ul id="ul63951620192918"><li><strong id="b10414165014417"><a name="b10414165014417"></a><a name="b10414165014417"></a>1</strong>: enabled.</li><li><strong id="b1280113241202"><a name="b1280113241202"></a><a name="b1280113241202"></a>0</strong>: disabled.</li><li><strong id="b179187537117"><a name="b179187537117"></a><a name="b179187537117"></a>-1</strong>: bypassed. That is, a client sends a request to the server without passing through WAF.</li></ul>
</td>
</tr>
</tbody>
</table>

## Examples<a name="section1641724123619"></a>

**protect\_status**  with a value of  **1**  is used as an example.

-   Request example

    ```
    {
        "protect_status": 1
    }
    ```


-   Response example

    ```
    {
        "protect_status": 1
    }
    ```


## Status Code<a name="section64595995"></a>

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

