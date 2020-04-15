# Canceling Isolation of a Host<a name="EN-US_TOPIC_0125375226"></a>

## Scenario<a name="section2140760920333"></a>

After a host fault is rectified, users must cancel the isolation of the host so that the host can be used properly.

Users can cancel the isolation of a host on MRS Manager.

## Prerequisites<a name="section4577156020144"></a>

-   The host status is  **Isolated**.
-   The host fault has been rectified.

## Procedure<a name="section38783114201418"></a>

1.  On MRS Manager, click  **Host**.
2.  Select the checkbox of the host that you want to cancel its isolation.
3.  Choose  **More**  \>  **Cancel Host Isolation**.
4.  In  **Cancel Host Isolation**, click **OK**.

    When  **Operation succeeded** is displayed, click **Finish**. Host isolation is canceled successfully, and the value of **Operational Status** becomes **Normal**.

5.  Click the name of the host for which isolation has been canceled.  **Status** of the host is displayed. Click **Start All Roles**.

