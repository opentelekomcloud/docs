# Querying the Source IP Header<a name="EN-US_TOPIC_0193631149"></a>

## Function Description<a name="section2348991"></a>

This API is used to query the source IP header.

## URI<a name="section21140920"></a>

-   URI format

    GET  /v1/\{project\_id\}/waf/map/sipheader?lang=\{lang\}

-   Parameter description

    **Table  1**  Path parameters

    <a name="table3668256"></a>
    <table><thead align="left"><tr id="row13281129"><th class="cellrowborder" valign="top" width="30.930000000000003%" id="mcps1.2.5.1.1"><p id="p2029696"><a name="p2029696"></a><a name="p2029696"></a><strong id="b85051959164116"><a name="b85051959164116"></a><a name="b85051959164116"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.62%" id="mcps1.2.5.1.2"><p id="p30187650"><a name="p30187650"></a><a name="p30187650"></a><strong id="b1179516094213"><a name="b1179516094213"></a><a name="b1179516094213"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.430000000000001%" id="mcps1.2.5.1.3"><p id="p29280601"><a name="p29280601"></a><a name="p29280601"></a><strong id="b1592841174214"><a name="b1592841174214"></a><a name="b1592841174214"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="34.02%" id="mcps1.2.5.1.4"><p id="p22918509"><a name="p22918509"></a><a name="p22918509"></a><strong id="b556162174217"><a name="b556162174217"></a><a name="b556162174217"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row44459941"><td class="cellrowborder" valign="top" width="30.930000000000003%" headers="mcps1.2.5.1.1 "><p id="p44485482"><a name="p44485482"></a><a name="p44485482"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.5.1.2 "><p id="p46554275"><a name="p46554275"></a><a name="p46554275"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.430000000000001%" headers="mcps1.2.5.1.3 "><p id="p12799929"><a name="p12799929"></a><a name="p12799929"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.5.1.4 "><p id="p30161299"><a name="p30161299"></a><a name="p30161299"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row3016237"><td class="cellrowborder" valign="top" width="30.930000000000003%" headers="mcps1.2.5.1.1 "><p id="p42988649"><a name="p42988649"></a><a name="p42988649"></a>lang</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.5.1.2 "><p id="p59528541"><a name="p59528541"></a><a name="p59528541"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.430000000000001%" headers="mcps1.2.5.1.3 "><p id="p57082546"><a name="p57082546"></a><a name="p57082546"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.5.1.4 "><p id="p60283536"><a name="p60283536"></a><a name="p60283536"></a>Specifies the language configuration. The options are <strong id="b10940161594515"><a name="b10940161594515"></a><a name="b10940161594515"></a>zh-cn</strong> and <strong id="b1794031594515"><a name="b1794031594515"></a><a name="b1794031594515"></a>en-us</strong>. The default value is <strong id="b4940181534510"><a name="b4940181534510"></a><a name="b4940181534510"></a>en-us</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section56050555"></a>

Request parameters

None

## Response<a name="section34692954"></a>

Response parameters

**Table  2**  Parameter description

<a name="table42162795"></a>
<table><thead align="left"><tr id="row59545267"><th class="cellrowborder" valign="top" width="36.20637936206379%" id="mcps1.2.4.1.1"><p id="p58437292"><a name="p58437292"></a><a name="p58437292"></a><strong id="b1876425194216"><a name="b1876425194216"></a><a name="b1876425194216"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="23.997600239976002%" id="mcps1.2.4.1.2"><p id="p35800173"><a name="p35800173"></a><a name="p35800173"></a><strong id="b99351725194216"><a name="b99351725194216"></a><a name="b99351725194216"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.4.1.3"><p id="p14132895"><a name="p14132895"></a><a name="p14132895"></a><strong id="b2897126204217"><a name="b2897126204217"></a><a name="b2897126204217"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row60087193"><td class="cellrowborder" valign="top" width="36.20637936206379%" headers="mcps1.2.4.1.1 "><p id="p35224503"><a name="p35224503"></a><a name="p35224503"></a>sipheadermap</p>
</td>
<td class="cellrowborder" valign="top" width="23.997600239976002%" headers="mcps1.2.4.1.2 "><p id="p229951334915"><a name="p229951334915"></a><a name="p229951334915"></a><a href="#table10363184164611">Table 3</a></p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p52149544"><a name="p52149544"></a><a name="p52149544"></a>Specifies the list of source IP headers.</p>
</td>
</tr>
<tr id="row66692715"><td class="cellrowborder" valign="top" width="36.20637936206379%" headers="mcps1.2.4.1.1 "><p id="p33400872"><a name="p33400872"></a><a name="p33400872"></a>locale</p>
</td>
<td class="cellrowborder" valign="top" width="23.997600239976002%" headers="mcps1.2.4.1.2 "><p id="p1865142714918"><a name="p1865142714918"></a><a name="p1865142714918"></a><a href="#table5644135016296">Table 4</a></p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p32682602"><a name="p32682602"></a><a name="p32682602"></a>Specifies additional information.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **sipheadermap**

