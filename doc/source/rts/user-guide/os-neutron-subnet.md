# OS::Neutron::Subnet<a name="EN-US_TOPIC_0088407123"></a>

The resource is not allowed to be updated.

A resource for managing Neutron subnets.

A subnet represents an IP address block that can be used for assigning IP addresses to virtual instances. Each subnet must have a CIDR and must be associated with a network. IP addresses can be either selected from the whole subnet CIDR, or from "allocation pools" that can be specified by the user.

>![](/images/icon-note.gif) **NOTE:**   
>A network can only have one subnet.  

## Required Properties<a name="section159742047808"></a>

<a name="table1512016462116"></a>
<table><thead align="left"><tr id="row7847135418546"><th class="cellrowborder" valign="top" width="31%" id="mcps1.1.3.1.1"><p id="p1120114617112"><a name="p1120114617112"></a><a name="p1120114617112"></a><strong id="b99841417184712"><a name="b99841417184712"></a><a name="b99841417184712"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="69%" id="mcps1.1.3.1.2"><p id="p812084611116"><a name="p812084611116"></a><a name="p812084611116"></a><strong id="b14985111715471"><a name="b14985111715471"></a><a name="b14985111715471"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row8847145418540"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p21730781"><a name="p21730781"></a><a name="p21730781"></a>cidr</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p61359305"><a name="p61359305"></a><a name="p61359305"></a>The CIDR.</p>
<p id="p15362835"><a name="p15362835"></a><a name="p15362835"></a>String value expected.</p>
<p id="p1182813216213"><a name="p1182813216213"></a><a name="p1182813216213"></a>Updates cause replacement.</p>
</td>
</tr>
</tbody>
</table>

## Optional Properties<a name="section810410565014"></a>

