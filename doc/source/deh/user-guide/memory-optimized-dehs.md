# Memory-optimized DeHs<a name="EN-US_TOPIC_0105897861"></a>

## Overview<a name="section16676164654612"></a>

Memory-optimized DeHs are classified as m3 DeHs. DeHs of the m3 type are designed for processing large-scale data sets in the memory. They use the latest Intel Xeon Skylake CPUs, network acceleration engines, and Data Plane Development Kit \(DPDK\) rapid packet processing mechanism to provide higher network performance, providing a maximum memory size of 512 GB based on DDR4 for high-memory computing applications.

M3 ECSs can be deployed on m3 DeHs.

## DeH Flavors<a name="section12590111016471"></a>

**Table  1**  Flavors of m3 DeHs

<a name="table12679291125"></a>
<table><thead align="left"><tr id="row1726842910128"><th class="cellrowborder" valign="top" width="17.340000000000003%" id="mcps1.2.6.1.1"><p id="p42681129111211"><a name="p42681129111211"></a><a name="p42681129111211"></a><strong id="b84235270672137"><a name="b84235270672137"></a><a name="b84235270672137"></a><strong id="b2102173618445"><a name="b2102173618445"></a><a name="b2102173618445"></a>Flavor Type</strong></strong></p>
</th>
<th class="cellrowborder" valign="top" width="13.930000000000003%" id="mcps1.2.6.1.2"><p id="p1426820297121"><a name="p1426820297121"></a><a name="p1426820297121"></a><strong id="b842352706142824"><a name="b842352706142824"></a><a name="b842352706142824"></a>Number of Sockets</strong></p>
</th>
<th class="cellrowborder" valign="top" width="19.610000000000003%" id="mcps1.2.6.1.3"><p id="p026862921214"><a name="p026862921214"></a><a name="p026862921214"></a><strong id="b842352706142828"><a name="b842352706142828"></a><a name="b842352706142828"></a>Number of Cores per Socket</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.52%" id="mcps1.2.6.1.4"><p id="p10268142913125"><a name="p10268142913125"></a><a name="p10268142913125"></a><strong id="b842352706142834"><a name="b842352706142834"></a><a name="b842352706142834"></a>Hardware Specifications</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.600000000000003%" id="mcps1.2.6.1.5"><p id="p16994164211432"><a name="p16994164211432"></a><a name="p16994164211432"></a><strong id="b842352706142839"><a name="b842352706142839"></a><a name="b842352706142839"></a>Number of vCPUs</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row6269229171217"><td class="cellrowborder" valign="top" width="17.340000000000003%" headers="mcps1.2.6.1.1 "><p id="p1178834518126"><a name="p1178834518126"></a><a name="p1178834518126"></a>m3</p>
</td>
<td class="cellrowborder" valign="top" width="13.930000000000003%" headers="mcps1.2.6.1.2 "><p id="p48641542145814"><a name="p48641542145814"></a><a name="p48641542145814"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="19.610000000000003%" headers="mcps1.2.6.1.3 "><p id="p13865204215819"><a name="p13865204215819"></a><a name="p13865204215819"></a>18</p>
</td>
<td class="cellrowborder" valign="top" width="33.52%" headers="mcps1.2.6.1.4 "><a name="ul209928558418"></a><a name="ul209928558418"></a><ul id="ul209928558418"><li>CPU: Intel&reg; Xeon&reg; Processor Gold 6151</li><li>Memory: 512 GB (or 524,288 MB)</li></ul>
</td>
<td class="cellrowborder" valign="top" width="15.600000000000003%" headers="mcps1.2.6.1.5 "><p id="p1657717113434"><a name="p1657717113434"></a><a name="p1657717113434"></a>60</p>
</td>
</tr>
</tbody>
</table>

>![](/images/icon-note.gif) **NOTE:**   
>The number of vCPUs for an m3 DeH is calculated as follows:   
>Number of vCPUs = \(2 x 18 x 2 - 12\) x 1 = 60  

## Flavors of Placeable ECSs<a name="section24891827164715"></a>

**Table  2**  ECS flavors supported by m3 DeHs

