# Managing Lifecycle of ECSs on a DeH in Batches<a name="EN-US_TOPIC_0046804375"></a>

## Scenarios<a name="section3231056202810"></a>

You can start, stop, restart, or delete multiple ECSs on a DeH at a time on the management console.

## Procedure<a name="section1241956132810"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  Under  **Computing**, click  **Dedicated Host**.

    The  **Dedicated Host**  page is displayed.

4.  Click the name of the target DeH in the list of DeHs.

    The DeH details page is displayed.

5.  On the  **ECSs on the DeH**  tab, select one or more target ECSs.

    You can concurrently select all ECSs on the current page by selecting the check box in the list header.

    >![](/images/icon-note.gif) **NOTE:**   
    >Except the deletion operation, ECSs to be operated in batches must be in the same state.  

6.  Click the corresponding button above the list to manage ECSs in batches.

    You can perform the following lifecycle management operations:

    -   **Start**  \(This operation can be performed only when ECSs are in the stopped state.\)
    -   **Stop**  \(This operation can be performed only when ECSs are in the started state.\)
    -   **Restart**  \(This operation can be performed only when ECSs are in the started state.\)
    -   **Delete**


