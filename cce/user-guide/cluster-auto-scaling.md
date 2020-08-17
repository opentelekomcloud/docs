# Cluster Auto Scaling<a name="cce_01_0157"></a>

The Cluster Auto Scaling feature allows CCE to automatically  scale out  a cluster \(add nodes to a cluster\) according to custom scale-up policies when workloads cannot be scheduled into the cluster due to insufficient cluster resources.

>![](public_sys-resources/icon-note.gif) **NOTE:** 
>-   Currently, master nodes cannot be automatically added to or removed from clusters.
>-   The Cluster Auto Scaling feature does not provide auto scale-down. You have to manually downsize a cluster based on resource usage.
>-   If both auto scale-up and auto scale-down are required, use the autoscaler add-on. For details, see  [autoscaler](autoscaler.md).

## Automatic Cluster Scaling-up<a name="section203712516160"></a>

1.  Log in to the CCE console. In the navigation pane, choose  **Resource Management**  \>  **Clusters**. In the card view of the cluster that needs auto scale-up, choose  **More**  \>  **Auto Scaling**.
2.  Click the  **Scale-out Settings**  tab and then  **Edit**. Set the maximum number of nodes, minimum number of nodes, cooldown period, and node configuration.

    **Table  1**  scale-up settings

    <a name="table6133357316271"></a>
    <table><thead align="left"><tr id="row6495428016271"><th class="cellrowborder" valign="top" width="26%" id="mcps1.2.3.1.1"><p id="p3992130816271"><a name="p3992130816271"></a><a name="p3992130816271"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="74%" id="mcps1.2.3.1.2"><p id="p1240055416271"><a name="p1240055416271"></a><a name="p1240055416271"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row264735262215"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p9762105862216"><a name="p9762105862216"></a><a name="p9762105862216"></a><span class="keyword" id="keyword166813866311444"><a name="keyword166813866311444"></a><a name="keyword166813866311444"></a>Cooldown Period</span></p>
    </td>
    <td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p id="p1776217589220"><a name="p1776217589220"></a><a name="p1776217589220"></a>Interval between consecutive scale-up operations, in the unit of second. The cooldown period ensures that a scale-up operation is initiated only when previous scaling operation is finished and the system is running stably.</p>
    <p id="p157621158192219"><a name="p157621158192219"></a><a name="p157621158192219"></a>The value ranges from 60 seconds to 3600 seconds. The default value is 900 seconds. If the value is less than 900 seconds, scale-up may not meet your expectation.</p>
    </td>
    </tr>
    <tr id="row559783816271"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p5077174216271"><a name="p5077174216271"></a><a name="p5077174216271"></a><span class="keyword" id="keyword263400725114141"><a name="keyword263400725114141"></a><a name="keyword263400725114141"></a>Maximum Nodes</span></p>
    </td>
    <td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p id="p12732340142311"><a name="p12732340142311"></a><a name="p12732340142311"></a>Maximum number of nodes to which the cluster can scale up.</p>
    <p id="p2079863914242"><a name="p2079863914242"></a><a name="p2079863914242"></a>1 ≤ Maximum Nodes &lt; cluster node quota</p>
    <div class="note" id="note93741436192516"><a name="note93741436192516"></a><a name="note93741436192516"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p183751136192514"><a name="p183751136192514"></a><a name="p183751136192514"></a>The cluster node quota depends on the cluster size (maximum number of nodes that can be managed by a cluster) and the node quota of the account. The cluster node quota used here is the smaller of the two.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row3382856916271"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p5575960016271"><a name="p5575960016271"></a><a name="p5575960016271"></a>Node Configuration</p>
    </td>
    <td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p id="p36381708171221"><a name="p36381708171221"></a><a name="p36381708171221"></a>If scale-up is required after the scale-up policy is executed, the system creates a node.</p>
    <a name="ol62317823171235"></a><a name="ol62317823171235"></a><ol id="ol62317823171235"><li>Click <strong id="b842352706101636"><a name="b842352706101636"></a><a name="b842352706101636"></a>Set</strong> and set the node parameters. For details about how to set the node parameters, see <a href="creating-a-node.md#li8652222123119">2</a>.</li><li>Click <strong id="b842352706115552"><a name="b842352706115552"></a><a name="b842352706115552"></a>Now Config</strong>.</li></ol>
    </td>
    </tr>
    </tbody>
    </table>

