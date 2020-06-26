# OSE::CES::Alarm<a name="EN-US_TOPIC_0088407210"></a>

A resource of CES.

## Required Properties<a name="section592819537234"></a>

<a name="table11176132172417"></a>
<table><thead align="left"><tr id="row1297193119406"><th class="cellrowborder" valign="top" width="34%" id="mcps1.1.3.1.1"><p id="p1517653222410"><a name="p1517653222410"></a><a name="p1517653222410"></a><strong id="b18279326173414"><a name="b18279326173414"></a><a name="b18279326173414"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="66%" id="mcps1.1.3.1.2"><p id="p151766320246"><a name="p151766320246"></a><a name="p151766320246"></a><strong id="b142809266340"><a name="b142809266340"></a><a name="b142809266340"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row89713315407"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p12176432192417"><a name="p12176432192417"></a><a name="p12176432192417"></a>evaluation_periods</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p60662241"><a name="p60662241"></a><a name="p60662241"></a>Consecutive count.</p>
<p id="p9089262"><a name="p9089262"></a><a name="p9089262"></a>Integer value expected.</p>
<p id="p14694501"><a name="p14694501"></a><a name="p14694501"></a>Can be updated without replacement.</p>
<p id="p65141645"><a name="p65141645"></a><a name="p65141645"></a>Allowed values: from 1 to 5, include 1 and 5.</p>
</td>
</tr>
<tr id="row1297143119401"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p351491416256"><a name="p351491416256"></a><a name="p351491416256"></a>comparison_operator</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p41981888"><a name="p41981888"></a><a name="p41981888"></a>Operator used to compare specified statistic with threshold.</p>
<p id="p42292677"><a name="p42292677"></a><a name="p42292677"></a>String value expected.</p>
<p id="p45089776"><a name="p45089776"></a><a name="p45089776"></a>Can be updated without replacement.</p>
<p id="p3154802"><a name="p3154802"></a><a name="p3154802"></a>Allowed values: gt, lt, ge, le, eq</p>
</td>
</tr>
<tr id="row29793114405"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p9176332142416"><a name="p9176332142416"></a><a name="p9176332142416"></a>meter_name</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p54212391"><a name="p54212391"></a><a name="p54212391"></a>Metric name.</p>
<p id="p18149477"><a name="p18149477"></a><a name="p18149477"></a>String value expected.</p>
<p id="p29127565"><a name="p29127565"></a><a name="p29127565"></a>Updates cause replacement.</p>
<p id="p60821498"><a name="p60821498"></a><a name="p60821498"></a>Allowed values: <strong id="b41121115175322"><a name="b41121115175322"></a><a name="b41121115175322"></a>cpu_util</strong>,&nbsp;<strong id="b34545722175322"><a name="b34545722175322"></a><a name="b34545722175322"></a>mem_util</strong>,&nbsp;<strong id="b42476042175322"><a name="b42476042175322"></a><a name="b42476042175322"></a>network_incoming_bytes_rate_inband</strong>, and&nbsp;<strong id="b28503563175333"><a name="b28503563175333"></a><a name="b28503563175333"></a>network_outgoing_bytes_rate_inband</strong>.</p>
<a name="ul5659154410359"></a><a name="ul5659154410359"></a><ul id="ul5659154410359"><li>cpu_util: CPU Usage.</li><li>mem_util: Memory Usage.</li><li>network_incoming_bytes_rate_inband: Inband Incoming Rate.</li><li>network_outgoing_bytes_rate_inband: Inband Outgoing Rate.</li></ul>
</td>
</tr>
<tr id="row497103164019"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p8176183222415"><a name="p8176183222415"></a><a name="p8176183222415"></a>period</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p53490308"><a name="p53490308"></a><a name="p53490308"></a>Period (seconds) to evaluate over.</p>
<p id="p11650730"><a name="p11650730"></a><a name="p11650730"></a>Integer value expected.</p>
<p id="p37747707"><a name="p37747707"></a><a name="p37747707"></a>Can be updated without replacement.</p>
<p id="p4185050"><a name="p4185050"></a><a name="p4185050"></a>Allowed values: 300, 1200, 3600, 14400, 86400</p>
<p id="p37665455"><a name="p37665455"></a><a name="p37665455"></a>During alarm interconnection with CES, the native attribute <strong id="b11693912131617"><a name="b11693912131617"></a><a name="b11693912131617"></a>period</strong> can be any value. However, CES supports only the preceding fixed values. Otherwise, alarm resource creation fails.</p>
</td>
</tr>
<tr id="row10971431164011"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p18176432152413"><a name="p18176432152413"></a><a name="p18176432152413"></a>resource_id</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p31003015"><a name="p31003015"></a><a name="p31003015"></a>ID of the group.</p>
<p id="p10591684"><a name="p10591684"></a><a name="p10591684"></a>String value expected.</p>
<p id="p28216300"><a name="p28216300"></a><a name="p28216300"></a>Updates cause replacement.</p>
<p id="p52620110"><a name="p52620110"></a><a name="p52620110"></a>This attributed is required by Cloud Eye (CES) for filtering.</p>
</td>
</tr>
<tr id="row1897631124018"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p51761732162417"><a name="p51761732162417"></a><a name="p51761732162417"></a>statistic</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p34370545"><a name="p34370545"></a><a name="p34370545"></a>Way to data aggregation.</p>
<p id="p40899451"><a name="p40899451"></a><a name="p40899451"></a>String value expected.</p>
<p id="p32550740"><a name="p32550740"></a><a name="p32550740"></a>Updates cause replacement.</p>
<p id="p24521205"><a name="p24521205"></a><a name="p24521205"></a>Allowed values: avg, min, max, variance.</p>
</td>
</tr>
<tr id="row129733111409"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p717683215242"><a name="p717683215242"></a><a name="p717683215242"></a>threshold</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p40060571"><a name="p40060571"></a><a name="p40060571"></a>Threshold value of the alarm.</p>
<p id="p25000827"><a name="p25000827"></a><a name="p25000827"></a>Integer value expected.</p>
<p id="p23680855"><a name="p23680855"></a><a name="p23680855"></a>Can be updated without replacement.</p>
</td>
</tr>
</tbody>
</table>

