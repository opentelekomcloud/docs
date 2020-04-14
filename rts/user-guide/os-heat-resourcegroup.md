# OS::Heat::ResourceGroup<a name="EN-US_TOPIC_0088407208"></a>

Creates one or more identically configured nested resources.

In addition to the refs attribute, this resource implements synthetic attributes that mirror those of the resources in the group. When getting an attribute from this resource, however, a list of attribute values for each resource in the group is returned. To get attribute values for a single resource in the group, synthetic attributes of the form resource.\{resource index\}.\{attribute name\} can be used. The resource ID of a particular resource in the group can be obtained via the synthetic attribute resource.\{resource index\}. Note, that if you get attribute without \{resource index\}, e.g. \[resource, \{attribute\_name\}\], you will get a list of this attributes value for all resources in group.

While each resource in the group will be identically configured, this resource does allow for some index-based customization of the properties of the resources in the group. For example:

```
resources:
  my_indexed_group:
    type: OS::Heat::ResourceGroup
    properties:
      count: 3
      resource_def:
        type: OS::Nova::Server
        properties:
          # create a unique name for each server
          # using its index in the group
          name: my_server_%index%
          image: CentOS 6.5
          flavor: 4GB Performance
```

would result in a group of three servers having the same image and flavor, but names of my\_server\_0, my\_server\_1, and my\_server\_2. The variable used for substitution can be customized by using the index\_var property.

## Required Properties<a name="section153485985613"></a>

<a name="table15629533105412"></a>
<table><thead align="left"><tr id="row6430469230"><th class="cellrowborder" valign="top" width="33%" id="mcps1.1.3.1.1"><p id="p1430156202317"><a name="p1430156202317"></a><a name="p1430156202317"></a><strong id="b1863716229239"><a name="b1863716229239"></a><a name="b1863716229239"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="67%" id="mcps1.1.3.1.2"><p id="p18430161235"><a name="p18430161235"></a><a name="p18430161235"></a><strong id="b1463812224236"><a name="b1463812224236"></a><a name="b1463812224236"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row94301863232"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p443086162319"><a name="p443086162319"></a><a name="p443086162319"></a>resource_def</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p36692685"><a name="p36692685"></a><a name="p36692685"></a>Resource definition for the resources in the group. The value of this property is the definition of a resource just as if it had been declared in the template itself.</p>
<p id="p61798714"><a name="p61798714"></a><a name="p61798714"></a>Map value expected.</p>
<p id="p19317517"><a name="p19317517"></a><a name="p19317517"></a>Can be updated without replacement.</p>
<p id="p39639927"><a name="p39639927"></a><a name="p39639927"></a><em id="i21215025"><a name="i21215025"></a><a name="i21215025"></a>Map properties:</em></p>
<a name="ul8540051"></a><a name="ul8540051"></a><ul id="ul8540051"><li>metadata<p id="p30714802"><a name="p30714802"></a><a name="p30714802"></a>Supplied metadata for the resources in the group.</p>
<p id="p7997767"><a name="p7997767"></a><a name="p7997767"></a>Map value expected.</p>
<p id="p13997913202514"><a name="p13997913202514"></a><a name="p13997913202514"></a>Can be updated without replacement.</p>
</li><li>properties<p id="p61327951"><a name="p61327951"></a><a name="p61327951"></a>Property values for the resources in the group.</p>
<p id="p15080647"><a name="p15080647"></a><a name="p15080647"></a>Map value expected.</p>
<p id="p24012258251"><a name="p24012258251"></a><a name="p24012258251"></a>Can be updated without replacement.</p>
</li><li>type<p id="p25661391"><a name="p25661391"></a><a name="p25661391"></a>The type of the resources in the group.</p>
<p id="p29625932"><a name="p29625932"></a><a name="p29625932"></a>String value expected.</p>
<p id="p109891343255"><a name="p109891343255"></a><a name="p109891343255"></a>Can be updated without replacement.</p>
</li></ul>
</td>
</tr>
</tbody>
</table>

