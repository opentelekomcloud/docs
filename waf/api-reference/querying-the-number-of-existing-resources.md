# Querying the Number of Existing Resources<a name="EN-US_TOPIC_0193631138"></a>

## Function Description<a name="section34155517"></a>

This API is used to query the number of existing resources of a user.

## URI<a name="section38964204"></a>

-   URI format

    GET  /v1/\{project\_id\}/waf/bundle/usage/\{resource\_type\}

-   Parameter description

    **Table  1**  Path parameters

    <a name="table1039446101818"></a>
    <table><thead align="left"><tr id="row133984613186"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p839346151813"><a name="p839346151813"></a><a name="p839346151813"></a><strong id="b4404192153716"><a name="b4404192153716"></a><a name="b4404192153716"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.2"><p id="p939114618181"><a name="p939114618181"></a><a name="p939114618181"></a><strong id="b16442112219376"><a name="b16442112219376"></a><a name="b16442112219376"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.3"><p id="p173994620185"><a name="p173994620185"></a><a name="p173994620185"></a><strong id="b1273215232374"><a name="b1273215232374"></a><a name="b1273215232374"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.5.1.4"><p id="p939184615184"><a name="p939184615184"></a><a name="p939184615184"></a><strong id="b47481324153713"><a name="b47481324153713"></a><a name="b47481324153713"></a>Description</strong></p>
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
    <tr id="row6706181910168"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p970043120256"><a name="p970043120256"></a><a name="p970043120256"></a>resource_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p8699203112517"><a name="p8699203112517"></a><a name="p8699203112517"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p2699103110258"><a name="p2699103110258"></a><a name="p2699103110258"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p21617533"><a name="p21617533"></a><a name="p21617533"></a>Specifies the resource type. The options are <span class="parmvalue" id="parmvalue2446131591919"><a name="parmvalue2446131591919"></a><a name="parmvalue2446131591919"></a><b>instance</b></span>, <span class="parmvalue" id="parmvalue1975716186197"><a name="parmvalue1975716186197"></a><a name="parmvalue1975716186197"></a><b>policy</b></span>, and <span class="parmvalue" id="parmvalue16323162491917"><a name="parmvalue16323162491917"></a><a name="parmvalue16323162491917"></a><b>certificate</b></span>.</p>
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
<table><thead align="left"><tr id="row48503826"><th class="cellrowborder" valign="top" width="24.490000000000002%" id="mcps1.2.4.1.1"><p id="p36495809"><a name="p36495809"></a><a name="p36495809"></a><strong id="b884261318381"><a name="b884261318381"></a><a name="b884261318381"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.349999999999998%" id="mcps1.2.4.1.2"><p id="p3370541"><a name="p3370541"></a><a name="p3370541"></a><strong id="b7170215153817"><a name="b7170215153817"></a><a name="b7170215153817"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="58.160000000000004%" id="mcps1.2.4.1.3"><p id="p4578365"><a name="p4578365"></a><a name="p4578365"></a><strong id="b149601015143813"><a name="b149601015143813"></a><a name="b149601015143813"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row41205286"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p49293864"><a name="p49293864"></a><a name="p49293864"></a>count</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p33380034"><a name="p33380034"></a><a name="p33380034"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p19428253"><a name="p19428253"></a><a name="p19428253"></a>Specifies the number of existing resources.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section6628133643318"></a>

The following shows the response if the number of uploaded certificates is queried.

Response example

```
{
   "count": 2
}
```

## Status Code<a name="section17855279"></a>

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

