# OSE::VPC::Subnet<a name="EN-US_TOPIC_0103361352"></a>

A resource for managing subnets

## Required Properties<a name="section15981242142217"></a>

<a name="table1123555113222"></a>
<table><thead align="left"><tr id="row3237351122210"><th class="cellrowborder" valign="top" width="34%" id="mcps1.1.3.1.1"><p id="p643749201717"><a name="p643749201717"></a><a name="p643749201717"></a><strong id="b68442017337"><a name="b68442017337"></a><a name="b68442017337"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="66%" id="mcps1.1.3.1.2"><p id="p164371961711"><a name="p164371961711"></a><a name="p164371961711"></a><strong id="b084512018335"><a name="b084512018335"></a><a name="b084512018335"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1923745122214"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p165291374231"><a name="p165291374231"></a><a name="p165291374231"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p75297712313"><a name="p75297712313"></a><a name="p75297712313"></a>Subnet name</p>
<p id="p1752910752314"><a name="p1752910752314"></a><a name="p1752910752314"></a>String value expected.</p>
<p id="p1152912713238"><a name="p1152912713238"></a><a name="p1152912713238"></a>Can be updated without replacement.</p>
<p id="p052914718239"><a name="p052914718239"></a><a name="p052914718239"></a>Value range: 1 to 64, which can contain digits, letters, underscores (_), and hyphens (-)</p>
</td>
</tr>
<tr id="row112375514227"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p1823755118224"><a name="p1823755118224"></a><a name="p1823755118224"></a>cidr</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p101441354172319"><a name="p101441354172319"></a><a name="p101441354172319"></a>Network segment of a subnet</p>
<p id="p141441854102313"><a name="p141441854102313"></a><a name="p141441854102313"></a>String value expected.</p>
<p id="p1514495413233"><a name="p1514495413233"></a><a name="p1514495413233"></a>Updates cause replacement.</p>
<p id="p1390155617230"><a name="p1390155617230"></a><a name="p1390155617230"></a>Value range: The value must be within the CIDR range of the VPC. The value must be in the CIDR format. The mask length cannot exceed 28 characters.</p>
</td>
</tr>
<tr id="row16237135117229"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p19237185162211"><a name="p19237185162211"></a><a name="p19237185162211"></a>gateway_ip</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p81181818153120"><a name="p81181818153120"></a><a name="p81181818153120"></a>Gateway of a subnet</p>
<p id="p61181418163116"><a name="p61181418163116"></a><a name="p61181418163116"></a>String value expected.</p>
<p id="p1611871883110"><a name="p1611871883110"></a><a name="p1611871883110"></a>Updates cause replacement.</p>
<p id="p14749619203111"><a name="p14749619203111"></a><a name="p14749619203111"></a>Value range: IP addresses in the subnet segment. The IP address must be valid.</p>
</td>
</tr>
<tr id="row1523775142220"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p169444318342"><a name="p169444318342"></a><a name="p169444318342"></a>vpc_id</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p136941643193419"><a name="p136941643193419"></a><a name="p136941643193419"></a>ID of the VPC to which the subnet belongs</p>
<p id="p1869494320341"><a name="p1869494320341"></a><a name="p1869494320341"></a>String value expected.</p>
<p id="p16694154311343"><a name="p16694154311343"></a><a name="p16694154311343"></a>Updates cause replacement.</p>
</td>
</tr>
</tbody>
</table>

## Optional Properties<a name="section125431356113413"></a>