<a name="table1352634845219"></a>
<table><thead align="left"><tr id="row165279486526"><th class="cellrowborder" valign="top" width="32.47%" id="mcps1.2.4.1.1"><p id="p202471645134218"><a name="p202471645134218"></a><a name="p202471645134218"></a><strong id="b134048273508"><a name="b134048273508"></a><a name="b134048273508"></a>Flavor Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="29.87%" id="mcps1.2.4.1.2"><p id="p2038862911476"><a name="p2038862911476"></a><a name="p2038862911476"></a><strong id="b842352706193754"><a name="b842352706193754"></a><a name="b842352706193754"></a>vCPUs</strong></p>
</th>
<th class="cellrowborder" valign="top" width="37.66%" id="mcps1.2.4.1.3"><p id="p838892910478"><a name="p838892910478"></a><a name="p838892910478"></a><strong id="b84235270619382"><a name="b84235270619382"></a><a name="b84235270619382"></a>Memory (RAM in GB)</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row16527174818526"><td class="cellrowborder" valign="top" width="32.47%" headers="mcps1.2.4.1.1 "><p id="p27530067203215"><a name="p27530067203215"></a><a name="p27530067203215"></a>m3.large.8</p>
</td>
<td class="cellrowborder" valign="top" width="29.87%" headers="mcps1.2.4.1.2 "><p id="p17443704203215"><a name="p17443704203215"></a><a name="p17443704203215"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="37.66%" headers="mcps1.2.4.1.3 "><p id="p59515798203733"><a name="p59515798203733"></a><a name="p59515798203733"></a>16</p>
</td>
</tr>
<tr id="row152754835211"><td class="cellrowborder" valign="top" width="32.47%" headers="mcps1.2.4.1.1 "><p id="p1535699203215"><a name="p1535699203215"></a><a name="p1535699203215"></a>m3.xlarge.8</p>
</td>
<td class="cellrowborder" valign="top" width="29.87%" headers="mcps1.2.4.1.2 "><p id="p1115135203215"><a name="p1115135203215"></a><a name="p1115135203215"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="37.66%" headers="mcps1.2.4.1.3 "><p id="p61879054203733"><a name="p61879054203733"></a><a name="p61879054203733"></a>32</p>
</td>
</tr>
<tr id="row1652718484520"><td class="cellrowborder" valign="top" width="32.47%" headers="mcps1.2.4.1.1 "><p id="p30035298203220"><a name="p30035298203220"></a><a name="p30035298203220"></a>m3.2xlarge.8</p>
</td>
<td class="cellrowborder" valign="top" width="29.87%" headers="mcps1.2.4.1.2 "><p id="p27498652203220"><a name="p27498652203220"></a><a name="p27498652203220"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="37.66%" headers="mcps1.2.4.1.3 "><p id="p16852482203733"><a name="p16852482203733"></a><a name="p16852482203733"></a>64</p>
</td>
</tr>
<tr id="row5527114835210"><td class="cellrowborder" valign="top" width="32.47%" headers="mcps1.2.4.1.1 "><p id="p34482845203220"><a name="p34482845203220"></a><a name="p34482845203220"></a>m3.4xlarge.8</p>
</td>
<td class="cellrowborder" valign="top" width="29.87%" headers="mcps1.2.4.1.2 "><p id="p46554934203220"><a name="p46554934203220"></a><a name="p46554934203220"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="37.66%" headers="mcps1.2.4.1.3 "><p id="p30368433203733"><a name="p30368433203733"></a><a name="p30368433203733"></a>128</p>
</td>
</tr>
<tr id="row332193415414"><td class="cellrowborder" valign="top" width="32.47%" headers="mcps1.2.4.1.1 "><p id="p38487038203220"><a name="p38487038203220"></a><a name="p38487038203220"></a>m3.8xlarge.8</p>
</td>
<td class="cellrowborder" valign="top" width="29.87%" headers="mcps1.2.4.1.2 "><p id="p43855233203220"><a name="p43855233203220"></a><a name="p43855233203220"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="37.66%" headers="mcps1.2.4.1.3 "><p id="p13904994203733"><a name="p13904994203733"></a><a name="p13904994203733"></a>256</p>
</td>
</tr>
<tr id="row3527648155219"><td class="cellrowborder" valign="top" width="32.47%" headers="mcps1.2.4.1.1 "><p id="p25120671203636"><a name="p25120671203636"></a><a name="p25120671203636"></a>m3.15xlarge.8</p>
</td>
<td class="cellrowborder" valign="top" width="29.87%" headers="mcps1.2.4.1.2 "><p id="p36263685203636"><a name="p36263685203636"></a><a name="p36263685203636"></a>60</p>
</td>
<td class="cellrowborder" valign="top" width="37.66%" headers="mcps1.2.4.1.3 "><p id="p51677410203636"><a name="p51677410203636"></a><a name="p51677410203636"></a>512</p>
</td>
</tr>
</tbody>
</table>

