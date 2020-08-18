# Configuring a Custom Bucket Policy \(Common Mode\)<a name="obs_03_0123"></a>

If you want to grant special permissions to specific users, you can configure custom bucket policies. If a standard bucket policy conflicts with a custom bucket policy, the authorization priority is given to the custom bucket policy and then the standard bucket policy.

This topic describes how to configure a custom bucket policy in common mode \(GUI\).

## Procedure<a name="section1761505716442"></a>

1.  In the bucket list, click the bucket to be operated. The  **Overview**  page of the bucket is displayed.
2.  In the navigation pane on the left, click  **Permissions**  to go to the permission management page.
3.  On the  **Bucket Policies**  tab page, configure a custom bucket policy according to your needs.

    On the right of  **Custom Bucket Policies**, select  **Common mode**  to configure the policy in the GUI mode.

4.  Click  **Create Bucket Policy**. Select a proper policy mode as required. Valid values are as follows:

    -   **Read-only**: The authorized user will be granted with the read permission on the bucket and objects. For subsequent operations, see  [5](#li3552175452220).
    -   **Read and write**: The authorized user will be granted with read and write permissions on the bucket and objects. For subsequent operations, see  [5](#li3552175452220).
    -   **Customized**: The authorized user will be granted with customized permissions on the bucket and objects. For detailed configuration, see  [6](#li588503161565).

    >![](public_sys-resources/icon-note.gif) **NOTE:** 
    >Only one bucket policy mode can be configured at a time.

5.  <a name="li3552175452220"></a>For the read-only and read and write modes, enter information about the authorized user in the following format and click  **OK**.

    **Figure  1**  Parameter settings of a custom bucket policy in the read-only or read and write mode<a name="fig3744459165110"></a>  
    ![](figures/parameter-settings-of-a-custom-bucket-policy-in-the-read-only-or-read-and-write-mode.png "parameter-settings-of-a-custom-bucket-policy-in-the-read-only-or-read-and-write-mode")

    **Table  1**  Parameters in bucket policies

    <a name="table374341792315"></a>
    <table><thead align="left"><tr id="row27504174239"><th class="cellrowborder" valign="top" width="15.151515151515152%" id="mcps1.2.4.1.1"><p id="p107559176234"><a name="p107559176234"></a><a name="p107559176234"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="37.37373737373738%" id="mcps1.2.4.1.2"><p id="p37601517192320"><a name="p37601517192320"></a><a name="p37601517192320"></a>Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="47.474747474747474%" id="mcps1.2.4.1.3"><p id="p1976317170239"><a name="p1976317170239"></a><a name="p1976317170239"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8783617122317"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.4.1.1 "><p id="p478519172231"><a name="p478519172231"></a><a name="p478519172231"></a>Principal</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.37373737373738%" headers="mcps1.2.4.1.2 "><a name="ul278810179232"></a><a name="ul278810179232"></a><ul id="ul278810179232"><li><strong id="b8700129123916"><a name="b8700129123916"></a><a name="b8700129123916"></a>Include</strong> or <strong id="b13701149143915"><a name="b13701149143915"></a><a name="b13701149143915"></a>Exclude</strong></li><li><strong id="b20217128143219"><a name="b20217128143219"></a><a name="b20217128143219"></a>Cloud service user</strong>, <strong id="b3946133123218"><a name="b3946133123218"></a><a name="b3946133123218"></a>Federated user</strong><a name="ul15575185754819"></a><a name="ul15575185754819"></a><ul id="ul15575185754819"><li>If you select <strong id="b1719003851715"><a name="b1719003851715"></a><a name="b1719003851715"></a>Cloud service user</strong>, you can specify the user to be the <strong id="b13691182461815"><a name="b13691182461815"></a><a name="b13691182461815"></a>Current account</strong> or <strong id="b811012284185"><a name="b811012284185"></a><a name="b811012284185"></a>Other account</strong>.<p id="p6813111014299"><a name="p6813111014299"></a><a name="p6813111014299"></a>If you select <strong id="b19285104818530"><a name="b19285104818530"></a><a name="b19285104818530"></a>Other account</strong>, enter the account ID, which is the <strong id="b1854913415546"><a name="b1854913415546"></a><a name="b1854913415546"></a>Domain ID</strong> on the <strong id="b314165115542"><a name="b314165115542"></a><a name="b314165115542"></a>My Credential</strong> page.</p>
    </li><li>If you select <strong id="b10799136191814"><a name="b10799136191814"></a><a name="b10799136191814"></a>Federated user</strong>, you can specify the user to be an <strong id="b14629912194"><a name="b14629912194"></a><a name="b14629912194"></a>Identity provider</strong> or a <strong id="b1312311791912"><a name="b1312311791912"></a><a name="b1312311791912"></a>User group</strong>.</li></ul>
    </li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="47.474747474747474%" headers="mcps1.2.4.1.3 "><p id="p19808171717235"><a name="p19808171717235"></a><a name="p19808171717235"></a>Specifies users on whom this bucket policy takes effect, including cloud service users and federated users. A cloud service user is the one who accesses the cloud services through registration with the cloud services. A federated user is the one who accesses the cloud services through federated identity authentication.</p>
    <a name="ul20673512167"></a><a name="ul20673512167"></a><ul id="ul20673512167"><li><strong id="b1104616143714"><a name="b1104616143714"></a><a name="b1104616143714"></a>Include</strong>: Specifies the user on whom the bucket policy statement takes effect.</li><li><strong id="b970317196371"><a name="b970317196371"></a><a name="b970317196371"></a>Exclude</strong>: Specifies that on all users except the specified user the bucket policy statement takes effect.</li></ul>
    </td>
    </tr>
    <tr id="row081741752319"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.4.1.1 "><p id="p15821617102320"><a name="p15821617102320"></a><a name="p15821617102320"></a>Resources</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.37373737373738%" headers="mcps1.2.4.1.2 "><a name="ul2824151742319"></a><a name="ul2824151742319"></a><ul id="ul2824151742319"><li><strong id="b41985308397"><a name="b41985308397"></a><a name="b41985308397"></a>Include</strong> or <strong id="b111991430193912"><a name="b111991430193912"></a><a name="b111991430193912"></a>Exclude</strong></li><li>Input format: <p id="p12830717162315"><a name="p12830717162315"></a><a name="p12830717162315"></a>Object: <em id="i1428683216397"><a name="i1428683216397"></a><a name="i1428683216397"></a>object name</em></p>
    <p id="p68341917112319"><a name="p68341917112319"></a><a name="p68341917112319"></a>Object set: <em id="i847916338396"><a name="i847916338396"></a><a name="i847916338396"></a>object name prefix*</em>, <em id="i1848013313917"><a name="i1848013313917"></a><a name="i1848013313917"></a>*object name suffix</em>, or *</p>
    </li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="47.474747474747474%" headers="mcps1.2.4.1.3 "><p id="p2084119170234"><a name="p2084119170234"></a><a name="p2084119170234"></a>Indicates the resource that a bucket policy applies to. With the read-only mode and read and write mode, the policy can only apply to objects.</p>
    <a name="ul7274173411710"></a><a name="ul7274173411710"></a><ul id="ul7274173411710"><li><strong id="b24951819019"><a name="b24951819019"></a><a name="b24951819019"></a>Include</strong>: Specifies the OBS resources on which the bucket policy statement takes effect.</li><li><strong id="b172155361308"><a name="b172155361308"></a><a name="b172155361308"></a>Exclude</strong>: Specifies that on all OBS resources except the specified ones the bucket policy statement takes effect.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

6.  <a name="li588503161565"></a>For the customized mode, set parameters based on the site requirements and click  **OK**.

    **Figure  2**  Parameter settings of a custom bucket policy in the customized mode<a name="fig53211555145821"></a>  
    ![](figures/parameter-settings-of-a-custom-bucket-policy-in-the-customized-mode.png "parameter-settings-of-a-custom-bucket-policy-in-the-customized-mode")

    [Table 2](#table25824246144542)  lists the meaning of each parameter.

    **Table  2**  Parameters in bucket policies

    <a name="table25824246144542"></a>
    <table><thead align="left"><tr id="row20874365144542"><th class="cellrowborder" valign="top" width="20.202020202020204%" id="mcps1.2.4.1.1"><p id="p13102027144542"><a name="p13102027144542"></a><a name="p13102027144542"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="34.343434343434346%" id="mcps1.2.4.1.2"><p id="p171671754714"><a name="p171671754714"></a><a name="p171671754714"></a>Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.45454545454546%" id="mcps1.2.4.1.3"><p id="p54631241144542"><a name="p54631241144542"></a><a name="p54631241144542"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row10774617144542"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.1 "><p id="p328816144542"><a name="p328816144542"></a><a name="p328816144542"></a>Effect</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.2.4.1.2 "><p id="p616717174717"><a name="p616717174717"></a><a name="p616717174717"></a><strong id="b97561137113311"><a name="b97561137113311"></a><a name="b97561137113311"></a>Allow</strong> or <strong id="b135788406338"><a name="b135788406338"></a><a name="b135788406338"></a>Deny</strong></p>
    </td>
    <td class="cellrowborder" valign="top" width="45.45454545454546%" headers="mcps1.2.4.1.3 "><p id="p04354171543"><a name="p04354171543"></a><a name="p04354171543"></a>Effect of a bucket policy.</p>
    <a name="ul1835191314190"></a><a name="ul1835191314190"></a><ul id="ul1835191314190"><li><strong id="b1391852611270"><a name="b1391852611270"></a><a name="b1391852611270"></a>Allow</strong>: Indicates access requests are allowed, if they match the configurations of this bucket policy.</li><li><strong id="b1037794816276"><a name="b1037794816276"></a><a name="b1037794816276"></a>Deny</strong>: Indicates access requests are denied, if they match the configurations of this bucket policy.</li></ul>
    </td>
    </tr>
    <tr id="row46881427144542"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.1 "><p id="p39299241144542"><a name="p39299241144542"></a><a name="p39299241144542"></a>Principal</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.2.4.1.2 "><a name="ul19561211185417"></a><a name="ul19561211185417"></a><ul id="ul19561211185417"><li><strong id="b830025419431"><a name="b830025419431"></a><a name="b830025419431"></a>Include</strong> or <strong id="b030075414316"><a name="b030075414316"></a><a name="b030075414316"></a>Exclude</strong></li><li><strong id="b19619115514331"><a name="b19619115514331"></a><a name="b19619115514331"></a>Cloud service user</strong>, <strong id="b1769811573338"><a name="b1769811573338"></a><a name="b1769811573338"></a>Federated user</strong><a name="ul3534111145812"></a><a name="ul3534111145812"></a><ul id="ul3534111145812"><li>If you select <strong id="b12105540112018"><a name="b12105540112018"></a><a name="b12105540112018"></a>Cloud service user</strong>, you can specify the user to be the <strong id="b15106124020204"><a name="b15106124020204"></a><a name="b15106124020204"></a>Current account</strong> or <strong id="b19107540182019"><a name="b19107540182019"></a><a name="b19107540182019"></a>Other account</strong>.<p id="p27327479313"><a name="p27327479313"></a><a name="p27327479313"></a>If you select <strong id="b22846587544"><a name="b22846587544"></a><a name="b22846587544"></a>Other account</strong>, enter the account ID, which is the <strong id="b429005865414"><a name="b429005865414"></a><a name="b429005865414"></a>Domain ID</strong> on the <strong id="b1529085812541"><a name="b1529085812541"></a><a name="b1529085812541"></a>My Credential</strong> page.</p>
    </li><li>If you select <strong id="b11332843172011"><a name="b11332843172011"></a><a name="b11332843172011"></a>Federated user</strong>, you can specify the user to be an <strong id="b18332134322012"><a name="b18332134322012"></a><a name="b18332134322012"></a>Identity provider</strong> or a <strong id="b1133313438201"><a name="b1133313438201"></a><a name="b1133313438201"></a>User group</strong>.</li></ul>
    </li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="45.45454545454546%" headers="mcps1.2.4.1.3 "><p id="p243601717416"><a name="p243601717416"></a><a name="p243601717416"></a>Specifies users on whom this bucket policy takes effect, including cloud service users and federated users. A cloud service user is the one who accesses the cloud services through registration with the cloud services. A federated user is the one who accesses the cloud services through federated identity authentication.</p>
    <a name="ul101874512014"></a><a name="ul101874512014"></a><ul id="ul101874512014"><li><strong id="b5139722814"><a name="b5139722814"></a><a name="b5139722814"></a>Include</strong>: Specifies the user on whom the bucket policy statement takes effect.</li><li><strong id="b1873720225119"><a name="b1873720225119"></a><a name="b1873720225119"></a>Exclude</strong>: Specifies that on all users except the specified user the bucket policy statement takes effect.</li></ul>
    </td>
    </tr>
    <tr id="row26311294144542"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.1 "><p id="p50840088144542"><a name="p50840088144542"></a><a name="p50840088144542"></a>Resources</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.2.4.1.2 "><a name="ul151711055754"></a><a name="ul151711055754"></a><ul id="ul151711055754"><li><strong id="b260811154416"><a name="b260811154416"></a><a name="b260811154416"></a>Include</strong> or <strong id="b1661019115446"><a name="b1661019115446"></a><a name="b1661019115446"></a>Exclude</strong></li><li>Resource input format:<p id="p13659113718819"><a name="p13659113718819"></a><a name="p13659113718819"></a>Object: <em id="i135851314448"><a name="i135851314448"></a><a name="i135851314448"></a>object name</em></p>
    <p id="p47531246786"><a name="p47531246786"></a><a name="p47531246786"></a>Object set: <em id="i193453404413"><a name="i193453404413"></a><a name="i193453404413"></a>object name prefix*</em>, <em id="i93461441445"><a name="i93461441445"></a><a name="i93461441445"></a>*object name suffix</em>, or *</p>
    <p id="p484811521683"><a name="p484811521683"></a><a name="p484811521683"></a>Blank: Indicates that the resource is the entire bucket.</p>
    </li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="45.45454545454546%" headers="mcps1.2.4.1.3 "><p id="p144361117943"><a name="p144361117943"></a><a name="p144361117943"></a>Indicates the resource that a bucket policy applies to.</p>
    <a name="ul1243923162015"></a><a name="ul1243923162015"></a><ul id="ul1243923162015"><li><strong id="b865918341216"><a name="b865918341216"></a><a name="b865918341216"></a>Include</strong>: Specifies the OBS resources on which the bucket policy statement takes effect.</li><li><strong id="b944620361117"><a name="b944620361117"></a><a name="b944620361117"></a>Exclude</strong>: Specifies that on all OBS resources except the specified ones the bucket policy statement takes effect.</li></ul>
    <p id="p24361917944"><a name="p24361917944"></a><a name="p24361917944"></a>Relationship between resource types and actions:</p>
    <a name="ul1943618171341"></a><a name="ul1943618171341"></a><ul id="ul1943618171341"><li>When a resource is an object or an object set, only the actions related to the object can be configured.</li><li>When the resource is a bucket, only the actions related to the bucket can be configured.</li></ul>
    </td>
    </tr>
    <tr id="row461371117754"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.1 "><p id="p420595051780"><a name="p420595051780"></a><a name="p420595051780"></a>Actions</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.2.4.1.2 "><a name="ul732518295298"></a><a name="ul732518295298"></a><ul id="ul732518295298"><li><strong id="b2283202443"><a name="b2283202443"></a><a name="b2283202443"></a>Include</strong> or <strong id="b1929620114413"><a name="b1929620114413"></a><a name="b1929620114413"></a>Exclude</strong></li><li>For details, see <a href="actions.md">Actions</a>.</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="45.45454545454546%" headers="mcps1.2.4.1.3 "><p id="p114369173413"><a name="p114369173413"></a><a name="p114369173413"></a>Operations stated in the bucket policy.</p>
    <a name="ul172495822013"></a><a name="ul172495822013"></a><ul id="ul172495822013"><li><strong id="b6426853183718"><a name="b6426853183718"></a><a name="b6426853183718"></a>Include</strong>: Specifies the actions on which the bucket policy takes effect.</li><li><strong id="b10431155616372"><a name="b10431155616372"></a><a name="b10431155616372"></a>Exclude</strong>: Specifies that on all actions except the specified ones the bucket policy takes effect.</li></ul>
    </td>
    </tr>
    <tr id="row8998688144542"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.1 "><p id="p57805116144542"><a name="p57805116144542"></a><a name="p57805116144542"></a>Conditions</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.2.4.1.2 "><a name="ul63480483323"></a><a name="ul63480483323"></a><ul id="ul63480483323"><li>Conditional Operator: see <a href="conditions.md#table16670126115713">Table 1</a>.</li><li>Key: For details, see <a href="conditions.md#table6707152645718">Table 2</a>, <a href="conditions.md#table1972610267573">Table 3</a>, and <a href="conditions.md#table14742526145718">Table 4</a>.</li><li><strong id="b142352724416"><a name="b142352724416"></a><a name="b142352724416"></a>Value</strong>: The entered value is associated with the key.</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="45.45454545454546%" headers="mcps1.2.4.1.3 "><p id="p34365171045"><a name="p34365171045"></a><a name="p34365171045"></a>Conditions for the policy statement to take effect.</p>
    </td>
    </tr>
    </tbody>
    </table>


