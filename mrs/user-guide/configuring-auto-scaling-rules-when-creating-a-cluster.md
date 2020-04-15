# Configuring Auto Scaling Rules When Creating a Cluster<a name="EN-US_TOPIC_0226022033"></a>

In big data application scenarios, especially real-time data analysis and processing, the number of cluster nodes needs to be dynamically increased or decreased according to data volume changes to add or reduce resources. The auto scaling function of MRS enables clusters to be elastically scaled out or in based on cluster loads. In addition, if the data volume changes regularly every day and you want to scale out or in a cluster before the data volume changes, you can use the MRS resource plan feature \(setting a Task node range based on the time range\).

-   Auto scaling rules: You can increase or decrease Task nodes based on real-time cluster loads. Auto scaling will be triggered when the data volume changes but there may be some delay.
-   Resource plans \(setting a Task node range based on the time range\): If the data volume changes periodically, you can create resource plans to resize the cluster before the data volume changes, thereby avoiding a delay in increasing or decreasing resources.

You can configure either auto scaling rules or resource plans or both of them to trigger the auto scaling. Configuring both resource plans and auto scaling rules improves the cluster node scalability to cope with occasionally unexpected data volume peaks.

In some service scenarios, resources need to be reallocated or service logic needs to be modified after cluster scale-out or scale-in. If you manually scale out or scale in a cluster, you can log in to cluster nodes to reallocate resources or modify service logic. If you use auto scaling, MRS enables you to customize automation scripts for resource reallocation and service logic modification. Automation scripts can be executed before and after auto scaling and automatically adapt to service load changes, all of which eliminates manual operations. In addition, automation scripts can be fully customized and executed at various moments, which can meet your personalized requirements and improve auto scaling flexibility.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>You can configure auto scaling rules when creating a cluster or after a cluster has been created. This section describes how to configure auto scaling rules during cluster creation. For details about how to configure auto scaling rules after cluster creation, see  [Using Auto Scaling in a Cluster](using-auto-scaling-in-a-cluster.md).  

## Background<a name="section1635634615287"></a>

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


## Adding an Auto Scaling Rule<a name="section6330143518162"></a>