<a name="table195142231218"></a>
<table><thead align="left"><tr id="row1397013233564"><th class="cellrowborder" valign="top" width="32%" id="mcps1.1.3.1.1"><p id="p182917321324"><a name="p182917321324"></a><a name="p182917321324"></a><strong id="b494843511566"><a name="b494843511566"></a><a name="b494843511566"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.1.3.1.2"><p id="p1751414231225"><a name="p1751414231225"></a><a name="p1751414231225"></a><strong id="b194993595610"><a name="b194993595610"></a><a name="b194993595610"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row897116239563"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p132381115318"><a name="p132381115318"></a><a name="p132381115318"></a>allocation_pools</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p19567671"><a name="p19567671"></a><a name="p19567671"></a>The start and end addresses for the allocation pools.</p>
<p id="p41891316"><a name="p41891316"></a><a name="p41891316"></a>List value expected.</p>
<p id="p41477528"><a name="p41477528"></a><a name="p41477528"></a>Can be updated without replacement.</p>
<p id="p37753436"><a name="p37753436"></a><a name="p37753436"></a><em id="i59962836"><a name="i59962836"></a><a name="i59962836"></a>List contents:</em></p>
<a name="ul38129489"></a><a name="ul38129489"></a><ul id="ul38129489"><li>*<p id="p1480890"><a name="p1480890"></a><a name="p1480890"></a>Map value expected.</p>
<p id="p13328014"><a name="p13328014"></a><a name="p13328014"></a>Can be updated without replacement.</p>
<p id="p1989116105313"><a name="p1989116105313"></a><a name="p1989116105313"></a><em id="i65498832"><a name="i65498832"></a><a name="i65498832"></a>Map properties:</em></p>
<a name="ul05593161433"></a><a name="ul05593161433"></a><ul id="ul05593161433"><li>end<p id="p20264512"><a name="p20264512"></a><a name="p20264512"></a>End address for the allocation pool.</p>
<p id="p48162888"><a name="p48162888"></a><a name="p48162888"></a>String value expected.</p>
<p id="p30812812"><a name="p30812812"></a><a name="p30812812"></a>Can be updated without replacement.</p>
<p id="p2013114326314"><a name="p2013114326314"></a><a name="p2013114326314"></a>Value must be of type ip_addr</p>
</li><li>start<p id="p30961791"><a name="p30961791"></a><a name="p30961791"></a>Start address for the allocation pool.</p>
<p id="p10220671"><a name="p10220671"></a><a name="p10220671"></a>String value expected.</p>
<p id="p24877176"><a name="p24877176"></a><a name="p24877176"></a>Can be updated without replacement.</p>
<p id="p1171113911313"><a name="p1171113911313"></a><a name="p1171113911313"></a>Value must be of type ip_addr</p>
</li></ul>
</li></ul>
</td>
</tr>
<tr id="row129711223195613"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p11514202310211"><a name="p11514202310211"></a><a name="p11514202310211"></a>dns_nameservers</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p16068435"><a name="p16068435"></a><a name="p16068435"></a>A specified set of DNS name servers to be used.</p>
<p id="p10398191"><a name="p10398191"></a><a name="p10398191"></a>List value expected.</p>
<p id="p26474858"><a name="p26474858"></a><a name="p26474858"></a>Can be updated without replacement.</p>
<p id="p36947133"><a name="p36947133"></a><a name="p36947133"></a>Defaults to "[]".</p>
</td>
</tr>
<tr id="row11971102355619"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p1651413231523"><a name="p1651413231523"></a><a name="p1651413231523"></a>enable_dhcp</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p39927800"><a name="p39927800"></a><a name="p39927800"></a>Set to true if DHCP is enabled and false if DHCP is disabled.</p>
<p id="p23805881"><a name="p23805881"></a><a name="p23805881"></a>Boolean value expected.</p>
<p id="p12926343"><a name="p12926343"></a><a name="p12926343"></a>Can be updated without replacement.</p>
<p id="p49228226"><a name="p49228226"></a><a name="p49228226"></a>Defaults to "True".</p>
</td>
</tr>
<tr id="row1597172355616"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p1514122312215"><a name="p1514122312215"></a><a name="p1514122312215"></a>gateway_ip</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p28063339"><a name="p28063339"></a><a name="p28063339"></a>The gateway IP address. Set to any of [ null | ~ | "" ] to create/update a subnet without a gateway. If omitted when creation, neutron will assign the first free IP address within the subnet to the gateway automatically. If remove this from template when update, the old gateway IP address will be detached.</p>
<p id="p51243459"><a name="p51243459"></a><a name="p51243459"></a>String value expected.</p>
<p id="p58537948"><a name="p58537948"></a><a name="p58537948"></a>Can be updated without replacement.</p>
</td>
</tr>
<tr id="row1797152345616"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p151418238217"><a name="p151418238217"></a><a name="p151418238217"></a>host_routes</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p43953342"><a name="p43953342"></a><a name="p43953342"></a>A list of host route dictionaries for the subnet.</p>
<p id="p60035760"><a name="p60035760"></a><a name="p60035760"></a>List value expected.</p>
<p id="p3450936"><a name="p3450936"></a><a name="p3450936"></a>Can be updated without replacement.</p>
<p id="p31058430"><a name="p31058430"></a><a name="p31058430"></a><em id="i35962059"><a name="i35962059"></a><a name="i35962059"></a>List contents:</em></p>
<a name="ul32704912"></a><a name="ul32704912"></a><ul id="ul32704912"><li>*<p id="p31852239"><a name="p31852239"></a><a name="p31852239"></a>Map value expected.</p>
<p id="p18234698"><a name="p18234698"></a><a name="p18234698"></a>Can be updated without replacement.</p>
<p id="p19228856646"><a name="p19228856646"></a><a name="p19228856646"></a><em id="i47812724"><a name="i47812724"></a><a name="i47812724"></a>Map properties:</em></p>
<a name="ul161876215518"></a><a name="ul161876215518"></a><ul id="ul161876215518"><li>destination<p id="p46124582"><a name="p46124582"></a><a name="p46124582"></a>The destination for static route.</p>
<p id="p12468057"><a name="p12468057"></a><a name="p12468057"></a>String value expected.</p>
<p id="p45103655"><a name="p45103655"></a><a name="p45103655"></a>Can be updated without replacement.</p>
<p id="p27768181351"><a name="p27768181351"></a><a name="p27768181351"></a>Value must be of type net_cidr</p>
</li><li>nexthop<p id="p42099501"><a name="p42099501"></a><a name="p42099501"></a>The next hop for the destination.</p>
<p id="p43351196"><a name="p43351196"></a><a name="p43351196"></a>String value expected.</p>
<p id="p54616452"><a name="p54616452"></a><a name="p54616452"></a>Can be updated without replacement.</p>
<p id="p169614271554"><a name="p169614271554"></a><a name="p169614271554"></a>Value must be of type ip_addr</p>
</li></ul>
</li></ul>
</td>
</tr>
<tr id="row497119234568"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p18515142319217"><a name="p18515142319217"></a><a name="p18515142319217"></a>ip_version</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p63307724"><a name="p63307724"></a><a name="p63307724"></a>The IP version, which is 4 or 6.</p>
<p id="p32898609"><a name="p32898609"></a><a name="p32898609"></a>Integer value expected.</p>
<p id="p27652029"><a name="p27652029"></a><a name="p27652029"></a>Updates cause replacement.</p>
<p id="p0651726132414"><a name="p0651726132414"></a><a name="p0651726132414"></a>Defaults to "4".</p>
<p id="p47541673"><a name="p47541673"></a><a name="p47541673"></a>Allowed values: 4, 6</p>
<div class="note" id="note097420583502"><a name="note097420583502"></a><a name="note097420583502"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p44316893"><a name="p44316893"></a><a name="p44316893"></a>Do not update this attribute. Otherwise, the network update will fail.</p>
</div></div>
</td>
</tr>
<tr id="row189712023105617"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p145153231024"><a name="p145153231024"></a><a name="p145153231024"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p29706272"><a name="p29706272"></a><a name="p29706272"></a>The name of the subnet.</p>
<p id="p66029863"><a name="p66029863"></a><a name="p66029863"></a>String value expected.</p>
<p id="p57397859"><a name="p57397859"></a><a name="p57397859"></a>Can be updated without replacement.</p>
</td>
</tr>
<tr id="row6971122319565"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p65151223921"><a name="p65151223921"></a><a name="p65151223921"></a>network</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p18714982"><a name="p18714982"></a><a name="p18714982"></a>The name of the attached network.</p>
<p id="p34217111"><a name="p34217111"></a><a name="p34217111"></a>String value expected.</p>
<p id="p39518545"><a name="p39518545"></a><a name="p39518545"></a>Updates cause replacement.</p>
</td>
</tr>
<tr id="row497192325615"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p155151223025"><a name="p155151223025"></a><a name="p155151223025"></a>network_id</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p394710391247"><a name="p394710391247"></a><a name="p394710391247"></a>The ID of the attached network.</p>
<p id="p46885581"><a name="p46885581"></a><a name="p46885581"></a>String value expected.</p>
<p id="p19317049"><a name="p19317049"></a><a name="p19317049"></a>Updates cause replacement.</p>
<div class="note" id="note19125754918"><a name="note19125754918"></a><a name="note19125754918"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p144347297614"><a name="p144347297614"></a><a name="p144347297614"></a>In the template, <strong id="b557351752111"><a name="b557351752111"></a><a name="b557351752111"></a>network </strong>and<strong id="b1057416177214"><a name="b1057416177214"></a><a name="b1057416177214"></a> network_id</strong> cannot appear at the same time, otherwise the stack will fail to create.</p>
</div></div>
</td>
</tr>
<tr id="row10971112315620"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p15151523426"><a name="p15151523426"></a><a name="p15151523426"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p37623884"><a name="p37623884"></a><a name="p37623884"></a>The ID of the tenant who owns the network. Only administrative users can specify a tenant ID other than their own.</p>
<p id="p3070644"><a name="p3070644"></a><a name="p3070644"></a>String value expected.</p>
<p id="p27635797"><a name="p27635797"></a><a name="p27635797"></a>Updates cause replacement.</p>
<div class="note" id="note880713917115"><a name="note880713917115"></a><a name="note880713917115"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p56376214"><a name="p56376214"></a><a name="p56376214"></a>Do not update this attribute. Otherwise, the network update will fail.</p>
</div></div>
</td>
</tr>
<tr id="row199711423135614"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p951552310210"><a name="p951552310210"></a><a name="p951552310210"></a>value_specs</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p23907090"><a name="p23907090"></a><a name="p23907090"></a>Extra parameters to include in the request.</p>
<p id="p13837224"><a name="p13837224"></a><a name="p13837224"></a>Map value expected.</p>
<p id="p57426156"><a name="p57426156"></a><a name="p57426156"></a>Can be updated without replacement.</p>
<p id="p47073359"><a name="p47073359"></a><a name="p47073359"></a>Defaults to "{}".</p>
</td>
</tr>
</tbody>
</table>

