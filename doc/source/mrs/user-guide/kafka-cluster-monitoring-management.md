# Kafka Cluster Monitoring Management<a name="EN-US_TOPIC_0221415082"></a>

The Kafka cluster monitoring management includes the following:

-   [Viewing Broker Information](#section1254019150558)
-   [Viewing Topic Information](#section2384151125912)
-   [Viewing Consumers Information](#section517576022)
-   [Modifying the Partition of a Topic Through KafkaManager](#section195268241735)

## Viewing Broker Information<a name="section1254019150558"></a>

1.  Log in to the KafkaManager web UI.
2.  On the cluster list page, click a cluster name to access the Summary page of the cluster.

    **Figure  1**  Summary page of the cluster<a name="fig51082016253"></a>  
    ![](figures/summary-page-of-the-cluster.png "summary-page-of-the-cluster")

3.  Click  **Brokers**  to access the Broker monitoring page. The page displays the Broker list and I/O statistics of the Broker nodes.

    **Figure  2**  Broker monitoring page<a name="fig4283026133010"></a>  
    ![](figures/broker-monitoring-page.png "broker-monitoring-page")


## Viewing Topic Information<a name="section2384151125912"></a>

1.  Log in to the KafkaManager web UI.
2.  On the cluster list page, click a cluster name to access the Summary page of the cluster.
3.  Choose  **Topic**  \>  **List**  to view the topic list of the current cluster and information about each topic.

    **Figure  3**  Topic list<a name="fig820314249365"></a>  
    ![](figures/topic-list.png "topic-list")

4.  Click a topic name to view details about the topic.

    **Figure  4**  Topic details<a name="fig597644733810"></a>  
    ![](figures/topic-details.png "topic-details")


## Viewing Consumers Information<a name="section517576022"></a>

1.  Log in to the KafkaManager web UI.
2.  On the cluster list page, click a cluster name to access the Summary page of the cluster.
3.  Click  **Consumers**  to view the consumer list of the current cluster and each consumer's consumption information.

    **Figure  5**  Consumer list<a name="fig1875394394113"></a>  
    ![](figures/consumer-list.png "consumer-list")

4.  Click a consumer name to view the list of the consumed topics.

    **Figure  6**  List of topics consumed by the consumer<a name="fig197791150114411"></a>  
    ![](figures/list-of-topics-consumed-by-the-consumer.png "list-of-topics-consumed-by-the-consumer")

5.  Click a topic name in the topic list of the consumer to view consumption information about the topic.

    **Figure  7**  Topic consumption details<a name="fig10399118144810"></a>  
    ![](figures/topic-consumption-details.png "topic-consumption-details")


## Modifying the Partition of a Topic Through KafkaManager<a name="section195268241735"></a>

1.  Log in to the KafkaManager web UI.
2.  On the cluster list page, click a cluster name to access the Summary page of the cluster.
3.  Choose  **Topic**  \>  **List**  to access the topic list page of the current cluster.
4.  Click a topic name to access the  **Topic Summary**  page.
5.  Click  **Add Partitions**. The page for adding partitions is displayed.

    **Figure  8**  Adding partitions<a name="fig122581408519"></a>  
    ![](figures/adding-partitions.png "adding-partitions")

6.  Confirm the topic name and modify the value of the  **Partitions**  parameter and click  **Add Partitions**  to add partitions.

    **Figure  9**  Modifying the number of partitions<a name="fig15559240162512"></a>  
    ![](figures/modifying-the-number-of-partitions.png "modifying-the-number-of-partitions")

7.  After the partitions are added successfully, click  **Go to topic view**  to return to the  **Topic Summary**  page.
8.  Check the number of partitions in  **Partition Information**  in the lower part of the  **Topic Summary**  page.

    **Figure  10**  Partition information<a name="fig191755129282"></a>  
    ![](figures/partition-information.png "partition-information")

9.  \(Optional\) If you are not satisfied with the assigned partitions, you can use the partition reassignment function to automatically reassign partitions.
    1.  On the  **Topic Summary**  page, click  **Generate Partition Assignments**.
    2.  Select the broker instance and click  **Generate Partition Assignments**  to generate a partition.
    3.  After partition generation, click  **Go to topic view**  to return to the  **Topic Summary**  page.
    4.  On the  **Topic Summary**  page, click  **Reassign Partitions**  to automatically assign partitions to the broker instance of the cluster.
    5.  Click  **Go to reassign partitions**  to view details about the reassigned partitions.

10. \(Optional\) If you are not satisfied with the automatically assigned partitions, you can manually assign the partitions.
    1.  On the  **Topic Summary**  page, click  **Manual Partition Assignments**  to access the page for manually assign partitions.
    2.  Manually assign a broker ID to each partition replica, and click  **Save Partition Assignment**  to save the changes.
    3.  Click  **Go to topic view**  to return to the  **Topic Summary**  page and view the partition details.


