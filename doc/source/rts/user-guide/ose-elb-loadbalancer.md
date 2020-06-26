# OSE::ELB::LoadBalancer<a name="EN-US_TOPIC_0088407187"></a>

A resource for ELB Loadbalancer.

>![](/images/icon-note.gif) **NOTE:**   
>In later version, the API for using the LBaaS v2 load balancers will be provided, and you can create native LBaaS v2 load balancers. However, created load balancer cannot be changed to LBaaS v2 load balancers.  

## Required Properties<a name="section10369538163913"></a>

<a name="table98091741124214"></a>
<table><thead align="left"><tr id="row5238568479"><th class="cellrowborder" valign="top" width="34%" id="mcps1.1.3.1.1"><p id="p1081012411428"><a name="p1081012411428"></a><a name="p1081012411428"></a><strong id="b13221152412434"><a name="b13221152412434"></a><a name="b13221152412434"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="66%" id="mcps1.1.3.1.2"><p id="p17810194111425"><a name="p17810194111425"></a><a name="p17810194111425"></a><strong id="b2222162412432"><a name="b2222162412432"></a><a name="b2222162412432"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row3238161474"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p1581074116423"><a name="p1581074116423"></a><a name="p1581074116423"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p39592934"><a name="p39592934"></a><a name="p39592934"></a>The admin state of the load balancer.</p>
<p id="p20792086"><a name="p20792086"></a><a name="p20792086"></a>Boolean value expected.</p>
<p id="p52911051"><a name="p52911051"></a><a name="p52911051"></a>Can be updated without replacement.</p>
<p id="p6437412"><a name="p6437412"></a><a name="p6437412"></a>Defaults to "True".</p>
</td>
</tr>
<tr id="row182388694717"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p2810341124214"><a name="p2810341124214"></a><a name="p2810341124214"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p51668403"><a name="p51668403"></a><a name="p51668403"></a>The name of the load balancer.</p>
<p id="p62362451"><a name="p62362451"></a><a name="p62362451"></a>String value expected.</p>
<p id="p24391147"><a name="p24391147"></a><a name="p24391147"></a>Can be updated without replacement.</p>
<p id="p19426193618388"><a name="p19426193618388"></a><a name="p19426193618388"></a>It is allowed to start with <strong id="b1279613252309"><a name="b1279613252309"></a><a name="b1279613252309"></a>numbers</strong>, <strong id="b107201029113015"><a name="b107201029113015"></a><a name="b107201029113015"></a>letters</strong>, _, and <strong id="b9809184113309"><a name="b9809184113309"></a><a name="b9809184113309"></a>-</strong> characters. It is allowed to include <strong id="b22921519153119"><a name="b22921519153119"></a><a name="b22921519153119"></a>numbers</strong>, <strong id="b929441919312"><a name="b929441919312"></a><a name="b929441919312"></a>letters</strong>, _, and <strong id="b5295111983114"><a name="b5295111983114"></a><a name="b5295111983114"></a>-</strong> characters, and the string length is <strong id="b547314383115"><a name="b547314383115"></a><a name="b547314383115"></a>1</strong> to <strong id="b1924693244214"><a name="b1924693244214"></a><a name="b1924693244214"></a>64</strong>.</p>
</td>
</tr>
<tr id="row623818614716"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p081074113421"><a name="p081074113421"></a><a name="p081074113421"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p64406284"><a name="p64406284"></a><a name="p64406284"></a>The type of the load balancer.</p>
<p id="p42785651"><a name="p42785651"></a><a name="p42785651"></a>String value expected.</p>
<p id="p49526544"><a name="p49526544"></a><a name="p49526544"></a>Updates cause replacement.</p>
<p id="p43085716"><a name="p43085716"></a><a name="p43085716"></a>Allowed values: External, Internal</p>
</td>
</tr>
<tr id="row623810644718"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p12810174114214"><a name="p12810174114214"></a><a name="p12810174114214"></a>vpc_id</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p15310620"><a name="p15310620"></a><a name="p15310620"></a>The ID of vpc.</p>
<p id="p3577853"><a name="p3577853"></a><a name="p3577853"></a>String value expected.</p>
<p id="p32200678"><a name="p32200678"></a><a name="p32200678"></a>Updates cause replacement.</p>
<div class="note" id="note4572111112532"><a name="note4572111112532"></a><a name="note4572111112532"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p2538989"><a name="p2538989"></a><a name="p2538989"></a>You must specify the VPC ID when using the RTS to perform operations on ELB.</p>
<a name="ul22850903"></a><a name="ul22850903"></a><ul id="ul22850903"><li>Only one VPC is supported for each tenant.</li><li>You must add the VPC ID in the Heat template. (You can query the VPC using the API.)</li></ul>
</div></div>
</td>
</tr>
</tbody>
</table>

