# Modifying a Log Transfer Task<a name="lts_01_0025"></a>

## Scenarios<a name="section48277357143234"></a>

This section describes how to modify a log transfer task. You can modify the log topic, Object Storage Service \(OBS\) bucket, log prefix, and status of the transfer task.

## Prerequisites<a name="section29149019143234"></a>

-   You have created a log group.
-   You have created a log topic.
-   You have configured a log transfer task.

## Procedure<a name="section674884143234"></a>

1.  Log in to the management console.
2.  In the upper left corner of the management console, select the target region and project.
3.  Click  **Service List**  and choose  **Management & Deployment**  \>  **Log Tank Service**.
4.  In the navigation pane on the left, choose  **Log Transfer**.

    **Figure  1**  Log transfer page<a name="fig10633138191818"></a>  
    ![](figures/log-transfer-page.png "log-transfer-page")

5.  In the log transfer task list, locate the target transfer task and click  **Modify**  in the  **Operation**  column.

    The  **Modify Log Transfer**  page is displayed.

    **Figure  2**  Modifying parameters for a log transfer task<a name="fig1162012511176"></a>  
    ![](figures/modifying-parameters-for-a-log-transfer-task.png "modifying-parameters-for-a-log-transfer-task")

6.  Modify the transfer task by following the instructions in  [Table 1](#table23279244163823).

    **Table  1**  Modification description

    <a name="table23279244163823"></a>
    <table><thead align="left"><tr id="r9b320f28ba1e4d1881bb20480d66c1ea"><th class="cellrowborder" valign="top" width="21.25%" id="mcps1.2.4.1.1"><p id="a0ea6aa344b064411bb5c115e4aa4510a"><a name="a0ea6aa344b064411bb5c115e4aa4510a"></a><a name="a0ea6aa344b064411bb5c115e4aa4510a"></a><strong id="b84235270610452"><a name="b84235270610452"></a><a name="b84235270610452"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="65.14%" id="mcps1.2.4.1.2"><p id="ad5be5ab358f74da49122bbdc3ad7d469"><a name="ad5be5ab358f74da49122bbdc3ad7d469"></a><a name="ad5be5ab358f74da49122bbdc3ad7d469"></a><strong id="b84235270681846"><a name="b84235270681846"></a><a name="b84235270681846"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="13.61%" id="mcps1.2.4.1.3"><p id="p4639182717443"><a name="p4639182717443"></a><a name="p4639182717443"></a><strong id="b1330392512497"><a name="b1330392512497"></a><a name="b1330392512497"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r77bd0944864c4dad9cee530dd8208dc3"><td class="cellrowborder" valign="top" width="21.25%" headers="mcps1.2.4.1.1 "><p id="ac0c92b549e104e139e0db38aed340f01"><a name="ac0c92b549e104e139e0db38aed340f01"></a><a name="ac0c92b549e104e139e0db38aed340f01"></a>Log Topic Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="65.14%" headers="mcps1.2.4.1.2 "><p id="a240655ed6e1f4c2da2fff23dd6a09565"><a name="a240655ed6e1f4c2da2fff23dd6a09565"></a><a name="a240655ed6e1f4c2da2fff23dd6a09565"></a>Select the log topic that you have created.</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.61%" headers="mcps1.2.4.1.3 "><p id="p34907356539"><a name="p34907356539"></a><a name="p34907356539"></a>LogTopic1</p>
    </td>
    </tr>
    <tr id="rd56087b2bbd142788d2dbb5eb3df3d93"><td class="cellrowborder" valign="top" width="21.25%" headers="mcps1.2.4.1.1 "><p id="aa7487ba807314096994ee93e13f561d3"><a name="aa7487ba807314096994ee93e13f561d3"></a><a name="aa7487ba807314096994ee93e13f561d3"></a>OBS Bucket</p>
    </td>
    <td class="cellrowborder" valign="top" width="65.14%" headers="mcps1.2.4.1.2 "><p id="a5963b1b4b93442548e64574bb49bcdc9"><a name="a5963b1b4b93442548e64574bb49bcdc9"></a><a name="a5963b1b4b93442548e64574bb49bcdc9"></a>Select the desired OBS bucket.</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.61%" headers="mcps1.2.4.1.3 "><p id="p1824719285386"><a name="p1824719285386"></a><a name="p1824719285386"></a>obs-8a09</p>
    </td>
    </tr>
    <tr id="ra149c1a748234fbf87a1106cfafd1938"><td class="cellrowborder" valign="top" width="21.25%" headers="mcps1.2.4.1.1 "><p id="a4b5e1888f9e248288cf474cff2c6dcd6"><a name="a4b5e1888f9e248288cf474cff2c6dcd6"></a><a name="a4b5e1888f9e248288cf474cff2c6dcd6"></a>Log Prefix</p>
    </td>
    <td class="cellrowborder" valign="top" width="65.14%" headers="mcps1.2.4.1.2 "><p id="a3aa402c2a32c4ff8bb750e1fccc49af8"><a name="a3aa402c2a32c4ff8bb750e1fccc49af8"></a><a name="a3aa402c2a32c4ff8bb750e1fccc49af8"></a>Enter a prefix as required.</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.61%" headers="mcps1.2.4.1.3 "><p id="p196391727124416"><a name="p196391727124416"></a><a name="p196391727124416"></a>LTS</p>
    </td>
    </tr>
    <tr id="row744818185414"><td class="cellrowborder" valign="top" width="21.25%" headers="mcps1.2.4.1.1 "><p id="p1777144217712"><a name="p1777144217712"></a><a name="p1777144217712"></a>Format</p>
    </td>
    <td class="cellrowborder" valign="top" width="65.14%" headers="mcps1.2.4.1.2 "><p id="p147776421778"><a name="p147776421778"></a><a name="p147776421778"></a>Select <strong id="b0367258103919"><a name="b0367258103919"></a><a name="b0367258103919"></a>Raw Log Format</strong> or <strong id="b203686585399"><a name="b203686585399"></a><a name="b203686585399"></a>JSON</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.61%" headers="mcps1.2.4.1.3 "><p id="p126391627174410"><a name="p126391627174410"></a><a name="p126391627174410"></a>JSON</p>
    </td>
    </tr>
    <tr id="r74f80a2ec0794d0cbec96aa11f8600ca"><td class="cellrowborder" valign="top" width="21.25%" headers="mcps1.2.4.1.1 "><p id="a65ab7d15967f4de0b469b1859a1be77b"><a name="a65ab7d15967f4de0b469b1859a1be77b"></a><a name="a65ab7d15967f4de0b469b1859a1be77b"></a>Transfer Log to OBS</p>
    </td>
    <td class="cellrowborder" valign="top" width="65.14%" headers="mcps1.2.4.1.2 "><p id="a2d59b0e3d7ca4fb7ada2a1f21ac80605"><a name="a2d59b0e3d7ca4fb7ada2a1f21ac80605"></a><a name="a2d59b0e3d7ca4fb7ada2a1f21ac80605"></a>Enable or disable log transfer.</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.61%" headers="mcps1.2.4.1.3 "><p id="p763913274445"><a name="p763913274445"></a><a name="p763913274445"></a>Enable</p>
    </td>
    </tr>
    <tr id="row14902102212341"><td class="cellrowborder" valign="top" width="21.25%" headers="mcps1.2.4.1.1 "><p id="p890332253419"><a name="p890332253419"></a><a name="p890332253419"></a>Log Transfer Interval</p>
    </td>
    <td class="cellrowborder" valign="top" width="65.14%" headers="mcps1.2.4.1.2 "><p id="p1490362210344"><a name="p1490362210344"></a><a name="p1490362210344"></a>Specifies the interval, in the unit of seconds, at which logs are automatically transferred to the OBS bucket. The default value is 120.</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.61%" headers="mcps1.2.4.1.3 "><p id="p20639427204415"><a name="p20639427204415"></a><a name="p20639427204415"></a>120</p>
    </td>
    </tr>
    </tbody>
    </table>

7.  Click  **OK**.

