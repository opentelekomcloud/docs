# Creating a Cron Job<a name="cce_01_0151"></a>

A  cron job  is a  short-lived job  that runs at a specified time. You can perform  time synchronization  for all active nodes at a fixed time point.

## Prerequisites<a name="s50bf087555b1437aa249c1259138706c"></a>

Nodes have been added. For more information, see  [Creating Nodes](creating-a-node.md). If  clusters  and  node  resources are available, skip this operation.

## Procedure<a name="s631f9f0386834b23ae6d1e4d19d53382"></a>

1.  \(Optional\) If you use a  private container image  to create your cron job, upload the container image to the image repository.

    For details, see  [Image Repository](image-repository.md).

2.  Log in to the CCE console. In the navigation pane, choose  **Workloads \> Cron Jobs**. Then, click  **Create Cron Job**_._
3.  Configure the basic cron job information listed in  [Table 1](#tfadd3a11520b424d9063fe347c9c8c46). The parameters marked with an asterisk \(\*\) are mandatory.

    **Table  1**  Basic cron job information

    <a name="tfadd3a11520b424d9063fe347c9c8c46"></a>
    <table><thead align="left"><tr id="r18c18c1a53de41548275e3d1a693371d"><th class="cellrowborder" valign="top" width="19.77%" id="mcps1.2.3.1.1"><p id="a88b4790b6aa74bfc9eb95386662ddebd"><a name="a88b4790b6aa74bfc9eb95386662ddebd"></a><a name="a88b4790b6aa74bfc9eb95386662ddebd"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="80.23%" id="mcps1.2.3.1.2"><p id="a958597fbe1df427a8adb7f8cd27f7ae3"><a name="a958597fbe1df427a8adb7f8cd27f7ae3"></a><a name="a958597fbe1df427a8adb7f8cd27f7ae3"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r56788b8cc82f49d290f64df3cc1dc0f3"><td class="cellrowborder" valign="top" width="19.77%" headers="mcps1.2.3.1.1 "><p id="a7ce6034eee6a45c4a2025b16a465af01"><a name="a7ce6034eee6a45c4a2025b16a465af01"></a><a name="a7ce6034eee6a45c4a2025b16a465af01"></a>* Job Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.23%" headers="mcps1.2.3.1.2 "><p id="a0c8ce3cf0d1348f9a9671b5175534afd"><a name="a0c8ce3cf0d1348f9a9671b5175534afd"></a><a name="a0c8ce3cf0d1348f9a9671b5175534afd"></a>Name of a new cron job. The name must be unique.</p>
    </td>
    </tr>
    <tr id="row15341125115344"><td class="cellrowborder" valign="top" width="19.77%" headers="mcps1.2.3.1.1 "><p id="a75643f9a614b4180b6b9404f503c5dfd"><a name="a75643f9a614b4180b6b9404f503c5dfd"></a><a name="a75643f9a614b4180b6b9404f503c5dfd"></a>* Cluster</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.23%" headers="mcps1.2.3.1.2 "><p id="a760cf36b9e3b4d168c5ea807b62896d2"><a name="a760cf36b9e3b4d168c5ea807b62896d2"></a><a name="a760cf36b9e3b4d168c5ea807b62896d2"></a>Cluster to which a new cron job belongs.</p>
    </td>
    </tr>
    <tr id="row1259861015571"><td class="cellrowborder" valign="top" width="19.77%" headers="mcps1.2.3.1.1 "><p id="p125066193578"><a name="p125066193578"></a><a name="p125066193578"></a>* Namespace</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.23%" headers="mcps1.2.3.1.2 "><p id="p2050991925711"><a name="p2050991925711"></a><a name="p2050991925711"></a>Namespace to which a cron job belongs. If you do not specify this parameter, the value <strong id="b28378323103254"><a name="b28378323103254"></a><a name="b28378323103254"></a>default</strong> is used by default.</p>
    </td>
    </tr>
    <tr id="rdc1b35b8ff3c4072a49b1da4db8f71e5"><td class="cellrowborder" valign="top" width="19.77%" headers="mcps1.2.3.1.1 "><p id="a26499db509ff4ab7a1ac006ca3a8746d"><a name="a26499db509ff4ab7a1ac006ca3a8746d"></a><a name="a26499db509ff4ab7a1ac006ca3a8746d"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.23%" headers="mcps1.2.3.1.2 "><p id="a49218e0435a24eb7bdfce65248bef274"><a name="a49218e0435a24eb7bdfce65248bef274"></a><a name="a49218e0435a24eb7bdfce65248bef274"></a>Description of a cron job.</p>
    </td>
    </tr>
    </tbody>
    </table>

4.  Click  **Next: Configure Timing Rule**.
5.  Set the scheduling rule.

    **Table  2**  Scheduling rule parameters

    <a name="t3c443d636816401eb8c228607c440faf"></a>
    <table><thead align="left"><tr id="rb7c79e2ffbb74c248bcef71ba9477eca"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.3.1.1"><p id="en-us_topic_0093532762_p72699752917"><a name="en-us_topic_0093532762_p72699752917"></a><a name="en-us_topic_0093532762_p72699752917"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="80%" id="mcps1.2.3.1.2"><p id="en-us_topic_0093532762_p9269379294"><a name="en-us_topic_0093532762_p9269379294"></a><a name="en-us_topic_0093532762_p9269379294"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r6305be1a630244bf81ac437522f31cf0"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0093532762_p162871332056"><a name="en-us_topic_0093532762_p162871332056"></a><a name="en-us_topic_0093532762_p162871332056"></a>* <span class="keyword" id="keyword66956724811736"><a name="keyword66956724811736"></a><a name="keyword66956724811736"></a>Concurrent Policy</span></p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="a1238035c6c934a228d56a1884594bf19"><a name="a1238035c6c934a228d56a1884594bf19"></a><a name="a1238035c6c934a228d56a1884594bf19"></a>The following policies are supported:</p>
    <a name="u8a387ed341d640999663e82cfc513fb5"></a><a name="u8a387ed341d640999663e82cfc513fb5"></a><ul id="u8a387ed341d640999663e82cfc513fb5"><li><span class="keyword" id="keyword86904001311738"><a name="keyword86904001311738"></a><a name="keyword86904001311738"></a>Forbid</span>: A new job cannot be created before the previous job is complete.</li><li><span class="keyword" id="keyword18304597411742"><a name="keyword18304597411742"></a><a name="keyword18304597411742"></a>Allow</span>: New cron jobs can be created continuously.</li><li><span class="keyword" id="keyword1432863011744"><a name="keyword1432863011744"></a><a name="keyword1432863011744"></a>Replace</span>: A new job replaces the previous job when it is time to create the job but the previous job is not complete.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0093532762_row8270974297"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="a86a31e64aad144e19e5df3d4e25158b9"><a name="a86a31e64aad144e19e5df3d4e25158b9"></a><a name="a86a31e64aad144e19e5df3d4e25158b9"></a>* <span class="keyword" id="keyword89073930811746"><a name="keyword89073930811746"></a><a name="keyword89073930811746"></a>Schedule</span></p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="aca0cc43e08524e1d86ab0896157991c5"><a name="aca0cc43e08524e1d86ab0896157991c5"></a><a name="aca0cc43e08524e1d86ab0896157991c5"></a>Time when a new cron job is executed.</p>
    </td>
    </tr>
    <tr id="row57993169"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p5369911316108"><a name="p5369911316108"></a><a name="p5369911316108"></a>Job Records</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p5466090716108"><a name="p5466090716108"></a><a name="p5466090716108"></a>You can set the number of jobs that are successfully executed or fail to be executed. The value <strong id="b59214552017"><a name="b59214552017"></a><a name="b59214552017"></a>0</strong> indicates that the number of reserved tasks is not limited.</p>
    </td>
    </tr>
    </tbody>
    </table>

6.  Click  **Next: Add Container**. On the  **Add Container**  tab page,
    1.  Click  **Select Container Image**  to select the image to be deployed.
        -   **My Images**: displays all image repositories you created.
        -   **Third-Party Images**: CCE allows you to create a job from any third-party image repository other than SWR. When you create a job using a third-party image, ensure that the node where the job is running can access public networks. For details about how to use a third-party image, see  [Using a Third-Party Image](using-a-third-party-image.md).
            -   If your image repository does not require authentication, set  **Secret Authentication**  to  **No**, enter an image address in  **Image Address**, and then click  **OK**.
            -   If your image repository must be  authenticated  \(account and password\), you need to create a key and then use a third-party image. For details, see  [Using a Third-Party Image](using-a-third-party-image.md).

        -   **Shared Images**: The images shared by other tenants using the SWR service are displayed here. You can create workloads based on the shared images.

    2.  Set image parameters.

        **Table  3**  Image parameters

        <a name="t7eeb89498d8449aaaf341f1d6441a1e6"></a>
        <table><thead align="left"><tr id="en-us_topic_0107283736_en-us_topic_0107283470_row0282348486"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.3.1.1"><p id="en-us_topic_0107283736_en-us_topic_0107283470_p3282147483"><a name="en-us_topic_0107283736_en-us_topic_0107283470_p3282147483"></a><a name="en-us_topic_0107283736_en-us_topic_0107283470_p3282147483"></a>Parameter</p>
        </th>
        <th class="cellrowborder" valign="top" width="77%" id="mcps1.2.3.1.2"><p id="en-us_topic_0107283736_en-us_topic_0107283470_p1828244144819"><a name="en-us_topic_0107283736_en-us_topic_0107283470_p1828244144819"></a><a name="en-us_topic_0107283736_en-us_topic_0107283470_p1828244144819"></a>Description</p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="en-us_topic_0107283736_en-us_topic_0107283470_row1844916557597"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0107283736_en-us_topic_0107283470_p182837474815"><a name="en-us_topic_0107283736_en-us_topic_0107283470_p182837474815"></a><a name="en-us_topic_0107283736_en-us_topic_0107283470_p182837474815"></a>Image</p>
        </td>
        <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0107283736_en-us_topic_0107283470_p3283134134820"><a name="en-us_topic_0107283736_en-us_topic_0107283470_p3283134134820"></a><a name="en-us_topic_0107283736_en-us_topic_0107283470_p3283134134820"></a>Name of the image. You can click <strong id="en-us_topic_0107283736_b84235270617012"><a name="en-us_topic_0107283736_b84235270617012"></a><a name="en-us_topic_0107283736_b84235270617012"></a>Change Image</strong> to update it.</p>
        </td>
        </tr>
        <tr id="en-us_topic_0107283736_en-us_topic_0107283470_row338117362515"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0107283736_en-us_topic_0107283470_p1038143616517"><a name="en-us_topic_0107283736_en-us_topic_0107283470_p1038143616517"></a><a name="en-us_topic_0107283736_en-us_topic_0107283470_p1038143616517"></a>* Image Version</p>
        </td>
        <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0107283736_p14236148133915"><a name="en-us_topic_0107283736_p14236148133915"></a><a name="en-us_topic_0107283736_p14236148133915"></a>Version of the image to be deployed.</p>
        </td>
        </tr>
        <tr id="en-us_topic_0107283736_en-us_topic_0107283470_row32839494813"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0107283736_en-us_topic_0107283470_p122831140486"><a name="en-us_topic_0107283736_en-us_topic_0107283470_p122831140486"></a><a name="en-us_topic_0107283736_en-us_topic_0107283470_p122831140486"></a>* Container Name</p>
        </td>
        <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0107283736_en-us_topic_0107283470_p528314415486"><a name="en-us_topic_0107283736_en-us_topic_0107283470_p528314415486"></a><a name="en-us_topic_0107283736_en-us_topic_0107283470_p528314415486"></a>Name of the container. You can modify it.</p>
        </td>
        </tr>
        <tr id="en-us_topic_0107283736_en-us_topic_0107283470_row152831345485"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0107283736_en-us_topic_0107283470_p875325925918"><a name="en-us_topic_0107283736_en-us_topic_0107283470_p875325925918"></a><a name="en-us_topic_0107283736_en-us_topic_0107283470_p875325925918"></a>Container Resources</p>
        </td>
        <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><div class="p" id="en-us_topic_0107283736_en-us_topic_0107283470_p1825119142351"><a name="en-us_topic_0107283736_en-us_topic_0107283470_p1825119142351"></a><a name="en-us_topic_0107283736_en-us_topic_0107283470_p1825119142351"></a>For more information about <strong id="en-us_topic_0107283736_b1672210449245"><a name="en-us_topic_0107283736_b1672210449245"></a><a name="en-us_topic_0107283736_b1672210449245"></a>Request</strong> and <strong id="en-us_topic_0107283736_b5722194432420"><a name="en-us_topic_0107283736_b5722194432420"></a><a name="en-us_topic_0107283736_b5722194432420"></a>Limit</strong>, see <a href="setting-container-specifications.md">Setting Container Specifications</a>.<a name="en-us_topic_0107283736_en-us_topic_0107283470_ul1674183414114"></a><a name="en-us_topic_0107283736_en-us_topic_0107283470_ul1674183414114"></a><ul id="en-us_topic_0107283736_en-us_topic_0107283470_ul1674183414114"><li><strong id="en-us_topic_0107283736_b1834123719193"><a name="en-us_topic_0107283736_b1834123719193"></a><a name="en-us_topic_0107283736_b1834123719193"></a>Request</strong>: the amount of resources that CCE will guarantee to a container.</li><li><strong id="en-us_topic_0107283736_b842352706161350"><a name="en-us_topic_0107283736_b842352706161350"></a><a name="en-us_topic_0107283736_b842352706161350"></a>Limit</strong>: If a container is overloaded, the system may be faulty. To avoid this situation, set the maximum limits for the container resource quota to ensure that container resources do not exceed the limits.</li><li>GPU settings:<div class="note" id="en-us_topic_0107283736_en-us_topic_0107283470_note118204916050"><a name="en-us_topic_0107283736_en-us_topic_0107283470_note118204916050"></a><a name="en-us_topic_0107283736_en-us_topic_0107283470_note118204916050"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0107283736_en-us_topic_0107283470_p1063844316050"><a name="en-us_topic_0107283736_en-us_topic_0107283470_p1063844316050"></a><a name="en-us_topic_0107283736_en-us_topic_0107283470_p1063844316050"></a>GPU can be configured only when the cluster contains GPU nodes.</p>
        </div></div>
        <a name="en-us_topic_0107283736_en-us_topic_0107283470_ul2409689116041"></a><a name="en-us_topic_0107283736_en-us_topic_0107283470_ul2409689116041"></a><ul id="en-us_topic_0107283736_en-us_topic_0107283470_ul2409689116041"><li>GPU quota: Select <span class="uicontrol" id="en-us_topic_0107283736_uicontrol93352013121413"><a name="en-us_topic_0107283736_uicontrol93352013121413"></a><a name="en-us_topic_0107283736_uicontrol93352013121413"></a><b>Use</b></span> and set the percentage. For example, if this parameter is set to 10%, the container is allowed to use 10% of GPU resources. If you do not select <span class="uicontrol" id="en-us_topic_0107283736_uicontrol16417155441419"><a name="en-us_topic_0107283736_uicontrol16417155441419"></a><a name="en-us_topic_0107283736_uicontrol16417155441419"></a><b>Use</b></span> or set this parameter to 0, no GPU resources can be used.</li><li>GPU/Graphics Card: If <strong id="en-us_topic_0107283736_b11611829191320"><a name="en-us_topic_0107283736_b11611829191320"></a><a name="en-us_topic_0107283736_b11611829191320"></a>Any GPU type</strong> is selected, the container uses a random GPU in the node. If you select a specific GPU, the container uses this GPU.</li></ul>
        </li></ul>
        </div>
        </td>
        </tr>
        </tbody>
        </table>

    3.  \(Optional\) Perform advanced settings.

        **Table  4**  Advanced settings

        <a name="tf56c7b65fd00476dbf686d494609ec01"></a>
        <table><thead align="left"><tr id="rd70607f9bfa74a83a6e424e8abda265c"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.3.1.1"><p id="a85705044d3104d34957e244b20e98de2"><a name="a85705044d3104d34957e244b20e98de2"></a><a name="a85705044d3104d34957e244b20e98de2"></a>Parameter</p>
        </th>
        <th class="cellrowborder" valign="top" width="77%" id="mcps1.2.3.1.2"><p id="ab80a0aae28b54ab1afe9009e2466b2e6"><a name="ab80a0aae28b54ab1afe9009e2466b2e6"></a><a name="ab80a0aae28b54ab1afe9009e2466b2e6"></a>Description</p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="r616e69d5a2004b079888d8a4a2a83762"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="ae1906e2a0f4e48c8a290d2ffdc9e83bf"><a name="ae1906e2a0f4e48c8a290d2ffdc9e83bf"></a><a name="ae1906e2a0f4e48c8a290d2ffdc9e83bf"></a>Lifecycle</p>
        </td>
        <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><div class="p" id="p35489275239"><a name="p35489275239"></a><a name="p35489275239"></a>Actions defined in the lifecycle script definition are taken for the lifecycle events of container tasks.<a name="u86a34d59537a4e5ebbcd8d62f0fb6fc7"></a><a name="u86a34d59537a4e5ebbcd8d62f0fb6fc7"></a><ul id="u86a34d59537a4e5ebbcd8d62f0fb6fc7"><li><strong id="b24794299110119"><a name="b24794299110119"></a><a name="b24794299110119"></a>Start Command</strong>: If you enter a container startup command, the command is immediately executed after the container starts. For details, see <a href="advanced-container-settings.md">Advanced Container Settings</a>.</li><li><strong id="b797546874101115"><a name="b797546874101115"></a><a name="b797546874101115"></a>Post-Start</strong>: The command is triggered after a job starts. For details, see <a href="setting-container-lifecycle-parameters.md">Setting Container Lifecycle Parameters</a>.</li><li><strong id="b715570416101125"><a name="b715570416101125"></a><a name="b715570416101125"></a>Pre-Stop</strong>: The command is triggered before a job is stopped. For details, see <a href="setting-container-lifecycle-parameters.md">Setting Container Lifecycle Parameters</a>.</li></ul>
        </div>
        </td>
        </tr>
        <tr id="r159688429d2c4ad5b55d2b63b5bc6a46"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="acab0841bbf1548e08722d5ec9fb378e9"><a name="acab0841bbf1548e08722d5ec9fb378e9"></a><a name="acab0841bbf1548e08722d5ec9fb378e9"></a>Environment Variables</p>
        </td>
        <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><div class="p" id="p19408181613184"><a name="p19408181613184"></a><a name="p19408181613184"></a>Environment variables can be added to a container. In general, environment variables are used to set parameters. On the <strong id="b14284216151619"><a name="b14284216151619"></a><a name="b14284216151619"></a>Environment Variables</strong> tab page, click <strong id="b1928451611610"><a name="b1928451611610"></a><a name="b1928451611610"></a>Add Environment Variable</strong>. Currently, environment variables can be added using any of the following methods:<a name="ul145379401817"></a><a name="ul145379401817"></a><ul id="ul145379401817"><li><strong id="b284992934420"><a name="b284992934420"></a><a name="b284992934420"></a>Added manually</strong>: Set <strong id="b88501129194417"><a name="b88501129194417"></a><a name="b88501129194417"></a>Variable Name</strong> and <strong id="b6850162964413"><a name="b6850162964413"></a><a name="b6850162964413"></a>Variable Value/Reference</strong>.</li><li><strong id="b19672134174410"><a name="b19672134174410"></a><a name="b19672134174410"></a>Added from secret</strong>: Set <strong id="b146731634184410"><a name="b146731634184410"></a><a name="b146731634184410"></a>Variable Name</strong> and select the desired secret name and data. The prerequisite of this method is that a secret has been created. For details, see <a href="creating-a-secret.md">Creating a Secret</a>.</li><li><strong id="b0260959833"><a name="b0260959833"></a><a name="b0260959833"></a>Added from configmap</strong>: Set <strong id="b11582102918515"><a name="b11582102918515"></a><a name="b11582102918515"></a>Variable Name</strong> and select the desired ConfigMap name and data. The prerequisite of this method is that a ConfigMap has been created. For details, see <a href="creating-a-configmap.md">Creating a ConfigMap</a>.</li></ul>
        </div>
        </td>
        </tr>
        </tbody>
        </table>

    4.  \(Optional\) One cron job instance contains one or more related containers. If your cron job contains multiple containers, click  **Add Container**  to add containers.

7.  Click  **Create**.

    If the status is  **Started**, the cron job has been created successfully.


## Using kubectl<a name="section13519162224919"></a>

A cron job has the following configuration parameters:

-   **.spec.schedule**: takes a  [Cron](https://en.wikipedia.org/wiki/Cron)  format string, for example,  **0**  \* \* \* \* or  **@hourly**, as schedule time of jobs to be created and executed.
-   **.spec.jobTemplate**: specifies jobs to be run, and has exactly the same schema as when you are  [Creating a Job Using kubectl](creating-a-job.md#section450152719412).
-   **.spec.startingDeadlineSeconds**: specifies the deadline for starting a job.
-   **.spec.concurrencyPolicy**: specifies how to treat concurrent executions of a job created by the Cron job. The following options are supported:
    -   **Allow**  \(default value\): allows concurrently running jobs.
    -   **Forbid**: forbids concurrent runs, skipping next run if previous has not finished yet.
    -   **Replace**: cancels the currently running job and replaces it with a new one.


The following is an example cron job, which is saved in the  **cronjob.yaml**  file.

```
apiVersion: batch/v2alpha1
kind: CronJob
metadata:
  name: hello
spec:
  schedule: "*/1 * * * *"
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: hello
            image: busybox
            args:
            - /bin/sh
            - -c
            - date; echo Hello from the Kubernetes cluster
          restartPolicy: OnFailure
```

1.  Run the following command to create a cron job

    **kubectl create -f cronjob.yaml**

    Information similar to the following is displayed:

    ```
    cronjob "hello" created
    ```

2.  Run the following commands to view the running status of the cron job:

    **kubectl get cronjob**

    ```
    NAME      SCHEDULE      SUSPEND   ACTIVE    LAST-SCHEDULE
    hello     */1 * * * *   False     0         <none>
    ```

    **kubectl get jobs**

    ```
    NAME               DESIRED   SUCCESSFUL   AGE
    hello-1202039034   1         1            49s
    $ pods=$(kubectl get pods --selector=job-name=hello-1202039034 --output=jsonpath={.items..metadata.name} -a)
    ```

    **kubectl logs $pods**

    ```
    Mon Aug 29 21:34:09 UTC 2016
    Hello from the Kubernetes cluster
    ```

    **kubectl delete cronjob hello**

    ```
    cronjob "hello" deleted
    ```

    >![](public_sys-resources/icon-notice.gif) **NOTICE:**   
    >Deleting a cron job will not automatically delete its jobs. You can delete the jobs by running the  **kubectl delete job**  command.  


## Related Operations<a name="s28175da725cf46d49a4cfca59155a5d2"></a>

After a cron job is created, you can perform operations listed in  [Table 5](#t6d520710097a4ee098eae42bcb508608).

**Table  5**  Other operations

<a name="t6d520710097a4ee098eae42bcb508608"></a>
<table><thead align="left"><tr id="r8d59bf3aa5394e84ae626a36c585013d"><th class="cellrowborder" valign="top" width="28.999999999999996%" id="mcps1.2.3.1.1"><p id="a8245dffabcbf4810a7333d8ce9a67789"><a name="a8245dffabcbf4810a7333d8ce9a67789"></a><a name="a8245dffabcbf4810a7333d8ce9a67789"></a>Operation</p>
</th>
<th class="cellrowborder" valign="top" width="71%" id="mcps1.2.3.1.2"><p id="en-us_topic_0093532762_p685713442569"><a name="en-us_topic_0093532762_p685713442569"></a><a name="en-us_topic_0093532762_p685713442569"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row82414466296"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.3.1.1 "><p id="p147711757162810"><a name="p147711757162810"></a><a name="p147711757162810"></a>Viewing a YAML file</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.3.1.2 "><p id="p15771257142816"><a name="p15771257142816"></a><a name="p15771257142816"></a>Click <strong id="b84235270611943"><a name="b84235270611943"></a><a name="b84235270611943"></a>More</strong> &gt; <strong id="b84235270611958"><a name="b84235270611958"></a><a name="b84235270611958"></a>View YAML</strong> next to the cron job name to view the YAML file of the current job.</p>
</td>
</tr>
<tr id="r25f2ff5451494127b1af5ab34b807936"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.3.1.1 "><p id="a6abaef816404455581dc7dbaddf656ee"><a name="a6abaef816404455581dc7dbaddf656ee"></a><a name="a6abaef816404455581dc7dbaddf656ee"></a>Stopping a cron job</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.3.1.2 "><a name="obe7516d58ade42a389e52e27f663e03d"></a><a name="obe7516d58ade42a389e52e27f663e03d"></a><ol id="obe7516d58ade42a389e52e27f663e03d"><li>Select the job to be stopped and click <strong id="b842352706102439"><a name="b842352706102439"></a><a name="b842352706102439"></a>Stop</strong> in the <strong id="b12271357184317"><a name="b12271357184317"></a><a name="b12271357184317"></a>Operation</strong> column.</li><li>Click <strong id="a14b4819ca5b74b27beebaa7cc918e410"><a name="a14b4819ca5b74b27beebaa7cc918e410"></a><a name="a14b4819ca5b74b27beebaa7cc918e410"></a>OK</strong>.</li></ol>
</td>
</tr>
<tr id="r9fec8c34ebbb44e3888c677862a174e0"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0093532762_p685874410564"><a name="en-us_topic_0093532762_p685874410564"></a><a name="en-us_topic_0093532762_p685874410564"></a>Deleting a cron job</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.3.1.2 "><a name="o9409a54b32c14e4799c05e5f0a643633"></a><a name="o9409a54b32c14e4799c05e5f0a643633"></a><ol id="o9409a54b32c14e4799c05e5f0a643633"><li>Select the cron job to be deleted and click <strong id="b842352706111124"><a name="b842352706111124"></a><a name="b842352706111124"></a>More</strong> &gt; <strong id="b842352706111132"><a name="b842352706111132"></a><a name="b842352706111132"></a>Delete</strong> in the <strong id="b842352706111135"><a name="b842352706111135"></a><a name="b842352706111135"></a>Operation</strong> column.</li><li>Click <strong id="a14b4819ca5b74b27beebaa7cc918e410_1"><a name="a14b4819ca5b74b27beebaa7cc918e410_1"></a><a name="a14b4819ca5b74b27beebaa7cc918e410_1"></a>OK</strong>.<p id="a3be1d4db3fa4464dbc950b89a31d57aa"><a name="a3be1d4db3fa4464dbc950b89a31d57aa"></a><a name="a3be1d4db3fa4464dbc950b89a31d57aa"></a>Deleted jobs cannot be restored. Therefore, exercise caution when deleting a job.</p>
</li></ol>
</td>
</tr>
</tbody>
</table>

