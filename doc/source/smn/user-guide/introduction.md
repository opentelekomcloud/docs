# Introduction<a name="en-us_topic_0044170758"></a>

SMN enables you to publish messages in the following formats:

-   Text
-   JSON
-   Template

After you publish a message to a topic, SMN will deliver the message to all confirmed subscription endpoints in the topic.

For SMS endpoints, if an SMS message is oversized, the system divides it into multiple parts when sending it to subscribers. However, you must note that SMN only sends the first two parts of the SMS message and does not send any additional parts. You are charged based on the actual number of messages sent to the subscribers.

You must ensure that firewall policies of the HTTP or HTTPS endpoints allow SMN to send messages from the Internet. An SMN HTTP or HTTPS message consists of a message header and body. For details, see  [HTTP/HTTPS Message Format](http-https-message-format.md).

