## Getting Started

This section explains basic SMN terms and helps you quickly configure your SMN service.

A topic is a collection of messages and serves as a basic unit for isolating messages. Each topic may have subscribers of multiple types, including email, SMS, HTTP, and HTTPS. You can publish messages to the topic in three formats: text, JSON, or template.

Actually, messages you published in text, JSON, or template format can be delivered to subscribers of all types, including email, SMS, HTTP, and HTTPS. The message an email or HTTP/HTTPS subscriber receives contains the message subject, content, and unsubscription link. The message an SMS subscriber receives contains only the message content.

- **Text**: common text message

	The text message you published to a topic does not refer to an SMS message in this context. It might be delivered to all types of subscribers, including SMS, email, HTTP, and HTTPS. For details about sending a text message, see section <a href="Publishing a Text Message">Publishing a Text Message</a>.

- **JSON**: JSON-structured message

	You can specify message protocols and different message content for each protocol. For details about sending a JSON message, see section <a href="Publishing a JSON Message">Publishing a JSON Message</a>.

- **Template**: customized message template, in which you can replace the tags (the placeholders) with specified message content

	When publishing messages using a template, you need to select a template by name and specify content for each tag. SMN will replace the tags with the content you have entered. If you do not enter specific content for a tag, the system will treat the tag as empty when it sends the message. For details about sending messages using a template, see section <a href="Publishing Messages Using a Template">Publishing Messages Using a Template</a>.

To publish messages to a topic authorized to you by other users, see section <a href="Sending Messages to an Authorized Topic">Sending Messages to an Authorized Topic</a>.
