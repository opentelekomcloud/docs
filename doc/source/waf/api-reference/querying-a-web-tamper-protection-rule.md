# Querying a Web Tamper Protection Rule<a name="EN-US_TOPIC_0193631183"></a>

## Function Description<a name="section30135943"></a>

This API is used to query details about a web tamper protection rule.

## URI<a name="section2788037"></a>

-   URI format

    GET  /v1/\{project\_id\}/waf/policy/\{policy\_id\}/antitamper/\{antitamper\_rule\_id\}

-   Parameter description

    **Table  1**  Path parameters

    <a name="table13712871"></a>
    <table><thead align="left"><tr id="row62900404"><th class="cellrowborder" valign="top" width="30.930000000000003%" id="mcps1.2.5.1.1"><p id="p61767935"><a name="p61767935"></a><a name="p61767935"></a><strong id="b146175212588"><a name="b146175212588"></a><a name="b146175212588"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.62%" id="mcps1.2.5.1.2"><p id="p37146843"><a name="p37146843"></a><a name="p37146843"></a><strong id="b122896619582"><a name="b122896619582"></a><a name="b122896619582"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.430000000000001%" id="mcps1.2.5.1.3"><p id="p56104303"><a name="p56104303"></a><a name="p56104303"></a><strong id="b6741149165816"><a name="b6741149165816"></a><a name="b6741149165816"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="34.02%" id="mcps1.2.5.1.4"><p id="p48154724"><a name="p48154724"></a><a name="p48154724"></a><strong id="b10558711185812"><a name="b10558711185812"></a><a name="b10558711185812"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8218594"><td class="cellrowborder" valign="top" width="30.930000000000003%" headers="mcps1.2.5.1.1 "><p id="p61726352"><a name="p61726352"></a><a name="p61726352"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.5.1.2 "><p id="p33778582"><a name="p33778582"></a><a name="p33778582"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.430000000000001%" headers="mcps1.2.5.1.3 "><p id="p51710621"><a name="p51710621"></a><a name="p51710621"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.5.1.4 "><p id="p27810764"><a name="p27810764"></a><a name="p27810764"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row48970291"><td class="cellrowborder" valign="top" width="30.930000000000003%" headers="mcps1.2.5.1.1 "><p id="p7170610"><a name="p7170610"></a><a name="p7170610"></a>policy_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.5.1.2 "><p id="p43948526"><a name="p43948526"></a><a name="p43948526"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.430000000000001%" headers="mcps1.2.5.1.3 "><p id="p3060814"><a name="p3060814"></a><a name="p3060814"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.5.1.4 "><p id="p46599354"><a name="p46599354"></a><a name="p46599354"></a>Specifies the policy ID.</p>
    </td>
    </tr>
    <tr id="row16741009"><td class="cellrowborder" valign="top" width="30.930000000000003%" headers="mcps1.2.5.1.1 "><p id="p13844475"><a name="p13844475"></a><a name="p13844475"></a>antitamper_rule_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.5.1.2 "><p id="p47660710"><a name="p47660710"></a><a name="p47660710"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.430000000000001%" headers="mcps1.2.5.1.3 "><p id="p35312314"><a name="p35312314"></a><a name="p35312314"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.5.1.4 "><p id="p41725149"><a name="p41725149"></a><a name="p41725149"></a>Specifies the ID of a web tamper protection rule.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section25092333"></a>

Request parameters

None

## Response<a name="section24504410"></a>

Response parameters

**Table  2**  Parameter description

<a name="table9030076"></a>
<table><thead align="left"><tr id="row65221839"><th class="cellrowborder" valign="top" width="24.467553244675532%" id="mcps1.2.4.1.1"><p id="p48477639"><a name="p48477639"></a><a name="p48477639"></a><strong id="b1648184519581"><a name="b1648184519581"></a><a name="b1648184519581"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="35.736426357364266%" id="mcps1.2.4.1.2"><p id="p34374671"><a name="p34374671"></a><a name="p34374671"></a><strong id="b19648144745810"><a name="b19648144745810"></a><a name="b19648144745810"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.4.1.3"><p id="p32884943"><a name="p32884943"></a><a name="p32884943"></a><strong id="b9134105417581"><a name="b9134105417581"></a><a name="b9134105417581"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row27529036"><td class="cellrowborder" valign="top" width="24.467553244675532%" headers="mcps1.2.4.1.1 "><p id="p15259444"><a name="p15259444"></a><a name="p15259444"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="35.736426357364266%" headers="mcps1.2.4.1.2 "><p id="p28055465"><a name="p28055465"></a><a name="p28055465"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p57900178"><a name="p57900178"></a><a name="p57900178"></a>Specifies the ID of a web tamper protection rule.</p>
</td>
</tr>
<tr id="row51339558"><td class="cellrowborder" valign="top" width="24.467553244675532%" headers="mcps1.2.4.1.1 "><p id="p64863513"><a name="p64863513"></a><a name="p64863513"></a>policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="35.736426357364266%" headers="mcps1.2.4.1.2 "><p id="p19453172"><a name="p19453172"></a><a name="p19453172"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p32203104"><a name="p32203104"></a><a name="p32203104"></a>Specifies the policy ID.</p>
</td>
</tr>
<tr id="row21392484"><td class="cellrowborder" valign="top" width="24.467553244675532%" headers="mcps1.2.4.1.1 "><p id="p55069611"><a name="p55069611"></a><a name="p55069611"></a>hostname</p>
</td>
<td class="cellrowborder" valign="top" width="35.736426357364266%" headers="mcps1.2.4.1.2 "><p id="p31453527"><a name="p31453527"></a><a name="p31453527"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p64707792"><a name="p64707792"></a><a name="p64707792"></a>Specifies the domain name.</p>
</td>
</tr>
<tr id="row45499221"><td class="cellrowborder" valign="top" width="24.467553244675532%" headers="mcps1.2.4.1.1 "><p id="p61558251"><a name="p61558251"></a><a name="p61558251"></a>path</p>
</td>
<td class="cellrowborder" valign="top" width="35.736426357364266%" headers="mcps1.2.4.1.2 "><p id="p20162434"><a name="p20162434"></a><a name="p20162434"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p22544449"><a name="p22544449"></a><a name="p22544449"></a>Specifies the URL protected by the web tamper protection rule, excluding a domain name.</p>
</td>
</tr>
<tr id="row1573456"><td class="cellrowborder" valign="top" width="24.467553244675532%" headers="mcps1.2.4.1.1 "><p id="p60341087"><a name="p60341087"></a><a name="p60341087"></a>timestamp</p>
</td>
<td class="cellrowborder" valign="top" width="35.736426357364266%" headers="mcps1.2.4.1.2 "><p id="p55789867"><a name="p55789867"></a><a name="p55789867"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p12128762"><a name="p12128762"></a><a name="p12128762"></a>Specifies the time when the cache is refreshed.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section15436112218515"></a>

Rule ID  **3a9b5c0f96784ec8abd8ba61a98064ef**  is used as an example.

Response example

```
{
      "id": "3a9b5c0f96784ec8abd8ba61a98064ef",
      "policy_id": "yuc0e55865544d1f8c95cf71df108c6b",
      "hostname": "www.aaa.com",
      "path": "/a",
      "timestamp": 1499817600
}
```

## Status Code<a name="section19213099"></a>

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

