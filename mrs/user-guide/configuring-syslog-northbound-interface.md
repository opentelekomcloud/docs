# Configuring Syslog Northbound Interface<a name="EN-US_TOPIC_0125375440"></a>

## Scenario<a name="section16490974171050"></a>

You can configure the northbound interface so that alarms generated on MRS Manager can be reported to your monitoring O&M system using Syslog.

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>The Syslog protocol is not encrypted. Therefore, data can be easily stolen during transmission. This represents a significant security risk.  

## Prerequisites<a name="section5808627417134"></a>

-   The corresponding ECS of the interconnected server and the Master node of the MRS cluster are deployed on the same VPC.
-   The Master node can access the IP address and specific ports of the interconnected server.

## Procedure<a name="section58423188183440"></a>

1.  On MRS Manager, click  **System**.
2.  In  **Configuration**, click **Configure Syslog**  under **Monitoring and Alarm**.

    The switch of the  **Syslog Service**  is disabled by default. Click the switch to enable the Syslog service.

3.  On the displayed page, set Syslog parameters listed in  [Table 1](#table27202707183556):

    **Table  1**  Description of Syslog parameters

    <a name="table27202707183556"></a>
    <table><thead align="left"><tr id="row47060330183556"><th class="cellrowborder" valign="top" width="24.872487248724873%" id="mcps1.2.4.1.1"><p id="p14351306183556"><a name="p14351306183556"></a><a name="p14351306183556"></a><strong id="b4750022117163"><a name="b4750022117163"></a><a name="b4750022117163"></a>Area</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="41.7941794179418%" id="mcps1.2.4.1.2"><p id="p21605148183556"><a name="p21605148183556"></a><a name="p21605148183556"></a><strong id="b2231270717163"><a name="b2231270717163"></a><a name="b2231270717163"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p5186587183556"><a name="p5186587183556"></a><a name="p5186587183556"></a><strong id="b6249884917163"><a name="b6249884917163"></a><a name="b6249884917163"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row46679286183556"><td class="cellrowborder" rowspan="6" valign="top" width="24.872487248724873%" headers="mcps1.2.4.1.1 "><p id="p50057990183715"><a name="p50057990183715"></a><a name="p50057990183715"></a>Syslog Protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.7941794179418%" headers="mcps1.2.4.1.2 "><p id="p27288609171616"><a name="p27288609171616"></a><a name="p27288609171616"></a><span class="parmname" id="parmname30334101183953"><a name="parmname30334101183953"></a><a name="parmname30334101183953"></a><b>Server IP Address</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p62893743171616"><a name="p62893743171616"></a><a name="p62893743171616"></a>Specifies the IP address of the interconnected server.</p>
    </td>
    </tr>
    <tr id="row29064819183556"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p2861998594335"><a name="p2861998594335"></a><a name="p2861998594335"></a><span class="parmname" id="parmname4396602018401"><a name="parmname4396602018401"></a><a name="parmname4396602018401"></a><b>Server Port</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p8106911171616"><a name="p8106911171616"></a><a name="p8106911171616"></a>Specifies the port number for interconnection.</p>
    </td>
    </tr>
    <tr id="row49691024183556"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p7884211171623"><a name="p7884211171623"></a><a name="p7884211171623"></a><span class="parmname" id="parmname2705336118406"><a name="parmname2705336118406"></a><a name="parmname2705336118406"></a><b>Protocol</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p34641380171623"><a name="p34641380171623"></a><a name="p34641380171623"></a>Specifies the protocol type. Possible values are:</p>
    <a name="ul43336972171623"></a><a name="ul43336972171623"></a><ul id="ul43336972171623"><li><span class="parmvalue" id="parmvalue29139435153342"><a name="parmvalue29139435153342"></a><a name="parmvalue29139435153342"></a><b>TCP</b></span></li><li><span class="parmvalue" id="parmvalue35394249153344"><a name="parmvalue35394249153344"></a><a name="parmvalue35394249153344"></a><b>UDP</b></span></li></ul>
    </td>
    </tr>
    <tr id="row23540789183556"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p23694862171634"><a name="p23694862171634"></a><a name="p23694862171634"></a><span class="parmname" id="parmname19864330184013"><a name="parmname19864330184013"></a><a name="parmname19864330184013"></a><b>Severity</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p1852986618356"><a name="p1852986618356"></a><a name="p1852986618356"></a>Specifies the message severity. Possible values are:</p>
    <a name="ul52948469171644"></a><a name="ul52948469171644"></a><ul id="ul52948469171644"><li><span class="parmvalue" id="parmvalue56757637153346"><a name="parmvalue56757637153346"></a><a name="parmvalue56757637153346"></a><b>Informational</b></span></li><li><span class="parmvalue" id="parmvalue56740577153347"><a name="parmvalue56740577153347"></a><a name="parmvalue56740577153347"></a><b>Emergency</b></span></li><li><span class="parmvalue" id="parmvalue45090428153349"><a name="parmvalue45090428153349"></a><a name="parmvalue45090428153349"></a><b>Alert</b></span></li><li><span class="parmvalue" id="parmvalue302693153352"><a name="parmvalue302693153352"></a><a name="parmvalue302693153352"></a><b>Critical</b></span></li><li><span class="parmvalue" id="parmvalue23215426153359"><a name="parmvalue23215426153359"></a><a name="parmvalue23215426153359"></a><b>Error</b></span></li><li><span class="parmvalue" id="parmvalue4727945015341"><a name="parmvalue4727945015341"></a><a name="parmvalue4727945015341"></a><b>Warning</b></span></li><li><span class="parmvalue" id="parmvalue5878855515343"><a name="parmvalue5878855515343"></a><a name="parmvalue5878855515343"></a><b>Notice</b></span></li><li><span class="parmvalue" id="parmvalue1493165215345"><a name="parmvalue1493165215345"></a><a name="parmvalue1493165215345"></a><b>Debug</b></span></li></ul>
    </td>
    </tr>
    <tr id="row17804690183556"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p18796795183644"><a name="p18796795183644"></a><a name="p18796795183644"></a><span class="parmname" id="parmname4751106184042"><a name="parmname4751106184042"></a><a name="parmname4751106184042"></a><b>Facility</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p46145461183644"><a name="p46145461183644"></a><a name="p46145461183644"></a>Specifies the module where the log is generated.</p>
    </td>
    </tr>
    <tr id="row19573745183642"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1870209171656"><a name="p1870209171656"></a><a name="p1870209171656"></a><span class="parmname" id="parmname1087380184046"><a name="parmname1087380184046"></a><a name="parmname1087380184046"></a><b>Identifier</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p17269261171656"><a name="p17269261171656"></a><a name="p17269261171656"></a>Specifies the product. The default value is <strong id="b41280966182110"><a name="b41280966182110"></a><a name="b41280966182110"></a>MRS Manager</strong>.</p>
    </td>
    </tr>
    <tr id="row23164398183655"><td class="cellrowborder" rowspan="3" valign="top" width="24.872487248724873%" headers="mcps1.2.4.1.1 "><p id="p60367007183655"><a name="p60367007183655"></a><a name="p60367007183655"></a>Report Message</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.7941794179418%" headers="mcps1.2.4.1.2 "><p id="p2947273417177"><a name="p2947273417177"></a><a name="p2947273417177"></a><span class="parmname" id="parmname21026306184054"><a name="parmname21026306184054"></a><a name="parmname21026306184054"></a><b>Report Format</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p3848123417177"><a name="p3848123417177"></a><a name="p3848123417177"></a>Specifies the message format of alarms. For details about the format requirements, see the help information on the WebUI.</p>
    </td>
    </tr>
    <tr id="row24943443183655"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p131473117177"><a name="p131473117177"></a><a name="p131473117177"></a><span class="parmname" id="parmname2070225118412"><a name="parmname2070225118412"></a><a name="parmname2070225118412"></a><b>Report Alarm Type</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p3938439317177"><a name="p3938439317177"></a><a name="p3938439317177"></a>Specifies the type of alarms to be reported. Possible values are:</p>
    <a name="ul5247844153723"></a><a name="ul5247844153723"></a><ul id="ul5247844153723"><li><span class="parmvalue" id="parmvalue6554735416245"><a name="parmvalue6554735416245"></a><a name="parmvalue6554735416245"></a><b>Fault</b></span><p id="p1460411216247"><a name="p1460411216247"></a><a name="p1460411216247"></a>Syslog alarm information is reported if the Manager generates an alarm.</p>
    </li><li><span class="parmvalue" id="parmvalue3509694916613"><a name="parmvalue3509694916613"></a><a name="parmvalue3509694916613"></a><b>Clear</b></span><p id="p4655013016614"><a name="p4655013016614"></a><a name="p4655013016614"></a>Syslog alarm information is reported if the Manager clears an alarm.</p>
    </li><li><span class="parmvalue" id="parmvalue4090283416623"><a name="parmvalue4090283416623"></a><a name="parmvalue4090283416623"></a><b>Event</b></span><p id="p2058575516624"><a name="p2058575516624"></a><a name="p2058575516624"></a>Syslog alarm information is reported if the Manager generates an event.</p>
    </li></ul>
    </td>
    </tr>
    <tr id="row17684574183655"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p5573828817177"><a name="p5573828817177"></a><a name="p5573828817177"></a><span class="parmname" id="parmname1216896218419"><a name="parmname1216896218419"></a><a name="parmname1216896218419"></a><b>Report Alarm Severity</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p1850744217177"><a name="p1850744217177"></a><a name="p1850744217177"></a>Specifies the severity of alarms to be reported. Possible values are <span class="parmvalue" id="parmvalue49114409154012"><a name="parmvalue49114409154012"></a><a name="parmvalue49114409154012"></a><b>Warning</b></span>,&nbsp;<span class="parmvalue" id="parmvalue17977466154027"><a name="parmvalue17977466154027"></a><a name="parmvalue17977466154027"></a><b>Minor</b></span>,&nbsp;<span class="parmvalue" id="parmvalue30359747154039"><a name="parmvalue30359747154039"></a><a name="parmvalue30359747154039"></a><b>Major</b></span>, and&nbsp;<span class="parmvalue" id="parmvalue49871741154044"><a name="parmvalue49871741154044"></a><a name="parmvalue49871741154044"></a><b>Critical</b></span>.</p>
    </td>
    </tr>
    <tr id="row2785453918375"><td class="cellrowborder" rowspan="2" valign="top" width="24.872487248724873%" headers="mcps1.2.4.1.1 "><p id="p594299018375"><a name="p594299018375"></a><a name="p594299018375"></a>Uncleared Alarm Reporting</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.7941794179418%" headers="mcps1.2.4.1.2 "><p id="p11887742171722"><a name="p11887742171722"></a><a name="p11887742171722"></a><span class="parmname" id="parmname4463079184117"><a name="parmname4463079184117"></a><a name="parmname4463079184117"></a><b>Periodic Uncleared Alarm Reporting</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p18169756162439"><a name="p18169756162439"></a><a name="p18169756162439"></a>Specifies whether uncleared alarms are reported periodically.</p>
    <p id="p16283600162447"><a name="p16283600162447"></a><a name="p16283600162447"></a>The switch of the <span class="parmname" id="parmname23133484195613"><a name="parmname23133484195613"></a><a name="parmname23133484195613"></a><b>Periodic Uncleared Alarm Reporting</b></span> is disabled by default. Click the switch to enable the function.</p>
    </td>
    </tr>
    <tr id="row309494818375"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p9646743171722"><a name="p9646743171722"></a><a name="p9646743171722"></a><span class="parmname" id="parmname5637069184124"><a name="parmname5637069184124"></a><a name="parmname5637069184124"></a><b>Report Interval (min)</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p44865856162532"><a name="p44865856162532"></a><a name="p44865856162532"></a>Specifies the interval for periodical alarm report.</p>
    <p id="p43188737171722"><a name="p43188737171722"></a><a name="p43188737171722"></a>This parameter is available only when <span class="parmname" id="parmname3447147411353"><a name="parmname3447147411353"></a><a name="parmname3447147411353"></a><b>Periodic Uncleared Alarm Reporting</b></span> is enabled. The interval is measured in minutes and the default value is&nbsp;<strong id="b10532331171722"><a name="b10532331171722"></a><a name="b10532331171722"></a>15</strong>. The value range is&nbsp;<strong id="b27682122171722"><a name="b27682122171722"></a><a name="b27682122171722"></a>5</strong>&nbsp;to&nbsp;<strong id="b47812507171722"><a name="b47812507171722"></a><a name="b47812507171722"></a>1440</strong>.</p>
    </td>
    </tr>
    <tr id="row44235729103414"><td class="cellrowborder" rowspan="3" valign="top" width="24.872487248724873%" headers="mcps1.2.4.1.1 "><p id="p55101617103724"><a name="p55101617103724"></a><a name="p55101617103724"></a>Heartbeat Settings</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.7941794179418%" headers="mcps1.2.4.1.2 "><p id="p705851103719"><a name="p705851103719"></a><a name="p705851103719"></a><span class="parmname" id="parmname25682404103937"><a name="parmname25682404103937"></a><a name="parmname25682404103937"></a><b>Heartbeat Report</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p17323066103714"><a name="p17323066103714"></a><a name="p17323066103714"></a>Specifies whether periodical report of Syslog heartbeat messages is enabled.</p>
    <p id="p12049298103714"><a name="p12049298103714"></a><a name="p12049298103714"></a>The switch of the <span class="parmname" id="parmname568841352009"><a name="parmname568841352009"></a><a name="parmname568841352009"></a><b>Heartbeat Report</b></span> is disabled by default. Click the switch to enable the function.</p>
    </td>
    </tr>
    <tr id="row17014690103417"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p660720010376"><a name="p660720010376"></a><a name="p660720010376"></a><span class="parmname" id="parmname47618862103946"><a name="parmname47618862103946"></a><a name="parmname47618862103946"></a><b>Heartbeat Period (min)</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p26338196103654"><a name="p26338196103654"></a><a name="p26338196103654"></a>Specifies the interval for periodical heartbeat report. This parameter is available only when <span class="parmvalue" id="parmvalue21256327104215"><a name="parmvalue21256327104215"></a><a name="parmvalue21256327104215"></a><b>Heartbeat Report</b></span>&nbsp;is enabled. The unit of the interval is minute and the default value is&nbsp;<span class="parmvalue" id="parmvalue1904712410402"><a name="parmvalue1904712410402"></a><a name="parmvalue1904712410402"></a><b>15</b></span>. The value range is&nbsp;<span class="parmvalue" id="parmvalue395735410404"><a name="parmvalue395735410404"></a><a name="parmvalue395735410404"></a><b>1</b></span>&nbsp;to&nbsp;<span class="parmvalue" id="parmvalue4567060610408"><a name="parmvalue4567060610408"></a><a name="parmvalue4567060610408"></a><b>60</b></span>.</p>
    </td>
    </tr>
    <tr id="row8748200103421"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p62648414103644"><a name="p62648414103644"></a><a name="p62648414103644"></a><span class="parmname" id="parmname13185721103951"><a name="parmname13185721103951"></a><a name="parmname13185721103951"></a><b>Heartbeat Packet</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p63707038103635"><a name="p63707038103635"></a><a name="p63707038103635"></a>Specifies the heartbeat report content. This parameter is available only when <span class="parmname" id="parmname6224427610428"><a name="parmname6224427610428"></a><a name="parmname6224427610428"></a><b>Heartbeat Report</b></span> is enabled. The identifier cannot be empty. The value must contain a maximum of 256 characters. It can contain only numbers, letters, underscores (_), vertical bars (|), colons (:), commas (,), periods (.), and spaces.</p>
    </td>
    </tr>
    </tbody>
    </table>

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >When the heartbeat packets are reported periodically, reporting packets may be interrupted in scenarios \(active/standby management node switchover\) where some clusters are automatically restored from faults. Wait until the restoration is complete.  

4.  Click  **OK**  to complete the settings.

