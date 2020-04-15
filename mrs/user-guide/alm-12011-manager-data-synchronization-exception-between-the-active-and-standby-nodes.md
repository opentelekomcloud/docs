# ALM-12011 Manager Data Synchronization Exception Between the Active and Standby Nodes<a name="EN-US_TOPIC_0125375236"></a>

## Description<a name="sd8cba70ea9764890ab99eb2e559a4afe"></a>

This alarm is generated when the standby Manager fails to synchronize files with the active Manager and is cleared when they succeed in synchronizing files.

## Attribute<a name="s1aefc329de16494e94ef9d44725ce201"></a>

<a name="tf6387ac3690a4ddeb6b52997e1e1e0ed"></a>
<table><thead align="left"><tr id="r39cd379b67d9479fad53a4494a1ee340"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="en-us_topic_0035461635_p156557912324"><a name="en-us_topic_0035461635_p156557912324"></a><a name="en-us_topic_0035461635_p156557912324"></a><strong id="adb247f6630534d29ab53b8e8184a0f50"><a name="adb247f6630534d29ab53b8e8184a0f50"></a><a name="adb247f6630534d29ab53b8e8184a0f50"></a>Alarm ID</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="a9402e3149fed43b2a5cc54ed11ee8df3"><a name="a9402e3149fed43b2a5cc54ed11ee8df3"></a><a name="a9402e3149fed43b2a5cc54ed11ee8df3"></a><strong id="ae2d053152b4d485cba5d007c25f4b792"><a name="ae2d053152b4d485cba5d007c25f4b792"></a><a name="ae2d053152b4d485cba5d007c25f4b792"></a>Alarm Severity</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="en-us_topic_0035461635_p134881812324"><a name="en-us_topic_0035461635_p134881812324"></a><a name="en-us_topic_0035461635_p134881812324"></a><strong id="aaa7c9bbcd63d4dbf8056c116dee003a6"><a name="aaa7c9bbcd63d4dbf8056c116dee003a6"></a><a name="aaa7c9bbcd63d4dbf8056c116dee003a6"></a>Automatically Cleared</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r891112c1c93e45619b0ce20500277415"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="a6075e75da27a4927a56605fc606c6b7a"><a name="a6075e75da27a4927a56605fc606c6b7a"></a><a name="a6075e75da27a4927a56605fc606c6b7a"></a>12011</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="aa7c20093ad9d460aa309536f38fe8ac2"><a name="aa7c20093ad9d460aa309536f38fe8ac2"></a><a name="aa7c20093ad9d460aa309536f38fe8ac2"></a>Critical</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="a3782a1bb81a24b04b3ae7d140dec1870"><a name="a3782a1bb81a24b04b3ae7d140dec1870"></a><a name="a3782a1bb81a24b04b3ae7d140dec1870"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s88907ceaa6f84ae8bf224d340ebc14e9"></a>

