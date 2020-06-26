# Managing a Bandwidth Scaling Policy<a name="EN-US_TOPIC_0112331246"></a>

You can adjust the bandwidth through the bandwidth scaling policy. This section describes how to manage a bandwidth scaling policy, including enabling, disabling, modifying, deleting, and executing a bandwidth scaling policy.

## Enabling a Bandwidth Scaling Policy<a name="en-us_topic_0042018371_section47602278104932"></a>

A bandwidth scaling policy can be enabled only when its status is  **Disabled**.

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner to select a region and a project.
3.  Under  **Computing**, click  **Auto Scaling**. In the navigation pane on the left, choose  **Bandwidth Scaling**.
4.  In the bandwidth scaling policy list, locate the row containing the target policy and click  **Enable**  in the  **Operation**  column. 
5.  In the displayed  **Enable Bandwidth Scaling Policy**  dialog box, click  **Yes**.

## Disabling a Bandwidth Scaling Policy<a name="section25871448152519"></a>

A bandwidth scaling policy can be disabled only when its status is  **Enabled**.

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner to select a region and a project.
3.  Under  **Computing**, click  **Auto Scaling**. In the navigation pane on the left, choose  **Bandwidth Scaling**.
4.  In the bandwidth scaling policy list, locate the row containing the target policy and click  **Disable**  in the  **Operation**  column.
5.  In the displayed  **Disable Bandwidth Scaling Policy**  dialog box, click  **Yes**.

    >![](/images/icon-note.gif) **NOTE:**   
    >After a bandwidth scaling policy is disabled, its status changes to  **Disabled**. AS does not automatically trigger any scaling action based on a  **Disabled**  bandwidth scaling policy.  


## Modifying a Bandwidth Scaling Policy<a name="en-us_topic_0042018374_section2227263611026"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner to select a region and a project.
3.  Under  **Computing**, click  **Auto Scaling**. In the navigation pane on the left, choose  **Bandwidth Scaling**.

1.  In the bandwidth scaling policy list, locate the row containing the target policy and click the policy name to switch to its details page.

    Click  **Modify**  in the upper right corner of the page.

    You can also locate the row containing the target policy, click  **More**  in the  **Operation**  column, and select  **Modify**.

2.  Modify parameters. You can modify the following parameters of a bandwidth scaling policy:  **Policy Name**,  **EIP**,  **Policy Type**,  **Scaling Action**, and  **Cooldown Period**.
3.  Click  **OK**.

>![](/images/icon-note.gif) **NOTE:**   
>A bandwidth scaling policy which is being executed cannot be modified.  

## Deleting a Bandwidth Scaling Policy<a name="en-us_topic_0042018375_section1959939911151"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner to select a region and a project.
3.  Under  **Computing**, click  **Auto Scaling**. In the navigation pane on the left, choose  **Bandwidth Scaling**.
4.  In the bandwidth scaling policy list, locate the row containing the target policy, click  **More**  in the  **Operation**  column, and select  **Delete**.
5.  In the displayed  **Delete Bandwidth Scaling Policy**  dialog box, click  **Yes**.

    You can also select one or more scaling policies and click  **Delete**  above the list to delete one or more scaling policies.


>![](/images/icon-note.gif) **NOTE:**   
>-   You can delete a bandwidth scaling policy when you no longer need it. If you do not need it only during a specified period of time, you are advised to disable rather than delete it.  
>-   A bandwidth scaling policy can be deleted only when it is not being executed.  

## Executing a Bandwidth Scaling Policy<a name="en-us_topic_0151018598_sbdc76804de224059adf54b5a048df0e7"></a>

By executing a bandwidth scaling policy, you can immediately adjust the bandwidth to that configured in the bandwidth scaling policy, instead of having to wait until the trigger condition is met.

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner to select a region and a project.
3.  Under  **Computing**, click  **Auto Scaling**. In the navigation pane on the left, choose  **Bandwidth Scaling**.
4.  In the bandwidth scaling policy list, locate the row that contains the target policy and click  **Execute Now**  in the  **Operation**  column.
5.  In the displayed  **Execute Bandwidth Scaling Policy**  dialog box, click  **Yes**.

You can also go to the bandwidth scaling policy details page and click  **Execute Now**  in the upper right corner.

>![](/images/icon-note.gif) **NOTE:**   
>-   A bandwidth scaling policy can be executed only when the policy is enabled and no other bandwidth scaling policy is being executed.  
>-   Executing a bandwidth scaling policy does not affect automatic adjustment of the bandwidth when the trigger condition of the policy is met.  

