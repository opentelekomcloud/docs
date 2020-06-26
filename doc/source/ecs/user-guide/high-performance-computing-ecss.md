# High-Performance Computing ECSs<a name="EN-US_TOPIC_0035470100"></a>

## Overview<a name="section13984653191338"></a>

H1 ECSs provide a large number of CPU cores, large memory size, and high throughput. These ECSs are suitable for high-performance processor applications restricted by computing performance.

H2 ECSs are designed to meet high-end computational needs, such as molecular modeling and computational fluid dynamics. In addition to the substantial CPU power, the H2 ECSs offer diverse options for low-latency RDMA networking using EDR InfiniBand NICs to support memory-intensive computational requirements.

HL1 ECSs are the second generation of high-computing ECSs, featuring large memory capacity. They allow ECSs to interconnect with each other using 100 Gbit/s RDMA InfiniBand NICs and support 56 Gbit/s shared high I/O storage.

## Specifications<a name="section43299283191352"></a>

**Table  1**  H1 ECS specifications

<a name="table3536950120255"></a>
<table><thead align="left"><tr id="row6035678020255"><th class="cellrowborder" valign="top" width="26.779999999999998%" id="mcps1.2.5.1.1"><p id="p159211739191415"><a name="p159211739191415"></a><a name="p159211739191415"></a>Flavor</p>
</th>
<th class="cellrowborder" valign="top" width="22.35%" id="mcps1.2.5.1.2"><p id="p40022793163354"><a name="p40022793163354"></a><a name="p40022793163354"></a>vCPUs</p>
</th>
<th class="cellrowborder" valign="top" width="22.27%" id="mcps1.2.5.1.3"><p id="p20620767163354"><a name="p20620767163354"></a><a name="p20620767163354"></a>Memory (GB)</p>
</th>
<th class="cellrowborder" valign="top" width="28.599999999999998%" id="mcps1.2.5.1.4"><p id="p1926853135311"><a name="p1926853135311"></a><a name="p1926853135311"></a>Virtualization Type</p>
</th>
</tr>
</thead>
<tbody><tr id="row3179496520255"><td class="cellrowborder" valign="top" width="26.779999999999998%" headers="mcps1.2.5.1.1 "><p id="p892133913140"><a name="p892133913140"></a><a name="p892133913140"></a>h1.large</p>
</td>
<td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.2.5.1.2 "><p id="p2514179720530"><a name="p2514179720530"></a><a name="p2514179720530"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="22.27%" headers="mcps1.2.5.1.3 "><p id="p2321963720530"><a name="p2321963720530"></a><a name="p2321963720530"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="28.599999999999998%" headers="mcps1.2.5.1.4 "><p id="p82682031531"><a name="p82682031531"></a><a name="p82682031531"></a>Xen</p>
</td>
</tr>
<tr id="row2527953920255"><td class="cellrowborder" valign="top" width="26.779999999999998%" headers="mcps1.2.5.1.1 "><p id="p592114396141"><a name="p592114396141"></a><a name="p592114396141"></a>h1.xlarge</p>
</td>
<td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.2.5.1.2 "><p id="p2416025820530"><a name="p2416025820530"></a><a name="p2416025820530"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="22.27%" headers="mcps1.2.5.1.3 "><p id="p1082390520530"><a name="p1082390520530"></a><a name="p1082390520530"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="28.599999999999998%" headers="mcps1.2.5.1.4 "><p id="p1979843385312"><a name="p1979843385312"></a><a name="p1979843385312"></a>Xen</p>
</td>
</tr>
<tr id="row5593261320255"><td class="cellrowborder" valign="top" width="26.779999999999998%" headers="mcps1.2.5.1.1 "><p id="p6922163941420"><a name="p6922163941420"></a><a name="p6922163941420"></a>h1.2xlarge</p>
</td>
<td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.2.5.1.2 "><p id="p2658483020636"><a name="p2658483020636"></a><a name="p2658483020636"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="22.27%" headers="mcps1.2.5.1.3 "><p id="p588765920636"><a name="p588765920636"></a><a name="p588765920636"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="28.599999999999998%" headers="mcps1.2.5.1.4 "><p id="p28026333533"><a name="p28026333533"></a><a name="p28026333533"></a>Xen</p>
</td>
</tr>
<tr id="row5366391920255"><td class="cellrowborder" valign="top" width="26.779999999999998%" headers="mcps1.2.5.1.1 "><p id="p1492215398148"><a name="p1492215398148"></a><a name="p1492215398148"></a>h1.4xlarge</p>
</td>
<td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.2.5.1.2 "><p id="p2034590520636"><a name="p2034590520636"></a><a name="p2034590520636"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="22.27%" headers="mcps1.2.5.1.3 "><p id="p3740564820636"><a name="p3740564820636"></a><a name="p3740564820636"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="28.599999999999998%" headers="mcps1.2.5.1.4 "><p id="p08079333537"><a name="p08079333537"></a><a name="p08079333537"></a>Xen</p>
</td>
</tr>
<tr id="row1236616320628"><td class="cellrowborder" valign="top" width="26.779999999999998%" headers="mcps1.2.5.1.1 "><p id="p2922123914141"><a name="p2922123914141"></a><a name="p2922123914141"></a>h1.8xlarge</p>
</td>
<td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.2.5.1.2 "><p id="p4224659720636"><a name="p4224659720636"></a><a name="p4224659720636"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="22.27%" headers="mcps1.2.5.1.3 "><p id="p6653119720636"><a name="p6653119720636"></a><a name="p6653119720636"></a>64</p>
</td>
<td class="cellrowborder" valign="top" width="28.599999999999998%" headers="mcps1.2.5.1.4 "><p id="p178121833195316"><a name="p178121833195316"></a><a name="p178121833195316"></a>Xen</p>
</td>
</tr>
<tr id="row24068710102318"><td class="cellrowborder" valign="top" width="26.779999999999998%" headers="mcps1.2.5.1.1 "><p id="p39223395144"><a name="p39223395144"></a><a name="p39223395144"></a>h1.large.4</p>
</td>
<td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.2.5.1.2 "><p id="p14575492102339"><a name="p14575492102339"></a><a name="p14575492102339"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="22.27%" headers="mcps1.2.5.1.3 "><p id="p39764208102339"><a name="p39764208102339"></a><a name="p39764208102339"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="28.599999999999998%" headers="mcps1.2.5.1.4 "><p id="p3818333115317"><a name="p3818333115317"></a><a name="p3818333115317"></a>Xen</p>
</td>
</tr>
<tr id="row38040930102318"><td class="cellrowborder" valign="top" width="26.779999999999998%" headers="mcps1.2.5.1.1 "><p id="p1492217394141"><a name="p1492217394141"></a><a name="p1492217394141"></a>h1.xlarge.4</p>
</td>
<td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.2.5.1.2 "><p id="p10683144102349"><a name="p10683144102349"></a><a name="p10683144102349"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="22.27%" headers="mcps1.2.5.1.3 "><p id="p60028336102349"><a name="p60028336102349"></a><a name="p60028336102349"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="28.599999999999998%" headers="mcps1.2.5.1.4 "><p id="p16821133375315"><a name="p16821133375315"></a><a name="p16821133375315"></a>Xen</p>
</td>
</tr>
<tr id="row9971580102318"><td class="cellrowborder" valign="top" width="26.779999999999998%" headers="mcps1.2.5.1.1 "><p id="p392273913149"><a name="p392273913149"></a><a name="p392273913149"></a>h1.2xlarge.4</p>
</td>
<td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.2.5.1.2 "><p id="p45691156102349"><a name="p45691156102349"></a><a name="p45691156102349"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="22.27%" headers="mcps1.2.5.1.3 "><p id="p9996126102349"><a name="p9996126102349"></a><a name="p9996126102349"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="28.599999999999998%" headers="mcps1.2.5.1.4 "><p id="p582513336532"><a name="p582513336532"></a><a name="p582513336532"></a>Xen</p>
</td>
</tr>
<tr id="row17032163102318"><td class="cellrowborder" valign="top" width="26.779999999999998%" headers="mcps1.2.5.1.1 "><p id="p392293981416"><a name="p392293981416"></a><a name="p392293981416"></a>h1.4xlarge.4</p>
</td>
<td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.2.5.1.2 "><p id="p38802016102349"><a name="p38802016102349"></a><a name="p38802016102349"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="22.27%" headers="mcps1.2.5.1.3 "><p id="p55955621102349"><a name="p55955621102349"></a><a name="p55955621102349"></a>64</p>
</td>
<td class="cellrowborder" valign="top" width="28.599999999999998%" headers="mcps1.2.5.1.4 "><p id="p1383019333538"><a name="p1383019333538"></a><a name="p1383019333538"></a>Xen</p>
</td>
</tr>
<tr id="row32693070102318"><td class="cellrowborder" valign="top" width="26.779999999999998%" headers="mcps1.2.5.1.1 "><p id="p3922143921415"><a name="p3922143921415"></a><a name="p3922143921415"></a>h1.8xlarge.4</p>
</td>
<td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.2.5.1.2 "><p id="p18590713102349"><a name="p18590713102349"></a><a name="p18590713102349"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="22.27%" headers="mcps1.2.5.1.3 "><p id="p29452803102349"><a name="p29452803102349"></a><a name="p29452803102349"></a>128</p>
</td>
<td class="cellrowborder" valign="top" width="28.599999999999998%" headers="mcps1.2.5.1.4 "><p id="p1383420333538"><a name="p1383420333538"></a><a name="p1383420333538"></a>Xen</p>
</td>
</tr>
<tr id="row58866397102325"><td class="cellrowborder" valign="top" width="26.779999999999998%" headers="mcps1.2.5.1.1 "><p id="p59221939131419"><a name="p59221939131419"></a><a name="p59221939131419"></a>h1.large.8</p>
</td>
<td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.2.5.1.2 "><p id="p32376045102349"><a name="p32376045102349"></a><a name="p32376045102349"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="22.27%" headers="mcps1.2.5.1.3 "><p id="p5214006102349"><a name="p5214006102349"></a><a name="p5214006102349"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="28.599999999999998%" headers="mcps1.2.5.1.4 "><p id="p14839143310537"><a name="p14839143310537"></a><a name="p14839143310537"></a>Xen</p>
</td>
</tr>
<tr id="row24044771102325"><td class="cellrowborder" valign="top" width="26.779999999999998%" headers="mcps1.2.5.1.1 "><p id="p13922539111418"><a name="p13922539111418"></a><a name="p13922539111418"></a>h1.xlarge.8</p>
</td>
<td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.2.5.1.2 "><p id="p53487699102349"><a name="p53487699102349"></a><a name="p53487699102349"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="22.27%" headers="mcps1.2.5.1.3 "><p id="p37536388102349"><a name="p37536388102349"></a><a name="p37536388102349"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="28.599999999999998%" headers="mcps1.2.5.1.4 "><p id="p1284443312539"><a name="p1284443312539"></a><a name="p1284443312539"></a>Xen</p>
</td>
</tr>
<tr id="row23281590102325"><td class="cellrowborder" valign="top" width="26.779999999999998%" headers="mcps1.2.5.1.1 "><p id="p199221639161418"><a name="p199221639161418"></a><a name="p199221639161418"></a>h1.2xlarge.8</p>
</td>
<td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.2.5.1.2 "><p id="p14672139102349"><a name="p14672139102349"></a><a name="p14672139102349"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="22.27%" headers="mcps1.2.5.1.3 "><p id="p47592574102349"><a name="p47592574102349"></a><a name="p47592574102349"></a>64</p>
</td>
<td class="cellrowborder" valign="top" width="28.599999999999998%" headers="mcps1.2.5.1.4 "><p id="p1685033319539"><a name="p1685033319539"></a><a name="p1685033319539"></a>Xen</p>
</td>
</tr>
<tr id="row38926599102325"><td class="cellrowborder" valign="top" width="26.779999999999998%" headers="mcps1.2.5.1.1 "><p id="p129221739161414"><a name="p129221739161414"></a><a name="p129221739161414"></a>h1.4xlarge.8</p>
</td>
<td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.2.5.1.2 "><p id="p43169658102349"><a name="p43169658102349"></a><a name="p43169658102349"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="22.27%" headers="mcps1.2.5.1.3 "><p id="p7081403102349"><a name="p7081403102349"></a><a name="p7081403102349"></a>128</p>
</td>
<td class="cellrowborder" valign="top" width="28.599999999999998%" headers="mcps1.2.5.1.4 "><p id="p1585614337536"><a name="p1585614337536"></a><a name="p1585614337536"></a>Xen</p>
</td>
</tr>
<tr id="row13684749102325"><td class="cellrowborder" valign="top" width="26.779999999999998%" headers="mcps1.2.5.1.1 "><p id="p1922239181415"><a name="p1922239181415"></a><a name="p1922239181415"></a>h1.8xlarge.8</p>
</td>
<td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.2.5.1.2 "><p id="p61546832102349"><a name="p61546832102349"></a><a name="p61546832102349"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="22.27%" headers="mcps1.2.5.1.3 "><p id="p19237528102349"><a name="p19237528102349"></a><a name="p19237528102349"></a>256</p>
</td>
<td class="cellrowborder" valign="top" width="28.599999999999998%" headers="mcps1.2.5.1.4 "><p id="p17859833125316"><a name="p17859833125316"></a><a name="p17859833125316"></a>Xen</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  H2 ECS specifications

