# Querying Load Balancers by Tag<a name="EN-US_TOPIC_0109852829"></a>

## Function<a name="en-us_topic_0101985068_section26892385111837"></a>

This API is used to query load balancers using tags.

## URI<a name="en-us_topic_0101985068_section12799799112015"></a>

POST /v2.0/\{project\_id\}/loadbalancers/resource\_instances/action

**Table  1**  Parameter description

<a name="table33323423"></a>
<table><thead align="left"><tr id="row8420641"><th class="cellrowborder" valign="top" width="11%" id="mcps1.2.5.1.1"><p id="p10983320"><a name="p10983320"></a><a name="p10983320"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.2"><p id="p17233719"><a name="p17233719"></a><a name="p17233719"></a><strong id="en-us_topic_0101985068_b84235270616735"><a name="en-us_topic_0101985068_b84235270616735"></a><a name="en-us_topic_0101985068_b84235270616735"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p4164548117122"><a name="p4164548117122"></a><a name="p4164548117122"></a><strong id="en-us_topic_0101985068_b842352706151111"><a name="en-us_topic_0101985068_b842352706151111"></a><a name="en-us_topic_0101985068_b842352706151111"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="62%" id="mcps1.2.5.1.4"><p id="p53754023"><a name="p53754023"></a><a name="p53754023"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row53906008171138"><td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.1 "><p id="p16126074171144"><a name="p16126074171144"></a><a name="p16126074171144"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p31143627171144"><a name="p31143627171144"></a><a name="p31143627171144"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p39605860171144"><a name="p39605860171144"></a><a name="p39605860171144"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.5.1.4 "><p id="p11184131"><a name="p11184131"></a><a name="p11184131"></a>Specifies the ID of the project where the tag is used.</p>
<p id="p8222164914610"><a name="p8222164914610"></a><a name="p8222164914610"></a></p>
</td>
</tr>
</tbody>
</table>

## Constraints<a name="en-us_topic_0101985068_section27305719113118"></a>

None

## Request<a name="en-us_topic_0101985068_section49859218113148"></a>

**Table  2**  Request parameters

