# ALM-26051 Storm Service Unavailable<a name="EN-US_TOPIC_0125375842"></a>

## Description<a name="sba5c581f4cb64707906e1da18ee703df"></a>

The system checks the Storm service availability every 30 seconds. This alarm is generated if the Storm service becomes unavailable after all Nimbus nodes in a cluster become abnormal.

This alarm is cleared after the Storm service recovers.

## Attribute<a name="sd3ff1c76020c4f98a73da86970712683"></a>

<a name="t0b9daf90fe9d4544a9796c49e5bfb56a"></a>
<table><thead align="left"><tr id="r0ac009caf492418183485fe865ceb40c"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="a8765b8d7420e47dd81f488017b4f034f"><a name="a8765b8d7420e47dd81f488017b4f034f"></a><a name="a8765b8d7420e47dd81f488017b4f034f"></a><strong id="en-us_topic_0053790965_b85402717567"><a name="en-us_topic_0053790965_b85402717567"></a><a name="en-us_topic_0053790965_b85402717567"></a>Alarm ID</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="en-us_topic_0053790965_p206737517567"><a name="en-us_topic_0053790965_p206737517567"></a><a name="en-us_topic_0053790965_p206737517567"></a><strong id="a988872368af14925bb8c85e9b42b02f7"><a name="a988872368af14925bb8c85e9b42b02f7"></a><a name="a988872368af14925bb8c85e9b42b02f7"></a>Alarm Severity</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="a0aaa03d7cb12476abea82430129bf8dc"><a name="a0aaa03d7cb12476abea82430129bf8dc"></a><a name="a0aaa03d7cb12476abea82430129bf8dc"></a><strong id="en-us_topic_0053790965_b805716717567"><a name="en-us_topic_0053790965_b805716717567"></a><a name="en-us_topic_0053790965_b805716717567"></a>Automatically Cleared</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r18adf29096a94085980dc15b6357fda5"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="acce771b564f2457bbee286d326ef8723"><a name="acce771b564f2457bbee286d326ef8723"></a><a name="acce771b564f2457bbee286d326ef8723"></a>26051</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="a8b167d01edc045b084ca990c5b86121d"><a name="a8b167d01edc045b084ca990c5b86121d"></a><a name="a8b167d01edc045b084ca990c5b86121d"></a>Critical</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="a2585ee08843344af9e07f65fe72ad912"><a name="a2585ee08843344af9e07f65fe72ad912"></a><a name="a2585ee08843344af9e07f65fe72ad912"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s976499594bdd4d8487487393c6254136"></a>

<a name="t4e6922576d7d47429dc7eb3f8277dfd0"></a>
<table><thead align="left"><tr id="ree8de12f4222426f961c9213b6b0eba9"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="a723ae4b2648a44d28ec1bd6b3be389b7"><a name="a723ae4b2648a44d28ec1bd6b3be389b7"></a><a name="a723ae4b2648a44d28ec1bd6b3be389b7"></a><strong id="a38d98a1f67fa4f1aa06b01cb07cfea7a"><a name="a38d98a1f67fa4f1aa06b01cb07cfea7a"></a><a name="a38d98a1f67fa4f1aa06b01cb07cfea7a"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="a04e5fceebde14f079c1b9ecf54a333d1"><a name="a04e5fceebde14f079c1b9ecf54a333d1"></a><a name="a04e5fceebde14f079c1b9ecf54a333d1"></a><strong id="a5ca72086ca1c4197985dd75b38fc40f2"><a name="a5ca72086ca1c4197985dd75b38fc40f2"></a><a name="a5ca72086ca1c4197985dd75b38fc40f2"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="re0ca6f4a88c144a5a7891a1574abf868"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="ac5492d1766e542559eeb8c2f675cf78d"><a name="ac5492d1766e542559eeb8c2f675cf78d"></a><a name="ac5492d1766e542559eeb8c2f675cf78d"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a71a646fade434543ab6d116605ad6279"><a name="a71a646fade434543ab6d116605ad6279"></a><a name="a71a646fade434543ab6d116605ad6279"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="r228250c3a1e549629780f201bfa80a9e"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a0c11b199768e428eb8b14ac5da4864e4"><a name="a0c11b199768e428eb8b14ac5da4864e4"></a><a name="a0c11b199768e428eb8b14ac5da4864e4"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a3c18cc613b044097a3398e29029c8a8b"><a name="a3c18cc613b044097a3398e29029c8a8b"></a><a name="a3c18cc613b044097a3398e29029c8a8b"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="r933a036507a444419c7f72e710684ae3"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="acf777df78add4ff29bb21d7b37e176f1"><a name="acf777df78add4ff29bb21d7b37e176f1"></a><a name="acf777df78add4ff29bb21d7b37e176f1"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0053790965_p454197817567"><a name="en-us_topic_0053790965_p454197817567"></a><a name="en-us_topic_0053790965_p454197817567"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="sd0395a7f943144a9b4988d7ea6924fda"></a>