## Optional Properties<a name="section94354912391"></a>

<a name="table7782101812441"></a>
<table><thead align="left"><tr id="row8857248194810"><th class="cellrowborder" valign="top" width="34%" id="mcps1.1.3.1.1"><p id="p1078212185448"><a name="p1078212185448"></a><a name="p1078212185448"></a><strong id="b99754054915"><a name="b99754054915"></a><a name="b99754054915"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="66%" id="mcps1.1.3.1.2"><p id="p578281815449"><a name="p578281815449"></a><a name="p578281815449"></a><strong id="b79769034910"><a name="b79769034910"></a><a name="b79769034910"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row14857248194810"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p2782818164413"><a name="p2782818164413"></a><a name="p2782818164413"></a>az</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p22330104"><a name="p22330104"></a><a name="p22330104"></a>The ID or name of the availability zone.</p>
<p id="p66753213"><a name="p66753213"></a><a name="p66753213"></a>String value expected.</p>
<p id="p63908009"><a name="p63908009"></a><a name="p63908009"></a>Updates cause replacement.</p>
<div class="note" id="note16832691114515"><a name="note16832691114515"></a><a name="note16832691114515"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul46242770"></a><a name="ul46242770"></a><ul id="ul46242770"><li>The AZ attribute is mandatory, and you need to specify it.</li><li>If the AZ attribute is not specified, calls are made to the Nova API to randomly select an AZ.</li></ul>
</div></div>
</td>
</tr>
<tr id="row68571448144810"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p8782141820449"><a name="p8782141820449"></a><a name="p8782141820449"></a>bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p4268172"><a name="p4268172"></a><a name="p4268172"></a>The bandwidth of the load balancer, in Mbit/s.</p>
<p id="p38413555"><a name="p38413555"></a><a name="p38413555"></a>Integer value expected.</p>
<p id="p10177679"><a name="p10177679"></a><a name="p10177679"></a>Can be updated without replacement.</p>
<p id="p24490249"><a name="p24490249"></a><a name="p24490249"></a>Allowed values: from 1 to 300, include 1 and 300</p>
<div class="note" id="note539750912510"><a name="note539750912510"></a><a name="note539750912510"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p15387322"><a name="p15387322"></a><a name="p15387322"></a>The default bandwidth size value of an ELB listener is 300, and you can use only the default value.</p>
</div></div>
</td>
</tr>
<tr id="row685784818481"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p578216184446"><a name="p578216184446"></a><a name="p578216184446"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p37553123"><a name="p37553123"></a><a name="p37553123"></a>The description of the load balancer.</p>
<p id="p2433789"><a name="p2433789"></a><a name="p2433789"></a>String value expected.</p>
<p id="p21904105"><a name="p21904105"></a><a name="p21904105"></a>Can be updated without replacement.</p>
<p id="p62919225"><a name="p62919225"></a><a name="p62919225"></a>It is allowed to start with <strong id="b616424474219"><a name="b616424474219"></a><a name="b616424474219"></a>numbers</strong>, <strong id="b10165164464218"><a name="b10165164464218"></a><a name="b10165164464218"></a>letters</strong>, _, and <strong id="b10166174444216"><a name="b10166174444216"></a><a name="b10166174444216"></a>-</strong> characters. It is allowed to include <strong id="b171661144114212"><a name="b171661144114212"></a><a name="b171661144114212"></a>numbers</strong>, <strong id="b11167134474213"><a name="b11167134474213"></a><a name="b11167134474213"></a>letters</strong>, _, and <strong id="b181676449424"><a name="b181676449424"></a><a name="b181676449424"></a>-</strong> characters, and the string length is <strong id="b131671744204214"><a name="b131671744204214"></a><a name="b131671744204214"></a>1</strong> to <strong id="b20155827173610"><a name="b20155827173610"></a><a name="b20155827173610"></a>128</strong>.</p>
</td>
</tr>
<tr id="row108570489482"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p117821418114417"><a name="p117821418114417"></a><a name="p117821418114417"></a>security_group</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p63292461"><a name="p63292461"></a><a name="p63292461"></a>The ID of the security group.</p>
<p id="p32761244"><a name="p32761244"></a><a name="p32761244"></a>String value expected.</p>
<p id="p26415746"><a name="p26415746"></a><a name="p26415746"></a>Updates cause replacement.</p>
</td>
</tr>
<tr id="row885715480482"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p578231864413"><a name="p578231864413"></a><a name="p578231864413"></a>vip_subnet_id</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p59300704"><a name="p59300704"></a><a name="p59300704"></a>The ID of the network on which to allocate the VIP.</p>
<p id="p63944289"><a name="p63944289"></a><a name="p63944289"></a>String value expected.</p>
<p id="p38627694"><a name="p38627694"></a><a name="p38627694"></a>Updates cause replacement.</p>
<p id="p12104926"><a name="p12104926"></a><a name="p12104926"></a>Value must be of type neutron.network</p>
</td>
</tr>
</tbody>
</table>

