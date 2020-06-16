# Connecting a Domain Name to WAF<a name="EN-US_TOPIC_0193630656"></a>

## Function Description<a name="section61598046"></a>

This API is used to connect a domain name to WAF.

## URI<a name="section17511502"></a>

-   URI format

    PUT  /v1/\{project\_id\}/waf/instance/\{instance\_id\}/access\_status

-   Parameter description

    **Table  1**  Path parameters

    <a name="table61708842"></a>
    <table><thead align="left"><tr id="row52390583"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p15778808"><a name="p15778808"></a><a name="p15778808"></a><strong id="b1217402317425"><a name="b1217402317425"></a><a name="b1217402317425"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.2"><p id="p3015103"><a name="p3015103"></a><a name="p3015103"></a><strong id="b1275217241423"><a name="b1275217241423"></a><a name="b1275217241423"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.3"><p id="p42896753"><a name="p42896753"></a><a name="p42896753"></a><strong id="b6846173104219"><a name="b6846173104219"></a><a name="b6846173104219"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.5.1.4"><p id="p52084984"><a name="p52084984"></a><a name="p52084984"></a><strong id="b16721123210425"><a name="b16721123210425"></a><a name="b16721123210425"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row58134204"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p11250084"><a name="p11250084"></a><a name="p11250084"></a>projecte_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p38841625"><a name="p38841625"></a><a name="p38841625"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p59163906"><a name="p59163906"></a><a name="p59163906"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p27547080"><a name="p27547080"></a><a name="p27547080"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row46597129"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p16271076"><a name="p16271076"></a><a name="p16271076"></a>instance_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p42888784"><a name="p42888784"></a><a name="p42888784"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p51439476"><a name="p51439476"></a><a name="p51439476"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p5848057"><a name="p5848057"></a><a name="p5848057"></a>Specifies the instance ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section23385790"></a>

Request parameters

**Table  2**  Parameter description

<a name="table49945669"></a>
<table><thead align="left"><tr id="row22862784"><th class="cellrowborder" valign="top" width="19.388061193880613%" id="mcps1.2.5.1.1"><p id="p39946191"><a name="p39946191"></a><a name="p39946191"></a><strong id="b12289154717429"><a name="b12289154717429"></a><a name="b12289154717429"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p14416027"><a name="p14416027"></a><a name="p14416027"></a><strong id="b77018480428"><a name="b77018480428"></a><a name="b77018480428"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p26847499"><a name="p26847499"></a><a name="p26847499"></a><strong id="b3884910426"><a name="b3884910426"></a><a name="b3884910426"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="52.03479652034796%" id="mcps1.2.5.1.4"><p id="p27163783"><a name="p27163783"></a><a name="p27163783"></a><strong id="b285216493426"><a name="b285216493426"></a><a name="b285216493426"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row52782840"><td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.2.5.1.1 "><p id="p47551686"><a name="p47551686"></a><a name="p47551686"></a>access_status</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p26481368"><a name="p26481368"></a><a name="p26481368"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p64616087"><a name="p64616087"></a><a name="p64616087"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="52.03479652034796%" headers="mcps1.2.5.1.4 "><p id="p865434175514"><a name="p865434175514"></a><a name="p865434175514"></a>Specifies whether a domain name is connected to WAF.</p>
<p id="p18206134020151"><a name="p18206134020151"></a><a name="p18206134020151"></a><strong id="b11808213272"><a name="b11808213272"></a><a name="b11808213272"></a>1</strong>: The domain name is connected to WAF.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section9145519"></a>

Response parameters

**Table  3**  Parameter description

