# Viewing a Monitoring Report<a name="EN-US_TOPIC_0204851468"></a>

## Scenarios<a name="section87788284194"></a>

This topic describes how to view the monitoring report of an EIP, covering the current protection status, protection settings, and the traffic and anomalies within the last 24 hours.

## Prerequisites<a name="section284611418201"></a>

You have obtained an account and its password to log in to the management console.

## Procedure<a name="section1544716185202"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon_dt-4.png)  in the upper left corner and select the region or project.
3.  Under  **Security**, choose  **Anti-DDoS**. The  **Security Console**  is displayed.
4.  Select the  **Public IP Addresses**  tab, locate the target IP address and click  **View Monitoring Report**  in the  **Operation**  column, as shown in  [Figure 1](#fig28737219154047)

    **Figure  1**  Viewing a monitoring report<a name="fig28737219154047"></a>  
    ![](figures/viewing-a-monitoring-report.png "viewing-a-monitoring-report")

5.  On the  **Monitoring Report**  page, view monitoring details about a public IP address.

    -   You can view information such as the current protection status, protection settings, and the traffic and anomalies within the last 24 hours.
    -   A 24-hour defense traffic chart is generated from data points taken in five-minute intervals. It includes the following information:
        -   **Traffic \(Kbps\)**  displays the traffic status of the selected ECS, including the incoming attack traffic and normal traffic.
        -   **Packet Rate \(pps\)**  displays the packet rate of the selected ECS, including the attack packet rate and normal incoming packet rate.

    -   The attack event list within one day records DDoS attacks on the ECS within one day, including cleaning events and black hole events.

    **Figure  2**  Monitoring report<a name="fig3537135062113"></a>  
    ![](figures/monitoring-report.png "monitoring-report")

    >![](/images/icon-note.gif) **NOTE:**   
    >On the  **Monitoring Report**  page, click  ![](figures/icon_download.png)  to download the monitoring report about the public IP address.  


