# Monitoring Metrics<a name="waf_01_0092"></a>

## Function Description<a name="section1563963116197"></a>

This section describes monitoring metrics reported by WAF to Cloud Eye as well as their namespaces and dimensions. You can use the management console or APIs provided by Cloud Eye to query the monitoring metrics of the monitored object and alarms generated for WAF.

## Namespace<a name="section20825105342312"></a>

SYS.WAF

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>A namespace is an abstract collection of resources and objects. Multiple namespaces can be created in a single cluster, but they are isolated from each other. This enables namespaces to share the same cluster services without affecting each other.  

## Monitoring Metrics<a name="section678433510243"></a>

**Table  1**  Monitoring metrics

<a name="table6436153422511"></a>
<table><thead align="left"><tr id="row74379348253"><th class="cellrowborder" valign="top" width="12.807438512297539%" id="mcps1.2.7.1.1"><p id="p1215973616615"><a name="p1215973616615"></a><a name="p1215973616615"></a>Metric ID</p>
</th>
<th class="cellrowborder" valign="top" width="13.20735852829434%" id="mcps1.2.7.1.2"><p id="p74371634132514"><a name="p74371634132514"></a><a name="p74371634132514"></a>Metric Name</p>
</th>
<th class="cellrowborder" valign="top" width="18.49630073985203%" id="mcps1.2.7.1.3"><p id="p12437134112516"><a name="p12437134112516"></a><a name="p12437134112516"></a>Meaning</p>
</th>
<th class="cellrowborder" valign="top" width="18.49630073985203%" id="mcps1.2.7.1.4"><p id="p443718344250"><a name="p443718344250"></a><a name="p443718344250"></a>Value Range</p>
</th>
<th class="cellrowborder" valign="top" width="18.49630073985203%" id="mcps1.2.7.1.5"><p id="p94371734132518"><a name="p94371734132518"></a><a name="p94371734132518"></a>Measurement Object &amp; Dimension</p>
</th>
<th class="cellrowborder" valign="top" width="18.49630073985203%" id="mcps1.2.7.1.6"><p id="p11437934112513"><a name="p11437934112513"></a><a name="p11437934112513"></a>Monitoring Interval (Raw Data)</p>
</th>
</tr>
</thead>
<tbody><tr id="row3437034182519"><td class="cellrowborder" valign="top" width="12.807438512297539%" headers="mcps1.2.7.1.1 "><p id="p32424470616"><a name="p32424470616"></a><a name="p32424470616"></a>attacks</p>
</td>
<td class="cellrowborder" valign="top" width="13.20735852829434%" headers="mcps1.2.7.1.2 "><p id="p15437123412258"><a name="p15437123412258"></a><a name="p15437123412258"></a>attacks</p>
</td>
<td class="cellrowborder" valign="top" width="18.49630073985203%" headers="mcps1.2.7.1.3 "><p id="p66979856105927"><a name="p66979856105927"></a><a name="p66979856105927"></a>Total number of attacks on a protected domain name in a given period</p>
</td>
<td class="cellrowborder" valign="top" width="18.49630073985203%" headers="mcps1.2.7.1.4 "><p id="p44238505105853"><a name="p44238505105853"></a><a name="p44238505105853"></a>&gt;= 0 count</p>
</td>
<td class="cellrowborder" valign="top" width="18.49630073985203%" headers="mcps1.2.7.1.5 "><p id="p26549182105853"><a name="p26549182105853"></a><a name="p26549182105853"></a>Measurement object: protected domain name</p>
<p id="p1646853032815"><a name="p1646853032815"></a><a name="p1646853032815"></a>Dimension: waf_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="18.49630073985203%" headers="mcps1.2.7.1.6 "><p id="p94372034202515"><a name="p94372034202515"></a><a name="p94372034202515"></a>5 minutes</p>
</td>
</tr>
<tr id="row1943793410258"><td class="cellrowborder" valign="top" width="12.807438512297539%" headers="mcps1.2.7.1.1 "><p id="p169489279614"><a name="p169489279614"></a><a name="p169489279614"></a>requests</p>
</td>
<td class="cellrowborder" valign="top" width="13.20735852829434%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0015479905_p156401051664"><a name="en-us_topic_0015479905_p156401051664"></a><a name="en-us_topic_0015479905_p156401051664"></a>requests</p>
</td>
<td class="cellrowborder" valign="top" width="18.49630073985203%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0015479905_p588890221664"><a name="en-us_topic_0015479905_p588890221664"></a><a name="en-us_topic_0015479905_p588890221664"></a>Total number of requests for a protected domain name in a given period</p>
</td>
<td class="cellrowborder" valign="top" width="18.49630073985203%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0015479905_p52815001664"><a name="en-us_topic_0015479905_p52815001664"></a><a name="en-us_topic_0015479905_p52815001664"></a>&gt;= 0 count</p>
</td>
<td class="cellrowborder" valign="top" width="18.49630073985203%" headers="mcps1.2.7.1.5 "><p id="p19542104152815"><a name="p19542104152815"></a><a name="p19542104152815"></a>Measurement object: protected domain name</p>
<p id="p13542114111281"><a name="p13542114111281"></a><a name="p13542114111281"></a>Dimension: waf_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="18.49630073985203%" headers="mcps1.2.7.1.6 "><p id="p1643717345255"><a name="p1643717345255"></a><a name="p1643717345255"></a>5 minutes</p>
</td>
</tr>
</tbody>
</table>

## Dimensions<a name="section788316593818"></a>

**Table  2**  Dimensions

<a name="table1398773714387"></a>
<table><thead align="left"><tr id="row169885372386"><th class="cellrowborder" valign="top" width="38.11%" id="mcps1.2.3.1.1"><p id="p119889378384"><a name="p119889378384"></a><a name="p119889378384"></a>Key</p>
</th>
<th class="cellrowborder" valign="top" width="61.89%" id="mcps1.2.3.1.2"><p id="p11988937193816"><a name="p11988937193816"></a><a name="p11988937193816"></a>Value</p>
</th>
</tr>
</thead>
<tbody><tr id="row59889379385"><td class="cellrowborder" valign="top" width="38.11%" headers="mcps1.2.3.1.1 "><p id="p189882371380"><a name="p189882371380"></a><a name="p189882371380"></a>waf_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="61.89%" headers="mcps1.2.3.1.2 "><p id="p598803711386"><a name="p598803711386"></a><a name="p598803711386"></a>Domain name ID</p>
</td>
</tr>
</tbody>
</table>

