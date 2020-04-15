# Managing Lifecycle of ECSs on DeHs<a name="EN-US_TOPIC_0046800268"></a>

## Scenarios<a name="section3231056202810"></a>

You can start, stop, restart, or delete ECSs on DeHs on the management console.

## Procedure<a name="section1241956132810"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  Under  **Computing**, click  **Dedicated Host**.

    The  **Dedicated Host**  page is displayed.

4.  Click the name of the target DeH in the list of DeHs.

    The DeH details page is displayed.

5.  On the  **ECSs on the DeH**  tab, locate the target ECS and click the target option in the  **Operation**  column to manage the ECS lifecycle.

    You can perform the following lifecycle management operations:

    -   **Modify Specifications**  \(This operation can be performed only when ECSs are in the stopped state.\)
    -   **Start**  \(This operation can be performed only when ECSs are in the stopped state.\)
    -   **Stop**  \(This operation can be performed only when ECSs are in the started state.\)
    -   **Restart**  \(This operation can be performed only when ECSs are in the started state.\)
    -   **Delete**


## Related Operations<a name="section6175746102828"></a>

On the  **ECSs on the DeH**  tab of the DeH details page, you can also click  **Create ECS**  to create ECSs.

For details, see "[Creating an ECS](https://docs.otc.t-systems.com/en-us/usermanual/ecs/en-us_topic_0021831611.html)".

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>-   When selecting an ECS type, pay attention to mapping between the ECS type and the DeH type. If no matched DeH resources exist, ECSs cannot be created.  