1.  Log in to the MRS management console.
2.  Click  **Create Cluster**. The  **Create Cluster**  page is displayed.
3.  In  **Cluster Node**, click  **Auto Scaling**  in the  **Operation**  column of the  **Task**  node. 
4.  Add an auto scaling rule.

    You can configure the auto scaling rule to adjust the number of nodes, which affects the actual price. Therefore, exercise caution when performing this operation.

    -   **Node Type**: Select the type of Task nodes for which an auto scaling rule is to be added. For an analysis cluster, the option is  **Analysis Task**. For a streaming cluster, the option is  **Streaming Task**. For a hybrid cluster, the options are  **Analysis Task**  and  **Streaming Task**.
    -   **Default Node Range**: Enter a Task node range, in which auto scaling is performed. This constraint applies to all scale-in and scale-out rules. The value ranges from 0 to 500.
    -   To add the auto scaling rule, perform the following operations:
        1.  In  **Type**, select  **Scale-out**  or  **Scale-in**.
        2.  Configure the  **Rule Name**,  **If**,  **Last for**,  **Add**, and  **Cooldown Period**  parameters. For details about monitoring metrics that trigger auto scaling, see  [Table 1](using-auto-scaling-in-a-cluster.md#table46006826145048).
        3.  Click  **OK**.

            You can view the added scaling rules in the  **Add Auto Scaling Rule**  area and edit or delete the rule in the  **Operation**  column.

        4.  Add more rules by clicking  **Add Auto Scaling Rule**.

5.  Click  **OK**.

    You can view the added scaling rules in the  **Add Auto Scaling Rule**  area and edit or delete the rule in the  **Operation**  column.


## Adding a Resource Plan<a name="section18694155918248"></a>

If the data volume changes regularly every day and you want to scale out or in a cluster before the data volume changes, you can create resource plans to adjust the number of Task nodes as planned in the specified time range.

For example, the service data volume for real-time processing peaks between 7:00 and 13:00 every day and is stable and low for other time. Assume that an MRS streaming cluster is used to process the service data. Between 7:00 and 13:00, five Task nodes are required for processing the peak data volume, and only two task nodes are required for other time. You can perform the following steps to configure a resource plan.

1.  Log in to the MRS management console.
2.  Click  **Create Cluster**. The  **Create Cluster**  page is displayed.
3.  In  **Cluster Node**, click  **Auto Scaling**  in the  **Operation**  column of the  **Task**  node.
4.  Add a resource plan.

    You can configure the resource plan to adjust the number of nodes, which affects the actual price. Therefore, exercise caution when performing this operation.

    -   **Node Type**: Select the type of Task nodes for which an auto scaling rule is to be added. For an analysis cluster, the option is  **Analysis Task**. For a streaming cluster, the option is  **Streaming Task**. For a hybrid cluster, the options are  **Analysis Task**  and  **Streaming Task**.
    -   **Default Node Range**: Enter a Task node range, in which auto scaling is performed. This constraint applies to all scale-in and scale-out rules. The value ranges from 0 to 500. For example, the default node range  **2-2**  indicates that the number of Task nodes is fixed to 2 except the time range specified in the resource plan.
    -   To add the resource plan, perform the following operations:
        1.  Configure the  **Time Range**  and  **Node Range**  parameters. For example, set  **Time Range**  to  **07:00-13:00**, and  **Node Range**  to  **5-5**. This indicates that the number of Task nodes is fixed to 5 in the time range specified in the resource plan. For details about the parameters, see  [Table 2](using-auto-scaling-in-a-cluster.md#table1846575414619).
        2.  Add more resource plans by clicking  **Add Resource Plan**.
        3.  Click  **OK**.

            You can view the added resource plan in the  **Auto Scaling**  area and edit or delete the plan in the  **Operation**  column.


5.  \(Optional\) Configure a bootstrap action.
    1.  On the  **Set Advanced Options**  tab page, click  **Add**  in the  **Bootstrap Action**  area. 

    1.  Configure the  **Name**,  **Script Path**,  **Parameter**,  **Execution Node**,  **Execution Time**, and  **Action upon Failure**  parameter. For details about the parameters, see  [Table 1](#table12821236132315).

        **Table  1**  Parameters

        <a name="table12821236132315"></a>
        <table><thead align="left"><tr id="en-us_topic_0173178961_row1574783017401"><th class="cellrowborder" valign="top" width="27%" id="mcps1.2.3.1.1"><p id="en-us_topic_0173178961_p1674723044017"><a name="en-us_topic_0173178961_p1674723044017"></a><a name="en-us_topic_0173178961_p1674723044017"></a>Parameter</p>
        </th>
        <th class="cellrowborder" valign="top" width="73%" id="mcps1.2.3.1.2"><p id="en-us_topic_0173178961_p15747183094010"><a name="en-us_topic_0173178961_p15747183094010"></a><a name="en-us_topic_0173178961_p15747183094010"></a><strong id="en-us_topic_0173178961_b842352706134712"><a name="en-us_topic_0173178961_b842352706134712"></a><a name="en-us_topic_0173178961_b842352706134712"></a>Description</strong></p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="en-us_topic_0173178961_row77471830174011"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0173178961_p074793014020"><a name="en-us_topic_0173178961_p074793014020"></a><a name="en-us_topic_0173178961_p074793014020"></a>Name</p>
        </td>
        <td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0173178961_p15747133015400"><a name="en-us_topic_0173178961_p15747133015400"></a><a name="en-us_topic_0173178961_p15747133015400"></a>Name of a bootstrap action script</p>
        <p id="en-us_topic_0173178961_p11747230104016"><a name="en-us_topic_0173178961_p11747230104016"></a><a name="en-us_topic_0173178961_p11747230104016"></a>The value can contain only digits, letters, spaces, hyphens (-), and underscores (_) and cannot start with a space.</p>
        <p id="en-us_topic_0173178961_p2074714304407"><a name="en-us_topic_0173178961_p2074714304407"></a><a name="en-us_topic_0173178961_p2074714304407"></a>The value can contain 1 to 64 characters.</p>
        <div class="note" id="en-us_topic_0173178961_note874733015401"><a name="en-us_topic_0173178961_note874733015401"></a><a name="en-us_topic_0173178961_note874733015401"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0173178961_p57475301403"><a name="en-us_topic_0173178961_p57475301403"></a><a name="en-us_topic_0173178961_p57475301403"></a>A name must be unique in the same cluster. You can set the same name for different clusters.</p>
        </div></div>
        </td>
        </tr>
        <tr id="en-us_topic_0173178961_row374783034013"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0173178961_p117472303401"><a name="en-us_topic_0173178961_p117472303401"></a><a name="en-us_topic_0173178961_p117472303401"></a>Script Path</p>
        </td>
        <td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0173178961_p27472030104010"><a name="en-us_topic_0173178961_p27472030104010"></a><a name="en-us_topic_0173178961_p27472030104010"></a>Script path. The value can be an OBS bucket path or a local VM path.</p>
        <a name="en-us_topic_0173178961_ul107475303406"></a><a name="en-us_topic_0173178961_ul107475303406"></a><ul id="en-us_topic_0173178961_ul107475303406"><li>An OBS bucket path must start with <strong id="en-us_topic_0173178961_b842352706112621"><a name="en-us_topic_0173178961_b842352706112621"></a><a name="en-us_topic_0173178961_b842352706112621"></a>s3a://</strong> and end with <strong id="en-us_topic_0173178961_b842352706112629"><a name="en-us_topic_0173178961_b842352706112629"></a><a name="en-us_topic_0173178961_b842352706112629"></a>.sh</strong>. For example, the path of the example script for installing Zeppelin is as follows: s3a://mrs-samples-bootstrap-eu-de/zeppelin/zeppelin_install.sh</li><li>A local VM path must start with a slash (/) and end with <strong id="en-us_topic_0173178961_b842352706112916"><a name="en-us_topic_0173178961_b842352706112916"></a><a name="en-us_topic_0173178961_b842352706112916"></a>.sh</strong>. For example, the path of the example script for installing Zeppelin is as follows: /opt/bootstrap/zeppelin/zeppelin_install.sh</li></ul>
        </td>
        </tr>
        <tr id="en-us_topic_0173178961_row274823064014"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0173178961_p8748183014016"><a name="en-us_topic_0173178961_p8748183014016"></a><a name="en-us_topic_0173178961_p8748183014016"></a>Execution Node</p>
        </td>
        <td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0173178961_p474833019404"><a name="en-us_topic_0173178961_p474833019404"></a><a name="en-us_topic_0173178961_p474833019404"></a>Select a type of the node where the bootstrap action script is executed.</p>
        <div class="note" id="en-us_topic_0173178961_note4748530114019"><a name="en-us_topic_0173178961_note4748530114019"></a><a name="en-us_topic_0173178961_note4748530114019"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="en-us_topic_0173178961_ul7461220103311"></a><a name="en-us_topic_0173178961_ul7461220103311"></a><ul id="en-us_topic_0173178961_ul7461220103311"><li>If you select <strong id="en-us_topic_0173178961_b842352706113232"><a name="en-us_topic_0173178961_b842352706113232"></a><a name="en-us_topic_0173178961_b842352706113232"></a>Master</strong>, you can choose whether to run the script only on the active Master nodes by enabling or disabling the switch <a name="en-us_topic_0173178961_image188871133428"></a><a name="en-us_topic_0173178961_image188871133428"></a><span><img id="en-us_topic_0173178961_image188871133428" src="figures/icon_mrs_disable_hec.png"></span>.</li><li>If you enable it, the script runs only on the active Master nodes. If you disable it, the script runs on all Master nodes. This switch is disabled by default.</li></ul>
        </div></div>
        </td>
        </tr>
        <tr id="en-us_topic_0173178961_row27481330124012"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0173178961_p3748103011406"><a name="en-us_topic_0173178961_p3748103011406"></a><a name="en-us_topic_0173178961_p3748103011406"></a>Parameters</p>
        </td>
        <td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0173178961_p1748530194020"><a name="en-us_topic_0173178961_p1748530194020"></a><a name="en-us_topic_0173178961_p1748530194020"></a>Bootstrap action script parameters</p>
        </td>
        </tr>
        <tr id="en-us_topic_0173178961_row15749153054013"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0173178961_p4748133094012"><a name="en-us_topic_0173178961_p4748133094012"></a><a name="en-us_topic_0173178961_p4748133094012"></a>Execution Time</p>
        </td>
        <td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0173178961_p672101713338"><a name="en-us_topic_0173178961_p672101713338"></a><a name="en-us_topic_0173178961_p672101713338"></a>Select the time when the bootstrap action script is executed. Currently, the following two options are available: <strong id="en-us_topic_0173178961_b842352706114015"><a name="en-us_topic_0173178961_b842352706114015"></a><a name="en-us_topic_0173178961_b842352706114015"></a>Before component start</strong> and <strong id="en-us_topic_0173178961_b842352706114018"><a name="en-us_topic_0173178961_b842352706114018"></a><a name="en-us_topic_0173178961_b842352706114018"></a>After component start</strong></p>
        </td>
        </tr>
        <tr id="en-us_topic_0173178961_row474917307402"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0173178961_p197493309403"><a name="en-us_topic_0173178961_p197493309403"></a><a name="en-us_topic_0173178961_p197493309403"></a>Action upon Failure</p>
        </td>
        <td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.3.1.2 "><div class="p" id="en-us_topic_0173178961_p1974915300402"><a name="en-us_topic_0173178961_p1974915300402"></a><a name="en-us_topic_0173178961_p1974915300402"></a>Whether to continue to execute subsequent scripts and create a cluster after the script fails to be executed.<div class="note" id="en-us_topic_0173178961_note4749183094012"><a name="en-us_topic_0173178961_note4749183094012"></a><a name="en-us_topic_0173178961_note4749183094012"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0173178961_p147496308407"><a name="en-us_topic_0173178961_p147496308407"></a><a name="en-us_topic_0173178961_p147496308407"></a>You are advised to set this parameter to <strong id="en-us_topic_0173178961_b842352706114220"><a name="en-us_topic_0173178961_b842352706114220"></a><a name="en-us_topic_0173178961_b842352706114220"></a>Continue</strong> in the debugging phase so that the cluster can continue to be installed and started no matter whether the bootstrap action is successful.</p>
        </div></div>
        </div>
        </td>
        </tr>
        </tbody>
        </table>

    2.  Click  **OK**  to save the bootstrap action.


