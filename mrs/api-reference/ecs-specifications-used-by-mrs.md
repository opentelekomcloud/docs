# ECS Specifications Used by MRS<a name="EN-US_TOPIC_0220013660"></a>

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

## ECS Flavor Naming Rules<a name="section741930611313"></a>

AB.C.D

Example: m3.8xlarge.8

In the preceding flavor:

-   **A**  specifies the ECS type. For example,  **s**  indicates a general-purpose ECS,  **c**  a computing ECS, and  **m**  a memory-optimized ECS.
-   **B**  specifies the type ID. For example, the  **1**  in  **s1**  indicates a general-purpose first-generation ECS, and the  **2**  in  **s2**  indicates a general-purpose second-generation ECS.
-   **C**  specifies a flavor size and can be any of the following options: medium, large, and xlarge.
-   **D**  specifies the ratio of memory to vCPUs expressed in a digit. For example, value  **4**  indicates that the ratio of memory to vCPUs is 4.

## Specifications<a name="section1399585312355"></a>

**Table  1**  S1 ECS specifications

<a name="table66778917103035"></a>
<table><thead align="left"><tr id="row21254511103035"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.6.1.1"><p id="p52972653162927"><a name="p52972653162927"></a><a name="p52972653162927"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="23%" id="mcps1.2.6.1.2"><p id="p62926494162927"><a name="p62926494162927"></a><a name="p62926494162927"></a>vCPUs</p>
</th>
<th class="cellrowborder" valign="top" width="21%" id="mcps1.2.6.1.3"><p id="p63881219162927"><a name="p63881219162927"></a><a name="p63881219162927"></a>Memory (GB)</p>
</th>
<th class="cellrowborder" valign="top" width="21%" id="mcps1.2.6.1.4"><p id="p6996228162927"><a name="p6996228162927"></a><a name="p6996228162927"></a>Flavor</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.6.1.5"><p id="p19167123116295"><a name="p19167123116295"></a><a name="p19167123116295"></a>Virtualization Type</p>
</th>
</tr>
</thead>
<tbody><tr id="row8532241591"><td class="cellrowborder" rowspan="3" valign="top" width="23%" headers="mcps1.2.6.1.1 "><p id="p3534747915"><a name="p3534747915"></a><a name="p3534747915"></a>S1</p>
<p id="p15824165112920"><a name="p15824165112920"></a><a name="p15824165112920"></a></p>
<p id="p114844523910"><a name="p114844523910"></a><a name="p114844523910"></a></p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.2 "><p id="p2302959557"><a name="p2302959557"></a><a name="p2302959557"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.6.1.3 "><p id="p33037525517"><a name="p33037525517"></a><a name="p33037525517"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.6.1.4 "><p id="p1595765119474"><a name="p1595765119474"></a><a name="p1595765119474"></a>s1.xlarge.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.6.1.5 "><p id="p612815911919"><a name="p612815911919"></a><a name="p612815911919"></a>XEN</p>
</td>
</tr>
<tr id="row98249514915"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p8666211135514"><a name="p8666211135514"></a><a name="p8666211135514"></a>16</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p566681116551"><a name="p566681116551"></a><a name="p566681116551"></a>64</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p1931920523532"><a name="p1931920523532"></a><a name="p1931920523532"></a>s1.4xlarge.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p17814459790"><a name="p17814459790"></a><a name="p17814459790"></a>XEN</p>
</td>
</tr>
<tr id="row34841252894"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p566617118550"><a name="p566617118550"></a><a name="p566617118550"></a>32</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p15666511115520"><a name="p15666511115520"></a><a name="p15666511115520"></a>128</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p1831916526534"><a name="p1831916526534"></a><a name="p1831916526534"></a>s1.8xlarge.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p1950414018107"><a name="p1950414018107"></a><a name="p1950414018107"></a>XEN</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  C2 ECS specifications

