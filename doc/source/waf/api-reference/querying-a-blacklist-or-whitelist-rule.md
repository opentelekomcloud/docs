# Querying a Blacklist or Whitelist Rule<a name="EN-US_TOPIC_0193631125"></a>

## Function Description<a name="section51375086"></a>

This API is used to query a blacklist or whitelist rule.

## URI<a name="section59722591"></a>

-   URI format

    GET  /v1/\{project\_id\}/waf/policy/\{policy\_id\}/whiteblackip/\{whiteblackip\_rule\_id\}

-   Parameter description

    **Table  1**  Path parameters

    <a name="table41741021"></a>
    <table><thead align="left"><tr id="row24986044"><th class="cellrowborder" valign="top" width="30.930000000000003%" id="mcps1.2.5.1.1"><p id="p10603677"><a name="p10603677"></a><a name="p10603677"></a><strong id="b1123458103719"><a name="b1123458103719"></a><a name="b1123458103719"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.62%" id="mcps1.2.5.1.2"><p id="p53591474"><a name="p53591474"></a><a name="p53591474"></a><strong id="b16457185920372"><a name="b16457185920372"></a><a name="b16457185920372"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.430000000000001%" id="mcps1.2.5.1.3"><p id="p45942115"><a name="p45942115"></a><a name="p45942115"></a><strong id="b1160130163816"><a name="b1160130163816"></a><a name="b1160130163816"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="34.02%" id="mcps1.2.5.1.4"><p id="p30323866"><a name="p30323866"></a><a name="p30323866"></a><strong id="b1439641153811"><a name="b1439641153811"></a><a name="b1439641153811"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row40314044"><td class="cellrowborder" valign="top" width="30.930000000000003%" headers="mcps1.2.5.1.1 "><p id="p44212147"><a name="p44212147"></a><a name="p44212147"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.5.1.2 "><p id="p24414183"><a name="p24414183"></a><a name="p24414183"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.430000000000001%" headers="mcps1.2.5.1.3 "><p id="p31391807"><a name="p31391807"></a><a name="p31391807"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.5.1.4 "><p id="p59708452"><a name="p59708452"></a><a name="p59708452"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row505158"><td class="cellrowborder" valign="top" width="30.930000000000003%" headers="mcps1.2.5.1.1 "><p id="p40917865"><a name="p40917865"></a><a name="p40917865"></a>policy_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.5.1.2 "><p id="p26012748"><a name="p26012748"></a><a name="p26012748"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.430000000000001%" headers="mcps1.2.5.1.3 "><p id="p26657815"><a name="p26657815"></a><a name="p26657815"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.5.1.4 "><p id="p11799411"><a name="p11799411"></a><a name="p11799411"></a>Specifies the policy ID.</p>
    </td>
    </tr>
    <tr id="row39085839"><td class="cellrowborder" valign="top" width="30.930000000000003%" headers="mcps1.2.5.1.1 "><p id="p11836358"><a name="p11836358"></a><a name="p11836358"></a>whiteblackip_rule_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.5.1.2 "><p id="p19220962"><a name="p19220962"></a><a name="p19220962"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.430000000000001%" headers="mcps1.2.5.1.3 "><p id="p13394123"><a name="p13394123"></a><a name="p13394123"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.5.1.4 "><p id="p11182184"><a name="p11182184"></a><a name="p11182184"></a>Specifies the ID of a blacklist or whitelist rule.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section632413"></a>

Request parameters

None

## Response<a name="section5691720"></a>

Response parameters

**Table  2**  Parameter description

<a name="table47305227"></a>
<table><thead align="left"><tr id="row17264294"><th class="cellrowborder" valign="top" width="42.85571442855714%" id="mcps1.2.4.1.1"><p id="p56230546"><a name="p56230546"></a><a name="p56230546"></a><strong id="b1191313719381"><a name="b1191313719381"></a><a name="b1191313719381"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.4.1.2"><p id="p58380403"><a name="p58380403"></a><a name="p58380403"></a><strong id="b4198163919383"><a name="b4198163919383"></a><a name="b4198163919383"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.4.1.3"><p id="p31192241"><a name="p31192241"></a><a name="p31192241"></a><strong id="b81314402385"><a name="b81314402385"></a><a name="b81314402385"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row12294718"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p56348114"><a name="p56348114"></a><a name="p56348114"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p794485"><a name="p794485"></a><a name="p794485"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p64353362"><a name="p64353362"></a><a name="p64353362"></a>Specifies the ID of a blacklist or whitelist rule.</p>
</td>
</tr>
<tr id="row42309349"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p4505225"><a name="p4505225"></a><a name="p4505225"></a>policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p29378938"><a name="p29378938"></a><a name="p29378938"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p30883743"><a name="p30883743"></a><a name="p30883743"></a>Specifies the policy ID.</p>
</td>
</tr>
<tr id="row9518232"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p32779367"><a name="p32779367"></a><a name="p32779367"></a>addr</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p37883103"><a name="p37883103"></a><a name="p37883103"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p48632487"><a name="p48632487"></a><a name="p48632487"></a>Specifies the public IP address or range (IP address and subnet mask). For example, <em id="i20748919102619"><a name="i20748919102619"></a><a name="i20748919102619"></a>X.X.</em><strong id="b1074819197262"><a name="b1074819197262"></a><a name="b1074819197262"></a>0.125</strong> or <em id="i8764131962612"><a name="i8764131962612"></a><a name="i8764131962612"></a>X.X.</em><strong id="b1076416198267"><a name="b1076416198267"></a><a name="b1076416198267"></a>6.0/24</strong>.</p>
</td>
</tr>
<tr id="row35039200"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p19602980"><a name="p19602980"></a><a name="p19602980"></a>white</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p44337548"><a name="p44337548"></a><a name="p44337548"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p131673177539"><a name="p131673177539"></a><a name="p131673177539"></a>Specifies the IP address type.</p>
<a name="ul3374102111535"></a><a name="ul3374102111535"></a><ul id="ul3374102111535"><li><strong id="b8654163317459"><a name="b8654163317459"></a><a name="b8654163317459"></a>1</strong>: <strong id="b2655103318450"><a name="b2655103318450"></a><a name="b2655103318450"></a>Whitelist</strong></li><li><strong id="b221293910458"><a name="b221293910458"></a><a name="b221293910458"></a>0</strong>: <strong id="b0213113904518"><a name="b0213113904518"></a><a name="b0213113904518"></a>Blacklist</strong></li></ul>
</td>
</tr>
<tr id="row42709387"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p36908350"><a name="p36908350"></a><a name="p36908350"></a>timestamp</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p36786353"><a name="p36786353"></a><a name="p36786353"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p26904588"><a name="p26904588"></a><a name="p26904588"></a>Specifies the time when a blacklist or whitelist rule is added.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section1151111284618"></a>

_X.X._**0.125**  is used as an example.

Response example

```
{
  "id": "44d887434169475794b2717438f7fa78",
  "policy_id": "ertr45c0f96784ec8abd8ba61a98064ef",
  "addr": "X.X.0.125",
  "white": 0
  "timestamp": 1499817600
}
```

## Status Code<a name="section51225481"></a>

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

