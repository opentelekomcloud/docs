# VPC Monitoring Metrics<a name="vpc_api_0010"></a>

## Description<a name="section45043704193247"></a>

This section describes monitoring metrics reported by VPC to Cloud Eye as well as their namespaces and dimensions. You can use APIs provided by Cloud Eye to query the monitoring metrics of the monitored object and alarms generated for VPC.

## Namespace<a name="section20626347193247"></a>

SYS.VPC

## Metrics<a name="section4222089193247"></a>

**Table  1**  EIP and Bandwidth metrics

<a name="table6444895193247"></a>
<table><thead align="left"><tr id="en-us_topic_0118498910_en-us_topic_0024607920_row17328334193247"><th class="cellrowborder" valign="top" width="14.98850114988501%" id="mcps1.2.7.1.1"><p id="en-us_topic_0118498910_en-us_topic_0024607920_p61417783193247"><a name="en-us_topic_0118498910_en-us_topic_0024607920_p61417783193247"></a><a name="en-us_topic_0118498910_en-us_topic_0024607920_p61417783193247"></a>Metric</p>
</th>
<th class="cellrowborder" valign="top" width="10.528947105289472%" id="mcps1.2.7.1.2"><p id="en-us_topic_0118498910_en-us_topic_0024607920_p8784488193247"><a name="en-us_topic_0118498910_en-us_topic_0024607920_p8784488193247"></a><a name="en-us_topic_0118498910_en-us_topic_0024607920_p8784488193247"></a>Metric Name</p>
</th>
<th class="cellrowborder" valign="top" width="21.697830216978303%" id="mcps1.2.7.1.3"><p id="en-us_topic_0118498910_en-us_topic_0024607920_p40454922193247"><a name="en-us_topic_0118498910_en-us_topic_0024607920_p40454922193247"></a><a name="en-us_topic_0118498910_en-us_topic_0024607920_p40454922193247"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="12.278772122787721%" id="mcps1.2.7.1.4"><p id="en-us_topic_0118498910_en-us_topic_0024607920_p55623236193247"><a name="en-us_topic_0118498910_en-us_topic_0024607920_p55623236193247"></a><a name="en-us_topic_0118498910_en-us_topic_0024607920_p55623236193247"></a>Value Range</p>
</th>
<th class="cellrowborder" valign="top" width="21.347865213478652%" id="mcps1.2.7.1.5"><p id="en-us_topic_0118498910_en-us_topic_0024607920_p9188287193247"><a name="en-us_topic_0118498910_en-us_topic_0024607920_p9188287193247"></a><a name="en-us_topic_0118498910_en-us_topic_0024607920_p9188287193247"></a>Measurement Object &amp; Dimension</p>
</th>
<th class="cellrowborder" valign="top" width="19.15808419158084%" id="mcps1.2.7.1.6"><p id="en-us_topic_0118498910_p116611739175520"><a name="en-us_topic_0118498910_p116611739175520"></a><a name="en-us_topic_0118498910_p116611739175520"></a><strong id="en-us_topic_0118498910_b63113175012"><a name="en-us_topic_0118498910_b63113175012"></a><a name="en-us_topic_0118498910_b63113175012"></a>Monitoring Interval (Raw Data)</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0118498910_en-us_topic_0024607920_row173875718321"><td class="cellrowborder" valign="top" width="14.98850114988501%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0118498910_en-us_topic_0024607920_p131326819339"><a name="en-us_topic_0118498910_en-us_topic_0024607920_p131326819339"></a><a name="en-us_topic_0118498910_en-us_topic_0024607920_p131326819339"></a>upstream_bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="10.528947105289472%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0118498910_en-us_topic_0024607920_p7133182333"><a name="en-us_topic_0118498910_en-us_topic_0024607920_p7133182333"></a><a name="en-us_topic_0118498910_en-us_topic_0024607920_p7133182333"></a>Outbound Bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="21.697830216978303%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0118498910_p179215408321"><a name="en-us_topic_0118498910_p179215408321"></a><a name="en-us_topic_0118498910_p179215408321"></a>Network rate of outbound traffic </p>
<p id="en-us_topic_0118498910_p478910501515"><a name="en-us_topic_0118498910_p478910501515"></a><a name="en-us_topic_0118498910_p478910501515"></a>Unit: bit/s</p>
</td>
<td class="cellrowborder" valign="top" width="12.278772122787721%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0118498910_p16856133111520"><a name="en-us_topic_0118498910_p16856133111520"></a><a name="en-us_topic_0118498910_p16856133111520"></a>≥ 0 bit/s</p>
</td>
<td class="cellrowborder" valign="top" width="21.347865213478652%" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0118498910_p14941182731011"><a name="en-us_topic_0118498910_p14941182731011"></a><a name="en-us_topic_0118498910_p14941182731011"></a>Object: Bandwidth or EIP</p>
<p id="en-us_topic_0118498910_p2094120273109"><a name="en-us_topic_0118498910_p2094120273109"></a><a name="en-us_topic_0118498910_p2094120273109"></a>Dimension<sup id="en-us_topic_0118498910_sup996111317111"><a name="en-us_topic_0118498910_sup996111317111"></a><a name="en-us_topic_0118498910_sup996111317111"></a>a</sup>:</p>
<p id="en-us_topic_0118498910_p394132711018"><a name="en-us_topic_0118498910_p394132711018"></a><a name="en-us_topic_0118498910_p394132711018"></a>bandwidth_id,</p>
<p id="en-us_topic_0118498910_p994111271109"><a name="en-us_topic_0118498910_p994111271109"></a><a name="en-us_topic_0118498910_p994111271109"></a>publicip_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.15808419158084%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0118498910_p1166213397559"><a name="en-us_topic_0118498910_p1166213397559"></a><a name="en-us_topic_0118498910_p1166213397559"></a>1 minute</p>
</td>
</tr>
<tr id="en-us_topic_0118498910_en-us_topic_0024607920_row2515145493216"><td class="cellrowborder" valign="top" width="14.98850114988501%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0118498910_en-us_topic_0024607920_p131416813315"><a name="en-us_topic_0118498910_en-us_topic_0024607920_p131416813315"></a><a name="en-us_topic_0118498910_en-us_topic_0024607920_p131416813315"></a>downstream_bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="10.528947105289472%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0118498910_en-us_topic_0024607920_p18143178133311"><a name="en-us_topic_0118498910_en-us_topic_0024607920_p18143178133311"></a><a name="en-us_topic_0118498910_en-us_topic_0024607920_p18143178133311"></a>Inbound Bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="21.697830216978303%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0118498910_p14794440113211"><a name="en-us_topic_0118498910_p14794440113211"></a><a name="en-us_topic_0118498910_p14794440113211"></a>Network rate of inbound traffic </p>
<p id="en-us_topic_0118498910_p1561138115211"><a name="en-us_topic_0118498910_p1561138115211"></a><a name="en-us_topic_0118498910_p1561138115211"></a>Unit: bit/s</p>
</td>
<td class="cellrowborder" valign="top" width="12.278772122787721%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0118498910_p1785863115157"><a name="en-us_topic_0118498910_p1785863115157"></a><a name="en-us_topic_0118498910_p1785863115157"></a>≥ 0 bit/s</p>
</td>
<td class="cellrowborder" valign="top" width="21.347865213478652%" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0118498910_p19445113119103"><a name="en-us_topic_0118498910_p19445113119103"></a><a name="en-us_topic_0118498910_p19445113119103"></a>Object: Bandwidth or EIP</p>
<p id="en-us_topic_0118498910_p344623181019"><a name="en-us_topic_0118498910_p344623181019"></a><a name="en-us_topic_0118498910_p344623181019"></a>Dimension:</p>
<p id="en-us_topic_0118498910_p5446831151014"><a name="en-us_topic_0118498910_p5446831151014"></a><a name="en-us_topic_0118498910_p5446831151014"></a>bandwidth_id,</p>
<p id="en-us_topic_0118498910_p1544693151019"><a name="en-us_topic_0118498910_p1544693151019"></a><a name="en-us_topic_0118498910_p1544693151019"></a>publicip_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.15808419158084%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0118498910_p2662133918557"><a name="en-us_topic_0118498910_p2662133918557"></a><a name="en-us_topic_0118498910_p2662133918557"></a>1 minute</p>
</td>
</tr>
<tr id="en-us_topic_0118498910_row6251357113315"><td class="cellrowborder" valign="top" width="14.98850114988501%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0118498910_p199051635348"><a name="en-us_topic_0118498910_p199051635348"></a><a name="en-us_topic_0118498910_p199051635348"></a>up_stream</p>
</td>
<td class="cellrowborder" valign="top" width="10.528947105289472%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0118498910_p55042030141711"><a name="en-us_topic_0118498910_p55042030141711"></a><a name="en-us_topic_0118498910_p55042030141711"></a>Outbound Traffic</p>
</td>
<td class="cellrowborder" valign="top" width="21.697830216978303%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0118498910_p050623091713"><a name="en-us_topic_0118498910_p050623091713"></a><a name="en-us_topic_0118498910_p050623091713"></a>Network traffic going out of the cloud platform </p>
<p id="en-us_topic_0118498910_p29751350115210"><a name="en-us_topic_0118498910_p29751350115210"></a><a name="en-us_topic_0118498910_p29751350115210"></a>Unit: byte</p>
</td>
<td class="cellrowborder" valign="top" width="12.278772122787721%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0118498910_p55084302174"><a name="en-us_topic_0118498910_p55084302174"></a><a name="en-us_topic_0118498910_p55084302174"></a>≥ 0 bytes</p>
</td>
<td class="cellrowborder" valign="top" width="21.347865213478652%" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0118498910_p17314631101319"><a name="en-us_topic_0118498910_p17314631101319"></a><a name="en-us_topic_0118498910_p17314631101319"></a>Object: Bandwidth or EIP</p>
<p id="en-us_topic_0118498910_p731403115136"><a name="en-us_topic_0118498910_p731403115136"></a><a name="en-us_topic_0118498910_p731403115136"></a>Dimension:</p>
<p id="en-us_topic_0118498910_p4314163119134"><a name="en-us_topic_0118498910_p4314163119134"></a><a name="en-us_topic_0118498910_p4314163119134"></a>bandwidth_id,</p>
<p id="en-us_topic_0118498910_p15314163171315"><a name="en-us_topic_0118498910_p15314163171315"></a><a name="en-us_topic_0118498910_p15314163171315"></a>publicip_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.15808419158084%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0118498910_p966233925510"><a name="en-us_topic_0118498910_p966233925510"></a><a name="en-us_topic_0118498910_p966233925510"></a>1 minute</p>
</td>
</tr>
<tr id="en-us_topic_0118498910_row84711354143318"><td class="cellrowborder" valign="top" width="14.98850114988501%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0118498910_p29277317341"><a name="en-us_topic_0118498910_p29277317341"></a><a name="en-us_topic_0118498910_p29277317341"></a>down_stream</p>
</td>
<td class="cellrowborder" valign="top" width="10.528947105289472%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0118498910_p1451019302175"><a name="en-us_topic_0118498910_p1451019302175"></a><a name="en-us_topic_0118498910_p1451019302175"></a>Inbound Traffic</p>
</td>
<td class="cellrowborder" valign="top" width="21.697830216978303%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0118498910_p1051010308176"><a name="en-us_topic_0118498910_p1051010308176"></a><a name="en-us_topic_0118498910_p1051010308176"></a>Network traffic going into the cloud platform </p>
<p id="en-us_topic_0118498910_p8822319165320"><a name="en-us_topic_0118498910_p8822319165320"></a><a name="en-us_topic_0118498910_p8822319165320"></a>Unit: byte</p>
</td>
<td class="cellrowborder" valign="top" width="12.278772122787721%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0118498910_p15512163016174"><a name="en-us_topic_0118498910_p15512163016174"></a><a name="en-us_topic_0118498910_p15512163016174"></a>≥ 0 bytes</p>
</td>
<td class="cellrowborder" valign="top" width="21.347865213478652%" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0118498910_p2638143411134"><a name="en-us_topic_0118498910_p2638143411134"></a><a name="en-us_topic_0118498910_p2638143411134"></a>Object: Bandwidth or EIP</p>
<p id="en-us_topic_0118498910_p7638153412133"><a name="en-us_topic_0118498910_p7638153412133"></a><a name="en-us_topic_0118498910_p7638153412133"></a>Dimension:</p>
<p id="en-us_topic_0118498910_p15638113471319"><a name="en-us_topic_0118498910_p15638113471319"></a><a name="en-us_topic_0118498910_p15638113471319"></a>bandwidth_id,</p>
<p id="en-us_topic_0118498910_p196388346137"><a name="en-us_topic_0118498910_p196388346137"></a><a name="en-us_topic_0118498910_p196388346137"></a>publicip_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.15808419158084%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0118498910_p15662183910558"><a name="en-us_topic_0118498910_p15662183910558"></a><a name="en-us_topic_0118498910_p15662183910558"></a>1 minute</p>
</td>
</tr>
<tr id="en-us_topic_0118498910_row157931920151418"><td class="cellrowborder" colspan="6" valign="top" headers="mcps1.2.7.1.1 mcps1.2.7.1.2 mcps1.2.7.1.3 mcps1.2.7.1.4 mcps1.2.7.1.5 mcps1.2.7.1.6 "><div class="p" id="en-us_topic_0118498910_p13558154816619"><a name="en-us_topic_0118498910_p13558154816619"></a><a name="en-us_topic_0118498910_p13558154816619"></a><strong id="en-us_topic_0118498910_b154853505173"><a name="en-us_topic_0118498910_b154853505173"></a><a name="en-us_topic_0118498910_b154853505173"></a>a</strong>: If a service has multiple dimensions, all dimensions are mandatory when you use APIs to query the metrics.<a name="en-us_topic_0118498910_ul2558164815619"></a><a name="en-us_topic_0118498910_ul2558164815619"></a><ul id="en-us_topic_0118498910_ul2558164815619"><li>Query a monitoring metric: <p id="en-us_topic_0118498910_p196421916162213"><a name="en-us_topic_0118498910_p196421916162213"></a><a name="en-us_topic_0118498910_p196421916162213"></a>dim.0=bandwidth_id,530cd6b0-86d7-4818-837f-935f6a27414d&amp;dim.1=publicip_id,3773b058-5b4f-4366-9035-9bbd9964714a</p>
</li><li>Query monitoring metrics in batches:<p id="en-us_topic_0118498910_p125596481467"><a name="en-us_topic_0118498910_p125596481467"></a><a name="en-us_topic_0118498910_p125596481467"></a>"dimensions": [</p>
<p id="en-us_topic_0118498910_p1055919488614"><a name="en-us_topic_0118498910_p1055919488614"></a><a name="en-us_topic_0118498910_p1055919488614"></a>{</p>
<p id="en-us_topic_0118498910_p85595481617"><a name="en-us_topic_0118498910_p85595481617"></a><a name="en-us_topic_0118498910_p85595481617"></a>"name": "bandwidth_id",</p>
<p id="en-us_topic_0118498910_p2559748366"><a name="en-us_topic_0118498910_p2559748366"></a><a name="en-us_topic_0118498910_p2559748366"></a>"value": "530cd6b0-86d7-4818-837f-935f6a27414d"</p>
<p id="en-us_topic_0118498910_p1455913481360"><a name="en-us_topic_0118498910_p1455913481360"></a><a name="en-us_topic_0118498910_p1455913481360"></a>}</p>
<p id="en-us_topic_0118498910_p3559194818611"><a name="en-us_topic_0118498910_p3559194818611"></a><a name="en-us_topic_0118498910_p3559194818611"></a>{</p>
<p id="en-us_topic_0118498910_p1819695719711"><a name="en-us_topic_0118498910_p1819695719711"></a><a name="en-us_topic_0118498910_p1819695719711"></a>"name": "publicip_id",</p>
<p id="en-us_topic_0118498910_p125591481564"><a name="en-us_topic_0118498910_p125591481564"></a><a name="en-us_topic_0118498910_p125591481564"></a>"value": "3773b058-5b4f-4366-9035-9bbd9964714a"</p>
<p id="en-us_topic_0118498910_p12559448369"><a name="en-us_topic_0118498910_p12559448369"></a><a name="en-us_topic_0118498910_p12559448369"></a>}</p>
<p id="en-us_topic_0118498910_p855924816616"><a name="en-us_topic_0118498910_p855924816616"></a><a name="en-us_topic_0118498910_p855924816616"></a>],</p>
</li></ul>
</div>
</td>
</tr>
</tbody>
</table>

## Dimension<a name="section27751125193247"></a>

<a name="table30802540193247"></a>
<table><thead align="left"><tr id="row7692483193247"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p19111369193247"><a name="p19111369193247"></a><a name="p19111369193247"></a>Key</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p4517093193247"><a name="p4517093193247"></a><a name="p4517093193247"></a>Value</p>
</th>
</tr>
</thead>
<tbody><tr id="row30340220193247"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p41638776193247"><a name="p41638776193247"></a><a name="p41638776193247"></a>publicip_id</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p17297729193247"><a name="p17297729193247"></a><a name="p17297729193247"></a>Specifies the EIP ID.</p>
</td>
</tr>
<tr id="row21461838193247"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p60687284193247"><a name="p60687284193247"></a><a name="p60687284193247"></a>bandwidth_id</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p16722971193247"><a name="p16722971193247"></a><a name="p16722971193247"></a>Specifies the bandwidth ID.</p>
</td>
</tr>
</tbody>
</table>

