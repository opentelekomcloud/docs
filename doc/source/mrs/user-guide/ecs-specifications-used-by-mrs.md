# ECS Specifications Used by MRS<a name="EN-US_TOPIC_0221415923"></a>

MRS uses ECSs of the following types in different application scenarios.

-   General computing \(S1\)
-   General computing \(C2\)
-   General computing-plus \(C3\)
-   General computing-plus \(C4\)
-   Disk-intensive \(D1\)
-   Disk-intensive \(D2\)
-   High-performance computing \(H1\)
-   Memory-optimized \(M3\)
-   Memory-optimized \(M4\)

## ECS Flavor Naming Rules<a name="en-us_topic_0220013660_section741930611313"></a>

AB.C.D

Example: m3.8xlarge.8

In the preceding flavor:

-   **A**  specifies the ECS type. For example,  **s**  indicates a general-purpose ECS,  **c**  a computing ECS, and  **m**  a memory-optimized ECS.
-   **B**  specifies the type ID. For example, the  **1**  in  **s1**  indicates a general-purpose first-generation ECS, and the  **2**  in  **s2**  indicates a general-purpose second-generation ECS.
-   **C**  specifies a flavor size and can be any of the following options: medium, large, and xlarge.
-   **D**  specifies the ratio of memory to vCPUs expressed in a digit. For example, value  **4**  indicates that the ratio of memory to vCPUs is 4.

## Specifications<a name="en-us_topic_0220013660_section1399585312355"></a>

**Table  1**  S1 ECS specifications

<a name="en-us_topic_0220013660_table66778917103035"></a>
<table><thead align="left"><tr id="en-us_topic_0220013660_row21254511103035"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.6.1.1"><p id="en-us_topic_0220013660_p52972653162927"><a name="en-us_topic_0220013660_p52972653162927"></a><a name="en-us_topic_0220013660_p52972653162927"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="23%" id="mcps1.2.6.1.2"><p id="en-us_topic_0220013660_p62926494162927"><a name="en-us_topic_0220013660_p62926494162927"></a><a name="en-us_topic_0220013660_p62926494162927"></a>vCPUs</p>
</th>
<th class="cellrowborder" valign="top" width="21%" id="mcps1.2.6.1.3"><p id="en-us_topic_0220013660_p63881219162927"><a name="en-us_topic_0220013660_p63881219162927"></a><a name="en-us_topic_0220013660_p63881219162927"></a>Memory (GB)</p>
</th>
<th class="cellrowborder" valign="top" width="21%" id="mcps1.2.6.1.4"><p id="en-us_topic_0220013660_p6996228162927"><a name="en-us_topic_0220013660_p6996228162927"></a><a name="en-us_topic_0220013660_p6996228162927"></a>Flavor</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.6.1.5"><p id="en-us_topic_0220013660_p19167123116295"><a name="en-us_topic_0220013660_p19167123116295"></a><a name="en-us_topic_0220013660_p19167123116295"></a>Virtualization Type</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0220013660_row8532241591"><td class="cellrowborder" rowspan="3" valign="top" width="23%" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0220013660_p3534747915"><a name="en-us_topic_0220013660_p3534747915"></a><a name="en-us_topic_0220013660_p3534747915"></a>S1</p>
<p id="en-us_topic_0220013660_p15824165112920"><a name="en-us_topic_0220013660_p15824165112920"></a><a name="en-us_topic_0220013660_p15824165112920"></a></p>
<p id="en-us_topic_0220013660_p114844523910"><a name="en-us_topic_0220013660_p114844523910"></a><a name="en-us_topic_0220013660_p114844523910"></a></p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0220013660_p2302959557"><a name="en-us_topic_0220013660_p2302959557"></a><a name="en-us_topic_0220013660_p2302959557"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0220013660_p33037525517"><a name="en-us_topic_0220013660_p33037525517"></a><a name="en-us_topic_0220013660_p33037525517"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0220013660_p1595765119474"><a name="en-us_topic_0220013660_p1595765119474"></a><a name="en-us_topic_0220013660_p1595765119474"></a>s1.xlarge.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.6.1.5 "><p id="en-us_topic_0220013660_p612815911919"><a name="en-us_topic_0220013660_p612815911919"></a><a name="en-us_topic_0220013660_p612815911919"></a>XEN</p>
</td>
</tr>
<tr id="en-us_topic_0220013660_row98249514915"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0220013660_p8666211135514"><a name="en-us_topic_0220013660_p8666211135514"></a><a name="en-us_topic_0220013660_p8666211135514"></a>16</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0220013660_p566681116551"><a name="en-us_topic_0220013660_p566681116551"></a><a name="en-us_topic_0220013660_p566681116551"></a>64</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0220013660_p1931920523532"><a name="en-us_topic_0220013660_p1931920523532"></a><a name="en-us_topic_0220013660_p1931920523532"></a>s1.4xlarge.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0220013660_p17814459790"><a name="en-us_topic_0220013660_p17814459790"></a><a name="en-us_topic_0220013660_p17814459790"></a>XEN</p>
</td>
</tr>
<tr id="en-us_topic_0220013660_row34841252894"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0220013660_p566617118550"><a name="en-us_topic_0220013660_p566617118550"></a><a name="en-us_topic_0220013660_p566617118550"></a>32</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0220013660_p15666511115520"><a name="en-us_topic_0220013660_p15666511115520"></a><a name="en-us_topic_0220013660_p15666511115520"></a>128</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0220013660_p1831916526534"><a name="en-us_topic_0220013660_p1831916526534"></a><a name="en-us_topic_0220013660_p1831916526534"></a>s1.8xlarge.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0220013660_p1950414018107"><a name="en-us_topic_0220013660_p1950414018107"></a><a name="en-us_topic_0220013660_p1950414018107"></a>XEN</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  C2 ECS specifications

