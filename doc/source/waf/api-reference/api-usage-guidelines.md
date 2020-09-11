# API Usage Guidelines<a name="EN-US_TOPIC_0193631143"></a>

Public cloud APIs comply with the RESTful API design principles. REST-based Web services are organized into resources. Each resource is identified by one or more Uniform Resource Identifiers \(URIs\). An application accesses a resource based on the resource's Unified Resource Locator \(URL\). A URL is usually in the following format:  _https://Endpoint/uri_. In the URL,  **uri**  indicates the resource path, that is, the API access path.

Public cloud APIs use HTTPS as the transmission protocol. Requests/Responses are transmitted by using JSON messages, with media type represented by  **Application/json**.

For details about how to use APIs, see  [API Usage Guidelines](https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328001.html?tag=API%20Documents).

>![](/images/icon-notice.gif) **NOTICE:**   
>The following table lists the additional request header fields required for the POST, PUT, PATCH, and DELETE methods.  

<a name="tdfc57d5638cd437a9acf408b1c13641b"></a>
<table><thead align="left"><tr id="rb4195bd3ee6a44488c466d41c6644665"><th class="cellrowborder" valign="top" width="19.74%" id="mcps1.1.5.1.1"><p id="aa79becf302ca469483a0de48a9e06d19"><a name="aa79becf302ca469483a0de48a9e06d19"></a><a name="aa79becf302ca469483a0de48a9e06d19"></a><strong id="b1844753665617"><a name="b1844753665617"></a><a name="b1844753665617"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26.490000000000002%" id="mcps1.1.5.1.2"><p id="abe266326263e4cc0af1bc6626a1d841b"><a name="abe266326263e4cc0af1bc6626a1d841b"></a><a name="abe266326263e4cc0af1bc6626a1d841b"></a><strong id="b6267183819560"><a name="b6267183819560"></a><a name="b6267183819560"></a>Description</strong></p>
</th>
<th class="cellrowborder" valign="top" width="19.93%" id="mcps1.1.5.1.3"><p id="a8efc45469e5540f993b52578749436e1"><a name="a8efc45469e5540f993b52578749436e1"></a><a name="a8efc45469e5540f993b52578749436e1"></a><strong id="b432263945611"><a name="b432263945611"></a><a name="b432263945611"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.839999999999996%" id="mcps1.1.5.1.4"><p id="ac75836023a6343cb8d1a016b9b51f7a3"><a name="ac75836023a6343cb8d1a016b9b51f7a3"></a><a name="ac75836023a6343cb8d1a016b9b51f7a3"></a>Example</p>
</th>
</tr>
</thead>
<tbody><tr id="r8c92183e5223419ea855f14b6948d3b7"><td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0091607286_p46301737411"><a name="en-us_topic_0091607286_p46301737411"></a><a name="en-us_topic_0091607286_p46301737411"></a>x-request-source-type</p>
</td>
<td class="cellrowborder" valign="top" width="26.490000000000002%" headers="mcps1.1.5.1.2 "><p id="p1493958183511"><a name="p1493958183511"></a><a name="p1493958183511"></a>Type of a request resource</p>
<a name="ul1222313528312"></a><a name="ul1222313528312"></a><ul id="ul1222313528312"><li><span class="parmvalue" id="parmvalue09731215134114"><a name="parmvalue09731215134114"></a><a name="parmvalue09731215134114"></a><b>ApiCall</b></span>: invoked by an API.</li><li><span class="parmvalue" id="parmvalue11910125204819"><a name="parmvalue11910125204819"></a><a name="parmvalue11910125204819"></a><b>ConsoleAction</b></span>: invoked by the console.</li><li><span class="parmvalue" id="parmvalue42931981491"><a name="parmvalue42931981491"></a><a name="parmvalue42931981491"></a><b>SystemAction</b></span>: invoked by the system.</li></ul>
</td>
<td class="cellrowborder" valign="top" width="19.93%" headers="mcps1.1.5.1.3 "><p id="ae1d97a206af543fcaa349136e4bfbd52"><a name="ae1d97a206af543fcaa349136e4bfbd52"></a><a name="ae1d97a206af543fcaa349136e4bfbd52"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.839999999999996%" headers="mcps1.1.5.1.4 "><p id="a075a6640793e4cccb1629d7636e9189a"><a name="a075a6640793e4cccb1629d7636e9189a"></a><a name="a075a6640793e4cccb1629d7636e9189a"></a>ApiCall</p>
</td>
</tr>
</tbody>
</table>

