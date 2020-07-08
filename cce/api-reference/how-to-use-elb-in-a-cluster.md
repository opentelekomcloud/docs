# How to Use ELB in a Cluster<a name="cce_02_0087"></a>

This section describes how to use the Elastic Load Balancer \(ELB\) in a cluster created by CCE.

## Procedure<a name="section50156865193415"></a>

Create a Service. For details about how to use an open-source API to create a Service, See  [Creating a Service](creating-a-service.md).

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>Before enabling sticky session, ensure that the following conditions are met:  
>-   The workload protocol is TCP.  
>-   Anti-affinity has been configured between pods of the workload. That is, all pods of the workload are deployed on different nodes.  

Automatically creating an ELB:

```
apiVersion: v1 
kind: Service 
metadata: 
  annotations:   
    kubernetes.io/elb.class: union
    kubernetes.io/session-affinity-mode: SOURCE_IP
    kubernetes.io/elb.subnet-id: 5083f225-9bf8-48fa-9c8b-67bd9693c4c0
    kubernetes.io/elb.autocreate: "{\"type\":\"public\",\"bandwidth_name\":\"cce-bandwidth-1551163379627\",\"bandwidth_chargemode\":\"traffic\",\"bandwidth_size\":5,\"bandwidth_sharetype\":\"PER\",\"eip_type\":\"5_bgp\",\"name\":\"james\"}"
  labels: 
    app: nginx 
  name: nginx 
spec: 
  externalTrafficPolicy: Local
  ports: 
  - name: service0 
    port: 80
    protocol: TCP 
    targetPort: 80
  selector: 
    app: nginx 
  type: LoadBalancer
```

Using an existing ELB:

```
apiVersion: v1 
kind: Service 
metadata: 
  annotations:   
    kubernetes.io/elb.class: union
    kubernetes.io/session-affinity-mode: SOURCE_IP
    kubernetes.io/elb.id: 3c7caa5a-a641-4bff-801a-feace27424b6
    kubernetes.io/elb.subnet-id: 5083f225-9bf8-48fa-9c8b-67bd9693c4c0
  labels: 
    app: nginx 
  name: nginx 
spec: 
  loadBalancerIP: 10.78.42.242
  externalTrafficPolicy: Local
  ports: 
  - name: service0 
    port: 80
    protocol: TCP 
    targetPort: 80
  selector: 
    app: nginx 
  type: LoadBalancer
```

**Table  1**  Key parameters