-   The cluster cannot provide the Storm service.
-   Users cannot run new Storm tasks.

## Possible Causes<a name="s1c255dca5d3048949b3a2dc138f55538"></a>

-   The Kerberos component is faulty.
-   ZooKeeper is faulty or suspended.
-   The active and standby Nimbus nodes in the Storm cluster are abnormal.

## Procedure<a name="s567dc7bd01f24b3eac346204db9d503a"></a>

1.  Check the Kerberos component status. For clusters without Kerberos authentication, skip this step and go to  [2](#lb64e255b203a48b988de6d690e446406).
    1.  On MRS Manager, click  **Service**.
    2.  <a name="l9dae94f06edf4971b6bd3b4907b1b238"></a>Check whether the health status of the Kerberos service is  **Good**.
        -   If yes, go to  [2.a](#l19871efb3f5445b9a8ffc349d8c1f356).
        -   If no, go to  [1.c](#le1600b747ef846ce91a61fad7b0f517f).

    3.  <a name="le1600b747ef846ce91a61fad7b0f517f"></a>Rectify the fault by following instructions in ALM-25500 KrbServer Service Unavailable.
    4.  Perform  [1.b](#l9dae94f06edf4971b6bd3b4907b1b238)  again.

2.  <a name="lb64e255b203a48b988de6d690e446406"></a>Check the ZooKeeper component status.
    1.  <a name="l19871efb3f5445b9a8ffc349d8c1f356"></a>Check whether the health status of the ZooKeeper service is  **Good**.
        -   If yes, go to  [3.a](#la63a1d9965c84eaba53b6f54f0080ab9).
        -   If no, go to  [2.b](#l93c7acccf742497aad168f7896c2fe2f).

    2.  <a name="l93c7acccf742497aad168f7896c2fe2f"></a>If the ZooKeeper service is stopped, start it. For other problems, follow the instructions in ALM-13000 ZooKeeper Service Unavailable.
    3.  Perform  [2.a](#l19871efb3f5445b9a8ffc349d8c1f356)  again.

3.  Check the status of the active and standby Nimbus nodes.
    1.  <a name="la63a1d9965c84eaba53b6f54f0080ab9"></a>Choose  **Service**  \>  **Storm**  \>  **Nimbus**.
    2.  In  **Role**, check whether only one active Nimbus node exists.
        -   If yes, go to  [4.a](#l2521b0284f1a493587d2a7eb6134b6d9).
        -   If no, go to  [3.c](#l0aeb71e24a5f4d729788a9af05c08445).

    3.  <a name="l0aeb71e24a5f4d729788a9af05c08445"></a>Select the two Nimbus instances and choose  **More**  \>  **Restart Instance**. Check whether the restart is successful.
        -   If yes, go to  [3.d](#lc8363d1f39d146749ad95d42f8019b37).
        -   If no, go to  [4.a](#l2521b0284f1a493587d2a7eb6134b6d9).

    4.  <a name="lc8363d1f39d146749ad95d42f8019b37"></a>Log in to MRS Manager again and choose  **Service**  \>  **Storm**  \>  **Nimbus**. Check whether the health status of Nimbus is **Good**.
        -   If yes, go to  [3.e](#l24e05c600a684f1f9989ef644f8fa677).
        -   If no, go to  [4.a](#l2521b0284f1a493587d2a7eb6134b6d9).

    5.  <a name="l24e05c600a684f1f9989ef644f8fa677"></a>Wait 30 seconds and check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [4.a](#l2521b0284f1a493587d2a7eb6134b6d9).

4.  Collect fault information.
    1.  <a name="l2521b0284f1a493587d2a7eb6134b6d9"></a>On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="s66bd2ac52362473d9b639de6091f257e"></a>

N/A

