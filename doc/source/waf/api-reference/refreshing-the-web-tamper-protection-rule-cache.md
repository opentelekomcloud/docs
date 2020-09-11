# Refreshing the Web Tamper Protection Rule Cache<a name="EN-US_TOPIC_0193631160"></a>

## Function Description<a name="section13997563"></a>

This API is used to refresh cache in a web tamper protection rule in the event of changes on the protected webpage.

## URI<a name="section58869205"></a>

-   URI format

    POST /v1/\{project\_id\}/waf/policy/\{policy\_id\}/antitamper/\{antitamper\_rule\_id\}/cache

-   Parameter description

    **Table  1**  Path parameters

    <a name="table43562928"></a>
    <table><thead align="left"><tr id="row65864810"><th class="cellrowborder" valign="top" width="30.930000000000003%" id="mcps1.2.5.1.1"><p id="p33449373"><a name="p33449373"></a><a name="p33449373"></a><strong id="b729451910111"><a name="b729451910111"></a><a name="b729451910111"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.62%" id="mcps1.2.5.1.2"><p id="p25044664"><a name="p25044664"></a><a name="p25044664"></a><strong id="b7382172418111"><a name="b7382172418111"></a><a name="b7382172418111"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.430000000000001%" id="mcps1.2.5.1.3"><p id="p15351908"><a name="p15351908"></a><a name="p15351908"></a><strong id="b1284116259110"><a name="b1284116259110"></a><a name="b1284116259110"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="34.02%" id="mcps1.2.5.1.4"><p id="p35545032"><a name="p35545032"></a><a name="p35545032"></a><strong id="b5310027817"><a name="b5310027817"></a><a name="b5310027817"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row60575373"><td class="cellrowborder" valign="top" width="30.930000000000003%" headers="mcps1.2.5.1.1 "><p id="p7658203"><a name="p7658203"></a><a name="p7658203"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.5.1.2 "><p id="p16334681"><a name="p16334681"></a><a name="p16334681"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.430000000000001%" headers="mcps1.2.5.1.3 "><p id="p48040751"><a name="p48040751"></a><a name="p48040751"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.5.1.4 "><p id="p66095622"><a name="p66095622"></a><a name="p66095622"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row57989689"><td class="cellrowborder" valign="top" width="30.930000000000003%" headers="mcps1.2.5.1.1 "><p id="p66653236"><a name="p66653236"></a><a name="p66653236"></a>policy_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.5.1.2 "><p id="p30203011"><a name="p30203011"></a><a name="p30203011"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.430000000000001%" headers="mcps1.2.5.1.3 "><p id="p30524815"><a name="p30524815"></a><a name="p30524815"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.5.1.4 "><p id="p56590911"><a name="p56590911"></a><a name="p56590911"></a>Specifies the policy ID.</p>
    </td>
    </tr>
    <tr id="row39556152"><td class="cellrowborder" valign="top" width="30.930000000000003%" headers="mcps1.2.5.1.1 "><p id="p49931738"><a name="p49931738"></a><a name="p49931738"></a>antitamper_rule_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.5.1.2 "><p id="p17938964"><a name="p17938964"></a><a name="p17938964"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.430000000000001%" headers="mcps1.2.5.1.3 "><p id="p43769999"><a name="p43769999"></a><a name="p43769999"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.5.1.4 "><p id="p55709043"><a name="p55709043"></a><a name="p55709043"></a>Specifies the ID of a web tamper protection rule.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section60060800"></a>

Request parameters

None

## Response<a name="section3676294"></a>

Response parameters

**Table  2**  Parameter description

<a name="table9030076"></a>
<table><thead align="left"><tr id="row65221839"><th class="cellrowborder" valign="top" width="30.15698430156984%" id="mcps1.2.4.1.1"><p id="p48477639"><a name="p48477639"></a><a name="p48477639"></a><strong id="b14580102843416"><a name="b14580102843416"></a><a name="b14580102843416"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="30.046995300469952%" id="mcps1.2.4.1.2"><p id="p34374671"><a name="p34374671"></a><a name="p34374671"></a><strong id="b58841029143420"><a name="b58841029143420"></a><a name="b58841029143420"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.4.1.3"><p id="p32884943"><a name="p32884943"></a><a name="p32884943"></a><strong id="b1814903115344"><a name="b1814903115344"></a><a name="b1814903115344"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row27529036"><td class="cellrowborder" valign="top" width="30.15698430156984%" headers="mcps1.2.4.1.1 "><p id="p15259444"><a name="p15259444"></a><a name="p15259444"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="30.046995300469952%" headers="mcps1.2.4.1.2 "><p id="p28055465"><a name="p28055465"></a><a name="p28055465"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p57900178"><a name="p57900178"></a><a name="p57900178"></a>Specifies the ID of a web tamper protection rule.</p>
</td>
</tr>
<tr id="row51339558"><td class="cellrowborder" valign="top" width="30.15698430156984%" headers="mcps1.2.4.1.1 "><p id="p64863513"><a name="p64863513"></a><a name="p64863513"></a>policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="30.046995300469952%" headers="mcps1.2.4.1.2 "><p id="p19453172"><a name="p19453172"></a><a name="p19453172"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p32203104"><a name="p32203104"></a><a name="p32203104"></a>Specifies the policy ID.</p>
</td>
</tr>
<tr id="row21392484"><td class="cellrowborder" valign="top" width="30.15698430156984%" headers="mcps1.2.4.1.1 "><p id="p55069611"><a name="p55069611"></a><a name="p55069611"></a>hostname</p>
</td>
<td class="cellrowborder" valign="top" width="30.046995300469952%" headers="mcps1.2.4.1.2 "><p id="p31453527"><a name="p31453527"></a><a name="p31453527"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p64707792"><a name="p64707792"></a><a name="p64707792"></a>Specifies the domain name.</p>
</td>
</tr>
<tr id="row45499221"><td class="cellrowborder" valign="top" width="30.15698430156984%" headers="mcps1.2.4.1.1 "><p id="p61558251"><a name="p61558251"></a><a name="p61558251"></a>path</p>
</td>
<td class="cellrowborder" valign="top" width="30.046995300469952%" headers="mcps1.2.4.1.2 "><p id="p20162434"><a name="p20162434"></a><a name="p20162434"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p22544449"><a name="p22544449"></a><a name="p22544449"></a>Specifies the URL protected by the web tamper protection rule, excluding a domain name.</p>
</td>
</tr>
<tr id="row1573456"><td class="cellrowborder" valign="top" width="30.15698430156984%" headers="mcps1.2.4.1.1 "><p id="p60341087"><a name="p60341087"></a><a name="p60341087"></a>timestamp</p>
</td>
<td class="cellrowborder" valign="top" width="30.046995300469952%" headers="mcps1.2.4.1.2 "><p id="p55789867"><a name="p55789867"></a><a name="p55789867"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p22685339"><a name="p22685339"></a><a name="p22685339"></a>Specifies the time when the cache is refreshed.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section19676101712612"></a>

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

## Status Code<a name="section33086646"></a>

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

