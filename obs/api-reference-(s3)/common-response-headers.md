# Common Response Headers<a name="EN-US_TOPIC_0125560484"></a>

[Table 1](#table33358910)  describes headers common to OBS REST responses.

**Table  1**  Common response headers

<a name="table33358910"></a>
<table><thead align="left"><tr id="row64051613"><th class="cellrowborder" valign="top" width="30.830000000000002%" id="mcps1.2.3.1.1"><p id="p20798169"><a name="p20798169"></a><a name="p20798169"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="69.17%" id="mcps1.2.3.1.2"><p id="p6930125"><a name="p6930125"></a><a name="p6930125"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row24469282"><td class="cellrowborder" valign="top" width="30.830000000000002%" headers="mcps1.2.3.1.1 "><p id="p35854848"><a name="p35854848"></a><a name="p35854848"></a>Content-Length</p>
</td>
<td class="cellrowborder" valign="top" width="69.17%" headers="mcps1.2.3.1.2 "><p id="p18561550"><a name="p18561550"></a><a name="p18561550"></a>Indicates the length (in bytes) of a response body.</p>
<p id="p32836222"><a name="p32836222"></a><a name="p32836222"></a>Type: String</p>
<p id="p27090548"><a name="p27090548"></a><a name="p27090548"></a>Default: None</p>
</td>
</tr>
<tr id="row42488344"><td class="cellrowborder" valign="top" width="30.830000000000002%" headers="mcps1.2.3.1.1 "><p id="p19003830"><a name="p19003830"></a><a name="p19003830"></a>Connection</p>
</td>
<td class="cellrowborder" valign="top" width="69.17%" headers="mcps1.2.3.1.2 "><p id="p62915265"><a name="p62915265"></a><a name="p62915265"></a>Indicates whether the connection to the server is opened or closed.</p>
<p id="p29366474"><a name="p29366474"></a><a name="p29366474"></a>Type: String.</p>
<p id="p62971680"><a name="p62971680"></a><a name="p62971680"></a>Valid values: <strong id="b29874211"><a name="b29874211"></a><a name="b29874211"></a>keep-alive | close</strong></p>
<p id="p432444"><a name="p432444"></a><a name="p432444"></a>Default: None</p>
</td>
</tr>
<tr id="row3891996"><td class="cellrowborder" valign="top" width="30.830000000000002%" headers="mcps1.2.3.1.1 "><p id="p46816221"><a name="p46816221"></a><a name="p46816221"></a>Date</p>
</td>
<td class="cellrowborder" valign="top" width="69.17%" headers="mcps1.2.3.1.2 "><p id="p34017551"><a name="p34017551"></a><a name="p34017551"></a>Indicates the date and time at which OBS responds to a request.</p>
<p id="p37722505"><a name="p37722505"></a><a name="p37722505"></a>Type: String</p>
<p id="p3958233"><a name="p3958233"></a><a name="p3958233"></a>Default: None</p>
</td>
</tr>
<tr id="row35624103"><td class="cellrowborder" valign="top" width="30.830000000000002%" headers="mcps1.2.3.1.1 "><p id="p66980105"><a name="p66980105"></a><a name="p66980105"></a>ETag</p>
</td>
<td class="cellrowborder" valign="top" width="69.17%" headers="mcps1.2.3.1.2 "><p id="ole_link20"><a name="ole_link20"></a><a name="ole_link20"></a>Indicates the hash value of an object. The entity tag (ETag) only reflects changes to the contents of an object, not its metadata.</p>
<p id="p40352987"><a name="p40352987"></a><a name="p40352987"></a>Type: String</p>
</td>
</tr>
<tr id="row51425456"><td class="cellrowborder" valign="top" width="30.830000000000002%" headers="mcps1.2.3.1.1 "><p id="p4712373"><a name="p4712373"></a><a name="p4712373"></a>x-amz-id-2</p>
</td>
<td class="cellrowborder" valign="top" width="69.17%" headers="mcps1.2.3.1.2 "><p id="p46157910"><a name="p46157910"></a><a name="p46157910"></a>Indicates a special token that helps OBS troubleshoot faults.</p>
<p id="p12768013"><a name="p12768013"></a><a name="p12768013"></a>Type: String</p>
<p id="p47803261"><a name="p47803261"></a><a name="p47803261"></a>Default: None</p>
</td>
</tr>
<tr id="row27576165"><td class="cellrowborder" valign="top" width="30.830000000000002%" headers="mcps1.2.3.1.1 "><p id="p19076877"><a name="p19076877"></a><a name="p19076877"></a>x-amz-request-id</p>
</td>
<td class="cellrowborder" valign="top" width="69.17%" headers="mcps1.2.3.1.2 "><p id="p1723181"><a name="p1723181"></a><a name="p1723181"></a>Indicates the value created by OBS to uniquely identify a request. OBS uses this value to troubleshoot faults.</p>
<p id="p15508634"><a name="p15508634"></a><a name="p15508634"></a>Type: String</p>
<p id="p5359982"><a name="p5359982"></a><a name="p5359982"></a>Default: None</p>
</td>
</tr>
<tr id="row48239842"><td class="cellrowborder" valign="top" width="30.830000000000002%" headers="mcps1.2.3.1.1 "><p id="p15113143"><a name="p15113143"></a><a name="p15113143"></a>x-reserved</p>
</td>
<td class="cellrowborder" valign="top" width="69.17%" headers="mcps1.2.3.1.2 "><p id="p16205056"><a name="p16205056"></a><a name="p16205056"></a>Indicates the copyright.</p>
<p id="p11627780"><a name="p11627780"></a><a name="p11627780"></a>Type: String</p>
<p id="p37541158"><a name="p37541158"></a><a name="p37541158"></a>Default: None</p>
</td>
</tr>
</tbody>
</table>

