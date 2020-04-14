# Uploading a Certificate<a name="EN-US_TOPIC_0193631163"></a>

## Function Description<a name="section5909008"></a>

This API is used to upload a certificate.

## URI<a name="section53181073"></a>

-   URI format

    POST  /v1/\{project\_id\}/waf/certificate

-   Parameter description

    **Table  1**  Path parameters

    <a name="table6333726152318"></a>
    <table><thead align="left"><tr id="row16331202682317"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p73311326162320"><a name="p73311326162320"></a><a name="p73311326162320"></a><strong id="b43013176296"><a name="b43013176296"></a><a name="b43013176296"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.2"><p id="p1333162616234"><a name="p1333162616234"></a><a name="p1333162616234"></a><strong id="b18410718172915"><a name="b18410718172915"></a><a name="b18410718172915"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.3"><p id="p18331102622313"><a name="p18331102622313"></a><a name="p18331102622313"></a><strong id="b736311193291"><a name="b736311193291"></a><a name="b736311193291"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.5.1.4"><p id="p1133116269234"><a name="p1133116269234"></a><a name="p1133116269234"></a><strong id="b3941131915297"><a name="b3941131915297"></a><a name="b3941131915297"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row173335264239"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p13311626142316"><a name="p13311626142316"></a><a name="p13311626142316"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p1033312692319"><a name="p1033312692319"></a><a name="p1033312692319"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p933392672311"><a name="p933392672311"></a><a name="p933392672311"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p73336265234"><a name="p73336265234"></a><a name="p73336265234"></a>Specifies the project ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section8867609"></a>

Request parameters

**Table  2**  Parameter description

