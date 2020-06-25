# Performing a Health Check<a name="EN-US_TOPIC_0125375923"></a>

## Scenario<a name="s5674fd0b53a049229ad47593b46a13a2"></a>

To ensure that cluster parameters, configurations, and monitoring are correct and that the cluster can run stably for a long time, you can perform a health check during routine maintenance.

>![](/images/icon-note.gif) **NOTE:**   
>A system health check includes MRS Manager, service-level, and host-level health checks:  
>-   MRS Manager health checks focus on whether the unified management platform can provide management functions.  
>-   Service-level health checks focus on whether components can provide services properly.  
>-   Host-level health checks focus on whether host indicators are normal.  
>The system health check has three types of check items: Health Status, related alarms, and customized monitoring indicators for each check object. The health check results are not always the same as the  **Health Status**  on the portal.  

## Procedure<a name="s2bb186281bff48e2ac6b39bf9904fa55"></a>

-   Manually perform the health check for all services.

    1.  On MRS Manager, click  **Service**.
    2.  Choose  **More**  \>  **Start Cluster Health Check**  to start the health check for all services.

    >![](/images/icon-note.gif) **NOTE:**   
    >-   The cluster health checks include MRS Manager, service, and host status checks.  
    >-   To perform cluster health checks, you can also choose  **System**  \>  **Check Health Status**  \>  **Start Cluster Health Check**  on MRS Manager.  
    >-   To export the health check result, click  **Export Report**  in the upper left corner.  

-   Manually perform the health check for a service.
    1.  On MRS Manager, click  **Service**, and click the target service in the service list.
    2.  Choose  **More**  \>  **Start Service Health Check**  to start the health check for a specified service.

-   Manually perform the health check for a host.
    1.  On MRS Manager, click  **Host**.
    2.  Select the check box of the target host.
    3.  Choose  **More**  \>  **Start Host Health Check**  to start the health check for the host.


-   Perform an automatic health check.
    1.  On MRS Manager, click  **System**.
    2.  Under  **Maintenance**, click **Check Health Status**.
    3.  Click  **Configure Health Check**  to configure automatic health check items.

        **Periodic Health Check** indicates whether to enable the automatic health check function. The switch of the **Periodic Health Check** is disabled by default. Click the switch to enable the function. Select **Daily**,  **Weekly**, or **Monthly**  as required.

        Click  **OK** to save the configuration. The **Health check configuration saved successfully**  is displayed in the upper-right corner.



