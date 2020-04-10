# Mappings Between SMN Operations and APIs<a name="smn_ug_a6000"></a>

**Table  1**  Mappings between SMN operations and APIs

<a name="table40610457155253"></a>
<table><thead align="left"><tr id="row7466420155253"><th class="cellrowborder" valign="top" width="25.82%" id="mcps1.2.4.1.1"><p id="p7202482155253"><a name="p7202482155253"></a><a name="p7202482155253"></a>Operation</p>
</th>
<th class="cellrowborder" valign="top" width="27.13%" id="mcps1.2.4.1.2"><p id="p46530145155253"><a name="p46530145155253"></a><a name="p46530145155253"></a>API</p>
</th>
<th class="cellrowborder" valign="top" width="47.05%" id="mcps1.2.4.1.3"><p id="p10845389155253"><a name="p10845389155253"></a><a name="p10845389155253"></a>Function</p>
</th>
</tr>
</thead>
<tbody><tr id="row30499637155253"><td class="cellrowborder" valign="top" width="25.82%" headers="mcps1.2.4.1.1 "><p id="p4199904616713"><a name="p4199904616713"></a><a name="p4199904616713"></a>SMN:UpdateTopic</p>
</td>
<td class="cellrowborder" valign="top" width="27.13%" headers="mcps1.2.4.1.2 "><p id="p56594888155253"><a name="p56594888155253"></a><a name="p56594888155253"></a>UpdateTopic</p>
</td>
<td class="cellrowborder" valign="top" width="47.05%" headers="mcps1.2.4.1.3 "><p id="p30182576161234"><a name="p30182576161234"></a><a name="p30182576161234"></a>Modify the topic. Currently, only the <strong id="b842352706192856"><a name="b842352706192856"></a><a name="b842352706192856"></a>display_name</strong> field value can be changed.</p>
</td>
</tr>
<tr id="row52831096155253"><td class="cellrowborder" valign="top" width="25.82%" headers="mcps1.2.4.1.1 "><p id="p253506116713"><a name="p253506116713"></a><a name="p253506116713"></a>SMN:DeleteTopic</p>
</td>
<td class="cellrowborder" valign="top" width="27.13%" headers="mcps1.2.4.1.2 "><p id="p7542409155253"><a name="p7542409155253"></a><a name="p7542409155253"></a>DeleteTopic</p>
</td>
<td class="cellrowborder" valign="top" width="47.05%" headers="mcps1.2.4.1.3 "><p id="p1549416916138"><a name="p1549416916138"></a><a name="p1549416916138"></a>Delete a topic and its subscribers. If a topic is deleted, any pending messages may fail to send to the topic subscribers.</p>
</td>
</tr>
<tr id="row62598497155253"><td class="cellrowborder" valign="top" width="25.82%" headers="mcps1.2.4.1.1 "><p id="p1429388816713"><a name="p1429388816713"></a><a name="p1429388816713"></a>SMN:QueryTopicDetail</p>
</td>
<td class="cellrowborder" valign="top" width="27.13%" headers="mcps1.2.4.1.2 "><p id="p2493507155253"><a name="p2493507155253"></a><a name="p2493507155253"></a>QueryTopicDetail</p>
</td>
<td class="cellrowborder" valign="top" width="47.05%" headers="mcps1.2.4.1.3 "><p id="p51055184161330"><a name="p51055184161330"></a><a name="p51055184161330"></a>Query details about a topic.</p>
</td>
</tr>
<tr id="row5827766155253"><td class="cellrowborder" valign="top" width="25.82%" headers="mcps1.2.4.1.1 "><p id="p3763483316713"><a name="p3763483316713"></a><a name="p3763483316713"></a>SMN:ListTopicAttributes</p>
</td>
<td class="cellrowborder" valign="top" width="27.13%" headers="mcps1.2.4.1.2 "><p id="p51030558155253"><a name="p51030558155253"></a><a name="p51030558155253"></a>ListTopicAttributes</p>
</td>
<td class="cellrowborder" valign="top" width="47.05%" headers="mcps1.2.4.1.3 "><p id="p61745869161340"><a name="p61745869161340"></a><a name="p61745869161340"></a>Query the list of topic attributes.</p>
</td>
</tr>
<tr id="row22966150155253"><td class="cellrowborder" valign="top" width="25.82%" headers="mcps1.2.4.1.1 "><p id="p4588028416713"><a name="p4588028416713"></a><a name="p4588028416713"></a>SMN:UpdateTopicAttribute</p>
</td>
<td class="cellrowborder" valign="top" width="27.13%" headers="mcps1.2.4.1.2 "><p id="p21511815155253"><a name="p21511815155253"></a><a name="p21511815155253"></a>UpdateTopicAttribute</p>
</td>
<td class="cellrowborder" valign="top" width="47.05%" headers="mcps1.2.4.1.3 "><p id="p14685560161438"><a name="p14685560161438"></a><a name="p14685560161438"></a>Modify topic attributes.</p>
</td>
</tr>
<tr id="row45748200155253"><td class="cellrowborder" valign="top" width="25.82%" headers="mcps1.2.4.1.1 "><p id="p3861765816713"><a name="p3861765816713"></a><a name="p3861765816713"></a>SMN:DeleteTopicAttributes</p>
</td>
<td class="cellrowborder" valign="top" width="27.13%" headers="mcps1.2.4.1.2 "><p id="p43102455155253"><a name="p43102455155253"></a><a name="p43102455155253"></a>DeleteTopicAttributes</p>
</td>
<td class="cellrowborder" valign="top" width="47.05%" headers="mcps1.2.4.1.3 "><p id="p1637937155253"><a name="p1637937155253"></a><a name="p1637937155253"></a>Delete all topic attributes.</p>
</td>
</tr>
<tr id="row14741435155253"><td class="cellrowborder" valign="top" width="25.82%" headers="mcps1.2.4.1.1 "><p id="p3831067116713"><a name="p3831067116713"></a><a name="p3831067116713"></a>SMN:DeleteTopicAttributeByName</p>
</td>
<td class="cellrowborder" valign="top" width="27.13%" headers="mcps1.2.4.1.2 "><p id="p14685611155253"><a name="p14685611155253"></a><a name="p14685611155253"></a>DeleteTopicAttributeByName</p>
</td>
<td class="cellrowborder" valign="top" width="47.05%" headers="mcps1.2.4.1.3 "><p id="p20696347161512"><a name="p20696347161512"></a><a name="p20696347161512"></a>Delete a specified topic attribute.</p>
</td>
</tr>
<tr id="row3257009916547"><td class="cellrowborder" valign="top" width="25.82%" headers="mcps1.2.4.1.1 "><p id="p6285939916713"><a name="p6285939916713"></a><a name="p6285939916713"></a>SMN:ListSubscriptionsByTopic</p>
</td>
<td class="cellrowborder" valign="top" width="27.13%" headers="mcps1.2.4.1.2 "><p id="p1779667816547"><a name="p1779667816547"></a><a name="p1779667816547"></a>ListSubscriptionsByTopic</p>
</td>
<td class="cellrowborder" valign="top" width="47.05%" headers="mcps1.2.4.1.3 "><p id="p48133186161538"><a name="p48133186161538"></a><a name="p48133186161538"></a>Query the subscription list of a specified topic by page. The list is sorted by time when the subscriptions are added in ascending order. You can specify values of <strong id="b842352706142447"><a name="b842352706142447"></a><a name="b842352706142447"></a>offset</strong> and <strong id="b842352706142454"><a name="b842352706142454"></a><a name="b842352706142454"></a>limit</strong>. If no subscription has been added, an empty list is returned.</p>
</td>
</tr>
<tr id="row6424497716551"><td class="cellrowborder" valign="top" width="25.82%" headers="mcps1.2.4.1.1 "><p id="p6625710816713"><a name="p6625710816713"></a><a name="p6625710816713"></a>SMN:Subscribe</p>
</td>
<td class="cellrowborder" valign="top" width="27.13%" headers="mcps1.2.4.1.2 "><p id="p52424616551"><a name="p52424616551"></a><a name="p52424616551"></a>Subscribe</p>
</td>
<td class="cellrowborder" valign="top" width="47.05%" headers="mcps1.2.4.1.3 "><p id="p61570312161554"><a name="p61570312161554"></a><a name="p61570312161554"></a>Add a subscription to a specified topic and send a confirmation message to the subscriber. After confirming the subscription, the subscriber can receive notification messages published to the topic.</p>
</td>
</tr>
<tr id="row1552135216559"><td class="cellrowborder" valign="top" width="25.82%" headers="mcps1.2.4.1.1 "><p id="p184048016713"><a name="p184048016713"></a><a name="p184048016713"></a>SMN:Unsubscribe</p>
</td>
<td class="cellrowborder" valign="top" width="27.13%" headers="mcps1.2.4.1.2 "><p id="p3144820416559"><a name="p3144820416559"></a><a name="p3144820416559"></a>Unsubscribe</p>
</td>
<td class="cellrowborder" valign="top" width="47.05%" headers="mcps1.2.4.1.3 "><p id="p41500538161616"><a name="p41500538161616"></a><a name="p41500538161616"></a>Delete a subscription. This operation requires identity authentication. Only the subscriber or the topic owner can delete a subscription.</p>
</td>
</tr>
<tr id="row501468261662"><td class="cellrowborder" valign="top" width="25.82%" headers="mcps1.2.4.1.1 "><p id="p2425111816713"><a name="p2425111816713"></a><a name="p2425111816713"></a>SMN:Publish</p>
</td>
<td class="cellrowborder" valign="top" width="27.13%" headers="mcps1.2.4.1.2 "><p id="p456766331662"><a name="p456766331662"></a><a name="p456766331662"></a>Publish</p>
</td>
<td class="cellrowborder" valign="top" width="47.05%" headers="mcps1.2.4.1.3 "><p id="p88198101662"><a name="p88198101662"></a><a name="p88198101662"></a>Publish messages to a topic. After a message ID is returned, the message has been saved and is to be delivered to subscribers of the topic. The message form varies depending on the protocol of each subscription.</p>
</td>
</tr>
</tbody>
</table>

