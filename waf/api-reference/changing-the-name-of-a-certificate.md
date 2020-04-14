# Changing the Name of a Certificate<a name="EN-US_TOPIC_0193631186"></a>

## Function Description<a name="section5909008"></a>

This API is used to change the name of a certificate.

## URI<a name="section53181073"></a>

-   URI format

    PUT  /v1/\{project\_id\}/waf/certificate/\{certificate\_id\}

-   Parameter description

    **Table  1**  Path parameters

    <a name="table6333726152318"></a>
    <table><thead align="left"><tr id="row16331202682317"><th class="cellrowborder" valign="top" width="19.538046195380463%" id="mcps1.2.5.1.1"><p id="p73311326162320"><a name="p73311326162320"></a><a name="p73311326162320"></a><strong id="b227061152517"><a name="b227061152517"></a><a name="b227061152517"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23.31766823317668%" id="mcps1.2.5.1.2"><p id="p1333162616234"><a name="p1333162616234"></a><a name="p1333162616234"></a><strong id="b1977525605112"><a name="b1977525605112"></a><a name="b1977525605112"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.3"><p id="p18331102622313"><a name="p18331102622313"></a><a name="p18331102622313"></a><strong id="b101611134259"><a name="b101611134259"></a><a name="b101611134259"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.5.1.4"><p id="p1133116269234"><a name="p1133116269234"></a><a name="p1133116269234"></a><strong id="b7146161414255"><a name="b7146161414255"></a><a name="b7146161414255"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row173335264239"><td class="cellrowborder" valign="top" width="19.538046195380463%" headers="mcps1.2.5.1.1 "><p id="p13311626142316"><a name="p13311626142316"></a><a name="p13311626142316"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.31766823317668%" headers="mcps1.2.5.1.2 "><p id="p1033312692319"><a name="p1033312692319"></a><a name="p1033312692319"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p933392672311"><a name="p933392672311"></a><a name="p933392672311"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p73336265234"><a name="p73336265234"></a><a name="p73336265234"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row24271533411"><td class="cellrowborder" valign="top" width="19.538046195380463%" headers="mcps1.2.5.1.1 "><p id="p14381533410"><a name="p14381533410"></a><a name="p14381533410"></a>certificate_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.31766823317668%" headers="mcps1.2.5.1.2 "><p id="p94315154342"><a name="p94315154342"></a><a name="p94315154342"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p1844191515349"><a name="p1844191515349"></a><a name="p1844191515349"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p3441915153410"><a name="p3441915153410"></a><a name="p3441915153410"></a>Specifies the certificate ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section8867609"></a>

Request parameters

**Table  2**  Parameter description

<a name="table848611508595"></a>
<table><thead align="left"><tr id="row848645016598"><th class="cellrowborder" valign="top" width="20.580000000000002%" id="mcps1.2.5.1.1"><p id="p14736601303"><a name="p14736601303"></a><a name="p14736601303"></a><strong id="b105911739192512"><a name="b105911739192512"></a><a name="b105911739192512"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.2%" id="mcps1.2.5.1.2"><p id="p1738801502"><a name="p1738801502"></a><a name="p1738801502"></a><strong id="b1977525605112_1"><a name="b1977525605112_1"></a><a name="b1977525605112_1"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.06%" id="mcps1.2.5.1.3"><p id="p197387015014"><a name="p197387015014"></a><a name="p197387015014"></a><strong id="b101611134259_1"><a name="b101611134259_1"></a><a name="b101611134259_1"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="48.16%" id="mcps1.2.5.1.4"><p id="p16740904018"><a name="p16740904018"></a><a name="p16740904018"></a><strong id="b344374752518"><a name="b344374752518"></a><a name="b344374752518"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row048655010593"><td class="cellrowborder" valign="top" width="20.580000000000002%" headers="mcps1.2.5.1.1 "><p id="p12742601105"><a name="p12742601105"></a><a name="p12742601105"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="15.2%" headers="mcps1.2.5.1.2 "><p id="p5745110902"><a name="p5745110902"></a><a name="p5745110902"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.06%" headers="mcps1.2.5.1.3 "><p id="p6746140305"><a name="p6746140305"></a><a name="p6746140305"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.16%" headers="mcps1.2.5.1.4 "><p id="p4746801001"><a name="p4746801001"></a><a name="p4746801001"></a>Specifies the certificate name. The maximum length is 256 characters. Only digits, letters, underscores (_), and hyphens (-) are allowed.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section12699617"></a>

