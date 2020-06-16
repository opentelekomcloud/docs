# OS::Neutron::LBaaS::HealthMonitor<a name="EN-US_TOPIC_0088407067"></a>

A resource to handle load balancer health monitors.

This resource creates and manages Neutron LBaaS v2 healthmonitors, which watches status of the load balanced servers.

## Required Properties<a name="section15858125117127"></a>

<a name="table62811834171310"></a>
<table><thead align="left"><tr id="row897652693"><th class="cellrowborder" valign="top" width="36%" id="mcps1.1.3.1.1"><p id="p15281134191319"><a name="p15281134191319"></a><a name="p15281134191319"></a><strong id="b8366113113719"><a name="b8366113113719"></a><a name="b8366113113719"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.1.3.1.2"><p id="p8281163412134"><a name="p8281163412134"></a><a name="p8281163412134"></a><strong id="b103672031673"><a name="b103672031673"></a><a name="b103672031673"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row2976172198"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p1128110341139"><a name="p1128110341139"></a><a name="p1128110341139"></a>delay</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p11577965"><a name="p11577965"></a><a name="p11577965"></a>The minimum time in milliseconds between regular connections of the member.</p>
<p id="p37092822"><a name="p37092822"></a><a name="p37092822"></a>Integer value expected.</p>
<p id="p65399943"><a name="p65399943"></a><a name="p65399943"></a>Can be updated without replacement.</p>
<p id="p51728577"><a name="p51728577"></a><a name="p51728577"></a>The value must be in the range 0 to 2147483647, include 0 and 2147483647.</p>
</td>
</tr>
<tr id="row179761126914"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p42821034141318"><a name="p42821034141318"></a><a name="p42821034141318"></a>max_retries</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p29265213"><a name="p29265213"></a><a name="p29265213"></a>Number of permissible connection failures before changing the member status to INACTIVE.</p>
<p id="p62060329"><a name="p62060329"></a><a name="p62060329"></a>Integer value expected.</p>
<p id="p21672049"><a name="p21672049"></a><a name="p21672049"></a>Can be updated without replacement.</p>
<p id="p60830720"><a name="p60830720"></a><a name="p60830720"></a>The value must be in the range 1 to 10, include 1 and 10.</p>
</td>
</tr>
<tr id="row17976122917"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p2028283461317"><a name="p2028283461317"></a><a name="p2028283461317"></a>pool</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p28341308"><a name="p28341308"></a><a name="p28341308"></a>ID or name of the load balancing pool.</p>
<p id="p53745188"><a name="p53745188"></a><a name="p53745188"></a>String value expected.</p>
<p id="p13944645"><a name="p13944645"></a><a name="p13944645"></a>Updates cause replacement.</p>
<p id="p58392946"><a name="p58392946"></a><a name="p58392946"></a>Value must be of type neutron.lbaas.pool</p>
</td>
</tr>
<tr id="row12976102593"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p92827340139"><a name="p92827340139"></a><a name="p92827340139"></a>timeout</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p32208152"><a name="p32208152"></a><a name="p32208152"></a>Maximum number of milliseconds for a monitor to wait for a connection to be established before it times out.</p>
<p id="p21437916"><a name="p21437916"></a><a name="p21437916"></a>Integer value expected.</p>
<p id="p58723519"><a name="p58723519"></a><a name="p58723519"></a>Can be updated without replacement.</p>
<p id="p58749626"><a name="p58749626"></a><a name="p58749626"></a>The value must be in the range 0 to 2147483647, include 0 and 2147483647.</p>
</td>
</tr>
<tr id="row159764210910"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p102821734181314"><a name="p102821734181314"></a><a name="p102821734181314"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p61099269"><a name="p61099269"></a><a name="p61099269"></a>One of predefined health monitor types.</p>
<p id="p13022510"><a name="p13022510"></a><a name="p13022510"></a>String value expected.</p>
<p id="p50093732"><a name="p50093732"></a><a name="p50093732"></a>Updates cause replacement.</p>
<p id="p48190407"><a name="p48190407"></a><a name="p48190407"></a>Allowed values: PING, TCP, HTTP</p>
</td>
</tr>
</tbody>
</table>

## Optional Properties<a name="section161501720134"></a>

