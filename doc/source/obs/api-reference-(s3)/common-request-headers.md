# Common Request Headers<a name="EN-US_TOPIC_0125560462"></a>

[Table 1](#table25197309)  describes headers common to OBS REST requests.

**Table  1**  Common request headers

<a name="table25197309"></a>
<table><thead align="left"><tr id="row54071934"><th class="cellrowborder" valign="top" width="33.71%" id="mcps1.2.4.1.1"><p id="p17750533"><a name="p17750533"></a><a name="p17750533"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="32.96%" id="mcps1.2.4.1.2"><p id="p28507060"><a name="p28507060"></a><a name="p28507060"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="33.33%" id="mcps1.2.4.1.3"><p id="p27370548"><a name="p27370548"></a><a name="p27370548"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row2421933"><td class="cellrowborder" valign="top" width="33.71%" headers="mcps1.2.4.1.1 "><p id="p61958854"><a name="p61958854"></a><a name="p61958854"></a>Authorization</p>
</td>
<td class="cellrowborder" valign="top" width="32.96%" headers="mcps1.2.4.1.2 "><p id="p52611239"><a name="p52611239"></a><a name="p52611239"></a>Indicates the authentication information carried in a request.</p>
<p id="p3739106"><a name="p3739106"></a><a name="p3739106"></a>Type: String</p>
<p id="p33651961"><a name="p33651961"></a><a name="p33651961"></a>Default: None</p>
</td>
<td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p41454307"><a name="p41454307"></a><a name="p41454307"></a>Conditional: optional for anonymous requests and mandatory for other requests</p>
</td>
</tr>
<tr id="row37544449"><td class="cellrowborder" valign="top" width="33.71%" headers="mcps1.2.4.1.1 "><p id="p21201539"><a name="p21201539"></a><a name="p21201539"></a>Content-Length</p>
</td>
<td class="cellrowborder" valign="top" width="32.96%" headers="mcps1.2.4.1.2 "><p id="p39603122"><a name="p39603122"></a><a name="p39603122"></a>Indicates the length of request content (excluding headers) defined by RFC 2616.</p>
<p id="p20883781"><a name="p20883781"></a><a name="p20883781"></a>Type: String</p>
<p id="p53736309"><a name="p53736309"></a><a name="p53736309"></a>Default: None</p>
</td>
<td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p57673781"><a name="p57673781"></a><a name="p57673781"></a>Conditional: mandatory for PUT requests and requests that load XML content</p>
</td>
</tr>
<tr id="row49301983"><td class="cellrowborder" valign="top" width="33.71%" headers="mcps1.2.4.1.1 "><p id="p34037668"><a name="p34037668"></a><a name="p34037668"></a>Content-Type</p>
</td>
<td class="cellrowborder" valign="top" width="32.96%" headers="mcps1.2.4.1.2 "><p id="p5587738"><a name="p5587738"></a><a name="p5587738"></a>Indicates the content type of a requested resource, for example, <strong id="b50289647"><a name="b50289647"></a><a name="b50289647"></a>text</strong>/<strong id="b49953640"><a name="b49953640"></a><a name="b49953640"></a>plain</strong>.</p>
<p id="p46929584"><a name="p46929584"></a><a name="p46929584"></a>Type: String</p>
<p id="p19713079"><a name="p19713079"></a><a name="p19713079"></a>Default: None</p>
</td>
<td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p53255599"><a name="p53255599"></a><a name="p53255599"></a>Optional</p>
</td>
</tr>
<tr id="row9538345"><td class="cellrowborder" valign="top" width="33.71%" headers="mcps1.2.4.1.1 "><p id="p34408496"><a name="p34408496"></a><a name="p34408496"></a>Date</p>
</td>
<td class="cellrowborder" valign="top" width="32.96%" headers="mcps1.2.4.1.2 "><p id="p35624820"><a name="p35624820"></a><a name="p35624820"></a>Indicates the date and time at which a request is initiated.</p>
<p id="p52187928"><a name="p52187928"></a><a name="p52187928"></a>Type: String</p>
<p id="p67038172"><a name="p67038172"></a><a name="p67038172"></a>Default: None</p>
</td>
<td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p61382865"><a name="p61382865"></a><a name="p61382865"></a>Conditional: optional for anonymous requests or requests containing optional header <strong id="b15574875"><a name="b15574875"></a><a name="b15574875"></a>x-amz-date</strong></p>
</td>
</tr>
<tr id="row5956154"><td class="cellrowborder" valign="top" width="33.71%" headers="mcps1.2.4.1.1 "><p id="p12686464"><a name="p12686464"></a><a name="p12686464"></a>Host</p>
</td>
<td class="cellrowborder" valign="top" width="32.96%" headers="mcps1.2.4.1.2 "><p id="p65933096115340"><a name="p65933096115340"></a><a name="p65933096115340"></a>Indicates a host address. For example, <strong id="b52657395145458"><a name="b52657395145458"></a><a name="b52657395145458"></a>bucketname.obs.example.com</strong>.</p>
<p id="p53880264"><a name="p53880264"></a><a name="p53880264"></a>Type: String</p>
<p id="p15160332"><a name="p15160332"></a><a name="p15160332"></a>Default: None</p>
</td>
<td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p20027347"><a name="p20027347"></a><a name="p20027347"></a>Mandatory</p>
</td>
</tr>
<tr id="row19866165511115"><td class="cellrowborder" valign="top" width="33.71%" headers="mcps1.2.4.1.1 "><p id="p2636530171316"><a name="p2636530171316"></a><a name="p2636530171316"></a>x-amz-security-token</p>
</td>
<td class="cellrowborder" valign="top" width="32.96%" headers="mcps1.2.4.1.2 "><p id="p176361330141312"><a name="p176361330141312"></a><a name="p176361330141312"></a>Header field used to identify the request of a federated user. When the federal authentication function is enabled, users sending such requests are identified as federated users.</p>
<p id="p186362030201310"><a name="p186362030201310"></a><a name="p186362030201310"></a>Type: string</p>
</td>
<td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p1063603061316"><a name="p1063603061316"></a><a name="p1063603061316"></a>Optional. This parameter must be carried in the request sent by federated users.</p>
</td>
</tr>
</tbody>
</table>

