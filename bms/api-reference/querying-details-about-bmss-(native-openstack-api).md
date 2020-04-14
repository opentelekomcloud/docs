# Querying Details About BMSs \(Native OpenStack API\)<a name="EN-US_TOPIC_0053158679"></a>

## Function<a name="section33716833"></a>

This API is used to query details about BMSs.

## Constraints<a name="section29822855153557"></a>

-   The query result returned by this interface includes both ECS and BMS details. You need to filter out the BMS details using the flavor used to create the BMSs or the tags added to the BMSs during BMS creation.
-   If the image is used as the search criteria, other search criteria and pagination criteria are not supported. If both the image and other search criteria are used, the BMS details are filtered out by image. If the image is not used as the search criteria, this interface has no restrictions.

## URI<a name="section35016046"></a>

GET /v2.1/\{project\_id\}/servers/detail\{?changes-since=\{changes-since\}&image=\{image\}&flavor=\{flavor\}&name=\{name\}&status=\{status\}&limit=\{limit\}&marker=\{marker\}&tags=\{tags\}&not-tags=\{not-tags\}&reservation\_id=\{reservation\_id\}&sort\_key=\{sort\_key\}&sort\_dir=\{sort\_dir\}\}

[Table 1](#table0524112565)  lists the parameters.

**Table  1**  Parameter description

<a name="table0524112565"></a>
<table><thead align="left"><tr id="row252211165610"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p55073076202321"><a name="p55073076202321"></a><a name="p55073076202321"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p44659366114813"><a name="p44659366114813"></a><a name="p44659366114813"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p19572211"><a name="p19572211"></a><a name="p19572211"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1524119564"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p6789122714241"><a name="p6789122714241"></a><a name="p6789122714241"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p4344474"><a name="p4344474"></a><a name="p4344474"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p16358126"><a name="p16358126"></a><a name="p16358126"></a>Specifies the project ID.</p>
<p id="p9141450142010"><a name="p9141450142010"></a><a name="p9141450142010"></a>For how to obtain the project ID, see <a href="https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328009.html" target="_blank" rel="noopener noreferrer">Obtaining Required Information</a>.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section46708959"></a>

-   Request parameters

    <a name="table835318258318"></a>
    <table><thead align="left"><tr id="en-us_topic_0053158693_row1458874235211"><th class="cellrowborder" valign="top" width="19.85%" id="mcps1.1.5.1.1"><p id="en-us_topic_0053158693_p59978491115233"><a name="en-us_topic_0053158693_p59978491115233"></a><a name="en-us_topic_0053158693_p59978491115233"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.39%" id="mcps1.1.5.1.2"><p id="en-us_topic_0053158693_p26419641115233"><a name="en-us_topic_0053158693_p26419641115233"></a><a name="en-us_topic_0053158693_p26419641115233"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.75%" id="mcps1.1.5.1.3"><p id="en-us_topic_0053158693_p59616187115233"><a name="en-us_topic_0053158693_p59616187115233"></a><a name="en-us_topic_0053158693_p59616187115233"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="41.010000000000005%" id="mcps1.1.5.1.4"><p id="en-us_topic_0053158693_p64181866115233"><a name="en-us_topic_0053158693_p64181866115233"></a><a name="en-us_topic_0053158693_p64181866115233"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0053158693_row686311283276"><td class="cellrowborder" valign="top" width="19.85%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0053158693_p10447191065310"><a name="en-us_topic_0053158693_p10447191065310"></a><a name="en-us_topic_0053158693_p10447191065310"></a>changes-since</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.39%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0053158693_p644915104533"><a name="en-us_topic_0053158693_p644915104533"></a><a name="en-us_topic_0053158693_p644915104533"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.75%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0053158693_p13454131016536"><a name="en-us_topic_0053158693_p13454131016536"></a><a name="en-us_topic_0053158693_p13454131016536"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.010000000000005%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0053158693_p445791014538"><a name="en-us_topic_0053158693_p445791014538"></a><a name="en-us_topic_0053158693_p445791014538"></a>Specifies the timestamp of the last <span id="en-us_topic_0053158693_text121698161638"><a name="en-us_topic_0053158693_text121698161638"></a><a name="en-us_topic_0053158693_text121698161638"></a>BMS</span><span id="en-us_topic_0053158693_text216912161937"><a name="en-us_topic_0053158693_text216912161937"></a><a name="en-us_topic_0053158693_text216912161937"></a></span> status update. The parameter is in ISO 8601 time format, for example, <strong id="en-us_topic_0053158693_b119409183716"><a name="en-us_topic_0053158693_b119409183716"></a><a name="en-us_topic_0053158693_b119409183716"></a>2013-06-09T06:42:18Z</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0053158693_row16588164215216"><td class="cellrowborder" valign="top" width="19.85%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0053158693_p17387161075313"><a name="en-us_topic_0053158693_p17387161075313"></a><a name="en-us_topic_0053158693_p17387161075313"></a>image</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.39%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0053158693_p123900108538"><a name="en-us_topic_0053158693_p123900108538"></a><a name="en-us_topic_0053158693_p123900108538"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.75%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0053158693_p2393161013538"><a name="en-us_topic_0053158693_p2393161013538"></a><a name="en-us_topic_0053158693_p2393161013538"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.010000000000005%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0053158693_p1339701010533"><a name="en-us_topic_0053158693_p1339701010533"></a><a name="en-us_topic_0053158693_p1339701010533"></a>Specifies the image ID.</p>
    <div class="note" id="en-us_topic_0053158693_note623794911339"><a name="en-us_topic_0053158693_note623794911339"></a><a name="en-us_topic_0053158693_note623794911339"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0053158693_p17237114943316"><a name="en-us_topic_0053158693_p17237114943316"></a><a name="en-us_topic_0053158693_p17237114943316"></a>If the image is used as the search criteria, other search criteria and pagination criteria are not supported. If both the image and other search criteria are used, the BMS details are filtered out by image. If the image is not used as the search criteria, this interface has no restrictions.</p>
    </div></div>
    </td>
    </tr>
    <tr id="en-us_topic_0053158693_row05881842195216"><td class="cellrowborder" valign="top" width="19.85%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0053158693_p839991012531"><a name="en-us_topic_0053158693_p839991012531"></a><a name="en-us_topic_0053158693_p839991012531"></a>flavor</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.39%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0053158693_p12402210155311"><a name="en-us_topic_0053158693_p12402210155311"></a><a name="en-us_topic_0053158693_p12402210155311"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.75%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0053158693_p15406610135318"><a name="en-us_topic_0053158693_p15406610135318"></a><a name="en-us_topic_0053158693_p15406610135318"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.010000000000005%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0053158693_p1040881015311"><a name="en-us_topic_0053158693_p1040881015311"></a><a name="en-us_topic_0053158693_p1040881015311"></a>Specifies the flavor ID.</p>
    <p id="en-us_topic_0053158693_p7741128113511"><a name="en-us_topic_0053158693_p7741128113511"></a><a name="en-us_topic_0053158693_p7741128113511"></a>You can obtain the flavor ID from the <span id="en-us_topic_0053158693_text9235625735"><a name="en-us_topic_0053158693_text9235625735"></a><a name="en-us_topic_0053158693_text9235625735"></a>BMS</span><span id="en-us_topic_0053158693_text32351725734"><a name="en-us_topic_0053158693_text32351725734"></a><a name="en-us_topic_0053158693_text32351725734"></a></span> console or using the <a href="querying-bms-flavors-(native-openstack-api).md">Querying BMS Flavors (Native OpenStack API)</a> API.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0053158693_row058811420527"><td class="cellrowborder" valign="top" width="19.85%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0053158693_p5413201085313"><a name="en-us_topic_0053158693_p5413201085313"></a><a name="en-us_topic_0053158693_p5413201085313"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.39%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0053158693_p1941781012535"><a name="en-us_topic_0053158693_p1941781012535"></a><a name="en-us_topic_0053158693_p1941781012535"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.75%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0053158693_p3422121055318"><a name="en-us_topic_0053158693_p3422121055318"></a><a name="en-us_topic_0053158693_p3422121055318"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.010000000000005%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0053158693_p842631015536"><a name="en-us_topic_0053158693_p842631015536"></a><a name="en-us_topic_0053158693_p842631015536"></a>Specifies the <span id="en-us_topic_0053158693_text13209132811312"><a name="en-us_topic_0053158693_text13209132811312"></a><a name="en-us_topic_0053158693_text13209132811312"></a>BMS</span><span id="en-us_topic_0053158693_text920922816319"><a name="en-us_topic_0053158693_text920922816319"></a><a name="en-us_topic_0053158693_text920922816319"></a></span> name. This parameter supports fuzzy matching.</p>
    <p id="en-us_topic_0053158693_p7429181015313"><a name="en-us_topic_0053158693_p7429181015313"></a><a name="en-us_topic_0053158693_p7429181015313"></a>For example, the regular expression <strong id="en-us_topic_0053158693_b84235270616859"><a name="en-us_topic_0053158693_b84235270616859"></a><a name="en-us_topic_0053158693_b84235270616859"></a>?name=bob</strong> will return both <strong id="en-us_topic_0053158693_b84235270616910"><a name="en-us_topic_0053158693_b84235270616910"></a><a name="en-us_topic_0053158693_b84235270616910"></a>bob</strong> and <strong id="en-us_topic_0053158693_b84235270616915"><a name="en-us_topic_0053158693_b84235270616915"></a><a name="en-us_topic_0053158693_b84235270616915"></a>bobb</strong>. To obtain only <strong id="en-us_topic_0053158693_b84235270616107"><a name="en-us_topic_0053158693_b84235270616107"></a><a name="en-us_topic_0053158693_b84235270616107"></a>bob</strong>, you can use a regular expression matching the basic database syntax, such as MySQL or PostgreSQL (official website: <a href="https://www.postgresql.org/docs/9.2/static/functions-matching.html" target="_blank" rel="noopener noreferrer">https://www.postgresql.org/docs/9.2/static/functions-matching.html</a>).</p>
    </td>
    </tr>
    <tr id="en-us_topic_0053158693_row105881642195217"><td class="cellrowborder" valign="top" width="19.85%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0053158693_p1743421075315"><a name="en-us_topic_0053158693_p1743421075315"></a><a name="en-us_topic_0053158693_p1743421075315"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.39%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0053158693_p843711020539"><a name="en-us_topic_0053158693_p843711020539"></a><a name="en-us_topic_0053158693_p843711020539"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.75%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0053158693_p11440101010537"><a name="en-us_topic_0053158693_p11440101010537"></a><a name="en-us_topic_0053158693_p11440101010537"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.010000000000005%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0053158693_p7441161020531"><a name="en-us_topic_0053158693_p7441161020531"></a><a name="en-us_topic_0053158693_p7441161020531"></a>Specifies the <span id="en-us_topic_0053158693_text4817131535"><a name="en-us_topic_0053158693_text4817131535"></a><a name="en-us_topic_0053158693_text4817131535"></a>BMS</span><span id="en-us_topic_0053158693_text1781773117312"><a name="en-us_topic_0053158693_text1781773117312"></a><a name="en-us_topic_0053158693_text1781773117312"></a></span> status.</p>
    <p id="en-us_topic_0053158693_p117067951617"><a name="en-us_topic_0053158693_p117067951617"></a><a name="en-us_topic_0053158693_p117067951617"></a>Value range:</p>
    <a name="en-us_topic_0053158693_ul29109448426"></a><a name="en-us_topic_0053158693_ul29109448426"></a><ul id="en-us_topic_0053158693_ul29109448426"><li><strong id="en-us_topic_0053158693_en-us_topic_0113746489_b23014110118"><a name="en-us_topic_0053158693_en-us_topic_0113746489_b23014110118"></a><a name="en-us_topic_0053158693_en-us_topic_0113746489_b23014110118"></a>ACTIVE</strong>: Running, Stopping, Deleting</li><li><strong id="en-us_topic_0053158693_en-us_topic_0113746489_b56772617123"><a name="en-us_topic_0053158693_en-us_topic_0113746489_b56772617123"></a><a name="en-us_topic_0053158693_en-us_topic_0113746489_b56772617123"></a>BUILD</strong>: Creating</li><li><strong id="en-us_topic_0053158693_en-us_topic_0113746489_b2334141210"><a name="en-us_topic_0053158693_en-us_topic_0113746489_b2334141210"></a><a name="en-us_topic_0053158693_en-us_topic_0113746489_b2334141210"></a>ERROR</strong>: Faulty</li><li><strong id="en-us_topic_0053158693_en-us_topic_0113746489_b1059115316129"><a name="en-us_topic_0053158693_en-us_topic_0113746489_b1059115316129"></a><a name="en-us_topic_0053158693_en-us_topic_0113746489_b1059115316129"></a>HARD_REBOOT</strong>: Forcibly Restarting</li><li><strong id="en-us_topic_0053158693_en-us_topic_0113746489_b391019910131"><a name="en-us_topic_0053158693_en-us_topic_0113746489_b391019910131"></a><a name="en-us_topic_0053158693_en-us_topic_0113746489_b391019910131"></a>REBOOT</strong>: Restarting</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0053158693_row16588142145219"><td class="cellrowborder" valign="top" width="19.85%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0053158693_p1445843114279"><a name="en-us_topic_0053158693_p1445843114279"></a><a name="en-us_topic_0053158693_p1445843114279"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.39%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0053158693_p15457103122713"><a name="en-us_topic_0053158693_p15457103122713"></a><a name="en-us_topic_0053158693_p15457103122713"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.75%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0053158693_p15455113112714"><a name="en-us_topic_0053158693_p15455113112714"></a><a name="en-us_topic_0053158693_p15455113112714"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.010000000000005%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0053158693_p345110316275"><a name="en-us_topic_0053158693_p345110316275"></a><a name="en-us_topic_0053158693_p345110316275"></a>Specifies the number of <span id="en-us_topic_0053158693_text59831335739"><a name="en-us_topic_0053158693_text59831335739"></a><a name="en-us_topic_0053158693_text59831335739"></a>BMS</span><span id="en-us_topic_0053158693_text1098373515319"><a name="en-us_topic_0053158693_text1098373515319"></a><a name="en-us_topic_0053158693_text1098373515319"></a></span>s displayed on each page.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0053158693_row12307152919453"><td class="cellrowborder" valign="top" width="19.85%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0053158693_p34602410233"><a name="en-us_topic_0053158693_p34602410233"></a><a name="en-us_topic_0053158693_p34602410233"></a>marker</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.39%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0053158693_p1946094112310"><a name="en-us_topic_0053158693_p1946094112310"></a><a name="en-us_topic_0053158693_p1946094112310"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.75%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0053158693_p14460249231"><a name="en-us_topic_0053158693_p14460249231"></a><a name="en-us_topic_0053158693_p14460249231"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.010000000000005%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0053158693_p174601046239"><a name="en-us_topic_0053158693_p174601046239"></a><a name="en-us_topic_0053158693_p174601046239"></a>Specifies the <span id="en-us_topic_0053158693_text71323381731"><a name="en-us_topic_0053158693_text71323381731"></a><a name="en-us_topic_0053158693_text71323381731"></a>BMS</span><span id="en-us_topic_0053158693_text613212389311"><a name="en-us_topic_0053158693_text613212389311"></a><a name="en-us_topic_0053158693_text613212389311"></a></span> ID to which the marker corresponds. The query will start from the next ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0053158693_row14320610478"><td class="cellrowborder" valign="top" width="19.85%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0053158693_p5324615479"><a name="en-us_topic_0053158693_p5324615479"></a><a name="en-us_topic_0053158693_p5324615479"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.39%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0053158693_p143218664715"><a name="en-us_topic_0053158693_p143218664715"></a><a name="en-us_topic_0053158693_p143218664715"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.75%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0053158693_p143211619479"><a name="en-us_topic_0053158693_p143211619479"></a><a name="en-us_topic_0053158693_p143211619479"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.010000000000005%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0053158693_p123246194714"><a name="en-us_topic_0053158693_p123246194714"></a><a name="en-us_topic_0053158693_p123246194714"></a>Queries the <span id="en-us_topic_0053158693_text142391140333"><a name="en-us_topic_0053158693_text142391140333"></a><a name="en-us_topic_0053158693_text142391140333"></a>BMS</span><span id="en-us_topic_0053158693_text162393401630"><a name="en-us_topic_0053158693_text162393401630"></a><a name="en-us_topic_0053158693_text162393401630"></a></span>s with specified tags.</p>
    <p id="en-us_topic_0053158693_p12820165216471"><a name="en-us_topic_0053158693_p12820165216471"></a><a name="en-us_topic_0053158693_p12820165216471"></a>Added in micro version 2.26.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0053158693_row1658884211523"><td class="cellrowborder" valign="top" width="19.85%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0053158693_p203418324539"><a name="en-us_topic_0053158693_p203418324539"></a><a name="en-us_topic_0053158693_p203418324539"></a>not-tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.39%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0053158693_p173673215532"><a name="en-us_topic_0053158693_p173673215532"></a><a name="en-us_topic_0053158693_p173673215532"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.75%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0053158693_p238132105317"><a name="en-us_topic_0053158693_p238132105317"></a><a name="en-us_topic_0053158693_p238132105317"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.010000000000005%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0053158693_p154313328536"><a name="en-us_topic_0053158693_p154313328536"></a><a name="en-us_topic_0053158693_p154313328536"></a>Queries the <span id="en-us_topic_0053158693_text179892421232"><a name="en-us_topic_0053158693_text179892421232"></a><a name="en-us_topic_0053158693_text179892421232"></a>BMS</span><span id="en-us_topic_0053158693_text149891342231"><a name="en-us_topic_0053158693_text149891342231"></a><a name="en-us_topic_0053158693_text149891342231"></a></span>s with tags not containing the specified value. The value is a list of tag keys.</p>
    <div class="note" id="en-us_topic_0053158693_note124521913175616"><a name="en-us_topic_0053158693_note124521913175616"></a><a name="en-us_topic_0053158693_note124521913175616"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0053158693_p1745221311560"><a name="en-us_topic_0053158693_p1745221311560"></a><a name="en-us_topic_0053158693_p1745221311560"></a>If the tags added before the function upgrade are in the format of "Key.Value", query tags using "Key".</p>
    <p id="en-us_topic_0053158693_p213418685710"><a name="en-us_topic_0053158693_p213418685710"></a><a name="en-us_topic_0053158693_p213418685710"></a>For example, an existing tag is <strong id="en-us_topic_0053158693_b84235270610509"><a name="en-us_topic_0053158693_b84235270610509"></a><a name="en-us_topic_0053158693_b84235270610509"></a>a.b</strong>. After the tag function upgrade, query the tag using "not-tags=a".</p>
    </div></div>
    <p id="en-us_topic_0053158693_p19441232135317"><a name="en-us_topic_0053158693_p19441232135317"></a><a name="en-us_topic_0053158693_p19441232135317"></a>Added in micro version 2.26.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0053158693_row1158812424528"><td class="cellrowborder" valign="top" width="19.85%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0053158693_p184717323539"><a name="en-us_topic_0053158693_p184717323539"></a><a name="en-us_topic_0053158693_p184717323539"></a>reservation_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.39%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0053158693_p1650832195311"><a name="en-us_topic_0053158693_p1650832195311"></a><a name="en-us_topic_0053158693_p1650832195311"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.75%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0053158693_p1453143220535"><a name="en-us_topic_0053158693_p1453143220535"></a><a name="en-us_topic_0053158693_p1453143220535"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.010000000000005%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0053158693_p5551832185311"><a name="en-us_topic_0053158693_p5551832185311"></a><a name="en-us_topic_0053158693_p5551832185311"></a>Specifies the reserved ID, which can be used to query <span id="en-us_topic_0053158693_text63205019314"><a name="en-us_topic_0053158693_text63205019314"></a><a name="en-us_topic_0053158693_text63205019314"></a>BMS</span><span id="en-us_topic_0053158693_text734501833"><a name="en-us_topic_0053158693_text734501833"></a><a name="en-us_topic_0053158693_text734501833"></a></span>s created in a batch.</p>
    <p id="en-us_topic_0053158693_p45753218534"><a name="en-us_topic_0053158693_p45753218534"></a><a name="en-us_topic_0053158693_p45753218534"></a>Added in micro version 2.26.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0053158693_row1758864217526"><td class="cellrowborder" valign="top" width="19.85%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0053158693_p10633321531"><a name="en-us_topic_0053158693_p10633321531"></a><a name="en-us_topic_0053158693_p10633321531"></a>sort_key</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.39%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0053158693_p106613212531"><a name="en-us_topic_0053158693_p106613212531"></a><a name="en-us_topic_0053158693_p106613212531"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.75%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0053158693_p196963275311"><a name="en-us_topic_0053158693_p196963275311"></a><a name="en-us_topic_0053158693_p196963275311"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.010000000000005%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0053158693_p167133212536"><a name="en-us_topic_0053158693_p167133212536"></a><a name="en-us_topic_0053158693_p167133212536"></a>Specifies the BMS sorting attribute, which can be the <span id="en-us_topic_0053158693_text62627567316"><a name="en-us_topic_0053158693_text62627567316"></a><a name="en-us_topic_0053158693_text62627567316"></a>BMS</span><span id="en-us_topic_0053158693_text1726217563313"><a name="en-us_topic_0053158693_text1726217563313"></a><a name="en-us_topic_0053158693_text1726217563313"></a></span> UUID (<strong id="en-us_topic_0053158693_b1735217112617"><a name="en-us_topic_0053158693_b1735217112617"></a><a name="en-us_topic_0053158693_b1735217112617"></a>uuid</strong>), <span id="en-us_topic_0053158693_text142381559638"><a name="en-us_topic_0053158693_text142381559638"></a><a name="en-us_topic_0053158693_text142381559638"></a>BMS</span><span id="en-us_topic_0053158693_text22392599316"><a name="en-us_topic_0053158693_text22392599316"></a><a name="en-us_topic_0053158693_text22392599316"></a></span> status (<strong id="en-us_topic_0053158693_b575761619614"><a name="en-us_topic_0053158693_b575761619614"></a><a name="en-us_topic_0053158693_b575761619614"></a>vm_state</strong>), <span id="en-us_topic_0053158693_text135136112411"><a name="en-us_topic_0053158693_text135136112411"></a><a name="en-us_topic_0053158693_text135136112411"></a>BMS</span><span id="en-us_topic_0053158693_text6513116415"><a name="en-us_topic_0053158693_text6513116415"></a><a name="en-us_topic_0053158693_text6513116415"></a></span> name (<strong id="en-us_topic_0053158693_b027110341562"><a name="en-us_topic_0053158693_b027110341562"></a><a name="en-us_topic_0053158693_b027110341562"></a>display_name</strong>), <span id="en-us_topic_0053158693_text1810916516416"><a name="en-us_topic_0053158693_text1810916516416"></a><a name="en-us_topic_0053158693_text1810916516416"></a>BMS</span><span id="en-us_topic_0053158693_text17109175241"><a name="en-us_topic_0053158693_text17109175241"></a><a name="en-us_topic_0053158693_text17109175241"></a></span> task status (<strong id="en-us_topic_0053158693_b145994513618"><a name="en-us_topic_0053158693_b145994513618"></a><a name="en-us_topic_0053158693_b145994513618"></a>task_state</strong>), power status (<strong id="en-us_topic_0053158693_b9292451066"><a name="en-us_topic_0053158693_b9292451066"></a><a name="en-us_topic_0053158693_b9292451066"></a>power_state</strong>), creation time (<strong id="en-us_topic_0053158693_b30356567"><a name="en-us_topic_0053158693_b30356567"></a><a name="en-us_topic_0053158693_b30356567"></a>created_at</strong>), last time when the <span id="en-us_topic_0053158693_text1058920618712"><a name="en-us_topic_0053158693_text1058920618712"></a><a name="en-us_topic_0053158693_text1058920618712"></a>BMS</span><span id="en-us_topic_0053158693_text1059536977"><a name="en-us_topic_0053158693_text1059536977"></a><a name="en-us_topic_0053158693_text1059536977"></a></span> is updated (<strong id="en-us_topic_0053158693_b9391131672"><a name="en-us_topic_0053158693_b9391131672"></a><a name="en-us_topic_0053158693_b9391131672"></a>updated_at</strong>), and AZ (<strong id="en-us_topic_0053158693_b198324171673"><a name="en-us_topic_0053158693_b198324171673"></a><a name="en-us_topic_0053158693_b198324171673"></a>availability_zone</strong>). You can specify multiple <strong id="en-us_topic_0053158693_b8423527061280"><a name="en-us_topic_0053158693_b8423527061280"></a><a name="en-us_topic_0053158693_b8423527061280"></a>sort_key</strong> and <strong id="en-us_topic_0053158693_b8423527061289"><a name="en-us_topic_0053158693_b8423527061289"></a><a name="en-us_topic_0053158693_b8423527061289"></a>sort_dir</strong> pairs.</p>
    <p id="en-us_topic_0053158693_p1321581482211"><a name="en-us_topic_0053158693_p1321581482211"></a><a name="en-us_topic_0053158693_p1321581482211"></a>The default sorting is the reverse order by <strong id="en-us_topic_0053158693_b6725857464"><a name="en-us_topic_0053158693_b6725857464"></a><a name="en-us_topic_0053158693_b6725857464"></a>created_at</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0053158693_row135891242165217"><td class="cellrowborder" valign="top" width="19.85%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0053158693_p1327414444539"><a name="en-us_topic_0053158693_p1327414444539"></a><a name="en-us_topic_0053158693_p1327414444539"></a>sort_dir</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.39%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0053158693_p16275104445317"><a name="en-us_topic_0053158693_p16275104445317"></a><a name="en-us_topic_0053158693_p16275104445317"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.75%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0053158693_p202804443536"><a name="en-us_topic_0053158693_p202804443536"></a><a name="en-us_topic_0053158693_p202804443536"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.010000000000005%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0053158693_p15283154425314"><a name="en-us_topic_0053158693_p15283154425314"></a><a name="en-us_topic_0053158693_p15283154425314"></a>Specifies the sorting direction.</p>
    <a name="en-us_topic_0053158693_ul22858441530"></a><a name="en-us_topic_0053158693_ul22858441530"></a><ul id="en-us_topic_0053158693_ul22858441530"><li><strong id="en-us_topic_0053158693_b2483023315742"><a name="en-us_topic_0053158693_b2483023315742"></a><a name="en-us_topic_0053158693_b2483023315742"></a>asc</strong>: The query results are displayed in ascending order.</li><li><strong id="en-us_topic_0053158693_b191712644011"><a name="en-us_topic_0053158693_b191712644011"></a><a name="en-us_topic_0053158693_b191712644011"></a>desc</strong> (default value): The query results are displayed in descending order.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request
    -   With no optional parameter

        ```
        https://{ECS Endpoint}/v2.1/bbf1946d374b44a0a2a95533562ba954/servers/detail
        ```

    -   With an optional parameter

        ```
        https://{ECS Endpoint}/v2.1/bbf1946d374b44a0a2a95533562ba954/servers/detail?tags=__type_baremetal
        ```

    -   With multiple optional parameters

        ```
        https://{ECS Endpoint}/v2.1/bbf1946d374b44a0a2a95533562ba954/servers/detail?tags=__type_baremetal&name=bms-test01
        ```



## Response Message<a name="section17727455"></a>

-   Response parameters

    <a name="table61256692"></a>
    <table><thead align="left"><tr id="row16697504"><th class="cellrowborder" valign="top" width="17.86%" id="mcps1.1.4.1.1"><p id="p59978491115233"><a name="p59978491115233"></a><a name="p59978491115233"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.1.4.1.2"><p id="p26419641115233"><a name="p26419641115233"></a><a name="p26419641115233"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="32.14%" id="mcps1.1.4.1.3"><p id="p64181866115233"><a name="p64181866115233"></a><a name="p64181866115233"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row64050727"><td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.1.4.1.1 "><p id="p20726409"><a name="p20726409"></a><a name="p20726409"></a>servers</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.4.1.2 "><p id="p491044173818"><a name="p491044173818"></a><a name="p491044173818"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.14%" headers="mcps1.1.4.1.3 "><p id="p24702645"><a name="p24702645"></a><a name="p24702645"></a>Specifies details about the <span id="text56791793514"><a name="text56791793514"></a><a name="text56791793514"></a>BMS</span><span id="text06791091752"><a name="text06791091752"></a><a name="text06791091752"></a></span>. For details, see <a href="querying-details-about-a-bms-(native-openstack-api).md#table6149040">Table 2</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "servers": [
    {
                "tenant_id": "c685484a8cc2416b97260938705deb64",
                "addresses": {
                    "08a7715f-7de6-4ff9-a343-95ba4209f24a": [
    {
                            "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:0e:c4:77",
                            "OS-EXT-IPS:type": "fixed",
                            "addr": "192.168.0.107",
                            "version": 4
                        }
                    ]
                },
                "metadata": {
                    "op_svc_userid": "1311c433dd9b408886f57d695c229cbe"
                },
                "OS-EXT-STS:task_state": null,
                "OS-DCF:diskConfig": "MANUAL",
                "OS-EXT-AZ:availability_zone": "az-dc-1",
                "links": [
    {
                        "rel": "self",
                        "href": "https://openstack.example.com/v2.1/c685484a8cc2416b97260938705deb65/servers/95bf2490-5428-432c-ad9b-5e3406f869dd"
                    },
    {
                        "rel": "bookmark",
                        "href": "https://openstack.example.com/c685484a8cc2416b97260938705deb65/servers/95bf2490-5428-432c-ad9b-5e3406f869dd"
                        }
                ],
                "OS-EXT-STS:power_state": 1,
                "id": "95bf2490-5428-432c-ad9b-5e3406f869dd",
                "os-extended-volumes:volumes_attached": [
    {
                        "id": "dfa375b5-9856-44ad-a937-a4802b6434c3"
                    },
    {
                        "id": "bb9f1b27-843b-4561-b62e-ca18eeaec417"
                    },
    {
                        "id": "86e801c3-acc6-465d-890c-d43ba493f553"
                    },
    {
                        "id": "0994d3ac-3c6a-495c-a439-c597a4f08fa6"
                        }
                ],
                "OS-EXT-SRV-ATTR:host": "bms.az1",
                "image": {
                    "links": [
    {
                            "rel": "bookmark",
                            "href": "https://openstack.example.com/c685484a8cc2416b97260938705deb65/images/1a6635d8-afea-4f2b-abb6-27a202bad319"
                        }
                    ],
                    "id": "1a6635d8-afea-4f2b-abb6-27a202bad319"
                },
                "OS-SRV-USG:terminated_at": null,
                "accessIPv4": "",
                "accessIPv6": "",
                "created": "2017-05-24T06:14:05Z",
                "hostId": "e9c3ee0fcc58ab6085cf30df70b5544eab958858fb50d925f023e53e",
                "OS-EXT-SRV-ATTR:hypervisor_hostname": "nova004@2",
                "key_name": "KeyPair-JX",
                "flavor": {
                    "links": [
    {
                            "rel": "bookmark",
                            "href": "https://openstack.example.com/c685484a8cc2416b97260938705deb65/flavors/physical.83.medium"
                        }
                    ],
                    "id": "physical.83.medium"
                },
                "security_groups": [
    {
                        "name": "0011b620-4982-42e4-ad12-47c95ca495c4"
                        }
                ],
                "config_drive": "",
                "OS-EXT-STS:vm_state": "active",
                "OS-EXT-SRV-ATTR:instance_name": "instance-0000ebd3",
                "user_id": "1311c433dd9b408886f57d695c229cbe",
                "name": "bms",
                "progress": 0, 
                "OS-SRV-USG:launched_at": "2017-05-25T03:40:25.066078",
                "updated": "2017-05-25T03:40:25Z",
                "status": "ACTIVE"
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

