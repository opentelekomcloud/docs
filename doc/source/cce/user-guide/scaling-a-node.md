# Scaling a Node<a name="cce_01_0209"></a>

This section describes how to scale in or out CCE cluster nodes.

## Prerequisites<a name="section194973810277"></a>

Before using the node scaling function, you must install the  [autoscaler](autoscaler.md)  add-on of v1.13.8 or later.

## Procedure<a name="section81948308420"></a>

1.  Log in to the CCE console. In the navigation pane on the left, choose  **Auto Scaling**. On the  **Node Scaling**  tab page, check whether the  [autoscaler](autoscaler.md)  add-on has been installed and is running properly.
2.  After installing the autoscaler add-on, click  **Create Node Scaling Policy**.
3.  On the  **Create Node Scaling Policy**  page, set policy parameters listed in  [Table 1](#table8638121213265).

    **Table  1**  Node scaling policy parameters

    <a name="table8638121213265"></a>
    <table><thead align="left"><tr id="row10638181262612"><th class="cellrowborder" valign="top" width="20.02%" id="mcps1.2.3.1.1"><p id="p1063821214265"><a name="p1063821214265"></a><a name="p1063821214265"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="79.97999999999999%" id="mcps1.2.3.1.2"><p id="p1638181232617"><a name="p1638181232617"></a><a name="p1638181232617"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1922964644615"><td class="cellrowborder" valign="top" width="20.02%" headers="mcps1.2.3.1.1 "><p id="p9231104613468"><a name="p9231104613468"></a><a name="p9231104613468"></a>Policy Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="79.97999999999999%" headers="mcps1.2.3.1.2 "><p id="p285719544104"><a name="p285719544104"></a><a name="p285719544104"></a>Name of the policy to be created. Set this parameter as required.</p>
    </td>
    </tr>
    <tr id="row42961494311"><td class="cellrowborder" valign="top" width="20.02%" headers="mcps1.2.3.1.1 "><p id="p2714182116117"><a name="p2714182116117"></a><a name="p2714182116117"></a>Associated Node Pool</p>
    </td>
    <td class="cellrowborder" valign="top" width="79.97999999999999%" headers="mcps1.2.3.1.2 "><p id="p189054447531"><a name="p189054447531"></a><a name="p189054447531"></a>Add a node pool. You can associate multiple node pools to use the same scaling policy.</p>
    </td>
    </tr>
    <tr id="row572593234714"><td class="cellrowborder" valign="top" width="20.02%" headers="mcps1.2.3.1.1 "><p id="p14725432104718"><a name="p14725432104718"></a><a name="p14725432104718"></a>Execution Rules</p>
    </td>
    <td class="cellrowborder" valign="top" width="79.97999999999999%" headers="mcps1.2.3.1.2 "><p id="p14777027105419"><a name="p14777027105419"></a><a name="p14777027105419"></a>Click <span class="uicontrol" id="uicontrol68881357514"><a name="uicontrol68881357514"></a><a name="uicontrol68881357514"></a><b>Add Rule</b></span>. In the <span class="uicontrol" id="uicontrol126941857125118"><a name="uicontrol126941857125118"></a><a name="uicontrol126941857125118"></a><b>Add Rule</b></span> dialog box displayed, set the following parameters:</p>
    <p id="p661454207"><a name="p661454207"></a><a name="p661454207"></a><span class="parmname" id="parmname2088601185216"><a name="parmname2088601185216"></a><a name="parmname2088601185216"></a><b>Rule Name</b></span>: Enter a custom rule name.</p>
    <p id="p2614341704"><a name="p2614341704"></a><a name="p2614341704"></a><span class="parmname" id="parmname24217373528"><a name="parmname24217373528"></a><a name="parmname24217373528"></a><b>Type</b></span>: You can select <span class="parmvalue" id="parmvalue2828155016525"><a name="parmvalue2828155016525"></a><a name="parmvalue2828155016525"></a><b>Metric-based</b></span> or <span class="parmvalue" id="parmvalue17444653115218"><a name="parmvalue17444653115218"></a><a name="parmvalue17444653115218"></a><b>Scheduled</b></span>. The differences between the two types are as follows:</p>
    <a name="ul56611653205511"></a><a name="ul56611653205511"></a><ul id="ul56611653205511"><li><strong id="b1598011319536"><a name="b1598011319536"></a><a name="b1598011319536"></a>Metric-based</strong>:<a name="ul1350972245920"></a><a name="ul1350972245920"></a><ul id="ul1350972245920"><li><span class="parmname" id="parmname12806202418537"><a name="parmname12806202418537"></a><a name="parmname12806202418537"></a><b>Condition</b></span>: Select <span class="parmvalue" id="parmvalue244593535311"><a name="parmvalue244593535311"></a><a name="parmvalue244593535311"></a><b>CPU usage</b></span> or <span class="parmvalue" id="parmvalue07313395537"><a name="parmvalue07313395537"></a><a name="parmvalue07313395537"></a><b>Memory usage</b></span> and enter a value. The value must be greater than the scale-in percentage configured in the autoscaler add-on.</li><li><span class="parmname" id="parmname835314140542"><a name="parmname835314140542"></a><a name="parmname835314140542"></a><b>Action</b></span>: Set an action to be taken when the trigger condition is met. As shown in <a href="#fig1083019104112">Figure 1</a>, five pods will be added when the memory usage exceeds 40%.</li></ul>
    </li><li><strong id="b98364237211"><a name="b98364237211"></a><a name="b98364237211"></a>Scheduled</strong>:<a name="ul102271758646"></a><a name="ul102271758646"></a><ul id="ul102271758646"><li><span class="parmname" id="parmname199851147221"><a name="parmname199851147221"></a><a name="parmname199851147221"></a><b>Periodic Triggering</b></span>: Select <span class="parmvalue" id="parmvalue163131580210"><a name="parmvalue163131580210"></a><a name="parmvalue163131580210"></a><b>Yes</b></span> or <span class="parmvalue" id="parmvalue5416711318"><a name="parmvalue5416711318"></a><a name="parmvalue5416711318"></a><b>No</b></span>.</li><li><span class="parmname" id="parmname10402112252"><a name="parmname10402112252"></a><a name="parmname10402112252"></a><b>Triggered At</b></span>: The value option is decided by <span class="parmname" id="parmname133114101561"><a name="parmname133114101561"></a><a name="parmname133114101561"></a><b>Periodic Triggering</b></span>. If <span class="parmname" id="parmname1195885814616"><a name="parmname1195885814616"></a><a name="parmname1195885814616"></a><b>Periodic Triggering</b></span> is set to <span class="parmvalue" id="parmvalue149161641715"><a name="parmvalue149161641715"></a><a name="parmvalue149161641715"></a><b>Yes</b></span>, you can set <span class="parmname" id="parmname119685581177"><a name="parmname119685581177"></a><a name="parmname119685581177"></a><b>Triggered At</b></span> to a specific time point every day, every week, or every month. The configuration in <a href="#fig15641103912113">Figure 2</a> indicates that the rule will be triggered at 15:00 every day. If you select <span class="parmvalue" id="parmvalue655693781015"><a name="parmvalue655693781015"></a><a name="parmvalue655693781015"></a><b>No</b></span> for <span class="parmname" id="parmname1864114471012"><a name="parmname1864114471012"></a><a name="parmname1864114471012"></a><b>Periodic Triggering</b></span>, you can set <span class="parmname" id="parmname1723815811017"><a name="parmname1723815811017"></a><a name="parmname1723815811017"></a><b>Triggered At</b></span> to a specific time point on a certain day in a certain month. The configuration in <a href="#fig1426162312211">Figure 3</a>indicates that the task is triggered at 15:00 on March 6 every year.</li><li><span class="parmname" id="parmname53781332141"><a name="parmname53781332141"></a><a name="parmname53781332141"></a><b>Action</b></span>: Set an action to be taken when the <span class="parmname" id="parmname1086392821616"><a name="parmname1086392821616"></a><a name="parmname1086392821616"></a><b>Triggered At</b></span> value is reached. As shown in <a href="#fig33041138310">Figure 4</a>, five pods will be added at 15:00 every day.</li></ul>
    </li></ul>
    <p id="p162368519564"><a name="p162368519564"></a><a name="p162368519564"></a>You can click <strong id="b39038611617"><a name="b39038611617"></a><a name="b39038611617"></a>Add Rule</strong> again to add more node scaling policies. You can add a maximum of one CPU usage-based rule and one memory usage-based rule. The total number of rules cannot exceed 10.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Figure  1**  Action to be taken when a metric-based condition is met<a name="fig1083019104112"></a>  
    ![](figures/action-to-be-taken-when-a-metric-based-condition-is-met.png "action-to-be-taken-when-a-metric-based-condition-is-met")

    **Figure  2**  Periodic Triggering \(Yes\)<a name="fig15641103912113"></a>  
    ![](figures/periodic-triggering-(yes).png "periodic-triggering-(yes)")

    **Figure  3**  Periodic Triggering \(No\)<a name="fig1426162312211"></a>  
    ![](figures/periodic-triggering-(no).png "periodic-triggering-(no)")

    **Figure  4**  Action to be taken when a scheduled condition is met<a name="fig33041138310"></a>  
    ![](figures/action-to-be-taken-when-a-scheduled-condition-is-met.png "action-to-be-taken-when-a-scheduled-condition-is-met")

4.  After the configuration is complete, click  **Create Now**. The  **Node Scaling**  page is displayed. You can view the created policy in the list.

## Deleting a Node Scaling Policy<a name="section12412142815127"></a>

1.  Log in to the CCE console. In the navigation pane, choose  **Auto Scaling**. On the  **Node Scaling**  tab page, click  **Delete**  in the  **Operation**  column of the policy to be deleted.
2.  In the  **Delete Node Policy**  dialog box displayed, confirm whether to delete the policy.
3.  Enter  **DELETE**  in the text box.
4.  Click  **OK**  to delete the policy.

## Editing a Node Scaling Policy<a name="section1811041171219"></a>

1.  Log in to the CCE console. In the navigation pane, choose  **Auto Scaling**. On the  **Node Scaling**  tab page, click  **Edit**  in the  **Operation**  column of the policy to be edited.
2.  On the  **Create Node Scaling Policy**  page displayed, modify policy parameters listed in  [Table 1](#table8638121213265).
3.  After the configuration is complete, click  **OK**.

## Cloning a Node Scaling Policy<a name="section12876105120126"></a>

1.  Log in to the CCE console. In the navigation pane, choose  **Auto Scaling**. On the  **Node Scaling**  tab page, click  **More**  \>  **Clone**  in the  **Operation**  column of the policy to be cloned.
2.  On the  **Create Node Scaling Policy**  page displayed, some parameters have been cloned. Add or modify other policy parameters based on service requirements.
3.  Click  **Create Now**  to clone the policy. The cloned policy is displayed in the policy list on the  **Node Scaling**  tab page.

## Enabling or Disabling a Node Scaling Policy<a name="section2151186136"></a>

1.  Log in to the CCE console. In the navigation pane, choose  **Auto Scaling**. On the  **Node Scaling**  tab page, click  **More**  \>  **Disable**  or  **Enable**  in the  **Operation**  column of the policy.
2.  In the dialog box displayed, confirm whether to disable or enable the node policy.
3.  Click  **OK**. The policy status is displayed in the node scaling list.

## Viewing a Node Scaling Policy<a name="section1819811305414"></a>

You can view the associated node pool, rules, and scaling history of a node scaling policy and rectify faults according to the error information displayed.

1.  Log in to the CCE console. In the navigation pane, choose  **Auto Scaling**. On the  **Node Scaling**  tab page, click  ![](figures/icon-monitoring-12.png)  in front of the policy to be viewed.
2.  In the expanded area, the  **Associated Node Pool**,  **Execution Rules**, and  **Scaling Records**  tab pages are displayed. If the policy is abnormal, locate and rectify the fault based on the error information.

    >![](/images/icon-note.gif) **NOTE:** 
    >You can also enable or disable auto scaling in  **Node Pool Management**. Log in to the CCE console. In the navigation pane, choose  **Resource Management**  \>  **Node Pools**, and click  **Edit**  in the upper right corner of the node pool to be operated. In the  **Edit Node Pool**  dialog box displayed, you can enable  **Autoscaler**  and set the limits of the number of nodes and the cooling interval for auto scaling.


