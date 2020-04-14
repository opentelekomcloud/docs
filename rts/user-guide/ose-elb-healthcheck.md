# OSE::ELB::HealthCheck<a name="EN-US_TOPIC_0088407189"></a>

A resource for ELB Health Check.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>You must configure health checks for load balancers.  

## Required Properties<a name="section111401653420"></a>

<a name="table10981721131"></a>
<table><thead align="left"><tr id="row1411817351235"><th class="cellrowborder" valign="top" width="31%" id="mcps1.1.3.1.1"><p id="p119810211331"><a name="p119810211331"></a><a name="p119810211331"></a><strong id="b15421252715"><a name="b15421252715"></a><a name="b15421252715"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="69%" id="mcps1.1.3.1.2"><p id="p198142119317"><a name="p198142119317"></a><a name="p198142119317"></a><strong id="b135430525116"><a name="b135430525116"></a><a name="b135430525116"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1111810351738"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p189813212317"><a name="p189813212317"></a><a name="p189813212317"></a>listener_id</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p24627600"><a name="p24627600"></a><a name="p24627600"></a>The ID of listener associated.</p>
<p id="p20321813"><a name="p20321813"></a><a name="p20321813"></a>String value expected.</p>
<p id="p48678592"><a name="p48678592"></a><a name="p48678592"></a>Updates cause replacement.</p>
<p id="p35454146"><a name="p35454146"></a><a name="p35454146"></a>Value must be of type elb.ls</p>
</td>
</tr>
</tbody>
</table>

## Optional Properties<a name="section4793404314"></a>

