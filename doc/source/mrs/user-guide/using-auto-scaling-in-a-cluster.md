# Using Auto Scaling in a Cluster<a name="EN-US_TOPIC_0125375927"></a>

In big data application scenarios, especially real-time data analysis and processing, the number of cluster nodes needs to be dynamically increased or decreased according to data volume changes to add or reduce resources. The auto scaling function of MRS enables clusters to be elastically scaled out or in based on cluster loads. In addition, if the data volume changes regularly every day and you want to scale out or in a cluster before the data volume changes, you can use the MRS resource plan feature \(setting a Task node range based on the time range\).

-   Auto scaling rules: You can increase or decrease Task nodes based on real-time cluster loads. Auto scaling will be triggered when the data volume changes but there may be some delay.
-   Resource plans \(setting a Task node range based on the time range\): If the data volume changes periodically, you can create resource plans to resize the cluster before the data volume changes, thereby avoiding a delay in increasing or decreasing resources.

You can configure either auto scaling rules or resource plans or both of them to trigger the auto scaling. Configuring both resource plans and auto scaling rules improves the cluster node scalability to cope with occasionally unexpected data volume peaks.

In some service scenarios, resources need to be reallocated or service logic needs to be modified after cluster scale-out or scale-in. If you manually scale out or scale in a cluster, you can log in to cluster nodes to reallocate resources or modify service logic. If you use auto scaling, MRS enables you to customize automation scripts for resource reallocation and service logic modification. Automation scripts can be executed before and after auto scaling and automatically adapt to service load changes, all of which eliminates manual operations. In addition, automation scripts can be fully customized and executed at various moments, which can meet your personalized requirements and improve auto scaling flexibility.

>![](/images/icon-note.gif) **NOTE:**   
>You can configure auto scaling rules when creating a cluster or after a cluster has been created. This section describes how to configure auto scaling rules after a cluster has been created. For details about how to configure auto scaling rules during cluster creation, see  [Configuring Auto Scaling Rules When Creating a Cluster](configuring-auto-scaling-rules-when-creating-a-cluster.md).  

## Background<a name="section123416471427"></a>

You can configure either auto scaling rules or resource plans or both of them to trigger the auto scaling.

-   Auto scaling rules:
    -   A user can set a maximum of five scale-out or scale-in rules.
    -   The system judges rules set by the user in sequence and cluster scale-out rules take priorities over cluster scale-in rules. Place rules according to their importance degrees and put the most important rule in the front to prevent the rules from being repeatedly triggered due to the unexpected result of cluster scale-out or scale-in.
    -   Comparison factors are  **Greater than**, **Greater than or equal to**, **Less than**, and **Less than or equal to**.
    -   Cluster scale-out or scale-in can be triggered only after the configured metric threshold is reached for 5n \(the default value of  **n**  is 1\) consecutive minutes.
    -   After each cluster scale-out or scale-in, there is a cooldown period. The default cooldown period is  **20** minutes and the minimum cooldown period is **0**  minutes.
    -   In each cluster scale-out or scale-in, at least one node and at most 100 nodes can be added or reduced.

-   Resource plans \(setting a Task node range based on the time range\):
    -   You can specify a Task node range \(minimum number to maximum number\) in a time range. If the number of Task nodes is beyond the Task node range in a resource plan, the system triggers auto scaling.
    -   You can set a maximum of five resource plans for a cluster.
    -   A resource plan cycle is by day. The start time and end time can be set to any time point between 00:00 and 23:59. The start time must be at least 30 minutes earlier than the end time. Time ranges configured for different resource plans cannot overlap.
    -   After a resource plan triggers cluster scale-out or scale-in, there is a 10-minute cooldown period. Auto scaling will not be triggered again within the cooldown period.
    -   When a resource plan is enabled, the number of Task nodes is limited to the default node range at any time except the time range set in the resource plan.
    -   If the resource plan is not enabled, the number of Task nodes is not limited to the default node range.

-   Automation scripts:
    -   You can set an automation script so that it can automatically run on cluster nodes when auto scaling is triggered.
    -   You can set a maximum number of 10 automation scripts for a cluster.
    -   You can specify an automation script to be executed on one or more types of nodes.
    -   Automation scripts can be executed before or after scale-out or scale-in.
    -   Before using automation scripts, upload them to a cluster VM or OBS bucket in the same region as the cluster. The automation scripts uploaded to the cluster VM can be executed only on the existing nodes. If you want to make the automation scripts run on the new nodes, upload them to the OBS bucket.


## Using Auto Scaling Rules Alone<a name="section2323121984319"></a>

You can configure auto scaling rules to adjust the number of Task nodes based on data volume changes to increase or decrease resources.

