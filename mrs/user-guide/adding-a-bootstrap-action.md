# Adding a Bootstrap Action<a name="EN-US_TOPIC_0226028061"></a>

## Adding a Bootstrap Action When Creating a Cluster<a name="section12545411416"></a>

1.  Log in to the MRS management console.
2.  Click  **Create Cluster**. The  **Create Cluster**  page is displayed.
3.  On the  **Advanced Settings**  tab page, select  **Configure**. The  **Bootstrap Action**  tab page is displayed.
4.  On the  **Bootstrap Action**  tab page, click  **Add**. The page is displayed, as shown in the following figure.

    **Figure  1**  Adding a bootstrap action<a name="fig12747430134016"></a>  
    ![](figures/adding-a-bootstrap-action.png "adding-a-bootstrap-action")

    **Table  1**  Parameters

    <a name="table37491430154018"></a>
    <table><thead align="left"><tr id="row1574783017401"><th class="cellrowborder" valign="top" width="27%" id="mcps1.2.3.1.1"><p id="p1674723044017"><a name="p1674723044017"></a><a name="p1674723044017"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="73%" id="mcps1.2.3.1.2"><p id="p15747183094010"><a name="p15747183094010"></a><a name="p15747183094010"></a><strong id="b842352706134712"><a name="b842352706134712"></a><a name="b842352706134712"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row77471830174011"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.3.1.1 "><p id="p074793014020"><a name="p074793014020"></a><a name="p074793014020"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.3.1.2 "><p id="p15747133015400"><a name="p15747133015400"></a><a name="p15747133015400"></a>Name of a bootstrap action script</p>
    <p id="p11747230104016"><a name="p11747230104016"></a><a name="p11747230104016"></a>The value can contain only digits, letters, spaces, hyphens (-), and underscores (_) and cannot start with a space.</p>
    <p id="p2074714304407"><a name="p2074714304407"></a><a name="p2074714304407"></a>The value can contain 1 to 64 characters.</p>
    <div class="note" id="note874733015401"><a name="note874733015401"></a><a name="note874733015401"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p57475301403"><a name="p57475301403"></a><a name="p57475301403"></a>A name must be unique in the same cluster. You can set the same name for different clusters.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row374783034013"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.3.1.1 "><p id="p117472303401"><a name="p117472303401"></a><a name="p117472303401"></a>Script Path</p>
    </td>
    <td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.3.1.2 "><p id="p27472030104010"><a name="p27472030104010"></a><a name="p27472030104010"></a>Script path. The value can be an OBS bucket path or a local VM path.</p>
    <a name="ul107475303406"></a><a name="ul107475303406"></a><ul id="ul107475303406"><li>An OBS bucket path must start with <strong id="b842352706112621"><a name="b842352706112621"></a><a name="b842352706112621"></a>s3a://</strong> and end with <strong id="b842352706112629"><a name="b842352706112629"></a><a name="b842352706112629"></a>.sh</strong>. For example, the path of the example script for installing Zeppelin is as follows: s3a://mrs-samples-bootstrap-eu-de/zeppelin/zeppelin_install.sh</li><li>A local VM path must start with a slash (/) and end with <strong id="b842352706112916"><a name="b842352706112916"></a><a name="b842352706112916"></a>.sh</strong>. For example, the path of the example script for installing Zeppelin is as follows: /opt/bootstrap/zeppelin/zeppelin_install.sh</li></ul>
    </td>
    </tr>
    <tr id="row274823064014"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.3.1.1 "><p id="p8748183014016"><a name="p8748183014016"></a><a name="p8748183014016"></a>Execution Node</p>
    </td>
    <td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.3.1.2 "><p id="p474833019404"><a name="p474833019404"></a><a name="p474833019404"></a>Select a type of the node where the bootstrap action script is executed.</p>
    <div class="note" id="note4748530114019"><a name="note4748530114019"></a><a name="note4748530114019"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul7461220103311"></a><a name="ul7461220103311"></a><ul id="ul7461220103311"><li>If you select <strong id="b842352706113232"><a name="b842352706113232"></a><a name="b842352706113232"></a>Master</strong>, you can choose whether to run the script only on the active Master nodes by enabling or disabling the switch <a name="image188871133428"></a><a name="image188871133428"></a><span><img id="image188871133428" src="figures/icon_mrs_disable_hec-53.png"></span>.</li><li>If you enable it, the script runs only on the active Master nodes. If you disable it, the script runs on all Master nodes. This switch is disabled by default.</li></ul>
    </div></div>
    </td>
    </tr>
    <tr id="row27481330124012"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.3.1.1 "><p id="p3748103011406"><a name="p3748103011406"></a><a name="p3748103011406"></a>Parameters</p>
    </td>
    <td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.3.1.2 "><p id="p1748530194020"><a name="p1748530194020"></a><a name="p1748530194020"></a>Bootstrap action script parameters</p>
    </td>
    </tr>
    <tr id="row15749153054013"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.3.1.1 "><p id="p4748133094012"><a name="p4748133094012"></a><a name="p4748133094012"></a>Execution Time</p>
    </td>
    <td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.3.1.2 "><p id="p672101713338"><a name="p672101713338"></a><a name="p672101713338"></a>Select the time when the bootstrap action script is executed. Currently, the following two options are available: <strong id="b842352706114015"><a name="b842352706114015"></a><a name="b842352706114015"></a>Before component start</strong> and <strong id="b842352706114018"><a name="b842352706114018"></a><a name="b842352706114018"></a>After component start</strong></p>
    </td>
    </tr>
    <tr id="row474917307402"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.3.1.1 "><p id="p197493309403"><a name="p197493309403"></a><a name="p197493309403"></a>Action upon Failure</p>
    </td>
    <td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.3.1.2 "><div class="p" id="p1974915300402"><a name="p1974915300402"></a><a name="p1974915300402"></a>Whether to continue to execute subsequent scripts and create a cluster after the script fails to be executed.<div class="note" id="note4749183094012"><a name="note4749183094012"></a><a name="note4749183094012"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p147496308407"><a name="p147496308407"></a><a name="p147496308407"></a>You are advised to set this parameter to <strong id="b842352706114220"><a name="b842352706114220"></a><a name="b842352706114220"></a>Continue</strong> in the debugging phase so that the cluster can continue to be installed and started no matter whether the bootstrap action is successful.</p>
    </div></div>
    </div>
    </td>
    </tr>
    </tbody>
    </table>

