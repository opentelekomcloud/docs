# Managing AS Policies<a name="EN-US_TOPIC_0042158948"></a>

An AS policy specifies the conditions for triggering a scaling action as well as the triggered operation. If the conditions are met, a scaling action is triggered to perform the required operation. This section describes how to manage an AS policy, including modifying, enabling, disabling, executing, and deleting an AS policy.

## Modifying an AS Policy<a name="section3429568117294"></a>

Modify parameter settings of an AS policy if it cannot meet service requirements.

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner to select a region and a project.
3.  Under  **Computing**, click  **Auto Scaling**. In the navigation pane on the left, choose  **Instance Scaling**. Then click the  **AS Groups**  tab.
4.  Locate the row containing the target AS group and click  **View AS Policy**  in the  **Operation**  column. On the displayed page, locate the row containing the target AS policy and choose  **More**  \>  **Modify**  in the  **Operation**  column.
5.  In the displayed  **Modify AS Policy**  dialog box, modify the parameters and click  **OK**.

## Enabling an AS Policy<a name="section206278173059"></a>

An AS policy can trigger scaling actions only when it and the AS group are both enabled. You can enable one or more AS policies for an AS group as required.

-   Before enabling multiple AS policies, ensure that the AS policies do not conflict with one another.
-   An AS policy can be enabled only when its status is  **Disabled**.

Locate the row containing the target AS group and click  **View AS Policy**  in the  **Operation**  column. On the displayed page, locate the row containing the target AS policy and click  **Enable**  in the  **Operation**  column. To concurrently enable multiple AS policies, select these AS policies and click  **Enable**  in the upper part of the AS policy list.

## Disabling an AS Policy<a name="section6367887185112"></a>

Disable a specified AS policy if you do not want it to trigger any scaling action within a specified period of time.

-   If all AS policies of an AS group are disabled, no scaling action will be triggered for this AS group. However, if you manually change the value of  **Expected Instances**, a scaling action will still be triggered.
-   You can disable an AS policy only when its status is  **Enabled**.

Locate the row containing the target AS group and click  **View AS Policy**  in the  **Operation**  column. On the displayed page, locate the row containing the target AS policy and click  **Disable**  in the  **Operation**  column. To concurrently disable multiple AS policies, select these AS policies and click  **Disable**  in the upper part of the AS policy list.

## Manually Executing an AS policy<a name="section1969644685112"></a>

Perform this operation to make the number of instances in an AS group reach the expected number of instances immediately.

-   You can manually execute an AS policy if the scaling conditions configured in the AS policy are not met.
-   You can manually execute an AS policy only when the AS group and AS policy are both in  **Enabled**  state.

    Locate the row containing the target AS group and click  **View AS Policy**  in the  **Operation**  column. On the displayed page, locate the row containing the target AS policy and click  **Execute Now**  in the  **Operation**  column.


## Deleting an AS Policy<a name="section353374285112"></a>

Delete an AS policy that will not be used for triggering scaling actions.

An AS policy can be deleted even when the scaling action triggered based on the AS policy is in progress. Deleting the AS policy does not adversely affect the in-progress scaling action.

Locate the row containing the target AS group and click  **View AS Policy**  in the  **Operation**  column. On the displayed page, locate the row containing the target AS policy and choose  **More**  \>  **Delete**  in the  **Operation**  column.

To concurrently delete multiple AS policies, select these AS policies and click  **Delete**  in the upper part of the AS policy list.

