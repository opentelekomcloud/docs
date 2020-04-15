# What Are the Differences Between Data Warehouses and the Hadoop Big Data Platform?<a name="dws_03_0005"></a>

Generally, the Hadoop big data platform can be regarded as a new-generation data warehousing system. It shares the characteristics of modern data warehouses and is widely used by enterprises. Because of the scalability of MPP, the MPP-based data warehousing system is grouped into the big data platform sometimes.

However, data warehouses greatly differ from the Hadoop platform in terms of functions and user experience in different scenarios. You can determine which one is more appropriate for your specific situation according to the following table.

**Table  1**  Feature comparison between data warehouses and the Hadoop big data platform

<a name="table198891524105517"></a>
<table><tbody><tr id="row45742575510"><td class="cellrowborder" valign="top" width="28.000000000000004%"><p id="p1657122515519"><a name="p1657122515519"></a><a name="p1657122515519"></a><strong id="b5172078216239"><a name="b5172078216239"></a><a name="b5172078216239"></a>Feature</strong></p>
</td>
<td class="cellrowborder" valign="top" width="36%"><p id="p657325145510"><a name="p657325145510"></a><a name="p657325145510"></a><strong id="b2863382816239"><a name="b2863382816239"></a><a name="b2863382816239"></a>Hadoop</strong></p>
</td>
<td class="cellrowborder" valign="top" width="36%"><p id="p18571251555"><a name="p18571251555"></a><a name="p18571251555"></a><strong id="b3763873816239"><a name="b3763873816239"></a><a name="b3763873816239"></a>Data Warehouse</strong></p>
</td>
</tr>
<tr id="row457192515514"><td class="cellrowborder" valign="top" width="28.000000000000004%"><p id="p957112511551"><a name="p957112511551"></a><a name="p957112511551"></a>Number of compute nodes</p>
</td>
<td class="cellrowborder" valign="top" width="36%"><p id="p1057325145514"><a name="p1057325145514"></a><a name="p1057325145514"></a>Thousands</p>
</td>
<td class="cellrowborder" valign="top" width="36%"><p id="p1157172525511"><a name="p1157172525511"></a><a name="p1157172525511"></a>128 or less</p>
</td>
</tr>
<tr id="row1574257557"><td class="cellrowborder" valign="top" width="28.000000000000004%"><p id="p6571425105514"><a name="p6571425105514"></a><a name="p6571425105514"></a>Data volume</p>
</td>
<td class="cellrowborder" valign="top" width="36%"><p id="p1057112516555"><a name="p1057112516555"></a><a name="p1057112516555"></a>Greater than 10 PB</p>
</td>
<td class="cellrowborder" valign="top" width="36%"><p id="p145842525520"><a name="p145842525520"></a><a name="p145842525520"></a>5 PB or less</p>
</td>
</tr>
<tr id="row2581425135513"><td class="cellrowborder" valign="top" width="28.000000000000004%"><p id="p05818258557"><a name="p05818258557"></a><a name="p05818258557"></a>Data type</p>
</td>
<td class="cellrowborder" valign="top" width="36%"><p id="p1558625115517"><a name="p1558625115517"></a><a name="p1558625115517"></a>Relational, semi-relational, and unstructured data such as voice, images, and videos</p>
</td>
<td class="cellrowborder" valign="top" width="36%"><p id="p658182515517"><a name="p658182515517"></a><a name="p658182515517"></a>Relational data</p>
</td>
</tr>
<tr id="row5589253556"><td class="cellrowborder" valign="top" width="28.000000000000004%"><p id="p1858132575518"><a name="p1858132575518"></a><a name="p1858132575518"></a>Latency</p>
</td>
<td class="cellrowborder" valign="top" width="36%"><p id="p1158425185513"><a name="p1158425185513"></a><a name="p1158425185513"></a>Medium to high</p>
</td>
<td class="cellrowborder" valign="top" width="36%"><p id="p5580256552"><a name="p5580256552"></a><a name="p5580256552"></a>Low</p>
</td>
</tr>
<tr id="row458425155515"><td class="cellrowborder" valign="top" width="28.000000000000004%"><p id="p155842535515"><a name="p155842535515"></a><a name="p155842535515"></a>Application ecosystem</p>
</td>
<td class="cellrowborder" valign="top" width="36%"><p id="p155842517554"><a name="p155842517554"></a><a name="p155842517554"></a>Innovative/artificial intelligence</p>
</td>
<td class="cellrowborder" valign="top" width="36%"><p id="p9583258551"><a name="p9583258551"></a><a name="p9583258551"></a>Traditional database/BI</p>
</td>
</tr>
<tr id="row25820259553"><td class="cellrowborder" valign="top" width="28.000000000000004%"><p id="p858525115514"><a name="p858525115514"></a><a name="p858525115514"></a>Application development API</p>
</td>
<td class="cellrowborder" valign="top" width="36%"><p id="p35882565517"><a name="p35882565517"></a><a name="p35882565517"></a>Various programming language APIs, such as SQL and MapReduce</p>
</td>
<td class="cellrowborder" valign="top" width="36%"><p id="p258125135519"><a name="p258125135519"></a><a name="p258125135519"></a>Standard database SQL</p>
</td>
</tr>
<tr id="row75832525519"><td class="cellrowborder" valign="top" width="28.000000000000004%"><p id="p125872520553"><a name="p125872520553"></a><a name="p125872520553"></a>Scalability</p>
</td>
<td class="cellrowborder" valign="top" width="36%"><p id="p2058162525514"><a name="p2058162525514"></a><a name="p2058162525514"></a>Unlimited scalability with its comprehensive programming APIs</p>
</td>
<td class="cellrowborder" valign="top" width="36%"><p id="p1858192585510"><a name="p1858192585510"></a><a name="p1858192585510"></a>Limited scalability supported by UDF</p>
</td>
</tr>
<tr id="row13581425145515"><td class="cellrowborder" valign="top" width="28.000000000000004%"><p id="p25862535513"><a name="p25862535513"></a><a name="p25862535513"></a>Transaction support</p>
</td>
<td class="cellrowborder" valign="top" width="36%"><p id="p19591625195513"><a name="p19591625195513"></a><a name="p19591625195513"></a>Limited</p>
</td>
<td class="cellrowborder" valign="top" width="36%"><p id="p85919256552"><a name="p85919256552"></a><a name="p85919256552"></a>Comprehensive</p>
</td>
</tr>
</tbody>
</table>

Data warehouses and the Hadoop platform work together to meet customers' service requirements in different scenarios. DWS on the public cloud can seamlessly integrate with Hadoop-based MRS on the public cloud to provide the SQL-over-Hadoop feature, allowing data sharing cross platforms and services. Therefore, you can enjoy not only openness, convenience, and innovation of the Hadoop platform, but also manage and use your massive volumes of data using data warehouses. Additionally, you can use upper-layer applications of conventional data warehouses, especially BI applications.

