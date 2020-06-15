# Managing Background Tasks<a name="EN-US_TOPIC_0237964733"></a>

## Scenario<a name="section37540721"></a>

After you initiate certain instance operations such as scaling up instances, and changing a password, a background task will start for each operation. On the DCS console, you can view the background task status and clear task information by deleting task records.

## Prerequisites<a name="section2322177"></a>

At least one DCS instance has been created.

## Procedure<a name="section20899598"></a>

1.  Log in to the management console.
2.  Click![](figures/icon-region.png)  in the upper left corner of the management console and select a region and a project.
3.  Click  **Service List**, and choose  **Database**  \>  **Distributed Cache Service**  to launch the DCS console.
4.  In the navigation pane, choose  **Cache Manager**.
5.  Click the name of the DCS instance whose background task you want to view.
6.  Click the  **Background Task Management**  tab.

    A list of background tasks is displayed.

7.  Filter background tasks, refresh task status, or delete task records.

    -   To filter background tasks by date, click  ![](figures/icon-date.png)  on top of the background task list, specify  **Start Date**  and  **End Date**, and click  **OK**.
    -   To delete the record of a background task, choose  **Operation**  \>  **Delete**  in the same row as the task.

    >![](/images/icon-note.gif) **NOTE:**   
    >Only tasks whose status is  **Successful**  or  **Failed**  can have their records deleted.  


