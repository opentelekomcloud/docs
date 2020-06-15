# How Does DMS Ensure Message Security in a Queue?<a name="EN-US_TOPIC_0144327163"></a>

DMS uses a reliable authentication mechanism to prevent unauthorized access to messages to ensure queue security.

DMS queues:

-   Before you manage messages on the DMS console, you must complete your identity authentication. 
-   If you use APIs to send and retrieve messages, you must obtain a token, and add the obtained token to the API request header. In addition, the API request must be signed using the access key ID/secret access key \(AK/SK pair\), so that this API request can be sent through the API gateway. For details on how to obtain a token and AK/SK, see the  _Distributed Message Service API Reference_.

Kafka premium instances:

-   For intra-VPC access, the client and the server must be in the same VPC and have been configured with correct security group rules. You can enable SASL authentication to encrypt data before transmission for higher security.
-   For public access, enable SASL authentication.