<a name="table18256889221911"></a>
<table><thead align="left"><tr id="row63682094221911"><th class="cellrowborder" valign="top" width="12.171217121712171%" id="mcps1.2.11.1.1"><p id="p175988154152"><a name="p175988154152"></a><a name="p175988154152"></a>Flavor</p>
</th>
<th class="cellrowborder" valign="top" width="7.520752075207521%" id="mcps1.2.11.1.2"><p id="p2607746163359"><a name="p2607746163359"></a><a name="p2607746163359"></a>vCPUs</p>
</th>
<th class="cellrowborder" valign="top" width="8.270827082708271%" id="mcps1.2.11.1.3"><p id="p9900879163359"><a name="p9900879163359"></a><a name="p9900879163359"></a>Memory (GB)</p>
</th>
<th class="cellrowborder" valign="top" width="14.201420142014202%" id="mcps1.2.11.1.4"><p id="p1826116713518"><a name="p1826116713518"></a><a name="p1826116713518"></a>Maximum/Assured Bandwidth (Gbit/s)</p>
</th>
<th class="cellrowborder" valign="top" width="8.37083708370837%" id="mcps1.2.11.1.5"><p id="p122629710511"><a name="p122629710511"></a><a name="p122629710511"></a>Max. PPS (10,000)</p>
</th>
<th class="cellrowborder" valign="top" width="7.920792079207921%" id="mcps1.2.11.1.6"><p id="p9262071556"><a name="p9262071556"></a><a name="p9262071556"></a>NIC Multi-Queue</p>
</th>
<th class="cellrowborder" valign="top" width="8.270827082708271%" id="mcps1.2.11.1.7"><p id="p43651545205311"><a name="p43651545205311"></a><a name="p43651545205311"></a>Virtualization Type</p>
</th>
<th class="cellrowborder" valign="top" width="8.270827082708271%" id="mcps1.2.11.1.8"><p id="p40391949122"><a name="p40391949122"></a><a name="p40391949122"></a>Local Disks</p>
</th>
<th class="cellrowborder" valign="top" width="11.261126112611262%" id="mcps1.2.11.1.9"><p id="p38374889913"><a name="p38374889913"></a><a name="p38374889913"></a>Capacity of One Local Disk (TB)</p>
</th>
<th class="cellrowborder" valign="top" width="13.74137413741374%" id="mcps1.2.11.1.10"><p id="p60576639192517"><a name="p60576639192517"></a><a name="p60576639192517"></a>Network Type</p>
</th>
</tr>
</thead>
<tbody><tr id="row57748759221911"><td class="cellrowborder" valign="top" width="12.171217121712171%" headers="mcps1.2.11.1.1 "><p id="p155998159156"><a name="p155998159156"></a><a name="p155998159156"></a>h2.3xlarge.10</p>
</td>
<td class="cellrowborder" valign="top" width="7.520752075207521%" headers="mcps1.2.11.1.2 "><p id="p60071762221911"><a name="p60071762221911"></a><a name="p60071762221911"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="8.270827082708271%" headers="mcps1.2.11.1.3 "><p id="p33974514221911"><a name="p33974514221911"></a><a name="p33974514221911"></a>128</p>
</td>
<td class="cellrowborder" valign="top" width="14.201420142014202%" headers="mcps1.2.11.1.4 "><p id="p175366402166"><a name="p175366402166"></a><a name="p175366402166"></a>13/13</p>
</td>
<td class="cellrowborder" valign="top" width="8.37083708370837%" headers="mcps1.2.11.1.5 "><p id="p9254433161616"><a name="p9254433161616"></a><a name="p9254433161616"></a>90</p>
</td>
<td class="cellrowborder" valign="top" width="7.920792079207921%" headers="mcps1.2.11.1.6 "><p id="p1091172171610"><a name="p1091172171610"></a><a name="p1091172171610"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="8.270827082708271%" headers="mcps1.2.11.1.7 "><p id="p636584555320"><a name="p636584555320"></a><a name="p636584555320"></a>KVM</p>
</td>
<td class="cellrowborder" valign="top" width="8.270827082708271%" headers="mcps1.2.11.1.8 "><p id="p59620089122"><a name="p59620089122"></a><a name="p59620089122"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="11.261126112611262%" headers="mcps1.2.11.1.9 "><p id="p21358276913"><a name="p21358276913"></a><a name="p21358276913"></a>3.2</p>
</td>
<td class="cellrowborder" valign="top" width="13.74137413741374%" headers="mcps1.2.11.1.10 "><p id="p7760766192517"><a name="p7760766192517"></a><a name="p7760766192517"></a>100 Gbit/s EDR InfiniBand</p>
</td>
</tr>
<tr id="row22621721222117"><td class="cellrowborder" valign="top" width="12.171217121712171%" headers="mcps1.2.11.1.1 "><p id="p18599161521510"><a name="p18599161521510"></a><a name="p18599161521510"></a>h2.3xlarge.20</p>
</td>
<td class="cellrowborder" valign="top" width="7.520752075207521%" headers="mcps1.2.11.1.2 "><p id="p49562930222117"><a name="p49562930222117"></a><a name="p49562930222117"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="8.270827082708271%" headers="mcps1.2.11.1.3 "><p id="p55174388222117"><a name="p55174388222117"></a><a name="p55174388222117"></a>256</p>
</td>
<td class="cellrowborder" valign="top" width="14.201420142014202%" headers="mcps1.2.11.1.4 "><p id="p1153624020165"><a name="p1153624020165"></a><a name="p1153624020165"></a>13/13</p>
</td>
<td class="cellrowborder" valign="top" width="8.37083708370837%" headers="mcps1.2.11.1.5 "><p id="p15254143361612"><a name="p15254143361612"></a><a name="p15254143361612"></a>90</p>
</td>
<td class="cellrowborder" valign="top" width="7.920792079207921%" headers="mcps1.2.11.1.6 "><p id="p1591142110167"><a name="p1591142110167"></a><a name="p1591142110167"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="8.270827082708271%" headers="mcps1.2.11.1.7 "><p id="p536524515319"><a name="p536524515319"></a><a name="p536524515319"></a>KVM</p>
</td>
<td class="cellrowborder" valign="top" width="8.270827082708271%" headers="mcps1.2.11.1.8 "><p id="p175805739122"><a name="p175805739122"></a><a name="p175805739122"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="11.261126112611262%" headers="mcps1.2.11.1.9 "><p id="p52298800913"><a name="p52298800913"></a><a name="p52298800913"></a>3.2</p>
</td>
<td class="cellrowborder" valign="top" width="13.74137413741374%" headers="mcps1.2.11.1.10 "><p id="p24642342192517"><a name="p24642342192517"></a><a name="p24642342192517"></a>100 Gbit/s EDR InfiniBand</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  HL1 ECS specifications

