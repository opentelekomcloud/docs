# Adding a False Alarm Masking Rule<a name="EN-US_TOPIC_0193631119"></a>

## Function Description<a name="section37846565"></a>

This API is used to add a false alarm masking rule.

## URI<a name="section5074769"></a>

-   URI format

    POST  /v1/\{project\_id\}/waf/policy/\{policy\_id\}/ignore

-   Parameter description

    **Table  1**  Path parameters

    <a name="table26015259"></a>
    <table><thead align="left"><tr id="row11776346"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p14359950"><a name="p14359950"></a><a name="p14359950"></a><strong id="b19215190123816"><a name="b19215190123816"></a><a name="b19215190123816"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.2"><p id="p22305295"><a name="p22305295"></a><a name="p22305295"></a><strong id="b1643918153819"><a name="b1643918153819"></a><a name="b1643918153819"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.3"><p id="p61898436"><a name="p61898436"></a><a name="p61898436"></a><strong id="b18456193143811"><a name="b18456193143811"></a><a name="b18456193143811"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.5.1.4"><p id="p47717397"><a name="p47717397"></a><a name="p47717397"></a><strong id="b29566515387"><a name="b29566515387"></a><a name="b29566515387"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row39903980"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p10996910"><a name="p10996910"></a><a name="p10996910"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p18334533"><a name="p18334533"></a><a name="p18334533"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p8702233"><a name="p8702233"></a><a name="p8702233"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p33792273"><a name="p33792273"></a><a name="p33792273"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row35695006"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p5614408"><a name="p5614408"></a><a name="p5614408"></a>policy_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p52113931"><a name="p52113931"></a><a name="p52113931"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p60478862"><a name="p60478862"></a><a name="p60478862"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p66949625"><a name="p66949625"></a><a name="p66949625"></a>Specifies the policy ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section45672928"></a>

Request parameters

**Table  2**  Parameter description

<a name="table28978345"></a>
<table><thead align="left"><tr id="row42969978"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p58016212"><a name="p58016212"></a><a name="p58016212"></a><strong id="b101746308388"><a name="b101746308388"></a><a name="b101746308388"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.2"><p id="p1692722"><a name="p1692722"></a><a name="p1692722"></a><strong id="b3592131163820"><a name="b3592131163820"></a><a name="b3592131163820"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.2982701729827%" id="mcps1.2.5.1.3"><p id="p2892797"><a name="p2892797"></a><a name="p2892797"></a><strong id="b142240343383"><a name="b142240343383"></a><a name="b142240343383"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.84601539846015%" id="mcps1.2.5.1.4"><p id="p32989980"><a name="p32989980"></a><a name="p32989980"></a><strong id="b12581335133814"><a name="b12581335133814"></a><a name="b12581335133814"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row54942712"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p21174648"><a name="p21174648"></a><a name="p21174648"></a>path</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p37424900"><a name="p37424900"></a><a name="p37424900"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.2982701729827%" headers="mcps1.2.5.1.3 "><p id="p11518085"><a name="p11518085"></a><a name="p11518085"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.84601539846015%" headers="mcps1.2.5.1.4 "><p id="p60549731"><a name="p60549731"></a><a name="p60549731"></a>Specifies a misreported URL excluding a domain name.</p>
</td>
</tr>
<tr id="row8076672"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p50230708"><a name="p50230708"></a><a name="p50230708"></a>event_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p42155511"><a name="p42155511"></a><a name="p42155511"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.2982701729827%" headers="mcps1.2.5.1.3 "><p id="p59153268"><a name="p59153268"></a><a name="p59153268"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.84601539846015%" headers="mcps1.2.5.1.4 "><p id="p26685393"><a name="p26685393"></a><a name="p26685393"></a>Specifies the event ID.</p>
<p id="p167454859433"><a name="p167454859433"></a><a name="p167454859433"></a>ID of a misreported event in <strong id="b16330640781"><a name="b16330640781"></a><a name="b16330640781"></a>Events</strong> whose type is not <strong id="b193384406816"><a name="b193384406816"></a><a name="b193384406816"></a>Custom</strong>. Click <strong id="b6704827144719"><a name="b6704827144719"></a><a name="b6704827144719"></a>Handle False Alarm</strong> in the row containing the attack event to obtain the event ID.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section8403169"></a>

Response parameters

**Table  3**  Parameter description

