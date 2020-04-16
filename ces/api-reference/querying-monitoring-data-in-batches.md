# Querying Monitoring Data in Batches<a name="EN-US_TOPIC_0171212584"></a>

## Function<a name="section28757494191739"></a>

You can query the monitoring data of specified metrics within a specified time range and specified granularities in batches. At present, you can query the monitoring data of a maximum of 10 metrics in batches. 

## URI<a name="section26247582191739"></a>

POST /V1.0/\{project\_id\}/batch-query-metric-data

-   Parameter description

    **Table  1**  Parameter description

    <a name="table61299064191739"></a>
    <table><thead align="left"><tr id="row46292936191739"><th class="cellrowborder" valign="top" width="19.39%" id="mcps1.2.4.1.1"><p id="p58740307191739"><a name="p58740307191739"></a><a name="p58740307191739"></a><strong id="b842352706201552"><a name="b842352706201552"></a><a name="b842352706201552"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.41%" id="mcps1.2.4.1.2"><p id="p60344431191739"><a name="p60344431191739"></a><a name="p60344431191739"></a><strong id="b842352706201556"><a name="b842352706201556"></a><a name="b842352706201556"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="60.199999999999996%" id="mcps1.2.4.1.3"><p id="p56060739191739"><a name="p56060739191739"></a><a name="p56060739191739"></a><strong id="b842352706201559"><a name="b842352706201559"></a><a name="b842352706201559"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row44626040191739"><td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.2.4.1.1 "><p id="p57939510191739"><a name="p57939510191739"></a><a name="p57939510191739"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.41%" headers="mcps1.2.4.1.2 "><p id="p62588708191739"><a name="p62588708191739"></a><a name="p62588708191739"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.199999999999996%" headers="mcps1.2.4.1.3 "><p id="p36520554191739"><a name="p36520554191739"></a><a name="p36520554191739"></a>Specifies the project ID.</p>
    <p id="p55701252564"><a name="p55701252564"></a><a name="p55701252564"></a>For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section60249534191739"></a>

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>1.  The size of a POST request cannot exceed 512 KB. Otherwise, the request will be denied.  
>2.  The default maximum query intervals of different periods are different.  
>    If  **period**  is  **1**, the maximum interval between  **from**  and  **to**  is 4 hours. If the interval between  **from**  and  **to**  is longer than 4 hours, adjust the value of  **from**  to  **to**  -  **4\*3600\*1000**.  
>    If  **period**  is  **300**, the maximum interval between  **from**  and  **to**  is one day. If the interval between  **from**  and  **to**  is longer than one day, adjust the value of  **from**  to  **to**  -  **24\*3600\*1000**.  
>    If  **period**  is  **1200**, the maximum interval between  **from**  and  **to**  is three days. If the interval between  **from**  and  **to**  is longer than three days, adjust the value of  **from**  to  **to**  -  **3\*24\*3600\*1000**.  
>    If  **period**  is  **3600**, the maximum interval between  **from**  and  **to**  is 10 days. If the interval between  **from**  and  **to**  is longer than 10 days, adjust the value of  **from**  to  **to**  -  **10\*24\*3600\*1000**.  
>    If  **period**  is  **14400**, the maximum interval between  **from**  and  **to**  is 30 days. If the interval between  **from**  and  **to**  is longer than 30 days, adjust the value of  **from**  to  **to**  -  **30\*24\*3600\*1000**.  
>    If  **period**  is  **86400,**  the maximum interval between  **from**  and  **to**  is 180 days. If the interval between  **from**  and  **to**  is longer than 180 days, adjust the value of  **from**  to  **to**  -  **180\*24\*3600\*1000**.  

