# Querying Event Type in Alarm Notifications<a name="EN-US_TOPIC_0193631131"></a>

## Function Description<a name="section2348991"></a>

This API is used to query event type in an alarm notification.

## URI<a name="section21140920"></a>

-   URI format

    GET  /v1/\{project\_id\}/waf/map/threat?lang=\{lang\}

-   Parameter description

    **Table  1**  Path parameters

    <a name="table3668256"></a>
    <table><thead align="left"><tr id="row13281129"><th class="cellrowborder" valign="top" width="30.930000000000003%" id="mcps1.2.5.1.1"><p id="p2029696"><a name="p2029696"></a><a name="p2029696"></a><strong id="b14401121281618"><a name="b14401121281618"></a><a name="b14401121281618"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.62%" id="mcps1.2.5.1.2"><p id="p30187650"><a name="p30187650"></a><a name="p30187650"></a><strong id="b1619251414161"><a name="b1619251414161"></a><a name="b1619251414161"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.430000000000001%" id="mcps1.2.5.1.3"><p id="p29280601"><a name="p29280601"></a><a name="p29280601"></a><strong id="b11227316111615"><a name="b11227316111615"></a><a name="b11227316111615"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="34.02%" id="mcps1.2.5.1.4"><p id="p22918509"><a name="p22918509"></a><a name="p22918509"></a><strong id="b5522171791617"><a name="b5522171791617"></a><a name="b5522171791617"></a>Description</strong></p>
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
    <td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.5.1.4 "><p id="p60283536"><a name="p60283536"></a><a name="p60283536"></a>Specifies the language configuration. The options are <strong id="b4580838911"><a name="b4580838911"></a><a name="b4580838911"></a>zh-cn</strong> and <strong id="b75801338616"><a name="b75801338616"></a><a name="b75801338616"></a>en-us</strong>. The default value is <strong id="b19580123817116"><a name="b19580123817116"></a><a name="b19580123817116"></a>en-us</strong>.</p>
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
<table><thead align="left"><tr id="row59545267"><th class="cellrowborder" valign="top" width="36.20637936206379%" id="mcps1.2.4.1.1"><p id="p58437292"><a name="p58437292"></a><a name="p58437292"></a><strong id="b1255515015179"><a name="b1255515015179"></a><a name="b1255515015179"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="23.997600239976002%" id="mcps1.2.4.1.2"><p id="p35800173"><a name="p35800173"></a><a name="p35800173"></a><strong id="b12630175"><a name="b12630175"></a><a name="b12630175"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.4.1.3"><p id="p14132895"><a name="p14132895"></a><a name="p14132895"></a><strong id="b94036314175"><a name="b94036314175"></a><a name="b94036314175"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row60087193"><td class="cellrowborder" valign="top" width="36.20637936206379%" headers="mcps1.2.4.1.1 "><p id="p35224503"><a name="p35224503"></a><a name="p35224503"></a>threats</p>
</td>
<td class="cellrowborder" valign="top" width="23.997600239976002%" headers="mcps1.2.4.1.2 "><p id="p34612505"><a name="p34612505"></a><a name="p34612505"></a>List</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p52149544"><a name="p52149544"></a><a name="p52149544"></a>Specifies the list of event types.</p>
</td>
</tr>
<tr id="row66692715"><td class="cellrowborder" valign="top" width="36.20637936206379%" headers="mcps1.2.4.1.1 "><p id="p33400872"><a name="p33400872"></a><a name="p33400872"></a>locale</p>
</td>
<td class="cellrowborder" valign="top" width="23.997600239976002%" headers="mcps1.2.4.1.2 "><p id="p21116101"><a name="p21116101"></a><a name="p21116101"></a><a href="#table10363184164611">Table 3</a></p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p32682602"><a name="p32682602"></a><a name="p32682602"></a>Specifies event names.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **locale**