<a name="table55078859"></a>
<table><thead align="left"><tr id="row22625886"><th class="cellrowborder" valign="top" width="33.506649335066484%" id="mcps1.2.4.1.1"><p id="p20757491"><a name="p20757491"></a><a name="p20757491"></a><strong id="b1222213115395"><a name="b1222213115395"></a><a name="b1222213115395"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26.697330266973296%" id="mcps1.2.4.1.2"><p id="p3635196"><a name="p3635196"></a><a name="p3635196"></a><strong id="b10994424392"><a name="b10994424392"></a><a name="b10994424392"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.4.1.3"><p id="p26015458"><a name="p26015458"></a><a name="p26015458"></a><strong id="b415814543911"><a name="b415814543911"></a><a name="b415814543911"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row32812531"><td class="cellrowborder" valign="top" width="33.506649335066484%" headers="mcps1.2.4.1.1 "><p id="p40569326"><a name="p40569326"></a><a name="p40569326"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="26.697330266973296%" headers="mcps1.2.4.1.2 "><p id="p64889978"><a name="p64889978"></a><a name="p64889978"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p21596862"><a name="p21596862"></a><a name="p21596862"></a>Specifies the ID of a false alarm masking rule.</p>
</td>
</tr>
<tr id="row60154037"><td class="cellrowborder" valign="top" width="33.506649335066484%" headers="mcps1.2.4.1.1 "><p id="p40638849"><a name="p40638849"></a><a name="p40638849"></a>policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="26.697330266973296%" headers="mcps1.2.4.1.2 "><p id="p3412506"><a name="p3412506"></a><a name="p3412506"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p7977575"><a name="p7977575"></a><a name="p7977575"></a>Specifies the policy ID.</p>
</td>
</tr>
<tr id="row4689317"><td class="cellrowborder" valign="top" width="33.506649335066484%" headers="mcps1.2.4.1.1 "><p id="p44290396"><a name="p44290396"></a><a name="p44290396"></a>path</p>
</td>
<td class="cellrowborder" valign="top" width="26.697330266973296%" headers="mcps1.2.4.1.2 "><p id="p30752315"><a name="p30752315"></a><a name="p30752315"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p6326519018715"><a name="p6326519018715"></a><a name="p6326519018715"></a>Specifies a misreported URL excluding a domain name.</p>
</td>
</tr>
<tr id="row470312574414"><td class="cellrowborder" valign="top" width="33.506649335066484%" headers="mcps1.2.4.1.1 "><p id="p15703157164110"><a name="p15703157164110"></a><a name="p15703157164110"></a>event_id</p>
</td>
<td class="cellrowborder" valign="top" width="26.697330266973296%" headers="mcps1.2.4.1.2 "><p id="p470425715413"><a name="p470425715413"></a><a name="p470425715413"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p107041575411"><a name="p107041575411"></a><a name="p107041575411"></a>Specifies the event ID.</p>
</td>
</tr>
<tr id="row1526717534217"><td class="cellrowborder" valign="top" width="33.506649335066484%" headers="mcps1.2.4.1.1 "><p id="p162671059425"><a name="p162671059425"></a><a name="p162671059425"></a>event_type</p>
</td>
<td class="cellrowborder" valign="top" width="26.697330266973296%" headers="mcps1.2.4.1.2 "><p id="p62682512424"><a name="p62682512424"></a><a name="p62682512424"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p1326819514426"><a name="p1326819514426"></a><a name="p1326819514426"></a>Specifies the event type.</p>
</td>
</tr>
<tr id="row4077641"><td class="cellrowborder" valign="top" width="33.506649335066484%" headers="mcps1.2.4.1.1 "><p id="p61853493"><a name="p61853493"></a><a name="p61853493"></a>timestamp</p>
</td>
<td class="cellrowborder" valign="top" width="26.697330266973296%" headers="mcps1.2.4.1.2 "><p id="p44076997"><a name="p44076997"></a><a name="p44076997"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p12128762"><a name="p12128762"></a><a name="p12128762"></a>Specifies the time when a false alarm masking rule is added.</p>
</td>
</tr>
<tr id="row67156410597"><td class="cellrowborder" valign="top" width="33.506649335066484%" headers="mcps1.2.4.1.1 "><p id="p164965752714"><a name="p164965752714"></a><a name="p164965752714"></a>rule</p>
</td>
<td class="cellrowborder" valign="top" width="26.697330266973296%" headers="mcps1.2.4.1.2 "><p id="p4496177192720"><a name="p4496177192720"></a><a name="p4496177192720"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p849657142719"><a name="p849657142719"></a><a name="p849657142719"></a>Specifies the rule ID, which consists of six digits and cannot be empty.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="section12614079815"></a>

Rule ID  **100001**  is used as example.

-   Request example

    ```
    {
      "path": "/a",
      "event_id": "3737fb122f2140f39292f597ad3b7e9a"
    
    }
    ```


-   Response example

    ```
    {
      "id": "6cdc116040d444f6b3e1bf1dd629f1d0",
      "policy_id": "44d887434169475794b2717438f7fa78",
      "path": "/a",
      "event_id": "3737fb122f2140f39292f597ad3b7e9a",
      "event_type": "xss",
      "rule": "100001",
      "timestamp": 1499817600
    }
    ```


## Status Code<a name="section8519663"></a>

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