-   Request parameters

    **Table  2**  Request parameters

    <a name="table126111056191313"></a>
    <table><thead align="left"><tr id="row9612145681314"><th class="cellrowborder" valign="top" width="19.84%" id="mcps1.2.5.1.1"><p id="p11612105614136"><a name="p11612105614136"></a><a name="p11612105614136"></a><strong id="b842352706201721"><a name="b842352706201721"></a><a name="b842352706201721"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15.840000000000002%" id="mcps1.2.5.1.2"><p id="p26121256161314"><a name="p26121256161314"></a><a name="p26121256161314"></a><strong id="b842352706201727"><a name="b842352706201727"></a><a name="b842352706201727"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.94%" id="mcps1.2.5.1.3"><p id="p15612956111314"><a name="p15612956111314"></a><a name="p15612956111314"></a><strong id="b842352706201732"><a name="b842352706201732"></a><a name="b842352706201732"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="45.379999999999995%" id="mcps1.2.5.1.4"><p id="p20612205681313"><a name="p20612205681313"></a><a name="p20612205681313"></a><strong id="b842352706201738"><a name="b842352706201738"></a><a name="b842352706201738"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row661213566135"><td class="cellrowborder" valign="top" width="19.84%" headers="mcps1.2.5.1.1 "><p id="p2061214566138"><a name="p2061214566138"></a><a name="p2061214566138"></a>metrics</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.840000000000002%" headers="mcps1.2.5.1.2 "><p id="p126121656191320"><a name="p126121656191320"></a><a name="p126121656191320"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.94%" headers="mcps1.2.5.1.3 "><p id="p1612356131312"><a name="p1612356131312"></a><a name="p1612356131312"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.379999999999995%" headers="mcps1.2.5.1.4 "><p id="p3612135691311"><a name="p3612135691311"></a><a name="p3612135691311"></a>Specifies the metric data. The maximum length of the array is 10.</p>
    <p id="p9586154053018"><a name="p9586154053018"></a><a name="p9586154053018"></a>For details, see <a href="#table53651023191739">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="row14613165620136"><td class="cellrowborder" valign="top" width="19.84%" headers="mcps1.2.5.1.1 "><p id="p19613145621317"><a name="p19613145621317"></a><a name="p19613145621317"></a>from</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.840000000000002%" headers="mcps1.2.5.1.2 "><p id="p1061395631319"><a name="p1061395631319"></a><a name="p1061395631319"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.94%" headers="mcps1.2.5.1.3 "><p id="p1276519458171"><a name="p1276519458171"></a><a name="p1276519458171"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.379999999999995%" headers="mcps1.2.5.1.4 "><p id="p156131056141313"><a name="p156131056141313"></a><a name="p156131056141313"></a>Specifies the start time of the query. The value is a UNIX timestamp and the unit is ms. Set the value of <strong id="b84235270617327"><a name="b84235270617327"></a><a name="b84235270617327"></a>from</strong> to at least one period earlier than the current time. Rollup aggregates the raw data generated within a period to the start time of the period. Therefore, if values of <strong id="b84235270617852"><a name="b84235270617852"></a><a name="b84235270617852"></a>from</strong> and <strong id="b84235270617856"><a name="b84235270617856"></a><a name="b84235270617856"></a>to</strong> are within a period, the query result will be empty due to the rollup failure. You are advised to set <strong id="b59113991318926"><a name="b59113991318926"></a><a name="b59113991318926"></a>from</strong> to be at least one period earlier than the current time. Take the 5-minute period as an example. If it is 10:35 now, the raw data generated between 10:30 and 10:35 will be aggregated to 10:30. Therefore, in this example, if the value of <strong id="b842352706171230"><a name="b842352706171230"></a><a name="b842352706171230"></a>period</strong> is 5 minutes, the value of <strong id="b842352706171445"><a name="b842352706171445"></a><a name="b842352706171445"></a>from</strong> should be 10:30 or earlier.</p>
    <div class="note" id="note261365613131"><a name="note261365613131"></a><a name="note261365613131"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p3614125613130"><a name="p3614125613130"></a><a name="p3614125613130"></a>Cloud Eye rounds up the value of <strong id="b842352706171848"><a name="b842352706171848"></a><a name="b842352706171848"></a>from</strong> based on the level of granularity required to perform the rollup.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row261415569133"><td class="cellrowborder" valign="top" width="19.84%" headers="mcps1.2.5.1.1 "><p id="p5614115615138"><a name="p5614115615138"></a><a name="p5614115615138"></a>to</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.840000000000002%" headers="mcps1.2.5.1.2 "><p id="p26141356131313"><a name="p26141356131313"></a><a name="p26141356131313"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.94%" headers="mcps1.2.5.1.3 "><p id="p1895091934710"><a name="p1895091934710"></a><a name="p1895091934710"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.379999999999995%" headers="mcps1.2.5.1.4 "><p id="p56149563137"><a name="p56149563137"></a><a name="p56149563137"></a>Specifies the end time of the query. The value is a UNIX timestamp and the unit is ms. The value of parameter <strong id="b14360145152210"><a name="b14360145152210"></a><a name="b14360145152210"></a>from</strong> must be earlier than that of parameter <strong id="b636120450222"><a name="b636120450222"></a><a name="b636120450222"></a>to</strong>.</p>
    </td>
    </tr>
    <tr id="row186144562138"><td class="cellrowborder" valign="top" width="19.84%" headers="mcps1.2.5.1.1 "><p id="p9614185613136"><a name="p9614185613136"></a><a name="p9614185613136"></a>period</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.840000000000002%" headers="mcps1.2.5.1.2 "><p id="p861417562138"><a name="p861417562138"></a><a name="p861417562138"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.94%" headers="mcps1.2.5.1.3 "><p id="p4226363272"><a name="p4226363272"></a><a name="p4226363272"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.379999999999995%" headers="mcps1.2.5.1.4 "><p id="p761415611136"><a name="p761415611136"></a><a name="p761415611136"></a>Specifies the data monitoring granularity.</p>
    <p id="p36141756101312"><a name="p36141756101312"></a><a name="p36141756101312"></a>It is an enumerated value. Options include:</p>
    <a name="ul15614205613137"></a><a name="ul15614205613137"></a><ul id="ul15614205613137"><li><strong id="b842352706202151"><a name="b842352706202151"></a><a name="b842352706202151"></a>1</strong>: raw data</li><li><strong id="b62644269151643"><a name="b62644269151643"></a><a name="b62644269151643"></a>300</strong>: The data monitoring granularity is 5 minutes.</li><li><strong id="b32331302151643"><a name="b32331302151643"></a><a name="b32331302151643"></a>1200</strong>: The data monitoring granularity is 20 minutes.</li><li><strong id="b5763828151838"><a name="b5763828151838"></a><a name="b5763828151838"></a>3600</strong>: The data monitoring granularity is 1 hour.</li><li><strong id="b62926040151853"><a name="b62926040151853"></a><a name="b62926040151853"></a>14400</strong>: The data monitoring granularity is 4 hours.</li><li><strong id="b48617980151911"><a name="b48617980151911"></a><a name="b48617980151911"></a>86400</strong>: The data monitoring granularity is one day.</li></ul>
    </td>
    </tr>
    <tr id="row4614956161314"><td class="cellrowborder" valign="top" width="19.84%" headers="mcps1.2.5.1.1 "><p id="p361445615133"><a name="p361445615133"></a><a name="p361445615133"></a>filter</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.840000000000002%" headers="mcps1.2.5.1.2 "><p id="p1261485611131"><a name="p1261485611131"></a><a name="p1261485611131"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.94%" headers="mcps1.2.5.1.3 "><p id="p56146564139"><a name="p56146564139"></a><a name="p56146564139"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.379999999999995%" headers="mcps1.2.5.1.4 "><p id="p166141756101314"><a name="p166141756101314"></a><a name="p166141756101314"></a>Specifies the data rollup method. The following methods are supported:</p>
    <a name="en-us_topic_0046434864_ul7891893153925"></a><a name="en-us_topic_0046434864_ul7891893153925"></a><ul id="en-us_topic_0046434864_ul7891893153925"><li>If <strong id="b35508392550"><a name="b35508392550"></a><a name="b35508392550"></a>Avg.</strong> is selected for <strong id="b9551739135514"><a name="b9551739135514"></a><a name="b9551739135514"></a>Statistic</strong>, Cloud Eye calculates the average value of metric data within a rollup period.</li><li>If <strong id="b142451941165510"><a name="b142451941165510"></a><a name="b142451941165510"></a>Max.</strong> is selected for <strong id="b162469413559"><a name="b162469413559"></a><a name="b162469413559"></a>Statistic</strong>, Cloud Eye calculates the maximum value of metric data within a rollup period.</li><li>If <strong id="b1956564217552"><a name="b1956564217552"></a><a name="b1956564217552"></a>Min.</strong> is selected for <strong id="b456654215553"><a name="b456654215553"></a><a name="b456654215553"></a>Statistic</strong>, Cloud Eye calculates the minimum value of metric data within a rollup period.</li><li>If <strong id="b14863134345513"><a name="b14863134345513"></a><a name="b14863134345513"></a>Sum</strong> is selected for <strong id="b20864154335515"><a name="b20864154335515"></a><a name="b20864154335515"></a>Statistic</strong>, Cloud Eye calculates the sum of metric data within a rollup period.</li><li>If <strong id="b189754520559"><a name="b189754520559"></a><a name="b189754520559"></a>Variance</strong> is selected for <strong id="b99717453554"><a name="b99717453554"></a><a name="b99717453554"></a>Statistic</strong>, Cloud Eye calculates the variance value of metric data within a rollup period.</li></ul>
    <p id="p361495615137"><a name="p361495615137"></a><a name="p361495615137"></a>The value of <strong id="b842352706202454"><a name="b842352706202454"></a><a name="b842352706202454"></a>filter</strong> does not affect the query result of raw data. (The period is <strong id="b3821784215552"><a name="b3821784215552"></a><a name="b3821784215552"></a>1</strong>.)</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Field  **metrics**  data structure description

    <a name="table53651023191739"></a>
    <table><thead align="left"><tr id="row41871473191739"><th class="cellrowborder" valign="top" width="18.9%" id="mcps1.2.5.1.1"><p id="p36146190191739"><a name="p36146190191739"></a><a name="p36146190191739"></a><strong id="b1342795521"><a name="b1342795521"></a><a name="b1342795521"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15.840000000000002%" id="mcps1.2.5.1.2"><p id="p42160267191739"><a name="p42160267191739"></a><a name="p42160267191739"></a><strong id="b146511717"><a name="b146511717"></a><a name="b146511717"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15.55%" id="mcps1.2.5.1.3"><p id="p59538448191739"><a name="p59538448191739"></a><a name="p59538448191739"></a><strong id="b546876443"><a name="b546876443"></a><a name="b546876443"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="49.71%" id="mcps1.2.5.1.4"><p id="p57884998191739"><a name="p57884998191739"></a><a name="p57884998191739"></a><strong id="b137901096"><a name="b137901096"></a><a name="b137901096"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row37226944191739"><td class="cellrowborder" valign="top" width="18.9%" headers="mcps1.2.5.1.1 "><p id="p62592488191739"><a name="p62592488191739"></a><a name="p62592488191739"></a>namespace</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.840000000000002%" headers="mcps1.2.5.1.2 "><p id="p36826781191739"><a name="p36826781191739"></a><a name="p36826781191739"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.55%" headers="mcps1.2.5.1.3 "><p id="p30179270191739"><a name="p30179270191739"></a><a name="p30179270191739"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.71%" headers="mcps1.2.5.1.4 "><p id="p20849626154022"><a name="p20849626154022"></a><a name="p20849626154022"></a>Specifies the metric namespace. Its value must be in the <strong id="b23775928154022"><a name="b23775928154022"></a><a name="b23775928154022"></a>service.item</strong> format and can contain 3 to 32 characters.</p>
    <p id="p3510376515230"><a name="p3510376515230"></a><a name="p3510376515230"></a><strong id="b1875203315245"><a name="b1875203315245"></a><a name="b1875203315245"></a>service</strong> and <strong id="b3455057115245"><a name="b3455057115245"></a><a name="b3455057115245"></a>item</strong> each must be a string that starts with a letter and contains only uppercase letters, lowercase letters, digits, and underscores (_).</p>
    </td>
    </tr>
    <tr id="row35201547191739"><td class="cellrowborder" valign="top" width="18.9%" headers="mcps1.2.5.1.1 "><p id="p32753092191739"><a name="p32753092191739"></a><a name="p32753092191739"></a>dimensions</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.840000000000002%" headers="mcps1.2.5.1.2 "><p id="p35754801191739"><a name="p35754801191739"></a><a name="p35754801191739"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.55%" headers="mcps1.2.5.1.3 "><p id="p10457787191739"><a name="p10457787191739"></a><a name="p10457787191739"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.71%" headers="mcps1.2.5.1.4 "><p id="p41774409191739"><a name="p41774409191739"></a><a name="p41774409191739"></a>Specifies the list of the metric dimensions.</p>
    <p id="p40425365191739"><a name="p40425365191739"></a><a name="p40425365191739"></a>Each dimension is a JSON object, and its structure is as follows:</p>
    <p id="p485214919175"><a name="p485214919175"></a><a name="p485214919175"></a>{</p>
    <p id="p685215495171"><a name="p685215495171"></a><a name="p685215495171"></a>"name": "instance_id",</p>
    <p id="p2654105914173"><a name="p2654105914173"></a><a name="p2654105914173"></a>"value": "33328f02-3814-422e-b688-bfdba93d4050"</p>
    <p id="p1785218497174"><a name="p1785218497174"></a><a name="p1785218497174"></a>}</p>
    <p id="p1374219413211"><a name="p1374219413211"></a><a name="p1374219413211"></a>For details, see <a href="#table346618584132">Table 4</a>.</p>
    </td>
    </tr>
    <tr id="row12862050101510"><td class="cellrowborder" valign="top" width="18.9%" headers="mcps1.2.5.1.1 "><p id="p92442516150"><a name="p92442516150"></a><a name="p92442516150"></a>metric_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.840000000000002%" headers="mcps1.2.5.1.2 "><p id="p14244151201510"><a name="p14244151201510"></a><a name="p14244151201510"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.55%" headers="mcps1.2.5.1.3 "><p id="p14573015279"><a name="p14573015279"></a><a name="p14573015279"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.71%" headers="mcps1.2.5.1.4 "><p id="p14244185181519"><a name="p14244185181519"></a><a name="p14244185181519"></a>The value can be a string of 1 to 64 characters and must start with a letter and contain only uppercase letters, lowercase letters, digits, and underscores (_).</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **dimensions**  field data structure description

    <a name="table346618584132"></a>
    <table><thead align="left"><tr id="row0468185851318"><th class="cellrowborder" valign="top" width="19.84%" id="mcps1.2.5.1.1"><p id="p16468105821312"><a name="p16468105821312"></a><a name="p16468105821312"></a><strong id="b883076772"><a name="b883076772"></a><a name="b883076772"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15.840000000000002%" id="mcps1.2.5.1.2"><p id="p046812587133"><a name="p046812587133"></a><a name="p046812587133"></a><strong id="b1257968417"><a name="b1257968417"></a><a name="b1257968417"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.94%" id="mcps1.2.5.1.3"><p id="p18468185813136"><a name="p18468185813136"></a><a name="p18468185813136"></a><strong id="b1217615059"><a name="b1217615059"></a><a name="b1217615059"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="45.379999999999995%" id="mcps1.2.5.1.4"><p id="p16468158101318"><a name="p16468158101318"></a><a name="p16468158101318"></a><strong id="b504598158"><a name="b504598158"></a><a name="b504598158"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1047175861314"><td class="cellrowborder" valign="top" width="19.84%" headers="mcps1.2.5.1.1 "><p id="p9588164019308"><a name="p9588164019308"></a><a name="p9588164019308"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.840000000000002%" headers="mcps1.2.5.1.2 "><p id="p6471105841315"><a name="p6471105841315"></a><a name="p6471105841315"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.94%" headers="mcps1.2.5.1.3 "><p id="p3662932162713"><a name="p3662932162713"></a><a name="p3662932162713"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.379999999999995%" headers="mcps1.2.5.1.4 "><p id="p19551520125012"><a name="p19551520125012"></a><a name="p19551520125012"></a>Specifies the monitoring dimension. For example, the monitoring dimension of an ECS is <strong id="b107567226584"><a name="b107567226584"></a><a name="b107567226584"></a>instance_id</strong>, which is listed in the <strong id="b175614226581"><a name="b175614226581"></a><a name="b175614226581"></a>key</strong> column in <a href="ecs-metrics.md#en-us_topic_0022067719_section36963297112133">Dimension</a>.</p>
    <p id="p3963077184830"><a name="p3963077184830"></a><a name="p3963077184830"></a>The value can be a string of 1 to 32 characters and must start with a letter and contain only uppercase letters, lowercase letters, digits, underscores (_), and hyphens (-).</p>
    </td>
    </tr>
    <tr id="row10471155851315"><td class="cellrowborder" valign="top" width="19.84%" headers="mcps1.2.5.1.1 "><p id="p19588184023011"><a name="p19588184023011"></a><a name="p19588184023011"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.840000000000002%" headers="mcps1.2.5.1.2 "><p id="p1047245861319"><a name="p1047245861319"></a><a name="p1047245861319"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.94%" headers="mcps1.2.5.1.3 "><p id="p1588154012306"><a name="p1588154012306"></a><a name="p1588154012306"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.379999999999995%" headers="mcps1.2.5.1.4 "><p id="p11371113251615"><a name="p11371113251615"></a><a name="p11371113251615"></a>Specifies the dimension value, for example, an ECS ID.</p>
    <p id="p91691546145115"><a name="p91691546145115"></a><a name="p91691546145115"></a>The value can be a string of 1 to 256 characters and must start with a letter or a digit and contain only uppercase letters, lowercase letters, digits, underscores (_), and hyphens (-).</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    {
      "metrics" : [
        {
          "namespace": "SYS.ECS",
          "dimensions": [
              {
                "name": "instance_id",
                "value": "faea5b75-e390-4e2b-8733-9226a9026070"
              }
           ],
         "metric_name": "disk_write_bytes_rate"
        },
        {
          "namespace": "SYS.ECS",
          "dimensions": [
              {
                "name": "instance_id",
                "value": "06b4020f-461a-4a52-84da-53fa71c2f42b"
              }
           ],
         "metric_name": "disk_write_requests_rate"
        }
      ],
      "from": 1484153313000,
      "to": 1484653313000,
      "period": "1",
      "filter": "average"  
    }
    ```


## Response<a name="section25137312191739"></a>

-   Response parameters

    **Table  5**  Response parameters

    <a name="table39426324191739"></a>
    <table><thead align="left"><tr id="row53703872191739"><th class="cellrowborder" valign="top" width="18.24182418241824%" id="mcps1.2.4.1.1"><p id="p55046364191739"><a name="p55046364191739"></a><a name="p55046364191739"></a><strong id="b842352706203043"><a name="b842352706203043"></a><a name="b842352706203043"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.631463146314633%" id="mcps1.2.4.1.2"><p id="p46397032191739"><a name="p46397032191739"></a><a name="p46397032191739"></a><strong id="b943759699"><a name="b943759699"></a><a name="b943759699"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="67.12671267126713%" id="mcps1.2.4.1.3"><p id="p63273191739"><a name="p63273191739"></a><a name="p63273191739"></a><strong id="b842352706203052"><a name="b842352706203052"></a><a name="b842352706203052"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5125191191739"><td class="cellrowborder" valign="top" width="18.24182418241824%" headers="mcps1.2.4.1.1 "><p id="p12487337191739"><a name="p12487337191739"></a><a name="p12487337191739"></a>metrics</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.631463146314633%" headers="mcps1.2.4.1.2 "><p id="p56609115191739"><a name="p56609115191739"></a><a name="p56609115191739"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.12671267126713%" headers="mcps1.2.4.1.3 "><p id="p21935611191739"><a name="p21935611191739"></a><a name="p21935611191739"></a>Specifies the metric data.</p>
    <p id="p172665194275"><a name="p172665194275"></a><a name="p172665194275"></a>For details, see <a href="#table8753531192320">Table 6</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6**  Field  **metrics**  data structure description

    <a name="table8753531192320"></a>
    <table><thead align="left"><tr id="row17752173192319"><th class="cellrowborder" valign="top" width="18.24182418241824%" id="mcps1.2.4.1.1"><p id="p1575173132314"><a name="p1575173132314"></a><a name="p1575173132314"></a><strong id="b1600994399"><a name="b1600994399"></a><a name="b1600994399"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.631463146314633%" id="mcps1.2.4.1.2"><p id="p127511931102317"><a name="p127511931102317"></a><a name="p127511931102317"></a><strong id="b557675471"><a name="b557675471"></a><a name="b557675471"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="67.12671267126713%" id="mcps1.2.4.1.3"><p id="p275113132313"><a name="p275113132313"></a><a name="p275113132313"></a><strong id="b349256371"><a name="b349256371"></a><a name="b349256371"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3668159122515"><td class="cellrowborder" valign="top" width="18.24182418241824%" headers="mcps1.2.4.1.1 "><p id="p8678510152516"><a name="p8678510152516"></a><a name="p8678510152516"></a>unit</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.631463146314633%" headers="mcps1.2.4.1.2 "><p id="p667891072518"><a name="p667891072518"></a><a name="p667891072518"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.12671267126713%" headers="mcps1.2.4.1.3 "><p id="p86781310162514"><a name="p86781310162514"></a><a name="p86781310162514"></a>Specifies the metric unit.</p>
    </td>
    </tr>
    <tr id="row1728144112517"><td class="cellrowborder" valign="top" width="18.24182418241824%" headers="mcps1.2.4.1.1 "><p id="p2678191012252"><a name="p2678191012252"></a><a name="p2678191012252"></a>datapoints</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.631463146314633%" headers="mcps1.2.4.1.2 "><p id="p467819100259"><a name="p467819100259"></a><a name="p467819100259"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.12671267126713%" headers="mcps1.2.4.1.3 "><p id="p86781010162510"><a name="p86781010162510"></a><a name="p86781010162510"></a>Specifies the metric data list. Since Cloud Eye rounds up the value of <strong id="b1473920010172743"><a name="b1473920010172743"></a><a name="b1473920010172743"></a>from</strong> based on the level of granularity for data query, <strong id="b842352706173039"><a name="b842352706173039"></a><a name="b842352706173039"></a>datapoints</strong> may contain more data points than expected.</p>
    <p id="p12628543182913"><a name="p12628543182913"></a><a name="p12628543182913"></a>For details, see <a href="#table776113112239">Table 8</a>.</p>
    </td>
    </tr>
    <tr id="row956045965010"><td class="cellrowborder" valign="top" width="18.24182418241824%" headers="mcps1.2.4.1.1 "><p id="p123045818513"><a name="p123045818513"></a><a name="p123045818513"></a>namespace</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.631463146314633%" headers="mcps1.2.4.1.2 "><p id="p5304188105112"><a name="p5304188105112"></a><a name="p5304188105112"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.12671267126713%" headers="mcps1.2.4.1.3 "><p id="p230478155114"><a name="p230478155114"></a><a name="p230478155114"></a>Specifies the metric namespace. Its value must be in the <strong id="b189629281058"><a name="b189629281058"></a><a name="b189629281058"></a>service.item</strong> format and can contain 3 to 32 characters. <strong id="b20962028956"><a name="b20962028956"></a><a name="b20962028956"></a>service</strong> and <strong id="b89630287510"><a name="b89630287510"></a><a name="b89630287510"></a>item</strong> each must be a string that starts with a letter and contains only uppercase letters, lowercase letters, digits, and underscores (_).</p>
    </td>
    </tr>
    <tr id="row12582417515"><td class="cellrowborder" valign="top" width="18.24182418241824%" headers="mcps1.2.4.1.1 "><p id="p9304178165114"><a name="p9304178165114"></a><a name="p9304178165114"></a>dimensions</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.631463146314633%" headers="mcps1.2.4.1.2 "><p id="p1321914122293"><a name="p1321914122293"></a><a name="p1321914122293"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.12671267126713%" headers="mcps1.2.4.1.3 "><p id="p13304288519"><a name="p13304288519"></a><a name="p13304288519"></a>Specifies the metric dimension list.</p>
    <p id="p103046865111"><a name="p103046865111"></a><a name="p103046865111"></a>Each dimension is a JSON object, and its structure is as follows:</p>
    <p id="p1130419855113"><a name="p1130419855113"></a><a name="p1130419855113"></a>{</p>
    <p id="p1930415895112"><a name="p1930415895112"></a><a name="p1930415895112"></a>"name": "instance_id",</p>
    <p id="p1430412865119"><a name="p1430412865119"></a><a name="p1430412865119"></a>"value": "33328f02-3814-422e-b688-bfdba93d4050"</p>
    <p id="p11304108165115"><a name="p11304108165115"></a><a name="p11304108165115"></a>}</p>
    <p id="p3304128175119"><a name="p3304128175119"></a><a name="p3304128175119"></a>For details, see <a href="#table14755123118236">Table 7</a>.</p>
    </td>
    </tr>
    <tr id="row1889026105113"><td class="cellrowborder" valign="top" width="18.24182418241824%" headers="mcps1.2.4.1.1 "><p id="p1030514814513"><a name="p1030514814513"></a><a name="p1030514814513"></a>metric_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.631463146314633%" headers="mcps1.2.4.1.2 "><p id="p7305158125114"><a name="p7305158125114"></a><a name="p7305158125114"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.12671267126713%" headers="mcps1.2.4.1.3 "><p id="p113054810512"><a name="p113054810512"></a><a name="p113054810512"></a>The value can be a string of 1 to 64 characters and must start with a letter and contain only uppercase letters, lowercase letters, digits, and underscores (_).</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  7** **dimensions**  field data structure description

    <a name="table14755123118236"></a>
    <table><thead align="left"><tr id="row14754143118239"><th class="cellrowborder" valign="top" width="18.24182418241824%" id="mcps1.2.4.1.1"><p id="p1975415316232"><a name="p1975415316232"></a><a name="p1975415316232"></a><strong id="b1424792285"><a name="b1424792285"></a><a name="b1424792285"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.631463146314633%" id="mcps1.2.4.1.2"><p id="p67542031102320"><a name="p67542031102320"></a><a name="p67542031102320"></a><strong id="b1318187360"><a name="b1318187360"></a><a name="b1318187360"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="67.12671267126713%" id="mcps1.2.4.1.3"><p id="p17543319231"><a name="p17543319231"></a><a name="p17543319231"></a><strong id="b1110887672"><a name="b1110887672"></a><a name="b1110887672"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row16755143114233"><td class="cellrowborder" valign="top" width="18.24182418241824%" headers="mcps1.2.4.1.1 "><p id="p2618131922615"><a name="p2618131922615"></a><a name="p2618131922615"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.631463146314633%" headers="mcps1.2.4.1.2 "><p id="p32021649142716"><a name="p32021649142716"></a><a name="p32021649142716"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.12671267126713%" headers="mcps1.2.4.1.3 "><p id="p468551818481"><a name="p468551818481"></a><a name="p468551818481"></a>Specifies the monitoring dimension. For example, the monitoring dimension of an ECS is <strong id="b59501730175710"><a name="b59501730175710"></a><a name="b59501730175710"></a>instance_id</strong>, which is listed in the <strong id="b20951930125711"><a name="b20951930125711"></a><a name="b20951930125711"></a>key</strong> column in <a href="ecs-metrics.md#en-us_topic_0022067719_section36963297112133">Dimension</a>.</p>
    <p id="p1661871910269"><a name="p1661871910269"></a><a name="p1661871910269"></a>The value can be a string of 1 to 32 characters and must start with a letter and contain only uppercase letters, lowercase letters, digits, underscores (_), and hyphens (-).</p>
    </td>
    </tr>
    <tr id="row1375516313231"><td class="cellrowborder" valign="top" width="18.24182418241824%" headers="mcps1.2.4.1.1 "><p id="p66191819102618"><a name="p66191819102618"></a><a name="p66191819102618"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.631463146314633%" headers="mcps1.2.4.1.2 "><p id="p176192019102610"><a name="p176192019102610"></a><a name="p176192019102610"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.12671267126713%" headers="mcps1.2.4.1.3 "><p id="p1684517374483"><a name="p1684517374483"></a><a name="p1684517374483"></a>Specifies the dimension value, for example, an ECS ID.</p>
    <p id="p1961910191267"><a name="p1961910191267"></a><a name="p1961910191267"></a>The value can be a string of 1 to 256 characters and must start with a letter or a digit and contain only uppercase letters, lowercase letters, digits, underscores (_), and hyphens (-).</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  8** **datapoints**  field data structure description

    <a name="table776113112239"></a>
    <table><thead align="left"><tr id="row97565318232"><th class="cellrowborder" valign="top" width="18.24182418241824%" id="mcps1.2.4.1.1"><p id="p167551431202315"><a name="p167551431202315"></a><a name="p167551431202315"></a><strong id="b1016476332"><a name="b1016476332"></a><a name="b1016476332"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.631463146314633%" id="mcps1.2.4.1.2"><p id="p20756123152313"><a name="p20756123152313"></a><a name="p20756123152313"></a><strong id="b1141368587"><a name="b1141368587"></a><a name="b1141368587"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="67.12671267126713%" id="mcps1.2.4.1.3"><p id="p10756123132310"><a name="p10756123132310"></a><a name="p10756123132310"></a><strong id="b124756908"><a name="b124756908"></a><a name="b124756908"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1175615318237"><td class="cellrowborder" valign="top" width="18.24182418241824%" headers="mcps1.2.4.1.1 "><p id="p44866403191739"><a name="p44866403191739"></a><a name="p44866403191739"></a>max/min/average/sum/variance</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.631463146314633%" headers="mcps1.2.4.1.2 "><p id="p28996077191739"><a name="p28996077191739"></a><a name="p28996077191739"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.12671267126713%" headers="mcps1.2.4.1.3 "><p id="p2071217915428"><a name="p2071217915428"></a><a name="p2071217915428"></a>Specifies the metric value.</p>
    <p id="p66980889191739"><a name="p66980889191739"></a><a name="p66980889191739"></a>The value of this parameter is the same as that of parameter <strong id="b39431374153949"><a name="b39431374153949"></a><a name="b39431374153949"></a>filter</strong>.</p>
    </td>
    </tr>
    <tr id="row16756331192316"><td class="cellrowborder" valign="top" width="18.24182418241824%" headers="mcps1.2.4.1.1 "><p id="p40923954191739"><a name="p40923954191739"></a><a name="p40923954191739"></a>timestamp</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.631463146314633%" headers="mcps1.2.4.1.2 "><p id="p576175692718"><a name="p576175692718"></a><a name="p576175692718"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.12671267126713%" headers="mcps1.2.4.1.3 "><p id="p26617833191739"><a name="p26617833191739"></a><a name="p26617833191739"></a>Specifies the time when the metric is collected. It is a UNIX timestamp and the unit is ms.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "metrics": [
           {
               "unit": "request/s",
               "datapoints": [
                 {
                     "average": 0,
                     "timestamp": 1484401920000
                 },
                {
                     "average": 1,
                     "timestamp": 1484407920000
                 }
        ],
        "namespace": "MINE.APP",
        "dimensions": [
           {
              "name": "instance_id",
              "value": "33328f02-3814-422e-b688-bfdba93d4050"
            }
        ],
        "metric_name": "cpu_util"
     },
     {
         "unit": "request/s",
         "datapoints": [
           {
               "average": 2.3,
               "timestamp": 1484401920000
            },
           {
               "average": 1.2,
               "timestamp": 1484407920000
           }
       ],
        "namespace": "MINE.APP",
        "dimensions": [
          {
               "name": "instance_id",
               "value": "33328f02-3814-422e-b688-bfdba93d4051"
           }
         ],
          "metric_name": "cpu_util"
      }
     ]
    }
    ```


