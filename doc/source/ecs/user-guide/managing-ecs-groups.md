# Managing ECS Groups<a name="EN-US_TOPIC_0032980085"></a>

## Scenarios<a name="section33282082212946"></a>

An ECS group allows you to create ECSs on different physical servers, thereby improving service reliability. This function does not apply to existing ECSs. You cannot add existing ECSs to an ECS group.

## Notes<a name="section50994308215238"></a>

An existing ECS cannot be added to an ECS group.

## Procedure<a name="section5508038321333"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region-0.png)  in the upper left corner and select the desired region and project.
3.  Under  **Computing**, click  **Elastic Cloud Server**.
4.  In the navigation pane on the left, choose  **ECS Group**.
5.  On the  **ECS Group**  page, click  **Create ECS Group**.
6.  Enter the name of the target ECS group.

    The  **Anti-affinity**  policy is used by default.

7.  Click  **OK**.

## Follow-up Procedure<a name="section5656963010194"></a>

To add an ECS to an ECS group when creating the ECS, expand  **Advanced Options**  and select the target ECS group.

