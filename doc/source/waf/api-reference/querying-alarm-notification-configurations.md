# Querying Alarm Notification Configurations<a name="EN-US_TOPIC_0193631105"></a>

## Function Description<a name="section26619133"></a>

This API is used to query alarm notification configurations.

## URI<a name="section8666197"></a>

-   URI format

    GET /v1/\{project\_id\}/waf/config/alert

-   Parameter description

    **Table  1**  Path parameters

    <a name="table4654722"></a>
    <table><thead align="left"><tr id="row28022645"><th class="cellrowborder" valign="top" width="17.528247175282473%" id="mcps1.2.5.1.1"><p id="p55241806"><a name="p55241806"></a><a name="p55241806"></a><strong id="b1524615412475"><a name="b1524615412475"></a><a name="b1524615412475"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.58804119588041%" id="mcps1.2.5.1.2"><p id="p45401307"><a name="p45401307"></a><a name="p45401307"></a><strong id="b16472443184715"><a name="b16472443184715"></a><a name="b16472443184715"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.58804119588041%" id="mcps1.2.5.1.3"><p id="p53627269"><a name="p53627269"></a><a name="p53627269"></a><strong id="b8571845164717"><a name="b8571845164717"></a><a name="b8571845164717"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43.295670432956705%" id="mcps1.2.5.1.4"><p id="p48841523"><a name="p48841523"></a><a name="p48841523"></a><strong id="b9370204654718"><a name="b9370204654718"></a><a name="b9370204654718"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row63849294"><td class="cellrowborder" valign="top" width="17.528247175282473%" headers="mcps1.2.5.1.1 "><p id="p4410301"><a name="p4410301"></a><a name="p4410301"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.58804119588041%" headers="mcps1.2.5.1.2 "><p id="p21690089"><a name="p21690089"></a><a name="p21690089"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.58804119588041%" headers="mcps1.2.5.1.3 "><p id="p12066745"><a name="p12066745"></a><a name="p12066745"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.295670432956705%" headers="mcps1.2.5.1.4 "><p id="p37882261"><a name="p37882261"></a><a name="p37882261"></a>Specifies the project ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section10886911"></a>

Request parameters

None

## Response<a name="section30873341"></a>

Response parameters

**Table  2**  Parameter description

