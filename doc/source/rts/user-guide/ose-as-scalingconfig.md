# OSE::AS::ScalingConfig<a name="EN-US_TOPIC_0088407096"></a>

A resource for managing autoscaling configuration.

## Required Properties<a name="section08439872"></a>

<a name="table1873317541955"></a>
<table><thead align="left"><tr id="row1783818147210"><th class="cellrowborder" valign="top" width="31%" id="mcps1.1.3.1.1"><p id="p13734554251"><a name="p13734554251"></a><a name="p13734554251"></a><strong id="b1158213583014"><a name="b1158213583014"></a><a name="b1158213583014"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="69%" id="mcps1.1.3.1.2"><p id="p37342541351"><a name="p37342541351"></a><a name="p37342541351"></a><strong id="b25821557307"><a name="b25821557307"></a><a name="b25821557307"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1583812141124"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p7734854654"><a name="p7734854654"></a><a name="p7734854654"></a>scaling_configuration_name</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p40871265"><a name="p40871265"></a><a name="p40871265"></a>Autoscaling configuration name.</p>
<p id="p32297070"><a name="p32297070"></a><a name="p32297070"></a>String value expected.</p>
<p id="p22238181"><a name="p22238181"></a><a name="p22238181"></a>Updates cause replacement.</p>
<p id="p632418514253"><a name="p632418514253"></a><a name="p632418514253"></a>It is allowed to start with <strong id="b1279613252309"><a name="b1279613252309"></a><a name="b1279613252309"></a>numbers</strong>, <strong id="b107201029113015"><a name="b107201029113015"></a><a name="b107201029113015"></a>letters</strong>, _, and <strong id="b9809184113309"><a name="b9809184113309"></a><a name="b9809184113309"></a>-</strong> characters. It is allowed to include <strong id="b22921519153119"><a name="b22921519153119"></a><a name="b22921519153119"></a>numbers</strong>, <strong id="b929441919312"><a name="b929441919312"></a><a name="b929441919312"></a>letters</strong>, _, and <strong id="b5295111983114"><a name="b5295111983114"></a><a name="b5295111983114"></a>-</strong> characters, and the string length is <strong id="b547314383115"><a name="b547314383115"></a><a name="b547314383115"></a>1</strong> to <strong id="b55691446103119"><a name="b55691446103119"></a><a name="b55691446103119"></a>64</strong>.</p>
</td>
</tr>
<tr id="row483815142214"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p1773415549513"><a name="p1773415549513"></a><a name="p1773415549513"></a>instance_config</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p38397760"><a name="p38397760"></a><a name="p38397760"></a>Instance configuration.</p>
<p id="p10035525"><a name="p10035525"></a><a name="p10035525"></a>Map value expected.</p>
<p id="p23210864"><a name="p23210864"></a><a name="p23210864"></a>Updates cause replacement.</p>
<p id="p7571186"><a name="p7571186"></a><a name="p7571186"></a><em id="i60490187183831"><a name="i60490187183831"></a><a name="i60490187183831"></a>Map properties:</em></p>
<a name="ul9286311"></a><a name="ul9286311"></a><ul id="ul9286311"><li>instance_id<p id="p3209192918130"><a name="p3209192918130"></a><a name="p3209192918130"></a>Cloud server ID, if instance_id is specified, it will use this existing instance as a bus dtemplate to create an autoscaling configuration. The flavorRef, imageRef, and disk fields do not take effect at this time. The flavorRef, imageRef, and disk fields are required when the instance_id field is not passed in.</p>
<p id="p3210182971316"><a name="p3210182971316"></a><a name="p3210182971316"></a>String value expected.</p>
<p id="p1121092971316"><a name="p1121092971316"></a><a name="p1121092971316"></a>Updates cause replacement.</p>
</li><li>flavorRef<p id="p15237148151316"><a name="p15237148151316"></a><a name="p15237148151316"></a>Cloud server specification ID, which defines the cloud server CPUs and memory size.</p>
<p id="p8237154891311"><a name="p8237154891311"></a><a name="p8237154891311"></a>String value expected.</p>
<p id="p142381548131311"><a name="p142381548131311"></a><a name="p142381548131311"></a>Updates cause replacement.</p>
</li><li>imageRef<p id="p7523160191419"><a name="p7523160191419"></a><a name="p7523160191419"></a>Image ID.</p>
<p id="p155242005148"><a name="p155242005148"></a><a name="p155242005148"></a>String value expected.</p>
<p id="p85250021414"><a name="p85250021414"></a><a name="p85250021414"></a>Updates cause replacement.</p>
</li><li>disk<p id="p25501120191412"><a name="p25501120191412"></a><a name="p25501120191412"></a>Disk group information, system disk must be selected, data disk is optional.</p>
<p id="p1455192041410"><a name="p1455192041410"></a><a name="p1455192041410"></a>List value expected.</p>
<p id="p8552720101410"><a name="p8552720101410"></a><a name="p8552720101410"></a>Updates cause replacement.</p>
<p id="p6553112018149"><a name="p6553112018149"></a><a name="p6553112018149"></a><em id="i48949182183831"><a name="i48949182183831"></a><a name="i48949182183831"></a>List contents:</em></p>
<a name="ul823513314141"></a><a name="ul823513314141"></a><ul id="ul823513314141"><li>*<p id="p3398145319148"><a name="p3398145319148"></a><a name="p3398145319148"></a>Map value expected.</p>
<p id="p7399155319148"><a name="p7399155319148"></a><a name="p7399155319148"></a>Updates cause replacement.</p>
<p id="p1140011536145"><a name="p1140011536145"></a><a name="p1140011536145"></a><em id="i59377795183831"><a name="i59377795183831"></a><a name="i59377795183831"></a>Map properties:</em></p>
<p id="p1637945891410"><a name="p1637945891410"></a><a name="p1637945891410"></a>- size</p>
<p id="p76001031615"><a name="p76001031615"></a><a name="p76001031615"></a>Disk size, in GB.</p>
<p id="p8600706168"><a name="p8600706168"></a><a name="p8600706168"></a>Integer value expected.</p>
<p id="p166011801161"><a name="p166011801161"></a><a name="p166011801161"></a>Updates cause replacement.</p>
<p id="p1960280161612"><a name="p1960280161612"></a><a name="p1960280161612"></a>The size of system disk is range from 140 to 32768, include 140 and 32768.</p>
<p id="p3603505169"><a name="p3603505169"></a><a name="p3603505169"></a>The size of data disk is range from 10 to 32768, include 10 and 32768.</p>
<p id="p25061164161"><a name="p25061164161"></a><a name="p25061164161"></a>- volume_type</p>
<p id="p10973203811620"><a name="p10973203811620"></a><a name="p10973203811620"></a>The type of volume.</p>
<p id="p1297483881619"><a name="p1297483881619"></a><a name="p1297483881619"></a>String value expected.</p>
<p id="p11975123815165"><a name="p11975123815165"></a><a name="p11975123815165"></a>Updates cause replacement.</p>
<p id="p2975938171612"><a name="p2975938171612"></a><a name="p2975938171612"></a>Allowed values: SSD, SATA, SAS, uh-l1 (Ultra-high I/O (Latency optimized)).</p>
<p id="p169480314154"><a name="p169480314154"></a><a name="p169480314154"></a>- disk_type</p>
<p id="p97619891710"><a name="p97619891710"></a><a name="p97619891710"></a>Disk type, system disk or data disk.</p>
<p id="p167658111719"><a name="p167658111719"></a><a name="p167658111719"></a>String value expected.</p>
<p id="p1078384171"><a name="p1078384171"></a><a name="p1078384171"></a>Updates cause replacement.</p>
<p id="p97813815172"><a name="p97813815172"></a><a name="p97813815172"></a>Allowed values: SYS, DATA</p>
</li></ul>
</li><li>key_name<p id="p1028916568171"><a name="p1028916568171"></a><a name="p1028916568171"></a>SSH key name to logon server, which mutually exclusive with adminPass.</p>
<p id="p729016566178"><a name="p729016566178"></a><a name="p729016566178"></a>String value expected.</p>
<p id="p8290356171711"><a name="p8290356171711"></a><a name="p8290356171711"></a>Updates cause replacement.</p>
</li><li>adminPass<p id="p97161619186"><a name="p97161619186"></a><a name="p97161619186"></a>Initial password for administrator account.</p>
<p id="p1571181691820"><a name="p1571181691820"></a><a name="p1571181691820"></a>String value expected.</p>
<p id="p19711416111810"><a name="p19711416111810"></a><a name="p19711416111810"></a>Updates cause replacement.</p>
<p id="p47231614189"><a name="p47231614189"></a><a name="p47231614189"></a>The length is range from 8 to 26. The password can only contain letters, numbers, and special characters, namely "!@$%^-_=+[{}]:,./?". It must contain at least three of the four characters. The password can not contain user name or the reverse of it.</p>
</li><li>personality<p id="p17285747171814"><a name="p17285747171814"></a><a name="p17285747171814"></a>File inject content.</p>
<p id="p228617477188"><a name="p228617477188"></a><a name="p228617477188"></a>List value expected.</p>
<p id="p42873474180"><a name="p42873474180"></a><a name="p42873474180"></a>Updates cause replacement.</p>
<p id="p32885471184"><a name="p32885471184"></a><a name="p32885471184"></a>Only support the injection of text files, the maximum is five. The maximum size of each file is 1KB.</p>
<p id="p13289144741815"><a name="p13289144741815"></a><a name="p13289144741815"></a><em id="i1368925852813"><a name="i1368925852813"></a><a name="i1368925852813"></a>List contents:</em></p>
<a name="ul11590110161915"></a><a name="ul11590110161915"></a><ul id="ul11590110161915"><li>*<p id="p10593908193"><a name="p10593908193"></a><a name="p10593908193"></a>Map value expected.</p>
<p id="p135942031911"><a name="p135942031911"></a><a name="p135942031911"></a>Updates cause replacement.</p>
<p id="p175942011199"><a name="p175942011199"></a><a name="p175942011199"></a><em id="i7770173822918"><a name="i7770173822918"></a><a name="i7770173822918"></a>Map properties:</em></p>
<p id="p865813271917"><a name="p865813271917"></a><a name="p865813271917"></a>- path</p>
<p id="p123535396197"><a name="p123535396197"></a><a name="p123535396197"></a>Path of the injected file.</p>
<p id="p13354103961916"><a name="p13354103961916"></a><a name="p13354103961916"></a>String value expected.</p>
<p id="p135416392197"><a name="p135416392197"></a><a name="p135416392197"></a>Updates cause replacement.</p>
<p id="p6336124671917"><a name="p6336124671917"></a><a name="p6336124671917"></a>- content</p>
<p id="p3907181002017"><a name="p3907181002017"></a><a name="p3907181002017"></a>Content of the injected file.</p>
<p id="p6908210172015"><a name="p6908210172015"></a><a name="p6908210172015"></a>String value expected.</p>
<p id="p1990951010204"><a name="p1990951010204"></a><a name="p1990951010204"></a>Updates cause replacement.</p>
<p id="p16910010132016"><a name="p16910010132016"></a><a name="p16910010132016"></a>The content must be encoded by base64.</p>
</li></ul>
</li><li>public_ip<p id="p144081546152010"><a name="p144081546152010"></a><a name="p144081546152010"></a>Elastic IP information.</p>
<p id="p17409154612205"><a name="p17409154612205"></a><a name="p17409154612205"></a>Map value expected.</p>
<p id="p54101746132014"><a name="p54101746132014"></a><a name="p54101746132014"></a>Updates cause replacement.</p>
<p id="p94111846172019"><a name="p94111846172019"></a><a name="p94111846172019"></a><em id="i11661871337"><a name="i11661871337"></a><a name="i11661871337"></a>Map properties:</em></p>
<a name="ul15336112382120"></a><a name="ul15336112382120"></a><ul id="ul15336112382120"><li>eip<p id="p1333917235219"><a name="p1333917235219"></a><a name="p1333917235219"></a>Elastic IP configuration parameters.</p>
<p id="p14340723122113"><a name="p14340723122113"></a><a name="p14340723122113"></a>Map value expected.</p>
<p id="p153421623112113"><a name="p153421623112113"></a><a name="p153421623112113"></a>Updates cause replacement.</p>
<p id="p6343142318216"><a name="p6343142318216"></a><a name="p6343142318216"></a><em id="i74621932173311"><a name="i74621932173311"></a><a name="i74621932173311"></a>Map properties:</em></p>
<p id="p20495025142113"><a name="p20495025142113"></a><a name="p20495025142113"></a>- ip_type</p>
<p id="p277275011217"><a name="p277275011217"></a><a name="p277275011217"></a>The type of IP.</p>
<p id="p127731450192117"><a name="p127731450192117"></a><a name="p127731450192117"></a>String value expected.</p>
<p id="p477416505213"><a name="p477416505213"></a><a name="p477416505213"></a>Updates cause replacement.</p>
<p id="p1677565020219"><a name="p1677565020219"></a><a name="p1677565020219"></a>Allowed values: 5_bgp, 5_lxbgp, 5_telcom, 5_union</p>
<p id="p1690014107220"><a name="p1690014107220"></a><a name="p1690014107220"></a>- bandwidth</p>
<p id="p206078252225"><a name="p206078252225"></a><a name="p206078252225"></a>IP address bandwidth.</p>
<p id="p17608102520229"><a name="p17608102520229"></a><a name="p17608102520229"></a>Map value expected.</p>
<p id="p6609192515220"><a name="p6609192515220"></a><a name="p6609192515220"></a>Updates cause replacement.</p>
<p id="p561062542211"><a name="p561062542211"></a><a name="p561062542211"></a><em id="i507215379"><a name="i507215379"></a><a name="i507215379"></a>Map properties:</em></p>
<p id="p693133472214"><a name="p693133472214"></a><a name="p693133472214"></a>- size</p>
<p id="p1992317283232"><a name="p1992317283232"></a><a name="p1992317283232"></a>The size of bandwidth.</p>
<p id="p1924728142317"><a name="p1924728142317"></a><a name="p1924728142317"></a>Integer value expected.</p>
<p id="p4925132813233"><a name="p4925132813233"></a><a name="p4925132813233"></a>Updates cause replacement.</p>
<p id="p4925328112317"><a name="p4925328112317"></a><a name="p4925328112317"></a>Range from 1 to 300, include 1 and 300.</p>
<p id="p8514204232319"><a name="p8514204232319"></a><a name="p8514204232319"></a>- share_type</p>
<p id="p193391752249"><a name="p193391752249"></a><a name="p193391752249"></a>The share type of bandwidth.</p>
<p id="p0340185132414"><a name="p0340185132414"></a><a name="p0340185132414"></a>String value expected.</p>
<p id="p1834110592410"><a name="p1834110592410"></a><a name="p1834110592410"></a>Updates cause replacement.</p>
<p id="p1134217516247"><a name="p1134217516247"></a><a name="p1134217516247"></a>Allowed values: PER</p>
<p id="p167386252249"><a name="p167386252249"></a><a name="p167386252249"></a>- charging_mode</p>
<p id="p1822837112419"><a name="p1822837112419"></a><a name="p1822837112419"></a>The charging mode of bandwidth.</p>
<p id="p82314375244"><a name="p82314375244"></a><a name="p82314375244"></a>String value expected.</p>
<p id="p524203711247"><a name="p524203711247"></a><a name="p524203711247"></a>Updates cause replacement.</p>
<p id="p1325113782417"><a name="p1325113782417"></a><a name="p1325113782417"></a>Allowed values: bandwidth, traffic</p>
</li></ul>
</li><li>user_data<p id="p831416852518"><a name="p831416852518"></a><a name="p831416852518"></a>Cloud-init user data.</p>
<p id="p231548162510"><a name="p231548162510"></a><a name="p231548162510"></a>String value expected.</p>
<p id="p19315783255"><a name="p19315783255"></a><a name="p19315783255"></a>Updates cause replacement.</p>
</li><li>metadata<p id="p1675062482514"><a name="p1675062482514"></a><a name="p1675062482514"></a>Metadata for creating cloud server.</p>
<p id="p1075115249257"><a name="p1075115249257"></a><a name="p1075115249257"></a>Map value expected.</p>
<p id="p137521624192510"><a name="p137521624192510"></a><a name="p137521624192510"></a>Updates cause replacement.</p>
</li></ul>
</td>
</tr>
</tbody>
</table>

## HOT Syntax<a name="section049034814710"></a>

```
heat_template_version: 2014-10-16
...
resources:
  ...
  the_resource:
    type: OSE::AS::ScalingConfig
    properties:
      scaling_configuration_name: String
      instance_config:
      key_name: String
      flavorRef: String
      imageRef: String
      disk: [{"disk_type": String, "size":  Integer, "volume_type": String}, {"disk_type": String, "size": Integer,  "volume_type": String},…]
      personality: [{"path": String, "content":  String}, {"path": String, "content": String},…]
      public_ip: {"eip": {"ip_type": String,  "bandwidth": {"size": Integer, "share_type": String, "charging_mode": String}}}
      user_data: String
      metadata: {…}
```

