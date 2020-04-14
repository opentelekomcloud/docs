# OS::Heat::SoftwareComponent<a name="EN-US_TOPIC_0088407175"></a>

A resource for describing and storing a software component.

This resource is similar to OS::Heat::SoftwareConfig. In contrast to SoftwareConfig which allows for storing only one configuration \(e.g. one script\), SoftwareComponent allows for storing multiple configurations to address handling of all lifecycle hooks \(CREATE, UPDATE, DELETE\) for a software component in one place.

This resource is backed by the persistence layer and the API of the SoftwareConfig resource, and only adds handling for the additional configs property and attribute.

## Required Properties<a name="section204310408330"></a>

<a name="table1325512814216"></a>
<table><thead align="left"><tr id="row665424417345"><th class="cellrowborder" valign="top" width="36%" id="mcps1.1.3.1.1"><p id="p22561428624"><a name="p22561428624"></a><a name="p22561428624"></a><strong id="b13128120163513"><a name="b13128120163513"></a><a name="b13128120163513"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.1.3.1.2"><p id="p1825619281729"><a name="p1825619281729"></a><a name="p1825619281729"></a><strong id="b3129609353"><a name="b3129609353"></a><a name="b3129609353"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row56541144183410"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p52571328122"><a name="p52571328122"></a><a name="p52571328122"></a>configs</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p10607763"><a name="p10607763"></a><a name="p10607763"></a>The list of configurations for the different lifecycle actions of the represented software component.</p>
<p id="p28361011"><a name="p28361011"></a><a name="p28361011"></a>List value expected.</p>
<p id="p53922507"><a name="p53922507"></a><a name="p53922507"></a>Updates cause replacement.</p>
<p id="p15540517"><a name="p15540517"></a><a name="p15540517"></a>The length must be at least 1.</p>
<p id="p5646931"><a name="p5646931"></a><a name="p5646931"></a>List contents:</p>
<a name="ul50822380"></a><a name="ul50822380"></a><ul id="ul50822380"><li>*<p id="p18451219359"><a name="p18451219359"></a><a name="p18451219359"></a>Map value expected.</p>
<p id="p845142133511"><a name="p845142133511"></a><a name="p845142133511"></a>Updates cause replacement.</p>
<p id="p145202153514"><a name="p145202153514"></a><a name="p145202153514"></a>Map properties:</p>
<a name="ul2946182703613"></a><a name="ul2946182703613"></a><ul id="ul2946182703613"><li>actions<p id="p124941812193818"><a name="p124941812193818"></a><a name="p124941812193818"></a>Lifecycle actions to which the configuration applies. The string values provided for this property can include the standard resource actions CREATE, DELETE, and UPDATE supported by Heat.</p>
<p id="p14964125386"><a name="p14964125386"></a><a name="p14964125386"></a>List value expected.</p>
<p id="p7496812113820"><a name="p7496812113820"></a><a name="p7496812113820"></a>Updates cause replacement.</p>
<p id="p174971120389"><a name="p174971120389"></a><a name="p174971120389"></a>Defaults to "[CREATE, UPDATE]".</p>
<p id="p174971612163814"><a name="p174971612163814"></a><a name="p174971612163814"></a>The length must be at least 1.</p>
<p id="p249701293818"><a name="p249701293818"></a><a name="p249701293818"></a>List contents:</p>
<p id="p84981512133816"><a name="p84981512133816"></a><a name="p84981512133816"></a>*</p>
<p id="p5499151216387"><a name="p5499151216387"></a><a name="p5499151216387"></a>String value expected.</p>
<p id="p14499101210381"><a name="p14499101210381"></a><a name="p14499101210381"></a>Updates cause replacement.</p>
</li><li>config<p id="p910051873916"><a name="p910051873916"></a><a name="p910051873916"></a>Configuration script or manifest which specifies what actual configuration is performed.</p>
<p id="p310113184393"><a name="p310113184393"></a><a name="p310113184393"></a>String value expected.</p>
<p id="p201013185395"><a name="p201013185395"></a><a name="p201013185395"></a>Updates cause replacement.</p>
</li><li>tool<p id="p7483228133917"><a name="p7483228133917"></a><a name="p7483228133917"></a>The configuration tool used to actually apply the configuration on a server. This string property has to be understood by in-instance tools running inside deployed servers.</p>
<p id="p10484162818391"><a name="p10484162818391"></a><a name="p10484162818391"></a>String value expected.</p>
<p id="p1748412810391"><a name="p1748412810391"></a><a name="p1748412810391"></a>Updates cause replacement.</p>
</li></ul>
</li></ul>
</td>
</tr>
</tbody>
</table>

## Optional Properties<a name="section7205104903320"></a>

