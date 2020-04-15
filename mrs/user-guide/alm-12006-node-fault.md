# ALM-12006 Node Fault<a name="EN-US_TOPIC_0125376074"></a>

## Description<a name="sb97f568031f148e9bd08d8bb0f9d19dc"></a>

Controller checks the NodeAgent status every 30 seconds. This alarm is generated when Controller fails to receive the status report of a NodeAgent for three times consecutively and is cleared when Controller can properly receive the status report of the NodeAgent.

## Attribute<a name="sa874f5a4152c43c981618c2f154171ab"></a>

<a name="tdf0d9fd35c1840528a329a7b3eba7c03"></a>
<table><thead align="left"><tr id="rea9a583e70844a8db19ce52f93772cf4"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="aeb1603889cb44f8cabc2e5cf32ec3239"><a name="aeb1603889cb44f8cabc2e5cf32ec3239"></a><a name="aeb1603889cb44f8cabc2e5cf32ec3239"></a><strong id="en-us_topic_0035461475_b244983011576"><a name="en-us_topic_0035461475_b244983011576"></a><a name="en-us_topic_0035461475_b244983011576"></a>Alarm ID</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="af32b1bf8053244a2800481b4445cf240"><a name="af32b1bf8053244a2800481b4445cf240"></a><a name="af32b1bf8053244a2800481b4445cf240"></a><strong id="afdec43eedaab41bdafa07c7d41231cdf"><a name="afdec43eedaab41bdafa07c7d41231cdf"></a><a name="afdec43eedaab41bdafa07c7d41231cdf"></a>Alarm Severity</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="a489bdc7d3fd94de5ade80287ae542421"><a name="a489bdc7d3fd94de5ade80287ae542421"></a><a name="a489bdc7d3fd94de5ade80287ae542421"></a><strong id="a632c6c19086a4aaebc8528a1f9dbec13"><a name="a632c6c19086a4aaebc8528a1f9dbec13"></a><a name="a632c6c19086a4aaebc8528a1f9dbec13"></a>Automatically Cleared</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r5dc330f580b3422fadced4cfe135cb85"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="a73b68d2a72bb4c78ad0fc22a298d7f54"><a name="a73b68d2a72bb4c78ad0fc22a298d7f54"></a><a name="a73b68d2a72bb4c78ad0fc22a298d7f54"></a>12006</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="a6a7a0f5dab944259b7b68e4ede1d529a"><a name="a6a7a0f5dab944259b7b68e4ede1d529a"></a><a name="a6a7a0f5dab944259b7b68e4ede1d529a"></a>Critical</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0035461475_p278925211576"><a name="en-us_topic_0035461475_p278925211576"></a><a name="en-us_topic_0035461475_p278925211576"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s31123a7e20594212ac92cf0a40c3148b"></a>

<a name="t28dac0dec97e470796bfaf8f9af42f25"></a>
<table><thead align="left"><tr id="r13cafb7af34b469cb698f2f3bb0d0464"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="a4954ed5782f5495fa7ef2815c01dfae2"><a name="a4954ed5782f5495fa7ef2815c01dfae2"></a><a name="a4954ed5782f5495fa7ef2815c01dfae2"></a><strong id="a687c9b6102b9452eb395e91727b3a072"><a name="a687c9b6102b9452eb395e91727b3a072"></a><a name="a687c9b6102b9452eb395e91727b3a072"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="a08c29a0a321c4b638338cd3166bb0cdd"><a name="a08c29a0a321c4b638338cd3166bb0cdd"></a><a name="a08c29a0a321c4b638338cd3166bb0cdd"></a><strong id="a7e2e6ce0b07b4e50ab212d00a4a8ef8d"><a name="a7e2e6ce0b07b4e50ab212d00a4a8ef8d"></a><a name="a7e2e6ce0b07b4e50ab212d00a4a8ef8d"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r0377f369a9b146d6aa1ba49188db2548"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a94d8cdc860e64ae69b55051b08f8d456"><a name="a94d8cdc860e64ae69b55051b08f8d456"></a><a name="a94d8cdc860e64ae69b55051b08f8d456"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="ab6992884ef2e4c47bab0eb1d38c1f2a3"><a name="ab6992884ef2e4c47bab0eb1d38c1f2a3"></a><a name="ab6992884ef2e4c47bab0eb1d38c1f2a3"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="r1077c828ca0048959444a09e5a735f31"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a28c0406e223f491c9b47ac78378d0dc8"><a name="a28c0406e223f491c9b47ac78378d0dc8"></a><a name="a28c0406e223f491c9b47ac78378d0dc8"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a204120d3597940c78b238f8b25bcd565"><a name="a204120d3597940c78b238f8b25bcd565"></a><a name="a204120d3597940c78b238f8b25bcd565"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="r19b17b50b48746aba5ef800a29ff0dcc"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a0629514645024319a97ed58cb2682ac4"><a name="a0629514645024319a97ed58cb2682ac4"></a><a name="a0629514645024319a97ed58cb2682ac4"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="ab34a72bca4f74b13984b98533a885c10"><a name="ab34a72bca4f74b13984b98533a885c10"></a><a name="ab34a72bca4f74b13984b98533a885c10"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s63d9ad3a6a5b409bb8a9cc3941654415"></a>

Services on the node are unavailable.

## Possible Causes<a name="sfbe6b2ed0b70484e8f85c9a5cd6e241b"></a>

The network is disconnected or the hardware is faulty.

## Procedure<a name="s04b13cd89cd4443093cbe1f0d35c6e59"></a>

1.  Check whether the network is disconnected or the hardware is faulty.
    1.  In the alarm list on MRS Manager, locate the row that contains the alarm, and view its host address in the alarm details.
    2.  Log in to the active management node.
    3.  Run the following command to check whether the faulty node is reachable:

        **ping** _IP address of the faulty host_

        1.  If yes, go to  [2](#l29180cefa5e0486b9b5cc7f458e5b51c).
        2.  If no, go to  [1.d](#la89e4a443e1a42de8b50c4481de1fdd5).

    4.  <a name="la89e4a443e1a42de8b50c4481de1fdd5"></a>Contact the public cloud O&M personnel to check whether a network fault occurs and rectify the fault.
        -   If yes, go to  [2](#l29180cefa5e0486b9b5cc7f458e5b51c).
        -   If no, go to  [1.f](#l92526bdf019d479b90aec39dbf7190a8).

    5.  Rectify the network fault and check whether the alarm is cleared from the alarm list.
        -   If yes, no further action is required.
        -   If no, go to  [1.f](#l92526bdf019d479b90aec39dbf7190a8).

    6.  <a name="l92526bdf019d479b90aec39dbf7190a8"></a>Contact the public cloud O&M personnel to check whether a hardware fault \(for example, a CPU fault or memory fault\) occurs on the node.
        -   If yes, go to  [1.g](#l9c5c6900f4a44bfcad474d87c7de8f17).
        -   If no, go to  [2](#l29180cefa5e0486b9b5cc7f458e5b51c).

    7.  <a name="l9c5c6900f4a44bfcad474d87c7de8f17"></a>Repair the faulty components and restart the node. Check whether the alarm is cleared from the alarm list.
        -   If yes, no further action is required.
        -   If no, go to  [2](#l29180cefa5e0486b9b5cc7f458e5b51c).

2.  <a name="l29180cefa5e0486b9b5cc7f458e5b51c"></a>Collect fault information.
    1.  On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="s8f8e2708d8184b3b8f62f8bf0a2bf53d"></a>

N/A