<a name="ta710255655974150b6cd34f279195035"></a>
<table><thead align="left"><tr id="r64ba5b8a6b544740accbbae111663310"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="ae311546b76d0425ba032fa9d2f9431bf"><a name="ae311546b76d0425ba032fa9d2f9431bf"></a><a name="ae311546b76d0425ba032fa9d2f9431bf"></a><strong id="adcc61d7995204798afbd4d198f4e4cf0"><a name="adcc61d7995204798afbd4d198f4e4cf0"></a><a name="adcc61d7995204798afbd4d198f4e4cf0"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="a7dc9b169f2494a5e9ce0a4dc17d1c43e"><a name="a7dc9b169f2494a5e9ce0a4dc17d1c43e"></a><a name="a7dc9b169f2494a5e9ce0a4dc17d1c43e"></a><strong id="a665f6550a9e948b9bd0a73cf1ca5bdbd"><a name="a665f6550a9e948b9bd0a73cf1ca5bdbd"></a><a name="a665f6550a9e948b9bd0a73cf1ca5bdbd"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r2ac6fb14eaa14c22b85f876c00fc4587"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a3e0205bd7c7649fd86c43b30b30fbe18"><a name="a3e0205bd7c7649fd86c43b30b30fbe18"></a><a name="a3e0205bd7c7649fd86c43b30b30fbe18"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a0d31cd43d22b449b8ce7e74f7c1d1bc5"><a name="a0d31cd43d22b449b8ce7e74f7c1d1bc5"></a><a name="a0d31cd43d22b449b8ce7e74f7c1d1bc5"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="rf3087247c653471b90063ce642b95ef9"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="ab15a3f9af4e14f88b1d1119bb83345a2"><a name="ab15a3f9af4e14f88b1d1119bb83345a2"></a><a name="ab15a3f9af4e14f88b1d1119bb83345a2"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a1e9b1f17967a4e7a873dc9340c255a12"><a name="a1e9b1f17967a4e7a873dc9340c255a12"></a><a name="a1e9b1f17967a4e7a873dc9340c255a12"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="r99dc0504994b4015912d2093e970f3d2"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a11ff919db81d43babf0a3d34a53870dd"><a name="a11ff919db81d43babf0a3d34a53870dd"></a><a name="a11ff919db81d43babf0a3d34a53870dd"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="aad1f23cf602f4b89a84a6801f2cb18ce"><a name="aad1f23cf602f4b89a84a6801f2cb18ce"></a><a name="aad1f23cf602f4b89a84a6801f2cb18ce"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
<tr id="rff81b76f06d14721a971f92151c36c86"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035461635_p644338312324"><a name="en-us_topic_0035461635_p644338312324"></a><a name="en-us_topic_0035461635_p644338312324"></a>Local Manager HA Name</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="aa7a4e39f900846b993df31b3e4e62f07"><a name="aa7a4e39f900846b993df31b3e4e62f07"></a><a name="aa7a4e39f900846b993df31b3e4e62f07"></a>Specifies a local Manager HA.</p>
</td>
</tr>
<tr id="r42f55fab4c1845459aa992850fe1a52e"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a6a7e4b8c12434e36bf39b892bc96976d"><a name="a6a7e4b8c12434e36bf39b892bc96976d"></a><a name="a6a7e4b8c12434e36bf39b892bc96976d"></a>Peer Manager HA Name</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a0d92477408684032b14da9ef5325b4f6"><a name="a0d92477408684032b14da9ef5325b4f6"></a><a name="a0d92477408684032b14da9ef5325b4f6"></a>Specifies a peer Manager HA.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="se5882c3d855648ea98676e365ee7819a"></a>

Because the configuration files on the standby Manager are not updated, some configurations will be lost after an active/standby switchover. Manager and some components may not run properly.

## Possible Causes<a name="sa65cba7dd0a448e4a321c124cac3e7ea"></a>

The link between the active and standby Managers is interrupted.

## Procedure<a name="s2fb142050d7e49048b01a3dd3e490440"></a>

1.  Check whether the network between the active and standby Manager servers is in the normal state.
    1.  In the alarm list on MRS Manager, locate the row that contains the alarm, and view the IP address of the standby Manager in the alarm details.
    2.  Log in to the active management node. Run the following command to check whether the standby Manager is reachable:

        **ping** _IP address of the standby Manager_

        1.  If yes, go to  [2](#l2379588c44e3406b9fc4a036349ef93c).
        2.  If no, go to  [1.c](#lc883cad8adee420f9704fdaf5cbb9ac9).

    3.  <a name="lc883cad8adee420f9704fdaf5cbb9ac9"></a>Contact the public cloud O&M personnel to check whether the network is faulty.
        -   If yes, go to  [1.d](#l0b6f9ddbf7c0450396bebc67e1c3bf5e).
        -   If no, go to  [2](#l2379588c44e3406b9fc4a036349ef93c).

    4.  <a name="l0b6f9ddbf7c0450396bebc67e1c3bf5e"></a>Rectify the network fault and check whether the alarm is cleared from the alarm list.
        -   If yes, no further action is required.
        -   If no, go to  [2](#l2379588c44e3406b9fc4a036349ef93c).

2.  <a name="l2379588c44e3406b9fc4a036349ef93c"></a>Collect fault information.
    1.  On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="s410b75344f664468bbb22306cf384503"></a>

N/A