<a name="table367241161115"></a>
<table><thead align="left"><tr id="row118484141119"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.6.1.1"><p id="p1392144120110"><a name="p1392144120110"></a><a name="p1392144120110"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="23%" id="mcps1.2.6.1.2"><p id="p1296184111116"><a name="p1296184111116"></a><a name="p1296184111116"></a>vCPUs</p>
</th>
<th class="cellrowborder" valign="top" width="21%" id="mcps1.2.6.1.3"><p id="p149884171118"><a name="p149884171118"></a><a name="p149884171118"></a>Memory (GB)</p>
</th>
<th class="cellrowborder" valign="top" width="21%" id="mcps1.2.6.1.4"><p id="p10102241121115"><a name="p10102241121115"></a><a name="p10102241121115"></a>Flavor</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.6.1.5"><p id="p8104154117112"><a name="p8104154117112"></a><a name="p8104154117112"></a>Virtualization Type</p>
</th>
</tr>
</thead>
<tbody><tr id="row6824183441213"><td class="cellrowborder" rowspan="2" valign="top" width="23%" headers="mcps1.2.6.1.1 "><p id="p13262641141118"><a name="p13262641141118"></a><a name="p13262641141118"></a>C2</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.2 "><p id="p351101995520"><a name="p351101995520"></a><a name="p351101995520"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.6.1.3 "><p id="p115191910553"><a name="p115191910553"></a><a name="p115191910553"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.6.1.4 "><p id="p13515267546"><a name="p13515267546"></a><a name="p13515267546"></a>c2.2xlarge.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.6.1.5 "><p id="p138255348122"><a name="p138255348122"></a><a name="p138255348122"></a>KVM</p>
</td>
</tr>
<tr id="row1526034121120"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p18511119165514"><a name="p18511119165514"></a><a name="p18511119165514"></a>16</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p11511419175515"><a name="p11511419175515"></a><a name="p11511419175515"></a>32</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p19515176135414"><a name="p19515176135414"></a><a name="p19515176135414"></a>c2.4xlarge.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p82781241141113"><a name="p82781241141113"></a><a name="p82781241141113"></a>KVM</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  General computing-plus \(C3\) ECS specifications

<a name="table3949605220464"></a>
<table><thead align="left"><tr id="row5755737620464"><th class="cellrowborder" valign="top" width="23.232323232323235%" id="mcps1.2.6.1.1"><p id="p32920979204624"><a name="p32920979204624"></a><a name="p32920979204624"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="23.232323232323235%" id="mcps1.2.6.1.2"><p id="p41529665204624"><a name="p41529665204624"></a><a name="p41529665204624"></a>vCPUs</p>
</th>
<th class="cellrowborder" valign="top" width="19.191919191919194%" id="mcps1.2.6.1.3"><p id="p9028760204624"><a name="p9028760204624"></a><a name="p9028760204624"></a>Memory (GB)</p>
</th>
<th class="cellrowborder" valign="top" width="22.222222222222225%" id="mcps1.2.6.1.4"><p id="p5297585204624"><a name="p5297585204624"></a><a name="p5297585204624"></a>Flavor</p>
</th>
<th class="cellrowborder" valign="top" width="12.121212121212121%" id="mcps1.2.6.1.5"><p id="p84201252123120"><a name="p84201252123120"></a><a name="p84201252123120"></a>Virtualization Type</p>
</th>
</tr>
</thead>
<tbody><tr id="row2115659920464"><td class="cellrowborder" rowspan="7" valign="top" width="23.232323232323235%" headers="mcps1.2.6.1.1 "><p id="p1639654719185"><a name="p1639654719185"></a><a name="p1639654719185"></a>C3</p>
</td>
<td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.6.1.2 "><p id="p1478753518587"><a name="p1478753518587"></a><a name="p1478753518587"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.6.1.3 "><p id="p57871235145814"><a name="p57871235145814"></a><a name="p57871235145814"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.6.1.4 "><p id="p1983291835812"><a name="p1983291835812"></a><a name="p1983291835812"></a>c3.2xlarge.2.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.6.1.5 "><p id="p714614176327"><a name="p714614176327"></a><a name="p714614176327"></a>KVM</p>
</td>
</tr>
<tr id="row1339712614367"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p1478793525820"><a name="p1478793525820"></a><a name="p1478793525820"></a>4</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p778723555817"><a name="p778723555817"></a><a name="p778723555817"></a>16</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p58321185585"><a name="p58321185585"></a><a name="p58321185585"></a>c3.xlarge.4.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p9361114613616"><a name="p9361114613616"></a><a name="p9361114613616"></a>KVM</p>
</td>
</tr>
<tr id="row58396907204611"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p1778713512588"><a name="p1778713512588"></a><a name="p1778713512588"></a>8</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p27873357588"><a name="p27873357588"></a><a name="p27873357588"></a>32</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p683231814581"><a name="p683231814581"></a><a name="p683231814581"></a>c3.2xlarge.4.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p1160181710322"><a name="p1160181710322"></a><a name="p1160181710322"></a>KVM</p>
</td>
</tr>
<tr id="row19288388204611"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p10787235105818"><a name="p10787235105818"></a><a name="p10787235105818"></a>16</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p378719357584"><a name="p378719357584"></a><a name="p378719357584"></a>32</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p1483221817585"><a name="p1483221817585"></a><a name="p1483221817585"></a>c3.4xlarge.2.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p11163171763213"><a name="p11163171763213"></a><a name="p11163171763213"></a>KVM</p>
</td>
</tr>
<tr id="row39706029204611"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p19787133585814"><a name="p19787133585814"></a><a name="p19787133585814"></a>16</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p6787173545812"><a name="p6787173545812"></a><a name="p6787173545812"></a>64</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p1883219185581"><a name="p1883219185581"></a><a name="p1883219185581"></a>c3.4xlarge.4.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p14657219153217"><a name="p14657219153217"></a><a name="p14657219153217"></a>KVM</p>
</td>
</tr>
<tr id="row4280432102715"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p634214211587"><a name="p634214211587"></a><a name="p634214211587"></a>32</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p63421642145814"><a name="p63421642145814"></a><a name="p63421642145814"></a>128</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p1537512712586"><a name="p1537512712586"></a><a name="p1537512712586"></a>c3.8xlarge.4.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p14281153262720"><a name="p14281153262720"></a><a name="p14281153262720"></a>KVM</p>
</td>
</tr>
<tr id="row28491536204611"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p113421742175817"><a name="p113421742175817"></a><a name="p113421742175817"></a>60</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p1734374235817"><a name="p1734374235817"></a><a name="p1734374235817"></a>256</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p113751827145816"><a name="p113751827145816"></a><a name="p113751827145816"></a>c3.15xlarge.4.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p16664419133218"><a name="p16664419133218"></a><a name="p16664419133218"></a>KVM</p>
</td>
</tr>
</tbody>
</table>

