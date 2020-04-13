# Sending a Request<a name="EN-US_TOPIC_0125560363"></a>

OBS is based on a standard request and response model. A request sent to OBS must comply with HTTP 1.1 and headers of a request must contain OBS-defined parameters, for example, authentication fields.

Requests can be sent to OBS using multiple HTTP methods such as  **GET**, **PUT**, **POST**, **DELETE**, and **HEAD**. You can send a **GET**, **PUT**, **POST**, **DELETE**, or **HEAD** request to read, create, update, delete, or obtain a resource. [Table 1](#table55931017)  describes the request methods supported by OBS REST APIs.

**Table  1**  HTTP request methods supported by OBS REST APIs

<a name="table55931017"></a>
<table><thead align="left"><tr id="row5662578"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p56015673"><a name="p56015673"></a><a name="p56015673"></a>Method</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p40975656"><a name="p40975656"></a><a name="p40975656"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row30693864"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p3175073"><a name="p3175073"></a><a name="p3175073"></a>GET</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p55854330"><a name="p55854330"></a><a name="p55854330"></a>Requests that the server returns a specific resource, for example, a bucket list or object.</p>
</td>
</tr>
<tr id="row32926922"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p49834998"><a name="p49834998"></a><a name="p49834998"></a>PUT</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p10103063"><a name="p10103063"></a><a name="p10103063"></a>Requests that the server creates a specific resource, for example, a bucket or object.</p>
</td>
</tr>
<tr id="row23818711"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p50267458"><a name="p50267458"></a><a name="p50267458"></a>POST</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p45132310"><a name="p45132310"></a><a name="p45132310"></a>Requests that the server performs specific operations on a specific resource, for example, initiating or completing a multipart upload.</p>
</td>
</tr>
<tr id="row3537606"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p18110665"><a name="p18110665"></a><a name="p18110665"></a>DELETE</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p57677769"><a name="p57677769"></a><a name="p57677769"></a>Requests that the server deletes a specific resource, for example, an object.</p>
</td>
</tr>
<tr id="row49337875"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p36944920"><a name="p36944920"></a><a name="p36944920"></a>HEAD</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p39748558"><a name="p39748558"></a><a name="p39748558"></a>Requests that the server returns the metadata of a specific resource, for example, object metadata.</p>
</td>
</tr>
</tbody>
</table>

## Request Headers<a name="section42253696"></a>

Parameters must be specified in the headers of requests sent to OBS using OBS REST APIs. For details about headers common to OBS REST requests, see section  [Common Request Headers](common-request-headers.md).