## Optional Properties<a name="section7420928195714"></a>

<a name="table3199163545714"></a>
<table><thead align="left"><tr id="row41915258289"><th class="cellrowborder" valign="top" width="33%" id="mcps1.1.3.1.1"><p id="p719112552818"><a name="p719112552818"></a><a name="p719112552818"></a><strong id="b7201025162819"><a name="b7201025162819"></a><a name="b7201025162819"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="67%" id="mcps1.1.3.1.2"><p id="p1820152582814"><a name="p1820152582814"></a><a name="p1820152582814"></a><strong id="b1020182512284"><a name="b1020182512284"></a><a name="b1020182512284"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row321192532815"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p1221925172810"><a name="p1221925172810"></a><a name="p1221925172810"></a>count</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p12059425"><a name="p12059425"></a><a name="p12059425"></a>The number of resources to create.</p>
<p id="p41425962"><a name="p41425962"></a><a name="p41425962"></a>Integer value expected.</p>
<p id="p37289346"><a name="p37289346"></a><a name="p37289346"></a>Can be updated without replacement.</p>
<p id="p59801"><a name="p59801"></a><a name="p59801"></a>Defaults to "1".</p>
<p id="p538217"><a name="p538217"></a><a name="p538217"></a>The value must be at least 0.</p>
</td>
</tr>
<tr id="row1239759142818"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p04075911284"><a name="p04075911284"></a><a name="p04075911284"></a>index_var</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p43595579"><a name="p43595579"></a><a name="p43595579"></a>A variable that this resource will use to replace with the current index of a given resource in the group. Can be used, for example, to customize the name property of grouped servers in order to differentiate them when listed with nova client.</p>
<p id="p56815897"><a name="p56815897"></a><a name="p56815897"></a>String value expected.</p>
<p id="p41581026"><a name="p41581026"></a><a name="p41581026"></a>Updates cause replacement.</p>
<p id="p38684921"><a name="p38684921"></a><a name="p38684921"></a>Defaults to "%index%".</p>
<p id="p12619974"><a name="p12619974"></a><a name="p12619974"></a>The length must be at least 3.</p>
</td>
</tr>
</tbody>
</table>

## Attributes<a name="section1332223325815"></a>

<a name="table432433312583"></a>
<table><thead align="left"><tr id="row755084332912"><th class="cellrowborder" valign="top" width="34%" id="mcps1.1.3.1.1"><p id="p182281656112919"><a name="p182281656112919"></a><a name="p182281656112919"></a><strong id="b102282569295"><a name="b102282569295"></a><a name="b102282569295"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="66%" id="mcps1.1.3.1.2"><p id="p1623115565297"><a name="p1623115565297"></a><a name="p1623115565297"></a><strong id="b12314562292"><a name="b12314562292"></a><a name="b12314562292"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row17550443172917"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p15503437295"><a name="p15503437295"></a><a name="p15503437295"></a>attributes</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p15550154392915"><a name="p15550154392915"></a><a name="p15550154392915"></a>A map of resource names to the specified attribute of each individual resource. Requires heat_template_version: 2014-10-16.</p>
</td>
</tr>
<tr id="row1855034315294"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p4550114316291"><a name="p4550114316291"></a><a name="p4550114316291"></a>refs</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p25506438298"><a name="p25506438298"></a><a name="p25506438298"></a>A list of resource IDs for the resources in the group.</p>
</td>
</tr>
</tbody>
</table>

## HOT Syntax<a name="section539424155911"></a>

```
heat_template_version: 2014-10-16
...
resources:
  ...
  the_resource:
    type: OS::Heat::ResourceGroup
    properties:
      count: Integer
      index_var: String
      removal_policies: [{"resource_list": [Value, Value, ...]}, {"resource_list": [Value, Value, ...]}, ...]
      resource_def: {"type": String, "properties": {...}, "metadata": {...}}
```

