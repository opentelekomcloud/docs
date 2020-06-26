# ALM-12037 NTP Server Is Abnormal<a name="EN-US_TOPIC_0125375613"></a>

## Description<a name="s3eceb87d615a4e4b80fcbbb4745254c1"></a>

This alarm is generated when the NTP server is abnormal and is cleared after the NTP server recovers.

## Attribute<a name="sa492b5e1f4b44093a91faaef801a37c7"></a>

<a name="t5edc43e3974f41219b36c8e7bb08a005"></a>
<table><thead align="left"><tr id="r5fc4e6bb37fa4f11a97769fb412f1fc6"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="acbcb5147e04446fd81be5d4652006b97"><a name="acbcb5147e04446fd81be5d4652006b97"></a><a name="acbcb5147e04446fd81be5d4652006b97"></a><strong id="af6ec458325dd4a57871518a3902a60d3"><a name="af6ec458325dd4a57871518a3902a60d3"></a><a name="af6ec458325dd4a57871518a3902a60d3"></a>Alarm ID</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="a56b7375ad01e478985b455f4d8e034be"><a name="a56b7375ad01e478985b455f4d8e034be"></a><a name="a56b7375ad01e478985b455f4d8e034be"></a><strong id="af147d7879ccd42a58edf1c2382afcbb6"><a name="af147d7879ccd42a58edf1c2382afcbb6"></a><a name="af147d7879ccd42a58edf1c2382afcbb6"></a>Alarm Severity</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="aad8a69d35e0e459288b4241abbbfa137"><a name="aad8a69d35e0e459288b4241abbbfa137"></a><a name="aad8a69d35e0e459288b4241abbbfa137"></a><strong id="a295798011550460f9c5d4152f114372e"><a name="a295798011550460f9c5d4152f114372e"></a><a name="a295798011550460f9c5d4152f114372e"></a>Automatically Cleared</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r74e986d4ed4b4e948ad4124a0ff15edc"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="ad11c398616cc4554938b685b9b30fdca"><a name="ad11c398616cc4554938b685b9b30fdca"></a><a name="ad11c398616cc4554938b685b9b30fdca"></a>12037</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="a84250f20c7c04f338cff73422e9f364b"><a name="a84250f20c7c04f338cff73422e9f364b"></a><a name="a84250f20c7c04f338cff73422e9f364b"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="a840fb1b1a93c4e059b6d4fa509b50329"><a name="a840fb1b1a93c4e059b6d4fa509b50329"></a><a name="a840fb1b1a93c4e059b6d4fa509b50329"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s3de6431482be4b4094ec0535330d9b84"></a>

<a name="t73254d89082943db86feb611ae2ddbc5"></a>
<table><thead align="left"><tr id="r67d8fc13e7614232af4c53ef317cb9ca"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="af7b286bf3b714596a0b0a2fa7445852f"><a name="af7b286bf3b714596a0b0a2fa7445852f"></a><a name="af7b286bf3b714596a0b0a2fa7445852f"></a><strong id="a9a870b3e54ff4f8fb9bb9f562a4c3441"><a name="a9a870b3e54ff4f8fb9bb9f562a4c3441"></a><a name="a9a870b3e54ff4f8fb9bb9f562a4c3441"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="a6e4472717c5443b48e2a7ad1fe03c9ef"><a name="a6e4472717c5443b48e2a7ad1fe03c9ef"></a><a name="a6e4472717c5443b48e2a7ad1fe03c9ef"></a><strong id="aef80779eff0c40babc568469861dbe6e"><a name="aef80779eff0c40babc568469861dbe6e"></a><a name="aef80779eff0c40babc568469861dbe6e"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r91b68f3ce405462ebc0490a8cadbc3b7"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="ad64d31bf57464a558926e364d841d5f6"><a name="ad64d31bf57464a558926e364d841d5f6"></a><a name="ad64d31bf57464a558926e364d841d5f6"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="ab4698746dd144fd4b3e6ccc16fcedd97"><a name="ab4698746dd144fd4b3e6ccc16fcedd97"></a><a name="ab4698746dd144fd4b3e6ccc16fcedd97"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="rc65ba3097e324f37a54172e5e7a54fab"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a37a5daed69cd402fbed3baa1243698e0"><a name="a37a5daed69cd402fbed3baa1243698e0"></a><a name="a37a5daed69cd402fbed3baa1243698e0"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a8ade6252cc5d49869ec2aba8af90631a"><a name="a8ade6252cc5d49869ec2aba8af90631a"></a><a name="a8ade6252cc5d49869ec2aba8af90631a"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="r2645b48222d449bda2e0fb408b6a8993"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="ae55a21410440489e81d4cd7363f098b5"><a name="ae55a21410440489e81d4cd7363f098b5"></a><a name="ae55a21410440489e81d4cd7363f098b5"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a74af3b12911e4ac08692ec729c40a03c"><a name="a74af3b12911e4ac08692ec729c40a03c"></a><a name="a74af3b12911e4ac08692ec729c40a03c"></a>Specifies the IP address of the NTP server for which the alarm is generated.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s6e435e6eb2f5490a852842d0a39f8262"></a>

