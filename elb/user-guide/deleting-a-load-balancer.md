# Deleting a Load Balancer<a name="EN-US_TOPIC_0166333714"></a>

## Scenarios<a name="section20538244111217"></a>

When a load balancer is not in use any more, you can delete it at any time. A deleted load balancer cannot be recovered. Exercise caution when performing this operation.

If a public network load balancer is deleted, the bound EIP will not be deleted by default.

## Prerequisites<a name="section131941342381"></a>

The following resources have been deleted or removed:

-   Listeners
-   Backend server groups
-   Backend servers

## Procedure<a name="section13384917815"></a>

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/icon-region.png)  and select the desired region and project.
3.  Click  **Service List**. Under  **Network**, click  **Elastic Load Balancing**.
4.  Locate the target load balancer and click  **Delete**  in the  **Operation**  column.
5.  In the displayed dialog box, click  **Yes**.

## Export Load Balancer Information<a name="section19169366120"></a>

You can also export the load balancer list as a local backup.

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/icon-region.png)  and select the desired region and project.
3.  Click  **Service List**. Under  **Network**, click  **Elastic Load Balancing**.
4.  In the upper right corner of the load balancer list, click  ![](figures/20180702-151924(espace).png).

