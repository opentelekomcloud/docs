# General-Purpose ECSs<a name="EN-US_TOPIC_0035470101"></a>

## Overview<a name="section21906772103453"></a>

General-purpose ECSs provide a balance of computing, memory, and network resources and a baseline level of CPU performance with the ability to burst above the baseline. These ECSs are suitable for many applications, such as web servers, enterprise R&D, and small-scale databases.

S2 ECSs use Intel® Xeon® Scalable processors, which significantly improve the comprehensive performance. They provide a balance of computing, memory, and network resources and a baseline level of CPU performance with the ability to burst above the baseline. These ECSs are suitable for many applications.

## Specifications<a name="section26311304103459"></a>

**Table  1**  S2 ECS specifications

<a name="table477598401959"></a>
<table><thead align="left"><tr id="row11866311959"><th class="cellrowborder" valign="top" width="16.16161616161616%" id="mcps1.2.8.1.1"><p id="p115939515532"><a name="p115939515532"></a><a name="p115939515532"></a>Flavor</p>
</th>
<th class="cellrowborder" valign="top" width="12.12121212121212%" id="mcps1.2.8.1.2"><p id="p3699556719753"><a name="p3699556719753"></a><a name="p3699556719753"></a>vCPUs</p>
</th>
<th class="cellrowborder" valign="top" width="15.151515151515149%" id="mcps1.2.8.1.3"><p id="p4385097319753"><a name="p4385097319753"></a><a name="p4385097319753"></a>Memory (GB)</p>
</th>
<th class="cellrowborder" valign="top" width="19.19191919191919%" id="mcps1.2.8.1.4"><p id="p107291434184215"><a name="p107291434184215"></a><a name="p107291434184215"></a>Maximum/Assured Bandwidth (Gbit/s)</p>
</th>
<th class="cellrowborder" valign="top" width="14.14141414141414%" id="mcps1.2.8.1.5"><p id="p1972918347421"><a name="p1972918347421"></a><a name="p1972918347421"></a>Maximum PPS (10,000)</p>
</th>
<th class="cellrowborder" valign="top" width="10.1010101010101%" id="mcps1.2.8.1.6"><p id="p117291134104211"><a name="p117291134104211"></a><a name="p117291134104211"></a>NIC Multi-Queue</p>
</th>
<th class="cellrowborder" valign="top" width="13.13131313131313%" id="mcps1.2.8.1.7"><p id="p10826634191219"><a name="p10826634191219"></a><a name="p10826634191219"></a>Virtualization Type</p>
</th>
</tr>
</thead>
<tbody><tr id="row388151959"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.2.8.1.1 "><p id="p1559314516533"><a name="p1559314516533"></a><a name="p1559314516533"></a>s2.medium.1</p>
</td>
<td class="cellrowborder" valign="top" width="12.12121212121212%" headers="mcps1.2.8.1.2 "><p id="p533387381959"><a name="p533387381959"></a><a name="p533387381959"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515149%" headers="mcps1.2.8.1.3 "><p id="p254705081959"><a name="p254705081959"></a><a name="p254705081959"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.8.1.4 "><p id="p84651721124216"><a name="p84651721124216"></a><a name="p84651721124216"></a>0.5/0.1</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.8.1.5 "><p id="p9891182811424"><a name="p9891182811424"></a><a name="p9891182811424"></a>5</p>
</td>
<td class="cellrowborder" valign="top" width="10.1010101010101%" headers="mcps1.2.8.1.6 "><p id="p1090163264219"><a name="p1090163264219"></a><a name="p1090163264219"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.2.8.1.7 "><p id="p13827734111210"><a name="p13827734111210"></a><a name="p13827734111210"></a>KVM</p>
</td>
</tr>
<tr id="row459544041959"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.2.8.1.1 "><p id="p8593159537"><a name="p8593159537"></a><a name="p8593159537"></a>s2.large.1</p>
</td>
<td class="cellrowborder" valign="top" width="12.12121212121212%" headers="mcps1.2.8.1.2 "><p id="p538326941959"><a name="p538326941959"></a><a name="p538326941959"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515149%" headers="mcps1.2.8.1.3 "><p id="p654809661959"><a name="p654809661959"></a><a name="p654809661959"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.8.1.4 "><p id="p16373935018"><a name="p16373935018"></a><a name="p16373935018"></a>0.8/0.2</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.8.1.5 "><p id="p168174212496"><a name="p168174212496"></a><a name="p168174212496"></a>10</p>
</td>
<td class="cellrowborder" valign="top" width="10.1010101010101%" headers="mcps1.2.8.1.6 "><p id="p17452113214493"><a name="p17452113214493"></a><a name="p17452113214493"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.2.8.1.7 "><p id="p208275345125"><a name="p208275345125"></a><a name="p208275345125"></a>KVM</p>
</td>
</tr>
<tr id="row212220931959"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.2.8.1.1 "><p id="p1059310515531"><a name="p1059310515531"></a><a name="p1059310515531"></a>s2.xlarge.1</p>
</td>
<td class="cellrowborder" valign="top" width="12.12121212121212%" headers="mcps1.2.8.1.2 "><p id="p543726571959"><a name="p543726571959"></a><a name="p543726571959"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515149%" headers="mcps1.2.8.1.3 "><p id="p421091361959"><a name="p421091361959"></a><a name="p421091361959"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.8.1.4 "><p id="p156375914502"><a name="p156375914502"></a><a name="p156375914502"></a>1.5/0.4</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.8.1.5 "><p id="p158144210491"><a name="p158144210491"></a><a name="p158144210491"></a>15</p>
</td>
<td class="cellrowborder" valign="top" width="10.1010101010101%" headers="mcps1.2.8.1.6 "><p id="p9453932144914"><a name="p9453932144914"></a><a name="p9453932144914"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.2.8.1.7 "><p id="p5827133441213"><a name="p5827133441213"></a><a name="p5827133441213"></a>KVM</p>
</td>
</tr>
<tr id="row288099461959"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.2.8.1.1 "><p id="p95931255537"><a name="p95931255537"></a><a name="p95931255537"></a>s2.2xlarge.1</p>
</td>
<td class="cellrowborder" valign="top" width="12.12121212121212%" headers="mcps1.2.8.1.2 "><p id="p434992051959"><a name="p434992051959"></a><a name="p434992051959"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515149%" headers="mcps1.2.8.1.3 "><p id="p337747171959"><a name="p337747171959"></a><a name="p337747171959"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.8.1.4 "><p id="p19637189145011"><a name="p19637189145011"></a><a name="p19637189145011"></a>3/0.8</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.8.1.5 "><p id="p8811742104910"><a name="p8811742104910"></a><a name="p8811742104910"></a>20</p>
</td>
<td class="cellrowborder" valign="top" width="10.1010101010101%" headers="mcps1.2.8.1.6 "><p id="p345383254912"><a name="p345383254912"></a><a name="p345383254912"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.2.8.1.7 "><p id="p582711346124"><a name="p582711346124"></a><a name="p582711346124"></a>KVM</p>
</td>
</tr>
<tr id="row599249481959"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.2.8.1.1 "><p id="p65930517535"><a name="p65930517535"></a><a name="p65930517535"></a>s2.4xlarge.1</p>
</td>
<td class="cellrowborder" valign="top" width="12.12121212121212%" headers="mcps1.2.8.1.2 "><p id="p438639621959"><a name="p438639621959"></a><a name="p438639621959"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515149%" headers="mcps1.2.8.1.3 "><p id="p633200051959"><a name="p633200051959"></a><a name="p633200051959"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.8.1.4 "><p id="p1864612955016"><a name="p1864612955016"></a><a name="p1864612955016"></a>4/1.5</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.8.1.5 "><p id="p138715427495"><a name="p138715427495"></a><a name="p138715427495"></a>30</p>
</td>
<td class="cellrowborder" valign="top" width="10.1010101010101%" headers="mcps1.2.8.1.6 "><p id="p1646213254911"><a name="p1646213254911"></a><a name="p1646213254911"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.2.8.1.7 "><p id="p382753431213"><a name="p382753431213"></a><a name="p382753431213"></a>KVM</p>
</td>
</tr>
<tr id="row564944771959"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.2.8.1.1 "><p id="p05941752533"><a name="p05941752533"></a><a name="p05941752533"></a>s2.8xlarge.1</p>
</td>
<td class="cellrowborder" valign="top" width="12.12121212121212%" headers="mcps1.2.8.1.2 "><p id="p180083521959"><a name="p180083521959"></a><a name="p180083521959"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515149%" headers="mcps1.2.8.1.3 "><p id="p493904411959"><a name="p493904411959"></a><a name="p493904411959"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.8.1.4 "><p id="p864612916506"><a name="p864612916506"></a><a name="p864612916506"></a>6/3</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.8.1.5 "><p id="p1987194218494"><a name="p1987194218494"></a><a name="p1987194218494"></a>50</p>
</td>
<td class="cellrowborder" valign="top" width="10.1010101010101%" headers="mcps1.2.8.1.6 "><p id="p546233284920"><a name="p546233284920"></a><a name="p546233284920"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.2.8.1.7 "><p id="p1982763461211"><a name="p1982763461211"></a><a name="p1982763461211"></a>KVM</p>
</td>
</tr>
<tr id="row352807961959"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.2.8.1.1 "><p id="p155941654533"><a name="p155941654533"></a><a name="p155941654533"></a>s2.medium.2</p>
</td>
<td class="cellrowborder" valign="top" width="12.12121212121212%" headers="mcps1.2.8.1.2 "><p id="p188338101959"><a name="p188338101959"></a><a name="p188338101959"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515149%" headers="mcps1.2.8.1.3 "><p id="p491436661959"><a name="p491436661959"></a><a name="p491436661959"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.8.1.4 "><p id="p116461792504"><a name="p116461792504"></a><a name="p116461792504"></a>0.5/0.1</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.8.1.5 "><p id="p198774215497"><a name="p198774215497"></a><a name="p198774215497"></a>5</p>
</td>
<td class="cellrowborder" valign="top" width="10.1010101010101%" headers="mcps1.2.8.1.6 "><p id="p246243234919"><a name="p246243234919"></a><a name="p246243234919"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.2.8.1.7 "><p id="p188277348127"><a name="p188277348127"></a><a name="p188277348127"></a>KVM</p>
</td>
</tr>
<tr id="row50292659191342"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.2.8.1.1 "><p id="p1159420517534"><a name="p1159420517534"></a><a name="p1159420517534"></a>s2.large.2</p>
</td>
<td class="cellrowborder" valign="top" width="12.12121212121212%" headers="mcps1.2.8.1.2 "><p id="p21909021191342"><a name="p21909021191342"></a><a name="p21909021191342"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515149%" headers="mcps1.2.8.1.3 "><p id="p29800280191342"><a name="p29800280191342"></a><a name="p29800280191342"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.8.1.4 "><p id="p10646093501"><a name="p10646093501"></a><a name="p10646093501"></a>0.8/0.2</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.8.1.5 "><p id="p198720424493"><a name="p198720424493"></a><a name="p198720424493"></a>10</p>
</td>
<td class="cellrowborder" valign="top" width="10.1010101010101%" headers="mcps1.2.8.1.6 "><p id="p9462203254910"><a name="p9462203254910"></a><a name="p9462203254910"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.2.8.1.7 "><p id="p14827133491214"><a name="p14827133491214"></a><a name="p14827133491214"></a>KVM</p>
</td>
</tr>
<tr id="row43581420191342"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.2.8.1.1 "><p id="p7594185195314"><a name="p7594185195314"></a><a name="p7594185195314"></a>s2.xlarge.2</p>
</td>
<td class="cellrowborder" valign="top" width="12.12121212121212%" headers="mcps1.2.8.1.2 "><p id="p28362577191342"><a name="p28362577191342"></a><a name="p28362577191342"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515149%" headers="mcps1.2.8.1.3 "><p id="p15667423191342"><a name="p15667423191342"></a><a name="p15667423191342"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.8.1.4 "><p id="p46461297504"><a name="p46461297504"></a><a name="p46461297504"></a>1.5/0.4</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.8.1.5 "><p id="p1387184244913"><a name="p1387184244913"></a><a name="p1387184244913"></a>15</p>
</td>
<td class="cellrowborder" valign="top" width="10.1010101010101%" headers="mcps1.2.8.1.6 "><p id="p12462113216496"><a name="p12462113216496"></a><a name="p12462113216496"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.2.8.1.7 "><p id="p0619165814147"><a name="p0619165814147"></a><a name="p0619165814147"></a>KVM</p>
</td>
</tr>
<tr id="row37213243191342"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.2.8.1.1 "><p id="p5594145135314"><a name="p5594145135314"></a><a name="p5594145135314"></a>s2.2xlarge.2</p>
</td>
<td class="cellrowborder" valign="top" width="12.12121212121212%" headers="mcps1.2.8.1.2 "><p id="p16473696191342"><a name="p16473696191342"></a><a name="p16473696191342"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515149%" headers="mcps1.2.8.1.3 "><p id="p59300970191342"><a name="p59300970191342"></a><a name="p59300970191342"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.8.1.4 "><p id="p86471793509"><a name="p86471793509"></a><a name="p86471793509"></a>3/0.8</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.8.1.5 "><p id="p68724294912"><a name="p68724294912"></a><a name="p68724294912"></a>20</p>
</td>
<td class="cellrowborder" valign="top" width="10.1010101010101%" headers="mcps1.2.8.1.6 "><p id="p146219329499"><a name="p146219329499"></a><a name="p146219329499"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.2.8.1.7 "><p id="p963535851412"><a name="p963535851412"></a><a name="p963535851412"></a>KVM</p>
</td>
</tr>
<tr id="row56701193191342"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.2.8.1.1 "><p id="p3594553537"><a name="p3594553537"></a><a name="p3594553537"></a>s2.4xlarge.2</p>
</td>
<td class="cellrowborder" valign="top" width="12.12121212121212%" headers="mcps1.2.8.1.2 "><p id="p63218839191342"><a name="p63218839191342"></a><a name="p63218839191342"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515149%" headers="mcps1.2.8.1.3 "><p id="p20452344191342"><a name="p20452344191342"></a><a name="p20452344191342"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.8.1.4 "><p id="p564714910507"><a name="p564714910507"></a><a name="p564714910507"></a>4/1.5</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.8.1.5 "><p id="p1787242134917"><a name="p1787242134917"></a><a name="p1787242134917"></a>30</p>
</td>
<td class="cellrowborder" valign="top" width="10.1010101010101%" headers="mcps1.2.8.1.6 "><p id="p1546223204917"><a name="p1546223204917"></a><a name="p1546223204917"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.2.8.1.7 "><p id="p2649958201418"><a name="p2649958201418"></a><a name="p2649958201418"></a>KVM</p>
</td>
</tr>
<tr id="row5879428191342"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.2.8.1.1 "><p id="p1059515175311"><a name="p1059515175311"></a><a name="p1059515175311"></a>s2.8xlarge.2</p>
</td>
<td class="cellrowborder" valign="top" width="12.12121212121212%" headers="mcps1.2.8.1.2 "><p id="p58245071191342"><a name="p58245071191342"></a><a name="p58245071191342"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515149%" headers="mcps1.2.8.1.3 "><p id="p20230288191342"><a name="p20230288191342"></a><a name="p20230288191342"></a>64</p>
</td>
<td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.8.1.4 "><p id="p12647493500"><a name="p12647493500"></a><a name="p12647493500"></a>6/3</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.8.1.5 "><p id="p1188642164915"><a name="p1188642164915"></a><a name="p1188642164915"></a>50</p>
</td>
<td class="cellrowborder" valign="top" width="10.1010101010101%" headers="mcps1.2.8.1.6 "><p id="p04621832144916"><a name="p04621832144916"></a><a name="p04621832144916"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.2.8.1.7 "><p id="p6661125812144"><a name="p6661125812144"></a><a name="p6661125812144"></a>KVM</p>
</td>
</tr>
<tr id="row14942819191342"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.2.8.1.1 "><p id="p159515514533"><a name="p159515514533"></a><a name="p159515514533"></a>s2.medium.4</p>
</td>
<td class="cellrowborder" valign="top" width="12.12121212121212%" headers="mcps1.2.8.1.2 "><p id="p21679653191342"><a name="p21679653191342"></a><a name="p21679653191342"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515149%" headers="mcps1.2.8.1.3 "><p id="p11221506191342"><a name="p11221506191342"></a><a name="p11221506191342"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.8.1.4 "><p id="p1464739195011"><a name="p1464739195011"></a><a name="p1464739195011"></a>0.5/0.1</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.8.1.5 "><p id="p58844264915"><a name="p58844264915"></a><a name="p58844264915"></a>5</p>
</td>
<td class="cellrowborder" valign="top" width="10.1010101010101%" headers="mcps1.2.8.1.6 "><p id="p1946243214497"><a name="p1946243214497"></a><a name="p1946243214497"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.2.8.1.7 "><p id="p166773584147"><a name="p166773584147"></a><a name="p166773584147"></a>KVM</p>
</td>
</tr>
<tr id="row34065318191342"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.2.8.1.1 "><p id="p1659514516539"><a name="p1659514516539"></a><a name="p1659514516539"></a>s2.large.4</p>
</td>
<td class="cellrowborder" valign="top" width="12.12121212121212%" headers="mcps1.2.8.1.2 "><p id="p3337154191342"><a name="p3337154191342"></a><a name="p3337154191342"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515149%" headers="mcps1.2.8.1.3 "><p id="p1874083191342"><a name="p1874083191342"></a><a name="p1874083191342"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.8.1.4 "><p id="p36471195506"><a name="p36471195506"></a><a name="p36471195506"></a>0.8/0.2</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.8.1.5 "><p id="p1788842184912"><a name="p1788842184912"></a><a name="p1788842184912"></a>10</p>
</td>
<td class="cellrowborder" valign="top" width="10.1010101010101%" headers="mcps1.2.8.1.6 "><p id="p846263234913"><a name="p846263234913"></a><a name="p846263234913"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.2.8.1.7 "><p id="p12691205861418"><a name="p12691205861418"></a><a name="p12691205861418"></a>KVM</p>
</td>
</tr>
<tr id="row15811817191425"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.2.8.1.1 "><p id="p195951556531"><a name="p195951556531"></a><a name="p195951556531"></a>s2.xlarge.4</p>
</td>
<td class="cellrowborder" valign="top" width="12.12121212121212%" headers="mcps1.2.8.1.2 "><p id="p51199203191425"><a name="p51199203191425"></a><a name="p51199203191425"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515149%" headers="mcps1.2.8.1.3 "><p id="p53494782191425"><a name="p53494782191425"></a><a name="p53494782191425"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.8.1.4 "><p id="p18647299504"><a name="p18647299504"></a><a name="p18647299504"></a>1.5/0.4</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.8.1.5 "><p id="p388184211491"><a name="p388184211491"></a><a name="p388184211491"></a>15</p>
</td>
<td class="cellrowborder" valign="top" width="10.1010101010101%" headers="mcps1.2.8.1.6 "><p id="p546223284910"><a name="p546223284910"></a><a name="p546223284910"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.2.8.1.7 "><p id="p17705155821410"><a name="p17705155821410"></a><a name="p17705155821410"></a>KVM</p>
</td>
</tr>
<tr id="row39274866191425"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.2.8.1.1 "><p id="p85953518533"><a name="p85953518533"></a><a name="p85953518533"></a>s2.2xlarge.4</p>
</td>
<td class="cellrowborder" valign="top" width="12.12121212121212%" headers="mcps1.2.8.1.2 "><p id="p43001319191425"><a name="p43001319191425"></a><a name="p43001319191425"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515149%" headers="mcps1.2.8.1.3 "><p id="p60554837191425"><a name="p60554837191425"></a><a name="p60554837191425"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.8.1.4 "><p id="p1647169185013"><a name="p1647169185013"></a><a name="p1647169185013"></a>3/0.8</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.8.1.5 "><p id="p58884204918"><a name="p58884204918"></a><a name="p58884204918"></a>20</p>
</td>
<td class="cellrowborder" valign="top" width="10.1010101010101%" headers="mcps1.2.8.1.6 "><p id="p17462232194916"><a name="p17462232194916"></a><a name="p17462232194916"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.2.8.1.7 "><p id="p2717658111417"><a name="p2717658111417"></a><a name="p2717658111417"></a>KVM</p>
</td>
</tr>
<tr id="row33191825191425"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.2.8.1.1 "><p id="p10595757532"><a name="p10595757532"></a><a name="p10595757532"></a>s2.4xlarge.4</p>
</td>
<td class="cellrowborder" valign="top" width="12.12121212121212%" headers="mcps1.2.8.1.2 "><p id="p37649990191425"><a name="p37649990191425"></a><a name="p37649990191425"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515149%" headers="mcps1.2.8.1.3 "><p id="p29750320191425"><a name="p29750320191425"></a><a name="p29750320191425"></a>64</p>
</td>
<td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.8.1.4 "><p id="p564712919502"><a name="p564712919502"></a><a name="p564712919502"></a>4/1.5</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.8.1.5 "><p id="p78854220494"><a name="p78854220494"></a><a name="p78854220494"></a>30</p>
</td>
<td class="cellrowborder" valign="top" width="10.1010101010101%" headers="mcps1.2.8.1.6 "><p id="p1346253212494"><a name="p1346253212494"></a><a name="p1346253212494"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.2.8.1.7 "><p id="p814815391515"><a name="p814815391515"></a><a name="p814815391515"></a>KVM</p>
</td>
</tr>
<tr id="row18231215191425"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.2.8.1.1 "><p id="p1359512595311"><a name="p1359512595311"></a><a name="p1359512595311"></a>s2.8xlarge.4</p>
</td>
<td class="cellrowborder" valign="top" width="12.12121212121212%" headers="mcps1.2.8.1.2 "><p id="p3001165191425"><a name="p3001165191425"></a><a name="p3001165191425"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515149%" headers="mcps1.2.8.1.3 "><p id="p41767822191425"><a name="p41767822191425"></a><a name="p41767822191425"></a>128</p>
</td>
<td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.8.1.4 "><p id="p1764713917507"><a name="p1764713917507"></a><a name="p1764713917507"></a>6/3</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.8.1.5 "><p id="p288174214490"><a name="p288174214490"></a><a name="p288174214490"></a>50</p>
</td>
<td class="cellrowborder" valign="top" width="10.1010101010101%" headers="mcps1.2.8.1.6 "><p id="p18462173284910"><a name="p18462173284910"></a><a name="p18462173284910"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.2.8.1.7 "><p id="p115913371518"><a name="p115913371518"></a><a name="p115913371518"></a>KVM</p>
</td>
</tr>
<tr id="row29918714191425"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.2.8.1.1 "><p id="p19596254533"><a name="p19596254533"></a><a name="p19596254533"></a>s2.medium.8</p>
</td>
<td class="cellrowborder" valign="top" width="12.12121212121212%" headers="mcps1.2.8.1.2 "><p id="p362197191425"><a name="p362197191425"></a><a name="p362197191425"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515149%" headers="mcps1.2.8.1.3 "><p id="p29337974191425"><a name="p29337974191425"></a><a name="p29337974191425"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.8.1.4 "><p id="p36476965016"><a name="p36476965016"></a><a name="p36476965016"></a>0.5/0.1</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.8.1.5 "><p id="p38824218497"><a name="p38824218497"></a><a name="p38824218497"></a>5</p>
</td>
<td class="cellrowborder" valign="top" width="10.1010101010101%" headers="mcps1.2.8.1.6 "><p id="p1346212329493"><a name="p1346212329493"></a><a name="p1346212329493"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.2.8.1.7 "><p id="p117115316155"><a name="p117115316155"></a><a name="p117115316155"></a>KVM</p>
</td>
</tr>
<tr id="row1436713191425"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.2.8.1.1 "><p id="p3596145165317"><a name="p3596145165317"></a><a name="p3596145165317"></a>s2.large.8</p>
</td>
<td class="cellrowborder" valign="top" width="12.12121212121212%" headers="mcps1.2.8.1.2 "><p id="p40731387191425"><a name="p40731387191425"></a><a name="p40731387191425"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515149%" headers="mcps1.2.8.1.3 "><p id="p10908088191425"><a name="p10908088191425"></a><a name="p10908088191425"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.8.1.4 "><p id="p1664716911505"><a name="p1664716911505"></a><a name="p1664716911505"></a>0.8/0.2</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.8.1.5 "><p id="p128811423495"><a name="p128811423495"></a><a name="p128811423495"></a>10</p>
</td>
<td class="cellrowborder" valign="top" width="10.1010101010101%" headers="mcps1.2.8.1.6 "><p id="p546243294913"><a name="p546243294913"></a><a name="p546243294913"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.2.8.1.7 "><p id="p5182183121520"><a name="p5182183121520"></a><a name="p5182183121520"></a>KVM</p>
</td>
</tr>
<tr id="row13454652191425"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.2.8.1.1 "><p id="p1359614514538"><a name="p1359614514538"></a><a name="p1359614514538"></a>s2.xlarge.8</p>
</td>
<td class="cellrowborder" valign="top" width="12.12121212121212%" headers="mcps1.2.8.1.2 "><p id="p10547176191425"><a name="p10547176191425"></a><a name="p10547176191425"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515149%" headers="mcps1.2.8.1.3 "><p id="p49014953191425"><a name="p49014953191425"></a><a name="p49014953191425"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.8.1.4 "><p id="p264712915501"><a name="p264712915501"></a><a name="p264712915501"></a>1.5/0.4</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.8.1.5 "><p id="p178816426492"><a name="p178816426492"></a><a name="p178816426492"></a>15</p>
</td>
<td class="cellrowborder" valign="top" width="10.1010101010101%" headers="mcps1.2.8.1.6 "><p id="p9462203215494"><a name="p9462203215494"></a><a name="p9462203215494"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.2.8.1.7 "><p id="p1319119319153"><a name="p1319119319153"></a><a name="p1319119319153"></a>KVM</p>
</td>
</tr>
<tr id="row18549560191425"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.2.8.1.1 "><p id="p1559614585311"><a name="p1559614585311"></a><a name="p1559614585311"></a>s2.2xlarge.8</p>
</td>
<td class="cellrowborder" valign="top" width="12.12121212121212%" headers="mcps1.2.8.1.2 "><p id="p33747850191425"><a name="p33747850191425"></a><a name="p33747850191425"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515149%" headers="mcps1.2.8.1.3 "><p id="p49221354191425"><a name="p49221354191425"></a><a name="p49221354191425"></a>64</p>
</td>
<td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.8.1.4 "><p id="p464812965016"><a name="p464812965016"></a><a name="p464812965016"></a>3/0.8</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.8.1.5 "><p id="p208814426497"><a name="p208814426497"></a><a name="p208814426497"></a>20</p>
</td>
<td class="cellrowborder" valign="top" width="10.1010101010101%" headers="mcps1.2.8.1.6 "><p id="p12462153254919"><a name="p12462153254919"></a><a name="p12462153254919"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.2.8.1.7 "><p id="p10204838150"><a name="p10204838150"></a><a name="p10204838150"></a>KVM</p>
</td>
</tr>
<tr id="row43372269191425"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.2.8.1.1 "><p id="p559675135318"><a name="p559675135318"></a><a name="p559675135318"></a>s2.4xlarge.8</p>
</td>
<td class="cellrowborder" valign="top" width="12.12121212121212%" headers="mcps1.2.8.1.2 "><p id="p10109784191425"><a name="p10109784191425"></a><a name="p10109784191425"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515149%" headers="mcps1.2.8.1.3 "><p id="p13586209191425"><a name="p13586209191425"></a><a name="p13586209191425"></a>128</p>
</td>
<td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.8.1.4 "><p id="p15465321164215"><a name="p15465321164215"></a><a name="p15465321164215"></a>4/1.5</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.8.1.5 "><p id="p689352819422"><a name="p689352819422"></a><a name="p689352819422"></a>30</p>
</td>
<td class="cellrowborder" valign="top" width="10.1010101010101%" headers="mcps1.2.8.1.6 "><p id="p1191932164212"><a name="p1191932164212"></a><a name="p1191932164212"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.2.8.1.7 "><p id="p92127317152"><a name="p92127317152"></a><a name="p92127317152"></a>KVM</p>
</td>
</tr>
<tr id="row19438003191425"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.2.8.1.1 "><p id="p105971555316"><a name="p105971555316"></a><a name="p105971555316"></a>s2.8xlarge.8</p>
</td>
<td class="cellrowborder" valign="top" width="12.12121212121212%" headers="mcps1.2.8.1.2 "><p id="p10334226191425"><a name="p10334226191425"></a><a name="p10334226191425"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515149%" headers="mcps1.2.8.1.3 "><p id="p31765949191425"><a name="p31765949191425"></a><a name="p31765949191425"></a>256</p>
</td>
<td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.8.1.4 "><p id="p10465821134211"><a name="p10465821134211"></a><a name="p10465821134211"></a>6/3</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.8.1.5 "><p id="p9893628174217"><a name="p9893628174217"></a><a name="p9893628174217"></a>50</p>
</td>
<td class="cellrowborder" valign="top" width="10.1010101010101%" headers="mcps1.2.8.1.6 "><p id="p1591332124217"><a name="p1591332124217"></a><a name="p1591332124217"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.2.8.1.7 "><p id="p82260321514"><a name="p82260321514"></a><a name="p82260321514"></a>KVM</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  S1, C1, C2, and M1 ECS specifications

