# Adding Pay-per-Use EIPs to a Shared Bandwidth<a name="vpc010006"></a>

## Scenarios<a name="section15598193716333"></a>

Add pay-per-use EIPs to a shared bandwidth and the EIPs can then share that bandwidth. You can add multiple EIPs to a shared bandwidth at the same time.

>![](/images/icon-note.gif) **NOTE:**   
>-   After an EIP is added to a shared bandwidth, the original bandwidth size used by the EIP will become invalid. The EIP will use the shared bandwidth.  
>-   The EIP's original dedicated bandwidth will be deleted.  

## Procedure<a name="section67201052194510"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  On the console homepage, under  **Network**, click  **Elastic IP**.
4.  In the navigation pane on the left, choose  **Elastic IP and Bandwidth**  \>  **Shared Bandwidths**.
5.  In the shared bandwidth list, locate the row that contains the bandwidth to which EIPs are to be added, choose  **More**  \>  **Add EIP**  in the  **Operation**  column, and select the EIPs to be added in the displayed dialog box.

    **Figure  1**  Add EIP<a name="fig91601550174919"></a>  
    ![](figures/add-eip.png "add-eip")

6.  Click  **OK**.

