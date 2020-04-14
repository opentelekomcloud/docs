# Disabling an AS Group<a name="EN-US_TOPIC_0042018373"></a>

## Scenarios<a name="section2495449014355"></a>

When you are required to stop an instance in an AS group for configuration or upgrade, disable the AS group before performing the operation. This prevents the instance from being deleted in a health check. When the instance status restores, enable the AS group again.

If a scaling action, for example, creating an instance or EVS disk, consistently fails \(the failure cause can be viewed on the  **Elastic Cloud Server**  page\) and retries in an AS group, use either of the following methods to stop the retry:

-   Disable the AS group. Then, the scaling action that is being performed fails and will not retry. Enable the AS group again when the environment recovers or after replacing the AS configuration.
-   Disable the AS group and change the expected number of instances to the number of existing instances. After the scaling action fails and ends, the scaling action will not retry.

After an AS group is disabled, its status changes to  **Disabled**. AS does not automatically trigger any scaling actions for a  **Disabled**  AS group. When an AS group has an in-progress scaling action, the scaling action does not stop immediately after the AS group is disabled.

You can disable an AS group when its status is  **Enabled**  or  **Abnormal**.

## Procedure<a name="section51147066105242"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner to select a region and a project.
3.  Under  **Computing**, click  **Auto Scaling**. In the navigation pane on the left, choose  **Instance Scaling**. Then click the  **AS Groups**  tab.
4.  In the AS group list, locate the row containing the target AS group and click  **Disable**  in the  **Operation**  column. You can also click the AS group name and then  **Disable**  to the right of  **Status**  on the  **Basic Information**  page to disable the AS group.
5.  In the  **Disable AS Group**  dialog box, click  **Yes**.

