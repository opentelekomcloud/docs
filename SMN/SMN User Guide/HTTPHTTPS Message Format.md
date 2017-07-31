

## HTTP/HTTPS Message Format

### Scenarios

This section describes the format of messages sent to the HTTP or HTTPS endpoint. You can identify a message based on its message type. An HTTP/HTTPS message contains HTTP/HTTPS header and content. The HTTP/HTTPS content contains JSON character strings.

### HTTP/HTTPS Message Header Information

The message header of an SMN HTTP/HTTPS contains the following parameters: **X-SMN-TOPIC-URN**, **X-SMN-MESSAGE-ID**, **X-SMN-MESSAGE-TYPE**, and **X-SMN-SUBSCRIPTION-URN**.

**Table 1** HTTP/HTTPS header parameter description

<table>
<tr>
<th>Parameter</th>
<th>Description</th>
</tr>
<tr>
<td> X-SMN-MESSAGE-TYPE </td>
<td>Indicates the message type, which can be:                   
                                                                                        
<ul><li>SubscriptionConfirmation</li>                                  
                                                                                        
<li>Notification</li>                                                                                                                                
<li>UnsubscribeConfirmation</li></ul> </td>
</tr>
<tr>
<td> X-SMN-MESSAGE-ID</td>
<td>Indicates the unique message ID. </td>
</tr>
<tr>
<td>X-SMN-TOPIC-URN</td>
<td>Indicates the URN of the topic to which the message belongs. </td>
</tr>
<tr>
<td>X-SMN-SUBSCRIPTION-URN</td>
<td>Identifies the subscription endpoint.</td>
</tr>
</table> 

### Format of HTTP/HTTPS Subscription Confirmation Messages

After you add an HTTP/HTTPS endpoint, SMN sends a subscription confirmation message to the subscriber. The content of the subscription confirmation message contains JSON character strings. The subscriber needs to obtain the subscription URL (**subscribe_url**) to confirm the subscription. <a href="#table2">Table 2 </a>describes the JSON strings in detail.

<a name="table2">**Table 2** Content of an HTTP/HTTPS subscription confirmation message</a>
<table>
<tr>
<th>Parameter</th>
<th>Description</th>
</tr>
<tr>
<td> type   </td>
<td>Indicates the message type, the value of which is <b>SubscriptionConfirmation</b>.
</tr>
<tr>
<td>subscribe_url </td>
<td>Indicates the URL to be accessed for subscription confirmation.  </td>
</tr>
<tr>
<td> topic_urn </td>
<td>Indicates the URN of the topic to which the message belongs.  </td>
</tr>
<tr>
<td>message_id </td>
<td> Indicates the unique message ID.</td>
</tr>
<tr>
<td> message </td>
<td> Indicates the message content.</td>
</tr>
<tr>
<td> signature</td>
<td> <p>Indicates the signature information.</p> 
<p>The signature includes the <b>message</b>, <b>message_id</b>, <b>subscribe_url</b>,<b>timestamp</b>, <b>topic_urn</b>, and <b>type</b> fields. For details about signature check, see <a href="Message Signature Verification.md">Message Signature Verification</a>. </p></td>
</tr>
<tr>
<td> signature_version</td>
<td> Indicates the signature version, which is <b>V1</b> currently. </td>
</tr>
<tr>
<td> signing_cert_url</td>
<td> Indicates the certificate URL for the message signature check. </td>
</tr>
<tr>
<td> timestamp</td>
<td> Indicates the time stamp of the first message sending. </td>
</tr>
</table> 

### Format of HTTP/HTTPS Notification Messages

After the HTTP/HTTPS subscriber confirms the subscription, the subscriber can receive notification messages published to the topic. The HTTP/HTTPS content of the notification message contains JSON character strings, which are described in <a href="#table3">Table 3</a>.

<a name="table3">**Table 3** Content of an HTTP/HTTPS notification message</a>

<table>
<tr>
<th>Parameter</th>
<th>Description</th>
</tr>
<tr>
<td> type   </td>
<td>Indicates the message type, the value of which is <b>SubscriptionConfirmation</b>.
</tr>
<tr>
<td>topic_urn  </td>
<td>Indicates the URN of the topic to which the message belongs.   </td>
</tr>

<tr>
<td>message_id </td>
<td> Indicates the unique message ID.</td>
</tr>
<tr>
<td> message </td>
<td> Indicates the message content.</td>
</tr>
<tr>
<td>  unsubscribe_url </td>
<td>Indicates the URL for canceling a subscription. </td>
</tr>
<tr>
<td> signature</td>
<td> <p>Indicates the signature information.</p> 
<p>The signature includes the <b>message</b>, <b>message_id</b>, <b>subject</b>,<b>timestamp</b>, <b>topic_urn</b>, and <b>type</b> fields. If the value of the <b>subject</b> field is empty, the signature is not checked.For details about signature check, see <i>Message Signature Verification</i>. </p></td>
</tr>
<tr>
<td> signature_version</td>
<td> Indicates the signature version, which is <b>V1</b> currently. </td>
</tr>
<tr>
<td> signing_cert_url</td>
<td> Indicates the certificate URL for the message signature check. </td>
</tr>
<tr>
<td> timestamp</td>
<td> Indicates the time stamp of the first message sending. </td>
</tr>
</table> 

### Format of HTTP/HTTPS Unsubscription Confirmation Messages

After an HTTP/HTTPS subscription is canceled, the subscriber receives an unsubscription confirmation message sent by SMN. The content of the unsubscription confirmation message contains JSON character strings, which are described in <a href="#table4">Table 4</a>.

<a name="table4">**Table 4** Content of an HTTP/HTTPS unsubscription confirmation message</a>


<table>
<tr>
<th>Parameter</th>
<th>Description</th>
</tr>
<tr>
<td> type   </td>
<td>Indicates the message type, the value of which is <b>UnsubscribeConfirmation</b>.
</tr>
<tr>
<td>subscribe_url </td>
<td>Indicates the URL to be accessed for subscription confirmation.  </td>
</tr>
<tr>
<td> topic_urn </td>
<td>Indicates the URN of the topic to which the message belongs.  </td>
</tr>
<tr>
<td>message_id </td>
<td> Indicates the unique message ID.</td>
</tr>
<tr>
<td> message </td>
<td> Indicates the message content.</td>
</tr>
<tr>
<td> signature</td>
<td> <p>Indicates the signature information.</p> 
<p>The signature includes the <b>message</b>, <b>message_id</b>, <b>subscribe_url</b>,<b>timestamp</b>, <b>topic_urn</b>, and <b>type</b> fields. For details about signature check, see <a href="Message Signature Verification.md">Message Signature Verification</a>. </p></td>
</tr>
<tr>
<td> signature_version</td>
<td> Indicates the signature version, which is <b>V1</b> currently. </td>
</tr>
<tr>
<td> signing_cert_url</td>
<td> Indicates the certificate URL for the message signature check. </td>
</tr>
<tr>
<td> timestamp</td>
<td> Indicates the time stamp of the first message sending. </td>
</tr>
</table> 