## Optional Properties<a name="section59341120245"></a>

<a name="table2915320172717"></a>
<table><thead align="left"><tr id="row8406399439"><th class="cellrowborder" valign="top" width="34%" id="mcps1.1.3.1.1"><p id="p0916520132710"><a name="p0916520132710"></a><a name="p0916520132710"></a><strong id="b13221152412434"><a name="b13221152412434"></a><a name="b13221152412434"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="66%" id="mcps1.1.3.1.2"><p id="p89161720172714"><a name="p89161720172714"></a><a name="p89161720172714"></a><strong id="b2222162412432"><a name="b2222162412432"></a><a name="b2222162412432"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row19406796437"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p18916182002715"><a name="p18916182002715"></a><a name="p18916182002715"></a>action_enabled</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p50487104"><a name="p50487104"></a><a name="p50487104"></a>Whether to enable this alarm to trigger actions.</p>
<p id="p51730756"><a name="p51730756"></a><a name="p51730756"></a>Boolean value expected.</p>
<p id="p62923625"><a name="p62923625"></a><a name="p62923625"></a>Can be updated without replacement.</p>
<p id="p29441721"><a name="p29441721"></a><a name="p29441721"></a>Defaults to "True".</p>
</td>
</tr>
<tr id="row164061984314"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p591692002711"><a name="p591692002711"></a><a name="p591692002711"></a>alarm_actions</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p35969186"><a name="p35969186"></a><a name="p35969186"></a>A list of URLs (webhooks) to invoke when state transitions to alarm.</p>
<p id="p55287222"><a name="p55287222"></a><a name="p55287222"></a>List value expected.</p>
<p id="p27822952"><a name="p27822952"></a><a name="p27822952"></a>Can be updated without replacement.</p>
</td>
</tr>
<tr id="row11406109184315"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p19916020182714"><a name="p19916020182714"></a><a name="p19916020182714"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p39066610"><a name="p39066610"></a><a name="p39066610"></a>Description for the alarm.</p>
<p id="p16055172"><a name="p16055172"></a><a name="p16055172"></a>String value expected.</p>
<p id="p10278824"><a name="p10278824"></a><a name="p10278824"></a>Can be updated without replacement.</p>
<p id="p25400560"><a name="p25400560"></a><a name="p25400560"></a>Allowed pattern: ^[^\&amp;\"\'\(\)]{0,256}$</p>
</td>
</tr>
<tr id="row144062915439"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p1791617204278"><a name="p1791617204278"></a><a name="p1791617204278"></a>enabled</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p44179476"><a name="p44179476"></a><a name="p44179476"></a>Whether to enable alarm.</p>
<p id="p62070971"><a name="p62070971"></a><a name="p62070971"></a>Boolean value expected.</p>
<p id="p21767833"><a name="p21767833"></a><a name="p21767833"></a>Can be updated without replacement.</p>
<p id="p61692775"><a name="p61692775"></a><a name="p61692775"></a>Defaults to "True".</p>
</td>
</tr>
<tr id="row74061697436"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p1491616200279"><a name="p1491616200279"></a><a name="p1491616200279"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p31058912"><a name="p31058912"></a><a name="p31058912"></a>Name of the alarm.</p>
<p id="p11094757"><a name="p11094757"></a><a name="p11094757"></a>String value expected.</p>
<p id="p32743949"><a name="p32743949"></a><a name="p32743949"></a>Can be updated without replacement.</p>
<p id="p8478854143419"><a name="p8478854143419"></a><a name="p8478854143419"></a>It is allowed to start with <strong id="b1279613252309"><a name="b1279613252309"></a><a name="b1279613252309"></a>numbers</strong>, <strong id="b107201029113015"><a name="b107201029113015"></a><a name="b107201029113015"></a>letters</strong>, _, and <strong id="b9809184113309"><a name="b9809184113309"></a><a name="b9809184113309"></a>-</strong> characters. It is allowed to include <strong id="b22921519153119"><a name="b22921519153119"></a><a name="b22921519153119"></a>numbers</strong>, <strong id="b929441919312"><a name="b929441919312"></a><a name="b929441919312"></a>letters</strong>, _, and <strong id="b5295111983114"><a name="b5295111983114"></a><a name="b5295111983114"></a>-</strong> characters, and the string length is <strong id="b547314383115"><a name="b547314383115"></a><a name="b547314383115"></a>1</strong> to <strong id="b20155827173610"><a name="b20155827173610"></a><a name="b20155827173610"></a>128</strong>.</p>
</td>
</tr>
<tr id="row144067974314"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p119161520172710"><a name="p119161520172710"></a><a name="p119161520172710"></a>unit</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p46692626"><a name="p46692626"></a><a name="p46692626"></a>Unit of data.</p>
<p id="p17580453"><a name="p17580453"></a><a name="p17580453"></a>String value expected.</p>
<p id="p24006353"><a name="p24006353"></a><a name="p24006353"></a>Can be updated without replacement.</p>
<p id="p14730592"><a name="p14730592"></a><a name="p14730592"></a>The string length allowed is <strong id="b1384341333711"><a name="b1384341333711"></a><a name="b1384341333711"></a>0</strong> to<strong id="b1284301313713"><a name="b1284301313713"></a><a name="b1284301313713"></a> 32</strong>.</p>
</td>
</tr>
<tr id="row6407090432"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p691612032720"><a name="p691612032720"></a><a name="p691612032720"></a>matching_metadata</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p52327279"><a name="p52327279"></a><a name="p52327279"></a>Meter should match this resource metadata (key=value) additionally to the meter_name.</p>
<p id="p1183466"><a name="p1183466"></a><a name="p1183466"></a>Map value expected.</p>
<p id="p10651195"><a name="p10651195"></a><a name="p10651195"></a>Can be updated without replacement.</p>
<p id="p28751891"><a name="p28751891"></a><a name="p28751891"></a>Defaults to "{}".</p>
<div class="note" id="note12463867175416"><a name="note12463867175416"></a><a name="note12463867175416"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p47201796"><a name="p47201796"></a><a name="p47201796"></a>This parameter is invalid in the current version.</p>
</div></div>
</td>
</tr>
<tr id="row176281620204511"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p11628152018459"><a name="p11628152018459"></a><a name="p11628152018459"></a>resource_type</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p3245502814496"><a name="p3245502814496"></a><a name="p3245502814496"></a>Alarm type of resource.</p>
<p id="p2365980314496"><a name="p2365980314496"></a><a name="p2365980314496"></a>String value expected.</p>
<p id="p1161164014496"><a name="p1161164014496"></a><a name="p1161164014496"></a>Updates cause replacement.</p>
<p id="p3739590014496"><a name="p3739590014496"></a><a name="p3739590014496"></a>Defaults to "RTS.Group".</p>
<p id="p101878414496"><a name="p101878414496"></a><a name="p101878414496"></a>Allowed values: RTS.Group, AS.Group</p>
</td>
</tr>
</tbody>
</table>

## HOT Syntax<a name="section978010136243"></a>

```
heat_template_version: 2014-10-16
...
resources:
  ...
  the_resource:
    type: OSE::CES::Alarm
    properties:
      action_enabled: Boolean
      alarm_actions: […]
      comparison_operator: String
      description: String
      enabled: Boolean
      evaluation_periods: Integer
      meter_name: String
      name: String
      period: Integer
      resource_id: String
      statistic: String
      threshold: Integer
      unit: String
```

