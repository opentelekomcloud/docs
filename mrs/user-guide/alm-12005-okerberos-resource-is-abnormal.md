# ALM-12005 OKerberos Resource Is Abnormal<a name="EN-US_TOPIC_0125375280"></a>

## Description<a name="s286d67102901486db8b06b3eb2adffd6"></a>

The alarm module monitors the status of the Kerberos resource in Manager. This alarm is generated when the Kerberos resource is abnormal and is cleared after the Kerberos resource recovers and the alarm handling is complete.

## Attribute<a name="s34fac170e7fd4c47949daecf56b10a49"></a>

<a name="ta9b8b6b842104edd8dbb4ffbf55dddb3"></a>
<table><thead align="left"><tr id="re813ad731c3d45239f190b99600e6f1d"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="a3dc7e11d85524f51b9142b2d40b559e5"><a name="a3dc7e11d85524f51b9142b2d40b559e5"></a><a name="a3dc7e11d85524f51b9142b2d40b559e5"></a><strong id="a414cc790843d4409b6e9ba82da34df91"><a name="a414cc790843d4409b6e9ba82da34df91"></a><a name="a414cc790843d4409b6e9ba82da34df91"></a>Alarm ID</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="aeb0c5cd13ffa4b8f835be1d54ac626ee"><a name="aeb0c5cd13ffa4b8f835be1d54ac626ee"></a><a name="aeb0c5cd13ffa4b8f835be1d54ac626ee"></a><strong id="af4bf1d3ffb1b47888e1e8436f4c6aee0"><a name="af4bf1d3ffb1b47888e1e8436f4c6aee0"></a><a name="af4bf1d3ffb1b47888e1e8436f4c6aee0"></a>Alarm Severity</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="a62f7ed30b8d947a0bb7a4e6c9bad23c5"><a name="a62f7ed30b8d947a0bb7a4e6c9bad23c5"></a><a name="a62f7ed30b8d947a0bb7a4e6c9bad23c5"></a><strong id="a2919908cd4ff471e8494575d1ad8ba1b"><a name="a2919908cd4ff471e8494575d1ad8ba1b"></a><a name="a2919908cd4ff471e8494575d1ad8ba1b"></a>Automatically Cleared</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r4dca8ffa55054d158d2ba176737b4134"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="a26b5d9cffcc74a5f9d3f2ca6e49f7bf8"><a name="a26b5d9cffcc74a5f9d3f2ca6e49f7bf8"></a><a name="a26b5d9cffcc74a5f9d3f2ca6e49f7bf8"></a>12005</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="a1be547b219c94e2cbb636d34d96f03d3"><a name="a1be547b219c94e2cbb636d34d96f03d3"></a><a name="a1be547b219c94e2cbb636d34d96f03d3"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="aeff3b8a380c54790b329e74ec8dd0970"><a name="aeff3b8a380c54790b329e74ec8dd0970"></a><a name="aeff3b8a380c54790b329e74ec8dd0970"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s9a458e4d74a1417984bd321ff1d64a93"></a>

<a name="t46fa32338459400c8f42811c89affc00"></a>
<table><thead align="left"><tr id="rc54d3b44e1714fb0bdbfcf55e3e91415"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="a987fad326c444c05826478afa59c627f"><a name="a987fad326c444c05826478afa59c627f"></a><a name="a987fad326c444c05826478afa59c627f"></a><strong id="a626f9a52c5894f30a485924b13d68076"><a name="a626f9a52c5894f30a485924b13d68076"></a><a name="a626f9a52c5894f30a485924b13d68076"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="ae367b54c48ea47c48e95681b9c1de3c4"><a name="ae367b54c48ea47c48e95681b9c1de3c4"></a><a name="ae367b54c48ea47c48e95681b9c1de3c4"></a><strong id="a41c28ea009bf4a458748bd0b7647f685"><a name="a41c28ea009bf4a458748bd0b7647f685"></a><a name="a41c28ea009bf4a458748bd0b7647f685"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r037cd56e8ab64254a58c16712a6e665b"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a00da395d4d854a3cbde5afc23b5925a3"><a name="a00da395d4d854a3cbde5afc23b5925a3"></a><a name="a00da395d4d854a3cbde5afc23b5925a3"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a024dd7fc0ccf471aa2ceec8b7dad710d"><a name="a024dd7fc0ccf471aa2ceec8b7dad710d"></a><a name="a024dd7fc0ccf471aa2ceec8b7dad710d"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="r93c811f9af3b44c38995f8656c9e5abc"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="afc6663f5fe2d4247a8bcba6170003d54"><a name="afc6663f5fe2d4247a8bcba6170003d54"></a><a name="afc6663f5fe2d4247a8bcba6170003d54"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="ab1639b29a9084222acac875aabfda1a6"><a name="ab1639b29a9084222acac875aabfda1a6"></a><a name="ab1639b29a9084222acac875aabfda1a6"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="r9a5c6ddcaf274b0fa22a4ed6d34b01ab"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="ae33b8845e5894966b2a1abd7f590b187"><a name="ae33b8845e5894966b2a1abd7f590b187"></a><a name="ae33b8845e5894966b2a1abd7f590b187"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a4e5540aa60364e6c8d434f00ed3f7c22"><a name="a4e5540aa60364e6c8d434f00ed3f7c22"></a><a name="a4e5540aa60364e6c8d434f00ed3f7c22"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s92e9ab0b166f4861b7c1a4dc75b36473"></a>

The Kerberos resources are abnormal and the Manager authentication service is unavailable. As a result, the security authentication function cannot be provided for upper-layer web services. Users may be unable to log in to Manager.

## Possible Causes<a name="s735430d5a9274735b35dae85edae8166"></a>

The OLdap resource on which the OKerberos depends is abnormal.

## Procedure<a name="s130b316db2464168af61dee776632da0"></a>

1.  Check whether the OLdap resource on which the OKerberos depends is abnormal in Manager.
    1.  Log in to the active management node.
    2.  Run the following command to check whether the OLdap resource managed by HA is in the normal state:

        **sh $\{BIGDATA\_HOME\}/OMSV100R001C00x8664/workspace0/ha/module/hacom/script/status\_ha.sh**

        The OLdap resource is in the normal state when it is in the  **Active\_normal** state on the active node and in the **Standby\_normal**  state on the standby node.

        -   If yes, go to  [3](#lfe4c30d108de4c628b11674811f9aff9).
        -   If no, go to  [2](#l7da3c3b34fd448b0a0ab71330e75955e).

2.  <a name="l7da3c3b34fd448b0a0ab71330e75955e"></a>See  [ALM-12004 OLdap Resource Is Abnormal](alm-12004-oldap-resource-is-abnormal.md)  for further assistance. After the OLdap resource status recovers, check whether the OKerberos resource is in the normal state.
    -   If yes, no further action is required.
    -   If no, go to  [3](#lfe4c30d108de4c628b11674811f9aff9).

3.  <a name="lfe4c30d108de4c628b11674811f9aff9"></a>Collect fault information.
    1.  On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="s6e41feef433e4041818bf455ee7af34c"></a>

N/A