**Table  4**  C4 ECS specifications

<a name="table823966144719"></a>
<table><thead align="left"><tr id="row1825415614476"><th class="cellrowborder" valign="top" width="23.232323232323235%" id="mcps1.2.6.1.1"><p id="p42622610479"><a name="p42622610479"></a><a name="p42622610479"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="23.232323232323235%" id="mcps1.2.6.1.2"><p id="p1926526104711"><a name="p1926526104711"></a><a name="p1926526104711"></a>vCPUs</p>
</th>
<th class="cellrowborder" valign="top" width="19.191919191919194%" id="mcps1.2.6.1.3"><p id="p17269146104710"><a name="p17269146104710"></a><a name="p17269146104710"></a>Memory (GB)</p>
</th>
<th class="cellrowborder" valign="top" width="22.222222222222225%" id="mcps1.2.6.1.4"><p id="p1527246134711"><a name="p1527246134711"></a><a name="p1527246134711"></a>Flavor</p>
</th>
<th class="cellrowborder" valign="top" width="12.121212121212121%" id="mcps1.2.6.1.5"><p id="p92745613476"><a name="p92745613476"></a><a name="p92745613476"></a>Virtualization Type</p>
</th>
</tr>
</thead>
<tbody><tr id="row102796664710"><td class="cellrowborder" rowspan="8" valign="top" width="23.232323232323235%" headers="mcps1.2.6.1.1 "><p id="p5281967474"><a name="p5281967474"></a><a name="p5281967474"></a>C4</p>
<p id="p18879453579"><a name="p18879453579"></a><a name="p18879453579"></a></p>
<p id="p96176451570"><a name="p96176451570"></a><a name="p96176451570"></a></p>
<p id="p101149468578"><a name="p101149468578"></a><a name="p101149468578"></a></p>
<p id="p1617646195717"><a name="p1617646195717"></a><a name="p1617646195717"></a></p>
<p id="p14152247145713"><a name="p14152247145713"></a><a name="p14152247145713"></a></p>
</td>
<td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.6.1.2 "><p id="p17748145920017"><a name="p17748145920017"></a><a name="p17748145920017"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.6.1.3 "><p id="p19748155917018"><a name="p19748155917018"></a><a name="p19748155917018"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.6.1.4 "><p id="p14844152503"><a name="p14844152503"></a><a name="p14844152503"></a>c4.xlarge.4.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.6.1.5 "><p id="p829217654716"><a name="p829217654716"></a><a name="p829217654716"></a>KVM</p>
</td>
</tr>
<tr id="row14295146164711"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p974855914017"><a name="p974855914017"></a><a name="p974855914017"></a>8</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p13748185914017"><a name="p13748185914017"></a><a name="p13748185914017"></a>16</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p6844152201"><a name="p6844152201"></a><a name="p6844152201"></a>c4.2xlarge.2.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p8310136154720"><a name="p8310136154720"></a><a name="p8310136154720"></a>KVM</p>
</td>
</tr>
<tr id="row183421766474"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p127489592011"><a name="p127489592011"></a><a name="p127489592011"></a>8</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p1474815916012"><a name="p1474815916012"></a><a name="p1474815916012"></a>32</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p18844152804"><a name="p18844152804"></a><a name="p18844152804"></a>c4.2xlarge.4.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p635556134711"><a name="p635556134711"></a><a name="p635556134711"></a>KVM</p>
</td>
</tr>
<tr id="row98744511577"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p127480599014"><a name="p127480599014"></a><a name="p127480599014"></a>16</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p197486591202"><a name="p197486591202"></a><a name="p197486591202"></a>32</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p178445521209"><a name="p178445521209"></a><a name="p178445521209"></a>c4.4xlarge.2.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p1987145165717"><a name="p1987145165717"></a><a name="p1987145165717"></a>KVM</p>
</td>
</tr>
<tr id="row15617134555715"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p274810598010"><a name="p274810598010"></a><a name="p274810598010"></a>16</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p197481359307"><a name="p197481359307"></a><a name="p197481359307"></a>64</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p17844352104"><a name="p17844352104"></a><a name="p17844352104"></a>c4.4xlarge.4.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p161715457573"><a name="p161715457573"></a><a name="p161715457573"></a>KVM</p>
</td>
</tr>
<tr id="row1411413460575"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p2074885914010"><a name="p2074885914010"></a><a name="p2074885914010"></a>32</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p1574919591309"><a name="p1574919591309"></a><a name="p1574919591309"></a>64</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p178444521109"><a name="p178444521109"></a><a name="p178444521109"></a>c4.8xlarge.2.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p711494617574"><a name="p711494617574"></a><a name="p711494617574"></a>KVM</p>
</td>
</tr>
<tr id="row161711466576"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p0749159101"><a name="p0749159101"></a><a name="p0749159101"></a>32</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p47497599014"><a name="p47497599014"></a><a name="p47497599014"></a>128</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p98441652206"><a name="p98441652206"></a><a name="p98441652206"></a>c4.8xlarge.4.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p9617346195710"><a name="p9617346195710"></a><a name="p9617346195710"></a>KVM</p>
</td>
</tr>
<tr id="row8152114795716"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p107492591704"><a name="p107492591704"></a><a name="p107492591704"></a>64</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p117495599017"><a name="p117495599017"></a><a name="p117495599017"></a>256</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p1584475215018"><a name="p1584475215018"></a><a name="p1584475215018"></a>c4.16xlarge.4.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p1415274705715"><a name="p1415274705715"></a><a name="p1415274705715"></a>KVM</p>
</td>
</tr>
</tbody>
</table>

