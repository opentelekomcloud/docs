# Managing High-Speed Networks<a name="EN-US_TOPIC_0053537013"></a>

A high-speed network is an internal network among BMSs and provides high bandwidth for connecting BMSs in the same AZ. If you want to deploy services requiring high throughput and low latency, you can create high-speed networks.

## Restrictions<a name="section3172298191210"></a>

-   When creating a BMS, the network segment used by common NICs cannot overlap with that used by high-speed NICs.
-   The high-speed network does not support security groups, EIPs, DNS, VPNs, and Direct Connect connections.
-   You must select different high-speed networks for different high-speed NICs of a BMS.
-   After a BMS is provisioned, you cannot configure a high-speed network.

## Create a High-Speed Network<a name="section9719598219"></a>

1.  Log in to the management console.
2.  Under  **Computing**, click  **Bare Metal Server**.

    The BMS console is displayed.

3.  Click the  **High-Speed Networks**  tab and then click  **Create High-Speed Network**.
4.  Set the name and subnet for the high-speed network and click  **OK**.

## Change the Name of a High-Speed Network<a name="section10841132814213"></a>

1.  Log in to the management console.
2.  Under  **Computing**, click  **Bare Metal Server**.

    The BMS console is displayed.

3.  Click the  **High-Speed Networks**  tab. Locate the target high-speed network and click  **Modify**  in the  **Operation**  column.
4.  Change the high-speed network name and click  **OK**.

## Manage Private IP Addresses<a name="section1657616457520"></a>

1.  Log in to the management console.
2.  Under  **Computing**, click  **Bare Metal Server**.

    The BMS console is displayed.

3.  Click the  **High-Speed Networks**  tab. Locate the target high-speed network, click  **More**  in the  **Operation**  column, and select  **Manage Private IP Address**  from the drop-down list.
    -   To reserve a private IP address in the high-speed network for binding the IP address to a BMS during BMS creation or for other purposes, perform steps  [4](#li1182125141618)  to  [5](#li1464622114267).
    -   To delete a private IP address, perform step  [6](#li20230111011919).

4.  <a name="li1182125141618"></a>Click  **Assign Private IP Address**.
    -   If you select  **Automatic Assignment**, the system automatically assigns a private IP address.
    -   If you select  **Manual Assignment**, you can specify a specific IP address in the high-speed network segment as the private IP address.

5.  <a name="li1464622114267"></a>Click  **OK**.
6.  <a name="li20230111011919"></a>Locate the row that contains the target private IP address, and click  **Delete**  in the  **Operation**  column. In the displayed dialog box, click  **OK**  to delete the IP address.

