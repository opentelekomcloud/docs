# Forwarding Policy<a name="EN-US_TOPIC_0114694934"></a>

## Scenarios<a name="section79409283156"></a>

Enhanced load balancers allow you to add forwarding policies to forward requests based on domain names or URLs. This function is only supported for HTTP or HTTPS listeners.

A maximum of 500 forwarding policies can be added to a listener. Requests for videos, images, audio, or text are forwarded to different backend server groups, making it easy to allocate resources.

After a forwarding policy is added, the load balancer forwards requests based on the specified domain name or URL:

-   If the domain name or URL in a request matches the forwarding policy, the request is forwarded to the backend server group you configured when adding the forwarding policy.
-   If the domain name or URL in a request does not match the forwarding policy, the request is forwarded to the default backend server group associated with the listener.

## Add a Forwarding Policy<a name="section191183222317"></a>

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/en-us_image_0114695108.png)  and select the desired region and project.
3.  Click  **Service List**. Under  **Network**, click  **Elastic Load Balancing**.
4.  Locate the target load balancer and click its name.
5.  Click  **Listeners**, locate the target listener, and click its name.
6.  Click  **Add**  on the right of  **Forwarding Policies**.
7.  In the  **Add Forwarding Policy**  dialog box, specify the parameters by referring to  [Table 1](#table10859681016).
8.  Click  **OK**.

    Alternatively, locate the target load balancer and click its name to switch to the details page. In the  **Listeners**  area, click  **Add**  on the right of  **Forwarding Policies**  and then add a forwarding policy.


**Table  1**  Forwarding policy parameters

<a name="table10859681016"></a>
<table><thead align="left"><tr id="row109196141011"><th class="cellrowborder" valign="top" width="16.16161616161616%" id="mcps1.2.5.1.1"><p id="p205701231181017"><a name="p205701231181017"></a><a name="p205701231181017"></a><strong id="b84235270615222"><a name="b84235270615222"></a><a name="b84235270615222"></a>Item</strong></p>
</th>
<th class="cellrowborder" valign="top" width="19.321932193219325%" id="mcps1.2.5.1.2"><p id="p69376201010"><a name="p69376201010"></a><a name="p69376201010"></a><strong>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="47.97479747974798%" id="mcps1.2.5.1.3"><p id="p294665107"><a name="p294665107"></a><a name="p294665107"></a><strong id="b501472349"><a name="b501472349"></a><a name="b501472349"></a>Description</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.541654165416542%" id="mcps1.2.5.1.4"><p id="p119718601010"><a name="p119718601010"></a><a name="p119718601010"></a><strong id="b159418934"><a name="b159418934"></a><a name="b159418934"></a>Example Value</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row141006651018"><td class="cellrowborder" rowspan="5" valign="top" width="16.16161616161616%" headers="mcps1.2.5.1.1 "><p id="p457093112107"><a name="p457093112107"></a><a name="p457093112107"></a>Configure Forwarding Policy</p>
</td>
<td class="cellrowborder" valign="top" width="19.321932193219325%" headers="mcps1.2.5.1.2 "><p id="p171025641010"><a name="p171025641010"></a><a name="p171025641010"></a>Name</p>
</td>
<td class="cellrowborder" valign="top" width="47.97479747974798%" headers="mcps1.2.5.1.3 "><p id="p510396141018"><a name="p510396141018"></a><a name="p510396141018"></a>Specifies the forwarding policy name.</p>
</td>
<td class="cellrowborder" valign="top" width="16.541654165416542%" headers="mcps1.2.5.1.4 "><p id="p5104136141017"><a name="p5104136141017"></a><a name="p5104136141017"></a>forwarding_policy-q582</p>
</td>
</tr>
<tr id="row15105761109"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p2107062104"><a name="p2107062104"></a><a name="p2107062104"></a>Domain Name</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p210718619109"><a name="p210718619109"></a><a name="p210718619109"></a>Specifies the domain name for triggering the forwarding policy. The specified domain name will be exactly matched. Note that either a domain name or URL must be specified.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p4108167108"><a name="p4108167108"></a><a name="p4108167108"></a>www.test.com</p>
</td>
</tr>
<tr id="row16108186101017"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p911056121017"><a name="p911056121017"></a><a name="p911056121017"></a>URL</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p18111176151015"><a name="p18111176151015"></a><a name="p18111176151015"></a>Specifies the URL for triggering the forwarding policy.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p511313661015"><a name="p511313661015"></a><a name="p511313661015"></a>/login.php</p>
</td>
</tr>
<tr id="row11113116161018"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p171138691020"><a name="p171138691020"></a><a name="p171138691020"></a>URL Matching Rule</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><a name="ul141168619107"></a><a name="ul141168619107"></a><ul id="ul141168619107"><li><strong id="b70231846"><a name="b70231846"></a><a name="b70231846"></a>Exact match</strong><p id="p17117367106"><a name="p17117367106"></a><a name="p17117367106"></a>The request URL is identical to the preset URL.</p>
</li><li><strong id="b215297650"><a name="b215297650"></a><a name="b215297650"></a>Prefix match</strong><p id="p1111820611102"><a name="p1111820611102"></a><a name="p1111820611102"></a>The requested URL starts with the specified URL string.</p>
</li><li><strong id="b1923641375"><a name="b1923641375"></a><a name="b1923641375"></a>Regular expression match</strong><div class="p" id="p1612017621016"><a name="p1612017621016"></a><a name="p1612017621016"></a>The requested URL matches the specified URL string based on the regular expression.<div class="note" id="note15121066104"><a name="note15121066104"></a><a name="note15121066104"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p57071461154245"><a name="p57071461154245"></a><a name="p57071461154245"></a><strong id="b1280834494519"><a name="b1280834494519"></a><a name="b1280834494519"></a>Exact match</strong> enjoys the highest priority, followed by <strong id="b1886234814455"><a name="b1886234814455"></a><a name="b1886234814455"></a>Prefix match</strong>. <strong id="b18195185313454"><a name="b18195185313454"></a><a name="b18195185313454"></a>Regular expression match</strong> is the last matching rule that will be used.</p>
</div></div>
</div>
</li></ul>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p19123167101"><a name="p19123167101"></a><a name="p19123167101"></a>Exact match</p>
</td>
</tr>
<tr id="row151292617103"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p413126171017"><a name="p413126171017"></a><a name="p413126171017"></a>Description</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p013218618109"><a name="p013218618109"></a><a name="p013218618109"></a>Provides supplementary information about the forwarding policy.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p213376191011"><a name="p213376191011"></a><a name="p213376191011"></a>N/A</p>
</td>
</tr>
<tr id="row2079614577109"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.2.5.1.1 "><p id="p7796857121015"><a name="p7796857121015"></a><a name="p7796857121015"></a>Add Backend Server Group</p>
</td>
<td class="cellrowborder" valign="top" width="19.321932193219325%" headers="mcps1.2.5.1.2 "><p id="p19796145771015"><a name="p19796145771015"></a><a name="p19796145771015"></a>Backend Server Group</p>
</td>
<td class="cellrowborder" valign="top" width="47.97479747974798%" headers="mcps1.2.5.1.3 "><p id="p81191352185715"><a name="p81191352185715"></a><a name="p81191352185715"></a>Specifies whether a new or existing backend server group will be used. You can select <strong id="b311819527573"><a name="b311819527573"></a><a name="b311819527573"></a>Create new</strong> or <strong id="b16118105212572"><a name="b16118105212572"></a><a name="b16118105212572"></a>Use existing</strong>.</p>
<p id="p184301216593"><a name="p184301216593"></a><a name="p184301216593"></a>If you select <strong id="b9300195912574"><a name="b9300195912574"></a><a name="b9300195912574"></a>Create new</strong>, set parameters by referring to <a href="adding-or-removing-backend-servers-from-an-enhanced-load-balancer.md#en-us_topic_0091131437_table83118104911">Table 1</a> and <a href="adding-or-removing-backend-servers-from-an-enhanced-load-balancer.md#en-us_topic_0091131437_table736610293">Table 2</a>.</p>
<div class="note" id="note085961618274"><a name="note085961618274"></a><a name="note085961618274"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p13859616142716"><a name="p13859616142716"></a><a name="p13859616142716"></a>The backend protocol can only be HTTP.</p>
</div></div>
</td>
<td class="cellrowborder" valign="top" width="16.541654165416542%" headers="mcps1.2.5.1.4 "><p id="p87961057131011"><a name="p87961057131011"></a><a name="p87961057131011"></a>Create new</p>
</td>
</tr>
</tbody>
</table>

## URL Matching Example<a name="section19645182316511"></a>

The following table lists how a URL is matched, and  [Figure 1](#fig87121434403)  shows how a request is forwarded to a backend server group.

**Table  2**  URL matching

<a name="table5831113119590"></a>
<table><thead align="left"><tr id="row4697541666"><th class="cellrowborder" valign="top" id="mcps1.2.7.1.1"><p id="p669813413615"><a name="p669813413615"></a><a name="p669813413615"></a><strong id="b842352706142041"><a name="b842352706142041"></a><a name="b842352706142041"></a>URL Matching Rule</strong></p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.2.7.1.2"><p id="p969884114610"><a name="p969884114610"></a><a name="p969884114610"></a><strong id="b8423527069304"><a name="b8423527069304"></a><a name="b8423527069304"></a>URL</strong></p>
</th>
<th class="cellrowborder" colspan="4" valign="top" id="mcps1.2.7.1.3"><p id="p193919591169"><a name="p193919591169"></a><a name="p193919591169"></a><strong id="b8423527069308"><a name="b8423527069308"></a><a name="b8423527069308"></a>Preset URL</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1289643195912"><td class="cellrowborder" valign="top" width="19.69393878775755%" headers="mcps1.2.7.1.1 "><p id="p17134761873"><a name="p17134761873"></a><a name="p17134761873"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="15.053010602120423%" headers="mcps1.2.7.1.2 "><p id="p17134567713"><a name="p17134567713"></a><a name="p17134567713"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="16.313262652530504%" headers="mcps1.2.7.1.3 "><p id="p1089663175919"><a name="p1089663175919"></a><a name="p1089663175919"></a>/elb/index.html</p>
</td>
<td class="cellrowborder" valign="top" width="16.313262652530504%" headers="mcps1.2.7.1.3 "><p id="p6896113175915"><a name="p6896113175915"></a><a name="p6896113175915"></a>/elb</p>
</td>
<td class="cellrowborder" valign="top" width="16.313262652530504%" headers="mcps1.2.7.1.3 "><p id="p1689673113599"><a name="p1689673113599"></a><a name="p1689673113599"></a>/elb[^\s]*</p>
</td>
<td class="cellrowborder" valign="top" width="16.313262652530504%" headers="mcps1.2.7.1.3 "><p id="p3896731205919"><a name="p3896731205919"></a><a name="p3896731205919"></a>/index.html</p>
</td>
</tr>
<tr id="row2896103116597"><td class="cellrowborder" valign="top" width="19.69393878775755%" headers="mcps1.2.7.1.1 "><p id="p1689783116593"><a name="p1689783116593"></a><a name="p1689783116593"></a>Exact match</p>
</td>
<td class="cellrowborder" rowspan="3" valign="top" width="15.053010602120423%" headers="mcps1.2.7.1.2 "><p id="p118978317599"><a name="p118978317599"></a><a name="p118978317599"></a>/elb/index.html</p>
</td>
<td class="cellrowborder" valign="top" width="16.313262652530504%" headers="mcps1.2.7.1.3 "><p id="p38975312592"><a name="p38975312592"></a><a name="p38975312592"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="16.313262652530504%" headers="mcps1.2.7.1.3 "><p id="p17897103116599"><a name="p17897103116599"></a><a name="p17897103116599"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="16.313262652530504%" headers="mcps1.2.7.1.3 "><p id="p289713114590"><a name="p289713114590"></a><a name="p289713114590"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="16.313262652530504%" headers="mcps1.2.7.1.3 "><p id="p1189733155917"><a name="p1189733155917"></a><a name="p1189733155917"></a>-</p>
</td>
</tr>
<tr id="row198979312599"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p7897103195912"><a name="p7897103195912"></a><a name="p7897103195912"></a>Prefix match</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p989713315591"><a name="p989713315591"></a><a name="p989713315591"></a>√</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p1589763110598"><a name="p1589763110598"></a><a name="p1589763110598"></a>√</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p1489753118593"><a name="p1489753118593"></a><a name="p1489753118593"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p18897183115599"><a name="p18897183115599"></a><a name="p18897183115599"></a>-</p>
</td>
</tr>
<tr id="row18971031195914"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p13897631125920"><a name="p13897631125920"></a><a name="p13897631125920"></a>Regular expression match</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p289715311594"><a name="p289715311594"></a><a name="p289715311594"></a>√</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p11897173105916"><a name="p11897173105916"></a><a name="p11897173105916"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p489714312592"><a name="p489714312592"></a><a name="p489714312592"></a>√</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p10897731155915"><a name="p10897731155915"></a><a name="p10897731155915"></a>-</p>
</td>
</tr>
</tbody>
</table>

**Figure  1**  Request forwarding<a name="fig87121434403"></a>  
![](figures/request-forwarding.jpg "request-forwarding")

In this figure, the system first searches the requested URL \(/elb\_gls/glossary.html\) using the  **Exact match**  rule. If no exactly matched URL is found, the  **Prefix match**  rule is used. If the start string of the requested URL matches that of specified URL, the request is forwarded to backend server group 2. Even if the requested URL also matches rule 3 \(**Regular expression match**\), the request is forwarded to backend server group 2 because  **Prefix match**  takes effect in priority.

## Modify a Forwarding Policy<a name="section0239201242216"></a>

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/en-us_image_0155033570.png)  and select the desired region and project.
3.  Click  **Service List**. Under  **Network**, click  **Elastic Load Balancing**.
4.  Locate the target load balancer and click its name.
5.  Click  **Listeners**, locate the target listener, and click its name.
6.  Click  **Forwarding Policies**. 
7.  Locate the target forwarding policy and click  ![](figures/en-us_image_0155041158.png)  on the right of its name.
8.  In the  **Modify Forwarding Policy**  dialog box, modify the parameters and click  **OK**.

## Delete a Forwarding Policy<a name="section4306132117396"></a>

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/en-us_image_0121143837.png)  and select the desired region and project.
3.  Click  **Service List**. Under  **Network**, click  **Elastic Load Balancing**.
4.  Locate the target load balancer and click its name.
5.  Click  **Listeners**, locate the target listener, and click its name.
6.  Click  **Forwarding Policies**. 
7.  Locate the target forwarding policy and click  ![](figures/en-us_image_0155036235.png)  on the right of its name.
8.  In the displayed dialog box, click  **Yes**.

