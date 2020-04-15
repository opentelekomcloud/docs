# OS::Heat::StructuredConfig<a name="EN-US_TOPIC_0088407202"></a>

A resource which has same logic with OS::Heat::SoftwareConfig.

This resource is like OS::Heat::SoftwareConfig except that the config property is represented by a Map rather than a String.

This is useful for configuration tools which use YAML or JSON as their configuration syntax. The resulting configuration is transferred, stored and returned by the software\_configs API as parsed JSON.

## Optional Properties<a name="section16226175416538"></a>

<a name="table104903487543"></a>
<table><thead align="left"><tr id="row1389173020813"><th class="cellrowborder" valign="top" width="31%" id="mcps1.1.3.1.1"><p id="p4491124814546"><a name="p4491124814546"></a><a name="p4491124814546"></a><strong id="b136631244682"><a name="b136631244682"></a><a name="b136631244682"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="69%" id="mcps1.1.3.1.2"><p id="p12491848135412"><a name="p12491848135412"></a><a name="p12491848135412"></a><strong id="b0663124419810"><a name="b0663124419810"></a><a name="b0663124419810"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row389193012810"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p6491134825410"><a name="p6491134825410"></a><a name="p6491134825410"></a>config</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p12442072"><a name="p12442072"></a><a name="p12442072"></a>Map representing the configuration data structure which will be serialized to JSON format.</p>
<p id="p44869788"><a name="p44869788"></a><a name="p44869788"></a>Map value expected.</p>
<p id="p1174908"><a name="p1174908"></a><a name="p1174908"></a>Updates cause replacement.</p>
</td>
</tr>
<tr id="row389103017819"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p1249112481542"><a name="p1249112481542"></a><a name="p1249112481542"></a>group</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p28058753"><a name="p28058753"></a><a name="p28058753"></a>Namespace to group this software config by when delivered to a server. This may imply what configuration tool is going to perform the configuration.</p>
<p id="p51202191"><a name="p51202191"></a><a name="p51202191"></a>String value expected.</p>
<p id="p58166543"><a name="p58166543"></a><a name="p58166543"></a>Updates cause replacement.</p>
<p id="p53736840"><a name="p53736840"></a><a name="p53736840"></a>Defaults to "Heat::Ungrouped".</p>
</td>
</tr>
<tr id="row19891130885"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p1749154875415"><a name="p1749154875415"></a><a name="p1749154875415"></a>inputs</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p57716789"><a name="p57716789"></a><a name="p57716789"></a>Schema representing the inputs that this software config is expecting.</p>
<p id="p49689059"><a name="p49689059"></a><a name="p49689059"></a>List value expected.</p>
<p id="p44548351"><a name="p44548351"></a><a name="p44548351"></a>Updates cause replacement.</p>
<p id="p65390842"><a name="p65390842"></a><a name="p65390842"></a><em id="i13888555"><a name="i13888555"></a><a name="i13888555"></a>List contents:</em></p>
<a name="ul62166841"></a><a name="ul62166841"></a><ul id="ul62166841"><li>*<p id="p177791352135519"><a name="p177791352135519"></a><a name="p177791352135519"></a>Map value expected.</p>
<p id="p147794523558"><a name="p147794523558"></a><a name="p147794523558"></a>Updates cause replacement.</p>
<p id="p277945235515"><a name="p277945235515"></a><a name="p277945235515"></a><em id="i46484818"><a name="i46484818"></a><a name="i46484818"></a>Map properties:</em></p>
<a name="ul113242035618"></a><a name="ul113242035618"></a><ul id="ul113242035618"><li>default<p id="p13934265612"><a name="p13934265612"></a><a name="p13934265612"></a>Default value for the input if none is specified.</p>
<p id="p16904275612"><a name="p16904275612"></a><a name="p16904275612"></a>String value expected.</p>
<p id="p121074265612"><a name="p121074265612"></a><a name="p121074265612"></a>Updates cause replacement.</p>
</li><li>description<p id="p12805150195617"><a name="p12805150195617"></a><a name="p12805150195617"></a>Description of the input.</p>
<p id="p1880685015561"><a name="p1880685015561"></a><a name="p1880685015561"></a>String value expected.</p>
<p id="p198074508568"><a name="p198074508568"></a><a name="p198074508568"></a>Updates cause replacement.</p>
</li><li>name<p id="p58005594561"><a name="p58005594561"></a><a name="p58005594561"></a>Name of the input.</p>
<p id="p198010596569"><a name="p198010596569"></a><a name="p198010596569"></a>String value expected.</p>
<p id="p180113598569"><a name="p180113598569"></a><a name="p180113598569"></a>Updates cause replacement.</p>
</li><li>replace_on_change<p id="p742981118575"><a name="p742981118575"></a><a name="p742981118575"></a>Replace the deployment instead of updating it when the input value changes.</p>
<p id="p1343031116570"><a name="p1343031116570"></a><a name="p1343031116570"></a>Boolean value expected.</p>
<p id="p443013119575"><a name="p443013119575"></a><a name="p443013119575"></a>Updates cause replacement.</p>
<p id="p14311311125713"><a name="p14311311125713"></a><a name="p14311311125713"></a>Defaults to "False".</p>
</li><li>type<p id="p4819420135719"><a name="p4819420135719"></a><a name="p4819420135719"></a>Type of the value of the input.</p>
<p id="p88201820175710"><a name="p88201820175710"></a><a name="p88201820175710"></a>String value expected.</p>
<p id="p14820162010572"><a name="p14820162010572"></a><a name="p14820162010572"></a>Updates cause replacement.</p>
<p id="p18821132095714"><a name="p18821132095714"></a><a name="p18821132095714"></a>Defaults to "String".</p>
<p id="p3822122014576"><a name="p3822122014576"></a><a name="p3822122014576"></a>Allowed values: String, Number, CommaDelimitedList, Json, Boolean</p>
</li></ul>
</li></ul>
</td>
</tr>
<tr id="row1589163016815"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p11491114835416"><a name="p11491114835416"></a><a name="p11491114835416"></a>options</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p56323821"><a name="p56323821"></a><a name="p56323821"></a>Map containing options specific to the configuration management tool used by this resource.</p>
<p id="p37152348"><a name="p37152348"></a><a name="p37152348"></a>Map value expected.</p>
<p id="p65935681"><a name="p65935681"></a><a name="p65935681"></a>Updates cause replacement.</p>
</td>
</tr>
<tr id="row489173015820"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p449184818545"><a name="p449184818545"></a><a name="p449184818545"></a>outputs</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p39189945"><a name="p39189945"></a><a name="p39189945"></a>Schema representing the outputs that this software config will produce.</p>
<p id="p17165190"><a name="p17165190"></a><a name="p17165190"></a>List value expected.</p>
<p id="p20268990"><a name="p20268990"></a><a name="p20268990"></a>Updates cause replacement.</p>
<p id="p48203184"><a name="p48203184"></a><a name="p48203184"></a><em id="i12517232"><a name="i12517232"></a><a name="i12517232"></a>List contents:</em></p>
<a name="ul12143859"></a><a name="ul12143859"></a><ul id="ul12143859"><li>*<p id="p11271172011584"><a name="p11271172011584"></a><a name="p11271172011584"></a>Map value expected.</p>
<p id="p4272152014581"><a name="p4272152014581"></a><a name="p4272152014581"></a>Updates cause replacement.</p>
<p id="p42731020105814"><a name="p42731020105814"></a><a name="p42731020105814"></a><em id="i4605057"><a name="i4605057"></a><a name="i4605057"></a>Map properties:</em></p>
<a name="ul1725893085816"></a><a name="ul1725893085816"></a><ul id="ul1725893085816"><li>description<p id="p137714241594"><a name="p137714241594"></a><a name="p137714241594"></a>Description of the output.</p>
<p id="p1477210247596"><a name="p1477210247596"></a><a name="p1477210247596"></a>String value expected.</p>
<p id="p6772192445910"><a name="p6772192445910"></a><a name="p6772192445910"></a>Updates cause replacement.</p>
</li><li>error_output<p id="p19636134175920"><a name="p19636134175920"></a><a name="p19636134175920"></a>Denotes that the deployment is in an error state if this output has a value.</p>
<p id="p4637534135915"><a name="p4637534135915"></a><a name="p4637534135915"></a>Boolean value expected.</p>
<p id="p1663833425916"><a name="p1663833425916"></a><a name="p1663833425916"></a>Updates cause replacement.</p>
<p id="p106387347598"><a name="p106387347598"></a><a name="p106387347598"></a>Defaults to "False".</p>
</li><li>name<p id="p870254411596"><a name="p870254411596"></a><a name="p870254411596"></a>Name of the output.</p>
<p id="p1070364413599"><a name="p1070364413599"></a><a name="p1070364413599"></a>String value expected.</p>
<p id="p17703154414598"><a name="p17703154414598"></a><a name="p17703154414598"></a>Updates cause replacement.</p>
</li><li>type<p id="p18450185419592"><a name="p18450185419592"></a><a name="p18450185419592"></a>Type of the value of the output.</p>
<p id="p174508542590"><a name="p174508542590"></a><a name="p174508542590"></a>String value expected.</p>
<p id="p645135475917"><a name="p645135475917"></a><a name="p645135475917"></a>Updates cause replacement.</p>
<p id="p12451115475910"><a name="p12451115475910"></a><a name="p12451115475910"></a>Defaults to "String".</p>
<p id="p10452554155915"><a name="p10452554155915"></a><a name="p10452554155915"></a>Allowed values: String, Number, CommaDelimitedList, Json, Boolean</p>
</li></ul>
</li></ul>
</td>
</tr>
</tbody>
</table>

