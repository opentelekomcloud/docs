## Publishing Messages to a Topic


This section describes how to use SMN to publish messages in three different formats: text, JSON, and template.

After you publish a message to a topic, SMN will send the message to all confirmed subscription endpoints in the topic.

If an SMS message is oversized, the system divides it into multiple parts when sending it to subscribers. However, you must note that SMN only sends the first two parts of the SMS message. Any additional parts will not be sent. You are charged based on the actual number of messages sent.

In addition, you must ensure that the firewall policies of the HTTP or HTTPS endpoints allow SMN to send messages from the Internet. An SMN HTTP or HTTPS message consists of a message header and body. For details, see section <a href="HTTP/HTTPS Message Format">HTTP/HTTPS Message Format</a>.