## Attributes<a name="section134811335113"></a>

<a name="table1897285215719"></a>
<table><thead align="left"><tr id="row1734144031"><th class="cellrowborder" valign="top" width="32%" id="mcps1.1.3.1.1"><p id="p89729521278"><a name="p89729521278"></a><a name="p89729521278"></a><strong id="b040713209313"><a name="b040713209313"></a><a name="b040713209313"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.1.3.1.2"><p id="p597216524719"><a name="p597216524719"></a><a name="p597216524719"></a><strong id="b6409142013317"><a name="b6409142013317"></a><a name="b6409142013317"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row173419412312"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p597219521678"><a name="p597219521678"></a><a name="p597219521678"></a>allocation_pools</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p89720521874"><a name="p89720521874"></a><a name="p89720521874"></a>Ip allocation pools and their ranges.</p>
</td>
</tr>
<tr id="row473414739"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p297216529711"><a name="p297216529711"></a><a name="p297216529711"></a>cidr</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p1197217521577"><a name="p1197217521577"></a><a name="p1197217521577"></a>CIDR block notation for this subnet.</p>
</td>
</tr>
<tr id="row1373415410310"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p1697265212710"><a name="p1697265212710"></a><a name="p1697265212710"></a>dns_nameservers</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p49723521472"><a name="p49723521472"></a><a name="p49723521472"></a>List of dns nameservers.</p>
</td>
</tr>
<tr id="row20734241838"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p1897219521714"><a name="p1897219521714"></a><a name="p1897219521714"></a>enable_dhcp</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p1197218526715"><a name="p1197218526715"></a><a name="p1197218526715"></a>true if DHCP is enabled for this subnet; false otherwise.</p>
</td>
</tr>
<tr id="row13734194536"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p179721052071"><a name="p179721052071"></a><a name="p179721052071"></a>gateway_ip</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p69729524710"><a name="p69729524710"></a><a name="p69729524710"></a>Ip of the subnets gateway.</p>
</td>
</tr>
<tr id="row673464132"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p179720521071"><a name="p179720521071"></a><a name="p179720521071"></a>host_routes</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p10972252877"><a name="p10972252877"></a><a name="p10972252877"></a>Additional routes for this subnet.</p>
</td>
</tr>
<tr id="row373418412315"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p8972165210717"><a name="p8972165210717"></a><a name="p8972165210717"></a>ip_version</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p097310527711"><a name="p097310527711"></a><a name="p097310527711"></a>Ip version for the subnet.</p>
</td>
</tr>
<tr id="row47344410310"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p11973452977"><a name="p11973452977"></a><a name="p11973452977"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p1597314523713"><a name="p1597314523713"></a><a name="p1597314523713"></a>Friendly name of the subnet.</p>
</td>
</tr>
<tr id="row147342418310"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p159736526719"><a name="p159736526719"></a><a name="p159736526719"></a>network_id</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p1697311521471"><a name="p1697311521471"></a><a name="p1697311521471"></a>Parent network of the subnet.</p>
</td>
</tr>
<tr id="row117346417315"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p11973165213710"><a name="p11973165213710"></a><a name="p11973165213710"></a>show</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p697315525717"><a name="p697315525717"></a><a name="p697315525717"></a>Detailed information about resource.</p>
</td>
</tr>
<tr id="row1673418418311"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p4973185210710"><a name="p4973185210710"></a><a name="p4973185210710"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p20973135214720"><a name="p20973135214720"></a><a name="p20973135214720"></a>Tenant owning the subnet.</p>
</td>
</tr>
</tbody>
</table>

## HOT Syntax<a name="section192315115112"></a>

```
heat_template_version: 2014-10-16
...
resources:
  ...
  the_resource:
    type: OS::Neutron::Subnet
    properties:
      allocation_pools: [{"start": String, "end": String}, {"start": String, "end": String}, ...]
      cidr: String
      dns_nameservers: [Value, Value, ...]
      enable_dhcp: Boolean
      gateway_ip: String
      host_routes: [{"destination": String, "nexthop": String}, {"destination": String, "nexthop": String}, ...]
      ip_version: Integer
      name: String
      network: String
      network_id: String
      tenant_id: String
      value_specs: {...}
```

