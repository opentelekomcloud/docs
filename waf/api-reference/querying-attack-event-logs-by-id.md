# Querying Attack Event Logs by ID<a name="EN-US_TOPIC_0193631154"></a>

## Function Description<a name="section62974086"></a>

This API is used to query attack event logs by ID.

## URI<a name="section29895862"></a>

-   URI format

    GET  /v1/\{project\_id\}/waf/event/\{event\_id\}

-   Parameter description

    **Table  1**  Path parameters

    <a name="table35852760"></a>
    <table><thead align="left"><tr id="row31235826"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p47073998"><a name="p47073998"></a><a name="p47073998"></a><strong id="b846802116410"><a name="b846802116410"></a><a name="b846802116410"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.2"><p id="p54897527"><a name="p54897527"></a><a name="p54897527"></a><strong id="b8415102415419"><a name="b8415102415419"></a><a name="b8415102415419"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.3"><p id="p17514708"><a name="p17514708"></a><a name="p17514708"></a><strong id="b13160112615415"><a name="b13160112615415"></a><a name="b13160112615415"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.5.1.4"><p id="p9405262"><a name="p9405262"></a><a name="p9405262"></a><strong id="b142591284412"><a name="b142591284412"></a><a name="b142591284412"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row23628748"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p34880439"><a name="p34880439"></a><a name="p34880439"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p6743286"><a name="p6743286"></a><a name="p6743286"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p9335282"><a name="p9335282"></a><a name="p9335282"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p17960338"><a name="p17960338"></a><a name="p17960338"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row27425315"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p6858037"><a name="p6858037"></a><a name="p6858037"></a>event_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p18630111"><a name="p18630111"></a><a name="p18630111"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p32644042"><a name="p32644042"></a><a name="p32644042"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p26921758"><a name="p26921758"></a><a name="p26921758"></a>Specifies the event ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section627304"></a>

Request parameters

None

## Response<a name="section5645742"></a>

Response parameters

**Table  2**  Parameter description

