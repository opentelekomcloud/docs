# Why Do Consumers Need to Acknowledge Messages?<a name="EN-US_TOPIC_0144327167"></a>

Messages need to be acknowledged to ensure the reliability of messages. The reliability in sending and retrieving messages is the result of joint efforts from DMS, message producers, and message consumers. DMS considers a message to be retrieved only after a consumer acknowledges the message \(that is, acknowledges the message retrieval\).

While a message is being retrieved, it remains in the queue. It cannot be retrieved again within 30s since the start of retrieval. If the message is not acknowledged within this period, DMS determines that the message is not successfully retrieved, and the message can be retrieved again.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>Only messages retrieved using APIs need to be acknowledged. Messages retrieved using the DMS console are automatically acknowledged.  