<a name="table10363184164611"></a>
<table><thead align="left"><tr id="row153652046460"><th class="cellrowborder" valign="top" width="36.236376362363764%" id="mcps1.2.4.1.1"><p id="p136610484618"><a name="p136610484618"></a><a name="p136610484618"></a><strong id="b4167162875017"><a name="b4167162875017"></a><a name="b4167162875017"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="23.967603239676034%" id="mcps1.2.4.1.2"><p id="p1136784104617"><a name="p1136784104617"></a><a name="p1136784104617"></a><strong id="b328095578"><a name="b328095578"></a><a name="b328095578"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.4.1.3"><p id="p43671345468"><a name="p43671345468"></a><a name="p43671345468"></a><strong id="b985514337500"><a name="b985514337500"></a><a name="b985514337500"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1499039124610"><td class="cellrowborder" valign="top" width="36.236376362363764%" headers="mcps1.2.4.1.1 "><p id="p71417914468"><a name="p71417914468"></a><a name="p71417914468"></a>xss</p>
</td>
<td class="cellrowborder" valign="top" width="23.967603239676034%" headers="mcps1.2.4.1.2 "><p id="p14141696468"><a name="p14141696468"></a><a name="p14141696468"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p6159944612"><a name="p6159944612"></a><a name="p6159944612"></a>Specifies XSS attack.</p>
</td>
</tr>
<tr id="row999018918466"><td class="cellrowborder" valign="top" width="36.236376362363764%" headers="mcps1.2.4.1.1 "><p id="p111729124610"><a name="p111729124610"></a><a name="p111729124610"></a>sqli</p>
</td>
<td class="cellrowborder" valign="top" width="23.967603239676034%" headers="mcps1.2.4.1.2 "><p id="p17176918462"><a name="p17176918462"></a><a name="p17176918462"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p91810920462"><a name="p91810920462"></a><a name="p91810920462"></a>Specifies SQL injection.</p>
</td>
</tr>
<tr id="row99909994619"><td class="cellrowborder" valign="top" width="36.236376362363764%" headers="mcps1.2.4.1.1 "><p id="p19209954613"><a name="p19209954613"></a><a name="p19209954613"></a>cmdi</p>
</td>
<td class="cellrowborder" valign="top" width="23.967603239676034%" headers="mcps1.2.4.1.2 "><p id="p14211799464"><a name="p14211799464"></a><a name="p14211799464"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p72219934613"><a name="p72219934613"></a><a name="p72219934613"></a>Specifies command injection.</p>
</td>
</tr>
<tr id="row10786142191711"><td class="cellrowborder" valign="top" width="36.236376362363764%" headers="mcps1.2.4.1.1 "><p id="p27865426177"><a name="p27865426177"></a><a name="p27865426177"></a>cc</p>
</td>
<td class="cellrowborder" valign="top" width="23.967603239676034%" headers="mcps1.2.4.1.2 "><p id="p97861342161715"><a name="p97861342161715"></a><a name="p97861342161715"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p578634271720"><a name="p578634271720"></a><a name="p578634271720"></a>Specifies CC attack.</p>
</td>
</tr>
<tr id="row121151047101711"><td class="cellrowborder" valign="top" width="36.236376362363764%" headers="mcps1.2.4.1.1 "><p id="p1632464641717"><a name="p1632464641717"></a><a name="p1632464641717"></a>custom</p>
</td>
<td class="cellrowborder" valign="top" width="23.967603239676034%" headers="mcps1.2.4.1.2 "><p id="p153251146121714"><a name="p153251146121714"></a><a name="p153251146121714"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p1832684611718"><a name="p1832684611718"></a><a name="p1832684611718"></a>Specifies Precise Protection.</p>
</td>
</tr>
<tr id="row1652495201710"><td class="cellrowborder" valign="top" width="36.236376362363764%" headers="mcps1.2.4.1.1 "><p id="p17469125120179"><a name="p17469125120179"></a><a name="p17469125120179"></a>illegal</p>
</td>
<td class="cellrowborder" valign="top" width="23.967603239676034%" headers="mcps1.2.4.1.2 "><p id="p7469135117175"><a name="p7469135117175"></a><a name="p7469135117175"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p847045141711"><a name="p847045141711"></a><a name="p847045141711"></a>Specifies invalid requests.</p>
</td>
</tr>
<tr id="row1148625421716"><td class="cellrowborder" valign="top" width="36.236376362363764%" headers="mcps1.2.4.1.1 "><p id="p16793185361716"><a name="p16793185361716"></a><a name="p16793185361716"></a>lfi</p>
</td>
<td class="cellrowborder" valign="top" width="23.967603239676034%" headers="mcps1.2.4.1.2 "><p id="p1979405315173"><a name="p1979405315173"></a><a name="p1979405315173"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p117951153131716"><a name="p117951153131716"></a><a name="p117951153131716"></a>Specifies local file inclusion.</p>
</td>
</tr>
<tr id="row193101356161712"><td class="cellrowborder" valign="top" width="36.236376362363764%" headers="mcps1.2.4.1.1 "><p id="p17603185531720"><a name="p17603185531720"></a><a name="p17603185531720"></a>robot</p>
</td>
<td class="cellrowborder" valign="top" width="23.967603239676034%" headers="mcps1.2.4.1.2 "><p id="p14604165541718"><a name="p14604165541718"></a><a name="p14604165541718"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p660585517172"><a name="p660585517172"></a><a name="p660585517172"></a>Specifies malicious crawlers.</p>
</td>
</tr>
<tr id="row753558121714"><td class="cellrowborder" valign="top" width="36.236376362363764%" headers="mcps1.2.4.1.1 "><p id="p3348145711711"><a name="p3348145711711"></a><a name="p3348145711711"></a>antitamper</p>
</td>
<td class="cellrowborder" valign="top" width="23.967603239676034%" headers="mcps1.2.4.1.2 "><p id="p1634917572179"><a name="p1634917572179"></a><a name="p1634917572179"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p143501357161717"><a name="p143501357161717"></a><a name="p143501357161717"></a>Specifies Web Tamper Protection.</p>
</td>
</tr>
<tr id="row283411712214"><td class="cellrowborder" valign="top" width="36.236376362363764%" headers="mcps1.2.4.1.1 "><p id="p383461710220"><a name="p383461710220"></a><a name="p383461710220"></a>rfi</p>
</td>
<td class="cellrowborder" valign="top" width="23.967603239676034%" headers="mcps1.2.4.1.2 "><p id="p8834141742214"><a name="p8834141742214"></a><a name="p8834141742214"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p138351317192213"><a name="p138351317192213"></a><a name="p138351317192213"></a>Specifies remote file inclusion.</p>
</td>
</tr>
<tr id="row1651172232219"><td class="cellrowborder" valign="top" width="36.236376362363764%" headers="mcps1.2.4.1.1 "><p id="p10654102112220"><a name="p10654102112220"></a><a name="p10654102112220"></a>vuln</p>
</td>
<td class="cellrowborder" valign="top" width="23.967603239676034%" headers="mcps1.2.4.1.2 "><p id="p6655122113224"><a name="p6655122113224"></a><a name="p6655122113224"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p965713213222"><a name="p965713213222"></a><a name="p965713213222"></a>Specifies other types of attacks.</p>
</td>
</tr>
<tr id="row1626142414227"><td class="cellrowborder" valign="top" width="36.236376362363764%" headers="mcps1.2.4.1.1 "><p id="p12974102315223"><a name="p12974102315223"></a><a name="p12974102315223"></a>whiteblackip</p>
</td>
<td class="cellrowborder" valign="top" width="23.967603239676034%" headers="mcps1.2.4.1.2 "><p id="p497612312212"><a name="p497612312212"></a><a name="p497612312212"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p297810239225"><a name="p297810239225"></a><a name="p297810239225"></a>Specifies Blacklist and Whitelist.</p>
</td>
</tr>
<tr id="row175573263222"><td class="cellrowborder" valign="top" width="36.236376362363764%" headers="mcps1.2.4.1.1 "><p id="p14799025112217"><a name="p14799025112217"></a><a name="p14799025112217"></a>webshell</p>
</td>
<td class="cellrowborder" valign="top" width="23.967603239676034%" headers="mcps1.2.4.1.2 "><p id="p19801525182212"><a name="p19801525182212"></a><a name="p19801525182212"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p14803225192214"><a name="p14803225192214"></a><a name="p14803225192214"></a>Specifies webshells.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section182891739095"></a>

Response example

```
{
  "threats": ["xss", "sqli", "cmdi"],
  "locale": {
       "xss":  "Cross Site Scripting",
       "sqli": "SQL Injection",
       "cmdi": "Command Injection"
   }
}
```

## Status Code<a name="section43801132"></a>

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

