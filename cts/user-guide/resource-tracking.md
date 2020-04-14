# Resource Tracking<a name="en-us_topic_0043371378"></a>

## Scenarios<a name="section28509637193319"></a>

This section describes how to view operation records of any cloud resource throughout its lifecycle and how to check details of a specific operation.

## Prerequisites<a name="section13625028193339"></a>

You have enabled CTS and the tracker is normal. For details about how to enable CTS, see  [Enabling CTS](enabling-cts.md).

## Procedure<a name="section727451193431"></a>

The following steps use an ECS as an example to describe how to view all operation records.

1.  Log in to the management console using the administrator account.
2.  Click  ![](figures/icon-region-0.png)  in the upper left corner to select the desired region and project.
3.  Click  **Service List**  and choose  **Management & Deployment**  \>  **Cloud Trace Service**.
4.  Choose  **Trace List**  in the navigation pane on the left.
5.  <a name="li36410601182"></a>On the trace list page, click  **Filter**. In the displayed box, specify  **Trace Source**,  **Resource Type**, and  **Search By**, and click  **Query**  to query the specified traces.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >For example, you can select  **ECS**  for  **Trace Source**,  **ecs **for  **Resource Type**, and  **Resource ID**  for  **Search By**, enter  _ID of the faulty ECS_  in the right text box, and click  **Query**  to query traces of the last seven days.  

6.  Choose  **Tracker**  from the left pane to switch to the  **Tracker**  page and obtain the OBS bucket name.
7.  <a name="li14173783182013"></a>Download archived or all trace files by following the instructions in  [Querying Archived Traces](querying-archived-traces.md).
8.  Check all operation and change records of the ECS in the results obtained in  [5](#li36410601182)  and  [7](#li14173783182013).