<a name="table15683171611354"></a>
<table><thead align="left"><tr id="row1068411611352"><th class="cellrowborder" valign="top" width="19.44%" id="mcps1.2.5.1.1"><p id="p5684101653518"><a name="p5684101653518"></a><a name="p5684101653518"></a><strong id="b1221154202710"><a name="b1221154202710"></a><a name="b1221154202710"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.660000000000004%" id="mcps1.2.5.1.2"><p id="p156844167359"><a name="p156844167359"></a><a name="p156844167359"></a><strong id="b142253312"><a name="b142253312"></a><a name="b142253312"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.350000000000001%" id="mcps1.2.5.1.3"><p id="p9684316123513"><a name="p9684316123513"></a><a name="p9684316123513"></a><strong id="b677203796"><a name="b677203796"></a><a name="b677203796"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51.550000000000004%" id="mcps1.2.5.1.4"><p id="p8684116183517"><a name="p8684116183517"></a><a name="p8684116183517"></a><strong id="b804148098"><a name="b804148098"></a><a name="b804148098"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1684101615357"><td class="cellrowborder" valign="top" width="19.44%" headers="mcps1.2.5.1.1 "><p id="p268417167352"><a name="p268417167352"></a><a name="p268417167352"></a>access_status</p>
</td>
<td class="cellrowborder" valign="top" width="14.660000000000004%" headers="mcps1.2.5.1.2 "><p id="p146841416193519"><a name="p146841416193519"></a><a name="p146841416193519"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.350000000000001%" headers="mcps1.2.5.1.3 "><p id="p116842016173519"><a name="p116842016173519"></a><a name="p116842016173519"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="51.550000000000004%" headers="mcps1.2.5.1.4 "><p id="p012517913529"><a name="p012517913529"></a><a name="p012517913529"></a>Specifies whether a domain name is connected to WAF.</p>
<a name="ul1712616919526"></a><a name="ul1712616919526"></a><ul id="ul1712616919526"><li><strong id="b48391127181116"><a name="b48391127181116"></a><a name="b48391127181116"></a>1</strong>: The domain name is connected to WAF.</li><li><strong id="b96294872718"><a name="b96294872718"></a><a name="b96294872718"></a>0</strong>: The domain name is not connected to WAF.</li></ul>
</td>
</tr>
<tr id="row668461614351"><td class="cellrowborder" valign="top" width="19.44%" headers="mcps1.2.5.1.1 "><p id="p3684171616351"><a name="p3684171616351"></a><a name="p3684171616351"></a>protect_status</p>
</td>
<td class="cellrowborder" valign="top" width="14.660000000000004%" headers="mcps1.2.5.1.2 "><p id="p17684016113517"><a name="p17684016113517"></a><a name="p17684016113517"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.350000000000001%" headers="mcps1.2.5.1.3 "><p id="p6684316103513"><a name="p6684316103513"></a><a name="p6684316103513"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="51.550000000000004%" headers="mcps1.2.5.1.4 "><p id="p158432573520"><a name="p158432573520"></a><a name="p158432573520"></a>Specifies the WAF mode of a domain name.</p>
<a name="ul484375711526"></a><a name="ul484375711526"></a><ul id="ul484375711526"><li><strong id="b1477211479513"><a name="b1477211479513"></a><a name="b1477211479513"></a>1</strong>: enabled.</li><li><strong id="b3129155116209"><a name="b3129155116209"></a><a name="b3129155116209"></a>0</strong>: disabled.</li><li><strong id="b1868532511120"><a name="b1868532511120"></a><a name="b1868532511120"></a>-1</strong>: bypassed. That is, a client sends a request to the server without passing through WAF.</li></ul>
</td>
</tr>
</tbody>
</table>

## Examples<a name="section3802184912372"></a>

**access\_status**  with a value of  **1**  is used as an example.

-   Request example

    ```
    {
     "access_status": 1
    }
    ```


-   Response examples

    The following shows the response if the domain name is connected to WAF:

    ```
    {
      "access_status": 1,
      "protect_status": 1
    }
    ```

    The following shows the response if connection fails:

    ```
    {
     "access_status": 0,
     "protect_status": 0
    }
    ```


## Status Code<a name="section15200810"></a>

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