<a name="en-us_topic_0101985068_table8367729113248"></a>
<table><thead align="left"><tr id="en-us_topic_0101985068_row43833417113248"><th class="cellrowborder" valign="top" width="11.111111111111112%" id="mcps1.2.5.1.1"><p id="en-us_topic_0101985068_p536598411333"><a name="en-us_topic_0101985068_p536598411333"></a><a name="en-us_topic_0101985068_p536598411333"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="12.121212121212121%" id="mcps1.2.5.1.2"><p id="en-us_topic_0101985068_p3199158711333"><a name="en-us_topic_0101985068_p3199158711333"></a><a name="en-us_topic_0101985068_p3199158711333"></a><strong id="b215354160"><a name="b215354160"></a><a name="b215354160"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.151515151515152%" id="mcps1.2.5.1.3"><p id="en-us_topic_0101985068_p4118173411333"><a name="en-us_topic_0101985068_p4118173411333"></a><a name="en-us_topic_0101985068_p4118173411333"></a><strong id="b848880367"><a name="b848880367"></a><a name="b848880367"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="61.61616161616161%" id="mcps1.2.5.1.4"><p id="en-us_topic_0101985068_p4738612911333"><a name="en-us_topic_0101985068_p4738612911333"></a><a name="en-us_topic_0101985068_p4738612911333"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0101985068_row41902111113248"><td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0101985068_p5213792111333"><a name="en-us_topic_0101985068_p5213792111333"></a><a name="en-us_topic_0101985068_p5213792111333"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0101985068_p6242210211333"><a name="en-us_topic_0101985068_p6242210211333"></a><a name="en-us_topic_0101985068_p6242210211333"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0101983303_p4459890810595"><a name="en-us_topic_0101983303_p4459890810595"></a><a name="en-us_topic_0101983303_p4459890810595"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="61.61616161616161%" headers="mcps1.2.5.1.4 "><p id="p1278512512915"><a name="p1278512512915"></a><a name="p1278512512915"></a>Specifies the included tags. A maximum of 10 keys are allowed for each query operation, and each key can have a maximum of 10 values.</p>
<p id="p128391286914"><a name="p128391286914"></a><a name="p128391286914"></a>The tag key cannot be left blank or set to an empty string.</p>
<p id="en-us_topic_0101985068_p5312813011333"><a name="en-us_topic_0101985068_p5312813011333"></a><a name="en-us_topic_0101985068_p5312813011333"></a>Each tag key and each tag value of the same tag key must be unique.</p>
</td>
</tr>
<tr id="en-us_topic_0101985068_row51668533113248"><td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0101985068_p859230011333"><a name="en-us_topic_0101985068_p859230011333"></a><a name="en-us_topic_0101985068_p859230011333"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0101985068_p2488769011333"><a name="en-us_topic_0101985068_p2488769011333"></a><a name="en-us_topic_0101985068_p2488769011333"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0101985068_p263701311333"><a name="en-us_topic_0101985068_p263701311333"></a><a name="en-us_topic_0101985068_p263701311333"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61.61616161616161%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0101985068_p1227147611333"><a name="en-us_topic_0101985068_p1227147611333"></a><a name="en-us_topic_0101985068_p1227147611333"></a>Sets the page size. This parameter is available when <strong id="b1114712095155210"><a name="b1114712095155210"></a><a name="b1114712095155210"></a>action</strong> is set to <strong id="b830806447155210"><a name="b830806447155210"></a><a name="b830806447155210"></a>filter</strong>. Both the default value and maximum value are <strong id="b149466305155210"><a name="b149466305155210"></a><a name="b149466305155210"></a>1000</strong>, and the minimum value is <strong id="b2079801414155210"><a name="b2079801414155210"></a><a name="b2079801414155210"></a>1</strong>. The value cannot be a negative integer.</p>
</td>
</tr>
<tr id="en-us_topic_0101985068_row32324594113248"><td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0101985068_p2042734411333"><a name="en-us_topic_0101985068_p2042734411333"></a><a name="en-us_topic_0101985068_p2042734411333"></a>offset</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0101985068_p4400212911333"><a name="en-us_topic_0101985068_p4400212911333"></a><a name="en-us_topic_0101985068_p4400212911333"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0101985068_p740269111333"><a name="en-us_topic_0101985068_p740269111333"></a><a name="en-us_topic_0101985068_p740269111333"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61.61616161616161%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0101985068_p10755812145954"><a name="en-us_topic_0101985068_p10755812145954"></a><a name="en-us_topic_0101985068_p10755812145954"></a>Specifies the index position. The query starts from the next load balancer indexed by this parameter. This parameter is not required when you query load balancers on the first page. The value in the response returned for querying the load balancers on the previous page will be included in this parameter for querying the load balancers on subsequent pages. This parameter is not available when <strong id="b1091458401155259"><a name="b1091458401155259"></a><a name="b1091458401155259"></a>action</strong> is set to <strong id="b689865490155259"><a name="b689865490155259"></a><a name="b689865490155259"></a>count</strong>. If <strong id="b425781242155259"><a name="b425781242155259"></a><a name="b425781242155259"></a>action</strong> is set to <strong id="b418074720155259"><a name="b418074720155259"></a><a name="b418074720155259"></a>filter</strong>, the value must be a positive integer, and the default value is <strong id="b1892680631155259"><a name="b1892680631155259"></a><a name="b1892680631155259"></a>0</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0101985068_row28664513113248"><td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0101985068_p4148911711333"><a name="en-us_topic_0101985068_p4148911711333"></a><a name="en-us_topic_0101985068_p4148911711333"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0101985068_p517534011333"><a name="en-us_topic_0101985068_p517534011333"></a><a name="en-us_topic_0101985068_p517534011333"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0101985068_p1654939111333"><a name="en-us_topic_0101985068_p1654939111333"></a><a name="en-us_topic_0101985068_p1654939111333"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61.61616161616161%" headers="mcps1.2.5.1.4 "><p id="p580055365520"><a name="p580055365520"></a><a name="p580055365520"></a>Identifies the operation. The value can be <strong id="b14800653115510"><a name="b14800653115510"></a><a name="b14800653115510"></a>filter</strong> or <strong id="b5800145315519"><a name="b5800145315519"></a><a name="b5800145315519"></a>count</strong>.</p>
<p id="p175411162566"><a name="p175411162566"></a><a name="p175411162566"></a><strong id="b1554111695612"><a name="b1554111695612"></a><a name="b1554111695612"></a>filter</strong>: indicates pagination query.</p>
<p id="en-us_topic_0101985068_p6543230311333"><a name="en-us_topic_0101985068_p6543230311333"></a><a name="en-us_topic_0101985068_p6543230311333"></a><strong id="b1467249206155350"><a name="b1467249206155350"></a><a name="b1467249206155350"></a>count</strong>: indicates that all load balancers meeting the search criteria will be returned.</p>
</td>
</tr>
<tr id="en-us_topic_0101985068_row17840786113248"><td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0101985068_p593862811333"><a name="en-us_topic_0101985068_p593862811333"></a><a name="en-us_topic_0101985068_p593862811333"></a>matches</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0101985068_p1126682511333"><a name="en-us_topic_0101985068_p1126682511333"></a><a name="en-us_topic_0101985068_p1126682511333"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p178180642815"><a name="p178180642815"></a><a name="p178180642815"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="61.61616161616161%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0101985068_p3478100911333"><a name="en-us_topic_0101985068_p3478100911333"></a><a name="en-us_topic_0101985068_p3478100911333"></a>Specifies the search criteria. The tag key is the parameter to match, for example, <strong id="b1815994217155439"><a name="b1815994217155439"></a><a name="b1815994217155439"></a>resource_name</strong>. <strong id="en-us_topic_0101985068_b842352706122736"><a name="en-us_topic_0101985068_b842352706122736"></a><a name="en-us_topic_0101985068_b842352706122736"></a>value</strong> indicates the matched value. The key is a fixed dictionary value.</p>
<p id="en-us_topic_0101985068_p5840073591254"><a name="en-us_topic_0101985068_p5840073591254"></a><a name="en-us_topic_0101985068_p5840073591254"></a>Currently, only <strong id="b1334412258573"><a name="b1334412258573"></a><a name="b1334412258573"></a>resource_name</strong> can be used for search. For details, see <a href="#en-us_topic_0101985068_table17701361113436">Table 4</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **tags**  parameter description

