# Querying BMSs \(Native OpenStack API\)<a name="EN-US_TOPIC_0053158693"></a>

## Function<a name="section56354875"></a>

This API is used to query BMSs.

## Constraints<a name="section54054835151740"></a>

-   The query result returned by this interface includes both ECSs and BMSs. You need to filter out the BMSs using the flavor used to create the BMSs or the tags added to the BMSs during BMS creation.
-   If the image is used as the search criteria, other search criteria and pagination criteria are not supported. If both the image and other search criteria are used, the BMSs are filtered out by image. If the image is not used as the search criteria, this interface has no restrictions.

## URI<a name="section37431827"></a>

GET /v2.1/\{project\_id\}/servers\{?changes-since=\{changes-since\}&image=\{image\}&flavor=\{flavor\}&name=\{name\}&status=\{status\}&limit=\{limit\}&marker=\{marker\}&tags=\{tags\}&not-tags=\{not-tags\}&reservation\_id=\{reservation\_id\}&sort\_key=\{sort\_key\}&sort\_dir=\{sort\_dir\}\}

[Table 1](#table67612156510)  lists the parameters.

**Table  1**  Parameter description

<a name="table67612156510"></a>
<table><thead align="left"><tr id="row67810155512"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p47678793154517"><a name="p47678793154517"></a><a name="p47678793154517"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p62557569154517"><a name="p62557569154517"></a><a name="p62557569154517"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p37549795154517"><a name="p37549795154517"></a><a name="p37549795154517"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row17821535110"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1019106154517"><a name="p1019106154517"></a><a name="p1019106154517"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p15438763154517"><a name="p15438763154517"></a><a name="p15438763154517"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p42580325154517"><a name="p42580325154517"></a><a name="p42580325154517"></a>Specifies the project ID.</p>
<p id="p9141450142010"><a name="p9141450142010"></a><a name="p9141450142010"></a>For how to obtain the project ID, see <a href="https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328009.html" target="_blank" rel="noopener noreferrer">Obtaining Required Information</a>.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section131361554145510"></a>

-   Request parameters

    <a name="table1758718426522"></a>
    <table><thead align="left"><tr id="row1458874235211"><th class="cellrowborder" valign="top" width="19.85%" id="mcps1.1.5.1.1"><p id="p59978491115233"><a name="p59978491115233"></a><a name="p59978491115233"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.39%" id="mcps1.1.5.1.2"><p id="p26419641115233"><a name="p26419641115233"></a><a name="p26419641115233"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.75%" id="mcps1.1.5.1.3"><p id="p59616187115233"><a name="p59616187115233"></a><a name="p59616187115233"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="41.010000000000005%" id="mcps1.1.5.1.4"><p id="p64181866115233"><a name="p64181866115233"></a><a name="p64181866115233"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row686311283276"><td class="cellrowborder" valign="top" width="19.85%" headers="mcps1.1.5.1.1 "><p id="p10447191065310"><a name="p10447191065310"></a><a name="p10447191065310"></a>changes-since</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.39%" headers="mcps1.1.5.1.2 "><p id="p644915104533"><a name="p644915104533"></a><a name="p644915104533"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.75%" headers="mcps1.1.5.1.3 "><p id="p13454131016536"><a name="p13454131016536"></a><a name="p13454131016536"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.010000000000005%" headers="mcps1.1.5.1.4 "><p id="p445791014538"><a name="p445791014538"></a><a name="p445791014538"></a>Specifies the timestamp of the last <span id="text121698161638"><a name="text121698161638"></a><a name="text121698161638"></a>BMS</span><span id="text216912161937"><a name="text216912161937"></a><a name="text216912161937"></a></span> status update. The parameter is in ISO 8601 time format, for example, <strong id="b119409183716"><a name="b119409183716"></a><a name="b119409183716"></a>2013-06-09T06:42:18Z</strong>.</p>
    </td>
    </tr>
    <tr id="row16588164215216"><td class="cellrowborder" valign="top" width="19.85%" headers="mcps1.1.5.1.1 "><p id="p17387161075313"><a name="p17387161075313"></a><a name="p17387161075313"></a>image</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.39%" headers="mcps1.1.5.1.2 "><p id="p123900108538"><a name="p123900108538"></a><a name="p123900108538"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.75%" headers="mcps1.1.5.1.3 "><p id="p2393161013538"><a name="p2393161013538"></a><a name="p2393161013538"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.010000000000005%" headers="mcps1.1.5.1.4 "><p id="p1339701010533"><a name="p1339701010533"></a><a name="p1339701010533"></a>Specifies the image ID.</p>
    <div class="note" id="note623794911339"><a name="note623794911339"></a><a name="note623794911339"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p17237114943316"><a name="p17237114943316"></a><a name="p17237114943316"></a>If the image is used as the search criteria, other search criteria and pagination criteria are not supported. If both the image and other search criteria are used, the BMS details are filtered out by image. If the image is not used as the search criteria, this interface has no restrictions.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row05881842195216"><td class="cellrowborder" valign="top" width="19.85%" headers="mcps1.1.5.1.1 "><p id="p839991012531"><a name="p839991012531"></a><a name="p839991012531"></a>flavor</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.39%" headers="mcps1.1.5.1.2 "><p id="p12402210155311"><a name="p12402210155311"></a><a name="p12402210155311"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.75%" headers="mcps1.1.5.1.3 "><p id="p15406610135318"><a name="p15406610135318"></a><a name="p15406610135318"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.010000000000005%" headers="mcps1.1.5.1.4 "><p id="p1040881015311"><a name="p1040881015311"></a><a name="p1040881015311"></a>Specifies the flavor ID.</p>
    <p id="p7741128113511"><a name="p7741128113511"></a><a name="p7741128113511"></a>You can obtain the flavor ID from the <span id="text9235625735"><a name="text9235625735"></a><a name="text9235625735"></a>BMS</span><span id="text32351725734"><a name="text32351725734"></a><a name="text32351725734"></a></span> console or using the <a href="querying-bms-flavors-(native-openstack-api).md">Querying BMS Flavors (Native OpenStack API)</a> API.</p>
    </td>
    </tr>
    <tr id="row058811420527"><td class="cellrowborder" valign="top" width="19.85%" headers="mcps1.1.5.1.1 "><p id="p5413201085313"><a name="p5413201085313"></a><a name="p5413201085313"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.39%" headers="mcps1.1.5.1.2 "><p id="p1941781012535"><a name="p1941781012535"></a><a name="p1941781012535"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.75%" headers="mcps1.1.5.1.3 "><p id="p3422121055318"><a name="p3422121055318"></a><a name="p3422121055318"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.010000000000005%" headers="mcps1.1.5.1.4 "><p id="p842631015536"><a name="p842631015536"></a><a name="p842631015536"></a>Specifies the <span id="text13209132811312"><a name="text13209132811312"></a><a name="text13209132811312"></a>BMS</span><span id="text920922816319"><a name="text920922816319"></a><a name="text920922816319"></a></span> name. This parameter supports fuzzy matching.</p>
    <p id="p7429181015313"><a name="p7429181015313"></a><a name="p7429181015313"></a>For example, the regular expression <strong id="b84235270616859"><a name="b84235270616859"></a><a name="b84235270616859"></a>?name=bob</strong> will return both <strong id="b84235270616910"><a name="b84235270616910"></a><a name="b84235270616910"></a>bob</strong> and <strong id="b84235270616915"><a name="b84235270616915"></a><a name="b84235270616915"></a>bobb</strong>. To obtain only <strong id="b84235270616107"><a name="b84235270616107"></a><a name="b84235270616107"></a>bob</strong>, you can use a regular expression matching the basic database syntax, such as MySQL or PostgreSQL (official website: <a href="https://www.postgresql.org/docs/9.2/static/functions-matching.html" target="_blank" rel="noopener noreferrer">https://www.postgresql.org/docs/9.2/static/functions-matching.html</a>).</p>
    </td>
    </tr>
    <tr id="row105881642195217"><td class="cellrowborder" valign="top" width="19.85%" headers="mcps1.1.5.1.1 "><p id="p1743421075315"><a name="p1743421075315"></a><a name="p1743421075315"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.39%" headers="mcps1.1.5.1.2 "><p id="p843711020539"><a name="p843711020539"></a><a name="p843711020539"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.75%" headers="mcps1.1.5.1.3 "><p id="p11440101010537"><a name="p11440101010537"></a><a name="p11440101010537"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.010000000000005%" headers="mcps1.1.5.1.4 "><p id="p7441161020531"><a name="p7441161020531"></a><a name="p7441161020531"></a>Specifies the <span id="text4817131535"><a name="text4817131535"></a><a name="text4817131535"></a>BMS</span><span id="text1781773117312"><a name="text1781773117312"></a><a name="text1781773117312"></a></span> status.</p>
    <p id="p117067951617"><a name="p117067951617"></a><a name="p117067951617"></a>Value range:</p>
    <a name="ul29109448426"></a><a name="ul29109448426"></a><ul id="ul29109448426"><li><strong id="en-us_topic_0113746489_b23014110118"><a name="en-us_topic_0113746489_b23014110118"></a><a name="en-us_topic_0113746489_b23014110118"></a>ACTIVE</strong>: Running, Stopping, Deleting</li><li><strong id="en-us_topic_0113746489_b56772617123"><a name="en-us_topic_0113746489_b56772617123"></a><a name="en-us_topic_0113746489_b56772617123"></a>BUILD</strong>: Creating</li><li><strong id="en-us_topic_0113746489_b2334141210"><a name="en-us_topic_0113746489_b2334141210"></a><a name="en-us_topic_0113746489_b2334141210"></a>ERROR</strong>: Faulty</li><li><strong id="en-us_topic_0113746489_b1059115316129"><a name="en-us_topic_0113746489_b1059115316129"></a><a name="en-us_topic_0113746489_b1059115316129"></a>HARD_REBOOT</strong>: Forcibly Restarting</li><li><strong id="en-us_topic_0113746489_b391019910131"><a name="en-us_topic_0113746489_b391019910131"></a><a name="en-us_topic_0113746489_b391019910131"></a>REBOOT</strong>: Restarting</li></ul>
    </td>
    </tr>
    <tr id="row16588142145219"><td class="cellrowborder" valign="top" width="19.85%" headers="mcps1.1.5.1.1 "><p id="p1445843114279"><a name="p1445843114279"></a><a name="p1445843114279"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.39%" headers="mcps1.1.5.1.2 "><p id="p15457103122713"><a name="p15457103122713"></a><a name="p15457103122713"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.75%" headers="mcps1.1.5.1.3 "><p id="p15455113112714"><a name="p15455113112714"></a><a name="p15455113112714"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.010000000000005%" headers="mcps1.1.5.1.4 "><p id="p345110316275"><a name="p345110316275"></a><a name="p345110316275"></a>Specifies the number of <span id="text59831335739"><a name="text59831335739"></a><a name="text59831335739"></a>BMS</span><span id="text1098373515319"><a name="text1098373515319"></a><a name="text1098373515319"></a></span>s displayed on each page.</p>
    </td>
    </tr>
    <tr id="row12307152919453"><td class="cellrowborder" valign="top" width="19.85%" headers="mcps1.1.5.1.1 "><p id="p34602410233"><a name="p34602410233"></a><a name="p34602410233"></a>marker</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.39%" headers="mcps1.1.5.1.2 "><p id="p1946094112310"><a name="p1946094112310"></a><a name="p1946094112310"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.75%" headers="mcps1.1.5.1.3 "><p id="p14460249231"><a name="p14460249231"></a><a name="p14460249231"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.010000000000005%" headers="mcps1.1.5.1.4 "><p id="p174601046239"><a name="p174601046239"></a><a name="p174601046239"></a>Specifies the <span id="text71323381731"><a name="text71323381731"></a><a name="text71323381731"></a>BMS</span><span id="text613212389311"><a name="text613212389311"></a><a name="text613212389311"></a></span> ID to which the marker corresponds. The query will start from the next ID.</p>
    </td>
    </tr>
    <tr id="row14320610478"><td class="cellrowborder" valign="top" width="19.85%" headers="mcps1.1.5.1.1 "><p id="p5324615479"><a name="p5324615479"></a><a name="p5324615479"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.39%" headers="mcps1.1.5.1.2 "><p id="p143218664715"><a name="p143218664715"></a><a name="p143218664715"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.75%" headers="mcps1.1.5.1.3 "><p id="p143211619479"><a name="p143211619479"></a><a name="p143211619479"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.010000000000005%" headers="mcps1.1.5.1.4 "><p id="p123246194714"><a name="p123246194714"></a><a name="p123246194714"></a>Queries the <span id="text142391140333"><a name="text142391140333"></a><a name="text142391140333"></a>BMS</span><span id="text162393401630"><a name="text162393401630"></a><a name="text162393401630"></a></span>s with specified tags.</p>
    <p id="p12820165216471"><a name="p12820165216471"></a><a name="p12820165216471"></a>Added in micro version 2.26.</p>
    </td>
    </tr>
    <tr id="row1658884211523"><td class="cellrowborder" valign="top" width="19.85%" headers="mcps1.1.5.1.1 "><p id="p203418324539"><a name="p203418324539"></a><a name="p203418324539"></a>not-tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.39%" headers="mcps1.1.5.1.2 "><p id="p173673215532"><a name="p173673215532"></a><a name="p173673215532"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.75%" headers="mcps1.1.5.1.3 "><p id="p238132105317"><a name="p238132105317"></a><a name="p238132105317"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.010000000000005%" headers="mcps1.1.5.1.4 "><p id="p154313328536"><a name="p154313328536"></a><a name="p154313328536"></a>Queries the <span id="text179892421232"><a name="text179892421232"></a><a name="text179892421232"></a>BMS</span><span id="text149891342231"><a name="text149891342231"></a><a name="text149891342231"></a></span>s with tags not containing the specified value. The value is a list of tag keys.</p>
    <div class="note" id="note124521913175616"><a name="note124521913175616"></a><a name="note124521913175616"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1745221311560"><a name="p1745221311560"></a><a name="p1745221311560"></a>If the tags added before the function upgrade are in the format of "Key.Value", query tags using "Key".</p>
    <p id="p213418685710"><a name="p213418685710"></a><a name="p213418685710"></a>For example, an existing tag is <strong id="b84235270610509"><a name="b84235270610509"></a><a name="b84235270610509"></a>a.b</strong>. After the tag function upgrade, query the tag using "not-tags=a".</p>
    </div></div>
    <p id="p19441232135317"><a name="p19441232135317"></a><a name="p19441232135317"></a>Added in micro version 2.26.</p>
    </td>
    </tr>
    <tr id="row1158812424528"><td class="cellrowborder" valign="top" width="19.85%" headers="mcps1.1.5.1.1 "><p id="p184717323539"><a name="p184717323539"></a><a name="p184717323539"></a>reservation_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.39%" headers="mcps1.1.5.1.2 "><p id="p1650832195311"><a name="p1650832195311"></a><a name="p1650832195311"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.75%" headers="mcps1.1.5.1.3 "><p id="p1453143220535"><a name="p1453143220535"></a><a name="p1453143220535"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.010000000000005%" headers="mcps1.1.5.1.4 "><p id="p5551832185311"><a name="p5551832185311"></a><a name="p5551832185311"></a>Specifies the reserved ID, which can be used to query <span id="text63205019314"><a name="text63205019314"></a><a name="text63205019314"></a>BMS</span><span id="text734501833"><a name="text734501833"></a><a name="text734501833"></a></span>s created in a batch.</p>
    <p id="p45753218534"><a name="p45753218534"></a><a name="p45753218534"></a>Added in micro version 2.26.</p>
    </td>
    </tr>
    <tr id="row1758864217526"><td class="cellrowborder" valign="top" width="19.85%" headers="mcps1.1.5.1.1 "><p id="p10633321531"><a name="p10633321531"></a><a name="p10633321531"></a>sort_key</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.39%" headers="mcps1.1.5.1.2 "><p id="p106613212531"><a name="p106613212531"></a><a name="p106613212531"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.75%" headers="mcps1.1.5.1.3 "><p id="p196963275311"><a name="p196963275311"></a><a name="p196963275311"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.010000000000005%" headers="mcps1.1.5.1.4 "><p id="p167133212536"><a name="p167133212536"></a><a name="p167133212536"></a>Specifies the BMS sorting attribute, which can be the <span id="text62627567316"><a name="text62627567316"></a><a name="text62627567316"></a>BMS</span><span id="text1726217563313"><a name="text1726217563313"></a><a name="text1726217563313"></a></span> UUID (<strong id="b1735217112617"><a name="b1735217112617"></a><a name="b1735217112617"></a>uuid</strong>), <span id="text142381559638"><a name="text142381559638"></a><a name="text142381559638"></a>BMS</span><span id="text22392599316"><a name="text22392599316"></a><a name="text22392599316"></a></span> status (<strong id="b575761619614"><a name="b575761619614"></a><a name="b575761619614"></a>vm_state</strong>), <span id="text135136112411"><a name="text135136112411"></a><a name="text135136112411"></a>BMS</span><span id="text6513116415"><a name="text6513116415"></a><a name="text6513116415"></a></span> name (<strong id="b027110341562"><a name="b027110341562"></a><a name="b027110341562"></a>display_name</strong>), <span id="text1810916516416"><a name="text1810916516416"></a><a name="text1810916516416"></a>BMS</span><span id="text17109175241"><a name="text17109175241"></a><a name="text17109175241"></a></span> task status (<strong id="b145994513618"><a name="b145994513618"></a><a name="b145994513618"></a>task_state</strong>), power status (<strong id="b9292451066"><a name="b9292451066"></a><a name="b9292451066"></a>power_state</strong>), creation time (<strong id="b30356567"><a name="b30356567"></a><a name="b30356567"></a>created_at</strong>), last time when the <span id="text1058920618712"><a name="text1058920618712"></a><a name="text1058920618712"></a>BMS</span><span id="text1059536977"><a name="text1059536977"></a><a name="text1059536977"></a></span> is updated (<strong id="b9391131672"><a name="b9391131672"></a><a name="b9391131672"></a>updated_at</strong>), and AZ (<strong id="b198324171673"><a name="b198324171673"></a><a name="b198324171673"></a>availability_zone</strong>). You can specify multiple <strong id="b8423527061280"><a name="b8423527061280"></a><a name="b8423527061280"></a>sort_key</strong> and <strong id="b8423527061289"><a name="b8423527061289"></a><a name="b8423527061289"></a>sort_dir</strong> pairs.</p>
    <p id="p1321581482211"><a name="p1321581482211"></a><a name="p1321581482211"></a>The default sorting is the reverse order by <strong id="b6725857464"><a name="b6725857464"></a><a name="b6725857464"></a>created_at</strong>.</p>
    </td>
    </tr>
    <tr id="row135891242165217"><td class="cellrowborder" valign="top" width="19.85%" headers="mcps1.1.5.1.1 "><p id="p1327414444539"><a name="p1327414444539"></a><a name="p1327414444539"></a>sort_dir</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.39%" headers="mcps1.1.5.1.2 "><p id="p16275104445317"><a name="p16275104445317"></a><a name="p16275104445317"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.75%" headers="mcps1.1.5.1.3 "><p id="p202804443536"><a name="p202804443536"></a><a name="p202804443536"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.010000000000005%" headers="mcps1.1.5.1.4 "><p id="p15283154425314"><a name="p15283154425314"></a><a name="p15283154425314"></a>Specifies the sorting direction.</p>
    <a name="ul22858441530"></a><a name="ul22858441530"></a><ul id="ul22858441530"><li><strong id="b2483023315742"><a name="b2483023315742"></a><a name="b2483023315742"></a>asc</strong>: The query results are displayed in ascending order.</li><li><strong id="b191712644011"><a name="b191712644011"></a><a name="b191712644011"></a>desc</strong> (default value): The query results are displayed in descending order.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request
    -   With no optional parameter

        ```
        GET https://{ECS Endpoint}/v2.1/bbf1946d374b44a0a2a95533562ba954/servers
        ```

    -   With an optional parameter

        ```
        GET https://{ECS Endpoint}/v2.1/bbf1946d374b44a0a2a95533562ba954/servers?tags=__type_baremetal
        ```

    -   With multiple optional parameters

        ```
        GET https://{ECS Endpoint}/v2.1/bbf1946d374b44a0a2a95533562ba954/servers?tags=__type_baremetal&name=bms-test01
        ```



## Response Message<a name="section12079142"></a>

-   Response parameters

    <a name="table44736746"></a>
    <table><thead align="left"><tr id="row8242429"><th class="cellrowborder" valign="top" width="23.36%" id="mcps1.1.4.1.1"><p id="p09797427505"><a name="p09797427505"></a><a name="p09797427505"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="25.22%" id="mcps1.1.4.1.2"><p id="p8982164210504"><a name="p8982164210504"></a><a name="p8982164210504"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="51.42%" id="mcps1.1.4.1.3"><p id="p1898519426507"><a name="p1898519426507"></a><a name="p1898519426507"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row18745119"><td class="cellrowborder" valign="top" width="23.36%" headers="mcps1.1.4.1.1 "><p id="p41959665"><a name="p41959665"></a><a name="p41959665"></a>servers</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.22%" headers="mcps1.1.4.1.2 "><p id="p16804102"><a name="p16804102"></a><a name="p16804102"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.42%" headers="mcps1.1.4.1.3 "><p id="p36377578"><a name="p36377578"></a><a name="p36377578"></a>Specifies the <span id="text542414112416"><a name="text542414112416"></a><a name="text542414112416"></a>BMS</span><span id="text74251911344"><a name="text74251911344"></a><a name="text74251911344"></a></span> list. For details, see <a href="#table11253402">Table 2</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2** **servers**  field data structure description

    <a name="table11253402"></a>
    <table><thead align="left"><tr id="row10267559"><th class="cellrowborder" valign="top" width="23.599999999999998%" id="mcps1.2.4.1.1"><p id="p689134705020"><a name="p689134705020"></a><a name="p689134705020"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="25.380000000000003%" id="mcps1.2.4.1.2"><p id="p79316472500"><a name="p79316472500"></a><a name="p79316472500"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="51.019999999999996%" id="mcps1.2.4.1.3"><p id="p1991747185016"><a name="p1991747185016"></a><a name="p1991747185016"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row15663"><td class="cellrowborder" valign="top" width="23.599999999999998%" headers="mcps1.2.4.1.1 "><p id="p1268752"><a name="p1268752"></a><a name="p1268752"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.380000000000003%" headers="mcps1.2.4.1.2 "><p id="p2786131"><a name="p2786131"></a><a name="p2786131"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.019999999999996%" headers="mcps1.2.4.1.3 "><p id="p24350086"><a name="p24350086"></a><a name="p24350086"></a>Specifies the <span id="text46502131440"><a name="text46502131440"></a><a name="text46502131440"></a>BMS</span><span id="text16500131412"><a name="text16500131412"></a><a name="text16500131412"></a></span> name.</p>
    </td>
    </tr>
    <tr id="row17824184"><td class="cellrowborder" valign="top" width="23.599999999999998%" headers="mcps1.2.4.1.1 "><p id="p34472770"><a name="p34472770"></a><a name="p34472770"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.380000000000003%" headers="mcps1.2.4.1.2 "><p id="p18974148"><a name="p18974148"></a><a name="p18974148"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.019999999999996%" headers="mcps1.2.4.1.3 "><p id="p60510987"><a name="p60510987"></a><a name="p60510987"></a>Specifies the unique ID of the <span id="text163215161641"><a name="text163215161641"></a><a name="text163215161641"></a>BMS</span><span id="text6321216147"><a name="text6321216147"></a><a name="text6321216147"></a></span>.</p>
    </td>
    </tr>
    <tr id="row7727977"><td class="cellrowborder" valign="top" width="23.599999999999998%" headers="mcps1.2.4.1.1 "><p id="p21986423"><a name="p21986423"></a><a name="p21986423"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.380000000000003%" headers="mcps1.2.4.1.2 "><p id="p14181463161150"><a name="p14181463161150"></a><a name="p14181463161150"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.019999999999996%" headers="mcps1.2.4.1.3 "><p id="p52375797"><a name="p52375797"></a><a name="p52375797"></a>Specifies shortcut links of the <span id="text14899617746"><a name="text14899617746"></a><a name="text14899617746"></a>BMS</span><span id="text28997171941"><a name="text28997171941"></a><a name="text28997171941"></a></span>. For details, see <a href="#table64121649">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **links**  field data structure description

    <a name="table64121649"></a>
    <table><thead align="left"><tr id="row59320951"><th class="cellrowborder" valign="top" width="23.86%" id="mcps1.2.4.1.1"><p id="p189635514509"><a name="p189635514509"></a><a name="p189635514509"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="25.240000000000002%" id="mcps1.2.4.1.2"><p id="p79654516507"><a name="p79654516507"></a><a name="p79654516507"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="50.9%" id="mcps1.2.4.1.3"><p id="p12968551135019"><a name="p12968551135019"></a><a name="p12968551135019"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row61486274"><td class="cellrowborder" valign="top" width="23.86%" headers="mcps1.2.4.1.1 "><p id="p14332335"><a name="p14332335"></a><a name="p14332335"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p14933841"><a name="p14933841"></a><a name="p14933841"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.9%" headers="mcps1.2.4.1.3 "><p id="p1681623"><a name="p1681623"></a><a name="p1681623"></a>Specifies the shortcut link marker name. The value can be:</p>
    <a name="ul207311644172510"></a><a name="ul207311644172510"></a><ul id="ul207311644172510"><li><strong id="en-us_topic_0131326852_b320113110516"><a name="en-us_topic_0131326852_b320113110516"></a><a name="en-us_topic_0131326852_b320113110516"></a>self</strong>: resource link that contains the version number. It is used when immediate tracing is required.</li><li><strong id="en-us_topic_0131326852_b84171947711"><a name="en-us_topic_0131326852_b84171947711"></a><a name="en-us_topic_0131326852_b84171947711"></a>bookmark</strong>: resource link that can be stored for a long time.</li></ul>
    </td>
    </tr>
    <tr id="row15134612"><td class="cellrowborder" valign="top" width="23.86%" headers="mcps1.2.4.1.1 "><p id="p17944037"><a name="p17944037"></a><a name="p17944037"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p21885054"><a name="p21885054"></a><a name="p21885054"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.9%" headers="mcps1.2.4.1.3 "><p id="p27858965"><a name="p27858965"></a><a name="p27858965"></a>Specifies the corresponding shortcut link.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "servers": [
            {
                "name": "bms",
                "links": [
                    {
                        "rel": "self",
                        "href": "https://openstack.example.com/v2.1/c685484a8cc2416b97260938705deb65/servers/820abbd0-2d8b-4bc5-ae46-69cacfd4fbaa"
                    },
                    {
                        "rel": "bookmark",
                        "href": "https://openstack.example.com/c685484a8cc2416b97260938705deb65/servers/820abbd0-2d8e-4bc5-ae46-69cacfd4fbaa"
                    }
                ],
                "id": "820abbd0-2d8e-4bc5-ae46-69cacfd4fbaa"
            }
        ]
    }
    ```


## Returned Values<a name="section7610951"></a>

Normal values

<a name="en-us_topic_0106040941_table753804619176"></a>
<table><thead align="left"><tr id="en-us_topic_0106040941_row10735134615172"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="en-us_topic_0106040941_p19735204616177"><a name="en-us_topic_0106040941_p19735204616177"></a><a name="en-us_topic_0106040941_p19735204616177"></a>Returned Values</p>
</th>
<th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="en-us_topic_0106040941_p207355465176"><a name="en-us_topic_0106040941_p207355465176"></a><a name="en-us_topic_0106040941_p207355465176"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0106040941_row1473514621713"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0106040941_p13735144611178"><a name="en-us_topic_0106040941_p13735144611178"></a><a name="en-us_topic_0106040941_p13735144611178"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0106040941_p207351246161711"><a name="en-us_topic_0106040941_p207351246161711"></a><a name="en-us_topic_0106040941_p207351246161711"></a>The server has successfully processed the request.</p>
</td>
</tr>
</tbody>
</table>

For details about other returned values, see  [Status Codes](status-codes.md).

## Error Codes<a name="section14752650154917"></a>

See  [Error Codes](error-codes.md).