5.  Click  **OK**.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >After the bootstrap action is successfully added, you can edit or delete it in the  **Operation**  column.  


## Adding an Automation Script on the Auto Scaling Page<a name="section1675203104312"></a>

1.  Log in to the MRS management console.
2.  Click  ![](figures/wwx437827-中软基础平台部-datasight-image-bbfbe22f-2a2d-4e1b-8f10-a7782fd1d3ed-54.png)in the upper left corner on the management console and select  **Region**  and  **Project**.
3.  Choose  **Clusters**  \>  **Active Clusters**, select a running cluster, and click its name to switch to the cluster details page.
4.  On the  **Nodes**  tab page, click  **Auto Scaling**  in the  **Operation**  column of the Task node group. The  **Auto Scaling**  page is displayed.
5.  Configure a resource plan.

    You can configure the resource plan to adjust the number of nodes, which affects the actual price. Therefore, exercise caution when performing this operation.

    Configuration procedure:

    1.  On the  **Auto Scaling**  page, enable  **Auto Scaling**.
    2.  Set  **Default Range**  to  **2-2**  for  **Node Range**.****  This indicates that the number of Task nodes is fixed to 2 beyond the time range specified in the resource plan.
    3.  Click  **Configure Node Range in a Specified Time Range**  under  **Default Range**.
    4.  Configure  **Time Range**  to  **07:00-13:00**, and  **Node Range**  to  **5-5**. This indicates that the number of Task nodes is fixed to 5 in the specified time range. For details about the parameters, see  [Table 2](using-auto-scaling-in-a-cluster.md#table1846575414619).

        You can click  **Configure Node Range in a Specified Time Range**  to configure multiple resource plans.

6.  \(Optional\) Configure an automation script.
    1.  In  **Automation Script**  of  **Advanced Settings**, click  **Add**. The  **Automation Script**  page is displayed.

    1.  Set the following parameters:  **Name**,  **Script Path**,  **Execution Node Type**,  **Parameter**,  **Execution Time**, and  **Action upon Failure**. For details about the parameters, see  [Table 3](using-auto-scaling-in-a-cluster.md#table15644113520578).
    2.  Click  **OK**  to save the automation script configurations.

7.  Select  **I agree to authorize MRS to scale out or in nodes based on the above policy**.
8.  Click  **OK**.