<a name="table1819001615355"></a>
<table><thead align="left"><tr id="row1519121663519"><th class="cellrowborder" valign="top" width="34.28657134286571%" id="mcps1.2.4.1.1"><p id="p18191161619356"><a name="p18191161619356"></a><a name="p18191161619356"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.118588141185882%" id="mcps1.2.4.1.2"><p id="p1191141613357"><a name="p1191141613357"></a><a name="p1191141613357"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51.594840515948405%" id="mcps1.2.4.1.3"><p id="p1919116161353"><a name="p1919116161353"></a><a name="p1919116161353"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row7430236123515"><td class="cellrowborder" valign="top" width="34.28657134286571%" headers="mcps1.2.4.1.1 "><p id="p2430336153520"><a name="p2430336153520"></a><a name="p2430336153520"></a>kubernetes.io/elb.class</p>
</td>
<td class="cellrowborder" valign="top" width="14.118588141185882%" headers="mcps1.2.4.1.2 "><p id="p19430103693512"><a name="p19430103693512"></a><a name="p19430103693512"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="p1380805311426"><a name="p1380805311426"></a><a name="p1380805311426"></a>Mandatory and must be set to <span class="uicontrol" id="uicontrol16781216134315"><a name="uicontrol16781216134315"></a><a name="uicontrol16781216134315"></a><b>union</b></span> if an enhanced load balancer is in use.</p>
</td>
</tr>
<tr id="row15191171618357"><td class="cellrowborder" valign="top" width="34.28657134286571%" headers="mcps1.2.4.1.1 "><p id="p204451615124716"><a name="p204451615124716"></a><a name="p204451615124716"></a>kubernetes.io/session-affinity-mode</p>
</td>
<td class="cellrowborder" valign="top" width="14.118588141185882%" headers="mcps1.2.4.1.2 "><p id="p1090683224719"><a name="p1090683224719"></a><a name="p1090683224719"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="p12830929125713"><a name="p12830929125713"></a><a name="p12830929125713"></a>Optional. If sticky session is enabled, add this parameter.</p>
<p id="p16904132104710"><a name="p16904132104710"></a><a name="p16904132104710"></a>The value <strong id="b10851032194318"><a name="b10851032194318"></a><a name="b10851032194318"></a>SOURCE_IP</strong> indicates that listeners ensure sticky session based on source IP addresses.</p>
</td>
</tr>
<tr id="row81941516153513"><td class="cellrowborder" valign="top" width="34.28657134286571%" headers="mcps1.2.4.1.1 "><p id="p4764162894719"><a name="p4764162894719"></a><a name="p4764162894719"></a>kubernetes.io/elb.id</p>
</td>
<td class="cellrowborder" valign="top" width="14.118588141185882%" headers="mcps1.2.4.1.2 "><p id="p77621528184710"><a name="p77621528184710"></a><a name="p77621528184710"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="p59344376579"><a name="p59344376579"></a><a name="p59344376579"></a>Optional. This parameter is mandatory if an existing ELB is used.</p>
<p id="p416573016509"><a name="p416573016509"></a><a name="p416573016509"></a>It indicates the ID of an enhanced load balancer.</p>
</td>
</tr>
<tr id="row201957167350"><td class="cellrowborder" valign="top" width="34.28657134286571%" headers="mcps1.2.4.1.1 "><p id="p18758202864719"><a name="p18758202864719"></a><a name="p18758202864719"></a>kubernetes.io/elb.subnet-id</p>
</td>
<td class="cellrowborder" valign="top" width="14.118588141185882%" headers="mcps1.2.4.1.2 "><p id="p336744055219"><a name="p336744055219"></a><a name="p336744055219"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="p2075662814474"><a name="p2075662814474"></a><a name="p2075662814474"></a>Optional. This parameter is mandatory only if a load balancer will be automatically created. For clusters of v1.11.7-r0 or later, this parameter can be left unspecified.</p>
</td>
</tr>
<tr id="row1719518169356"><td class="cellrowborder" valign="top" width="34.28657134286571%" headers="mcps1.2.4.1.1 "><p id="p9754162844712"><a name="p9754162844712"></a><a name="p9754162844712"></a>kubernetes.io/elb.autocreate</p>
</td>
<td class="cellrowborder" valign="top" width="14.118588141185882%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0079615000_p32706975"><a name="en-us_topic_0079615000_p32706975"></a><a name="en-us_topic_0079615000_p32706975"></a><a href="#table19417184671919">elb.autocreate</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="p127521028194718"><a name="p127521028194718"></a><a name="p127521028194718"></a>Optional. This parameter is mandatory if a public network load balancer will be automatically created. The system will create an enhanced load balancer and an EIP. This parameter is also mandatory if a private network load balancer will be automatically created. The system will create an enhanced load balancer.</p>
<p id="p115519391615"><a name="p115519391615"></a><a name="p115519391615"></a><strong id="b1574518310446"><a name="b1574518310446"></a><a name="b1574518310446"></a>Example:</strong></p>
<a name="ul286913611614"></a><a name="ul286913611614"></a><ul id="ul286913611614"><li>Value for a public network load balancer that is automatically created: "{\"type\":\"public\",\"bandwidth_name\":\"cce-bandwidth-1551163379627\",\"bandwidth_chargemode\":\"traffic\",\"bandwidth_size\":5,\"bandwidth_sharetype\":\"PER\",\"eip_type\":\"5_bgp\",\"name\":\"james\"}"</li><li>Value for a private network load balancer that is automatically created: "{\"type\":\"inner\"}"</li></ul>
</td>
</tr>
<tr id="row121515334113"><td class="cellrowborder" valign="top" width="34.28657134286571%" headers="mcps1.2.4.1.1 "><p id="p92162033131111"><a name="p92162033131111"></a><a name="p92162033131111"></a>loadBalancerIP</p>
</td>
<td class="cellrowborder" valign="top" width="14.118588141185882%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0079615000_p47822814"><a name="en-us_topic_0079615000_p47822814"></a><a name="en-us_topic_0079615000_p47822814"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="p7217113331120"><a name="p7217113331120"></a><a name="p7217113331120"></a>Private IP address of a private network load balancer or public IP address of a public network load balancer.</p>
</td>
</tr>
<tr id="row14980162901115"><td class="cellrowborder" valign="top" width="34.28657134286571%" headers="mcps1.2.4.1.1 "><p id="p398162913117"><a name="p398162913117"></a><a name="p398162913117"></a>externalTrafficPolicy</p>
</td>
<td class="cellrowborder" valign="top" width="14.118588141185882%" headers="mcps1.2.4.1.2 "><p id="p142173231413"><a name="p142173231413"></a><a name="p142173231413"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="p119811329111112"><a name="p119811329111112"></a><a name="p119811329111112"></a>Optional. If sticky session is enabled, add this parameter so requests are transferred to a fixed node. If a LoadBalancer Service with this parameter set to <strong id="b134197138450"><a name="b134197138450"></a><a name="b134197138450"></a>Local</strong> is created for a workload, the workload can be accessed only when the client is installed on the same node as the server.</p>
</td>
</tr>
<tr id="row17120113981313"><td class="cellrowborder" valign="top" width="34.28657134286571%" headers="mcps1.2.4.1.1 "><p id="p17120639161311"><a name="p17120639161311"></a><a name="p17120639161311"></a>port</p>
</td>
<td class="cellrowborder" valign="top" width="14.118588141185882%" headers="mcps1.2.4.1.2 "><p id="p1120939161311"><a name="p1120939161311"></a><a name="p1120939161311"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="p1120163961310"><a name="p1120163961310"></a><a name="p1120163961310"></a>Access port that is registered on the load balancer and mapped to the cluster-internal IP address.</p>
</td>
</tr>
<tr id="row02694357138"><td class="cellrowborder" valign="top" width="34.28657134286571%" headers="mcps1.2.4.1.1 "><p id="p627233515132"><a name="p627233515132"></a><a name="p627233515132"></a>targetPort</p>
</td>
<td class="cellrowborder" valign="top" width="14.118588141185882%" headers="mcps1.2.4.1.2 "><p id="p19272143531318"><a name="p19272143531318"></a><a name="p19272143531318"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="p8272035161316"><a name="p8272035161316"></a><a name="p8272035161316"></a>Container port on the CCE console.</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  Data structure of the  **elb.autocreate**  field

