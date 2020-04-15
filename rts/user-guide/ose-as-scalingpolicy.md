# OSE::AS::ScalingPolicy<a name="EN-US_TOPIC_0088407071"></a>

A resource for managing autoscaling policy.

## Required Properties<a name="section656696121715"></a>

<a name="table17942114019176"></a>
<table><thead align="left"><tr id="row8803448183214"><th class="cellrowborder" valign="top" width="32%" id="mcps1.1.3.1.1"><p id="p6716174616318"><a name="p6716174616318"></a><a name="p6716174616318"></a><strong id="b1871674623117"><a name="b1871674623117"></a><a name="b1871674623117"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.1.3.1.2"><p id="p1571814603119"><a name="p1571814603119"></a><a name="p1571814603119"></a><strong id="b10719174615316"><a name="b10719174615316"></a><a name="b10719174615316"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1180394873217"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p980384812320"><a name="p980384812320"></a><a name="p980384812320"></a>scaling_policy_name</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p30724919184530"><a name="p30724919184530"></a><a name="p30724919184530"></a>Autoscaling policy name.</p>
<p id="p8088820184530"><a name="p8088820184530"></a><a name="p8088820184530"></a>String value expected.</p>
<p id="p5690517184530"><a name="p5690517184530"></a><a name="p5690517184530"></a>Can be updated without replacement.</p>
<p id="p51214661184530"><a name="p51214661184530"></a><a name="p51214661184530"></a>It is allowed to start with <strong id="b1279613252309"><a name="b1279613252309"></a><a name="b1279613252309"></a>numbers</strong>, <strong id="b107201029113015"><a name="b107201029113015"></a><a name="b107201029113015"></a>letters</strong>, _, and <strong id="b9809184113309"><a name="b9809184113309"></a><a name="b9809184113309"></a>-</strong> characters. It is allowed to include <strong id="b22921519153119"><a name="b22921519153119"></a><a name="b22921519153119"></a>numbers</strong>, <strong id="b929441919312"><a name="b929441919312"></a><a name="b929441919312"></a>letters</strong>, _, and <strong id="b5295111983114"><a name="b5295111983114"></a><a name="b5295111983114"></a>-</strong> characters, and the string length is <strong id="b547314383115"><a name="b547314383115"></a><a name="b547314383115"></a>1</strong> to <strong id="b55691446103119"><a name="b55691446103119"></a><a name="b55691446103119"></a>64</strong>.</p>
</td>
</tr>
<tr id="row1380312488324"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p1380415489325"><a name="p1380415489325"></a><a name="p1380415489325"></a>scaling_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p22960124184530"><a name="p22960124184530"></a><a name="p22960124184530"></a>Autoscaling group ID.</p>
<p id="p5314526184530"><a name="p5314526184530"></a><a name="p5314526184530"></a>String value expected.</p>
<p id="p47830740184530"><a name="p47830740184530"></a><a name="p47830740184530"></a>Updates cause replacement.</p>
</td>
</tr>
<tr id="row168043484326"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p78041548123216"><a name="p78041548123216"></a><a name="p78041548123216"></a>scaling_policy_type</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p39109193184530"><a name="p39109193184530"></a><a name="p39109193184530"></a>The type of autoscaling policy.</p>
<p id="p16438421184530"><a name="p16438421184530"></a><a name="p16438421184530"></a>String value expected.</p>
<p id="p13728065184530"><a name="p13728065184530"></a><a name="p13728065184530"></a>Can be updated without replacement.</p>
<p id="p56443726184530"><a name="p56443726184530"></a><a name="p56443726184530"></a>Allowed values: ALARM, SCHEDULED, RECURRENCE</p>
<a name="ul125676201213"></a><a name="ul125676201213"></a><ul id="ul125676201213"><li>ALARM: AS automatically increases or decreases the number of instances in an AS group or sets the number of instances to a specified value if Cloud Eye (CES) generates an alarm for a configured metric, such as CPU usage.</li><li>SCHEDULED: AS automatically increases or decreases the number of instances in an AS group or sets the number of instances to a specified value at a specified time.</li><li>RECURRENCE: AS increases or decreases the number of instances in an AS group or sets the number of instances to a specified value at a configured interval, such as one day, one week, or month.</li></ul>
</td>
</tr>
</tbody>
</table>