<a name="table22516184173957"></a>
<table><thead align="left"><tr id="row33523545173957"><th class="cellrowborder" valign="top" width="22.61%" id="mcps1.2.5.1.1"><p id="p132919597519"><a name="p132919597519"></a><a name="p132919597519"></a>Flavor</p>
</th>
<th class="cellrowborder" valign="top" width="20.43%" id="mcps1.2.5.1.2"><p id="p5791402162942"><a name="p5791402162942"></a><a name="p5791402162942"></a>vCPUs</p>
</th>
<th class="cellrowborder" valign="top" width="26.83%" id="mcps1.2.5.1.3"><p id="p66450389162942"><a name="p66450389162942"></a><a name="p66450389162942"></a>Memory (GB)</p>
</th>
<th class="cellrowborder" valign="top" width="30.130000000000003%" id="mcps1.2.5.1.4"><p id="p1833318216119"><a name="p1833318216119"></a><a name="p1833318216119"></a>Virtualization Type</p>
</th>
</tr>
</thead>
<tbody><tr id="row28438458195333"><td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.1 "><p id="p1629105913519"><a name="p1629105913519"></a><a name="p1629105913519"></a>s1.medium</p>
</td>
<td class="cellrowborder" valign="top" width="20.43%" headers="mcps1.2.5.1.2 "><p id="p37011621195351"><a name="p37011621195351"></a><a name="p37011621195351"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="26.83%" headers="mcps1.2.5.1.3 "><p id="p45151358195351"><a name="p45151358195351"></a><a name="p45151358195351"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="30.130000000000003%" headers="mcps1.2.5.1.4 "><p id="p89822038191013"><a name="p89822038191013"></a><a name="p89822038191013"></a>Xen</p>
</td>
</tr>
<tr id="row39070457195333"><td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.1 "><p id="p82910592517"><a name="p82910592517"></a><a name="p82910592517"></a>s1.large</p>
</td>
<td class="cellrowborder" valign="top" width="20.43%" headers="mcps1.2.5.1.2 "><p id="p41622880195351"><a name="p41622880195351"></a><a name="p41622880195351"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="26.83%" headers="mcps1.2.5.1.3 "><p id="p16010111195351"><a name="p16010111195351"></a><a name="p16010111195351"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="30.130000000000003%" headers="mcps1.2.5.1.4 "><p id="p89831386107"><a name="p89831386107"></a><a name="p89831386107"></a>Xen</p>
</td>
</tr>
<tr id="row13545503195333"><td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.1 "><p id="p52911759959"><a name="p52911759959"></a><a name="p52911759959"></a>s1.xlarge</p>
</td>
<td class="cellrowborder" valign="top" width="20.43%" headers="mcps1.2.5.1.2 "><p id="p18524441195351"><a name="p18524441195351"></a><a name="p18524441195351"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="26.83%" headers="mcps1.2.5.1.3 "><p id="p24084713195351"><a name="p24084713195351"></a><a name="p24084713195351"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="30.130000000000003%" headers="mcps1.2.5.1.4 "><p id="p49831238101011"><a name="p49831238101011"></a><a name="p49831238101011"></a>Xen</p>
</td>
</tr>
<tr id="row43199762195333"><td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.1 "><p id="p129275917513"><a name="p129275917513"></a><a name="p129275917513"></a>s1.2xlarge</p>
</td>
<td class="cellrowborder" valign="top" width="20.43%" headers="mcps1.2.5.1.2 "><p id="p7181390195351"><a name="p7181390195351"></a><a name="p7181390195351"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="26.83%" headers="mcps1.2.5.1.3 "><p id="p44821737195351"><a name="p44821737195351"></a><a name="p44821737195351"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="30.130000000000003%" headers="mcps1.2.5.1.4 "><p id="p99832038161013"><a name="p99832038161013"></a><a name="p99832038161013"></a>Xen</p>
</td>
</tr>
<tr id="row35198851195333"><td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.1 "><p id="p202926591052"><a name="p202926591052"></a><a name="p202926591052"></a>s1.4xlarge</p>
</td>
<td class="cellrowborder" valign="top" width="20.43%" headers="mcps1.2.5.1.2 "><p id="p39407624195351"><a name="p39407624195351"></a><a name="p39407624195351"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="26.83%" headers="mcps1.2.5.1.3 "><p id="p37900984195351"><a name="p37900984195351"></a><a name="p37900984195351"></a>64</p>
</td>
<td class="cellrowborder" valign="top" width="30.130000000000003%" headers="mcps1.2.5.1.4 "><p id="p15983143861010"><a name="p15983143861010"></a><a name="p15983143861010"></a>Xen</p>
</td>
</tr>
<tr id="row27047593195333"><td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.1 "><p id="p8292155916518"><a name="p8292155916518"></a><a name="p8292155916518"></a>s1.8xlarge</p>
</td>
<td class="cellrowborder" valign="top" width="20.43%" headers="mcps1.2.5.1.2 "><p id="p1713557195351"><a name="p1713557195351"></a><a name="p1713557195351"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="26.83%" headers="mcps1.2.5.1.3 "><p id="p4580435195351"><a name="p4580435195351"></a><a name="p4580435195351"></a>128</p>
</td>
<td class="cellrowborder" valign="top" width="30.130000000000003%" headers="mcps1.2.5.1.4 "><p id="p1298353821010"><a name="p1298353821010"></a><a name="p1298353821010"></a>Xen</p>
</td>
</tr>
<tr id="row65035839173957"><td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.1 "><p id="p329265915517"><a name="p329265915517"></a><a name="p329265915517"></a>c1.medium</p>
</td>
<td class="cellrowborder" valign="top" width="20.43%" headers="mcps1.2.5.1.2 "><p id="p2551194174039"><a name="p2551194174039"></a><a name="p2551194174039"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="26.83%" headers="mcps1.2.5.1.3 "><p id="p5320134174039"><a name="p5320134174039"></a><a name="p5320134174039"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="30.130000000000003%" headers="mcps1.2.5.1.4 "><p id="p1098310383103"><a name="p1098310383103"></a><a name="p1098310383103"></a>Xen</p>
</td>
</tr>
<tr id="row57840050173957"><td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.1 "><p id="p1929355910513"><a name="p1929355910513"></a><a name="p1929355910513"></a>c1.large</p>
</td>
<td class="cellrowborder" valign="top" width="20.43%" headers="mcps1.2.5.1.2 "><p id="p36386150174039"><a name="p36386150174039"></a><a name="p36386150174039"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="26.83%" headers="mcps1.2.5.1.3 "><p id="p61597001174039"><a name="p61597001174039"></a><a name="p61597001174039"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="30.130000000000003%" headers="mcps1.2.5.1.4 "><p id="p798311383103"><a name="p798311383103"></a><a name="p798311383103"></a>Xen</p>
</td>
</tr>
<tr id="row1115876617406"><td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.1 "><p id="p1429317599510"><a name="p1429317599510"></a><a name="p1429317599510"></a>c1.xlarge</p>
</td>
<td class="cellrowborder" valign="top" width="20.43%" headers="mcps1.2.5.1.2 "><p id="p47949486174039"><a name="p47949486174039"></a><a name="p47949486174039"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="26.83%" headers="mcps1.2.5.1.3 "><p id="p58703123174039"><a name="p58703123174039"></a><a name="p58703123174039"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="30.130000000000003%" headers="mcps1.2.5.1.4 "><p id="p82741640101119"><a name="p82741640101119"></a><a name="p82741640101119"></a>Xen</p>
</td>
</tr>
<tr id="row5929870173957"><td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.1 "><p id="p92935591355"><a name="p92935591355"></a><a name="p92935591355"></a>c1.2xlarge</p>
</td>
<td class="cellrowborder" valign="top" width="20.43%" headers="mcps1.2.5.1.2 "><p id="p53090939174039"><a name="p53090939174039"></a><a name="p53090939174039"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="26.83%" headers="mcps1.2.5.1.3 "><p id="p5398779174039"><a name="p5398779174039"></a><a name="p5398779174039"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="30.130000000000003%" headers="mcps1.2.5.1.4 "><p id="p15287104017117"><a name="p15287104017117"></a><a name="p15287104017117"></a>Xen</p>
</td>
</tr>
<tr id="row45714607173957"><td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.1 "><p id="p929313596516"><a name="p929313596516"></a><a name="p929313596516"></a>c1.4xlarge</p>
</td>
<td class="cellrowborder" valign="top" width="20.43%" headers="mcps1.2.5.1.2 "><p id="p46828894174039"><a name="p46828894174039"></a><a name="p46828894174039"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="26.83%" headers="mcps1.2.5.1.3 "><p id="p35044068174039"><a name="p35044068174039"></a><a name="p35044068174039"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="30.130000000000003%" headers="mcps1.2.5.1.4 "><p id="p16300154081118"><a name="p16300154081118"></a><a name="p16300154081118"></a>Xen</p>
</td>
</tr>
<tr id="row6550134173957"><td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.1 "><p id="p32932591955"><a name="p32932591955"></a><a name="p32932591955"></a>c1.8xlarge</p>
</td>
<td class="cellrowborder" valign="top" width="20.43%" headers="mcps1.2.5.1.2 "><p id="p35988912174039"><a name="p35988912174039"></a><a name="p35988912174039"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="26.83%" headers="mcps1.2.5.1.3 "><p id="p29420789174039"><a name="p29420789174039"></a><a name="p29420789174039"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="30.130000000000003%" headers="mcps1.2.5.1.4 "><p id="p8310124051110"><a name="p8310124051110"></a><a name="p8310124051110"></a>Xen</p>
</td>
</tr>
<tr id="row1801009391213"><td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.1 "><p id="p172932599520"><a name="p172932599520"></a><a name="p172932599520"></a>c2.medium</p>
</td>
<td class="cellrowborder" valign="top" width="20.43%" headers="mcps1.2.5.1.2 "><p id="p7985891240"><a name="p7985891240"></a><a name="p7985891240"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="26.83%" headers="mcps1.2.5.1.3 "><p id="p646849891240"><a name="p646849891240"></a><a name="p646849891240"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="30.130000000000003%" headers="mcps1.2.5.1.4 "><p id="p15325154061110"><a name="p15325154061110"></a><a name="p15325154061110"></a>Xen</p>
</td>
</tr>
<tr id="row6483686591213"><td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.1 "><p id="p429425916510"><a name="p429425916510"></a><a name="p429425916510"></a>c2.large</p>
</td>
<td class="cellrowborder" valign="top" width="20.43%" headers="mcps1.2.5.1.2 "><p id="p3057709891240"><a name="p3057709891240"></a><a name="p3057709891240"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="26.83%" headers="mcps1.2.5.1.3 "><p id="p6082588691240"><a name="p6082588691240"></a><a name="p6082588691240"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="30.130000000000003%" headers="mcps1.2.5.1.4 "><p id="p1933984010112"><a name="p1933984010112"></a><a name="p1933984010112"></a>Xen</p>
</td>
</tr>
<tr id="row810537891213"><td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.1 "><p id="p8294195912515"><a name="p8294195912515"></a><a name="p8294195912515"></a>c2.xlarge</p>
</td>
<td class="cellrowborder" valign="top" width="20.43%" headers="mcps1.2.5.1.2 "><p id="p6053106191240"><a name="p6053106191240"></a><a name="p6053106191240"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="26.83%" headers="mcps1.2.5.1.3 "><p id="p406890291240"><a name="p406890291240"></a><a name="p406890291240"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="30.130000000000003%" headers="mcps1.2.5.1.4 "><p id="p173513402114"><a name="p173513402114"></a><a name="p173513402114"></a>Xen</p>
</td>
</tr>
<tr id="row3614008491213"><td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.1 "><p id="p1529414591154"><a name="p1529414591154"></a><a name="p1529414591154"></a>c2.2xlarge</p>
</td>
<td class="cellrowborder" valign="top" width="20.43%" headers="mcps1.2.5.1.2 "><p id="p6320490791240"><a name="p6320490791240"></a><a name="p6320490791240"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="26.83%" headers="mcps1.2.5.1.3 "><p id="p1932382791240"><a name="p1932382791240"></a><a name="p1932382791240"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="30.130000000000003%" headers="mcps1.2.5.1.4 "><p id="p43628403116"><a name="p43628403116"></a><a name="p43628403116"></a>Xen</p>
</td>
</tr>
<tr id="row3895062891213"><td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.1 "><p id="p1629420595518"><a name="p1629420595518"></a><a name="p1629420595518"></a>c2.4xlarge</p>
</td>
<td class="cellrowborder" valign="top" width="20.43%" headers="mcps1.2.5.1.2 "><p id="p5330129391240"><a name="p5330129391240"></a><a name="p5330129391240"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="26.83%" headers="mcps1.2.5.1.3 "><p id="p2243746291240"><a name="p2243746291240"></a><a name="p2243746291240"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="30.130000000000003%" headers="mcps1.2.5.1.4 "><p id="p3173164615112"><a name="p3173164615112"></a><a name="p3173164615112"></a>Xen</p>
</td>
</tr>
<tr id="row5815063291213"><td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.1 "><p id="p1629415591359"><a name="p1629415591359"></a><a name="p1629415591359"></a>c2.8xlarge</p>
</td>
<td class="cellrowborder" valign="top" width="20.43%" headers="mcps1.2.5.1.2 "><p id="p1069952491240"><a name="p1069952491240"></a><a name="p1069952491240"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="26.83%" headers="mcps1.2.5.1.3 "><p id="p6135511291240"><a name="p6135511291240"></a><a name="p6135511291240"></a>64</p>
</td>
<td class="cellrowborder" valign="top" width="30.130000000000003%" headers="mcps1.2.5.1.4 "><p id="p1618354616113"><a name="p1618354616113"></a><a name="p1618354616113"></a>Xen</p>
</td>
</tr>
<tr id="row216944920257"><td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.1 "><p id="p429412591255"><a name="p429412591255"></a><a name="p429412591255"></a>m1.medium</p>
</td>
<td class="cellrowborder" valign="top" width="20.43%" headers="mcps1.2.5.1.2 "><p id="p5541363120312"><a name="p5541363120312"></a><a name="p5541363120312"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="26.83%" headers="mcps1.2.5.1.3 "><p id="p5931913220312"><a name="p5931913220312"></a><a name="p5931913220312"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="30.130000000000003%" headers="mcps1.2.5.1.4 "><p id="p1219416469112"><a name="p1219416469112"></a><a name="p1219416469112"></a>Xen</p>
</td>
</tr>
<tr id="row342561520257"><td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.1 "><p id="p3294259652"><a name="p3294259652"></a><a name="p3294259652"></a>m1.large</p>
</td>
<td class="cellrowborder" valign="top" width="20.43%" headers="mcps1.2.5.1.2 "><p id="p5542040820312"><a name="p5542040820312"></a><a name="p5542040820312"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="26.83%" headers="mcps1.2.5.1.3 "><p id="p5986808820312"><a name="p5986808820312"></a><a name="p5986808820312"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="30.130000000000003%" headers="mcps1.2.5.1.4 "><p id="p3203194681115"><a name="p3203194681115"></a><a name="p3203194681115"></a>Xen</p>
</td>
</tr>
<tr id="row2105034020257"><td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.1 "><p id="p92950598519"><a name="p92950598519"></a><a name="p92950598519"></a>m1.xlarge</p>
</td>
<td class="cellrowborder" valign="top" width="20.43%" headers="mcps1.2.5.1.2 "><p id="p5714101820312"><a name="p5714101820312"></a><a name="p5714101820312"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="26.83%" headers="mcps1.2.5.1.3 "><p id="p6501971820312"><a name="p6501971820312"></a><a name="p6501971820312"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="30.130000000000003%" headers="mcps1.2.5.1.4 "><p id="p321210463118"><a name="p321210463118"></a><a name="p321210463118"></a>Xen</p>
</td>
</tr>
<tr id="row6167291120257"><td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.1 "><p id="p1729512591457"><a name="p1729512591457"></a><a name="p1729512591457"></a>m1.2xlarge</p>
</td>
<td class="cellrowborder" valign="top" width="20.43%" headers="mcps1.2.5.1.2 "><p id="p5126683420312"><a name="p5126683420312"></a><a name="p5126683420312"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="26.83%" headers="mcps1.2.5.1.3 "><p id="p5897290220312"><a name="p5897290220312"></a><a name="p5897290220312"></a>64</p>
</td>
<td class="cellrowborder" valign="top" width="30.130000000000003%" headers="mcps1.2.5.1.4 "><p id="p11225246101119"><a name="p11225246101119"></a><a name="p11225246101119"></a>Xen</p>
</td>
</tr>
<tr id="row3491135920257"><td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.1 "><p id="p172958591159"><a name="p172958591159"></a><a name="p172958591159"></a>m1.4xlarge</p>
</td>
<td class="cellrowborder" valign="top" width="20.43%" headers="mcps1.2.5.1.2 "><p id="p1194012120312"><a name="p1194012120312"></a><a name="p1194012120312"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="26.83%" headers="mcps1.2.5.1.3 "><p id="p2762572520312"><a name="p2762572520312"></a><a name="p2762572520312"></a>128</p>
</td>
<td class="cellrowborder" valign="top" width="30.130000000000003%" headers="mcps1.2.5.1.4 "><p id="p1423704621119"><a name="p1423704621119"></a><a name="p1423704621119"></a>Xen</p>
</td>
</tr>
</tbody>
</table>

## Scenarios<a name="section19143182213303"></a>

-   Applications

    General-purpose ECSs are suitable for applications that have no special requirements on CPU performance, memory, disk capacity, or bandwidth, but have high requirements on security and reliability. They feature low initial investment and maintenance costs.

-   Application scenarios

    Enterprise website deployment, enterprise office environment setup, enterprise R&D and testing activities, web servers, R&D and testing environments, and small-scale databases


## Notes<a name="section19230673185147"></a>

-   General-purpose ECSs support all released OSs.
-   Specifications can be exchanged between general-purpose \(S1, C1, C2, or M1\) ECSs and H1 ECSs. For details, see  [Changing a General-Purpose ECS to an H1 ECS](changing-a-general-purpose-ecs-to-an-h1-ecs.md).

