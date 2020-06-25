# Memory-optimized ECSs<a name="EN-US_TOPIC_0035550301"></a>

## Overview<a name="section25374905172644"></a>

-   M4 ECSs use second-generation Intel® Xeon® Scalable processors with technologies optimized to offer powerful and stable computing performance. Using 25GE high-speed intelligent NICs, M4 ECSs provide a maximum memory size of 512 GB based on DDR4 for large-memory applications with high requirements on network bandwidth and Packets Per Second \(PPS\).
-   M3 ECSs are developed based on the KVM virtualization platform and designed for processing large-scale data sets in the memory. They use Intel® Xeon® Scalable processors, network acceleration engines, and DPDK rapid packet processing mechanism to provide higher network performance, offering a maximum memory size of 512 GB based on DDR4 for high-memory computing applications.
-   M2 ECSs use Intel Xeon E5-2690 v4 CPUs and are designed for memory-optimized applications.

## Specifications<a name="section83746578616"></a>

**Table  1**  M4 ECS specifications

<a name="table285612469463"></a>
<table><thead align="left"><tr id="row1885610463467"><th class="cellrowborder" valign="top" width="14.705882352941178%" id="mcps1.2.8.1.1"><p id="p28572464465"><a name="p28572464465"></a><a name="p28572464465"></a>Flavor</p>
</th>
<th class="cellrowborder" valign="top" width="11.76470588235294%" id="mcps1.2.8.1.2"><p id="p16857114674620"><a name="p16857114674620"></a><a name="p16857114674620"></a>vCPUs</p>
</th>
<th class="cellrowborder" valign="top" width="14.705882352941178%" id="mcps1.2.8.1.3"><p id="p1585714614610"><a name="p1585714614610"></a><a name="p1585714614610"></a>Memory (GB)</p>
</th>
<th class="cellrowborder" valign="top" width="18.627450980392158%" id="mcps1.2.8.1.4"><p id="p11857246124612"><a name="p11857246124612"></a><a name="p11857246124612"></a>Maximum/Assured Bandwidth (Gbit/s)</p>
</th>
<th class="cellrowborder" valign="top" width="14.705882352941178%" id="mcps1.2.8.1.5"><p id="p18578467465"><a name="p18578467465"></a><a name="p18578467465"></a>Maximum PPS (10,000)</p>
</th>
<th class="cellrowborder" valign="top" width="9.803921568627452%" id="mcps1.2.8.1.6"><p id="p1285744613465"><a name="p1285744613465"></a><a name="p1285744613465"></a>NIC Multi-Queue</p>
</th>
<th class="cellrowborder" valign="top" width="15.686274509803921%" id="mcps1.2.8.1.7"><p id="p1285719467467"><a name="p1285719467467"></a><a name="p1285719467467"></a>Virtualization Type</p>
</th>
</tr>
</thead>
<tbody><tr id="row7857154615465"><td class="cellrowborder" valign="top" width="14.705882352941178%" headers="mcps1.2.8.1.1 "><p id="p774119397477"><a name="p774119397477"></a><a name="p774119397477"></a>m4.large.8</p>
</td>
<td class="cellrowborder" valign="top" width="11.76470588235294%" headers="mcps1.2.8.1.2 "><p id="p167411139144718"><a name="p167411139144718"></a><a name="p167411139144718"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="14.705882352941178%" headers="mcps1.2.8.1.3 "><p id="p18741153917479"><a name="p18741153917479"></a><a name="p18741153917479"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="18.627450980392158%" headers="mcps1.2.8.1.4 "><p id="p995124674713"><a name="p995124674713"></a><a name="p995124674713"></a>4/1.2</p>
</td>
<td class="cellrowborder" valign="top" width="14.705882352941178%" headers="mcps1.2.8.1.5 "><p id="p324335634715"><a name="p324335634715"></a><a name="p324335634715"></a>40</p>
</td>
<td class="cellrowborder" valign="top" width="9.803921568627452%" headers="mcps1.2.8.1.6 "><p id="p3664153114817"><a name="p3664153114817"></a><a name="p3664153114817"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="15.686274509803921%" headers="mcps1.2.8.1.7 "><p id="p6858146204619"><a name="p6858146204619"></a><a name="p6858146204619"></a>KVM</p>
</td>
</tr>
<tr id="row9858164615465"><td class="cellrowborder" valign="top" width="14.705882352941178%" headers="mcps1.2.8.1.1 "><p id="p1074133914470"><a name="p1074133914470"></a><a name="p1074133914470"></a>m4.xlarge.8</p>
</td>
<td class="cellrowborder" valign="top" width="11.76470588235294%" headers="mcps1.2.8.1.2 "><p id="p147411839124719"><a name="p147411839124719"></a><a name="p147411839124719"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="14.705882352941178%" headers="mcps1.2.8.1.3 "><p id="p974143914710"><a name="p974143914710"></a><a name="p974143914710"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="18.627450980392158%" headers="mcps1.2.8.1.4 "><p id="p295114614478"><a name="p295114614478"></a><a name="p295114614478"></a>8/2.4</p>
</td>
<td class="cellrowborder" valign="top" width="14.705882352941178%" headers="mcps1.2.8.1.5 "><p id="p19243115617473"><a name="p19243115617473"></a><a name="p19243115617473"></a>80</p>
</td>
<td class="cellrowborder" valign="top" width="9.803921568627452%" headers="mcps1.2.8.1.6 "><p id="p1566443204817"><a name="p1566443204817"></a><a name="p1566443204817"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="15.686274509803921%" headers="mcps1.2.8.1.7 "><p id="p08591746114617"><a name="p08591746114617"></a><a name="p08591746114617"></a>KVM</p>
</td>
</tr>
<tr id="row1285920462467"><td class="cellrowborder" valign="top" width="14.705882352941178%" headers="mcps1.2.8.1.1 "><p id="p27411839154714"><a name="p27411839154714"></a><a name="p27411839154714"></a>m4.2xlarge.8</p>
</td>
<td class="cellrowborder" valign="top" width="11.76470588235294%" headers="mcps1.2.8.1.2 "><p id="p1574223904714"><a name="p1574223904714"></a><a name="p1574223904714"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="14.705882352941178%" headers="mcps1.2.8.1.3 "><p id="p17742163917476"><a name="p17742163917476"></a><a name="p17742163917476"></a>64</p>
</td>
<td class="cellrowborder" valign="top" width="18.627450980392158%" headers="mcps1.2.8.1.4 "><p id="p17951134615477"><a name="p17951134615477"></a><a name="p17951134615477"></a>15/4.5</p>
</td>
<td class="cellrowborder" valign="top" width="14.705882352941178%" headers="mcps1.2.8.1.5 "><p id="p42431756124718"><a name="p42431756124718"></a><a name="p42431756124718"></a>150</p>
</td>
<td class="cellrowborder" valign="top" width="9.803921568627452%" headers="mcps1.2.8.1.6 "><p id="p066418314489"><a name="p066418314489"></a><a name="p066418314489"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="15.686274509803921%" headers="mcps1.2.8.1.7 "><p id="p1685918469467"><a name="p1685918469467"></a><a name="p1685918469467"></a>KVM</p>
</td>
</tr>
<tr id="row28601746184612"><td class="cellrowborder" valign="top" width="14.705882352941178%" headers="mcps1.2.8.1.1 "><p id="p9742203944715"><a name="p9742203944715"></a><a name="p9742203944715"></a>m4.3xlarge.8</p>
</td>
<td class="cellrowborder" valign="top" width="11.76470588235294%" headers="mcps1.2.8.1.2 "><p id="p97427399473"><a name="p97427399473"></a><a name="p97427399473"></a>12</p>
</td>
<td class="cellrowborder" valign="top" width="14.705882352941178%" headers="mcps1.2.8.1.3 "><p id="p5742239104718"><a name="p5742239104718"></a><a name="p5742239104718"></a>96</p>
</td>
<td class="cellrowborder" valign="top" width="18.627450980392158%" headers="mcps1.2.8.1.4 "><p id="p995111463479"><a name="p995111463479"></a><a name="p995111463479"></a>17/7</p>
</td>
<td class="cellrowborder" valign="top" width="14.705882352941178%" headers="mcps1.2.8.1.5 "><p id="p18243125615476"><a name="p18243125615476"></a><a name="p18243125615476"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="9.803921568627452%" headers="mcps1.2.8.1.6 "><p id="p8664103134818"><a name="p8664103134818"></a><a name="p8664103134818"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="15.686274509803921%" headers="mcps1.2.8.1.7 "><p id="p118606463468"><a name="p118606463468"></a><a name="p118606463468"></a>KVM</p>
</td>
</tr>
<tr id="row78601946124612"><td class="cellrowborder" valign="top" width="14.705882352941178%" headers="mcps1.2.8.1.1 "><p id="p207427399478"><a name="p207427399478"></a><a name="p207427399478"></a>m4.4xlarge.8</p>
</td>
<td class="cellrowborder" valign="top" width="11.76470588235294%" headers="mcps1.2.8.1.2 "><p id="p97421939124711"><a name="p97421939124711"></a><a name="p97421939124711"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="14.705882352941178%" headers="mcps1.2.8.1.3 "><p id="p6742143994712"><a name="p6742143994712"></a><a name="p6742143994712"></a>128</p>
</td>
<td class="cellrowborder" valign="top" width="18.627450980392158%" headers="mcps1.2.8.1.4 "><p id="p2951144644718"><a name="p2951144644718"></a><a name="p2951144644718"></a>20/9</p>
</td>
<td class="cellrowborder" valign="top" width="14.705882352941178%" headers="mcps1.2.8.1.5 "><p id="p14243125614715"><a name="p14243125614715"></a><a name="p14243125614715"></a>280</p>
</td>
<td class="cellrowborder" valign="top" width="9.803921568627452%" headers="mcps1.2.8.1.6 "><p id="p1166443134819"><a name="p1166443134819"></a><a name="p1166443134819"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="15.686274509803921%" headers="mcps1.2.8.1.7 "><p id="p13861174664618"><a name="p13861174664618"></a><a name="p13861174664618"></a>KVM</p>
</td>
</tr>
<tr id="row1086164620464"><td class="cellrowborder" valign="top" width="14.705882352941178%" headers="mcps1.2.8.1.1 "><p id="p13742539164712"><a name="p13742539164712"></a><a name="p13742539164712"></a>m4.6xlarge.8</p>
</td>
<td class="cellrowborder" valign="top" width="11.76470588235294%" headers="mcps1.2.8.1.2 "><p id="p074223974710"><a name="p074223974710"></a><a name="p074223974710"></a>24</p>
</td>
<td class="cellrowborder" valign="top" width="14.705882352941178%" headers="mcps1.2.8.1.3 "><p id="p13742839174710"><a name="p13742839174710"></a><a name="p13742839174710"></a>192</p>
</td>
<td class="cellrowborder" valign="top" width="18.627450980392158%" headers="mcps1.2.8.1.4 "><p id="p1695184610479"><a name="p1695184610479"></a><a name="p1695184610479"></a>25/14</p>
</td>
<td class="cellrowborder" valign="top" width="14.705882352941178%" headers="mcps1.2.8.1.5 "><p id="p8243115674712"><a name="p8243115674712"></a><a name="p8243115674712"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="9.803921568627452%" headers="mcps1.2.8.1.6 "><p id="p76654318484"><a name="p76654318484"></a><a name="p76654318484"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="15.686274509803921%" headers="mcps1.2.8.1.7 "><p id="p6862346144617"><a name="p6862346144617"></a><a name="p6862346144617"></a>KVM</p>
</td>
</tr>
<tr id="row4491162314473"><td class="cellrowborder" valign="top" width="14.705882352941178%" headers="mcps1.2.8.1.1 "><p id="p2074293934718"><a name="p2074293934718"></a><a name="p2074293934718"></a>m4.8xlarge.8</p>
</td>
<td class="cellrowborder" valign="top" width="11.76470588235294%" headers="mcps1.2.8.1.2 "><p id="p274215393472"><a name="p274215393472"></a><a name="p274215393472"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="14.705882352941178%" headers="mcps1.2.8.1.3 "><p id="p3742173984713"><a name="p3742173984713"></a><a name="p3742173984713"></a>256</p>
</td>
<td class="cellrowborder" valign="top" width="18.627450980392158%" headers="mcps1.2.8.1.4 "><p id="p109511464470"><a name="p109511464470"></a><a name="p109511464470"></a>30/18</p>
</td>
<td class="cellrowborder" valign="top" width="14.705882352941178%" headers="mcps1.2.8.1.5 "><p id="p1524315617470"><a name="p1524315617470"></a><a name="p1524315617470"></a>550</p>
</td>
<td class="cellrowborder" valign="top" width="9.803921568627452%" headers="mcps1.2.8.1.6 "><p id="p86651364814"><a name="p86651364814"></a><a name="p86651364814"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="15.686274509803921%" headers="mcps1.2.8.1.7 "><p id="p179161987483"><a name="p179161987483"></a><a name="p179161987483"></a>KVM</p>
</td>
</tr>
<tr id="row1728916261472"><td class="cellrowborder" valign="top" width="14.705882352941178%" headers="mcps1.2.8.1.1 "><p id="p10742539204719"><a name="p10742539204719"></a><a name="p10742539204719"></a>m4.16xlarge.8</p>
</td>
<td class="cellrowborder" valign="top" width="11.76470588235294%" headers="mcps1.2.8.1.2 "><p id="p47421139204713"><a name="p47421139204713"></a><a name="p47421139204713"></a>64</p>
</td>
<td class="cellrowborder" valign="top" width="14.705882352941178%" headers="mcps1.2.8.1.3 "><p id="p4742133914479"><a name="p4742133914479"></a><a name="p4742133914479"></a>512</p>
</td>
<td class="cellrowborder" valign="top" width="18.627450980392158%" headers="mcps1.2.8.1.4 "><p id="p69511946194711"><a name="p69511946194711"></a><a name="p69511946194711"></a>40/36</p>
</td>
<td class="cellrowborder" valign="top" width="14.705882352941178%" headers="mcps1.2.8.1.5 "><p id="p624325654714"><a name="p624325654714"></a><a name="p624325654714"></a>1000</p>
</td>
<td class="cellrowborder" valign="top" width="9.803921568627452%" headers="mcps1.2.8.1.6 "><p id="p66653311481"><a name="p66653311481"></a><a name="p66653311481"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="15.686274509803921%" headers="mcps1.2.8.1.7 "><p id="p139162812483"><a name="p139162812483"></a><a name="p139162812483"></a>KVM</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  M3 ECS specifications

