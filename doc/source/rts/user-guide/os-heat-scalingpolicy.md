# OS::Heat::ScalingPolicy<a name="EN-US_TOPIC_0088407177"></a>

A resource to manage scaling of OS::Heat::AutoScalingGroup.

Resource to manage scaling for OS::Heat::AutoScalingGroup, i.e. define which metric should be scaled and scaling adjustment, set cooldown etc.

## Required Properties<a name="section96095101808"></a>

<a name="table432433312583"></a>
<table><thead align="left"><tr id="row11944630163117"><th class="cellrowborder" valign="top" width="32%" id="mcps1.1.3.1.1"><p id="p8944193033119"><a name="p8944193033119"></a><a name="p8944193033119"></a><strong id="b1855550103113"><a name="b1855550103113"></a><a name="b1855550103113"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.1.3.1.2"><p id="p19441330173118"><a name="p19441330173118"></a><a name="p19441330173118"></a><strong id="b1856150183111"><a name="b1856150183111"></a><a name="b1856150183111"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row139441630123118"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p3944173017312"><a name="p3944173017312"></a><a name="p3944173017312"></a>adjustment_type</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p51783064"><a name="p51783064"></a><a name="p51783064"></a>Type of adjustment (absolute or percentage).</p>
<p id="p63394397"><a name="p63394397"></a><a name="p63394397"></a>String value expected.</p>
<p id="p33678668"><a name="p33678668"></a><a name="p33678668"></a>Can be updated without replacement.</p>
<p id="p34672556"><a name="p34672556"></a><a name="p34672556"></a>Allowed values: change_in_capacity, exact_capacity, percent_change_in_capacity</p>
</td>
</tr>
<tr id="row12944193019312"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p39441330193113"><a name="p39441330193113"></a><a name="p39441330193113"></a>auto_scaling_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p57013647"><a name="p57013647"></a><a name="p57013647"></a>AutoScaling group ID to apply policy to.</p>
<p id="p43360780"><a name="p43360780"></a><a name="p43360780"></a>String value expected.</p>
<p id="p54702703"><a name="p54702703"></a><a name="p54702703"></a>Updates cause replacement.</p>
</td>
</tr>
<tr id="row4944143093118"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p794443014312"><a name="p794443014312"></a><a name="p794443014312"></a>scaling_adjustment</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p1733939"><a name="p1733939"></a><a name="p1733939"></a>Size of adjustment.</p>
<p id="p15605454"><a name="p15605454"></a><a name="p15605454"></a>Number value expected.</p>
<p id="p6231364"><a name="p6231364"></a><a name="p6231364"></a>Can be updated without replacement.</p>
</td>
</tr>
</tbody>
</table>

## Optional Properties<a name="section31038461716"></a>

<a name="table0982105215115"></a>
<table><thead align="left"><tr id="row865525963211"><th class="cellrowborder" valign="top" width="32%" id="mcps1.1.3.1.1"><p id="p1965612596325"><a name="p1965612596325"></a><a name="p1965612596325"></a><strong id="b9656105973216"><a name="b9656105973216"></a><a name="b9656105973216"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.1.3.1.2"><p id="p06561059183218"><a name="p06561059183218"></a><a name="p06561059183218"></a><strong id="b765685917326"><a name="b765685917326"></a><a name="b765685917326"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row2656165943215"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p0657145983216"><a name="p0657145983216"></a><a name="p0657145983216"></a>cooldown</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p51336373"><a name="p51336373"></a><a name="p51336373"></a>Cooldown period, in seconds.</p>
<p id="p59374178"><a name="p59374178"></a><a name="p59374178"></a>Number value expected.</p>
<p id="p64605559"><a name="p64605559"></a><a name="p64605559"></a>Can be updated without replacement.</p>
</td>
</tr>
<tr id="row158004023417"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p115811340123418"><a name="p115811340123418"></a><a name="p115811340123418"></a>min_adjustment_step</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p95818406349"><a name="p95818406349"></a><a name="p95818406349"></a>Minimum number of resources that are added or removed when the AutoScaling group scales up or down. This can be used only when specifying percent_change_in_capacity for the adjustment_type property.</p>
<p id="p1086825019346"><a name="p1086825019346"></a><a name="p1086825019346"></a>Integer value expected.</p>
<p id="p1527715119343"><a name="p1527715119343"></a><a name="p1527715119343"></a>Can be updated without replacement.</p>
<p id="p18766192310350"><a name="p18766192310350"></a><a name="p18766192310350"></a>The value must be at least 0.</p>
</td>
</tr>
</tbody>
</table>

## Attributes<a name="section47976221924"></a>

<a name="table1325512814216"></a>
<table><thead align="left"><tr id="row4261133393315"><th class="cellrowborder" valign="top" width="32%" id="mcps1.1.3.1.1"><p id="p132618338337"><a name="p132618338337"></a><a name="p132618338337"></a><strong id="b14262173313314"><a name="b14262173313314"></a><a name="b14262173313314"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.1.3.1.2"><p id="p102621233183313"><a name="p102621233183313"></a><a name="p102621233183313"></a><strong id="b326216332332"><a name="b326216332332"></a><a name="b326216332332"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1526273323316"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p3263153303314"><a name="p3263153303314"></a><a name="p3263153303314"></a>alarm_url</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p19263193311331"><a name="p19263193311331"></a><a name="p19263193311331"></a>A signed url to handle the alarm.</p>
</td>
</tr>
</tbody>
</table>

## HOT Syntax<a name="section118671694312"></a>

```
heat_template_version: 2014-10-16
...
resources:
  ...
  the_resource:
    type: OS::Heat::ScalingPolicy
    properties:
      adjustment_type: String
      auto_scaling_group_id: String
      cooldown: Number
      min_adjustment_step: Integer
      scaling_adjustment: Number
```