<a name="table9898111163513"></a>
<table><thead align="left"><tr id="row1899191115353"><th class="cellrowborder" valign="top" width="35%" id="mcps1.1.3.1.1"><p id="p113791111916"><a name="p113791111916"></a><a name="p113791111916"></a><strong id="b385874113313"><a name="b385874113313"></a><a name="b385874113313"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="65%" id="mcps1.1.3.1.2"><p id="p7139161118920"><a name="p7139161118920"></a><a name="p7139161118920"></a><strong id="b785915411337"><a name="b785915411337"></a><a name="b785915411337"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row20899121163510"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p16899101133515"><a name="p16899101133515"></a><a name="p16899101133515"></a>dhcp_enable</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p7638134843514"><a name="p7638134843514"></a><a name="p7638134843514"></a>Whether the DHCP function is enabled on a subnet</p>
<p id="p10638154819356"><a name="p10638154819356"></a><a name="p10638154819356"></a>String value expected.</p>
<p id="p16912195603513"><a name="p16912195603513"></a><a name="p16912195603513"></a>Can be updated without replacement.</p>
<p id="p17543133319213"><a name="p17543133319213"></a><a name="p17543133319213"></a>Allowed value: true and false</p>
<p id="p135437338217"><a name="p135437338217"></a><a name="p135437338217"></a>Default value: true</p>
</td>
</tr>
<tr id="row1989941163511"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p1089961118357"><a name="p1089961118357"></a><a name="p1089961118357"></a>primary_dns</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p19802329153610"><a name="p19802329153610"></a><a name="p19802329153610"></a>Subnet DNS server address 1</p>
<p id="p0802529113611"><a name="p0802529113611"></a><a name="p0802529113611"></a>String value expected.</p>
<p id="p68028294368"><a name="p68028294368"></a><a name="p68028294368"></a>Can be updated without replacement.</p>
<p id="p980252914366"><a name="p980252914366"></a><a name="p980252914366"></a>The value must be a valid IP address.</p>
</td>
</tr>
<tr id="row589981183515"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p1589915116357"><a name="p1589915116357"></a><a name="p1589915116357"></a>secondary_dns</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p1589345715360"><a name="p1589345715360"></a><a name="p1589345715360"></a>Subnet DNS server address 2</p>
<p id="p1893135719362"><a name="p1893135719362"></a><a name="p1893135719362"></a>String value expected.</p>
<p id="p289312574363"><a name="p289312574363"></a><a name="p289312574363"></a>Can be updated without replacement.</p>
<p id="p189355718361"><a name="p189355718361"></a><a name="p189355718361"></a>The value must be a valid IP address.</p>
</td>
</tr>
<tr id="row198991311203512"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p2899141113519"><a name="p2899141113519"></a><a name="p2899141113519"></a>dnsList</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p3151812123714"><a name="p3151812123714"></a><a name="p3151812123714"></a>A set of subnet DNS server addresses</p>
<p id="p91169522317"><a name="p91169522317"></a><a name="p91169522317"></a>Use this field if you want to use more than two DNS servers. This field is the parent set of subnet DNS server address 1 and subnet DNS server address 2.</p>
<p id="p1115111127370"><a name="p1115111127370"></a><a name="p1115111127370"></a>List value.</p>
<p id="p215112126377"><a name="p215112126377"></a><a name="p215112126377"></a>Can be updated without replacement.</p>
<p id="p51511212163714"><a name="p51511212163714"></a><a name="p51511212163714"></a>The value in the set must be a valid IP address.</p>
</td>
</tr>
<tr id="row1189912115352"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p11899101183510"><a name="p11899101183510"></a><a name="p11899101183510"></a>availability_zone</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p0557112123914"><a name="p0557112123914"></a><a name="p0557112123914"></a>ID of the AZ where the subnet is located</p>
<p id="p105571021163917"><a name="p105571021163917"></a><a name="p105571021163917"></a>String value expected.</p>
<p id="p155712218394"><a name="p155712218394"></a><a name="p155712218394"></a>Updates cause replacement.</p>
</td>
</tr>
</tbody>
</table>

## HOT Syntax<a name="section2555147153915"></a>

```
heat_template_version: 2014-10-16
... 
resources:
  ...
  the_resource:
    type: OSE::VPC::Subnet
    properties:
      name: String
      cidr: String
      gateway_ip: String
      vpc_id: String
      dhcp_enable: Boolean
      primary_dns: String
      secondary_dns: String
      dnsList: [...]
      availability_zone: String
```

