# ALM-12010 Manager Heartbeat Interruption Between the Active and Standby Nodes<a name="EN-US_TOPIC_0125375801"></a>

## Description<a name="s7b86bebe152f4e7e92160cef1f9779b1"></a>

This alarm is generated when the active Manager does not receive a heartbeat signal from the standby Manager or 7 seconds. It is cleared when the active Manager receives a heartbeat signal from the standby Manager.

## Attribute<a name="s17680c5b6b8549789edb57bc4b382ddd"></a>

<a name="t35ebd2172d36451aa2ea3a952a12d5de"></a>
<table><thead align="left"><tr id="re803d1ab70d84832a6742a96bade18f9"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="a043d11bd075b4dc580fdae2c2e4de982"><a name="a043d11bd075b4dc580fdae2c2e4de982"></a><a name="a043d11bd075b4dc580fdae2c2e4de982"></a><strong id="ac8965d7137d44c7cb156ffd255e1a166"><a name="ac8965d7137d44c7cb156ffd255e1a166"></a><a name="ac8965d7137d44c7cb156ffd255e1a166"></a>Alarm ID</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="ae4a465f7fccc40cd9844681edcee90d7"><a name="ae4a465f7fccc40cd9844681edcee90d7"></a><a name="ae4a465f7fccc40cd9844681edcee90d7"></a><strong id="a6e8eb5cef28f4562b4be7c1f61520840"><a name="a6e8eb5cef28f4562b4be7c1f61520840"></a><a name="a6e8eb5cef28f4562b4be7c1f61520840"></a>Alarm Severity</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="adc68edbd7cd0455d8be13a89c8746926"><a name="adc68edbd7cd0455d8be13a89c8746926"></a><a name="adc68edbd7cd0455d8be13a89c8746926"></a><strong id="ad8010e7c3983409087102eac3db8b49c"><a name="ad8010e7c3983409087102eac3db8b49c"></a><a name="ad8010e7c3983409087102eac3db8b49c"></a>Automatically Cleared</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r7b494d22de8f428496d5278f5a442c59"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="aa2575ecc925745079e2eef9ed29d5973"><a name="aa2575ecc925745079e2eef9ed29d5973"></a><a name="aa2575ecc925745079e2eef9ed29d5973"></a>12010</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="a0e090a8f5ab34843a477aa89be00c205"><a name="a0e090a8f5ab34843a477aa89be00c205"></a><a name="a0e090a8f5ab34843a477aa89be00c205"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="af75789deb3d844538a85be9bd5f3ee6f"><a name="af75789deb3d844538a85be9bd5f3ee6f"></a><a name="af75789deb3d844538a85be9bd5f3ee6f"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## **Parameters**<a name="sc63af639590740eb95bd65b88e380b94"></a>