<a name="table2092313018406"></a>
<table><thead align="left"><tr id="row116364517395"><th class="cellrowborder" valign="top" width="36%" id="mcps1.1.3.1.1"><p id="p1392416020407"><a name="p1392416020407"></a><a name="p1392416020407"></a><strong id="b1927292117398"><a name="b1927292117398"></a><a name="b1927292117398"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.1.3.1.2"><p id="p592415094020"><a name="p592415094020"></a><a name="p592415094020"></a><strong id="b15273102110396"><a name="b15273102110396"></a><a name="b15273102110396"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row186367518398"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p1492420134014"><a name="p1492420134014"></a><a name="p1492420134014"></a>inputs</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p49100499"><a name="p49100499"></a><a name="p49100499"></a>Schema representing the inputs that this software config is expecting.</p>
<p id="p39251311"><a name="p39251311"></a><a name="p39251311"></a>List value expected.</p>
<p id="p17717481"><a name="p17717481"></a><a name="p17717481"></a>Updates cause replacement.</p>
<p id="p25239602"><a name="p25239602"></a><a name="p25239602"></a><em id="i8198163"><a name="i8198163"></a><a name="i8198163"></a>List contents:</em></p>
<a name="ul31141853"></a><a name="ul31141853"></a><ul id="ul31141853"><li>*<p id="p5281203414011"><a name="p5281203414011"></a><a name="p5281203414011"></a>Map value expected.</p>
<p id="p92812034104010"><a name="p92812034104010"></a><a name="p92812034104010"></a>Updates cause replacement.</p>
<p id="p9282734114012"><a name="p9282734114012"></a><a name="p9282734114012"></a><em id="i65799365"><a name="i65799365"></a><a name="i65799365"></a>Map properties:</em></p>
<a name="ul7476155044015"></a><a name="ul7476155044015"></a><ul id="ul7476155044015"><li>default<p id="p5402193215415"><a name="p5402193215415"></a><a name="p5402193215415"></a>Default value for the input if none is specified.</p>
<p id="p440313329418"><a name="p440313329418"></a><a name="p440313329418"></a>String value expected.</p>
<p id="p64048327415"><a name="p64048327415"></a><a name="p64048327415"></a>Updates cause replacement.</p>
</li><li>description<p id="p152922041144120"><a name="p152922041144120"></a><a name="p152922041144120"></a>Description of the input.</p>
<p id="p929354115415"><a name="p929354115415"></a><a name="p929354115415"></a>String value expected.</p>
<p id="p429474118418"><a name="p429474118418"></a><a name="p429474118418"></a>Updates cause replacement.</p>
</li><li>name<p id="p662055054116"><a name="p662055054116"></a><a name="p662055054116"></a>Name of the input.</p>
<p id="p1462105094120"><a name="p1462105094120"></a><a name="p1462105094120"></a>String value expected.</p>
<p id="p96211150174113"><a name="p96211150174113"></a><a name="p96211150174113"></a>Updates cause replacement.</p>
</li><li>replace_on_change<p id="p132421802428"><a name="p132421802428"></a><a name="p132421802428"></a>Replace the deployment instead of updating it when the input value changes.</p>
<p id="p152431034218"><a name="p152431034218"></a><a name="p152431034218"></a>Boolean value expected.</p>
<p id="p82448024217"><a name="p82448024217"></a><a name="p82448024217"></a>Updates cause replacement.</p>
<p id="p13245202426"><a name="p13245202426"></a><a name="p13245202426"></a>Defaults to "False".</p>
</li><li>type<p id="p7735151011427"><a name="p7735151011427"></a><a name="p7735151011427"></a>Type of the value of the input.</p>
<p id="p12736710194211"><a name="p12736710194211"></a><a name="p12736710194211"></a>String value expected.</p>
<p id="p77371110174212"><a name="p77371110174212"></a><a name="p77371110174212"></a>Updates cause replacement.</p>
<p id="p13737161084219"><a name="p13737161084219"></a><a name="p13737161084219"></a>Defaults to "String".</p>
<p id="p13738121084211"><a name="p13738121084211"></a><a name="p13738121084211"></a>Allowed values: String, Number, CommaDelimitedList, Json, Boolean</p>
</li></ul>
</li></ul>
</td>
</tr>
<tr id="row1563617512397"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p59245012400"><a name="p59245012400"></a><a name="p59245012400"></a>options</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p50593787"><a name="p50593787"></a><a name="p50593787"></a>Map containing options specific to the configuration management tool used by this resource.</p>
<p id="p52690904"><a name="p52690904"></a><a name="p52690904"></a>Map value expected.</p>
<p id="p4456091"><a name="p4456091"></a><a name="p4456091"></a>Updates cause replacement.</p>
</td>
</tr>
<tr id="row15636105103920"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p1692413019408"><a name="p1692413019408"></a><a name="p1692413019408"></a>outputs</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p25399071"><a name="p25399071"></a><a name="p25399071"></a>Schema representing the outputs that this software config will produce.</p>
<p id="p27265050"><a name="p27265050"></a><a name="p27265050"></a>List value expected.</p>
<p id="p44058864"><a name="p44058864"></a><a name="p44058864"></a>Updates cause replacement.</p>
<p id="p60985456"><a name="p60985456"></a><a name="p60985456"></a><em id="i31361845"><a name="i31361845"></a><a name="i31361845"></a>List contents:</em></p>
<a name="ul40874910"></a><a name="ul40874910"></a><ul id="ul40874910"><li>*<p id="p173166144313"><a name="p173166144313"></a><a name="p173166144313"></a>Map value expected.</p>
<p id="p1144634319"><a name="p1144634319"></a><a name="p1144634319"></a>Updates cause replacement.</p>
<p id="p20536144312"><a name="p20536144312"></a><a name="p20536144312"></a><em id="i14515208"><a name="i14515208"></a><a name="i14515208"></a>Map properties:</em></p>
<a name="ul1316691364319"></a><a name="ul1316691364319"></a><ul id="ul1316691364319"><li>description<p id="p253417427430"><a name="p253417427430"></a><a name="p253417427430"></a>Description of the output.</p>
<p id="p1553514425434"><a name="p1553514425434"></a><a name="p1553514425434"></a>String value expected.</p>
<p id="p10537184210438"><a name="p10537184210438"></a><a name="p10537184210438"></a>Updates cause replacement.</p>
</li><li>error_output<p id="p122669517431"><a name="p122669517431"></a><a name="p122669517431"></a>Denotes that the deployment is in an error state if this output has a value.</p>
<p id="p18267125194320"><a name="p18267125194320"></a><a name="p18267125194320"></a>Boolean value expected.</p>
<p id="p6269195154311"><a name="p6269195154311"></a><a name="p6269195154311"></a>Updates cause replacement.</p>
<p id="p202691551164315"><a name="p202691551164315"></a><a name="p202691551164315"></a>Defaults to "False".</p>
</li><li>name<p id="p119101859194310"><a name="p119101859194310"></a><a name="p119101859194310"></a>Name of the output.</p>
<p id="p17911195994319"><a name="p17911195994319"></a><a name="p17911195994319"></a>String value expected.</p>
<p id="p20912115964318"><a name="p20912115964318"></a><a name="p20912115964318"></a>Updates cause replacement.</p>
</li><li>type<p id="p92821954419"><a name="p92821954419"></a><a name="p92821954419"></a>Type of the value of the output.</p>
<p id="p52831598447"><a name="p52831598447"></a><a name="p52831598447"></a>String value expected.</p>
<p id="p7284109154417"><a name="p7284109154417"></a><a name="p7284109154417"></a>Updates cause replacement.</p>
<p id="p112852096448"><a name="p112852096448"></a><a name="p112852096448"></a>Defaults to "String".</p>
<p id="p228614912448"><a name="p228614912448"></a><a name="p228614912448"></a>Allowed values: String, Number, CommaDelimitedList, Json, Boolean</p>
</li></ul>
</li></ul>
</td>
</tr>
</tbody>
</table>

