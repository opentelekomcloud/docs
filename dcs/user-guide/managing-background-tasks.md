# Managing Background Tasks<a name="dcs-en-ug-180312009"></a>

## Scenario<a name="section8949122417468"></a>

After you initiate certain instance operations such as scaling up instances, and changing a password, a background task will start for each operation. On the DCS console, you can view the background task status and clear task information by deleting task records.

## Prerequisites<a name="section994932416463"></a>

At least one DCS instance has been created.

## Procedure<a name="section6949172419462"></a>

1.  Log in to the management console.
2.  Click  ![](figures/project.png) in the upper left corner of the management console and select a region and a project.
3.  Click  **Service List**, and choose **Database** \> **Distributed Cache Service**  to launch the DCS console.
4.  In the navigation pane, choose  **Cache Manager**.
5.  Click the name of the DCS instance whose background task you want to view.
6.  Click the  **Background Tasks **tab.

    A list of background tasks is displayed.

7.  Filter background tasks, refresh task status, or delete task records.
    -   To filter background tasks by date, click  ![](figures/en-us_image_0232710363.png) on top of the background task list, specify **Start Date **and **End Date**, and click **OK**.
    -   To delete the record of a background task, choose  **Operation** \> **Delete**  in the same row as the task.

        >![](public_sys-resources/icon-note.gif) **NOTE:** 
        >Only tasks whose status is  **Successful**  or  **Failed**  can have their records deleted.



