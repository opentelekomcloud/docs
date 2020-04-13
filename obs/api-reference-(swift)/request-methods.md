# Request Methods<a name="obs_03_0008"></a>

A request sent to OBS \(compatible with OpenStack Swift\) must comply with HTTP 1.1. In addition, the headers of a request must contain parameters defined in IAM, for example, authentication fields.

HTTP supports several HTTP request methods, such as GET, PUT, POST, DELETE, HEAD, and COPY. A request method indicates how to access specific resources.  [Table 1](request-methods.md#table55931017)  describes the request methods supported by REST APIs that are provided by OBS \(compatible with OpenStack Swift\).

**Table  1**  REST request methods supported by OBS \(compatible with OpenStack Swift\)

<a name="table55931017"></a>
<table><thead align="left"><tr id="row43512002"><th class="cellrowborder" valign="top" width="23.79%" id="mcps1.2.3.1.1"><p id="p34811256"><a name="p34811256"></a><a name="p34811256"></a>Method</p>
</th>
<th class="cellrowborder" valign="top" width="76.21%" id="mcps1.2.3.1.2"><p id="p1139524"><a name="p1139524"></a><a name="p1139524"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row25192587"><td class="cellrowborder" valign="top" width="23.79%" headers="mcps1.2.3.1.1 "><p id="p27333687"><a name="p27333687"></a><a name="p27333687"></a>GET</p>
</td>
<td class="cellrowborder" valign="top" width="76.21%" headers="mcps1.2.3.1.2 "><p id="p66545072"><a name="p66545072"></a><a name="p66545072"></a>Requests the server to return a specific resource, for example, obtaining a container or object list or downloading an object.</p>
</td>
</tr>
<tr id="row62034741"><td class="cellrowborder" valign="top" width="23.79%" headers="mcps1.2.3.1.1 "><p id="p58758091"><a name="p58758091"></a><a name="p58758091"></a>PUT</p>
</td>
<td class="cellrowborder" valign="top" width="76.21%" headers="mcps1.2.3.1.2 "><p id="p61784930"><a name="p61784930"></a><a name="p61784930"></a>Requests the server to store a specific resource, for example, creating a container or uploading an object.</p>
</td>
</tr>
<tr id="row19193461"><td class="cellrowborder" valign="top" width="23.79%" headers="mcps1.2.3.1.1 "><p id="p11166512"><a name="p11166512"></a><a name="p11166512"></a>POST</p>
</td>
<td class="cellrowborder" valign="top" width="76.21%" headers="mcps1.2.3.1.2 "><p id="p32072255"><a name="p32072255"></a><a name="p32072255"></a>Requests the server to modify a specific resource such as container or object metadata.</p>
</td>
</tr>
<tr id="row20214842"><td class="cellrowborder" valign="top" width="23.79%" headers="mcps1.2.3.1.1 "><p id="p26789475"><a name="p26789475"></a><a name="p26789475"></a>DELETE</p>
</td>
<td class="cellrowborder" valign="top" width="76.21%" headers="mcps1.2.3.1.2 "><p id="p22463828"><a name="p22463828"></a><a name="p22463828"></a>Requests the server to delete a specific resource such as an object.</p>
</td>
</tr>
<tr id="row64416501"><td class="cellrowborder" valign="top" width="23.79%" headers="mcps1.2.3.1.1 "><p id="p50354060"><a name="p50354060"></a><a name="p50354060"></a>HEAD</p>
</td>
<td class="cellrowborder" valign="top" width="76.21%" headers="mcps1.2.3.1.2 "><p id="p52147080"><a name="p52147080"></a><a name="p52147080"></a>Requests the server to return the digest of a specific resource, for example, obtaining object metadata.</p>
</td>
</tr>
<tr id="row7477386152536"><td class="cellrowborder" valign="top" width="23.79%" headers="mcps1.2.3.1.1 "><p id="p187614152536"><a name="p187614152536"></a><a name="p187614152536"></a>COPY</p>
</td>
<td class="cellrowborder" valign="top" width="76.21%" headers="mcps1.2.3.1.2 "><p id="p15196741152536"><a name="p15196741152536"></a><a name="p15196741152536"></a>Requests the server to copy a specific resource such as an object.</p>
</td>
</tr>
</tbody>
</table>

## Request Headers<a name="section20832974"></a>

When sending a REST request to OBS \(compatible with OpenStack Swift\), you need to add parameters in request headers. For details about request headers, see the descriptions of the specific operations.

## HTTP Request Rules<a name="section354231515409"></a>

-   The number of HTTP headers cannot exceed 90. If the token header is included, the number of HTTP headers cannot exceed 91.
-   The total size of all HTTP headers cannot exceed 4096 bytes.
-   The length per HTTP request line cannot exceed 8192 bytes.
-   The data in an HTTP request cannot exceed 5 GB.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >When sending a REST request to OBS \(compatible with OpenStack Swift\), you must comply with the preceding HTTP request rules. If any upper limit is exceeded, the error response may be different from that defined by OpenStack Swift. The request rules for the original OpenStack Swift APIs do not strictly check requests based on the preceding rules, but require users to comply with the preceding standard HTTP request rules.  

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >When the parameter length \(request headers and content\) of a request exceeds the buffer size of the server, OBS \(compatible with OpenStack Swift\) returns a 413 Request Entity Too Large: head, whereas OpenStack Swift returns a 400 Bad Request.  