<a name="en-us_topic_0220013660_table367241161115"></a>
<table><thead align="left"><tr id="en-us_topic_0220013660_row118484141119"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.6.1.1"><p id="en-us_topic_0220013660_p1392144120110"><a name="en-us_topic_0220013660_p1392144120110"></a><a name="en-us_topic_0220013660_p1392144120110"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="23%" id="mcps1.2.6.1.2"><p id="en-us_topic_0220013660_p1296184111116"><a name="en-us_topic_0220013660_p1296184111116"></a><a name="en-us_topic_0220013660_p1296184111116"></a>vCPUs</p>
</th>
<th class="cellrowborder" valign="top" width="21%" id="mcps1.2.6.1.3"><p id="en-us_topic_0220013660_p149884171118"><a name="en-us_topic_0220013660_p149884171118"></a><a name="en-us_topic_0220013660_p149884171118"></a>Memory (GB)</p>
</th>
<th class="cellrowborder" valign="top" width="21%" id="mcps1.2.6.1.4"><p id="en-us_topic_0220013660_p10102241121115"><a name="en-us_topic_0220013660_p10102241121115"></a><a name="en-us_topic_0220013660_p10102241121115"></a>Flavor</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.6.1.5"><p id="en-us_topic_0220013660_p8104154117112"><a name="en-us_topic_0220013660_p8104154117112"></a><a name="en-us_topic_0220013660_p8104154117112"></a>Virtualization Type</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0220013660_row6824183441213"><td class="cellrowborder" rowspan="2" valign="top" width="23%" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0220013660_p13262641141118"><a name="en-us_topic_0220013660_p13262641141118"></a><a name="en-us_topic_0220013660_p13262641141118"></a>C2</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0220013660_p351101995520"><a name="en-us_topic_0220013660_p351101995520"></a><a name="en-us_topic_0220013660_p351101995520"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0220013660_p115191910553"><a name="en-us_topic_0220013660_p115191910553"></a><a name="en-us_topic_0220013660_p115191910553"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0220013660_p13515267546"><a name="en-us_topic_0220013660_p13515267546"></a><a name="en-us_topic_0220013660_p13515267546"></a>c2.2xlarge.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.6.1.5 "><p id="en-us_topic_0220013660_p138255348122"><a name="en-us_topic_0220013660_p138255348122"></a><a name="en-us_topic_0220013660_p138255348122"></a>KVM</p>
</td>
</tr>
<tr id="en-us_topic_0220013660_row1526034121120"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0220013660_p18511119165514"><a name="en-us_topic_0220013660_p18511119165514"></a><a name="en-us_topic_0220013660_p18511119165514"></a>16</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0220013660_p11511419175515"><a name="en-us_topic_0220013660_p11511419175515"></a><a name="en-us_topic_0220013660_p11511419175515"></a>32</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0220013660_p19515176135414"><a name="en-us_topic_0220013660_p19515176135414"></a><a name="en-us_topic_0220013660_p19515176135414"></a>c2.4xlarge.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0220013660_p82781241141113"><a name="en-us_topic_0220013660_p82781241141113"></a><a name="en-us_topic_0220013660_p82781241141113"></a>KVM</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  General computing-plus \(C3\) ECS specifications

<a name="en-us_topic_0220013660_table3949605220464"></a>
<table><thead align="left"><tr id="en-us_topic_0220013660_row5755737620464"><th class="cellrowborder" valign="top" width="23.232323232323235%" id="mcps1.2.6.1.1"><p id="en-us_topic_0220013660_p32920979204624"><a name="en-us_topic_0220013660_p32920979204624"></a><a name="en-us_topic_0220013660_p32920979204624"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="23.232323232323235%" id="mcps1.2.6.1.2"><p id="en-us_topic_0220013660_p41529665204624"><a name="en-us_topic_0220013660_p41529665204624"></a><a name="en-us_topic_0220013660_p41529665204624"></a>vCPUs</p>
</th>
<th class="cellrowborder" valign="top" width="19.191919191919194%" id="mcps1.2.6.1.3"><p id="en-us_topic_0220013660_p9028760204624"><a name="en-us_topic_0220013660_p9028760204624"></a><a name="en-us_topic_0220013660_p9028760204624"></a>Memory (GB)</p>
</th>
<th class="cellrowborder" valign="top" width="22.222222222222225%" id="mcps1.2.6.1.4"><p id="en-us_topic_0220013660_p5297585204624"><a name="en-us_topic_0220013660_p5297585204624"></a><a name="en-us_topic_0220013660_p5297585204624"></a>Flavor</p>
</th>
<th class="cellrowborder" valign="top" width="12.121212121212121%" id="mcps1.2.6.1.5"><p id="en-us_topic_0220013660_p84201252123120"><a name="en-us_topic_0220013660_p84201252123120"></a><a name="en-us_topic_0220013660_p84201252123120"></a>Virtualization Type</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0220013660_row2115659920464"><td class="cellrowborder" rowspan="7" valign="top" width="23.232323232323235%" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0220013660_p1639654719185"><a name="en-us_topic_0220013660_p1639654719185"></a><a name="en-us_topic_0220013660_p1639654719185"></a>C3</p>
</td>
<td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0220013660_p1478753518587"><a name="en-us_topic_0220013660_p1478753518587"></a><a name="en-us_topic_0220013660_p1478753518587"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0220013660_p57871235145814"><a name="en-us_topic_0220013660_p57871235145814"></a><a name="en-us_topic_0220013660_p57871235145814"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0220013660_p1983291835812"><a name="en-us_topic_0220013660_p1983291835812"></a><a name="en-us_topic_0220013660_p1983291835812"></a>c3.2xlarge.2.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.6.1.5 "><p id="en-us_topic_0220013660_p714614176327"><a name="en-us_topic_0220013660_p714614176327"></a><a name="en-us_topic_0220013660_p714614176327"></a>KVM</p>
</td>
</tr>
<tr id="en-us_topic_0220013660_row1339712614367"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0220013660_p1478793525820"><a name="en-us_topic_0220013660_p1478793525820"></a><a name="en-us_topic_0220013660_p1478793525820"></a>4</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0220013660_p778723555817"><a name="en-us_topic_0220013660_p778723555817"></a><a name="en-us_topic_0220013660_p778723555817"></a>16</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0220013660_p58321185585"><a name="en-us_topic_0220013660_p58321185585"></a><a name="en-us_topic_0220013660_p58321185585"></a>c3.xlarge.4.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0220013660_p9361114613616"><a name="en-us_topic_0220013660_p9361114613616"></a><a name="en-us_topic_0220013660_p9361114613616"></a>KVM</p>
</td>
</tr>
<tr id="en-us_topic_0220013660_row58396907204611"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0220013660_p1778713512588"><a name="en-us_topic_0220013660_p1778713512588"></a><a name="en-us_topic_0220013660_p1778713512588"></a>8</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0220013660_p27873357588"><a name="en-us_topic_0220013660_p27873357588"></a><a name="en-us_topic_0220013660_p27873357588"></a>32</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0220013660_p683231814581"><a name="en-us_topic_0220013660_p683231814581"></a><a name="en-us_topic_0220013660_p683231814581"></a>c3.2xlarge.4.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0220013660_p1160181710322"><a name="en-us_topic_0220013660_p1160181710322"></a><a name="en-us_topic_0220013660_p1160181710322"></a>KVM</p>
</td>
</tr>
<tr id="en-us_topic_0220013660_row19288388204611"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0220013660_p10787235105818"><a name="en-us_topic_0220013660_p10787235105818"></a><a name="en-us_topic_0220013660_p10787235105818"></a>16</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0220013660_p378719357584"><a name="en-us_topic_0220013660_p378719357584"></a><a name="en-us_topic_0220013660_p378719357584"></a>32</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0220013660_p1483221817585"><a name="en-us_topic_0220013660_p1483221817585"></a><a name="en-us_topic_0220013660_p1483221817585"></a>c3.4xlarge.2.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0220013660_p11163171763213"><a name="en-us_topic_0220013660_p11163171763213"></a><a name="en-us_topic_0220013660_p11163171763213"></a>KVM</p>
</td>
</tr>
<tr id="en-us_topic_0220013660_row39706029204611"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0220013660_p19787133585814"><a name="en-us_topic_0220013660_p19787133585814"></a><a name="en-us_topic_0220013660_p19787133585814"></a>16</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0220013660_p6787173545812"><a name="en-us_topic_0220013660_p6787173545812"></a><a name="en-us_topic_0220013660_p6787173545812"></a>64</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0220013660_p1883219185581"><a name="en-us_topic_0220013660_p1883219185581"></a><a name="en-us_topic_0220013660_p1883219185581"></a>c3.4xlarge.4.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0220013660_p14657219153217"><a name="en-us_topic_0220013660_p14657219153217"></a><a name="en-us_topic_0220013660_p14657219153217"></a>KVM</p>
</td>
</tr>
<tr id="en-us_topic_0220013660_row4280432102715"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0220013660_p634214211587"><a name="en-us_topic_0220013660_p634214211587"></a><a name="en-us_topic_0220013660_p634214211587"></a>32</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0220013660_p63421642145814"><a name="en-us_topic_0220013660_p63421642145814"></a><a name="en-us_topic_0220013660_p63421642145814"></a>128</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0220013660_p1537512712586"><a name="en-us_topic_0220013660_p1537512712586"></a><a name="en-us_topic_0220013660_p1537512712586"></a>c3.8xlarge.4.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0220013660_p14281153262720"><a name="en-us_topic_0220013660_p14281153262720"></a><a name="en-us_topic_0220013660_p14281153262720"></a>KVM</p>
</td>
</tr>
<tr id="en-us_topic_0220013660_row28491536204611"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0220013660_p113421742175817"><a name="en-us_topic_0220013660_p113421742175817"></a><a name="en-us_topic_0220013660_p113421742175817"></a>60</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0220013660_p1734374235817"><a name="en-us_topic_0220013660_p1734374235817"></a><a name="en-us_topic_0220013660_p1734374235817"></a>256</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0220013660_p113751827145816"><a name="en-us_topic_0220013660_p113751827145816"></a><a name="en-us_topic_0220013660_p113751827145816"></a>c3.15xlarge.4.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0220013660_p16664419133218"><a name="en-us_topic_0220013660_p16664419133218"></a><a name="en-us_topic_0220013660_p16664419133218"></a>KVM</p>
</td>
</tr>
</tbody>
</table>

