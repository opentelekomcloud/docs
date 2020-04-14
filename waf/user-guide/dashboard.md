# Dashboard<a name="EN-US_TOPIC_0193630186"></a>

This section describes how to  view event logs  in a specified time \(for example, today\), including attack and request statistics, the number of attacks from the top 5 source IP addresses, and event distribution.

## Prerequisites<a name="section2256777914731"></a>

Login credentials have been obtained.

## Procedure<a name="section61533550183130"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner of the management console and select a region or project.
3.  Choose  **Security**  \>  **Web Application Firewall**. The  **Dashboard**  page is displayed.
4.  In the domain name drop-down list, select a domain name to view its event logs. The query time can be  **Yesterday**,  **Today**,  **Past 3 days**,  **Past 7 days**, and  **Past 30 days**  \(see  [Figure 1](#fig5451829111656)\).

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >You can select  **All domain names**  or a specific domain name from the drop-down list.  

    **Figure  1**  Viewing event logs<a name="fig5451829111656"></a>  
    ![](figures/viewing-event-logs.png "viewing-event-logs")

    **Table  1**  Parameter description of event logs

    <a name="table2857356711453"></a>
    <table><thead align="left"><tr id="row2386908311453"><th class="cellrowborder" valign="top" width="25.81258125812581%" id="mcps1.2.4.1.1"><p id="p1936630111453"><a name="p1936630111453"></a><a name="p1936630111453"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="38.033803380338036%" id="mcps1.2.4.1.2"><p id="p2516658611453"><a name="p2516658611453"></a><a name="p2516658611453"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="36.153615361536154%" id="mcps1.2.4.1.3"><p id="p21644893114937"><a name="p21644893114937"></a><a name="p21644893114937"></a>Remarks</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2572158511453"><td class="cellrowborder" valign="top" width="25.81258125812581%" headers="mcps1.2.4.1.1 "><p id="p46185398114652"><a name="p46185398114652"></a><a name="p46185398114652"></a>Requests</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.033803380338036%" headers="mcps1.2.4.1.2 "><p id="p50029725114652"><a name="p50029725114652"></a><a name="p50029725114652"></a>Total number of requests to the specified domain name</p>
    <p id="p47614347114652"><a name="p47614347114652"></a><a name="p47614347114652"></a>If <strong id="b1640172581218"><a name="b1640172581218"></a><a name="b1640172581218"></a>All domain names</strong> is selected, the total number of requests to all domain names is displayed.</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.153615361536154%" headers="mcps1.2.4.1.3 "><p id="p3345389611453"><a name="p3345389611453"></a><a name="p3345389611453"></a>N/A</p>
    </td>
    </tr>
    <tr id="row3264961511453"><td class="cellrowborder" valign="top" width="25.81258125812581%" headers="mcps1.2.4.1.1 "><p id="p53764047114652"><a name="p53764047114652"></a><a name="p53764047114652"></a>Peak Value</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.033803380338036%" headers="mcps1.2.4.1.2 "><p id="p59920569114652"><a name="p59920569114652"></a><a name="p59920569114652"></a>Maximum number of requests to the specified domain name per second</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.153615361536154%" headers="mcps1.2.4.1.3 "><p id="p1218804711453"><a name="p1218804711453"></a><a name="p1218804711453"></a>N/A</p>
    </td>
    </tr>
    <tr id="row4258356411453"><td class="cellrowborder" valign="top" width="25.81258125812581%" headers="mcps1.2.4.1.1 "><p id="p61333475114652"><a name="p61333475114652"></a><a name="p61333475114652"></a>Attacks</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.033803380338036%" headers="mcps1.2.4.1.2 "><p id="p1955603114652"><a name="p1955603114652"></a><a name="p1955603114652"></a>Number of attacks on the specified domain name</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.153615361536154%" headers="mcps1.2.4.1.3 "><p id="p6676667411453"><a name="p6676667411453"></a><a name="p6676667411453"></a>N/A</p>
    </td>
    </tr>
    <tr id="row6402915811453"><td class="cellrowborder" valign="top" width="25.81258125812581%" headers="mcps1.2.4.1.1 "><p id="p16348957114652"><a name="p16348957114652"></a><a name="p16348957114652"></a>Attack Sources</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.033803380338036%" headers="mcps1.2.4.1.2 "><p id="p49197101114652"><a name="p49197101114652"></a><a name="p49197101114652"></a>Number of sources that attack the specified domain name</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.153615361536154%" headers="mcps1.2.4.1.3 "><p id="p3617334411453"><a name="p3617334411453"></a><a name="p3617334411453"></a>N/A</p>
    </td>
    </tr>
    <tr id="row5712464411453"><td class="cellrowborder" valign="top" width="25.81258125812581%" headers="mcps1.2.4.1.1 "><p id="p6369341911453"><a name="p6369341911453"></a><a name="p6369341911453"></a>Attacks</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.033803380338036%" headers="mcps1.2.4.1.2 "><p id="p5889333511453"><a name="p5889333511453"></a><a name="p5889333511453"></a>Trend of attacks</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.153615361536154%" headers="mcps1.2.4.1.3 "><p id="p563086411453"><a name="p563086411453"></a><a name="p563086411453"></a>The trend of attacks is displayed by default.</p>
    </td>
    </tr>
    <tr id="row5067778111453"><td class="cellrowborder" valign="top" width="25.81258125812581%" headers="mcps1.2.4.1.1 "><p id="p1125956311453"><a name="p1125956311453"></a><a name="p1125956311453"></a>Requests</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.033803380338036%" headers="mcps1.2.4.1.2 "><p id="p3960941011453"><a name="p3960941011453"></a><a name="p3960941011453"></a>Trend of requests</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.153615361536154%" headers="mcps1.2.4.1.3 "><p id="p5424563311453"><a name="p5424563311453"></a><a name="p5424563311453"></a>Click <strong id="b190251171112"><a name="b190251171112"></a><a name="b190251171112"></a>Requests</strong> to view the trend of requests.</p>
    </td>
    </tr>
    <tr id="row1844865611453"><td class="cellrowborder" valign="top" width="25.81258125812581%" headers="mcps1.2.4.1.1 "><p id="p1794614311453"><a name="p1794614311453"></a><a name="p1794614311453"></a>Event Distribution</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.033803380338036%" headers="mcps1.2.4.1.2 "><p id="p4435146711453"><a name="p4435146711453"></a><a name="p4435146711453"></a>Types of attack events</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.153615361536154%" headers="mcps1.2.4.1.3 "><a name="ul5009385314278"></a><a name="ul5009385314278"></a><ul id="ul5009385314278"><li>Click any colored area in the event distribution circle under <strong id="b842352706113520"><a name="b842352706113520"></a><a name="b842352706113520"></a>Event Distribution</strong> to view the type, number, and proportion of an attack.</li><li>To stop displaying information about a specific type of event, click the corresponding legend with the same color to the right of the circle.</li></ul>
    </td>
    </tr>
    <tr id="row53276882114737"><td class="cellrowborder" valign="top" width="25.81258125812581%" headers="mcps1.2.4.1.1 "><p id="p20460182114737"><a name="p20460182114737"></a><a name="p20460182114737"></a>Top 5 Source IP Addresses (Attacks)</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.033803380338036%" headers="mcps1.2.4.1.2 "><p id="p46662075114737"><a name="p46662075114737"></a><a name="p46662075114737"></a>Top 5 attack source IP addresses and their cumulative number of attacks</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.153615361536154%" headers="mcps1.2.4.1.3 "><p id="p21531753114737"><a name="p21531753114737"></a><a name="p21531753114737"></a>N/A</p>
    </td>
    </tr>
    </tbody>
    </table>


