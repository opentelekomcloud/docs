# What Can I Do If hostname of the Production Site Server and DR Site Server Are Different After a Planned Failover or Failover?<a name="sdrs_06_0404"></a>

## Symptom<a name="section37204431987"></a>

Users have changed  **hostname**  of the production site server before they perform a planned failover or failover for the first time. After the planned failover or failover, users start the DR site server and find that  **hostname**  of the DR site server is not updated accordingly.

## **Possible Causes**<a name="section11269131061117"></a>

For Linux servers, if you have changed  **hostname**  of the production site server before you perform a planned failover or failover for the first time, this modification will not synchronize to the DR site server.

## **Prerequisites**<a name="section2084985454913"></a>

-   The production site server is a Linux server with Cloud-Init installed.
-   **hostname**  of the production site server has been changed.

## Solution 1 \(If You Have Not Performed a Planned Failover or Failover\)<a name="section183011437149"></a>

Set  **preserve\_hostname: false**  to  **preserve\_hostname: true**  in the Cloud-Init configuration file  **/etc/cloud/cloud.cfg**  to ensure that  **hostname**  of the production site server and DR site server are the same after you enable protection.

The procedure is as follows:

1.  Log in to the production site server.
2.  Run the following command to edit the  **/etc/cloud/cloud.cfg**  configuration file:

    **sudo vim /etc/cloud/cloud.cfg**

3.  Modify  **preserve\_hostname**.
    -   If  **preserve\_hostname: false**  is already available in the  **/etc/cloud/cloud.cfg**  configuration file, change it to  **preserve\_hostname: true**.
    -   If  **preserve\_hostname: false**  is unavailable in the  **/etc/cloud/cloud.cfg**  configuration file, add  **preserve\_hostname: true**  before  **cloud\_init\_modules**.

4.  Perform a planned failover or failover.

    After the planned failover or failover,  **hostname**  of the DR site server and production site server are the same.


## Solution 2 \(If You Have Performed a Planned Failover or Failover\)<a name="section2538238204516"></a>

If you have not modified configuration file  **/etc/cloud/cloud.cfg**  before the planned failover or failover, log in to the DR site server and manually change  **hostname**  of the DR site server to that of the production site server.