If the NTP server configured on the active OMS node is abnormal, the active OMS node fails to synchronize time with the NTP server and a time offset may be generated in the cluster.

## Possible Causes<a name="s85c7e4567da14f79a619ed623138ea72"></a>

-   The NTP server network is faulty.
-   The NTP server authentication fails.
-   The NTP server time cannot be obtained.
-   The time obtained from the NTP server is not being continuously updated.

## Procedure<a name="sc834d049513b40389a86391843caa958"></a>

1.  Check the NTP server network.
    1.  On the MRS Manager portal, view the real-time alarm list and locate the target alarm.
    2.  In the  **Alarm Details**  area, view the additional information to check whether the NTP server is successfully pinged.
        -   If yes, go to  [2](#ld61fbd0ccbb244d7bcb1e221d3286e45).
        -   If no, go to  [1.c](#ld9a1a87677a3475387c27525094b8146).

    3.  <a name="ld9a1a87677a3475387c27525094b8146"></a>Contact the public cloud O&M personnel to check the network configuration and ensure that the network between the NTP server and the active OMS node is in the normal state. Then, check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [2](#ld61fbd0ccbb244d7bcb1e221d3286e45).

2.  <a name="ld61fbd0ccbb244d7bcb1e221d3286e45"></a>Check whether the NTP server authentication fails.
    1.  Log in to the active management node.
    2.  Run the  **ntpq -np** command to check whether the NTP server authentication fails. If **refid** of the NTP server is **.AUTH.**, the authentication fails.
        -   If yes, go to  [5](#l1d126b8d55e4478fad5d946b115a6cee).
        -   If no, go to  [3](#lfdaf3b6dbf4d46b1965c61e53bc4d459).

3.  <a name="lfdaf3b6dbf4d46b1965c61e53bc4d459"></a>Check whether the time can be obtained from the NTP server.
    1.  View the additional information of the alarm to check whether the time can be obtained from the NTP server.
        -   If yes, go to  [4](#lcd1401fcf18944118b00619aa99e7681).
        -   If no, go to  [3.b](#l3d50397f374d4ab7bce7db2efb3674c2).

    2.  <a name="l3d50397f374d4ab7bce7db2efb3674c2"></a>Contact the public cloud O&M personnel to rectify the NTP server fault. After the NTP server is in the normal state, check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [4](#lcd1401fcf18944118b00619aa99e7681).

4.  <a name="lcd1401fcf18944118b00619aa99e7681"></a>Check whether the time obtained from the NTP server is being continuously updated.
    1.  View the additional information of the alarm to check whether the time obtained from the NTP server is being continuously updated.
        -   If yes, go to  [5](#l1d126b8d55e4478fad5d946b115a6cee).
        -   If no, go to  [4.b](#l40ab755ff2db40cdb2a1cef91d03e8af).

    2.  <a name="l40ab755ff2db40cdb2a1cef91d03e8af"></a>Contact the provider of the NTP server to rectify the NTP server fault. After the NTP server is in the normal state, check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [5](#l1d126b8d55e4478fad5d946b115a6cee).

5.  <a name="l1d126b8d55e4478fad5d946b115a6cee"></a>Collect fault information.
    1.  On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="sa20172464bdc45338ed5202674b2d2f2"></a>

N/A

