# Handling False Alarms<a name="waf_01_0024"></a>

This section describes how to mask  false alarms  and view event details if you find out that an event is misreported.

## Prerequisites<a name="section32633759143848"></a>

-   Login credentials have been obtained.
-   The event list contains at least one misreported event.

## Procedure<a name="section14647895143912"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner of the management console and select a region or project.
3.  Choose  **Security**  \>  **Web Application Firewall**. In the navigation pane, choose  **Events**. The  **Events**  page is displayed.
4.  Click the  **Search**  tab. In the domain name drop-down list, select a domain name or  **All domain names**  to view target event logs. The query time can be  **Yesterday**,  **Today**,  **Past 3 days**,  **Past 7 days**,  **Past 30 days**, or a user-defined time. See  [Figure 1](#fig194311743164914).  [Table 1](#table146358613417)  and  [Table 2](#table135241210519)  list related parameters.

    In the upper right corner of the event list, click  **Search by ID**  to search a target event by ID.

    **Figure  1**  Search tab page<a name="fig194311743164914"></a>  
    ![](figures/search-tab-page.png "search-tab-page")

    **Table  1**  Event parameters

    <a name="table146358613417"></a>
    <table><thead align="left"><tr id="row863606163419"><th class="cellrowborder" valign="top" width="35.809999999999995%" id="mcps1.2.3.1.1"><p id="p18636268343"><a name="p18636268343"></a><a name="p18636268343"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="64.19%" id="mcps1.2.3.1.2"><p id="p26369693419"><a name="p26369693419"></a><a name="p26369693419"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row18636563347"><td class="cellrowborder" valign="top" width="35.809999999999995%" headers="mcps1.2.3.1.1 "><p id="p863619643414"><a name="p863619643414"></a><a name="p863619643414"></a>Event Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.19%" headers="mcps1.2.3.1.2 "><p id="p263610619345"><a name="p263610619345"></a><a name="p263610619345"></a>Type of an attack</p>
    <p id="p946816714218"><a name="p946816714218"></a><a name="p946816714218"></a>By default, <strong id="b19111135812559"><a name="b19111135812559"></a><a name="b19111135812559"></a>All</strong> is selected. You can view logs of all attack types or select an attack type to view target attack logs.</p>
    </td>
    </tr>
    <tr id="row1563616616349"><td class="cellrowborder" valign="top" width="35.809999999999995%" headers="mcps1.2.3.1.1 "><p id="p36361763345"><a name="p36361763345"></a><a name="p36361763345"></a>Source IP Address</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.19%" headers="mcps1.2.3.1.2 "><p id="p15246151320427"><a name="p15246151320427"></a><a name="p15246151320427"></a>Public IP address of the web visitor/attacker</p>
    <p id="p66364618344"><a name="p66364618344"></a><a name="p66364618344"></a>By default, <strong id="b16906126154519"><a name="b16906126154519"></a><a name="b16906126154519"></a>All</strong> is selected. You can view logs of all attack source IP addresses, select an attack source IP address, or enter an attack source IP address to view target attack logs.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  Log list parameters

    <a name="table135241210519"></a>
    <table><thead align="left"><tr id="row135266102011"><th class="cellrowborder" valign="top" width="35.199999999999996%" id="mcps1.2.3.1.1"><p id="p151817452118"><a name="p151817452118"></a><a name="p151817452118"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="64.8%" id="mcps1.2.3.1.2"><p id="p1818154515118"><a name="p1818154515118"></a><a name="p1818154515118"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row152661018114"><td class="cellrowborder" valign="top" width="35.199999999999996%" headers="mcps1.2.3.1.1 "><p id="p1056814367118"><a name="p1056814367118"></a><a name="p1056814367118"></a>Time</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.8%" headers="mcps1.2.3.1.2 "><p id="p856817369112"><a name="p856817369112"></a><a name="p856817369112"></a>Time when an attack occurs</p>
    </td>
    </tr>
    <tr id="row352616101114"><td class="cellrowborder" valign="top" width="35.199999999999996%" headers="mcps1.2.3.1.1 "><p id="p656818369112"><a name="p656818369112"></a><a name="p656818369112"></a>Source IP Address</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.8%" headers="mcps1.2.3.1.2 "><p id="p6568163613117"><a name="p6568163613117"></a><a name="p6568163613117"></a>Public IP address of the web visitor/attacker</p>
    </td>
    </tr>
    <tr id="row652611010115"><td class="cellrowborder" valign="top" width="35.199999999999996%" headers="mcps1.2.3.1.1 "><p id="p95681136218"><a name="p95681136218"></a><a name="p95681136218"></a>Domain Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.8%" headers="mcps1.2.3.1.2 "><p id="p13568163617118"><a name="p13568163617118"></a><a name="p13568163617118"></a>Attacked domain name</p>
    </td>
    </tr>
    <tr id="row10526810313"><td class="cellrowborder" valign="top" width="35.199999999999996%" headers="mcps1.2.3.1.1 "><p id="p105681236616"><a name="p105681236616"></a><a name="p105681236616"></a>URL</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.8%" headers="mcps1.2.3.1.2 "><p id="p15689361714"><a name="p15689361714"></a><a name="p15689361714"></a>Attacked URL</p>
    </td>
    </tr>
    <tr id="row635713296113"><td class="cellrowborder" valign="top" width="35.199999999999996%" headers="mcps1.2.3.1.1 "><p id="p175681036316"><a name="p175681036316"></a><a name="p175681036316"></a>Malicious Load</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.8%" headers="mcps1.2.3.1.2 "><p id="p115684361018"><a name="p115684361018"></a><a name="p115684361018"></a>Location of the malicious load</p>
    </td>
    </tr>
    <tr id="row33596297111"><td class="cellrowborder" valign="top" width="35.199999999999996%" headers="mcps1.2.3.1.1 "><p id="p85682036716"><a name="p85682036716"></a><a name="p85682036716"></a>Event Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.8%" headers="mcps1.2.3.1.2 "><p id="p1856843612117"><a name="p1856843612117"></a><a name="p1856843612117"></a>Type of an attack</p>
    </td>
    </tr>
    <tr id="row17359429116"><td class="cellrowborder" valign="top" width="35.199999999999996%" headers="mcps1.2.3.1.1 "><p id="p1556810365113"><a name="p1556810365113"></a><a name="p1556810365113"></a>Protective Action</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.8%" headers="mcps1.2.3.1.2 "><p id="p556853615117"><a name="p556853615117"></a><a name="p556853615117"></a>The options are <strong id="b13686123512297"><a name="b13686123512297"></a><a name="b13686123512297"></a>Block</strong>, <strong id="b9686035102920"><a name="b9686035102920"></a><a name="b9686035102920"></a>Log only</strong>, <strong id="b4687435102919"><a name="b4687435102919"></a><a name="b4687435102919"></a>Allow</strong>, <strong id="b136881835162919"><a name="b136881835162919"></a><a name="b136881835162919"></a>Verification code</strong>, <span class="parmvalue" id="parmvalue17141649154916"><a name="parmvalue17141649154916"></a><a name="parmvalue17141649154916"></a><b>Filter</b></span>, and <span class="parmvalue" id="parmvalue177251243154914"><a name="parmvalue177251243154914"></a><a name="parmvalue177251243154914"></a><b>Mismatch</b></span>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >To view event details, click  **Details**  in the  **Operation**  column of the event list.  

5.  If an event is misreported, add a false alarm masking rule by clicking  **Handle False Alarm**  in the row of the event.  [Figure 2](#fig16174064111318)  displays the  **Handle False Alarm**  dialog box.  [Table 3](#table35022095114540)  lists related parameters.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >False alarm masking only applies to events logged by built-in basic web protection rules. If you want to mask events logged by custom rules, delete the rules.  

    **Figure  2**  Handling a false alarm<a name="fig16174064111318"></a>  
    ![](figures/handling-a-false-alarm.png "handling-a-false-alarm")

    **Table  3**  Parameter description

    <a name="table35022095114540"></a>
    <table><thead align="left"><tr id="row3795605114540"><th class="cellrowborder" valign="top" width="19.46%" id="mcps1.2.4.1.1"><p id="p15532793114540"><a name="p15532793114540"></a><a name="p15532793114540"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="54.54%" id="mcps1.2.4.1.2"><p id="p50196703114540"><a name="p50196703114540"></a><a name="p50196703114540"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="26%" id="mcps1.2.4.1.3"><p id="p484549421532"><a name="p484549421532"></a><a name="p484549421532"></a>Example Value</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row49117151114540"><td class="cellrowborder" valign="top" width="19.46%" headers="mcps1.2.4.1.1 "><p id="p19066291114540"><a name="p19066291114540"></a><a name="p19066291114540"></a>Domain Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.54%" headers="mcps1.2.4.1.2 "><p id="p25759607111430"><a name="p25759607111430"></a><a name="p25759607111430"></a>Domain name where an attack occurs, which is obtained automatically by the system</p>
    </td>
    <td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.3 "><p id="p325361901532"><a name="p325361901532"></a><a name="p325361901532"></a>--</p>
    </td>
    </tr>
    <tr id="row7791918114540"><td class="cellrowborder" valign="top" width="19.46%" headers="mcps1.2.4.1.1 "><p id="p4870307111345"><a name="p4870307111345"></a><a name="p4870307111345"></a>Path</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.54%" headers="mcps1.2.4.1.2 "><p id="p4453024316644"><a name="p4453024316644"></a><a name="p4453024316644"></a>Misreported URL excluding a domain name</p>
    <a name="ul1515617591337"></a><a name="ul1515617591337"></a><ul id="ul1515617591337"><li>Prefix match: The path ending with * indicates that the path is used as a prefix. For example, if the path to be protected is <strong id="b1441113340528"><a name="b1441113340528"></a><a name="b1441113340528"></a>/admin/test.php</strong> or <strong id="b15411183455219"><a name="b15411183455219"></a><a name="b15411183455219"></a>/adminabc</strong>, set <strong id="b9411113425218"><a name="b9411113425218"></a><a name="b9411113425218"></a>Path</strong> to <span class="parmvalue" id="parmvalue13411143415211"><a name="parmvalue13411143415211"></a><a name="parmvalue13411143415211"></a><b>/admin*</b></span>.</li><li>Exact match: The path to be entered must match the path to be protected. If the path to be protected is <span class="parmvalue" id="parmvalue158383714524"><a name="parmvalue158383714524"></a><a name="parmvalue158383714524"></a><b>/admin</b></span>, set <strong id="b68353715529"><a name="b68353715529"></a><a name="b68353715529"></a>Path</strong> to <span class="parmvalue" id="parmvalue12830373522"><a name="parmvalue12830373522"></a><a name="parmvalue12830373522"></a><b>/admin</b></span>.</li></ul>
    <div class="note" id="note1170665517195"><a name="note1170665517195"></a><a name="note1170665517195"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul20707155819344"></a><a name="ul20707155819344"></a><ul id="ul20707155819344"><li>The path supports prefix and exact matches only and does not support regular expressions.</li><li>The path cannot contain two or more consecutive slashes. For example, <span class="parmvalue" id="parmvalue470517151214"><a name="parmvalue470517151214"></a><a name="parmvalue470517151214"></a><b>///admin</b></span>. If you enter <strong id="b177054151416"><a name="b177054151416"></a><a name="b177054151416"></a>///admin</strong>, the WAF engine converts <strong id="b57052015610"><a name="b57052015610"></a><a name="b57052015610"></a>///</strong> to <strong id="b9705015212"><a name="b9705015212"></a><a name="b9705015212"></a>/</strong>.</li></ul>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.3 "><p id="p181857061532"><a name="p181857061532"></a><a name="p181857061532"></a><strong id="b4333124435218"><a name="b4333124435218"></a><a name="b4333124435218"></a>/admin*</strong></p>
    </td>
    </tr>
    <tr id="row6648026114540"><td class="cellrowborder" valign="top" width="19.46%" headers="mcps1.2.4.1.1 "><p id="p14932980114558"><a name="p14932980114558"></a><a name="p14932980114558"></a>Event ID</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.54%" headers="mcps1.2.4.1.2 "><p id="p6504365416657"><a name="p6504365416657"></a><a name="p6504365416657"></a>ID of a built-in rule that is automatically read. The value consists of six digits.</p>
    </td>
    <td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.3 "><p id="p637561071532"><a name="p637561071532"></a><a name="p637561071532"></a>223604</p>
    </td>
    </tr>
    </tbody>
    </table>

6.  Click  **OK**. The event is no longer displayed in the event list.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >You can switch to the  **Domains**  page, locate the row containing the target domain name, click  **Configure Policy**  in the  **Operation**  column. In the  **False Alarm Masking**  area, click  **Customize Rule**  to view the added false alarm rule.  


