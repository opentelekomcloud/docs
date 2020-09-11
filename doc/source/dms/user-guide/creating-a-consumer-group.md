# Creating a Consumer Group<a name="EN-US_TOPIC_0143117234"></a>

## Scenario<a name="section42353227"></a>

A consumer group must be created in order to retrieve messages. A maximum of three consumer groups can be created in each queue.

Messages in a queue are retrievable to all consumer groups created in that queue.

## Prerequisites<a name="section45634724"></a>

A queue has been created.

## Procedure<a name="section8059334"></a>

1.  Log in to the management console.
2.  Click  ![](figures/project.png)  in the upper left corner to select a region and a project.
3.  Click  **Service List**, and choose  **Application**  \>  **Distributed Message Service**  to open the DMS console.
4.  In the navigation pane, choose  **Queue Manager**.
5.  Open the  **Create Consumer Group**  dialog box using either of the methods:
    -   Method 1

        In the queue list, choose  **More**  \>  **Create Consumer Group**  in the same row as the queue for which you want to create a consumer group.

    -   Method 2
        1.  Click the name of a queue for which you want to create a consumer group.
        2.  On the queue details page, click the  **Consumer Groups**  tab.
        3.  Click  **Create Consumer Group**.

6.  Specify  **Consumer Group Name**.

    A default consumer group name is generated, which you can change if required. A consumer group name is 1 to 32 characters long. Only letters, digits, underscores \(\_\), and hyphens \(-\) are allowed. Consumer group names must be unique within their queue.

7.  Click  **OK**.

