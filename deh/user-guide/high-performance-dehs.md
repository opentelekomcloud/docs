# High-performance DeHs<a name="EN-US_TOPIC_0046252753"></a>

## Overview<a name="section112992713379"></a>

High-performance DeHs are classified as h1 DeHs. DeHs of the h1 type provide high-performance hardware and stable system running environment for ECSs that occupy a large number of computing and memory resources and have high-throughput storage systems.

High-performance ECSs can be deployed on h1 DeHs.

## DeH Flavors<a name="section12266162916120"></a>

**Table  1**  Flavors of h1 DeHs

<a name="table12679291125"></a>
<table><thead align="left"><tr id="row1726842910128"><th class="cellrowborder" valign="top" width="25.040000000000003%" id="mcps1.2.6.1.1"><p id="p42681129111211"><a name="p42681129111211"></a><a name="p42681129111211"></a><strong id="b1418856124918"><a name="b1418856124918"></a><a name="b1418856124918"></a>Flavor Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.24%" id="mcps1.2.6.1.2"><p id="p1426820297121"><a name="p1426820297121"></a><a name="p1426820297121"></a><strong id="b84235270615129"><a name="b84235270615129"></a><a name="b84235270615129"></a>Number of Sockets</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.86%" id="mcps1.2.6.1.3"><p id="p026862921214"><a name="p026862921214"></a><a name="p026862921214"></a><strong id="b84235270615140"><a name="b84235270615140"></a><a name="b84235270615140"></a>Number of Cores per Socket</strong></p>
</th>
<th class="cellrowborder" valign="top" width="29.01%" id="mcps1.2.6.1.4"><p id="p10268142913125"><a name="p10268142913125"></a><a name="p10268142913125"></a><strong id="b84235270615145"><a name="b84235270615145"></a><a name="b84235270615145"></a>Hardware Specifications</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.85%" id="mcps1.2.6.1.5"><p id="p16994164211432"><a name="p16994164211432"></a><a name="p16994164211432"></a><strong id="b84235270615151"><a name="b84235270615151"></a><a name="b84235270615151"></a>Number of vCPUs</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row6269229171217"><td class="cellrowborder" valign="top" width="25.040000000000003%" headers="mcps1.2.6.1.1 "><p id="p1178834518126"><a name="p1178834518126"></a><a name="p1178834518126"></a>h1</p>
</td>
<td class="cellrowborder" valign="top" width="15.24%" headers="mcps1.2.6.1.2 "><p id="p13269129181215"><a name="p13269129181215"></a><a name="p13269129181215"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="15.86%" headers="mcps1.2.6.1.3 "><p id="p3269142971212"><a name="p3269142971212"></a><a name="p3269142971212"></a>12</p>
</td>
<td class="cellrowborder" valign="top" width="29.01%" headers="mcps1.2.6.1.4 "><a name="ul1151442934717"></a><a name="ul1151442934717"></a><ul id="ul1151442934717"><li>CPU:<a name="ul717715312357"></a><a name="ul717715312357"></a><ul id="ul717715312357"><li>Intel&reg; Xeon&reg; Processor E5-2690 v3 (30 MB Cache, 2.60 GHz)</li><li>Intel&reg; Xeon&reg; Processor E5-2690 v4 (35 MB Cache, 2.60 GHz)</li></ul>
</li><li>Memory: 264 GB (or 270,336 MB)</li></ul>
</td>
<td class="cellrowborder" valign="top" width="14.85%" headers="mcps1.2.6.1.5 "><p id="p1199513426436"><a name="p1199513426436"></a><a name="p1199513426436"></a>36</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>The number of vCPUs for an h1 DeH is calculated as follows:  
>Number of vCPUs = \(2 x 12 x 2 - 12\) x 1 = 36  

## Flavors of Placeable ECSs<a name="section989895174611"></a>

**Table  2**  ECS flavors supported by h1 DeHs

