# Restarting DCS Instances<a name="en-us_topic_0054235818"></a>

## Scenario<a name="section32267243"></a>

On the DCS console, you can restart one or multiple DCS instances at a time.

>![](public_sys-resources/icon-notice.gif) **NOTICE:** 
>-   While a DCS instance is restarting, it cannot be read from or written to.
>-   If the DCS instance is a single-node instance, data will also be deleted from it when it is restarted.
>-   An attempt to restart a DCS instance while it is being backed up may result in a failure.

## Prerequisites<a name="section21969731"></a>

The DCS instances you want to restart are in the  **Running**  or  **Faulty**  state.

## Procedure<a name="section63509856"></a>

1.  Log in to the management console.
2.  Click  ![](figures/project.png) in the upper left corner of the management console and select a region and a project.
3.  Click  **Service List**, and choose **Database** \> **Distributed Cache Service**  to launch the DCS console.
4.  In the navigation pane, choose  **Cache Manager**.
5.  Choose instances to restart.
    -   To restart a single instance, choose  **Restart**  in the same row as the instance.
    -   To restart multiple instances, select the instances to restart and click  **Restart**  above the instance list.

6.  In the displayed dialog box, click  **Yes**.

    It takes 1 to 30 minutes to restart DCS instances. After DCS instances are restarted, their status changes to  **Running**.

    >![](public_sys-resources/icon-note.gif) **NOTE:** 
    >By default, only the instance process will restart. However, selecting  **Force restart**  will restart the VM on which the chosen DCS instance runs.