1.  Log in to the MRS management console.
2.  Click  ![](figures/dt_mrs_project_region_image01.png)  in the upper-left corner on the management console and select **Region** and **Project**.
3.  Choose  **Clusters \> Active Clusters**, select a running cluster, and click its name to switch to the cluster information page.
4.  On the  **Nodes**  tab page, click  **Auto Scaling**  in the  **Operation**  column of the Task node group. The  **Auto Scaling**  page is displayed.
5.  Configure an auto scaling rule.

    You can configure the auto scaling rule to adjust the number of nodes, which affects the actual price. Therefore, exercise caution when performing this operation.

    -   **Auto Scaling**: indicates whether to enable auto scaling. Auto scaling is disabled by default. After you enable it, you can configure the following parameters.
    -   **Node Range**
        -   **Default Range**: Enter the minimum and maximum number of nodes. This value range is 0 to 500 and applies to all scale-out and scale-in rules.
        -   **Configure Node Range in a Specified Time Range**: This parameter is used to configure an auto scaling resource plan. This parameter is not configured here.

    -   **Auto Scaling Rule**: To enable  **Auto Scaling**, configure scale-out or scale-in rules.

        Configuration procedure:

        1.  Select  **Scale Out** or **Scale In**.
        2.  Click  **Add Rule**. The **Add Rule**  page is displayed.
        3.  Configure the parameters  **Rule Name**, **If**, **Last**, **Add**, **Cooldown Period**.
        4.  Click  **OK**.

            You can view the rules you configured in the  **Scale Out**  or **Scale In**  area on the **Auto Scaling**  page.


6.  Select  **I agree to authorize MRS to scale out or in nodes based on the above rule.**.
7.  Click  **OK**.

## Using Resource Plans Alone<a name="section2613204734619"></a>

If the data volume changes regularly every day and you want to scale out or in a cluster before the data volume changes, you can create resource plans to adjust the number of Task nodes as planned in the specified time range.

For example, the service data volume for real-time processing peaks between 7:00 and 13:00 every day and is stable and low for other time. Assume that an MRS streaming cluster is used to process the service data. Between 7:00 and 13:00, five Task nodes are required for processing the peak data volume, and only two task nodes are required for other time. You can perform the following steps to configure a resource plan.

