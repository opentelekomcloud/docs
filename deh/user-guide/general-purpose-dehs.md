# General-purpose DeHs<a name="EN-US_TOPIC_0046252752"></a>

## Overview<a name="section20154144619137"></a>

General-purpose DeHs provide generic hardware performance. ECSs created on this type of DeHs can handle regular workloads and the workload surges within a short period of time.

General-purpose DeHs are classified into general, s2, and s2-medium DeH types.

-   DeHs of the general type can be used to deploy S1, C1, C2, and M1 ECSs. DeHs of the general type can provide generic vCPU performance and improve performance based on workload requirements, offering higher performance in a short term.
-   DeHs of the s2 type can be used to deploy the S2 ECSs. The S2 ECSs use the latest-generation Intel® Xeon® Skylake CPUs, providing better cost-effectiveness.
-   The s2-medium DeHs are similar to s2 DeHs and can be used to deploy the S2 ECSs.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>The number of vCPUs for a DeH is calculated as follows:  
>Number of vCPUs = \(Number of sockets x Number of cores x Number of single-core threads - CPU overheads\) x CPU overcommitment ratio  
>-   general DeHs  
>    Number of vCPUs = \(2 x 12 x 2 - 12\) x 2 = 72  
>-   s2 DeHs  
>    Number of vCPUs = \(2 x 22 x 2 - 16\) x 2 = 144  
>-   s2-medium DeHs  
>    Number of vCPUs = \(2 x 12 x 2 - 12\) x 2 = 72  

## DeH Flavors<a name="section324812342584"></a>

**Table  1**  Flavors of general DeHs

<a name="table8862194220587"></a>
<table><thead align="left"><tr id="row5863442105814"><th class="cellrowborder" valign="top" width="16%" id="mcps1.2.6.1.1"><p id="p4384102125910"><a name="p4384102125910"></a><a name="p4384102125910"></a><strong id="b842352706104944"><a name="b842352706104944"></a><a name="b842352706104944"></a>Flavor Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.6.1.2"><p id="p1186454295817"><a name="p1186454295817"></a><a name="p1186454295817"></a><strong id="b842352706104955"><a name="b842352706104955"></a><a name="b842352706104955"></a>Number of Sockets</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.3"><p id="p16950831185911"><a name="p16950831185911"></a><a name="p16950831185911"></a><strong id="b842352706105035"><a name="b842352706105035"></a><a name="b842352706105035"></a>Number of Cores per Socket</strong></p>
</th>
<th class="cellrowborder" valign="top" width="32%" id="mcps1.2.6.1.4"><p id="p1140118363594"><a name="p1140118363594"></a><a name="p1140118363594"></a><strong id="b842352706105058"><a name="b842352706105058"></a><a name="b842352706105058"></a>Hardware Specifications</strong></p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.6.1.5"><p id="p75778144319"><a name="p75778144319"></a><a name="p75778144319"></a><strong id="b842352706184219"><a name="b842352706184219"></a><a name="b842352706184219"></a>Number of vCPUs</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1286464219587"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.1 "><p id="p88391121819"><a name="p88391121819"></a><a name="p88391121819"></a>general</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.6.1.2 "><p id="p48641542145814"><a name="p48641542145814"></a><a name="p48641542145814"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.3 "><p id="p13865204215819"><a name="p13865204215819"></a><a name="p13865204215819"></a>12</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.6.1.4 "><a name="ul209928558418"></a><a name="ul209928558418"></a><ul id="ul209928558418"><li>CPU:<a name="ul467065518276"></a><a name="ul467065518276"></a><ul id="ul467065518276"><li>Intel&reg; Xeon&reg; Processor E5-2658A v3 (30 MB cache, 2.20 GHz)</li><li>Intel&reg; Xeon&reg; Processor E5-2658 v4 (35 MB Cache, 2.30 GHz)</li></ul>
</li><li>Memory: 264 GB (or 270,336 MB)</li></ul>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.6.1.5 "><p id="p1657717113434"><a name="p1657717113434"></a><a name="p1657717113434"></a>72</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  Flavors of s2 DeHs

<a name="table3861202817579"></a>
<table><thead align="left"><tr id="row14880132895717"><th class="cellrowborder" valign="top" width="16.37%" id="mcps1.2.6.1.1"><p id="p108831628135711"><a name="p108831628135711"></a><a name="p108831628135711"></a><strong id="b998013195251"><a name="b998013195251"></a><a name="b998013195251"></a>Flavor Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.45%" id="mcps1.2.6.1.2"><p id="p168904287571"><a name="p168904287571"></a><a name="p168904287571"></a><strong id="b2088573681"><a name="b2088573681"></a><a name="b2088573681"></a>Number of Sockets</strong></p>
</th>
<th class="cellrowborder" valign="top" width="18.44%" id="mcps1.2.6.1.3"><p id="p58947282576"><a name="p58947282576"></a><a name="p58947282576"></a><strong id="b1169464643"><a name="b1169464643"></a><a name="b1169464643"></a>Number of Cores per Socket</strong></p>
</th>
<th class="cellrowborder" valign="top" width="32.22%" id="mcps1.2.6.1.4"><p id="p12899228145720"><a name="p12899228145720"></a><a name="p12899228145720"></a><strong id="b533767601"><a name="b533767601"></a><a name="b533767601"></a>Hardware Specifications</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.520000000000003%" id="mcps1.2.6.1.5"><p id="p790513286570"><a name="p790513286570"></a><a name="p790513286570"></a><strong id="b14994287161135"><a name="b14994287161135"></a><a name="b14994287161135"></a>Number of vCPUs</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1890762818577"><td class="cellrowborder" valign="top" width="16.37%" headers="mcps1.2.6.1.1 "><p id="p591242805713"><a name="p591242805713"></a><a name="p591242805713"></a>s2</p>
</td>
<td class="cellrowborder" valign="top" width="16.45%" headers="mcps1.2.6.1.2 "><p id="p491714281574"><a name="p491714281574"></a><a name="p491714281574"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="18.44%" headers="mcps1.2.6.1.3 "><p id="p992214283572"><a name="p992214283572"></a><a name="p992214283572"></a>22</p>
</td>
<td class="cellrowborder" valign="top" width="32.22%" headers="mcps1.2.6.1.4 "><a name="ul2092620285571"></a><a name="ul2092620285571"></a><ul id="ul2092620285571"><li>CPU: Intel&reg; Xeon&reg; Processor Gold 6161 (30.25 MB Cache, 2.20 GHz)</li><li>Memory: 704 GB (or 720,896 MB)</li></ul>
</td>
<td class="cellrowborder" valign="top" width="16.520000000000003%" headers="mcps1.2.6.1.5 "><p id="p1959152875715"><a name="p1959152875715"></a><a name="p1959152875715"></a>144</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Flavors of s2-medium DeHs

