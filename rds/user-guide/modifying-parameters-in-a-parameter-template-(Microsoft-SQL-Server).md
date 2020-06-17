# Modifying Parameters in a Parameter Template<a name="en-us_topic_sqlserver_configuration"></a>

You can modify parameters in a custom parameter template as required for optimal RDS database performance.

You can change parameter values in custom parameter templates only and cannot change parameter values in default parameter templates. When you change parameter values in a custom parameter template, the changes take effect for all DB instances to which the parameter template applies.

If you change a parameter value, when the change takes effect is determined by the type of parameter.

The RDS console displays the statuses of DB instances to which the parameter template applies. For example, if the DB instance has not used the latest changes made to its parameter template, its status is  **Pending reboot**. You need to manually reboot the DB instance for the latest parameter changes to take effect for that DB instance.

>![](/images/icon-note.gif) **NOTE:**   
>RDS has default parameter templates whose parameter values cannot be changed. You can view these parameter values by clicking the default parameter templates. If a custom parameter template is set incorrectly and causes a database reboot to fail, you can configure the custom parameter template by referring to the configurations of the default parameter template.  

## Modifying Parameters in Batches<a name="section9213173102320"></a>

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  Choose  **Parameter Template Management**  in the navigation pane on the left. On the  **Custom Templates**  page, click the target parameter template.
5.  Modify the parameters as required.

    Relevant parameters are as follows:

    -   For details on parameter descriptions, visit the  [Microsoft SQL Server official website](https://msdn.microsoft.com/en-us/library/ms189631.aspx).
    -   Set  **remote access**  to  **0**  \(default value\) to prevent locally stored procedures from running on a remote server and remotely stored procedures from running on a local server.
    -   The  **max server memory \(MB\)**  parameter indicates the server memory. The default value equals to the OS memory \(MB\) minuses 520 \(MB\). Its minimum value is 1024 MB.

    Available operations are as follows:

    >![](/images/icon-notice.gif) **NOTICE:**   
    >After you modify parameters in a parameter template, some modifications immediately take effect for the DB instance to which the parameter template applies. Exercise caution when performing this operation.  

    -   To save the modifications, click  **Save**.
    -   To cancel the modifications, click  **Cancel**.
    -   To preview the modifications, click  **Preview**.

    >![](/images/icon-note.gif) **NOTE:**   
    >For details about the parameter template statuses, see  [Parameter Template Statuses](db-instance-statuses.md#sf14afc99d1fe4941b44ffca460288867).  
    >After you modify parameters in a parameter template, you need to click the DB instance to which the parameter template applies to view the status of the parameter template. On the displayed  **Basic Information**  page, if the status of the parameter template is  **Pending reboot**, you must reboot the DB instance for the modifications to take effect.  


## Modifying Instance Parameters<a name="section32191319235"></a>

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  On the  **Instance Management**  page, click the target DB instance.
5.  In the navigation pane on the left, choose  **Parameters**. On the displayed page, modify parameters as required.

    Relevant parameters are as follows:

    -   For details on parameter descriptions, visit the  [Microsoft SQL Server official website](https://msdn.microsoft.com/en-us/library/ms189631.aspx).
    -   Set  **remote access**  to  **0**  \(default value\) to prevent locally stored procedures from running on a remote server and remotely stored procedures from running on a local server.
    -   The  **max server memory \(MB\)**  parameter indicates the server memory. The default value equals to the OS memory \(MB\) minuses 520 \(MB\). Its minimum value is 1024 MB.

    Available operations are as follows:

    >![](/images/icon-notice.gif) **NOTICE:**   
    >After you modify parameters in a parameter template, the modifications immediately take effect for the DB instance to which the parameter template applies.  
    >For details about the parameter template statuses, see  [Parameter Template Statuses](db-instance-statuses.md#sf14afc99d1fe4941b44ffca460288867).  
    >After you modify parameters in a parameter template, you need to view the status of the DB instance to which the parameter template applies. If the status is  **Pending reboot**, you must reboot the DB instance for the modifications to take effect.  
    >-   If you have modified parameters of a primary DB instance, you need to reboot the primary DB instance for the modifications to take effect. \(For primary/standby DB instances, the parameter modifications also apply to the standby DB instance.\)  
    >-   If you have modified parameters of a read replica, you need to reboot the read replica for the modifications to take effect.  

    -   To save the modifications, click  **Save**.
    -   To cancel the modifications, click  **Cancel**.
    -   To preview the modifications, click  **Preview**.


