# Monitoring Metrics<a name="EN-US_TOPIC_0200894988"></a>

## Function Description<a name="en-us_topic_0200878955_section1563963116197"></a>

This section describes monitoring metrics reported by WAF to Cloud Eye as well as their namespaces and dimensions. You can use the management console or APIs provided by Cloud Eye to query the monitoring metrics of the monitored object and alarms generated for WAF.

## Namespace<a name="en-us_topic_0200878955_section20825105342312"></a>

SYS.WAF

## Monitoring Metrics<a name="en-us_topic_0200878955_section678433510243"></a>

**Table  1**  Monitoring metrics

<a name="en-us_topic_0200878955_table6436153422511"></a>
<table><thead align="left"><tr id="en-us_topic_0200878955_row74379348253"><th class="cellrowborder" valign="top" width="12.807438512297539%" id="mcps1.2.7.1.1"><p id="en-us_topic_0200878955_p1215973616615"><a name="en-us_topic_0200878955_p1215973616615"></a><a name="en-us_topic_0200878955_p1215973616615"></a>Metric ID</p>
</th>
<th class="cellrowborder" valign="top" width="13.20735852829434%" id="mcps1.2.7.1.2"><p id="en-us_topic_0200878955_p74371634132514"><a name="en-us_topic_0200878955_p74371634132514"></a><a name="en-us_topic_0200878955_p74371634132514"></a>Metric Name</p>
</th>
<th class="cellrowborder" valign="top" width="18.49630073985203%" id="mcps1.2.7.1.3"><p id="en-us_topic_0200878955_p12437134112516"><a name="en-us_topic_0200878955_p12437134112516"></a><a name="en-us_topic_0200878955_p12437134112516"></a>Meaning</p>
</th>
<th class="cellrowborder" valign="top" width="18.49630073985203%" id="mcps1.2.7.1.4"><p id="en-us_topic_0200878955_p443718344250"><a name="en-us_topic_0200878955_p443718344250"></a><a name="en-us_topic_0200878955_p443718344250"></a>Value Range</p>
</th>
<th class="cellrowborder" valign="top" width="18.49630073985203%" id="mcps1.2.7.1.5"><p id="en-us_topic_0200878955_p94371734132518"><a name="en-us_topic_0200878955_p94371734132518"></a><a name="en-us_topic_0200878955_p94371734132518"></a>Measurement Object &amp; Dimension</p>
</th>
<th class="cellrowborder" valign="top" width="18.49630073985203%" id="mcps1.2.7.1.6"><p id="en-us_topic_0200878955_p11437934112513"><a name="en-us_topic_0200878955_p11437934112513"></a><a name="en-us_topic_0200878955_p11437934112513"></a>Monitoring Interval (Raw Data)</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0200878955_row3437034182519"><td class="cellrowborder" valign="top" width="12.807438512297539%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0200878955_p32424470616"><a name="en-us_topic_0200878955_p32424470616"></a><a name="en-us_topic_0200878955_p32424470616"></a>attacks</p>
</td>
<td class="cellrowborder" valign="top" width="13.20735852829434%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0200878955_p15437123412258"><a name="en-us_topic_0200878955_p15437123412258"></a><a name="en-us_topic_0200878955_p15437123412258"></a>attacks</p>
</td>
<td class="cellrowborder" valign="top" width="18.49630073985203%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0200878955_p66979856105927"><a name="en-us_topic_0200878955_p66979856105927"></a><a name="en-us_topic_0200878955_p66979856105927"></a>Total number of attacks on a protected domain name in a given period</p>
</td>
<td class="cellrowborder" valign="top" width="18.49630073985203%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0200878955_p44238505105853"><a name="en-us_topic_0200878955_p44238505105853"></a><a name="en-us_topic_0200878955_p44238505105853"></a>&gt;= 0 count</p>
</td>
<td class="cellrowborder" valign="top" width="18.49630073985203%" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0200878955_p26549182105853"><a name="en-us_topic_0200878955_p26549182105853"></a><a name="en-us_topic_0200878955_p26549182105853"></a>Measurement object: protected domain name</p>
<p id="en-us_topic_0200878955_p1646853032815"><a name="en-us_topic_0200878955_p1646853032815"></a><a name="en-us_topic_0200878955_p1646853032815"></a>Dimension: waf_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="18.49630073985203%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0200878955_p94372034202515"><a name="en-us_topic_0200878955_p94372034202515"></a><a name="en-us_topic_0200878955_p94372034202515"></a>5 minutes</p>
</td>
</tr>
<tr id="en-us_topic_0200878955_row1943793410258"><td class="cellrowborder" valign="top" width="12.807438512297539%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0200878955_p169489279614"><a name="en-us_topic_0200878955_p169489279614"></a><a name="en-us_topic_0200878955_p169489279614"></a>requests</p>
</td>
<td class="cellrowborder" valign="top" width="13.20735852829434%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0200878955_en-us_topic_0015479905_p156401051664"><a name="en-us_topic_0200878955_en-us_topic_0015479905_p156401051664"></a><a name="en-us_topic_0200878955_en-us_topic_0015479905_p156401051664"></a>requests</p>
</td>
<td class="cellrowborder" valign="top" width="18.49630073985203%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0200878955_en-us_topic_0015479905_p588890221664"><a name="en-us_topic_0200878955_en-us_topic_0015479905_p588890221664"></a><a name="en-us_topic_0200878955_en-us_topic_0015479905_p588890221664"></a>Total number of requests for a protected domain name in a given period</p>
</td>
<td class="cellrowborder" valign="top" width="18.49630073985203%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0200878955_en-us_topic_0015479905_p52815001664"><a name="en-us_topic_0200878955_en-us_topic_0015479905_p52815001664"></a><a name="en-us_topic_0200878955_en-us_topic_0015479905_p52815001664"></a>&gt;= 0 count</p>
</td>
<td class="cellrowborder" valign="top" width="18.49630073985203%" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0200878955_p19542104152815"><a name="en-us_topic_0200878955_p19542104152815"></a><a name="en-us_topic_0200878955_p19542104152815"></a>Measurement object: protected domain name</p>
<p id="en-us_topic_0200878955_p13542114111281"><a name="en-us_topic_0200878955_p13542114111281"></a><a name="en-us_topic_0200878955_p13542114111281"></a>Dimension: waf_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="18.49630073985203%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0200878955_p1643717345255"><a name="en-us_topic_0200878955_p1643717345255"></a><a name="en-us_topic_0200878955_p1643717345255"></a>5 minutes</p>
</td>
</tr>
</tbody>
</table>