<a name="table78931175110"></a>
<table><thead align="left"><tr id="row18119111125112"><th class="cellrowborder" valign="top" width="15.998400159984%" id="mcps1.2.6.1.1"><p id="p412413115114"><a name="p412413115114"></a><a name="p412413115114"></a><strong id="b63891932152511"><a name="b63891932152511"></a><a name="b63891932152511"></a>Flavor Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.018298170182977%" id="mcps1.2.6.1.2"><p id="p112817195115"><a name="p112817195115"></a><a name="p112817195115"></a><strong id="b1227877612"><a name="b1227877612"></a><a name="b1227877612"></a>Number of Sockets</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.948205179482045%" id="mcps1.2.6.1.3"><p id="p1013251115119"><a name="p1013251115119"></a><a name="p1013251115119"></a><strong id="b787465510"><a name="b787465510"></a><a name="b787465510"></a>Number of Cores per Socket</strong></p>
</th>
<th class="cellrowborder" valign="top" width="32.3967603239676%" id="mcps1.2.6.1.4"><p id="p31382114519"><a name="p31382114519"></a><a name="p31382114519"></a><strong id="b404947772"><a name="b404947772"></a><a name="b404947772"></a>Hardware Specifications</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.638336166383358%" id="mcps1.2.6.1.5"><p id="p1614414195115"><a name="p1614414195115"></a><a name="p1614414195115"></a><strong id="b842352706162739"><a name="b842352706162739"></a><a name="b842352706162739"></a>Number of vCPUs</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row414918195118"><td class="cellrowborder" valign="top" width="15.998400159984%" headers="mcps1.2.6.1.1 "><p id="p7152121185115"><a name="p7152121185115"></a><a name="p7152121185115"></a>s2-medium</p>
</td>
<td class="cellrowborder" valign="top" width="17.018298170182977%" headers="mcps1.2.6.1.2 "><p id="p1415710118516"><a name="p1415710118516"></a><a name="p1415710118516"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="17.948205179482045%" headers="mcps1.2.6.1.3 "><p id="p1016210105113"><a name="p1016210105113"></a><a name="p1016210105113"></a>12</p>
</td>
<td class="cellrowborder" valign="top" width="32.3967603239676%" headers="mcps1.2.6.1.4 "><a name="ul17168141165116"></a><a name="ul17168141165116"></a><ul id="ul17168141165116"><li>CPU: Intel&reg; Xeon&reg; Processor Gold 5118 (16.5 MB L3 Cache, 2.30 GHz)</li><li>Memory: 328 GB (or 335,872 MB)</li></ul>
</td>
<td class="cellrowborder" valign="top" width="16.638336166383358%" headers="mcps1.2.6.1.5 "><p id="p41831195114"><a name="p41831195114"></a><a name="p41831195114"></a>72</p>
</td>
</tr>
</tbody>
</table>

## Flavors of Placeable ECSs<a name="section929425823817"></a>

**Table  4**  ECS flavors supported by general DeHs

