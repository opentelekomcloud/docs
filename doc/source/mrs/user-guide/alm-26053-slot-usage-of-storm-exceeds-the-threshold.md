# ALM-26053 Slot Usage of Storm Exceeds the Threshold<a name="EN-US_TOPIC_0125375213"></a>

## Description<a name="s03c6c42d4b274c40ba9e0fcabd88ab4b"></a>

The system checks the slot usage of Storm every 60 seconds and compares it with the threshold. This alarm is generated if the slot usage exceeds the threshold.

To modify the threshold, users can choose  **System**  \>  **Threshold Configuration**  on MRS Manager.

This alarm is cleared if the slot usage is lower than or equal to the threshold.

## Attribute<a name="s6297c8b248584a7eb28925005fce2d46"></a>

<a name="tafc882f788c84c339b8497feafa839bf"></a>
<table><thead align="left"><tr id="r04c4beda114c410e9f2f64c898e8eb45"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="afdc75f91af6246e29783ecc7a6508cd5"><a name="afdc75f91af6246e29783ecc7a6508cd5"></a><a name="afdc75f91af6246e29783ecc7a6508cd5"></a><strong id="ada5c3d82824445e8bf110b561b424be4"><a name="ada5c3d82824445e8bf110b561b424be4"></a><a name="ada5c3d82824445e8bf110b561b424be4"></a>Alarm ID</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="a89617aabb2264e0e9999380b28691190"><a name="a89617aabb2264e0e9999380b28691190"></a><a name="a89617aabb2264e0e9999380b28691190"></a><strong id="a75508494e17c414dbefc4530b40b5166"><a name="a75508494e17c414dbefc4530b40b5166"></a><a name="a75508494e17c414dbefc4530b40b5166"></a>Alarm Severity</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="a65bf926312634b7a9e157a7633e4bbe4"><a name="a65bf926312634b7a9e157a7633e4bbe4"></a><a name="a65bf926312634b7a9e157a7633e4bbe4"></a><strong id="abdf8986aba3843bbace427a1c9e367a3"><a name="abdf8986aba3843bbace427a1c9e367a3"></a><a name="abdf8986aba3843bbace427a1c9e367a3"></a>Automatically Cleared</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r58fa1995d39f4e2182edd28f23c6c866"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0053790967_p420326841881"><a name="en-us_topic_0053790967_p420326841881"></a><a name="en-us_topic_0053790967_p420326841881"></a>26053</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0053790967_p492042251881"><a name="en-us_topic_0053790967_p492042251881"></a><a name="en-us_topic_0053790967_p492042251881"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0053790967_p261193031881"><a name="en-us_topic_0053790967_p261193031881"></a><a name="en-us_topic_0053790967_p261193031881"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s2896845c0c014472b82ded595bd2c0a6"></a>