<a name="table19417184671919"></a>
<table><thead align="left"><tr id="row14418174611912"><th class="cellrowborder" valign="top" width="29.727027297270276%" id="mcps1.2.4.1.1"><p id="p1141924611199"><a name="p1141924611199"></a><a name="p1141924611199"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18.678132186781323%" id="mcps1.2.4.1.2"><p id="p1641911466191"><a name="p1641911466191"></a><a name="p1641911466191"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51.594840515948405%" id="mcps1.2.4.1.3"><p id="p1941920463197"><a name="p1941920463197"></a><a name="p1941920463197"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row194191846181915"><td class="cellrowborder" valign="top" width="29.727027297270276%" headers="mcps1.2.4.1.1 "><p id="p152321411112318"><a name="p152321411112318"></a><a name="p152321411112318"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="18.678132186781323%" headers="mcps1.2.4.1.2 "><p id="p7419646171920"><a name="p7419646171920"></a><a name="p7419646171920"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="p87791494919"><a name="p87791494919"></a><a name="p87791494919"></a>Name of the load balancer that is automatically created.</p>
<p id="p9912132016296"><a name="p9912132016296"></a><a name="p9912132016296"></a>The value is a string of 1 to 64 characters that consist of letters, digits, underscores (_), and hyphens (-).</p>
</td>
</tr>
<tr id="row142064681919"><td class="cellrowborder" valign="top" width="29.727027297270276%" headers="mcps1.2.4.1.1 "><p id="p20862285225"><a name="p20862285225"></a><a name="p20862285225"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="18.678132186781323%" headers="mcps1.2.4.1.2 "><p id="p8420746101918"><a name="p8420746101918"></a><a name="p8420746101918"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="p4703183013491"><a name="p4703183013491"></a><a name="p4703183013491"></a>Network type of the load balancer.</p>
<a name="ul152311045124913"></a><a name="ul152311045124913"></a><ul id="ul152311045124913"><li><strong id="b569141515463"><a name="b569141515463"></a><a name="b569141515463"></a>public</strong>: public network load balancer.</li><li><strong id="b1443315167463"><a name="b1443315167463"></a><a name="b1443315167463"></a>inner</strong>: private network load balancer.</li></ul>
</td>
</tr>
<tr id="row194201046151910"><td class="cellrowborder" valign="top" width="29.727027297270276%" headers="mcps1.2.4.1.1 "><p id="p128042817221"><a name="p128042817221"></a><a name="p128042817221"></a>bandwidth_name</p>
</td>
<td class="cellrowborder" valign="top" width="18.678132186781323%" headers="mcps1.2.4.1.2 "><p id="p1142084619195"><a name="p1142084619195"></a><a name="p1142084619195"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="p6964103318220"><a name="p6964103318220"></a><a name="p6964103318220"></a>Bandwidth name. The default value is <strong id="b13335121924617"><a name="b13335121924617"></a><a name="b13335121924617"></a>cce-bandwidth-******</strong>.</p>
<p id="p1236952875020"><a name="p1236952875020"></a><a name="p1236952875020"></a>The value is a string of 1 to 64 characters that consist of letters, digits, underscores (_), hyphens (-), and periods (.).</p>
</td>
</tr>
<tr id="row942194619199"><td class="cellrowborder" valign="top" width="29.727027297270276%" headers="mcps1.2.4.1.1 "><p id="p77502811221"><a name="p77502811221"></a><a name="p77502811221"></a>bandwidth_chargemode</p>
</td>
<td class="cellrowborder" valign="top" width="18.678132186781323%" headers="mcps1.2.4.1.2 "><p id="p11421446191914"><a name="p11421446191914"></a><a name="p11421446191914"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="p3178181495216"><a name="p3178181495216"></a><a name="p3178181495216"></a>Bandwidth billing mode.</p>
<p id="p17993157195913"><a name="p17993157195913"></a><a name="p17993157195913"></a>The value is <strong id="b267410514014"><a name="b267410514014"></a><a name="b267410514014"></a>traffic</strong>, indicating that the billing is based on traffic.</p>
</td>
</tr>
<tr id="row124211046101910"><td class="cellrowborder" valign="top" width="29.727027297270276%" headers="mcps1.2.4.1.1 "><p id="p187492819229"><a name="p187492819229"></a><a name="p187492819229"></a>bandwidth_size</p>
</td>
<td class="cellrowborder" valign="top" width="18.678132186781323%" headers="mcps1.2.4.1.2 "><p id="p114229463196"><a name="p114229463196"></a><a name="p114229463196"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="p12958233152218"><a name="p12958233152218"></a><a name="p12958233152218"></a>Bandwidth size.</p>
</td>
</tr>
<tr id="row1942224601917"><td class="cellrowborder" valign="top" width="29.727027297270276%" headers="mcps1.2.4.1.1 "><p id="p16731228202214"><a name="p16731228202214"></a><a name="p16731228202214"></a>bandwidth_sharetype</p>
</td>
<td class="cellrowborder" valign="top" width="18.678132186781323%" headers="mcps1.2.4.1.2 "><p id="p84221246111913"><a name="p84221246111913"></a><a name="p84221246111913"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="p188864421731"><a name="p188864421731"></a><a name="p188864421731"></a>Bandwidth sharing mode.</p>
<a name="ul51872412"></a><a name="ul51872412"></a><ul id="ul51872412"><li><strong id="b165472015185110"><a name="b165472015185110"></a><a name="b165472015185110"></a>PER</strong>: dedicated bandwidth.</li><li><strong id="b820421695110"><a name="b820421695110"></a><a name="b820421695110"></a>WHOLE</strong>: shared bandwidth.</li></ul>
</td>
</tr>
<tr id="row1242219461193"><td class="cellrowborder" valign="top" width="29.727027297270276%" headers="mcps1.2.4.1.1 "><p id="p1972102872220"><a name="p1972102872220"></a><a name="p1972102872220"></a>eip_type</p>
</td>
<td class="cellrowborder" valign="top" width="18.678132186781323%" headers="mcps1.2.4.1.2 "><p id="p132201811174611"><a name="p132201811174611"></a><a name="p132201811174611"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="p11956103372218"><a name="p11956103372218"></a><a name="p11956103372218"></a>EIP type.</p>
</td>
</tr>
</tbody>
</table>

