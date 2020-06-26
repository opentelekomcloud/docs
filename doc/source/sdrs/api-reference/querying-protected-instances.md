# Querying Protected Instances<a name="sdrs_05_0503"></a>

## Function<a name="en-us_topic_0079693002_section34649765"></a>

This API is used to query all protected instances of the current tenant.

## Constraints and Limitations<a name="section05625817356"></a>

None

## URI<a name="en-us_topic_0079693002_section39390935"></a>

-   URI format

    GET /v1/\{project\_id\}/protected-instances

-   Parameter description

    <a name="en-us_topic_0079693002_table63321005"></a>
    <table><thead align="left"><tr id="en-us_topic_0079693002_row37593218"><th class="cellrowborder" valign="top" width="16.831683168316832%" id="mcps1.1.5.1.1"><p id="p9233435142118"><a name="p9233435142118"></a><a name="p9233435142118"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.82178217821782%" id="mcps1.1.5.1.2"><p id="p023343562111"><a name="p023343562111"></a><a name="p023343562111"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.841584158415841%" id="mcps1.1.5.1.3"><p id="p22331735192115"><a name="p22331735192115"></a><a name="p22331735192115"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="49.504950495049506%" id="mcps1.1.5.1.4"><p id="p323353552116"><a name="p323353552116"></a><a name="p323353552116"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0079693002_row29123463"><td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.1.5.1.1 "><p id="p423363582116"><a name="p423363582116"></a><a name="p423363582116"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.5.1.2 "><p id="p72337356212"><a name="p72337356212"></a><a name="p72337356212"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.1.5.1.3 "><p id="p1123383512216"><a name="p1123383512216"></a><a name="p1123383512216"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.504950495049506%" headers="mcps1.1.5.1.4 "><p id="p0233133515212"><a name="p0233133515212"></a><a name="p0233133515212"></a>Specifies the project ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   **Request filter**  field description

    <a name="en-us_topic_0079693002_table54932709"></a>
    <table><thead align="left"><tr id="en-us_topic_0079693002_row41882373"><th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.1"><p id="p5993153132217"><a name="p5993153132217"></a><a name="p5993153132217"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.1.5.1.2"><p id="p159934352213"><a name="p159934352213"></a><a name="p159934352213"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.1.5.1.3"><p id="p17993932228"><a name="p17993932228"></a><a name="p17993932228"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.1.5.1.4"><p id="p6993133142211"><a name="p6993133142211"></a><a name="p6993133142211"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0079693002_row27990155"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p109936319223"><a name="p109936319223"></a><a name="p109936319223"></a>server_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.2 "><p id="p169931338224"><a name="p169931338224"></a><a name="p169931338224"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.3 "><p id="p2993153152218"><a name="p2993153152218"></a><a name="p2993153152218"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.5.1.4 "><p id="p1499311316224"><a name="p1499311316224"></a><a name="p1499311316224"></a>Specifies the ID of the protection group, in which all protected instances are queried.</p>
    <p id="p1048183415411"><a name="p1048183415411"></a><a name="p1048183415411"></a>For details, see the parameter description in <a href="querying-protection-groups.md">Querying Protection Groups</a>.</p>
    </td>
    </tr>
    <tr id="row456416853418"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0098680634_p11113121412125"><a name="en-us_topic_0098680634_p11113121412125"></a><a name="en-us_topic_0098680634_p11113121412125"></a>server_group_ids</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0098680634_p1811371412124"><a name="en-us_topic_0098680634_p1811371412124"></a><a name="en-us_topic_0098680634_p1811371412124"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0098680634_p9113191413128"><a name="en-us_topic_0098680634_p9113191413128"></a><a name="en-us_topic_0098680634_p9113191413128"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.5.1.4 "><p id="p3536550151920"><a name="p3536550151920"></a><a name="p3536550151920"></a>Specifies the protection group ID list. The value is in the following format: server_group_ids=['server_group_id1','server_group_id2',...,'server_group_idx']. Convert it using URL encoding.</p>
    <a name="ul16112828111918"></a><a name="ul16112828111918"></a><ul id="ul16112828111918"><li>All the protected instances with valid <strong id="b118041356194117"><a name="b118041356194117"></a><a name="b118041356194117"></a>server_group_id</strong> in <strong id="b742317474213"><a name="b742317474213"></a><a name="b742317474213"></a>server_group_ids</strong> are returned.</li><li>The protected instances of a maximum of 30 <strong id="b7103652174210"><a name="b7103652174210"></a><a name="b7103652174210"></a>server_group_id</strong> values can be queried.</li><li>If parameters <strong id="b84235270611260"><a name="b84235270611260"></a><a name="b84235270611260"></a>server_group_id</strong> and <strong id="b84235270611263"><a name="b84235270611263"></a><a name="b84235270611263"></a>server_group_ids</strong> are both specified in the request, <strong id="b842352706112623"><a name="b842352706112623"></a><a name="b842352706112623"></a>server_group_id</strong> will be ignored.</li></ul>
    </td>
    </tr>
    <tr id="row368674415413"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p1023184073717"><a name="p1023184073717"></a><a name="p1023184073717"></a>protected_instance_ids</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.2 "><p id="p22314405374"><a name="p22314405374"></a><a name="p22314405374"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.3 "><p id="p1843012811381"><a name="p1843012811381"></a><a name="p1843012811381"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.5.1.4 "><p id="p114871084298"><a name="p114871084298"></a><a name="p114871084298"></a>Specifies the protected instance ID list. The value is in the following format: protected_instance_ids=['protected_instance_id1','protected_instance_id2',...,'protected_instance_idx']. Convert it using URL encoding.</p>
    <a name="ul2717122943019"></a><a name="ul2717122943019"></a><ul id="ul2717122943019"><li>All the protected instances with valid <strong id="b1547615104414"><a name="b1547615104414"></a><a name="b1547615104414"></a>protected_instance_id</strong> in <strong id="b2054981524410"><a name="b2054981524410"></a><a name="b2054981524410"></a>protected_instance_ids</strong> are returned.</li><li>The protected instances of a maximum of 30 <strong id="b17833199124511"><a name="b17833199124511"></a><a name="b17833199124511"></a>protected_instance_id</strong> values can be queried.</li><li>If parameter <strong id="b1958594464614"><a name="b1958594464614"></a><a name="b1958594464614"></a>server_group_id</strong> or <strong id="b1158664424612"><a name="b1158664424612"></a><a name="b1158664424612"></a>server_group_ids</strong> is specified in the request, <strong id="b1658764444619"><a name="b1658764444619"></a><a name="b1658764444619"></a>protected_instance_ids</strong> will be ignored.</li></ul>
    </td>
    </tr>
    <tr id="row18946143774014"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p109937312222"><a name="p109937312222"></a><a name="p109937312222"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.2 "><p id="p18993123132214"><a name="p18993123132214"></a><a name="p18993123132214"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.3 "><p id="p1399319320225"><a name="p1399319320225"></a><a name="p1399319320225"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.5.1.4 "><p id="p15993238229"><a name="p15993238229"></a><a name="p15993238229"></a>Specifies the maximum number of results returned each time. The value is a positive integer from 0 to 1000. The default value is <strong id="b842352706161435"><a name="b842352706161435"></a><a name="b842352706161435"></a>1000</strong>.</p>
    </td>
    </tr>
    <tr id="row37594054014"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p109931738226"><a name="p109931738226"></a><a name="p109931738226"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.2 "><p id="p1299314316228"><a name="p1299314316228"></a><a name="p1299314316228"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.3 "><p id="p2993113152211"><a name="p2993113152211"></a><a name="p2993113152211"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.5.1.4 "><p id="p699303162217"><a name="p699303162217"></a><a name="p699303162217"></a>Specifies the offset of each request. The default value is <strong id="b74201644142916"><a name="b74201644142916"></a><a name="b74201644142916"></a>0</strong>. The value must be a number and cannot be negative.</p>
    </td>
    </tr>
    <tr id="row11694161516"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p33631043105615"><a name="p33631043105615"></a><a name="p33631043105615"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.2 "><p id="p193637436561"><a name="p193637436561"></a><a name="p193637436561"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.3 "><p id="p2363174355610"><a name="p2363174355610"></a><a name="p2363174355610"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.5.1.4 "><p id="p6363134316569"><a name="p6363134316569"></a><a name="p6363134316569"></a>Specifies the status of a protected instance.</p>
    <p id="p188093812119"><a name="p188093812119"></a><a name="p188093812119"></a>For details, see <a href="protected-instance-status.md">Protected Instance Status</a>.</p>
    </td>
    </tr>
    <tr id="row1911344218407"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p179931336225"><a name="p179931336225"></a><a name="p179931336225"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.2 "><p id="p18993039227"><a name="p18993039227"></a><a name="p18993039227"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.3 "><p id="p11993173102214"><a name="p11993173102214"></a><a name="p11993173102214"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.5.1.4 "><p id="p169932352210"><a name="p169932352210"></a><a name="p169932352210"></a>Specifies the name of a protected instance. Fuzzy search is supported.</p>
    </td>
    </tr>
    <tr id="row1547615224210"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p1315305251611"><a name="p1315305251611"></a><a name="p1315305251611"></a>query_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.2 "><p id="p41537522160"><a name="p41537522160"></a><a name="p41537522160"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.3 "><p id="p18153205216167"><a name="p18153205216167"></a><a name="p18153205216167"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.5.1.4 "><p id="p1415405216161"><a name="p1415405216161"></a><a name="p1415405216161"></a>Specifies the query type.</p>
    <a name="ul650863217178"></a><a name="ul650863217178"></a><ul id="ul650863217178"><li><strong id="b84235270615149"><a name="b84235270615149"></a><a name="b84235270615149"></a>status_abnormal</strong>: indicates to query protected instances in the abnormal status.</li><li>This parameter is invalid when the value is set to <strong id="b14611173322915"><a name="b14611173322915"></a><a name="b14611173322915"></a>general</strong> or left empty.</li></ul>
    </td>
    </tr>
    <tr id="row442614260214"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p13773157191611"><a name="p13773157191611"></a><a name="p13773157191611"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.2 "><p id="p3773957151611"><a name="p3773957151611"></a><a name="p3773957151611"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.3 "><p id="p1177518571167"><a name="p1177518571167"></a><a name="p1177518571167"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.5.1.4 "><p id="p1577510578162"><a name="p1577510578162"></a><a name="p1577510578162"></a>Specifies the current production site AZ of the protection group containing the protected instance.</p>
    <p id="p17962192313549"><a name="p17962192313549"></a><a name="p17962192313549"></a>You can obtain this value by calling the API described in <a href="querying-an-active-active-domain.md">Querying an Active-Active Domain</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section14778764117"></a>

