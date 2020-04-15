# Managing Resource Distribution<a name="EN-US_TOPIC_0125375394"></a>

## Scenario<a name="section35449204153239"></a>

You can query the top value curves, bottom value curves, or average data curves of key service and host monitoring indicators, that is, the resource distribution information, on MRS Manager. MRS Manager allows you to view the monitoring data of the last hour.

You can also modify the resource distribution on MRS Manager to display both the top and bottom value curves in service and host resource distribution figures.

Resource distribution of some monitoring indicators is not recorded.

## Procedure<a name="section37360238153324"></a>

-   View the resource distribution of service monitoring indicators.
    1.  On MRS Manager, click  **Service**.
    2.  Select the specific service in the service list.
    3.  Click  **Resource Distribution**.

        Select key service indicators in  **Metric**. MRS Manager displays the resource distribution data of the selected service indicators in the last hour.


-   View the resource distribution of host monitoring indicators.
    1.  On MRS Manager, click  **Host**.
    2.  Click the specific host in the host list.
    3.  Click  **Resource Distribution**.

        Select key host indicators from  **Metric**. MRS Manager displays the resource distribution data of the selected indicators in the last hour.


-   Configure resource distribution.
    1.  On MRS Manager, click  **System**.
    2.  In  **Configuration**, click **Configure Resource Contribution Ranking** under **Monitoring and Alarm**.

        Modify the displayed resource distribution quantity.

        -   Set  **Number of Top Resources**  to the number of top values.
        -   Set  **Number of Bottom Resources**  to the number of bottom values.

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >The sum of the number of top and bottom values must not be greater than five.  

    3.  Click  **OK**  to save the settings.

        The  **Number of top and bottom resources saved successfully**  is displayed in the upper-right corner.