<a name="table24864505285"></a>
<table><thead align="left"><tr id="row84963505289"><th class="cellrowborder" valign="top" width="30.259999999999998%" id="mcps1.2.4.1.1"><p id="p150285016288"><a name="p150285016288"></a><a name="p150285016288"></a><strong id="b128981937205316"><a name="b128981937205316"></a><a name="b128981937205316"></a>ECS Flavor</strong></p>
</th>
<th class="cellrowborder" valign="top" width="29.89%" id="mcps1.2.4.1.2"><p id="p1450625011285"><a name="p1450625011285"></a><a name="p1450625011285"></a><strong id="b1222908171"><a name="b1222908171"></a><a name="b1222908171"></a>vCPUs</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.85%" id="mcps1.2.4.1.3"><p id="p250812509281"><a name="p250812509281"></a><a name="p250812509281"></a><strong id="b143801584"><a name="b143801584"></a><a name="b143801584"></a>Memory (RAM in GB)</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1510105011288"><td class="cellrowborder" valign="top" width="30.259999999999998%" headers="mcps1.2.4.1.1 "><p id="p1551465011280"><a name="p1551465011280"></a><a name="p1551465011280"></a>s1.medium</p>
</td>
<td class="cellrowborder" valign="top" width="29.89%" headers="mcps1.2.4.1.2 "><p id="p1351612509288"><a name="p1351612509288"></a><a name="p1351612509288"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="39.85%" headers="mcps1.2.4.1.3 "><p id="p7522195062815"><a name="p7522195062815"></a><a name="p7522195062815"></a>4</p>
</td>
</tr>
<tr id="row4523195022816"><td class="cellrowborder" valign="top" width="30.259999999999998%" headers="mcps1.2.4.1.1 "><p id="p125261150152818"><a name="p125261150152818"></a><a name="p125261150152818"></a>s1.large</p>
</td>
<td class="cellrowborder" valign="top" width="29.89%" headers="mcps1.2.4.1.2 "><p id="p12528185052815"><a name="p12528185052815"></a><a name="p12528185052815"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="39.85%" headers="mcps1.2.4.1.3 "><p id="p653175020283"><a name="p653175020283"></a><a name="p653175020283"></a>8</p>
</td>
</tr>
<tr id="row195321050192819"><td class="cellrowborder" valign="top" width="30.259999999999998%" headers="mcps1.2.4.1.1 "><p id="p17534195012281"><a name="p17534195012281"></a><a name="p17534195012281"></a>s1.xlarge</p>
</td>
<td class="cellrowborder" valign="top" width="29.89%" headers="mcps1.2.4.1.2 "><p id="p165373506281"><a name="p165373506281"></a><a name="p165373506281"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="39.85%" headers="mcps1.2.4.1.3 "><p id="p5539145011284"><a name="p5539145011284"></a><a name="p5539145011284"></a>16</p>
</td>
</tr>
<tr id="row13541185012280"><td class="cellrowborder" valign="top" width="30.259999999999998%" headers="mcps1.2.4.1.1 "><p id="p75431350142814"><a name="p75431350142814"></a><a name="p75431350142814"></a>s1.2xlarge</p>
</td>
<td class="cellrowborder" valign="top" width="29.89%" headers="mcps1.2.4.1.2 "><p id="p20545450182818"><a name="p20545450182818"></a><a name="p20545450182818"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="39.85%" headers="mcps1.2.4.1.3 "><p id="p11549050152817"><a name="p11549050152817"></a><a name="p11549050152817"></a>32</p>
</td>
</tr>
<tr id="row1455045010286"><td class="cellrowborder" valign="top" width="30.259999999999998%" headers="mcps1.2.4.1.1 "><p id="p165532505286"><a name="p165532505286"></a><a name="p165532505286"></a>s1.4xlarge</p>
</td>
<td class="cellrowborder" valign="top" width="29.89%" headers="mcps1.2.4.1.2 "><p id="p6555115012814"><a name="p6555115012814"></a><a name="p6555115012814"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="39.85%" headers="mcps1.2.4.1.3 "><p id="p5558125017285"><a name="p5558125017285"></a><a name="p5558125017285"></a>64</p>
</td>
</tr>
<tr id="row9559150192811"><td class="cellrowborder" valign="top" width="30.259999999999998%" headers="mcps1.2.4.1.1 "><p id="p65601450192815"><a name="p65601450192815"></a><a name="p65601450192815"></a>s1.8xlarge</p>
</td>
<td class="cellrowborder" valign="top" width="29.89%" headers="mcps1.2.4.1.2 "><p id="p1056365020282"><a name="p1056365020282"></a><a name="p1056365020282"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="39.85%" headers="mcps1.2.4.1.3 "><p id="p17565950162819"><a name="p17565950162819"></a><a name="p17565950162819"></a>128</p>
</td>
</tr>
<tr id="row55662050182817"><td class="cellrowborder" valign="top" width="30.259999999999998%" headers="mcps1.2.4.1.1 "><p id="p13570050182810"><a name="p13570050182810"></a><a name="p13570050182810"></a>c1.medium</p>
</td>
<td class="cellrowborder" valign="top" width="29.89%" headers="mcps1.2.4.1.2 "><p id="p1857375042813"><a name="p1857375042813"></a><a name="p1857375042813"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="39.85%" headers="mcps1.2.4.1.3 "><p id="p6576350202813"><a name="p6576350202813"></a><a name="p6576350202813"></a>1</p>
</td>
</tr>
<tr id="row75773504281"><td class="cellrowborder" valign="top" width="30.259999999999998%" headers="mcps1.2.4.1.1 "><p id="p12581125022820"><a name="p12581125022820"></a><a name="p12581125022820"></a>c1.large</p>
</td>
<td class="cellrowborder" valign="top" width="29.89%" headers="mcps1.2.4.1.2 "><p id="p9584850132816"><a name="p9584850132816"></a><a name="p9584850132816"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="39.85%" headers="mcps1.2.4.1.3 "><p id="p1358610509286"><a name="p1358610509286"></a><a name="p1358610509286"></a>2</p>
</td>
</tr>
<tr id="row1858865018280"><td class="cellrowborder" valign="top" width="30.259999999999998%" headers="mcps1.2.4.1.1 "><p id="p1659016507281"><a name="p1659016507281"></a><a name="p1659016507281"></a>c1.xlarge</p>
</td>
<td class="cellrowborder" valign="top" width="29.89%" headers="mcps1.2.4.1.2 "><p id="p1759185032813"><a name="p1759185032813"></a><a name="p1759185032813"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="39.85%" headers="mcps1.2.4.1.3 "><p id="p4596650162811"><a name="p4596650162811"></a><a name="p4596650162811"></a>4</p>
</td>
</tr>
<tr id="row859685032819"><td class="cellrowborder" valign="top" width="30.259999999999998%" headers="mcps1.2.4.1.1 "><p id="p7598185022819"><a name="p7598185022819"></a><a name="p7598185022819"></a>c1.2xlarge</p>
</td>
<td class="cellrowborder" valign="top" width="29.89%" headers="mcps1.2.4.1.2 "><p id="p760155032819"><a name="p760155032819"></a><a name="p760155032819"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="39.85%" headers="mcps1.2.4.1.3 "><p id="p13604135012817"><a name="p13604135012817"></a><a name="p13604135012817"></a>8</p>
</td>
</tr>
<tr id="row12604175016281"><td class="cellrowborder" valign="top" width="30.259999999999998%" headers="mcps1.2.4.1.1 "><p id="p260815013286"><a name="p260815013286"></a><a name="p260815013286"></a>c1.4xlarge</p>
</td>
<td class="cellrowborder" valign="top" width="29.89%" headers="mcps1.2.4.1.2 "><p id="p1061065014285"><a name="p1061065014285"></a><a name="p1061065014285"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="39.85%" headers="mcps1.2.4.1.3 "><p id="p8612195042813"><a name="p8612195042813"></a><a name="p8612195042813"></a>16</p>
</td>
</tr>
<tr id="row146141050162810"><td class="cellrowborder" valign="top" width="30.259999999999998%" headers="mcps1.2.4.1.1 "><p id="p18616750112820"><a name="p18616750112820"></a><a name="p18616750112820"></a>c1.8xlarge</p>
</td>
<td class="cellrowborder" valign="top" width="29.89%" headers="mcps1.2.4.1.2 "><p id="p1461817506286"><a name="p1461817506286"></a><a name="p1461817506286"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="39.85%" headers="mcps1.2.4.1.3 "><p id="p106206502284"><a name="p106206502284"></a><a name="p106206502284"></a>32</p>
</td>
</tr>
<tr id="row462219502282"><td class="cellrowborder" valign="top" width="30.259999999999998%" headers="mcps1.2.4.1.1 "><p id="p1762615508286"><a name="p1762615508286"></a><a name="p1762615508286"></a>c2.medium</p>
</td>
<td class="cellrowborder" valign="top" width="29.89%" headers="mcps1.2.4.1.2 "><p id="p76281650112813"><a name="p76281650112813"></a><a name="p76281650112813"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="39.85%" headers="mcps1.2.4.1.3 "><p id="p1763065015285"><a name="p1763065015285"></a><a name="p1763065015285"></a>2</p>
</td>
</tr>
<tr id="row126321750102815"><td class="cellrowborder" valign="top" width="30.259999999999998%" headers="mcps1.2.4.1.1 "><p id="p1963613503285"><a name="p1963613503285"></a><a name="p1963613503285"></a>c2.large</p>
</td>
<td class="cellrowborder" valign="top" width="29.89%" headers="mcps1.2.4.1.2 "><p id="p12637195012285"><a name="p12637195012285"></a><a name="p12637195012285"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="39.85%" headers="mcps1.2.4.1.3 "><p id="p2640185010284"><a name="p2640185010284"></a><a name="p2640185010284"></a>4</p>
</td>
</tr>
<tr id="row1364155032816"><td class="cellrowborder" valign="top" width="30.259999999999998%" headers="mcps1.2.4.1.1 "><p id="p9643115022818"><a name="p9643115022818"></a><a name="p9643115022818"></a>c2.xlarge</p>
</td>
<td class="cellrowborder" valign="top" width="29.89%" headers="mcps1.2.4.1.2 "><p id="p464555092811"><a name="p464555092811"></a><a name="p464555092811"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="39.85%" headers="mcps1.2.4.1.3 "><p id="p10647205016285"><a name="p10647205016285"></a><a name="p10647205016285"></a>8</p>
</td>
</tr>
<tr id="row16648105014285"><td class="cellrowborder" valign="top" width="30.259999999999998%" headers="mcps1.2.4.1.1 "><p id="p96511450122814"><a name="p96511450122814"></a><a name="p96511450122814"></a>c2.2xlarge</p>
</td>
<td class="cellrowborder" valign="top" width="29.89%" headers="mcps1.2.4.1.2 "><p id="p1465145012812"><a name="p1465145012812"></a><a name="p1465145012812"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="39.85%" headers="mcps1.2.4.1.3 "><p id="p156543501285"><a name="p156543501285"></a><a name="p156543501285"></a>16</p>
</td>
</tr>
<tr id="row13654105017289"><td class="cellrowborder" valign="top" width="30.259999999999998%" headers="mcps1.2.4.1.1 "><p id="p1765755082813"><a name="p1765755082813"></a><a name="p1765755082813"></a>c2.4xlarge</p>
</td>
<td class="cellrowborder" valign="top" width="29.89%" headers="mcps1.2.4.1.2 "><p id="p20659165018285"><a name="p20659165018285"></a><a name="p20659165018285"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="39.85%" headers="mcps1.2.4.1.3 "><p id="p1866120509288"><a name="p1866120509288"></a><a name="p1866120509288"></a>32</p>
</td>
</tr>
<tr id="row866365022815"><td class="cellrowborder" valign="top" width="30.259999999999998%" headers="mcps1.2.4.1.1 "><p id="p866755013285"><a name="p866755013285"></a><a name="p866755013285"></a>c2.8xlarge</p>
</td>
<td class="cellrowborder" valign="top" width="29.89%" headers="mcps1.2.4.1.2 "><p id="p10669145042819"><a name="p10669145042819"></a><a name="p10669145042819"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="39.85%" headers="mcps1.2.4.1.3 "><p id="p1967125052813"><a name="p1967125052813"></a><a name="p1967125052813"></a>64</p>
</td>
</tr>
<tr id="row1767305013280"><td class="cellrowborder" valign="top" width="30.259999999999998%" headers="mcps1.2.4.1.1 "><p id="p9677145032814"><a name="p9677145032814"></a><a name="p9677145032814"></a>m1.medium</p>
</td>
<td class="cellrowborder" valign="top" width="29.89%" headers="mcps1.2.4.1.2 "><p id="p136791450192810"><a name="p136791450192810"></a><a name="p136791450192810"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="39.85%" headers="mcps1.2.4.1.3 "><p id="p4683155092819"><a name="p4683155092819"></a><a name="p4683155092819"></a>8</p>
</td>
</tr>
<tr id="row18684175052818"><td class="cellrowborder" valign="top" width="30.259999999999998%" headers="mcps1.2.4.1.1 "><p id="p5686175020281"><a name="p5686175020281"></a><a name="p5686175020281"></a>m1.large</p>
</td>
<td class="cellrowborder" valign="top" width="29.89%" headers="mcps1.2.4.1.2 "><p id="p1868805012810"><a name="p1868805012810"></a><a name="p1868805012810"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="39.85%" headers="mcps1.2.4.1.3 "><p id="p196931450132817"><a name="p196931450132817"></a><a name="p196931450132817"></a>16</p>
</td>
</tr>
<tr id="row4693185072816"><td class="cellrowborder" valign="top" width="30.259999999999998%" headers="mcps1.2.4.1.1 "><p id="p176959508282"><a name="p176959508282"></a><a name="p176959508282"></a>m1.xlarge</p>
</td>
<td class="cellrowborder" valign="top" width="29.89%" headers="mcps1.2.4.1.2 "><p id="p18697550132813"><a name="p18697550132813"></a><a name="p18697550132813"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="39.85%" headers="mcps1.2.4.1.3 "><p id="p769955017282"><a name="p769955017282"></a><a name="p769955017282"></a>32</p>
</td>
</tr>
<tr id="row14700145019287"><td class="cellrowborder" valign="top" width="30.259999999999998%" headers="mcps1.2.4.1.1 "><p id="p87031350142813"><a name="p87031350142813"></a><a name="p87031350142813"></a>m1.2xlarge</p>
</td>
<td class="cellrowborder" valign="top" width="29.89%" headers="mcps1.2.4.1.2 "><p id="p3705750172815"><a name="p3705750172815"></a><a name="p3705750172815"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="39.85%" headers="mcps1.2.4.1.3 "><p id="p670795022814"><a name="p670795022814"></a><a name="p670795022814"></a>64</p>
</td>
</tr>
<tr id="row1670825092811"><td class="cellrowborder" valign="top" width="30.259999999999998%" headers="mcps1.2.4.1.1 "><p id="p8711105032817"><a name="p8711105032817"></a><a name="p8711105032817"></a>m1.4xlarge</p>
</td>
<td class="cellrowborder" valign="top" width="29.89%" headers="mcps1.2.4.1.2 "><p id="p1071325022817"><a name="p1071325022817"></a><a name="p1071325022817"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="39.85%" headers="mcps1.2.4.1.3 "><p id="p671514506281"><a name="p671514506281"></a><a name="p671514506281"></a>128</p>
</td>
</tr>
</tbody>
</table>

