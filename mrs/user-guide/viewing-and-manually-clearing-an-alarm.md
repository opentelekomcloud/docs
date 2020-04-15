# Viewing and Manually Clearing an Alarm<a name="EN-US_TOPIC_0125375696"></a>

## Scenario<a name="section36000642162238"></a>

You can view and manually clear an alarm on MRS Manager.

Generally, the system automatically clears an alarm when the fault that generated the alarm is rectified. If the alarm is not cleared automatically after the fault is rectified, and if the alarm has no impact on the system, you can manually clear the alarm.

On the MRS Manager portal, you can view the most recent 100,000 alarms, including those that have either been manually or automatically cleared, or not cleared. If the number of cleared alarms exceeds 100,000 and is about to reach 110,000, the system automatically dumps the earliest 10,000 cleared alarms to the dump path  **$\{BIGDATA\_HOME\}/OMSV100R001C00x8664/workspace/data**  on the active management node. The directory will be automatically generated when alarms are dumped for the first time.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>You can set an interval for automatic page refreshing or click  ![](figures/en-us_image_0125375675.jpg)  to refresh the page immediately.  
>The following parameters are supported:  
>-   **Refresh every 30 seconds**: refreshes the page once every 30 seconds.  
>-   **Refresh every 60 seconds**: refreshes the page once every 60 seconds.  
>-   **Stop refreshing**: stops page refreshing.  

## Procedure<a name="section1141339162319"></a>

1.  On MRS Manager, click  **Alarms**  and view the alarm information.
    -   By default, alarms are displayed in descending order by  **Generated On**. You can click **Alarm ID**,  **Alarm Name**,  **Severity**, **Generated On**, **Location**, or **Operation**  to change the display mode.
    -   You can filter out all alarms of the same severity in  **Severity**, including cleared alarms and uncleared alarms.
    -   You can click![](figures/en-us_image_0125375994.jpg),![](figures/en-us_image_0125375251.jpg),![](figures/en-us_image_0125376031.jpg) or ![](figures/en-us_image_0125375210.jpg) to filter out alarms whose severity is **Critical**, **Major**, **Minor**, or **Warning**.


1.  Click  **Advanced Search**. In the displayed alarm search area, set search criteria and click **Search**  to view the information about specified alarms. Click **Reset**  to reset search criteria.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >You can set  **Start Time** and **End Time**  to specify the time range when alarms are generated.  

    Rectify the fault by referring to the help information  [Alarm Reference](alarm-reference.md). If the alarms are generated due to other cloud services on which MRS depends, you need to contact the maintenance personnel of the relevant cloud services.

2.  If the alarm needs to be manually cleared, click  **Clear Alarm**.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If you want to clear multiple alarms, select those you want to clear and click  **Clear Alarm**  to clear them in batches. A maximum of 300 alarms can be cleared each time.  


