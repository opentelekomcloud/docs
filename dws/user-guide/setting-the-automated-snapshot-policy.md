# Setting the Automated Snapshot Policy<a name="dws_01_0089"></a>

This section describes how to set the automated snapshot policy for a cluster. After the automated snapshot policy is enabled, the system automatically creates snapshots based on the preset time and period.

## Setting the Automated Snapshot Policy<a name="section13594386114220"></a>

1.  Log in to the DWS management console.
2.  In the navigation tree on the left, click  **Cluster Management**.
3.  In the cluster list, click the name of the cluster that you want to view. Then click  **Snapshots**.
4.  On the  **Snapshots**  page, click the  **Automated Snapshot Status**  switch to enable the policy. The  **Snapshot Policy**  page is displayed.
    -   ![](figures/icon-button3.png)  indicates that the policy is enabled.
    -   ![](figures/icon-dws-off.jpg)  indicates that the policy is disabled \(default\).

5.  On the  **Snapshot Policy**  page, configure the following parameters:

    **Figure  1**  View of configuring the snapshot policy<a name="fig1957223555319"></a>  
    ![](figures/view-of-configuring-the-snapshot-policy.png "view-of-configuring-the-snapshot-policy")

      

    **Table  1**  Parameter description

    <a name="table1355651818416"></a>
    <table><thead align="left"><tr id="row555312181040"><th class="cellrowborder" valign="top" width="28.000000000000004%" id="mcps1.2.3.1.1"><p id="p1055313187410"><a name="p1055313187410"></a><a name="p1055313187410"></a><strong id="b84235270692541"><a name="b84235270692541"></a><a name="b84235270692541"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="72%" id="mcps1.2.3.1.2"><p id="p1755314181848"><a name="p1755314181848"></a><a name="p1755314181848"></a><strong id="b842352706181449"><a name="b842352706181449"></a><a name="b842352706181449"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row155542181842"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.3.1.1 "><p id="p04771730104018"><a name="p04771730104018"></a><a name="p04771730104018"></a>Retention Days</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.3.1.2 "><p id="p19553121817411"><a name="p19553121817411"></a><a name="p19553121817411"></a>It is used to set the retention days of the snapshots that are automatically created. The value ranges from 1 to 10 days.</p>
    <div class="note" id="note125545181345"><a name="note125545181345"></a><a name="note125545181345"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p555319181643"><a name="p555319181643"></a><a name="p555319181643"></a>You cannot delete the snapshots that are automatically created. The system automatically deletes these snapshots when their retention duration expires.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row7556518248"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.3.1.1 "><p id="p7399234124010"><a name="p7399234124010"></a><a name="p7399234124010"></a>Start Time</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.3.1.2 "><p id="p14556918545"><a name="p14556918545"></a><a name="p14556918545"></a>It is used to set the time when the automatic snapshot creation begins. The time must be set to an integer. The automatic creation task is triggered within one hour after the creation start time you set. </p>
    </td>
    </tr>
    <tr id="row35566181148"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.3.1.1 "><p id="p20322183715408"><a name="p20322183715408"></a><a name="p20322183715408"></a>Execution Period</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.3.1.2 "><p id="p9556121819416"><a name="p9556121819416"></a><a name="p9556121819416"></a>It is used to set the automatic snapshot creation cycle.</p>
    </td>
    </tr>
    </tbody>
    </table>

6.  Click  **OK**.
7.  \(Optional\) Click  **Modify Snapshot Policy**  to modify the automatic creation policy you have enabled.