**Table  5**  ECS flavors supported by s2 DeHs

<a name="table14107132793212"></a>
<table><thead align="left"><tr id="row1410920274329"><th class="cellrowborder" valign="top" width="30.769999999999996%" id="mcps1.2.4.1.1"><p id="p9559153919331"><a name="p9559153919331"></a><a name="p9559153919331"></a><strong id="b17931753145318"><a name="b17931753145318"></a><a name="b17931753145318"></a>ECS Flavor</strong></p>
</th>
<th class="cellrowborder" valign="top" width="29.49%" id="mcps1.2.4.1.2"><p id="p75612039183315"><a name="p75612039183315"></a><a name="p75612039183315"></a><strong id="b1010023887"><a name="b1010023887"></a><a name="b1010023887"></a>vCPUs</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.739999999999995%" id="mcps1.2.4.1.3"><p id="p55643394332"><a name="p55643394332"></a><a name="p55643394332"></a><strong id="b1024613352340"><a name="b1024613352340"></a><a name="b1024613352340"></a>Memory (RAM in GB)</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row710952715326"><td class="cellrowborder" valign="top" width="30.769999999999996%" headers="mcps1.2.4.1.1 "><p id="p498452871959"><a name="p498452871959"></a><a name="p498452871959"></a>s2.medium.1</p>
</td>
<td class="cellrowborder" valign="top" width="29.49%" headers="mcps1.2.4.1.2 "><p id="p533387381959"><a name="p533387381959"></a><a name="p533387381959"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="39.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p254705081959"><a name="p254705081959"></a><a name="p254705081959"></a>1</p>
</td>
</tr>
<tr id="row141091527163217"><td class="cellrowborder" valign="top" width="30.769999999999996%" headers="mcps1.2.4.1.1 "><p id="p23580101959"><a name="p23580101959"></a><a name="p23580101959"></a>s2.large.1</p>
</td>
<td class="cellrowborder" valign="top" width="29.49%" headers="mcps1.2.4.1.2 "><p id="p538326941959"><a name="p538326941959"></a><a name="p538326941959"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="39.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p654809661959"><a name="p654809661959"></a><a name="p654809661959"></a>2</p>
</td>
</tr>
<tr id="row14109182703216"><td class="cellrowborder" valign="top" width="30.769999999999996%" headers="mcps1.2.4.1.1 "><p id="p553968881959"><a name="p553968881959"></a><a name="p553968881959"></a>s2.xlarge.1</p>
</td>
<td class="cellrowborder" valign="top" width="29.49%" headers="mcps1.2.4.1.2 "><p id="p543726571959"><a name="p543726571959"></a><a name="p543726571959"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="39.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p421091361959"><a name="p421091361959"></a><a name="p421091361959"></a>4</p>
</td>
</tr>
<tr id="row1416303503715"><td class="cellrowborder" valign="top" width="30.769999999999996%" headers="mcps1.2.4.1.1 "><p id="p513975701959"><a name="p513975701959"></a><a name="p513975701959"></a>s2.2xlarge.1</p>
</td>
<td class="cellrowborder" valign="top" width="29.49%" headers="mcps1.2.4.1.2 "><p id="p434992051959"><a name="p434992051959"></a><a name="p434992051959"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="39.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p337747171959"><a name="p337747171959"></a><a name="p337747171959"></a>8</p>
</td>
</tr>
<tr id="row17163143512372"><td class="cellrowborder" valign="top" width="30.769999999999996%" headers="mcps1.2.4.1.1 "><p id="p286467851959"><a name="p286467851959"></a><a name="p286467851959"></a>s2.4xlarge.1</p>
</td>
<td class="cellrowborder" valign="top" width="29.49%" headers="mcps1.2.4.1.2 "><p id="p438639621959"><a name="p438639621959"></a><a name="p438639621959"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="39.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p633200051959"><a name="p633200051959"></a><a name="p633200051959"></a>16</p>
</td>
</tr>
<tr id="row161631835133711"><td class="cellrowborder" valign="top" width="30.769999999999996%" headers="mcps1.2.4.1.1 "><p id="p412027901959"><a name="p412027901959"></a><a name="p412027901959"></a>s2.8xlarge.1</p>
</td>
<td class="cellrowborder" valign="top" width="29.49%" headers="mcps1.2.4.1.2 "><p id="p180083521959"><a name="p180083521959"></a><a name="p180083521959"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="39.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p493904411959"><a name="p493904411959"></a><a name="p493904411959"></a>32</p>
</td>
</tr>
<tr id="row13785194143712"><td class="cellrowborder" valign="top" width="30.769999999999996%" headers="mcps1.2.4.1.1 "><p id="p212140271959"><a name="p212140271959"></a><a name="p212140271959"></a>s2.medium.2</p>
</td>
<td class="cellrowborder" valign="top" width="29.49%" headers="mcps1.2.4.1.2 "><p id="p188338101959"><a name="p188338101959"></a><a name="p188338101959"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="39.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p491436661959"><a name="p491436661959"></a><a name="p491436661959"></a>2</p>
</td>
</tr>
<tr id="row1778594173714"><td class="cellrowborder" valign="top" width="30.769999999999996%" headers="mcps1.2.4.1.1 "><p id="p65012455191342"><a name="p65012455191342"></a><a name="p65012455191342"></a>s2.large.2</p>
</td>
<td class="cellrowborder" valign="top" width="29.49%" headers="mcps1.2.4.1.2 "><p id="p21909021191342"><a name="p21909021191342"></a><a name="p21909021191342"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="39.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p29800280191342"><a name="p29800280191342"></a><a name="p29800280191342"></a>4</p>
</td>
</tr>
<tr id="row207851041143718"><td class="cellrowborder" valign="top" width="30.769999999999996%" headers="mcps1.2.4.1.1 "><p id="p61101725191342"><a name="p61101725191342"></a><a name="p61101725191342"></a>s2.xlarge.2</p>
</td>
<td class="cellrowborder" valign="top" width="29.49%" headers="mcps1.2.4.1.2 "><p id="p28362577191342"><a name="p28362577191342"></a><a name="p28362577191342"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="39.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p15667423191342"><a name="p15667423191342"></a><a name="p15667423191342"></a>8</p>
</td>
</tr>
<tr id="row107861641153710"><td class="cellrowborder" valign="top" width="30.769999999999996%" headers="mcps1.2.4.1.1 "><p id="p38649248191342"><a name="p38649248191342"></a><a name="p38649248191342"></a>s2.2xlarge.2</p>
</td>
<td class="cellrowborder" valign="top" width="29.49%" headers="mcps1.2.4.1.2 "><p id="p16473696191342"><a name="p16473696191342"></a><a name="p16473696191342"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="39.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p59300970191342"><a name="p59300970191342"></a><a name="p59300970191342"></a>16</p>
</td>
</tr>
<tr id="row1978674114374"><td class="cellrowborder" valign="top" width="30.769999999999996%" headers="mcps1.2.4.1.1 "><p id="p46027169191342"><a name="p46027169191342"></a><a name="p46027169191342"></a>s2.4xlarge.2</p>
</td>
<td class="cellrowborder" valign="top" width="29.49%" headers="mcps1.2.4.1.2 "><p id="p63218839191342"><a name="p63218839191342"></a><a name="p63218839191342"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="39.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p20452344191342"><a name="p20452344191342"></a><a name="p20452344191342"></a>32</p>
</td>
</tr>
<tr id="row727614715376"><td class="cellrowborder" valign="top" width="30.769999999999996%" headers="mcps1.2.4.1.1 "><p id="p28040663191342"><a name="p28040663191342"></a><a name="p28040663191342"></a>s2.8xlarge.2</p>
</td>
<td class="cellrowborder" valign="top" width="29.49%" headers="mcps1.2.4.1.2 "><p id="p58245071191342"><a name="p58245071191342"></a><a name="p58245071191342"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="39.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p20230288191342"><a name="p20230288191342"></a><a name="p20230288191342"></a>64</p>
</td>
</tr>
<tr id="row22760474371"><td class="cellrowborder" valign="top" width="30.769999999999996%" headers="mcps1.2.4.1.1 "><p id="p55891870192010"><a name="p55891870192010"></a><a name="p55891870192010"></a>s2.medium.4</p>
</td>
<td class="cellrowborder" valign="top" width="29.49%" headers="mcps1.2.4.1.2 "><p id="p21679653191342"><a name="p21679653191342"></a><a name="p21679653191342"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="39.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p11221506191342"><a name="p11221506191342"></a><a name="p11221506191342"></a>4</p>
</td>
</tr>
<tr id="row1627612475378"><td class="cellrowborder" valign="top" width="30.769999999999996%" headers="mcps1.2.4.1.1 "><p id="p10093170192010"><a name="p10093170192010"></a><a name="p10093170192010"></a>s2.large.4</p>
</td>
<td class="cellrowborder" valign="top" width="29.49%" headers="mcps1.2.4.1.2 "><p id="p3337154191342"><a name="p3337154191342"></a><a name="p3337154191342"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="39.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p1874083191342"><a name="p1874083191342"></a><a name="p1874083191342"></a>8</p>
</td>
</tr>
<tr id="row202761247103718"><td class="cellrowborder" valign="top" width="30.769999999999996%" headers="mcps1.2.4.1.1 "><p id="p43055268192010"><a name="p43055268192010"></a><a name="p43055268192010"></a>s2.xlarge.4</p>
</td>
<td class="cellrowborder" valign="top" width="29.49%" headers="mcps1.2.4.1.2 "><p id="p51199203191425"><a name="p51199203191425"></a><a name="p51199203191425"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="39.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p53494782191425"><a name="p53494782191425"></a><a name="p53494782191425"></a>16</p>
</td>
</tr>
<tr id="row6276144718372"><td class="cellrowborder" valign="top" width="30.769999999999996%" headers="mcps1.2.4.1.1 "><p id="p47450885192010"><a name="p47450885192010"></a><a name="p47450885192010"></a>s2.2xlarge.4</p>
</td>
<td class="cellrowborder" valign="top" width="29.49%" headers="mcps1.2.4.1.2 "><p id="p43001319191425"><a name="p43001319191425"></a><a name="p43001319191425"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="39.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p60554837191425"><a name="p60554837191425"></a><a name="p60554837191425"></a>32</p>
</td>
</tr>
<tr id="row15277104713379"><td class="cellrowborder" valign="top" width="30.769999999999996%" headers="mcps1.2.4.1.1 "><p id="p30630513192010"><a name="p30630513192010"></a><a name="p30630513192010"></a>s2.4xlarge.4</p>
</td>
<td class="cellrowborder" valign="top" width="29.49%" headers="mcps1.2.4.1.2 "><p id="p37649990191425"><a name="p37649990191425"></a><a name="p37649990191425"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="39.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p29750320191425"><a name="p29750320191425"></a><a name="p29750320191425"></a>64</p>
</td>
</tr>
<tr id="row1327794763715"><td class="cellrowborder" valign="top" width="30.769999999999996%" headers="mcps1.2.4.1.1 "><p id="p49501836192010"><a name="p49501836192010"></a><a name="p49501836192010"></a>s2.8xlarge.4</p>
</td>
<td class="cellrowborder" valign="top" width="29.49%" headers="mcps1.2.4.1.2 "><p id="p3001165191425"><a name="p3001165191425"></a><a name="p3001165191425"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="39.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p41767822191425"><a name="p41767822191425"></a><a name="p41767822191425"></a>128</p>
</td>
</tr>
<tr id="row1527734720372"><td class="cellrowborder" valign="top" width="30.769999999999996%" headers="mcps1.2.4.1.1 "><p id="p5272342192036"><a name="p5272342192036"></a><a name="p5272342192036"></a>s2.medium.8</p>
</td>
<td class="cellrowborder" valign="top" width="29.49%" headers="mcps1.2.4.1.2 "><p id="p362197191425"><a name="p362197191425"></a><a name="p362197191425"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="39.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p29337974191425"><a name="p29337974191425"></a><a name="p29337974191425"></a>8</p>
</td>
</tr>
<tr id="row13277194718373"><td class="cellrowborder" valign="top" width="30.769999999999996%" headers="mcps1.2.4.1.1 "><p id="p18332561192036"><a name="p18332561192036"></a><a name="p18332561192036"></a>s2.large.8</p>
</td>
<td class="cellrowborder" valign="top" width="29.49%" headers="mcps1.2.4.1.2 "><p id="p40731387191425"><a name="p40731387191425"></a><a name="p40731387191425"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="39.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p10908088191425"><a name="p10908088191425"></a><a name="p10908088191425"></a>16</p>
</td>
</tr>
<tr id="row1327724715373"><td class="cellrowborder" valign="top" width="30.769999999999996%" headers="mcps1.2.4.1.1 "><p id="p9773193192036"><a name="p9773193192036"></a><a name="p9773193192036"></a>s2.xlarge.8</p>
</td>
<td class="cellrowborder" valign="top" width="29.49%" headers="mcps1.2.4.1.2 "><p id="p10547176191425"><a name="p10547176191425"></a><a name="p10547176191425"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="39.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p49014953191425"><a name="p49014953191425"></a><a name="p49014953191425"></a>32</p>
</td>
</tr>
<tr id="row4277144713717"><td class="cellrowborder" valign="top" width="30.769999999999996%" headers="mcps1.2.4.1.1 "><p id="p11118763192036"><a name="p11118763192036"></a><a name="p11118763192036"></a>s2.2xlarge.8</p>
</td>
<td class="cellrowborder" valign="top" width="29.49%" headers="mcps1.2.4.1.2 "><p id="p33747850191425"><a name="p33747850191425"></a><a name="p33747850191425"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="39.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p49221354191425"><a name="p49221354191425"></a><a name="p49221354191425"></a>64</p>
</td>
</tr>
<tr id="row7786114119375"><td class="cellrowborder" valign="top" width="30.769999999999996%" headers="mcps1.2.4.1.1 "><p id="p52515049192036"><a name="p52515049192036"></a><a name="p52515049192036"></a>s2.4xlarge.8</p>
</td>
<td class="cellrowborder" valign="top" width="29.49%" headers="mcps1.2.4.1.2 "><p id="p10109784191425"><a name="p10109784191425"></a><a name="p10109784191425"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="39.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p13586209191425"><a name="p13586209191425"></a><a name="p13586209191425"></a>128</p>
</td>
</tr>
<tr id="row1109112711321"><td class="cellrowborder" valign="top" width="30.769999999999996%" headers="mcps1.2.4.1.1 "><p id="p31418686192036"><a name="p31418686192036"></a><a name="p31418686192036"></a>s2.8xlarge.8</p>
</td>
<td class="cellrowborder" valign="top" width="29.49%" headers="mcps1.2.4.1.2 "><p id="p10334226191425"><a name="p10334226191425"></a><a name="p10334226191425"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="39.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p31765949191425"><a name="p31765949191425"></a><a name="p31765949191425"></a>256</p>
</td>
</tr>
</tbody>
</table>