**Table  4**  C4 ECS specifications

<a name="en-us_topic_0220013660_table823966144719"></a>
<table><thead align="left"><tr id="en-us_topic_0220013660_row1825415614476"><th class="cellrowborder" valign="top" width="23.232323232323235%" id="mcps1.2.6.1.1"><p id="en-us_topic_0220013660_p42622610479"><a name="en-us_topic_0220013660_p42622610479"></a><a name="en-us_topic_0220013660_p42622610479"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="23.232323232323235%" id="mcps1.2.6.1.2"><p id="en-us_topic_0220013660_p1926526104711"><a name="en-us_topic_0220013660_p1926526104711"></a><a name="en-us_topic_0220013660_p1926526104711"></a>vCPUs</p>
</th>
<th class="cellrowborder" valign="top" width="19.191919191919194%" id="mcps1.2.6.1.3"><p id="en-us_topic_0220013660_p17269146104710"><a name="en-us_topic_0220013660_p17269146104710"></a><a name="en-us_topic_0220013660_p17269146104710"></a>Memory (GB)</p>
</th>
<th class="cellrowborder" valign="top" width="22.222222222222225%" id="mcps1.2.6.1.4"><p id="en-us_topic_0220013660_p1527246134711"><a name="en-us_topic_0220013660_p1527246134711"></a><a name="en-us_topic_0220013660_p1527246134711"></a>Flavor</p>
</th>
<th class="cellrowborder" valign="top" width="12.121212121212121%" id="mcps1.2.6.1.5"><p id="en-us_topic_0220013660_p92745613476"><a name="en-us_topic_0220013660_p92745613476"></a><a name="en-us_topic_0220013660_p92745613476"></a>Virtualization Type</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0220013660_row102796664710"><td class="cellrowborder" rowspan="8" valign="top" width="23.232323232323235%" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0220013660_p5281967474"><a name="en-us_topic_0220013660_p5281967474"></a><a name="en-us_topic_0220013660_p5281967474"></a>C4</p>
<p id="en-us_topic_0220013660_p18879453579"><a name="en-us_topic_0220013660_p18879453579"></a><a name="en-us_topic_0220013660_p18879453579"></a></p>
<p id="en-us_topic_0220013660_p96176451570"><a name="en-us_topic_0220013660_p96176451570"></a><a name="en-us_topic_0220013660_p96176451570"></a></p>
<p id="en-us_topic_0220013660_p101149468578"><a name="en-us_topic_0220013660_p101149468578"></a><a name="en-us_topic_0220013660_p101149468578"></a></p>
<p id="en-us_topic_0220013660_p1617646195717"><a name="en-us_topic_0220013660_p1617646195717"></a><a name="en-us_topic_0220013660_p1617646195717"></a></p>
<p id="en-us_topic_0220013660_p14152247145713"><a name="en-us_topic_0220013660_p14152247145713"></a><a name="en-us_topic_0220013660_p14152247145713"></a></p>
</td>
<td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0220013660_p17748145920017"><a name="en-us_topic_0220013660_p17748145920017"></a><a name="en-us_topic_0220013660_p17748145920017"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0220013660_p19748155917018"><a name="en-us_topic_0220013660_p19748155917018"></a><a name="en-us_topic_0220013660_p19748155917018"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0220013660_p14844152503"><a name="en-us_topic_0220013660_p14844152503"></a><a name="en-us_topic_0220013660_p14844152503"></a>c4.xlarge.4.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.6.1.5 "><p id="en-us_topic_0220013660_p829217654716"><a name="en-us_topic_0220013660_p829217654716"></a><a name="en-us_topic_0220013660_p829217654716"></a>KVM</p>
</td>
</tr>
<tr id="en-us_topic_0220013660_row14295146164711"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0220013660_p974855914017"><a name="en-us_topic_0220013660_p974855914017"></a><a name="en-us_topic_0220013660_p974855914017"></a>8</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0220013660_p13748185914017"><a name="en-us_topic_0220013660_p13748185914017"></a><a name="en-us_topic_0220013660_p13748185914017"></a>16</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0220013660_p6844152201"><a name="en-us_topic_0220013660_p6844152201"></a><a name="en-us_topic_0220013660_p6844152201"></a>c4.2xlarge.2.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0220013660_p8310136154720"><a name="en-us_topic_0220013660_p8310136154720"></a><a name="en-us_topic_0220013660_p8310136154720"></a>KVM</p>
</td>
</tr>
<tr id="en-us_topic_0220013660_row183421766474"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0220013660_p127489592011"><a name="en-us_topic_0220013660_p127489592011"></a><a name="en-us_topic_0220013660_p127489592011"></a>8</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0220013660_p1474815916012"><a name="en-us_topic_0220013660_p1474815916012"></a><a name="en-us_topic_0220013660_p1474815916012"></a>32</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0220013660_p18844152804"><a name="en-us_topic_0220013660_p18844152804"></a><a name="en-us_topic_0220013660_p18844152804"></a>c4.2xlarge.4.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0220013660_p635556134711"><a name="en-us_topic_0220013660_p635556134711"></a><a name="en-us_topic_0220013660_p635556134711"></a>KVM</p>
</td>
</tr>
<tr id="en-us_topic_0220013660_row98744511577"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0220013660_p127480599014"><a name="en-us_topic_0220013660_p127480599014"></a><a name="en-us_topic_0220013660_p127480599014"></a>16</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0220013660_p197486591202"><a name="en-us_topic_0220013660_p197486591202"></a><a name="en-us_topic_0220013660_p197486591202"></a>32</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0220013660_p178445521209"><a name="en-us_topic_0220013660_p178445521209"></a><a name="en-us_topic_0220013660_p178445521209"></a>c4.4xlarge.2.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0220013660_p1987145165717"><a name="en-us_topic_0220013660_p1987145165717"></a><a name="en-us_topic_0220013660_p1987145165717"></a>KVM</p>
</td>
</tr>
<tr id="en-us_topic_0220013660_row15617134555715"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0220013660_p274810598010"><a name="en-us_topic_0220013660_p274810598010"></a><a name="en-us_topic_0220013660_p274810598010"></a>16</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0220013660_p197481359307"><a name="en-us_topic_0220013660_p197481359307"></a><a name="en-us_topic_0220013660_p197481359307"></a>64</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0220013660_p17844352104"><a name="en-us_topic_0220013660_p17844352104"></a><a name="en-us_topic_0220013660_p17844352104"></a>c4.4xlarge.4.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0220013660_p161715457573"><a name="en-us_topic_0220013660_p161715457573"></a><a name="en-us_topic_0220013660_p161715457573"></a>KVM</p>
</td>
</tr>
<tr id="en-us_topic_0220013660_row1411413460575"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0220013660_p2074885914010"><a name="en-us_topic_0220013660_p2074885914010"></a><a name="en-us_topic_0220013660_p2074885914010"></a>32</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0220013660_p1574919591309"><a name="en-us_topic_0220013660_p1574919591309"></a><a name="en-us_topic_0220013660_p1574919591309"></a>64</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0220013660_p178444521109"><a name="en-us_topic_0220013660_p178444521109"></a><a name="en-us_topic_0220013660_p178444521109"></a>c4.8xlarge.2.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0220013660_p711494617574"><a name="en-us_topic_0220013660_p711494617574"></a><a name="en-us_topic_0220013660_p711494617574"></a>KVM</p>
</td>
</tr>
<tr id="en-us_topic_0220013660_row161711466576"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0220013660_p0749159101"><a name="en-us_topic_0220013660_p0749159101"></a><a name="en-us_topic_0220013660_p0749159101"></a>32</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0220013660_p47497599014"><a name="en-us_topic_0220013660_p47497599014"></a><a name="en-us_topic_0220013660_p47497599014"></a>128</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0220013660_p98441652206"><a name="en-us_topic_0220013660_p98441652206"></a><a name="en-us_topic_0220013660_p98441652206"></a>c4.8xlarge.4.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0220013660_p9617346195710"><a name="en-us_topic_0220013660_p9617346195710"></a><a name="en-us_topic_0220013660_p9617346195710"></a>KVM</p>
</td>
</tr>
<tr id="en-us_topic_0220013660_row8152114795716"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0220013660_p107492591704"><a name="en-us_topic_0220013660_p107492591704"></a><a name="en-us_topic_0220013660_p107492591704"></a>64</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0220013660_p117495599017"><a name="en-us_topic_0220013660_p117495599017"></a><a name="en-us_topic_0220013660_p117495599017"></a>256</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0220013660_p1584475215018"><a name="en-us_topic_0220013660_p1584475215018"></a><a name="en-us_topic_0220013660_p1584475215018"></a>c4.16xlarge.4.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0220013660_p1415274705715"><a name="en-us_topic_0220013660_p1415274705715"></a><a name="en-us_topic_0220013660_p1415274705715"></a>KVM</p>
</td>
</tr>
</tbody>
</table>