**Table  5**  D1 ECS specifications

<a name="table47541937112515"></a>
<table><thead align="left"><tr id="row1775413371257"><th class="cellrowborder" valign="top" width="13%" id="mcps1.2.8.1.1"><p id="p17228105016252"><a name="p17228105016252"></a><a name="p17228105016252"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="8%" id="mcps1.2.8.1.2"><p id="p123165013254"><a name="p123165013254"></a><a name="p123165013254"></a>vCPUs</p>
</th>
<th class="cellrowborder" valign="top" width="11%" id="mcps1.2.8.1.3"><p id="p7236185013252"><a name="p7236185013252"></a><a name="p7236185013252"></a>Memory (GB)</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.8.1.4"><p id="p18237155062514"><a name="p18237155062514"></a><a name="p18237155062514"></a>Flavor</p>
</th>
<th class="cellrowborder" valign="top" width="11%" id="mcps1.2.8.1.5"><p id="p724035017257"><a name="p724035017257"></a><a name="p724035017257"></a>Virtualization Type</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.8.1.6"><p id="p1624105092519"><a name="p1624105092519"></a><a name="p1624105092519"></a>Local Disk (GB)</p>
</th>
<th class="cellrowborder" valign="top" width="28.999999999999996%" id="mcps1.2.8.1.7"><p id="p9205101061511"><a name="p9205101061511"></a><a name="p9205101061511"></a>Hardware</p>
</th>
</tr>
</thead>
<tbody><tr id="row974834394812"><td class="cellrowborder" rowspan="4" valign="top" width="13%" headers="mcps1.2.8.1.1 "><p id="p9760548192919"><a name="p9760548192919"></a><a name="p9760548192919"></a>D1</p>
<p id="p18258142365410"><a name="p18258142365410"></a><a name="p18258142365410"></a></p>
</td>
<td class="cellrowborder" valign="top" width="8%" headers="mcps1.2.8.1.2 "><p id="p787054695413"><a name="p787054695413"></a><a name="p787054695413"></a>44</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.8.1.3 "><p id="p128705468546"><a name="p128705468546"></a><a name="p128705468546"></a>3232</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.8.1.4 "><p id="p164813321546"><a name="p164813321546"></a><a name="p164813321546"></a>d1.xlarge.mrslinux.mrs</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.8.1.5 "><p id="p1875013430483"><a name="p1875013430483"></a><a name="p1875013430483"></a>KVM</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.8.1.6 "><p id="p17750443104811"><a name="p17750443104811"></a><a name="p17750443104811"></a>3×1800</p>
</td>
<td class="cellrowborder" rowspan="4" valign="top" width="28.999999999999996%" headers="mcps1.2.8.1.7 "><p id="p449920318167"><a name="p449920318167"></a><a name="p449920318167"></a>CPU: Intel&reg; Xeon&reg; Gold 6151 Processor v5</p>
<p id="p676115981618"><a name="p676115981618"></a><a name="p676115981618"></a>Memory: 20 × 32 GB</p>
<p id="p1525820237549"><a name="p1525820237549"></a><a name="p1525820237549"></a></p>
</td>
</tr>
<tr id="row14967171717297"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p887044665417"><a name="p887044665417"></a><a name="p887044665417"></a>88</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p1287004610547"><a name="p1287004610547"></a><a name="p1287004610547"></a>6464</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p7648832155416"><a name="p7648832155416"></a><a name="p7648832155416"></a>d1.2xlarge.mrslinux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p10967117172915"><a name="p10967117172915"></a><a name="p10967117172915"></a>KVM</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p169678175293"><a name="p169678175293"></a><a name="p169678175293"></a>6×1800</p>
</td>
</tr>
<tr id="row575615372253"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p158705469542"><a name="p158705469542"></a><a name="p158705469542"></a>16</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p6870246145413"><a name="p6870246145413"></a><a name="p6870246145413"></a>128</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p1964873265412"><a name="p1964873265412"></a><a name="p1964873265412"></a>d1.4xlarge.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p10756133715250"><a name="p10756133715250"></a><a name="p10756133715250"></a>KVM</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p1675663717258"><a name="p1675663717258"></a><a name="p1675663717258"></a>12×1800</p>
</td>
</tr>
<tr id="row18257162325419"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p148701462540"><a name="p148701462540"></a><a name="p148701462540"></a>36</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p9870164610544"><a name="p9870164610544"></a><a name="p9870164610544"></a>256</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p11648183218542"><a name="p11648183218542"></a><a name="p11648183218542"></a>d1.8xlarge.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p1225810232540"><a name="p1225810232540"></a><a name="p1225810232540"></a>KVM</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p1925812235542"><a name="p1925812235542"></a><a name="p1925812235542"></a>24×1800</p>
</td>
</tr>
</tbody>
</table>