<a name="table10363184164611"></a>
<table><thead align="left"><tr id="row153652046460"><th class="cellrowborder" valign="top" width="36.236376362363764%" id="mcps1.2.4.1.1"><p id="p136610484618"><a name="p136610484618"></a><a name="p136610484618"></a><strong id="b18458605449"><a name="b18458605449"></a><a name="b18458605449"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="23.967603239676034%" id="mcps1.2.4.1.2"><p id="p1136784104617"><a name="p1136784104617"></a><a name="p1136784104617"></a><strong id="b280218154414"><a name="b280218154414"></a><a name="b280218154414"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.4.1.3"><p id="p43671345468"><a name="p43671345468"></a><a name="p43671345468"></a><strong id="b1859918216442"><a name="b1859918216442"></a><a name="b1859918216442"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1499039124610"><td class="cellrowborder" valign="top" width="36.236376362363764%" headers="mcps1.2.4.1.1 "><p id="p116411451194918"><a name="p116411451194918"></a><a name="p116411451194918"></a>default</p>
</td>
<td class="cellrowborder" valign="top" width="23.967603239676034%" headers="mcps1.2.4.1.2 "><p id="p19988142919502"><a name="p19988142919502"></a><a name="p19988142919502"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p6159944612"><a name="p6159944612"></a><a name="p6159944612"></a>Specifies the default HTTP request header to identify the real source IP address.</p>
</td>
</tr>
<tr id="row999018918466"><td class="cellrowborder" valign="top" width="36.236376362363764%" headers="mcps1.2.4.1.1 "><p id="p111729124610"><a name="p111729124610"></a><a name="p111729124610"></a>cloudflare</p>
</td>
<td class="cellrowborder" valign="top" width="23.967603239676034%" headers="mcps1.2.4.1.2 "><p id="p17176918462"><a name="p17176918462"></a><a name="p17176918462"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p91810920462"><a name="p91810920462"></a><a name="p91810920462"></a>Specifies the HTTP request header used by Cloudflare to identify the real source IP address.</p>
</td>
</tr>
<tr id="row99909994619"><td class="cellrowborder" valign="top" width="36.236376362363764%" headers="mcps1.2.4.1.1 "><p id="p15934118115010"><a name="p15934118115010"></a><a name="p15934118115010"></a>akamai</p>
</td>
<td class="cellrowborder" valign="top" width="23.967603239676034%" headers="mcps1.2.4.1.2 "><p id="p14211799464"><a name="p14211799464"></a><a name="p14211799464"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p72219934613"><a name="p72219934613"></a><a name="p72219934613"></a>Specifies the HTTP request header used by Akamai to identify the real source IP address.</p>
</td>
</tr>
<tr id="row10786142191711"><td class="cellrowborder" valign="top" width="36.236376362363764%" headers="mcps1.2.4.1.1 "><p id="p27865426177"><a name="p27865426177"></a><a name="p27865426177"></a>custom</p>
</td>
<td class="cellrowborder" valign="top" width="23.967603239676034%" headers="mcps1.2.4.1.2 "><p id="p97861342161715"><a name="p97861342161715"></a><a name="p97861342161715"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p578634271720"><a name="p578634271720"></a><a name="p578634271720"></a>Specifies the custom HTTP request header to identify the real source IP address.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **locale**

