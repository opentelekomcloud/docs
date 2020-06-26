# Configuring the Number of Health Check Reports to Be Reserved<a name="EN-US_TOPIC_0125375541"></a>

## Scenario<a name="section12012924155126"></a>

Health check reports of MRS clusters, services, and hosts may vary with the time and scenario. You can modify the number of health check reports to be reserved on MRS Manager for later comparison.

This setting is valid for health check reports of clusters, services, and hosts. Report files are saved in  **$BIGDATA\_DATA\_HOME/Manager/healthcheck**  on the active management node by default and are automatically synchronized to the standby management node.

## Prerequisites<a name="section3225276215519"></a>

-   You have specified service requirements and planned the save time and health check frequency.
-   The disk spaces of the active and standby management nodes are sufficient.

## Procedure<a name="section38680709155053"></a>

1.  On MRS Manager, choose  **System**  \>  **Check Health Status**  \>  **Configure Health Check**.
2.  Set  **Max. Number of Health Check Reports** to the number of health check reports to be reserved. The value ranges from **1** to **100** and the default is **50**.
3.  Click  **OK** to save the configuration. The **Health check configuration saved successfully**  is displayed in the upper-right corner.

