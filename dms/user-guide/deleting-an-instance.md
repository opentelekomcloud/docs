# Deleting an Instance<a name="EN-US_TOPIC_0143117216"></a>

## Scenario<a name="section33628036"></a>

Delete one or more Kafka premium instances at a time. With a few clicks on the DMS console, you can delete multiple Kafka premium instances that failed to be created.

>![](public_sys-resources/icon-warning.gif) **WARNING:**   
>Deleting a Kafka premium instance will delete the data in the instance without any backup. Exercise caution when performing this operation.  

## Prerequisites<a name="section34216874"></a>

-   The Kafka premium instance you want to delete already exists.
-   The status of the Kafka premium instance you want to delete is in the  **Running**  or  **Faulty**  state.

## Deleting a Kafka Premium Instance<a name="section949205010406"></a>

1.  Log in to the management console.
2.  Choose  **Application**  \>  **Distributed Message Service**  to open the DMS console.
3.  In the navigation pane, choose  **Kafka Premium**.
4.  Select one or more Kafka premium instances in the instance list.

    Kafka premium instances in  **Creating**,  **Starting**,  **Stopping**, or  **Restarting**  state cannot be deleted.

5.  Click  **Delete**  on the top of the instance list.
6.  Click  **Yes**.

    It takes 1 to 60 seconds to delete a Kafka premium instance.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >To delete a Kafka premium instance, you can also choose  **Operation**  \>  **Delete**  in the same row as the chosen Kafka premium instance on the  **Kafka Premium**  page.  


## Deleting a Kafka Premium Instance That Failed to be Created<a name="section586292817397"></a>

1.  Log in to the management console.
2.  Choose  **Application**  \>  **Distributed Message Service**  to open the DMS console.
3.  In the navigation pane, choose  **Kafka Premium**.

    If there are Kafka premium instances that failed to be created,  **Instance Creation Failures**  and quantity information will be displayed.

4.  Click the icon or quantity next to  **Instance Creation Failures**.

    The  **Instance Creation Failures**  page is displayed.

5.  Delete Kafka premium instances that failed to be created in either of the following ways:
    -   To delete all Kafka premium instances that failed to be created at once, click  **Clear Failed Instance**.
    -   To delete a single Kafka premium instance that failed to be created, click  **Delete **in the same row as the chosen Kafka premium instance.


