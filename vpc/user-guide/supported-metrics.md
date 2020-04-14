# Supported Metrics<a name="vpc010012"></a>

## Description<a name="section829218111642"></a>

This section describes the namespace, list, and dimensions of EIP and bandwidth metrics on Cloud Eye. You can use APIs or the Cloud Eye console to query the metrics of the monitored metrics and alarms generated for EIP and bandwidth.

## Namespace<a name="section2061005615173"></a>

SYS.VPC

## Monitoring Metrics<a name="section6270316149"></a>

**Table  1**  EIP and Bandwidth metrics

<a name="en-us_topic_0024607920_table6444895193247"></a>
<table><thead align="left"><tr id="en-us_topic_0024607920_row17328334193247"><th class="cellrowborder" valign="top" width="14.98850114988501%" id="mcps1.2.7.1.1"><p id="en-us_topic_0024607920_p61417783193247"><a name="en-us_topic_0024607920_p61417783193247"></a><a name="en-us_topic_0024607920_p61417783193247"></a>Metric</p>
</th>
<th class="cellrowborder" valign="top" width="10.528947105289472%" id="mcps1.2.7.1.2"><p id="en-us_topic_0024607920_p8784488193247"><a name="en-us_topic_0024607920_p8784488193247"></a><a name="en-us_topic_0024607920_p8784488193247"></a>Metric Name</p>
</th>
<th class="cellrowborder" valign="top" width="21.697830216978303%" id="mcps1.2.7.1.3"><p id="en-us_topic_0024607920_p40454922193247"><a name="en-us_topic_0024607920_p40454922193247"></a><a name="en-us_topic_0024607920_p40454922193247"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="12.278772122787721%" id="mcps1.2.7.1.4"><p id="en-us_topic_0024607920_p55623236193247"><a name="en-us_topic_0024607920_p55623236193247"></a><a name="en-us_topic_0024607920_p55623236193247"></a>Value Range</p>
</th>
<th class="cellrowborder" valign="top" width="21.347865213478652%" id="mcps1.2.7.1.5"><p id="en-us_topic_0024607920_p9188287193247"><a name="en-us_topic_0024607920_p9188287193247"></a><a name="en-us_topic_0024607920_p9188287193247"></a>Measurement Object &amp; Dimension</p>
</th>
<th class="cellrowborder" valign="top" width="19.15808419158084%" id="mcps1.2.7.1.6"><p id="p116611739175520"><a name="p116611739175520"></a><a name="p116611739175520"></a><strong id="b63113175012"><a name="b63113175012"></a><a name="b63113175012"></a>Monitoring Interval (Raw Data)</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0024607920_row173875718321"><td class="cellrowborder" valign="top" width="14.98850114988501%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0024607920_p131326819339"><a name="en-us_topic_0024607920_p131326819339"></a><a name="en-us_topic_0024607920_p131326819339"></a>upstream_bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="10.528947105289472%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0024607920_p7133182333"><a name="en-us_topic_0024607920_p7133182333"></a><a name="en-us_topic_0024607920_p7133182333"></a>Outbound Bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="21.697830216978303%" headers="mcps1.2.7.1.3 "><p id="p179215408321"><a name="p179215408321"></a><a name="p179215408321"></a>Network rate of outbound traffic </p>
<p id="p478910501515"><a name="p478910501515"></a><a name="p478910501515"></a>Unit: bit/s</p>
</td>
<td class="cellrowborder" valign="top" width="12.278772122787721%" headers="mcps1.2.7.1.4 "><p id="p16856133111520"><a name="p16856133111520"></a><a name="p16856133111520"></a>≥ 0 bit/s</p>
</td>
<td class="cellrowborder" valign="top" width="21.347865213478652%" headers="mcps1.2.7.1.5 "><p id="p14941182731011"><a name="p14941182731011"></a><a name="p14941182731011"></a>Object: Bandwidth or EIP</p>
<p id="p2094120273109"><a name="p2094120273109"></a><a name="p2094120273109"></a>Dimension<sup id="sup996111317111"><a name="sup996111317111"></a><a name="sup996111317111"></a>a</sup>:</p>
<p id="p394132711018"><a name="p394132711018"></a><a name="p394132711018"></a>bandwidth_id,</p>
<p id="p994111271109"><a name="p994111271109"></a><a name="p994111271109"></a>publicip_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.15808419158084%" headers="mcps1.2.7.1.6 "><p id="p1166213397559"><a name="p1166213397559"></a><a name="p1166213397559"></a>1 minute</p>
</td>
</tr>
<tr id="en-us_topic_0024607920_row2515145493216"><td class="cellrowborder" valign="top" width="14.98850114988501%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0024607920_p131416813315"><a name="en-us_topic_0024607920_p131416813315"></a><a name="en-us_topic_0024607920_p131416813315"></a>downstream_bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="10.528947105289472%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0024607920_p18143178133311"><a name="en-us_topic_0024607920_p18143178133311"></a><a name="en-us_topic_0024607920_p18143178133311"></a>Inbound Bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="21.697830216978303%" headers="mcps1.2.7.1.3 "><p id="p14794440113211"><a name="p14794440113211"></a><a name="p14794440113211"></a>Network rate of inbound traffic </p>
<p id="p1561138115211"><a name="p1561138115211"></a><a name="p1561138115211"></a>Unit: bit/s</p>
</td>
<td class="cellrowborder" valign="top" width="12.278772122787721%" headers="mcps1.2.7.1.4 "><p id="p1785863115157"><a name="p1785863115157"></a><a name="p1785863115157"></a>≥ 0 bit/s</p>
</td>
<td class="cellrowborder" valign="top" width="21.347865213478652%" headers="mcps1.2.7.1.5 "><p id="p19445113119103"><a name="p19445113119103"></a><a name="p19445113119103"></a>Object: Bandwidth or EIP</p>
<p id="p344623181019"><a name="p344623181019"></a><a name="p344623181019"></a>Dimension:</p>
<p id="p5446831151014"><a name="p5446831151014"></a><a name="p5446831151014"></a>bandwidth_id,</p>
<p id="p1544693151019"><a name="p1544693151019"></a><a name="p1544693151019"></a>publicip_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.15808419158084%" headers="mcps1.2.7.1.6 "><p id="p2662133918557"><a name="p2662133918557"></a><a name="p2662133918557"></a>1 minute</p>
</td>
</tr>
<tr id="row6251357113315"><td class="cellrowborder" valign="top" width="14.98850114988501%" headers="mcps1.2.7.1.1 "><p id="p199051635348"><a name="p199051635348"></a><a name="p199051635348"></a>up_stream</p>
</td>
<td class="cellrowborder" valign="top" width="10.528947105289472%" headers="mcps1.2.7.1.2 "><p id="p55042030141711"><a name="p55042030141711"></a><a name="p55042030141711"></a>Outbound Traffic</p>
</td>
<td class="cellrowborder" valign="top" width="21.697830216978303%" headers="mcps1.2.7.1.3 "><p id="p050623091713"><a name="p050623091713"></a><a name="p050623091713"></a>Network traffic going out of the cloud platform </p>
<p id="p29751350115210"><a name="p29751350115210"></a><a name="p29751350115210"></a>Unit: byte</p>
</td>
<td class="cellrowborder" valign="top" width="12.278772122787721%" headers="mcps1.2.7.1.4 "><p id="p55084302174"><a name="p55084302174"></a><a name="p55084302174"></a>≥ 0 bytes</p>
</td>
<td class="cellrowborder" valign="top" width="21.347865213478652%" headers="mcps1.2.7.1.5 "><p id="p17314631101319"><a name="p17314631101319"></a><a name="p17314631101319"></a>Object: Bandwidth or EIP</p>
<p id="p731403115136"><a name="p731403115136"></a><a name="p731403115136"></a>Dimension:</p>
<p id="p4314163119134"><a name="p4314163119134"></a><a name="p4314163119134"></a>bandwidth_id,</p>
<p id="p15314163171315"><a name="p15314163171315"></a><a name="p15314163171315"></a>publicip_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.15808419158084%" headers="mcps1.2.7.1.6 "><p id="p966233925510"><a name="p966233925510"></a><a name="p966233925510"></a>1 minute</p>
</td>
</tr>
<tr id="row84711354143318"><td class="cellrowborder" valign="top" width="14.98850114988501%" headers="mcps1.2.7.1.1 "><p id="p29277317341"><a name="p29277317341"></a><a name="p29277317341"></a>down_stream</p>
</td>
<td class="cellrowborder" valign="top" width="10.528947105289472%" headers="mcps1.2.7.1.2 "><p id="p1451019302175"><a name="p1451019302175"></a><a name="p1451019302175"></a>Inbound Traffic</p>
</td>
<td class="cellrowborder" valign="top" width="21.697830216978303%" headers="mcps1.2.7.1.3 "><p id="p1051010308176"><a name="p1051010308176"></a><a name="p1051010308176"></a>Network traffic going into the cloud platform </p>
<p id="p8822319165320"><a name="p8822319165320"></a><a name="p8822319165320"></a>Unit: byte</p>
</td>
<td class="cellrowborder" valign="top" width="12.278772122787721%" headers="mcps1.2.7.1.4 "><p id="p15512163016174"><a name="p15512163016174"></a><a name="p15512163016174"></a>≥ 0 bytes</p>
</td>
<td class="cellrowborder" valign="top" width="21.347865213478652%" headers="mcps1.2.7.1.5 "><p id="p2638143411134"><a name="p2638143411134"></a><a name="p2638143411134"></a>Object: Bandwidth or EIP</p>
<p id="p7638153412133"><a name="p7638153412133"></a><a name="p7638153412133"></a>Dimension:</p>
<p id="p15638113471319"><a name="p15638113471319"></a><a name="p15638113471319"></a>bandwidth_id,</p>
<p id="p196388346137"><a name="p196388346137"></a><a name="p196388346137"></a>publicip_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.15808419158084%" headers="mcps1.2.7.1.6 "><p id="p15662183910558"><a name="p15662183910558"></a><a name="p15662183910558"></a>1 minute</p>
</td>
</tr>
<tr id="row157931920151418"><td class="cellrowborder" colspan="6" valign="top" headers="mcps1.2.7.1.1 mcps1.2.7.1.2 mcps1.2.7.1.3 mcps1.2.7.1.4 mcps1.2.7.1.5 mcps1.2.7.1.6 "><div class="p" id="p13558154816619"><a name="p13558154816619"></a><a name="p13558154816619"></a><strong id="b154853505173"><a name="b154853505173"></a><a name="b154853505173"></a>a</strong>: If a service has multiple dimensions, all dimensions are mandatory when you use APIs to query the metrics.<a name="ul2558164815619"></a><a name="ul2558164815619"></a><ul id="ul2558164815619"><li>Query a monitoring metric: <p id="p196421916162213"><a name="p196421916162213"></a><a name="p196421916162213"></a>dim.0=bandwidth_id,530cd6b0-86d7-4818-837f-935f6a27414d&amp;dim.1=publicip_id,3773b058-5b4f-4366-9035-9bbd9964714a</p>
</li><li>Query monitoring metrics in batches:<p id="p125596481467"><a name="p125596481467"></a><a name="p125596481467"></a>"dimensions": [</p>
<p id="p1055919488614"><a name="p1055919488614"></a><a name="p1055919488614"></a>{</p>
<p id="p85595481617"><a name="p85595481617"></a><a name="p85595481617"></a>"name": "bandwidth_id",</p>
<p id="p2559748366"><a name="p2559748366"></a><a name="p2559748366"></a>"value": "530cd6b0-86d7-4818-837f-935f6a27414d"</p>
<p id="p1455913481360"><a name="p1455913481360"></a><a name="p1455913481360"></a>}</p>
<p id="p3559194818611"><a name="p3559194818611"></a><a name="p3559194818611"></a>{</p>
<p id="p1819695719711"><a name="p1819695719711"></a><a name="p1819695719711"></a>"name": "publicip_id",</p>
<p id="p125591481564"><a name="p125591481564"></a><a name="p125591481564"></a>"value": "3773b058-5b4f-4366-9035-9bbd9964714a"</p>
<p id="p12559448369"><a name="p12559448369"></a><a name="p12559448369"></a>}</p>
<p id="p855924816616"><a name="p855924816616"></a><a name="p855924816616"></a>],</p>
</li></ul>
</div>
</td>
</tr>
</tbody>
</table>

