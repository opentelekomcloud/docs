# ALM-43008 Direct Memory Usage of the JobHistory Process Exceeds the Threshold<a name="EN-US_TOPIC_0125376108"></a>

## Description<a name="s0b849c4600f74271875a7b9aba47de19"></a>

The system checks the direct memory usage of the JobHistory process every 30 seconds. The alarm is generated when the direct memory usage of the JobHistory process exceeds the threshold \(90% of the maximum memory\).

## Attribute<a name="s7bf030c849e048c3a39225092a7113d2"></a>

<a name="tf8494100349f4c0783986d1671846859"></a>
<table><thead align="left"><tr id="rfb5af1dec215459c8eb92a56fffd0b64"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="a8ef9655b57324cba88053b51a32172ee"><a name="a8ef9655b57324cba88053b51a32172ee"></a><a name="a8ef9655b57324cba88053b51a32172ee"></a>Alarm ID</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="aaa66fb82c9164373889ab25a7f0a60cb"><a name="aaa66fb82c9164373889ab25a7f0a60cb"></a><a name="aaa66fb82c9164373889ab25a7f0a60cb"></a>Alarm Severity</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="aa4b6bc0996f54e749bcf6b50f99c7eae"><a name="aa4b6bc0996f54e749bcf6b50f99c7eae"></a><a name="aa4b6bc0996f54e749bcf6b50f99c7eae"></a>Automatically Cleared</p>
</th>
</tr>
</thead>
<tbody><tr id="rdfcebf433451487e9fac2a7783e5712c"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="a8a27b1c6a75749f5902577e8df5e0193"><a name="a8a27b1c6a75749f5902577e8df5e0193"></a><a name="a8a27b1c6a75749f5902577e8df5e0193"></a>43008</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="accfe7793b57c4e069f904576299aff0c"><a name="accfe7793b57c4e069f904576299aff0c"></a><a name="accfe7793b57c4e069f904576299aff0c"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="a247a7c708d51416994803d198960e9c8"><a name="a247a7c708d51416994803d198960e9c8"></a><a name="a247a7c708d51416994803d198960e9c8"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s24ff4d78d6754bb78a94bb89b65bea05"></a>

<a name="t2f23193d5c6e4e7ebc439467e8e51bd1"></a>
<table><thead align="left"><tr id="rcf8713e30f8d47598ae0e8f4759164f8"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="a6e2b623698054dc6a6f291334ea9f579"><a name="a6e2b623698054dc6a6f291334ea9f579"></a><a name="a6e2b623698054dc6a6f291334ea9f579"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="a623c308e075b4ce692710108d6f7da5b"><a name="a623c308e075b4ce692710108d6f7da5b"></a><a name="a623c308e075b4ce692710108d6f7da5b"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="rbcb7fa4086af4564b82ad8030cce0c39"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="ab07e93df2abd45eb8122e7fb55f93452"><a name="ab07e93df2abd45eb8122e7fb55f93452"></a><a name="ab07e93df2abd45eb8122e7fb55f93452"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a789563f252fc431cb754706a6c1a3ad4"><a name="a789563f252fc431cb754706a6c1a3ad4"></a><a name="a789563f252fc431cb754706a6c1a3ad4"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="r8fac64ce92a543eaa4c7c17b22695afd"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="aea0759ba251a4df383427334fd35958a"><a name="aea0759ba251a4df383427334fd35958a"></a><a name="aea0759ba251a4df383427334fd35958a"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a2f4644f31fd14b978b4f526049dca815"><a name="a2f4644f31fd14b978b4f526049dca815"></a><a name="a2f4644f31fd14b978b4f526049dca815"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="r579e26142ff14f50a63956c13b274c16"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="ab30690bdc3294e10a4b9acd73a76d98d"><a name="ab30690bdc3294e10a4b9acd73a76d98d"></a><a name="ab30690bdc3294e10a4b9acd73a76d98d"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="ad76ffb0e1f874a0996617ab2c9b6b553"><a name="ad76ffb0e1f874a0996617ab2c9b6b553"></a><a name="ad76ffb0e1f874a0996617ab2c9b6b553"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s706da3e098714339adfd27be376d83fc"></a>

Overhigh direct memory usage of the JobHistory process deteriorates JobHistory running performance or even causes OOM, which results in unavailable JobHistory process.

## Possible Causes<a name="sc9440ca4483a408dbf89fe438a5c511c"></a>

The direct memory of the JobHistory process is overused or inappropriately allocated.

## Procedure<a name="sc203587d4be648758cbebacf5319700b"></a>

1.  Check direct memory usage.
    1.  On MRS Manager, click  **Alarm** and select the alarm whose **Alarm ID** is **43008**. Then check the IP address and role name of the instance in **Location**.
    2.  On MRS Manager, choose  **Service** \> **Spark** \> **Instance** and click the JobHistory for which the alarm is generated to enter the **Instance Status** page. Then choose **Customize** \> **Direct Memory of JobHistory** and click **OK**.
    3.  Check whether the used direct memory of the JobHistory process reaches 90% of the maximum direct memory specified for JobHistory.
        -   If yes, go to  [1.d](#lcad505cae0a641f0afc6429bc722dbde).
        -   If no, go to  [2](#l0c85b10f6eff444da366b6b7731382be).

    4.  <a name="lcad505cae0a641f0afc6429bc722dbde"></a>On MRS Manager, choose  **Service** \> **Spark** \> **Service Configuration**, and set **Type** to **All**. Choose **JobHistory** \> **Default**. Increase the value of **-XX:MaxDirectMemorySize** in **SPARK\_DAEMON\_JAVA\_OPTS**  as required.
    5.  Check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [2](#l0c85b10f6eff444da366b6b7731382be).

2.  <a name="l0c85b10f6eff444da366b6b7731382be"></a>Collect fault information.
    1.  On MRS Manager, choose  **System** \> **Export Log**.
    2.  Select  **Spark** from the **Service** drop-down list and click **OK**.
    3.  Set  **Start Time** for log collection to 10 minutes ahead of the alarm generation time and **End Time** to 10 minutes behind the alarm generation time, and click **Download**.
    4.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="se35770ef3fd94f3c90cec0827a448753"></a>

N/A

