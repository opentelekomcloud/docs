## Mappings Between SMN Operations and APIs


<span id="_table40610457155253" class="anchor"></span>**Table A-1** Mappings between SMN operations and APIs

<table>
<tr>
<th>Operation</th>
<th>API</th> 
<th>Function</th>
</tr>
<tr>
<td>SMN:UpdateTopic </td>
<td>UpdateTopic</td>
 <td>Modify the topic attribute. Currently, only the <b>display_name</b> field value can be modified.  </td>
</tr>
<tr>
<td>SMN:DeleteTopic</td>
<td>DeleteTopic</td>
 <td>Delete a topic and its subscribers. If a topic is deleted, a pending message may fail to send to the topic subscribers.</td>
</tr>
<tr>
<td>SMN:QueryTopicDetail </td>
<td>QueryTopicDetail</td>
 <td>Query detailed information about a topic.</td>
</tr>
<tr>
<td>SMN:ListTopicAttributes </td>
<td>ListTopicAttributes</td>
 <td>Query the topic attribute information.</td>
</tr>
<tr>
<td> SMN:UpdateTopicAttribute </td>
<td>UpdateTopicAttribute</td>
 <td>Modify the topic attributes. </td>
</tr>
<tr>
<td>SMN:DeleteTopicAttributes </td>
<td>DeleteTopicAttributes</td>
 <td>Delete all topic attributes. </td>
</tr>
<tr>
<td>SMN:DeleteTopicAttributeByName </td>
<td>DeleteTopicAttributeByName</td>
 <td>Delete a specified topic attribute.</td>
</tr>
<tr>
<td>SMN:ListSubscriptionsByTopic </td>
<td>ListSubscriptionsByTopic </td>
 <td>Query the subscription list of a specified topic by page. The list is sorted by the subscription creation time in ascending order. You can specify the values of <b>offset</b> and <b>limit</b>. If no subscription has been added, an empty list is returned.</td>
</tr>
<tr>
<td>SMN:Subscribe </td>
<td>Subscribe  </td>
 <td>Add a subscription to a specified topic and send a confirmation message to the subscriber. After confirming the subscription, the subscriber can receive notification messages published to the topic. </td>
</tr>
<tr>
<td>SMN:Unsubscribe </td>
<td>Unsubscribe   </td>
 <td> Delete a subscription. Subscription deletion requires identity authentication. Only the subscriber or the topic owner can delete a subscription.  </td>
</tr>
<tr>
<td>SMN:Publish </td>
<td>Publish    </td>
 <td>Publish messages to a topic. After the message ID is returned, the message has been saved and is to be pushed to the subscribers of the topic. The message format varies depending on the protocol of a subscription.        </td>
</tr>
</table> 