## Attributes<a name="section18429125618333"></a>

<a name="table155121044174614"></a>
<table><thead align="left"><tr id="row5516191134414"><th class="cellrowborder" valign="top" width="37%" id="mcps1.1.3.1.1"><p id="p125132044144610"><a name="p125132044144610"></a><a name="p125132044144610"></a><strong id="b1911712313440"><a name="b1911712313440"></a><a name="b1911712313440"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="63%" id="mcps1.1.3.1.2"><p id="p14513104410462"><a name="p14513104410462"></a><a name="p14513104410462"></a><strong id="b19119523124411"><a name="b19119523124411"></a><a name="b19119523124411"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row451617154416"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p10513344164618"><a name="p10513344164618"></a><a name="p10513344164618"></a>config</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p15513544154615"><a name="p15513544154615"></a><a name="p15513544154615"></a>The config value of the software config.</p>
<p id="p0109101712314"><a name="p0109101712314"></a><a name="p0109101712314"></a>The config is generally read from a script file and often contains some parameter substitutions. The config value is the script content that actually runs in the virtual machine.</p>
</td>
</tr>
</tbody>
</table>

## HOT Syntax<a name="section67251368349"></a>

```
heat_template_version: 2014-10-16
...
resources:
  ...
  the_resource:
    type: OS::Heat::SoftwareComponent
    properties:
      configs: [{"config": String, "tool": String, "actions": [String, String, ...]}, {"config": String, "tool": String, "actions": [String, String, ...]}, ...]
      inputs: [{"type": String, "default": String, "name": String, "replace_on_change": Boolean, "description": String}, {"type": String, "default": String, "name": String, "replace_on_change": Boolean, "description": String}, ...]
      options: {...}
      outputs: [{"type": String, "name": String, "error_output": Boolean, "description": String}, {"type": String, "name": String, "error_output": Boolean, "description": String}, ...]
```

