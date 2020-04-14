# Creating a Log Transfer Task<a name="lts_01_0023"></a>

## Scenarios<a name="section6114814810429"></a>

This section describes how to create a log transfer task. Logs uploaded to LTS can be stored for seven days. To store the logs for a longer period of time, you can transfer them to an OBS bucket.

## Prerequisites<a name="section61878755104447"></a>

-   You have created a log group.

-   You have created a log topic.
-   You have created an OBS bucket.

## Procedure<a name="section378185018292"></a>

1.  Log in to the management console.
2.  In the upper left corner of the management console, select the target region and project.
3.  Click  **Service List**  and choose  **Management & Deployment**  \>  **Log Tank Service**.

1.  In the navigation pane on the left, choose  **Log Transfer**.

    **Figure  1**  Create Log Transfer<a name="fig129031841175410"></a>  
    ![](figures/create-log-transfer.png "create-log-transfer")

2.  On the displayed page, click  **Create Log Transfer**.

    **Figure  2**  Create Log Transfer<a name="fig85471646319"></a>  
    ![](figures/create-log-transfer-4.png "create-log-transfer-4")

3.  On the displayed page, configure parameters.

    **Table  1**  Parameters description

    <a name="table15492133314293"></a>
    <table><thead align="left"><tr id="row54892335297"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.4.1.1"><p id="p14897331294"><a name="p14897331294"></a><a name="p14897331294"></a><strong id="b1461839183618"><a name="b1461839183618"></a><a name="b1461839183618"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="71%" id="mcps1.2.4.1.2"><p id="p04891033132914"><a name="p04891033132914"></a><a name="p04891033132914"></a><strong id="b84235270681846"><a name="b84235270681846"></a><a name="b84235270681846"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="12%" id="mcps1.2.4.1.3"><p id="p1824672863818"><a name="p1824672863818"></a><a name="p1824672863818"></a><strong id="b762613816428"><a name="b762613816428"></a><a name="b762613816428"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row134891433122913"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="p44891433112912"><a name="p44891433112912"></a><a name="p44891433112912"></a>Log Group Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.2 "><p id="p11489733182916"><a name="p11489733182916"></a><a name="p11489733182916"></a>Specifies the log group name. Select a created log group.</p>
    </td>
    <td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.3 "><p id="p7805113317136"><a name="p7805113317136"></a><a name="p7805113317136"></a>lts-group-wule</p>
    </td>
    </tr>
    <tr id="row049063313297"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="p11489163315292"><a name="p11489163315292"></a><a name="p11489163315292"></a>Log Topic</p>
    </td>
    <td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.2 "><p id="p1149013382915"><a name="p1149013382915"></a><a name="p1149013382915"></a>Specifies the log topic name. Select a created log topic.</p>
    </td>
    <td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.3 "><p id="p34907356539"><a name="p34907356539"></a><a name="p34907356539"></a>LogTopic1</p>
    </td>
    </tr>
    <tr id="row04902333298"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="p15490533112910"><a name="p15490533112910"></a><a name="p15490533112910"></a>OBS Bucket</p>
    </td>
    <td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.2 "><p id="p11490833182919"><a name="p11490833182919"></a><a name="p11490833182919"></a>Specifies the created OBS bucket. If no OBS bucket is available, click <strong id="b1979118482144"><a name="b1979118482144"></a><a name="b1979118482144"></a>View OBS Bucket</strong> and create an OBS bucket by following the instructions in <a href="https://docs.otc.t-systems.com/en-us/usermanual/obs/en-us_topic_0045853662.html" target="_blank" rel="noopener noreferrer">Managing Buckets</a> in the <em id="i197945481140"><a name="i197945481140"></a><a name="i197945481140"></a>OBS Console Operation Guide</em>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.3 "><p id="p1824719285386"><a name="p1824719285386"></a><a name="p1824719285386"></a>obs-8a09</p>
    </td>
    </tr>
    <tr id="row749263382910"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="p74901933122919"><a name="p74901933122919"></a><a name="p74901933122919"></a>Log Prefix</p>
    </td>
    <td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.2 "><p id="p349213372912"><a name="p349213372912"></a><a name="p349213372912"></a>Specifies the prefix of logs transferred to OBS buckets. It distinguishes log files from other files in OBS buckets.</p>
    <p id="p12624155716158"><a name="p12624155716158"></a><a name="p12624155716158"></a>The name format of the transferred log file is <em id="i5331104811712"><a name="i5331104811712"></a><a name="i5331104811712"></a>Log prefix</em><strong id="b43415482715"><a name="b43415482715"></a><a name="b43415482715"></a>_LogTank_Region_</strong><em id="i8342104813720"><a name="i8342104813720"></a><a name="i8342104813720"></a>transfer time</em>_<em id="i1145951210816"><a name="i1145951210816"></a><a name="i1145951210816"></a>xxx</em>.</p>
    <p id="p10795193781918"><a name="p10795193781918"></a><a name="p10795193781918"></a>The value must meet the following requirements:</p>
    <a name="ul1548674510203"></a><a name="ul1548674510203"></a><ul id="ul1548674510203"><li>Must be a string of 0 to 64 characters.</li><li>Only allows uppercase and lowercase letters, digits, underscores (_), hyphens (-), and periods (.).</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.3 "><p id="p16247428133812"><a name="p16247428133812"></a><a name="p16247428133812"></a>lts</p>
    </td>
    </tr>
    <tr id="row0492173342913"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="p7492173352911"><a name="p7492173352911"></a><a name="p7492173352911"></a>Format</p>
    </td>
    <td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.2 "><p id="p13492733202915"><a name="p13492733202915"></a><a name="p13492733202915"></a>Specifies the storage format of logs. The value can be <strong id="b1145015312291"><a name="b1145015312291"></a><a name="b1145015312291"></a>Raw Log Format</strong> or <strong id="b1140417341299"><a name="b1140417341299"></a><a name="b1140417341299"></a>JSON</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.3 "><p id="p8247528203816"><a name="p8247528203816"></a><a name="p8247528203816"></a>JSON</p>
    </td>
    </tr>
    <tr id="row14924336297"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="p549263342919"><a name="p549263342919"></a><a name="p549263342919"></a>Transfer Log to OBS</p>
    </td>
    <td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.2 "><p id="p11492233192911"><a name="p11492233192911"></a><a name="p11492233192911"></a>Specifies whether to enable log transfer.</p>
    </td>
    <td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.3 "><p id="p149191209411"><a name="p149191209411"></a><a name="p149191209411"></a>Enable</p>
    </td>
    </tr>
    <tr id="row11492183352916"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="p74921336297"><a name="p74921336297"></a><a name="p74921336297"></a>Log Transfer Interval</p>
    </td>
    <td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.2 "><p id="p194921733132913"><a name="p194921733132913"></a><a name="p194921733132913"></a>Specifies the interval, in the unit of seconds, at which logs are automatically transferred to the OBS bucket. The default value is 120.</p>
    </td>
    <td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.3 "><p id="p22471289386"><a name="p22471289386"></a><a name="p22471289386"></a>120</p>
    </td>
    </tr>
    </tbody>
    </table>

4.  Click  **OK**.

    When the log transfer status changes  **Normal**, the transfer task is created successfully.