<a name="table3322324131511"></a>
<table><thead align="left"><tr id="row163513841111"><th class="cellrowborder" valign="top" width="36%" id="mcps1.1.3.1.1"><p id="p133229242154"><a name="p133229242154"></a><a name="p133229242154"></a><strong id="b15460221111112"><a name="b15460221111112"></a><a name="b15460221111112"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.1.3.1.2"><p id="p23221124141512"><a name="p23221124141512"></a><a name="p23221124141512"></a><strong id="b2046113213110"><a name="b2046113213110"></a><a name="b2046113213110"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row53514831114"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p3322824151519"><a name="p3322824151519"></a><a name="p3322824151519"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p34260525"><a name="p34260525"></a><a name="p34260525"></a>The administrative state of the health monitor.</p>
<p id="p39909275"><a name="p39909275"></a><a name="p39909275"></a>Boolean value expected.</p>
<p id="p23639161"><a name="p23639161"></a><a name="p23639161"></a>Updates are not supported.</p>
<p id="p11425865"><a name="p11425865"></a><a name="p11425865"></a>Allowed values: True</p>
</td>
</tr>
<tr id="row935118841117"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p432252431518"><a name="p432252431518"></a><a name="p432252431518"></a>expected_codes</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p6632171571017"><a name="p6632171571017"></a><a name="p6632171571017"></a>The HTTP status codes expected in response from the member to declare it healthy.</p>
<p id="p3900101710102"><a name="p3900101710102"></a><a name="p3900101710102"></a>Specify one of the following values:</p>
<a name="ul970322612108"></a><a name="ul970322612108"></a><ul id="ul970322612108"><li>a single value, such as 200.</li><li>a list, such as 200, 202.</li><li>a range, such as 200 to 204.</li></ul>
<p id="p7956575"><a name="p7956575"></a><a name="p7956575"></a>String value expected.</p>
<p id="p4500317"><a name="p4500317"></a><a name="p4500317"></a>Can be updated without replacement.</p>
<p id="p40502857"><a name="p40502857"></a><a name="p40502857"></a>Defaults to "200".</p>
</td>
</tr>
<tr id="row113514813115"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p143225248156"><a name="p143225248156"></a><a name="p143225248156"></a>http_method</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p59505975"><a name="p59505975"></a><a name="p59505975"></a>The HTTP method used for requests by the monitor of type HTTP.</p>
<p id="p65791731"><a name="p65791731"></a><a name="p65791731"></a>String value expected.</p>
<p id="p55254674"><a name="p55254674"></a><a name="p55254674"></a>Can be updated without replacement.</p>
<p id="p27530019"><a name="p27530019"></a><a name="p27530019"></a>Defaults to "GET".</p>
<p id="p46443585"><a name="p46443585"></a><a name="p46443585"></a>Allowed values: GET, HEAD, POST, PUT, DELETE, TRACE, OPTIONS, CONNECT, PATCH</p>
</td>
</tr>
<tr id="row16351182119"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p17322524131517"><a name="p17322524131517"></a><a name="p17322524131517"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p3834029"><a name="p3834029"></a><a name="p3834029"></a>ID of the tenant who owns the health monitor.</p>
<p id="p34506261"><a name="p34506261"></a><a name="p34506261"></a>String value expected.</p>
<p id="p42120893"><a name="p42120893"></a><a name="p42120893"></a>Updates cause replacement.</p>
</td>
</tr>
<tr id="row435158161113"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p183221724171519"><a name="p183221724171519"></a><a name="p183221724171519"></a>url_path</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p56349145"><a name="p56349145"></a><a name="p56349145"></a>The HTTP path used in the HTTP request used by the monitor to test a member health. A valid value is a string that begins with a forward slash (/).</p>
<p id="p37380264"><a name="p37380264"></a><a name="p37380264"></a>String value expected.</p>
<p id="p878058"><a name="p878058"></a><a name="p878058"></a>Can be updated without replacement.</p>
<p id="p7902530"><a name="p7902530"></a><a name="p7902530"></a>Defaults to "/".</p>
</td>
</tr>
</tbody>
</table>

## Attributes<a name="section1183609151319"></a>

<a name="table19581161218170"></a>
<table><thead align="left"><tr id="row121975111126"><th class="cellrowborder" valign="top" width="36%" id="mcps1.1.3.1.1"><p id="p185813123175"><a name="p185813123175"></a><a name="p185813123175"></a><strong id="b322115114124"><a name="b322115114124"></a><a name="b322115114124"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.1.3.1.2"><p id="p85811312161711"><a name="p85811312161711"></a><a name="p85811312161711"></a><strong id="b5222135120127"><a name="b5222135120127"></a><a name="b5222135120127"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row14223175112124"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p5582131221715"><a name="p5582131221715"></a><a name="p5582131221715"></a>pools</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p9582141231710"><a name="p9582141231710"></a><a name="p9582141231710"></a>The list of Pools related to this monitor.</p>
</td>
</tr>
</tbody>
</table>

## HOT Syntax<a name="section151641319141319"></a>

```
heat_template_version: 2014-10-16
...
resources:
  ...
  the_resource:
    type: OS::Neutron::LBaaS::HealthMonitor
    properties:
      admin_state_up: Boolean
      delay: Integer
      expected_codes: String
      http_method: String
      max_retries: Integer
      pool: String
      tenant_id: String
      timeout: Integer
      type: String
      url_path: String
```