## Attributes<a name="section8997141111541"></a>

<a name="table15257162013015"></a>
<table><thead align="left"><tr id="row330313347139"><th class="cellrowborder" valign="top" width="32%" id="mcps1.1.3.1.1"><p id="p7257162011013"><a name="p7257162011013"></a><a name="p7257162011013"></a><strong id="b14795165119138"><a name="b14795165119138"></a><a name="b14795165119138"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.1.3.1.2"><p id="p17257720309"><a name="p17257720309"></a><a name="p17257720309"></a><strong id="b17971951191310"><a name="b17971951191310"></a><a name="b17971951191310"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row193031134131311"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p02573202007"><a name="p02573202007"></a><a name="p02573202007"></a>config</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p925710201703"><a name="p925710201703"></a><a name="p925710201703"></a>The config value of the software config.</p>
<p id="p33071021112"><a name="p33071021112"></a><a name="p33071021112"></a>The config is generally read from a script file and often contains some parameter substitutions. The config value is the script content that actually runs in the virtual machine.</p>
</td>
</tr>
</tbody>
</table>

## HOT Syntax<a name="section64112026165414"></a>

```
heat_template_version: 2014-10-16
...
resources:
  ...
  the_resource:
    type: OS::Heat::StructuredConfig
    properties:
      config: {...}
      group: String
      inputs: [{"type": String, "default": String, "name": String, "replace_on_change": Boolean, "description": String}, {"type": String, "default": String, "name": String, "replace_on_change": Boolean, "description": String}, ...]
      options: {...}
      outputs: [{"type": String, "name": String, "error_output": Boolean, "description": String}, {"type": String, "name": String, "error_output": Boolean, "description": String}, ...]
```