## Dimensions<a name="en-us_topic_0200878955_section788316593818"></a>

**Table  2**  Dimensions

<a name="en-us_topic_0200878955_table1398773714387"></a>
<table><thead align="left"><tr id="en-us_topic_0200878955_row169885372386"><th class="cellrowborder" valign="top" width="38.11%" id="mcps1.2.3.1.1"><p id="en-us_topic_0200878955_p119889378384"><a name="en-us_topic_0200878955_p119889378384"></a><a name="en-us_topic_0200878955_p119889378384"></a>Key</p>
</th>
<th class="cellrowborder" valign="top" width="61.89%" id="mcps1.2.3.1.2"><p id="en-us_topic_0200878955_p11988937193816"><a name="en-us_topic_0200878955_p11988937193816"></a><a name="en-us_topic_0200878955_p11988937193816"></a>Value</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0200878955_row59889379385"><td class="cellrowborder" valign="top" width="38.11%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0200878955_p189882371380"><a name="en-us_topic_0200878955_p189882371380"></a><a name="en-us_topic_0200878955_p189882371380"></a>waf_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="61.89%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0200878955_p598803711386"><a name="en-us_topic_0200878955_p598803711386"></a><a name="en-us_topic_0200878955_p598803711386"></a>Domain name ID</p>
</td>
</tr>
</tbody>
</table>

