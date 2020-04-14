# Configuring an Object Policy<a name="obs_03_0075"></a>

An object policy applies to a specific object, which is also part of a bucket policy. The resource of an object policy is the selected object, and the actions and conditions are the object related actions and conditions configured in the bucket policy.

## Procedure<a name="section1427668152517"></a>

1.  In the bucket list, click the bucket to be operated. The  **Summary**  page of the bucket is displayed.
2.  In the navigation pane on the left, click  **Objects**.
3.  On the right of the object to be operated, choose  **More**  \>  **Configure Object Policy**. The  **Configure Object Policy**  dialog box is displayed.
4.  Select a proper policy mode as required. Valid options are as follows:

    -   Read-only mode: The authorized user has the read permission to the object. For follow-up procedure, see  [5](#li3552175452220).
    -   Read and write mode: The authorized user has the read and write permissions to the object. For follow-up procedure, see  [5](#li3552175452220).
    -   Customized: The authorized user will be granted with customized permissions to the object. For detailed configuration, see  [6](#li588503161565).

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >You can configure only one object policy at a time.  

5.  <a name="li3552175452220"></a>For read-only and read and write modes, enter information about the authorized user in the following format and click  **OK**.

    **Figure  1**  Parameter settings of an object policy in the read-only or read and write mode<a name="fig17275162821520"></a>  
    ![](figures/parameter-settings-of-an-object-policy-in-the-read-only-or-read-and-write-mode.png "parameter-settings-of-an-object-policy-in-the-read-only-or-read-and-write-mode")

    **Table  1**  Object policy parameters in read-only or read and write mode

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
    <td class="cellrowborder" valign="top" width="37.37373737373738%" headers="mcps1.2.4.1.2 "><a name="ul278810179232"></a><a name="ul278810179232"></a><ul id="ul278810179232"><li><strong id="b1499114720199"><a name="b1499114720199"></a><a name="b1499114720199"></a>Include</strong> or <strong id="b195001647151916"><a name="b195001647151916"></a><a name="b195001647151916"></a>Exclude</strong></li><li>Cloud service user, Federated user<a name="ul103531411807"></a><a name="ul103531411807"></a><ul id="ul103531411807"><li>If you select <strong id="b12681481385"><a name="b12681481385"></a><a name="b12681481385"></a>Cloud service user</strong>, you can specify the user to be the <strong id="b1826984853817"><a name="b1826984853817"></a><a name="b1826984853817"></a>Current account</strong> or <strong id="b52702048203815"><a name="b52702048203815"></a><a name="b52702048203815"></a>Other account</strong>.<p id="p119889201618"><a name="p119889201618"></a><a name="p119889201618"></a>If you select <strong id="b12744659724"><a name="b12744659724"></a><a name="b12744659724"></a>Other account</strong>, enter the account ID, which is the <strong id="b574555913216"><a name="b574555913216"></a><a name="b574555913216"></a>Domain ID</strong> on the <strong id="b5745159926"><a name="b5745159926"></a><a name="b5745159926"></a>My Credential</strong> page.</p>
    </li><li>If you select <strong id="b452255323811"><a name="b452255323811"></a><a name="b452255323811"></a>Federated user</strong>, you can specify the user to be an <strong id="b1252315303814"><a name="b1252315303814"></a><a name="b1252315303814"></a>Identity provider</strong> or a <strong id="b15523155393814"><a name="b15523155393814"></a><a name="b15523155393814"></a>User group</strong>.</li></ul>
    </li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="47.474747474747474%" headers="mcps1.2.4.1.3 "><p id="p19808171717235"><a name="p19808171717235"></a><a name="p19808171717235"></a>Indicates the user that the object policy applies to.</p>
    <a name="ul25601236173218"></a><a name="ul25601236173218"></a><ul id="ul25601236173218"><li><strong id="obs_03_0049_b9396124819353"><a name="obs_03_0049_b9396124819353"></a><a name="obs_03_0049_b9396124819353"></a>Include</strong>: Specifies the user on whom the bucket policy statement takes effect.</li><li><strong id="obs_03_0049_b13188853163520"><a name="obs_03_0049_b13188853163520"></a><a name="obs_03_0049_b13188853163520"></a>Exclude</strong>: Specifies that on all users except the specified user the bucket policy statement takes effect.</li></ul>
    </td>
    </tr>
    <tr id="row081741752319"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.4.1.1 "><p id="p15821617102320"><a name="p15821617102320"></a><a name="p15821617102320"></a>Resources</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.37373737373738%" headers="mcps1.2.4.1.2 "><p id="p882465163013"><a name="p882465163013"></a><a name="p882465163013"></a><strong id="b5961111282010"><a name="b5961111282010"></a><a name="b5961111282010"></a>Include</strong> or <strong id="b796319127204"><a name="b796319127204"></a><a name="b796319127204"></a>Exclude</strong></p>
    </td>
    <td class="cellrowborder" valign="top" width="47.474747474747474%" headers="mcps1.2.4.1.3 "><p id="p2084119170234"><a name="p2084119170234"></a><a name="p2084119170234"></a>Resources on which the object policy takes effect.</p>
    <a name="ul1441045823718"></a><a name="ul1441045823718"></a><ul id="ul1441045823718"><li><strong id="obs_03_0118_b184419873610"><a name="obs_03_0118_b184419873610"></a><a name="obs_03_0118_b184419873610"></a>Include</strong>: Indicates that the policy takes effect only on the specified OBS resources.</li><li><strong id="obs_03_0118_b171841311113612"><a name="obs_03_0118_b171841311113612"></a><a name="obs_03_0118_b171841311113612"></a>Exclude</strong>: Indicates that the bucket policy takes effect on all OBS resources except the specified ones.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

6.  <a name="li588503161565"></a>For the customized mode, set parameters based on the site requirements and click  **OK**.

    **Figure  2**  Parameter settings of an object policy in the customized mode<a name="fig53211555145821"></a>  
    ![](figures/parameter-settings-of-an-object-policy-in-the-customized-mode.png "parameter-settings-of-an-object-policy-in-the-customized-mode")

    **Table  2**  Object policy parameters in the custom mode

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
    <td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.2.4.1.2 "><p id="p616717174717"><a name="p616717174717"></a><a name="p616717174717"></a><strong id="b0711135462019"><a name="b0711135462019"></a><a name="b0711135462019"></a>Allow</strong> or <strong id="b1771213544202"><a name="b1771213544202"></a><a name="b1771213544202"></a>Deny</strong></p>
    </td>
    <td class="cellrowborder" valign="top" width="45.45454545454546%" headers="mcps1.2.4.1.3 "><p id="p1615161923718"><a name="p1615161923718"></a><a name="p1615161923718"></a>Effect of the object policy.</p>
    <a name="ul415919103710"></a><a name="ul415919103710"></a><ul id="ul415919103710"><li><strong id="obs_03_0115_b1391852611270"><a name="obs_03_0115_b1391852611270"></a><a name="obs_03_0115_b1391852611270"></a>Allow</strong>: Indicates that access requests are allowed, if they match the configurations of the bucket policy.</li><li><strong id="obs_03_0115_b1037794816276"><a name="obs_03_0115_b1037794816276"></a><a name="obs_03_0115_b1037794816276"></a>Deny</strong>: Indicates that access requests are denied, if they match the configurations of the bucket policy.</li></ul>
    </td>
    </tr>
    <tr id="row46881427144542"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.1 "><p id="p39299241144542"><a name="p39299241144542"></a><a name="p39299241144542"></a>Principal</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.2.4.1.2 "><a name="ul19561211185417"></a><a name="ul19561211185417"></a><ul id="ul19561211185417"><li><strong id="b57446226218"><a name="b57446226218"></a><a name="b57446226218"></a>Include</strong> or <strong id="b1745222142115"><a name="b1745222142115"></a><a name="b1745222142115"></a>Exclude</strong></li><li>Cloud service user, Federated user<a name="ul16810162511812"></a><a name="ul16810162511812"></a><ul id="ul16810162511812"><li>If you select <strong id="b664717160398"><a name="b664717160398"></a><a name="b664717160398"></a>Cloud service user</strong>, you can specify the user to be the <strong id="b1064741663914"><a name="b1064741663914"></a><a name="b1064741663914"></a>Current account</strong> or <strong id="b1164861613399"><a name="b1164861613399"></a><a name="b1164861613399"></a>Other account</strong>.<p id="p17218630181616"><a name="p17218630181616"></a><a name="p17218630181616"></a>If you select <strong id="b1024981319313"><a name="b1024981319313"></a><a name="b1024981319313"></a>Other account</strong>, enter the account ID, which is the <strong id="b1024916132316"><a name="b1024916132316"></a><a name="b1024916132316"></a>Domain ID</strong> on the <strong id="b32507131339"><a name="b32507131339"></a><a name="b32507131339"></a>My Credential</strong> page.</p>
    </li><li>If you select <strong id="b9859208399"><a name="b9859208399"></a><a name="b9859208399"></a>Federated user</strong>, you can specify the user to be an <strong id="b286102013393"><a name="b286102013393"></a><a name="b286102013393"></a>Identity provider</strong> or a <strong id="b168619207395"><a name="b168619207395"></a><a name="b168619207395"></a>User group</strong>.</li></ul>
    </li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="45.45454545454546%" headers="mcps1.2.4.1.3 "><p id="p1715111933716"><a name="p1715111933716"></a><a name="p1715111933716"></a>Specifies users on whom this object policy takes effect, including cloud service users and federated users. A cloud service user is the one who accesses the cloud services through registration with the cloud services. A federated user is the one who accesses the cloud services through federated identity authentication.</p>
    <a name="ul119112314313"></a><a name="ul119112314313"></a><ul id="ul119112314313"><li><strong id="obs_03_0049_b9396124819353_1"><a name="obs_03_0049_b9396124819353_1"></a><a name="obs_03_0049_b9396124819353_1"></a>Include</strong>: Specifies the user on whom the bucket policy statement takes effect.</li><li><strong id="obs_03_0049_b13188853163520_1"><a name="obs_03_0049_b13188853163520_1"></a><a name="obs_03_0049_b13188853163520_1"></a>Exclude</strong>: Specifies that on all users except the specified user the bucket policy statement takes effect.</li></ul>
    </td>
    </tr>
    <tr id="row26311294144542"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.1 "><p id="p50840088144542"><a name="p50840088144542"></a><a name="p50840088144542"></a>Resources</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.2.4.1.2 "><a name="ul151711055754"></a><a name="ul151711055754"></a><ul id="ul151711055754"><li><strong id="b188441334211"><a name="b188441334211"></a><a name="b188441334211"></a>Include</strong> or <strong id="b19845133132113"><a name="b19845133132113"></a><a name="b19845133132113"></a>Exclude</strong></li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="45.45454545454546%" headers="mcps1.2.4.1.3 "><p id="p1016819183718"><a name="p1016819183718"></a><a name="p1016819183718"></a>Resources on which the object policy takes effect.</p>
    <a name="ul98281632306"></a><a name="ul98281632306"></a><ul id="ul98281632306"><li><strong id="obs_03_0118_b184419873610_1"><a name="obs_03_0118_b184419873610_1"></a><a name="obs_03_0118_b184419873610_1"></a>Include</strong>: Indicates that the policy takes effect only on the specified OBS resources.</li><li><strong id="obs_03_0118_b171841311113612_1"><a name="obs_03_0118_b171841311113612_1"></a><a name="obs_03_0118_b171841311113612_1"></a>Exclude</strong>: Indicates that the bucket policy takes effect on all OBS resources except the specified ones.</li></ul>
    </td>
    </tr>
    <tr id="row461371117754"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.1 "><p id="p420595051780"><a name="p420595051780"></a><a name="p420595051780"></a>Actions</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.2.4.1.2 "><a name="ul732518295298"></a><a name="ul732518295298"></a><ul id="ul732518295298"><li><strong id="b4794124413212"><a name="b4794124413212"></a><a name="b4794124413212"></a>Include</strong> or <strong id="b479513445217"><a name="b479513445217"></a><a name="b479513445217"></a>Exclude</strong></li><li>For details about the actions, see <a href="actions.md#section387654045518">Actions Related to Objects</a>.</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="45.45454545454546%" headers="mcps1.2.4.1.3 "><p id="p1916419183710"><a name="p1916419183710"></a><a name="p1916419183710"></a>Operation stated in the object policy.</p>
    <a name="ul13161219203711"></a><a name="ul13161219203711"></a><ul id="ul13161219203711"><li><strong id="obs_03_0051_b125261325103613"><a name="obs_03_0051_b125261325103613"></a><a name="obs_03_0051_b125261325103613"></a>Include</strong>: Specifies the actions on which the bucket policy takes effect.</li><li><strong id="obs_03_0051_b2084382816362"><a name="obs_03_0051_b2084382816362"></a><a name="obs_03_0051_b2084382816362"></a>Exclude</strong>: Specifies that on all except the specified actions the bucket policy takes effect.</li></ul>
    </td>
    </tr>
    <tr id="row8998688144542"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.1 "><p id="p57805116144542"><a name="p57805116144542"></a><a name="p57805116144542"></a>Conditions</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.2.4.1.2 "><a name="ul63480483323"></a><a name="ul63480483323"></a><ul id="ul63480483323"><li>Condition operator: For details, see <a href="conditions.md#table16670126115713">Table 1</a>.</li><li><strong id="b115271075253"><a name="b115271075253"></a><a name="b115271075253"></a>Key</strong>: For details, see <a href="conditions.md#table6707152645718">Table 2</a> and <a href="conditions.md#table14742526145718">Table 4</a>.</li><li><strong id="b799974262210"><a name="b799974262210"></a><a name="b799974262210"></a>Value</strong>: The entered value is associated with the key.</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="45.45454545454546%" headers="mcps1.2.4.1.3 "><p id="p1116019133714"><a name="p1116019133714"></a><a name="p1116019133714"></a>Condition for an object policy to take effect.</p>
    </td>
    </tr>
    </tbody>
    </table>

7.  Click  **OK**.

    After the object policy is configured successfully, it is displayed in the list under  **Custom Bucket Policies**.


