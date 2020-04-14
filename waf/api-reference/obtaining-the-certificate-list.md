# Obtaining the Certificate List<a name="EN-US_TOPIC_0193631110"></a>

## Function Description<a name="section34155517"></a>

This API is used to obtain the certificate list of a user.

## URI<a name="section38964204"></a>

-   URI format

    GET  /v1/\{project\_id\}/waf/certificate?offset=\{offset\}&limit=\{limit\}

-   Parameter description

    **Table  1**  Path parameters

    <a name="table1039446101818"></a>
    <table><thead align="left"><tr id="row133984613186"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p839346151813"><a name="p839346151813"></a><a name="p839346151813"></a><strong id="b179121613193"><a name="b179121613193"></a><a name="b179121613193"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.2"><p id="p939114618181"><a name="p939114618181"></a><a name="p939114618181"></a><strong id="b594417741915"><a name="b594417741915"></a><a name="b594417741915"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.3"><p id="p173994620185"><a name="p173994620185"></a><a name="p173994620185"></a><strong id="b179444816199"><a name="b179444816199"></a><a name="b179444816199"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.5.1.4"><p id="p939184615184"><a name="p939184615184"></a><a name="p939184615184"></a><strong id="b18353951914"><a name="b18353951914"></a><a name="b18353951914"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row83944617189"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p9398461184"><a name="p9398461184"></a><a name="p9398461184"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p639174611820"><a name="p639174611820"></a><a name="p639174611820"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p1339646181816"><a name="p1339646181816"></a><a name="p1339646181816"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p1539114661810"><a name="p1539114661810"></a><a name="p1539114661810"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row6706181910168"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p970043120256"><a name="p970043120256"></a><a name="p970043120256"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p8699203112517"><a name="p8699203112517"></a><a name="p8699203112517"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p2699103110258"><a name="p2699103110258"></a><a name="p2699103110258"></a>Long</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p21617533"><a name="p21617533"></a><a name="p21617533"></a>Specifies the number of returned pages. Its value ranges from <strong id="b182506512333"><a name="b182506512333"></a><a name="b182506512333"></a>0</strong> to <strong id="b172508515338"><a name="b172508515338"></a><a name="b172508515338"></a>65535</strong>. The default value is <strong id="b825015143314"><a name="b825015143314"></a><a name="b825015143314"></a>0</strong>.</p>
    </td>
    </tr>
    <tr id="row139211333181614"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p126961631102512"><a name="p126961631102512"></a><a name="p126961631102512"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p369553116251"><a name="p369553116251"></a><a name="p369553116251"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p269473120252"><a name="p269473120252"></a><a name="p269473120252"></a>Long</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p25357967"><a name="p25357967"></a><a name="p25357967"></a>Specifies the maximum number of records displayed on each page. Its value ranges from <strong id="b165636793319"><a name="b165636793319"></a><a name="b165636793319"></a>0</strong> to <strong id="b056312723313"><a name="b056312723313"></a><a name="b056312723313"></a>50</strong>. The default value is <strong id="b125632714337"><a name="b125632714337"></a><a name="b125632714337"></a>10</strong>. If <strong id="b771592013262"><a name="b771592013262"></a><a name="b771592013262"></a>limit</strong> is <strong id="b1899632313266"><a name="b1899632313266"></a><a name="b1899632313266"></a>-1</strong>, one page with 65535 records is displayed.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section15133516"></a>

Request parameters

None

## Response<a name="section1983919"></a>

Response parameters

**Table  2**  Parameter description

<a name="table50183647"></a>
<table><thead align="left"><tr id="row48503826"><th class="cellrowborder" valign="top" width="24.490000000000002%" id="mcps1.2.4.1.1"><p id="p36495809"><a name="p36495809"></a><a name="p36495809"></a><strong id="b10431135810265"><a name="b10431135810265"></a><a name="b10431135810265"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.349999999999998%" id="mcps1.2.4.1.2"><p id="p3370541"><a name="p3370541"></a><a name="p3370541"></a><strong id="b115417595267"><a name="b115417595267"></a><a name="b115417595267"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="58.160000000000004%" id="mcps1.2.4.1.3"><p id="p4578365"><a name="p4578365"></a><a name="p4578365"></a><strong id="b1921420012712"><a name="b1921420012712"></a><a name="b1921420012712"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row41205286"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p49293864"><a name="p49293864"></a><a name="p49293864"></a>total</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p33380034"><a name="p33380034"></a><a name="p33380034"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p19428253"><a name="p19428253"></a><a name="p19428253"></a>Specifies the total number of certificates.</p>
</td>
</tr>
<tr id="row40636554"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p3226601"><a name="p3226601"></a><a name="p3226601"></a>items</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p60028124"><a name="p60028124"></a><a name="p60028124"></a><a href="#table16394183011019">Table 3</a></p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p30439884"><a name="p30439884"></a><a name="p30439884"></a>Specifies the certificate objects.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **items**

