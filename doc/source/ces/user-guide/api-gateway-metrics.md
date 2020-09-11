# API Gateway Metrics<a name="EN-US_TOPIC_0084572248"></a>

**Table  1**  API Gateway metrics

<a name="table47977864163937"></a>
<table><thead align="left"><tr id="en-us_topic_0015479905_row43554686153251"><th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.7.1.1"><p id="p1839163792517"><a name="p1839163792517"></a><a name="p1839163792517"></a>Metric ID</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.7.1.2"><p id="en-us_topic_0015479905_p12757995153251"><a name="en-us_topic_0015479905_p12757995153251"></a><a name="en-us_topic_0015479905_p12757995153251"></a>Metric</p>
</th>
<th class="cellrowborder" valign="top" width="22%" id="mcps1.2.7.1.3"><p id="en-us_topic_0015479905_p26764654153251"><a name="en-us_topic_0015479905_p26764654153251"></a><a name="en-us_topic_0015479905_p26764654153251"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.7.1.4"><p id="en-us_topic_0015479905_p20453337153251"><a name="en-us_topic_0015479905_p20453337153251"></a><a name="en-us_topic_0015479905_p20453337153251"></a>Value Range</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.7.1.5"><p id="en-us_topic_0015479905_p46107605153251"><a name="en-us_topic_0015479905_p46107605153251"></a><a name="en-us_topic_0015479905_p46107605153251"></a>Monitored Object</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.7.1.6"><p id="en-us_topic_0015479905_p1822752020370"><a name="en-us_topic_0015479905_p1822752020370"></a><a name="en-us_topic_0015479905_p1822752020370"></a>Monitoring Period (Raw Data)</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0015479905_row43728521153251"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p52349342153251"><a name="p52349342153251"></a><a name="p52349342153251"></a>api_calls</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0015479905_p1159693894434"><a name="en-us_topic_0015479905_p1159693894434"></a><a name="en-us_topic_0015479905_p1159693894434"></a>Requests</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0015479905_p6693675394434"><a name="en-us_topic_0015479905_p6693675394434"></a><a name="en-us_topic_0015479905_p6693675394434"></a>Number of times that the API has been called</p>
<p id="en-us_topic_0015479905_p144867303119"><a name="en-us_topic_0015479905_p144867303119"></a><a name="en-us_topic_0015479905_p144867303119"></a>Unit: Times/15 min</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.7.1.4 "><p id="p3518768153251"><a name="p3518768153251"></a><a name="p3518768153251"></a>≥ 0 times/15 min</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.7.1.5 "><p id="p16584791153251"><a name="p16584791153251"></a><a name="p16584791153251"></a>API</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0015479905_p098717269377"><a name="en-us_topic_0015479905_p098717269377"></a><a name="en-us_topic_0015479905_p098717269377"></a>15 minutes</p>
</td>
</tr>
<tr id="en-us_topic_0015479905_row15045394153251"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p10717405153251"><a name="p10717405153251"></a><a name="p10717405153251"></a>error_4xx</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0015479905_p874935794434"><a name="en-us_topic_0015479905_p874935794434"></a><a name="en-us_topic_0015479905_p874935794434"></a>4xx Errors</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0015479905_p3760929194434"><a name="en-us_topic_0015479905_p3760929194434"></a><a name="en-us_topic_0015479905_p3760929194434"></a>Number of times that the API returns a 4xx error</p>
<p id="en-us_topic_0015479905_p598819511012"><a name="en-us_topic_0015479905_p598819511012"></a><a name="en-us_topic_0015479905_p598819511012"></a>Unit: Times/15 min</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.7.1.4 "><p id="p5025880153251"><a name="p5025880153251"></a><a name="p5025880153251"></a>≥ 0 times/15 min</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.7.1.5 "><p id="p86261746473"><a name="p86261746473"></a><a name="p86261746473"></a>API</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0015479905_p6251227163718"><a name="en-us_topic_0015479905_p6251227163718"></a><a name="en-us_topic_0015479905_p6251227163718"></a>15 minutes</p>
</td>
</tr>
<tr id="en-us_topic_0015479905_row39987979153251"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p17800853153251"><a name="p17800853153251"></a><a name="p17800853153251"></a>error_5xx</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0015479905_p3675668594434"><a name="en-us_topic_0015479905_p3675668594434"></a><a name="en-us_topic_0015479905_p3675668594434"></a>5xx Errors</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0015479905_p2450149994434"><a name="en-us_topic_0015479905_p2450149994434"></a><a name="en-us_topic_0015479905_p2450149994434"></a>Number of times that the API returns a 5xx error</p>
<p id="en-us_topic_0015479905_p1018215817110"><a name="en-us_topic_0015479905_p1018215817110"></a><a name="en-us_topic_0015479905_p1018215817110"></a>Unit: Times/15 min</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.7.1.4 "><p id="p35387863153251"><a name="p35387863153251"></a><a name="p35387863153251"></a>≥ 0 times/15 min</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.7.1.5 "><p id="p111361988474"><a name="p111361988474"></a><a name="p111361988474"></a>API</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0015479905_p176442718374"><a name="en-us_topic_0015479905_p176442718374"></a><a name="en-us_topic_0015479905_p176442718374"></a>15 minutes</p>
</td>
</tr>
<tr id="en-us_topic_0015479905_row27949047153251"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p49280315153251"><a name="p49280315153251"></a><a name="p49280315153251"></a>error_503</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0015479905_p1063533594434"><a name="en-us_topic_0015479905_p1063533594434"></a><a name="en-us_topic_0015479905_p1063533594434"></a>503 Errors</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0015479905_p5615582494434"><a name="en-us_topic_0015479905_p5615582494434"></a><a name="en-us_topic_0015479905_p5615582494434"></a>Number of times that the API returns a 503 error</p>
<p id="en-us_topic_0015479905_p11925192323"><a name="en-us_topic_0015479905_p11925192323"></a><a name="en-us_topic_0015479905_p11925192323"></a>Unit: Times/15 min</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.7.1.4 "><p id="p10380530153251"><a name="p10380530153251"></a><a name="p10380530153251"></a>≥ 0 times/15 min</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.7.1.5 "><p id="p1413619814470"><a name="p1413619814470"></a><a name="p1413619814470"></a>API</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0015479905_p174441928133710"><a name="en-us_topic_0015479905_p174441928133710"></a><a name="en-us_topic_0015479905_p174441928133710"></a>15 minutes</p>
</td>
</tr>
<tr id="en-us_topic_0015479905_row51214241153251"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p54712841153251"><a name="p54712841153251"></a><a name="p54712841153251"></a>latency_median</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0015479905_p118873794434"><a name="en-us_topic_0015479905_p118873794434"></a><a name="en-us_topic_0015479905_p118873794434"></a>Average Latency</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0015479905_p2917884594434"><a name="en-us_topic_0015479905_p2917884594434"></a><a name="en-us_topic_0015479905_p2917884594434"></a>Average latency of the API</p>
<p id="en-us_topic_0015479905_p872819171516"><a name="en-us_topic_0015479905_p872819171516"></a><a name="en-us_topic_0015479905_p872819171516"></a>Unit: ms</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.7.1.4 "><p id="p53993267153251"><a name="p53993267153251"></a><a name="p53993267153251"></a>≥ 0 ms</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.7.1.5 "><p id="p247516104471"><a name="p247516104471"></a><a name="p247516104471"></a>API</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0015479905_p14485328193714"><a name="en-us_topic_0015479905_p14485328193714"></a><a name="en-us_topic_0015479905_p14485328193714"></a>15 minutes</p>
</td>
</tr>
<tr id="en-us_topic_0015479905_row35298012153251"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p40566722153251"><a name="p40566722153251"></a><a name="p40566722153251"></a>latency_max</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0015479905_p6497757494434"><a name="en-us_topic_0015479905_p6497757494434"></a><a name="en-us_topic_0015479905_p6497757494434"></a>Maximum Latency</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0015479905_p2869216194434"><a name="en-us_topic_0015479905_p2869216194434"></a><a name="en-us_topic_0015479905_p2869216194434"></a>Maximum latency of the API</p>
<p id="en-us_topic_0015479905_p9721823015"><a name="en-us_topic_0015479905_p9721823015"></a><a name="en-us_topic_0015479905_p9721823015"></a>Unit: ms</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.7.1.4 "><p id="p29705006153251"><a name="p29705006153251"></a><a name="p29705006153251"></a>≥ 0 ms</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.7.1.5 "><p id="p947541034713"><a name="p947541034713"></a><a name="p947541034713"></a>API</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0015479905_p252462893713"><a name="en-us_topic_0015479905_p252462893713"></a><a name="en-us_topic_0015479905_p252462893713"></a>15 minutes</p>
</td>
</tr>
</tbody>
</table>

