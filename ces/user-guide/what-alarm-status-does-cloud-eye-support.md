# What Alarm Status Does Cloud Eye Support?<a name="EN-US_TOPIC_0084812079"></a>

Cloud Eye supports three alarm status:  **Alarm**,  **OK**, and  **Insufficient data**.

-   If an alarm rule is disabled, its alarm status is considered as invalid, and  **Disabled**  is displayed.
-   **Insufficient data**  indicates that no monitoring data is reported for three consecutive hours because the corresponding service instance is deleted or the instance status is abnormal.
-   **Alarm**  indicates that the monitoring data meets the preset alarm policy.
-   **OK**  indicates that the monitoring data is reported normally and does not meet the preset alarm policy.

