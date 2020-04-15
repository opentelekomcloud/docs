# Dedicated General-purpose DeHs<a name="EN-US_TOPIC_0121650682"></a>

## Overview<a name="section970214475319"></a>

Dedicated general-purpose DeHs are classified as c3 DeHs. DeHs of the c3 type can be used to deploy C3 ECSs. The C3 ECSs use the latest-generation Intel Xeon Skylake CPUs and high-performance networks to improve comprehensive performance and stability, meeting the requirements of enterprise-level applications on service stability and computing performance.

## DeHs Flavors<a name="section380612821316"></a>

**Table  1**  Flavors of c3 DeHs

<a name="table127671448175710"></a>
<table><thead align="left"><tr id="row179114484572"><th class="cellrowborder" valign="top" width="16%" id="mcps1.2.6.1.1"><p id="p179774815715"><a name="p179774815715"></a><a name="p179774815715"></a><strong id="b842352706123443"><a name="b842352706123443"></a><a name="b842352706123443"></a><strong id="b16932113733415"><a name="b16932113733415"></a><a name="b16932113733415"></a>Flavor Type</strong></strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.079999999999998%" id="mcps1.2.6.1.2"><p id="p580274865712"><a name="p580274865712"></a><a name="p580274865712"></a><strong id="b842352706123452"><a name="b842352706123452"></a><a name="b842352706123452"></a>Number of Sockets</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.63%" id="mcps1.2.6.1.3"><p id="p17807124815716"><a name="p17807124815716"></a><a name="p17807124815716"></a><strong id="b84235270612350"><a name="b84235270612350"></a><a name="b84235270612350"></a>Number of Cores per Socket</strong></p>
</th>
<th class="cellrowborder" valign="top" width="36.97%" id="mcps1.2.6.1.4"><p id="p1281419484576"><a name="p1281419484576"></a><a name="p1281419484576"></a><strong id="b84235270612355"><a name="b84235270612355"></a><a name="b84235270612355"></a>Hardware Specifications</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.32%" id="mcps1.2.6.1.5"><p id="p1581911488577"><a name="p1581911488577"></a><a name="p1581911488577"></a><strong id="b842352706123510"><a name="b842352706123510"></a><a name="b842352706123510"></a>Number of vCPUs</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row168241448135718"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.1 "><p id="p582816488573"><a name="p582816488573"></a><a name="p582816488573"></a>c3</p>
</td>
<td class="cellrowborder" valign="top" width="15.079999999999998%" headers="mcps1.2.6.1.2 "><p id="p2834184817579"><a name="p2834184817579"></a><a name="p2834184817579"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="16.63%" headers="mcps1.2.6.1.3 "><p id="p183934805711"><a name="p183934805711"></a><a name="p183934805711"></a>18</p>
</td>
<td class="cellrowborder" valign="top" width="36.97%" headers="mcps1.2.6.1.4 "><a name="ul13845848105710"></a><a name="ul13845848105710"></a><ul id="ul13845848105710"><li>CPU: Intel&reg; Xeon&reg; Processor Gold 6151</li><li>Memory: 256 GB (or 262,144 MB)</li></ul>
</td>
<td class="cellrowborder" valign="top" width="15.32%" headers="mcps1.2.6.1.5 "><p id="p14879848185716"><a name="p14879848185716"></a><a name="p14879848185716"></a>60</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>The number of vCPUs for a c3 DeH is calculated as follows:   
>Number of vCPUs = \(2 x 18 x 2 - 12\) x 1 = 60  

## Flavors of Placeable ECSs<a name="section1535463531311"></a>

**Table  2**  ECS flavors supported by c3 DeHs

