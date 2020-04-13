# Viewing Background Tasks<a name="EN-US_TOPIC_0221089391"></a>

After you initiate certain instance operations such as configuring public access and modifying the capacity threshold capacity, a background task will start for each operation. On the console, you can view the background task status and clear task information by deleting task records.

## Procedure<a name="section1625104935317"></a>

1.  Log in to the management console.
2.  Choose  **Application**  \>  **Distributed Message Service**  to open the DMS console.
3.  In the navigation pane, choose  **Kafka Premium**.
4.  Click the name of an instance.
5.  Click the  **Background Task Management**  tab.

    A list of background tasks is displayed.

6.  Click  ![](figures/icon-date.png), specify  **Start Date**  and  **End Date**, and click  **OK**  to view tasks started in the selected time period.
    -   Click  ![](figures/icon-refresh.png)  to refresh the task status.
    -   To clear the record of a background task, choose  **Operation**  \>  **Delete**.

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >You can only delete the records of tasks in the  **Successful**  or  **Failed**  state.  