**Table  6**  D2 ECS specifications

<a name="table1215815565720"></a>
<table><thead align="left"><tr id="row419985115711"><th class="cellrowborder" valign="top" width="13%" id="mcps1.2.8.1.1"><p id="p8205115155714"><a name="p8205115155714"></a><a name="p8205115155714"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="8%" id="mcps1.2.8.1.2"><p id="p1521311515579"><a name="p1521311515579"></a><a name="p1521311515579"></a>vCPUs</p>
</th>
<th class="cellrowborder" valign="top" width="11%" id="mcps1.2.8.1.3"><p id="p19218155577"><a name="p19218155577"></a><a name="p19218155577"></a>Memory (GB)</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.8.1.4"><p id="p172241559574"><a name="p172241559574"></a><a name="p172241559574"></a>Flavor</p>
</th>
<th class="cellrowborder" valign="top" width="11%" id="mcps1.2.8.1.5"><p id="p182291595720"><a name="p182291595720"></a><a name="p182291595720"></a>Virtualization Type</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.8.1.6"><p id="p82336514571"><a name="p82336514571"></a><a name="p82336514571"></a>Local Disk (GB)</p>
</th>
<th class="cellrowborder" valign="top" width="28.999999999999996%" id="mcps1.2.8.1.7"><p id="p18238856576"><a name="p18238856576"></a><a name="p18238856576"></a>Hardware</p>
</th>
</tr>
</thead>
<tbody><tr id="row82414510575"><td class="cellrowborder" rowspan="4" valign="top" width="13%" headers="mcps1.2.8.1.1 "><p id="p18247155135712"><a name="p18247155135712"></a><a name="p18247155135712"></a>D2</p>
<p id="p791575319569"><a name="p791575319569"></a><a name="p791575319569"></a></p>
<p id="p541755414562"><a name="p541755414562"></a><a name="p541755414562"></a></p>
</td>
<td class="cellrowborder" valign="top" width="8%" headers="mcps1.2.8.1.2 "><p id="p112011279592"><a name="p112011279592"></a><a name="p112011279592"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.8.1.3 "><p id="p420827105920"><a name="p420827105920"></a><a name="p420827105920"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.8.1.4 "><p id="p16113117125917"><a name="p16113117125917"></a><a name="p16113117125917"></a>d2.xlarge.8.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.8.1.5 "><p id="p9268651572"><a name="p9268651572"></a><a name="p9268651572"></a>KVM</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.8.1.6 "><p id="p9271195185720"><a name="p9271195185720"></a><a name="p9271195185720"></a>2×1800</p>
</td>
<td class="cellrowborder" rowspan="4" valign="top" width="28.999999999999996%" headers="mcps1.2.8.1.7 "><p id="p1627812515571"><a name="p1627812515571"></a><a name="p1627812515571"></a>CPU: Intel&reg; Xeon&reg; Gold 6151 Processor v5</p>
<p id="p16281155145713"><a name="p16281155145713"></a><a name="p16281155145713"></a>Memory: 20 × 32 GB</p>
<p id="p29161553205613"><a name="p29161553205613"></a><a name="p29161553205613"></a></p>
<p id="p1841765414561"><a name="p1841765414561"></a><a name="p1841765414561"></a></p>
</td>
</tr>
<tr id="row112846595717"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p182114279598"><a name="p182114279598"></a><a name="p182114279598"></a>8</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p3254270595"><a name="p3254270595"></a><a name="p3254270595"></a>64</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p411381785915"><a name="p411381785915"></a><a name="p411381785915"></a>d2.2xlarge.8.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p231015512573"><a name="p231015512573"></a><a name="p231015512573"></a>KVM</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p83154510577"><a name="p83154510577"></a><a name="p83154510577"></a>4×1800</p>
</td>
</tr>
<tr id="row18915195325616"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p152572745914"><a name="p152572745914"></a><a name="p152572745914"></a>16</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p5251227115917"><a name="p5251227115917"></a><a name="p5251227115917"></a>128</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p19113417135916"><a name="p19113417135916"></a><a name="p19113417135916"></a>d2.4xlarge.8.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p3915953135618"><a name="p3915953135618"></a><a name="p3915953135618"></a>KVM</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p179153532567"><a name="p179153532567"></a><a name="p179153532567"></a>8×1800</p>
</td>
</tr>
<tr id="row74171254145617"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p1525142710597"><a name="p1525142710597"></a><a name="p1525142710597"></a>32</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p8253277598"><a name="p8253277598"></a><a name="p8253277598"></a>256</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p911391712598"><a name="p911391712598"></a><a name="p911391712598"></a>d2.8xlarge.8.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p17417554145618"><a name="p17417554145618"></a><a name="p17417554145618"></a>KVM</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p6417175417566"><a name="p6417175417566"></a><a name="p6417175417566"></a>16×1800</p>
</td>
</tr>
</tbody>
</table>