## Returned Values<a name="section40827282191739"></a>

-   Normal

    200

-   Abnormal

    <a name="table56792418191739"></a>
    <table><thead align="left"><tr id="row38483636191739"><th class="cellrowborder" valign="top" width="32.519999999999996%" id="mcps1.1.3.1.1"><p id="p30166797191739"><a name="p30166797191739"></a><a name="p30166797191739"></a><strong id="b842352706203153"><a name="b842352706203153"></a><a name="b842352706203153"></a>Returned Values</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="67.47999999999999%" id="mcps1.1.3.1.2"><p id="p27591491191739"><a name="p27591491191739"></a><a name="p27591491191739"></a><strong id="b842352706203123"><a name="b842352706203123"></a><a name="b842352706203123"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row20318269191739"><td class="cellrowborder" valign="top" width="32.519999999999996%" headers="mcps1.1.3.1.1 "><p id="p35167075191739"><a name="p35167075191739"></a><a name="p35167075191739"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.47999999999999%" headers="mcps1.1.3.1.2 "><p id="p29960863191739"><a name="p29960863191739"></a><a name="p29960863191739"></a>Request error</p>
    </td>
    </tr>
    <tr id="row1212311191739"><td class="cellrowborder" valign="top" width="32.519999999999996%" headers="mcps1.1.3.1.1 "><p id="p31088396191739"><a name="p31088396191739"></a><a name="p31088396191739"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.47999999999999%" headers="mcps1.1.3.1.2 "><p id="p35132170191739"><a name="p35132170191739"></a><a name="p35132170191739"></a>The authentication information is not provided or is incorrect.</p>
    </td>
    </tr>
    <tr id="row47754075191739"><td class="cellrowborder" valign="top" width="32.519999999999996%" headers="mcps1.1.3.1.1 "><p id="p42874872191739"><a name="p42874872191739"></a><a name="p42874872191739"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.47999999999999%" headers="mcps1.1.3.1.2 "><p id="p50312626191739"><a name="p50312626191739"></a><a name="p50312626191739"></a>You are forbidden to access the page requested.</p>
    </td>
    </tr>
    <tr id="row50160453191739"><td class="cellrowborder" valign="top" width="32.519999999999996%" headers="mcps1.1.3.1.1 "><p id="p36464884191739"><a name="p36464884191739"></a><a name="p36464884191739"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.47999999999999%" headers="mcps1.1.3.1.2 "><p id="p865652191739"><a name="p865652191739"></a><a name="p865652191739"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row7790874191739"><td class="cellrowborder" valign="top" width="32.519999999999996%" headers="mcps1.1.3.1.1 "><p id="p27081046191739"><a name="p27081046191739"></a><a name="p27081046191739"></a>429 Too Many Requests</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.47999999999999%" headers="mcps1.1.3.1.2 "><p id="p46081078191739"><a name="p46081078191739"></a><a name="p46081078191739"></a>Concurrent requests are excessive.</p>
    </td>
    </tr>
    <tr id="row12076519191739"><td class="cellrowborder" valign="top" width="32.519999999999996%" headers="mcps1.1.3.1.1 "><p id="p38673977191739"><a name="p38673977191739"></a><a name="p38673977191739"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.47999999999999%" headers="mcps1.1.3.1.2 "><p id="p45584419191739"><a name="p45584419191739"></a><a name="p45584419191739"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row7606593191739"><td class="cellrowborder" valign="top" width="32.519999999999996%" headers="mcps1.1.3.1.1 "><p id="p12154307191739"><a name="p12154307191739"></a><a name="p12154307191739"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.47999999999999%" headers="mcps1.1.3.1.2 "><p id="p44974834191739"><a name="p44974834191739"></a><a name="p44974834191739"></a>The service is currently unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Code<a name="section142437169473"></a>

For details, see  [Error Codes](error-codes.md).

