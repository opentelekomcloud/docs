# OS::Heat::SoftwareConfig<a name="EN-US_TOPIC_0088407192"></a>

A resource for describing and storing software configuration.

The software\_configs API which backs this resource creates immutable configs, so any change to the template resource definition will result in a new config being created, and the old one being deleted.

Configs can be defined in the same template which uses them, or they can be created in one stack, and passed to another stack via a parameter.

A config resource can be referenced in other resource properties which are config-aware. This includes the properties OS::Nova::Server user\_data, OS::Heat::SoftwareDeployment config and OS::Heat::MultipartMime parts config.

Along with the config script itself, this resource can define schemas for inputs and outputs which the config script is expected to consume and produce. Inputs and outputs are optional and will map to concepts which are specific to the configuration tool being used.

>![](/images/icon-note.gif) **NOTE:**   
>If the software configuration function is used, the cloud-init tool must be installed on images.  

## Optional Properties<a name="section1025082782011"></a>

<a name="table268216573215"></a>
<table><thead align="left"><tr id="row11570145804512"><th class="cellrowborder" valign="top" width="33%" id="mcps1.1.3.1.1"><p id="p3570658124516"><a name="p3570658124516"></a><a name="p3570658124516"></a><strong id="b2095215144610"><a name="b2095215144610"></a><a name="b2095215144610"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="67%" id="mcps1.1.3.1.2"><p id="p4570058164519"><a name="p4570058164519"></a><a name="p4570058164519"></a><strong id="b11971315204613"><a name="b11971315204613"></a><a name="b11971315204613"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row0570105894514"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p35702585451"><a name="p35702585451"></a><a name="p35702585451"></a>config</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p14400487"><a name="p14400487"></a><a name="p14400487"></a>Configuration script or manifest which specifies what actual configuration is performed.</p>
<p id="p62495522"><a name="p62495522"></a><a name="p62495522"></a>String value expected.</p>
<p id="p25588789"><a name="p25588789"></a><a name="p25588789"></a>Updates cause replacement.</p>
</td>
</tr>
<tr id="row13570165804518"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p1957055894510"><a name="p1957055894510"></a><a name="p1957055894510"></a>group</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p59426032"><a name="p59426032"></a><a name="p59426032"></a>Namespace to group this software config by when delivered to a server. This may imply what configuration tool is going to perform the configuration.</p>
<p id="p65072241"><a name="p65072241"></a><a name="p65072241"></a>String value expected.</p>
<p id="p48779263"><a name="p48779263"></a><a name="p48779263"></a>Updates cause replacement.</p>
<p id="p36360186"><a name="p36360186"></a><a name="p36360186"></a>Defaults to "Heat::Ungrouped".</p>
</td>
</tr>
<tr id="row125708581452"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p11570175804513"><a name="p11570175804513"></a><a name="p11570175804513"></a>inputs</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p59493923"><a name="p59493923"></a><a name="p59493923"></a>Schema representing the inputs that this software config is expecting.</p>
<p id="p65683259"><a name="p65683259"></a><a name="p65683259"></a>List value expected.</p>
<p id="p54278420"><a name="p54278420"></a><a name="p54278420"></a>Updates cause replacement.</p>
<p id="p18743735"><a name="p18743735"></a><a name="p18743735"></a><em id="i34475894"><a name="i34475894"></a><a name="i34475894"></a>List contents:</em></p>
<a name="ul409500"></a><a name="ul409500"></a><ul id="ul409500"><li>*<p id="p34211830"><a name="p34211830"></a><a name="p34211830"></a>Map value expected.</p>
<p id="p39471019"><a name="p39471019"></a><a name="p39471019"></a>Updates cause replacement.</p>
<p id="p14356171012474"><a name="p14356171012474"></a><a name="p14356171012474"></a><em id="i43035983"><a name="i43035983"></a><a name="i43035983"></a>Map properties:</em></p>
<a name="ul163813915232"></a><a name="ul163813915232"></a><ul id="ul163813915232"><li>default<p id="p33392154"><a name="p33392154"></a><a name="p33392154"></a>Default value for the input if none is specified.</p>
<p id="p32093935"><a name="p32093935"></a><a name="p32093935"></a>String value expected.</p>
<p id="p16887113374710"><a name="p16887113374710"></a><a name="p16887113374710"></a>Updates cause replacement.</p>
</li><li>description<p id="p47803537"><a name="p47803537"></a><a name="p47803537"></a>Description of the input.</p>
<p id="p27578655"><a name="p27578655"></a><a name="p27578655"></a>String value expected.</p>
<p id="p9825104204713"><a name="p9825104204713"></a><a name="p9825104204713"></a>Updates cause replacement.</p>
</li><li>name<p id="p18058533"><a name="p18058533"></a><a name="p18058533"></a>Name of the input.</p>
<p id="p28309076"><a name="p28309076"></a><a name="p28309076"></a>String value expected.</p>
<p id="p154815566479"><a name="p154815566479"></a><a name="p154815566479"></a>Updates cause replacement.</p>
</li><li>replace_on_change<p id="p45626804"><a name="p45626804"></a><a name="p45626804"></a>Replace the deployment instead of updating it when the input value changes.</p>
<p id="p7988053"><a name="p7988053"></a><a name="p7988053"></a>Boolean value expected.</p>
<p id="p4783620"><a name="p4783620"></a><a name="p4783620"></a>Updates cause replacement.</p>
<p id="p0436094483"><a name="p0436094483"></a><a name="p0436094483"></a>Defaults to "False".</p>
</li><li>type<p id="p45495342"><a name="p45495342"></a><a name="p45495342"></a>Type of the value of the input.</p>
<p id="p6804902"><a name="p6804902"></a><a name="p6804902"></a>String value expected.</p>
<p id="p61244120"><a name="p61244120"></a><a name="p61244120"></a>Updates cause replacement.</p>
<p id="p14326175"><a name="p14326175"></a><a name="p14326175"></a>Defaults to "String".</p>
<p id="p1261112229480"><a name="p1261112229480"></a><a name="p1261112229480"></a>Allowed values: String, Number, CommaDelimitedList, Json, Boolean</p>
</li></ul>
</li></ul>
</td>
</tr>
<tr id="row0570205812452"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p1857018581455"><a name="p1857018581455"></a><a name="p1857018581455"></a>options</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p41907998"><a name="p41907998"></a><a name="p41907998"></a>Map containing options specific to the configuration management tool used by this resource.</p>
<p id="p41627663"><a name="p41627663"></a><a name="p41627663"></a>Map value expected.</p>
<p id="p39104649"><a name="p39104649"></a><a name="p39104649"></a>Updates cause replacement.</p>
</td>
</tr>
<tr id="row85700589452"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p45701958184519"><a name="p45701958184519"></a><a name="p45701958184519"></a>outputs</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p13360005"><a name="p13360005"></a><a name="p13360005"></a>Schema representing the outputs that this software config will produce.</p>
<p id="p53131185"><a name="p53131185"></a><a name="p53131185"></a>List value expected.</p>
<p id="p8418617"><a name="p8418617"></a><a name="p8418617"></a>Updates cause replacement.</p>
<p id="p8658696"><a name="p8658696"></a><a name="p8658696"></a><em id="i10819406"><a name="i10819406"></a><a name="i10819406"></a>List contents:</em></p>
<a name="ul22073660"></a><a name="ul22073660"></a><ul id="ul22073660"><li>*<p id="p35610445"><a name="p35610445"></a><a name="p35610445"></a>Map value expected.</p>
<p id="p52058554"><a name="p52058554"></a><a name="p52058554"></a>Updates cause replacement.</p>
<p id="p2420104434912"><a name="p2420104434912"></a><a name="p2420104434912"></a><em id="i55993312"><a name="i55993312"></a><a name="i55993312"></a>Map properties:</em></p>
<a name="ul1645612022717"></a><a name="ul1645612022717"></a><ul id="ul1645612022717"><li>description<p id="p16935490"><a name="p16935490"></a><a name="p16935490"></a>Description of the output.</p>
<p id="p18201686"><a name="p18201686"></a><a name="p18201686"></a>String value expected.</p>
<p id="p2155791509"><a name="p2155791509"></a><a name="p2155791509"></a>Updates cause replacement.</p>
</li><li>error_output<p id="p34598031"><a name="p34598031"></a><a name="p34598031"></a>Denotes that the deployment is in an error state if this output has a value.</p>
<p id="p42946824"><a name="p42946824"></a><a name="p42946824"></a>Boolean value expected.</p>
<p id="p50977096"><a name="p50977096"></a><a name="p50977096"></a>Updates cause replacement.</p>
<p id="p1324063114508"><a name="p1324063114508"></a><a name="p1324063114508"></a>Defaults to "False".</p>
</li><li>name<p id="p57257659"><a name="p57257659"></a><a name="p57257659"></a>Name of the output.</p>
<p id="p45556885"><a name="p45556885"></a><a name="p45556885"></a>String value expected.</p>
<p id="p9465193918509"><a name="p9465193918509"></a><a name="p9465193918509"></a>Updates cause replacement.</p>
</li><li>type<p id="p62957461"><a name="p62957461"></a><a name="p62957461"></a>Type of the value of the output.</p>
<p id="p29746244"><a name="p29746244"></a><a name="p29746244"></a>String value expected.</p>
<p id="p66389604"><a name="p66389604"></a><a name="p66389604"></a>Updates cause replacement.</p>
<p id="p60635527"><a name="p60635527"></a><a name="p60635527"></a>Defaults to "String".</p>
<p id="p1471224816500"><a name="p1471224816500"></a><a name="p1471224816500"></a>Allowed values: String, Number, CommaDelimitedList, Json, Boolean</p>
</li></ul>
</li></ul>
</td>
</tr>
</tbody>
</table>