<a name="table27568023202527"></a>
<table><thead align="left"><tr id="row27025704202527"><th class="cellrowborder" valign="top" width="12.111211121112111%" id="mcps1.2.9.1.1"><p id="p23133277172"><a name="p23133277172"></a><a name="p23133277172"></a>Flavor</p>
</th>
<th class="cellrowborder" valign="top" width="11.511151115111511%" id="mcps1.2.9.1.2"><p id="p3432627216349"><a name="p3432627216349"></a><a name="p3432627216349"></a>vCPUs</p>
</th>
<th class="cellrowborder" valign="top" width="14.161416141614161%" id="mcps1.2.9.1.3"><p id="p2896461516349"><a name="p2896461516349"></a><a name="p2896461516349"></a>Memory (GB)</p>
</th>
<th class="cellrowborder" valign="top" width="15.001500150015001%" id="mcps1.2.9.1.4"><p id="p1111345012173"><a name="p1111345012173"></a><a name="p1111345012173"></a>Maximum/Assured Bandwidth (Gbit/s)</p>
</th>
<th class="cellrowborder" valign="top" width="11.511151115111511%" id="mcps1.2.9.1.5"><p id="p11149502177"><a name="p11149502177"></a><a name="p11149502177"></a>Max. PPS (10,000)</p>
</th>
<th class="cellrowborder" valign="top" width="10.2010201020102%" id="mcps1.2.9.1.6"><p id="p1411411507176"><a name="p1411411507176"></a><a name="p1411411507176"></a>NIC Multi-Queue</p>
</th>
<th class="cellrowborder" valign="top" width="10.561056105610561%" id="mcps1.2.9.1.7"><p id="p6618192495416"><a name="p6618192495416"></a><a name="p6618192495416"></a>Virtualization Type</p>
</th>
<th class="cellrowborder" valign="top" width="14.941494149414941%" id="mcps1.2.9.1.8"><p id="p14027851202527"><a name="p14027851202527"></a><a name="p14027851202527"></a>Network Type</p>
</th>
</tr>
</thead>
<tbody><tr id="row62514137202527"><td class="cellrowborder" valign="top" width="12.111211121112111%" headers="mcps1.2.9.1.1 "><p id="p1631352761718"><a name="p1631352761718"></a><a name="p1631352761718"></a>hl1.8xlarge.8</p>
</td>
<td class="cellrowborder" valign="top" width="11.511151115111511%" headers="mcps1.2.9.1.2 "><p id="p52988451202527"><a name="p52988451202527"></a><a name="p52988451202527"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="14.161416141614161%" headers="mcps1.2.9.1.3 "><p id="p64206127202527"><a name="p64206127202527"></a><a name="p64206127202527"></a>256</p>
</td>
<td class="cellrowborder" valign="top" width="15.001500150015001%" headers="mcps1.2.9.1.4 "><p id="p33313759202527"><a name="p33313759202527"></a><a name="p33313759202527"></a>9/9</p>
</td>
<td class="cellrowborder" valign="top" width="11.511151115111511%" headers="mcps1.2.9.1.5 "><p id="p17200183715175"><a name="p17200183715175"></a><a name="p17200183715175"></a>90</p>
</td>
<td class="cellrowborder" valign="top" width="10.2010201020102%" headers="mcps1.2.9.1.6 "><p id="p117101134201719"><a name="p117101134201719"></a><a name="p117101134201719"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="10.561056105610561%" headers="mcps1.2.9.1.7 "><p id="p962412249542"><a name="p962412249542"></a><a name="p962412249542"></a>KVM</p>
</td>
<td class="cellrowborder" valign="top" width="14.941494149414941%" headers="mcps1.2.9.1.8 "><p id="p14059931202527"><a name="p14059931202527"></a><a name="p14059931202527"></a>100 Gbit/s EDR InfiniBand</p>
</td>
</tr>
</tbody>
</table>

