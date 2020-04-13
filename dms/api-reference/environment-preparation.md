# Environment Preparation<a name="EN-US_TOPIC_0086094036"></a>

## Creating a Standard Queue<a name="section1702133611562"></a>

Log in to the DMS console and create a queue. Set  **Type**  to  **Standard**. Record the queue ID for subsequent operations. If you have an available queue, skip this step.

## Creating a Consumer Group<a name="section17686053145613"></a>

Log in to the DMS console and create a consumer group for the queue created in the previous section. Record the consumer group ID for subsequent operations. If you have an available consumer group, skip this step.

## Creating an AK/SK Pair<a name="section1144417605714"></a>

Log in to the management console. Click the username and choose My Credential. Click the  **Access Keys**  tab and click  **Add Access Key**. Save the  **credentials.csv**  file. You can obtain Access Key ID and Secret Access Key from the  **credentials.csv**  file. If you have an available AK/SK pair, skip this step.

## Obtaining a Project ID<a name="section15964151916579"></a>

Log in to the management console. Click the username and choose My Credential. Click the  **Projects**  tab and obtain the project ID based on your region.

## Obtaining Region and Endpoint Information<a name="section128673917572"></a>

Obtain the server name from the enterprise administrator.

## Environment Information<a name="section14133175219570"></a>

**Table  1**  Summary of required environment information

<a name="table621111583614"></a>
<table><thead align="left"><tr id="row7214858860"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="p17216258369"><a name="p17216258369"></a><a name="p17216258369"></a>Category</p>
</th>
<th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.2"><p id="p42176586618"><a name="p42176586618"></a><a name="p42176586618"></a>Project</p>
</th>
<th class="cellrowborder" valign="top" width="55.00000000000001%" id="mcps1.2.4.1.3"><p id="p1321955812610"><a name="p1321955812610"></a><a name="p1321955812610"></a>Example Value</p>
</th>
</tr>
</thead>
<tbody><tr id="row202201558265"><td class="cellrowborder" rowspan="5" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p82211583611"><a name="p82211583611"></a><a name="p82211583611"></a>DMS</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p152224581565"><a name="p152224581565"></a><a name="p152224581565"></a>Queue name</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p12477194619220"><a name="p12477194619220"></a><a name="p12477194619220"></a>-</p>
</td>
</tr>
<tr id="row82257581364"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1022545816616"><a name="p1022545816616"></a><a name="p1022545816616"></a>Queue ID</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p947694610223"><a name="p947694610223"></a><a name="p947694610223"></a>-</p>
</td>
</tr>
<tr id="row322665812618"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p182264584611"><a name="p182264584611"></a><a name="p182264584611"></a>Queue type</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p6475204642214"><a name="p6475204642214"></a><a name="p6475204642214"></a>-</p>
</td>
</tr>
<tr id="row5228205811612"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p182283581565"><a name="p182283581565"></a><a name="p182283581565"></a>Consumer group name</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p047314632216"><a name="p047314632216"></a><a name="p047314632216"></a>-</p>
</td>
</tr>
<tr id="row132302582610"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1923216581362"><a name="p1923216581362"></a><a name="p1923216581362"></a>Consumer group ID</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p194711346202219"><a name="p194711346202219"></a><a name="p194711346202219"></a>-</p>
</td>
</tr>
<tr id="row12326581265"><td class="cellrowborder" rowspan="2" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p132334581617"><a name="p132334581617"></a><a name="p132334581617"></a>Access key</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p72348581562"><a name="p72348581562"></a><a name="p72348581562"></a>AK</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p947074632213"><a name="p947074632213"></a><a name="p947074632213"></a>-</p>
</td>
</tr>
<tr id="row13235185814618"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p723715581069"><a name="p723715581069"></a><a name="p723715581069"></a>SK</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p134668467226"><a name="p134668467226"></a><a name="p134668467226"></a>-</p>
</td>
</tr>
<tr id="row32396581765"><td class="cellrowborder" rowspan="3" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p62419581617"><a name="p62419581617"></a><a name="p62419581617"></a>Project</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p1624105814615"><a name="p1624105814615"></a><a name="p1624105814615"></a>Region</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p624155810615"><a name="p624155810615"></a><a name="p624155810615"></a>-</p>
</td>
</tr>
<tr id="row82421581762"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p3242125818620"><a name="p3242125818620"></a><a name="p3242125818620"></a>Project</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p112430585619"><a name="p112430585619"></a><a name="p112430585619"></a>-</p>
</td>
</tr>
<tr id="row132431558569"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p112441581615"><a name="p112441581615"></a><a name="p112441581615"></a>Project ID</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p224510581611"><a name="p224510581611"></a><a name="p224510581611"></a>-</p>
</td>
</tr>
<tr id="row1245195817616"><td class="cellrowborder" rowspan="3" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p12246195813610"><a name="p12246195813610"></a><a name="p12246195813610"></a>Region and endpoint</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p724645819616"><a name="p724645819616"></a><a name="p724645819616"></a>Region name</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p1924612581611"><a name="p1924612581611"></a><a name="p1924612581611"></a>-</p>
</td>
</tr>
<tr id="row9247458661"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1824716586612"><a name="p1824716586612"></a><a name="p1824716586612"></a>Region</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p13248165818616"><a name="p13248165818616"></a><a name="p13248165818616"></a>-</p>
</td>
</tr>
<tr id="row824815581362"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p42498587610"><a name="p42498587610"></a><a name="p42498587610"></a>Endpoint</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p1925015582617"><a name="p1925015582617"></a><a name="p1925015582617"></a>-</p>
</td>
</tr>
</tbody>
</table>

