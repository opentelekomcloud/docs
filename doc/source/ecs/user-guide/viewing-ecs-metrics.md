# Viewing ECS Metrics<a name="EN-US_TOPIC_0027371530"></a>

## Scenarios<a name="section11121260224613"></a>

The public cloud platform provides Cloud Eye, which monitors the running statuses of your ECSs. You can obtain the monitoring metrics of each ECS on the management console.

## Prerequisites<a name="section8439794224022"></a>

-   The ECS is running properly.

    Cloud Eye does not display the monitoring data for a stopped, faulty, or deleted ECS. After such an ECS restarts or recovers, the monitoring data is available in Cloud Eye.

    >![](/images/icon-note.gif) **NOTE:**   
    >Cloud Eye discontinues monitoring ECSs that remain in  **Stopped**  or  **Faulty**  state for 24 hours and removes them from the monitoring list. However, the alarm rules for such ECSs are not automatically deleted.  

-   Alarm rules have been configured in Cloud Eye for the target ECS.

    The monitoring data is unavailable for the ECSs without alarm rules configured in Cloud Eye. For details, see  [Setting Alarm Rules](setting-alarm-rules.md).

-   The target ECS has been properly running for at least 10 minutes.

    The monitoring data and graphics are available for a new ECS after the ECS runs for at least 10 minutes.


## Procedure<a name="section44667294224513"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region-0.png)  in the upper left corner and select the desired region and project.
3.  Under  **Computing**, click  **Elastic Cloud Server**.
4.  In the search box above the upper right corner of the ECS list, enter the ECS name, IP address, or ID for search.
5.  Click the name of the target ECS. The page providing details about the ECS is displayed.
6.  Click the  **Monitoring**  tab to view the monitoring data.
7.  In the ECS monitoring area, select a duration to view the monitoring data.

    You can view the monitoring data of the ECS in the last 1, 3, or 12 hours.


