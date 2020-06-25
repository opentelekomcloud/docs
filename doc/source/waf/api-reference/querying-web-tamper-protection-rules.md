# Querying Web Tamper Protection Rules<a name="EN-US_TOPIC_0193631112"></a>

## Function Description<a name="section53061583"></a>

This API is used to query all web tamper protection rules in a policy.

## URI<a name="section7792206"></a>

-   URI format

    GET  /v1/\{project\_id\}/waf/policy/\{policy\_id\}/antitamper?offset=\{offset\}&&limit=\{limit\}

-   Parameter description

    **Table  1**  Path parameters

    <a name="table18800076"></a>
    <table><thead align="left"><tr id="row9898845"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p63609005"><a name="p63609005"></a><a name="p63609005"></a><strong id="b9525174814268"><a name="b9525174814268"></a><a name="b9525174814268"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.2"><p id="p52055798"><a name="p52055798"></a><a name="p52055798"></a><strong id="b1285017508262"><a name="b1285017508262"></a><a name="b1285017508262"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.3"><p id="p55770079"><a name="p55770079"></a><a name="p55770079"></a><strong id="b1768485262618"><a name="b1768485262618"></a><a name="b1768485262618"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.5.1.4"><p id="p21082512"><a name="p21082512"></a><a name="p21082512"></a><strong id="b187961455132613"><a name="b187961455132613"></a><a name="b187961455132613"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row29961906"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p10995308"><a name="p10995308"></a><a name="p10995308"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p18204775"><a name="p18204775"></a><a name="p18204775"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p65300683"><a name="p65300683"></a><a name="p65300683"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p54863934"><a name="p54863934"></a><a name="p54863934"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row24013366"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p66034502"><a name="p66034502"></a><a name="p66034502"></a>policy_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p47194426"><a name="p47194426"></a><a name="p47194426"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p64652155"><a name="p64652155"></a><a name="p64652155"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p2333168"><a name="p2333168"></a><a name="p2333168"></a>Specifies the policy ID.</p>
    </td>
    </tr>
    <tr id="row20998513"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p12721202062818"><a name="p12721202062818"></a><a name="p12721202062818"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p63861336"><a name="p63861336"></a><a name="p63861336"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p5385712"><a name="p5385712"></a><a name="p5385712"></a>Long</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p21617533"><a name="p21617533"></a><a name="p21617533"></a>Specifies the number of returned pages. Its value ranges from <strong id="b1624044616344"><a name="b1624044616344"></a><a name="b1624044616344"></a>0</strong> to <strong id="b162405463348"><a name="b162405463348"></a><a name="b162405463348"></a>65535</strong>. The default value is <strong id="b18240174613420"><a name="b18240174613420"></a><a name="b18240174613420"></a>0</strong>.</p>
    </td>
    </tr>
    <tr id="row33870085"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p74511024142814"><a name="p74511024142814"></a><a name="p74511024142814"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p24182274"><a name="p24182274"></a><a name="p24182274"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p12607163"><a name="p12607163"></a><a name="p12607163"></a>Long</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p25357967"><a name="p25357967"></a><a name="p25357967"></a>Specifies the maximum number of records displayed on each page. Its value ranges from <strong id="b11630124723418"><a name="b11630124723418"></a><a name="b11630124723418"></a>0</strong> to <strong id="b963015474342"><a name="b963015474342"></a><a name="b963015474342"></a>50</strong>. The default value is <strong id="b263074715344"><a name="b263074715344"></a><a name="b263074715344"></a>10</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section3020994"></a>

Request parameters

None

## Response<a name="section27188948"></a>

Response parameters

**Table  2**  Parameter description