<a name="table10833218224040"></a>
<table><thead align="left"><tr id="row5178155224040"><th class="cellrowborder" valign="top" width="13.861386138613863%" id="mcps1.2.8.1.1"><p id="p42611119415"><a name="p42611119415"></a><a name="p42611119415"></a>Flavor</p>
</th>
<th class="cellrowborder" valign="top" width="11.881188118811881%" id="mcps1.2.8.1.2"><p id="p910503163011"><a name="p910503163011"></a><a name="p910503163011"></a>vCPUs</p>
</th>
<th class="cellrowborder" valign="top" width="13.861386138613863%" id="mcps1.2.8.1.3"><p id="p6641941163011"><a name="p6641941163011"></a><a name="p6641941163011"></a>Memory (GB)</p>
</th>
<th class="cellrowborder" valign="top" width="18.81188118811881%" id="mcps1.2.8.1.4"><p id="p91221927543"><a name="p91221927543"></a><a name="p91221927543"></a>Maximum/Assured Bandwidth (Gbit/s)</p>
</th>
<th class="cellrowborder" valign="top" width="14.85148514851485%" id="mcps1.2.8.1.5"><p id="p191233274415"><a name="p191233274415"></a><a name="p191233274415"></a>Maximum PPS (10,000)</p>
</th>
<th class="cellrowborder" valign="top" width="10.891089108910892%" id="mcps1.2.8.1.6"><p id="p1312312271849"><a name="p1312312271849"></a><a name="p1312312271849"></a>NIC Multi-Queue</p>
</th>
<th class="cellrowborder" valign="top" width="15.841584158415841%" id="mcps1.2.8.1.7"><p id="p35021151114316"><a name="p35021151114316"></a><a name="p35021151114316"></a>Virtualization Type</p>
</th>
</tr>
</thead>
<tbody><tr id="row57282794203215"><td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.8.1.1 "><p id="p127913415"><a name="p127913415"></a><a name="p127913415"></a>m3.large.8</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.2.8.1.2 "><p id="p17443704203215"><a name="p17443704203215"></a><a name="p17443704203215"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.8.1.3 "><p id="p59515798203733"><a name="p59515798203733"></a><a name="p59515798203733"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.8.1.4 "><p id="p1580915914419"><a name="p1580915914419"></a><a name="p1580915914419"></a>1.5/0.6</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.8.1.5 "><p id="p436210511245"><a name="p436210511245"></a><a name="p436210511245"></a>30</p>
</td>
<td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.2.8.1.6 "><p id="p29745453416"><a name="p29745453416"></a><a name="p29745453416"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.8.1.7 "><p id="p185081351134319"><a name="p185081351134319"></a><a name="p185081351134319"></a>KVM</p>
</td>
</tr>
<tr id="row57168339203215"><td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.8.1.1 "><p id="p1927017411"><a name="p1927017411"></a><a name="p1927017411"></a>m3.xlarge.8</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.2.8.1.2 "><p id="p1115135203215"><a name="p1115135203215"></a><a name="p1115135203215"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.8.1.3 "><p id="p61879054203733"><a name="p61879054203733"></a><a name="p61879054203733"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.8.1.4 "><p id="p118091591847"><a name="p118091591847"></a><a name="p118091591847"></a>3/1.1</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.8.1.5 "><p id="p16363651144"><a name="p16363651144"></a><a name="p16363651144"></a>50</p>
</td>
<td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.2.8.1.6 "><p id="p7974154513415"><a name="p7974154513415"></a><a name="p7974154513415"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.8.1.7 "><p id="p2511051104316"><a name="p2511051104316"></a><a name="p2511051104316"></a>KVM</p>
</td>
</tr>
<tr id="row41647057203220"><td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.8.1.1 "><p id="p102719119419"><a name="p102719119419"></a><a name="p102719119419"></a>m3.2xlarge.8</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.2.8.1.2 "><p id="p27498652203220"><a name="p27498652203220"></a><a name="p27498652203220"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.8.1.3 "><p id="p16852482203733"><a name="p16852482203733"></a><a name="p16852482203733"></a>64</p>
</td>
<td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.8.1.4 "><p id="p78092595410"><a name="p78092595410"></a><a name="p78092595410"></a>5/2</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.8.1.5 "><p id="p2036312511412"><a name="p2036312511412"></a><a name="p2036312511412"></a>90</p>
</td>
<td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.2.8.1.6 "><p id="p139747453418"><a name="p139747453418"></a><a name="p139747453418"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.8.1.7 "><p id="p151613519433"><a name="p151613519433"></a><a name="p151613519433"></a>KVM</p>
</td>
</tr>
<tr id="row30442359203220"><td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.8.1.1 "><p id="p627171442"><a name="p627171442"></a><a name="p627171442"></a>m3.4xlarge.8</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.2.8.1.2 "><p id="p46554934203220"><a name="p46554934203220"></a><a name="p46554934203220"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.8.1.3 "><p id="p30368433203733"><a name="p30368433203733"></a><a name="p30368433203733"></a>128</p>
</td>
<td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.8.1.4 "><p id="p13809195920420"><a name="p13809195920420"></a><a name="p13809195920420"></a>10/4.5</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.8.1.5 "><p id="p036316518419"><a name="p036316518419"></a><a name="p036316518419"></a>130</p>
</td>
<td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.2.8.1.6 "><p id="p16974164518418"><a name="p16974164518418"></a><a name="p16974164518418"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.8.1.7 "><p id="p1951914514430"><a name="p1951914514430"></a><a name="p1951914514430"></a>KVM</p>
</td>
</tr>
<tr id="row64039116203220"><td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.8.1.1 "><p id="p20281211646"><a name="p20281211646"></a><a name="p20281211646"></a>m3.8xlarge.8</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.2.8.1.2 "><p id="p43855233203220"><a name="p43855233203220"></a><a name="p43855233203220"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.8.1.3 "><p id="p13904994203733"><a name="p13904994203733"></a><a name="p13904994203733"></a>256</p>
</td>
<td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.8.1.4 "><p id="p1080914595414"><a name="p1080914595414"></a><a name="p1080914595414"></a>15/9</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.8.1.5 "><p id="p18363851342"><a name="p18363851342"></a><a name="p18363851342"></a>260</p>
</td>
<td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.2.8.1.6 "><p id="p0974245546"><a name="p0974245546"></a><a name="p0974245546"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.8.1.7 "><p id="p125252516438"><a name="p125252516438"></a><a name="p125252516438"></a>KVM</p>
</td>
</tr>
<tr id="row19105347203636"><td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.8.1.1 "><p id="p12813112413"><a name="p12813112413"></a><a name="p12813112413"></a>m3.15xlarge.8</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.2.8.1.2 "><p id="p36263685203636"><a name="p36263685203636"></a><a name="p36263685203636"></a>60</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.8.1.3 "><p id="p51677410203636"><a name="p51677410203636"></a><a name="p51677410203636"></a>512</p>
</td>
<td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.8.1.4 "><p id="p9810175916418"><a name="p9810175916418"></a><a name="p9810175916418"></a>17/17</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.8.1.5 "><p id="p16363175111415"><a name="p16363175111415"></a><a name="p16363175111415"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.2.8.1.6 "><p id="p197411458412"><a name="p197411458412"></a><a name="p197411458412"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.8.1.7 "><p id="p1172594794317"><a name="p1172594794317"></a><a name="p1172594794317"></a>KVM</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  M2 ECS specifications

