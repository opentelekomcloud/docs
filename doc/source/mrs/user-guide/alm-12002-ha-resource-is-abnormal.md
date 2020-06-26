# ALM-12002 HA Resource Is Abnormal<a name="EN-US_TOPIC_0125375751"></a>

## Description<a name="s31e769cb69684355a5a4638fffd10534"></a>

The high availability \(HA\) software periodically checks the WebService floating IP addresses and databases of Manager. This alarm is generated when any of these is abnormal.

This alarm is cleared when the HA software detects that the floating IP addresses or databases are in the normal state.

## **Attribute**<a name="s343a5a9b695a489ea7807e9cd6e7faa6"></a>

<a name="t73e9295a2eb04511837e97c84db9cb28"></a>
<table><thead align="left"><tr id="rf028f7916b264b6983bf69ba4e55abf7"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="aac02990371d548d9b91c4ff4ebd5b119"><a name="aac02990371d548d9b91c4ff4ebd5b119"></a><a name="aac02990371d548d9b91c4ff4ebd5b119"></a><strong id="a3aa38ec8a5524588b3a4d80b806f35eb"><a name="a3aa38ec8a5524588b3a4d80b806f35eb"></a><a name="a3aa38ec8a5524588b3a4d80b806f35eb"></a>Alarm ID</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="a35e91a1a7d724ecd9f76f3f570a08fe0"><a name="a35e91a1a7d724ecd9f76f3f570a08fe0"></a><a name="a35e91a1a7d724ecd9f76f3f570a08fe0"></a><strong id="a6a6cada96da245e38dd67c8717a3862c"><a name="a6a6cada96da245e38dd67c8717a3862c"></a><a name="a6a6cada96da245e38dd67c8717a3862c"></a>Alarm Severity</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="ab40e83998b26464bb1fdb167c4617e86"><a name="ab40e83998b26464bb1fdb167c4617e86"></a><a name="ab40e83998b26464bb1fdb167c4617e86"></a><strong id="a4194bf9323044700911a79023beebaac"><a name="a4194bf9323044700911a79023beebaac"></a><a name="a4194bf9323044700911a79023beebaac"></a>Automatically Cleared</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r7f5ea298765d41aeb73c07eaa423356b"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="a21424d79ceb94347bca684e6b319cc52"><a name="a21424d79ceb94347bca684e6b319cc52"></a><a name="a21424d79ceb94347bca684e6b319cc52"></a>12002</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="afa60f646ae554e12bdc06593ab8d1e75"><a name="afa60f646ae554e12bdc06593ab8d1e75"></a><a name="afa60f646ae554e12bdc06593ab8d1e75"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="aabc205a1d4d24554b266d6132180825f"><a name="aabc205a1d4d24554b266d6132180825f"></a><a name="aabc205a1d4d24554b266d6132180825f"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s107a10c0308040f689f1f612886b4c4f"></a>

<a name="t56bf09995c2a4435b154a558626c6f96"></a>
<table><thead align="left"><tr id="rfb8e0f5583cf49e8b4e323e038eb3235"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="ae69734ab07684cff8df777670ef73194"><a name="ae69734ab07684cff8df777670ef73194"></a><a name="ae69734ab07684cff8df777670ef73194"></a><strong id="a931b1ad9021a47b4beae69b408429ca1"><a name="a931b1ad9021a47b4beae69b408429ca1"></a><a name="a931b1ad9021a47b4beae69b408429ca1"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="abd3343835d334361bf687c5722747d6f"><a name="abd3343835d334361bf687c5722747d6f"></a><a name="abd3343835d334361bf687c5722747d6f"></a><strong id="ae778b34a6c1e41c59dc5fdd5f2d1459e"><a name="ae778b34a6c1e41c59dc5fdd5f2d1459e"></a><a name="ae778b34a6c1e41c59dc5fdd5f2d1459e"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="rf259c48987f34318883518d2a217fc6a"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a276ead050366469c8f29cecb2071a9b0"><a name="a276ead050366469c8f29cecb2071a9b0"></a><a name="a276ead050366469c8f29cecb2071a9b0"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a64edab0e9b7e4d0bbd593b9b12b83704"><a name="a64edab0e9b7e4d0bbd593b9b12b83704"></a><a name="a64edab0e9b7e4d0bbd593b9b12b83704"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="r3b22c4615f9b4c17ad6f9c07e516ff2c"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="ac0fb4a130ce2402c83ead5855d4a4144"><a name="ac0fb4a130ce2402c83ead5855d4a4144"></a><a name="ac0fb4a130ce2402c83ead5855d4a4144"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="aa7e8b49fb54b40d7a0c9aa3b2c2dcec8"><a name="aa7e8b49fb54b40d7a0c9aa3b2c2dcec8"></a><a name="aa7e8b49fb54b40d7a0c9aa3b2c2dcec8"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="rb7e7e7e982ec4bd1bc108d4fd941c058"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="aa3b6cc3f84fd467faf598cdcfca1722a"><a name="aa3b6cc3f84fd467faf598cdcfca1722a"></a><a name="aa3b6cc3f84fd467faf598cdcfca1722a"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="ae06caa975f7c4b91a20814e1d06d4fb1"><a name="ae06caa975f7c4b91a20814e1d06d4fb1"></a><a name="ae06caa975f7c4b91a20814e1d06d4fb1"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
<tr id="ra558ae0f5fe04511a8656a6d0ed60ffd"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a232eff77524b4b089168f2793627306d"><a name="a232eff77524b4b089168f2793627306d"></a><a name="a232eff77524b4b089168f2793627306d"></a>RESName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a09d8832c18294d53850bb5473473613d"><a name="a09d8832c18294d53850bb5473473613d"></a><a name="a09d8832c18294d53850bb5473473613d"></a>Specifies the resource for which the alarm is generated.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="sa8d49af957394b6b9bf720d99d3b0f4d"></a>

