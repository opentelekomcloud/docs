# OS::Neutron::Router<a name="EN-US_TOPIC_0088407115"></a>

A resource that implements Neutron router.

Router is a physical or virtual network device that passes network traffic between different networks.

## Optional Properties<a name="section1863647461"></a>

<a name="table21591350124620"></a>
<table><thead align="left"><tr id="row111041842113819"><th class="cellrowborder" valign="top" width="31%" id="mcps1.1.3.1.1"><p id="p17159115010461"><a name="p17159115010461"></a><a name="p17159115010461"></a><strong id="b691914133415"><a name="b691914133415"></a><a name="b691914133415"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="69%" id="mcps1.1.3.1.2"><p id="p915985054611"><a name="p915985054611"></a><a name="p915985054611"></a><strong id="b49417141346"><a name="b49417141346"></a><a name="b49417141346"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row2104842103814"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p015975010460"><a name="p015975010460"></a><a name="p015975010460"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p40613049"><a name="p40613049"></a><a name="p40613049"></a>The administrative state of the router.</p>
<p id="p29973122"><a name="p29973122"></a><a name="p29973122"></a>Boolean value expected.</p>
<p id="p1322648"><a name="p1322648"></a><a name="p1322648"></a>Can be updated without replacement.</p>
<p id="p11903835"><a name="p11903835"></a><a name="p11903835"></a>Defaults to "True".</p>
</td>
</tr>
<tr id="row1104174253814"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p20160185094618"><a name="p20160185094618"></a><a name="p20160185094618"></a>external_gateway_info</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p24686548"><a name="p24686548"></a><a name="p24686548"></a>External network gateway configuration for a router.</p>
<p id="p20852340"><a name="p20852340"></a><a name="p20852340"></a>You can use <strong id="b25663607131047"><a name="b25663607131047"></a><a name="b25663607131047"></a>GET /v2.0/networks?router:external=True</strong>&nbsp;or<strong id="b65486281131047"><a name="b65486281131047"></a><a name="b65486281131047"></a> neutron net-external-list</strong> to query the network information.</p>
<p id="p53453333"><a name="p53453333"></a><a name="p53453333"></a>Map value expected.</p>
<p id="p11317952"><a name="p11317952"></a><a name="p11317952"></a>Can be updated without replacement.</p>
<p id="p34752711"><a name="p34752711"></a><a name="p34752711"></a><em id="i33489226"><a name="i33489226"></a><a name="i33489226"></a>Map properties:</em></p>
<a name="ul63506193"></a><a name="ul63506193"></a><ul id="ul63506193"><li>enable_snat<p id="p43728028"><a name="p43728028"></a><a name="p43728028"></a>Enables Source NAT on the router gateway. NOTE: The default policy setting in Neutron restricts usage of this property to administrative users only.</p>
<p id="p58007937"><a name="p58007937"></a><a name="p58007937"></a>Boolean value expected.</p>
<p id="p265554024717"><a name="p265554024717"></a><a name="p265554024717"></a>Can be updated without replacement.</p>
</li><li>network<p id="p11942749114711"><a name="p11942749114711"></a><a name="p11942749114711"></a>ID or name of the external network for the gateway.</p>
<p id="p14942849164715"><a name="p14942849164715"></a><a name="p14942849164715"></a>String value expected.</p>
<p id="p14943184913473"><a name="p14943184913473"></a><a name="p14943184913473"></a>Can be updated without replacement.</p>
</li></ul>
</td>
</tr>
<tr id="row15104124253814"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p14160185094618"><a name="p14160185094618"></a><a name="p14160185094618"></a>l3_agent_ids</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p7555415"><a name="p7555415"></a><a name="p7555415"></a>ID list of the L3 agent. User can specify multi-agents for highly available router. NOTE: The default policy setting in Neutron restricts usage of this property to administrative users only.</p>
<p id="p889874"><a name="p889874"></a><a name="p889874"></a>String value expected.</p>
<p id="p8008872"><a name="p8008872"></a><a name="p8008872"></a>Can be updated without replacement.</p>
</td>
</tr>
<tr id="row9104642183812"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p516045015466"><a name="p516045015466"></a><a name="p516045015466"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p44738861"><a name="p44738861"></a><a name="p44738861"></a>The name of the router.</p>
<p id="p67105430"><a name="p67105430"></a><a name="p67105430"></a>String value expected.</p>
<p id="p67077966"><a name="p67077966"></a><a name="p67077966"></a>Can be updated without replacement.</p>
</td>
</tr>
<tr id="row16745183913404"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p7160115013469"><a name="p7160115013469"></a><a name="p7160115013469"></a>value_specs</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p64606197"><a name="p64606197"></a><a name="p64606197"></a>Extra parameters to include in the creation request.</p>
<p id="p44584861"><a name="p44584861"></a><a name="p44584861"></a>Map value expected.</p>
<p id="p65719431"><a name="p65719431"></a><a name="p65719431"></a>Can be updated without replacement.</p>
<p id="p54603973"><a name="p54603973"></a><a name="p54603973"></a>Defaults to "{}".</p>
</td>
</tr>
</tbody>
</table>

## Attributes<a name="section1696871094614"></a>

<a name="table2349715154916"></a>
<table><thead align="left"><tr id="row1883519292418"><th class="cellrowborder" valign="top" width="32%" id="mcps1.1.3.1.1"><p id="p183491315184920"><a name="p183491315184920"></a><a name="p183491315184920"></a><strong id="b1446314425410"><a name="b1446314425410"></a><a name="b1446314425410"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.1.3.1.2"><p id="p334971515491"><a name="p334971515491"></a><a name="p334971515491"></a><strong id="b1346494215416"><a name="b1346494215416"></a><a name="b1346494215416"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row188352295417"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p14349515154912"><a name="p14349515154912"></a><a name="p14349515154912"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p534941516497"><a name="p534941516497"></a><a name="p534941516497"></a>Administrative state of the router.</p>
</td>
</tr>
<tr id="row198353299416"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p13349181518494"><a name="p13349181518494"></a><a name="p13349181518494"></a>external_gateway_info</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p1234911519494"><a name="p1234911519494"></a><a name="p1234911519494"></a>Gateway network for the router.</p>
</td>
</tr>
<tr id="row083512954114"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p8349151513499"><a name="p8349151513499"></a><a name="p8349151513499"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p0349191544919"><a name="p0349191544919"></a><a name="p0349191544919"></a>Friendly name of the router.</p>
</td>
</tr>
<tr id="row383532914112"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p93495153496"><a name="p93495153496"></a><a name="p93495153496"></a>show</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p734917150495"><a name="p734917150495"></a><a name="p734917150495"></a>Detailed information about resource.</p>
</td>
</tr>
<tr id="row14835729124117"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p11349215114910"><a name="p11349215114910"></a><a name="p11349215114910"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p13499153492"><a name="p13499153492"></a><a name="p13499153492"></a>The status of the router.</p>
</td>
</tr>
<tr id="row88351529164116"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p7349171512493"><a name="p7349171512493"></a><a name="p7349171512493"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p13491015204916"><a name="p13491015204916"></a><a name="p13491015204916"></a>Tenant owning the router.</p>
</td>
</tr>
</tbody>
</table>

## HOT Syntax<a name="section2094963274611"></a>

```
heat_template_version: 2014-10-16
...
resources:
  ...
  the_resource:
    type: OS::Neutron::Router
    properties:
      admin_state_up: Boolean
      external_gateway_info: {"network": String, "enable_snat": Boolean}
      l3_agent_ids: String
      name: String
      value_specs: {...}
```