## Scenarios<a name="section1792295234211"></a>

-   Applications

    High-performance computing first-generation ECSs are suitable for applications that require a large number of parallel computing resources and high-performance infrastructure services to meet computing and storage requirements and ensure high rendering efficiency, such as scientific computing.

    High-performance computing second-generation ECSs are suitable for such applications as HPC, big data, and Artificial Intelligence \(AI\).

    -   High-performance hardware: The ratio of memory to vCPU is 8:1. They have a large number of multithreading and physical CPUs, providing high-performance storage I/O and high-throughput network connections.
    -   Dedicated for HPC clusters: Multiple HL1 ECSs form a cluster, which can be used to install scalable cluster file systems, such as Luster. HPC applications running on H2 ECSs can read and modify the data stored on the ECSs.
    -   RDMA network connection: As with H2 ECSs, HL1 ECSs also offer RDMA network using EDR 100 Gbit/s InfiniBand. HL1 ECSs can communicate with H2 ECSs through the RDMA protocol. In addition, to achieve high storage I/O, the HL1 ECSs can access EVS disks through the RDMA protocol. The full storage path can reach a bandwidth of 56 Gbit/s.

-   Application scenarios

    H1 ECSs apply to computing and storage systems for genetic engineering, games, animations, biopharmaceuticals, and scientific computing.

    H2 and HL1 ECSs provide computing capabilities for clusters with a large memory, good connectivity between nodes, and high storage I/O. The typical application scenarios include HPC, big data, and AI. In HPC solution, HL1 ECSs are perfectly suited for the Luster parallel distributed file system, generally used for large-scale cluster computing.

    For example, in HPC scenario, H2 ECSs can be used as compute nodes, and HL1 ECSs can be used as storage nodes.


