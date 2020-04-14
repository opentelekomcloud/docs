# Locating a Resource<a name="obs_03_0007"></a>

In REST, specific information or data on a network is represented by a resource, which is referenced with a uniform resource identifier \(URI\). Clients on a network can locate resources using uniform resource locators \(URLs\). In OBS \(compatible with OpenStack Swift\), a resource can be an account, container, object, or specific resource related to an account, container, or object. Such a resource is identified by a URL and can be operated after requests are sent using the URL.

The common URL format is as follows \(the content in brackets \(\[ \]\) is optional\):

protocol ://hostname\[:port\] /v1/account\[/container\] \[/object\] \[?param\]

[Table 1](locating-a-resource.md#table6854763)  describes parameters in a URL.

**Table  1**  URL parameters

<a name="table6854763"></a>
<table><thead align="left"><tr id="row32038589"><th class="cellrowborder" valign="top" width="17.11%" id="mcps1.2.4.1.1"><p id="p44988935"><a name="p44988935"></a><a name="p44988935"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="65.60000000000001%" id="mcps1.2.4.1.2"><p id="p20225109"><a name="p20225109"></a><a name="p20225109"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="17.29%" id="mcps1.2.4.1.3"><p id="p65584754"><a name="p65584754"></a><a name="p65584754"></a>Required or Optional</p>
</th>
</tr>
</thead>
<tbody><tr id="row27621136"><td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.2.4.1.1 "><p id="p54018267"><a name="p54018267"></a><a name="p54018267"></a>protocol</p>
</td>
<td class="cellrowborder" valign="top" width="65.60000000000001%" headers="mcps1.2.4.1.2 "><p id="p26810586"><a name="p26810586"></a><a name="p26810586"></a>Indicates the protocol used for sending requests. Possible values include HTTP and HTTPS.</p>
<p id="p39968683"><a name="p39968683"></a><a name="p39968683"></a>You can specify HTTPS to ensure secure access to resources.</p>
</td>
<td class="cellrowborder" valign="top" width="17.29%" headers="mcps1.2.4.1.3 "><p id="p14183880"><a name="p14183880"></a><a name="p14183880"></a>Required</p>
</td>
</tr>
<tr id="row53749059"><td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.2.4.1.1 "><p id="p63226018"><a name="p63226018"></a><a name="p63226018"></a>hostname</p>
</td>
<td class="cellrowborder" valign="top" width="65.60000000000001%" headers="mcps1.2.4.1.2 "><p id="p5659133"><a name="p5659133"></a><a name="p5659133"></a>Indicates the host name, namely, the domain name or service IP address of OBS (compatible with OpenStack Swift).</p>
</td>
<td class="cellrowborder" valign="top" width="17.29%" headers="mcps1.2.4.1.3 "><p id="p34112870"><a name="p34112870"></a><a name="p34112870"></a>Required</p>
</td>
</tr>
<tr id="row48680776"><td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.2.4.1.1 "><p id="p44771124"><a name="p44771124"></a><a name="p44771124"></a>port</p>
</td>
<td class="cellrowborder" valign="top" width="65.60000000000001%" headers="mcps1.2.4.1.2 "><p id="p49971353155110"><a name="p49971353155110"></a><a name="p49971353155110"></a>Indicates the port enabled for protocols used for sending requests. The value varies with software server deployment. In OBS (compatible with OpenStack Swift), the HTTP port is <strong id="b403665502162048"><a name="b403665502162048"></a><a name="b403665502162048"></a>80</strong>&nbsp;and the HTTPS port is&nbsp;<strong id="b1793576432162048"><a name="b1793576432162048"></a><a name="b1793576432162048"></a>443</strong>. If this parameter is not specified, the default port will be used.</p>
</td>
<td class="cellrowborder" valign="top" width="17.29%" headers="mcps1.2.4.1.3 "><p id="p35946674"><a name="p35946674"></a><a name="p35946674"></a>Optional</p>
</td>
</tr>
<tr id="row10729716172858"><td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.2.4.1.1 "><p id="p63800683172858"><a name="p63800683172858"></a><a name="p63800683172858"></a>v1</p>
</td>
<td class="cellrowborder" valign="top" width="65.60000000000001%" headers="mcps1.2.4.1.2 "><p id="p472863172858"><a name="p472863172858"></a><a name="p472863172858"></a>Indicates the version used in the request. <strong id="b46555465"><a name="b46555465"></a><a name="b46555465"></a>v1</strong> indicates the object storage version.</p>
</td>
<td class="cellrowborder" valign="top" width="17.29%" headers="mcps1.2.4.1.3 "><p id="p25767589173144"><a name="p25767589173144"></a><a name="p25767589173144"></a>Required</p>
</td>
</tr>
<tr id="row59923241172854"><td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.2.4.1.1 "><p id="p21944357172854"><a name="p21944357172854"></a><a name="p21944357172854"></a>account</p>
</td>
<td class="cellrowborder" valign="top" width="65.60000000000001%" headers="mcps1.2.4.1.2 "><p id="p32662489172854"><a name="p32662489172854"></a><a name="p32662489172854"></a>Indicates a user path. Each path identifies a unique user in the system. An account consists of a management prefix and a project ID, for example, <strong id="b842352706101410"><a name="b842352706101410"></a><a name="b842352706101410"></a>AUTH_</strong><em id="i842352697101413"><a name="i842352697101413"></a><a name="i842352697101413"></a>ProjectID</em>.</p>
</td>
<td class="cellrowborder" valign="top" width="17.29%" headers="mcps1.2.4.1.3 "><p id="p28415982172854"><a name="p28415982172854"></a><a name="p28415982172854"></a>Required</p>
</td>
</tr>
<tr id="row10118767"><td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.2.4.1.1 "><p id="p42763981"><a name="p42763981"></a><a name="p42763981"></a>container</p>
</td>
<td class="cellrowborder" valign="top" width="65.60000000000001%" headers="mcps1.2.4.1.2 "><p id="p52847049"><a name="p52847049"></a><a name="p52847049"></a>Indicates a container path.</p>
</td>
<td class="cellrowborder" valign="top" width="17.29%" headers="mcps1.2.4.1.3 "><p id="p48772767"><a name="p48772767"></a><a name="p48772767"></a>Optional</p>
</td>
</tr>
<tr id="row32859274"><td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.2.4.1.1 "><p id="p62499712"><a name="p62499712"></a><a name="p62499712"></a>object</p>
</td>
<td class="cellrowborder" valign="top" width="65.60000000000001%" headers="mcps1.2.4.1.2 "><p id="p37952466"><a name="p37952466"></a><a name="p37952466"></a>Indicates an object path.</p>
</td>
<td class="cellrowborder" valign="top" width="17.29%" headers="mcps1.2.4.1.3 "><p id="p59198213"><a name="p59198213"></a><a name="p59198213"></a>Optional</p>
</td>
</tr>
<tr id="row55809335"><td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.2.4.1.1 "><p id="p54685102"><a name="p54685102"></a><a name="p54685102"></a>param</p>
</td>
<td class="cellrowborder" valign="top" width="65.60000000000001%" headers="mcps1.2.4.1.2 "><p id="p47559554"><a name="p47559554"></a><a name="p47559554"></a>Indicates the specific resource. By default, it is the requested container or object itself.</p>
</td>
<td class="cellrowborder" valign="top" width="17.29%" headers="mcps1.2.4.1.3 "><p id="p58187889"><a name="p58187889"></a><a name="p58187889"></a>Optional</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>HTTP is less secure than HTTPS. HTTPS is recommended.  
>In OBS \(compatible with OpenStack Swift\), HTTPS supports TLS 1.2 only.  

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>If the version in a URL is set to V1 \(the correct one is actually v1\), OBS \(compatible with OpenStack Swift\) returns a 404 Not Found error code, whereas OpenStack Swift returns a 400 Bad Request error code.  

