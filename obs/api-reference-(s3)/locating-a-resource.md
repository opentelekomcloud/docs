# Locating a Resource<a name="EN-US_TOPIC_0125560479"></a>

In REST, specific network information or data on a network is represented by a resource, which is identified with a uniform resource identifier \(URI\). Clients on a network can locate resources using unified resource locator \(URL\).

In OBS, a resource can be a bucket, object, or specific resource related to a bucket or object. These resources are identified by a URL and can be operated after requests are sent using the URL.

The following provides a common URL format. The parameters in brackets \(\[ \]\) are optional.

**protocol://**\[**bucket.**\]**domain\[:prot\]\[/object\]\[?param\]**

[Table 1](#table6854763)  describes URL parameters.

**Table  1**  URL parameters

<a name="table6854763"></a>
<table><thead align="left"><tr id="row62517084"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p30719029"><a name="p30719029"></a><a name="p30719029"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p5213419"><a name="p5213419"></a><a name="p5213419"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p19633765"><a name="p19633765"></a><a name="p19633765"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row46831115"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p35224007"><a name="p35224007"></a><a name="p35224007"></a>protocol</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p34572286"><a name="p34572286"></a><a name="p34572286"></a>Indicates the protocol used for sending requests. Available values are HTTP and HTTPS.</p>
<p id="p42715124"><a name="p42715124"></a><a name="p42715124"></a>You can specify HTTPS to ensure secure access to resources.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p37373042"><a name="p37373042"></a><a name="p37373042"></a>Mandatory</p>
</td>
</tr>
<tr id="row9725192119323"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1795522173216"><a name="p1795522173216"></a><a name="p1795522173216"></a>bucket</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p2795122233217"><a name="p2795122233217"></a><a name="p2795122233217"></a>Indicates the path of a bucket. Each path identifies a unique bucket in OBS.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p379542210327"><a name="p379542210327"></a><a name="p379542210327"></a>Optional</p>
</td>
</tr>
<tr id="row1551231193113"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p135344812156"><a name="p135344812156"></a><a name="p135344812156"></a>domain</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p323103261516"><a name="p323103261516"></a><a name="p323103261516"></a>Domain name or IP address of the server for saving resources.</p>
<div class="notice" id="note3123154303113"><a name="note3123154303113"></a><a name="note3123154303113"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><p id="p18123164318319"><a name="p18123164318319"></a><a name="p18123164318319"></a>The name of the host in this document is used as an example. Please refer to the actual information when accessing OBS. Obtain this value from <a href="https://docs.otc.t-systems.com/en-us/endpoint/index.html" target="_blank" rel="noopener noreferrer">Regions and Endpoints</a>.</p>
</div></div>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p125929367153"><a name="p125929367153"></a><a name="p125929367153"></a>Mandatory</p>
</td>
</tr>
<tr id="row14240860"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p12659036"><a name="p12659036"></a><a name="p12659036"></a>port</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p18749013"><a name="p18749013"></a><a name="p18749013"></a>Indicates the port enabled for protocols used for sending requests. The value varies with software server deployment. If the value is not specified, default ports are enabled. Normally, ports <strong id="b34523390"><a name="b34523390"></a><a name="b34523390"></a>80</strong>&nbsp;and&nbsp;<strong id="b42275054"><a name="b42275054"></a><a name="b42275054"></a>443</strong>&nbsp;are enabled by default for HTTP and HTTPS, respectively. In the OBS, ports&nbsp;<strong id="b3401794814523"><a name="b3401794814523"></a><a name="b3401794814523"></a>80</strong>&nbsp;and&nbsp;<strong id="b171211557194911"><a name="b171211557194911"></a><a name="b171211557194911"></a>443</strong> are enabled by default for HTTP and HTTPS, respectively.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p5694497"><a name="p5694497"></a><a name="p5694497"></a>Optional</p>
</td>
</tr>
<tr id="row17855085"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p36975818"><a name="p36975818"></a><a name="p36975818"></a>object</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p42251271"><a name="p42251271"></a><a name="p42251271"></a>Indicates the path of an object.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p66909772"><a name="p66909772"></a><a name="p66909772"></a>Optional</p>
</td>
</tr>
<tr id="row65317042"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p56189015"><a name="p56189015"></a><a name="p56189015"></a>param</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p55016344"><a name="p55016344"></a><a name="p55016344"></a>Indicates the specific resource related to a bucket or object. If this parameter is not specified, the bucket or object itself is operated.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p27138911"><a name="p27138911"></a><a name="p27138911"></a>Optional</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>The recommended protocol is HTTPS, because HTTP security is inefficient.  
>HTTPS supports TLS1.1 and TLS1.2, but not TLS1.0.  

## Basic Concepts Involved in Regions and Domain Name-based Access<a name="section2151171715919"></a>

The following table describes the concepts involved in regions and domain name–based access, for example, global domain name.

**Table  2**  Basic concepts

<a name="table1103414015930"></a>
<table><thead align="left"><tr id="row6693569315930"><th class="cellrowborder" valign="top" width="26.529999999999998%" id="mcps1.2.4.1.1"><p id="p5308203515930"><a name="p5308203515930"></a><a name="p5308203515930"></a>Concept</p>
</th>
<th class="cellrowborder" valign="top" width="26.529999999999998%" id="mcps1.2.4.1.2"><p id="p467761515930"><a name="p467761515930"></a><a name="p467761515930"></a>Example</p>
</th>
<th class="cellrowborder" valign="top" width="46.94%" id="mcps1.2.4.1.3"><p id="p4334250215930"><a name="p4334250215930"></a><a name="p4334250215930"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row2108179415930"><td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p2990378715930"><a name="p2990378715930"></a><a name="p2990378715930"></a>Global domain name</p>
</td>
<td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.2 "><p id="p628768815930"><a name="p628768815930"></a><a name="p628768815930"></a>obs.example.com</p>
</td>
<td class="cellrowborder" valign="top" width="46.94%" headers="mcps1.2.4.1.3 "><p id="p3954073815930"><a name="p3954073815930"></a><a name="p3954073815930"></a>Unique global domain name of the multi-region cluster. The domain name serves as the unified access point of OBS in the cluster.</p>
</td>
</tr>
<tr id="row2032232515930"><td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p3549562015930"><a name="p3549562015930"></a><a name="p3549562015930"></a>Region type</p>
</td>
<td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.2 "><p id="p5657299615930"><a name="p5657299615930"></a><a name="p5657299615930"></a>Default region</p>
</td>
<td class="cellrowborder" valign="top" width="46.94%" headers="mcps1.2.4.1.3 "><p id="p1900998115930"><a name="p1900998115930"></a><a name="p1900998115930"></a>Regions are divided into the default region and non-default region. There is only one default region in a multi-region cluster. Other regions are non-default regions.</p>
</td>
</tr>
<tr id="row3687210215930"><td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p3385024615930"><a name="p3385024615930"></a><a name="p3385024615930"></a>Region name</p>
</td>
<td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.2 "><p id="p5751537815930"><a name="p5751537815930"></a><a name="p5751537815930"></a>region2</p>
</td>
<td class="cellrowborder" valign="top" width="46.94%" headers="mcps1.2.4.1.3 "><p id="p2823406715930"><a name="p2823406715930"></a><a name="p2823406715930"></a>Name of the default region or a non-default region.</p>
</td>
</tr>
<tr id="row5278001915930"><td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p4732316615930"><a name="p4732316615930"></a><a name="p4732316615930"></a>Region domain name</p>
</td>
<td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.2 "><p id="p797125015930"><a name="p797125015930"></a><a name="p797125015930"></a>region2.example.com</p>
</td>
<td class="cellrowborder" valign="top" width="46.94%" headers="mcps1.2.4.1.3 "><p id="p4169147715930"><a name="p4169147715930"></a><a name="p4169147715930"></a>Each region can have a domain name, which serves as the access point of OBS in the region.</p>
</td>
</tr>
<tr id="row3967898115930"><td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p5988090115930"><a name="p5988090115930"></a><a name="p5988090115930"></a>Virtual hosting style</p>
</td>
<td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.2 "><p id="p1851479315930"><a name="p1851479315930"></a><a name="p1851479315930"></a>mybucket.region2.example.com or mybucket.obs.example.com</p>
</td>
<td class="cellrowborder" valign="top" width="46.94%" headers="mcps1.2.4.1.3 "><p id="p2330325815930"><a name="p2330325815930"></a><a name="p2330325815930"></a>The virtual hosting style is a style where buckets are accessed as hosts.</p>
</td>
</tr>
</tbody>
</table>

In cross-region interaction, requests may be redirected. The system will handle all requests from client, but not all of the requests will be recorded in metering file. \(eg. 301 redirect request.\)

It does not incur re-metering problems. \(If users access the global firstly and then jump to a local bucket, there is only one Charging Data Record.\)

OBS supports virtual hosting-style access to all regions.

If you want to use virtual hosting-style access, the correct URI is  **http://mybucket.region2.example.com** or **http://mybucket.obs.example.com**.

