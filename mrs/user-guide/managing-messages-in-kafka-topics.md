# Managing Messages in Kafka Topics<a name="EN-US_TOPIC_0125375527"></a>

## Scenario<a name="sbbd9f80b60f54249af96f7cab5d397d1"></a>

Users can produce or consume messages in Kafka topics using the MRS cluster client. For clusters with Kerberos authentication enabled, the user must have the permission to perform these operations.

## Prerequisites<a name="sb30cd6d5ec904393ad5f0bbd9f93d829"></a>

The client has been updated.

## Procedure<a name="s14181899c3ca436bb0b5b5f1221e7dd2"></a>

1.  On MRS Manager, choose  **Service**  \>  **Kafka**  \>  **Instance**. Query the IP addresses of the Kafka instances.

    Record the IP address of any Kafka instance.

2.  Log in to the node where the client is installed.

    For example, if you have updated the client on the Master2 node, log in to the Master2 node to use the client. For details, see  [Client Management](client-management.md).

3.  Run the following command to switch the user:

    **sudo su - omm**

4.  Run the following command to switch to the client directory, for example,  **/opt/client/Kafka/kafka/bin**.

    **cd /opt/client/Kafka/kafka/bin**

5.  Run the following command to configure the environment variables:

    **source /opt/client/bigdata\_env**

6.  If Kerberos authentication is enabled, run the following command to authenticate the user. If Kerberos authentication is disabled, skip this step.

    **kinit** _**Kafka username**_

    For example,  **kinit admin**

7.  Manage messages in Kafka topics using the following commands:

    -   Produce messages.

        **sh kafka-console-producer.sh --broker-list** _**IP address of the node where the Kafka instance is located**_**:21005 --topic** _**Topic name**_ **--producer.config /opt/client/Kafka/kafka/config/producer.properties**

        You can input specified information as the messages produced by the producer and then press  **Enter** to send the messages. To end message producing, press **Ctrl + C**  to exit.

    -   Consume messages.

        **sh kafka-console-consumer.sh --topic** _**Topic name**_ **--bootstrap-server** _**IP address of the node where the Kafka instance is located**_**:21005 --new-consumer --consumer.config /opt/client/Kafka/kafka/config/consumer.properties**

        In the configuration file,  **group.id** \(indicating the consumer group\) is set to **example-group1**  by default. Users can change the value as required. The value takes effect each time a consumption occurs.

        By default, the system reads unprocessed messages in the current consumer group when the command is executed. If a new consumer group is specified in the configuration file and the  **--from-beginning**  parameter is added to the command, the system reads all messages that have not been automatically deleted in Kafka.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   For the IP address of the node where the Kafka instance is located, use the IP address of any Broker instance.  
    >-   If Kerberos authentication is enabled, change the port to  **21007**.  


