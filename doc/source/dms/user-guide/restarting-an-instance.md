# Restarting an Instance<a name="EN-US_TOPIC_0143117097"></a>

## Scenario<a name="section42474604"></a>

Restart one or more Kafka premium instances at a time on the DMS console.

>![](/images/icon-warning.gif) **WARNING:**   
>When a Kafka premium instance is being restarted, message retrieval and creation requests of the client will be rejected. Existing messages are not affected.  

## Prerequisites<a name="section46727122"></a>

The status of the Kafka premium instance you want to restart is either  **Running**  or  **Faulty**.

## Procedure<a name="section58551735104011"></a>

1.  Log in to the management console.
2.  Choose  **Application**  \>  **Distributed Message Service**  to open the DMS console.
3.  In the navigation pane, choose  **Kafka Premium**.
4.  Select one or more Kafka premium instances in the instance list.
5.  Click  **Restart**  on the top of the instance list.
6.  Click  **Yes**.

    It takes 3 to 15 minutes to restart a Kafka premium instance. After it is successfully restarted, the Kafka premium instance status should be  **Running**.

    >![](/images/icon-note.gif) **NOTE:**   
    >Restarting a Kafka premium instance only restarts the instance process and does not restart the VM where the instance is located.  
    >To restart a Kafka premium instance, you can also choose  **Operation**  \>  **Restart**  in the same row as the chosen Kafka premium instance on the  **Kafka Premium**  page.  


