# Why Do I Fail to Publish Messages to a DMS Message Queue?<a name="smn_faq_0022"></a>

Check whether required message queue permission is granted to SMN in the DMS service. If no, perform the following operations to grant permissions. If SMN has been granted but you still cannot push messages, the failure may be caused by unstable network connection or other reasons. You can contact customer service to deal with the problem.

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  on the upper left to select the desired region and project.
3.  In the  **Application** category, click **Distributed Message Service**.

    The DMS console is displayed.

4.  In the queue list, locate the required queue and click its name. Detailed queue information is displayed.
5.  On the  **Policy Management** tab, click **Create Queue Policy**.

    Set  **Permission** to **Allow**, **Policy Type** to **Service-based**, and **Service** to **SMN**. Specify the action as needed.

6.  Click  **OK**.

