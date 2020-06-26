# Modifying an AS Group<a name="EN-US_TOPIC_0042018374"></a>

## Scenarios<a name="section2495449014355"></a>

You can modify an AS group as needed. The values of the following parameters can be changed: ,  **Max. Instances**,  **Min. Instances**,  **Expected Instances**,  **Cooldown Period**,  **Health Check Method**,  **Health Check Interval**,  **Health Check Grace Period**,  **Enterprise project**,  **Instance Removal Policy**,  **EIP**, and  **Notification Mode**.

>![](/images/icon-note.gif) **NOTE:**   
>Changing the value of  **Expected Instances**  will trigger a scaling action. Then, AS automatically increases or decreases the number of instances to the value of  **Expected Instances**.  

If an AS group is not enabled and does not contain any ECS instances, and no scaling action is being performed, you can also modify  **Subnet**  and  **ELB**  configurations.

## Procedure<a name="section2227263611026"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner to select a region and a project.
3.  Under  **Computing**, click  **Auto Scaling**. In the navigation pane on the left, choose  **Instance Scaling**. Then click the  **AS Groups**  tab.

1.  In the AS group list, locate the row containing the target AS group, click the AS group name to switch to the  **Basic Information**  page, and click  **Modify**  in the upper right corner.

    You can also locate the row containing the target AS group and choose  **More**  \>  **Modify**  in the  **Operation**  column.

2.  In the  **Modify AS Group**  dialog box, modify related data, for example, the expected number of instances.
3.  Click  **OK**.

