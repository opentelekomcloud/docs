# Configuring an Alarm Threshold<a name="EN-US_TOPIC_0125375295"></a>

## Scenario<a name="section49745071163727"></a>

You can configure an alarm threshold to learn the indicator health status. After  **Send Alarm** is selected, the system sends an alarm message when the monitored data reaches the alarm threshold. You can view the alarm information in **Alarms**.

## Procedure<a name="section5781253916386"></a>

1.  On MRS Manager, click  **System**.
2.  In  **Configuration**, click **Configure Alarm Threshold**  under  **Monitoring and Alarm**.
3.  Click an indicator, for example,  **CPU Usage**, and click **Create Rule**.
4.  Set the parameters for monitoring indicator rules.

    **Table  1**  Parameters for monitoring indicator rules

    <a name="table3492860016544"></a>
    <table><thead align="left"><tr id="row4462834316544"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p5812602616544"><a name="p5812602616544"></a><a name="p5812602616544"></a><strong id="b44376580165535"><a name="b44376580165535"></a><a name="b44376580165535"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p1058767416544"><a name="p1058767416544"></a><a name="p1058767416544"></a><strong id="b37733260165535"><a name="b37733260165535"></a><a name="b37733260165535"></a>Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p5229524616544"><a name="p5229524616544"></a><a name="p5229524616544"></a><strong id="b36495204165535"><a name="b36495204165535"></a><a name="b36495204165535"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row805652716544"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p4859891616544"><a name="p4859891616544"></a><a name="p4859891616544"></a><span class="parmname" id="parmname22581971183752"><a name="parmname22581971183752"></a><a name="parmname22581971183752"></a><b>Rule Name</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p4419810116544"><a name="p4419810116544"></a><a name="p4419810116544"></a>CPU_MAX (example)</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p2327646016544"><a name="p2327646016544"></a><a name="p2327646016544"></a>Specifies the rule name.</p>
    </td>
    </tr>
    <tr id="row816154816544"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p5710563616544"><a name="p5710563616544"></a><a name="p5710563616544"></a><span class="parmname" id="parmname61380221183758"><a name="parmname61380221183758"></a><a name="parmname61380221183758"></a><b>Reference Date</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p6215378016544"><a name="p6215378016544"></a><a name="p6215378016544"></a>3/18/2017 (example)</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p129142916544"><a name="p129142916544"></a><a name="p129142916544"></a>Specifies the date on which the reference indicator history is generated.</p>
    </td>
    </tr>
    <tr id="row1162286516544"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p192802216544"><a name="p192802216544"></a><a name="p192802216544"></a><span class="parmname" id="parmname352460918381"><a name="parmname352460918381"></a><a name="parmname352460918381"></a><b>Threshold Type</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><a name="ul2195207916544"></a><a name="ul2195207916544"></a><ul id="ul2195207916544"><li>Max. value</li><li>Min. value</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p4290328610122"><a name="p4290328610122"></a><a name="p4290328610122"></a>Specifies whether to use the maximum or minimum value of the indicator for setting the threshold.</p>
    <a name="ul2269900210215"></a><a name="ul2269900210215"></a><ul id="ul2269900210215"><li>If this parameter is set to <span class="parmvalue" id="parmvalue6518547310215"><a name="parmvalue6518547310215"></a><a name="parmvalue6518547310215"></a><b>Max. value</b></span>, an alarm is generated when the actual value of the indicator is greater than the threshold.</li><li>If this parameter is set to <span class="parmvalue" id="parmvalue3344748510215"><a name="parmvalue3344748510215"></a><a name="parmvalue3344748510215"></a><b>Min. value</b></span>, an alarm is generated when the actual value of the indicator is smaller than the threshold.</li></ul>
    </td>
    </tr>
    <tr id="row2214657916567"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p3834495165623"><a name="p3834495165623"></a><a name="p3834495165623"></a><span class="parmname" id="parmname2872212818387"><a name="parmname2872212818387"></a><a name="parmname2872212818387"></a><b>Alarm Severity</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><a name="ul15501458165638"></a><a name="ul15501458165638"></a><ul id="ul15501458165638"><li>Critical</li><li>Major</li><li>Minor</li><li>Warning</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p4786351116567"><a name="p4786351116567"></a><a name="p4786351116567"></a>Specifies the alarm severity.</p>
    </td>
    </tr>
    <tr id="row3690074165614"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p42583564165644"><a name="p42583564165644"></a><a name="p42583564165644"></a><span class="parmname" id="parmname57572601183820"><a name="parmname57572601183820"></a><a name="parmname57572601183820"></a><b>Time Range</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p26716660165644"><a name="p26716660165644"></a><a name="p26716660165644"></a>From 00:00 to 23:59 (example)</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p16565865165644"><a name="p16565865165644"></a><a name="p16565865165644"></a>Specifies the period in which the rule takes effect.</p>
    </td>
    </tr>
    <tr id="row10349798165611"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p64029158165644"><a name="p64029158165644"></a><a name="p64029158165644"></a><span class="parmname" id="parmname32896910183825"><a name="parmname32896910183825"></a><a name="parmname32896910183825"></a><b>Threshold</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p18979289165644"><a name="p18979289165644"></a><a name="p18979289165644"></a>80 (example)</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p60927412165644"><a name="p60927412165644"></a><a name="p60927412165644"></a>Specifies the threshold of the rule monitoring indicator.</p>
    </td>
    </tr>
    <tr id="row5057446165648"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p6999947165648"><a name="p6999947165648"></a><a name="p6999947165648"></a><span class="parmname" id="parmname12042297183829"><a name="parmname12042297183829"></a><a name="parmname12042297183829"></a><b>Date</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><a name="ul3770183216572"></a><a name="ul3770183216572"></a><ul id="ul3770183216572"><li>Workday</li><li>Weekend</li><li>Other</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p24190739165648"><a name="p24190739165648"></a><a name="p24190739165648"></a>Specifies the days when the rule takes effect.</p>
    </td>
    </tr>
    <tr id="row1894008185754"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p19196945185754"><a name="p19196945185754"></a><a name="p19196945185754"></a><span class="parmname" id="parmname17394889185810"><a name="parmname17394889185810"></a><a name="parmname17394889185810"></a><b>Add Date</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p11448711185754"><a name="p11448711185754"></a><a name="p11448711185754"></a>11/06 (example)</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p54930369185754"><a name="p54930369185754"></a><a name="p54930369185754"></a>This parameter takes effect when you set Date to Others. You can select multiple dates.</p>
    </td>
    </tr>
    </tbody>
    </table>

5.  Click  **OK**. The **Rule saved successfully**  is displayed in the upper-right corner.

    **Send Alarm** is selected by default. MRS Manager checks whether the values of monitoring indicators meet the threshold requirements. If the number of times that the values do not meet the threshold requirements during consecutive checks exceeds the value of **Trigger Count**, an alarm will be sent. The value of **Trigger Count** can be customized. **Check Period \(s\)**  specifies the interval for MRS Manager to check monitoring indicators.

6.  In the row that contains the newly added rule, click  **Apply** in the **Operation**  column. If a dialog box indicating that the rule is applied successfully is displayed in the upper-right corner, the rule is added. The icon turns green, indicating that the operation is complete. Click **Cancel** in the **Operation**  column. If a dialog box indicating that the rule is canceled successfully is displayed in the upper-right corner, the rule is canceled.