<a name="en-us_topic_0101985068_table7454577113348"></a>
<table><thead align="left"><tr id="en-us_topic_0101985068_row38752726113348"><th class="cellrowborder" valign="top" width="11%" id="mcps1.2.5.1.1"><p id="en-us_topic_0101985068_p43189747113359"><a name="en-us_topic_0101985068_p43189747113359"></a><a name="en-us_topic_0101985068_p43189747113359"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.2"><p id="en-us_topic_0101985068_p8708651113359"><a name="en-us_topic_0101985068_p8708651113359"></a><a name="en-us_topic_0101985068_p8708651113359"></a><strong id="b1249354661"><a name="b1249354661"></a><a name="b1249354661"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="en-us_topic_0101985068_p34312115113359"><a name="en-us_topic_0101985068_p34312115113359"></a><a name="en-us_topic_0101985068_p34312115113359"></a><strong id="b466745786"><a name="b466745786"></a><a name="b466745786"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="61%" id="mcps1.2.5.1.4"><p id="en-us_topic_0101985068_p27817907113359"><a name="en-us_topic_0101985068_p27817907113359"></a><a name="en-us_topic_0101985068_p27817907113359"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0101985068_row9570394113348"><td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0101985068_p44290621113359"><a name="en-us_topic_0101985068_p44290621113359"></a><a name="en-us_topic_0101985068_p44290621113359"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0101985068_p30770583113359"><a name="en-us_topic_0101985068_p30770583113359"></a><a name="en-us_topic_0101985068_p30770583113359"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0101985068_p9389322113359"><a name="en-us_topic_0101985068_p9389322113359"></a><a name="en-us_topic_0101985068_p9389322113359"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0101985068_p22337597113359"><a name="en-us_topic_0101985068_p22337597113359"></a><a name="en-us_topic_0101985068_p22337597113359"></a>Specifies the tag key. It contains a maximum of 127 Unicode characters and cannot be left blank. (This parameter is not verified in the search process.)</p>
</td>
</tr>
<tr id="en-us_topic_0101985068_row2555815113348"><td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0101985068_p43763228113359"><a name="en-us_topic_0101985068_p43763228113359"></a><a name="en-us_topic_0101985068_p43763228113359"></a>values</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0101985068_p55160616113359"><a name="en-us_topic_0101985068_p55160616113359"></a><a name="en-us_topic_0101985068_p55160616113359"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p1735071062819"><a name="p1735071062819"></a><a name="p1735071062819"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.5.1.4 "><p id="p58600025"><a name="p58600025"></a><a name="p58600025"></a>Lists the tag values. Each tag value can contain a maximum of 255 Unicode characters. The values are in the OR relationship.</p>
<p id="p3440173494517"><a name="p3440173494517"></a><a name="p3440173494517"></a>If no tag values in the list, the tag key is used for full search. If each value in the list starts with an asterisk (*), fuzzy match is performed based on the part after the asterisk.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **matches**  parameter description