**Table  5**  D1 ECS specifications

<a name="en-us_topic_0220013660_table47541937112515"></a>
<table><thead align="left"><tr id="en-us_topic_0220013660_row1775413371257"><th class="cellrowborder" valign="top" width="13%" id="mcps1.2.8.1.1"><p id="en-us_topic_0220013660_p17228105016252"><a name="en-us_topic_0220013660_p17228105016252"></a><a name="en-us_topic_0220013660_p17228105016252"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="8%" id="mcps1.2.8.1.2"><p id="en-us_topic_0220013660_p123165013254"><a name="en-us_topic_0220013660_p123165013254"></a><a name="en-us_topic_0220013660_p123165013254"></a>vCPUs</p>
</th>
<th class="cellrowborder" valign="top" width="11%" id="mcps1.2.8.1.3"><p id="en-us_topic_0220013660_p7236185013252"><a name="en-us_topic_0220013660_p7236185013252"></a><a name="en-us_topic_0220013660_p7236185013252"></a>Memory (GB)</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.8.1.4"><p id="en-us_topic_0220013660_p18237155062514"><a name="en-us_topic_0220013660_p18237155062514"></a><a name="en-us_topic_0220013660_p18237155062514"></a>Flavor</p>
</th>
<th class="cellrowborder" valign="top" width="11%" id="mcps1.2.8.1.5"><p id="en-us_topic_0220013660_p724035017257"><a name="en-us_topic_0220013660_p724035017257"></a><a name="en-us_topic_0220013660_p724035017257"></a>Virtualization Type</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.8.1.6"><p id="en-us_topic_0220013660_p1624105092519"><a name="en-us_topic_0220013660_p1624105092519"></a><a name="en-us_topic_0220013660_p1624105092519"></a>Local Disk (GB)</p>
</th>
<th class="cellrowborder" valign="top" width="28.999999999999996%" id="mcps1.2.8.1.7"><p id="en-us_topic_0220013660_p9205101061511"><a name="en-us_topic_0220013660_p9205101061511"></a><a name="en-us_topic_0220013660_p9205101061511"></a>Hardware</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0220013660_row974834394812"><td class="cellrowborder" rowspan="4" valign="top" width="13%" headers="mcps1.2.8.1.1 "><p id="en-us_topic_0220013660_p9760548192919"><a name="en-us_topic_0220013660_p9760548192919"></a><a name="en-us_topic_0220013660_p9760548192919"></a>D1</p>
<p id="en-us_topic_0220013660_p18258142365410"><a name="en-us_topic_0220013660_p18258142365410"></a><a name="en-us_topic_0220013660_p18258142365410"></a></p>
</td>
<td class="cellrowborder" valign="top" width="8%" headers="mcps1.2.8.1.2 "><p id="en-us_topic_0220013660_p787054695413"><a name="en-us_topic_0220013660_p787054695413"></a><a name="en-us_topic_0220013660_p787054695413"></a>44</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.8.1.3 "><p id="en-us_topic_0220013660_p128705468546"><a name="en-us_topic_0220013660_p128705468546"></a><a name="en-us_topic_0220013660_p128705468546"></a>3232</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.8.1.4 "><p id="en-us_topic_0220013660_p164813321546"><a name="en-us_topic_0220013660_p164813321546"></a><a name="en-us_topic_0220013660_p164813321546"></a>d1.xlarge.mrslinux.mrs</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.8.1.5 "><p id="en-us_topic_0220013660_p1875013430483"><a name="en-us_topic_0220013660_p1875013430483"></a><a name="en-us_topic_0220013660_p1875013430483"></a>KVM</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.8.1.6 "><p id="en-us_topic_0220013660_p17750443104811"><a name="en-us_topic_0220013660_p17750443104811"></a><a name="en-us_topic_0220013660_p17750443104811"></a>3×1800</p>
</td>
<td class="cellrowborder" rowspan="4" valign="top" width="28.999999999999996%" headers="mcps1.2.8.1.7 "><p id="en-us_topic_0220013660_p449920318167"><a name="en-us_topic_0220013660_p449920318167"></a><a name="en-us_topic_0220013660_p449920318167"></a>CPU: Intel&reg; Xeon&reg; Gold 6151 Processor v5</p>
<p id="en-us_topic_0220013660_p676115981618"><a name="en-us_topic_0220013660_p676115981618"></a><a name="en-us_topic_0220013660_p676115981618"></a>Memory: 20 × 32 GB</p>
<p id="en-us_topic_0220013660_p1525820237549"><a name="en-us_topic_0220013660_p1525820237549"></a><a name="en-us_topic_0220013660_p1525820237549"></a></p>
</td>
</tr>
<tr id="en-us_topic_0220013660_row14967171717297"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="en-us_topic_0220013660_p887044665417"><a name="en-us_topic_0220013660_p887044665417"></a><a name="en-us_topic_0220013660_p887044665417"></a>88</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="en-us_topic_0220013660_p1287004610547"><a name="en-us_topic_0220013660_p1287004610547"></a><a name="en-us_topic_0220013660_p1287004610547"></a>6464</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="en-us_topic_0220013660_p7648832155416"><a name="en-us_topic_0220013660_p7648832155416"></a><a name="en-us_topic_0220013660_p7648832155416"></a>d1.2xlarge.mrslinux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="en-us_topic_0220013660_p10967117172915"><a name="en-us_topic_0220013660_p10967117172915"></a><a name="en-us_topic_0220013660_p10967117172915"></a>KVM</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="en-us_topic_0220013660_p169678175293"><a name="en-us_topic_0220013660_p169678175293"></a><a name="en-us_topic_0220013660_p169678175293"></a>6×1800</p>
</td>
</tr>
<tr id="en-us_topic_0220013660_row575615372253"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="en-us_topic_0220013660_p158705469542"><a name="en-us_topic_0220013660_p158705469542"></a><a name="en-us_topic_0220013660_p158705469542"></a>16</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="en-us_topic_0220013660_p6870246145413"><a name="en-us_topic_0220013660_p6870246145413"></a><a name="en-us_topic_0220013660_p6870246145413"></a>128</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="en-us_topic_0220013660_p1964873265412"><a name="en-us_topic_0220013660_p1964873265412"></a><a name="en-us_topic_0220013660_p1964873265412"></a>d1.4xlarge.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="en-us_topic_0220013660_p10756133715250"><a name="en-us_topic_0220013660_p10756133715250"></a><a name="en-us_topic_0220013660_p10756133715250"></a>KVM</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="en-us_topic_0220013660_p1675663717258"><a name="en-us_topic_0220013660_p1675663717258"></a><a name="en-us_topic_0220013660_p1675663717258"></a>12×1800</p>
</td>
</tr>
<tr id="en-us_topic_0220013660_row18257162325419"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="en-us_topic_0220013660_p148701462540"><a name="en-us_topic_0220013660_p148701462540"></a><a name="en-us_topic_0220013660_p148701462540"></a>36</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="en-us_topic_0220013660_p9870164610544"><a name="en-us_topic_0220013660_p9870164610544"></a><a name="en-us_topic_0220013660_p9870164610544"></a>256</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="en-us_topic_0220013660_p11648183218542"><a name="en-us_topic_0220013660_p11648183218542"></a><a name="en-us_topic_0220013660_p11648183218542"></a>d1.8xlarge.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="en-us_topic_0220013660_p1225810232540"><a name="en-us_topic_0220013660_p1225810232540"></a><a name="en-us_topic_0220013660_p1225810232540"></a>KVM</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="en-us_topic_0220013660_p1925812235542"><a name="en-us_topic_0220013660_p1925812235542"></a><a name="en-us_topic_0220013660_p1925812235542"></a>24×1800</p>
</td>
</tr>
</tbody>
</table>

