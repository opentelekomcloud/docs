# What Is the Maximum Size of a Message?<a name="EN-US_TOPIC_0144327161"></a>

The size of each message, including the message body and attributes, cannot exceed 512 KB.

On the DMS console, only one message can be sent at a time. The  **Message Body**  input box displays the remaining number of bytes allowed in a message as you are creating the message. If the message size exceeds 512 KB, you cannot click  **OK**  to create the message.

Multiple messages can be sent at a time through APIs, but the aggregated message size cannot exceed 512 KB. If the aggregated message size exceeds 512 KB, messages fail to be created and the API caller receives the error message "The message size is \{message size\}, larger than the size limit \{max allowed size\}".

If a Kafka SDK API is used to create messages in a Kafka queue, the maximum size of a single message is 10 MB. If the DMS console is used to create messages in a Kafka queue, the maximum size of a single message is 512 KB.

If messages are created in a topic of a Kafka premium instance, the maximum size of a single message is 10 MB.

