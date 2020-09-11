# API Calls Metrics<a name="EN-US_TOPIC_0171212570"></a>

## Function<a name="section59820001153251"></a>

This topic describes metrics reported by API Calls to Cloud Eye as well as their namespaces and dimensions. You can use APIs provided by Cloud Eye to query the metrics of the monitored object and alarms generated for API Calls.

## Namespace<a name="section55128484153251"></a>

SYS.APIGATEWAY

## Metrics<a name="section57564324153251"></a>

<a name="table32198700153251"></a>
<table><thead align="left"><tr id="row43554686153251"><th class="cellrowborder" valign="top" width="20.007999200079997%" id="mcps1.1.6.1.1"><p id="p38268712153251"><a name="p38268712153251"></a><a name="p38268712153251"></a>Metric</p>
</th>
<th class="cellrowborder" valign="top" width="19.528047195280475%" id="mcps1.1.6.1.2"><p id="p12757995153251"><a name="p12757995153251"></a><a name="p12757995153251"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="34.73652634736527%" id="mcps1.1.6.1.3"><p id="p26764654153251"><a name="p26764654153251"></a><a name="p26764654153251"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="11.818818118188183%" id="mcps1.1.6.1.4"><p id="p20453337153251"><a name="p20453337153251"></a><a name="p20453337153251"></a>Value Range</p>
</th>
<th class="cellrowborder" valign="top" width="13.908609139086096%" id="mcps1.1.6.1.5"><p id="p46107605153251"><a name="p46107605153251"></a><a name="p46107605153251"></a>Monitored Object</p>
</th>
</tr>
</thead>
<tbody><tr id="row43728521153251"><td class="cellrowborder" valign="top" width="20.007999200079997%" headers="mcps1.1.6.1.1 "><p id="p52349342153251"><a name="p52349342153251"></a><a name="p52349342153251"></a>api_calls</p>
</td>
<td class="cellrowborder" valign="top" width="19.528047195280475%" headers="mcps1.1.6.1.2 "><p id="p12438332153251"><a name="p12438332153251"></a><a name="p12438332153251"></a>Requests</p>
</td>
<td class="cellrowborder" valign="top" width="34.73652634736527%" headers="mcps1.1.6.1.3 "><p id="p871946153251"><a name="p871946153251"></a><a name="p871946153251"></a>Number of times that the API has been called</p>
<p id="p252451418514"><a name="p252451418514"></a><a name="p252451418514"></a>Unit: Times/15 min</p>
</td>
<td class="cellrowborder" valign="top" width="11.818818118188183%" headers="mcps1.1.6.1.4 "><p id="p3518768153251"><a name="p3518768153251"></a><a name="p3518768153251"></a>≥ 0 times/15 min</p>
</td>
<td class="cellrowborder" valign="top" width="13.908609139086096%" headers="mcps1.1.6.1.5 "><p id="p16584791153251"><a name="p16584791153251"></a><a name="p16584791153251"></a>API</p>
</td>
</tr>
<tr id="row15045394153251"><td class="cellrowborder" valign="top" width="20.007999200079997%" headers="mcps1.1.6.1.1 "><p id="p10717405153251"><a name="p10717405153251"></a><a name="p10717405153251"></a>error_4xx</p>
</td>
<td class="cellrowborder" valign="top" width="19.528047195280475%" headers="mcps1.1.6.1.2 "><p id="p62803452153251"><a name="p62803452153251"></a><a name="p62803452153251"></a>4xx Errors</p>
</td>
<td class="cellrowborder" valign="top" width="34.73652634736527%" headers="mcps1.1.6.1.3 "><p id="p53914840153251"><a name="p53914840153251"></a><a name="p53914840153251"></a>Number of times that the API returns a 4xx error</p>
<p id="p16857716115110"><a name="p16857716115110"></a><a name="p16857716115110"></a>Unit: Times/15 min</p>
</td>
<td class="cellrowborder" valign="top" width="11.818818118188183%" headers="mcps1.1.6.1.4 "><p id="p5025880153251"><a name="p5025880153251"></a><a name="p5025880153251"></a>≥ 0 times/15 min</p>
</td>
<td class="cellrowborder" valign="top" width="13.908609139086096%" headers="mcps1.1.6.1.5 "><p id="p86261746473"><a name="p86261746473"></a><a name="p86261746473"></a>API</p>
</td>
</tr>
<tr id="row39987979153251"><td class="cellrowborder" valign="top" width="20.007999200079997%" headers="mcps1.1.6.1.1 "><p id="p17800853153251"><a name="p17800853153251"></a><a name="p17800853153251"></a>error_5xx</p>
</td>
<td class="cellrowborder" valign="top" width="19.528047195280475%" headers="mcps1.1.6.1.2 "><p id="p32583008153251"><a name="p32583008153251"></a><a name="p32583008153251"></a>5xx Errors</p>
</td>
<td class="cellrowborder" valign="top" width="34.73652634736527%" headers="mcps1.1.6.1.3 "><p id="p21978004153251"><a name="p21978004153251"></a><a name="p21978004153251"></a>Number of times that the API returns a 5xx error</p>
<p id="p878392016516"><a name="p878392016516"></a><a name="p878392016516"></a>Unit: Times/15 min</p>
</td>
<td class="cellrowborder" valign="top" width="11.818818118188183%" headers="mcps1.1.6.1.4 "><p id="p35387863153251"><a name="p35387863153251"></a><a name="p35387863153251"></a>≥ 0 times/15 min</p>
</td>
<td class="cellrowborder" valign="top" width="13.908609139086096%" headers="mcps1.1.6.1.5 "><p id="p111361988474"><a name="p111361988474"></a><a name="p111361988474"></a>API</p>
</td>
</tr>
<tr id="row27949047153251"><td class="cellrowborder" valign="top" width="20.007999200079997%" headers="mcps1.1.6.1.1 "><p id="p49280315153251"><a name="p49280315153251"></a><a name="p49280315153251"></a>error_503</p>
</td>
<td class="cellrowborder" valign="top" width="19.528047195280475%" headers="mcps1.1.6.1.2 "><p id="p32282572153251"><a name="p32282572153251"></a><a name="p32282572153251"></a>503 Errors</p>
</td>
<td class="cellrowborder" valign="top" width="34.73652634736527%" headers="mcps1.1.6.1.3 "><p id="p64751505153251"><a name="p64751505153251"></a><a name="p64751505153251"></a>Number of times that the API returns a 503 error</p>
<p id="p1154112325117"><a name="p1154112325117"></a><a name="p1154112325117"></a>Unit: Times/15 min</p>
</td>
<td class="cellrowborder" valign="top" width="11.818818118188183%" headers="mcps1.1.6.1.4 "><p id="p10380530153251"><a name="p10380530153251"></a><a name="p10380530153251"></a>≥ 0 times/15 min</p>
</td>
<td class="cellrowborder" valign="top" width="13.908609139086096%" headers="mcps1.1.6.1.5 "><p id="p1413619814470"><a name="p1413619814470"></a><a name="p1413619814470"></a>API</p>
</td>
</tr>
<tr id="row51214241153251"><td class="cellrowborder" valign="top" width="20.007999200079997%" headers="mcps1.1.6.1.1 "><p id="p54712841153251"><a name="p54712841153251"></a><a name="p54712841153251"></a>latency_median</p>
</td>
<td class="cellrowborder" valign="top" width="19.528047195280475%" headers="mcps1.1.6.1.2 "><p id="p2555113153251"><a name="p2555113153251"></a><a name="p2555113153251"></a>Average Latency</p>
</td>
<td class="cellrowborder" valign="top" width="34.73652634736527%" headers="mcps1.1.6.1.3 "><p id="p65323867192225"><a name="p65323867192225"></a><a name="p65323867192225"></a>Average latency of the API</p>
<p id="p5637610153251"><a name="p5637610153251"></a><a name="p5637610153251"></a></p>
<p id="p16838924195118"><a name="p16838924195118"></a><a name="p16838924195118"></a>Unit: ms</p>
</td>
<td class="cellrowborder" valign="top" width="11.818818118188183%" headers="mcps1.1.6.1.4 "><p id="p12562183616527"><a name="p12562183616527"></a><a name="p12562183616527"></a>≥ 0 ms</p>
</td>
<td class="cellrowborder" valign="top" width="13.908609139086096%" headers="mcps1.1.6.1.5 "><p id="p247516104471"><a name="p247516104471"></a><a name="p247516104471"></a>API</p>
</td>
</tr>
<tr id="row35298012153251"><td class="cellrowborder" valign="top" width="20.007999200079997%" headers="mcps1.1.6.1.1 "><p id="p40566722153251"><a name="p40566722153251"></a><a name="p40566722153251"></a>latency_max</p>
</td>
<td class="cellrowborder" valign="top" width="19.528047195280475%" headers="mcps1.1.6.1.2 "><p id="p64679020153251"><a name="p64679020153251"></a><a name="p64679020153251"></a>Maximum Latency</p>
</td>
<td class="cellrowborder" valign="top" width="34.73652634736527%" headers="mcps1.1.6.1.3 "><p id="p23557821192232"><a name="p23557821192232"></a><a name="p23557821192232"></a>Maximum latency of the API</p>
<p id="p4509250153251"><a name="p4509250153251"></a><a name="p4509250153251"></a></p>
</td>
<td class="cellrowborder" valign="top" width="11.818818118188183%" headers="mcps1.1.6.1.4 "><p id="p15562143610527"><a name="p15562143610527"></a><a name="p15562143610527"></a>≥ 0 ms</p>
</td>
<td class="cellrowborder" valign="top" width="13.908609139086096%" headers="mcps1.1.6.1.5 "><p id="p947541034713"><a name="p947541034713"></a><a name="p947541034713"></a>API</p>
</td>
</tr>
</tbody>
</table>

## Dimension<a name="section45895235153251"></a>

<a name="table26526577153251"></a>
<table><thead align="left"><tr id="row46969777153251"><th class="cellrowborder" valign="top" width="40.400000000000006%" id="mcps1.1.3.1.1"><p id="p46455583153251"><a name="p46455583153251"></a><a name="p46455583153251"></a>Key</p>
</th>
<th class="cellrowborder" valign="top" width="59.599999999999994%" id="mcps1.1.3.1.2"><p id="p4805882153251"><a name="p4805882153251"></a><a name="p4805882153251"></a>Value</p>
</th>
</tr>
</thead>
<tbody><tr id="row53732137153251"><td class="cellrowborder" valign="top" width="40.400000000000006%" headers="mcps1.1.3.1.1 "><p id="p57335829153251"><a name="p57335829153251"></a><a name="p57335829153251"></a>api_id</p>
</td>
<td class="cellrowborder" valign="top" width="59.599999999999994%" headers="mcps1.1.3.1.2 "><p id="p13690533153251"><a name="p13690533153251"></a><a name="p13690533153251"></a>APIs</p>
</td>
</tr>
</tbody>
</table>

