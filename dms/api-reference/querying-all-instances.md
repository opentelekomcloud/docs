# Querying All Instances<a name="EN-US_TOPIC_0128036934"></a>

## Function<a name="section5938171365812"></a>

This API is used to query the instances of a tenant by set conditions.

## URI<a name="section426522743113"></a>

GET /v1.0/\{project\_id\}/instances?engine=\{engine\}&name=\{name\}&status=\{status\}&id=\{id\}&includeFailure=\{includeFailure\}&exactMatchName=\{exactMatchName\}

[Table 1](#table18266132712318)  describes the parameters.

**Table  1**  Parameter description

<a name="table18266132712318"></a>
<table><thead align="left"><tr id="row175711227103112"><th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.1"><p id="p1157112710315"><a name="p1157112710315"></a><a name="p1157112710315"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.2"><p id="p1457110277317"><a name="p1457110277317"></a><a name="p1457110277317"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="13.96%" id="mcps1.2.5.1.3"><p id="p5571827203118"><a name="p5571827203118"></a><a name="p5571827203118"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="55.04%" id="mcps1.2.5.1.4"><p id="p11571527103111"><a name="p11571527103111"></a><a name="p11571527103111"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row185711027143116"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="p135714274313"><a name="p135714274313"></a><a name="p135714274313"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p105721727173110"><a name="p105721727173110"></a><a name="p105721727173110"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="13.96%" headers="mcps1.2.5.1.3 "><p id="p5572112714314"><a name="p5572112714314"></a><a name="p5572112714314"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="55.04%" headers="mcps1.2.5.1.4 "><p id="p15572227133118"><a name="p15572227133118"></a><a name="p15572227133118"></a>Indicates the ID of a project.</p>
</td>
</tr>
<tr id="row057272713119"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="p957252733119"><a name="p957252733119"></a><a name="p957252733119"></a>engine</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p155721027133116"><a name="p155721027133116"></a><a name="p155721027133116"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="13.96%" headers="mcps1.2.5.1.3 "><p id="p17572102733116"><a name="p17572102733116"></a><a name="p17572102733116"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="55.04%" headers="mcps1.2.5.1.4 "><p id="p105321732135516"><a name="p105321732135516"></a><a name="p105321732135516"></a>kafka</p>
</td>
</tr>
<tr id="row457242753118"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="p11572142714314"><a name="p11572142714314"></a><a name="p11572142714314"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p155721227153118"><a name="p155721227153118"></a><a name="p155721227153118"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="13.96%" headers="mcps1.2.5.1.3 "><p id="p16572112773110"><a name="p16572112773110"></a><a name="p16572112773110"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="55.04%" headers="mcps1.2.5.1.4 "><p id="p1057272723112"><a name="p1057272723112"></a><a name="p1057272723112"></a>Indicates the instance name.</p>
</td>
</tr>
<tr id="row55721927203116"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="p185721027183117"><a name="p185721027183117"></a><a name="p185721027183117"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p157222793118"><a name="p157222793118"></a><a name="p157222793118"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="13.96%" headers="mcps1.2.5.1.3 "><p id="p7572182711319"><a name="p7572182711319"></a><a name="p7572182711319"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="55.04%" headers="mcps1.2.5.1.4 "><p id="p16572192723115"><a name="p16572192723115"></a><a name="p16572192723115"></a>Indicates the instance ID.</p>
</td>
</tr>
<tr id="row165721827183118"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="p135721427163118"><a name="p135721427163118"></a><a name="p135721427163118"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p7572182713311"><a name="p7572182713311"></a><a name="p7572182713311"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="13.96%" headers="mcps1.2.5.1.3 "><p id="p45721327193113"><a name="p45721327193113"></a><a name="p45721327193113"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="55.04%" headers="mcps1.2.5.1.4 "><p id="p1557272719314"><a name="p1557272719314"></a><a name="p1557272719314"></a>Indicates the instance status. For details, see <a href="instance-status.md">Instance Status</a>.</p>
</td>
</tr>
<tr id="row125721827183111"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="p1057216272319"><a name="p1057216272319"></a><a name="p1057216272319"></a>includeFailure</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p155721727103111"><a name="p155721727103111"></a><a name="p155721727103111"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="13.96%" headers="mcps1.2.5.1.3 "><p id="p6572727173119"><a name="p6572727173119"></a><a name="p6572727173119"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="55.04%" headers="mcps1.2.5.1.4 "><p id="p274610572098"><a name="p274610572098"></a><a name="p274610572098"></a>Indicates whether to return instances that fail to be created. Options:</p>
<p id="p1249162111312"><a name="p1249162111312"></a><a name="p1249162111312"></a><strong id="b1249010211431"><a name="b1249010211431"></a><a name="b1249010211431"></a>false</strong>: Do not return instances that fail to be created.</p>
<p id="p152161128031"><a name="p152161128031"></a><a name="p152161128031"></a><strong id="b152160281333"><a name="b152160281333"></a><a name="b152160281333"></a>true</strong> or other values: Return instances that fail to be created.</p>
<p id="p189194330320"><a name="p189194330320"></a><a name="p189194330320"></a>If this parameter is not specified, instances that fail to be created are returned by default.</p>
</td>
</tr>
<tr id="row45731827103111"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="p35732027103110"><a name="p35732027103110"></a><a name="p35732027103110"></a>exactMatchName</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p18573162718314"><a name="p18573162718314"></a><a name="p18573162718314"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="13.96%" headers="mcps1.2.5.1.3 "><p id="p957392714314"><a name="p957392714314"></a><a name="p957392714314"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="55.04%" headers="mcps1.2.5.1.4 "><p id="p1957372793113"><a name="p1957372793113"></a><a name="p1957372793113"></a>Indicates whether to search for the instance that precisely matches a specified instance name.</p>
<p id="p195731927153115"><a name="p195731927153115"></a><a name="p195731927153115"></a>The default value is <strong id="b187231814174318"><a name="b187231814174318"></a><a name="b187231814174318"></a>false</strong>, indicating that a fuzzy search is performed based on a specified instance name. If the value is <strong id="b3411918436"><a name="b3411918436"></a><a name="b3411918436"></a>true</strong>, the instance that precisely matches a specified instance name is queried.</p>
</td>
</tr>
</tbody>
</table>

**Example**

```
GET /v1.0/bd6b78e2ff9e4e47bc260803ddcc7a21/instances?start=1&limit=10&name=&status=&id=&includeFailure=true&exactMatchName=false  
```

## Request<a name="section9295727203111"></a>

**Request parameters**

None.

**Example request**

None.

## Response<a name="section152971327193118"></a>

**Response parameters**

[Table 2](#table11299182793112)  describes the parameters.

**Table  2**  Parameter description

<a name="table11299182793112"></a>
<table><thead align="left"><tr id="row175738277312"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p10573112733113"><a name="p10573112733113"></a><a name="p10573112733113"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p2057332733112"><a name="p2057332733112"></a><a name="p2057332733112"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p19573102714310"><a name="p19573102714310"></a><a name="p19573102714310"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row757372716315"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p65734273313"><a name="p65734273313"></a><a name="p65734273313"></a>instances</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p12573112793110"><a name="p12573112793110"></a><a name="p12573112793110"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1257372713111"><a name="p1257372713111"></a><a name="p1257372713111"></a>Indicates instance details.</p>
</td>
</tr>
<tr id="row957352733119"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p95732273317"><a name="p95732273317"></a><a name="p95732273317"></a>instance_num</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p18573327153119"><a name="p18573327153119"></a><a name="p18573327153119"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p8573192718314"><a name="p8573192718314"></a><a name="p8573192718314"></a>Indicates the number of instances.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  instance parameter description

<a name="table3307172743119"></a>
<table><thead align="left"><tr id="row6573827193112"><th class="cellrowborder" valign="top" width="21.782178217821784%" id="mcps1.2.4.1.1"><p id="p14573132793114"><a name="p14573132793114"></a><a name="p14573132793114"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.82178217821782%" id="mcps1.2.4.1.2"><p id="p957320271319"><a name="p957320271319"></a><a name="p957320271319"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="60.396039603960396%" id="mcps1.2.4.1.3"><p id="p115731827103110"><a name="p115731827103110"></a><a name="p115731827103110"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row8573112783118"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.1 "><p id="p2057302723118"><a name="p2057302723118"></a><a name="p2057302723118"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.4.1.2 "><p id="p257342719317"><a name="p257342719317"></a><a name="p257342719317"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.396039603960396%" headers="mcps1.2.4.1.3 "><p id="p457317272311"><a name="p457317272311"></a><a name="p457317272311"></a>Indicates the instance name.</p>
</td>
</tr>
<tr id="row35731727123118"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.1 "><p id="p157311275319"><a name="p157311275319"></a><a name="p157311275319"></a>engine</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.4.1.2 "><p id="p2057312273317"><a name="p2057312273317"></a><a name="p2057312273317"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.396039603960396%" headers="mcps1.2.4.1.3 "><p id="p15739279311"><a name="p15739279311"></a><a name="p15739279311"></a>Indicates the message engine.</p>
</td>
</tr>
<tr id="row8790154518286"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.1 "><p id="p195751727133110"><a name="p195751727133110"></a><a name="p195751727133110"></a>port</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.4.1.2 "><p id="p45751277316"><a name="p45751277316"></a><a name="p45751277316"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="60.396039603960396%" headers="mcps1.2.4.1.3 "><p id="p45751827173116"><a name="p45751827173116"></a><a name="p45751827173116"></a>Indicates the port number of an instance.</p>
</td>
</tr>
<tr id="row13791164518286"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.1 "><p id="p105754278312"><a name="p105754278312"></a><a name="p105754278312"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.4.1.2 "><p id="p17575727183116"><a name="p17575727183116"></a><a name="p17575727183116"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.396039603960396%" headers="mcps1.2.4.1.3 "><p id="p7575627103119"><a name="p7575627103119"></a><a name="p7575627103119"></a>Indicates the status of an instance. For details, see <a href="instance-status.md">Instance Status</a>.</p>
</td>
</tr>
<tr id="row498910852910"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.1 "><p id="p136531119370"><a name="p136531119370"></a><a name="p136531119370"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.4.1.2 "><p id="p166511133720"><a name="p166511133720"></a><a name="p166511133720"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.396039603960396%" headers="mcps1.2.4.1.3 "><p id="p20877106205912"><a name="p20877106205912"></a><a name="p20877106205912"></a>Indicates the instance type. Options:</p>
</td>
</tr>
<tr id="row139907810292"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.1 "><p id="p18574142773116"><a name="p18574142773116"></a><a name="p18574142773116"></a>specification</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.4.1.2 "><p id="p1357412716318"><a name="p1357412716318"></a><a name="p1357412716318"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.396039603960396%" headers="mcps1.2.4.1.3 "><p id="p1063171143716"><a name="p1063171143716"></a><a name="p1063171143716"></a>Indicates the specifications of an instance.</p>
</td>
</tr>
<tr id="row799015862917"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.1 "><p id="p185731927153114"><a name="p185731927153114"></a><a name="p185731927153114"></a>engine_version</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.4.1.2 "><p id="p9573427123113"><a name="p9573427123113"></a><a name="p9573427123113"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.396039603960396%" headers="mcps1.2.4.1.3 "><p id="p145731527193113"><a name="p145731527193113"></a><a name="p145731527193113"></a>Indicates the engine version.</p>
</td>
</tr>
<tr id="row14990789294"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.1 "><p id="p6575202717314"><a name="p6575202717314"></a><a name="p6575202717314"></a>connect_address</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.4.1.2 "><p id="p457511272316"><a name="p457511272316"></a><a name="p457511272316"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.396039603960396%" headers="mcps1.2.4.1.3 "><p id="p205751927133113"><a name="p205751927133113"></a><a name="p205751927133113"></a>Indicates the IP address of an instance.</p>
</td>
</tr>
<tr id="row12573132743117"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.1 "><p id="p195757275316"><a name="p195757275316"></a><a name="p195757275316"></a>instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.4.1.2 "><p id="p18575927153112"><a name="p18575927153112"></a><a name="p18575927153112"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.396039603960396%" headers="mcps1.2.4.1.3 "><p id="p18575182773119"><a name="p18575182773119"></a><a name="p18575182773119"></a>Indicates the instance ID.</p>
</td>
</tr>
<tr id="row2574427113112"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.1 "><p id="p1575132783113"><a name="p1575132783113"></a><a name="p1575132783113"></a>resource_spec_code</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.4.1.2 "><p id="p2576142713314"><a name="p2576142713314"></a><a name="p2576142713314"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.396039603960396%" headers="mcps1.2.4.1.3 "><p id="p1957682763116"><a name="p1957682763116"></a><a name="p1957682763116"></a>Indicates the resource specifications identifier.</p>
<a name="ul265171193719"></a><a name="ul265171193719"></a><ul id="ul265171193719"><li><strong id="b1492323118434"><a name="b1492323118434"></a><a name="b1492323118434"></a>dms.instance.kafka.cluster.c3.mini</strong>: Kafka instance, 100 MB reference bandwidth</li><li><strong id="b14366951115715"><a name="b14366951115715"></a><a name="b14366951115715"></a>dms.instance.kafka.cluster.c3.small.2</strong>: Kafka instance, 300 MB reference bandwidth</li><li><strong id="b1016345395720"><a name="b1016345395720"></a><a name="b1016345395720"></a>dms.instance.kafka.cluster.c3.middle.2</strong>: Kafka instance, 600 MB reference bandwidth</li><li><strong id="b13581155918252"><a name="b13581155918252"></a><a name="b13581155918252"></a>dms.instance.kafka.cluster.c3.high.2</strong>: Kafka instance, 1200 MB reference bandwidth</li></ul>
</td>
</tr>
<tr id="row16221151813012"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.1 "><p id="p1965151113372"><a name="p1965151113372"></a><a name="p1965151113372"></a>charging_mode</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.4.1.2 "><p id="p176541116371"><a name="p176541116371"></a><a name="p176541116371"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="60.396039603960396%" headers="mcps1.2.4.1.3 "><p id="p385716498276"><a name="p385716498276"></a><a name="p385716498276"></a>Billing mode.</p>
</td>
</tr>
<tr id="row1922121811308"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.1 "><p id="p1857822723111"><a name="p1857822723111"></a><a name="p1857822723111"></a>vpc_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.4.1.2 "><p id="p257817271313"><a name="p257817271313"></a><a name="p257817271313"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.396039603960396%" headers="mcps1.2.4.1.3 "><p id="p3578927143113"><a name="p3578927143113"></a><a name="p3578927143113"></a>Indicates the ID of a VPC.</p>
</td>
</tr>
<tr id="row5221318163016"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.1 "><p id="p14578627133114"><a name="p14578627133114"></a><a name="p14578627133114"></a>vpc_name</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.4.1.2 "><p id="p85781127153117"><a name="p85781127153117"></a><a name="p85781127153117"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.396039603960396%" headers="mcps1.2.4.1.3 "><p id="p457810274319"><a name="p457810274319"></a><a name="p457810274319"></a>Indicates the name of a VPC.</p>
</td>
</tr>
<tr id="row6246144323018"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.1 "><p id="p957812713114"><a name="p957812713114"></a><a name="p957812713114"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.4.1.2 "><p id="p65789275312"><a name="p65789275312"></a><a name="p65789275312"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.396039603960396%" headers="mcps1.2.4.1.3 "><p id="p157816279315"><a name="p157816279315"></a><a name="p157816279315"></a>Indicates the time when an instance is created. </p>
<p id="p66601112371"><a name="p66601112371"></a><a name="p66601112371"></a>The time is in the format of timestamp, that is, the offset milliseconds from 1970-01-01 00:00:00 UTC to the specified time.</p>
</td>
</tr>
<tr id="row219881113118"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.1 "><p id="p136641113711"><a name="p136641113711"></a><a name="p136641113711"></a>product_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.4.1.2 "><p id="p9661011193716"><a name="p9661011193716"></a><a name="p9661011193716"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.396039603960396%" headers="mcps1.2.4.1.3 "><p id="p66681133712"><a name="p66681133712"></a><a name="p66681133712"></a>Indicates the product ID.</p>
</td>
</tr>
<tr id="row919971173111"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.1 "><p id="p7667116373"><a name="p7667116373"></a><a name="p7667116373"></a>security_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.4.1.2 "><p id="p1566121123714"><a name="p1566121123714"></a><a name="p1566121123714"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.396039603960396%" headers="mcps1.2.4.1.3 "><p id="p966141113716"><a name="p966141113716"></a><a name="p966141113716"></a>Indicates the security group ID.</p>
</td>
</tr>
<tr id="row1119913114315"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.1 "><p id="p96612117377"><a name="p96612117377"></a><a name="p96612117377"></a>security_group_name</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.4.1.2 "><p id="p1366211203718"><a name="p1366211203718"></a><a name="p1366211203718"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.396039603960396%" headers="mcps1.2.4.1.3 "><p id="p5661411163716"><a name="p5661411163716"></a><a name="p5661411163716"></a>Indicates the security group name.</p>
</td>
</tr>
<tr id="row1349152873111"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.1 "><p id="p2066111103711"><a name="p2066111103711"></a><a name="p2066111103711"></a>subnet_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.4.1.2 "><p id="p366811133711"><a name="p366811133711"></a><a name="p366811133711"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.396039603960396%" headers="mcps1.2.4.1.3 "><p id="p1166201143713"><a name="p1166201143713"></a><a name="p1166201143713"></a>Indicates the subnet ID.</p>
</td>
</tr>
<tr id="row16492628193117"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.1 "><p id="p0683116377"><a name="p0683116377"></a><a name="p0683116377"></a>available_zones</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.4.1.2 "><p id="p1168121163713"><a name="p1168121163713"></a><a name="p1168121163713"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="60.396039603960396%" headers="mcps1.2.4.1.3 "><p id="p668191116370"><a name="p668191116370"></a><a name="p668191116370"></a>Indicates the ID of the AZ to which the instance node belongs. The AZ ID is returned.</p>
</td>
</tr>
<tr id="row649214281313"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.1 "><p id="p55781427153110"><a name="p55781427153110"></a><a name="p55781427153110"></a>user_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.4.1.2 "><p id="p20578192712318"><a name="p20578192712318"></a><a name="p20578192712318"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.396039603960396%" headers="mcps1.2.4.1.3 "><p id="p3578927153120"><a name="p3578927153120"></a><a name="p3578927153120"></a>Indicates the user ID.</p>
</td>
</tr>
<tr id="row1183405783116"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.1 "><p id="p457814276312"><a name="p457814276312"></a><a name="p457814276312"></a>user_name</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.4.1.2 "><p id="p4578162793118"><a name="p4578162793118"></a><a name="p4578162793118"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.396039603960396%" headers="mcps1.2.4.1.3 "><p id="p5578122710311"><a name="p5578122710311"></a><a name="p5578122710311"></a>Indicates the username.</p>
</td>
</tr>
<tr id="row48817541406"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.1 "><p id="p782331591216"><a name="p782331591216"></a><a name="p782331591216"></a>access_user</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.4.1.2 "><p id="p18823715171218"><a name="p18823715171218"></a><a name="p18823715171218"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.396039603960396%" headers="mcps1.2.4.1.3 "><p id="p1823181551214"><a name="p1823181551214"></a><a name="p1823181551214"></a>Indicates the username of an instance.</p>
</td>
</tr>
<tr id="row450172453220"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.1 "><p id="p1457818275315"><a name="p1457818275315"></a><a name="p1457818275315"></a>maintain_begin</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.4.1.2 "><p id="p13578127163110"><a name="p13578127163110"></a><a name="p13578127163110"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.396039603960396%" headers="mcps1.2.4.1.3 "><p id="p81093614219"><a name="p81093614219"></a><a name="p81093614219"></a>Indicates the time at which a maintenance time window starts.</p>
<p id="p173615219113"><a name="p173615219113"></a><a name="p173615219113"></a>Format: HH:mm</p>
</td>
</tr>
<tr id="row17501102420326"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.1 "><p id="p1578182743117"><a name="p1578182743117"></a><a name="p1578182743117"></a>maintain_end</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.4.1.2 "><p id="p75789276314"><a name="p75789276314"></a><a name="p75789276314"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.396039603960396%" headers="mcps1.2.4.1.3 "><p id="p11109136229"><a name="p11109136229"></a><a name="p11109136229"></a>Indicates the time at which the maintenance time window ends.</p>
<p id="p103593211218"><a name="p103593211218"></a><a name="p103593211218"></a>Format: HH:mm</p>
</td>
</tr>
<tr id="row1501202413212"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.1 "><p id="p18574727173116"><a name="p18574727173116"></a><a name="p18574727173116"></a>storage_space</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.4.1.2 "><p id="p105742272312"><a name="p105742272312"></a><a name="p105742272312"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="60.396039603960396%" headers="mcps1.2.4.1.3 "><p id="p057412719313"><a name="p057412719313"></a><a name="p057412719313"></a>Indicates the message storage space. Unit: GB</p>
</td>
</tr>
<tr id="row9834135710312"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.1 "><p id="p9834175713316"><a name="p9834175713316"></a><a name="p9834175713316"></a>total_storage_space</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.4.1.2 "><p id="p4834185773111"><a name="p4834185773111"></a><a name="p4834185773111"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="60.396039603960396%" headers="mcps1.2.4.1.3 "><p id="p5834105711315"><a name="p5834105711315"></a><a name="p5834105711315"></a>Indicates the message storage space. Unit: GB</p>
</td>
</tr>
<tr id="row1628222911338"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.1 "><p id="p85751827183117"><a name="p85751827183117"></a><a name="p85751827183117"></a>used_storage_space</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.4.1.2 "><p id="p457552743117"><a name="p457552743117"></a><a name="p457552743117"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="60.396039603960396%" headers="mcps1.2.4.1.3 "><p id="p12575152718318"><a name="p12575152718318"></a><a name="p12575152718318"></a>Indicates the used message storage space. Unit: GB</p>
</td>
</tr>
<tr id="row928212993317"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.1 "><p id="p3574127123110"><a name="p3574127123110"></a><a name="p3574127123110"></a>partition_num</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.4.1.2 "><p id="p2574427143110"><a name="p2574427143110"></a><a name="p2574427143110"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="60.396039603960396%" headers="mcps1.2.4.1.3 "><p id="p105757271313"><a name="p105757271313"></a><a name="p105757271313"></a>Indicates the maximum number of topics in a Kafka instance.</p>
</td>
</tr>
<tr id="row11282142914336"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.1 "><p id="p974553544713"><a name="p974553544713"></a><a name="p974553544713"></a>enable_publicip</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.4.1.2 "><p id="p10745123554715"><a name="p10745123554715"></a><a name="p10745123554715"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="60.396039603960396%" headers="mcps1.2.4.1.3 "><p id="p137451135174712"><a name="p137451135174712"></a><a name="p137451135174712"></a>Indicates whether to enable public access for an instance.</p>
<a name="ul16745143518477"></a><a name="ul16745143518477"></a><ul id="ul16745143518477"><li><strong id="b862519318216"><a name="b862519318216"></a><a name="b862519318216"></a>true</strong>: enable</li><li><strong id="b534914817385"><a name="b534914817385"></a><a name="b534914817385"></a>false</strong>: disable</li></ul>
</td>
</tr>
<tr id="row145742027193110"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.1 "><p id="p71092245167"><a name="p71092245167"></a><a name="p71092245167"></a>ssl_enable</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.4.1.2 "><p id="p10109162471615"><a name="p10109162471615"></a><a name="p10109162471615"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="60.396039603960396%" headers="mcps1.2.4.1.3 "><p id="p71091624131614"><a name="p71091624131614"></a><a name="p71091624131614"></a>Indicates whether to enable security authentication.</p>
<a name="ul10462144102117"></a><a name="ul10462144102117"></a><ul id="ul10462144102117"><li><strong id="b205164461325"><a name="b205164461325"></a><a name="b205164461325"></a>true</strong>: enable</li><li><strong id="b2162163623818"><a name="b2162163623818"></a><a name="b2162163623818"></a>false</strong>: disable</li></ul>
</td>
</tr>
<tr id="row14575102713319"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.1 "><p id="p2516175432812"><a name="p2516175432812"></a><a name="p2516175432812"></a>storage_resource_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.4.1.2 "><p id="p251415413281"><a name="p251415413281"></a><a name="p251415413281"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.396039603960396%" headers="mcps1.2.4.1.3 "><p id="p651215544286"><a name="p651215544286"></a><a name="p651215544286"></a>Storage resource ID</p>
</td>
</tr>
<tr id="row45755277314"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.1 "><p id="p54253862613"><a name="p54253862613"></a><a name="p54253862613"></a>storage_spec_code</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.4.1.2 "><p id="p34481152265"><a name="p34481152265"></a><a name="p34481152265"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.396039603960396%" headers="mcps1.2.4.1.3 "><p id="p194481158263"><a name="p194481158263"></a><a name="p194481158263"></a>I/O specification</p>
</td>
</tr>
<tr id="row836717814350"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.1 "><p id="p63671687358"><a name="p63671687358"></a><a name="p63671687358"></a>service_type</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.4.1.2 "><p id="p163673873510"><a name="p163673873510"></a><a name="p163673873510"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.396039603960396%" headers="mcps1.2.4.1.3 "><p id="p183673810358"><a name="p183673810358"></a><a name="p183673810358"></a>Indicates the DMS service type.</p>
</td>
</tr>
<tr id="row23671086358"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.1 "><p id="p12367158183514"><a name="p12367158183514"></a><a name="p12367158183514"></a>storage_type</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.4.1.2 "><p id="p1836818873517"><a name="p1836818873517"></a><a name="p1836818873517"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.396039603960396%" headers="mcps1.2.4.1.3 "><p id="p16368181357"><a name="p16368181357"></a><a name="p16368181357"></a>Indicates the storage type.</p>
</td>
</tr>
<tr id="row287516417350"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.1 "><p id="p3875114173517"><a name="p3875114173517"></a><a name="p3875114173517"></a>retention_policy</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.4.1.2 "><p id="p12875114133513"><a name="p12875114133513"></a><a name="p12875114133513"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.396039603960396%" headers="mcps1.2.4.1.3 "><p id="p887534116352"><a name="p887534116352"></a><a name="p887534116352"></a>Indicates the message retention policy.</p>
</td>
</tr>
<tr id="row11110104012571"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.1 "><p id="p81102403578"><a name="p81102403578"></a><a name="p81102403578"></a>kafka_public_status</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.4.1.2 "><p id="p911034065717"><a name="p911034065717"></a><a name="p911034065717"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.396039603960396%" headers="mcps1.2.4.1.3 "><p id="p1211054020574"><a name="p1211054020574"></a><a name="p1211054020574"></a>Indicates whether Kafka public access is enabled.</p>
</td>
</tr>
<tr id="row101909110583"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.1 "><p id="p1319041114588"><a name="p1319041114588"></a><a name="p1319041114588"></a>public_boundwidth</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.4.1.2 "><p id="p1719011110583"><a name="p1719011110583"></a><a name="p1719011110583"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="60.396039603960396%" headers="mcps1.2.4.1.3 "><p id="p171907114589"><a name="p171907114589"></a><a name="p171907114589"></a>Indicates the public network bandwidth.</p>
</td>
</tr>
</tbody>
</table>

**Example response**

```
{
    "instances": [
        {
            "name": "kafka-lxy-test",
            "engine": "kafka",
            "port": 9093,
            "status": "RUNNING",
            "type": "cluster",
            "specification": "100MB",
            "engine_version": "2.3.0",
            "connect_address": "192.168.1.239,192.168.1.126,192.168.1.176",
            "instance_id": "8354dde6-8229-4ff4-844d-ab7121be9745",
            "resource_spec_code": "dms.instance.kafka.cluster.c3.mini",
            "charging_mode": 1,
            "vpc_id": "aaa5c155-7a9a-4d92-a804-e19cadcbca63",
            "vpc_name": "vpc-3a7f",
            "created_at": "1572866120990",
            "product_id": "00300-30308-0--0",
            "security_group_id": "3283b880-2256-498c-aa70-154f08f65331",
            "security_group_name": "Default_All",
            "subnet_id": "598d6280-a437-4c2f-9870-a4fc80e7ba66",
            "available_zones": [
                "cn-cmcc1b-01"
            ],
            "user_id": "674f286936eb47f28f4fa54b130d4db9",
            "user_name": "hby-cwx522020",
            "access_user": "root",
            "maintain_begin": "22:00:00",
            "maintain_end": "02:00:00",
            "storage_space": 492,
            "total_storage_space": 600,
            "used_storage_space": 25,
            "partition_num": "300",
            "enable_publicip": false,
            "ssl_enable": true,
            "storage_resource_id": "3d737481-04d7-4874-a04b-2b3d884eab99",
            "storage_spec_code": "dms.physical.storage.ultra",
            "service_type": "advanced",
            "storage_type": "hec",
            "retention_policy": "time_base",
            "kafka_public_status": "closed",
            "public_boundwidth": 0
        }   
    ],
    "instance_num": 1
}
```

## Status Code<a name="section103948275315"></a>

[Table 4](#table1239452718312)  describes the status code of successful operations. For details about other status codes, see  [Status Code](status-code.md).

**Table  4**  Status code

<a name="table1239452718312"></a>
<table><thead align="left"><tr id="row7581182719318"><th class="cellrowborder" valign="top" width="15.15%" id="mcps1.2.3.1.1"><p id="p1858192719314"><a name="p1858192719314"></a><a name="p1858192719314"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="84.85000000000001%" id="mcps1.2.3.1.2"><p id="p15811927203112"><a name="p15811927203112"></a><a name="p15811927203112"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row9581127103111"><td class="cellrowborder" valign="top" width="15.15%" headers="mcps1.2.3.1.1 "><p id="p458111273315"><a name="p458111273315"></a><a name="p458111273315"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="84.85000000000001%" headers="mcps1.2.3.1.2 "><p id="p4581927153115"><a name="p4581927153115"></a><a name="p4581927153115"></a>All instances are queried successfully.</p>
</td>
</tr>
</tbody>
</table>