<a name="table18121958193911"></a>
<table><thead align="left"><tr id="row7123258193919"><th class="cellrowborder" valign="top" width="30.380000000000003%" id="mcps1.2.4.1.1"><p id="p199841619184020"><a name="p199841619184020"></a><a name="p199841619184020"></a><strong id="b10541175333718"><a name="b10541175333718"></a><a name="b10541175333718"></a>ECS Flavor</strong></p>
</th>
<th class="cellrowborder" valign="top" width="29.110000000000003%" id="mcps1.2.4.1.2"><p id="p17989161934011"><a name="p17989161934011"></a><a name="p17989161934011"></a><strong id="b84235270610514"><a name="b84235270610514"></a><a name="b84235270610514"></a>vCPUs</strong></p>
</th>
<th class="cellrowborder" valign="top" width="40.510000000000005%" id="mcps1.2.4.1.3"><p id="p179936198400"><a name="p179936198400"></a><a name="p179936198400"></a><strong id="b842352706123543"><a name="b842352706123543"></a><a name="b842352706123543"></a>Memory (RAM in GB)</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row148894185320"><td class="cellrowborder" valign="top" width="30.380000000000003%" headers="mcps1.2.4.1.1 "><p id="p08919181833"><a name="p08919181833"></a><a name="p08919181833"></a>c3.large.2</p>
</td>
<td class="cellrowborder" valign="top" width="29.110000000000003%" headers="mcps1.2.4.1.2 "><p id="p1889114185315"><a name="p1889114185315"></a><a name="p1889114185315"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="40.510000000000005%" headers="mcps1.2.4.1.3 "><p id="p589131814318"><a name="p589131814318"></a><a name="p589131814318"></a>4</p>
</td>
</tr>
<tr id="row712365812391"><td class="cellrowborder" valign="top" width="30.380000000000003%" headers="mcps1.2.4.1.1 "><p id="p19168386204624"><a name="p19168386204624"></a><a name="p19168386204624"></a>c3.large.4</p>
</td>
<td class="cellrowborder" valign="top" width="29.110000000000003%" headers="mcps1.2.4.1.2 "><p id="p47196992204624"><a name="p47196992204624"></a><a name="p47196992204624"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="40.510000000000005%" headers="mcps1.2.4.1.3 "><p id="p64859997204624"><a name="p64859997204624"></a><a name="p64859997204624"></a>8</p>
</td>
</tr>
<tr id="row61783403319"><td class="cellrowborder" valign="top" width="30.380000000000003%" headers="mcps1.2.4.1.1 "><p id="p1117810401037"><a name="p1117810401037"></a><a name="p1117810401037"></a>c3.xlarge.2</p>
</td>
<td class="cellrowborder" valign="top" width="29.110000000000003%" headers="mcps1.2.4.1.2 "><p id="p161783405315"><a name="p161783405315"></a><a name="p161783405315"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="40.510000000000005%" headers="mcps1.2.4.1.3 "><p id="p417804013320"><a name="p417804013320"></a><a name="p417804013320"></a>8</p>
</td>
</tr>
<tr id="row1812310587393"><td class="cellrowborder" valign="top" width="30.380000000000003%" headers="mcps1.2.4.1.1 "><p id="p18054373204624"><a name="p18054373204624"></a><a name="p18054373204624"></a>c3.xlarge.4</p>
</td>
<td class="cellrowborder" valign="top" width="29.110000000000003%" headers="mcps1.2.4.1.2 "><p id="p15110173204624"><a name="p15110173204624"></a><a name="p15110173204624"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="40.510000000000005%" headers="mcps1.2.4.1.3 "><p id="p15964478204624"><a name="p15964478204624"></a><a name="p15964478204624"></a>16</p>
</td>
</tr>
<tr id="row135894516412"><td class="cellrowborder" valign="top" width="30.380000000000003%" headers="mcps1.2.4.1.1 "><p id="p15891151345"><a name="p15891151345"></a><a name="p15891151345"></a>c3.2xlarge.2</p>
</td>
<td class="cellrowborder" valign="top" width="29.110000000000003%" headers="mcps1.2.4.1.2 "><p id="p20589251044"><a name="p20589251044"></a><a name="p20589251044"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="40.510000000000005%" headers="mcps1.2.4.1.3 "><p id="p5589185445"><a name="p5589185445"></a><a name="p5589185445"></a>16</p>
</td>
</tr>
<tr id="row12123175813912"><td class="cellrowborder" valign="top" width="30.380000000000003%" headers="mcps1.2.4.1.1 "><p id="p34929558204624"><a name="p34929558204624"></a><a name="p34929558204624"></a>c3.2xlarge.4</p>
</td>
<td class="cellrowborder" valign="top" width="29.110000000000003%" headers="mcps1.2.4.1.2 "><p id="p8300597204624"><a name="p8300597204624"></a><a name="p8300597204624"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="40.510000000000005%" headers="mcps1.2.4.1.3 "><p id="p1259733204624"><a name="p1259733204624"></a><a name="p1259733204624"></a>32</p>
</td>
</tr>
<tr id="row8571103816417"><td class="cellrowborder" valign="top" width="30.380000000000003%" headers="mcps1.2.4.1.1 "><p id="p857110381948"><a name="p857110381948"></a><a name="p857110381948"></a>c3.4xlarge.2</p>
</td>
<td class="cellrowborder" valign="top" width="29.110000000000003%" headers="mcps1.2.4.1.2 "><p id="p75715381947"><a name="p75715381947"></a><a name="p75715381947"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="40.510000000000005%" headers="mcps1.2.4.1.3 "><p id="p75711838249"><a name="p75711838249"></a><a name="p75711838249"></a>32</p>
</td>
</tr>
<tr id="row14351115454215"><td class="cellrowborder" valign="top" width="30.380000000000003%" headers="mcps1.2.4.1.1 "><p id="p15516174204624"><a name="p15516174204624"></a><a name="p15516174204624"></a>c3.4xlarge.4</p>
</td>
<td class="cellrowborder" valign="top" width="29.110000000000003%" headers="mcps1.2.4.1.2 "><p id="p29388703204624"><a name="p29388703204624"></a><a name="p29388703204624"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="40.510000000000005%" headers="mcps1.2.4.1.3 "><p id="p31674728204624"><a name="p31674728204624"></a><a name="p31674728204624"></a>64</p>
</td>
</tr>
<tr id="row15940152519"><td class="cellrowborder" valign="top" width="30.380000000000003%" headers="mcps1.2.4.1.1 "><p id="p2940151551"><a name="p2940151551"></a><a name="p2940151551"></a>c3.8xlarge.2</p>
</td>
<td class="cellrowborder" valign="top" width="29.110000000000003%" headers="mcps1.2.4.1.2 "><p id="p169402512510"><a name="p169402512510"></a><a name="p169402512510"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="40.510000000000005%" headers="mcps1.2.4.1.3 "><p id="p99402054512"><a name="p99402054512"></a><a name="p99402054512"></a>64</p>
</td>
</tr>
<tr id="row163511354144216"><td class="cellrowborder" valign="top" width="30.380000000000003%" headers="mcps1.2.4.1.1 "><p id="p35960458204624"><a name="p35960458204624"></a><a name="p35960458204624"></a>c3.8xlarge.4</p>
</td>
<td class="cellrowborder" valign="top" width="29.110000000000003%" headers="mcps1.2.4.1.2 "><p id="p37001786204624"><a name="p37001786204624"></a><a name="p37001786204624"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="40.510000000000005%" headers="mcps1.2.4.1.3 "><p id="p44354694204624"><a name="p44354694204624"></a><a name="p44354694204624"></a>128</p>
</td>
</tr>
<tr id="row11987182810516"><td class="cellrowborder" valign="top" width="30.380000000000003%" headers="mcps1.2.4.1.1 "><p id="p3987162813514"><a name="p3987162813514"></a><a name="p3987162813514"></a>c3.15xlarge.2</p>
</td>
<td class="cellrowborder" valign="top" width="29.110000000000003%" headers="mcps1.2.4.1.2 "><p id="p199875281957"><a name="p199875281957"></a><a name="p199875281957"></a>60</p>
</td>
<td class="cellrowborder" valign="top" width="40.510000000000005%" headers="mcps1.2.4.1.3 "><p id="p9987152810516"><a name="p9987152810516"></a><a name="p9987152810516"></a>128</p>
</td>
</tr>
<tr id="row13123158193913"><td class="cellrowborder" valign="top" width="30.380000000000003%" headers="mcps1.2.4.1.1 "><p id="p23228883204624"><a name="p23228883204624"></a><a name="p23228883204624"></a>c3.15xlarge.4</p>
</td>
<td class="cellrowborder" valign="top" width="29.110000000000003%" headers="mcps1.2.4.1.2 "><p id="p42717549204624"><a name="p42717549204624"></a><a name="p42717549204624"></a>60</p>
</td>
<td class="cellrowborder" valign="top" width="40.510000000000005%" headers="mcps1.2.4.1.3 "><p id="p37569478204624"><a name="p37569478204624"></a><a name="p37569478204624"></a>256</p>
</td>
</tr>
</tbody>
</table>