## Attributes<a name="section7472757103917"></a>

<a name="table8933142844616"></a>
<table><thead align="left"><tr id="row2075675335017"><th class="cellrowborder" valign="top" width="34%" id="mcps1.1.3.1.1"><p id="p993432874615"><a name="p993432874615"></a><a name="p993432874615"></a><strong id="b1728225205119"><a name="b1728225205119"></a><a name="b1728225205119"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="66%" id="mcps1.1.3.1.2"><p id="p13934152884619"><a name="p13934152884619"></a><a name="p13934152884619"></a><strong id="b102831510516"><a name="b102831510516"></a><a name="b102831510516"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1475615311502"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p893419284462"><a name="p893419284462"></a><a name="p893419284462"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p593472824618"><a name="p593472824618"></a><a name="p593472824618"></a>The status of the load balancer.</p>
</td>
</tr>
<tr id="row2757953155014"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p7934628144612"><a name="p7934628144612"></a><a name="p7934628144612"></a>vip_address</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p179345282469"><a name="p179345282469"></a><a name="p179345282469"></a>The VIP address of the load balancer.</p>
</td>
</tr>
<tr id="row1775785312502"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p093402884612"><a name="p093402884612"></a><a name="p093402884612"></a>vip_subnet_id</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p29341428104610"><a name="p29341428104610"></a><a name="p29341428104610"></a>The VIP subnet of the load balancer.</p>
</td>
</tr>
</tbody>
</table>

## HOT Syntax<a name="section14600126154012"></a>

```
heat_template_version: 2014-10-16
...
resources:
  ...
  the_resource:
    type: OSE::ELB::LoadBalancer
    properties:
      admin_state_up: Boolean
      az: String
      bandwidth: Integer
      description: String
      name: String
      security_group: String
      type: String
      vip_subnet_id: String
      vpc_id: String
```

