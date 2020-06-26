# Creating a Bandwidth Scaling Policy<a name="EN-US_TOPIC_0112331243"></a>

AS supports adjusting the purchased EIP bandwidth and shared bandwidth. This section describes how to create a bandwidth scaling policy to automatically adjust the bandwidths. The system supports three types of policies, including alarm-based, scheduled, and periodic. The basic information for creating a bandwidth scaling policy includes the policy name, policy type, and trigger condition.

## Creating an Alarm-based Bandwidth Scaling Policy<a name="en-us_topic_0042018368_section1488828102454"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner to select a region and a project.
3.  Under  **Computing**, click  **Auto Scaling**. In the navigation pane on the left, choose  **Bandwidth Scaling**.
4.  Click  **Create Bandwidth Scaling Policy**.
5.  Set parameters, such as the policy name, , policy type, and trigger condition. For details, see  [Creating a Bandwidth Scaling Policy](creating-a-bandwidth-scaling-policy.md).

    **Table  1**  Alarm policy parameters

    <a name="table1795013419434"></a>
    <table><thead align="left"><tr id="row7937184118438"><th class="cellrowborder" valign="top" width="17.17%" id="mcps1.2.4.1.1"><p id="p11936241194311"><a name="p11936241194311"></a><a name="p11936241194311"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="64.65%" id="mcps1.2.4.1.2"><p id="p159366417432"><a name="p159366417432"></a><a name="p159366417432"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.180000000000003%" id="mcps1.2.4.1.3"><p id="p8937141144312"><a name="p8937141144312"></a><a name="p8937141144312"></a>Example Value</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8754131033415"><td class="cellrowborder" valign="top" width="17.17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0042018359_p51849531448"><a name="en-us_topic_0042018359_p51849531448"></a><a name="en-us_topic_0042018359_p51849531448"></a>Region</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.65%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0042018359_p17184175316413"><a name="en-us_topic_0042018359_p17184175316413"></a><a name="en-us_topic_0042018359_p17184175316413"></a>Specifies the region where the AS group resides.</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.180000000000003%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0042018359_p12184135316415"><a name="en-us_topic_0042018359_p12184135316415"></a><a name="en-us_topic_0042018359_p12184135316415"></a>N/A</p>
    </td>
    </tr>
    <tr id="row2937141124311"><td class="cellrowborder" valign="top" width="17.17%" headers="mcps1.2.4.1.1 "><p id="p993774110436"><a name="p993774110436"></a><a name="p993774110436"></a>Policy Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.65%" headers="mcps1.2.4.1.2 "><p id="p179375412436"><a name="p179375412436"></a><a name="p179375412436"></a>Specifies the name of the bandwidth scaling policy.</p>
    <p id="p893711416433"><a name="p893711416433"></a><a name="p893711416433"></a>The name consists of only letters, digits, underscores (_), and hyphens (-).</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.180000000000003%" headers="mcps1.2.4.1.3 "><p id="p7937134164312"><a name="p7937134164312"></a><a name="p7937134164312"></a>N/A</p>
    </td>
    </tr>
    <tr id="row6937641144318"><td class="cellrowborder" valign="top" width="17.17%" headers="mcps1.2.4.1.1 "><p id="p814113820394"><a name="p814113820394"></a><a name="p814113820394"></a>EIP</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.65%" headers="mcps1.2.4.1.2 "><p id="p12937194154314"><a name="p12937194154314"></a><a name="p12937194154314"></a>Specifies the public network IP address whose bandwidth needs to be scaled.</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.180000000000003%" headers="mcps1.2.4.1.3 "><p id="p189371415436"><a name="p189371415436"></a><a name="p189371415436"></a>N/A</p>
    </td>
    </tr>
    <tr id="row19938541144319"><td class="cellrowborder" valign="top" width="17.17%" headers="mcps1.2.4.1.1 "><p id="p89376417435"><a name="p89376417435"></a><a name="p89376417435"></a>Policy Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.65%" headers="mcps1.2.4.1.2 "><p id="p4986700115224"><a name="p4986700115224"></a><a name="p4986700115224"></a>Select <strong id="b842352706171152"><a name="b842352706171152"></a><a name="b842352706171152"></a>Alarm</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.180000000000003%" headers="mcps1.2.4.1.3 "><p id="p19381410437"><a name="p19381410437"></a><a name="p19381410437"></a>Alarm</p>
    </td>
    </tr>
    <tr id="row17938441114315"><td class="cellrowborder" valign="top" width="17.17%" headers="mcps1.2.4.1.1 "><p id="p147080751205"><a name="p147080751205"></a><a name="p147080751205"></a>Alarm Rule</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.65%" headers="mcps1.2.4.1.2 "><p id="p505033881205"><a name="p505033881205"></a><a name="p505033881205"></a>You can use an existing alarm rule or create a new one. </p>
    <div class="p" id="p2787840394913"><a name="p2787840394913"></a><a name="p2787840394913"></a>To create an alarm rule, configure the following parameters:<a name="ul340997094947"></a><a name="ul340997094947"></a><ul id="ul340997094947"><li>Alarm Rule Name<p id="p2649132795040"><a name="p2649132795040"></a><a name="p2649132795040"></a>Specifies the name of the new alarm rule, for example, <strong id="b842352706172220"><a name="b842352706172220"></a><a name="b842352706172220"></a>as-alarm-7o1u</strong>.</p>
    </li><li>Trigger Condition<p id="p182080359512"><a name="p182080359512"></a><a name="p182080359512"></a>Select a monitoring metric and trigger condition based on the metric. <a href="#table46471722185419">Table 2</a> lists the supported monitoring metrics. An example value is <strong id="b79130453388"><a name="b79130453388"></a><a name="b79130453388"></a>Outbound Bandwidth</strong> <strong id="b883518145391"><a name="b883518145391"></a><a name="b883518145391"></a> Avg. &gt; 100 bit/s</strong></p>
    </li><li>Monitoring Interval<p id="p3466834095116"><a name="p3466834095116"></a><a name="p3466834095116"></a>Specifies the period for the metric, for example, 5 minutes.</p>
    </li><li>Consecutive Occurrences<p id="p4052459495128"><a name="p4052459495128"></a><a name="p4052459495128"></a>Specifies the number of consecutive times, for example, one time, for triggering a scaling action during a monitoring period.</p>
    </li></ul>
    </div>
    </td>
    <td class="cellrowborder" valign="top" width="18.180000000000003%" headers="mcps1.2.4.1.3 "><p id="p6938194120437"><a name="p6938194120437"></a><a name="p6938194120437"></a>N/A</p>
    </td>
    </tr>
    <tr id="row43276614816"><td class="cellrowborder" valign="top" width="17.17%" headers="mcps1.2.4.1.1 "><p id="p579934701205"><a name="p579934701205"></a><a name="p579934701205"></a>Scaling Action</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.65%" headers="mcps1.2.4.1.2 "><p id="p669595041205"><a name="p669595041205"></a><a name="p669595041205"></a>Specifies the execution action in the AS policy.</p>
    <div class="p" id="p36260748141218"><a name="p36260748141218"></a><a name="p36260748141218"></a>The following scaling action options are available:<a name="ul30641360141052"></a><a name="ul30641360141052"></a><ul id="ul30641360141052"><li>Add<p id="p2001153810029"><a name="p2001153810029"></a><a name="p2001153810029"></a>When a scaling action is triggered, the bandwidth is increased.</p>
    </li><li>Reduce<p id="p5844171910128"><a name="p5844171910128"></a><a name="p5844171910128"></a>When a scaling action is triggered, the bandwidth is decreased.</p>
    </li><li>Set to<p id="p6129265410320"><a name="p6129265410320"></a><a name="p6129265410320"></a>The bandwidth is set to a fixed value.</p>
    <div class="note" id="note15858554135611"><a name="note15858554135611"></a><a name="note15858554135611"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p3858145425617"><a name="p3858145425617"></a><a name="p3858145425617"></a>The step (minimum unit for bandwidth adjustment) varies depending on the bandwidth value range. The bandwidth will be automatically adjusted to the nearest value according to the actual step.</p>
    <a name="ul9790510185"></a><a name="ul9790510185"></a><ul id="ul9790510185"><li>If the bandwidth is less than or equal to 300 Mbit/s, the default step is 1 Mbit/s.</li><li>If the bandwidth ranges from 300 Mbit/s to 500 Mbit/s, the default step is 50 Mbit/s.</li></ul>
    </div></div>
    </li></ul>
    </div>
    </td>
    <td class="cellrowborder" valign="top" width="18.180000000000003%" headers="mcps1.2.4.1.3 "><p id="p332776114815"><a name="p332776114815"></a><a name="p332776114815"></a>N/A</p>
    </td>
    </tr>
    <tr id="row1063441813127"><td class="cellrowborder" valign="top" width="17.17%" headers="mcps1.2.4.1.1 "><p id="p663511810129"><a name="p663511810129"></a><a name="p663511810129"></a>Limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.65%" headers="mcps1.2.4.1.2 "><p id="p8369352121418"><a name="p8369352121418"></a><a name="p8369352121418"></a>Specifies the maximum and minimum bandwidth allowed (Mbit/s).</p>
    <a name="ul2026774911619"></a><a name="ul2026774911619"></a><ul id="ul2026774911619"><li>When <strong id="b1210316197208"><a name="b1210316197208"></a><a name="b1210316197208"></a>Scaling Action</strong> is set to <strong id="b7351152572016"><a name="b7351152572016"></a><a name="b7351152572016"></a>Add</strong>, this parameter specifies the maximum bandwidth allowed.</li><li>When <strong id="b15721152172019"><a name="b15721152172019"></a><a name="b15721152172019"></a>Scaling Action</strong> is set to <strong id="b19573205218201"><a name="b19573205218201"></a><a name="b19573205218201"></a>Reduce</strong>, this parameter specifies the minimum bandwidth allowed.<div class="note" id="note331014568524"><a name="note331014568524"></a><a name="note331014568524"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p11310356135217"><a name="p11310356135217"></a><a name="p11310356135217"></a>This parameter is unavailable if <strong id="b1607125012112"><a name="b1607125012112"></a><a name="b1607125012112"></a>Scaling Action</strong> is <strong id="b38391116142216"><a name="b38391116142216"></a><a name="b38391116142216"></a>Set to</strong>.</p>
    </div></div>
    </li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="18.180000000000003%" headers="mcps1.2.4.1.3 "><p id="p10635131811214"><a name="p10635131811214"></a><a name="p10635131811214"></a>50 Mbit/s</p>
    </td>
    </tr>
    <tr id="row149391541174310"><td class="cellrowborder" valign="top" width="17.17%" headers="mcps1.2.4.1.1 "><p id="p1793884111433"><a name="p1793884111433"></a><a name="p1793884111433"></a>Cooldown Period</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.65%" headers="mcps1.2.4.1.2 "><p id="p0938104164312"><a name="p0938104164312"></a><a name="p0938104164312"></a>Specifies a period of time in the unit of second after each scaling action is complete. During the cooldown period, scaling actions triggered by alarms will be denied. Scheduled and periodic scaling actions are not restricted.</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.180000000000003%" headers="mcps1.2.4.1.3 "><p id="p189393413439"><a name="p189393413439"></a><a name="p189393413439"></a>300</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  Monitoring metrics supported by the alarm policy

    <a name="table46471722185419"></a>
    <table><thead align="left"><tr id="row13647122225415"><th class="cellrowborder" valign="top" width="30.470000000000002%" id="mcps1.2.3.1.1"><p id="p15647182218541"><a name="p15647182218541"></a><a name="p15647182218541"></a>Metric</p>
    </th>
    <th class="cellrowborder" valign="top" width="69.53%" id="mcps1.2.3.1.2"><p id="p1465761020565"><a name="p1465761020565"></a><a name="p1465761020565"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row364711220544"><td class="cellrowborder" valign="top" width="30.470000000000002%" headers="mcps1.2.3.1.1 "><p id="p4647222185415"><a name="p4647222185415"></a><a name="p4647222185415"></a>Inbound Bandwidth</p>
    </td>
    <td class="cellrowborder" valign="top" width="69.53%" headers="mcps1.2.3.1.2 "><p id="p165719107561"><a name="p165719107561"></a><a name="p165719107561"></a>Indicates the network rate of inbound traffic.</p>
    </td>
    </tr>
    <tr id="row3647172295416"><td class="cellrowborder" valign="top" width="30.470000000000002%" headers="mcps1.2.3.1.1 "><p id="p20647182216541"><a name="p20647182216541"></a><a name="p20647182216541"></a>Inbound Traffic</p>
    </td>
    <td class="cellrowborder" valign="top" width="69.53%" headers="mcps1.2.3.1.2 "><p id="p146578106562"><a name="p146578106562"></a><a name="p146578106562"></a>Indicates the network traffic going into the cloud platform.</p>
    </td>
    </tr>
    <tr id="row186471122115416"><td class="cellrowborder" valign="top" width="30.470000000000002%" headers="mcps1.2.3.1.1 "><p id="p1664962212542"><a name="p1664962212542"></a><a name="p1664962212542"></a>Outbound Bandwidth</p>
    </td>
    <td class="cellrowborder" valign="top" width="69.53%" headers="mcps1.2.3.1.2 "><p id="p9657171020565"><a name="p9657171020565"></a><a name="p9657171020565"></a>Indicates the network rate of outbound traffic.</p>
    </td>
    </tr>
    <tr id="row764952215419"><td class="cellrowborder" valign="top" width="30.470000000000002%" headers="mcps1.2.3.1.1 "><p id="p964916229543"><a name="p964916229543"></a><a name="p964916229543"></a>Outbound Traffic</p>
    </td>
    <td class="cellrowborder" valign="top" width="69.53%" headers="mcps1.2.3.1.2 "><p id="p465711018568"><a name="p465711018568"></a><a name="p465711018568"></a>Indicates the network traffic going out of the cloud platform.</p>
    </td>
    </tr>
    </tbody>
    </table>