<a name="t2511d13ba3494125b752f1587a979032"></a>
<table><thead align="left"><tr id="r1e99b58becad40aca8627315aebeafc6"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="a94a04e30df8447ebad299cfcfc444096"><a name="a94a04e30df8447ebad299cfcfc444096"></a><a name="a94a04e30df8447ebad299cfcfc444096"></a><strong id="a6a4d385d530e4a9e911acb2ec324f9e7"><a name="a6a4d385d530e4a9e911acb2ec324f9e7"></a><a name="a6a4d385d530e4a9e911acb2ec324f9e7"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="a4d1789bb08ba49deab3e8b1ad5b2e30a"><a name="a4d1789bb08ba49deab3e8b1ad5b2e30a"></a><a name="a4d1789bb08ba49deab3e8b1ad5b2e30a"></a><strong id="ae2e66fba8d5c492fb1bc2c411cb671e8"><a name="ae2e66fba8d5c492fb1bc2c411cb671e8"></a><a name="ae2e66fba8d5c492fb1bc2c411cb671e8"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r894ba2b74dbf4ab4a842f30e70a86a71"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a16fc1a559d2040a59485aac05a120c81"><a name="a16fc1a559d2040a59485aac05a120c81"></a><a name="a16fc1a559d2040a59485aac05a120c81"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a8b7ff90731db4adba17fcbc850a74812"><a name="a8b7ff90731db4adba17fcbc850a74812"></a><a name="a8b7ff90731db4adba17fcbc850a74812"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="r895f7d357776473ba7f7bf8d0e5e11ac"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a537003fc91554bd6b7282f1d766e713c"><a name="a537003fc91554bd6b7282f1d766e713c"></a><a name="a537003fc91554bd6b7282f1d766e713c"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0053790967_p421312018815"><a name="en-us_topic_0053790967_p421312018815"></a><a name="en-us_topic_0053790967_p421312018815"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="r60fd18d4a913434589a4c76e7ae337f4"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a09425f4cf36f48fa84003f11d71bab35"><a name="a09425f4cf36f48fa84003f11d71bab35"></a><a name="a09425f4cf36f48fa84003f11d71bab35"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0053790967_p800105218815"><a name="en-us_topic_0053790967_p800105218815"></a><a name="en-us_topic_0053790967_p800105218815"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
<tr id="r048361d12ad2469eb4355755f6f721ae"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="ae0eed94b2bec4abd9e0ff7d74235eca1"><a name="ae0eed94b2bec4abd9e0ff7d74235eca1"></a><a name="ae0eed94b2bec4abd9e0ff7d74235eca1"></a>Trigger condition</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0053790967_p777338418815"><a name="en-us_topic_0053790967_p777338418815"></a><a name="en-us_topic_0053790967_p777338418815"></a>Generates an alarm when the actual indicator value exceeds the specified threshold.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="sf602c100de9b4711b823b4e2a391e3df"></a>

Users cannot run new Storm tasks.

## Possible Causes<a name="s611c957bf15b4fd69c20e9dfe9283a1d"></a>

-   Supervisors are abnormal in the cluster.
-   Supervisors are normal but have poor processing capability.

## Procedure<a name="sfa52741755414e0682473e64488a7b6e"></a>

1.  Check the supervisor status.
    1.  Choose  **Service**  \>  **Storm**  \>  **Supervisor**.
    2.  In  **Role**, check whether the cluster has supervisor instances that are in the **Bad** or **Concerning**  state.
        -   If yes, go to  [1.c](#le74a21968690462cbcec4970c80412a0).
        -   If no, go to  [2.a](#l17da8a10abfc40eab14b4a441199677e) or [3.a](#le8d8078214aa413a86c59df91914e1ba).

    3.  <a name="le74a21968690462cbcec4970c80412a0"></a>Select the supervisor instances that are in the  **Bad** or **Concerning** state and choose **More**  \>  **Restart Instance**.
        -   If the restart is successful, go to  [1.d](#lc7bc3e040e1845f2b2e205e23be451dc).
        -   If the restart fails, go to  [4.a](#l701ebacc76f344b8bb059e5d44cc6f7c).

    4.  <a name="lc7bc3e040e1845f2b2e205e23be451dc"></a>Wait a moment and then check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [2.a](#l17da8a10abfc40eab14b4a441199677e) or [3.a](#le8d8078214aa413a86c59df91914e1ba).

2.  Increase the number of slots for the supervisors.
    1.  <a name="l17da8a10abfc40eab14b4a441199677e"></a>On MRS Manager, choose  **Service \> Storm \> Supervisor \> Service Configuration \> Type \> All**.
    2.  Increase the value of  **supervisor.slots.ports**  to increase the number of slots for each supervisor. Then restart the instances.
    3.  Wait a moment and then check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [4.a](#l701ebacc76f344b8bb059e5d44cc6f7c).

3.  Expand the capacity of the supervisors.
    1.  <a name="le8d8078214aa413a86c59df91914e1ba"></a>Add nodes.
    2.  Wait a moment and then check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [4.a](#l701ebacc76f344b8bb059e5d44cc6f7c).

4.  Collect fault information.
    1.  <a name="l701ebacc76f344b8bb059e5d44cc6f7c"></a>On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="s4e7d33bc379f4be68056aca6fcf94bd0"></a>

N/A