<a name="table38605135203957"></a>
<table><thead align="left"><tr id="row66310215203957"><th class="cellrowborder" valign="top" width="15%" id="mcps1.2.8.1.1"><p id="p1640540629"><a name="p1640540629"></a><a name="p1640540629"></a>Flavor</p>
</th>
<th class="cellrowborder" valign="top" width="11%" id="mcps1.2.8.1.2"><p id="p61667870203957"><a name="p61667870203957"></a><a name="p61667870203957"></a>vCPUs</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.8.1.3"><p id="p29041564203957"><a name="p29041564203957"></a><a name="p29041564203957"></a>Memory (GB)</p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.8.1.4"><p id="p96871257623"><a name="p96871257623"></a><a name="p96871257623"></a>Maximum/Assured Bandwidth (Gbit/s)</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.8.1.5"><p id="p186875571321"><a name="p186875571321"></a><a name="p186875571321"></a>Maximum PPS (10,000)</p>
</th>
<th class="cellrowborder" valign="top" width="11%" id="mcps1.2.8.1.6"><p id="p11687185711216"><a name="p11687185711216"></a><a name="p11687185711216"></a>NIC Multi-Queue</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.8.1.7"><p id="p84271148153813"><a name="p84271148153813"></a><a name="p84271148153813"></a>Virtualization Type</p>
</th>
</tr>
</thead>
<tbody><tr id="row19640006203957"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.8.1.1 "><p id="p240617015219"><a name="p240617015219"></a><a name="p240617015219"></a>m2.8xlarge.8</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.8.1.2 "><p id="p9062754203957"><a name="p9062754203957"></a><a name="p9062754203957"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.8.1.3 "><p id="p62994446203957"><a name="p62994446203957"></a><a name="p62994446203957"></a>256</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.8.1.4 "><p id="p142297281321"><a name="p142297281321"></a><a name="p142297281321"></a>13/8</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.8.1.5 "><p id="p65394301724"><a name="p65394301724"></a><a name="p65394301724"></a>60</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.8.1.6 "><p id="p1549582519216"><a name="p1549582519216"></a><a name="p1549582519216"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.8.1.7 "><p id="p843412484380"><a name="p843412484380"></a><a name="p843412484380"></a>KVM</p>
</td>
</tr>
</tbody>
</table>

## Scenarios<a name="section2976132851911"></a>

-   High-performance relational \(MySQL\) and NoSQL \(MongoDB and Cassandra\) databases
-   Distributed web scale cache stores that provide in-memory caching of key-value type data \(Memcached and Redis\)
-   Applications processing big unstructured data in real time \(financial services, Hadoop/Spark clusters\)
-   High-performance computing \(HPC\) and electronic design automation \(EDA\)

## Notes on Using M4 ECSs<a name="section1673161413136"></a>

-   M4 ECSs do not have InfiniBand or SSD NICs configured.
-   M4 ECSs support modifying specifications if the source and target ECSs are of the same type.

## Notes on Using M3 ECSs<a name="section44163260352"></a>

-   M3 ECSs support all released OSs.
-   M3 ECSs do not have InfiniBand or SSD NICs configured.
-   M3 ECSs support modifying specifications if the source and target ECSs are of the same type.

## Notes on Using M2 ECSs<a name="section36944454224136"></a>

-   M2 ECSs support all released OSs.
-   M2 ECSs do not have InfiniBand or SSD NICs configured.
-   M2 ECSs support modifying specifications if the source and target ECSs are of the same type.
-   To improve network performance, you can set the NIC MTU of an M2 ECS to  **8888**.