<a name="table125971749174612"></a>
<table><thead align="left"><tr id="row45971349114617"><th class="cellrowborder" valign="top" width="26.58265826582658%" id="mcps1.2.4.1.1"><p id="p202471645134218"><a name="p202471645134218"></a><a name="p202471645134218"></a><strong id="b761823195116"><a name="b761823195116"></a><a name="b761823195116"></a>ECS Flavor</strong></p>
</th>
<th class="cellrowborder" valign="top" width="29.112911291129116%" id="mcps1.2.4.1.2"><p id="p2038862911476"><a name="p2038862911476"></a><a name="p2038862911476"></a><strong id="b84235270610514"><a name="b84235270610514"></a><a name="b84235270610514"></a>vCPUs</strong></p>
</th>
<th class="cellrowborder" valign="top" width="44.30443044304431%" id="mcps1.2.4.1.3"><p id="p838892910478"><a name="p838892910478"></a><a name="p838892910478"></a><strong id="b842352706105612"><a name="b842352706105612"></a><a name="b842352706105612"></a>Memory (RAM in GB)</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row35981949134611"><td class="cellrowborder" valign="top" width="26.58265826582658%" headers="mcps1.2.4.1.1 "><p id="p179111590473"><a name="p179111590473"></a><a name="p179111590473"></a>h1.large</p>
</td>
<td class="cellrowborder" valign="top" width="29.112911291129116%" headers="mcps1.2.4.1.2 "><p id="p4911169164720"><a name="p4911169164720"></a><a name="p4911169164720"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="44.30443044304431%" headers="mcps1.2.4.1.3 "><p id="p1891113911479"><a name="p1891113911479"></a><a name="p1891113911479"></a>4</p>
</td>
</tr>
<tr id="row4096977210127"><td class="cellrowborder" valign="top" width="26.58265826582658%" headers="mcps1.2.4.1.1 "><p id="p908222410127"><a name="p908222410127"></a><a name="p908222410127"></a>h1.large.4</p>
</td>
<td class="cellrowborder" valign="top" width="29.112911291129116%" headers="mcps1.2.4.1.2 "><p id="p487820310127"><a name="p487820310127"></a><a name="p487820310127"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="44.30443044304431%" headers="mcps1.2.4.1.3 "><p id="p5451430610127"><a name="p5451430610127"></a><a name="p5451430610127"></a>8</p>
</td>
</tr>
<tr id="row255518471024"><td class="cellrowborder" valign="top" width="26.58265826582658%" headers="mcps1.2.4.1.1 "><p id="p168212661024"><a name="p168212661024"></a><a name="p168212661024"></a>h1.large.8</p>
</td>
<td class="cellrowborder" valign="top" width="29.112911291129116%" headers="mcps1.2.4.1.2 "><p id="p141942111024"><a name="p141942111024"></a><a name="p141942111024"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="44.30443044304431%" headers="mcps1.2.4.1.3 "><p id="p60361201024"><a name="p60361201024"></a><a name="p60361201024"></a>16</p>
</td>
</tr>
<tr id="row1359874914467"><td class="cellrowborder" valign="top" width="26.58265826582658%" headers="mcps1.2.4.1.1 "><p id="p10911209204719"><a name="p10911209204719"></a><a name="p10911209204719"></a>h1.xlarge</p>
</td>
<td class="cellrowborder" valign="top" width="29.112911291129116%" headers="mcps1.2.4.1.2 "><p id="p0911293473"><a name="p0911293473"></a><a name="p0911293473"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="44.30443044304431%" headers="mcps1.2.4.1.3 "><p id="p1591189104715"><a name="p1591189104715"></a><a name="p1591189104715"></a>8</p>
</td>
</tr>
<tr id="row1500734810228"><td class="cellrowborder" valign="top" width="26.58265826582658%" headers="mcps1.2.4.1.1 "><p id="p2401928110228"><a name="p2401928110228"></a><a name="p2401928110228"></a>h1.xlarge.4</p>
</td>
<td class="cellrowborder" valign="top" width="29.112911291129116%" headers="mcps1.2.4.1.2 "><p id="p1573454110228"><a name="p1573454110228"></a><a name="p1573454110228"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="44.30443044304431%" headers="mcps1.2.4.1.3 "><p id="p726139810228"><a name="p726139810228"></a><a name="p726139810228"></a>16</p>
</td>
</tr>
<tr id="row6608671210259"><td class="cellrowborder" valign="top" width="26.58265826582658%" headers="mcps1.2.4.1.1 "><p id="p4761340710259"><a name="p4761340710259"></a><a name="p4761340710259"></a>h1.xlarge.8</p>
</td>
<td class="cellrowborder" valign="top" width="29.112911291129116%" headers="mcps1.2.4.1.2 "><p id="p5791451610259"><a name="p5791451610259"></a><a name="p5791451610259"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="44.30443044304431%" headers="mcps1.2.4.1.3 "><p id="p6345031610259"><a name="p6345031610259"></a><a name="p6345031610259"></a>32</p>
</td>
</tr>
<tr id="row16598124984618"><td class="cellrowborder" valign="top" width="26.58265826582658%" headers="mcps1.2.4.1.1 "><p id="p19124912476"><a name="p19124912476"></a><a name="p19124912476"></a>h1.2xlarge</p>
</td>
<td class="cellrowborder" valign="top" width="29.112911291129116%" headers="mcps1.2.4.1.2 "><p id="p891229194710"><a name="p891229194710"></a><a name="p891229194710"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="44.30443044304431%" headers="mcps1.2.4.1.3 "><p id="p199126954713"><a name="p199126954713"></a><a name="p199126954713"></a>16</p>
</td>
</tr>
<tr id="row4439708310321"><td class="cellrowborder" valign="top" width="26.58265826582658%" headers="mcps1.2.4.1.1 "><p id="p1527552910321"><a name="p1527552910321"></a><a name="p1527552910321"></a>h1.2xlarge.4</p>
</td>
<td class="cellrowborder" valign="top" width="29.112911291129116%" headers="mcps1.2.4.1.2 "><p id="p3016781310321"><a name="p3016781310321"></a><a name="p3016781310321"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="44.30443044304431%" headers="mcps1.2.4.1.3 "><p id="p5445553010321"><a name="p5445553010321"></a><a name="p5445553010321"></a>32</p>
</td>
</tr>
<tr id="row1274567910349"><td class="cellrowborder" valign="top" width="26.58265826582658%" headers="mcps1.2.4.1.1 "><p id="p2947438910349"><a name="p2947438910349"></a><a name="p2947438910349"></a>h1.2xlarge.8</p>
</td>
<td class="cellrowborder" valign="top" width="29.112911291129116%" headers="mcps1.2.4.1.2 "><p id="p2377955910349"><a name="p2377955910349"></a><a name="p2377955910349"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="44.30443044304431%" headers="mcps1.2.4.1.3 "><p id="p6312235910349"><a name="p6312235910349"></a><a name="p6312235910349"></a>64</p>
</td>
</tr>
<tr id="row2599149204614"><td class="cellrowborder" valign="top" width="26.58265826582658%" headers="mcps1.2.4.1.1 "><p id="p14912995478"><a name="p14912995478"></a><a name="p14912995478"></a>h1.4xlarge</p>
</td>
<td class="cellrowborder" valign="top" width="29.112911291129116%" headers="mcps1.2.4.1.2 "><p id="p109127920470"><a name="p109127920470"></a><a name="p109127920470"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="44.30443044304431%" headers="mcps1.2.4.1.3 "><p id="p149121297476"><a name="p149121297476"></a><a name="p149121297476"></a>32</p>
</td>
</tr>
<tr id="row14599194904616"><td class="cellrowborder" valign="top" width="26.58265826582658%" headers="mcps1.2.4.1.1 "><p id="p54786954142631"><a name="p54786954142631"></a><a name="p54786954142631"></a>h1.4xlarge.4</p>
</td>
<td class="cellrowborder" valign="top" width="29.112911291129116%" headers="mcps1.2.4.1.2 "><p id="p8558285142631"><a name="p8558285142631"></a><a name="p8558285142631"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="44.30443044304431%" headers="mcps1.2.4.1.3 "><p id="p22132493142631"><a name="p22132493142631"></a><a name="p22132493142631"></a>64</p>
</td>
</tr>
<tr id="row39634672142458"><td class="cellrowborder" valign="top" width="26.58265826582658%" headers="mcps1.2.4.1.1 "><p id="p28460220142631"><a name="p28460220142631"></a><a name="p28460220142631"></a>h1.4xlarge.8</p>
</td>
<td class="cellrowborder" valign="top" width="29.112911291129116%" headers="mcps1.2.4.1.2 "><p id="p23576498142631"><a name="p23576498142631"></a><a name="p23576498142631"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="44.30443044304431%" headers="mcps1.2.4.1.3 "><p id="p30648192142631"><a name="p30648192142631"></a><a name="p30648192142631"></a>128</p>
</td>
</tr>
<tr id="row41686554142458"><td class="cellrowborder" valign="top" width="26.58265826582658%" headers="mcps1.2.4.1.1 "><p id="p3015784114271"><a name="p3015784114271"></a><a name="p3015784114271"></a>h1.8xlarge</p>
</td>
<td class="cellrowborder" valign="top" width="29.112911291129116%" headers="mcps1.2.4.1.2 "><p id="p2686605714271"><a name="p2686605714271"></a><a name="p2686605714271"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="44.30443044304431%" headers="mcps1.2.4.1.3 "><p id="p2866702214271"><a name="p2866702214271"></a><a name="p2866702214271"></a>64</p>
</td>
</tr>
<tr id="row12088379142458"><td class="cellrowborder" valign="top" width="26.58265826582658%" headers="mcps1.2.4.1.1 "><p id="p2740256314271"><a name="p2740256314271"></a><a name="p2740256314271"></a>h1.8xlarge.4</p>
</td>
<td class="cellrowborder" valign="top" width="29.112911291129116%" headers="mcps1.2.4.1.2 "><p id="p501511014271"><a name="p501511014271"></a><a name="p501511014271"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="44.30443044304431%" headers="mcps1.2.4.1.3 "><p id="p357073714271"><a name="p357073714271"></a><a name="p357073714271"></a>128</p>
</td>
</tr>
<tr id="row31169315142458"><td class="cellrowborder" valign="top" width="26.58265826582658%" headers="mcps1.2.4.1.1 "><p id="p5293084114271"><a name="p5293084114271"></a><a name="p5293084114271"></a>h1.8xlarge.8</p>
</td>
<td class="cellrowborder" valign="top" width="29.112911291129116%" headers="mcps1.2.4.1.2 "><p id="p5953969614271"><a name="p5953969614271"></a><a name="p5953969614271"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="44.30443044304431%" headers="mcps1.2.4.1.3 "><p id="p5798609214271"><a name="p5798609214271"></a><a name="p5798609214271"></a>256</p>
</td>
</tr>
</tbody>
</table>

