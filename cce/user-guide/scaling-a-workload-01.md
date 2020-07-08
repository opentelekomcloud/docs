# Scaling a Workload<a name="cce_01_0208"></a>

For workloads, you can create HPA policies for scaling.

**Horizontal Pod Autoscaling \(HPA\)**: a policy that implements horizontal scaling of pods in Kubernetes. This policy adds the HPA-level cooldown time window and scaling threshold functions based on the HPA function provided by the Kubernetes community.

## Prerequisites<a name="section194973810277"></a>

Before configuring an HPA policy, you must install the metrics-server add-on to collect the running metrics of the workloads associated with the HPA policy.

## Constraints<a name="section107429267459"></a>

HPA policies can be created only for clusters of v1.13 or later.

## Creating an HPA Policy<a name="section97751315174715"></a>

1.  Log in to the CCE console. In the navigation pane on the left, choose  **Auto Scaling**. On the  **Workload Scaling**  tab page, check whether the metrics-server add-on has been installed and is running properly.
2.  After installing the metrics-server add-on, click  **Create HPA Policy**.
3.  On the  **Create HPA Policy**  page displayed, set the policy parameters listed in  [Table 1](#table8638121213265).

    **Table  1**  HPA policy parameters

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
    <tr id="row42961494311"><td class="cellrowborder" valign="top" width="20.02%" headers="mcps1.2.3.1.1 "><p id="p2714182116117"><a name="p2714182116117"></a><a name="p2714182116117"></a>Cluster Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="79.97999999999999%" headers="mcps1.2.3.1.2 "><p id="p161283411302"><a name="p161283411302"></a><a name="p161283411302"></a>Cluster to which the workload belongs.</p>
    </td>
    </tr>
    <tr id="row12321131519262"><td class="cellrowborder" valign="top" width="20.02%" headers="mcps1.2.3.1.1 "><p id="p14322181522614"><a name="p14322181522614"></a><a name="p14322181522614"></a>Namespace</p>
    </td>
    <td class="cellrowborder" valign="top" width="79.97999999999999%" headers="mcps1.2.3.1.2 "><p id="p1950113815188"><a name="p1950113815188"></a><a name="p1950113815188"></a>Namespace to which the workload belongs.</p>
    </td>
    </tr>
    <tr id="row1063812126263"><td class="cellrowborder" valign="top" width="20.02%" headers="mcps1.2.3.1.1 "><p id="p15639812122620"><a name="p15639812122620"></a><a name="p15639812122620"></a>Associated Workload</p>
    </td>
    <td class="cellrowborder" valign="top" width="79.97999999999999%" headers="mcps1.2.3.1.2 "><p id="p1520317181911"><a name="p1520317181911"></a><a name="p1520317181911"></a>Workload with which the HPA policy is associated.</p>
    </td>
    </tr>
    <tr id="row6649879161231"><td class="cellrowborder" valign="top" width="20.02%" headers="mcps1.2.3.1.1 "><p id="p1769363161231"><a name="p1769363161231"></a><a name="p1769363161231"></a>Pod Range</p>
    </td>
    <td class="cellrowborder" valign="top" width="79.97999999999999%" headers="mcps1.2.3.1.2 "><p id="p9100682161231"><a name="p9100682161231"></a><a name="p9100682161231"></a>Enter the minimum and maximum numbers of pods. When a policy is triggered, the workload pods are scaled within this range.</p>
    </td>
    </tr>
    <tr id="row465423512512"><td class="cellrowborder" valign="top" width="20.02%" headers="mcps1.2.3.1.1 "><p id="p1065512351354"><a name="p1065512351354"></a><a name="p1065512351354"></a>Cooldown Period</p>
    </td>
    <td class="cellrowborder" valign="top" width="79.97999999999999%" headers="mcps1.2.3.1.2 "><p id="p665503519514"><a name="p665503519514"></a><a name="p665503519514"></a>Set a cooldown period, within which scaling will not be triggered again when a policy is triggered.</p>
    </td>
    </tr>
    <tr id="row572593234714"><td class="cellrowborder" valign="top" width="20.02%" headers="mcps1.2.3.1.1 "><p id="p14725432104718"><a name="p14725432104718"></a><a name="p14725432104718"></a>Rules</p>
    </td>
    <td class="cellrowborder" valign="top" width="79.97999999999999%" headers="mcps1.2.3.1.2 "><a name="ul56611653205511"></a><a name="ul56611653205511"></a><ul id="ul56611653205511"><li><span class="parmname" id="parmname1784758141014"><a name="parmname1784758141014"></a><a name="parmname1784758141014"></a><b>Metric</b></span>: You can select <span class="parmvalue" id="parmvalue867911081114"><a name="parmvalue867911081114"></a><a name="parmvalue867911081114"></a><b>CPU usage</b></span> or <span class="parmvalue" id="parmvalue3384615201118"><a name="parmvalue3384615201118"></a><a name="parmvalue3384615201118"></a><b>Memory usage</b></span>. Usage = CPUs or memory used by pods/Requested CPUs or memory.</li><li><span class="parmname" id="parmname11418134810145"><a name="parmname11418134810145"></a><a name="parmname11418134810145"></a><b>Expected Value</b></span>: Enter an expected value. The expected value of the selected metric works with the threshold. The actual number of pods to be scaled is calculated using the following formula: Expected Value/Threshold x Number of current pods.</li><li><span class="parmname" id="parmname17591143391618"><a name="parmname17591143391618"></a><a name="parmname17591143391618"></a><b>Threshold</b></span>: When the metric value is less than the scale-in threshold, scale-in is triggered. When the metric value is greater than the scale-out threshold, scale-out is triggered.</li></ul>
    <p id="p162368519564"><a name="p162368519564"></a><a name="p162368519564"></a>You can click <span class="uicontrol" id="uicontrol59611559592"><a name="uicontrol59611559592"></a><a name="uicontrol59611559592"></a><b>Add Rule</b></span> again to add more scaling policies.</p>
    </td>
    </tr>
    </tbody>
    </table>

4.  After the configuration is complete, click  **Create**. The  **Workload Scaling**  page is displayed. You can view the created HPA policy in the list.

## Updating an HPA Policy<a name="section77571018204513"></a>

1.  Log in to the CCE console. In the navigation pane on the left, choose  **Auto Scaling**. On the  **Workload Scaling**  tab page, click  **Update**  in the  **Operation**  column of the policy to be updated.
2.  On the  **Update HPA Policy**  page displayed, set the policy parameters listed in  [Table 1](#table8638121213265).
3.  Click  **Update**.

## Cloning an HPA Policy<a name="section97031342134513"></a>

1.  Log in to the CCE console. In the navigation pane, choose  **Auto Scaling**. On the  **Workload Scaling**  tab page, click  **Clone**  in the  **Operation**  column of the policy to be updated.
2.  For example, for an HPA policy, on the  **Create HPA Policy**  page, you can view that parameters such as  **Pod Range**,  **Cooldown Period**, and  **Rules**  have been cloned. Add or modify other policy parameters as needed.
3.  Click  **Create**  to complete policy cloning. On the  **Workload Scaling**  tab page, you can view the cloned policy in the policy list.

## Editing a YAML File<a name="section191049274615"></a>

1.  Log in to the CCE console. In the navigation pane, choose  **Auto Scaling**. On the  **Workload Scaling**  tab page, click  **More**  \>  **Edit YAML**  in the  **Operation**  column of the policy to be updated.
2.  In the  **Edit YAML**  dialog box displayed, edit or download the YAML file.
3.  Click the close button in the upper right corner.

## Deleting an HPA Policy<a name="section149261320174611"></a>

1.  Log in to the CCE console. In the navigation pane, choose  **Auto Scaling**. On the  **Workload Scaling**  tab page, click  **More \> Delete**  in the  **Operation**  column of the policy to be deleted.
2.  In the  **Delete HPA Policy**  dialog box displayed, confirm whether to delete the HPA policy.
3.  Click  **Yes**  to delete the policy.

## Checking an HPA Policy<a name="section678215151476"></a>

You can view the rules, status, and events of the HPA policy and handle exceptions based on the error information displayed.

1.  Log in to the CCE console. In the navigation pane, choose  **Auto Scaling**. On the  **Workload Scaling**  tab page, click  ![](figures/icon-pull-down-5.png)  in front of the policy.
2.  In the expanded area, you can view the  **Rules**,  **Status**, and  **Events**  tab pages. If the policy is abnormal, locate and rectify the fault based on the error information.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >You can also view the created HPA policy on the workload details page. On the CCE console, choose  **Workloads**  \>  **Deployments**  or  **Workloads**  \>  **StatefulSets**  in the navigation pane, and click  **More**  \>  **Scaling**  in the  **Operation**  column. On the page displayed, the HPA policy configured on the  **Auto Scaling**  page is also displayed under  **Auto Scaling by HPA**.  

    **Table  2**  Event types and names

    <a name="table56931825193212"></a>
    <table><thead align="left"><tr id="row269117254324"><th class="cellrowborder" valign="top" width="17.531753175317533%" id="mcps1.2.4.1.1"><p id="p176911125153211"><a name="p176911125153211"></a><a name="p176911125153211"></a>Event Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="40.94409440944094%" id="mcps1.2.4.1.2"><p id="p76911525153218"><a name="p76911525153218"></a><a name="p76911525153218"></a>Event Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="41.52415241524153%" id="mcps1.2.4.1.3"><p id="p156911325133211"><a name="p156911325133211"></a><a name="p156911325133211"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2692325123216"><td class="cellrowborder" valign="top" width="17.531753175317533%" headers="mcps1.2.4.1.1 "><p id="p1769152583210"><a name="p1769152583210"></a><a name="p1769152583210"></a>Normal</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.94409440944094%" headers="mcps1.2.4.1.2 "><p id="p4692725173214"><a name="p4692725173214"></a><a name="p4692725173214"></a>SuccessfulRescale</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.52415241524153%" headers="mcps1.2.4.1.3 "><p id="p1969242553220"><a name="p1969242553220"></a><a name="p1969242553220"></a>The scaling is performed successfully.</p>
    </td>
    </tr>
    <tr id="row15692192511329"><td class="cellrowborder" rowspan="12" valign="top" width="17.531753175317533%" headers="mcps1.2.4.1.1 "><p id="p86921225133210"><a name="p86921225133210"></a><a name="p86921225133210"></a>Abnormal</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.94409440944094%" headers="mcps1.2.4.1.2 "><p id="p14692125103210"><a name="p14692125103210"></a><a name="p14692125103210"></a>InvalidTargetRange</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.52415241524153%" headers="mcps1.2.4.1.3 "><p id="p11692172514329"><a name="p11692172514329"></a><a name="p11692172514329"></a>Invalid target range.</p>
    </td>
    </tr>
    <tr id="row1669211256324"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p10692225173214"><a name="p10692225173214"></a><a name="p10692225173214"></a>InvalidSelector</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p66929256329"><a name="p66929256329"></a><a name="p66929256329"></a>Invalid selector.</p>
    </td>
    </tr>
    <tr id="row36921525173217"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p12692182515326"><a name="p12692182515326"></a><a name="p12692182515326"></a>FailedGetObjectMetric</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p36921725193219"><a name="p36921725193219"></a><a name="p36921725193219"></a>Objects fail to be obtained.</p>
    </td>
    </tr>
    <tr id="row769216258320"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1369272512320"><a name="p1369272512320"></a><a name="p1369272512320"></a>FailedGetPodsMetric</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p9692325113214"><a name="p9692325113214"></a><a name="p9692325113214"></a>Pods fail to be obtained.</p>
    </td>
    </tr>
    <tr id="row17692925143210"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p196920258323"><a name="p196920258323"></a><a name="p196920258323"></a>FailedGetResourceMetric</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p1369216257321"><a name="p1369216257321"></a><a name="p1369216257321"></a>Resources fail to be obtained.</p>
    </td>
    </tr>
    <tr id="row669216253320"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p176922251321"><a name="p176922251321"></a><a name="p176922251321"></a>FailedGetExternalMetric</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p1269242511325"><a name="p1269242511325"></a><a name="p1269242511325"></a>External metrics fail to be obtained.</p>
    </td>
    </tr>
    <tr id="row869212503211"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p369212583219"><a name="p369212583219"></a><a name="p369212583219"></a>InvalidMetricSourceType</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p15692152519329"><a name="p15692152519329"></a><a name="p15692152519329"></a>Invalid metric source type.</p>
    </td>
    </tr>
    <tr id="row11692142513324"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p469262553220"><a name="p469262553220"></a><a name="p469262553220"></a>FailedConvertHPA</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p19692725123218"><a name="p19692725123218"></a><a name="p19692725123218"></a>HPA conversion failed.</p>
    </td>
    </tr>
    <tr id="row1469282513323"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1369216256328"><a name="p1369216256328"></a><a name="p1369216256328"></a>FailedGetScale</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p1369212563217"><a name="p1369212563217"></a><a name="p1369212563217"></a>The scale fails to be obtained.</p>
    </td>
    </tr>
    <tr id="row186921525183211"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1769211256328"><a name="p1769211256328"></a><a name="p1769211256328"></a>FailedComputeMetricsReplicas</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p7692192503219"><a name="p7692192503219"></a><a name="p7692192503219"></a>Metric replicas fail to be calculated.</p>
    </td>
    </tr>
    <tr id="row176931225143214"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p106921025173215"><a name="p106921025173215"></a><a name="p106921025173215"></a>FailedGetScaleWindow</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p14693142523215"><a name="p14693142523215"></a><a name="p14693142523215"></a>Failed to obtain ScaleWindow.</p>
    </td>
    </tr>
    <tr id="row19693132523211"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p3693102520327"><a name="p3693102520327"></a><a name="p3693102520327"></a>FailedRescale</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p46931255327"><a name="p46931255327"></a><a name="p46931255327"></a>Re-scaling fails.</p>
    </td>
    </tr>
    </tbody>
    </table>


