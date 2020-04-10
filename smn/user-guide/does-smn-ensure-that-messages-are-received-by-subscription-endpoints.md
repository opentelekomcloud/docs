# Does SMN Ensure That Messages Are Received by Subscription Endpoints?<a name="smn_faq_0014"></a>

If a subscription endpoint is reachable, it will receive all messages delivered by SMN.

If an endpoint is unreachable, SMN saves the failed message in a message queue and tries to send it six more times. If the message still fails to send, SMN discards it and does not inform the publisher that the message delivery has failed.

The interval for re-sending a failed message varies depending on the length of the message queue. Usually, a failed message is processed within several hours. If the queue has too many failed messages, it will be processed within a day.

