# Viewing Metrics<a name="EN-US_TOPIC_0143117221"></a>

## Scenario<a name="section2938669717629"></a>

Cloud Eye monitors DMS metrics in real time. You can view these DMS metrics on the Cloud Eye console.

## Prerequisites<a name="section2862447517827"></a>

-   At least one queue has been created. The queue has at least one consumer group and at least one available message.
-   At least one Kafka premium instance has been created. The instance has at least one available message.

## Procedure<a name="section4474291117942"></a>

1.  Log in to the management console.
2.  Click  ![](figures/project.png)  in the upper left corner to select a region and a project.
3.  Click  **Service List**, and choose  **Application**  \>  **Distributed Message Service**  to open the DMS console.
4.  Perform the following steps to view the metrics.
    -   To view the metrics of a standard queue or a non-premium Kafka queue:
        1.  In the navigation pane, choose  **Queue Manager**.
        2.  In the same row as the queue for which you want to view the metrics, choose  **More**  \>  **View Metric**.

            On the Cloud Eye console, view the queue metrics. Metric data is reported to Cloud Eye every minute.

    -   To view the metrics of a consumer group:
        1.  In the navigation pane, choose  **Queue Manager**.
        2.  Click the name of a queue for which you want to view the metrics.
        3.  In the same row as the consumer group for which you want to view the metrics, choose  **More**  \>  **View Metric**.

            On the Cloud Eye console, view the consumer group metrics. Metric data is reported to Cloud Eye every minute.

    -   To view metrics of a Kafka premium instance:
        1.  In the navigation pane, choose  **Kafka Premium**.
        2.  In the same row as the instance for which you want to view the metrics, choose  **More**  \>  **View Metric**.

            On the Cloud Eye console, view the metrics of the instance, brokers, topics, and consumer groups. Metric data is reported to Cloud Eye every minute.