<a name="table5644135016296"></a>
<table><thead align="left"><tr id="row06502503297"><th class="cellrowborder" valign="top" width="36.236376362363764%" id="mcps1.2.4.1.1"><p id="p465010506292"><a name="p465010506292"></a><a name="p465010506292"></a><strong id="b191201527605"><a name="b191201527605"></a><a name="b191201527605"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="23.967603239676034%" id="mcps1.2.4.1.2"><p id="p8652155032917"><a name="p8652155032917"></a><a name="p8652155032917"></a><strong id="b1141216121304"><a name="b1141216121304"></a><a name="b1141216121304"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.4.1.3"><p id="p18654350172918"><a name="p18654350172918"></a><a name="p18654350172918"></a><strong id="b376414245020"><a name="b376414245020"></a><a name="b376414245020"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row206554501298"><td class="cellrowborder" valign="top" width="36.236376362363764%" headers="mcps1.2.4.1.1 "><p id="p20658175015297"><a name="p20658175015297"></a><a name="p20658175015297"></a>default</p>
</td>
<td class="cellrowborder" valign="top" width="23.967603239676034%" headers="mcps1.2.4.1.2 "><p id="p16658550162912"><a name="p16658550162912"></a><a name="p16658550162912"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p4661175011295"><a name="p4661175011295"></a><a name="p4661175011295"></a>The value is <strong id="b1974928103416"><a name="b1974928103416"></a><a name="b1974928103416"></a>Default</strong>.</p>
</td>
</tr>
<tr id="row10663185012295"><td class="cellrowborder" valign="top" width="36.236376362363764%" headers="mcps1.2.4.1.1 "><p id="p16663135018290"><a name="p16663135018290"></a><a name="p16663135018290"></a>cloudflare</p>
</td>
<td class="cellrowborder" valign="top" width="23.967603239676034%" headers="mcps1.2.4.1.2 "><p id="p196651350112919"><a name="p196651350112919"></a><a name="p196651350112919"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p666725010296"><a name="p666725010296"></a><a name="p666725010296"></a>The value is <strong id="b15169154253416"><a name="b15169154253416"></a><a name="b15169154253416"></a>CloudFlare</strong>.</p>
</td>
</tr>
<tr id="row1166716506298"><td class="cellrowborder" valign="top" width="36.236376362363764%" headers="mcps1.2.4.1.1 "><p id="p37409101321"><a name="p37409101321"></a><a name="p37409101321"></a>akamai</p>
</td>
<td class="cellrowborder" valign="top" width="23.967603239676034%" headers="mcps1.2.4.1.2 "><p id="p96731950152912"><a name="p96731950152912"></a><a name="p96731950152912"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p3675165020293"><a name="p3675165020293"></a><a name="p3675165020293"></a>The value is <strong id="b3390163217147"><a name="b3390163217147"></a><a name="b3390163217147"></a>Akamai</strong>.</p>
</td>
</tr>
<tr id="row967565014293"><td class="cellrowborder" valign="top" width="36.236376362363764%" headers="mcps1.2.4.1.1 "><p id="p1676155052920"><a name="p1676155052920"></a><a name="p1676155052920"></a>custom</p>
</td>
<td class="cellrowborder" valign="top" width="23.967603239676034%" headers="mcps1.2.4.1.2 "><p id="p36789507293"><a name="p36789507293"></a><a name="p36789507293"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p067885015291"><a name="p067885015291"></a><a name="p067885015291"></a>The value is <strong id="b2920184018354"><a name="b2920184018354"></a><a name="b2920184018354"></a>Custom</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section182891739095"></a>

Response example

```
{
  "sipheadermap": {
      "default": ["X-Forwarded-For"],
      "cloudflare": ["CF-Connecting-IP", "X-Forwarded-For"],
      "akamai": ["True-Client-IP"],
      "custom": []
  },
  "locale": {
       "default": "Default",
       "cloudflare": "CloudFlare",
       "akamai": "Akamai",
       "custom": "Custom"
   }
}
```

## Status Code<a name="section43801132"></a>

[Table 5](#en-us_topic_0193631139_t82c3440f3efb42a38b9d4dc4011a33d0)  describes the normal status code returned by the API.

**Table  5**  Status code

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