**Table  6**  D2 ECS specifications

<a name="en-us_topic_0220013660_table1215815565720"></a>
<table><thead align="left"><tr id="en-us_topic_0220013660_row419985115711"><th class="cellrowborder" valign="top" width="13%" id="mcps1.2.8.1.1"><p id="en-us_topic_0220013660_p8205115155714"><a name="en-us_topic_0220013660_p8205115155714"></a><a name="en-us_topic_0220013660_p8205115155714"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="8%" id="mcps1.2.8.1.2"><p id="en-us_topic_0220013660_p1521311515579"><a name="en-us_topic_0220013660_p1521311515579"></a><a name="en-us_topic_0220013660_p1521311515579"></a>vCPUs</p>
</th>
<th class="cellrowborder" valign="top" width="11%" id="mcps1.2.8.1.3"><p id="en-us_topic_0220013660_p19218155577"><a name="en-us_topic_0220013660_p19218155577"></a><a name="en-us_topic_0220013660_p19218155577"></a>Memory (GB)</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.8.1.4"><p id="en-us_topic_0220013660_p172241559574"><a name="en-us_topic_0220013660_p172241559574"></a><a name="en-us_topic_0220013660_p172241559574"></a>Flavor</p>
</th>
<th class="cellrowborder" valign="top" width="11%" id="mcps1.2.8.1.5"><p id="en-us_topic_0220013660_p182291595720"><a name="en-us_topic_0220013660_p182291595720"></a><a name="en-us_topic_0220013660_p182291595720"></a>Virtualization Type</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.8.1.6"><p id="en-us_topic_0220013660_p82336514571"><a name="en-us_topic_0220013660_p82336514571"></a><a name="en-us_topic_0220013660_p82336514571"></a>Local Disk (GB)</p>
</th>
<th class="cellrowborder" valign="top" width="28.999999999999996%" id="mcps1.2.8.1.7"><p id="en-us_topic_0220013660_p18238856576"><a name="en-us_topic_0220013660_p18238856576"></a><a name="en-us_topic_0220013660_p18238856576"></a>Hardware</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0220013660_row82414510575"><td class="cellrowborder" rowspan="4" valign="top" width="13%" headers="mcps1.2.8.1.1 "><p id="en-us_topic_0220013660_p18247155135712"><a name="en-us_topic_0220013660_p18247155135712"></a><a name="en-us_topic_0220013660_p18247155135712"></a>D2</p>
<p id="en-us_topic_0220013660_p791575319569"><a name="en-us_topic_0220013660_p791575319569"></a><a name="en-us_topic_0220013660_p791575319569"></a></p>
<p id="en-us_topic_0220013660_p541755414562"><a name="en-us_topic_0220013660_p541755414562"></a><a name="en-us_topic_0220013660_p541755414562"></a></p>
</td>
<td class="cellrowborder" valign="top" width="8%" headers="mcps1.2.8.1.2 "><p id="en-us_topic_0220013660_p112011279592"><a name="en-us_topic_0220013660_p112011279592"></a><a name="en-us_topic_0220013660_p112011279592"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.8.1.3 "><p id="en-us_topic_0220013660_p420827105920"><a name="en-us_topic_0220013660_p420827105920"></a><a name="en-us_topic_0220013660_p420827105920"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.8.1.4 "><p id="en-us_topic_0220013660_p16113117125917"><a name="en-us_topic_0220013660_p16113117125917"></a><a name="en-us_topic_0220013660_p16113117125917"></a>d2.xlarge.8.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.8.1.5 "><p id="en-us_topic_0220013660_p9268651572"><a name="en-us_topic_0220013660_p9268651572"></a><a name="en-us_topic_0220013660_p9268651572"></a>KVM</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.8.1.6 "><p id="en-us_topic_0220013660_p9271195185720"><a name="en-us_topic_0220013660_p9271195185720"></a><a name="en-us_topic_0220013660_p9271195185720"></a>2×1800</p>
</td>
<td class="cellrowborder" rowspan="4" valign="top" width="28.999999999999996%" headers="mcps1.2.8.1.7 "><p id="en-us_topic_0220013660_p1627812515571"><a name="en-us_topic_0220013660_p1627812515571"></a><a name="en-us_topic_0220013660_p1627812515571"></a>CPU: Intel&reg; Xeon&reg; Gold 6151 Processor v5</p>
<p id="en-us_topic_0220013660_p16281155145713"><a name="en-us_topic_0220013660_p16281155145713"></a><a name="en-us_topic_0220013660_p16281155145713"></a>Memory: 20 × 32 GB</p>
<p id="en-us_topic_0220013660_p29161553205613"><a name="en-us_topic_0220013660_p29161553205613"></a><a name="en-us_topic_0220013660_p29161553205613"></a></p>
<p id="en-us_topic_0220013660_p1841765414561"><a name="en-us_topic_0220013660_p1841765414561"></a><a name="en-us_topic_0220013660_p1841765414561"></a></p>
</td>
</tr>
<tr id="en-us_topic_0220013660_row112846595717"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="en-us_topic_0220013660_p182114279598"><a name="en-us_topic_0220013660_p182114279598"></a><a name="en-us_topic_0220013660_p182114279598"></a>8</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="en-us_topic_0220013660_p3254270595"><a name="en-us_topic_0220013660_p3254270595"></a><a name="en-us_topic_0220013660_p3254270595"></a>64</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="en-us_topic_0220013660_p411381785915"><a name="en-us_topic_0220013660_p411381785915"></a><a name="en-us_topic_0220013660_p411381785915"></a>d2.2xlarge.8.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="en-us_topic_0220013660_p231015512573"><a name="en-us_topic_0220013660_p231015512573"></a><a name="en-us_topic_0220013660_p231015512573"></a>KVM</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="en-us_topic_0220013660_p83154510577"><a name="en-us_topic_0220013660_p83154510577"></a><a name="en-us_topic_0220013660_p83154510577"></a>4×1800</p>
</td>
</tr>
<tr id="en-us_topic_0220013660_row18915195325616"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="en-us_topic_0220013660_p152572745914"><a name="en-us_topic_0220013660_p152572745914"></a><a name="en-us_topic_0220013660_p152572745914"></a>16</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="en-us_topic_0220013660_p5251227115917"><a name="en-us_topic_0220013660_p5251227115917"></a><a name="en-us_topic_0220013660_p5251227115917"></a>128</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="en-us_topic_0220013660_p19113417135916"><a name="en-us_topic_0220013660_p19113417135916"></a><a name="en-us_topic_0220013660_p19113417135916"></a>d2.4xlarge.8.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="en-us_topic_0220013660_p3915953135618"><a name="en-us_topic_0220013660_p3915953135618"></a><a name="en-us_topic_0220013660_p3915953135618"></a>KVM</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="en-us_topic_0220013660_p179153532567"><a name="en-us_topic_0220013660_p179153532567"></a><a name="en-us_topic_0220013660_p179153532567"></a>8×1800</p>
</td>
</tr>
<tr id="en-us_topic_0220013660_row74171254145617"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="en-us_topic_0220013660_p1525142710597"><a name="en-us_topic_0220013660_p1525142710597"></a><a name="en-us_topic_0220013660_p1525142710597"></a>32</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="en-us_topic_0220013660_p8253277598"><a name="en-us_topic_0220013660_p8253277598"></a><a name="en-us_topic_0220013660_p8253277598"></a>256</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="en-us_topic_0220013660_p911391712598"><a name="en-us_topic_0220013660_p911391712598"></a><a name="en-us_topic_0220013660_p911391712598"></a>d2.8xlarge.8.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="en-us_topic_0220013660_p17417554145618"><a name="en-us_topic_0220013660_p17417554145618"></a><a name="en-us_topic_0220013660_p17417554145618"></a>KVM</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="en-us_topic_0220013660_p6417175417566"><a name="en-us_topic_0220013660_p6417175417566"></a><a name="en-us_topic_0220013660_p6417175417566"></a>16×1800</p>
</td>
</tr>
</tbody>
</table>