3.  After confirming the scale-up configuration and node parameters, click  **OK**.
4.  Set the scale-up policy for the cluster. Click the  **Scaling-out Policies**  tab and click  **Add Policy**.
    -   Policy Name: Enter a policy name, for example,  **policy01**.
    -   Set  **Policy Type**. Currently, the following types of auto scale-up policies are supported:
        -   [Metric-based Policy](#table23209107191540): scale-up based on the CPU or memory settings

            **Table  2**  Parameters for adding a metric-based policy

            <a name="table23209107191540"></a>
            <table><thead align="left"><tr id="row64542335191540"><th class="cellrowborder" valign="top" width="26%" id="mcps1.2.3.1.1"><p id="p60546633191540"><a name="p60546633191540"></a><a name="p60546633191540"></a>Parameter</p>
            </th>
            <th class="cellrowborder" valign="top" width="74%" id="mcps1.2.3.1.2"><p id="p5330260191540"><a name="p5330260191540"></a><a name="p5330260191540"></a>Description</p>
            </th>
            </tr>
            </thead>
            <tbody><tr id="row29097928191540"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p8121931191540"><a name="p8121931191540"></a><a name="p8121931191540"></a>* Metric</p>
            </td>
            <td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p id="p53896712191540"><a name="p53896712191540"></a><a name="p53896712191540"></a>Select <strong id="b842352706105845"><a name="b842352706105845"></a><a name="b842352706105845"></a>Allocated CPU</strong> or <strong id="b842352706105849"><a name="b842352706105849"></a><a name="b842352706105849"></a>Allocated memory</strong>.</p>
            </td>
            </tr>
            <tr id="row32017871191540"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p43310752191540"><a name="p43310752191540"></a><a name="p43310752191540"></a>* Trigger Condition</p>
            </td>
            <td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p id="p18509989191540"><a name="p18509989191540"></a><a name="p18509989191540"></a>Set a condition for triggering a scale-up policy, that is, when the average CPU or memory allocation value is greater than or less than a specified percentage.</p>
            </td>
            </tr>
            <tr id="row32372174191540"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p4900477191540"><a name="p4900477191540"></a><a name="p4900477191540"></a>* Monitoring window</p>
            </td>
            <td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p id="p61394389191540"><a name="p61394389191540"></a><a name="p61394389191540"></a>Duration for which the metric is measured. Select a value from the drop-down list.</p>
            <p id="p15678591191540"><a name="p15678591191540"></a><a name="p15678591191540"></a>If you select <strong id="b8423527061147"><a name="b8423527061147"></a><a name="b8423527061147"></a>15min</strong>, the selected metric is measured every 15 minutes.</p>
            </td>
            </tr>
            <tr id="row6889597191540"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p21186461191540"><a name="p21186461191540"></a><a name="p21186461191540"></a>* <span id="ph4802843152619"><a name="ph4802843152619"></a><a name="ph4802843152619"></a>Threshold Crossings</span></p>
            </td>
            <td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p id="p38381790191540"><a name="p38381790191540"></a><a name="p38381790191540"></a>If you set this parameter to <strong id="b84235270617847"><a name="b84235270617847"></a><a name="b84235270617847"></a>3</strong>, the action is triggered if the metrics meet the specified threshold for three consecutive times.</p>
            </td>
            </tr>
            <tr id="row9891794191540"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p63037863191540"><a name="p63037863191540"></a><a name="p63037863191540"></a>* Action</p>
            </td>
            <td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p id="p5793264191540"><a name="p5793264191540"></a><a name="p5793264191540"></a>Action executed after a policy is triggered.</p>
            </td>
            </tr>
            </tbody>
            </table>

        -   [Scheduled Policy](#table62540231191540): scale-up at a specified time

            **Table  3**  Parameters for adding a scheduled policy

            <a name="table62540231191540"></a>
            <table><thead align="left"><tr id="row39885138191540"><th class="cellrowborder" valign="top" width="26%" id="mcps1.2.3.1.1"><p id="p9470775191540"><a name="p9470775191540"></a><a name="p9470775191540"></a>Parameter</p>
            </th>
            <th class="cellrowborder" valign="top" width="74%" id="mcps1.2.3.1.2"><p id="p28935333191540"><a name="p28935333191540"></a><a name="p28935333191540"></a>Description</p>
            </th>
            </tr>
            </thead>
            <tbody><tr id="row3287219191540"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p64938190191540"><a name="p64938190191540"></a><a name="p64938190191540"></a>* Policy Type</p>
            </td>
            <td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p id="p25502013191540"><a name="p25502013191540"></a><a name="p25502013191540"></a>Set this parameter to <strong id="b842352706171841"><a name="b842352706171841"></a><a name="b842352706171841"></a>Scheduled <span id="ph1086491242715"><a name="ph1086491242715"></a><a name="ph1086491242715"></a>p</span>olicy</strong>.</p>
            </td>
            </tr>
            <tr id="row28191528191540"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p1812401191540"><a name="p1812401191540"></a><a name="p1812401191540"></a>* Trigger Time</p>
            </td>
            <td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p id="p12586754191540"><a name="p12586754191540"></a><a name="p12586754191540"></a>Time at which the policy is triggered.</p>
            </td>
            </tr>
            <tr id="row46171925191540"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p48938470191540"><a name="p48938470191540"></a><a name="p48938470191540"></a>* Action</p>
            </td>
            <td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p id="p4593172191540"><a name="p4593172191540"></a><a name="p4593172191540"></a>Action executed after a policy is triggered.</p>
            </td>
            </tr>
            </tbody>
            </table>

        -   [Periodic Policy](#table60088509191540): The scale-up policy can be performed by day, week, or month.

            **Table  4**  Parameters for adding a periodic policy

            <a name="table60088509191540"></a>
            <table><thead align="left"><tr id="row12838474191540"><th class="cellrowborder" valign="top" width="26%" id="mcps1.2.3.1.1"><p id="p33283455191540"><a name="p33283455191540"></a><a name="p33283455191540"></a>Parameter</p>
            </th>
            <th class="cellrowborder" valign="top" width="74%" id="mcps1.2.3.1.2"><p id="p11605349191540"><a name="p11605349191540"></a><a name="p11605349191540"></a>Description</p>
            </th>
            </tr>
            </thead>
            <tbody><tr id="row4159900191540"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p1407635191540"><a name="p1407635191540"></a><a name="p1407635191540"></a>* Policy Type</p>
            </td>
            <td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p id="p46909639191540"><a name="p46909639191540"></a><a name="p46909639191540"></a>Set the parameter to <strong id="b1788560206172133"><a name="b1788560206172133"></a><a name="b1788560206172133"></a>Periodic <span id="ph45621166272"><a name="ph45621166272"></a><a name="ph45621166272"></a>p</span>olicy</strong>.</p>
            </td>
            </tr>
            <tr id="row19533571191540"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p38715420191540"><a name="p38715420191540"></a><a name="p38715420191540"></a>* Time Range</p>
            </td>
            <td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p id="p48941350191540"><a name="p48941350191540"></a><a name="p48941350191540"></a>Specify the time for triggering the policy.</p>
            </td>
            </tr>
            <tr id="row37818973191540"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p43437971191540"><a name="p43437971191540"></a><a name="p43437971191540"></a>* Action</p>
            </td>
            <td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p id="p28814733191540"><a name="p28814733191540"></a><a name="p28814733191540"></a>Action executed after a policy is triggered.</p>
            </td>
            </tr>
            </tbody>
            </table>


5.  Click  **OK**.

    After the auto scale-up is completed, choose  **Resource Management \> Nodes**  in the navigation pane. On the node list, you can view the nodes added during cluster auto scaling.


