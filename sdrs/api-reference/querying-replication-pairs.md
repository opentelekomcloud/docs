# Querying Replication Pairs<a name="sdrs_05_0603"></a>

## Function<a name="en-us_topic_0079693002_section34649765"></a>

This API is used to query all replication pairs in a specified protection group. If you do not specify the protection group, the system lists all the replication pairs of the tenant.

## Constraints and Limitations<a name="section8242191544111"></a>

None

## URI<a name="en-us_topic_0079693002_section39390935"></a>

-   URI format

    GET /v1/\{project\_id\}/replications

-   Parameter description

    <a name="en-us_topic_0079693002_table63321005"></a>
    <table><thead align="left"><tr id="en-us_topic_0079693002_row37593218"><th class="cellrowborder" valign="top" width="17.82178217821782%" id="mcps1.1.5.1.1"><p id="p7266170103719"><a name="p7266170103719"></a><a name="p7266170103719"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.82178217821782%" id="mcps1.1.5.1.2"><p id="p19266120123714"><a name="p19266120123714"></a><a name="p19266120123714"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.85148514851485%" id="mcps1.1.5.1.3"><p id="p19266208374"><a name="p19266208374"></a><a name="p19266208374"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="49.504950495049506%" id="mcps1.1.5.1.4"><p id="p6266120143715"><a name="p6266120143715"></a><a name="p6266120143715"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0079693002_row29123463"><td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.5.1.1 "><p id="p62669019379"><a name="p62669019379"></a><a name="p62669019379"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.5.1.2 "><p id="p72666016379"><a name="p72666016379"></a><a name="p72666016379"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.1.5.1.3 "><p id="p82664043719"><a name="p82664043719"></a><a name="p82664043719"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.504950495049506%" headers="mcps1.1.5.1.4 "><p id="p102661083713"><a name="p102661083713"></a><a name="p102661083713"></a>Specifies the project ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   **Request filter**  field description

    <a name="en-us_topic_0079693002_table54932709"></a>
    <table><thead align="left"><tr id="en-us_topic_0079693002_row41882373"><th class="cellrowborder" valign="top" width="19.68%" id="mcps1.1.5.1.1"><p id="en-us_topic_0079693002_p8696081161227"><a name="en-us_topic_0079693002_p8696081161227"></a><a name="en-us_topic_0079693002_p8696081161227"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.29%" id="mcps1.1.5.1.2"><p id="en-us_topic_0079693002_p33293980161227"><a name="en-us_topic_0079693002_p33293980161227"></a><a name="en-us_topic_0079693002_p33293980161227"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.6%" id="mcps1.1.5.1.3"><p id="en-us_topic_0079693002_p12457872161227"><a name="en-us_topic_0079693002_p12457872161227"></a><a name="en-us_topic_0079693002_p12457872161227"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="49.43%" id="mcps1.1.5.1.4"><p id="en-us_topic_0079693002_p2454675161227"><a name="en-us_topic_0079693002_p2454675161227"></a><a name="en-us_topic_0079693002_p2454675161227"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0079693002_row27990155"><td class="cellrowborder" valign="top" width="19.68%" headers="mcps1.1.5.1.1 "><p id="p1373492812595"><a name="p1373492812595"></a><a name="p1373492812595"></a>server_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.29%" headers="mcps1.1.5.1.2 "><p id="p1446373253819"><a name="p1446373253819"></a><a name="p1446373253819"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.6%" headers="mcps1.1.5.1.3 "><p id="p124641232133816"><a name="p124641232133816"></a><a name="p124641232133816"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.43%" headers="mcps1.1.5.1.4 "><p id="p174641832183813"><a name="p174641832183813"></a><a name="p174641832183813"></a>Specifies the ID of a protection group.</p>
    <p id="p153591912192"><a name="p153591912192"></a><a name="p153591912192"></a>You can obtain this value by calling the API described in <a href="querying-protection-groups.md">Querying Protection Groups</a>.</p>
    </td>
    </tr>
    <tr id="row93491834143716"><td class="cellrowborder" valign="top" width="19.68%" headers="mcps1.1.5.1.1 "><p id="p644423512379"><a name="p644423512379"></a><a name="p644423512379"></a>server_group_ids</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.29%" headers="mcps1.1.5.1.2 "><p id="p1344463513712"><a name="p1344463513712"></a><a name="p1344463513712"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.6%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0098680634_p9113191413128"><a name="en-us_topic_0098680634_p9113191413128"></a><a name="en-us_topic_0098680634_p9113191413128"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.43%" headers="mcps1.1.5.1.4 "><p id="p85241852143216"><a name="p85241852143216"></a><a name="p85241852143216"></a>Specifies the protection group ID list. The value is in the following format: server_group_ids=['server_group_id1','server_group_id2',...,'server_group_idx']. Convert it using URL encoding.</p>
    <a name="ul10888401339"></a><a name="ul10888401339"></a><ul id="ul10888401339"><li>All the replication pairs with valid <strong id="b16656812194617"><a name="b16656812194617"></a><a name="b16656812194617"></a>server_group_id</strong> in <strong id="b13656121215467"><a name="b13656121215467"></a><a name="b13656121215467"></a>server_group_ids</strong> are returned.</li><li>The replication pairs of a maximum of 30 <strong id="b683783394611"><a name="b683783394611"></a><a name="b683783394611"></a>server_group_id</strong> values can be queried.</li><li>If parameters <strong id="b1958594464614"><a name="b1958594464614"></a><a name="b1958594464614"></a>server_group_id</strong> and <strong id="b1158664424612"><a name="b1158664424612"></a><a name="b1158664424612"></a>server_group_ids</strong> are both specified in the request, <strong id="b1658764444619"><a name="b1658764444619"></a><a name="b1658764444619"></a>server_group_id</strong> will be ignored.</li></ul>
    </td>
    </tr>
    <tr id="row42471257594"><td class="cellrowborder" valign="top" width="19.68%" headers="mcps1.1.5.1.1 "><p id="p1573722810594"><a name="p1573722810594"></a><a name="p1573722810594"></a>protected_instance_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.29%" headers="mcps1.1.5.1.2 "><p id="p1464183273817"><a name="p1464183273817"></a><a name="p1464183273817"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.6%" headers="mcps1.1.5.1.3 "><p id="p64647326381"><a name="p64647326381"></a><a name="p64647326381"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.43%" headers="mcps1.1.5.1.4 "><p id="p7464103283816"><a name="p7464103283816"></a><a name="p7464103283816"></a>Specifies the ID of a protected instance.</p>
    <p id="p224775319192"><a name="p224775319192"></a><a name="p224775319192"></a>You can obtain this value by calling the API described in <a href="querying-protected-instances.md">Querying Protected Instances</a>.</p>
    </td>
    </tr>
    <tr id="row131583917377"><td class="cellrowborder" valign="top" width="19.68%" headers="mcps1.1.5.1.1 "><p id="p1023184073717"><a name="p1023184073717"></a><a name="p1023184073717"></a>protected_instance_ids</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.29%" headers="mcps1.1.5.1.2 "><p id="p22314405374"><a name="p22314405374"></a><a name="p22314405374"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.6%" headers="mcps1.1.5.1.3 "><p id="p1843012811381"><a name="p1843012811381"></a><a name="p1843012811381"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.43%" headers="mcps1.1.5.1.4 "><p id="p86202017183412"><a name="p86202017183412"></a><a name="p86202017183412"></a>Specifies the protected instance ID list. The value is in the following format: protected_instance_ids=['protected_instance_id1','protected_instance_id2',...,'protected_instance_idx']. Convert it using URL encoding.</p>
    <a name="ul413418239345"></a><a name="ul413418239345"></a><ul id="ul413418239345"><li>All the replication pairs with valid <strong id="b11221115364610"><a name="b11221115364610"></a><a name="b11221115364610"></a>protected_instance_id</strong> in <strong id="b522216538465"><a name="b522216538465"></a><a name="b522216538465"></a>protected_instance_ids</strong> are returned.</li><li>The replication pairs of a maximum of 30 <strong id="b17861910134712"><a name="b17861910134712"></a><a name="b17861910134712"></a>protected_instance_id</strong> values can be queried.</li><li>If parameters <strong id="b1015512177476"><a name="b1015512177476"></a><a name="b1015512177476"></a>protected_instance_id</strong> and <strong id="b415681744713"><a name="b415681744713"></a><a name="b415681744713"></a>protected_instance_ids</strong> are both specified in the request, <strong id="b6157617174714"><a name="b6157617174714"></a><a name="b6157617174714"></a>protected_instance_id</strong> will be ignored.</li></ul>
    </td>
    </tr>
    <tr id="row119592104596"><td class="cellrowborder" valign="top" width="19.68%" headers="mcps1.1.5.1.1 "><p id="p117381528165919"><a name="p117381528165919"></a><a name="p117381528165919"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.29%" headers="mcps1.1.5.1.2 "><p id="p19464193263817"><a name="p19464193263817"></a><a name="p19464193263817"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.6%" headers="mcps1.1.5.1.3 "><p id="p13464632163811"><a name="p13464632163811"></a><a name="p13464632163811"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.43%" headers="mcps1.1.5.1.4 "><p id="p5464532173820"><a name="p5464532173820"></a><a name="p5464532173820"></a>Specifies the name of a replication pair. Fuzzy search is supported.</p>
    </td>
    </tr>
    <tr id="row1911351315593"><td class="cellrowborder" valign="top" width="19.68%" headers="mcps1.1.5.1.1 "><p id="p373862885918"><a name="p373862885918"></a><a name="p373862885918"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.29%" headers="mcps1.1.5.1.2 "><p id="p346414321380"><a name="p346414321380"></a><a name="p346414321380"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.6%" headers="mcps1.1.5.1.3 "><p id="p12464143213384"><a name="p12464143213384"></a><a name="p12464143213384"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.43%" headers="mcps1.1.5.1.4 "><p id="p64641232133812"><a name="p64641232133812"></a><a name="p64641232133812"></a>Specifies the status of a replication pair.</p>
    <p id="p1423313322464"><a name="p1423313322464"></a><a name="p1423313322464"></a>For details, see <a href="replication-pair-status.md">Replication Pair Status</a>.</p>
    </td>
    </tr>
    <tr id="row11106615185911"><td class="cellrowborder" valign="top" width="19.68%" headers="mcps1.1.5.1.1 "><p id="p9738182814599"><a name="p9738182814599"></a><a name="p9738182814599"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.29%" headers="mcps1.1.5.1.2 "><p id="p8464332193818"><a name="p8464332193818"></a><a name="p8464332193818"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.6%" headers="mcps1.1.5.1.3 "><p id="p3464203293818"><a name="p3464203293818"></a><a name="p3464203293818"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.43%" headers="mcps1.1.5.1.4 "><p id="p1446453218380"><a name="p1446453218380"></a><a name="p1446453218380"></a>Specifies the maximum number of results returned each time. The value is a positive integer from 0 to 1000. The default value is <strong id="b842352706161435"><a name="b842352706161435"></a><a name="b842352706161435"></a>1000</strong>.</p>
    </td>
    </tr>
    <tr id="row525231713592"><td class="cellrowborder" valign="top" width="19.68%" headers="mcps1.1.5.1.1 "><p id="p19739122875919"><a name="p19739122875919"></a><a name="p19739122875919"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.29%" headers="mcps1.1.5.1.2 "><p id="p1446517329384"><a name="p1446517329384"></a><a name="p1446517329384"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.6%" headers="mcps1.1.5.1.3 "><p id="p346523217384"><a name="p346523217384"></a><a name="p346523217384"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.43%" headers="mcps1.1.5.1.4 "><p id="p7465193223814"><a name="p7465193223814"></a><a name="p7465193223814"></a>Specifies the offset of each request. The default value is <strong id="b74201644142916"><a name="b74201644142916"></a><a name="b74201644142916"></a>0</strong>. The value must be a number and cannot be negative.</p>
    </td>
    </tr>
    <tr id="row188811982614"><td class="cellrowborder" valign="top" width="19.68%" headers="mcps1.1.5.1.1 "><p id="p1315305251611"><a name="p1315305251611"></a><a name="p1315305251611"></a>query_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.29%" headers="mcps1.1.5.1.2 "><p id="p41537522160"><a name="p41537522160"></a><a name="p41537522160"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.6%" headers="mcps1.1.5.1.3 "><p id="p18153205216167"><a name="p18153205216167"></a><a name="p18153205216167"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.43%" headers="mcps1.1.5.1.4 "><p id="p1415405216161"><a name="p1415405216161"></a><a name="p1415405216161"></a>Specifies the query type.</p>
    <a name="ul179222514136"></a><a name="ul179222514136"></a><ul id="ul179222514136"><li>To query replication pairs in the abnormal status, set <strong id="b11545115712231"><a name="b11545115712231"></a><a name="b11545115712231"></a>query_type</strong> to <strong id="b17269471248"><a name="b17269471248"></a><a name="b17269471248"></a>status_abnormal</strong>.</li><li>Otherwise, set <strong id="b71722322261"><a name="b71722322261"></a><a name="b71722322261"></a>query_type</strong> to general or leave it empty.</li></ul>
    </td>
    </tr>
    <tr id="row445301418261"><td class="cellrowborder" valign="top" width="19.68%" headers="mcps1.1.5.1.1 "><p id="p13773157191611"><a name="p13773157191611"></a><a name="p13773157191611"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.29%" headers="mcps1.1.5.1.2 "><p id="p3773957151611"><a name="p3773957151611"></a><a name="p3773957151611"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.6%" headers="mcps1.1.5.1.3 "><p id="p1177518571167"><a name="p1177518571167"></a><a name="p1177518571167"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.43%" headers="mcps1.1.5.1.4 "><p id="p1577510578162"><a name="p1577510578162"></a><a name="p1577510578162"></a>Specifies the current production site of the protection group containing the replication pair.</p>
    <p id="p536413384228"><a name="p536413384228"></a><a name="p536413384228"></a>You can obtain this value by calling the API described in <a href="querying-an-active-active-domain.md">Querying an Active-Active Domain</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section11251204264911"></a>