**Table  7**  H1 ECS specifications

<a name="en-us_topic_0220013660_table0407254151418"></a>
<table><thead align="left"><tr id="en-us_topic_0220013660_row1443016544141"><th class="cellrowborder" valign="top" width="23.232323232323235%" id="mcps1.2.6.1.1"><p id="en-us_topic_0220013660_p74386548148"><a name="en-us_topic_0220013660_p74386548148"></a><a name="en-us_topic_0220013660_p74386548148"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="23.232323232323235%" id="mcps1.2.6.1.2"><p id="en-us_topic_0220013660_p14441195451411"><a name="en-us_topic_0220013660_p14441195451411"></a><a name="en-us_topic_0220013660_p14441195451411"></a>vCPUs</p>
</th>
<th class="cellrowborder" valign="top" width="19.191919191919194%" id="mcps1.2.6.1.3"><p id="en-us_topic_0220013660_p14446185417144"><a name="en-us_topic_0220013660_p14446185417144"></a><a name="en-us_topic_0220013660_p14446185417144"></a>Memory (GB)</p>
</th>
<th class="cellrowborder" valign="top" width="22.222222222222225%" id="mcps1.2.6.1.4"><p id="en-us_topic_0220013660_p9451145415145"><a name="en-us_topic_0220013660_p9451145415145"></a><a name="en-us_topic_0220013660_p9451145415145"></a>Flavor</p>
</th>
<th class="cellrowborder" valign="top" width="12.121212121212121%" id="mcps1.2.6.1.5"><p id="en-us_topic_0220013660_p245645461416"><a name="en-us_topic_0220013660_p245645461416"></a><a name="en-us_topic_0220013660_p245645461416"></a>Virtualization Type</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0220013660_row19460105414141"><td class="cellrowborder" rowspan="3" valign="top" width="23.232323232323235%" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0220013660_p6465154111411"><a name="en-us_topic_0220013660_p6465154111411"></a><a name="en-us_topic_0220013660_p6465154111411"></a>H1</p>
</td>
<td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0220013660_p1695312357558"><a name="en-us_topic_0220013660_p1695312357558"></a><a name="en-us_topic_0220013660_p1695312357558"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0220013660_p7953193517557"><a name="en-us_topic_0220013660_p7953193517557"></a><a name="en-us_topic_0220013660_p7953193517557"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0220013660_p6747153025518"><a name="en-us_topic_0220013660_p6747153025518"></a><a name="en-us_topic_0220013660_p6747153025518"></a>h1.2xlarge.4.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.6.1.5 "><p id="en-us_topic_0220013660_p164811954111418"><a name="en-us_topic_0220013660_p164811954111418"></a><a name="en-us_topic_0220013660_p164811954111418"></a>KVM</p>
</td>
</tr>
<tr id="en-us_topic_0220013660_row11482145411412"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0220013660_p10953103545519"><a name="en-us_topic_0220013660_p10953103545519"></a><a name="en-us_topic_0220013660_p10953103545519"></a>16</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0220013660_p19953235115517"><a name="en-us_topic_0220013660_p19953235115517"></a><a name="en-us_topic_0220013660_p19953235115517"></a>64</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0220013660_p15747113065511"><a name="en-us_topic_0220013660_p15747113065511"></a><a name="en-us_topic_0220013660_p15747113065511"></a>h1.4xlarge.4.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0220013660_p5497135420141"><a name="en-us_topic_0220013660_p5497135420141"></a><a name="en-us_topic_0220013660_p5497135420141"></a>KVM</p>
</td>
</tr>
<tr id="en-us_topic_0220013660_row150045421411"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0220013660_p20953135115519"><a name="en-us_topic_0220013660_p20953135115519"></a><a name="en-us_topic_0220013660_p20953135115519"></a>32</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0220013660_p295393585512"><a name="en-us_topic_0220013660_p295393585512"></a><a name="en-us_topic_0220013660_p295393585512"></a>128</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0220013660_p774714308553"><a name="en-us_topic_0220013660_p774714308553"></a><a name="en-us_topic_0220013660_p774714308553"></a>h1.8xlarge.4.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0220013660_p052175411143"><a name="en-us_topic_0220013660_p052175411143"></a><a name="en-us_topic_0220013660_p052175411143"></a>KVM</p>
</td>
</tr>
</tbody>
</table>