**Table  6**  ECS flavors supported by s2-medium DeHs

<a name="table13395161879"></a>
<table><thead align="left"><tr id="row134131011379"><th class="cellrowborder" valign="top" width="30.769999999999996%" id="mcps1.2.4.1.1"><p id="p174261312079"><a name="p174261312079"></a><a name="p174261312079"></a><strong id="b95559817548"><a name="b95559817548"></a><a name="b95559817548"></a>ECS Flavor</strong></p>
</th>
<th class="cellrowborder" valign="top" width="29.49%" id="mcps1.2.4.1.2"><p id="p1843571678"><a name="p1843571678"></a><a name="p1843571678"></a><strong id="b1520999854"><a name="b1520999854"></a><a name="b1520999854"></a>vCPUs</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.739999999999995%" id="mcps1.2.4.1.3"><p id="p6441815715"><a name="p6441815715"></a><a name="p6441815715"></a><strong id="b1545125816340"><a name="b1545125816340"></a><a name="b1545125816340"></a>Memory (RAM in GB)</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row344681575"><td class="cellrowborder" valign="top" width="30.769999999999996%" headers="mcps1.2.4.1.1 "><p id="p24531016712"><a name="p24531016712"></a><a name="p24531016712"></a>s2.medium.1</p>
</td>
<td class="cellrowborder" valign="top" width="29.49%" headers="mcps1.2.4.1.2 "><p id="p6460511878"><a name="p6460511878"></a><a name="p6460511878"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="39.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p19467171079"><a name="p19467171079"></a><a name="p19467171079"></a>1</p>
</td>
</tr>
<tr id="row1947114119715"><td class="cellrowborder" valign="top" width="30.769999999999996%" headers="mcps1.2.4.1.1 "><p id="p6478311777"><a name="p6478311777"></a><a name="p6478311777"></a>s2.large.1</p>
</td>
<td class="cellrowborder" valign="top" width="29.49%" headers="mcps1.2.4.1.2 "><p id="p174831811879"><a name="p174831811879"></a><a name="p174831811879"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="39.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p1649120117714"><a name="p1649120117714"></a><a name="p1649120117714"></a>2</p>
</td>
</tr>
<tr id="row549371274"><td class="cellrowborder" valign="top" width="30.769999999999996%" headers="mcps1.2.4.1.1 "><p id="p104991911174"><a name="p104991911174"></a><a name="p104991911174"></a>s2.xlarge.1</p>
</td>
<td class="cellrowborder" valign="top" width="29.49%" headers="mcps1.2.4.1.2 "><p id="p1350612112716"><a name="p1350612112716"></a><a name="p1350612112716"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="39.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p1551221678"><a name="p1551221678"></a><a name="p1551221678"></a>4</p>
</td>
</tr>
<tr id="row7515517717"><td class="cellrowborder" valign="top" width="30.769999999999996%" headers="mcps1.2.4.1.1 "><p id="p1252311574"><a name="p1252311574"></a><a name="p1252311574"></a>s2.2xlarge.1</p>
</td>
<td class="cellrowborder" valign="top" width="29.49%" headers="mcps1.2.4.1.2 "><p id="p11530111179"><a name="p11530111179"></a><a name="p11530111179"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="39.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p553715117713"><a name="p553715117713"></a><a name="p553715117713"></a>8</p>
</td>
</tr>
<tr id="row75381212714"><td class="cellrowborder" valign="top" width="30.769999999999996%" headers="mcps1.2.4.1.1 "><p id="p195494112720"><a name="p195494112720"></a><a name="p195494112720"></a>s2.4xlarge.1</p>
</td>
<td class="cellrowborder" valign="top" width="29.49%" headers="mcps1.2.4.1.2 "><p id="p755514119719"><a name="p755514119719"></a><a name="p755514119719"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="39.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p2561161974"><a name="p2561161974"></a><a name="p2561161974"></a>16</p>
</td>
</tr>
<tr id="row1856618117714"><td class="cellrowborder" valign="top" width="30.769999999999996%" headers="mcps1.2.4.1.1 "><p id="p1257371479"><a name="p1257371479"></a><a name="p1257371479"></a>s2.8xlarge.1</p>
</td>
<td class="cellrowborder" valign="top" width="29.49%" headers="mcps1.2.4.1.2 "><p id="p155791911274"><a name="p155791911274"></a><a name="p155791911274"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="39.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p658471177"><a name="p658471177"></a><a name="p658471177"></a>32</p>
</td>
</tr>
<tr id="row155871911474"><td class="cellrowborder" valign="top" width="30.769999999999996%" headers="mcps1.2.4.1.1 "><p id="p55921411277"><a name="p55921411277"></a><a name="p55921411277"></a>s2.medium.2</p>
</td>
<td class="cellrowborder" valign="top" width="29.49%" headers="mcps1.2.4.1.2 "><p id="p205981710711"><a name="p205981710711"></a><a name="p205981710711"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="39.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p56021819714"><a name="p56021819714"></a><a name="p56021819714"></a>2</p>
</td>
</tr>
<tr id="row1360510113714"><td class="cellrowborder" valign="top" width="30.769999999999996%" headers="mcps1.2.4.1.1 "><p id="p760816111713"><a name="p760816111713"></a><a name="p760816111713"></a>s2.large.2</p>
</td>
<td class="cellrowborder" valign="top" width="29.49%" headers="mcps1.2.4.1.2 "><p id="p36131716714"><a name="p36131716714"></a><a name="p36131716714"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="39.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p961819117712"><a name="p961819117712"></a><a name="p961819117712"></a>4</p>
</td>
</tr>
<tr id="row9621311712"><td class="cellrowborder" valign="top" width="30.769999999999996%" headers="mcps1.2.4.1.1 "><p id="p1162714115718"><a name="p1162714115718"></a><a name="p1162714115718"></a>s2.xlarge.2</p>
</td>
<td class="cellrowborder" valign="top" width="29.49%" headers="mcps1.2.4.1.2 "><p id="p146381413714"><a name="p146381413714"></a><a name="p146381413714"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="39.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p106422012073"><a name="p106422012073"></a><a name="p106422012073"></a>8</p>
</td>
</tr>
<tr id="row176471111272"><td class="cellrowborder" valign="top" width="30.769999999999996%" headers="mcps1.2.4.1.1 "><p id="p26491511979"><a name="p26491511979"></a><a name="p26491511979"></a>s2.2xlarge.2</p>
</td>
<td class="cellrowborder" valign="top" width="29.49%" headers="mcps1.2.4.1.2 "><p id="p136581918719"><a name="p136581918719"></a><a name="p136581918719"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="39.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p18665417719"><a name="p18665417719"></a><a name="p18665417719"></a>16</p>
</td>
</tr>
<tr id="row206685112713"><td class="cellrowborder" valign="top" width="30.769999999999996%" headers="mcps1.2.4.1.1 "><p id="p1467931372"><a name="p1467931372"></a><a name="p1467931372"></a>s2.4xlarge.2</p>
</td>
<td class="cellrowborder" valign="top" width="29.49%" headers="mcps1.2.4.1.2 "><p id="p146876113716"><a name="p146876113716"></a><a name="p146876113716"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="39.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p76941419715"><a name="p76941419715"></a><a name="p76941419715"></a>32</p>
</td>
</tr>
<tr id="row069817120714"><td class="cellrowborder" valign="top" width="30.769999999999996%" headers="mcps1.2.4.1.1 "><p id="p19702218714"><a name="p19702218714"></a><a name="p19702218714"></a>s2.8xlarge.2</p>
</td>
<td class="cellrowborder" valign="top" width="29.49%" headers="mcps1.2.4.1.2 "><p id="p16707121573"><a name="p16707121573"></a><a name="p16707121573"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="39.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p2071217117718"><a name="p2071217117718"></a><a name="p2071217117718"></a>64</p>
</td>
</tr>
<tr id="row1371614112714"><td class="cellrowborder" valign="top" width="30.769999999999996%" headers="mcps1.2.4.1.1 "><p id="p672217120716"><a name="p672217120716"></a><a name="p672217120716"></a>s2.medium.4</p>
</td>
<td class="cellrowborder" valign="top" width="29.49%" headers="mcps1.2.4.1.2 "><p id="p4728511975"><a name="p4728511975"></a><a name="p4728511975"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="39.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p7735112711"><a name="p7735112711"></a><a name="p7735112711"></a>4</p>
</td>
</tr>
<tr id="row4737812718"><td class="cellrowborder" valign="top" width="30.769999999999996%" headers="mcps1.2.4.1.1 "><p id="p7744011578"><a name="p7744011578"></a><a name="p7744011578"></a>s2.large.4</p>
</td>
<td class="cellrowborder" valign="top" width="29.49%" headers="mcps1.2.4.1.2 "><p id="p675212117715"><a name="p675212117715"></a><a name="p675212117715"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="39.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p47585118715"><a name="p47585118715"></a><a name="p47585118715"></a>8</p>
</td>
</tr>
<tr id="row11762101276"><td class="cellrowborder" valign="top" width="30.769999999999996%" headers="mcps1.2.4.1.1 "><p id="p27671115710"><a name="p27671115710"></a><a name="p27671115710"></a>s2.xlarge.4</p>
</td>
<td class="cellrowborder" valign="top" width="29.49%" headers="mcps1.2.4.1.2 "><p id="p0772319713"><a name="p0772319713"></a><a name="p0772319713"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="39.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p67791115711"><a name="p67791115711"></a><a name="p67791115711"></a>16</p>
</td>
</tr>
<tr id="row27813110712"><td class="cellrowborder" valign="top" width="30.769999999999996%" headers="mcps1.2.4.1.1 "><p id="p1878715113712"><a name="p1878715113712"></a><a name="p1878715113712"></a>s2.2xlarge.4</p>
</td>
<td class="cellrowborder" valign="top" width="29.49%" headers="mcps1.2.4.1.2 "><p id="p127921416716"><a name="p127921416716"></a><a name="p127921416716"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="39.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p1079921176"><a name="p1079921176"></a><a name="p1079921176"></a>32</p>
</td>
</tr>
<tr id="row17800121471"><td class="cellrowborder" valign="top" width="30.769999999999996%" headers="mcps1.2.4.1.1 "><p id="p280411116715"><a name="p280411116715"></a><a name="p280411116715"></a>s2.4xlarge.4</p>
</td>
<td class="cellrowborder" valign="top" width="29.49%" headers="mcps1.2.4.1.2 "><p id="p2813171876"><a name="p2813171876"></a><a name="p2813171876"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="39.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p13817911717"><a name="p13817911717"></a><a name="p13817911717"></a>64</p>
</td>
</tr>
<tr id="row1881916119717"><td class="cellrowborder" valign="top" width="30.769999999999996%" headers="mcps1.2.4.1.1 "><p id="p1982616112718"><a name="p1982616112718"></a><a name="p1982616112718"></a>s2.8xlarge.4</p>
</td>
<td class="cellrowborder" valign="top" width="29.49%" headers="mcps1.2.4.1.2 "><p id="p483261376"><a name="p483261376"></a><a name="p483261376"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="39.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p483718116713"><a name="p483718116713"></a><a name="p483718116713"></a>128</p>
</td>
</tr>
<tr id="row118385112717"><td class="cellrowborder" valign="top" width="30.769999999999996%" headers="mcps1.2.4.1.1 "><p id="p88449110711"><a name="p88449110711"></a><a name="p88449110711"></a>s2.medium.8</p>
</td>
<td class="cellrowborder" valign="top" width="29.49%" headers="mcps1.2.4.1.2 "><p id="p9852415712"><a name="p9852415712"></a><a name="p9852415712"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="39.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p178581711672"><a name="p178581711672"></a><a name="p178581711672"></a>8</p>
</td>
</tr>
<tr id="row385919113716"><td class="cellrowborder" valign="top" width="30.769999999999996%" headers="mcps1.2.4.1.1 "><p id="p1386510116711"><a name="p1386510116711"></a><a name="p1386510116711"></a>s2.large.8</p>
</td>
<td class="cellrowborder" valign="top" width="29.49%" headers="mcps1.2.4.1.2 "><p id="p19870417713"><a name="p19870417713"></a><a name="p19870417713"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="39.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p487519120710"><a name="p487519120710"></a><a name="p487519120710"></a>16</p>
</td>
</tr>
<tr id="row3877410720"><td class="cellrowborder" valign="top" width="30.769999999999996%" headers="mcps1.2.4.1.1 "><p id="p15885151374"><a name="p15885151374"></a><a name="p15885151374"></a>s2.xlarge.8</p>
</td>
<td class="cellrowborder" valign="top" width="29.49%" headers="mcps1.2.4.1.2 "><p id="p12889171776"><a name="p12889171776"></a><a name="p12889171776"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="39.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p17893101179"><a name="p17893101179"></a><a name="p17893101179"></a>32</p>
</td>
</tr>
<tr id="row28961311713"><td class="cellrowborder" valign="top" width="30.769999999999996%" headers="mcps1.2.4.1.1 "><p id="p108991411672"><a name="p108991411672"></a><a name="p108991411672"></a>s2.2xlarge.8</p>
</td>
<td class="cellrowborder" valign="top" width="29.49%" headers="mcps1.2.4.1.2 "><p id="p19059113717"><a name="p19059113717"></a><a name="p19059113717"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="39.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p179121411977"><a name="p179121411977"></a><a name="p179121411977"></a>64</p>
</td>
</tr>
<tr id="row19141812715"><td class="cellrowborder" valign="top" width="30.769999999999996%" headers="mcps1.2.4.1.1 "><p id="p79201110710"><a name="p79201110710"></a><a name="p79201110710"></a>s2.4xlarge.8</p>
</td>
<td class="cellrowborder" valign="top" width="29.49%" headers="mcps1.2.4.1.2 "><p id="p692741476"><a name="p692741476"></a><a name="p692741476"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="39.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p139351411572"><a name="p139351411572"></a><a name="p139351411572"></a>128</p>
</td>
</tr>
<tr id="row1939411278"><td class="cellrowborder" valign="top" width="30.769999999999996%" headers="mcps1.2.4.1.1 "><p id="p49441618719"><a name="p49441618719"></a><a name="p49441618719"></a>s2.8xlarge.8</p>
</td>
<td class="cellrowborder" valign="top" width="29.49%" headers="mcps1.2.4.1.2 "><p id="p49481118715"><a name="p49481118715"></a><a name="p49481118715"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="39.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p195512120710"><a name="p195512120710"></a><a name="p195512120710"></a>256</p>
</td>
</tr>
</tbody>
</table>