<a name="table13387725"></a>
<table><thead align="left"><tr id="row38469033"><th class="cellrowborder" valign="top" width="42.85571442855714%" id="mcps1.2.4.1.1"><p id="p28983974"><a name="p28983974"></a><a name="p28983974"></a><strong id="b2794194512276"><a name="b2794194512276"></a><a name="b2794194512276"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.4.1.2"><p id="p66000576"><a name="p66000576"></a><a name="p66000576"></a><strong id="b2542947142712"><a name="b2542947142712"></a><a name="b2542947142712"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.4.1.3"><p id="p44446430"><a name="p44446430"></a><a name="p44446430"></a><strong id="b49206498276"><a name="b49206498276"></a><a name="b49206498276"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row64473554"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p54975410"><a name="p54975410"></a><a name="p54975410"></a>total</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p23823243"><a name="p23823243"></a><a name="p23823243"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p50634500"><a name="p50634500"></a><a name="p50634500"></a>Specifies the total number of web tamper protection rules in a policy.</p>
</td>
</tr>
<tr id="row53057316"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p2675312"><a name="p2675312"></a><a name="p2675312"></a>items</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p15373745"><a name="p15373745"></a><a name="p15373745"></a><a href="#table16394183011019">Table 3</a></p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p37313871"><a name="p37313871"></a><a name="p37313871"></a>Specifies the web tamper protection rule objects.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **items**

<a name="table16394183011019"></a>
<table><thead align="left"><tr id="row939613301015"><th class="cellrowborder" valign="top" width="33.086691330866906%" id="mcps1.2.4.1.1"><p id="p039873016013"><a name="p039873016013"></a><a name="p039873016013"></a><strong id="b9419922172710"><a name="b9419922172710"></a><a name="b9419922172710"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.117288271172878%" id="mcps1.2.4.1.2"><p id="p183997301406"><a name="p183997301406"></a><a name="p183997301406"></a><strong id="b2055450730"><a name="b2055450730"></a><a name="b2055450730"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.4.1.3"><p id="p839973013010"><a name="p839973013010"></a><a name="p839973013010"></a><strong id="b395852515272"><a name="b395852515272"></a><a name="b395852515272"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row45300584611"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p75425576615"><a name="p75425576615"></a><a name="p75425576615"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p45421357765"><a name="p45421357765"></a><a name="p45421357765"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p115451357860"><a name="p115451357860"></a><a name="p115451357860"></a>Specifies the ID of a web tamper protection rule.</p>
</td>
</tr>
<tr id="row13530558966"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p654816571067"><a name="p654816571067"></a><a name="p654816571067"></a>policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p19549165715612"><a name="p19549165715612"></a><a name="p19549165715612"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p155111573613"><a name="p155111573613"></a><a name="p155111573613"></a>Specifies the ID of the policy to which the rule belongs.</p>
</td>
</tr>
<tr id="row8529258363"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p35531557162"><a name="p35531557162"></a><a name="p35531557162"></a>hostname</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p35543571865"><a name="p35543571865"></a><a name="p35543571865"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p185553571616"><a name="p185553571616"></a><a name="p185553571616"></a>Specifies the domain name.</p>
</td>
</tr>
<tr id="row9529135818611"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p655913571369"><a name="p655913571369"></a><a name="p655913571369"></a>path</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p3561657461"><a name="p3561657461"></a><a name="p3561657461"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p1256110577616"><a name="p1256110577616"></a><a name="p1256110577616"></a>Specifies the URL protected by the web tamper protection rule, excluding a domain name.</p>
</td>
</tr>
<tr id="row1552814587613"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p2563457866"><a name="p2563457866"></a><a name="p2563457866"></a>timestamp</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p12565205716611"><a name="p12565205716611"></a><a name="p12565205716611"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p55678578612"><a name="p55678578612"></a><a name="p55678578612"></a>Specifies the time when the cache is refreshed.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section13437554728"></a>

**total**  with a value of  **2**  is used as an example.

Response example

```
{
  "total": 2,
  "items": [{
      "id": "3a9b5c0f96784ec8abd8ba61a98064ef",
      "policy_id": "yuc0e55865544d1f8c95cf71df108c6b",
      "hostname": "www.aaa.com",
      "path": "/a",
      "timestamp": 1499817600
    }, {
      "id": "44d887434169475794b2717438f7fa78",
      "policy_id": "yuc0e55865544d1f8c95cf71df108c6b",
      "hostname": "www.bbb.com",
      "path": "/b",
      "timestamp": 1499817600
    }
  ]
}
```

## Status Code<a name="section43373941"></a>

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