## Features<a name="section3551415510283"></a>

High-performance computing ECSs have the following features:

-   Large memory capacity and more processor cores than other types of ECSs
-   Up to 32 vCPUs
-   H2 and HL1 ECSs use InfiniBand NICs that provide a bandwidth of 100 Gbit/s.
-   HL1 ECSs can use the following types of EVS disks as system disk and data disk:

    High I/O \(performance-optimized I\)

    Ultra-high I/O \(latency-optimized\)

-   HL1 ECSs support 56 Gbit/s shared high I/O storage.

    To support 56 Gbit/s shared high I/O storage, you only need to attach high I/O \(performance-optimized I\) or ultra-high I/O \(latency-optimized\) EVS disks to target HL1 ECSs.


## Notes on Using H1 ECSs<a name="section24935808102930"></a>

-   H1 ECSs do not support NIC hot swapping.
-   H1 ECSs support modifying specifications if the source and target ECSs are of the same type.
-   H1 ECSs support modifying specifications with general-purpose \(S1, C1, C2, or M1\) ECSs.
-   H1 ECSs support the following OSs:
    -   CentOS 6.8 64bit
    -   CentOS 7.2 64bit
    -   CentOS 7.3 64bit
    -   Windows Server 2008
    -   Windows Server 2012
    -   Windows Server 2016
    -   SUSE Enterprise Linux Server 11 SP3 64bit
    -   SUSE Enterprise Linux Server 11 SP4 64bit
    -   SUSE Enterprise Linux Server 12 SP1 64bit
    -   SUSE Enterprise Linux Server 12 SP2 64bit
    -   Red Hat Enterprise Linux 6.8 64bit
    -   Red Hat Enterprise Linux 7.3 64bit