<a name="table01910549582"></a>
<table><thead align="left"><tr id="row13191654175813"><th class="cellrowborder" valign="top" width="19.88%" id="mcps1.2.5.1.1"><p id="p877688145917"><a name="p877688145917"></a><a name="p877688145917"></a><strong id="b8504827182911"><a name="b8504827182911"></a><a name="b8504827182911"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.91%" id="mcps1.2.5.1.2"><p id="p277717819595"><a name="p277717819595"></a><a name="p277717819595"></a><strong id="b1756341310"><a name="b1756341310"></a><a name="b1756341310"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.63%" id="mcps1.2.5.1.3"><p id="p147799875915"><a name="p147799875915"></a><a name="p147799875915"></a><strong id="b1244670340"><a name="b1244670340"></a><a name="b1244670340"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="48.58%" id="mcps1.2.5.1.4"><p id="p87821486598"><a name="p87821486598"></a><a name="p87821486598"></a><strong id="b18738829172914"><a name="b18738829172914"></a><a name="b18738829172914"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row17191175417588"><td class="cellrowborder" valign="top" width="19.88%" headers="mcps1.2.5.1.1 "><p id="p1478588115915"><a name="p1478588115915"></a><a name="p1478588115915"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16.91%" headers="mcps1.2.5.1.2 "><p id="p1679028155913"><a name="p1679028155913"></a><a name="p1679028155913"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.63%" headers="mcps1.2.5.1.3 "><p id="p167911184598"><a name="p167911184598"></a><a name="p167911184598"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.58%" headers="mcps1.2.5.1.4 "><p id="p157946819593"><a name="p157946819593"></a><a name="p157946819593"></a>Specifies the certificate name. The maximum length is 256 characters. Only digits, letters, underscores (_), and hyphens (-) are allowed.</p>
</td>
</tr>
<tr id="row9191454185813"><td class="cellrowborder" valign="top" width="19.88%" headers="mcps1.2.5.1.1 "><p id="p67968816592"><a name="p67968816592"></a><a name="p67968816592"></a>content</p>
</td>
<td class="cellrowborder" valign="top" width="16.91%" headers="mcps1.2.5.1.2 "><p id="p57981813597"><a name="p57981813597"></a><a name="p57981813597"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.63%" headers="mcps1.2.5.1.3 "><p id="p3800178155915"><a name="p3800178155915"></a><a name="p3800178155915"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.58%" headers="mcps1.2.5.1.4 "><p id="p157351532185415"><a name="p157351532185415"></a><a name="p157351532185415"></a>Specifies the certificate content.</p>
<div class="note" id="note133525375548"><a name="note133525375548"></a><a name="note133525375548"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul642384215411"></a><a name="ul642384215411"></a><ul id="ul642384215411"><li>The following is an example of the obtained certificate content:<pre class="codeblock" id="codeblock15081228181110"><a name="codeblock15081228181110"></a><a name="codeblock15081228181110"></a>-----BEGIN CERTIFICATE-----
MIIDezCCAmOgAwIBAgIJAMJcdOLsrN3iMA0GCSqGSIb3DQEBCwUAMFQxCzAJBgNV
...
8qh1Vpk2FXoadOVze2fQFLBkkB7LPExj8Nrf76CJEA==
-----END CERTIFICATE-----</pre>
</li><li>Line endings are replaced with <strong id="b999516493332"><a name="b999516493332"></a><a name="b999516493332"></a>\n</strong> by default before uploading the certificate content. For example:<p id="p1352649185612"><a name="p1352649185612"></a><a name="p1352649185612"></a>-----BEGIN CERTIFICATE-----<span class="parmvalue" id="parmvalue825731415416"><a name="parmvalue825731415416"></a><a name="parmvalue825731415416"></a><b>\n</b></span>MIIDezCCAmOgAwIBAgIJAMJcdOLsrN3iMA0GCSqGSIb3DQEBCwUAMFQxCzAJBgNV<span class="parmvalue" id="parmvalue8677208416"><a name="parmvalue8677208416"></a><a name="parmvalue8677208416"></a><b>\n</b></span>...<span class="parmvalue" id="parmvalue078752311412"><a name="parmvalue078752311412"></a><a name="parmvalue078752311412"></a><b>\n</b></span>8qh1Vpk2FXoadOVze2fQFLBkkB7LPExj8Nrf76CJEA==<span class="parmvalue" id="parmvalue9427182815410"><a name="parmvalue9427182815410"></a><a name="parmvalue9427182815410"></a><b>\n</b></span>-----END CERTIFICATE-----</p>
</li></ul>
</div></div>
</td>
</tr>
<tr id="row171916540581"><td class="cellrowborder" valign="top" width="19.88%" headers="mcps1.2.5.1.1 "><p id="p180512812596"><a name="p180512812596"></a><a name="p180512812596"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="16.91%" headers="mcps1.2.5.1.2 "><p id="p78057895916"><a name="p78057895916"></a><a name="p78057895916"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.63%" headers="mcps1.2.5.1.3 "><p id="p580798175916"><a name="p580798175916"></a><a name="p580798175916"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.58%" headers="mcps1.2.5.1.4 "><p id="p778819469461"><a name="p778819469461"></a><a name="p778819469461"></a>Specifies the private key.</p>
<div class="note" id="note7377951114614"><a name="note7377951114614"></a><a name="note7377951114614"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul640212312508"></a><a name="ul640212312508"></a><ul id="ul640212312508"><li>The following is an example of the obtained private key:<pre class="codeblock" id="codeblock4689442101114"><a name="codeblock4689442101114"></a><a name="codeblock4689442101114"></a>-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAsj2QPAwXYcPDH0mvf6Jbej6RGgYlb4EFMS85BjKrKNPOTqZf
...
4j0RY9DeUgSLdy625BBmew2it9l/NynIScG4Ow6w8Bu4iBANGv94
-----END RSA PRIVATE KEY-----</pre>
</li><li>Line endings are replaced with <strong id="b1843619229371"><a name="b1843619229371"></a><a name="b1843619229371"></a>\n</strong> by default before uploading the private key. For example:<p id="p55316421506"><a name="p55316421506"></a><a name="p55316421506"></a>----BEGIN RSA PRIVATE KEY----<span class="parmvalue" id="parmvalue127084374214"><a name="parmvalue127084374214"></a><a name="parmvalue127084374214"></a><b>\n</b></span>MIIEowIBAAKCAQEAsj2QPAwXYcPDH0mvf6Jbej6RGgYlb4EFMS85BjKrKNPOTqZf<span class="parmvalue" id="parmvalue155198451217"><a name="parmvalue155198451217"></a><a name="parmvalue155198451217"></a><b>\n</b></span>...<span class="parmvalue" id="parmvalue142350521923"><a name="parmvalue142350521923"></a><a name="parmvalue142350521923"></a><b>\n</b></span>4j0RY9DeUgSLdy625BBmew2it9l/NynIScG4Ow6w8Bu4iBANGv94<span class="parmvalue" id="parmvalue12921256828"><a name="parmvalue12921256828"></a><a name="parmvalue12921256828"></a><b>\n</b></span>-----END RSA PRIVATE KEY-----</p>
</li></ul>
</div></div>
</td>
</tr>
</tbody>
</table>