-   Request parameter description

    None

-   Example request

    ```
    https://{Endpoint}/v1/{project_id}/protected-instances?server_group_ids=%5b%2221d65fa4-430e-4761-b9ad-4e27364f874c%22%2c%22943c7d15-0371-4b89-b1a6-db1ef35c9263%22%5d&status=available
    ```

    >![](/images/icon-note.gif) **NOTE:**   
    >Use URL encoding for  **server\_group\_ids**  or  **protected\_instance\_ids**.  


## Response<a name="en-us_topic_0079693002_section36549175"></a>

-   Parameter description

    <a name="table155991608555"></a>
    <table><thead align="left"><tr id="row460510055518"><th class="cellrowborder" valign="top" width="29.07%" id="mcps1.1.4.1.1"><p id="p56078010555"><a name="p56078010555"></a><a name="p56078010555"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.44%" id="mcps1.1.4.1.2"><p id="p961219016552"><a name="p961219016552"></a><a name="p961219016552"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.49%" id="mcps1.1.4.1.3"><p id="p186139012557"><a name="p186139012557"></a><a name="p186139012557"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row86164025512"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.1.4.1.1 "><p id="p14976144015221"><a name="p14976144015221"></a><a name="p14976144015221"></a>protected_instances</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.1.4.1.2 "><p id="p9976640172214"><a name="p9976640172214"></a><a name="p9976640172214"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.1.4.1.3 "><p id="p1697674092220"><a name="p1697674092220"></a><a name="p1697674092220"></a>Specifies the information about protected instances.</p>
    <p id="p154411354217"><a name="p154411354217"></a><a name="p154411354217"></a>For details, see <a href="#table503353570">Table 1</a>.</p>
    </td>
    </tr>
    <tr id="row166368013553"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.1.4.1.1 "><p id="p149761340122212"><a name="p149761340122212"></a><a name="p149761340122212"></a>count</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.1.4.1.2 "><p id="p139761640132215"><a name="p139761640132215"></a><a name="p139761640132215"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.1.4.1.3 "><p id="p1297664012212"><a name="p1297664012212"></a><a name="p1297664012212"></a>Specifies the number of protected instances.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  1** **protected\_instances**  field description

    <a name="table503353570"></a>
    <table><thead align="left"><tr id="row131163505710"><th class="cellrowborder" valign="top" width="29.07%" id="mcps1.2.4.1.1"><p id="p19375192311238"><a name="p19375192311238"></a><a name="p19375192311238"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.34%" id="mcps1.2.4.1.2"><p id="p137512392315"><a name="p137512392315"></a><a name="p137512392315"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.59%" id="mcps1.2.4.1.3"><p id="p183751523192314"><a name="p183751523192314"></a><a name="p183751523192314"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1829133585715"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p7375132315239"><a name="p7375132315239"></a><a name="p7375132315239"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.34%" headers="mcps1.2.4.1.2 "><p id="p237592310236"><a name="p237592310236"></a><a name="p237592310236"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.59%" headers="mcps1.2.4.1.3 "><p id="p937518232232"><a name="p937518232232"></a><a name="p937518232232"></a>Specifies the ID of a protected instance.</p>
    </td>
    </tr>
    <tr id="row1472144614199"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p13751523152316"><a name="p13751523152316"></a><a name="p13751523152316"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.34%" headers="mcps1.2.4.1.2 "><p id="p1537592313235"><a name="p1537592313235"></a><a name="p1537592313235"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.59%" headers="mcps1.2.4.1.3 "><p id="p7375102312318"><a name="p7375102312318"></a><a name="p7375102312318"></a>Specifies the name of a protected instance.</p>
    </td>
    </tr>
    <tr id="row1845264811918"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p1266741153611"><a name="p1266741153611"></a><a name="p1266741153611"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.34%" headers="mcps1.2.4.1.2 "><p id="p826674111364"><a name="p826674111364"></a><a name="p826674111364"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.59%" headers="mcps1.2.4.1.3 "><p id="p19266104123612"><a name="p19266104123612"></a><a name="p19266104123612"></a>Specifies the description of a protected instance.</p>
    </td>
    </tr>
    <tr id="row555943910310"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p14377923112315"><a name="p14377923112315"></a><a name="p14377923112315"></a>server_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.34%" headers="mcps1.2.4.1.2 "><p id="p18377823152317"><a name="p18377823152317"></a><a name="p18377823152317"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.59%" headers="mcps1.2.4.1.3 "><p id="p1237702319235"><a name="p1237702319235"></a><a name="p1237702319235"></a>Specifies the ID of a protection group.</p>
    </td>
    </tr>
    <tr id="row2503145051917"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p8375223142315"><a name="p8375223142315"></a><a name="p8375223142315"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.34%" headers="mcps1.2.4.1.2 "><p id="p17377723182310"><a name="p17377723182310"></a><a name="p17377723182310"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.59%" headers="mcps1.2.4.1.3 "><p id="p26171744195317"><a name="p26171744195317"></a><a name="p26171744195317"></a>Specifies the status of a protected instance.</p>
    <p id="p11377122372317"><a name="p11377122372317"></a><a name="p11377122372317"></a>For details, see <a href="protected-instance-status.md">Protected Instance Status</a>.</p>
    </td>
    </tr>
    <tr id="row168521941147"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p14745142282317"><a name="p14745142282317"></a><a name="p14745142282317"></a>progress</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.34%" headers="mcps1.2.4.1.2 "><p id="p1830712716181"><a name="p1830712716181"></a><a name="p1830712716181"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.59%" headers="mcps1.2.4.1.3 "><p id="p1330727191818"><a name="p1330727191818"></a><a name="p1330727191818"></a>Specifies the synchronization progress of a protected instance.</p>
    <p id="p12307127121818"><a name="p12307127121818"></a><a name="p12307127121818"></a>Unit: %</p>
    </td>
    </tr>
    <tr id="row156171333144116"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p33771237238"><a name="p33771237238"></a><a name="p33771237238"></a>source_server</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.34%" headers="mcps1.2.4.1.2 "><p id="p837714234239"><a name="p837714234239"></a><a name="p837714234239"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.59%" headers="mcps1.2.4.1.3 "><p id="p8377152312314"><a name="p8377152312314"></a><a name="p8377152312314"></a>Specifies the production site server ID.</p>
    </td>
    </tr>
    <tr id="row473463515411"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p1037702317238"><a name="p1037702317238"></a><a name="p1037702317238"></a>target_server</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.34%" headers="mcps1.2.4.1.2 "><p id="p23779231233"><a name="p23779231233"></a><a name="p23779231233"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.59%" headers="mcps1.2.4.1.3 "><p id="p12377192316233"><a name="p12377192316233"></a><a name="p12377192316233"></a>Specifies the DR site server ID.</p>
    </td>
    </tr>
    <tr id="row022814014120"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p12377923192314"><a name="p12377923192314"></a><a name="p12377923192314"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.34%" headers="mcps1.2.4.1.2 "><p id="p737762314230"><a name="p737762314230"></a><a name="p737762314230"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.59%" headers="mcps1.2.4.1.3 "><p id="p4377182318230"><a name="p4377182318230"></a><a name="p4377182318230"></a>Specifies the time when a protected instance was created.</p>
    <p id="p1078620139012"><a name="p1078620139012"></a><a name="p1078620139012"></a>The default format is as follows: "yyyy-MM-dd HH:mm:ss.SSS", for example, <strong id="b1618132120140"><a name="b1618132120140"></a><a name="b1618132120140"></a>2019-04-01 12:00:00.000</strong>.</p>
    </td>
    </tr>
    <tr id="row757514214419"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p1937717234231"><a name="p1937717234231"></a><a name="p1937717234231"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.34%" headers="mcps1.2.4.1.2 "><p id="p1377323132313"><a name="p1377323132313"></a><a name="p1377323132313"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.59%" headers="mcps1.2.4.1.3 "><p id="p1937716237235"><a name="p1937716237235"></a><a name="p1937716237235"></a>Specifies the time when a protected instance was updated.</p>
    <p id="p1942786173519"><a name="p1942786173519"></a><a name="p1942786173519"></a>The default format is as follows: "yyyy-MM-dd HH:mm:ss.SSS", for example, <strong id="b810333131517"><a name="b810333131517"></a><a name="b810333131517"></a>2019-04-01 12:00:00.000</strong>.</p>
    </td>
    </tr>
    <tr id="row08503318414"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p10235944142418"><a name="p10235944142418"></a><a name="p10235944142418"></a>priority_station</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.34%" headers="mcps1.2.4.1.2 "><p id="p10235154410245"><a name="p10235154410245"></a><a name="p10235154410245"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.59%" headers="mcps1.2.4.1.3 "><p id="p382553192519"><a name="p382553192519"></a><a name="p382553192519"></a>Specifies the current production site AZ of the protection group containing the protected instance.</p>
    <a name="ul782135312518"></a><a name="ul782135312518"></a><ul id="ul782135312518"><li><strong id="b17653238122310"><a name="b17653238122310"></a><a name="b17653238122310"></a>source</strong>: indicates that the current production site AZ is the <strong id="b1665418386237"><a name="b1665418386237"></a><a name="b1665418386237"></a>source_availability_zone</strong> value.</li><li><strong id="b1278154814238"><a name="b1278154814238"></a><a name="b1278154814238"></a>target</strong>: indicates that the current production site AZ is the <strong id="b187838483234"><a name="b187838483234"></a><a name="b187838483234"></a>target_availability_zone</strong> value.</li></ul>
    </td>
    </tr>
    <tr id="row1974415342560"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p1374517342565"><a name="p1374517342565"></a><a name="p1374517342565"></a>attachment</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.34%" headers="mcps1.2.4.1.2 "><p id="p474543475616"><a name="p474543475616"></a><a name="p474543475616"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.59%" headers="mcps1.2.4.1.3 "><p id="p1674513345564"><a name="p1674513345564"></a><a name="p1674513345564"></a>Specifies the attached replication pairs.</p>
    <p id="p94849197376"><a name="p94849197376"></a><a name="p94849197376"></a>For details, see <a href="#table1575342962014">Table 2</a>.</p>
    </td>
    </tr>
    <tr id="row1511716165613"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p198281231145613"><a name="p198281231145613"></a><a name="p198281231145613"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.34%" headers="mcps1.2.4.1.2 "><p id="p20771154912569"><a name="p20771154912569"></a><a name="p20771154912569"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.59%" headers="mcps1.2.4.1.3 "><p id="p15241635617"><a name="p15241635617"></a><a name="p15241635617"></a>Specifies the tag list.</p>
    <p id="p139197593379"><a name="p139197593379"></a><a name="p139197593379"></a>For details, see <a href="#table12339146338">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="row1347091555717"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p6472615185719"><a name="p6472615185719"></a><a name="p6472615185719"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.34%" headers="mcps1.2.4.1.2 "><p id="p10709144620575"><a name="p10709144620575"></a><a name="p10709144620575"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.59%" headers="mcps1.2.4.1.3 "><p id="p1786654614533"><a name="p1786654614533"></a><a name="p1786654614533"></a>Specifies the metadata of a protected instance.</p>
    <p id="p370974645720"><a name="p370974645720"></a><a name="p370974645720"></a>For details, see <a href="#table8582730112710">Table 4</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2** **attachment**  field description

    <a name="table1575342962014"></a>
    <table><thead align="left"><tr id="row157542290208"><th class="cellrowborder" valign="top" width="29.062906290629066%" id="mcps1.2.4.1.1"><p id="p167541029122015"><a name="p167541029122015"></a><a name="p167541029122015"></a><strong id="b9456951154117"><a name="b9456951154117"></a><a name="b9456951154117"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.42174217421742%" id="mcps1.2.4.1.2"><p id="p77541429102015"><a name="p77541429102015"></a><a name="p77541429102015"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.51535153515352%" id="mcps1.2.4.1.3"><p id="p13754172912015"><a name="p13754172912015"></a><a name="p13754172912015"></a><strong id="b1982665274115"><a name="b1982665274115"></a><a name="b1982665274115"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row57541029192012"><td class="cellrowborder" valign="top" width="29.062906290629066%" headers="mcps1.2.4.1.1 "><p id="p197541729112016"><a name="p197541729112016"></a><a name="p197541729112016"></a>replication</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.42174217421742%" headers="mcps1.2.4.1.2 "><p id="p197546293203"><a name="p197546293203"></a><a name="p197546293203"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.51535153515352%" headers="mcps1.2.4.1.3 "><p id="p11754162962013"><a name="p11754162962013"></a><a name="p11754162962013"></a>Specifies the ID of a replication pair.</p>
    </td>
    </tr>
    <tr id="row7754122902018"><td class="cellrowborder" valign="top" width="29.062906290629066%" headers="mcps1.2.4.1.1 "><p id="p17754152962012"><a name="p17754152962012"></a><a name="p17754152962012"></a>device</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.42174217421742%" headers="mcps1.2.4.1.2 "><p id="p1754132902020"><a name="p1754132902020"></a><a name="p1754132902020"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.51535153515352%" headers="mcps1.2.4.1.3 "><p id="p97541729162014"><a name="p97541729162014"></a><a name="p97541729162014"></a>Specifies the device name.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **tags**  field description

    <a name="table12339146338"></a>
    <table><thead align="left"><tr id="row43396416331"><th class="cellrowborder" valign="top" width="29.01290129012902%" id="mcps1.2.4.1.1"><p id="p13396473310"><a name="p13396473310"></a><a name="p13396473310"></a><strong id="b8226188154419"><a name="b8226188154419"></a><a name="b8226188154419"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.401740174017398%" id="mcps1.2.4.1.2"><p id="p7339247336"><a name="p7339247336"></a><a name="p7339247336"></a><strong id="b5715144294014"><a name="b5715144294014"></a><a name="b5715144294014"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.58535853585359%" id="mcps1.2.4.1.3"><p id="p7339343338"><a name="p7339343338"></a><a name="p7339343338"></a><strong id="b57498420443"><a name="b57498420443"></a><a name="b57498420443"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row43406415336"><td class="cellrowborder" valign="top" width="29.01290129012902%" headers="mcps1.2.4.1.1 "><p id="p7340204133310"><a name="p7340204133310"></a><a name="p7340204133310"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.401740174017398%" headers="mcps1.2.4.1.2 "><p id="p1334016412332"><a name="p1334016412332"></a><a name="p1334016412332"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.58535853585359%" headers="mcps1.2.4.1.3 "><p id="p9340164163314"><a name="p9340164163314"></a><a name="p9340164163314"></a>Specifies the tag key.</p>
    </td>
    </tr>
    <tr id="row113401848337"><td class="cellrowborder" valign="top" width="29.01290129012902%" headers="mcps1.2.4.1.1 "><p id="p193401449333"><a name="p193401449333"></a><a name="p193401449333"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.401740174017398%" headers="mcps1.2.4.1.2 "><p id="p12340546334"><a name="p12340546334"></a><a name="p12340546334"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.58535853585359%" headers="mcps1.2.4.1.3 "><p id="p1234015416337"><a name="p1234015416337"></a><a name="p1234015416337"></a>Specifies the tag value.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  Field  **metadata**  description

    <a name="table8582730112710"></a>
    <table><thead align="left"><tr id="row13583230202711"><th class="cellrowborder" valign="top" width="29.01290129012902%" id="mcps1.2.4.1.1"><p id="p18958174419296"><a name="p18958174419296"></a><a name="p18958174419296"></a><strong id="b3445153418161"><a name="b3445153418161"></a><a name="b3445153418161"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.64176417641764%" id="mcps1.2.4.1.2"><p id="p12958154420296"><a name="p12958154420296"></a><a name="p12958154420296"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.34533453345335%" id="mcps1.2.4.1.3"><p id="p395816448297"><a name="p395816448297"></a><a name="p395816448297"></a><strong id="b930512361165"><a name="b930512361165"></a><a name="b930512361165"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6583930152715"><td class="cellrowborder" valign="top" width="29.01290129012902%" headers="mcps1.2.4.1.1 "><p id="p1558353082720"><a name="p1558353082720"></a><a name="p1558353082720"></a>__system__frozen</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.64176417641764%" headers="mcps1.2.4.1.2 "><p id="p11583730102710"><a name="p11583730102710"></a><a name="p11583730102710"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.34533453345335%" headers="mcps1.2.4.1.3 "><p id="p958313303271"><a name="p958313303271"></a><a name="p958313303271"></a>Specifies whether the resource is frozen.</p>
    <a name="ul529114370311"></a><a name="ul529114370311"></a><ul id="ul529114370311"><li><strong id="b12328157201913"><a name="b12328157201913"></a><a name="b12328157201913"></a>true</strong>: indicates that the resource is frozen.</li><li>Empty: indicates that the resource is not frozen.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "protected_instances": [
            {
                "id": "67a2cc7e-fb87-41a8-ba28-9c032abcaee1",
                "name": "protected_instance_xff",
                "description": "protected_instance_xff",
                "server_group_id": "21d65fa4-430e-4761-b9ad-4e27364f874c",
                "status": "available",
                "progress": 0,
                "source_server": "d1e8e8a7-ae6f-4f40-bead-20093976961e",
                "target_server": "9bad52b9-ca5a-4274-ba9e-3c8ca9843fa1",
                "created_at": "2018-11-06 11:09:25.861",
                "updated_at": "2018-11-06 11:12:11.716",
                "priority_station": "source",
                "attachment": [
                    {
                        "replication": "08d6b5a0-9a12-4263-a468-30d71d10498c",
                        "device": "/dev/vdb"
                    },
                    {
                        "replication": "4c332757-dc77-458d-9883-03d701cde2f2",
                        "device": "/dev/vda"
                    }
                ],
                "tags": [
                    {                   
                       "key": "aaaaaaa",                   
                       "value": "01234567889"               
                     },                
                    {                   
                        "key": "ffffff",                   
                        "value": "dddd"
                    }
                ],
                "metadata": {} 
            },
            {
                "id": "50f5091e-9e9e-473c-a932-2a2cbcbeb1ff",
                "name": "ecs_sdrs_test",
                "description": "1111",
                "server_group_id": "943c7d15-0371-4b89-b1a6-db1ef35c9263",
                "status": "protected",
                "progress": 100,
                "source_server": "5fb92d6c-b0cb-46c9-824b-b90ec5500ae6",
                "target_server": "c6c0ff54-fa1f-43ef-9ccc-1774e40c8745",
                "created_at": "2018-11-06 09:27:52.258",
                "updated_at": "2018-11-06 09:44:59.853",
                "priority_station": "target",
                "attachment": [
                    {
                        "replication": "6568f7c4-0510-4f39-929d-8ffccbd4fd47",
                        "device": "/dev/vda"
                    }
                ],
                "tags": [
                    {                   
                         "key": "aaaaaaa",                   
                         "value": "01234567889"               
                    },                
                    {                   
                         "key": "ffffff",                   
                         "value": "dddd"                }
                ],
                "metadata": {} 
            }
        ],
        "count": 2
    }
    ```

    Or

    ```
    { 
         "error": { 
             "message": "XXXX",  
             "code": "XXX" 
         } 
     }
    ```

    In this example,  **error**  represents a general error, including  **badrequest**  \(shown below\) and  **itemNotFound**.

    ```
    { 
         "badrequest": { 
             "message": "XXXX",  
             "code": "XXX" 
         } 
     }
    ```


## Returned Values<a name="en-us_topic_0079693002_section60507121"></a>

-   Normal

    <a name="sdrs_05_0101_table4315991194956"></a>
    <table><thead align="left"><tr id="sdrs_05_0101_row2336641294956"><th class="cellrowborder" valign="top" width="42.59%" id="mcps1.1.3.1.1"><p id="sdrs_05_0101_p1363125894956"><a name="sdrs_05_0101_p1363125894956"></a><a name="sdrs_05_0101_p1363125894956"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.410000000000004%" id="mcps1.1.3.1.2"><p id="sdrs_05_0101_p3039012494956"><a name="sdrs_05_0101_p3039012494956"></a><a name="sdrs_05_0101_p3039012494956"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="sdrs_05_0101_row507566794956"><td class="cellrowborder" valign="top" width="42.59%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p847584694956"><a name="sdrs_05_0101_p847584694956"></a><a name="sdrs_05_0101_p847584694956"></a>200</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.410000000000004%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p1545496394956"><a name="sdrs_05_0101_p1545496394956"></a><a name="sdrs_05_0101_p1545496394956"></a>The server has accepted the request.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    <a name="sdrs_05_0101_table22458872203835"></a>
    <table><thead align="left"><tr id="sdrs_05_0101_row35704554203835"><th class="cellrowborder" valign="top" width="43.419999999999995%" id="mcps1.1.3.1.1"><p id="sdrs_05_0101_p6387753203835"><a name="sdrs_05_0101_p6387753203835"></a><a name="sdrs_05_0101_p6387753203835"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.58%" id="mcps1.1.3.1.2"><p id="sdrs_05_0101_p47646009203835"><a name="sdrs_05_0101_p47646009203835"></a><a name="sdrs_05_0101_p47646009203835"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="sdrs_05_0101_row34121538203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p12381163203835"><a name="sdrs_05_0101_p12381163203835"></a><a name="sdrs_05_0101_p12381163203835"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p63350108203835"><a name="sdrs_05_0101_p63350108203835"></a><a name="sdrs_05_0101_p63350108203835"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row33280063203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p11330608203835"><a name="sdrs_05_0101_p11330608203835"></a><a name="sdrs_05_0101_p11330608203835"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p45364094203835"><a name="sdrs_05_0101_p45364094203835"></a><a name="sdrs_05_0101_p45364094203835"></a>You must enter a username and the password to access the requested page.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row5623667203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p52863895203835"><a name="sdrs_05_0101_p52863895203835"></a><a name="sdrs_05_0101_p52863895203835"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p54117066203835"><a name="sdrs_05_0101_p54117066203835"></a><a name="sdrs_05_0101_p54117066203835"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row17291554203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p58438642203835"><a name="sdrs_05_0101_p58438642203835"></a><a name="sdrs_05_0101_p58438642203835"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p35909542203835"><a name="sdrs_05_0101_p35909542203835"></a><a name="sdrs_05_0101_p35909542203835"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row54750425203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p5599455203835"><a name="sdrs_05_0101_p5599455203835"></a><a name="sdrs_05_0101_p5599455203835"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p50902717203835"><a name="sdrs_05_0101_p50902717203835"></a><a name="sdrs_05_0101_p50902717203835"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row55471277203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p63988484203835"><a name="sdrs_05_0101_p63988484203835"></a><a name="sdrs_05_0101_p63988484203835"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p15684678203835"><a name="sdrs_05_0101_p15684678203835"></a><a name="sdrs_05_0101_p15684678203835"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row6944380203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p25623884203835"><a name="sdrs_05_0101_p25623884203835"></a><a name="sdrs_05_0101_p25623884203835"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p62268733203835"><a name="sdrs_05_0101_p62268733203835"></a><a name="sdrs_05_0101_p62268733203835"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row23547689203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p28314670203835"><a name="sdrs_05_0101_p28314670203835"></a><a name="sdrs_05_0101_p28314670203835"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p11786919203835"><a name="sdrs_05_0101_p11786919203835"></a><a name="sdrs_05_0101_p11786919203835"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row38973411203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p2729702203835"><a name="sdrs_05_0101_p2729702203835"></a><a name="sdrs_05_0101_p2729702203835"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p19779281203835"><a name="sdrs_05_0101_p19779281203835"></a><a name="sdrs_05_0101_p19779281203835"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row43795805203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p57799353203835"><a name="sdrs_05_0101_p57799353203835"></a><a name="sdrs_05_0101_p57799353203835"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p51235984203835"><a name="sdrs_05_0101_p51235984203835"></a><a name="sdrs_05_0101_p51235984203835"></a>Failed to complete the request because of a service error.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row58470678203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p38504500203835"><a name="sdrs_05_0101_p38504500203835"></a><a name="sdrs_05_0101_p38504500203835"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p31856770203835"><a name="sdrs_05_0101_p31856770203835"></a><a name="sdrs_05_0101_p31856770203835"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row18275474203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p3918444203835"><a name="sdrs_05_0101_p3918444203835"></a><a name="sdrs_05_0101_p3918444203835"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p48958538203835"><a name="sdrs_05_0101_p48958538203835"></a><a name="sdrs_05_0101_p48958538203835"></a>Failed to complete the request because the server receives an invalid response from an upstream server.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row37973662203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p55967806203835"><a name="sdrs_05_0101_p55967806203835"></a><a name="sdrs_05_0101_p55967806203835"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p37098455203835"><a name="sdrs_05_0101_p37098455203835"></a><a name="sdrs_05_0101_p37098455203835"></a>Failed to complete the request because the system is unavailable.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row65450640203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p67010448203835"><a name="sdrs_05_0101_p67010448203835"></a><a name="sdrs_05_0101_p67010448203835"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p59137180203835"><a name="sdrs_05_0101_p59137180203835"></a><a name="sdrs_05_0101_p59137180203835"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


