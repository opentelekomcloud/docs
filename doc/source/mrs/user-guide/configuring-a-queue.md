# Configuring a Queue<a name="EN-US_TOPIC_0125375808"></a>

## Scenario<a name="section3272361620242"></a>

On MRS Manager, you can modify queue configurations for a specific tenant.

## Prerequisites<a name="section3962351620239"></a>

A tenant associated with Yarn and allocated with dynamic resources has been added.

## Procedure<a name="section61061662030"></a>

1.  On MRS Manager, click  **Tenant**.
2.  Click the  **Dynamic Resource Plan**  tab.
3.  Click the  **Queue Configuration**  tab.
4.  In the tenant queue table, click  **Modify** in the **Operation** column of the specified  tenant queue.

    >![](/images/icon-note.gif) **NOTE:**   
    >In the tenant list on the left of the  **Tenant Management** tab, click the target tenant. In the displayed window, choose **Resource**. On the displayed page, click ![](figures/icon_mrs_clip.gif)  to open the queue configuration modification page.  

    **Table  1**  Queue configuration parameters

    <a name="table4944872120414"></a>
    <table><thead align="left"><tr id="row5801156820414"><th class="cellrowborder" valign="top" width="30.5%" id="mcps1.2.3.1.1"><p id="p131655020414"><a name="p131655020414"></a><a name="p131655020414"></a><strong id="b6420268220440"><a name="b6420268220440"></a><a name="b6420268220440"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="69.5%" id="mcps1.2.3.1.2"><p id="p3953176220414"><a name="p3953176220414"></a><a name="p3953176220414"></a><strong id="b3303478720440"><a name="b3303478720440"></a><a name="b3303478720440"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4795612120414"><td class="cellrowborder" valign="top" width="30.5%" headers="mcps1.2.3.1.1 "><p id="p5924061320414"><a name="p5924061320414"></a><a name="p5924061320414"></a><span class="parmname" id="parmname3623325518470"><a name="parmname3623325518470"></a><a name="parmname3623325518470"></a><b>Maximum Applications</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="69.5%" headers="mcps1.2.3.1.2 "><p id="p3376038220414"><a name="p3376038220414"></a><a name="p3376038220414"></a>Specifies the maximum number of applications. The value ranges from 1 to 2147483647.</p>
    </td>
    </tr>
    <tr id="row3540798720414"><td class="cellrowborder" valign="top" width="30.5%" headers="mcps1.2.3.1.1 "><p id="p4947466520414"><a name="p4947466520414"></a><a name="p4947466520414"></a><span class="parmname" id="parmname17543681184717"><a name="parmname17543681184717"></a><a name="parmname17543681184717"></a><b>Maximum AM Resource Percent</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="69.5%" headers="mcps1.2.3.1.2 "><p id="p4802492820414"><a name="p4802492820414"></a><a name="p4802492820414"></a>Specifies the maximum percentage of resources that can be used to run ApplicationMaster in a cluster. The value ranges from 0 to 1.</p>
    </td>
    </tr>
    <tr id="row2957117120414"><td class="cellrowborder" valign="top" width="30.5%" headers="mcps1.2.3.1.1 "><p id="p4645465420414"><a name="p4645465420414"></a><a name="p4645465420414"></a><span class="parmname" id="parmname26581504184738"><a name="parmname26581504184738"></a><a name="parmname26581504184738"></a><b>Minimum User Limit Percent (%)</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="69.5%" headers="mcps1.2.3.1.2 "><p id="p473060520414"><a name="p473060520414"></a><a name="p473060520414"></a>Specifies the minimum percentage of user resource usage. The value ranges from 0 to 100.</p>
    </td>
    </tr>
    <tr id="row4257544820414"><td class="cellrowborder" valign="top" width="30.5%" headers="mcps1.2.3.1.1 "><p id="p2605923320414"><a name="p2605923320414"></a><a name="p2605923320414"></a><span class="parmname" id="parmname65639907184754"><a name="parmname65639907184754"></a><a name="parmname65639907184754"></a><b>User Limit Factor</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="69.5%" headers="mcps1.2.3.1.2 "><p id="p3042309020414"><a name="p3042309020414"></a><a name="p3042309020414"></a>Specifies the limit&nbsp;factor of the maximum user resource usage. The maximum&nbsp;percentage of user resource usage&nbsp;can be&nbsp;<span id="ph3179871214444"><a name="ph3179871214444"></a><a name="ph3179871214444"></a>calculated by multiplying the limit factor with the percentage of the tenant's actual resource usage in the cluster. The minimum value is 0.</span></p>
    </td>
    </tr>
    <tr id="row537235720414"><td class="cellrowborder" valign="top" width="30.5%" headers="mcps1.2.3.1.1 "><p id="p3250779820414"><a name="p3250779820414"></a><a name="p3250779820414"></a><span class="parmname" id="parmname54064546145842"><a name="parmname54064546145842"></a><a name="parmname54064546145842"></a><b>State</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="69.5%" headers="mcps1.2.3.1.2 "><p id="p1588602020414"><a name="p1588602020414"></a><a name="p1588602020414"></a>Specifies the current status of a resource plan. The values are <span class="parmvalue" id="parmvalue57329048172143"><a name="parmvalue57329048172143"></a><a name="parmvalue57329048172143"></a><b>Running</b></span>&nbsp;<span id="ph43802728144646"><a name="ph43802728144646"></a><a name="ph43802728144646"></a>and</span>&nbsp;<span class="parmvalue" id="parmvalue46199391172143"><a name="parmvalue46199391172143"></a><a name="parmvalue46199391172143"></a><b>Stopped</b></span>.</p>
    </td>
    </tr>
    <tr id="row875645720414"><td class="cellrowborder" valign="top" width="30.5%" headers="mcps1.2.3.1.1 "><p id="p3818442920414"><a name="p3818442920414"></a><a name="p3818442920414"></a><span class="parmname" id="parmname1469397218484"><a name="parmname1469397218484"></a><a name="parmname1469397218484"></a><b>Default Resource Pool (Default Node Label Expression)</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="69.5%" headers="mcps1.2.3.1.2 "><p id="p593100820414"><a name="p593100820414"></a><a name="p593100820414"></a>Specifies the resource pool used by a queue. The default value is <span class="parmvalue" id="parmvalue3071400172143"><a name="parmvalue3071400172143"></a><a name="parmvalue3071400172143"></a><b>Default</b></span>. If you want to change the resource pool, configure the queue capacity first. For details, see&nbsp;<a href="configuring-the-queue-capacity-policy-of-a-resource-pool.md">Configuring the Queue Capacity Policy of a Resource Pool</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


