# ALM-24000 Flume Service Unavailable<a name="EN-US_TOPIC_0125375872"></a>

## Description<a name="s08533d0608b949cdaf295207071f59ca"></a>

The alarm module checks the Flume service status every 180 seconds. This alarm is generated when the Flume service is abnormal.

This alarm is cleared when the Flume service recovers.

## Attribute<a name="s5920c039f4a84f88baf5b0915cab08a2"></a>

<a name="t8c1fe241b02f4dfcaec26b9a0b82edd2"></a>
<table><thead align="left"><tr id="rc35e823b31704369811f302d91848649"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="a2a22468c4275403ba7093acba0a32f59"><a name="a2a22468c4275403ba7093acba0a32f59"></a><a name="a2a22468c4275403ba7093acba0a32f59"></a><strong id="a7fc6463c5cf04d7f8eefee2450099b2f"><a name="a7fc6463c5cf04d7f8eefee2450099b2f"></a><a name="a7fc6463c5cf04d7f8eefee2450099b2f"></a>Alarm ID</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="a71a1ea59fffe4cf8aac77718d75f1780"><a name="a71a1ea59fffe4cf8aac77718d75f1780"></a><a name="a71a1ea59fffe4cf8aac77718d75f1780"></a><strong id="a05643c82674d444ba4f5e0978567c369"><a name="a05643c82674d444ba4f5e0978567c369"></a><a name="a05643c82674d444ba4f5e0978567c369"></a>Alarm Severity</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="a78a1459e02a34c38b246cce1ca5de793"><a name="a78a1459e02a34c38b246cce1ca5de793"></a><a name="a78a1459e02a34c38b246cce1ca5de793"></a><strong id="ab9605b9ce7d64e339928fc3161066493"><a name="ab9605b9ce7d64e339928fc3161066493"></a><a name="ab9605b9ce7d64e339928fc3161066493"></a>Automatically Cleared</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r9410fcaa06a54b89b8e09b514e4f554e"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="a9e11e98f035e4a55ab7f1bf6b1e4ee15"><a name="a9e11e98f035e4a55ab7f1bf6b1e4ee15"></a><a name="a9e11e98f035e4a55ab7f1bf6b1e4ee15"></a>24000</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="afcdb1b375df8465081b565f06da6be6f"><a name="afcdb1b375df8465081b565f06da6be6f"></a><a name="afcdb1b375df8465081b565f06da6be6f"></a>Critical</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="aa9c3f49296a141439276a652b8cd46da"><a name="aa9c3f49296a141439276a652b8cd46da"></a><a name="aa9c3f49296a141439276a652b8cd46da"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="sfb5aba134d5d4ab9ae072e5810738315"></a>

<a name="t253741dd2eea4614b6abdfd6c157719c"></a>
<table><thead align="left"><tr id="r46be5060b52843b39118b7876a9d2957"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="acd4b5b6820764b33af5172f95d0fb217"><a name="acd4b5b6820764b33af5172f95d0fb217"></a><a name="acd4b5b6820764b33af5172f95d0fb217"></a><strong id="a3426689908b34cb5904034e219e1b828"><a name="a3426689908b34cb5904034e219e1b828"></a><a name="a3426689908b34cb5904034e219e1b828"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="adf55770680124a61b36599d7e9c10fa8"><a name="adf55770680124a61b36599d7e9c10fa8"></a><a name="adf55770680124a61b36599d7e9c10fa8"></a><strong id="a860fd4a7f8784eac9e36f77e9ab2b9ac"><a name="a860fd4a7f8784eac9e36f77e9ab2b9ac"></a><a name="a860fd4a7f8784eac9e36f77e9ab2b9ac"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r9af8528e38404fb69642b71bd6819730"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a5165ccf309a749b4ae6f9bbeafaf3f24"><a name="a5165ccf309a749b4ae6f9bbeafaf3f24"></a><a name="a5165ccf309a749b4ae6f9bbeafaf3f24"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="af25820982682473c9e0bdb78aa77733a"><a name="af25820982682473c9e0bdb78aa77733a"></a><a name="af25820982682473c9e0bdb78aa77733a"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="rb7313e8e8b404c06980d9a726e854873"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a645dd6e3e38244018cddfbece60d91c7"><a name="a645dd6e3e38244018cddfbece60d91c7"></a><a name="a645dd6e3e38244018cddfbece60d91c7"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="ab009fd0352d24a8eb9512ba418cd4351"><a name="ab009fd0352d24a8eb9512ba418cd4351"></a><a name="ab009fd0352d24a8eb9512ba418cd4351"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="ra60dd32265f34b309b92a837b2b3f992"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="afa37d11cd3814ea7968d2e712f317a05"><a name="afa37d11cd3814ea7968d2e712f317a05"></a><a name="afa37d11cd3814ea7968d2e712f317a05"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a40c4eb22d11f45c0a7b5a06f65031f64"><a name="a40c4eb22d11f45c0a7b5a06f65031f64"></a><a name="a40c4eb22d11f45c0a7b5a06f65031f64"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="sdb399cdeb4da46849c7584158e851266"></a>

Flume cannot work and data transmission is interrupted.

## Possible Causes<a name="s90ad3299502a4b36ad81b2e3cfd5125b"></a>

-   HDFS is unavailable.
-   LdapServer is unavailable.

## Procedure<a name="sceb4e95637d54f72b313018f4b01b0ed"></a>

1.  Check the HDFS status.

    On MRS Manager, check whether alarm ALM-14000 HDFS Service Unavailable is reported.

    -   If yes, clear the alarm according to the handling suggestions of "ALM-14000 HDFS Service Unavailable".
    -   If no, go to  [2](#l704ba1c895c94173a0af245b808f4fe5).

2.  <a name="l704ba1c895c94173a0af245b808f4fe5"></a>Check the LdapServer status.

    On MRS Manager, check whether alarm ALM-25000 LdapServer Service Unavailable is reported.

    -   If yes, clear the alarm according to the handling suggestions of "ALM-25000 LdapServer Service Unavailable".
    -   If no, go to  [3.a](#ld659052f0d3040819c0eca8c6a1499c7).

3.  Check whether the HDFS and LdapServer services are stopped.
    1.  <a name="ld659052f0d3040819c0eca8c6a1499c7"></a>In the service list on MRS Manager, check whether the HDFS and LdapServer services are stopped.
        -   If yes, start the HDFS and LdapServer services and go to  [3.b](#lde8d47c9bd394dd681604c1efed571c0).
        -   If no, go to  [4.a](#l7f5e4fe37963469bbb73c47b1225351d).

    2.  <a name="lde8d47c9bd394dd681604c1efed571c0"></a>Check whether the "ALM-24000 Flume Service Unavailable" alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [4.a](#l7f5e4fe37963469bbb73c47b1225351d).

4.  Collect fault information.
    1.  <a name="l7f5e4fe37963469bbb73c47b1225351d"></a>On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="s8b94430e9c084ac08b7bcea21f51e12f"></a>

N/A