<a name="table631416910415"></a>
<table><thead align="left"><tr id="row76127541"><th class="cellrowborder" valign="top" width="31%" id="mcps1.1.3.1.1"><p id="p1931417918412"><a name="p1931417918412"></a><a name="p1931417918412"></a><strong id="b1849833520414"><a name="b1849833520414"></a><a name="b1849833520414"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="69%" id="mcps1.1.3.1.2"><p id="p53151191746"><a name="p53151191746"></a><a name="p53151191746"></a><strong id="b149923516410"><a name="b149923516410"></a><a name="b149923516410"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row661927347"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p1731513910419"><a name="p1731513910419"></a><a name="p1731513910419"></a>healthcheck_connect_port</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p62689434"><a name="p62689434"></a><a name="p62689434"></a>The port of the health check.</p>
<p id="p27334001"><a name="p27334001"></a><a name="p27334001"></a>Integer value expected.</p>
<p id="p44679419"><a name="p44679419"></a><a name="p44679419"></a>Can be updated without replacement.</p>
<p id="p66570459"><a name="p66570459"></a><a name="p66570459"></a>Allowed values: from 1 to 65535, include 1 and 65535.</p>
</td>
</tr>
<tr id="row165272049"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p19315991949"><a name="p19315991949"></a><a name="p19315991949"></a>healthcheck_interval</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p23498118"><a name="p23498118"></a><a name="p23498118"></a>The interval between the health checks in seconds.</p>
<p id="p10156475"><a name="p10156475"></a><a name="p10156475"></a>Integer value expected.</p>
<p id="p24299418"><a name="p24299418"></a><a name="p24299418"></a>Can be updated without replacement.</p>
<p id="p17368170"><a name="p17368170"></a><a name="p17368170"></a>Allowed values: from 1 to 5, include 1 and 5.</p>
</td>
</tr>
<tr id="row136627447"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p183151198414"><a name="p183151198414"></a><a name="p183151198414"></a>healthcheck_protocol</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p64644525"><a name="p64644525"></a><a name="p64644525"></a>The protocol of the health check.</p>
<p id="p44929818"><a name="p44929818"></a><a name="p44929818"></a>String value expected.</p>
<p id="p1715181"><a name="p1715181"></a><a name="p1715181"></a>Can be updated without replacement.</p>
<p id="p15436631"><a name="p15436631"></a><a name="p15436631"></a>Allowed values: HTTP, TCP</p>
</td>
</tr>
<tr id="row136827348"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p12315149745"><a name="p12315149745"></a><a name="p12315149745"></a>healthcheck_timeout</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p42407580"><a name="p42407580"></a><a name="p42407580"></a>The timeout of the health check in seconds.</p>
<p id="p46123906"><a name="p46123906"></a><a name="p46123906"></a>Integer value expected.</p>
<p id="p12461970"><a name="p12461970"></a><a name="p12461970"></a>Can be updated without replacement.</p>
<p id="p45048871"><a name="p45048871"></a><a name="p45048871"></a>Allowed values: from 1 to 50, include 1 and 50.</p>
</td>
</tr>
<tr id="row768272411"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p63151391843"><a name="p63151391843"></a><a name="p63151391843"></a>healthcheck_uri</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p25079912"><a name="p25079912"></a><a name="p25079912"></a>The HTTP path used in the HTTP request to check a member health.</p>
<p id="p24392623"><a name="p24392623"></a><a name="p24392623"></a>String value expected.</p>
<p id="p18207023"><a name="p18207023"></a><a name="p18207023"></a>Can be updated without replacement.</p>
<p id="p98471940125612"><a name="p98471940125612"></a><a name="p98471940125612"></a>It is allowed to start with<strong id="b164946301965"><a name="b164946301965"></a><a name="b164946301965"></a> / </strong>characters. It is allowed to include <strong id="b171661144114212"><a name="b171661144114212"></a><a name="b171661144114212"></a>numbers</strong>, <strong id="b11167134474213"><a name="b11167134474213"></a><a name="b11167134474213"></a>letters</strong>, <strong id="b181676449424"><a name="b181676449424"></a><a name="b181676449424"></a>-/.%?#&amp;</strong> characters, and the string length is <strong id="b131671744204214"><a name="b131671744204214"></a><a name="b131671744204214"></a>1</strong> to <strong id="b13848184619712"><a name="b13848184619712"></a><a name="b13848184619712"></a>80</strong>.</p>
</td>
</tr>
<tr id="row1761327649"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p6315119348"><a name="p6315119348"></a><a name="p6315119348"></a>healthy_threshold</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p52473583"><a name="p52473583"></a><a name="p52473583"></a>The number of the successful threshold before change the member status to healthy.</p>
<p id="p2500200"><a name="p2500200"></a><a name="p2500200"></a>Integer value expected.</p>
<p id="p22501807"><a name="p22501807"></a><a name="p22501807"></a>Can be updated without replacement.</p>
<p id="p1189676"><a name="p1189676"></a><a name="p1189676"></a>Allowed values: from 1 to 10, include 1 and 10. The default value is <strong id="b6330309613838"><a name="b6330309613838"></a><a name="b6330309613838"></a>3</strong>.</p>
</td>
</tr>
<tr id="row17616271412"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p15315179142"><a name="p15315179142"></a><a name="p15315179142"></a>unhealthy_threshold</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p61967801"><a name="p61967801"></a><a name="p61967801"></a>The number of the failure threshold before change the member status to unhealthy.</p>
<p id="p20839305"><a name="p20839305"></a><a name="p20839305"></a>Integer value expected.</p>
<p id="p53336019"><a name="p53336019"></a><a name="p53336019"></a>Can be updated without replacement.</p>
<p id="p10262130"><a name="p10262130"></a><a name="p10262130"></a>Allowed values: from 1 to 10, include 1 and 10.</p>
</td>
</tr>
</tbody>
</table>

## HOT Syntax<a name="section1741129836"></a>

```
heat_template_version: 2014-10-16
...
resources:
  ...
  the_resource:
    type: OSE::ELB::HealthCheck
    properties:
      healthcheck_connect_port: Integer
      healthcheck_interval: Integer
      healthcheck_protocol: String
      healthcheck_timeout: Integer
      healthcheck_uri: String
      healthy_threshold: Integer
      listener_id: String
      unhealthy_threshold: Integer
```

