# Creating a Workload from a Chart<a name="cce_01_0146"></a>

## Creating a Chart-based Workload<a name="s94388d41fe234fba81844802bc682fb8"></a>

1.  Log in to the CCE console. In the navigation pane, choose  **Charts**  \>  **Uploaded Charts**.
2.  In the list of uploaded charts, click  **Install Chart**.
3.  Set the installation parameters listed in  [Table 1](#t26bc1c499f114b5185e5edcf61e44d95). The parameters marked with an asterisk \(\*\) are mandatory.

    **Table  1**  Installation parameters

    <a name="t26bc1c499f114b5185e5edcf61e44d95"></a>
    <table><thead align="left"><tr id="rbf609a3fcf2445d2b6d59cbcca7f75b3"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.3.1.1"><p id="a24b59ed54e3e49a7abefd7528912fb26"><a name="a24b59ed54e3e49a7abefd7528912fb26"></a><a name="a24b59ed54e3e49a7abefd7528912fb26"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="77%" id="mcps1.2.3.1.2"><p id="a48e24994d5e7491782edce936fd59c1a"><a name="a48e24994d5e7491782edce936fd59c1a"></a><a name="a48e24994d5e7491782edce936fd59c1a"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r4199465b1b1a4b31b17eac511ff9c594"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="a010899bea1f349bdad1eef099e4fa486"><a name="a010899bea1f349bdad1eef099e4fa486"></a><a name="a010899bea1f349bdad1eef099e4fa486"></a>* Release Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="a0153652b843848a3b6bdad99e3c3b39f"><a name="a0153652b843848a3b6bdad99e3c3b39f"></a><a name="a0153652b843848a3b6bdad99e3c3b39f"></a>Unique name of the chart release.</p>
    </td>
    </tr>
    <tr id="re1bc8a3557e9484baa79c65dc200a4b1"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="a634af1e2910741f1912518b3bfec7389"><a name="a634af1e2910741f1912518b3bfec7389"></a><a name="a634af1e2910741f1912518b3bfec7389"></a>* Chart Version</p>
    </td>
    <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="ac38c5df873f6444b981b35885f8eef62"><a name="ac38c5df873f6444b981b35885f8eef62"></a><a name="ac38c5df873f6444b981b35885f8eef62"></a>Chart version by default.</p>
    </td>
    </tr>
    <tr id="rbe9ab58d5e67480aa6e422ef627d53a3"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="a951eab31ec67431facfacf0c7a30e58b"><a name="a951eab31ec67431facfacf0c7a30e58b"></a><a name="a951eab31ec67431facfacf0c7a30e58b"></a>* Cluster</p>
    </td>
    <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="a7d5ca4f0299b4ff59ab86cbca0c02d38"><a name="a7d5ca4f0299b4ff59ab86cbca0c02d38"></a><a name="a7d5ca4f0299b4ff59ab86cbca0c02d38"></a><span class="keyword" id="keyword53828804114919"><a name="keyword53828804114919"></a><a name="keyword53828804114919"></a>Cluster</span> where the workload will be deployed.</p>
    </td>
    </tr>
    <tr id="rbd79869126dd476ba89ebd3a3103af0c"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0093297948_p441405163731"><a name="en-us_topic_0093297948_p441405163731"></a><a name="en-us_topic_0093297948_p441405163731"></a>* Namespace</p>
    </td>
    <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="a29df703802f0429a96ce7e488e7b6376"><a name="a29df703802f0429a96ce7e488e7b6376"></a><a name="a29df703802f0429a96ce7e488e7b6376"></a>Namespace to which the workload will be deployed.</p>
    </td>
    </tr>
    <tr id="r70f26452e7574784b0bcc4fa28655e23"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="ae76aa7c5d99b4e378bf694b82b9e5dc5"><a name="ae76aa7c5d99b4e378bf694b82b9e5dc5"></a><a name="ae76aa7c5d99b4e378bf694b82b9e5dc5"></a>Advanced Settings</p>
    </td>
    <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="a303f5e86580c4fa29c238785c98ea8ce"><a name="a303f5e86580c4fa29c238785c98ea8ce"></a><a name="a303f5e86580c4fa29c238785c98ea8ce"></a>You can import and replace the <strong id="b842352706155915"><a name="b842352706155915"></a><a name="b842352706155915"></a>values.yaml</strong> file or directly edit the chart parameters online.</p>
    <div class="note" id="na1d8e395109d472699025c5118ef563d"><a name="na1d8e395109d472699025c5118ef563d"></a><a name="na1d8e395109d472699025c5118ef563d"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p class="textintable" id="a428d67dfa7aa45e99ea2cc24c467e433"><a name="a428d67dfa7aa45e99ea2cc24c467e433"></a><a name="a428d67dfa7aa45e99ea2cc24c467e433"></a>An imported <strong id="b842352706155923"><a name="b842352706155923"></a><a name="b842352706155923"></a>values.yaml</strong> file must comply with YAML specifications, that is, KEY:VALUE format. The fields in the file are not restricted.</p>
    <p id="p112003015566"><a name="p112003015566"></a><a name="p112003015566"></a>The key value of the imported values.yaml must be the same as that of the selected chart package. Otherwise, the values.yaml does not take effect. That is, the key cannot be changed.</p>
    </div></div>
    <a name="o62d8e522faae46b79e270230405ddf10"></a><a name="o62d8e522faae46b79e270230405ddf10"></a><ol id="o62d8e522faae46b79e270230405ddf10"><li>Click <strong id="b842352706121548"><a name="b842352706121548"></a><a name="b842352706121548"></a>Import Configuration File</strong>.</li><li>Select the corresponding <strong id="b84235270616012"><a name="b84235270616012"></a><a name="b84235270616012"></a>values.yaml</strong> file and click <strong id="b842352706121623"><a name="b842352706121623"></a><a name="b842352706121623"></a>Open</strong>.</li></ol>
    </td>
    </tr>
    </tbody>
    </table>

4.  After the configuration is complete, click  **Next**.
5.  Confirm the configuration and click  **Submit**.
6.  Click  **Back to Release List**  to view the running status of the chart-based workload, or click  **Go to Release Details**  to view details about the chart-based workload.

## Upgrading a Chart-based Workload<a name="section5324101171010"></a>

1.  Log in to the CCE console. In the navigation pane, choose  **Charts**  \>  **Uploaded Charts**. Then click the  **Releases**  tab.
2.  Click  **Upgrade**  in the row where the desired workload resides and set the parameters for the workload.
3.  Select a chart version for  **Chart Version**.
4.  Follow the prompts to modify the chart parameters.
5.  Select an upgrade mode.
    -   If no more configuration is required, click  **Upgrade at One Click**.
    -   To change the access mode, click  **Upgrade**. For details about how to set the access mode, see  [Network Management](network-management.md). Click  **Next**  and then click  **Submit**.

6.  Click  **Back to Release List**. If the chart status changes to  **Upgrade successful**, the workload is successfully upgraded.

## Rolling Back a Chart-based Workload<a name="section13251511191012"></a>

1.  Log in to the CCE console. In the navigation pane, choose  **Charts**  \>  **Uploaded Charts**. Then click the  **Releases**  tab.
2.  Click  **More**  \>  **Roll Back**  for the workload to be rolled back, select the workload version, and click  **Roll back** **to this version**.

    In the workload list, if the status is  **Rollback successful**, the workload is rolled back successfully.


## Uninstalling a Chart-based Workload<a name="section15325151161011"></a>

1.  Log in to the CCE console. In the navigation pane, choose  **Charts**  \>  **Uploaded Charts**. Then click the  **Releases**  tab.
2.  Click  **More**  \>  **Uninstall**  next to the release to be uninstalled, and click  **OK**. Exercise caution when performing this operation because releases cannot be restored after being uninstalled.