**Table  8**  M3 ECS specifications

<a name="en-us_topic_0220013660_table11173155712141"></a>
<table><thead align="left"><tr id="en-us_topic_0220013660_row11191105718140"><th class="cellrowborder" valign="top" width="23.232323232323235%" id="mcps1.2.6.1.1"><p id="en-us_topic_0220013660_p17196457201410"><a name="en-us_topic_0220013660_p17196457201410"></a><a name="en-us_topic_0220013660_p17196457201410"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="23.232323232323235%" id="mcps1.2.6.1.2"><p id="en-us_topic_0220013660_p20199175711411"><a name="en-us_topic_0220013660_p20199175711411"></a><a name="en-us_topic_0220013660_p20199175711411"></a>vCPUs</p>
</th>
<th class="cellrowborder" valign="top" width="19.191919191919194%" id="mcps1.2.6.1.3"><p id="en-us_topic_0220013660_p720319574148"><a name="en-us_topic_0220013660_p720319574148"></a><a name="en-us_topic_0220013660_p720319574148"></a>Memory (GB)</p>
</th>
<th class="cellrowborder" valign="top" width="22.222222222222225%" id="mcps1.2.6.1.4"><p id="en-us_topic_0220013660_p7208185781418"><a name="en-us_topic_0220013660_p7208185781418"></a><a name="en-us_topic_0220013660_p7208185781418"></a>Flavor</p>
</th>
<th class="cellrowborder" valign="top" width="12.121212121212121%" id="mcps1.2.6.1.5"><p id="en-us_topic_0220013660_p32111457141410"><a name="en-us_topic_0220013660_p32111457141410"></a><a name="en-us_topic_0220013660_p32111457141410"></a>Virtualization Type</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0220013660_row1421565771419"><td class="cellrowborder" rowspan="3" valign="top" width="23.232323232323235%" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0220013660_p9220165771411"><a name="en-us_topic_0220013660_p9220165771411"></a><a name="en-us_topic_0220013660_p9220165771411"></a>M3</p>
<p id="en-us_topic_0220013660_p372265701618"><a name="en-us_topic_0220013660_p372265701618"></a><a name="en-us_topic_0220013660_p372265701618"></a></p>
</td>
<td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0220013660_p1188644875918"><a name="en-us_topic_0220013660_p1188644875918"></a><a name="en-us_topic_0220013660_p1188644875918"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0220013660_p7887144855917"><a name="en-us_topic_0220013660_p7887144855917"></a><a name="en-us_topic_0220013660_p7887144855917"></a>64</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0220013660_p778717427593"><a name="en-us_topic_0220013660_p778717427593"></a><a name="en-us_topic_0220013660_p778717427593"></a>m3.2xlarge.8.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.6.1.5 "><p id="en-us_topic_0220013660_p122361457121416"><a name="en-us_topic_0220013660_p122361457121416"></a><a name="en-us_topic_0220013660_p122361457121416"></a>KVM</p>
</td>
</tr>
<tr id="en-us_topic_0220013660_row123712571147"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0220013660_p4887848165916"><a name="en-us_topic_0220013660_p4887848165916"></a><a name="en-us_topic_0220013660_p4887848165916"></a>16</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0220013660_p128871448195912"><a name="en-us_topic_0220013660_p128871448195912"></a><a name="en-us_topic_0220013660_p128871448195912"></a>128</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0220013660_p1788342145915"><a name="en-us_topic_0220013660_p1788342145915"></a><a name="en-us_topic_0220013660_p1788342145915"></a>m3.4xlarge.8.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0220013660_p225245791416"><a name="en-us_topic_0220013660_p225245791416"></a><a name="en-us_topic_0220013660_p225245791416"></a>KVM</p>
</td>
</tr>
<tr id="en-us_topic_0220013660_row7254105771412"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0220013660_p2887848175911"><a name="en-us_topic_0220013660_p2887848175911"></a><a name="en-us_topic_0220013660_p2887848175911"></a>32</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0220013660_p1887144835911"><a name="en-us_topic_0220013660_p1887144835911"></a><a name="en-us_topic_0220013660_p1887144835911"></a>256</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0220013660_p127881424594"><a name="en-us_topic_0220013660_p127881424594"></a><a name="en-us_topic_0220013660_p127881424594"></a>m3.8xlarge.8.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0220013660_p5269135719141"><a name="en-us_topic_0220013660_p5269135719141"></a><a name="en-us_topic_0220013660_p5269135719141"></a>KVM</p>
</td>
</tr>
</tbody>
</table>

