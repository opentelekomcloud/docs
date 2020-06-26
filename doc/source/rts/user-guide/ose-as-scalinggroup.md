# OSE::AS::ScalingGroup<a name="EN-US_TOPIC_0088407205"></a>

A resource for managing autoscaling group.

## Required Properties<a name="section89487261545"></a>

<a name="table948714199511"></a>
<table><thead align="left"><tr id="row118441245202120"><th class="cellrowborder" valign="top" width="32%" id="mcps1.1.3.1.1"><p id="p758125153015"><a name="p758125153015"></a><a name="p758125153015"></a><strong id="b1158213583014"><a name="b1158213583014"></a><a name="b1158213583014"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.1.3.1.2"><p id="p858219515305"><a name="p858219515305"></a><a name="p858219515305"></a><strong id="b25821557307"><a name="b25821557307"></a><a name="b25821557307"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row2844545142116"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p16844174514212"><a name="p16844174514212"></a><a name="p16844174514212"></a>scaling_group_name</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p56201083184243"><a name="p56201083184243"></a><a name="p56201083184243"></a>Autoscaling group name.</p>
<p id="p36047699184243"><a name="p36047699184243"></a><a name="p36047699184243"></a>String value expected.</p>
<p id="p55993841184243"><a name="p55993841184243"></a><a name="p55993841184243"></a>Can be updated without replacement.</p>
<p id="p34182525184243"><a name="p34182525184243"></a><a name="p34182525184243"></a>It is allowed to start with <strong id="b1279613252309"><a name="b1279613252309"></a><a name="b1279613252309"></a>numbers</strong>, <strong id="b107201029113015"><a name="b107201029113015"></a><a name="b107201029113015"></a>letters</strong>, _, and <strong id="b9809184113309"><a name="b9809184113309"></a><a name="b9809184113309"></a>-</strong> characters. It is allowed to include <strong id="b22921519153119"><a name="b22921519153119"></a><a name="b22921519153119"></a>numbers</strong>, <strong id="b929441919312"><a name="b929441919312"></a><a name="b929441919312"></a>letters</strong>, _, and <strong id="b5295111983114"><a name="b5295111983114"></a><a name="b5295111983114"></a>-</strong> characters, and the string length is <strong id="b547314383115"><a name="b547314383115"></a><a name="b547314383115"></a>1</strong> to <strong id="b55691446103119"><a name="b55691446103119"></a><a name="b55691446103119"></a>64</strong>.</p>
</td>
</tr>
<tr id="row1684434512114"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p1084454562120"><a name="p1084454562120"></a><a name="p1084454562120"></a>scaling_configuration_id</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p21672455184243"><a name="p21672455184243"></a><a name="p21672455184243"></a>AS configuration ID.</p>
<p id="p60834374184243"><a name="p60834374184243"></a><a name="p60834374184243"></a>String value expected.</p>
<p id="p10638455184243"><a name="p10638455184243"></a><a name="p10638455184243"></a>Can be updated without replacement.</p>
</td>
</tr>
<tr id="row138440455212"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p12844145122118"><a name="p12844145122118"></a><a name="p12844145122118"></a>networks</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p37914849184243"><a name="p37914849184243"></a><a name="p37914849184243"></a>An ordered list of networks used to create instances, which are in same VPC defined in the vpc_id parameter.</p>
<p id="p5689321184243"><a name="p5689321184243"></a><a name="p5689321184243"></a>List value expected.</p>
<p id="p51203889184243"><a name="p51203889184243"></a><a name="p51203889184243"></a>Can be updated without replacement.</p>
<p id="p58181818184243"><a name="p58181818184243"></a><a name="p58181818184243"></a><em id="i53874317184243"><a name="i53874317184243"></a><a name="i53874317184243"></a>List contents:</em></p>
<a name="ul14573100"></a><a name="ul14573100"></a><ul id="ul14573100"><li>*<p id="p15692246184243"><a name="p15692246184243"></a><a name="p15692246184243"></a>Map value expected.</p>
<p id="p7012492184243"><a name="p7012492184243"></a><a name="p7012492184243"></a>Can be updated without replacement.</p>
<p id="p1287959182218"><a name="p1287959182218"></a><a name="p1287959182218"></a><em id="i31140990184243"><a name="i31140990184243"></a><a name="i31140990184243"></a>Map properties:</em></p>
<a name="ul438174017616"></a><a name="ul438174017616"></a><ul id="ul438174017616"><li>id<p id="p18986248184243"><a name="p18986248184243"></a><a name="p18986248184243"></a>The ID of network.</p>
<p id="p36658512184243"><a name="p36658512184243"></a><a name="p36658512184243"></a>String value expected.</p>
<p id="p16245191718236"><a name="p16245191718236"></a><a name="p16245191718236"></a>Can be updated without replacement.</p>
</li></ul>
</li></ul>
</td>
</tr>
<tr id="row108441945172110"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p184454532116"><a name="p184454532116"></a><a name="p184454532116"></a>security_groups</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p65441428184243"><a name="p65441428184243"></a><a name="p65441428184243"></a>An ordered list of security groups used to create instances.</p>
<p id="p52101943184243"><a name="p52101943184243"></a><a name="p52101943184243"></a>List value expected.</p>
<p id="p66264309184243"><a name="p66264309184243"></a><a name="p66264309184243"></a>Can be updated without replacement.</p>
<p id="p59507869184243"><a name="p59507869184243"></a><a name="p59507869184243"></a><em id="i65808778184243"><a name="i65808778184243"></a><a name="i65808778184243"></a>List contents:</em></p>
<a name="ul12525694"></a><a name="ul12525694"></a><ul id="ul12525694"><li>*<p id="p58870426184243"><a name="p58870426184243"></a><a name="p58870426184243"></a>Map value expected.</p>
<p id="p60071794184243"><a name="p60071794184243"></a><a name="p60071794184243"></a>Can be updated without replacement.</p>
<p id="p1782734752311"><a name="p1782734752311"></a><a name="p1782734752311"></a><em id="i33977108184243"><a name="i33977108184243"></a><a name="i33977108184243"></a>Map properties:</em></p>
<a name="ul1372024175"></a><a name="ul1372024175"></a><ul id="ul1372024175"><li>id<p id="p6141418184243"><a name="p6141418184243"></a><a name="p6141418184243"></a>The ID of security group.</p>
<p id="p55272767184243"><a name="p55272767184243"></a><a name="p55272767184243"></a>String value expected.</p>
<p id="p15204162413"><a name="p15204162413"></a><a name="p15204162413"></a>Can be updated without replacement.</p>
</li></ul>
</li></ul>
</td>
</tr>
<tr id="row78441453217"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p484454532110"><a name="p484454532110"></a><a name="p484454532110"></a>vpc_id</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p55435388184243"><a name="p55435388184243"></a><a name="p55435388184243"></a>Virtual private cloud ID.</p>
<p id="p29156446184243"><a name="p29156446184243"></a><a name="p29156446184243"></a>String value expected.</p>
<p id="p61081429184243"><a name="p61081429184243"></a><a name="p61081429184243"></a>Updates cause replacement.</p>
</td>
</tr>
</tbody>
</table>