**Table  7**  H1 ECS specifications

<a name="table0407254151418"></a>
<table><thead align="left"><tr id="row1443016544141"><th class="cellrowborder" valign="top" width="23.232323232323235%" id="mcps1.2.6.1.1"><p id="p74386548148"><a name="p74386548148"></a><a name="p74386548148"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="23.232323232323235%" id="mcps1.2.6.1.2"><p id="p14441195451411"><a name="p14441195451411"></a><a name="p14441195451411"></a>vCPUs</p>
</th>
<th class="cellrowborder" valign="top" width="19.191919191919194%" id="mcps1.2.6.1.3"><p id="p14446185417144"><a name="p14446185417144"></a><a name="p14446185417144"></a>Memory (GB)</p>
</th>
<th class="cellrowborder" valign="top" width="22.222222222222225%" id="mcps1.2.6.1.4"><p id="p9451145415145"><a name="p9451145415145"></a><a name="p9451145415145"></a>Flavor</p>
</th>
<th class="cellrowborder" valign="top" width="12.121212121212121%" id="mcps1.2.6.1.5"><p id="p245645461416"><a name="p245645461416"></a><a name="p245645461416"></a>Virtualization Type</p>
</th>
</tr>
</thead>
<tbody><tr id="row19460105414141"><td class="cellrowborder" rowspan="3" valign="top" width="23.232323232323235%" headers="mcps1.2.6.1.1 "><p id="p6465154111411"><a name="p6465154111411"></a><a name="p6465154111411"></a>H1</p>
</td>
<td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.6.1.2 "><p id="p1695312357558"><a name="p1695312357558"></a><a name="p1695312357558"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.6.1.3 "><p id="p7953193517557"><a name="p7953193517557"></a><a name="p7953193517557"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.6.1.4 "><p id="p6747153025518"><a name="p6747153025518"></a><a name="p6747153025518"></a>h1.2xlarge.4.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.6.1.5 "><p id="p164811954111418"><a name="p164811954111418"></a><a name="p164811954111418"></a>KVM</p>
</td>
</tr>
<tr id="row11482145411412"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p10953103545519"><a name="p10953103545519"></a><a name="p10953103545519"></a>16</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p19953235115517"><a name="p19953235115517"></a><a name="p19953235115517"></a>64</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p15747113065511"><a name="p15747113065511"></a><a name="p15747113065511"></a>h1.4xlarge.4.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p5497135420141"><a name="p5497135420141"></a><a name="p5497135420141"></a>KVM</p>
</td>
</tr>
<tr id="row150045421411"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p20953135115519"><a name="p20953135115519"></a><a name="p20953135115519"></a>32</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p295393585512"><a name="p295393585512"></a><a name="p295393585512"></a>128</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p774714308553"><a name="p774714308553"></a><a name="p774714308553"></a>h1.8xlarge.4.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p052175411143"><a name="p052175411143"></a><a name="p052175411143"></a>KVM</p>
</td>
</tr>
</tbody>
</table>

