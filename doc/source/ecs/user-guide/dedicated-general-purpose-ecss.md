# Dedicated General-Purpose ECSs<a name="EN-US_TOPIC_0091224748"></a>

## Overview<a name="section78382481397"></a>

C4 ECSs use second-generation Intel® Xeon® Scalable processors with technologies optimized and high-speed intelligent NICs to offer powerful and stable computing performance, including ultra-high network bandwidth and PPS.

C3 ECSs are newly released. They are developed based on KVM virtualization, use Intel® Xeon® Scalable processors and Data Plane Development Kit \(DPDK\) rapid packet processing mechanism, and feature high and stable computing performance. Working in high-performance networks, the C3 ECSs provide higher performance and stability, meeting enterprise-class application requirements.

## Specifications<a name="section375984364113"></a>

**Table  1**  C4 ECS specifications

<a name="table8948953114219"></a>
<table><thead align="left"><tr id="row12948753174220"><th class="cellrowborder" valign="top" width="14.401440144014401%" id="mcps1.2.8.1.1"><p id="p10948753134219"><a name="p10948753134219"></a><a name="p10948753134219"></a>Flavor</p>
</th>
<th class="cellrowborder" valign="top" width="11.841184118411844%" id="mcps1.2.8.1.2"><p id="p129489532421"><a name="p129489532421"></a><a name="p129489532421"></a>vCPUs</p>
</th>
<th class="cellrowborder" valign="top" width="13.731373137313732%" id="mcps1.2.8.1.3"><p id="p169481853114217"><a name="p169481853114217"></a><a name="p169481853114217"></a>Memory (GB)</p>
</th>
<th class="cellrowborder" valign="top" width="14.851485148514854%" id="mcps1.2.8.1.4"><p id="p11949135319428"><a name="p11949135319428"></a><a name="p11949135319428"></a>Maximum/Assured Bandwidth (Gbit/s)</p>
</th>
<th class="cellrowborder" valign="top" width="15.361536153615363%" id="mcps1.2.8.1.5"><p id="p194915532424"><a name="p194915532424"></a><a name="p194915532424"></a>Maximum PPS (10,000)</p>
</th>
<th class="cellrowborder" valign="top" width="10.791079107910791%" id="mcps1.2.8.1.6"><p id="p1994965364211"><a name="p1994965364211"></a><a name="p1994965364211"></a>NIC Multi-Queue</p>
</th>
<th class="cellrowborder" valign="top" width="19.021902190219027%" id="mcps1.2.8.1.7"><p id="p394914535420"><a name="p394914535420"></a><a name="p394914535420"></a>Virtualization Type</p>
</th>
</tr>
</thead>
<tbody><tr id="row7949185384216"><td class="cellrowborder" valign="top" width="14.401440144014401%" headers="mcps1.2.8.1.1 "><p id="p11418542432"><a name="p11418542432"></a><a name="p11418542432"></a>c4.large.2</p>
</td>
<td class="cellrowborder" valign="top" width="11.841184118411844%" headers="mcps1.2.8.1.2 "><p id="p155975178445"><a name="p155975178445"></a><a name="p155975178445"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="13.731373137313732%" headers="mcps1.2.8.1.3 "><p id="p259751716443"><a name="p259751716443"></a><a name="p259751716443"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="14.851485148514854%" headers="mcps1.2.8.1.4 "><p id="p982642415441"><a name="p982642415441"></a><a name="p982642415441"></a>4/1.2</p>
</td>
<td class="cellrowborder" valign="top" width="15.361536153615363%" headers="mcps1.2.8.1.5 "><p id="p4917143834415"><a name="p4917143834415"></a><a name="p4917143834415"></a>40</p>
</td>
<td class="cellrowborder" valign="top" width="10.791079107910791%" headers="mcps1.2.8.1.6 "><p id="p17103248184419"><a name="p17103248184419"></a><a name="p17103248184419"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="19.021902190219027%" headers="mcps1.2.8.1.7 "><p id="p1494912536425"><a name="p1494912536425"></a><a name="p1494912536425"></a>KVM</p>
</td>
</tr>
<tr id="row6949175384210"><td class="cellrowborder" valign="top" width="14.401440144014401%" headers="mcps1.2.8.1.1 "><p id="p1114135416430"><a name="p1114135416430"></a><a name="p1114135416430"></a>c4.xlarge.2</p>
</td>
<td class="cellrowborder" valign="top" width="11.841184118411844%" headers="mcps1.2.8.1.2 "><p id="p9597161719443"><a name="p9597161719443"></a><a name="p9597161719443"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="13.731373137313732%" headers="mcps1.2.8.1.3 "><p id="p25973174449"><a name="p25973174449"></a><a name="p25973174449"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="14.851485148514854%" headers="mcps1.2.8.1.4 "><p id="p17826172434412"><a name="p17826172434412"></a><a name="p17826172434412"></a>8/2.4</p>
</td>
<td class="cellrowborder" valign="top" width="15.361536153615363%" headers="mcps1.2.8.1.5 "><p id="p1591733813441"><a name="p1591733813441"></a><a name="p1591733813441"></a>80</p>
</td>
<td class="cellrowborder" valign="top" width="10.791079107910791%" headers="mcps1.2.8.1.6 "><p id="p710374824410"><a name="p710374824410"></a><a name="p710374824410"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="19.021902190219027%" headers="mcps1.2.8.1.7 "><p id="p1995018536429"><a name="p1995018536429"></a><a name="p1995018536429"></a>KVM</p>
</td>
</tr>
<tr id="row4950553104218"><td class="cellrowborder" valign="top" width="14.401440144014401%" headers="mcps1.2.8.1.1 "><p id="p131405494312"><a name="p131405494312"></a><a name="p131405494312"></a>c4.2xlarge.2</p>
</td>
<td class="cellrowborder" valign="top" width="11.841184118411844%" headers="mcps1.2.8.1.2 "><p id="p1959781712446"><a name="p1959781712446"></a><a name="p1959781712446"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="13.731373137313732%" headers="mcps1.2.8.1.3 "><p id="p8597161711443"><a name="p8597161711443"></a><a name="p8597161711443"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="14.851485148514854%" headers="mcps1.2.8.1.4 "><p id="p1682617241443"><a name="p1682617241443"></a><a name="p1682617241443"></a>15/4.5</p>
</td>
<td class="cellrowborder" valign="top" width="15.361536153615363%" headers="mcps1.2.8.1.5 "><p id="p1791743844412"><a name="p1791743844412"></a><a name="p1791743844412"></a>150</p>
</td>
<td class="cellrowborder" valign="top" width="10.791079107910791%" headers="mcps1.2.8.1.6 "><p id="p15103184813444"><a name="p15103184813444"></a><a name="p15103184813444"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="19.021902190219027%" headers="mcps1.2.8.1.7 "><p id="p10950125334213"><a name="p10950125334213"></a><a name="p10950125334213"></a>KVM</p>
</td>
</tr>
<tr id="row095085364210"><td class="cellrowborder" valign="top" width="14.401440144014401%" headers="mcps1.2.8.1.1 "><p id="p714654104311"><a name="p714654104311"></a><a name="p714654104311"></a>c4.3xlarge.2</p>
</td>
<td class="cellrowborder" valign="top" width="11.841184118411844%" headers="mcps1.2.8.1.2 "><p id="p75978171440"><a name="p75978171440"></a><a name="p75978171440"></a>12</p>
</td>
<td class="cellrowborder" valign="top" width="13.731373137313732%" headers="mcps1.2.8.1.3 "><p id="p14597151764411"><a name="p14597151764411"></a><a name="p14597151764411"></a>24</p>
</td>
<td class="cellrowborder" valign="top" width="14.851485148514854%" headers="mcps1.2.8.1.4 "><p id="p178271424164415"><a name="p178271424164415"></a><a name="p178271424164415"></a>17/7</p>
</td>
<td class="cellrowborder" valign="top" width="15.361536153615363%" headers="mcps1.2.8.1.5 "><p id="p29172038204420"><a name="p29172038204420"></a><a name="p29172038204420"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="10.791079107910791%" headers="mcps1.2.8.1.6 "><p id="p201031848144411"><a name="p201031848144411"></a><a name="p201031848144411"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="19.021902190219027%" headers="mcps1.2.8.1.7 "><p id="p119518530421"><a name="p119518530421"></a><a name="p119518530421"></a>KVM</p>
</td>
</tr>
<tr id="row7951195315424"><td class="cellrowborder" valign="top" width="14.401440144014401%" headers="mcps1.2.8.1.1 "><p id="p214165464313"><a name="p214165464313"></a><a name="p214165464313"></a>c4.4xlarge.2</p>
</td>
<td class="cellrowborder" valign="top" width="11.841184118411844%" headers="mcps1.2.8.1.2 "><p id="p9597101784410"><a name="p9597101784410"></a><a name="p9597101784410"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="13.731373137313732%" headers="mcps1.2.8.1.3 "><p id="p159814177446"><a name="p159814177446"></a><a name="p159814177446"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="14.851485148514854%" headers="mcps1.2.8.1.4 "><p id="p48271024194416"><a name="p48271024194416"></a><a name="p48271024194416"></a>20/9</p>
</td>
<td class="cellrowborder" valign="top" width="15.361536153615363%" headers="mcps1.2.8.1.5 "><p id="p1917203864416"><a name="p1917203864416"></a><a name="p1917203864416"></a>280</p>
</td>
<td class="cellrowborder" valign="top" width="10.791079107910791%" headers="mcps1.2.8.1.6 "><p id="p12103848154411"><a name="p12103848154411"></a><a name="p12103848154411"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="19.021902190219027%" headers="mcps1.2.8.1.7 "><p id="p99511853184213"><a name="p99511853184213"></a><a name="p99511853184213"></a>KVM</p>
</td>
</tr>
<tr id="row2095117538427"><td class="cellrowborder" valign="top" width="14.401440144014401%" headers="mcps1.2.8.1.1 "><p id="p114165410430"><a name="p114165410430"></a><a name="p114165410430"></a>c4.6xlarge.2</p>
</td>
<td class="cellrowborder" valign="top" width="11.841184118411844%" headers="mcps1.2.8.1.2 "><p id="p959814175442"><a name="p959814175442"></a><a name="p959814175442"></a>24</p>
</td>
<td class="cellrowborder" valign="top" width="13.731373137313732%" headers="mcps1.2.8.1.3 "><p id="p1659810174446"><a name="p1659810174446"></a><a name="p1659810174446"></a>48</p>
</td>
<td class="cellrowborder" valign="top" width="14.851485148514854%" headers="mcps1.2.8.1.4 "><p id="p2827172424416"><a name="p2827172424416"></a><a name="p2827172424416"></a>25/14</p>
</td>
<td class="cellrowborder" valign="top" width="15.361536153615363%" headers="mcps1.2.8.1.5 "><p id="p2917113813447"><a name="p2917113813447"></a><a name="p2917113813447"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.791079107910791%" headers="mcps1.2.8.1.6 "><p id="p1910313481443"><a name="p1910313481443"></a><a name="p1910313481443"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="19.021902190219027%" headers="mcps1.2.8.1.7 "><p id="p9951115364219"><a name="p9951115364219"></a><a name="p9951115364219"></a>KVM</p>
</td>
</tr>
<tr id="row1595175316428"><td class="cellrowborder" valign="top" width="14.401440144014401%" headers="mcps1.2.8.1.1 "><p id="p11455413432"><a name="p11455413432"></a><a name="p11455413432"></a>c4.8xlarge.2</p>
</td>
<td class="cellrowborder" valign="top" width="11.841184118411844%" headers="mcps1.2.8.1.2 "><p id="p115981017124418"><a name="p115981017124418"></a><a name="p115981017124418"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="13.731373137313732%" headers="mcps1.2.8.1.3 "><p id="p13598217194416"><a name="p13598217194416"></a><a name="p13598217194416"></a>64</p>
</td>
<td class="cellrowborder" valign="top" width="14.851485148514854%" headers="mcps1.2.8.1.4 "><p id="p682732417444"><a name="p682732417444"></a><a name="p682732417444"></a>30/18</p>
</td>
<td class="cellrowborder" valign="top" width="15.361536153615363%" headers="mcps1.2.8.1.5 "><p id="p4918113816444"><a name="p4918113816444"></a><a name="p4918113816444"></a>550</p>
</td>
<td class="cellrowborder" valign="top" width="10.791079107910791%" headers="mcps1.2.8.1.6 "><p id="p20104134864418"><a name="p20104134864418"></a><a name="p20104134864418"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="19.021902190219027%" headers="mcps1.2.8.1.7 "><p id="p179521353174218"><a name="p179521353174218"></a><a name="p179521353174218"></a>KVM</p>
</td>
</tr>
<tr id="row119521453204218"><td class="cellrowborder" valign="top" width="14.401440144014401%" headers="mcps1.2.8.1.1 "><p id="p17141854114314"><a name="p17141854114314"></a><a name="p17141854114314"></a>c4.16xlarge.2</p>
</td>
<td class="cellrowborder" valign="top" width="11.841184118411844%" headers="mcps1.2.8.1.2 "><p id="p125981417114419"><a name="p125981417114419"></a><a name="p125981417114419"></a>64</p>
</td>
<td class="cellrowborder" valign="top" width="13.731373137313732%" headers="mcps1.2.8.1.3 "><p id="p1459881724419"><a name="p1459881724419"></a><a name="p1459881724419"></a>128</p>
</td>
<td class="cellrowborder" valign="top" width="14.851485148514854%" headers="mcps1.2.8.1.4 "><p id="p08271724194419"><a name="p08271724194419"></a><a name="p08271724194419"></a>40/36</p>
</td>
<td class="cellrowborder" valign="top" width="15.361536153615363%" headers="mcps1.2.8.1.5 "><p id="p291853894413"><a name="p291853894413"></a><a name="p291853894413"></a>1000</p>
</td>
<td class="cellrowborder" valign="top" width="10.791079107910791%" headers="mcps1.2.8.1.6 "><p id="p51044489446"><a name="p51044489446"></a><a name="p51044489446"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="19.021902190219027%" headers="mcps1.2.8.1.7 "><p id="p3952115324215"><a name="p3952115324215"></a><a name="p3952115324215"></a>KVM</p>
</td>
</tr>
<tr id="row129521153164211"><td class="cellrowborder" valign="top" width="14.401440144014401%" headers="mcps1.2.8.1.1 "><p id="p1914754134318"><a name="p1914754134318"></a><a name="p1914754134318"></a>c4.large.4</p>
</td>
<td class="cellrowborder" valign="top" width="11.841184118411844%" headers="mcps1.2.8.1.2 "><p id="p5598201714446"><a name="p5598201714446"></a><a name="p5598201714446"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="13.731373137313732%" headers="mcps1.2.8.1.3 "><p id="p8598617134419"><a name="p8598617134419"></a><a name="p8598617134419"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="14.851485148514854%" headers="mcps1.2.8.1.4 "><p id="p1282752454410"><a name="p1282752454410"></a><a name="p1282752454410"></a>4/1.2</p>
</td>
<td class="cellrowborder" valign="top" width="15.361536153615363%" headers="mcps1.2.8.1.5 "><p id="p0918338104413"><a name="p0918338104413"></a><a name="p0918338104413"></a>40</p>
</td>
<td class="cellrowborder" valign="top" width="10.791079107910791%" headers="mcps1.2.8.1.6 "><p id="p2104204804416"><a name="p2104204804416"></a><a name="p2104204804416"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="19.021902190219027%" headers="mcps1.2.8.1.7 "><p id="p16953185364212"><a name="p16953185364212"></a><a name="p16953185364212"></a>KVM</p>
</td>
</tr>
<tr id="row395375334216"><td class="cellrowborder" valign="top" width="14.401440144014401%" headers="mcps1.2.8.1.1 "><p id="p1141354154315"><a name="p1141354154315"></a><a name="p1141354154315"></a>c4.xlarge.4</p>
</td>
<td class="cellrowborder" valign="top" width="11.841184118411844%" headers="mcps1.2.8.1.2 "><p id="p16598817134417"><a name="p16598817134417"></a><a name="p16598817134417"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="13.731373137313732%" headers="mcps1.2.8.1.3 "><p id="p5598317124415"><a name="p5598317124415"></a><a name="p5598317124415"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="14.851485148514854%" headers="mcps1.2.8.1.4 "><p id="p3827142454415"><a name="p3827142454415"></a><a name="p3827142454415"></a>8/2.4</p>
</td>
<td class="cellrowborder" valign="top" width="15.361536153615363%" headers="mcps1.2.8.1.5 "><p id="p791883874418"><a name="p791883874418"></a><a name="p791883874418"></a>80</p>
</td>
<td class="cellrowborder" valign="top" width="10.791079107910791%" headers="mcps1.2.8.1.6 "><p id="p710411488448"><a name="p710411488448"></a><a name="p710411488448"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="19.021902190219027%" headers="mcps1.2.8.1.7 "><p id="p595355318425"><a name="p595355318425"></a><a name="p595355318425"></a>KVM</p>
</td>
</tr>
<tr id="row295355384217"><td class="cellrowborder" valign="top" width="14.401440144014401%" headers="mcps1.2.8.1.1 "><p id="p201419549435"><a name="p201419549435"></a><a name="p201419549435"></a>c4.2xlarge.4</p>
</td>
<td class="cellrowborder" valign="top" width="11.841184118411844%" headers="mcps1.2.8.1.2 "><p id="p3598111715447"><a name="p3598111715447"></a><a name="p3598111715447"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="13.731373137313732%" headers="mcps1.2.8.1.3 "><p id="p1259831754418"><a name="p1259831754418"></a><a name="p1259831754418"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="14.851485148514854%" headers="mcps1.2.8.1.4 "><p id="p58275248444"><a name="p58275248444"></a><a name="p58275248444"></a>15/4.5</p>
</td>
<td class="cellrowborder" valign="top" width="15.361536153615363%" headers="mcps1.2.8.1.5 "><p id="p13918153844418"><a name="p13918153844418"></a><a name="p13918153844418"></a>150</p>
</td>
<td class="cellrowborder" valign="top" width="10.791079107910791%" headers="mcps1.2.8.1.6 "><p id="p1910434814444"><a name="p1910434814444"></a><a name="p1910434814444"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="19.021902190219027%" headers="mcps1.2.8.1.7 "><p id="p3954135318424"><a name="p3954135318424"></a><a name="p3954135318424"></a>KVM</p>
</td>
</tr>
<tr id="row13954185312420"><td class="cellrowborder" valign="top" width="14.401440144014401%" headers="mcps1.2.8.1.1 "><p id="p15141354134314"><a name="p15141354134314"></a><a name="p15141354134314"></a>c4.3xlarge.4</p>
</td>
<td class="cellrowborder" valign="top" width="11.841184118411844%" headers="mcps1.2.8.1.2 "><p id="p1598141714413"><a name="p1598141714413"></a><a name="p1598141714413"></a>12</p>
</td>
<td class="cellrowborder" valign="top" width="13.731373137313732%" headers="mcps1.2.8.1.3 "><p id="p195987175449"><a name="p195987175449"></a><a name="p195987175449"></a>48</p>
</td>
<td class="cellrowborder" valign="top" width="14.851485148514854%" headers="mcps1.2.8.1.4 "><p id="p18271524144412"><a name="p18271524144412"></a><a name="p18271524144412"></a>17/7</p>
</td>
<td class="cellrowborder" valign="top" width="15.361536153615363%" headers="mcps1.2.8.1.5 "><p id="p209181138194415"><a name="p209181138194415"></a><a name="p209181138194415"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="10.791079107910791%" headers="mcps1.2.8.1.6 "><p id="p1104144818441"><a name="p1104144818441"></a><a name="p1104144818441"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="19.021902190219027%" headers="mcps1.2.8.1.7 "><p id="p1295420536420"><a name="p1295420536420"></a><a name="p1295420536420"></a>KVM</p>
</td>
</tr>
<tr id="row20813193384311"><td class="cellrowborder" valign="top" width="14.401440144014401%" headers="mcps1.2.8.1.1 "><p id="p2015175474313"><a name="p2015175474313"></a><a name="p2015175474313"></a>c4.4xlarge.4</p>
</td>
<td class="cellrowborder" valign="top" width="11.841184118411844%" headers="mcps1.2.8.1.2 "><p id="p1659831714445"><a name="p1659831714445"></a><a name="p1659831714445"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="13.731373137313732%" headers="mcps1.2.8.1.3 "><p id="p135981117174416"><a name="p135981117174416"></a><a name="p135981117174416"></a>64</p>
</td>
<td class="cellrowborder" valign="top" width="14.851485148514854%" headers="mcps1.2.8.1.4 "><p id="p14827112494415"><a name="p14827112494415"></a><a name="p14827112494415"></a>20/9</p>
</td>
<td class="cellrowborder" valign="top" width="15.361536153615363%" headers="mcps1.2.8.1.5 "><p id="p1691853815447"><a name="p1691853815447"></a><a name="p1691853815447"></a>280</p>
</td>
<td class="cellrowborder" valign="top" width="10.791079107910791%" headers="mcps1.2.8.1.6 "><p id="p0104184884415"><a name="p0104184884415"></a><a name="p0104184884415"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="19.021902190219027%" headers="mcps1.2.8.1.7 "><p id="p356006204413"><a name="p356006204413"></a><a name="p356006204413"></a>KVM</p>
</td>
</tr>
<tr id="row3813153384319"><td class="cellrowborder" valign="top" width="14.401440144014401%" headers="mcps1.2.8.1.1 "><p id="p01511547433"><a name="p01511547433"></a><a name="p01511547433"></a>c4.6xlarge.4</p>
</td>
<td class="cellrowborder" valign="top" width="11.841184118411844%" headers="mcps1.2.8.1.2 "><p id="p135981517104410"><a name="p135981517104410"></a><a name="p135981517104410"></a>24</p>
</td>
<td class="cellrowborder" valign="top" width="13.731373137313732%" headers="mcps1.2.8.1.3 "><p id="p05981917154417"><a name="p05981917154417"></a><a name="p05981917154417"></a>96</p>
</td>
<td class="cellrowborder" valign="top" width="14.851485148514854%" headers="mcps1.2.8.1.4 "><p id="p16827524104415"><a name="p16827524104415"></a><a name="p16827524104415"></a>25/14</p>
</td>
<td class="cellrowborder" valign="top" width="15.361536153615363%" headers="mcps1.2.8.1.5 "><p id="p4918153844410"><a name="p4918153844410"></a><a name="p4918153844410"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.791079107910791%" headers="mcps1.2.8.1.6 "><p id="p16104114818449"><a name="p16104114818449"></a><a name="p16104114818449"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="19.021902190219027%" headers="mcps1.2.8.1.7 "><p id="p2056126144415"><a name="p2056126144415"></a><a name="p2056126144415"></a>KVM</p>
</td>
</tr>
<tr id="row6814533164314"><td class="cellrowborder" valign="top" width="14.401440144014401%" headers="mcps1.2.8.1.1 "><p id="p201545410435"><a name="p201545410435"></a><a name="p201545410435"></a>c4.8xlarge.4</p>
</td>
<td class="cellrowborder" valign="top" width="11.841184118411844%" headers="mcps1.2.8.1.2 "><p id="p1459881724412"><a name="p1459881724412"></a><a name="p1459881724412"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="13.731373137313732%" headers="mcps1.2.8.1.3 "><p id="p15598111712447"><a name="p15598111712447"></a><a name="p15598111712447"></a>128</p>
</td>
<td class="cellrowborder" valign="top" width="14.851485148514854%" headers="mcps1.2.8.1.4 "><p id="p182710243443"><a name="p182710243443"></a><a name="p182710243443"></a>30/18</p>
</td>
<td class="cellrowborder" valign="top" width="15.361536153615363%" headers="mcps1.2.8.1.5 "><p id="p19181338184420"><a name="p19181338184420"></a><a name="p19181338184420"></a>550</p>
</td>
<td class="cellrowborder" valign="top" width="10.791079107910791%" headers="mcps1.2.8.1.6 "><p id="p101045489449"><a name="p101045489449"></a><a name="p101045489449"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="19.021902190219027%" headers="mcps1.2.8.1.7 "><p id="p1556117674414"><a name="p1556117674414"></a><a name="p1556117674414"></a>KVM</p>
</td>
</tr>
<tr id="row11814433164319"><td class="cellrowborder" valign="top" width="14.401440144014401%" headers="mcps1.2.8.1.1 "><p id="p1715155418431"><a name="p1715155418431"></a><a name="p1715155418431"></a>c4.16xlarge.4</p>
</td>
<td class="cellrowborder" valign="top" width="11.841184118411844%" headers="mcps1.2.8.1.2 "><p id="p3599217104412"><a name="p3599217104412"></a><a name="p3599217104412"></a>64</p>
</td>
<td class="cellrowborder" valign="top" width="13.731373137313732%" headers="mcps1.2.8.1.3 "><p id="p165991217204415"><a name="p165991217204415"></a><a name="p165991217204415"></a>256</p>
</td>
<td class="cellrowborder" valign="top" width="14.851485148514854%" headers="mcps1.2.8.1.4 "><p id="p9827182444420"><a name="p9827182444420"></a><a name="p9827182444420"></a>40/36</p>
</td>
<td class="cellrowborder" valign="top" width="15.361536153615363%" headers="mcps1.2.8.1.5 "><p id="p89181638134418"><a name="p89181638134418"></a><a name="p89181638134418"></a>1000</p>
</td>
<td class="cellrowborder" valign="top" width="10.791079107910791%" headers="mcps1.2.8.1.6 "><p id="p310464854413"><a name="p310464854413"></a><a name="p310464854413"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="19.021902190219027%" headers="mcps1.2.8.1.7 "><p id="p85615624413"><a name="p85615624413"></a><a name="p85615624413"></a>KVM</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  C3 ECS specifications