<a name="table64771846"></a>
<table><thead align="left"><tr id="row64088200"><th class="cellrowborder" valign="top" width="17.169999999999998%" id="mcps1.2.4.1.1"><p id="p23761692"><a name="p23761692"></a><a name="p23761692"></a><strong id="b1149711596471"><a name="b1149711596471"></a><a name="b1149711596471"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="19.189999999999998%" id="mcps1.2.4.1.2"><p id="p45648893"><a name="p45648893"></a><a name="p45648893"></a><strong id="b999714253816"><a name="b999714253816"></a><a name="b999714253816"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="63.63999999999999%" id="mcps1.2.4.1.3"><p id="p6572818"><a name="p6572818"></a><a name="p6572818"></a><strong id="b1829416213480"><a name="b1829416213480"></a><a name="b1829416213480"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row62636227"><td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p40369658"><a name="p40369658"></a><a name="p40369658"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p48716828"><a name="p48716828"></a><a name="p48716828"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63.63999999999999%" headers="mcps1.2.4.1.3 "><p id="p53749011"><a name="p53749011"></a><a name="p53749011"></a>Specifies the unique ID of an alarm configuration.</p>
</td>
</tr>
<tr id="row13979058"><td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p58561923"><a name="p58561923"></a><a name="p58561923"></a>enabled</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p45895324"><a name="p45895324"></a><a name="p45895324"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="63.63999999999999%" headers="mcps1.2.4.1.3 "><p id="p26533798"><a name="p26533798"></a><a name="p26533798"></a>Specifies whether to send an alarm notification.</p>
<a name="ul11892104301314"></a><a name="ul11892104301314"></a><ul id="ul11892104301314"><li><strong id="b1352145117598"><a name="b1352145117598"></a><a name="b1352145117598"></a>true</strong>: Send the alarm notification.</li><li><strong id="b19132619013"><a name="b19132619013"></a><a name="b19132619013"></a>false</strong>: Do not send the alarm notification.</li></ul>
</td>
</tr>
<tr id="row37477597"><td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p15786515"><a name="p15786515"></a><a name="p15786515"></a>topic_urn</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p3639309"><a name="p3639309"></a><a name="p3639309"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63.63999999999999%" headers="mcps1.2.4.1.3 "><p id="p26348595"><a name="p26348595"></a><a name="p26348595"></a>Specifies the SMN topic to which an alarm is sent.</p>
</td>
</tr>
<tr id="row35810771"><td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p14991335"><a name="p14991335"></a><a name="p14991335"></a>sendfreq</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p6338652"><a name="p6338652"></a><a name="p6338652"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="63.63999999999999%" headers="mcps1.2.4.1.3 "><p id="p43668826"><a name="p43668826"></a><a name="p43668826"></a>Specifies the minimum interval between two alarms in minutes. The options are <strong id="b1979114262719"><a name="b1979114262719"></a><a name="b1979114262719"></a>5</strong>, <strong id="b580418428279"><a name="b580418428279"></a><a name="b580418428279"></a>15</strong>, <strong id="b148041542202715"><a name="b148041542202715"></a><a name="b148041542202715"></a>30</strong>, and <strong id="b48051342172711"><a name="b48051342172711"></a><a name="b48051342172711"></a>60</strong>.</p>
</td>
</tr>
<tr id="row57475115"><td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p24972744"><a name="p24972744"></a><a name="p24972744"></a>times</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p9526402"><a name="p9526402"></a><a name="p9526402"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="63.63999999999999%" headers="mcps1.2.4.1.3 "><p id="p33441088"><a name="p33441088"></a><a name="p33441088"></a>Specifies the alarm threshold. Alarm notifications are sent when the number of attacks is greater than or equal to the threshold within the configured period. This value is greater than or equal to <strong id="b17919112795614"><a name="b17919112795614"></a><a name="b17919112795614"></a>1</strong>.</p>
</td>
</tr>
<tr id="row32534340"><td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p18035908"><a name="p18035908"></a><a name="p18035908"></a>threat</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p51622461"><a name="p51622461"></a><a name="p51622461"></a>List&lt;String&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="63.63999999999999%" headers="mcps1.2.4.1.3 "><p id="p14124143915312"><a name="p14124143915312"></a><a name="p14124143915312"></a>Specifies the list of event types.</p>
<a name="ul527919447315"></a><a name="ul527919447315"></a><ul id="ul527919447315"><li><strong id="b737141018283"><a name="b737141018283"></a><a name="b737141018283"></a>all</strong> refers to all types of events.</li><li><span class="parmvalue" id="parmvalue141323227217"><a name="parmvalue141323227217"></a><a name="parmvalue141323227217"></a><b>cc</b></span> refers to CC attack.</li><li><span class="parmvalue" id="parmvalue651717257219"><a name="parmvalue651717257219"></a><a name="parmvalue651717257219"></a><b>cmdi</b></span> refers to command injection.</li><li><span class="parmvalue" id="parmvalue1477420416349"><a name="parmvalue1477420416349"></a><a name="parmvalue1477420416349"></a><b><span id="text177211341910"><a name="text177211341910"></a><a name="text177211341910"></a>custom</span></b></span> refers to Precise Protection events.</li><li><span class="parmvalue" id="parmvalue5959183316211"><a name="parmvalue5959183316211"></a><a name="parmvalue5959183316211"></a><b>illegal</b></span> refers to invalid requests.</li><li><span class="parmvalue" id="parmvalue1286431010316"><a name="parmvalue1286431010316"></a><a name="parmvalue1286431010316"></a><b>sqli</b></span> refers to SQL injection.</li><li><span class="parmvalue" id="parmvalue667213141837"><a name="parmvalue667213141837"></a><a name="parmvalue667213141837"></a><b>lfi</b></span> refers to local file inclusion.</li><li><strong id="b793672616318"><a name="b793672616318"></a><a name="b793672616318"></a>robot</strong> refers to malicious crawlers.</li><li><span class="parmvalue" id="parmvalue1977255016319"><a name="parmvalue1977255016319"></a><a name="parmvalue1977255016319"></a><b>antitamper</b></span> refers to Web Tamper Protection events.</li><li><span class="parmvalue" id="parmvalue11677254436"><a name="parmvalue11677254436"></a><a name="parmvalue11677254436"></a><b>rfi</b></span> refers to remote file inclusion.</li><li><span class="parmvalue" id="parmvalue194921581238"><a name="parmvalue194921581238"></a><a name="parmvalue194921581238"></a><b>vuln</b></span> refers to other types of attacks.</li><li><span class="parmvalue" id="parmvalue518820212412"><a name="parmvalue518820212412"></a><a name="parmvalue518820212412"></a><b>xss</b></span> refers to XSS attack.</li><li><span class="parmvalue" id="parmvalue1615281413355"><a name="parmvalue1615281413355"></a><a name="parmvalue1615281413355"></a><b><span id="text154249505594"><a name="text154249505594"></a><a name="text154249505594"></a>whiteblackip</span></b></span> refers to Blacklist and Whitelist events.</li><li><span class="parmvalue" id="parmvalue2017838943"><a name="parmvalue2017838943"></a><a name="parmvalue2017838943"></a><b>webshell</b></span> refers to webshells.</li></ul>
</td>
</tr>
<tr id="row51810310"><td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p35885554"><a name="p35885554"></a><a name="p35885554"></a>locale</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p21048787"><a name="p21048787"></a><a name="p21048787"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63.63999999999999%" headers="mcps1.2.4.1.3 "><p id="p27230225"><a name="p27230225"></a><a name="p27230225"></a>Specifies the language configuration. Only <strong id="b1453333516457"><a name="b1453333516457"></a><a name="b1453333516457"></a>zh-cn</strong> and <strong id="b8541203516457"><a name="b8541203516457"></a><a name="b8541203516457"></a>en-us</strong> are supported. The default value is <strong id="b254113534515"><a name="b254113534515"></a><a name="b254113534515"></a>en-us</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section107161616131618"></a>

Response example

```
{
    "id": "37b4bbe8a562453aa0163a96e6b71dd6",
    "enabled": true,
    "topic_urn": "urn:smn:eude:fca6f667ac5f4d9798d1641dfd38106b:wbtest",
    "sendfreq": 5,
    "times": 200,
    "threat": ["xss", "sqli", "cmdi"],
    "locale": "en-us"
}
```

## Status Code<a name="section9424614"></a>

[Table 3](#en-us_topic_0193631139_t82c3440f3efb42a38b9d4dc4011a33d0)  describes the normal status code returned by the API.

**Table  3**  Status code

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