**Table  8**  M3 ECS specifications

<a name="table11173155712141"></a>
<table><thead align="left"><tr id="row11191105718140"><th class="cellrowborder" valign="top" width="23.232323232323235%" id="mcps1.2.6.1.1"><p id="p17196457201410"><a name="p17196457201410"></a><a name="p17196457201410"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="23.232323232323235%" id="mcps1.2.6.1.2"><p id="p20199175711411"><a name="p20199175711411"></a><a name="p20199175711411"></a>vCPUs</p>
</th>
<th class="cellrowborder" valign="top" width="19.191919191919194%" id="mcps1.2.6.1.3"><p id="p720319574148"><a name="p720319574148"></a><a name="p720319574148"></a>Memory (GB)</p>
</th>
<th class="cellrowborder" valign="top" width="22.222222222222225%" id="mcps1.2.6.1.4"><p id="p7208185781418"><a name="p7208185781418"></a><a name="p7208185781418"></a>Flavor</p>
</th>
<th class="cellrowborder" valign="top" width="12.121212121212121%" id="mcps1.2.6.1.5"><p id="p32111457141410"><a name="p32111457141410"></a><a name="p32111457141410"></a>Virtualization Type</p>
</th>
</tr>
</thead>
<tbody><tr id="row1421565771419"><td class="cellrowborder" rowspan="3" valign="top" width="23.232323232323235%" headers="mcps1.2.6.1.1 "><p id="p9220165771411"><a name="p9220165771411"></a><a name="p9220165771411"></a>M3</p>
<p id="p372265701618"><a name="p372265701618"></a><a name="p372265701618"></a></p>
</td>
<td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.6.1.2 "><p id="p1188644875918"><a name="p1188644875918"></a><a name="p1188644875918"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.6.1.3 "><p id="p7887144855917"><a name="p7887144855917"></a><a name="p7887144855917"></a>64</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.6.1.4 "><p id="p778717427593"><a name="p778717427593"></a><a name="p778717427593"></a>m3.2xlarge.8.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.6.1.5 "><p id="p122361457121416"><a name="p122361457121416"></a><a name="p122361457121416"></a>KVM</p>
</td>
</tr>
<tr id="row123712571147"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p4887848165916"><a name="p4887848165916"></a><a name="p4887848165916"></a>16</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p128871448195912"><a name="p128871448195912"></a><a name="p128871448195912"></a>128</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p1788342145915"><a name="p1788342145915"></a><a name="p1788342145915"></a>m3.4xlarge.8.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p225245791416"><a name="p225245791416"></a><a name="p225245791416"></a>KVM</p>
</td>
</tr>
<tr id="row7254105771412"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p2887848175911"><a name="p2887848175911"></a><a name="p2887848175911"></a>32</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p1887144835911"><a name="p1887144835911"></a><a name="p1887144835911"></a>256</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p127881424594"><a name="p127881424594"></a><a name="p127881424594"></a>m3.8xlarge.8.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p5269135719141"><a name="p5269135719141"></a><a name="p5269135719141"></a>KVM</p>
</td>
</tr>
</tbody>
</table>

