# Replacing AS Configuration in an AS Group<a name="EN-US_TOPIC_0042018370"></a>

## Scenarios<a name="section2495449014355"></a>

If you need to change the ECS specifications in an AS group, you need to change the AS configuration. If an AS group is performing a scaling action, the instance configuration in the action is the one before the replacement.

## Procedure<a name="section1657416306249"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner to select a region and a project.
3.  Under  **Computing**, click  **Auto Scaling**. In the navigation pane on the left, choose  **Instance Scaling**. Then click the  **AS Groups**  tab.
4.  Click the name of the target AS group. On the  **Basic Information**   page, click  **Change Configuration**  to the right of  **Configuration Name**.

    You can also locate the row containing the target AS group and choose  **More**  \>  **Change Configuration**  in the  **Operation**  column.

5.  In the displayed  **Change AS Configuration**  dialog box, select another AS configuration to be used by the AS group.
6.  Click  **OK**.