## Optional Properties<a name="section412515351744"></a>

<a name="table81553293812"></a>
<table><thead align="left"><tr id="row1286685152514"><th class="cellrowborder" valign="top" width="33%" id="mcps1.1.3.1.1"><p id="p12361181952519"><a name="p12361181952519"></a><a name="p12361181952519"></a><strong id="b1736111194257"><a name="b1736111194257"></a><a name="b1736111194257"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="67%" id="mcps1.1.3.1.2"><p id="p17362101972510"><a name="p17362101972510"></a><a name="p17362101972510"></a><strong id="b173622193254"><a name="b173622193254"></a><a name="b173622193254"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1586612562514"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p8269626172513"><a name="p8269626172513"></a><a name="p8269626172513"></a>desire_instance_number</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p16298362184344"><a name="p16298362184344"></a><a name="p16298362184344"></a>Desired instance number allowed in autoscaling group.</p>
<p id="p12467533184344"><a name="p12467533184344"></a><a name="p12467533184344"></a>Integer value expected.</p>
<p id="p45098939184344"><a name="p45098939184344"></a><a name="p45098939184344"></a>Can be updated without replacement.</p>
</td>
</tr>
<tr id="row138665516254"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p686615582515"><a name="p686615582515"></a><a name="p686615582515"></a>min_instance_number</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p60892081184344"><a name="p60892081184344"></a><a name="p60892081184344"></a>The minimum instance number allowed in autoscaling group.</p>
<p id="p11157825184344"><a name="p11157825184344"></a><a name="p11157825184344"></a>Integer value expected.</p>
<p id="p33311568184344"><a name="p33311568184344"></a><a name="p33311568184344"></a>Can be updated without replacement.</p>
</td>
</tr>
<tr id="row186611582516"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p9866135172516"><a name="p9866135172516"></a><a name="p9866135172516"></a>max_instance_number</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p57833818184344"><a name="p57833818184344"></a><a name="p57833818184344"></a>The max instance number allowed in autoscaling group.</p>
<p id="p50742320184344"><a name="p50742320184344"></a><a name="p50742320184344"></a>Integer value expected.</p>
<p id="p54027697184344"><a name="p54027697184344"></a><a name="p54027697184344"></a>Can be updated without replacement.</p>
<div class="note" id="note16323175916509"><a name="note16323175916509"></a><a name="note16323175916509"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p16483731195117"><a name="p16483731195117"></a><a name="p16483731195117"></a>The max instance number can not be smaller than the minimum instance number, can be equal. The value must be greater than 0.</p>
</div></div>
</td>
</tr>
<tr id="row386675142519"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p386655152512"><a name="p386655152512"></a><a name="p386655152512"></a>cool_down_time</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p60397425184344"><a name="p60397425184344"></a><a name="p60397425184344"></a>Cool down period, in seconds.</p>
<p id="p6705917184344"><a name="p6705917184344"></a><a name="p6705917184344"></a>Integer value expected.</p>
<p id="p60353258184344"><a name="p60353258184344"></a><a name="p60353258184344"></a>Can be updated without replacement.</p>
<p id="p19715566181747"><a name="p19715566181747"></a><a name="p19715566181747"></a>Range from 0 to 86400, include 0 and 86400.</p>
</td>
</tr>
<tr id="row118665517251"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p11866195192519"><a name="p11866195192519"></a><a name="p11866195192519"></a>lb_listener_id</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p41219835184344"><a name="p41219835184344"></a><a name="p41219835184344"></a>ELB listener ID.</p>
<p id="p35434199184344"><a name="p35434199184344"></a><a name="p35434199184344"></a>String value expected.</p>
<p id="p50472337184344"><a name="p50472337184344"></a><a name="p50472337184344"></a>Can be updated without replacement.</p>
</td>
</tr>
<tr id="row886617572515"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p1586620542514"><a name="p1586620542514"></a><a name="p1586620542514"></a>lbaas_listeners</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p18676293184344"><a name="p18676293184344"></a><a name="p18676293184344"></a>Lbaas listener, which is mutually exclusive with lb_listener_id.</p>
<p id="p33868913184344"><a name="p33868913184344"></a><a name="p33868913184344"></a>List value expected.</p>
<p id="p36384769184344"><a name="p36384769184344"></a><a name="p36384769184344"></a>Can be updated without replacement.</p>
<p id="p65406103182528"><a name="p65406103182528"></a><a name="p65406103182528"></a><em id="i51784016182528"><a name="i51784016182528"></a><a name="i51784016182528"></a>List contents:</em></p>
<a name="ul5680771"></a><a name="ul5680771"></a><ul id="ul5680771"><li>*<p id="p35366507182528"><a name="p35366507182528"></a><a name="p35366507182528"></a>Map value expected.</p>
<p id="p49863111182528"><a name="p49863111182528"></a><a name="p49863111182528"></a>Can be updated without replacement.</p>
<p id="p1311975620276"><a name="p1311975620276"></a><a name="p1311975620276"></a><em id="i12380181182528"><a name="i12380181182528"></a><a name="i12380181182528"></a>Map properties:</em></p>
<a name="ul23821911141113"></a><a name="ul23821911141113"></a><ul id="ul23821911141113"><li>listener_id<p id="p62258621182710"><a name="p62258621182710"></a><a name="p62258621182710"></a>The listener id of the elastic load balancer.</p>
<p id="p24645599182528"><a name="p24645599182528"></a><a name="p24645599182528"></a>String value expected.</p>
<p id="p1051502320289"><a name="p1051502320289"></a><a name="p1051502320289"></a>Can be updated without replacement.</p>
</li><li>protocol_port<p id="p44576772182834"><a name="p44576772182834"></a><a name="p44576772182834"></a>The port that backend server listens.</p>
<p id="p26979935182726"><a name="p26979935182726"></a><a name="p26979935182726"></a>Integer value expected.</p>
<p id="p41492825182726"><a name="p41492825182726"></a><a name="p41492825182726"></a>Can be updated without replacement.</p>
<p id="p13539731182814"><a name="p13539731182814"></a><a name="p13539731182814"></a>Range from 1 to 65535, include 1 and 65535.</p>
</li><li>weight<p id="p51229245183056"><a name="p51229245183056"></a><a name="p51229245183056"></a>The request rate that backend server receive.</p>
<p id="p66006743182727"><a name="p66006743182727"></a><a name="p66006743182727"></a>Integer value expected.</p>
<p id="p57189778182727"><a name="p57189778182727"></a><a name="p57189778182727"></a>Can be updated without replacement.</p>
<p id="p1467814396286"><a name="p1467814396286"></a><a name="p1467814396286"></a>Range from 0 to 256, include 0 and 256.</p>
</li></ul>
</li></ul>
</td>
</tr>
<tr id="row108668513251"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p1086619592512"><a name="p1086619592512"></a><a name="p1086619592512"></a>available_zones</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p16495652184344"><a name="p16495652184344"></a><a name="p16495652184344"></a>An ordered list of available zones used to create instances.</p>
<p id="p14243146184344"><a name="p14243146184344"></a><a name="p14243146184344"></a>List value expected.</p>
<p id="p61079456184344"><a name="p61079456184344"></a><a name="p61079456184344"></a>Can be updated without replacement.</p>
</td>
</tr>
<tr id="row198661519257"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p138668582512"><a name="p138668582512"></a><a name="p138668582512"></a>health_periodic_audit_method</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p33747254184344"><a name="p33747254184344"></a><a name="p33747254184344"></a>The health periodic audit method, when the lb_listener_id and lbaas_listeners parameter is set, the default is ELB_AUDIT, otherwise, it defaults to NOVA_AUDIT.</p>
<p id="p35289830184344"><a name="p35289830184344"></a><a name="p35289830184344"></a>String value expected.</p>
<p id="p49173020184344"><a name="p49173020184344"></a><a name="p49173020184344"></a>Can be updated without replacement.</p>
<p id="p39904000184344"><a name="p39904000184344"></a><a name="p39904000184344"></a>Allowed values: ELB_AUDIT, NOVA_AUDIT</p>
</td>
</tr>
<tr id="row138665513253"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p1386611517258"><a name="p1386611517258"></a><a name="p1386611517258"></a>health_periodic_audit_time</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p18468009184344"><a name="p18468009184344"></a><a name="p18468009184344"></a>The health periodic audit time, in minutes.</p>
<p id="p31994354184344"><a name="p31994354184344"></a><a name="p31994354184344"></a>Integer value expected.</p>
<p id="p19513736184344"><a name="p19513736184344"></a><a name="p19513736184344"></a>Can be updated without replacement.</p>
<p id="p41405899184344"><a name="p41405899184344"></a><a name="p41405899184344"></a>Allowed values: 5, 15, 60, 180</p>
</td>
</tr>
<tr id="row986618512518"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p14866959259"><a name="p14866959259"></a><a name="p14866959259"></a>instance_terminate_policy</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p53020516184344"><a name="p53020516184344"></a><a name="p53020516184344"></a>The policy of terminating instances.</p>
<p id="p7422597184344"><a name="p7422597184344"></a><a name="p7422597184344"></a>String value expected.</p>
<p id="p66803376184344"><a name="p66803376184344"></a><a name="p66803376184344"></a>Can be updated without replacement.</p>
<p id="p64359479184344"><a name="p64359479184344"></a><a name="p64359479184344"></a>Allowed values: OLD_CONFIG_OLD_INSTANCE, OLD_CONFIG_NEW_INSTANCE, OLD_INSTANCE, NEW_INSTANCE</p>
<a name="ul712121695411"></a><a name="ul712121695411"></a><ul id="ul712121695411"><li>OLD_CONFIG_OLD_INSTANCE: The oldest instance created based on the oldest configuration is removed from the AS group first.</li><li>OLD_CONFIG_NEW_INSTANCE: The latest instance created based on the oldest configuration is removed from the AS group first.</li><li>OLD_INSTANCE: The oldest instance is removed from the AS group first.</li><li>NEW_INSTANCE: The latest instance is removed from the AS group first.</li></ul>
</td>
</tr>
<tr id="row786685132519"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p158661252258"><a name="p158661252258"></a><a name="p158661252258"></a>delete_publicip</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p8964495184344"><a name="p8964495184344"></a><a name="p8964495184344"></a>Whether to delete the elastic ip when terminating instances.</p>
<p id="p13571596184344"><a name="p13571596184344"></a><a name="p13571596184344"></a>Boolean value expected.</p>
<p id="p55035505184344"><a name="p55035505184344"></a><a name="p55035505184344"></a>Can be updated without replacement.</p>
</td>
</tr>
</tbody>
</table>