<a name="t173d531bf5a74d0691e38a397aeddc28"></a>
<table><thead align="left"><tr id="r073de3ed4fe44c4ba84d25217b1745d2"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="a59316869aac143f499d971f09b8d9b7d"><a name="a59316869aac143f499d971f09b8d9b7d"></a><a name="a59316869aac143f499d971f09b8d9b7d"></a><strong id="a2f83b7fc7f5645dbb2b6decf16b9e8bc"><a name="a2f83b7fc7f5645dbb2b6decf16b9e8bc"></a><a name="a2f83b7fc7f5645dbb2b6decf16b9e8bc"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="aee5a87ede9e54128a492b28e7a2ea0e6"><a name="aee5a87ede9e54128a492b28e7a2ea0e6"></a><a name="aee5a87ede9e54128a492b28e7a2ea0e6"></a><strong id="af6dfcf3347ca48678ed68c9f2ef3f9a7"><a name="af6dfcf3347ca48678ed68c9f2ef3f9a7"></a><a name="af6dfcf3347ca48678ed68c9f2ef3f9a7"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r6aed98e7a6cd4f2e9af856263f4333e0"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="ab6cd2d49899c46bf9a849cd681400a93"><a name="ab6cd2d49899c46bf9a849cd681400a93"></a><a name="ab6cd2d49899c46bf9a849cd681400a93"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="aa7f731ce3c4a4153a99143ac2076b3fc"><a name="aa7f731ce3c4a4153a99143ac2076b3fc"></a><a name="aa7f731ce3c4a4153a99143ac2076b3fc"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="r65293eb0303046bdba1f22f34a2b6601"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="ab8ba8a9d278644dfad3c54ab8cd92158"><a name="ab8ba8a9d278644dfad3c54ab8cd92158"></a><a name="ab8ba8a9d278644dfad3c54ab8cd92158"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a96d6d39b0daf4db7b322a455c1887d02"><a name="a96d6d39b0daf4db7b322a455c1887d02"></a><a name="a96d6d39b0daf4db7b322a455c1887d02"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="r6cc7ac858a004f31aecf55ea8aafd9fe"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="ada840b801b41467f888f9b0aaf4404ec"><a name="ada840b801b41467f888f9b0aaf4404ec"></a><a name="ada840b801b41467f888f9b0aaf4404ec"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="aba1cdd3e59dd41548d50f66f39d3f97d"><a name="aba1cdd3e59dd41548d50f66f39d3f97d"></a><a name="aba1cdd3e59dd41548d50f66f39d3f97d"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
<tr id="r2129bc73907a451999bfde0cec58601b"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="aea1cc59c1e464e8cbe0296a0f376d15a"><a name="aea1cc59c1e464e8cbe0296a0f376d15a"></a><a name="aea1cc59c1e464e8cbe0296a0f376d15a"></a>Local Manager HA Name</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a3b78f3cc4f8142eb9bc4d4000596ff56"><a name="a3b78f3cc4f8142eb9bc4d4000596ff56"></a><a name="a3b78f3cc4f8142eb9bc4d4000596ff56"></a>Specifies a local Manager HA.</p>
</td>
</tr>
<tr id="ra0a472ae83b948dfab8b7822858655a7"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a719e7cfe21a54d28b8a9d6d363d72657"><a name="a719e7cfe21a54d28b8a9d6d363d72657"></a><a name="a719e7cfe21a54d28b8a9d6d363d72657"></a>Peer Manager HA Name</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a17fd4bc33ee54ffe9fd495fdc646aa1f"><a name="a17fd4bc33ee54ffe9fd495fdc646aa1f"></a><a name="a17fd4bc33ee54ffe9fd495fdc646aa1f"></a>Specifies a peer Manager HA.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s7016279cff5448d9b04cdf0009169081"></a>

When the active Manager process is abnormal, an active/standby failover cannot be performed, and services are affected.

## Possible Causes<a name="s1dc887c19c0246288e2439d237485506"></a>

The link between the active and standby Managers is abnormal.

## Procedure<a name="s9849b25caf5245d1b6e40553676f8ad0"></a>

1.  Check whether the network between the active and standby Manager servers is in the normal state.
    1.  In the alarm list on MRS Manager, locate the row that contains the alarm, and view the IP address of the standby Manager server in the alarm details.
    2.  Log in to the active management node.
    3.  Run the following command to check whether the standby Manager is reachable:

        **ping** _heartbeat IP address of the standby Manager_

        -   If yes, go to  [2](#l379848d5ae9e4f18963fec0af55db113).
        -   If no, go to  [1.d](#lbe13d2c6d6a3419c9f57fd1a01d0e628).

    4.  <a name="lbe13d2c6d6a3419c9f57fd1a01d0e628"></a>Contact the public cloud O&M personnel to check whether the network is faulty.
        -   If yes, go to  [1.e](#lb6e744c495c04cb0a85be778187e3601).
        -   If no, go to  [2](#l379848d5ae9e4f18963fec0af55db113).

    5.  <a name="lb6e744c495c04cb0a85be778187e3601"></a>Rectify the network fault and check whether the alarm is cleared from the alarm list.
        -   If yes, no further action is required.
        -   If no, go to  [2](#l379848d5ae9e4f18963fec0af55db113).

2.  <a name="l379848d5ae9e4f18963fec0af55db113"></a>Collect fault information.
    1.  On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).lp, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="sfc25876361894bf582806e1c243e89bc"></a>

N/A

