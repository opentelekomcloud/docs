# Scaling a Workload<a name="cce_01_0057"></a>

After  scaling policies  are defined, instances can be automatically added or deleted based on resource changes, fixed time, and fixed periods. This reduces manual resource adjustment to cope with service changes and peak pressure, helping you save resources and labor costs.

-   **Auto Scaling**: includes alarm, scheduled, and periodic policies. This mode automatically scales in or out instances on a workload based on resource usage, scheduled time, or specified periods.
-   **Manual Scaling**: Manually scale in or out instances on a workload immediately after the workload is created.
-   **Maximum Number of Unavailable Pods**: maximum number of unavailable pods allowed in a rolling upgrade. If the number is equal to the total number of pods, services may be interrupted. Minimum number of alive pods = Total pods – Maximum number of unavailable pods.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If  **Maximum Number of Unavailable Pods**  is set to  **0**  when there is only one pod in the cluster, services will be interrupted during scaling.  


## Auto Scaling<a name="section1656965814562"></a>

You can define custom auto scaling policies, eliminating the need to repeatedly adjust resources as service load fluctuates.

Currently, CCE supports the following types of auto scaling policies:

[Metric-based policy](#li16804196913): After a workload is created, pods will be automatically scaled when the workload's CPU or memory usage exceeds or falls below a preset limit.

[Scheduled policy](#li1595211281895): scaling at a specified time. Scheduled auto scaling is applicable flash sales, premier shopping events, and other regular events that bring a high burst of traffic load.

[Periodic policy](#li35861531491): scaling at a specified time on a daily, weekly, or monthly basis. Periodic scheduling is applicable to scenarios where traffic changes periodically.

-   <a name="li16804196913"></a>**Metric-based policy**: Supports automatic scaling of workload based on the setting of the CPU/memory.
    1.  Log in to the CCE console. In the navigation pane, choose  **Workloads**  \>  **Deployments**  or  **StatefulSet**. In the same row as the workload for which you will add a scaling policy, choose  **Operation**  \>  **More**  \>  **Scale**.
    2.  In the  **Auto Scaling**  area, click  **Add Scaling Policy**.

        **Table  1**  Parameters for adding a metric-based policy

        <a name="table19998181617578"></a>
        <table><thead align="left"><tr id="row152117205715"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.3.1.1"><p id="p154121795719"><a name="p154121795719"></a><a name="p154121795719"></a>Parameter</p>
        </th>
        <th class="cellrowborder" valign="top" width="77%" id="mcps1.2.3.1.2"><p id="p87151735714"><a name="p87151735714"></a><a name="p87151735714"></a>Description</p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row18981795718"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p1612131785715"><a name="p1612131785715"></a><a name="p1612131785715"></a>Policy Name</p>
        </td>
        <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p1514161785713"><a name="p1514161785713"></a><a name="p1514161785713"></a>Enter the name of the scaling policy.</p>
        </td>
        </tr>
        <tr id="row315181717574"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p418141765713"><a name="p418141765713"></a><a name="p418141765713"></a>Policy Type</p>
        </td>
        <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p622317175715"><a name="p622317175715"></a><a name="p622317175715"></a>Set this parameter to <span class="uicontrol" id="uicontrol57503634515"><a name="uicontrol57503634515"></a><a name="uicontrol57503634515"></a><b>Metric-based policy</b></span>.</p>
        </td>
        </tr>
        <tr id="row17669451397"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p86701459915"><a name="p86701459915"></a><a name="p86701459915"></a>Metric</p>
        </td>
        <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p16701951895"><a name="p16701951895"></a><a name="p16701951895"></a>Set the metrics that describe the resource performance data or status.</p>
        <a name="ul20392191212016"></a><a name="ul20392191212016"></a><ul id="ul20392191212016"><li><strong id="b790894192518"><a name="b790894192518"></a><a name="b790894192518"></a>CPU Usage</strong>: indicates the CPU usage of the measured object, that is, the percentage of the CPU cores actually used by the measured object to the total CPU cores that the measured object has requested.</li><li><strong id="b1764184811255"><a name="b1764184811255"></a><a name="b1764184811255"></a>Physical Memory Usage</strong>: indicates the percentage of the physical memory size used by the measured object to the physical memory size that the measured object has applied for.</li></ul>
        </td>
        </tr>
        <tr id="row122211765714"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p102417173579"><a name="p102417173579"></a><a name="p102417173579"></a>Trigger Condition</p>
        </td>
        <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p02641715716"><a name="p02641715716"></a><a name="p02641715716"></a>You can set this parameter based on <span class="uicontrol" id="uicontrol1561224791720"><a name="uicontrol1561224791720"></a><a name="uicontrol1561224791720"></a><b>CPU Usage</b></span> or <span class="uicontrol" id="uicontrol166121847141715"><a name="uicontrol166121847141715"></a><a name="uicontrol166121847141715"></a><b>Physical Memory Usage</b></span>.</p>
        <p id="p102871735719"><a name="p102871735719"></a><a name="p102871735719"></a>If you set this parameter to the <strong id="b196183581268"><a name="b196183581268"></a><a name="b196183581268"></a>average physical memory usage &gt; 70%</strong>, the scaling policy will be triggered when the average memory usage exceeds 70%.</p>
        </td>
        </tr>
        <tr id="row15301217115716"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p631617195718"><a name="p631617195718"></a><a name="p631617195718"></a>Measurement Period</p>
        </td>
        <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p123318179571"><a name="p123318179571"></a><a name="p123318179571"></a>Metric statistics period. Select a value from the drop-down list box.</p>
        <p id="p1335151715719"><a name="p1335151715719"></a><a name="p1335151715719"></a>If the parameter is set to 20s, metric statistics is collected every 20 seconds.</p>
        </td>
        </tr>
        <tr id="row1735111705710"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p1936617175719"><a name="p1936617175719"></a><a name="p1936617175719"></a>Threshold Crossings</p>
        </td>
        <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p93816171572"><a name="p93816171572"></a><a name="p93816171572"></a>If the parameter is set to <strong id="b66181047141719"><a name="b66181047141719"></a><a name="b66181047141719"></a>3</strong>, the action is triggered if threshold is reached for three consecutive measurement periods.</p>
        </td>
        </tr>
        <tr id="row139111716578"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p240141775712"><a name="p240141775712"></a><a name="p240141775712"></a>Action</p>
        </td>
        <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p241121715570"><a name="p241121715570"></a><a name="p241121715570"></a>Action executed after a policy is triggered. Two actions are available: add or reduce pods.</p>
        </td>
        </tr>
        </tbody>
        </table>

    3.  Click  **OK**.
    4.  In the  **Auto Scaling**  area, check that the policy has been started.

        When the trigger condition is met, the auto scaling policy starts automatically.


-   <a name="li1595211281895"></a>**Scheduled policy**: scaling at a specified time.
    1.  In the  **Auto Scaling**  area, click  **Add Scaling Policy**. Select  **Scheduled policy**.

        **Table  2**  Parameters for adding a scheduled policy

        <a name="table0281144172511"></a>
        <table><thead align="left"><tr id="row1428011412512"><th class="cellrowborder" valign="top" width="26%" id="mcps1.2.3.1.1"><p id="p8280443259"><a name="p8280443259"></a><a name="p8280443259"></a>Parameter</p>
        </th>
        <th class="cellrowborder" valign="top" width="74%" id="mcps1.2.3.1.2"><p id="p12280847252"><a name="p12280847252"></a><a name="p12280847252"></a>Description</p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row1728054182516"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p20280164142516"><a name="p20280164142516"></a><a name="p20280164142516"></a>Policy Name</p>
        </td>
        <td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p id="p19280144112510"><a name="p19280144112510"></a><a name="p19280144112510"></a>Enter the name of the scaling policy.</p>
        </td>
        </tr>
        <tr id="row5280154182518"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p8280164192519"><a name="p8280164192519"></a><a name="p8280164192519"></a>Policy Type</p>
        </td>
        <td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p id="p15280134182513"><a name="p15280134182513"></a><a name="p15280134182513"></a>Set this parameter to <strong id="b71891229131820"><a name="b71891229131820"></a><a name="b71891229131820"></a>Scheduled policy</strong>.</p>
        </td>
        </tr>
        <tr id="row1728113415258"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p112804418256"><a name="p112804418256"></a><a name="p112804418256"></a>Trigger Time</p>
        </td>
        <td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p id="p1280646254"><a name="p1280646254"></a><a name="p1280646254"></a>Time at which the policy is enforced.</p>
        </td>
        </tr>
        <tr id="row112811346259"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p82812472513"><a name="p82812472513"></a><a name="p82812472513"></a>Action</p>
        </td>
        <td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p id="p82813416258"><a name="p82813416258"></a><a name="p82813416258"></a>Action executed after a policy is triggered. Three actions are available: add pods, reduce pods, and set the number of pods.</p>
        </td>
        </tr>
        </tbody>
        </table>

    2.  Click  **OK**.
    3.  In the  **Auto Scaling**  area, check that the policy has been started.

        When the trigger time is reached, you can see on the  **Pods**  tab page that the auto scaling policy has taken effect.


-   <a name="li35861531491"></a>**Periodic policy**: scaling at a specified time on a daily, weekly, or monthly basis.
    1.  In the  **Auto Scaling**  area, click  **Add Scaling Policy**. Select  **Periodic policy**.

        **Table  3**  Parameters for adding a periodic policy

        <a name="table184091016102710"></a>
        <table><thead align="left"><tr id="row13407141620275"><th class="cellrowborder" valign="top" width="26%" id="mcps1.2.3.1.1"><p id="p19407916192711"><a name="p19407916192711"></a><a name="p19407916192711"></a>Parameter</p>
        </th>
        <th class="cellrowborder" valign="top" width="74%" id="mcps1.2.3.1.2"><p id="p24071016172711"><a name="p24071016172711"></a><a name="p24071016172711"></a>Description</p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row10407101652718"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p18407191622715"><a name="p18407191622715"></a><a name="p18407191622715"></a>Policy Name</p>
        </td>
        <td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p id="p11407121616277"><a name="p11407121616277"></a><a name="p11407121616277"></a>Enter the name of the scaling policy.</p>
        </td>
        </tr>
        <tr id="row3409316102719"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p144071116132713"><a name="p144071116132713"></a><a name="p144071116132713"></a>Policy Type</p>
        </td>
        <td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p id="p7409181672718"><a name="p7409181672718"></a><a name="p7409181672718"></a>Set this parameter to <strong id="b8124749151812"><a name="b8124749151812"></a><a name="b8124749151812"></a>Periodic policy</strong>.</p>
        </td>
        </tr>
        <tr id="row1940915163272"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p5409161662713"><a name="p5409161662713"></a><a name="p5409161662713"></a>Time Range</p>
        </td>
        <td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p id="p6409131672714"><a name="p6409131672714"></a><a name="p6409131672714"></a>Specify the time for triggering the policy.</p>
        </td>
        </tr>
        <tr id="row154091616182715"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p174096168271"><a name="p174096168271"></a><a name="p174096168271"></a>Action</p>
        </td>
        <td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p id="p4409101613276"><a name="p4409101613276"></a><a name="p4409101613276"></a>Action executed after a policy is triggered. Three actions are available: add pods, reduce pods, and set the number of pods.</p>
        </td>
        </tr>
        </tbody>
        </table>

    2.  Click  **OK**.
    3.  In the  **Auto Scaling**  area, check that the policy has been started.

        When the trigger condition is met, the auto scaling policy starts automatically.



## Manual Scaling<a name="section1050418516503"></a>

1.  Log in to the CCE console. In the navigation pane, choose  **Workloads**  \>  **Deployments**  or  **StatefulSet**. In the same row as the workload for which you will add a scaling policy, choose  **Operation**  \>  **More**  \>  ****Scaling****.
2.  In the  **Manual Scaling**  area, click  ![](figures/icon-edit.png)  and change the number of pods to, for example,  **2**. Then, click  **Save**. The scaling takes effect immediately.
3.  On the  **Pods**  tab page, check that a new pod is being created. When the pod status becomes  **Running**, pod scaling is complete.

## Modifying Maximum Number of Unavailable Pods<a name="section7507175918309"></a>

1.  On the  **Stateless Workloads**  page or the  **Stateful Workloads**  page, click  **More \> Scale**  in the same row as the application for which you will modify the  **Maximum Number of Unavailable Pods**  parameter.
2.  Click  ![](figures/icon-edit-0.png)  to modify  **Maximum Number of Unavailable Pods**.
    -   If  **percentage**  is not selected,  **Maximum Number of Unavailable Pods**  indicates the maximum quantity of unavailable pods and cannot exceed the total number of pods that the application has.
    -   If  **percentage**  is selected,  **Maximum Number of Unavailable Pods**  indicates the maximum percentage of unavailable pods. The value range is \[0, 100\].

3.  Click  **Save**.

