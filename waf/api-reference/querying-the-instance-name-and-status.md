# Querying the Instance Name and Status<a name="EN-US_TOPIC_0193631173"></a>

## Function Description<a name="section17925194784510"></a>

This API is used to query the name and status of the instance for interconnecting with Cloud Eye.

## URI<a name="section15676185813475"></a>

-   URI format

    GET /v1/\{project\_id\}/waf/instance/\{instance\_id\}/metrics


-   Parameter description

    **Table  1**  Path parameters

    <a name="table1048819319483"></a>
    <table><thead align="left"><tr id="row353643114813"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p18536831104815"><a name="p18536831104815"></a><a name="p18536831104815"></a><strong id="b38451298118"><a name="b38451298118"></a><a name="b38451298118"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p4536173114815"><a name="p4536173114815"></a><a name="p4536173114815"></a><strong id="b166518108112"><a name="b166518108112"></a><a name="b166518108112"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p185364319489"><a name="p185364319489"></a><a name="p185364319489"></a><strong id="b12744911915"><a name="b12744911915"></a><a name="b12744911915"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p8536103112487"><a name="p8536103112487"></a><a name="p8536103112487"></a><strong id="b145901171010"><a name="b145901171010"></a><a name="b145901171010"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1953633115481"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p11536133110481"><a name="p11536133110481"></a><a name="p11536133110481"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p2536183144817"><a name="p2536183144817"></a><a name="p2536183144817"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p1953663124812"><a name="p1953663124812"></a><a name="p1953663124812"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p11537153117487"><a name="p11537153117487"></a><a name="p11537153117487"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row1537331104812"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1753783118487"><a name="p1753783118487"></a><a name="p1753783118487"></a>instance_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p19537631154812"><a name="p19537631154812"></a><a name="p19537631154812"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p10537103174812"><a name="p10537103174812"></a><a name="p10537103174812"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p115371531134814"><a name="p115371531134814"></a><a name="p115371531134814"></a>Specifies the instance ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section138291117497"></a>

Request parameters

None

## Response<a name="section1046935119499"></a>

Response parameters

**Table  2**  Parameter description

<a name="table20232171385015"></a>
<table><thead align="left"><tr id="row12271181316508"><th class="cellrowborder" valign="top" width="33.690000000000005%" id="mcps1.2.4.1.1"><p id="p8271413105017"><a name="p8271413105017"></a><a name="p8271413105017"></a><strong id="b97174217112"><a name="b97174217112"></a><a name="b97174217112"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="41.99%" id="mcps1.2.4.1.2"><p id="p3271121313509"><a name="p3271121313509"></a><a name="p3271121313509"></a><strong id="b1090734212112"><a name="b1090734212112"></a><a name="b1090734212112"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="24.320000000000004%" id="mcps1.2.4.1.3"><p id="p1927181395011"><a name="p1927181395011"></a><a name="p1927181395011"></a><strong id="b37870431213"><a name="b37870431213"></a><a name="b37870431213"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1927111139504"><td class="cellrowborder" valign="top" width="33.690000000000005%" headers="mcps1.2.4.1.1 "><p id="p3271121365015"><a name="p3271121365015"></a><a name="p3271121365015"></a>waf_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="41.99%" headers="mcps1.2.4.1.2 "><p id="p427115134503"><a name="p427115134503"></a><a name="p427115134503"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="24.320000000000004%" headers="mcps1.2.4.1.3 "><p id="p4271013145018"><a name="p4271013145018"></a><a name="p4271013145018"></a>Specifies the identifier of a metric dimension.</p>
</td>
</tr>
<tr id="row027110130503"><td class="cellrowborder" valign="top" width="33.690000000000005%" headers="mcps1.2.4.1.1 "><p id="p12711013205012"><a name="p12711013205012"></a><a name="p12711013205012"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="41.99%" headers="mcps1.2.4.1.2 "><p id="p427118130502"><a name="p427118130502"></a><a name="p427118130502"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="24.320000000000004%" headers="mcps1.2.4.1.3 "><p id="p527161318505"><a name="p527161318505"></a><a name="p527161318505"></a>Specifies the name of a resource instance.</p>
</td>
</tr>
<tr id="row18680145212501"><td class="cellrowborder" valign="top" width="33.690000000000005%" headers="mcps1.2.4.1.1 "><p id="p6521165815011"><a name="p6521165815011"></a><a name="p6521165815011"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="41.99%" headers="mcps1.2.4.1.2 "><p id="p752135816500"><a name="p752135816500"></a><a name="p752135816500"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="24.320000000000004%" headers="mcps1.2.4.1.3 "><p id="p3521205818506"><a name="p3521205818506"></a><a name="p3521205818506"></a>Specifies the status of a resource instance.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section9288151211513"></a>

Response example

```
{
     "waf_instance_id": "dhbvhdfbvdhbasdkjvfhwoow",
     "name": "www.test.com",
     "status": "enable"
}
```

## Status Code<a name="section124031118185219"></a>

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

