# Deleting a Consumer Group<a name="EN-US_TOPIC_0143117215"></a>

## Scenario<a name="section10185684"></a>

Deleting a consumer group does not impact normal messages in a queue. Normal messages still exist in the queue and can still be retrieved by other consumer groups.

Dead letter messages are specific to consumer groups. If a consumer group is deleted, the dead letter messages of the consumer group are also deleted, regardless of whether they have been retrieved. Deleted dead letter messages can no longer be retrieved.

## Prerequisites<a name="section24562296"></a>

A consumer group has been created.

## Procedure<a name="section19734077"></a>

1.  Log in to the management console.
2.  Click  ![](figures/project.png)  in the upper left corner to select a region and a project.
3.  Click  **Service List**, and choose  **Application**  \>  **Distributed Message Service**  to open the DMS console.
4.  In the navigation pane, choose  **Queue Manager**.
5.  Click the name of a queue for which you want to delete a consumer group.
6.  Choose  **Delete Consumer Group**  in the same row as the consumer group you want to delete.
7.  Click  **OK**.