-   The primary and extension NICs of an H1 ECS have specified application scenarios. For details, see  [Table 4](#en-us_topic_0035470100_table5727704815149).

    **Table  4**  Application scenarios of the NICs of an H1 ECS

    <a name="en-us_topic_0035470100_table5727704815149"></a>
    <table><thead align="left"><tr id="en-us_topic_0035470100_row748744015149"><th class="cellrowborder" valign="top" width="22.057794220577943%" id="mcps1.2.4.1.1"><p id="en-us_topic_0035470100_p3121282515149"><a name="en-us_topic_0035470100_p3121282515149"></a><a name="en-us_topic_0035470100_p3121282515149"></a>NIC Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.706629337066296%" id="mcps1.2.4.1.2"><p id="en-us_topic_0035470100_p4521089215149"><a name="en-us_topic_0035470100_p4521089215149"></a><a name="en-us_topic_0035470100_p4521089215149"></a>Application Scenario</p>
    </th>
    <th class="cellrowborder" valign="top" width="44.235576442355764%" id="mcps1.2.4.1.3"><p id="en-us_topic_0035470100_p3820364415149"><a name="en-us_topic_0035470100_p3820364415149"></a><a name="en-us_topic_0035470100_p3820364415149"></a>Remarks</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0035470100_row4443435015149"><td class="cellrowborder" valign="top" width="22.057794220577943%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0035470100_p250289715149"><a name="en-us_topic_0035470100_p250289715149"></a><a name="en-us_topic_0035470100_p250289715149"></a>Primary NIC</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.706629337066296%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0035470100_p140807015149"><a name="en-us_topic_0035470100_p140807015149"></a><a name="en-us_topic_0035470100_p140807015149"></a>Vertical layer 3 communication</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.235576442355764%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0035470100_p4694482315149"><a name="en-us_topic_0035470100_p4694482315149"></a><a name="en-us_topic_0035470100_p4694482315149"></a>N/A</p>
    </td>
    </tr>
    <tr id="en-us_topic_0035470100_row5070939915149"><td class="cellrowborder" valign="top" width="22.057794220577943%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0035470100_p6436483015149"><a name="en-us_topic_0035470100_p6436483015149"></a><a name="en-us_topic_0035470100_p6436483015149"></a>Extension NIC</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.706629337066296%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0035470100_p4616872615149"><a name="en-us_topic_0035470100_p4616872615149"></a><a name="en-us_topic_0035470100_p4616872615149"></a>Horizontal layer 2 communication</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.235576442355764%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0035470100_p4867930215149"><a name="en-us_topic_0035470100_p4867930215149"></a><a name="en-us_topic_0035470100_p4867930215149"></a>To improve network performance, you can set the MTU of an extension NIC to <strong id="b84235270612277"><a name="b84235270612277"></a><a name="b84235270612277"></a>8888</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Notes on Using H2 ECSs<a name="section11683564103115"></a>

-   H2 ECSs do not support OS reinstallation or change.
-   H2 ECSs do not support specifications modification.
-   H2 ECSs do not support cold migration, live migration, or HA.
-   H2 ECSs support the following OSs:
    -   For public images:
        -   CentOS 7.3 64bit
        -   SUSE Linux Enterprise Server 11 SP4 64bit
        -   SUSE Linux Enterprise Server 12 SP2 64bit

    -   For private images:
        -   CentOS 6.5 64bit
        -   CentOS 7.2 64bit
        -   CentOS 7.3 64bit
        -   SUSE Linux Enterprise Server 11 SP4 64bit
        -   SUSE Linux Enterprise Server 12 SP2 64bit
        -   Red Hat Enterprise Linux 7.2 64bit
        -   Red Hat Enterprise Linux 7.3 64bit


-   H2 ECSs use InfiniBand NICs that provide a bandwidth of 100 Gbit/s.
-   Each H2 ECS uses one PCIe 3.2 TB SSD card for temporary local storage.
-   If an H2 ECS is created using a private image, install an InfiniBand NIC driver on the ECS after the ECS creation following the instructions provided by Mellanox. Download the required version \(4.2-1.0.0.0\) of InfiniBand NIC driver from the official Mellanox website and install the driver by following the instructions provided by Mellanox.
    -   InfiniBand NIC type:  **Mellanox Technologies ConnectX-4 Infiniband HBA \(MCX455A-ECAT\)**
    -   Mellanox official website:  [http://www.mellanox.com/](http://www.mellanox.com/)
    -   NIC driver download path:  [http://www.mellanox.com/page/products\_dyn?product\_family=26&mtag=linux\_sw\_drivers](http://www.mellanox.com/page/products_dyn?product_family=26&mtag=linux_sw_drivers)

-   For SUSE H2 ECSs, if IP over InfiniBand \(IPoIB\) is required, you must manually configure an IP address for the InfiniBand NIC after installing the InfiniBand driver. For details, see  [How Can I Manually Configure an IP Address for an InfiniBand NIC?](how-can-i-manually-configure-an-ip-address-for-an-infiniband-nic.md)
-   After you delete an H2 ECS, the data stored in SSDs is automatically cleared. Therefore, do not store persistence data into SSDs during ECS running.

## Notes on Using HL1 ECSs<a name="section10721258203459"></a>

-   HL1 ECSs only support the attachment of high I/O \(performance-optimized I\) and ultra-high I/O \(latency-optimized\) EVS disks.

    To support 56 Gbit/s shared high I/O storage, you only need to attach high I/O \(performance-optimized I\) or ultra-high I/O \(latency-optimized\) EVS disks to target HL1 ECSs.

-   HL1 ECSs do not support specifications modification.
-   HL1 ECSs use InfiniBand NICs that provide a bandwidth of 100 Gbit/s.
-   HL1 ECSs created using a private image must have the InfiniBand NIC driver installed. Download the required version \(4.2-1.0.0.0\) of InfiniBand NIC driver from the official Mellanox website and install the driver by following the instructions provided by Mellanox.
    -   InfiniBand NIC type:  **Mellanox Technologies ConnectX-4 Infiniband HBA \(MCX455A-ECAT\)**
    -   Mellanox official website:  [http://www.mellanox.com/](http://www.mellanox.com/)

-   For SUSE HL1 ECSs, if IPoIB is required, you must manually configure an IP address for the InfiniBand NIC after installing the InfiniBand driver. For details, see  [How Can I Manually Configure an IP Address for an InfiniBand NIC?](how-can-i-manually-configure-an-ip-address-for-an-infiniband-nic.md)
-   HL1 ECSs support the following OSs:
    -   For public images:
        -   CentOS 7.3 64bit
        -   SUSE Linux Enterprise Server 11 SP4 64bit
        -   SUSE Linux Enterprise Server 12 SP2 64bit

    -   For private images:
        -   CentOS 6.5 64bit
        -   CentOS 7.2 64bit
        -   CentOS 7.3 64bit
        -   SUSE Linux Enterprise Server 11 SP4 64bit
        -   SUSE Linux Enterprise Server 12 SP2 64bit
        -   Red Hat Enterprise Linux 7.2 64bit
        -   Red Hat Enterprise Linux 7.3 64bit


-   Charging an HL1 ECS is stopped when it is stopped.

## Related Links<a name="section26607449225539"></a>

-   [Enabling NIC Multi-Queue](enabling-nic-multi-queue.md)
-   [How Can I Check Whether the Network Communication Between Two ECSs Equipped with an InfiniBand NIC Driver Is Normal?](how-can-i-check-whether-the-network-communication-between-two-ecss-equipped-with-an-infiniband-nic-d.md)

