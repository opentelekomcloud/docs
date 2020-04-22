# How Do I Delete an ECS Created During a Scaling Action?<a name="EN-US_TOPIC_0107177452"></a>

## Methods<a name="section18167182325715"></a>

Method 1

1.  Log in to the management console.
2.  Under  **Computing**, click  **Auto Scaling**. In the navigation pane on the left, choose  **Instance Scaling**.
3.  Click the AS group name on the  **AS Groups**  tab.
4.  On the AS group details page, click the  **Instances**  tab.
5.  Locate the row that contains the target instance and click  **Remove and Delete**  in the  **Operation**  column.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >To delete multiple instances, select the check boxes in front of them and click  **Remove and Delete**.  


Method 2

1.  Log in to the management console.
2.  Under  **Computing**, click  **Auto Scaling**. In the navigation pane on the left, choose  **Instance Scaling**.
3.  Click the AS group name on the  **AS Groups**  tab.
4.  On the AS group details page, click the  **AS Policies**  tab.
5.  Click  **Add Policy**. In the displayed  **Add Policy**  dialog box, add an as policy to reduce instances as needed or set the number of instances to a specified value.

Method 3

1.  Log in to the management console.
2.  Under  **Computing**, click  **Auto Scaling**. In the navigation pane on the left, choose  **Instance Scaling**.
3.  Click the AS group name on the  **AS Groups**  tab.
4.  On the AS group details page, click  **Modify**  in the upper right corner.
5.  In the displayed  **Modify AS Group**  dialog box, change the value of  **Expected Instances**.

