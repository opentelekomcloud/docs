# ALM-27003 DBService Heartbeat Interruption Between the Active and Standby Nodes<a name="EN-US_TOPIC_0125375682"></a>

## Description<a name="sc3487f1184cd46639d1860b185ced409"></a>

This alarm is generated when the active or standby DBService node does not receive heartbeat messages from the peer node. It is cleared when the heartbeat recovers.

## Attribute<a name="s92b37ad113db4acdb0529c4e163a3e03"></a>

<a name="en-us_topic_0035998746_table18176840"></a>
<table><thead align="left"><tr id="en-us_topic_0035998746_row123050"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="en-us_topic_0035998746_p9967070"><a name="en-us_topic_0035998746_p9967070"></a><a name="en-us_topic_0035998746_p9967070"></a>Alarm ID</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="en-us_topic_0035998746_p2026335"><a name="en-us_topic_0035998746_p2026335"></a><a name="en-us_topic_0035998746_p2026335"></a>Alarm Severity</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="en-us_topic_0035998746_p29915412"><a name="en-us_topic_0035998746_p29915412"></a><a name="en-us_topic_0035998746_p29915412"></a>Automatically Cleared</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998746_row7229285"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0035998746_p48701244"><a name="en-us_topic_0035998746_p48701244"></a><a name="en-us_topic_0035998746_p48701244"></a>27003</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0035998746_p52486654"><a name="en-us_topic_0035998746_p52486654"></a><a name="en-us_topic_0035998746_p52486654"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0035998746_p23560597"><a name="en-us_topic_0035998746_p23560597"></a><a name="en-us_topic_0035998746_p23560597"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s63371c82226a4bdb878d7f25ee1c560a"></a>

<a name="en-us_topic_0035998746_table29360233"></a>
<table><thead align="left"><tr id="en-us_topic_0035998746_row2035480"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0035998746_p30656219"><a name="en-us_topic_0035998746_p30656219"></a><a name="en-us_topic_0035998746_p30656219"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0035998746_p125790"><a name="en-us_topic_0035998746_p125790"></a><a name="en-us_topic_0035998746_p125790"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998746_row10189001"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998746_p20002757"><a name="en-us_topic_0035998746_p20002757"></a><a name="en-us_topic_0035998746_p20002757"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998746_p9610617"><a name="en-us_topic_0035998746_p9610617"></a><a name="en-us_topic_0035998746_p9610617"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998746_row19386696"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998746_p26818564"><a name="en-us_topic_0035998746_p26818564"></a><a name="en-us_topic_0035998746_p26818564"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998746_p24820109"><a name="en-us_topic_0035998746_p24820109"></a><a name="en-us_topic_0035998746_p24820109"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998746_row22054394"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998746_p41575456"><a name="en-us_topic_0035998746_p41575456"></a><a name="en-us_topic_0035998746_p41575456"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998746_p12168775"><a name="en-us_topic_0035998746_p12168775"></a><a name="en-us_topic_0035998746_p12168775"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998746_row42410114"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998746_p12667213"><a name="en-us_topic_0035998746_p12667213"></a><a name="en-us_topic_0035998746_p12667213"></a>Local DBService HA Name</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998746_p19411308"><a name="en-us_topic_0035998746_p19411308"></a><a name="en-us_topic_0035998746_p19411308"></a>Specifies a local DBService HA.</p>
</td>
</tr>
<tr id="en-us_topic_0035998746_row40484047"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998746_p57982344"><a name="en-us_topic_0035998746_p57982344"></a><a name="en-us_topic_0035998746_p57982344"></a>Peer DBService HA Name</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998746_p66058249"><a name="en-us_topic_0035998746_p66058249"></a><a name="en-us_topic_0035998746_p66058249"></a>Specifies a peer DBService HA.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="sf3572379468c4a63bfcb667bc3ab6102"></a>

During the DBService heartbeat interruption, only one node can provide services. If this node is faulty, no standby node is available for failover and the services become unavailable.

## Possible Causes<a name="s2c0a9f6148994190b385e477a1dbcbd4"></a>

The link between the active and standby DBService nodes is abnormal.

## Procedure<a name="s279dc4513c474478a18fd700479e8897"></a>

1.  Check whether the network between the active and standby DBService servers is in the normal state.
    1.  In the alarm list on MRS Manager, locate the row that contains the alarm, and view the IP address of the standby DBService server in the alarm details.
    2.  Log in to the active DBService server.
    3.  Run the  **ping** _heartbeat IP address of_ _the standby_ _DBService_  command to check whether the standby DBService server is reachable.
        -   If yes, go to  [2](#lab7350a8552548a9806916b60e68da69).
        -   If no, go to  [1.d](#l7079ef4a1be845c5b84275818adbbcaa).

    4.  <a name="l7079ef4a1be845c5b84275818adbbcaa"></a>Contact the network administrator to check whether the network is faulty.
        -   If yes, go to  [1.e](#l49fe060e9c664f6dbc39e491bd753c64).
        -   If no, go to  [2](#lab7350a8552548a9806916b60e68da69).

    5.  <a name="l49fe060e9c664f6dbc39e491bd753c64"></a>Rectify the network fault and check whether the alarm is cleared from the alarm list.
        -   If yes, no further action is required.
        -   If no, go to  [2](#lab7350a8552548a9806916b60e68da69).

2.  <a name="lab7350a8552548a9806916b60e68da69"></a>Collect fault information.
    1.  On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="sf93ca08bd32644a7a9796841b83eb6ed"></a>

N/A