<a name="en-us_topic_0101985068_table17701361113436"></a>
<table><thead align="left"><tr id="en-us_topic_0101985068_row51291081113436"><th class="cellrowborder" valign="top" width="11%" id="mcps1.2.5.1.1"><p id="en-us_topic_0101985068_p4040387911350"><a name="en-us_topic_0101985068_p4040387911350"></a><a name="en-us_topic_0101985068_p4040387911350"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.5.1.2"><p id="en-us_topic_0101985068_p5148878611350"><a name="en-us_topic_0101985068_p5148878611350"></a><a name="en-us_topic_0101985068_p5148878611350"></a><strong id="b846018967"><a name="b846018967"></a><a name="b846018967"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.3"><p id="en-us_topic_0101985068_p984215011350"><a name="en-us_topic_0101985068_p984215011350"></a><a name="en-us_topic_0101985068_p984215011350"></a><strong id="b1067542529"><a name="b1067542529"></a><a name="b1067542529"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="61%" id="mcps1.2.5.1.4"><p id="en-us_topic_0101985068_p5901664911350"><a name="en-us_topic_0101985068_p5901664911350"></a><a name="en-us_topic_0101985068_p5901664911350"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0101985068_row23733151113436"><td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0101985068_p5720393911350"><a name="en-us_topic_0101985068_p5720393911350"></a><a name="en-us_topic_0101985068_p5720393911350"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0101985068_p300746411350"><a name="en-us_topic_0101985068_p300746411350"></a><a name="en-us_topic_0101985068_p300746411350"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0101985068_p4227804611350"><a name="en-us_topic_0101985068_p4227804611350"></a><a name="en-us_topic_0101985068_p4227804611350"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.5.1.4 "><p id="p1490255131311"><a name="p1490255131311"></a><a name="p1490255131311"></a>Specifies the tag key for match.</p>
<p id="p1355213241415"><a name="p1355213241415"></a><a name="p1355213241415"></a>The value can be one of the following:</p>
<a name="ul538020471411"></a><a name="ul538020471411"></a><ul id="ul538020471411"><li><strong id="b99458594162"><a name="b99458594162"></a><a name="b99458594162"></a>resource_name</strong>: indicates the resource name.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0101985068_row21079477113436"><td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0101985068_p2663170711350"><a name="en-us_topic_0101985068_p2663170711350"></a><a name="en-us_topic_0101985068_p2663170711350"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0101985068_p968462111350"><a name="en-us_topic_0101985068_p968462111350"></a><a name="en-us_topic_0101985068_p968462111350"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0101985068_p4625685211350"><a name="en-us_topic_0101985068_p4625685211350"></a><a name="en-us_topic_0101985068_p4625685211350"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0101985068_p5581756011350"><a name="en-us_topic_0101985068_p5581756011350"></a><a name="en-us_topic_0101985068_p5581756011350"></a>Specifies the tag value for match. Each tag value can contain a maximum of 255 Unicode characters.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="en-us_topic_0101985068_section42444873113729"></a>

**Table  5**  Response parameters