1.  Log in to the MRS management console.
2.  Click  ![](figures/dt_mrs_project_region_image01.png)in the upper left corner on the management console and select  **Region**  and  **Project**.
3.  Choose  **Clusters**  \>  **Active Clusters**, select a running cluster, and click its name to switch to the cluster details page.
4.  On the  **Nodes**  tab page, click  **Auto Scaling**  in the  **Operation**  column of the Task node group. The  **Auto Scaling**  page is displayed.
5.  Configure a resource plan.

    You can configure the resource plan to adjust the number of nodes, which affects the actual price. Therefore, exercise caution when performing this operation.

    Configuration procedure:

    1.  On the  **Auto Scaling**  page, enable  **Auto Scaling**.
    2.  Set  **Default Range**  to  **2-2**  for  **Node Range**.****  This indicates that the number of Task nodes is fixed to 2 beyond the time range specified in the resource plan.
    3.  Click  **Configure Node Range in a Specified Time Range**  under  **Default Range**.
    4.  Configure  **Time Range**  to  **07:00-13:00**, and  **Node Range**  to  **5-5**. This indicates that the number of Task nodes is fixed to 5 in the specified time range. For details about the parameters, see  [Table 2](#table1846575414619).

        You can click  **Configure Node Range in a Specified Time Range**  to configure multiple resource plans.

6.  \(Optional\) Configure an automation script.
    1.  In  **Automation Script**  of  **Advanced Settings**, click  **Add**. The  **Automation Script**  page is displayed.

    1.  Set the following parameters:  **Name**,  **Script Path**,  **Execution Node Type**,  **Parameter**,  **Execution Time**, and  **Action upon Failure**. For details about the parameters, see  [Table 3](#table15644113520578).
    2.  Click  **OK**  to save the automation script configurations.

7.  Select  **I agree to authorize MRS to scale out or in nodes based on the above policy**.
8.  Click  **OK**.

## Using Auto Scaling Rules and Resource Plans Together<a name="section13737182014617"></a>

If the data volume is not stable and the expected fluctuation may occur, the fixed Task node range cannot guarantee that the requirements in some service scenarios are met. In this case, it is necessary to adjust the number of Task nodes based on the real-time loads and resource plans.

For example, even though the service data volume for real-time processing changes regularly from 7:00 to 13:00 every day, it is still unstable.

Assume that from five to eight Task nodes are needed from 7:00 to 13:00 and two to four Task nodes are required for other time. Therefore, you can set an auto scaling rule in addition to a resource plan. Therefore, when the data volume exceeds the expected value, the number of Task nodes can be adjusted based on the loads, without exceeding the node range specified in the resource plan. When a resource plan is triggered, the number of nodes is adjusted within the specified node range with minimum affect. That is, increase nodes to the minimum value of the node range and decrease nodes to the maximum value of the node range. Perform the following steps to configure both the auto scaling rule and the resource plan:

1.  Log in to the MRS management console.
2.  Click![](figures/dt_mrs_project_region_image01.png)in the upper left corner on the management console and select  **Region**  and  **Project**.
3.  Choose  **Clusters**  \>  **Active Clusters**, select a running cluster, and click its name to switch to the cluster details page.
4.  On the  **Nodes**  tab page, click  **Auto Scaling**  in the  **Operation**  column of the Task node group. The  **Auto Scaling**  page is displayed.
5.  Configure the auto scaling rule.

    You can configure the auto scaling rule to adjust the number of nodes, which affects the actual price. Therefore, exercise caution when performing this operation.

    -   **Auto Scaling**: indicates whether to enable auto scaling. Auto scaling is disabled by default. After you enable it, you can configure the following parameters.
    -   **Default Range**  of  **Node Range**: Enter the node range of Task nodes. This constraint applies to all cluster scale-out and scale-in rules. Set this parameter to  **2**  to  **4**.
    -   **Auto Scaling Rule**: To enable  **Auto Scaling**, configure the scale-out or scale-in rules.

        Configuration procedure:

        1.  Select  **Scale Out**  or  **Scale In.**
        2.  Click  **Add Rule**. The  **Add Rule**  page is displayed.
        3.  Configure the following parameters:  **Rule Name,** **If,** **Last,** **If,** **Cooldown Period.**
        4.  Click  **OK.**

            You can view the rules you configured in the  **Scale Out**  or  **Scale In**  area on the  **Auto Scaling**  page.


6.  Configure a resource plan.

    You can configure the resource plan to adjust the number of nodes, which affects the actual price. Therefore, exercise caution when performing this operation.

    Configuration procedure:

    1.  Click  **Configure Node Range in a Specified Time Range**  under  **Default Range**  on the  **Auto Scaling**  page.
    2.  Configure  **Time Range**  to  **07:00-13:00**  and  **Node Range**  to  **5-8**. For details about the parameters, see  [Table 2](#table1846575414619).
    3.  You can click  **Configure Node Range in a Specified Time Range**  to configure multiple resource plans.

7.  Configure automation scripts.
    1.  In  **Automation Script**  of  **Advanced Settings**, click  **Add**  The  **Automation Script**  page is displayed.

    1.  Set the following parameters:  **Name**,  **Script Path**,  **Execution Node Type**,  **Parameter**,  **Execution Time**, and  **Action upon Failure**. For details about the parameters, see  [Table 3](#table15644113520578).
    2.  Click  **OK**  to save the automation script configurations.

8.  Select  **I agree to authorize MRS to scale out or in nodes based on the above policy.**
9.  Click  **OK**

## Related Information<a name="section5517530395813"></a>

When adding rules, you can refer to  [Table 1](#table46006826145048)  to configure auto scaling metrics.

**Table  1**  Auto scaling metrics

<a name="table46006826145048"></a>
<table><thead align="left"><tr id="row28384021145048"><th class="cellrowborder" valign="top" width="15.598440155984402%" id="mcps1.2.5.1.1"><p id="p10135650103024"><a name="p10135650103024"></a><a name="p10135650103024"></a>Cluster Type</p>
</th>
<th class="cellrowborder" valign="top" width="24.437556244375564%" id="mcps1.2.5.1.2"><p id="p15681334103024"><a name="p15681334103024"></a><a name="p15681334103024"></a>Metric Name</p>
</th>
<th class="cellrowborder" valign="top" width="15.22847715228477%" id="mcps1.2.5.1.3"><p id="p62228505103024"><a name="p62228505103024"></a><a name="p62228505103024"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="44.73552644735527%" id="mcps1.2.5.1.4"><p id="p7344182103024"><a name="p7344182103024"></a><a name="p7344182103024"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row51577863171444"><td class="cellrowborder" rowspan="4" valign="top" width="15.598440155984402%" headers="mcps1.2.5.1.1 "><p id="p1016120103024"><a name="p1016120103024"></a><a name="p1016120103024"></a>Streaming cluster</p>
</td>
<td class="cellrowborder" valign="top" width="24.437556244375564%" headers="mcps1.2.5.1.2 "><p id="p15196910103024"><a name="p15196910103024"></a><a name="p15196910103024"></a>StormSlotAvailable</p>
</td>
<td class="cellrowborder" valign="top" width="15.22847715228477%" headers="mcps1.2.5.1.3 "><p id="p6406523190"><a name="p6406523190"></a><a name="p6406523190"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="44.73552644735527%" headers="mcps1.2.5.1.4 "><p id="zh-cn_topic_0094071568_p522926491510"><a name="zh-cn_topic_0094071568_p522926491510"></a><a name="zh-cn_topic_0094071568_p522926491510"></a>Number of available Storm slots</p>
<p id="a14777c8d74ff42b9aa7f911ec31f22d9"><a name="a14777c8d74ff42b9aa7f911ec31f22d9"></a><a name="a14777c8d74ff42b9aa7f911ec31f22d9"></a>Value range: 0 to 2147483647</p>
</td>
</tr>
<tr id="row40896131171444"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p7319460103024"><a name="p7319460103024"></a><a name="p7319460103024"></a>StormSlotAvailablePercentage</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p154113528199"><a name="p154113528199"></a><a name="p154113528199"></a>Percentage</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p72764414211"><a name="p72764414211"></a><a name="p72764414211"></a>Percentage of available Storm slots, that is, the proportion of available slots to total slots</p>
<p id="p18271744122117"><a name="p18271744122117"></a><a name="p18271744122117"></a>Value range: 0 to 100</p>
</td>
</tr>
<tr id="row50282427171444"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p26765346103024"><a name="p26765346103024"></a><a name="p26765346103024"></a>StormSlotUsed</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p04145271912"><a name="p04145271912"></a><a name="p04145271912"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p32734432113"><a name="p32734432113"></a><a name="p32734432113"></a>Number of the used Storm slots</p>
<p id="p172794419213"><a name="p172794419213"></a><a name="p172794419213"></a>Value range: 0 to 2147483647</p>
</td>
</tr>
<tr id="row31197485145048"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p32769415103024"><a name="p32769415103024"></a><a name="p32769415103024"></a>StormSlotUsedPercentage</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p341652161912"><a name="p341652161912"></a><a name="p341652161912"></a>Percentage</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p9277445215"><a name="p9277445215"></a><a name="p9277445215"></a>Percentage of the used Storm slots, that is, the proportion of the used slots to total slots</p>
<p id="p4278443219"><a name="p4278443219"></a><a name="p4278443219"></a>Value range: 0 to 100</p>
</td>
</tr>
<tr id="row32873277171331"><td class="cellrowborder" rowspan="14" valign="top" width="15.598440155984402%" headers="mcps1.2.5.1.1 "><p id="a21d107a499be49ba9e5a3571ad094f3c"><a name="a21d107a499be49ba9e5a3571ad094f3c"></a><a name="a21d107a499be49ba9e5a3571ad094f3c"></a>Analysis cluster</p>
</td>
<td class="cellrowborder" valign="top" width="24.437556244375564%" headers="mcps1.2.5.1.2 "><p id="p64636605103024"><a name="p64636605103024"></a><a name="p64636605103024"></a>YARNAppPending</p>
</td>
<td class="cellrowborder" valign="top" width="15.22847715228477%" headers="mcps1.2.5.1.3 "><p id="zh-cn_topic_0094071568_p190905631502"><a name="zh-cn_topic_0094071568_p190905631502"></a><a name="zh-cn_topic_0094071568_p190905631502"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="44.73552644735527%" headers="mcps1.2.5.1.4 "><p id="p527184432118"><a name="p527184432118"></a><a name="p527184432118"></a>Number of pending tasks on YARN</p>
<p id="p6271144172116"><a name="p6271144172116"></a><a name="p6271144172116"></a>Value range: 0 to 2147483647</p>
</td>
</tr>
<tr id="row3418098171331"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p62688371103024"><a name="p62688371103024"></a><a name="p62688371103024"></a>YARNAppPendingRatio</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="zh-cn_topic_0094071568_p643420251502"><a name="zh-cn_topic_0094071568_p643420251502"></a><a name="zh-cn_topic_0094071568_p643420251502"></a>Ratio</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p9271644122112"><a name="p9271644122112"></a><a name="p9271644122112"></a>Ratio of pending tasks on YARN, that is, the ratio of pending tasks to running tasks on Yarn</p>
<p id="p12784419219"><a name="p12784419219"></a><a name="p12784419219"></a>Value range: 0 to 2147483647</p>
</td>
</tr>
<tr id="row54442235171459"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p41214366103024"><a name="p41214366103024"></a><a name="p41214366103024"></a>YARNAppRunning</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="zh-cn_topic_0094071568_p314054641502"><a name="zh-cn_topic_0094071568_p314054641502"></a><a name="zh-cn_topic_0094071568_p314054641502"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p1628644162113"><a name="p1628644162113"></a><a name="p1628644162113"></a>Number of running tasks on YARN</p>
<p id="p1828134415212"><a name="p1828134415212"></a><a name="p1828134415212"></a>Value range: 0 to 2147483647</p>
</td>
</tr>
<tr id="row4374409171459"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p6215248103024"><a name="p6215248103024"></a><a name="p6215248103024"></a>YARNContainerAllocated</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="zh-cn_topic_0094071568_p461903831502"><a name="zh-cn_topic_0094071568_p461903831502"></a><a name="zh-cn_topic_0094071568_p461903831502"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p17281144172111"><a name="p17281144172111"></a><a name="p17281144172111"></a>Number of containers allocated to YARN</p>
<p id="p92854411218"><a name="p92854411218"></a><a name="p92854411218"></a>Value range: 0 to 2147483647</p>
</td>
</tr>
<tr id="row54218264171459"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p12001376103024"><a name="p12001376103024"></a><a name="p12001376103024"></a>YARNContainerPending</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="zh-cn_topic_0094071568_p335746051502"><a name="zh-cn_topic_0094071568_p335746051502"></a><a name="zh-cn_topic_0094071568_p335746051502"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p0282044182114"><a name="p0282044182114"></a><a name="p0282044182114"></a>Number of pending containers on YARN</p>
<p id="p1628114472112"><a name="p1628114472112"></a><a name="p1628114472112"></a>Value range: 0 to 2147483647</p>
</td>
</tr>
<tr id="row10447818171459"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p5014449103024"><a name="p5014449103024"></a><a name="p5014449103024"></a>YARNContainerPendingRatio</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="zh-cn_topic_0094071568_p340382961502"><a name="zh-cn_topic_0094071568_p340382961502"></a><a name="zh-cn_topic_0094071568_p340382961502"></a><span>Ratio</span></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p152812448214"><a name="p152812448214"></a><a name="p152812448214"></a>Ratio of pending containers on YARN, the ratio of pending containers to running containers on Yarn</p>
<p id="p112813442215"><a name="p112813442215"></a><a name="p112813442215"></a>Value range: 0 to 2147483647</p>
</td>
</tr>
<tr id="row63084750171459"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p54414442103024"><a name="p54414442103024"></a><a name="p54414442103024"></a>YARNCPUAllocated</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="zh-cn_topic_0094071568_p591757081502"><a name="zh-cn_topic_0094071568_p591757081502"></a><a name="zh-cn_topic_0094071568_p591757081502"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p162864410216"><a name="p162864410216"></a><a name="p162864410216"></a>Number of virtual CPUs (vCPUs) allocated to YARN</p>
<p id="p1128844162120"><a name="p1128844162120"></a><a name="p1128844162120"></a>Value range: 0 to 2147483647</p>
</td>
</tr>
<tr id="row8070279171459"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p55274302103024"><a name="p55274302103024"></a><a name="p55274302103024"></a>YARNCPUAvailable</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="zh-cn_topic_0094071568_p184875611502"><a name="zh-cn_topic_0094071568_p184875611502"></a><a name="zh-cn_topic_0094071568_p184875611502"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p16286440210"><a name="p16286440210"></a><a name="p16286440210"></a>Number of available vCPUs on YARN</p>
<p id="p15281444142117"><a name="p15281444142117"></a><a name="p15281444142117"></a>Value range: 0 to 2147483647</p>
</td>
</tr>
<tr id="row62206209171512"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p18989989103024"><a name="p18989989103024"></a><a name="p18989989103024"></a>YARNCPUAvailablePercentage</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="zh-cn_topic_0094071568_p254407301502"><a name="zh-cn_topic_0094071568_p254407301502"></a><a name="zh-cn_topic_0094071568_p254407301502"></a>Percentage</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p42854420215"><a name="p42854420215"></a><a name="p42854420215"></a>Percentage of available vCPUs on YARN, that is, the proportion of available vCPUs to total vCPUs</p>
<p id="p728204422116"><a name="p728204422116"></a><a name="p728204422116"></a>Value range: 0 to 100</p>
</td>
</tr>
<tr id="row40963897171512"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p51231776103024"><a name="p51231776103024"></a><a name="p51231776103024"></a>YARNCPUPending</p>
<p id="p58432803103024"><a name="p58432803103024"></a><a name="p58432803103024"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="zh-cn_topic_0094071568_p131951091502"><a name="zh-cn_topic_0094071568_p131951091502"></a><a name="zh-cn_topic_0094071568_p131951091502"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p183224415214"><a name="p183224415214"></a><a name="p183224415214"></a>Number of pending vCPUs on YARN</p>
<p id="p12326442216"><a name="p12326442216"></a><a name="p12326442216"></a>Value range: 0 to 2147483647</p>
</td>
</tr>
<tr id="row34017879171512"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p57910333103024"><a name="p57910333103024"></a><a name="p57910333103024"></a>YARNMemoryAllocated</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="zh-cn_topic_0094071568_p652522791502"><a name="zh-cn_topic_0094071568_p652522791502"></a><a name="zh-cn_topic_0094071568_p652522791502"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p432114412218"><a name="p432114412218"></a><a name="p432114412218"></a>Memory allocated to YARN. The unit is MB.</p>
<p id="p18326445217"><a name="p18326445217"></a><a name="p18326445217"></a>Value range: 0 to 2147483647</p>
</td>
</tr>
<tr id="row18296339171512"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p26482165103024"><a name="p26482165103024"></a><a name="p26482165103024"></a>YARNMemoryAvailable</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="zh-cn_topic_0094071568_p316230061502"><a name="zh-cn_topic_0094071568_p316230061502"></a><a name="zh-cn_topic_0094071568_p316230061502"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p532164415219"><a name="p532164415219"></a><a name="p532164415219"></a>Available memory on YARN. The unit is MB.</p>
<p id="p132124412217"><a name="p132124412217"></a><a name="p132124412217"></a>Value range: 0 to 2147483647</p>
</td>
</tr>
<tr id="row49374603171512"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p30076974103024"><a name="p30076974103024"></a><a name="p30076974103024"></a>YARNMemoryAvailablePercentage</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="zh-cn_topic_0094071568_p372944431502"><a name="zh-cn_topic_0094071568_p372944431502"></a><a name="zh-cn_topic_0094071568_p372944431502"></a>Percentage</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p1632644112116"><a name="p1632644112116"></a><a name="p1632644112116"></a>Percentage of available memory on YARN, that is, the proportion of available memory to total memory on YARN</p>
<p id="p10321144122118"><a name="p10321144122118"></a><a name="p10321144122118"></a>Value range: 0 to 100</p>
</td>
</tr>
<tr id="row14813895171512"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p33097999103024"><a name="p33097999103024"></a><a name="p33097999103024"></a>YARNMemoryPending</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="zh-cn_topic_0094071568_p569545521502"><a name="zh-cn_topic_0094071568_p569545521502"></a><a name="zh-cn_topic_0094071568_p569545521502"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p133184417219"><a name="p133184417219"></a><a name="p133184417219"></a>Pending memory on YARN</p>
<p id="p1133144192117"><a name="p1133144192117"></a><a name="p1133144192117"></a>Value range: 0 to 2147483647</p>
</td>
</tr>
</tbody>
</table>

>![](/images/icon-note.gif) **NOTE:**   
>When the value type is percentage or ratio in  [Table 1](#table46006826145048), the valid value can be accurate to percentile. The percentage metric value is a decimal value with a percent sign \(%\) removed. For example, 16.80 represents 16.80%.  

When adding a resource plan, you can refer to  [Table 2](#table1846575414619)  to set the corresponding parameters.

**Table  2**  Configuration items of a resource plan

<a name="table1846575414619"></a>
<table><thead align="left"><tr id="row5465205454613"><th class="cellrowborder" valign="top" width="22.720000000000002%" id="mcps1.2.3.1.1"><p id="p12738164611547"><a name="p12738164611547"></a><a name="p12738164611547"></a>Configuration Item</p>
</th>
<th class="cellrowborder" valign="top" width="77.28%" id="mcps1.2.3.1.2"><p id="p10738184625418"><a name="p10738184625418"></a><a name="p10738184625418"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row192519148582"><td class="cellrowborder" valign="top" width="22.720000000000002%" headers="mcps1.2.3.1.1 "><p id="p184661549465"><a name="p184661549465"></a><a name="p184661549465"></a>Time Range</p>
</td>
<td class="cellrowborder" valign="top" width="77.28%" headers="mcps1.2.3.1.2 "><p id="p358814318101"><a name="p358814318101"></a><a name="p358814318101"></a>Start time and end time of a resource plan, accurate to minutes. The parameter value ranges from 00:00 to 23:59. For example, if a resource plan starts at 8:00 and ends at 10:00 in the morning, set this parameter to <strong id="b34402582193"><a name="b34402582193"></a><a name="b34402582193"></a>08:00-10:00</strong>. The end time must be at least 30 minutes later than the start time.</p>
</td>
</tr>
<tr id="row1141151405818"><td class="cellrowborder" valign="top" width="22.720000000000002%" headers="mcps1.2.3.1.1 "><p id="p17466145474620"><a name="p17466145474620"></a><a name="p17466145474620"></a>Node Range</p>
</td>
<td class="cellrowborder" valign="top" width="77.28%" headers="mcps1.2.3.1.2 "><p id="p1068112713218"><a name="p1068112713218"></a><a name="p1068112713218"></a>The minimum and maximum number of nodes in a resource plan. The parameter value ranges from 0 to 500.</p>
<p id="p661418611116"><a name="p661418611116"></a><a name="p661418611116"></a>In the time range specified in the resource plan, if the number of Task nodes is less than the minimum number of nodes specified in the resource plan, the auto scaling function increases the number of Task nodes to the minimum value of the node range at a time. If the number of Task nodes is greater than the maximum number of nodes specified in the resource plan, the auto scaling function reduces the number of Task nodes to the maximum value of the node range at a time. The minimum number of nodes must be less than or equal to the maximum number of nodes.</p>
</td>
</tr>
</tbody>
</table>

>![](/images/icon-note.gif) **NOTE:**   
>-   When a resource plan is enabled, the  **Default Range**  parameter on the  **Auto Scaling**  page forcibly takes effect beyond the time range specified in the resource plan. For example, the  **Default Range**  is set to  **1**  to  **2**, and the time range is between  **08:00**  and  **10:00**  and node range is  **4**  to  **5**  in a resource plan. The number of Task nodes in other periods \(**0:00-8:00**  and  **10:00-23:59**\) of a day is forcibly limited to the default node range \(1 to 2\). If the number of nodes is greater than  **2**, automatic scale-in is triggered; if the number of nodes is less than  **1**, automatic scale-out is triggered.  
>-   When a resource plan is not enabled, the default node range takes effect in all time ranges. If the number of nodes is not within the default node range, the number of Task nodes is automatically increased or decreased to the default node range.  
>-   The time range cannot be overlapped among resource plans. The overlapped time range indicates that two effective resource plans exist at one time point. For example, if resource plan 1 takes effect from  **08:00**  to  **10:00**  and resource plan 2 takes effect from  **09:00**  to  **11:00**, the time range between  **09:00**  to  **10:00**  is overlapped.  
>-   Trans-day configuration for resource plans is not allowed. For example, if you want to configure a resource plan from  **23:00**  in the former day to  **01:00**  in the next day, configure two resource plans whose time ranges are  **23:00-00:00**  and  **00:00-01:00**  respectively.  

When adding an automation script, you can set related parameters by referring to  [Table 3](#table15644113520578).

**Table  3**  Configuration items of an automation script

<a name="table15644113520578"></a>
<table><thead align="left"><tr id="row064413565714"><th class="cellrowborder" valign="top" width="22.720000000000002%" id="mcps1.2.3.1.1"><p id="p10568421195610"><a name="p10568421195610"></a><a name="p10568421195610"></a>Configuration Item</p>
</th>
<th class="cellrowborder" valign="top" width="77.28%" id="mcps1.2.3.1.2"><p id="p17568182116562"><a name="p17568182116562"></a><a name="p17568182116562"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row864418357576"><td class="cellrowborder" valign="top" width="22.720000000000002%" headers="mcps1.2.3.1.1 "><p id="p11568162155619"><a name="p11568162155619"></a><a name="p11568162155619"></a>Name</p>
</td>
<td class="cellrowborder" valign="top" width="77.28%" headers="mcps1.2.3.1.2 "><p id="p15681121155611"><a name="p15681121155611"></a><a name="p15681121155611"></a>Automation script name.</p>
<p id="p175681521175610"><a name="p175681521175610"></a><a name="p175681521175610"></a>The value can contain only digits, letters, spaces, hyphens (-), and underscores (_) and cannot start with a space.</p>
<p id="p95688213569"><a name="p95688213569"></a><a name="p95688213569"></a>The value can contain a maximum of 1 to 64 characters.</p>
<div class="note" id="note145272125614"><a name="note145272125614"></a><a name="note145272125614"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p257132195615"><a name="p257132195615"></a><a name="p257132195615"></a>A name must be unique in the same cluster. You can set the same name for different clusters.</p>
</div></div>
</td>
</tr>
<tr id="row1664573505711"><td class="cellrowborder" valign="top" width="22.720000000000002%" headers="mcps1.2.3.1.1 "><p id="p13571152125613"><a name="p13571152125613"></a><a name="p13571152125613"></a>Script Path</p>
</td>
<td class="cellrowborder" valign="top" width="77.28%" headers="mcps1.2.3.1.2 "><p id="p105711521145612"><a name="p105711521145612"></a><a name="p105711521145612"></a>Script path.</p>
<p id="p1757162113569"><a name="p1757162113569"></a><a name="p1757162113569"></a>The value can be an OBS bucket path or a local VM path.</p>
<a name="ul129121753017"></a><a name="ul129121753017"></a><ul id="ul129121753017"><li>An OBS bucket path must start with <strong id="b1357182185620"><a name="b1357182185620"></a><a name="b1357182185620"></a>s3a://</strong> and end with <strong id="b057192165610"><a name="b057192165610"></a><a name="b057192165610"></a>.sh</strong>. For example, the path of the example script for installing Zeppelin is as follows: s3a://mrs-samples-bootstrap-eu-de/zeppelin/zeppelin_install.sh</li><li>A local VM path must start with a slash (/) and end with <strong id="b142391328111515"><a name="b142391328111515"></a><a name="b142391328111515"></a>.sh</strong>. For example, the path of the example script for installing Zeppelin is as follows: /opt/bootstrap/zeppelin/zeppelin_install.sh</li></ul>
</td>
</tr>
<tr id="row96451235185718"><td class="cellrowborder" valign="top" width="22.720000000000002%" headers="mcps1.2.3.1.1 "><p id="p19295152914568"><a name="p19295152914568"></a><a name="p19295152914568"></a>Execution Node Type</p>
</td>
<td class="cellrowborder" valign="top" width="77.28%" headers="mcps1.2.3.1.2 "><p id="p15324353145617"><a name="p15324353145617"></a><a name="p15324353145617"></a>Select a type of the node where the bootstrap action script is executed.</p>
<div class="note" id="note1385223393710"><a name="note1385223393710"></a><a name="note1385223393710"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul26783219257"></a><a name="ul26783219257"></a><ul id="ul26783219257"><li>If you select <strong id="b175610565714"><a name="b175610565714"></a><a name="b175610565714"></a>Master</strong> nodes, you can choose whether to run the script only on the active Master nodes by enabling or disabling the switch <a name="image16678182112518"></a><a name="image16678182112518"></a><span><img id="image16678182112518" src="figures/icon_mrs_disable_dt.png"></span>.</li><li>If you enable it, the script runs only on the active Master nodes. If you disable it, the script runs on all Master nodes. This switch is disabled by default.</li></ul>
</div></div>
</td>
</tr>
<tr id="row4645163515578"><td class="cellrowborder" valign="top" width="22.720000000000002%" headers="mcps1.2.3.1.1 "><p id="p1054761410585"><a name="p1054761410585"></a><a name="p1054761410585"></a>Parameter</p>
</td>
<td class="cellrowborder" valign="top" width="77.28%" headers="mcps1.2.3.1.2 "><p id="p20547111412589"><a name="p20547111412589"></a><a name="p20547111412589"></a>Automation script parameter.</p>
<p id="p2547114145816"><a name="p2547114145816"></a><a name="p2547114145816"></a>The following predefined variables can be imported to obtain auto scaling information:</p>
<a name="ul20469526946"></a><a name="ul20469526946"></a><ul id="ul20469526946"><li>${mrs_scale_node_num}: Number of auto scaling nodes. The value is always positive.</li><li>${mrs_scale_type}: Scale-out/in type. The value can be <strong id="b154751455812"><a name="b154751455812"></a><a name="b154751455812"></a>scale_out</strong> or <strong id="b1354719145587"><a name="b1354719145587"></a><a name="b1354719145587"></a>scale_in</strong>.</li><li>${mrs_scale_node_hostnames}: Host names of the auto scaling nodes. Use commas (,) to separate multiple host names.</li><li>${mrs_scale_node_ips}: IP address of the auto scaling nodes. Use commas (,) to separate multiple IP addresses.</li><li>${mrs_scale_rule_name}: Name of the triggered auto scaling rule. For a resource plan, this parameter is set to <strong id="b554781455816"><a name="b554781455816"></a><a name="b554781455816"></a>resource_plan</strong>.</li></ul>
</td>
</tr>
<tr id="row784105918817"><td class="cellrowborder" valign="top" width="22.720000000000002%" headers="mcps1.2.3.1.1 "><p id="p15547514145818"><a name="p15547514145818"></a><a name="p15547514145818"></a>Execution Time</p>
</td>
<td class="cellrowborder" valign="top" width="77.28%" headers="mcps1.2.3.1.2 "><p id="p1954761412589"><a name="p1954761412589"></a><a name="p1954761412589"></a>Select the execution time for the automation script.</p>
<p id="p45471114205811"><a name="p45471114205811"></a><a name="p45471114205811"></a>The following four options are supported: <strong id="b654751412581"><a name="b654751412581"></a><a name="b654751412581"></a>Before scale-out</strong>, <strong id="b16547214105812"><a name="b16547214105812"></a><a name="b16547214105812"></a>after scale-out</strong>, <strong id="b6547614105813"><a name="b6547614105813"></a><a name="b6547614105813"></a>before scale-in</strong>, and <strong id="b5547161455812"><a name="b5547161455812"></a><a name="b5547161455812"></a>after scale-in</strong>.</p>
<div class="note" id="note10385414155817"><a name="note10385414155817"></a><a name="note10385414155817"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p14549014155812"><a name="p14549014155812"></a><a name="p14549014155812"></a>Assume that the execution node includes the Task node.</p>
<a name="ul206920341113"></a><a name="ul206920341113"></a><ul id="ul206920341113"><li>The automation script executed before scale-out cannot run on the newly added Task nodes.</li><li>The automation script executed after scale-out can run on the newly added Task nodes.</li><li>The automation script executed before scale-in can run on Task nodes to be deleted.</li><li>The automation script executed after scale-in cannot run on the deleted Task nodes.</li></ul>
</div></div>
</td>
</tr>
<tr id="row764024151416"><td class="cellrowborder" valign="top" width="22.720000000000002%" headers="mcps1.2.3.1.1 "><p id="p175491514135811"><a name="p175491514135811"></a><a name="p175491514135811"></a>Action upon Failure</p>
</td>
<td class="cellrowborder" valign="top" width="77.28%" headers="mcps1.2.3.1.2 "><p id="p10549121412587"><a name="p10549121412587"></a><a name="p10549121412587"></a>Indicates whether to continue to execute subsequent scripts and scale-out/in after the script fails to be executed.</p>
<div class="note" id="note1539816141584"><a name="note1539816141584"></a><a name="note1539816141584"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul101241115164910"></a><a name="ul101241115164910"></a><ul id="ul101241115164910"><li>You are advised to set this parameter to <strong id="b17553191405812"><a name="b17553191405812"></a><a name="b17553191405812"></a>Continue</strong> in the commissioning phase so that the cluster can continue the scale-out/in operation no matter whether the script is executed successfully.</li><li>If the script fails to be executed, view the log in <strong id="b555318142584"><a name="b555318142584"></a><a name="b555318142584"></a>/var/log/Bootstrap</strong> on the cluster VM.</li><li>The scale-in operation cannot be undone. Therefore, the <strong id="b1755313146589"><a name="b1755313146589"></a><a name="b1755313146589"></a>Action upon Failure</strong> can only be set to <strong id="b955361485814"><a name="b955361485814"></a><a name="b955361485814"></a>Continue</strong>.</li></ul>
</div></div>
</td>
</tr>
</tbody>
</table>

>![](/images/icon-note.gif) **NOTE:**   
>The automation script is triggered only during auto scaling. It is not triggered when the cluster node is manually adjusted.  