<a name="table51758747"></a>
<table><thead align="left"><tr id="row5012580"><th class="cellrowborder" valign="top" width="32.35676432356764%" id="mcps1.2.4.1.1"><p id="p3365875"><a name="p3365875"></a><a name="p3365875"></a><strong id="b19031448174113"><a name="b19031448174113"></a><a name="b19031448174113"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.84721527847215%" id="mcps1.2.4.1.2"><p id="p4200491"><a name="p4200491"></a><a name="p4200491"></a><strong id="b2220150184117"><a name="b2220150184117"></a><a name="b2220150184117"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.4.1.3"><p id="p4695475"><a name="p4695475"></a><a name="p4695475"></a><strong id="b796765164111"><a name="b796765164111"></a><a name="b796765164111"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row42259276"><td class="cellrowborder" valign="top" width="32.35676432356764%" headers="mcps1.2.4.1.1 "><p id="p449360"><a name="p449360"></a><a name="p449360"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="27.84721527847215%" headers="mcps1.2.4.1.2 "><p id="p36398200"><a name="p36398200"></a><a name="p36398200"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p62573101"><a name="p62573101"></a><a name="p62573101"></a>Specifies the event ID.</p>
</td>
</tr>
<tr id="row26286999"><td class="cellrowborder" valign="top" width="32.35676432356764%" headers="mcps1.2.4.1.1 "><p id="p48872202"><a name="p48872202"></a><a name="p48872202"></a>time</p>
</td>
<td class="cellrowborder" valign="top" width="27.84721527847215%" headers="mcps1.2.4.1.2 "><p id="p66334269"><a name="p66334269"></a><a name="p66334269"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p4366680"><a name="p4366680"></a><a name="p4366680"></a>Specifies the attack time since Unix Epoch in milliseconds.</p>
</td>
</tr>
<tr id="row39300124"><td class="cellrowborder" valign="top" width="32.35676432356764%" headers="mcps1.2.4.1.1 "><p id="p29193512"><a name="p29193512"></a><a name="p29193512"></a>policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="27.84721527847215%" headers="mcps1.2.4.1.2 "><p id="p15864239"><a name="p15864239"></a><a name="p15864239"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p9935003"><a name="p9935003"></a><a name="p9935003"></a>Specifies the policy ID.</p>
</td>
</tr>
<tr id="row22306171"><td class="cellrowborder" valign="top" width="32.35676432356764%" headers="mcps1.2.4.1.1 "><p id="p61969401"><a name="p61969401"></a><a name="p61969401"></a>sip</p>
</td>
<td class="cellrowborder" valign="top" width="27.84721527847215%" headers="mcps1.2.4.1.2 "><p id="p53465551"><a name="p53465551"></a><a name="p53465551"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p35742374"><a name="p35742374"></a><a name="p35742374"></a>Specifies an attack source IP address.</p>
</td>
</tr>
<tr id="row53245913"><td class="cellrowborder" valign="top" width="32.35676432356764%" headers="mcps1.2.4.1.1 "><p id="p17951700"><a name="p17951700"></a><a name="p17951700"></a>host</p>
</td>
<td class="cellrowborder" valign="top" width="27.84721527847215%" headers="mcps1.2.4.1.2 "><p id="p44801571"><a name="p44801571"></a><a name="p44801571"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p5048623"><a name="p5048623"></a><a name="p5048623"></a>Specifies an attacked domain name.</p>
</td>
</tr>
<tr id="row1175675116105"><td class="cellrowborder" valign="top" width="32.35676432356764%" headers="mcps1.2.4.1.1 "><p id="p17757165115102"><a name="p17757165115102"></a><a name="p17757165115102"></a>host_id</p>
</td>
<td class="cellrowborder" valign="top" width="27.84721527847215%" headers="mcps1.2.4.1.2 "><p id="p207571151201017"><a name="p207571151201017"></a><a name="p207571151201017"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p1757185115105"><a name="p1757185115105"></a><a name="p1757185115105"></a>Specifies a domain name ID.</p>
</td>
</tr>
<tr id="row45437607"><td class="cellrowborder" valign="top" width="32.35676432356764%" headers="mcps1.2.4.1.1 "><p id="p56567512"><a name="p56567512"></a><a name="p56567512"></a>url</p>
</td>
<td class="cellrowborder" valign="top" width="27.84721527847215%" headers="mcps1.2.4.1.2 "><p id="p18565754"><a name="p18565754"></a><a name="p18565754"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p27431092"><a name="p27431092"></a><a name="p27431092"></a>Specifies the attacked URL, excluding a domain name.</p>
</td>
</tr>
<tr id="row45553242"><td class="cellrowborder" valign="top" width="32.35676432356764%" headers="mcps1.2.4.1.1 "><p id="p65933996"><a name="p65933996"></a><a name="p65933996"></a>attack</p>
</td>
<td class="cellrowborder" valign="top" width="27.84721527847215%" headers="mcps1.2.4.1.2 "><p id="p39053483"><a name="p39053483"></a><a name="p39053483"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p9215550"><a name="p9215550"></a><a name="p9215550"></a>Specifies the attack type.</p>
</td>
</tr>
<tr id="row15831091"><td class="cellrowborder" valign="top" width="32.35676432356764%" headers="mcps1.2.4.1.1 "><p id="p7249984"><a name="p7249984"></a><a name="p7249984"></a>rule</p>
</td>
<td class="cellrowborder" valign="top" width="27.84721527847215%" headers="mcps1.2.4.1.2 "><p id="p50377813"><a name="p50377813"></a><a name="p50377813"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p54071067"><a name="p54071067"></a><a name="p54071067"></a>Specifies the ID of the matched rule.</p>
</td>
</tr>
<tr id="row16877560"><td class="cellrowborder" valign="top" width="32.35676432356764%" headers="mcps1.2.4.1.1 "><p id="p24905097"><a name="p24905097"></a><a name="p24905097"></a>payload</p>
</td>
<td class="cellrowborder" valign="top" width="27.84721527847215%" headers="mcps1.2.4.1.2 "><p id="p4047008"><a name="p4047008"></a><a name="p4047008"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p59372194"><a name="p59372194"></a><a name="p59372194"></a>Specifies the hit load.</p>
</td>
</tr>
<tr id="row64587704"><td class="cellrowborder" valign="top" width="32.35676432356764%" headers="mcps1.2.4.1.1 "><p id="p64221512"><a name="p64221512"></a><a name="p64221512"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="27.84721527847215%" headers="mcps1.2.4.1.2 "><p id="p34559993"><a name="p34559993"></a><a name="p34559993"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p47896050"><a name="p47896050"></a><a name="p47896050"></a>Specifies the protective action.</p>
<a name="ul796714441001"></a><a name="ul796714441001"></a><ul id="ul796714441001"><li><strong id="b7284114331315"><a name="b7284114331315"></a><a name="b7284114331315"></a>Block</strong>: WAF blocks and logs detected attacks.</li><li><span class="parmvalue" id="parmvalue9749147101319"><a name="parmvalue9749147101319"></a><a name="parmvalue9749147101319"></a><b>Log only</b></span>: WAF logs detected attacks only.</li><li><strong id="b79771050194118"><a name="b79771050194118"></a><a name="b79771050194118"></a>Allow</strong>: WAF allows the requests that meet the specified conditions.</li><li><strong id="b1481976612"><a name="b1481976612"></a><a name="b1481976612"></a>Verification code</strong>: A verification code is displayed when the number of requests reaches the maximum limit in a CC attack protection rule. Upon completing the verification, you are no longer restricted by the maximum number of requests allowed.</li><li><strong id="b1774113218149"><a name="b1774113218149"></a><a name="b1774113218149"></a>Filter</strong>: WAF implements data masking.</li><li><span class="parmvalue" id="parmvalue1589162882312"><a name="parmvalue1589162882312"></a><a name="parmvalue1589162882312"></a><b>Mismatch</b></span>: The cached web page in the WAF engine does not match the original web page.</li></ul>
</td>
</tr>
<tr id="row17870339163918"><td class="cellrowborder" valign="top" width="32.35676432356764%" headers="mcps1.2.4.1.1 "><p id="p5870123917396"><a name="p5870123917396"></a><a name="p5870123917396"></a>payload_location</p>
</td>
<td class="cellrowborder" valign="top" width="27.84721527847215%" headers="mcps1.2.4.1.2 "><p id="p13870439123910"><a name="p13870439123910"></a><a name="p13870439123910"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p1687016394393"><a name="p1687016394393"></a><a name="p1687016394393"></a>Specifies the location in the request packet where the attack occurs. The options are as follows: <strong id="b958115414617"><a name="b958115414617"></a><a name="b958115414617"></a>body</strong>, <strong id="b75831354860"><a name="b75831354860"></a><a name="b75831354860"></a>url</strong>, <strong id="b65841854062"><a name="b65841854062"></a><a name="b65841854062"></a>params</strong>, and <strong id="b358405413611"><a name="b358405413611"></a><a name="b358405413611"></a>header</strong>.</p>
</td>
</tr>
<tr id="row19854951193920"><td class="cellrowborder" valign="top" width="32.35676432356764%" headers="mcps1.2.4.1.1 "><p id="p108696500394"><a name="p108696500394"></a><a name="p108696500394"></a>request_line</p>
</td>
<td class="cellrowborder" valign="top" width="27.84721527847215%" headers="mcps1.2.4.1.2 "><p id="p58701950173910"><a name="p58701950173910"></a><a name="p58701950173910"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p1387295083914"><a name="p1387295083914"></a><a name="p1387295083914"></a>Specifies the attack request method.</p>
</td>
</tr>
<tr id="row19266654123915"><td class="cellrowborder" valign="top" width="32.35676432356764%" headers="mcps1.2.4.1.1 "><p id="p18555205333912"><a name="p18555205333912"></a><a name="p18555205333912"></a>headers</p>
</td>
<td class="cellrowborder" valign="top" width="27.84721527847215%" headers="mcps1.2.4.1.2 "><p id="p12556353143912"><a name="p12556353143912"></a><a name="p12556353143912"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p15557105373911"><a name="p15557105373911"></a><a name="p15557105373911"></a>Specifies the attack request header.</p>
</td>
</tr>
<tr id="row19620115918423"><td class="cellrowborder" valign="top" width="32.35676432356764%" headers="mcps1.2.4.1.1 "><p id="p86201659124213"><a name="p86201659124213"></a><a name="p86201659124213"></a>cookie</p>
</td>
<td class="cellrowborder" valign="top" width="27.84721527847215%" headers="mcps1.2.4.1.2 "><p id="p136205593429"><a name="p136205593429"></a><a name="p136205593429"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p76201459124218"><a name="p76201459124218"></a><a name="p76201459124218"></a>Specifies the cookie.</p>
</td>
</tr>
<tr id="row11807555434"><td class="cellrowborder" valign="top" width="32.35676432356764%" headers="mcps1.2.4.1.1 "><p id="p868012414320"><a name="p868012414320"></a><a name="p868012414320"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="27.84721527847215%" headers="mcps1.2.4.1.2 "><p id="p6683646437"><a name="p6683646437"></a><a name="p6683646437"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p568317415433"><a name="p568317415433"></a><a name="p568317415433"></a>Specifies the body of an attack request.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section141961441151113"></a>

Event ID  **0000-0000-0000-13-56ef71f5745764348192f844658dd144**  is used as an example.

Response example

```
{
     "id": "0000-0000-0000-13-56ef71f5745764348192f844658dd144",
      "time": 1499817600,
      "policy_id": "xxx",
      "sip": "X.X.1.1",
      "host": "a.com",
      "host_id": "123",
      "url": "/login",
      "attack": "sqli",
      "rule": "20001",
      "payload": "1 or 1=1",
      "action": "block",
      "payload_location": "params",
      "request_line": "GET / ",
      "headers": {
        "Connection": "keep-alive",
        "User-Agent": "curl"
      },
      "cookie": "sid=123; uid=456",
      "body": "user=admin&pass=abc123"
    }

```

## Status Code<a name="section50811679"></a>

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

