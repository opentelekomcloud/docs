# Modifying an Alarm Rule<a name="EN-US_TOPIC_0084572315"></a>

## Procedure<a name="section61671706161623"></a>

1.  Log in to the management console.
2.  In the upper left corner, select a region and a project.
3.  Under  **Management & Deployment**, select  **Cloud Eye**.
4.  Choose  **Alarm Management**  \>  **Alarm Rules**.
5.  You can choose either of the following two methods to access the page for modifying alarm rules:
    -   On the  **Alarm Rules**  page, locate the row containing the target alarm rule, click  **More**  in the  **Operation**  column, and click  **Modify**.
    -   On the  **Alarm Rules**  page, click the name of the target alarm rule. On the displayed page, click  **Modify**  in the upper right corner.

6.  In the  **Modify Alarm Rule**  dialog box, modify parameters of the alarm rule.

    **Table  1**  Parameters

    <a name="table17926101914192"></a>
    <table><thead align="left"><tr id="row1092718193198"><th class="cellrowborder" valign="top" width="26.63%" id="mcps1.2.4.1.1"><p id="p109272193193"><a name="p109272193193"></a><a name="p109272193193"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="54.25%" id="mcps1.2.4.1.2"><p id="p1992731921913"><a name="p1992731921913"></a><a name="p1992731921913"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.12%" id="mcps1.2.4.1.3"><p id="p149271019141912"><a name="p149271019141912"></a><a name="p149271019141912"></a>Example Value</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row149301019131919"><td class="cellrowborder" valign="top" width="26.63%" headers="mcps1.2.4.1.1 "><p id="p8930171913191"><a name="p8930171913191"></a><a name="p8930171913191"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.25%" headers="mcps1.2.4.1.2 "><p id="p993013197198"><a name="p993013197198"></a><a name="p993013197198"></a>Specifies the alarm rule name. The system generates a name randomly but you can change it.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.12%" headers="mcps1.2.4.1.3 "><p id="p4930171915194"><a name="p4930171915194"></a><a name="p4930171915194"></a>alarm-b6al</p>
    </td>
    </tr>
    <tr id="row793119191192"><td class="cellrowborder" valign="top" width="26.63%" headers="mcps1.2.4.1.1 "><p id="p29318192193"><a name="p29318192193"></a><a name="p29318192193"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.25%" headers="mcps1.2.4.1.2 "><p id="p5931201911913"><a name="p5931201911913"></a><a name="p5931201911913"></a>(Optional) Provides supplementary information about the alarm rule.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.12%" headers="mcps1.2.4.1.3 "><p id="p0931319151917"><a name="p0931319151917"></a><a name="p0931319151917"></a>N/A</p>
    </td>
    </tr>
    <tr id="row1693181917195"><td class="cellrowborder" valign="top" width="26.63%" headers="mcps1.2.4.1.1 "><p id="p2093251915194"><a name="p2093251915194"></a><a name="p2093251915194"></a>Resource Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.25%" headers="mcps1.2.4.1.2 "><p id="p4932319181920"><a name="p4932319181920"></a><a name="p4932319181920"></a>Specifies the name of the service for which the alarm rule is configured.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.12%" headers="mcps1.2.4.1.3 "><p id="p39323195195"><a name="p39323195195"></a><a name="p39323195195"></a>Elastic Cloud Server</p>
    </td>
    </tr>
    <tr id="row593217197195"><td class="cellrowborder" valign="top" width="26.63%" headers="mcps1.2.4.1.1 "><p id="p29320199190"><a name="p29320199190"></a><a name="p29320199190"></a>Dimension</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.25%" headers="mcps1.2.4.1.2 "><p id="p593391911193"><a name="p593391911193"></a><a name="p593391911193"></a>Specifies the metric dimension of the alarm rule.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.12%" headers="mcps1.2.4.1.3 "><p id="p1593321915198"><a name="p1593321915198"></a><a name="p1593321915198"></a>ECSs</p>
    </td>
    </tr>
    <tr id="row19331519151919"><td class="cellrowborder" valign="top" width="26.63%" headers="mcps1.2.4.1.1 "><p id="p1893381911919"><a name="p1893381911919"></a><a name="p1893381911919"></a>Monitored Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.25%" headers="mcps1.2.4.1.2 "><p id="p2933201991911"><a name="p2933201991911"></a><a name="p2933201991911"></a>Specifies the resource for which the alarm rule is set. You can specify one or more resources.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.12%" headers="mcps1.2.4.1.3 "><p id="p4933191916199"><a name="p4933191916199"></a><a name="p4933191916199"></a>N/A</p>
    </td>
    </tr>
    <tr id="row99346193192"><td class="cellrowborder" valign="top" width="26.63%" headers="mcps1.2.4.1.1 "><p id="p5934519151919"><a name="p5934519151919"></a><a name="p5934519151919"></a>Monitored Object ID</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.25%" headers="mcps1.2.4.1.2 "><p id="p793421921917"><a name="p793421921917"></a><a name="p793421921917"></a>Specifies the resource ID.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.12%" headers="mcps1.2.4.1.3 "><p id="p18934919181914"><a name="p18934919181914"></a><a name="p18934919181914"></a>N/A</p>
    </td>
    </tr>
    <tr id="row179341319111912"><td class="cellrowborder" valign="top" width="26.63%" headers="mcps1.2.4.1.1 "><p id="p139354196196"><a name="p139354196196"></a><a name="p139354196196"></a>Metric</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.25%" headers="mcps1.2.4.1.2 "><p id="p8935121981918"><a name="p8935121981918"></a><a name="p8935121981918"></a>For example:</p>
    <a name="ul10935191920199"></a><a name="ul10935191920199"></a><ul id="ul10935191920199"><li>CPU Usage<p id="p17935111921915"><a name="p17935111921915"></a><a name="p17935111921915"></a>Indicates the CPU usage of the monitored object. The unit is percent.</p>
    </li></ul>
    <a name="ul16936121915198"></a><a name="ul16936121915198"></a><ul id="ul16936121915198"><li>Memory Usage<p id="p0937161913197"><a name="p0937161913197"></a><a name="p0937161913197"></a>Indicates the percentage of memory currently in use. The unit is percent.</p>
    </li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="19.12%" headers="mcps1.2.4.1.3 "><p id="p1693711911916"><a name="p1693711911916"></a><a name="p1693711911916"></a>N/A</p>
    </td>
    </tr>
    <tr id="row146141650115516"><td class="cellrowborder" valign="top" width="26.63%" headers="mcps1.2.4.1.1 "><p id="p19919125115513"><a name="p19919125115513"></a><a name="p19919125115513"></a>Alarm Policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.25%" headers="mcps1.2.4.1.2 "><p id="p1922251175510"><a name="p1922251175510"></a><a name="p1922251175510"></a>Specifies the policy that triggers an alarm.</p>
    <p id="p1692365111550"><a name="p1692365111550"></a><a name="p1692365111550"></a>For example, an alarm is triggered if the metric average data is 80% or more for three consecutive periods of 5 minutes.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.12%" headers="mcps1.2.4.1.3 "><p id="p492725155515"><a name="p492725155515"></a><a name="p492725155515"></a>N/A</p>
    </td>
    </tr>
    <tr id="row388575114916"><td class="cellrowborder" valign="top" width="26.63%" headers="mcps1.2.4.1.1 "><p id="p175502053154914"><a name="p175502053154914"></a><a name="p175502053154914"></a>Alarm Severity</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.25%" headers="mcps1.2.4.1.2 "><p id="p14553105374912"><a name="p14553105374912"></a><a name="p14553105374912"></a>Specifies the severity of the alarm. Valid values are <strong id="b842352706112510"><a name="b842352706112510"></a><a name="b842352706112510"></a>Critical</strong>, <strong id="b842352706112514"><a name="b842352706112514"></a><a name="b842352706112514"></a>Major</strong>, <strong id="b842352706112520"><a name="b842352706112520"></a><a name="b842352706112520"></a>Minor,</strong> and <strong id="b842352706112523"><a name="b842352706112523"></a><a name="b842352706112523"></a>Informational</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.12%" headers="mcps1.2.4.1.3 "><p id="p14555353134912"><a name="p14555353134912"></a><a name="p14555353134912"></a>Major</p>
    </td>
    </tr>
    <tr id="row19939141916195"><td class="cellrowborder" valign="top" width="26.63%" headers="mcps1.2.4.1.1 "><p id="p119391619141910"><a name="p119391619141910"></a><a name="p119391619141910"></a>Alarm Notification</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.25%" headers="mcps1.2.4.1.2 "><p id="p189391419101919"><a name="p189391419101919"></a><a name="p189391419101919"></a>Specifies whether to notify users when alarms are triggered. Notifications can be sent by emails or text messages, or HTTP/HTTPS requests sent to the servers.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.12%" headers="mcps1.2.4.1.3 "><p id="p12939111921911"><a name="p12939111921911"></a><a name="p12939111921911"></a>N/A</p>
    </td>
    </tr>
    </tbody>
    </table>


1.  Click  **OK**.