<a name="table3949605220464"></a>
<table><thead align="left"><tr id="row5755737620464"><th class="cellrowborder" valign="top" width="14.591459145914593%" id="mcps1.2.8.1.1"><p id="p119625912538"><a name="p119625912538"></a><a name="p119625912538"></a>Flavor</p>
</th>
<th class="cellrowborder" valign="top" width="11.65116511651165%" id="mcps1.2.8.1.2"><p id="p41529665204624"><a name="p41529665204624"></a><a name="p41529665204624"></a>vCPUs</p>
</th>
<th class="cellrowborder" valign="top" width="13.731373137313732%" id="mcps1.2.8.1.3"><p id="p9028760204624"><a name="p9028760204624"></a><a name="p9028760204624"></a>Memory (GB)</p>
</th>
<th class="cellrowborder" valign="top" width="14.92149214921492%" id="mcps1.2.8.1.4"><p id="p48701959115410"><a name="p48701959115410"></a><a name="p48701959115410"></a>Maximum/Assured Bandwidth (Gbit/s)</p>
</th>
<th class="cellrowborder" valign="top" width="15.151515151515152%" id="mcps1.2.8.1.5"><p id="p7870115905413"><a name="p7870115905413"></a><a name="p7870115905413"></a>Maximum PPS (10,000)</p>
</th>
<th class="cellrowborder" valign="top" width="10.931093109310929%" id="mcps1.2.8.1.6"><p id="p2870115935414"><a name="p2870115935414"></a><a name="p2870115935414"></a>NIC Multi-Queue</p>
</th>
<th class="cellrowborder" valign="top" width="19.021902190219024%" id="mcps1.2.8.1.7"><p id="p167851826171518"><a name="p167851826171518"></a><a name="p167851826171518"></a>Virtualization Type</p>
</th>
</tr>
</thead>
<tbody><tr id="row4782024320464"><td class="cellrowborder" valign="top" width="14.591459145914593%" headers="mcps1.2.8.1.1 "><p id="p019645920533"><a name="p019645920533"></a><a name="p019645920533"></a>c3.large.2</p>
</td>
<td class="cellrowborder" valign="top" width="11.65116511651165%" headers="mcps1.2.8.1.2 "><p id="p29312084204624"><a name="p29312084204624"></a><a name="p29312084204624"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="13.731373137313732%" headers="mcps1.2.8.1.3 "><p id="p25468631204624"><a name="p25468631204624"></a><a name="p25468631204624"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="14.92149214921492%" headers="mcps1.2.8.1.4 "><p id="p2147257145517"><a name="p2147257145517"></a><a name="p2147257145517"></a>1.5/0.6</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.8.1.5 "><p id="p1784643145513"><a name="p1784643145513"></a><a name="p1784643145513"></a>30</p>
</td>
<td class="cellrowborder" valign="top" width="10.931093109310929%" headers="mcps1.2.8.1.6 "><p id="p1492412255555"><a name="p1492412255555"></a><a name="p1492412255555"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="19.021902190219024%" headers="mcps1.2.8.1.7 "><p id="p4415173419165"><a name="p4415173419165"></a><a name="p4415173419165"></a>KVM</p>
</td>
</tr>
<tr id="row2115659920464"><td class="cellrowborder" valign="top" width="14.591459145914593%" headers="mcps1.2.8.1.1 "><p id="p11196135918538"><a name="p11196135918538"></a><a name="p11196135918538"></a>c3.xlarge.2</p>
</td>
<td class="cellrowborder" valign="top" width="11.65116511651165%" headers="mcps1.2.8.1.2 "><p id="p54672497204624"><a name="p54672497204624"></a><a name="p54672497204624"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="13.731373137313732%" headers="mcps1.2.8.1.3 "><p id="p66396173204624"><a name="p66396173204624"></a><a name="p66396173204624"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="14.92149214921492%" headers="mcps1.2.8.1.4 "><p id="p1214725715554"><a name="p1214725715554"></a><a name="p1214725715554"></a>3/1</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.8.1.5 "><p id="p1078417433551"><a name="p1078417433551"></a><a name="p1078417433551"></a>50</p>
</td>
<td class="cellrowborder" valign="top" width="10.931093109310929%" headers="mcps1.2.8.1.6 "><p id="p892414258558"><a name="p892414258558"></a><a name="p892414258558"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="19.021902190219024%" headers="mcps1.2.8.1.7 "><p id="p10430634121615"><a name="p10430634121615"></a><a name="p10430634121615"></a>KVM</p>
</td>
</tr>
<tr id="row3908502020464"><td class="cellrowborder" valign="top" width="14.591459145914593%" headers="mcps1.2.8.1.1 "><p id="p3196185911532"><a name="p3196185911532"></a><a name="p3196185911532"></a>c3.2xlarge.2</p>
</td>
<td class="cellrowborder" valign="top" width="11.65116511651165%" headers="mcps1.2.8.1.2 "><p id="p60681384204624"><a name="p60681384204624"></a><a name="p60681384204624"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="13.731373137313732%" headers="mcps1.2.8.1.3 "><p id="p16245046204624"><a name="p16245046204624"></a><a name="p16245046204624"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="14.92149214921492%" headers="mcps1.2.8.1.4 "><p id="p114745718550"><a name="p114745718550"></a><a name="p114745718550"></a>5/2</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.8.1.5 "><p id="p187849438559"><a name="p187849438559"></a><a name="p187849438559"></a>90</p>
</td>
<td class="cellrowborder" valign="top" width="10.931093109310929%" headers="mcps1.2.8.1.6 "><p id="p1892412535520"><a name="p1892412535520"></a><a name="p1892412535520"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="19.021902190219024%" headers="mcps1.2.8.1.7 "><p id="p444513349168"><a name="p444513349168"></a><a name="p444513349168"></a>KVM</p>
</td>
</tr>
<tr id="row4501963420464"><td class="cellrowborder" valign="top" width="14.591459145914593%" headers="mcps1.2.8.1.1 "><p id="p14196125917539"><a name="p14196125917539"></a><a name="p14196125917539"></a>c3.4xlarge.2</p>
</td>
<td class="cellrowborder" valign="top" width="11.65116511651165%" headers="mcps1.2.8.1.2 "><p id="p66732830204624"><a name="p66732830204624"></a><a name="p66732830204624"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="13.731373137313732%" headers="mcps1.2.8.1.3 "><p id="p36650153204624"><a name="p36650153204624"></a><a name="p36650153204624"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="14.92149214921492%" headers="mcps1.2.8.1.4 "><p id="p1314710574557"><a name="p1314710574557"></a><a name="p1314710574557"></a>10/4</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.8.1.5 "><p id="p18784144312551"><a name="p18784144312551"></a><a name="p18784144312551"></a>130</p>
</td>
<td class="cellrowborder" valign="top" width="10.931093109310929%" headers="mcps1.2.8.1.6 "><p id="p12924525195510"><a name="p12924525195510"></a><a name="p12924525195510"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="19.021902190219024%" headers="mcps1.2.8.1.7 "><p id="p74591834131619"><a name="p74591834131619"></a><a name="p74591834131619"></a>KVM</p>
</td>
</tr>
<tr id="row4430014820464"><td class="cellrowborder" valign="top" width="14.591459145914593%" headers="mcps1.2.8.1.1 "><p id="p8196155911537"><a name="p8196155911537"></a><a name="p8196155911537"></a>c3.8xlarge.2</p>
</td>
<td class="cellrowborder" valign="top" width="11.65116511651165%" headers="mcps1.2.8.1.2 "><p id="p28249412204624"><a name="p28249412204624"></a><a name="p28249412204624"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="13.731373137313732%" headers="mcps1.2.8.1.3 "><p id="p6500997204624"><a name="p6500997204624"></a><a name="p6500997204624"></a>64</p>
</td>
<td class="cellrowborder" valign="top" width="14.92149214921492%" headers="mcps1.2.8.1.4 "><p id="p41472573555"><a name="p41472573555"></a><a name="p41472573555"></a>15/8</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.8.1.5 "><p id="p1978764355516"><a name="p1978764355516"></a><a name="p1978764355516"></a>260</p>
</td>
<td class="cellrowborder" valign="top" width="10.931093109310929%" headers="mcps1.2.8.1.6 "><p id="p13924152565510"><a name="p13924152565510"></a><a name="p13924152565510"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="19.021902190219024%" headers="mcps1.2.8.1.7 "><p id="p1547233421618"><a name="p1547233421618"></a><a name="p1547233421618"></a>KVM</p>
</td>
</tr>
<tr id="row2992323420464"><td class="cellrowborder" valign="top" width="14.591459145914593%" headers="mcps1.2.8.1.1 "><p id="p0196125915320"><a name="p0196125915320"></a><a name="p0196125915320"></a>c3.15xlarge.2</p>
</td>
<td class="cellrowborder" valign="top" width="11.65116511651165%" headers="mcps1.2.8.1.2 "><p id="p14694799204624"><a name="p14694799204624"></a><a name="p14694799204624"></a>60</p>
</td>
<td class="cellrowborder" valign="top" width="13.731373137313732%" headers="mcps1.2.8.1.3 "><p id="p49428081204624"><a name="p49428081204624"></a><a name="p49428081204624"></a>128</p>
</td>
<td class="cellrowborder" valign="top" width="14.92149214921492%" headers="mcps1.2.8.1.4 "><p id="p12147105785520"><a name="p12147105785520"></a><a name="p12147105785520"></a>17/16</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.8.1.5 "><p id="p16787643165514"><a name="p16787643165514"></a><a name="p16787643165514"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="10.931093109310929%" headers="mcps1.2.8.1.6 "><p id="p592410256556"><a name="p592410256556"></a><a name="p592410256556"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="19.021902190219024%" headers="mcps1.2.8.1.7 "><p id="p10484183451610"><a name="p10484183451610"></a><a name="p10484183451610"></a>KVM</p>
</td>
</tr>
<tr id="row751642120464"><td class="cellrowborder" valign="top" width="14.591459145914593%" headers="mcps1.2.8.1.1 "><p id="p6196145910537"><a name="p6196145910537"></a><a name="p6196145910537"></a>c3.large.4</p>
</td>
<td class="cellrowborder" valign="top" width="11.65116511651165%" headers="mcps1.2.8.1.2 "><p id="p47196992204624"><a name="p47196992204624"></a><a name="p47196992204624"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="13.731373137313732%" headers="mcps1.2.8.1.3 "><p id="p64859997204624"><a name="p64859997204624"></a><a name="p64859997204624"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="14.92149214921492%" headers="mcps1.2.8.1.4 "><p id="p1784974915014"><a name="p1784974915014"></a><a name="p1784974915014"></a>1.5/0.6</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.8.1.5 "><p id="p1546134113015"><a name="p1546134113015"></a><a name="p1546134113015"></a>30</p>
</td>
<td class="cellrowborder" valign="top" width="10.931093109310929%" headers="mcps1.2.8.1.6 "><p id="p1770615341305"><a name="p1770615341305"></a><a name="p1770615341305"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="19.021902190219024%" headers="mcps1.2.8.1.7 "><p id="p8498173418166"><a name="p8498173418166"></a><a name="p8498173418166"></a>KVM</p>
</td>
</tr>
<tr id="row58396907204611"><td class="cellrowborder" valign="top" width="14.591459145914593%" headers="mcps1.2.8.1.1 "><p id="p1819795995314"><a name="p1819795995314"></a><a name="p1819795995314"></a>c3.xlarge.4</p>
</td>
<td class="cellrowborder" valign="top" width="11.65116511651165%" headers="mcps1.2.8.1.2 "><p id="p15110173204624"><a name="p15110173204624"></a><a name="p15110173204624"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="13.731373137313732%" headers="mcps1.2.8.1.3 "><p id="p15964478204624"><a name="p15964478204624"></a><a name="p15964478204624"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="14.92149214921492%" headers="mcps1.2.8.1.4 "><p id="p13849114918017"><a name="p13849114918017"></a><a name="p13849114918017"></a>3/1</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.8.1.5 "><p id="p74619411208"><a name="p74619411208"></a><a name="p74619411208"></a>50</p>
</td>
<td class="cellrowborder" valign="top" width="10.931093109310929%" headers="mcps1.2.8.1.6 "><p id="p4707193419010"><a name="p4707193419010"></a><a name="p4707193419010"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="19.021902190219024%" headers="mcps1.2.8.1.7 "><p id="p1351333420161"><a name="p1351333420161"></a><a name="p1351333420161"></a>KVM</p>
</td>
</tr>
<tr id="row19288388204611"><td class="cellrowborder" valign="top" width="14.591459145914593%" headers="mcps1.2.8.1.1 "><p id="p1719765985312"><a name="p1719765985312"></a><a name="p1719765985312"></a>c3.2xlarge.4</p>
</td>
<td class="cellrowborder" valign="top" width="11.65116511651165%" headers="mcps1.2.8.1.2 "><p id="p8300597204624"><a name="p8300597204624"></a><a name="p8300597204624"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="13.731373137313732%" headers="mcps1.2.8.1.3 "><p id="p1259733204624"><a name="p1259733204624"></a><a name="p1259733204624"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="14.92149214921492%" headers="mcps1.2.8.1.4 "><p id="p1484954910016"><a name="p1484954910016"></a><a name="p1484954910016"></a>5/2</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.8.1.5 "><p id="p3461741502"><a name="p3461741502"></a><a name="p3461741502"></a>90</p>
</td>
<td class="cellrowborder" valign="top" width="10.931093109310929%" headers="mcps1.2.8.1.6 "><p id="p1070715341707"><a name="p1070715341707"></a><a name="p1070715341707"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="19.021902190219024%" headers="mcps1.2.8.1.7 "><p id="p3787026151511"><a name="p3787026151511"></a><a name="p3787026151511"></a>KVM</p>
</td>
</tr>
<tr id="row39706029204611"><td class="cellrowborder" valign="top" width="14.591459145914593%" headers="mcps1.2.8.1.1 "><p id="p161971259145314"><a name="p161971259145314"></a><a name="p161971259145314"></a>c3.4xlarge.4</p>
</td>
<td class="cellrowborder" valign="top" width="11.65116511651165%" headers="mcps1.2.8.1.2 "><p id="p29388703204624"><a name="p29388703204624"></a><a name="p29388703204624"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="13.731373137313732%" headers="mcps1.2.8.1.3 "><p id="p31674728204624"><a name="p31674728204624"></a><a name="p31674728204624"></a>64</p>
</td>
<td class="cellrowborder" valign="top" width="14.92149214921492%" headers="mcps1.2.8.1.4 "><p id="p10849204911015"><a name="p10849204911015"></a><a name="p10849204911015"></a>10/4</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.8.1.5 "><p id="p144614411012"><a name="p144614411012"></a><a name="p144614411012"></a>130</p>
</td>
<td class="cellrowborder" valign="top" width="10.931093109310929%" headers="mcps1.2.8.1.6 "><p id="p13707103418015"><a name="p13707103418015"></a><a name="p13707103418015"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="19.021902190219024%" headers="mcps1.2.8.1.7 "><p id="p16787626121514"><a name="p16787626121514"></a><a name="p16787626121514"></a>KVM</p>
</td>
</tr>
<tr id="row21822156204611"><td class="cellrowborder" valign="top" width="14.591459145914593%" headers="mcps1.2.8.1.1 "><p id="p1019710595534"><a name="p1019710595534"></a><a name="p1019710595534"></a>c3.8xlarge.4</p>
</td>
<td class="cellrowborder" valign="top" width="11.65116511651165%" headers="mcps1.2.8.1.2 "><p id="p37001786204624"><a name="p37001786204624"></a><a name="p37001786204624"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="13.731373137313732%" headers="mcps1.2.8.1.3 "><p id="p44354694204624"><a name="p44354694204624"></a><a name="p44354694204624"></a>128</p>
</td>
<td class="cellrowborder" valign="top" width="14.92149214921492%" headers="mcps1.2.8.1.4 "><p id="p184924917018"><a name="p184924917018"></a><a name="p184924917018"></a>15/8</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.8.1.5 "><p id="p134644118018"><a name="p134644118018"></a><a name="p134644118018"></a>260</p>
</td>
<td class="cellrowborder" valign="top" width="10.931093109310929%" headers="mcps1.2.8.1.6 "><p id="p1370743414016"><a name="p1370743414016"></a><a name="p1370743414016"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="19.021902190219024%" headers="mcps1.2.8.1.7 "><p id="p378782620154"><a name="p378782620154"></a><a name="p378782620154"></a>KVM</p>
</td>
</tr>
<tr id="row28491536204611"><td class="cellrowborder" valign="top" width="14.591459145914593%" headers="mcps1.2.8.1.1 "><p id="p1519711599531"><a name="p1519711599531"></a><a name="p1519711599531"></a>c3.15xlarge.4</p>
</td>
<td class="cellrowborder" valign="top" width="11.65116511651165%" headers="mcps1.2.8.1.2 "><p id="p42717549204624"><a name="p42717549204624"></a><a name="p42717549204624"></a>60</p>
</td>
<td class="cellrowborder" valign="top" width="13.731373137313732%" headers="mcps1.2.8.1.3 "><p id="p37569478204624"><a name="p37569478204624"></a><a name="p37569478204624"></a>256</p>
</td>
<td class="cellrowborder" valign="top" width="14.92149214921492%" headers="mcps1.2.8.1.4 "><p id="p15849849901"><a name="p15849849901"></a><a name="p15849849901"></a>16/16</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.8.1.5 "><p id="p54614112014"><a name="p54614112014"></a><a name="p54614112014"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="10.931093109310929%" headers="mcps1.2.8.1.6 "><p id="p77070341402"><a name="p77070341402"></a><a name="p77070341402"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="19.021902190219024%" headers="mcps1.2.8.1.7 "><p id="p1278762615153"><a name="p1278762615153"></a><a name="p1278762615153"></a>KVM</p>
</td>
</tr>
</tbody>
</table>