If the WebService floating IP addresses of Manager are abnormal, users cannot log in to or use MRS Manager. If databases are abnormal, all core services and related service processes, such as alarm and monitoring functions, are affected.

## Possible Causes<a name="s53b8fc1d375a46d9864f5763db83c7ca"></a>

-   The floating IP address is abnormal.
-   An exception occurs in the database.

## Procedure<a name="scb8f6d4c8e704e6b9e9e5c8366aee7a2"></a>

1.  Check the status of the floating IP address on the active management node.
    1.  In the alarm list on MRS Manager, locate the row that contains the alarm, and view its host address and resource name in the alarm details.
    2.  Log in to the active management node. Run the following command to switch the user:

        **sudo su - root**

        **su - omm**

    3.  Go to the  **$\{BIGDATA\_HOME\}/om-0.0.1/sbin/** directory, run the **status-oms.sh** script to check whether the floating IP address of the active Manager is normal. View the command output, locate the row where **ResName** is **floatip**, and check whether the following information is displayed.

        For example:

        ```
        10-10-10-160 floatip Normal Normal Single_active
        ```

        -   If yes, go to  [2](#lf066eeea4d784f6bafc9f76590c2f802).
        -   If no, go to  [1.d](#l80ee8ea145024886b51d959328fbf5cb).

    4.  <a name="l80ee8ea145024886b51d959328fbf5cb"></a>Contact the public cloud O&M personnel to check whether the NIC configured with the floating IP address exists.
        -   If yes, go to  [2](#lf066eeea4d784f6bafc9f76590c2f802).
        -   If no, go to  [1.e](#l41dbdcf0478b499bb23ea520c2a530f6).

    5.  <a name="l41dbdcf0478b499bb23ea520c2a530f6"></a>Contact the public cloud O&M personnel to rectify NIC faults.

        Wait 5 minutes and check whether the alarm is cleared.

        -   If yes, no further action is required.
        -   If no, go to  [2](#lf066eeea4d784f6bafc9f76590c2f802).

2.  <a name="lf066eeea4d784f6bafc9f76590c2f802"></a>Check the database status of the active and standby management nodes.
    1.  Log in to the active and standby management nodes, run the  **sudo su - root**  and **su - ommdba** command to switch to user **ommdba**, and then run the **gs\_ctl query**  command. Check whether the following information is displayed in the command output.

        Command output of the active management node:

        ```
        Ha state: LOCAL_ROLE: Primary STATIC_CONNECTIONS: 1 DB_STATE: Normal DETAIL_INFORMATION: user/password invalid Senders info: No information Receiver info: No information
        ```

        Command output of the standby management node:

        ```
        Ha state: LOCAL_ROLE: Standby STATIC_CONNECTIONS: 1 DB_STATE : Normal DETAIL_INFORMATION: user/password invalid Senders info: No information Receiver info: No information
        ```

        -   If yes, go to  [2.c](#lf551c5a79aa7494380a9880feb5f6339).
        -   If no, go to  [2.b](#l68236939ab1843bbb46f11a85dab3357).

    1.  <a name="l68236939ab1843bbb46f11a85dab3357"></a>Contact the public cloud O&M personnel to check for and rectify network faults.
        -   If yes, go to  [2.c](#lf551c5a79aa7494380a9880feb5f6339).
        -   If no, go to  [3](#l85c31cbceaaa40fc9ecc31bf9855b118).

    1.  <a name="lf551c5a79aa7494380a9880feb5f6339"></a>Wait 5 minutes and check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [3](#l85c31cbceaaa40fc9ecc31bf9855b118).

3.  <a name="l85c31cbceaaa40fc9ecc31bf9855b118"></a>Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).

## Related Information<a name="s004ab9ef74ef40c394f70b4ca3a4c215"></a>

N/A

