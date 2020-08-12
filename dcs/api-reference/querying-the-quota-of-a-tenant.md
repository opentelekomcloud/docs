# Querying the Quota of a Tenant<a name="dcs-api-0312036"></a>

## Function<a name="section164151825713"></a>

This API is used to query the default instance quota and total memory quota of a tenant and the maximum and minimum quotas a tenant can apply for. Different tenants have different quotas in different regions.

## URI<a name="section14354165101817"></a>

GET  /v1.0/\{project\_id\}/quota

[Table 1](#table13653920143919)  describes the parameter.

**Table  1**  Parameter description

<a name="table13653920143919"></a>
<table><thead align="left"><tr id="row13652172011391"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p0652102011396"><a name="p0652102011396"></a><a name="p0652102011396"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p16521202391"><a name="p16521202391"></a><a name="p16521202391"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p765292023914"><a name="p765292023914"></a><a name="p765292023914"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p136521420153919"><a name="p136521420153919"></a><a name="p136521420153919"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row176531320103915"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p2065202017391"><a name="p2065202017391"></a><a name="p2065202017391"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p0653920173910"><a name="p0653920173910"></a><a name="p0653920173910"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p4653020183913"><a name="p4653020183913"></a><a name="p4653020183913"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p96533202399"><a name="p96533202399"></a><a name="p96533202399"></a>Project ID</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section116044010182"></a>

**Request parameters**

None.

**Example request**

None.

## Response<a name="section66414611916"></a>

**Response parameters**

[Table 2](#table114165246391)  describes the response parameters.

**Table  2**  Parameter description

<a name="table114165246391"></a>
<table><thead align="left"><tr id="row104150248391"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p12415924193920"><a name="p12415924193920"></a><a name="p12415924193920"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.2.5.1.2"><p id="p144151224163910"><a name="p144151224163910"></a><a name="p144151224163910"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.3"><p id="p54593291407"><a name="p54593291407"></a><a name="p54593291407"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="38%" id="mcps1.2.5.1.4"><p id="p2415182419396"><a name="p2415182419396"></a><a name="p2415182419396"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row13415324183915"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p441552483916"><a name="p441552483916"></a><a name="p441552483916"></a>quotas</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.2 "><p id="p06451925192319"><a name="p06451925192319"></a><a name="p06451925192319"></a>JSON</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.3 "><p id="p2046020291503"><a name="p2046020291503"></a><a name="p2046020291503"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="38%" headers="mcps1.2.5.1.4 "><p id="p15415102415391"><a name="p15415102415391"></a><a name="p15415102415391"></a>Quota information. For details, see <a href="#table1341618240392">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  quotas parameter description

<a name="table1341618240392"></a>
<table><thead align="left"><tr id="row241652418392"><th class="cellrowborder" valign="top" width="26%" id="mcps1.2.5.1.1"><p id="p0416122417395"><a name="p0416122417395"></a><a name="p0416122417395"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.2.5.1.2"><p id="p8416624203915"><a name="p8416624203915"></a><a name="p8416624203915"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.2.5.1.3"><p id="p1865085215017"><a name="p1865085215017"></a><a name="p1865085215017"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="38%" id="mcps1.2.5.1.4"><p id="p6416152423910"><a name="p6416152423910"></a><a name="p6416152423910"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row134163246394"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.5.1.1 "><p id="p104161424133913"><a name="p104161424133913"></a><a name="p104161424133913"></a>resources</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.2 "><p id="p341642453911"><a name="p341642453911"></a><a name="p341642453911"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.3 "><p id="p765019524010"><a name="p765019524010"></a><a name="p765019524010"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="38%" headers="mcps1.2.5.1.4 "><p id="p124164242391"><a name="p124164242391"></a><a name="p124164242391"></a>List of quotas For details, see <a href="#table164180248392">Table 4</a>.</p>
</td>
</tr>
<tr id="row84207492518"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.5.1.1 "><p id="p44203482511"><a name="p44203482511"></a><a name="p44203482511"></a>resource_user</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.2 "><p id="p17420134112519"><a name="p17420134112519"></a><a name="p17420134112519"></a>JSON</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.3 "><p id="p156511552305"><a name="p156511552305"></a><a name="p156511552305"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="38%" headers="mcps1.2.5.1.4 "><p id="p1242034112513"><a name="p1242034112513"></a><a name="p1242034112513"></a>Information about a resource tenant For details, see <a href="#table1641811248397">Table 5</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4**  resources parameter description

<a name="table164180248392"></a>
<table><thead align="left"><tr id="row84161724193917"><th class="cellrowborder" valign="top" width="24.752475247524753%" id="mcps1.2.4.1.1"><p id="p34161724103916"><a name="p34161724103916"></a><a name="p34161724103916"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="34.65346534653465%" id="mcps1.2.4.1.2"><p id="p24161224173920"><a name="p24161224173920"></a><a name="p24161224173920"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="40.59405940594059%" id="mcps1.2.4.1.3"><p id="p1541632411391"><a name="p1541632411391"></a><a name="p1541632411391"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row94171524133918"><td class="cellrowborder" valign="top" width="24.752475247524753%" headers="mcps1.2.4.1.1 "><p id="p12417824113917"><a name="p12417824113917"></a><a name="p12417824113917"></a>quota</p>
</td>
<td class="cellrowborder" valign="top" width="34.65346534653465%" headers="mcps1.2.4.1.2 "><p id="p641792411399"><a name="p641792411399"></a><a name="p641792411399"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="40.59405940594059%" headers="mcps1.2.4.1.3 "><p id="p18652185613414"><a name="p18652185613414"></a><a name="p18652185613414"></a>Maximum number of instances that can be created and maximum allowed total memory.</p>
</td>
</tr>
<tr id="row441752415393"><td class="cellrowborder" valign="top" width="24.752475247524753%" headers="mcps1.2.4.1.1 "><p id="p341772463919"><a name="p341772463919"></a><a name="p341772463919"></a>used</p>
</td>
<td class="cellrowborder" valign="top" width="34.65346534653465%" headers="mcps1.2.4.1.2 "><p id="p1341722443920"><a name="p1341722443920"></a><a name="p1341722443920"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="40.59405940594059%" headers="mcps1.2.4.1.3 "><p id="p841732473916"><a name="p841732473916"></a><a name="p841732473916"></a>Number of created instances and used memory.</p>
</td>
</tr>
<tr id="row143604574285"><td class="cellrowborder" valign="top" width="24.752475247524753%" headers="mcps1.2.4.1.1 "><p id="p19651145182911"><a name="p19651145182911"></a><a name="p19651145182911"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="34.65346534653465%" headers="mcps1.2.4.1.2 "><p id="p14651125162918"><a name="p14651125162918"></a><a name="p14651125162918"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40.59405940594059%" headers="mcps1.2.4.1.3 "><p id="p1065165202911"><a name="p1065165202911"></a><a name="p1065165202911"></a>Values:</p>
<a name="ul68511652669"></a><a name="ul68511652669"></a><ul id="ul68511652669"><li><strong id="b16686312155213"><a name="b16686312155213"></a><a name="b16686312155213"></a>instances</strong>: indicates the instance quota.</li><li><strong id="b88151814195218"><a name="b88151814195218"></a><a name="b88151814195218"></a>ram</strong>: indicates the memory quota.</li></ul>
</td>
</tr>
<tr id="row1141719245396"><td class="cellrowborder" valign="top" width="24.752475247524753%" headers="mcps1.2.4.1.1 "><p id="p341792416391"><a name="p341792416391"></a><a name="p341792416391"></a>unit</p>
</td>
<td class="cellrowborder" valign="top" width="34.65346534653465%" headers="mcps1.2.4.1.2 "><p id="p441715243393"><a name="p441715243393"></a><a name="p441715243393"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40.59405940594059%" headers="mcps1.2.4.1.3 "><p id="p19709101812711"><a name="p19709101812711"></a><a name="p19709101812711"></a>Resource unit.</p>
<a name="ul171513818816"></a><a name="ul171513818816"></a><ul id="ul171513818816"><li>When <strong id="b8123112911526"><a name="b8123112911526"></a><a name="b8123112911526"></a>type</strong> is set to <strong id="b91247297524"><a name="b91247297524"></a><a name="b91247297524"></a>instance</strong>, no value is returned.</li><li>When <strong id="b20493173112521"><a name="b20493173112521"></a><a name="b20493173112521"></a>type</strong> is set to <strong id="b154941831155211"><a name="b154941831155211"></a><a name="b154941831155211"></a>ram</strong>, <strong id="b64951831125220"><a name="b64951831125220"></a><a name="b64951831125220"></a>GB</strong> is returned.</li></ul>
</td>
</tr>
<tr id="row74177249394"><td class="cellrowborder" valign="top" width="24.752475247524753%" headers="mcps1.2.4.1.1 "><p id="p4417202413911"><a name="p4417202413911"></a><a name="p4417202413911"></a>max</p>
</td>
<td class="cellrowborder" valign="top" width="34.65346534653465%" headers="mcps1.2.4.1.2 "><p id="p134171724193914"><a name="p134171724193914"></a><a name="p134171724193914"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="40.59405940594059%" headers="mcps1.2.4.1.3 "><a name="ul35767124811"></a><a name="ul35767124811"></a><ul id="ul35767124811"><li>Indicates the maximum limit of instance quota when <strong id="b1370753417528"><a name="b1370753417528"></a><a name="b1370753417528"></a>type</strong> is set to <strong id="b12708934185211"><a name="b12708934185211"></a><a name="b12708934185211"></a>instance</strong>.</li><li>Indicates the maximum limit of memory quota when <strong id="b278614019529"><a name="b278614019529"></a><a name="b278614019529"></a>type</strong> is set to <strong id="b117871340185214"><a name="b117871340185214"></a><a name="b117871340185214"></a>ram</strong>.</li></ul>
</td>
</tr>
<tr id="row13418152412393"><td class="cellrowborder" valign="top" width="24.752475247524753%" headers="mcps1.2.4.1.1 "><p id="p341712483915"><a name="p341712483915"></a><a name="p341712483915"></a>min</p>
</td>
<td class="cellrowborder" valign="top" width="34.65346534653465%" headers="mcps1.2.4.1.2 "><p id="p14418132493912"><a name="p14418132493912"></a><a name="p14418132493912"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="40.59405940594059%" headers="mcps1.2.4.1.3 "><a name="ul6173136347"></a><a name="ul6173136347"></a><ul id="ul6173136347"><li>Indicates the minimum limit of instance quota when <strong id="b988410517524"><a name="b988410517524"></a><a name="b988410517524"></a>type</strong> is set to <strong id="b988545110527"><a name="b988545110527"></a><a name="b988545110527"></a>instance</strong>.</li><li>Indicates the minimum limit of memory quota when <strong id="b1020695411521"><a name="b1020695411521"></a><a name="b1020695411521"></a>type</strong> is set to <strong id="b1820725425220"><a name="b1820725425220"></a><a name="b1820725425220"></a>ram</strong>.</li></ul>
</td>
</tr>
</tbody>
</table>

**Table  5**  resource\_user parameter description

<a name="table1641811248397"></a>
<table><thead align="left"><tr id="row134181624153915"><th class="cellrowborder" valign="top" width="24.752475247524753%" id="mcps1.2.4.1.1"><p id="p1541872443910"><a name="p1541872443910"></a><a name="p1541872443910"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="22.772277227722775%" id="mcps1.2.4.1.2"><p id="p841810249390"><a name="p841810249390"></a><a name="p841810249390"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="52.475247524752476%" id="mcps1.2.4.1.3"><p id="p15418172443913"><a name="p15418172443913"></a><a name="p15418172443913"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row14418724113912"><td class="cellrowborder" valign="top" width="24.752475247524753%" headers="mcps1.2.4.1.1 "><p id="p134188244395"><a name="p134188244395"></a><a name="p134188244395"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="22.772277227722775%" headers="mcps1.2.4.1.2 "><p id="p6418132417393"><a name="p6418132417393"></a><a name="p6418132417393"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.475247524752476%" headers="mcps1.2.4.1.3 "><p id="p1441818240395"><a name="p1441818240395"></a><a name="p1441818240395"></a>Resource tenant ID</p>
</td>
</tr>
<tr id="row19418132443915"><td class="cellrowborder" valign="top" width="24.752475247524753%" headers="mcps1.2.4.1.1 "><p id="p64181324183914"><a name="p64181324183914"></a><a name="p64181324183914"></a>tenant_name</p>
</td>
<td class="cellrowborder" valign="top" width="22.772277227722775%" headers="mcps1.2.4.1.2 "><p id="p1941811242393"><a name="p1941811242393"></a><a name="p1941811242393"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="52.475247524752476%" headers="mcps1.2.4.1.3 "><p id="p19418152423912"><a name="p19418152423912"></a><a name="p19418152423912"></a>Resource tenant name</p>
</td>
</tr>
</tbody>
</table>

**Example response**

```
{
    "quotas": {
        "resources": [
            {
                "quota": 10,
                "used": 3,
                "type": "instance",
                "min": 1,
                "max": 10,
                "unit": null
            },
            {
                "quota": 800,
                "used": 22,
                "type": "ram",
                "min": 1,
                "max": 800,
                "unit": "GB"
            }
        ],
        "resource_user": {
            "tenant_id": "836152f9838a44089f40f3cf6fd432bf",
            "tenant_name": "op_svc_dcs_003"
        }
    }
}
```

## Status Code<a name="section29701335151315"></a>

[Table 6](#table597043515135)  describes the status code of successful operations. For details about other status codes, see  [Table 1](status-codes.md#table5210141351517).

**Table  6**  Status code

<a name="table597043515135"></a>
<table><thead align="left"><tr id="row3970103581319"><th class="cellrowborder" valign="top" width="15.98%" id="mcps1.2.3.1.1"><p id="p4970163512138"><a name="p4970163512138"></a><a name="p4970163512138"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="84.02%" id="mcps1.2.3.1.2"><p id="p14970113519134"><a name="p14970113519134"></a><a name="p14970113519134"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1970935151313"><td class="cellrowborder" valign="top" width="15.98%" headers="mcps1.2.3.1.1 "><p id="p17970163551313"><a name="p17970163551313"></a><a name="p17970163551313"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="84.02%" headers="mcps1.2.3.1.2 "><p id="p597033518133"><a name="p597033518133"></a><a name="p597033518133"></a>Tenant quota queried successfully.</p>
</td>
</tr>
</tbody>
</table>