## Optional Properties<a name="section1595911153179"></a>

<a name="table588975821820"></a>
<table><thead align="left"><tr id="row339211169343"><th class="cellrowborder" valign="top" width="33%" id="mcps1.1.3.1.1"><p id="p227910261345"><a name="p227910261345"></a><a name="p227910261345"></a><strong id="b18279326173414"><a name="b18279326173414"></a><a name="b18279326173414"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="67%" id="mcps1.1.3.1.2"><p id="p182792268347"><a name="p182792268347"></a><a name="p182792268347"></a><strong id="b142809266340"><a name="b142809266340"></a><a name="b142809266340"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row183921116193419"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p3392121616345"><a name="p3392121616345"></a><a name="p3392121616345"></a>alarm_id</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p44833912184612"><a name="p44833912184612"></a><a name="p44833912184612"></a>CES alarm rule ID, which must be selected when scaling_policy_type is ALARM.</p>
<p id="p852025184612"><a name="p852025184612"></a><a name="p852025184612"></a>String value expected.</p>
<p id="p7668231184612"><a name="p7668231184612"></a><a name="p7668231184612"></a>Can be updated without replacement.</p>
</td>
</tr>
<tr id="row9392916163412"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p539201643412"><a name="p539201643412"></a><a name="p539201643412"></a>scheduled_policy</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p20104939184612"><a name="p20104939184612"></a><a name="p20104939184612"></a>The scheduled policy, which must be set when scaling_policy_type is SCHEDULED or RECURRENCE.</p>
<p id="p17887324184612"><a name="p17887324184612"></a><a name="p17887324184612"></a>Map value expected.</p>
<p id="p26768191184612"><a name="p26768191184612"></a><a name="p26768191184612"></a>Can be updated without replacement.</p>
<p id="p39587134184612"><a name="p39587134184612"></a><a name="p39587134184612"></a><em id="i20739888184612"><a name="i20739888184612"></a><a name="i20739888184612"></a>Map properties:</em></p>
<a name="ul62033473"></a><a name="ul62033473"></a><ul id="ul62033473"><li>launch_time<p id="p19884659184612"><a name="p19884659184612"></a><a name="p19884659184612"></a>The launch time of scheduled policy. If scaling_policy_type is SCHEDULED, the format is: YYYY-MM-DDThh: mmZ, else if scaling_policy_type is RECURRENCE, the format is: hh: mm.</p>
<p id="p44744208184612"><a name="p44744208184612"></a><a name="p44744208184612"></a>String value expected.</p>
<p id="p071611453518"><a name="p071611453518"></a><a name="p071611453518"></a>Can be updated without replacement.</p>
</li><li>recurrence_type<p id="p32582690184612"><a name="p32582690184612"></a><a name="p32582690184612"></a>The recurrence type of scheduled policy, must be specified when scaling_policy_type is RECURRENCE.</p>
<p id="p24808759184612"><a name="p24808759184612"></a><a name="p24808759184612"></a>String value expected.</p>
<p id="p21952242184612"><a name="p21952242184612"></a><a name="p21952242184612"></a>Can be updated without replacement.</p>
<p id="p19641104210354"><a name="p19641104210354"></a><a name="p19641104210354"></a>Allowed values: Daily, Weekly and Monthly.</p>
</li><li>recurrence_value<p id="p13039271184612"><a name="p13039271184612"></a><a name="p13039271184612"></a>The recurrence value of scheduled policy. When the recurrence type is Daily, the recurrence value is null, indicating that it is executed every day. When the recurrence type is Weekly, the recurrence value is in the range 1-7 (1 for Sunday). When the recurrence type is Monthly, the recurrence value is in the range of 1-31.</p>
<p id="p50244575184612"><a name="p50244575184612"></a><a name="p50244575184612"></a>String value expected.</p>
<p id="p17589652163511"><a name="p17589652163511"></a><a name="p17589652163511"></a>Can be updated without replacement.</p>
</li><li>start_time<p id="p15920412184612"><a name="p15920412184612"></a><a name="p15920412184612"></a>The start time of scheduled policy, the format is: YYYY-MM-DDThh: mmZ.</p>
<p id="p9065988184612"><a name="p9065988184612"></a><a name="p9065988184612"></a>String value expected.</p>
<p id="p1764919019362"><a name="p1764919019362"></a><a name="p1764919019362"></a>Can be updated without replacement.</p>
</li><li>end_time<p id="p23493981184612"><a name="p23493981184612"></a><a name="p23493981184612"></a>The end time of scheduled policy, the format is: YYYY-MM-DDThh: mmZ, must be specified when scaling_policy_type is RECURRENCE.</p>
<p id="p10119244184612"><a name="p10119244184612"></a><a name="p10119244184612"></a>String value expected.</p>
<p id="p730428113613"><a name="p730428113613"></a><a name="p730428113613"></a>Can be updated without replacement.</p>
</li></ul>
</td>
</tr>
<tr id="row19392131614346"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p1339216164348"><a name="p1339216164348"></a><a name="p1339216164348"></a>scaling_policy_action</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p21697398184612"><a name="p21697398184612"></a><a name="p21697398184612"></a>Strategy to perform specific actions.</p>
<p id="p61058862184612"><a name="p61058862184612"></a><a name="p61058862184612"></a>Map value expected.</p>
<p id="p12658848184612"><a name="p12658848184612"></a><a name="p12658848184612"></a>Can be updated without replacement.</p>
<p id="p46820775184612"><a name="p46820775184612"></a><a name="p46820775184612"></a><em id="i18733795184612"><a name="i18733795184612"></a><a name="i18733795184612"></a>Map properties:</em></p>
<a name="ul18069451"></a><a name="ul18069451"></a><ul id="ul18069451"><li>operation<p id="p33837335184612"><a name="p33837335184612"></a><a name="p33837335184612"></a>The operation of scheduled policy action.</p>
<p id="p36100561184612"><a name="p36100561184612"></a><a name="p36100561184612"></a>String value expected.</p>
<p id="p56469597184612"><a name="p56469597184612"></a><a name="p56469597184612"></a>Can be updated without replacement.</p>
<p id="p38464333184612"><a name="p38464333184612"></a><a name="p38464333184612"></a>Allowed values: ADD, REMOVE and SET</p>
<p id="p1182634933613"><a name="p1182634933613"></a><a name="p1182634933613"></a>Default value: ADD.</p>
</li><li>instance_number<p id="p56102800184612"><a name="p56102800184612"></a><a name="p56102800184612"></a>The instance number per operation.</p>
<p id="p35163158184612"><a name="p35163158184612"></a><a name="p35163158184612"></a>Integer value expected.</p>
<p id="p48032972184612"><a name="p48032972184612"></a><a name="p48032972184612"></a>Can be updated without replacement.</p>
<p id="p17129403376"><a name="p17129403376"></a><a name="p17129403376"></a>Default value: 1</p>
</li></ul>
</td>
</tr>
<tr id="row1039213166345"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p039261611341"><a name="p039261611341"></a><a name="p039261611341"></a>cool_down_time</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p52319106184612"><a name="p52319106184612"></a><a name="p52319106184612"></a>Cool down period, in seconds.</p>
<p id="p1109906184612"><a name="p1109906184612"></a><a name="p1109906184612"></a>Integer value expected.</p>
<p id="p9989160184612"><a name="p9989160184612"></a><a name="p9989160184612"></a>Can be updated without replacement.</p>
</td>
</tr>
</tbody>
</table>

## HOT Syntax<a name="section4831625121712"></a>

```
heat_template_version: 2014-10-16
...
resources:
  ...
  the_resource:
    type: OSE::AS::ScalingPolicy
    properties:
      scaling_policy_name: String
      scaling_group_id: String
      scaling_policy_type: String
      alarm_id: String
      scheduled_policy: String
      scaling_policy_action: {"operation":  String, "instance_number": Integer}
      cool_down_time: Integer
```

