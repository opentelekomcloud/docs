# ALM-26052 Number of Available Supervisors in Storm Is Lower Than the Threshold<a name="EN-US_TOPIC_0125375806"></a>

## Description<a name="s59689fec171345748b27afbec7802da9"></a>

The system checks the number of supervisors every 60 seconds and compares it with the threshold. This alarm is generated if the number of supervisors is lower than the threshold.

To modify the threshold, users can choose  **System**  \>  **Threshold Configuration**  on MRS Manager.

This alarm is cleared if the number of supervisors is greater than or equal to the threshold.

## Attribute<a name="s9459d88e5ef940f3ac9d7fcb667188a5"></a>

<a name="t8ad1e697e7e34ba2b29dd80e254229f1"></a>
<table><thead align="left"><tr id="r4fe7955572fb48ab97e80558a1b0e5fc"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="a2b1d3deeab9e489f855d78b1b9b78f81"><a name="a2b1d3deeab9e489f855d78b1b9b78f81"></a><a name="a2b1d3deeab9e489f855d78b1b9b78f81"></a><strong id="a83914b18223f49d8a614f7ca5b0614e7"><a name="a83914b18223f49d8a614f7ca5b0614e7"></a><a name="a83914b18223f49d8a614f7ca5b0614e7"></a>Alarm ID</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="ae726b7542e664665a8bfcfd3c4b47df8"><a name="ae726b7542e664665a8bfcfd3c4b47df8"></a><a name="ae726b7542e664665a8bfcfd3c4b47df8"></a><strong id="acdec6a5f0bb546b5a954d42aeb933d41"><a name="acdec6a5f0bb546b5a954d42aeb933d41"></a><a name="acdec6a5f0bb546b5a954d42aeb933d41"></a>Alarm Severity</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="abf46d1bb0abf4d5197b67d48deea87d7"><a name="abf46d1bb0abf4d5197b67d48deea87d7"></a><a name="abf46d1bb0abf4d5197b67d48deea87d7"></a><strong id="a7e5880d705de42c5986a35888cfd6b58"><a name="a7e5880d705de42c5986a35888cfd6b58"></a><a name="a7e5880d705de42c5986a35888cfd6b58"></a>Automatically Cleared</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="ra78119780db64851a382f654fdd97bf0"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="a873274e928ee41369e0ab13d39e02f49"><a name="a873274e928ee41369e0ab13d39e02f49"></a><a name="a873274e928ee41369e0ab13d39e02f49"></a>26052</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="a2c11606ed339425eaffdbc141bd6a577"><a name="a2c11606ed339425eaffdbc141bd6a577"></a><a name="a2c11606ed339425eaffdbc141bd6a577"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="a3a2cce73639043bcb38bbece347e3099"><a name="a3a2cce73639043bcb38bbece347e3099"></a><a name="a3a2cce73639043bcb38bbece347e3099"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s24b906cba8dc442aa37760fe978f81b9"></a>

<a name="ta276ea981fcc43e2abff13a8743ca65d"></a>
<table><thead align="left"><tr id="r3d5fd6d4a9b4417097acd9bd4927f9df"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="acc00a1bfd1214b2bb8d8a3c334a4ef15"><a name="acc00a1bfd1214b2bb8d8a3c334a4ef15"></a><a name="acc00a1bfd1214b2bb8d8a3c334a4ef15"></a><strong id="ad3335d6d395441dd976cc84ff348690b"><a name="ad3335d6d395441dd976cc84ff348690b"></a><a name="ad3335d6d395441dd976cc84ff348690b"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="a2b84c7ad17f94b7c90586a354ad65319"><a name="a2b84c7ad17f94b7c90586a354ad65319"></a><a name="a2b84c7ad17f94b7c90586a354ad65319"></a><strong id="a5a6e95d356f14fec8a29158f8f8afc83"><a name="a5a6e95d356f14fec8a29158f8f8afc83"></a><a name="a5a6e95d356f14fec8a29158f8f8afc83"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="ra09952594faf4a8fb67f86d96341a07e"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="aebf90cab17cb471aaeeaf0aac05e7bda"><a name="aebf90cab17cb471aaeeaf0aac05e7bda"></a><a name="aebf90cab17cb471aaeeaf0aac05e7bda"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a49d5fdf6b6f84efeb9117c44b21a24a6"><a name="a49d5fdf6b6f84efeb9117c44b21a24a6"></a><a name="a49d5fdf6b6f84efeb9117c44b21a24a6"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="radecab18eee242a697970122eb66c031"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0053790966_p889946618550"><a name="en-us_topic_0053790966_p889946618550"></a><a name="en-us_topic_0053790966_p889946618550"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="af8a03e7a82b74c5daab9558f1183b46e"><a name="af8a03e7a82b74c5daab9558f1183b46e"></a><a name="af8a03e7a82b74c5daab9558f1183b46e"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="r7777d7874fda4610b23d48bdf37a06d2"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="aef8d736146af45aab076034f5bb601fc"><a name="aef8d736146af45aab076034f5bb601fc"></a><a name="aef8d736146af45aab076034f5bb601fc"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="ad8f36cbd219f4d5eb9a2d3825fca9a80"><a name="ad8f36cbd219f4d5eb9a2d3825fca9a80"></a><a name="ad8f36cbd219f4d5eb9a2d3825fca9a80"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
<tr id="r9af6d4d1fbda472485ede94dbd30ccf5"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0053790966_p22516311866"><a name="en-us_topic_0053790966_p22516311866"></a><a name="en-us_topic_0053790966_p22516311866"></a>Trigger Condition</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0053790966_p308264801866"><a name="en-us_topic_0053790966_p308264801866"></a><a name="en-us_topic_0053790966_p308264801866"></a>Generates an alarm when the actual indicator value exceeds the specified threshold.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="sbaa466f0acd64fbea8d44ad35193aefa"></a>

-   Existing tasks in the cluster cannot be executed.
-   The cluster can receive new Storm tasks but cannot execute them.

## Possible Causes<a name="s26a647514b9042f0ac3fbef2e938396a"></a>

Supervisors are abnormal in the cluster.

## Procedure<a name="s0b7743b9670f48eabd21228721f1b161"></a>

1.  Check the supervisor status.
    1.  Choose  **Service**  \>  **Storm**  \>  **Supervisor**.
    2.  In  **Role**, check whether the cluster has supervisor instances that are in the **Bad** or **Concerning**  state.
        -   If yes, go to  [1.c](#l84cf7148896948debd089466d0bd8f01).
        -   If no, go to  [2.a](#l2ff4db1cf6cf4e84a450dd3d9ab5010c).

    3.  <a name="l84cf7148896948debd089466d0bd8f01"></a>Select the supervisor instances that are in the  **Bad** or **Concerning** state and choose **More**  \>  **Restart Instance**.
        -   If the restart is successful, go to  [1.d](#l65eee08c6b47482b98a3801c5961b952).
        -   If the restart fails, go to  [2.a](#l2ff4db1cf6cf4e84a450dd3d9ab5010c).

    4.  <a name="l65eee08c6b47482b98a3801c5961b952"></a>Wait 30 seconds and check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [2.a](#l2ff4db1cf6cf4e84a450dd3d9ab5010c).

2.  Collect fault information.
    1.  <a name="l2ff4db1cf6cf4e84a450dd3d9ab5010c"></a>On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="sd2287509b21e4486a528dfbac0a095a1"></a>

N/A

