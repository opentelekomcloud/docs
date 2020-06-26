# Does DMS Support FIFO Delivery?<a name="EN-US_TOPIC_0144327158"></a>

Yes. When creating a queue, you can select  **Standard**  and then  **FIFO**. In a FIFO queue, messages are retrieved in the order they were sent. FIFO queues are useful in scenarios where the order of messages is important. In a standard queue, messages may be retrieved out of sequence. Standard queues are useful in scenarios where high concurrence is important.