6.  After setting the parameters, click  **Create Now**.

    The newly created bandwidth scaling policy is displayed on the  **Bandwidth Scaling**  page and is in  **Enabled**  state by default.


## Creating a Scheduled or Periodic Bandwidth Scaling Policy<a name="section14132201851120"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner to select a region and a project.
3.  Under  **Computing**, click  **Auto Scaling**. In the navigation pane on the left, choose  **Bandwidth Scaling**.
4.  Click  **Create Bandwidth Scaling Policy**.
5.  Set parameters, such as the policy name, policy type, and trigger condition. For details, see  [Table 3](#table085923816615).

    **Table  3**  Scheduled or periodic policy parameters

    <a name="table085923816615"></a>
    <table><thead align="left"><tr id="row11860143815611"><th class="cellrowborder" valign="top" width="15%" id="mcps1.2.4.1.1"><p id="p75748481205"><a name="p75748481205"></a><a name="p75748481205"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="67%" id="mcps1.2.4.1.2"><p id="p95829881205"><a name="p95829881205"></a><a name="p95829881205"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.3"><p id="p380245311205"><a name="p380245311205"></a><a name="p380245311205"></a>Example Value</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1853513215353"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.1 "><p id="p3328114103513"><a name="p3328114103513"></a><a name="p3328114103513"></a>Region</p>
    </td>
    <td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.2 "><p id="p7331104143510"><a name="p7331104143510"></a><a name="p7331104143510"></a>Specifies the region where the AS group resides.</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.3 "><p id="p6333143353"><a name="p6333143353"></a><a name="p6333143353"></a>N/A</p>
    </td>
    </tr>
    <tr id="row148601738166"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.1 "><p id="p39228151205"><a name="p39228151205"></a><a name="p39228151205"></a>Policy Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.2 "><p id="p19916233717"><a name="p19916233717"></a><a name="p19916233717"></a>Specifies the name of the bandwidth scaling policy.</p>
    <p id="p103996351276"><a name="p103996351276"></a><a name="p103996351276"></a>The name consists of only letters, digits, underscores (_), and hyphens (-).</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.3 "><p id="p348954431205"><a name="p348954431205"></a><a name="p348954431205"></a>as-policy-p6g5</p>
    </td>
    </tr>
    <tr id="row17368754674"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.1 "><p id="p198051448182711"><a name="p198051448182711"></a><a name="p198051448182711"></a>EIP</p>
    </td>
    <td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.2 "><p id="p7369189483"><a name="p7369189483"></a><a name="p7369189483"></a>Specifies the public network IP address whose bandwidth needs to be scaled. This parameter is mandatory when <strong id="b561950133411"><a name="b561950133411"></a><a name="b561950133411"></a>Resource Type</strong> is set to <strong id="b14638558103520"><a name="b14638558103520"></a><a name="b14638558103520"></a>EIP</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.3 "><p id="p143741291187"><a name="p143741291187"></a><a name="p143741291187"></a>N/A</p>
    </td>
    </tr>
    <tr id="row286063818614"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.1 "><p id="p45188451205"><a name="p45188451205"></a><a name="p45188451205"></a>Policy Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.2 "><p id="p28700433104726"><a name="p28700433104726"></a><a name="p28700433104726"></a>Specifies the policy type. You can select a scheduled or periodic policy.</p>
    <p id="p43666380115020"><a name="p43666380115020"></a><a name="p43666380115020"></a>If you select <strong id="b26692513118313"><a name="b26692513118313"></a><a name="b26692513118313"></a>Periodic</strong>, you are required to configure two more parameters:</p>
    <a name="ul54876080115118"></a><a name="ul54876080115118"></a><ul id="ul54876080115118"><li>Time Range<p id="p417886214753"><a name="p417886214753"></a><a name="p417886214753"></a>Specifies a time range during which the AS policy can be triggered.</p>
    </li><li>Interval<a name="ul5794335214657"></a><a name="ul5794335214657"></a><ul id="ul5794335214657"><li>One day</li><li>One week</li><li>One month</li></ul>
    </li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.3 "><p id="p531365191205"><a name="p531365191205"></a><a name="p531365191205"></a>N/A</p>
    </td>
    </tr>
    <tr id="row17860438161"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.1 "><p id="p889816412711"><a name="p889816412711"></a><a name="p889816412711"></a>Triggered At</p>
    </td>
    <td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.2 "><p id="p48991141972"><a name="p48991141972"></a><a name="p48991141972"></a>Specifies a time at which the AS policy is triggered.</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.3 "><p id="p642426221205"><a name="p642426221205"></a><a name="p642426221205"></a>N/A</p>
    </td>
    </tr>
    <tr id="row128601381261"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.1 "><p id="p9903343714"><a name="p9903343714"></a><a name="p9903343714"></a>Scaling Action</p>
    </td>
    <td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.2 "><p id="p59032121112324"><a name="p59032121112324"></a><a name="p59032121112324"></a>Specifies the action to be performed.</p>
    <div class="p" id="p61527048112324"><a name="p61527048112324"></a><a name="p61527048112324"></a>The following scaling action options are available:<a name="ul16872520112324"></a><a name="ul16872520112324"></a><ul id="ul16872520112324"><li>Add<p id="p1395431941115"><a name="p1395431941115"></a><a name="p1395431941115"></a>When a scaling action is triggered, the bandwidth is increased.</p>
    </li><li>Reduce<p id="p919514425116"><a name="p919514425116"></a><a name="p919514425116"></a>When a scaling action is triggered, the bandwidth is decreased.</p>
    </li><li>Set to<p id="p167684021219"><a name="p167684021219"></a><a name="p167684021219"></a>The bandwidth is set to a fixed value.</p>
    <div class="note" id="note1029375217579"><a name="note1029375217579"></a><a name="note1029375217579"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1729713525576"><a name="p1729713525576"></a><a name="p1729713525576"></a>The step (minimum unit for bandwidth adjustment) varies depending on the bandwidth value range. The bandwidth will be automatically adjusted to the nearest value according to the actual step.</p>
    <a name="ul12981052195716"></a><a name="ul12981052195716"></a><ul id="ul12981052195716"><li>If the bandwidth is less than or equal to 300 Mbit/s, the default step is 1 Mbit/s.</li><li>If the bandwidth ranges from 300 Mbit/s to 500 Mbit/s, the default step is 50 Mbit/s.</li></ul>
    </div></div>
    </li></ul>
    </div>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.3 "><p id="p163291612201212"><a name="p163291612201212"></a><a name="p163291612201212"></a>N/A</p>
    </td>
    </tr>
    <tr id="row1775512041719"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.1 "><p id="p16406131191717"><a name="p16406131191717"></a><a name="p16406131191717"></a>Limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.2 "><p id="p3408141191716"><a name="p3408141191716"></a><a name="p3408141191716"></a>Specifies the maximum and minimum bandwidth allowed.</p>
    <a name="ul940814112173"></a><a name="ul940814112173"></a><ul id="ul940814112173"><li>When <strong id="b16875134882211"><a name="b16875134882211"></a><a name="b16875134882211"></a>Scaling Action</strong> is set to <strong id="b1877134892218"><a name="b1877134892218"></a><a name="b1877134892218"></a>Add</strong>, this parameter specifies the maximum bandwidth allowed.</li><li>When <strong id="b1847202202315"><a name="b1847202202315"></a><a name="b1847202202315"></a>Scaling Action</strong> is set to <strong id="b5481927232"><a name="b5481927232"></a><a name="b5481927232"></a>Reduce</strong>, this parameter specifies the minimum bandwidth allowed.<div class="note" id="note9314174222"><a name="note9314174222"></a><a name="note9314174222"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p53361792219"><a name="p53361792219"></a><a name="p53361792219"></a>This parameter is unavailable if <strong id="b10607637238"><a name="b10607637238"></a><a name="b10607637238"></a>Scaling Action</strong> is <strong id="b13607163122311"><a name="b13607163122311"></a><a name="b13607163122311"></a>Set to</strong>.</p>
    </div></div>
    </li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.3 "><p id="p196137427234"><a name="p196137427234"></a><a name="p196137427234"></a>50 Mbit/s</p>
    </td>
    </tr>
    <tr id="row1786003818611"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.1 "><p id="p388576551205"><a name="p388576551205"></a><a name="p388576551205"></a>Cooldown Period</p>
    </td>
    <td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.2 "><p id="p21343661141258"><a name="p21343661141258"></a><a name="p21343661141258"></a>Specifies a period of time in the unit of second after each scaling action is complete. During the cooldown period, scaling actions triggered by alarms will be denied. Scheduled and periodic scaling actions are not restricted.</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.3 "><p id="p656113531205"><a name="p656113531205"></a><a name="p656113531205"></a>300</p>
    </td>
    </tr>
    </tbody>
    </table>

6.  After setting the parameters, click  **Create Now**.

