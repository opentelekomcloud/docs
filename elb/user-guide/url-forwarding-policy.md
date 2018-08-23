# URL Forwarding Policy<a name="EN-US_TOPIC_0114694934"></a>

## Scenarios<a name="section79409283156"></a>

Enhanced load balancers allow you to add forwarding policies to forward the requests from different clients to different backend ECS groups based on the domain names or URLs specified in the forwarding policies. Currently, you can add forwarding policies only for load balancers with the frontend protocol set to HTTP or HTTPS.

You can add a maximum of 20 forwarding policies. This allows you to easily forward video, image, audio, and text requests to different backend ECS groups for processing, improving the flexibility of service traffic distribution and facilitating resource allocation.

After a forwarding policy is added, the enhanced load balancer will forward frontend requests based on the following rules:

-   If the forwarding policy is matched, the request is forwarded to the backend ECS group based on this forwarding policy.
-   If the forwarding policy is not matched, the request is forwarded to the backend ECS group of the listener.

## Add a Forwarding Policy<a name="section191183222317"></a>

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/en-us_image_0114695108.png)  and select the desired region and project.
3.  Under  **Network**, click  **Elastic Load Balance**.
4.  On the  **Elastic Load Balance**  page, click the name of the target enhanced load balancer.
5.  Locate the listener to which a forwarding policy is to be added, click  **More**  in the  **Operation**  column, and select  **Add Forwarding Policy**  from the drop-down list.
6.  In the  **Forwarding Policy**  area, click  **Add Forwarding Policy**. In the displayed  **Add Forwarding Policy**  dialog box, specify the parameters based on  [Table 1](#table5765638104311).

**Table  1**  Forwarding policy parameters

<a name="table5765638104311"></a><table><thead align="left"><tr id="row16766173884314"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p16337205034318"><a name="p16337205034318"></a><a name="p16337205034318"></a><strong id="b842352706114331"><a name="b842352706114331"></a><a name="b842352706114331"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p2033814509436"><a name="p2033814509436"></a><a name="p2033814509436"></a><strong id="b8423527061772"><a name="b8423527061772"></a><a name="b8423527061772"></a>Description</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p9339165064318"><a name="p9339165064318"></a><a name="p9339165064318"></a><strong id="b842352706194150"><a name="b842352706194150"></a><a name="b842352706194150"></a>Example Value</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row37661383435"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p133414501436"><a name="p133414501436"></a><a name="p133414501436"></a>Name</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p73421750174316"><a name="p73421750174316"></a><a name="p73421750174316"></a>Specifies the forwarding policy name.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p334485017432"><a name="p334485017432"></a><a name="p334485017432"></a>l7policy-l2dc</p>
</td>
</tr>
<tr id="row9766113813431"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p19345250184318"><a name="p19345250184318"></a><a name="p19345250184318"></a>Domain Name</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p3347150204315"><a name="p3347150204315"></a><a name="p3347150204315"></a>Specifies the domain name for triggering the forwarding. Only exact match domain names are supported.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p3348165018433"><a name="p3348165018433"></a><a name="p3348165018433"></a>www.test.com</p>
</td>
</tr>
<tr id="row1176663812438"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p16350450104312"><a name="p16350450104312"></a><a name="p16350450104312"></a>URL</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p935219504434"><a name="p935219504434"></a><a name="p935219504434"></a>Specifies the URL for triggering the forwarding.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p9352155014316"><a name="p9352155014316"></a><a name="p9352155014316"></a>/login.php</p>
</td>
</tr>
<tr id="row776611380435"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p18354165016434"><a name="p18354165016434"></a><a name="p18354165016434"></a>URL Mapping Rule</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><a name="ul64331319184618"></a><a name="ul64331319184618"></a><ul id="ul64331319184618"><li id="li1343331913466"><a name="li1343331913466"></a><a name="li1343331913466"></a>Exact match<p id="p11249142118464"><a name="p11249142118464"></a><a name="p11249142118464"></a>The request URL is identical to the preset URL.</p>
</li><li id="li443318199466"><a name="li443318199466"></a><a name="li443318199466"></a>Prefix match<p id="p16368182216466"><a name="p16368182216466"></a><a name="p16368182216466"></a>The request URL matches the header of the preset URL.</p>
</li><li id="li2043314194460"><a name="li2043314194460"></a><a name="li2043314194460"></a>Regular expression match<div class="p" id="p126501338475"><a name="p126501338475"></a><a name="p126501338475"></a>The request URL matches the preset URL using the regular expression.<div class="note" id="note114701432124618"><a name="note114701432124618"></a><a name="note114701432124618"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p25204923195731"><a name="p25204923195731"></a><a name="p25204923195731"></a><strong id="b55227770195635"><a name="b55227770195635"></a><a name="b55227770195635"></a>Exact match</strong> enjoys the highest priority, followed by <strong id="b11072296195640"><a name="b11072296195640"></a><a name="b11072296195640"></a>Prefix match</strong>. <strong id="b51221551195650"><a name="b51221551195650"></a><a name="b51221551195650"></a>Regular expression match</strong> is the last matching rule that will be used.</p>
</div></div>
</div>
</li></ul>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p83592503434"><a name="p83592503434"></a><a name="p83592503434"></a>N/A</p>
</td>
</tr>
<tr id="row1176610389439"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1036175020432"><a name="p1036175020432"></a><a name="p1036175020432"></a>Forwarded To</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p7362250194319"><a name="p7362250194319"></a><a name="p7362250194319"></a>Specifies the backend ECS group for handling the requests. A backend ECS group is a necessary part of ELB and used to receive and handle the requests forwarded by the listener.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1636215012437"><a name="p1636215012437"></a><a name="p1636215012437"></a>pool-nvhc</p>
</td>
</tr>
<tr id="row376613818433"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1636455016433"><a name="p1636455016433"></a><a name="p1636455016433"></a>Description</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p17364205017435"><a name="p17364205017435"></a><a name="p17364205017435"></a>Provides supplementary information about the forwarding policy.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p13365250134315"><a name="p13365250134315"></a><a name="p13365250134315"></a>N/A</p>
</td>
</tr>
</tbody>
</table>

7. Click  **OK**.

**Example of URL matching**

The following table shows how a URL is matched, and  [Figure 1](#fig87121434403)  illustrates how a request is forwarded to the backend ECS group.

<a name="table5831113119590"></a><table><tbody><tr id="row889653135910"><td class="cellrowborder" rowspan="2" valign="top"><p id="p9896531165913"><a name="p9896531165913"></a><a name="p9896531165913"></a><strong id="b842352706142041"><a name="b842352706142041"></a><a name="b842352706142041"></a>URL Mapping Rule</strong></p>
</td>
<td class="cellrowborder" rowspan="2" valign="top"><p id="p689673145918"><a name="p689673145918"></a><a name="p689673145918"></a><strong id="b8423527069304"><a name="b8423527069304"></a><a name="b8423527069304"></a>URL</strong></p>
</td>
<td class="cellrowborder" colspan="4" valign="top"><p id="p38961531175918"><a name="p38961531175918"></a><a name="p38961531175918"></a><strong id="b8423527069308"><a name="b8423527069308"></a><a name="b8423527069308"></a>Preset URL</strong></p>
</td>
</tr>
<tr id="row1289643195912"><td class="cellrowborder" valign="top"><p id="p1089663175919"><a name="p1089663175919"></a><a name="p1089663175919"></a>/elb/index.html</p>
</td>
<td class="cellrowborder" valign="top"><p id="p6896113175915"><a name="p6896113175915"></a><a name="p6896113175915"></a>/elb</p>
</td>
<td class="cellrowborder" valign="top"><p id="p1689673113599"><a name="p1689673113599"></a><a name="p1689673113599"></a>/elb[^\s]*</p>
</td>
<td class="cellrowborder" valign="top"><p id="p3896731205919"><a name="p3896731205919"></a><a name="p3896731205919"></a>/index.html</p>
</td>
</tr>
<tr id="row2896103116597"><td class="cellrowborder" valign="top" width="15.933186637327465%"><p id="p1689783116593"><a name="p1689783116593"></a><a name="p1689783116593"></a>Exact match</p>
</td>
<td class="cellrowborder" rowspan="3" valign="top" width="18.81376275255051%"><p id="p118978317599"><a name="p118978317599"></a><a name="p118978317599"></a>/elb/index.html</p>
</td>
<td class="cellrowborder" valign="top" width="16.313262652530504%"><p id="p38975312592"><a name="p38975312592"></a><a name="p38975312592"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="16.313262652530504%"><p id="p17897103116599"><a name="p17897103116599"></a><a name="p17897103116599"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="16.313262652530504%"><p id="p289713114590"><a name="p289713114590"></a><a name="p289713114590"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="16.313262652530504%"><p id="p1189733155917"><a name="p1189733155917"></a><a name="p1189733155917"></a>-</p>
</td>
</tr>
<tr id="row198979312599"><td class="cellrowborder" valign="top"><p id="p7897103195912"><a name="p7897103195912"></a><a name="p7897103195912"></a>Prefix match</p>
</td>
<td class="cellrowborder" valign="top"><p id="p989713315591"><a name="p989713315591"></a><a name="p989713315591"></a>√</p>
</td>
<td class="cellrowborder" valign="top"><p id="p1589763110598"><a name="p1589763110598"></a><a name="p1589763110598"></a>√</p>
</td>
<td class="cellrowborder" valign="top"><p id="p1489753118593"><a name="p1489753118593"></a><a name="p1489753118593"></a>-</p>
</td>
<td class="cellrowborder" valign="top"><p id="p18897183115599"><a name="p18897183115599"></a><a name="p18897183115599"></a>-</p>
</td>
</tr>
<tr id="row18971031195914"><td class="cellrowborder" valign="top"><p id="p13897631125920"><a name="p13897631125920"></a><a name="p13897631125920"></a>Regular expression match</p>
</td>
<td class="cellrowborder" valign="top"><p id="p289715311594"><a name="p289715311594"></a><a name="p289715311594"></a>√</p>
</td>
<td class="cellrowborder" valign="top"><p id="p11897173105916"><a name="p11897173105916"></a><a name="p11897173105916"></a>-</p>
</td>
<td class="cellrowborder" valign="top"><p id="p489714312592"><a name="p489714312592"></a><a name="p489714312592"></a>√</p>
</td>
<td class="cellrowborder" valign="top"><p id="p10897731155915"><a name="p10897731155915"></a><a name="p10897731155915"></a>-</p>
</td>
</tr>
</tbody>
</table>

**Figure  1**  Request forwarding<a name="fig87121434403"></a>
![](figures/request-forwarding.jpg "Request forwarding")

In this figure, the system first searches the request URL \(/elb\_gls/glossary.html\) using the  **Exact match**  rule. If no precisely matched URL is found, the  **Prefix match**  rule is used. If a URL matches the prefix of the request URL, the request is forwarded to backend ECS group 2. Although the request URL also matches rule 3 \(**Regular expression match**\), the request is forwarded to backend ECS group 2 because  **Prefix match**  enjoys higher priority.

## Delete a Forwarding Policy<a name="section4306132117396"></a>

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/en-us_image_0121143837.png)  and select the desired region and project.
3.  Under  **Network**, click  **Elastic Load Balance**.
4.  On the  **Elastic Load Balance**  page, click the name of the target enhanced load balancer.
5.  In the  **Listeners**  area, locate the target listener and click its name to switch to the  **Forwarding Policy**  page. 
6.  Select the forwarding policy to be deleted and click  **Delete**  in the  **Operation**  column.
7.  In the  **Delete Forwarding Policy**  dialog box, click  **OK**  to delete the forwarding policy.

