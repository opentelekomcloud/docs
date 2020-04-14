# Enabling an AS Group<a name="EN-US_TOPIC_0042018371"></a>

## Scenarios<a name="section2495449014355"></a>

You can enable an AS group to automatically increase or decrease instances.

After an AS group is enabled, its status changes to  **Enabled**. AS monitors the AS policy and triggers a scaling action for AS groups only in  **Enabled**  state. After an AS group is enabled, AS triggers a scaling action to automatically add or remove instances if the number of instances in the AS group is different from the expected number of instances.

An AS group can be enabled only when its status is  **Disabled**. Only if the status of an AS group is  **Abnormal**, you can select  **Forcibly Enable**  from the  **More**  drop-down list to enable it.

After you create an AS group and add an AS configuration to an AS group, the AS group is automatically enabled.

## Enabling an AS group<a name="section47602278104932"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner to select a region and a project.
3.  Under  **Computing**, click  **Auto Scaling**. In the navigation pane on the left, choose  **Instance Scaling**. Then click the  **AS Groups**  tab.
4.  In the AS group list, locate the row containing the target AS group and click  **Enable**  in the  **Operation**  column. You can also click the AS group name and then  **Enable**  to the right of  **Status**  on the  **Basic Information**  page to enable the AS group. 
5.  In the  **Enable AS Group**  dialog box, click  **Yes**.

## Forcibly Enabling an AS Group<a name="section10127616112737"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner to select a region and a project.
3.  Under  **Computing**, click  **Auto Scaling**. In the navigation pane on the left, choose  **Instance Scaling**. Then click the  **AS Groups**  tab.
4.  In the AS group list, locate the row containing the target AS group and select  **Forcibly Enable**  from the  **More**  drop-down list in the  **Operation**  column. You can also click the AS group name and then  **Forcibly Enable**  to the right of  **Status**  on the  **Basic Information**  page  to enable the AS group.
5.  In the  **Forcibly Enable AS Group**  dialog box, click  **Yes**.