-   Request parameters

    None

-   Example request

    ```
    https://{Endpoint}/v1/{project_id}/replications?server_group_ids=%5b%2221d65fa4-430e-4761-b9ad-4e27364f874c%22%2c%22943c7d15-0371-4b89-b1a6-db1ef35c9263&status=available
    ```

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >Use URL encoding for  **server\_group\_ids**  or  **protected\_instance\_ids**.  


## Response<a name="en-us_topic_0079693002_section36549175"></a>

-   Parameter description

    <a name="table030131120410"></a>
    <table><thead align="left"><tr id="row39715118415"><th class="cellrowborder" valign="top" width="29.07%" id="mcps1.1.4.1.1"><p id="p89711112419"><a name="p89711112419"></a><a name="p89711112419"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.44%" id="mcps1.1.4.1.2"><p id="p99701120411"><a name="p99701120411"></a><a name="p99701120411"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.49%" id="mcps1.1.4.1.3"><p id="p597101124111"><a name="p597101124111"></a><a name="p597101124111"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row497161154114"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.1.4.1.1 "><p id="p19812113418"><a name="p19812113418"></a><a name="p19812113418"></a>replications</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.1.4.1.2 "><p id="p159881119412"><a name="p159881119412"></a><a name="p159881119412"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.1.4.1.3 "><p id="p79801116418"><a name="p79801116418"></a><a name="p79801116418"></a>Specifies the information about replication pairs.</p>
    <p id="p18992205304911"><a name="p18992205304911"></a><a name="p18992205304911"></a>For details, see <a href="#table111111245194113">Table 1</a>.</p>
    </td>
    </tr>
    <tr id="row1989116419"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.1.4.1.1 "><p id="p7986118412"><a name="p7986118412"></a><a name="p7986118412"></a>count</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.1.4.1.2 "><p id="p1898121111415"><a name="p1898121111415"></a><a name="p1898121111415"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.1.4.1.3 "><p id="p1398141134116"><a name="p1398141134116"></a><a name="p1398141134116"></a>Specifies the number of replication pairs.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  1** **replications**  field description

    <a name="table111111245194113"></a>
    <table><thead align="left"><tr id="row10237745184119"><th class="cellrowborder" valign="top" width="29.07%" id="mcps1.2.4.1.1"><p id="p142371645164118"><a name="p142371645164118"></a><a name="p142371645164118"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.44%" id="mcps1.2.4.1.2"><p id="p6237194510418"><a name="p6237194510418"></a><a name="p6237194510418"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.49%" id="mcps1.2.4.1.3"><p id="p1123794514419"><a name="p1123794514419"></a><a name="p1123794514419"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row15237645194116"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p9237445124113"><a name="p9237445124113"></a><a name="p9237445124113"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p72371945204115"><a name="p72371945204115"></a><a name="p72371945204115"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p1923713455416"><a name="p1923713455416"></a><a name="p1923713455416"></a>Specifies the ID of a replication pair.</p>
    </td>
    </tr>
    <tr id="row5237645124112"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p52377454412"><a name="p52377454412"></a><a name="p52377454412"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p823754594113"><a name="p823754594113"></a><a name="p823754594113"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p1823744514412"><a name="p1823744514412"></a><a name="p1823744514412"></a>Specifies the name of a replication pair.</p>
    </td>
    </tr>
    <tr id="row6237154519416"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p1423744584110"><a name="p1423744584110"></a><a name="p1423744584110"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p1123720453418"><a name="p1123720453418"></a><a name="p1123720453418"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p1223724554115"><a name="p1223724554115"></a><a name="p1223724554115"></a>Specifies the description of a replication pair.</p>
    </td>
    </tr>
    <tr id="row1675624210366"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p182391945104110"><a name="p182391945104110"></a><a name="p182391945104110"></a>replication_model</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p19239104518418"><a name="p19239104518418"></a><a name="p19239104518418"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p823974516416"><a name="p823974516416"></a><a name="p823974516416"></a>Specifies the replication mode of a replication pair. The default value is <strong id="b154591346194619"><a name="b154591346194619"></a><a name="b154591346194619"></a>hypermetro</strong>, indicating synchronous replication.</p>
    </td>
    </tr>
    <tr id="row12237194504115"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p1723713459419"><a name="p1723713459419"></a><a name="p1723713459419"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p10237104514417"><a name="p10237104514417"></a><a name="p10237104514417"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p14989153217341"><a name="p14989153217341"></a><a name="p14989153217341"></a>Specifies the status of a replication pair.</p>
    <p id="p698263217347"><a name="p698263217347"></a><a name="p698263217347"></a>For details, see <a href="replication-pair-status.md">Replication Pair Status</a>.</p>
    </td>
    </tr>
    <tr id="row18552444124215"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p112410453412"><a name="p112410453412"></a><a name="p112410453412"></a>progress</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p32418456411"><a name="p32418456411"></a><a name="p32418456411"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p192417459418"><a name="p192417459418"></a><a name="p192417459418"></a>Specifies the synchronization progress of a replication pair.</p>
    <p id="p12411945134110"><a name="p12411945134110"></a><a name="p12411945134110"></a>Unit: %</p>
    </td>
    </tr>
    <tr id="row52101819483"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p1931012731819"><a name="p1931012731819"></a><a name="p1931012731819"></a>replication_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p19589849375"><a name="p19589849375"></a><a name="p19589849375"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p17310171185"><a name="p17310171185"></a><a name="p17310171185"></a>Specifies the data synchronization status.</p>
    <a name="ul1231014717183"></a><a name="ul1231014717183"></a><ul id="ul1231014717183"><li><strong id="b45671721496"><a name="b45671721496"></a><a name="b45671721496"></a>active</strong>: Data has been synchronized.</li><li><strong id="b1479811519913"><a name="b1479811519913"></a><a name="b1479811519913"></a>inactive</strong>: Data is not synchronized.</li><li><strong id="b31301243984"><a name="b31301243984"></a><a name="b31301243984"></a>copying</strong>: Data is being synchronized.</li><li><strong id="b873942274910"><a name="b873942274910"></a><a name="b873942274910"></a>active-stopped</strong>: Data synchronization is stopped.</li></ul>
    </td>
    </tr>
    <tr id="row1295224218488"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p19238045144111"><a name="p19238045144111"></a><a name="p19238045144111"></a>attachment</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p123816451416"><a name="p123816451416"></a><a name="p123816451416"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p15238204518415"><a name="p15238204518415"></a><a name="p15238204518415"></a>Specifies the device name.</p>
    <p id="p148224382504"><a name="p148224382504"></a><a name="p148224382504"></a>For details, see <a href="#table47791613195012">Table 2</a>.</p>
    </td>
    </tr>
    <tr id="row13797144154914"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p1324114504119"><a name="p1324114504119"></a><a name="p1324114504119"></a>server_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p12241645174111"><a name="p12241645174111"></a><a name="p12241645174111"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p196131933102220"><a name="p196131933102220"></a><a name="p196131933102220"></a>Specifies the ID of a protection group.</p>
    </td>
    </tr>
    <tr id="row523724534116"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p102371745104116"><a name="p102371745104116"></a><a name="p102371745104116"></a>volume_ids</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p6238174513419"><a name="p6238174513419"></a><a name="p6238174513419"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p3238945194113"><a name="p3238945194113"></a><a name="p3238945194113"></a>Specifies the ID of the disk used to create a replication pair.</p>
    </td>
    </tr>
    <tr id="row18238745204115"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p11520200202317"><a name="p11520200202317"></a><a name="p11520200202317"></a>priority_station</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p052080132312"><a name="p052080132312"></a><a name="p052080132312"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p152013017236"><a name="p152013017236"></a><a name="p152013017236"></a>Specifies the current production site AZ of the protection group containing the replication pair.</p>
    <a name="ul9520190172318"></a><a name="ul9520190172318"></a><ul id="ul9520190172318"><li><strong id="b38099293294"><a name="b38099293294"></a><a name="b38099293294"></a>source</strong>: indicates that the current production site AZ is the <strong id="b081082932918"><a name="b081082932918"></a><a name="b081082932918"></a>source_availability_zone</strong> value.</li><li><strong id="b14382203442912"><a name="b14382203442912"></a><a name="b14382203442912"></a>target</strong>: indicates that the current production site AZ is the <strong id="b138333462919"><a name="b138333462919"></a><a name="b138333462919"></a>target_availability_zone</strong> value.</li></ul>
    </td>
    </tr>
    <tr id="row418193913501"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p51291514122112"><a name="p51291514122112"></a><a name="p51291514122112"></a>fault_level</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p146221632122113"><a name="p146221632122113"></a><a name="p146221632122113"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p7391102810268"><a name="p7391102810268"></a><a name="p7391102810268"></a>Specifies the fault level of a replication pair.</p>
    <a name="ul15357239152112"></a><a name="ul15357239152112"></a><ul id="ul15357239152112"><li><strong id="b84235270620364"><a name="b84235270620364"></a><a name="b84235270620364"></a>0</strong>: No fault occurs.</li><li><strong id="b0254829202018"><a name="b0254829202018"></a><a name="b0254829202018"></a>2</strong>: The disk of the current production site does not have read/write permissions. In this case, you are advised to perform a failover.</li><li><strong id="b030211301215"><a name="b030211301215"></a><a name="b030211301215"></a>5</strong>: The replication link is disconnected. In this case, a failover is not allowed. Contact the <span id="text1533123393119"><a name="text1533123393119"></a><a name="text1533123393119"></a>customer service</span> to obtain service support.</li></ul>
    </td>
    </tr>
    <tr id="row82381445114110"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p423874574115"><a name="p423874574115"></a><a name="p423874574115"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p122392454419"><a name="p122392454419"></a><a name="p122392454419"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p192391245104118"><a name="p192391245104118"></a><a name="p192391245104118"></a>Specifies the time when a replication pair was created.</p>
    <p id="p1170522111317"><a name="p1170522111317"></a><a name="p1170522111317"></a>The default format is as follows: "yyyy-MM-ddTHH:mm:ss.SSSZ", for example, <strong id="b12622173843418"><a name="b12622173843418"></a><a name="b12622173843418"></a>2019-04-01T12:00:00.000Z</strong>.</p>
    </td>
    </tr>
    <tr id="row82392045114114"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p19239745174120"><a name="p19239745174120"></a><a name="p19239745174120"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p16239144544115"><a name="p16239144544115"></a><a name="p16239144544115"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p12239745134118"><a name="p12239745134118"></a><a name="p12239745134118"></a>Specifies the time when a replication pair was updated.</p>
    <p id="p15338112513139"><a name="p15338112513139"></a><a name="p15338112513139"></a>The default format is as follows: "yyyy-MM-ddTHH:mm:ss.SSSZ", for example, <strong id="b4741331113511"><a name="b4741331113511"></a><a name="b4741331113511"></a>2019-04-01T12:00:00.000Z</strong>.</p>
    </td>
    </tr>
    <tr id="row923913456419"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p82411245114119"><a name="p82411245114119"></a><a name="p82411245114119"></a>record_metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p724115456411"><a name="p724115456411"></a><a name="p724115456411"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p1424134512413"><a name="p1424134512413"></a><a name="p1424134512413"></a>Specifies the SDR data of a replication pair.</p>
    <p id="p1039194815514"><a name="p1039194815514"></a><a name="p1039194815514"></a>For details, see <a href="#table5781813115015">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="row24071171901"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p16241194510417"><a name="p16241194510417"></a><a name="p16241194510417"></a>failure_detail</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p72411445104115"><a name="p72411445104115"></a><a name="p72411445104115"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p17241154534117"><a name="p17241154534117"></a><a name="p17241154534117"></a>Specifies the error code returned only when <strong id="b136121118251"><a name="b136121118251"></a><a name="b136121118251"></a>status</strong> of a replication pair is <strong id="b1561917119254"><a name="b1561917119254"></a><a name="b1561917119254"></a>error</strong>.</p>
    <p id="p149661057101814"><a name="p149661057101814"></a><a name="p149661057101814"></a>For details, see the returned value in <a href="error-code-description.md">Error Code Description</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2** **attachment**  field description

    <a name="table47791613195012"></a>
    <table><thead align="left"><tr id="row117791138501"><th class="cellrowborder" valign="top" width="29.07%" id="mcps1.2.4.1.1"><p id="p577821345016"><a name="p577821345016"></a><a name="p577821345016"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.44%" id="mcps1.2.4.1.2"><p id="p177981375019"><a name="p177981375019"></a><a name="p177981375019"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.49%" id="mcps1.2.4.1.3"><p id="p1677911375020"><a name="p1677911375020"></a><a name="p1677911375020"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row19756649173310"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p157796138502"><a name="p157796138502"></a><a name="p157796138502"></a>device</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p1877931375018"><a name="p1877931375018"></a><a name="p1877931375018"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p1477971317507"><a name="p1477971317507"></a><a name="p1477971317507"></a>Specifies the device name.</p>
    </td>
    </tr>
    <tr id="row2077917135506"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p1779131305015"><a name="p1779131305015"></a><a name="p1779131305015"></a>protected_instance</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p197792139509"><a name="p197792139509"></a><a name="p197792139509"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p157792132509"><a name="p157792132509"></a><a name="p157792132509"></a>Specifies the ID of the protected instance to which the replication pair is attached.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **record\_metadata**  field description

    <a name="table5781813115015"></a>
    <table><thead align="left"><tr id="row16780413205018"><th class="cellrowborder" valign="top" width="29.07%" id="mcps1.2.4.1.1"><p id="p1478061314507"><a name="p1478061314507"></a><a name="p1478061314507"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.44%" id="mcps1.2.4.1.2"><p id="p8780181335010"><a name="p8780181335010"></a><a name="p8780181335010"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.49%" id="mcps1.2.4.1.3"><p id="p187803137501"><a name="p187803137501"></a><a name="p187803137501"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row17780131355017"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p1878001305012"><a name="p1878001305012"></a><a name="p1878001305012"></a>multiattach</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p3780513115013"><a name="p3780513115013"></a><a name="p3780513115013"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p4780413155010"><a name="p4780413155010"></a><a name="p4780413155010"></a>Specifies whether the disk in a replication pair is a shared disk.</p>
    </td>
    </tr>
    <tr id="row678011315014"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p11780913175018"><a name="p11780913175018"></a><a name="p11780913175018"></a>bootable</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p1978017134502"><a name="p1978017134502"></a><a name="p1978017134502"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p7780101395019"><a name="p7780101395019"></a><a name="p7780101395019"></a>Specifies whether the disk in a replication pair is a system disk.</p>
    </td>
    </tr>
    <tr id="row8781713105015"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p15781121315010"><a name="p15781121315010"></a><a name="p15781121315010"></a>volume_size</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p378101375019"><a name="p378101375019"></a><a name="p378101375019"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p17781121375016"><a name="p17781121375016"></a><a name="p17781121375016"></a>Specifies the size of the disk in a replication pair. Unit: GB</p>
    </td>
    </tr>
    <tr id="row778112135503"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p207811913155015"><a name="p207811913155015"></a><a name="p207811913155015"></a>volume_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p2781131318506"><a name="p2781131318506"></a><a name="p2781131318506"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p15781181314509"><a name="p15781181314509"></a><a name="p15781181314509"></a>Specifies the type of the disk in a replication pair.</p>
    <a name="ul188853197144"></a><a name="ul188853197144"></a><ul id="ul188853197144"><li><strong id="b9853153921818"><a name="b9853153921818"></a><a name="b9853153921818"></a>SATA</strong>: common I/O</li><li><strong id="b1134915428185"><a name="b1134915428185"></a><a name="b1134915428185"></a>SAS</strong>: high I/O</li><li><strong id="b35571743141819"><a name="b35571743141819"></a><a name="b35571743141819"></a>SSD</strong>: ultra-high I/O</li><li><strong id="b14894184414189"><a name="b14894184414189"></a><a name="b14894184414189"></a>co-p1</strong>: high I/O (performance-optimized I)</li><li><strong id="b19152184620182"><a name="b19152184620182"></a><a name="b19152184620182"></a>uh-l1</strong>: ultra-high I/O (latency-optimized)<p id="p159027562599"><a name="p159027562599"></a><a name="p159027562599"></a>Disks of the co-p1 and uh-l1 types can be used on servers of the HANA, HL1, and HL2 types only.</p>
    </li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "count": 1,
        "replications": [
            {
                "id": "b93bc1c4-67ee-45a1-bc8a-d022fdd28811",
                "name": "test_replication_name",
                "description": "description_test",
                "replication_model": "hypermetro",
                "status": "available",
                "progress": 0,
                "replication_status": "active",
                "attachment": [               
                    {     
                        "device": "/dev/vda",                   
                        "protected_instance": "8a7a6339-679b-452b-948c-144e0ef85d9e"               
                    }           
                ],
                "server_group_id": "c2aee29a-2959-4d01-9755-01cc76a4d17d",
                "volume_ids": "48dda0c0-c800-46f2-9728-a519ff783d35,388b324a-a9d1-44a4-a00d-42085f22a9bc",
                "priority_station": "source",
                "fault_level": "0",
                "created_at": "2018-05-04T03:43:24.108526",
                "updated_at": "2018-05-04T03:44:28.322873",
                "record_metadata": {
                    "multiattach": false,
                    "bootable": false,
                    "volume_size": 10,
                    "volume_type": "SATA"
                }
            }
        ]
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