<a name="table16394183011019"></a>
<table><thead align="left"><tr id="row939613301015"><th class="cellrowborder" valign="top" width="24.787521247875212%" id="mcps1.2.4.1.1"><p id="p039873016013"><a name="p039873016013"></a><a name="p039873016013"></a><strong id="b16552850181110"><a name="b16552850181110"></a><a name="b16552850181110"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.27667233276672%" id="mcps1.2.4.1.2"><p id="p183997301406"><a name="p183997301406"></a><a name="p183997301406"></a><strong id="b603424731"><a name="b603424731"></a><a name="b603424731"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="41.935806419358066%" id="mcps1.2.4.1.3"><p id="p839973013010"><a name="p839973013010"></a><a name="p839973013010"></a><strong id="b134520161217"><a name="b134520161217"></a><a name="b134520161217"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row194351472276"><td class="cellrowborder" valign="top" width="24.787521247875212%" headers="mcps1.2.4.1.1 "><p id="p431664632715"><a name="p431664632715"></a><a name="p431664632715"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="33.27667233276672%" headers="mcps1.2.4.1.2 "><p id="p5316174618270"><a name="p5316174618270"></a><a name="p5316174618270"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="41.935806419358066%" headers="mcps1.2.4.1.3 "><p id="p9317204622716"><a name="p9317204622716"></a><a name="p9317204622716"></a>Specifies the certificate ID.</p>
</td>
</tr>
<tr id="row74352472273"><td class="cellrowborder" valign="top" width="24.787521247875212%" headers="mcps1.2.4.1.1 "><p id="p9318746172714"><a name="p9318746172714"></a><a name="p9318746172714"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="33.27667233276672%" headers="mcps1.2.4.1.2 "><p id="p432084622716"><a name="p432084622716"></a><a name="p432084622716"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="41.935806419358066%" headers="mcps1.2.4.1.3 "><p id="p12321846172712"><a name="p12321846172712"></a><a name="p12321846172712"></a>Specifies the certificate name.</p>
</td>
</tr>
<tr id="row106651551447"><td class="cellrowborder" valign="top" width="24.787521247875212%" headers="mcps1.2.4.1.1 "><p id="p466545510448"><a name="p466545510448"></a><a name="p466545510448"></a>expireTime</p>
</td>
<td class="cellrowborder" valign="top" width="33.27667233276672%" headers="mcps1.2.4.1.2 "><p id="p11665125516444"><a name="p11665125516444"></a><a name="p11665125516444"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="41.935806419358066%" headers="mcps1.2.4.1.3 "><p id="p17665655174419"><a name="p17665655174419"></a><a name="p17665655174419"></a>Specifies the time when the certificate expires.</p>
</td>
</tr>
<tr id="row172896158372"><td class="cellrowborder" valign="top" width="24.787521247875212%" headers="mcps1.2.4.1.1 "><p id="p1028912157374"><a name="p1028912157374"></a><a name="p1028912157374"></a>timestamp</p>
</td>
<td class="cellrowborder" valign="top" width="33.27667233276672%" headers="mcps1.2.4.1.2 "><p id="p328931510372"><a name="p328931510372"></a><a name="p328931510372"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="41.935806419358066%" headers="mcps1.2.4.1.3 "><p id="p6289715133717"><a name="p6289715133717"></a><a name="p6289715133717"></a>Specifies the time when the certificate is uploaded.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section6628133643318"></a>

**total**  with a value of  **2**  is used as an example.

Response example

```
{
   "total": 2,
    "items": [
        {
          "id": "388a7789d55b41d1918b3088a8f1e7f3",
          "name": "cert_a",
          "timestamp": 1544756441859,
          "expireTime": 1545978662373
        }, {
          "id": "388a7789d55b41d1918b3088a8f1e7f4",
          "name": "cert_b",
          "timestamp": 1544756441859,
          "expireTime": 1545978662356
        }]
}
```

## Status Code<a name="section17855279"></a>

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