<a name="en-us_topic_0101985068_table1619411411380"></a>
<table><thead align="left"><tr id="en-us_topic_0101985068_row1489458711380"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.1"><p id="en-us_topic_0101985068_p961931113812"><a name="en-us_topic_0101985068_p961931113812"></a><a name="en-us_topic_0101985068_p961931113812"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.2"><p id="en-us_topic_0101985068_p2996292113812"><a name="en-us_topic_0101985068_p2996292113812"></a><a name="en-us_topic_0101985068_p2996292113812"></a><strong id="b62212783"><a name="b62212783"></a><a name="b62212783"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="56.99999999999999%" id="mcps1.2.4.1.3"><p id="en-us_topic_0101985068_p41373128113812"><a name="en-us_topic_0101985068_p41373128113812"></a><a name="en-us_topic_0101985068_p41373128113812"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0101985068_row5969535711380"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0101985068_p60850085113812"><a name="en-us_topic_0101985068_p60850085113812"></a><a name="en-us_topic_0101985068_p60850085113812"></a>resources</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="p14789191332817"><a name="p14789191332817"></a><a name="p14789191332817"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0101985068_p12131870113812"><a name="en-us_topic_0101985068_p12131870113812"></a><a name="en-us_topic_0101985068_p12131870113812"></a>Lists the load balancers. For details, see <a href="#en-us_topic_0101985068_table19523872114014">Table 6</a>.</p>
</td>
</tr>
<tr id="en-us_topic_0101985068_row1166188011380"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0101985068_p52872252113812"><a name="en-us_topic_0101985068_p52872252113812"></a><a name="en-us_topic_0101985068_p52872252113812"></a>total_count</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0101985068_p9130341113812"><a name="en-us_topic_0101985068_p9130341113812"></a><a name="en-us_topic_0101985068_p9130341113812"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0101985068_p1360179113812"><a name="en-us_topic_0101985068_p1360179113812"></a><a name="en-us_topic_0101985068_p1360179113812"></a>Specifies the total number of queried records.</p>
</td>
</tr>
</tbody>
</table>

**Table  6** **resource**  parameter description

<a name="en-us_topic_0101985068_table19523872114014"></a>
<table><thead align="left"><tr id="en-us_topic_0101985068_row20749519114014"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.1"><p id="en-us_topic_0101985068_p18795200114045"><a name="en-us_topic_0101985068_p18795200114045"></a><a name="en-us_topic_0101985068_p18795200114045"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.2"><p id="en-us_topic_0101985068_p36327940114045"><a name="en-us_topic_0101985068_p36327940114045"></a><a name="en-us_topic_0101985068_p36327940114045"></a><strong id="b1630212615"><a name="b1630212615"></a><a name="b1630212615"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="56.99999999999999%" id="mcps1.2.4.1.3"><p id="en-us_topic_0101985068_p56882021114045"><a name="en-us_topic_0101985068_p56882021114045"></a><a name="en-us_topic_0101985068_p56882021114045"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0101985068_row59337252114014"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0101985068_p10547499114045"><a name="en-us_topic_0101985068_p10547499114045"></a><a name="en-us_topic_0101985068_p10547499114045"></a>resource_id</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0101985068_p12907908114045"><a name="en-us_topic_0101985068_p12907908114045"></a><a name="en-us_topic_0101985068_p12907908114045"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0101985068_p38907643114045"><a name="en-us_topic_0101985068_p38907643114045"></a><a name="en-us_topic_0101985068_p38907643114045"></a>Specifies the resource ID.</p>
</td>
</tr>
<tr id="en-us_topic_0101985068_row19801209114014"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0101985068_p43731755114045"><a name="en-us_topic_0101985068_p43731755114045"></a><a name="en-us_topic_0101985068_p43731755114045"></a>resource_detail</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0101985068_p33654350114045"><a name="en-us_topic_0101985068_p33654350114045"></a><a name="en-us_topic_0101985068_p33654350114045"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0101985068_p41647857114045"><a name="en-us_topic_0101985068_p41647857114045"></a><a name="en-us_topic_0101985068_p41647857114045"></a>Specifies the resource details. The value is a resource object, used for extension. The value is left blank by default.</p>
</td>
</tr>
<tr id="en-us_topic_0101985068_row21106477114014"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0101985068_p28081397114045"><a name="en-us_topic_0101985068_p28081397114045"></a><a name="en-us_topic_0101985068_p28081397114045"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="p13540121516286"><a name="p13540121516286"></a><a name="p13540121516286"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0101985068_p3786126114045"><a name="en-us_topic_0101985068_p3786126114045"></a><a name="en-us_topic_0101985068_p3786126114045"></a>Lists the tags. If there is no tag, an empty array is used by default. For details, see <a href="#table15683233145412">Table 7</a>.</p>
</td>
</tr>
<tr id="en-us_topic_0101985068_row15996779114014"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0101985068_p8622978114045"><a name="en-us_topic_0101985068_p8622978114045"></a><a name="en-us_topic_0101985068_p8622978114045"></a>resource_name</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0101985068_p2587446114045"><a name="en-us_topic_0101985068_p2587446114045"></a><a name="en-us_topic_0101985068_p2587446114045"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0101985068_p8256573114045"><a name="en-us_topic_0101985068_p8256573114045"></a><a name="en-us_topic_0101985068_p8256573114045"></a>Specifies the resource name. This parameter is an empty string by default if there is no resource name.</p>
</td>
</tr>
</tbody>
</table>

