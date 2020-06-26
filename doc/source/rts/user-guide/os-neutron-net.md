# OS::Neutron::Net<a name="EN-US_TOPIC_0088407095"></a>

A resource for managing Neutron net.

A network is a virtual isolated layer-2 broadcast domain which is typically reserved to the tenant who created it, unless the network has been explicitly configured to be shared.

## Optional Properties<a name="section155801059172614"></a>

<a name="table1617983715273"></a>
<table><thead align="left"><tr id="row550314250374"><th class="cellrowborder" valign="top" width="33%" id="mcps1.1.3.1.1"><p id="p9179163752712"><a name="p9179163752712"></a><a name="p9179163752712"></a><strong id="b191729168363"><a name="b191729168363"></a><a name="b191729168363"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="67%" id="mcps1.1.3.1.2"><p id="p91797371279"><a name="p91797371279"></a><a name="p91797371279"></a><strong id="b117231614367"><a name="b117231614367"></a><a name="b117231614367"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row18503182533710"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p01794375274"><a name="p01794375274"></a><a name="p01794375274"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p9074991"><a name="p9074991"></a><a name="p9074991"></a>A boolean value specifying the administrative status of the network.</p>
<p id="p14566059"><a name="p14566059"></a><a name="p14566059"></a>Boolean value expected.</p>
<p id="p63985672"><a name="p63985672"></a><a name="p63985672"></a>Can be updated without replacement.</p>
<p id="p39000144"><a name="p39000144"></a><a name="p39000144"></a>Defaults to "True".</p>
</td>
</tr>
<tr id="row13503125153710"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p517983710278"><a name="p517983710278"></a><a name="p517983710278"></a>dhcp_agent_ids</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p4895081"><a name="p4895081"></a><a name="p4895081"></a>The IDs of the DHCP agent to schedule the network. Note that the default policy setting in Neutron restricts usage of this property to administrative users only.</p>
<p id="p44055733"><a name="p44055733"></a><a name="p44055733"></a>List value expected.</p>
<p id="p60957279"><a name="p60957279"></a><a name="p60957279"></a>Can be updated without replacement.</p>
</td>
</tr>
<tr id="row5503825153717"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p18179123717275"><a name="p18179123717275"></a><a name="p18179123717275"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p38592537"><a name="p38592537"></a><a name="p38592537"></a>A string specifying a symbolic name for the network, which is not required to be unique.</p>
<p id="p11788515"><a name="p11788515"></a><a name="p11788515"></a>String value expected.</p>
<p id="p38987775"><a name="p38987775"></a><a name="p38987775"></a>Can be updated without replacement.</p>
</td>
</tr>
<tr id="row150362516371"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p4180537182717"><a name="p4180537182717"></a><a name="p4180537182717"></a>shared</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p3893243"><a name="p3893243"></a><a name="p3893243"></a>Whether this network should be shared across all tenants. Note that the default policy setting restricts usage of this attribute to administrative users only.</p>
<p id="p35039187"><a name="p35039187"></a><a name="p35039187"></a>Boolean value expected.</p>
<p id="p46917234"><a name="p46917234"></a><a name="p46917234"></a>Can be updated without replacement.</p>
<p id="p19601928"><a name="p19601928"></a><a name="p19601928"></a>Defaults to "False".</p>
</td>
</tr>
<tr id="row4503525163712"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p10180143719274"><a name="p10180143719274"></a><a name="p10180143719274"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p44252358"><a name="p44252358"></a><a name="p44252358"></a>The ID of the tenant which will own the network. Only administrative users can set the tenant identifier; this cannot be changed using authorization policies.</p>
<p id="p62726903"><a name="p62726903"></a><a name="p62726903"></a>String value expected.</p>
<p id="p27671220"><a name="p27671220"></a><a name="p27671220"></a>Updates cause replacement.</p>
</td>
</tr>
<tr id="row1150312510370"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p1518043715278"><a name="p1518043715278"></a><a name="p1518043715278"></a>value_specs</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p26776314"><a name="p26776314"></a><a name="p26776314"></a>Extra parameters to include in the request. Parameters are often specific to installed hardware or extensions.</p>
<p id="p39660238"><a name="p39660238"></a><a name="p39660238"></a>Map value expected.</p>
<p id="p21397825"><a name="p21397825"></a><a name="p21397825"></a>Can be updated without replacement.</p>
<p id="p58362700"><a name="p58362700"></a><a name="p58362700"></a>Defaults to "{}".</p>
</td>
</tr>
</tbody>
</table>

## Attributes<a name="section8865116152719"></a>

<a name="table2060611279298"></a>
<table><thead align="left"><tr id="row14877919143918"><th class="cellrowborder" valign="top" width="33%" id="mcps1.1.3.1.1"><p id="p19610427142910"><a name="p19610427142910"></a><a name="p19610427142910"></a><strong id="b166162305398"><a name="b166162305398"></a><a name="b166162305398"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="67%" id="mcps1.1.3.1.2"><p id="p9610132712297"><a name="p9610132712297"></a><a name="p9610132712297"></a><strong id="b5617143011399"><a name="b5617143011399"></a><a name="b5617143011399"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row4877719163913"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p861111271298"><a name="p861111271298"></a><a name="p861111271298"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p16613527162911"><a name="p16613527162911"></a><a name="p16613527162911"></a>The administrative status of the network.</p>
</td>
</tr>
<tr id="row48774193398"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p7617162715297"><a name="p7617162715297"></a><a name="p7617162715297"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p861822722917"><a name="p861822722917"></a><a name="p861822722917"></a>The name of the network.</p>
</td>
</tr>
<tr id="row128771719143912"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p1317019234304"><a name="p1317019234304"></a><a name="p1317019234304"></a>show</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p17620027132912"><a name="p17620027132912"></a><a name="p17620027132912"></a>Detailed information about resource.</p>
</td>
</tr>
<tr id="row387781912398"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p126211027152916"><a name="p126211027152916"></a><a name="p126211027152916"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p56221027162918"><a name="p56221027162918"></a><a name="p56221027162918"></a>The status of the network.</p>
</td>
</tr>
<tr id="row1887713196393"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p462312711293"><a name="p462312711293"></a><a name="p462312711293"></a>subnets</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p76241527142913"><a name="p76241527142913"></a><a name="p76241527142913"></a>Subnets of this network.</p>
</td>
</tr>
<tr id="row0877161963910"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p392416623115"><a name="p392416623115"></a><a name="p392416623115"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p1392511663115"><a name="p1392511663115"></a><a name="p1392511663115"></a>The tenant owning this network.</p>
</td>
</tr>
</tbody>
</table>

## HOT Syntax<a name="section93902151275"></a>

```
heat_template_version: 2014-10-16
...
resources:
  ...
  the_resource:
    type: OS::Neutron::Net
    properties:
      admin_state_up: Boolean
      dhcp_agent_ids: [Value, Value, ...]
      name: String
      shared: Boolean
      tenant_id: String
      value_specs: {...}
```

