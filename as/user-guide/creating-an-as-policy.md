# Creating an AS Policy<a name="EN-US_TOPIC_0151270383"></a>

## Scenarios<a name="section2495449014355"></a>

You can manage instances in an AS group through AS policies. This section describes how to create an AS policy.

## Creating an Alarm Policy<a name="section28492877113953"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner to select a region and a project.
3.  Under  **Computing**, click  **Auto Scaling**. In the navigation pane on the left, choose  **Instance Scaling**.
4.  Locate the row containing the target AS group and click  **View AS Policy**  in the  **Operation**  column.
5.  On the  **AS Policies**  page, click  **Add**.
6.  Set the parameters listed in  [Table 1](#table442371481205).

    **Table  1**  AS policy parameters

    <a name="table442371481205"></a>
    <table><thead align="left"><tr id="row577295371205"><th class="cellrowborder" valign="top" width="22.81%" id="mcps1.2.4.1.1"><p id="p75748481205"><a name="p75748481205"></a><a name="p75748481205"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="43.480000000000004%" id="mcps1.2.4.1.2"><p id="p95829881205"><a name="p95829881205"></a><a name="p95829881205"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.71%" id="mcps1.2.4.1.3"><p id="p380245311205"><a name="p380245311205"></a><a name="p380245311205"></a>Example Value</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row66764651205"><td class="cellrowborder" valign="top" width="22.81%" headers="mcps1.2.4.1.1 "><p id="p39228151205"><a name="p39228151205"></a><a name="p39228151205"></a>Policy Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.480000000000004%" headers="mcps1.2.4.1.2 "><p id="p493125731205"><a name="p493125731205"></a><a name="p493125731205"></a>Specifies the name of the AS policy to be created.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.71%" headers="mcps1.2.4.1.3 "><p id="p348954431205"><a name="p348954431205"></a><a name="p348954431205"></a>as-policy-p6g5</p>
    </td>
    </tr>
    <tr id="row456235351205"><td class="cellrowborder" valign="top" width="22.81%" headers="mcps1.2.4.1.1 "><p id="p45188451205"><a name="p45188451205"></a><a name="p45188451205"></a>Policy Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.480000000000004%" headers="mcps1.2.4.1.2 "><p id="p4986700115224"><a name="p4986700115224"></a><a name="p4986700115224"></a>Select <strong id="b842352706171152"><a name="b842352706171152"></a><a name="b842352706171152"></a>Alarm</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.71%" headers="mcps1.2.4.1.3 "><p id="p531365191205"><a name="p531365191205"></a><a name="p531365191205"></a>Alarm</p>
    </td>
    </tr>
    <tr id="row84666261205"><td class="cellrowborder" valign="top" width="22.81%" headers="mcps1.2.4.1.1 "><p id="p147080751205"><a name="p147080751205"></a><a name="p147080751205"></a>Alarm Rule</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.480000000000004%" headers="mcps1.2.4.1.2 "><p id="p505033881205"><a name="p505033881205"></a><a name="p505033881205"></a>Specifies whether a new alarm rule is to be created (<strong id="b16955153314166"><a name="b16955153314166"></a><a name="b16955153314166"></a>Create</strong>) or an existing alarm rule will be used (<strong id="b99568335160"><a name="b99568335160"></a><a name="b99568335160"></a>Use existing</strong>).</p>
    <div class="p" id="p2787840394913"><a name="p2787840394913"></a><a name="p2787840394913"></a>To create an alarm rule, configure the following parameters:<a name="ul340997094947"></a><a name="ul340997094947"></a><ul id="ul340997094947"><li>Alarm Rule Name<p id="p2649132795040"><a name="p2649132795040"></a><a name="p2649132795040"></a>Specifies the name of the new alarm rule, for example, <strong id="b842352706172220"><a name="b842352706172220"></a><a name="b842352706172220"></a>as-alarm-7o1u</strong>.</p>
    </li><li>Trigger Condition<p id="p182080359512"><a name="p182080359512"></a><a name="p182080359512"></a>Specifies a monitoring metric and condition for triggering a scaling action. For example, when CPU Usage becomes higher than 70%, AS automatically triggers a scaling action.</p>
    </li><li>Monitoring Interval<p id="p3466834095116"><a name="p3466834095116"></a><a name="p3466834095116"></a>Specifies the interval (such as five minutes) at which the alarm status is updated based on the alarm rule.</p>
    </li><li>Consecutive Occurrences<p id="p4052459495128"><a name="p4052459495128"></a><a name="p4052459495128"></a>Specifies the number of sampling points when an alarm is triggered. If <strong id="b842352706164722"><a name="b842352706164722"></a><a name="b842352706164722"></a>Occurrences</strong> is set to <strong id="b569758072164351"><a name="b569758072164351"></a><a name="b569758072164351"></a>n</strong>, the sampling points of the alarm rule are the sampling points in n consecutive sampling periods. Only if all the sampling points meet the threshold configured for the alarm rule will the alarm rule status be refreshed as the <strong id="b412799387164351"><a name="b412799387164351"></a><a name="b412799387164351"></a>Alarm</strong> status.</p>
    </li></ul>
    </div>
    </td>
    <td class="cellrowborder" valign="top" width="33.71%" headers="mcps1.2.4.1.3 "><p id="p642426221205"><a name="p642426221205"></a><a name="p642426221205"></a>N/A</p>
    </td>
    </tr>
    <tr id="row413126881205"><td class="cellrowborder" valign="top" width="22.81%" headers="mcps1.2.4.1.1 "><p id="p579934701205"><a name="p579934701205"></a><a name="p579934701205"></a>Scaling Action</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.480000000000004%" headers="mcps1.2.4.1.2 "><p id="p669595041205"><a name="p669595041205"></a><a name="p669595041205"></a>Specifies an action and the number or percentage of instances.</p>
    <div class="p" id="p36260748141218"><a name="p36260748141218"></a><a name="p36260748141218"></a>The following scaling action options are available:<a name="ul30641360141052"></a><a name="ul30641360141052"></a><ul id="ul30641360141052"><li>Add<p id="p2001153810029"><a name="p2001153810029"></a><a name="p2001153810029"></a>Adds instances to an AS group when the scaling action is performed.</p>
    </li><li>Reduce<p id="p5844171910128"><a name="p5844171910128"></a><a name="p5844171910128"></a>Removes instances from an AS group when the scaling action is performed.</p>
    </li><li>Set to<p id="p6129265410320"><a name="p6129265410320"></a><a name="p6129265410320"></a>Sets the expected number of instances in an AS group to a specified value.</p>
    </li></ul>
    </div>
    </td>
    <td class="cellrowborder" valign="top" width="33.71%" headers="mcps1.2.4.1.3 "><a name="ul38301652103420"></a><a name="ul38301652103420"></a><ul id="ul38301652103420"><li>Add 1 instance</li><li>Add 10% instances<div class="p" id="p36309970101916"><a name="p36309970101916"></a><a name="p36309970101916"></a>The number of instances to be added is 10% of the current number of instances in the AS group. If the product of the current number of instances and the percentage is not an integer, AS automatically rounds the value up or down:<a name="ul25878962102313"></a><a name="ul25878962102313"></a><ul id="ul25878962102313"><li>Rounds down the value that is greater than 1. </li></ul>
    <a name="ul13699143102321"></a><a name="ul13699143102321"></a><ul id="ul13699143102321"><li>Rounds up the value that is greater than 0 and less than 1 to 1. </li></ul>
    </div>
    </li></ul>
    </td>
    </tr>
    <tr id="row253348581205"><td class="cellrowborder" valign="top" width="22.81%" headers="mcps1.2.4.1.1 "><p id="p388576551205"><a name="p388576551205"></a><a name="p388576551205"></a>Cooldown Period</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.480000000000004%" headers="mcps1.2.4.1.2 "><p id="p21343661141258"><a name="p21343661141258"></a><a name="p21343661141258"></a>Specifies a period of time after each scaling action is complete. During the cooldown period, scaling actions triggered by alarms will be denied. Scheduled and periodic scaling actions are not restricted.</p>
    <div class="note" id="note57875228141258"><a name="note57875228141258"></a><a name="note57875228141258"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul51115008141258"></a><a name="ul51115008141258"></a><ul id="ul51115008141258"><li>If a scaling action is triggered by an AS policy, the cooldown period is that which is configured for that AS policy.</li><li>If a scaling action is triggered by manually changing the expected number of instances or by other actions, the cooldown period is that which is configured for the AS group. </li></ul>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="33.71%" headers="mcps1.2.4.1.3 "><p id="p31638772"><a name="p31638772"></a><a name="p31638772"></a>300</p>
    </td>
    </tr>
    </tbody>
    </table>

7.  Click  **OK**.

    The newly added AS policy is displayed on the  **AS Policy**  tab. In addition, the AS policy is in  **Enabled**  state by default.


## Creating a Scheduled or Periodic Policy<a name="section72110321079"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner to select a region and a project.
3.  Under  **Computing**, click  **Auto Scaling**. In the navigation pane on the left, choose  **Instance Scaling**.
4.  Locate the row containing the target AS group and click  **View AS Policy**  in the  **Operation**  column.
5.  On the  **AS Policies**  page, click  **Add**.
6.  Configure the parameters listed in  [Table 2](#table8241103213712).

    **Table  2**  Parameter description

    <a name="table8241103213712"></a>
    <table><thead align="left"><tr id="row112475325713"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="p162481932873"><a name="p162481932873"></a><a name="p162481932873"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="44%" id="mcps1.2.4.1.2"><p id="p62511632471"><a name="p62511632471"></a><a name="p62511632471"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="33%" id="mcps1.2.4.1.3"><p id="p725343213717"><a name="p725343213717"></a><a name="p725343213717"></a>Example Value</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row11255332778"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p62598323718"><a name="p62598323718"></a><a name="p62598323718"></a>Policy Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.4.1.2 "><p id="p62611232772"><a name="p62611232772"></a><a name="p62611232772"></a>Specifies the name of the AS policy to be created.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.3 "><p id="p122652326712"><a name="p122652326712"></a><a name="p122652326712"></a>as-policy-p6g5</p>
    </td>
    </tr>
    <tr id="row182651326713"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p0266143220716"><a name="p0266143220716"></a><a name="p0266143220716"></a>Policy Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.4.1.2 "><p id="p28700433104726"><a name="p28700433104726"></a><a name="p28700433104726"></a>Select <strong id="b842352706183028"><a name="b842352706183028"></a><a name="b842352706183028"></a>Scheduled</strong> or <strong id="b842352706183031"><a name="b842352706183031"></a><a name="b842352706183031"></a>Periodic</strong> for expanding resources at a specified time.</p>
    <p id="p43666380115020"><a name="p43666380115020"></a><a name="p43666380115020"></a>If you select <strong id="b26692513118313"><a name="b26692513118313"></a><a name="b26692513118313"></a>Periodic</strong>, you are required to configure two more parameters:</p>
    <a name="ul112044208127"></a><a name="ul112044208127"></a><ul id="ul112044208127"><li>Interval<a name="ul5794335214657"></a><a name="ul5794335214657"></a><ul id="ul5794335214657"><li>One day</li><li>One week</li><li>One month</li></ul>
    </li></ul>
    <a name="ul54876080115118"></a><a name="ul54876080115118"></a><ul id="ul54876080115118"><li>Time Range<p id="p417886214753"><a name="p417886214753"></a><a name="p417886214753"></a>Specifies a time range during which the AS policy can be triggered.</p>
    </li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.3 "><p id="p1129012323718"><a name="p1129012323718"></a><a name="p1129012323718"></a>N/A</p>
    </td>
    </tr>
    <tr id="row192922321570"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p1829411325712"><a name="p1829411325712"></a><a name="p1829411325712"></a>Triggered At</p>
    </td>
    <td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.4.1.2 "><p id="p11297932777"><a name="p11297932777"></a><a name="p11297932777"></a>Specifies a time at which the AS policy is triggered.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.3 "><p id="p1629833218711"><a name="p1629833218711"></a><a name="p1629833218711"></a>N/A</p>
    </td>
    </tr>
    <tr id="row103002321179"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p1230123210713"><a name="p1230123210713"></a><a name="p1230123210713"></a>Scaling Action</p>
    </td>
    <td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.4.1.2 "><p id="p59032121112324"><a name="p59032121112324"></a><a name="p59032121112324"></a>Specifies an action and the number of instances.</p>
    <div class="p" id="p61527048112324"><a name="p61527048112324"></a><a name="p61527048112324"></a>The following scaling action options are available:<a name="ul16872520112324"></a><a name="ul16872520112324"></a><ul id="ul16872520112324"><li>Add<p id="p24496875112324"><a name="p24496875112324"></a><a name="p24496875112324"></a>Adds instances to an AS group when the scaling action is performed.</p>
    </li><li>Reduce<p id="p38089867112324"><a name="p38089867112324"></a><a name="p38089867112324"></a>Removes instances from an AS group when the scaling action is performed.</p>
    </li><li>Set to<p id="p65380367112324"><a name="p65380367112324"></a><a name="p65380367112324"></a>Sets the expected number of instances in an AS group to a specified value.</p>
    </li></ul>
    </div>
    </td>
    <td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.3 "><a name="ul031716322711"></a><a name="ul031716322711"></a><ul id="ul031716322711"><li>Add 1 instance</li><li>Add 10% instances<p id="p163241032176"><a name="p163241032176"></a><a name="p163241032176"></a>The number of instances to be added is 10% of the current number of instances in the AS group. If the product of the current number of instances and the percentage is not an integer, AS automatically rounds the value up or down:</p>
    </li></ul>
    <a name="ul132693220716"></a><a name="ul132693220716"></a><ul id="ul132693220716"><li>Rounds down the value that is greater than 1. </li></ul>
    <a name="ul633133211711"></a><a name="ul633133211711"></a><ul id="ul633133211711"><li>Rounds up the value that is greater than 0 and less than 1 to 1. </li></ul>
    </td>
    </tr>
    <tr id="row1933516326711"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p19338232175"><a name="p19338232175"></a><a name="p19338232175"></a>Cooldown Period</p>
    </td>
    <td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.4.1.2 "><p id="p334110321475"><a name="p334110321475"></a><a name="p334110321475"></a>Specifies a period of time after each scaling action is complete. During the cooldown period, scaling actions triggered by alarms will be denied. Scheduled and periodic scaling actions are not restricted.</p>
    <div class="note" id="note9345143219717"><a name="note9345143219717"></a><a name="note9345143219717"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul153471326710"></a><a name="ul153471326710"></a><ul id="ul153471326710"><li>If a scaling action is triggered by an AS policy, the cooldown period is that which is configured for that AS policy.</li><li>If a scaling action is triggered by manually changing the expected number of instances or by other actions, the cooldown period is that which is configured for the AS group. </li></ul>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.3 "><p id="p835423216719"><a name="p835423216719"></a><a name="p835423216719"></a>300</p>
    </td>
    </tr>
    </tbody>
    </table>


1.  Click  **OK**.

    The newly added AS policy is displayed on the  **AS Policy**  tab. In addition, the AS policy is in  **Enabled**  state by default.


>![](public_sys-resources/icon-note.gif) **NOTE:**   
>If you have created scheduled or periodic AS policies that are triggered at the same time, AS will execute the one created later. This constraint does not apply to alarm-triggered AS policies.  

