# Stopping DCS Instances<a name="EN-US_TOPIC_0237964720"></a>

## Scenario<a name="section12284267"></a>

On the DCS console, you can stop one or multiple DCS instances at a time.

>![](/images/icon-note.gif) **NOTE:**   
>-   After a DCS instance is stopped, it can no longer be read from or written to. If it is a single-node instance, data will also be deleted from it when it is stopped.  
>-   An attempt to stop a DCS instance while it is being backed up may result in a failure.  

## Prerequisites<a name="section43449544"></a>

The DCS instances you want to stop are in the  **Running**  state.

## Procedure<a name="section55501577"></a>

1.  Log in to the management console.
2.  Click![](figures/icon-region.png)  in the upper left corner of the management console and select a region and a project.
3.  Click  **Service List**, and choose  **Database**  \>  **Distributed Cache Service**  to launch the DCS console.
4.  In the navigation pane, choose  **Cache Manager**.
5.  Choose instances to stop.
    -   To stop a single instance, click  **Stop**  in the same row as the instance.
    -   To stop multiple instances, select the instances to stop and click  **Stop**  above the instance list.

6.  In the  **Stop**  dialog box, click  **OK**  to confirm that you want to stop the instances.

    It takes 1 to 30 minutes to stop DCS instances. After DCS instances are stopped, their status changes from  **Running**  to  **Stopped**.


