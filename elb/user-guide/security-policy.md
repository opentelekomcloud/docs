# Security Policy<a name="EN-US_TOPIC_0161927472"></a>

## Scenarios<a name="section15451157527"></a>

When adding HTTPS listeners, you can select desired security policies to improve service security. A security policy is a combination of TLS protocols of different versions and supported cipher suites.

Only enhanced load balancers support this function.

## Add a Security Policy<a name="section76346198117"></a>

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/icon-region.png)  and select the desired region and project.
3.  Click  **Service List**. Under  **Network**, click  **Elastic Load Balancing**.
4.  Locate the target load balancer and click its name.
5.  Under  **Listeners**, click  **Add Listener**.
6.  In the  **Add Listener**  dialog, expand  **Advanced Settings**, and select a security policy.  [Table 1](#table1247813103533)  lists the parameters to be configured.

    **Table  1**  Security policy parameters

    <a name="table1247813103533"></a>
    <table><thead align="left"><tr id="row204784101539"><th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.1"><p id="p147851075312"><a name="p147851075312"></a><a name="p147851075312"></a><strong id="b1492643133813"><a name="b1492643133813"></a><a name="b1492643133813"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="26%" id="mcps1.2.5.1.2"><p id="p175102389132"><a name="p175102389132"></a><a name="p175102389132"></a><strong id="b1453215452384"><a name="b1453215452384"></a><a name="b1453215452384"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23%" id="mcps1.2.5.1.3"><p id="p2478181015313"><a name="p2478181015313"></a><a name="p2478181015313"></a><strong id="b3480115312385"><a name="b3480115312385"></a><a name="b3480115312385"></a>TLS Version</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="36%" id="mcps1.2.5.1.4"><p id="p5478131085310"><a name="p5478131085310"></a><a name="p5478131085310"></a><strong id="b159426569382"><a name="b159426569382"></a><a name="b159426569382"></a>Cipher Suite</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row125843182408"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="p12584131812401"><a name="p12584131812401"></a><a name="p12584131812401"></a>Security Policy TLS-1-0</p>
    </td>
    <td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.5.1.2 "><p id="p151120385139"><a name="p151120385139"></a><a name="p151120385139"></a>TLS 1.0, 1.1, and 1.2 and supported cipher suites (ultra-high compatibility and low security)</p>
    </td>
    <td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.3 "><p id="p1358411811405"><a name="p1358411811405"></a><a name="p1358411811405"></a>TLS 1.2, TLS 1.1, and TLS 1.0</p>
    </td>
    <td class="cellrowborder" rowspan="3" valign="top" width="36%" headers="mcps1.2.5.1.4 "><p id="p152111143203617"><a name="p152111143203617"></a><a name="p152111143203617"></a>ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:AES128-GCM-SHA256:AES256-GCM-SHA384:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA256:AES128-SHA256:AES256-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES128-SHA:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:AES128-SHA:AES256-SHA</p>
    </td>
    </tr>
    <tr id="row1250119222406"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p050232216409"><a name="p050232216409"></a><a name="p050232216409"></a>Security Policy TLS-1-1</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p351110382132"><a name="p351110382132"></a><a name="p351110382132"></a>TLS 1.1 and 1.2 and supported cipher suites (high compatibility and moderate security)</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p185021822194019"><a name="p185021822194019"></a><a name="p185021822194019"></a>TLS 1.2 and TLS 1.1</p>
    </td>
    </tr>
    <tr id="row19159426144017"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p31598266400"><a name="p31598266400"></a><a name="p31598266400"></a>Security Policy TLS-1-2</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p1751113851319"><a name="p1751113851319"></a><a name="p1751113851319"></a>TLS 1.2 and supported cipher suites (moderate compatibility and high security)</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p315914265406"><a name="p315914265406"></a><a name="p315914265406"></a>TLSv1.2</p>
    </td>
    </tr>
    <tr id="row148501331204010"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="p18850153164010"><a name="p18850153164010"></a><a name="p18850153164010"></a>Security Policy TLS-1-2-Strict</p>
    </td>
    <td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.5.1.2 "><p id="p2051117388131"><a name="p2051117388131"></a><a name="p2051117388131"></a>Strict TLS 1.2 and supported cipher suites (low compatibility and ultra-high security)</p>
    </td>
    <td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.3 "><p id="p3850531104014"><a name="p3850531104014"></a><a name="p3850531104014"></a>TLSv1.2</p>
    </td>
    <td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.5.1.4 "><p id="p12274148203711"><a name="p12274148203711"></a><a name="p12274148203711"></a>ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:AES128-GCM-SHA256:AES256-GCM-SHA384:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA256:AES128-SHA256:AES256-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA384</p>
    </td>
    </tr>
    </tbody>
    </table>

7.  Click  **OK**.

## Security Policy Differences<a name="section20639534152813"></a>

**Table  2**  Differences of four types of security policies

<a name="table15499151713314"></a>
<table><thead align="left"><tr id="row6917101743111"><th class="cellrowborder" valign="top" width="37.769999999999996%" id="mcps1.2.6.1.1"><p id="p13917121715317"><a name="p13917121715317"></a><a name="p13917121715317"></a>Security Policy</p>
</th>
<th class="cellrowborder" valign="top" width="13.34%" id="mcps1.2.6.1.2"><p id="p199171717143116"><a name="p199171717143116"></a><a name="p199171717143116"></a>TLS-1-0</p>
</th>
<th class="cellrowborder" valign="top" width="12.509999999999998%" id="mcps1.2.6.1.3"><p id="p1491751718319"><a name="p1491751718319"></a><a name="p1491751718319"></a>TLS-1-1</p>
</th>
<th class="cellrowborder" valign="top" width="12.629999999999999%" id="mcps1.2.6.1.4"><p id="p9917181710317"><a name="p9917181710317"></a><a name="p9917181710317"></a>TLS-1-2</p>
</th>
<th class="cellrowborder" valign="top" width="23.75%" id="mcps1.2.6.1.5"><p id="p1091714171314"><a name="p1091714171314"></a><a name="p1091714171314"></a>TLS-1-2-Strict</p>
</th>
</tr>
</thead>
<tbody><tr id="row169171176311"><td class="cellrowborder" colspan="5" valign="top" headers="mcps1.2.6.1.1 mcps1.2.6.1.2 mcps1.2.6.1.3 mcps1.2.6.1.4 mcps1.2.6.1.5 "><p id="p1491816176312"><a name="p1491816176312"></a><a name="p1491816176312"></a>TLS protocol</p>
</td>
</tr>
<tr id="row39185170319"><td class="cellrowborder" valign="top" width="37.769999999999996%" headers="mcps1.2.6.1.1 "><p id="p1391861719312"><a name="p1391861719312"></a><a name="p1391861719312"></a>TLS 1.0</p>
</td>
<td class="cellrowborder" valign="top" width="13.34%" headers="mcps1.2.6.1.2 "><p id="p7918101713315"><a name="p7918101713315"></a><a name="p7918101713315"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="12.509999999999998%" headers="mcps1.2.6.1.3 "><p id="p18918111720317"><a name="p18918111720317"></a><a name="p18918111720317"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="12.629999999999999%" headers="mcps1.2.6.1.4 "><p id="p13918141718316"><a name="p13918141718316"></a><a name="p13918141718316"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="23.75%" headers="mcps1.2.6.1.5 "><p id="p5918161713314"><a name="p5918161713314"></a><a name="p5918161713314"></a>-</p>
</td>
</tr>
<tr id="row15918121753111"><td class="cellrowborder" valign="top" width="37.769999999999996%" headers="mcps1.2.6.1.1 "><p id="p12918191743117"><a name="p12918191743117"></a><a name="p12918191743117"></a>TLS 1.1</p>
</td>
<td class="cellrowborder" valign="top" width="13.34%" headers="mcps1.2.6.1.2 "><p id="p391821763115"><a name="p391821763115"></a><a name="p391821763115"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="12.509999999999998%" headers="mcps1.2.6.1.3 "><p id="p19181917153111"><a name="p19181917153111"></a><a name="p19181917153111"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="12.629999999999999%" headers="mcps1.2.6.1.4 "><p id="p891861719312"><a name="p891861719312"></a><a name="p891861719312"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="23.75%" headers="mcps1.2.6.1.5 "><p id="p20918141713313"><a name="p20918141713313"></a><a name="p20918141713313"></a>-</p>
</td>
</tr>
<tr id="row1991811175315"><td class="cellrowborder" valign="top" width="37.769999999999996%" headers="mcps1.2.6.1.1 "><p id="p1691881711317"><a name="p1691881711317"></a><a name="p1691881711317"></a>TLS 1.2</p>
</td>
<td class="cellrowborder" valign="top" width="13.34%" headers="mcps1.2.6.1.2 "><p id="p79181317103118"><a name="p79181317103118"></a><a name="p79181317103118"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="12.509999999999998%" headers="mcps1.2.6.1.3 "><p id="p14918191713319"><a name="p14918191713319"></a><a name="p14918191713319"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="12.629999999999999%" headers="mcps1.2.6.1.4 "><p id="p9918917163117"><a name="p9918917163117"></a><a name="p9918917163117"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="23.75%" headers="mcps1.2.6.1.5 "><p id="p1991841713111"><a name="p1991841713111"></a><a name="p1991841713111"></a>√</p>
</td>
</tr>
<tr id="row291841733116"><td class="cellrowborder" colspan="5" valign="top" headers="mcps1.2.6.1.1 mcps1.2.6.1.2 mcps1.2.6.1.3 mcps1.2.6.1.4 mcps1.2.6.1.5 "><p id="p9918141713313"><a name="p9918141713313"></a><a name="p9918141713313"></a>Cipher suite</p>
</td>
</tr>
<tr id="row091921783110"><td class="cellrowborder" valign="top" width="37.769999999999996%" headers="mcps1.2.6.1.1 "><p id="p179196179315"><a name="p179196179315"></a><a name="p179196179315"></a>ECDHE-RSA-AES128-GCM-SHA256</p>
</td>
<td class="cellrowborder" valign="top" width="13.34%" headers="mcps1.2.6.1.2 "><p id="p59191517183116"><a name="p59191517183116"></a><a name="p59191517183116"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="12.509999999999998%" headers="mcps1.2.6.1.3 "><p id="p1391961753118"><a name="p1391961753118"></a><a name="p1391961753118"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="12.629999999999999%" headers="mcps1.2.6.1.4 "><p id="p9919121753115"><a name="p9919121753115"></a><a name="p9919121753115"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="23.75%" headers="mcps1.2.6.1.5 "><p id="p169198175315"><a name="p169198175315"></a><a name="p169198175315"></a>√</p>
</td>
</tr>
<tr id="row169191217103115"><td class="cellrowborder" valign="top" width="37.769999999999996%" headers="mcps1.2.6.1.1 "><p id="p9919161715316"><a name="p9919161715316"></a><a name="p9919161715316"></a>ECDHE-RSA-AES256-GCM-SHA384</p>
</td>
<td class="cellrowborder" valign="top" width="13.34%" headers="mcps1.2.6.1.2 "><p id="p1438611795714"><a name="p1438611795714"></a><a name="p1438611795714"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="12.509999999999998%" headers="mcps1.2.6.1.3 "><p id="p19386121716579"><a name="p19386121716579"></a><a name="p19386121716579"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="12.629999999999999%" headers="mcps1.2.6.1.4 "><p id="p438651712573"><a name="p438651712573"></a><a name="p438651712573"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="23.75%" headers="mcps1.2.6.1.5 "><p id="p73861417145713"><a name="p73861417145713"></a><a name="p73861417145713"></a>√</p>
</td>
</tr>
<tr id="row991931713115"><td class="cellrowborder" valign="top" width="37.769999999999996%" headers="mcps1.2.6.1.1 "><p id="p189194171311"><a name="p189194171311"></a><a name="p189194171311"></a>ECDHE-RSA-AES128-SHA256</p>
</td>
<td class="cellrowborder" valign="top" width="13.34%" headers="mcps1.2.6.1.2 "><p id="p8731818155716"><a name="p8731818155716"></a><a name="p8731818155716"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="12.509999999999998%" headers="mcps1.2.6.1.3 "><p id="p1173181817571"><a name="p1173181817571"></a><a name="p1173181817571"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="12.629999999999999%" headers="mcps1.2.6.1.4 "><p id="p1773116185574"><a name="p1773116185574"></a><a name="p1773116185574"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="23.75%" headers="mcps1.2.6.1.5 "><p id="p19731418135713"><a name="p19731418135713"></a><a name="p19731418135713"></a>√</p>
</td>
</tr>
<tr id="row191918179314"><td class="cellrowborder" valign="top" width="37.769999999999996%" headers="mcps1.2.6.1.1 "><p id="p1392081713116"><a name="p1392081713116"></a><a name="p1392081713116"></a>ECDHE-RSA-AES256-SHA384</p>
</td>
<td class="cellrowborder" valign="top" width="13.34%" headers="mcps1.2.6.1.2 "><p id="p59321319145714"><a name="p59321319145714"></a><a name="p59321319145714"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="12.509999999999998%" headers="mcps1.2.6.1.3 "><p id="p1293271914571"><a name="p1293271914571"></a><a name="p1293271914571"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="12.629999999999999%" headers="mcps1.2.6.1.4 "><p id="p493211197572"><a name="p493211197572"></a><a name="p493211197572"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="23.75%" headers="mcps1.2.6.1.5 "><p id="p1093261965715"><a name="p1093261965715"></a><a name="p1093261965715"></a>√</p>
</td>
</tr>
<tr id="row6920131719318"><td class="cellrowborder" valign="top" width="37.769999999999996%" headers="mcps1.2.6.1.1 "><p id="p1292071733117"><a name="p1292071733117"></a><a name="p1292071733117"></a>AES128-GCM-SHA256</p>
</td>
<td class="cellrowborder" valign="top" width="13.34%" headers="mcps1.2.6.1.2 "><p id="p336782114575"><a name="p336782114575"></a><a name="p336782114575"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="12.509999999999998%" headers="mcps1.2.6.1.3 "><p id="p193671121195714"><a name="p193671121195714"></a><a name="p193671121195714"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="12.629999999999999%" headers="mcps1.2.6.1.4 "><p id="p9367162110575"><a name="p9367162110575"></a><a name="p9367162110575"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="23.75%" headers="mcps1.2.6.1.5 "><p id="p2036782115713"><a name="p2036782115713"></a><a name="p2036782115713"></a>√</p>
</td>
</tr>
<tr id="row69201617183118"><td class="cellrowborder" valign="top" width="37.769999999999996%" headers="mcps1.2.6.1.1 "><p id="p1592011753110"><a name="p1592011753110"></a><a name="p1592011753110"></a>AES256-GCM-SHA384</p>
</td>
<td class="cellrowborder" valign="top" width="13.34%" headers="mcps1.2.6.1.2 "><p id="p196891122185712"><a name="p196891122185712"></a><a name="p196891122185712"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="12.509999999999998%" headers="mcps1.2.6.1.3 "><p id="p116891922185713"><a name="p116891922185713"></a><a name="p116891922185713"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="12.629999999999999%" headers="mcps1.2.6.1.4 "><p id="p768982214579"><a name="p768982214579"></a><a name="p768982214579"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="23.75%" headers="mcps1.2.6.1.5 "><p id="p206891922195718"><a name="p206891922195718"></a><a name="p206891922195718"></a>√</p>
</td>
</tr>
<tr id="row1292011713313"><td class="cellrowborder" valign="top" width="37.769999999999996%" headers="mcps1.2.6.1.1 "><p id="p1192017174319"><a name="p1192017174319"></a><a name="p1192017174319"></a>AES128-SHA256</p>
</td>
<td class="cellrowborder" valign="top" width="13.34%" headers="mcps1.2.6.1.2 "><p id="p588620237572"><a name="p588620237572"></a><a name="p588620237572"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="12.509999999999998%" headers="mcps1.2.6.1.3 "><p id="p1886102320578"><a name="p1886102320578"></a><a name="p1886102320578"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="12.629999999999999%" headers="mcps1.2.6.1.4 "><p id="p988619237577"><a name="p988619237577"></a><a name="p988619237577"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="23.75%" headers="mcps1.2.6.1.5 "><p id="p158861823155712"><a name="p158861823155712"></a><a name="p158861823155712"></a>√</p>
</td>
</tr>
<tr id="row1592171713113"><td class="cellrowborder" valign="top" width="37.769999999999996%" headers="mcps1.2.6.1.1 "><p id="p192171713114"><a name="p192171713114"></a><a name="p192171713114"></a>AES256-SHA256</p>
</td>
<td class="cellrowborder" valign="top" width="13.34%" headers="mcps1.2.6.1.2 "><p id="p5146182585720"><a name="p5146182585720"></a><a name="p5146182585720"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="12.509999999999998%" headers="mcps1.2.6.1.3 "><p id="p91461925105711"><a name="p91461925105711"></a><a name="p91461925105711"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="12.629999999999999%" headers="mcps1.2.6.1.4 "><p id="p13146182513574"><a name="p13146182513574"></a><a name="p13146182513574"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="23.75%" headers="mcps1.2.6.1.5 "><p id="p614652511571"><a name="p614652511571"></a><a name="p614652511571"></a>√</p>
</td>
</tr>
<tr id="row1092119177318"><td class="cellrowborder" valign="top" width="37.769999999999996%" headers="mcps1.2.6.1.1 "><p id="p12921171712318"><a name="p12921171712318"></a><a name="p12921171712318"></a>ECDHE-RSA-AES128-SHA</p>
</td>
<td class="cellrowborder" valign="top" width="13.34%" headers="mcps1.2.6.1.2 "><p id="p8921171717319"><a name="p8921171717319"></a><a name="p8921171717319"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="12.509999999999998%" headers="mcps1.2.6.1.3 "><p id="p18921181711312"><a name="p18921181711312"></a><a name="p18921181711312"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="12.629999999999999%" headers="mcps1.2.6.1.4 "><p id="p49211417163111"><a name="p49211417163111"></a><a name="p49211417163111"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="23.75%" headers="mcps1.2.6.1.5 "><p id="p1492111173317"><a name="p1492111173317"></a><a name="p1492111173317"></a>-</p>
</td>
</tr>
<tr id="row292191712319"><td class="cellrowborder" valign="top" width="37.769999999999996%" headers="mcps1.2.6.1.1 "><p id="p11921111712312"><a name="p11921111712312"></a><a name="p11921111712312"></a>ECDHE-RSA-AES256-SHA</p>
</td>
<td class="cellrowborder" valign="top" width="13.34%" headers="mcps1.2.6.1.2 "><p id="p159011449155720"><a name="p159011449155720"></a><a name="p159011449155720"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="12.509999999999998%" headers="mcps1.2.6.1.3 "><p id="p0901849155719"><a name="p0901849155719"></a><a name="p0901849155719"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="12.629999999999999%" headers="mcps1.2.6.1.4 "><p id="p19901114915571"><a name="p19901114915571"></a><a name="p19901114915571"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="23.75%" headers="mcps1.2.6.1.5 "><p id="p192131716316"><a name="p192131716316"></a><a name="p192131716316"></a>-</p>
</td>
</tr>
<tr id="row19921717123115"><td class="cellrowborder" valign="top" width="37.769999999999996%" headers="mcps1.2.6.1.1 "><p id="p1392171783118"><a name="p1392171783118"></a><a name="p1392171783118"></a>AES128-SHA</p>
</td>
<td class="cellrowborder" valign="top" width="13.34%" headers="mcps1.2.6.1.2 "><p id="p63361051155719"><a name="p63361051155719"></a><a name="p63361051155719"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="12.509999999999998%" headers="mcps1.2.6.1.3 "><p id="p6336145112579"><a name="p6336145112579"></a><a name="p6336145112579"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="12.629999999999999%" headers="mcps1.2.6.1.4 "><p id="p15336105125719"><a name="p15336105125719"></a><a name="p15336105125719"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="23.75%" headers="mcps1.2.6.1.5 "><p id="p1492211716315"><a name="p1492211716315"></a><a name="p1492211716315"></a>-</p>
</td>
</tr>
<tr id="row1792231793115"><td class="cellrowborder" valign="top" width="37.769999999999996%" headers="mcps1.2.6.1.1 "><p id="p892281733114"><a name="p892281733114"></a><a name="p892281733114"></a>AES256-SHA</p>
</td>
<td class="cellrowborder" valign="top" width="13.34%" headers="mcps1.2.6.1.2 "><p id="p8484105235718"><a name="p8484105235718"></a><a name="p8484105235718"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="12.509999999999998%" headers="mcps1.2.6.1.3 "><p id="p15484205235718"><a name="p15484205235718"></a><a name="p15484205235718"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="12.629999999999999%" headers="mcps1.2.6.1.4 "><p id="p1448414525571"><a name="p1448414525571"></a><a name="p1448414525571"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="23.75%" headers="mcps1.2.6.1.5 "><p id="p16922191711316"><a name="p16922191711316"></a><a name="p16922191711316"></a>-</p>
</td>
</tr>
<tr id="row992261715317"><td class="cellrowborder" valign="top" width="37.769999999999996%" headers="mcps1.2.6.1.1 "><p id="p892231720312"><a name="p892231720312"></a><a name="p892231720312"></a>ECDHE-ECDSA-AES128-GCM-SHA256</p>
</td>
<td class="cellrowborder" valign="top" width="13.34%" headers="mcps1.2.6.1.2 "><p id="p13887193517572"><a name="p13887193517572"></a><a name="p13887193517572"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="12.509999999999998%" headers="mcps1.2.6.1.3 "><p id="p188871035125717"><a name="p188871035125717"></a><a name="p188871035125717"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="12.629999999999999%" headers="mcps1.2.6.1.4 "><p id="p108878355575"><a name="p108878355575"></a><a name="p108878355575"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="23.75%" headers="mcps1.2.6.1.5 "><p id="p128871735135712"><a name="p128871735135712"></a><a name="p128871735135712"></a>√</p>
</td>
</tr>
<tr id="row10923917203118"><td class="cellrowborder" valign="top" width="37.769999999999996%" headers="mcps1.2.6.1.1 "><p id="p692331763116"><a name="p692331763116"></a><a name="p692331763116"></a>ECDHE-ECDSA-AES128-SHA256</p>
</td>
<td class="cellrowborder" valign="top" width="13.34%" headers="mcps1.2.6.1.2 "><p id="p133321349571"><a name="p133321349571"></a><a name="p133321349571"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="12.509999999999998%" headers="mcps1.2.6.1.3 "><p id="p11332173485714"><a name="p11332173485714"></a><a name="p11332173485714"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="12.629999999999999%" headers="mcps1.2.6.1.4 "><p id="p7332183418573"><a name="p7332183418573"></a><a name="p7332183418573"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="23.75%" headers="mcps1.2.6.1.5 "><p id="p4332434115714"><a name="p4332434115714"></a><a name="p4332434115714"></a>√</p>
</td>
</tr>
<tr id="row1923161713111"><td class="cellrowborder" valign="top" width="37.769999999999996%" headers="mcps1.2.6.1.1 "><p id="p99231617193115"><a name="p99231617193115"></a><a name="p99231617193115"></a>ECDHE-ECDSA-AES128-SHA</p>
</td>
<td class="cellrowborder" valign="top" width="13.34%" headers="mcps1.2.6.1.2 "><p id="p11432135485716"><a name="p11432135485716"></a><a name="p11432135485716"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="12.509999999999998%" headers="mcps1.2.6.1.3 "><p id="p114326548577"><a name="p114326548577"></a><a name="p114326548577"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="12.629999999999999%" headers="mcps1.2.6.1.4 "><p id="p64321854105716"><a name="p64321854105716"></a><a name="p64321854105716"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="23.75%" headers="mcps1.2.6.1.5 "><p id="p169231817143114"><a name="p169231817143114"></a><a name="p169231817143114"></a>-</p>
</td>
</tr>
<tr id="row209235176318"><td class="cellrowborder" valign="top" width="37.769999999999996%" headers="mcps1.2.6.1.1 "><p id="p99237178318"><a name="p99237178318"></a><a name="p99237178318"></a>ECDHE-ECDSA-AES256-GCM-SHA384</p>
</td>
<td class="cellrowborder" valign="top" width="13.34%" headers="mcps1.2.6.1.2 "><p id="p18691532115711"><a name="p18691532115711"></a><a name="p18691532115711"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="12.509999999999998%" headers="mcps1.2.6.1.3 "><p id="p148691132175718"><a name="p148691132175718"></a><a name="p148691132175718"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="12.629999999999999%" headers="mcps1.2.6.1.4 "><p id="p128691832105711"><a name="p128691832105711"></a><a name="p128691832105711"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="23.75%" headers="mcps1.2.6.1.5 "><p id="p98696324574"><a name="p98696324574"></a><a name="p98696324574"></a>√</p>
</td>
</tr>
<tr id="row3923131718315"><td class="cellrowborder" valign="top" width="37.769999999999996%" headers="mcps1.2.6.1.1 "><p id="p7923161723111"><a name="p7923161723111"></a><a name="p7923161723111"></a>ECDHE-ECDSA-AES256-SHA384</p>
</td>
<td class="cellrowborder" valign="top" width="13.34%" headers="mcps1.2.6.1.2 "><p id="p13949730105717"><a name="p13949730105717"></a><a name="p13949730105717"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="12.509999999999998%" headers="mcps1.2.6.1.3 "><p id="p1494993015717"><a name="p1494993015717"></a><a name="p1494993015717"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="12.629999999999999%" headers="mcps1.2.6.1.4 "><p id="p15949183095710"><a name="p15949183095710"></a><a name="p15949183095710"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="23.75%" headers="mcps1.2.6.1.5 "><p id="p394983011572"><a name="p394983011572"></a><a name="p394983011572"></a>√</p>
</td>
</tr>
<tr id="row129243172311"><td class="cellrowborder" valign="top" width="37.769999999999996%" headers="mcps1.2.6.1.1 "><p id="p59241517173119"><a name="p59241517173119"></a><a name="p59241517173119"></a>ECDHE-ECDSA-AES256-SHA</p>
</td>
<td class="cellrowborder" valign="top" width="13.34%" headers="mcps1.2.6.1.2 "><p id="p5931115613573"><a name="p5931115613573"></a><a name="p5931115613573"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="12.509999999999998%" headers="mcps1.2.6.1.3 "><p id="p0932135614574"><a name="p0932135614574"></a><a name="p0932135614574"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="12.629999999999999%" headers="mcps1.2.6.1.4 "><p id="p19932145614577"><a name="p19932145614577"></a><a name="p19932145614577"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="23.75%" headers="mcps1.2.6.1.5 "><p id="p1892471718313"><a name="p1892471718313"></a><a name="p1892471718313"></a>-</p>
</td>
</tr>
</tbody>
</table>

## Modify a Security Policy<a name="section1783252193616"></a>

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/icon-region.png)  and select the desired region and project.
3.  Click  **Service List**. Under  **Network**, click  **Elastic Load Balancing**.
4.  Locate the target load balancer and click its name.
5.  Locate the target listener and click  ![](figures/icon-edit-10.png)  on the right of its name.
6.  On the  **Modify Listener**  page, expand  **Advanced Settings**  and modify the security policy.
7.  Click  **OK**.