## Dimensions<a name="section91771135191816"></a>

<a name="en-us_topic_0024746310_en-us_topic_0024607920_table30802540193247"></a>
<table><thead align="left"><tr id="en-us_topic_0024746310_en-us_topic_0024607920_row7692483193247"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0024746310_en-us_topic_0024607920_p19111369193247"><a name="en-us_topic_0024746310_en-us_topic_0024607920_p19111369193247"></a><a name="en-us_topic_0024746310_en-us_topic_0024607920_p19111369193247"></a>Key</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0024746310_en-us_topic_0024607920_p4517093193247"><a name="en-us_topic_0024746310_en-us_topic_0024607920_p4517093193247"></a><a name="en-us_topic_0024746310_en-us_topic_0024607920_p4517093193247"></a>Value</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0024746310_en-us_topic_0024607920_row30340220193247"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0024746310_en-us_topic_0024607920_p41638776193247"><a name="en-us_topic_0024746310_en-us_topic_0024607920_p41638776193247"></a><a name="en-us_topic_0024746310_en-us_topic_0024607920_p41638776193247"></a>publicip_id</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0024746310_en-us_topic_0024607920_p17297729193247"><a name="en-us_topic_0024746310_en-us_topic_0024607920_p17297729193247"></a><a name="en-us_topic_0024746310_en-us_topic_0024607920_p17297729193247"></a>EIP ID</p>
</td>
</tr>
<tr id="en-us_topic_0024746310_en-us_topic_0024607920_row21461838193247"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0024746310_en-us_topic_0024607920_p60687284193247"><a name="en-us_topic_0024746310_en-us_topic_0024607920_p60687284193247"></a><a name="en-us_topic_0024746310_en-us_topic_0024607920_p60687284193247"></a>bandwidth_id</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0024746310_en-us_topic_0024607920_p16722971193247"><a name="en-us_topic_0024746310_en-us_topic_0024607920_p16722971193247"></a><a name="en-us_topic_0024746310_en-us_topic_0024607920_p16722971193247"></a>Bandwidth ID</p>
</td>
</tr>
</tbody>
</table>