**Table  9**  M4 ECS specifications

<a name="en-us_topic_0220013660_table1681161145018"></a>
<table><thead align="left"><tr id="en-us_topic_0220013660_row98212175019"><th class="cellrowborder" valign="top" width="23.232323232323235%" id="mcps1.2.6.1.1"><p id="en-us_topic_0220013660_p11821185019"><a name="en-us_topic_0220013660_p11821185019"></a><a name="en-us_topic_0220013660_p11821185019"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="23.232323232323235%" id="mcps1.2.6.1.2"><p id="en-us_topic_0220013660_p582111205020"><a name="en-us_topic_0220013660_p582111205020"></a><a name="en-us_topic_0220013660_p582111205020"></a>vCPUs</p>
</th>
<th class="cellrowborder" valign="top" width="19.191919191919194%" id="mcps1.2.6.1.3"><p id="en-us_topic_0220013660_p1482181195019"><a name="en-us_topic_0220013660_p1482181195019"></a><a name="en-us_topic_0220013660_p1482181195019"></a>Memory (GB)</p>
</th>
<th class="cellrowborder" valign="top" width="22.222222222222225%" id="mcps1.2.6.1.4"><p id="en-us_topic_0220013660_p0821918509"><a name="en-us_topic_0220013660_p0821918509"></a><a name="en-us_topic_0220013660_p0821918509"></a>Flavor</p>
</th>
<th class="cellrowborder" valign="top" width="12.121212121212121%" id="mcps1.2.6.1.5"><p id="en-us_topic_0220013660_p38261105010"><a name="en-us_topic_0220013660_p38261105010"></a><a name="en-us_topic_0220013660_p38261105010"></a>Virtualization Type</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0220013660_row982612508"><td class="cellrowborder" rowspan="4" valign="top" width="23.232323232323235%" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0220013660_p3824145017"><a name="en-us_topic_0220013660_p3824145017"></a><a name="en-us_topic_0220013660_p3824145017"></a>M4</p>
<p id="en-us_topic_0220013660_p188291185019"><a name="en-us_topic_0220013660_p188291185019"></a><a name="en-us_topic_0220013660_p188291185019"></a></p>
</td>
<td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0220013660_p98192212014"><a name="en-us_topic_0220013660_p98192212014"></a><a name="en-us_topic_0220013660_p98192212014"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0220013660_p7819112003"><a name="en-us_topic_0220013660_p7819112003"></a><a name="en-us_topic_0220013660_p7819112003"></a>64</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0220013660_p1774213571592"><a name="en-us_topic_0220013660_p1774213571592"></a><a name="en-us_topic_0220013660_p1774213571592"></a>m4.2xlarge.8.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.6.1.5 "><p id="en-us_topic_0220013660_p0834113509"><a name="en-us_topic_0220013660_p0834113509"></a><a name="en-us_topic_0220013660_p0834113509"></a>KVM</p>
</td>
</tr>
<tr id="en-us_topic_0220013660_row118341135018"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0220013660_p128191225014"><a name="en-us_topic_0220013660_p128191225014"></a><a name="en-us_topic_0220013660_p128191225014"></a>16</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0220013660_p281911220019"><a name="en-us_topic_0220013660_p281911220019"></a><a name="en-us_topic_0220013660_p281911220019"></a>128</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0220013660_p67421757115917"><a name="en-us_topic_0220013660_p67421757115917"></a><a name="en-us_topic_0220013660_p67421757115917"></a>m4.4xlarge.8.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0220013660_p14831116502"><a name="en-us_topic_0220013660_p14831116502"></a><a name="en-us_topic_0220013660_p14831116502"></a>KVM</p>
</td>
</tr>
<tr id="en-us_topic_0220013660_row19830119503"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0220013660_p108191217017"><a name="en-us_topic_0220013660_p108191217017"></a><a name="en-us_topic_0220013660_p108191217017"></a>32</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0220013660_p10819192208"><a name="en-us_topic_0220013660_p10819192208"></a><a name="en-us_topic_0220013660_p10819192208"></a>256</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0220013660_p27426571598"><a name="en-us_topic_0220013660_p27426571598"></a><a name="en-us_topic_0220013660_p27426571598"></a>m4.8xlarge.8.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0220013660_p1883813508"><a name="en-us_topic_0220013660_p1883813508"></a><a name="en-us_topic_0220013660_p1883813508"></a>KVM</p>
</td>
</tr>
<tr id="en-us_topic_0220013660_row08314175018"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0220013660_p9382111818013"><a name="en-us_topic_0220013660_p9382111818013"></a><a name="en-us_topic_0220013660_p9382111818013"></a>64</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0220013660_p33826181508"><a name="en-us_topic_0220013660_p33826181508"></a><a name="en-us_topic_0220013660_p33826181508"></a>512</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0220013660_p20798415155020"><a name="en-us_topic_0220013660_p20798415155020"></a><a name="en-us_topic_0220013660_p20798415155020"></a>m4.16xlarge.8.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0220013660_p78481135015"><a name="en-us_topic_0220013660_p78481135015"></a><a name="en-us_topic_0220013660_p78481135015"></a>KVM</p>
</td>
</tr>
</tbody>
</table>

