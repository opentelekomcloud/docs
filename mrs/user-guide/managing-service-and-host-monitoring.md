# Managing Service and Host Monitoring<a name="EN-US_TOPIC_0125375755"></a>

## Scenario<a name="section22723273145845"></a>

On MRS Manager, you can manage status and indicator information for all services \(including role instances\) and hosts.

-   Status information, including operation, health, configuration, and role instance status.
-   Information about key monitoring indicators of services.
-   Monitoring indicator exports.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>You can set an interval for automatic page refreshing or click  ![](figures/icon_mrs_fresh_r.png)  to refresh the page immediately.  
>The following parameters are supported:  
>-   **Refresh every 30 seconds**: refreshes the page once every 30 seconds.  
>-   **Refresh every 60 seconds**: refreshes the page once every 60 seconds.  
>-   **Stop refreshing**: stops page refreshing.  

## Managing Service Monitoring<a name="section49755960145853"></a>

1.  On MRS Manager, click  **Service**  to view the status of all services.

    The service list includes  **Service**, **Operating Status**, **Health Status**, **Configuration Status**, **Roles**, and **Operation**.

    -   [Table 1](#table4224219143943)  describes service operating status.

        **Table  1**  Service operating status

        <a name="table4224219143943"></a>
        <table><thead align="left"><tr id="row697972615211"><th class="cellrowborder" valign="top" width="30.080000000000002%" id="mcps1.2.3.1.1"><p id="p3820727315211"><a name="p3820727315211"></a><a name="p3820727315211"></a><strong id="b3612894015247"><a name="b3612894015247"></a><a name="b3612894015247"></a>Status</strong></p>
        </th>
        <th class="cellrowborder" valign="top" width="69.92%" id="mcps1.2.3.1.2"><p id="p778137015211"><a name="p778137015211"></a><a name="p778137015211"></a><strong id="b4076304015247"><a name="b4076304015247"></a><a name="b4076304015247"></a>Description</strong></p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row5297130815211"><td class="cellrowborder" valign="top" width="30.080000000000002%" headers="mcps1.2.3.1.1 "><p id="p5083471015211"><a name="p5083471015211"></a><a name="p5083471015211"></a><span class="parmvalue" id="parmvalue2106357120376"><a name="parmvalue2106357120376"></a><a name="parmvalue2106357120376"></a><b>Started</b></span></p>
        </td>
        <td class="cellrowborder" valign="top" width="69.92%" headers="mcps1.2.3.1.2 "><p id="p2397086515211"><a name="p2397086515211"></a><a name="p2397086515211"></a>Indicates that the service is started.</p>
        </td>
        </tr>
        <tr id="row5808148415211"><td class="cellrowborder" valign="top" width="30.080000000000002%" headers="mcps1.2.3.1.1 "><p id="p2645641315211"><a name="p2645641315211"></a><a name="p2645641315211"></a><span class="parmvalue" id="parmvalue1748621420378"><a name="parmvalue1748621420378"></a><a name="parmvalue1748621420378"></a><b>Stopped</b></span></p>
        </td>
        <td class="cellrowborder" valign="top" width="69.92%" headers="mcps1.2.3.1.2 "><p id="p6259470415211"><a name="p6259470415211"></a><a name="p6259470415211"></a>Indicates that the service is stopped.</p>
        </td>
        </tr>
        <tr id="row5119274015211"><td class="cellrowborder" valign="top" width="30.080000000000002%" headers="mcps1.2.3.1.1 "><p id="p6462099415211"><a name="p6462099415211"></a><a name="p6462099415211"></a><span class="parmvalue" id="parmvalue13790927203710"><a name="parmvalue13790927203710"></a><a name="parmvalue13790927203710"></a><b>Failed to start</b></span></p>
        </td>
        <td class="cellrowborder" valign="top" width="69.92%" headers="mcps1.2.3.1.2 "><p id="p6691800715211"><a name="p6691800715211"></a><a name="p6691800715211"></a>Indicates that the service fails to be started.</p>
        </td>
        </tr>
        <tr id="row6534040515211"><td class="cellrowborder" valign="top" width="30.080000000000002%" headers="mcps1.2.3.1.1 "><p id="p6219233015211"><a name="p6219233015211"></a><a name="p6219233015211"></a><span class="parmvalue" id="parmvalue3756259203712"><a name="parmvalue3756259203712"></a><a name="parmvalue3756259203712"></a><b>Failed to stop</b></span></p>
        </td>
        <td class="cellrowborder" valign="top" width="69.92%" headers="mcps1.2.3.1.2 "><p id="p441394715211"><a name="p441394715211"></a><a name="p441394715211"></a>Indicates that the service fails to be stopped.</p>
        </td>
        </tr>
        <tr id="row2217312515211"><td class="cellrowborder" valign="top" width="30.080000000000002%" headers="mcps1.2.3.1.1 "><p id="p6365139415211"><a name="p6365139415211"></a><a name="p6365139415211"></a><span class="parmvalue" id="parmvalue36016589203723"><a name="parmvalue36016589203723"></a><a name="parmvalue36016589203723"></a><b>Unknown</b></span></p>
        </td>
        <td class="cellrowborder" valign="top" width="69.92%" headers="mcps1.2.3.1.2 "><p id="p5548927415211"><a name="p5548927415211"></a><a name="p5548927415211"></a>Indicates the initial service status after the background system restarts.</p>
        </td>
        </tr>
        </tbody>
        </table>

    -   [Table 2](#table43931038143943)  describes service health status.

        **Table  2**  Service health status

        <a name="table43931038143943"></a>
        <table><thead align="left"><tr id="row796832715326"><th class="cellrowborder" valign="top" width="30.080000000000002%" id="mcps1.2.3.1.1"><p id="p4176970815326"><a name="p4176970815326"></a><a name="p4176970815326"></a><strong id="b1241478815343"><a name="b1241478815343"></a><a name="b1241478815343"></a>Status</strong></p>
        </th>
        <th class="cellrowborder" valign="top" width="69.92%" id="mcps1.2.3.1.2"><p id="p2790314815326"><a name="p2790314815326"></a><a name="p2790314815326"></a><strong id="b6607377615343"><a name="b6607377615343"></a><a name="b6607377615343"></a>Description</strong></p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row88536915326"><td class="cellrowborder" valign="top" width="30.080000000000002%" headers="mcps1.2.3.1.1 "><p id="p6668293715326"><a name="p6668293715326"></a><a name="p6668293715326"></a><span class="parmvalue" id="parmvalue2938017720393"><a name="parmvalue2938017720393"></a><a name="parmvalue2938017720393"></a><b>Good</b></span></p>
        </td>
        <td class="cellrowborder" valign="top" width="69.92%" headers="mcps1.2.3.1.2 "><p id="p3260885515326"><a name="p3260885515326"></a><a name="p3260885515326"></a>Indicates that all role instances in the service are running properly.</p>
        </td>
        </tr>
        <tr id="row1501145515326"><td class="cellrowborder" valign="top" width="30.080000000000002%" headers="mcps1.2.3.1.1 "><p id="p1531789615326"><a name="p1531789615326"></a><a name="p1531789615326"></a><span class="parmvalue" id="parmvalue1885109020395"><a name="parmvalue1885109020395"></a><a name="parmvalue1885109020395"></a><b>Bad</b></span></p>
        </td>
        <td class="cellrowborder" valign="top" width="69.92%" headers="mcps1.2.3.1.2 "><p id="p3279002715326"><a name="p3279002715326"></a><a name="p3279002715326"></a>Indicates that at least one role instance in the service is in the <span class="parmvalue" id="parmvalue7947061203926"><a name="parmvalue7947061203926"></a><a name="parmvalue7947061203926"></a><b>Bad</b></span> state or that the dependent service is abnormal.</p>
        </td>
        </tr>
        <tr id="row6132026315326"><td class="cellrowborder" valign="top" width="30.080000000000002%" headers="mcps1.2.3.1.1 "><p id="p5146429315326"><a name="p5146429315326"></a><a name="p5146429315326"></a><span class="parmvalue" id="parmvalue6195229520397"><a name="parmvalue6195229520397"></a><a name="parmvalue6195229520397"></a><b>Unknown</b></span></p>
        </td>
        <td class="cellrowborder" valign="top" width="69.92%" headers="mcps1.2.3.1.2 "><p id="p785818615326"><a name="p785818615326"></a><a name="p785818615326"></a>Indicates that all role instances in the service are in the <span class="parmvalue" id="parmvalue62393672203930"><a name="parmvalue62393672203930"></a><a name="parmvalue62393672203930"></a><b>Unknown</b></span> state.</p>
        </td>
        </tr>
        <tr id="row2918298315326"><td class="cellrowborder" valign="top" width="30.080000000000002%" headers="mcps1.2.3.1.1 "><p id="p1795521415326"><a name="p1795521415326"></a><a name="p1795521415326"></a><span class="parmvalue" id="parmvalue3545414620399"><a name="parmvalue3545414620399"></a><a name="parmvalue3545414620399"></a><b>Concerning</b></span></p>
        </td>
        <td class="cellrowborder" valign="top" width="69.92%" headers="mcps1.2.3.1.2 "><p id="p4508626915326"><a name="p4508626915326"></a><a name="p4508626915326"></a>Indicates that the background system is restarting the service.</p>
        </td>
        </tr>
        <tr id="row5543833615326"><td class="cellrowborder" valign="top" width="30.080000000000002%" headers="mcps1.2.3.1.1 "><p id="p5165625515326"><a name="p5165625515326"></a><a name="p5165625515326"></a><span class="parmvalue" id="parmvalue36215049203922"><a name="parmvalue36215049203922"></a><a name="parmvalue36215049203922"></a><b>Partially Healthy</b></span></p>
        </td>
        <td class="cellrowborder" valign="top" width="69.92%" headers="mcps1.2.3.1.2 "><p id="p2340714215326"><a name="p2340714215326"></a><a name="p2340714215326"></a>Indicates that the service that this service depends on is abnormal and the interfaces of the abnormal service cannot be invoked externally.</p>
        </td>
        </tr>
        </tbody>
        </table>

    -   [Table 3](#table16122213143943)  describes service configuration status.

        **Table  3**  Service configuration status

        <a name="table16122213143943"></a>
        <table><thead align="left"><tr id="row605808311544"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.3.1.1"><p id="p621440581544"><a name="p621440581544"></a><a name="p621440581544"></a><strong id="b5490965315429"><a name="b5490965315429"></a><a name="b5490965315429"></a>Status</strong></p>
        </th>
        <th class="cellrowborder" valign="top" width="70%" id="mcps1.2.3.1.2"><p id="p5039181544"><a name="p5039181544"></a><a name="p5039181544"></a><strong id="b1849688815429"><a name="b1849688815429"></a><a name="b1849688815429"></a>Description</strong></p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row67312031544"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p178743401544"><a name="p178743401544"></a><a name="p178743401544"></a><span class="parmvalue" id="parmvalue43845399203935"><a name="parmvalue43845399203935"></a><a name="parmvalue43845399203935"></a><b>Synchronized</b></span></p>
        </td>
        <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p385354131544"><a name="p385354131544"></a><a name="p385354131544"></a>Indicates that the latest configuration has taken effect.</p>
        </td>
        </tr>
        <tr id="row305740731544"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p408115641544"><a name="p408115641544"></a><a name="p408115641544"></a><span class="parmvalue" id="parmvalue52424420203937"><a name="parmvalue52424420203937"></a><a name="parmvalue52424420203937"></a><b>Expired</b></span></p>
        </td>
        <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p174023721544"><a name="p174023721544"></a><a name="p174023721544"></a>Indicates that the latest configuration has not taken effect after the parameter modification. You need to restart the related services.</p>
        </td>
        </tr>
        <tr id="row183102001544"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p27540411544"><a name="p27540411544"></a><a name="p27540411544"></a><span class="parmvalue" id="parmvalue42478584203948"><a name="parmvalue42478584203948"></a><a name="parmvalue42478584203948"></a><b>Failed</b></span></p>
        </td>
        <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p217507691544"><a name="p217507691544"></a><a name="p217507691544"></a>Indicates that communication is abnormal or data cannot be read or written during the parameter configuration. Try clicking <span class="parmname" id="parmname22856104174523"><a name="parmname22856104174523"></a><a name="parmname22856104174523"></a><b>Synchronize Configuration</b></span> to recover the previous configuration.</p>
        </td>
        </tr>
        <tr id="row94910071544"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p333548631544"><a name="p333548631544"></a><a name="p333548631544"></a><span class="parmvalue" id="parmvalue35085905203950"><a name="parmvalue35085905203950"></a><a name="parmvalue35085905203950"></a><b>Configuring</b></span></p>
        </td>
        <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p173893811544"><a name="p173893811544"></a><a name="p173893811544"></a>Indicates that the parameter is being configured.</p>
        </td>
        </tr>
        <tr id="row159676371544"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p603924091544"><a name="p603924091544"></a><a name="p603924091544"></a><span class="parmvalue" id="parmvalue45489335203952"><a name="parmvalue45489335203952"></a><a name="parmvalue45489335203952"></a><b>Unknown</b></span></p>
        </td>
        <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p599469651544"><a name="p599469651544"></a><a name="p599469651544"></a>Indicates that current configuration status cannot be obtained.</p>
        </td>
        </tr>
        </tbody>
        </table>

    By default, services are displayed in ascending order by  **Service** You can click **Service**, **Operating Status**, **Health Status**, or **Configuration Status**  to change the display mode.

2.  Click the target service in the service list to view its status and indicator information.
3.  Customize monitoring indicators and export customized monitoring information.

    For MRS 1.9.2 or later:

    1.  In the  **Charts**  area, click  **Customize**  to customize service monitoring metrics.
    2.  In  **Period**, select a time of period and click  **View**  to view the monitoring data within the time period.
    3.  Click  **Export**  to export the displayed metric information.

    For versions earlier than MRS 1.9.2:

    1.  In the  **Real-Time Monitoring**  area, click **Customize**  to customize key monitoring indicators.
    2.  Click  **History**  to display the page in which you can query historical monitoring information.
    3.  Select a time period, and click  **View**  to display the monitoring data in the specified time period.
    4.  Click  **Export**  to export the displayed indicator information.


## Managing Role Instance Monitoring<a name="section1458767914594"></a>

1.  On MRS Manager, click  **Service**, and click the target service in the service list.
2.  Click  **Instance**  to view the role instance status.

    The role instance list includes  **Role**, **Host Name**, **OM IP Address**, **Business IP Address**, **Rack**, **Operating Status**, **Health Status** and **Configuration Status**.

    -   [Table 4](#table63916714202542)  describes role instance operating status.

        **Table  4**  Role instance operating status

        <a name="table63916714202542"></a>
        <table><thead align="left"><tr id="row5859968202542"><th class="cellrowborder" valign="top" width="30.080000000000002%" id="mcps1.2.3.1.1"><p id="p4895379202542"><a name="p4895379202542"></a><a name="p4895379202542"></a><strong id="b44058412202542"><a name="b44058412202542"></a><a name="b44058412202542"></a>Status</strong></p>
        </th>
        <th class="cellrowborder" valign="top" width="69.92%" id="mcps1.2.3.1.2"><p id="p11961602202542"><a name="p11961602202542"></a><a name="p11961602202542"></a><strong id="b40545562202542"><a name="b40545562202542"></a><a name="b40545562202542"></a>Description</strong></p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row62965086202542"><td class="cellrowborder" valign="top" width="30.080000000000002%" headers="mcps1.2.3.1.1 "><p id="p67007235202542"><a name="p67007235202542"></a><a name="p67007235202542"></a><span class="parmvalue" id="parmvalue62199345204055"><a name="parmvalue62199345204055"></a><a name="parmvalue62199345204055"></a><b>Started</b></span></p>
        </td>
        <td class="cellrowborder" valign="top" width="69.92%" headers="mcps1.2.3.1.2 "><p id="p58876977202542"><a name="p58876977202542"></a><a name="p58876977202542"></a>Indicates that the role instance is started.</p>
        </td>
        </tr>
        <tr id="row60130746202542"><td class="cellrowborder" valign="top" width="30.080000000000002%" headers="mcps1.2.3.1.1 "><p id="p38752263202542"><a name="p38752263202542"></a><a name="p38752263202542"></a><span class="parmvalue" id="parmvalue26740973204057"><a name="parmvalue26740973204057"></a><a name="parmvalue26740973204057"></a><b>Stopped</b></span></p>
        </td>
        <td class="cellrowborder" valign="top" width="69.92%" headers="mcps1.2.3.1.2 "><p id="p51925617202542"><a name="p51925617202542"></a><a name="p51925617202542"></a>Indicates that the role instance is stopped.</p>
        </td>
        </tr>
        <tr id="row64677372202542"><td class="cellrowborder" valign="top" width="30.080000000000002%" headers="mcps1.2.3.1.1 "><p id="p4375771202542"><a name="p4375771202542"></a><a name="p4375771202542"></a><span class="parmvalue" id="parmvalue39213623204058"><a name="parmvalue39213623204058"></a><a name="parmvalue39213623204058"></a><b>Failed to start</b></span></p>
        </td>
        <td class="cellrowborder" valign="top" width="69.92%" headers="mcps1.2.3.1.2 "><p id="p18893195202542"><a name="p18893195202542"></a><a name="p18893195202542"></a>Indicates that the role instance fails to be started.</p>
        </td>
        </tr>
        <tr id="row53953844202542"><td class="cellrowborder" valign="top" width="30.080000000000002%" headers="mcps1.2.3.1.1 "><p id="p8185213202542"><a name="p8185213202542"></a><a name="p8185213202542"></a><span class="parmvalue" id="parmvalue109447120411"><a name="parmvalue109447120411"></a><a name="parmvalue109447120411"></a><b>Failed to stop</b></span></p>
        </td>
        <td class="cellrowborder" valign="top" width="69.92%" headers="mcps1.2.3.1.2 "><p id="p59022478202542"><a name="p59022478202542"></a><a name="p59022478202542"></a>Indicates that the role instance fails to be stopped.</p>
        </td>
        </tr>
        <tr id="row665404321754"><td class="cellrowborder" valign="top" width="30.080000000000002%" headers="mcps1.2.3.1.1 "><p id="p210659241754"><a name="p210659241754"></a><a name="p210659241754"></a><span class="parmvalue" id="parmvalue43510984204110"><a name="parmvalue43510984204110"></a><a name="parmvalue43510984204110"></a><b>Decommissioning</b></span></p>
        </td>
        <td class="cellrowborder" valign="top" width="69.92%" headers="mcps1.2.3.1.2 "><p id="p286182471754"><a name="p286182471754"></a><a name="p286182471754"></a>Indicates that the role instance is being decommissioned.</p>
        </td>
        </tr>
        <tr id="row5984014417536"><td class="cellrowborder" valign="top" width="30.080000000000002%" headers="mcps1.2.3.1.1 "><p id="p1521353317536"><a name="p1521353317536"></a><a name="p1521353317536"></a><span class="parmvalue" id="parmvalue60168322204121"><a name="parmvalue60168322204121"></a><a name="parmvalue60168322204121"></a><b>Decommissioned</b></span></p>
        </td>
        <td class="cellrowborder" valign="top" width="69.92%" headers="mcps1.2.3.1.2 "><p id="p2433665017536"><a name="p2433665017536"></a><a name="p2433665017536"></a>Indicates that the role instance has been decommissioned.</p>
        </td>
        </tr>
        <tr id="row3544974817541"><td class="cellrowborder" valign="top" width="30.080000000000002%" headers="mcps1.2.3.1.1 "><p id="p5285732517541"><a name="p5285732517541"></a><a name="p5285732517541"></a><span class="parmvalue" id="parmvalue13847483204123"><a name="parmvalue13847483204123"></a><a name="parmvalue13847483204123"></a><b>Recommissioning</b></span></p>
        </td>
        <td class="cellrowborder" valign="top" width="69.92%" headers="mcps1.2.3.1.2 "><p id="p5358493117541"><a name="p5358493117541"></a><a name="p5358493117541"></a>Indicates that the role instance is being re-commissioned.</p>
        </td>
        </tr>
        <tr id="row61440257202542"><td class="cellrowborder" valign="top" width="30.080000000000002%" headers="mcps1.2.3.1.1 "><p id="p10604946202542"><a name="p10604946202542"></a><a name="p10604946202542"></a><span class="parmvalue" id="parmvalue52007004204125"><a name="parmvalue52007004204125"></a><a name="parmvalue52007004204125"></a><b>Unknown</b></span></p>
        </td>
        <td class="cellrowborder" valign="top" width="69.92%" headers="mcps1.2.3.1.2 "><p id="p53694336202542"><a name="p53694336202542"></a><a name="p53694336202542"></a>Indicates the initial role instance status after the background system restarts.</p>
        </td>
        </tr>
        </tbody>
        </table>

    -   [Table 5](#table63054543194618)  describes role instance health status.

        **Table  5**  Role instance health status

        <a name="table63054543194618"></a>
        <table><thead align="left"><tr id="row47968876194618"><th class="cellrowborder" valign="top" width="30.080000000000002%" id="mcps1.2.3.1.1"><p id="p60414271194618"><a name="p60414271194618"></a><a name="p60414271194618"></a><strong id="b38849929194618"><a name="b38849929194618"></a><a name="b38849929194618"></a>Status</strong></p>
        </th>
        <th class="cellrowborder" valign="top" width="69.92%" id="mcps1.2.3.1.2"><p id="p18065077194618"><a name="p18065077194618"></a><a name="p18065077194618"></a><strong id="b32678912194618"><a name="b32678912194618"></a><a name="b32678912194618"></a>Description</strong></p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row43760865194656"><td class="cellrowborder" valign="top" width="30.080000000000002%" headers="mcps1.2.3.1.1 "><p id="p1546418419478"><a name="p1546418419478"></a><a name="p1546418419478"></a><span class="parmvalue" id="parmvalue36854344204131"><a name="parmvalue36854344204131"></a><a name="parmvalue36854344204131"></a><b>Good</b></span></p>
        </td>
        <td class="cellrowborder" valign="top" width="69.92%" headers="mcps1.2.3.1.2 "><p id="p4179906019478"><a name="p4179906019478"></a><a name="p4179906019478"></a>Indicates that the role instance is running properly.</p>
        </td>
        </tr>
        <tr id="row65697510194710"><td class="cellrowborder" valign="top" width="30.080000000000002%" headers="mcps1.2.3.1.1 "><p id="p50050888194717"><a name="p50050888194717"></a><a name="p50050888194717"></a><span class="parmvalue" id="parmvalue65530481204133"><a name="parmvalue65530481204133"></a><a name="parmvalue65530481204133"></a><b>Bad</b></span></p>
        </td>
        <td class="cellrowborder" valign="top" width="69.92%" headers="mcps1.2.3.1.2 "><p id="p57271914194717"><a name="p57271914194717"></a><a name="p57271914194717"></a>Indicates that the role instance running is abnormal. For example, a port cannot be accessed because the PID does not exist.</p>
        </td>
        </tr>
        <tr id="row45592912194727"><td class="cellrowborder" valign="top" width="30.080000000000002%" headers="mcps1.2.3.1.1 "><p id="p49452900194734"><a name="p49452900194734"></a><a name="p49452900194734"></a><span class="parmvalue" id="parmvalue65061553204134"><a name="parmvalue65061553204134"></a><a name="parmvalue65061553204134"></a><b>Unknown</b></span></p>
        </td>
        <td class="cellrowborder" valign="top" width="69.92%" headers="mcps1.2.3.1.2 "><p id="p44232088194734"><a name="p44232088194734"></a><a name="p44232088194734"></a>Indicates that the host on which the role instance is running does not connect to the background system.</p>
        </td>
        </tr>
        <tr id="row58993983194733"><td class="cellrowborder" valign="top" width="30.080000000000002%" headers="mcps1.2.3.1.1 "><p id="p43957887194743"><a name="p43957887194743"></a><a name="p43957887194743"></a><span class="parmvalue" id="parmvalue5046076204136"><a name="parmvalue5046076204136"></a><a name="parmvalue5046076204136"></a><b>Concerning</b></span></p>
        </td>
        <td class="cellrowborder" valign="top" width="69.92%" headers="mcps1.2.3.1.2 "><p id="p58005789194743"><a name="p58005789194743"></a><a name="p58005789194743"></a>Indicates that the background system is restarting the role instance.</p>
        </td>
        </tr>
        </tbody>
        </table>

    -   [Table 6](#table12379027194818)  describes role instance configuration status.

        **Table  6**  Role instance configuration status

        <a name="table12379027194818"></a>
        <table><thead align="left"><tr id="row16585551194818"><th class="cellrowborder" valign="top" width="30.080000000000002%" id="mcps1.2.3.1.1"><p id="p39040174194818"><a name="p39040174194818"></a><a name="p39040174194818"></a><strong id="b4481411194818"><a name="b4481411194818"></a><a name="b4481411194818"></a>Status</strong></p>
        </th>
        <th class="cellrowborder" valign="top" width="69.92%" id="mcps1.2.3.1.2"><p id="p30265299194818"><a name="p30265299194818"></a><a name="p30265299194818"></a><strong id="b38328041194818"><a name="b38328041194818"></a><a name="b38328041194818"></a>Description</strong></p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row61122488194823"><td class="cellrowborder" valign="top" width="30.080000000000002%" headers="mcps1.2.3.1.1 "><p id="p35104993194833"><a name="p35104993194833"></a><a name="p35104993194833"></a><span class="parmvalue" id="parmvalue32304467204140"><a name="parmvalue32304467204140"></a><a name="parmvalue32304467204140"></a><b>Synchronized</b></span></p>
        </td>
        <td class="cellrowborder" valign="top" width="69.92%" headers="mcps1.2.3.1.2 "><p id="p66021023194833"><a name="p66021023194833"></a><a name="p66021023194833"></a>Indicates that the latest configuration has taken effect.</p>
        </td>
        </tr>
        <tr id="row25995455194832"><td class="cellrowborder" valign="top" width="30.080000000000002%" headers="mcps1.2.3.1.1 "><p id="p36097664194840"><a name="p36097664194840"></a><a name="p36097664194840"></a><span class="parmvalue" id="parmvalue27582414204142"><a name="parmvalue27582414204142"></a><a name="parmvalue27582414204142"></a><b>Expired</b></span></p>
        </td>
        <td class="cellrowborder" valign="top" width="69.92%" headers="mcps1.2.3.1.2 "><p id="p25669999194840"><a name="p25669999194840"></a><a name="p25669999194840"></a>Indicates that the latest configuration has not taken effect after the parameter modification. You need to restart the related services.</p>
        </td>
        </tr>
        <tr id="row20836403194839"><td class="cellrowborder" valign="top" width="30.080000000000002%" headers="mcps1.2.3.1.1 "><p id="p44610963194848"><a name="p44610963194848"></a><a name="p44610963194848"></a><span class="parmvalue" id="parmvalue10640524204144"><a name="parmvalue10640524204144"></a><a name="parmvalue10640524204144"></a><b>Failed</b></span></p>
        </td>
        <td class="cellrowborder" valign="top" width="69.92%" headers="mcps1.2.3.1.2 "><p id="p51191634194848"><a name="p51191634194848"></a><a name="p51191634194848"></a>Indicates that communication is abnormal or data cannot be read or written during the parameter configuration. Try clicking <strong id="b38101377194852"><a name="b38101377194852"></a><a name="b38101377194852"></a>Synchronize Configuration</strong> to recover the previous configuration.</p>
        </td>
        </tr>
        <tr id="row64786225194847"><td class="cellrowborder" valign="top" width="30.080000000000002%" headers="mcps1.2.3.1.1 "><p id="p3966346219490"><a name="p3966346219490"></a><a name="p3966346219490"></a><span class="parmvalue" id="parmvalue21967772204145"><a name="parmvalue21967772204145"></a><a name="parmvalue21967772204145"></a><b>Configuring</b></span></p>
        </td>
        <td class="cellrowborder" valign="top" width="69.92%" headers="mcps1.2.3.1.2 "><p id="p4816373719490"><a name="p4816373719490"></a><a name="p4816373719490"></a>Indicates that the parameter is being configured.</p>
        </td>
        </tr>
        <tr id="row64493045194859"><td class="cellrowborder" valign="top" width="30.080000000000002%" headers="mcps1.2.3.1.1 "><p id="p3483504019494"><a name="p3483504019494"></a><a name="p3483504019494"></a><span class="parmvalue" id="parmvalue1124963204148"><a name="parmvalue1124963204148"></a><a name="parmvalue1124963204148"></a><b>Unknown</b></span></p>
        </td>
        <td class="cellrowborder" valign="top" width="69.92%" headers="mcps1.2.3.1.2 "><p id="p635742519494"><a name="p635742519494"></a><a name="p635742519494"></a>Indicates that configuration status cannot be obtained.</p>
        </td>
        </tr>
        </tbody>
        </table>

    By default, roles are displayed in ascending order by  **Role.** You can click **Role**, **Host Name**, **OM IP Address**, **Business IP Address**, **Rack**, **Operating Status**, **Health Status**, or **Configuration Status**  to change the display mode.

    You can filter out all instances of the same role in  **Role**.

    Click  **Advanced Search**, set search criteria in the role search area, and click  **Search**  to view specified role information. You can click  **Reset**  to reset search criteria. Fuzzy search is supported.

3.  Click the target role instance in the role instance list to view its status and indicator information.
4.  Customize monitoring indicators and export customized monitoring information. The operation process is the same as that of exporting service monitoring indicators.

## Managing Host Monitoring<a name="section5379558214590"></a>

1.  On MRS Manager, click  **Host**.

    The host list includes  **Host Name**, **OM IP Address**, **Business IP Address**, **Rack**, **Network Speed**, **Operating Status**, **Health Status**, **Disk Usage**, **Memory Usage** and **CPU Usage**.

    -   [Table 7](#table12921900145546) describes the operating  status.

        **Table  7**  Host operating  status

        <a name="table12921900145546"></a>
        <table><thead align="left"><tr id="row6278408715739"><th class="cellrowborder" valign="top" width="30.080000000000002%" id="mcps1.2.3.1.1"><p id="p5161708815739"><a name="p5161708815739"></a><a name="p5161708815739"></a><strong id="b4231516715755"><a name="b4231516715755"></a><a name="b4231516715755"></a>Status</strong></p>
        </th>
        <th class="cellrowborder" valign="top" width="69.92%" id="mcps1.2.3.1.2"><p id="p2023457915739"><a name="p2023457915739"></a><a name="p2023457915739"></a><strong id="b497653115755"><a name="b497653115755"></a><a name="b497653115755"></a>Description</strong></p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row1443255015739"><td class="cellrowborder" valign="top" width="30.080000000000002%" headers="mcps1.2.3.1.1 "><p id="p1774076215739"><a name="p1774076215739"></a><a name="p1774076215739"></a><span class="parmvalue" id="parmvalue2445020420424"><a name="parmvalue2445020420424"></a><a name="parmvalue2445020420424"></a><b>Normal</b></span></p>
        </td>
        <td class="cellrowborder" valign="top" width="69.92%" headers="mcps1.2.3.1.2 "><p id="p2771561415739"><a name="p2771561415739"></a><a name="p2771561415739"></a>The host and service roles on the host are running properly.</p>
        </td>
        </tr>
        <tr id="row3888631815739"><td class="cellrowborder" valign="top" width="30.080000000000002%" headers="mcps1.2.3.1.1 "><p id="p491516915739"><a name="p491516915739"></a><a name="p491516915739"></a><span class="parmvalue" id="parmvalue3139546920426"><a name="parmvalue3139546920426"></a><a name="parmvalue3139546920426"></a><b>Isolated</b></span></p>
        </td>
        <td class="cellrowborder" valign="top" width="69.92%" headers="mcps1.2.3.1.2 "><p id="p6258444215739"><a name="p6258444215739"></a><a name="p6258444215739"></a>The host is isolated by the user, and service roles on the host are stopped.</p>
        </td>
        </tr>
        </tbody>
        </table>

    -   [Table 8](#table17530916145640)  describes host health status.

        **Table  8**  Host health status

        <a name="table17530916145640"></a>
        <table><thead align="left"><tr id="row3133275515812"><th class="cellrowborder" valign="top" width="30.259999999999998%" id="mcps1.2.3.1.1"><p id="p3488639615812"><a name="p3488639615812"></a><a name="p3488639615812"></a><strong id="b4203687715836"><a name="b4203687715836"></a><a name="b4203687715836"></a>Status</strong></p>
        </th>
        <th class="cellrowborder" valign="top" width="69.74000000000001%" id="mcps1.2.3.1.2"><p id="p722583215812"><a name="p722583215812"></a><a name="p722583215812"></a><strong id="b4954387215836"><a name="b4954387215836"></a><a name="b4954387215836"></a>Description</strong></p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row348141715812"><td class="cellrowborder" valign="top" width="30.259999999999998%" headers="mcps1.2.3.1.1 "><p id="p2982875315812"><a name="p2982875315812"></a><a name="p2982875315812"></a><span class="parmvalue" id="parmvalue4819115720428"><a name="parmvalue4819115720428"></a><a name="parmvalue4819115720428"></a><b>Good</b></span></p>
        </td>
        <td class="cellrowborder" valign="top" width="69.74000000000001%" headers="mcps1.2.3.1.2 "><p id="p20995115812"><a name="p20995115812"></a><a name="p20995115812"></a>Indicates that the host can properly send heartbeats.</p>
        </td>
        </tr>
        <tr id="row5258260715812"><td class="cellrowborder" valign="top" width="30.259999999999998%" headers="mcps1.2.3.1.1 "><p id="p1883667715812"><a name="p1883667715812"></a><a name="p1883667715812"></a><span class="parmvalue" id="parmvalue30861090204210"><a name="parmvalue30861090204210"></a><a name="parmvalue30861090204210"></a><b>Bad</b></span></p>
        </td>
        <td class="cellrowborder" valign="top" width="69.74000000000001%" headers="mcps1.2.3.1.2 "><p id="p4937588715812"><a name="p4937588715812"></a><a name="p4937588715812"></a>Indicates that the host fails to send heartbeats due to timeout.</p>
        </td>
        </tr>
        <tr id="row1329905215812"><td class="cellrowborder" valign="top" width="30.259999999999998%" headers="mcps1.2.3.1.1 "><p id="p2467079315812"><a name="p2467079315812"></a><a name="p2467079315812"></a><span class="parmvalue" id="parmvalue65200786204212"><a name="parmvalue65200786204212"></a><a name="parmvalue65200786204212"></a><b>Unknown</b></span></p>
        </td>
        <td class="cellrowborder" valign="top" width="69.74000000000001%" headers="mcps1.2.3.1.2 "><p id="p5217724115812"><a name="p5217724115812"></a><a name="p5217724115812"></a>Indicates the initial status of the host when it is being added.</p>
        </td>
        </tr>
        </tbody>
        </table>

    By default, roles are displayed in ascending order by  **Host Name**. You can click **Host Name**, **OM IP Address**, **Business IP Address**, **Rack**, **NetWork Speed**, **Operating Status**, **Health Status**, **Disk Usage**, **Memory Usage**, or **CPU Usage**  to change the display mode.

    Click  **Advanced Search**, set search criteria in the role search area, and click  **Search**  to view specified host information. You can click  **Reset**  to reset search criteria. Fuzzy search is supported.

2.  Click the target host in the host list to view its status and indicator information.
3.  Customize monitoring indicators and export customized monitoring information.

    For MRS 1.9.2 or later:

    1.  In the  **Charts**  area, click  **Customize**  to customize service monitoring metrics.
    2.  In  **Period**, select a time of period and click  **View**  to view the monitoring data within the time period.
    3.  Click  **Export**  to export the displayed metric information.

    For versions earlier than MRS 1.9.2:

    1.  In the  **Real-Time Monitoring**  area, click **Customize**  to customize key monitoring indicators.
    2.  Click  **History**  to display the page in which you can query historical monitoring information.
    3.  Select a time period, and click  **View**  to display the monitoring data in the specified time period.
    4.  Click  **Export**  to export the displayed indicator information.