Response parameters

**Table  3**  Parameter description

<a name="table58327572"></a>
<table><thead align="left"><tr id="row12075850"><th class="cellrowborder" valign="top" width="20.810000000000002%" id="mcps1.2.4.1.1"><p id="p38619773"><a name="p38619773"></a><a name="p38619773"></a><strong id="b188104599258"><a name="b188104599258"></a><a name="b188104599258"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="21.58%" id="mcps1.2.4.1.2"><p id="p41193880"><a name="p41193880"></a><a name="p41193880"></a><strong id="b1967715082616"><a name="b1967715082616"></a><a name="b1967715082616"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="57.60999999999999%" id="mcps1.2.4.1.3"><p id="p48369988"><a name="p48369988"></a><a name="p48369988"></a><strong id="b96698111268"><a name="b96698111268"></a><a name="b96698111268"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row32676712"><td class="cellrowborder" valign="top" width="20.810000000000002%" headers="mcps1.2.4.1.1 "><p id="p29567983"><a name="p29567983"></a><a name="p29567983"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="21.58%" headers="mcps1.2.4.1.2 "><p id="p46196443"><a name="p46196443"></a><a name="p46196443"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.60999999999999%" headers="mcps1.2.4.1.3 "><p id="p50924436"><a name="p50924436"></a><a name="p50924436"></a>Specifies the certificate ID.</p>
</td>
</tr>
<tr id="row55666745"><td class="cellrowborder" valign="top" width="20.810000000000002%" headers="mcps1.2.4.1.1 "><p id="p12712463"><a name="p12712463"></a><a name="p12712463"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="21.58%" headers="mcps1.2.4.1.2 "><p id="p23076582"><a name="p23076582"></a><a name="p23076582"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.60999999999999%" headers="mcps1.2.4.1.3 "><p id="p57263845"><a name="p57263845"></a><a name="p57263845"></a>Specifies the certificate name.</p>
</td>
</tr>
<tr id="row944795925117"><td class="cellrowborder" valign="top" width="20.810000000000002%" headers="mcps1.2.4.1.1 "><p id="p466545510448"><a name="p466545510448"></a><a name="p466545510448"></a>expireTime</p>
</td>
<td class="cellrowborder" valign="top" width="21.58%" headers="mcps1.2.4.1.2 "><p id="p11665125516444"><a name="p11665125516444"></a><a name="p11665125516444"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="57.60999999999999%" headers="mcps1.2.4.1.3 "><p id="p17665655174419"><a name="p17665655174419"></a><a name="p17665655174419"></a>Specifies the time when the certificate expires.</p>
</td>
</tr>
<tr id="row3173155443810"><td class="cellrowborder" valign="top" width="20.810000000000002%" headers="mcps1.2.4.1.1 "><p id="p017335443813"><a name="p017335443813"></a><a name="p017335443813"></a>timestamp</p>
</td>
<td class="cellrowborder" valign="top" width="21.58%" headers="mcps1.2.4.1.2 "><p id="p1917365413819"><a name="p1917365413819"></a><a name="p1917365413819"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="57.60999999999999%" headers="mcps1.2.4.1.3 "><p id="p1117335413388"><a name="p1117335413388"></a><a name="p1117335413388"></a>Specifies the time when the certificate is uploaded.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="section15246722163414"></a>

A certificate named  **cert\_a**  is used as an example.

-   Request example

    ```
    {
     "name": "cert_b"
    }
    ```


-   Response example

    ```
    {
        "id": "388a7789d55b41d1918b3088a8f1e7f3",
        "name": "cert_b",
        "expireTime": 1565467166765,
        "timestamp": 1545467166765
    }
    ```


## Status Code<a name="section47187690"></a>

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

