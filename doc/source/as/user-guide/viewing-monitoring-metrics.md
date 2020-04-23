# Viewing Monitoring Metrics<a name="EN-US_TOPIC_0108337600"></a>

## Scenarios<a name="section1930814493166"></a>

The cloud platform provides Cloud Eye to help you obtain the running status of your ECSs. This section describes how to view details of AS group metrics to obtain information about the status of the ECSs in the AS group.

## Prerequisites<a name="en-us_topic_0027371530_section8439794224022"></a>

The ECS is running properly.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>-   Monitoring metrics such as  **CPU Usage**  and  **Disks Read Rate**  are available only when there is at least one instance in an AS group. If not, only the  **Number of Instances**  metric is available.  
>-   Monitoring data is not displayed for a stopped, faulty, or deleted ECS. After such an ECS restarts or recovers, the monitoring data is available.  

## Viewing Monitoring Metrics on Auto Scaling<a name="section53841197455"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner to select a region and a project.
3.  Under  **Computing**, click  **Auto Scaling**. In the navigation pane on the left, choose  **Instance Scaling**.
4.  On the  **AS Groups**  page, find the AS group to view monitoring data and click its name.
5.  Click the  **Monitoring**  tab to view the monitoring data.

    You can view data of the last 1, 3, and 12 hours. If you want to view data for a longer time range, click  **View more details**  to go to the  **Cloud Eye**  page, hover your mouse over a graph, and click  ![](figures/icon-image.png).


## Viewing Monitoring Metrics on Cloud Eye<a name="en-us_topic_0027371530_section44667294224513"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner to select a region and a project.
3.  Under  **Management & Deployment**, click  **Cloud Eye**.
4.  In the navigation pane on the left, choose  **Cloud Service Monitoring**  \>  **Auto Scaling**.
5.  Locate the row that contains the target metric and click  **View Metric**  in the  **Operation**  column to view monitoring data.

    You can view data of the last 1, 3, and 12 hours. Hover your mouse over a graph and click  ![](figures/icon-image.png)  to view data for a longer time range.


>![](public_sys-resources/icon-note.gif) **NOTE:**   
>It can take a period of time to obtain and transfer the monitoring data. Therefore, wait for a while and then check the data.  

