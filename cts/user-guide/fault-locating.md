# Fault Locating<a name="en-us_topic_0043371379"></a>

## **Scenarios**<a name="section6291060118322"></a>

If a resource or an action encounters an exception, you can query records of the resource or action in a specified time period and view its request and response to facilitate fault locating.

## Prerequisites<a name="section2947819183220"></a>

You have enabled CTS and the tracker is normal. For details about how to enable CTS, see  [Enabling CTS](enabling-cts.md).

## Procedure<a name="section64841869191343"></a>

The following steps use an ECS as an example to describe how to locate an ECS fault.

1.  Log in to the management console using the administrator account.
2.  Click  ![](figures/icon-region-0.png)  in the upper left corner to select the desired region and project.
3.  Click  **Service List**  and choose  **Management & Deployment**  \>  **Cloud Trace Service**.
4.  Choose  **Trace List**  in the navigation pane on the left.
5.  On the trace list page, click  **Filter**. In the displayed box, specify  **Trace Source**,  **Resource Type**, and  **Search By**, and click  **Query**.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >For example, you can select  **ECS**  for  **Trace Source**,  **ecs**  for  **Resource Type**, and  **Resource ID**  for  **Search By**, enter  _ID of the faulty VM_  in the right text box, and set the time range to 06:00 to 12:00 at a certain date.  

6.  Check the query result. Pay attention to the request type and response of each trace, and traces whose status is  **warning**  or  **incident**  and traces whose response shows a failure.

The following steps take the locating of an ECS creation fault as an example.

1.  Log in to the management console using the administrator account.
2.  Click  ![](figures/icon-region-0.png)  in the upper left corner to select the desired region and project.
3.  Click  **Service List**  and choose  **Management & Deployment**  \>  **Cloud Trace Service**.
4.  Choose  **Trace List**  in the navigation pane on the left.
5.  Specify filters based on the failed ECS creation task. For example, you can select  **ECS**  for  **Trace Source**,  **ecs**  for  **Resource Type**, and  **warning**  for the trace status to query the trace named  **createSingleServer**.
6.  Locate the fault based on the error code or error message in the trace.