**Table  7** **tags**  parameter description

<a name="table15683233145412"></a>
<table><thead align="left"><tr id="row12684733125410"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.1"><p id="p5684933185414"><a name="p5684933185414"></a><a name="p5684933185414"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.2"><p id="p36841533155417"><a name="p36841533155417"></a><a name="p36841533155417"></a><strong id="b920109721"><a name="b920109721"></a><a name="b920109721"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="57.99999999999999%" id="mcps1.2.4.1.3"><p id="p3684153320546"><a name="p3684153320546"></a><a name="p3684153320546"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1668411338548"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p1684193355413"><a name="p1684193355413"></a><a name="p1684193355413"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p9684173325410"><a name="p9684173325410"></a><a name="p9684173325410"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p13684143310547"><a name="p13684143310547"></a><a name="p13684143310547"></a>Specifies the tag key. It contains a maximum of 127 Unicode characters and cannot be left blank. (This parameter is not verified in the search process.)</p>
</td>
</tr>
<tr id="row26849339548"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p2684183316545"><a name="p2684183316545"></a><a name="p2684183316545"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p4684433185412"><a name="p4684433185412"></a><a name="p4684433185412"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p9684173316541"><a name="p9684173316541"></a><a name="p9684173316541"></a>Specifies the tag value. Each tag value can contain a maximum of 255 Unicode characters.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section1329552492510"></a>

-   Example request 1 \(when  **action**  is set to  **filter**\)

    ```
    POST https://{Endpoint}/v2.0/6a0de1c3-7d74-4f4a-b75e-e57135bd2b97/loadbalancers/resource_instances/action
    
    {
        "offset": "100", 
        "limit": "100", 
        "action": "filter", 
        "matches": [
            {
                "key": "resource_name", 
                "value": "resource1"
            }
        ], 
        "tags": [
            {
                "key": "key1", 
                "values": [
                    "*value1", 
                    "value2"
                ]
            }
        ]
    }
    ```

-   Example response 1

    ```
    {
        "resources": [
            {
                "resource_detail": "", 
                "resource_id": "154d135b-3a89-4e89-8023-06efb9acdc05", 
                "resource_name": "resouece1", 
                "tags": [
                    {
                        "key": "key1",
                        "value": "value1"
                    }, 
                    {
                        "key": "key2", 
                        "value": "value1"
                    }
                ]
            }
        ], 
        "total_count": 1000
    }
    ```

-   Example request 2 \(when  **action**  is set to  **count**\)

    ```
    POST https://{Endpoint}/v2.0/6a0de1c3-7d74-4f4a-b75e-e57135bd2b97/loadbalancers/resource_instances/action
    
    {
        "action": "count", 
        "tags": [
            {
                "key": "key1",
                "values": [
                    "value1", 
                    "value2"
                ]
            }, 
            {
                "key": "key2", 
                "values": [
                    "value1", 
                    "value2"
                ]
            }
        ], 
        "matches": [
            {
                "key": "resource_name", 
                "value": "resource1"
            }
        ]
    }
    ```


-   Example response 2

    ```
    {
        "total_count": 1000
    }
    ```


## Status Code<a name="en-us_topic_0101985068_section21716397115122"></a>

For details, see  [Status Codes](status-codes.md).