**Table  9**  M4 ECS specifications

<a name="table1681161145018"></a>
<table><thead align="left"><tr id="row98212175019"><th class="cellrowborder" valign="top" width="23.232323232323235%" id="mcps1.2.6.1.1"><p id="p11821185019"><a name="p11821185019"></a><a name="p11821185019"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="23.232323232323235%" id="mcps1.2.6.1.2"><p id="p582111205020"><a name="p582111205020"></a><a name="p582111205020"></a>vCPUs</p>
</th>
<th class="cellrowborder" valign="top" width="19.191919191919194%" id="mcps1.2.6.1.3"><p id="p1482181195019"><a name="p1482181195019"></a><a name="p1482181195019"></a>Memory (GB)</p>
</th>
<th class="cellrowborder" valign="top" width="22.222222222222225%" id="mcps1.2.6.1.4"><p id="p0821918509"><a name="p0821918509"></a><a name="p0821918509"></a>Flavor</p>
</th>
<th class="cellrowborder" valign="top" width="12.121212121212121%" id="mcps1.2.6.1.5"><p id="p38261105010"><a name="p38261105010"></a><a name="p38261105010"></a>Virtualization Type</p>
</th>
</tr>
</thead>
<tbody><tr id="row982612508"><td class="cellrowborder" rowspan="4" valign="top" width="23.232323232323235%" headers="mcps1.2.6.1.1 "><p id="p3824145017"><a name="p3824145017"></a><a name="p3824145017"></a>M4</p>
<p id="p188291185019"><a name="p188291185019"></a><a name="p188291185019"></a></p>
</td>
<td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.6.1.2 "><p id="p98192212014"><a name="p98192212014"></a><a name="p98192212014"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.6.1.3 "><p id="p7819112003"><a name="p7819112003"></a><a name="p7819112003"></a>64</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.6.1.4 "><p id="p1774213571592"><a name="p1774213571592"></a><a name="p1774213571592"></a>m4.2xlarge.8.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.6.1.5 "><p id="p0834113509"><a name="p0834113509"></a><a name="p0834113509"></a>KVM</p>
</td>
</tr>
<tr id="row118341135018"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p128191225014"><a name="p128191225014"></a><a name="p128191225014"></a>16</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p281911220019"><a name="p281911220019"></a><a name="p281911220019"></a>128</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p67421757115917"><a name="p67421757115917"></a><a name="p67421757115917"></a>m4.4xlarge.8.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p14831116502"><a name="p14831116502"></a><a name="p14831116502"></a>KVM</p>
</td>
</tr>
<tr id="row19830119503"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p108191217017"><a name="p108191217017"></a><a name="p108191217017"></a>32</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p10819192208"><a name="p10819192208"></a><a name="p10819192208"></a>256</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p27426571598"><a name="p27426571598"></a><a name="p27426571598"></a>m4.8xlarge.8.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p1883813508"><a name="p1883813508"></a><a name="p1883813508"></a>KVM</p>
</td>
</tr>
<tr id="row08314175018"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p9382111818013"><a name="p9382111818013"></a><a name="p9382111818013"></a>64</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p33826181508"><a name="p33826181508"></a><a name="p33826181508"></a>512</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p20798415155020"><a name="p20798415155020"></a><a name="p20798415155020"></a>m4.16xlarge.8.linux.mrs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p78481135015"><a name="p78481135015"></a><a name="p78481135015"></a>KVM</p>
</td>
</tr>
</tbody>
</table>

