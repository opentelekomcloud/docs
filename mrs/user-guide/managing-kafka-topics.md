# Managing Kafka Topics<a name="EN-US_TOPIC_0125376118"></a>

## Scenario<a name="s7fa227cd6cac4a74ae25352ad5c13f11"></a>

Users can manage Kafka topics on the MRS cluster client to meet service requirements. For clusters with Kerberos authentication enabled, the management permission is required.

## Prerequisites<a name="s4e15ca2c56ec4999a284f0d4f07ac0da"></a>

The client has been updated.

## Procedure<a name="sf92ea9c82ebe492ab9bc74d45c4a858a"></a>

1.  On MRS Manager, choose  **Service**  \>  **ZooKeeper**  \>  **Instance**. Query the IP addresses of the ZooKeeper instances.

    Record the IP address of any ZooKeeper instance.

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

7.  Manage Kafka topics using the following commands:

    -   Create a topic.

        **sh kafka-topics.sh --create --topic  _Topic name_  --partitions** _**Number of partitions used by the topic**_ **--replication-factor** _**Number of replicas of the topic**_ **--zookeeper** _**IP address of the node where the ZooKeeper instance is located:clientPort**_**/kafka**

    -   Delete a topic.

        **sh kafka-topics.sh --delete --topic** _**Topic name**_ **--zookeeper** _**IP address of the node where the ZooKeeper instance is located**_**:**_**clientPort**_**/kafka**

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   The number of topic partitions or topic backups cannot exceed the number of Kafka instances.  
    >-   By default,  **clientPort** of ZooKeeper is **24002**.  
    >-   There are three ZooKeeper instances. Use the IP address of any one.  
    >-   For details about managing messages in Kafka topics, see  [Managing Messages in Kafka Topics](managing-messages-in-kafka-topics.md).  