## Response<a name="section12699617"></a>

Response parameters

**Table  3**  Parameter description

<a name="table58327572"></a>
<table><thead align="left"><tr id="row12075850"><th class="cellrowborder" valign="top" width="42.85571442855714%" id="mcps1.2.4.1.1"><p id="p38619773"><a name="p38619773"></a><a name="p38619773"></a><strong id="b169731844183116"><a name="b169731844183116"></a><a name="b169731844183116"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.4.1.2"><p id="p41193880"><a name="p41193880"></a><a name="p41193880"></a><strong id="b1167946163113"><a name="b1167946163113"></a><a name="b1167946163113"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.4.1.3"><p id="p48369988"><a name="p48369988"></a><a name="p48369988"></a><strong id="b3818124620312"><a name="b3818124620312"></a><a name="b3818124620312"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row32676712"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p29567983"><a name="p29567983"></a><a name="p29567983"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p46196443"><a name="p46196443"></a><a name="p46196443"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p50924436"><a name="p50924436"></a><a name="p50924436"></a>Specifies the certificate ID.</p>
</td>
</tr>
<tr id="row55666745"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p12712463"><a name="p12712463"></a><a name="p12712463"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p23076582"><a name="p23076582"></a><a name="p23076582"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p57263845"><a name="p57263845"></a><a name="p57263845"></a>Specifies the certificate name.</p>
</td>
</tr>
<tr id="row944795925117"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p466545510448"><a name="p466545510448"></a><a name="p466545510448"></a>expireTime</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p11665125516444"><a name="p11665125516444"></a><a name="p11665125516444"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p17665655174419"><a name="p17665655174419"></a><a name="p17665655174419"></a>Specifies the time when the certificate expires.</p>
</td>
</tr>
<tr id="row64272916384"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p124275910384"><a name="p124275910384"></a><a name="p124275910384"></a>timestamp</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p1342716963812"><a name="p1342716963812"></a><a name="p1342716963812"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p2042739183818"><a name="p2042739183818"></a><a name="p2042739183818"></a>Specifies the time when the certificate is uploaded.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="section15246722163414"></a>

A certificate named  **cert\_a**  is used as an example.

-   Request example

    ```
    {
     "name": "cert_a",
     "content": "-----BEGIN CERTIFICATE-----\nMIIDezCCAmOgAwIBAgIJAMJcdOLsrN3iMA0GCSqGSIb3DQEBCwUAMFQxCzAJBgNV\n...\n8qh1Vpk2FXoadOVze2fQFLBkkB7LPExj8Nrf76CJEA==\n-----END CERTIFICATE-----",
     "key": "----BEGIN RSA PRIVATE KEY----\nMIIEowIBAAKCAQEAsj2QPAwXYcPDH0mvf6Jbej6RGgYlb4EFMS85BjKrKNPOTqZf\n...\n4j0RY9DeUgSLdy625BBmew2it9l/NynIScG4Ow6w8Bu4iBANGv94\n-----END RSA PRIVATE KEY-----"
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