## Attributes<a name="section194581436132016"></a>

<a name="table1892313220288"></a>
<table><thead align="left"><tr id="row137151138195111"><th class="cellrowborder" valign="top" width="33%" id="mcps1.1.3.1.1"><p id="p1354935616512"><a name="p1354935616512"></a><a name="p1354935616512"></a><strong id="b8550456145116"><a name="b8550456145116"></a><a name="b8550456145116"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="67%" id="mcps1.1.3.1.2"><p id="p5551165614514"><a name="p5551165614514"></a><a name="p5551165614514"></a><strong id="b2551115612514"><a name="b2551115612514"></a><a name="b2551115612514"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row13715133815513"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p5715153855117"><a name="p5715153855117"></a><a name="p5715153855117"></a>config</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p3715143810512"><a name="p3715143810512"></a><a name="p3715143810512"></a>The config value of the software config.</p>
<p id="p12839321101115"><a name="p12839321101115"></a><a name="p12839321101115"></a>The config is generally read from a script file and often contains some parameter substitutions. The config value is the script content that actually runs in the virtual machine.</p>
</td>
</tr>
</tbody>
</table>

## HOT Syntax<a name="section187336105215"></a>

```
heat_template_version: 2014-10-16
...
resources:
  ...
  the_resource:
    type: OS::Heat::SoftwareConfig
    properties:
      config: String
      group: String
      inputs: [{"type": String, "default": String, "name": String, "replace_on_change": Boolean, "description": String}, {"type": String, "default": String, "name": String, "replace_on_change": Boolean, "description": String}, ...]
      options: {...}
      outputs: [{"type": String, "name": String, "error_output": Boolean, "description": String}, {"type": String, "name": String, "error_output": Boolean, "description": String}, ...]
```