## Attributes<a name="section1212254519419"></a>

<a name="table93994512167"></a>
<table><thead align="left"><tr id="row9749123216313"><th class="cellrowborder" valign="top" width="33%" id="mcps1.1.3.1.1"><p id="p6716174616318"><a name="p6716174616318"></a><a name="p6716174616318"></a><strong id="b1871674623117"><a name="b1871674623117"></a><a name="b1871674623117"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="67%" id="mcps1.1.3.1.2"><p id="p1571814603119"><a name="p1571814603119"></a><a name="p1571814603119"></a><strong id="b10719174615316"><a name="b10719174615316"></a><a name="b10719174615316"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row2749153213114"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p2749103216315"><a name="p2749103216315"></a><a name="p2749103216315"></a>instances</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p97491732153119"><a name="p97491732153119"></a><a name="p97491732153119"></a>A list of all instances information. The information of instances may be obtained through the following expression: "{ get_attr: [&lt;autoscaling_group_resource_name&gt;, instances] }".</p>
</td>
</tr>
</tbody>
</table>

## HOT Syntax<a name="section13111583410"></a>

```
heat_template_version: 2014-10-16
...
resources:
  ...
  the_resource:
    type: OSE::AS::ScalingGroup
    properties:
      scaling_group_name: String
      scaling_configuration_id: String
      desire_instance_number: Integer
      min_instance_number: Integer
      max_instance_number: Integer
      cool_down_time: Integer
      lb_listener_id: String
      available_zones: [String, String,…]
      networks: [String, String,…]
      security_groups: [{"id": String}, {"id":  String},…]
      vpc_id: String
      health_periodic_audit_method: String
      health_periodic_audit_time: Integer
      instance_terminate_policy: String
      notifications: [String, String,…]
      delete_publicip: Boolean
```

