# Error Responses Syntax<a name="EN-US_TOPIC_0125560307"></a>

## Error Response Headers<a name="section43457779"></a>

In an error response, header information contains:

-   Content-Type: application/xml
-   HTTP status code 3_xx_, 4_xx_, or 5_xx_. For details, see [Table 1](error-codes.md#table30733758).

## Error Response Body<a name="section55575695"></a>

The response body contains several elements that provide error details. The following is an example error response containing all common elements in REST error responses:

```
<?xml version="1.0" encoding="UTF-8"?> 
 <Error> 
 <Code>NoSuchKey</Code> 
 <Message>The resource you requested does not exist</Message> 
 <Resource>/example-bucket/object</Resource> 
 <RequestId>001B21A61C6C0000013402C4616D5285</RequestId> 
 <HostId>RkRCRDJENDc5MzdGQkQ4OUY3MTI4NTQ3NDk2Mjg0M0FB 
 QUFBQUFBYmJiYmJiYmJD</HostId> 
 </Error>     
```

## Error Response Elements<a name="section30419215"></a>

[Table 1](#table5435182)  describes REST response elements.

**Table  1**  Error response elements

<a name="table5435182"></a>
<table><thead align="left"><tr id="row3125665"><th class="cellrowborder" valign="top" width="24.25%" id="mcps1.2.3.1.1"><p id="p51852321"><a name="p51852321"></a><a name="p51852321"></a>Element</p>
</th>
<th class="cellrowborder" valign="top" width="75.75%" id="mcps1.2.3.1.2"><p id="p39288453"><a name="p39288453"></a><a name="p39288453"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row28248118"><td class="cellrowborder" valign="top" width="24.25%" headers="mcps1.2.3.1.1 "><p id="p6396187"><a name="p6396187"></a><a name="p6396187"></a>Error</p>
</td>
<td class="cellrowborder" valign="top" width="75.75%" headers="mcps1.2.3.1.2 "><p id="p48329116"><a name="p48329116"></a><a name="p48329116"></a>Container of all error elements.</p>
</td>
</tr>
<tr id="row32308867"><td class="cellrowborder" valign="top" width="24.25%" headers="mcps1.2.3.1.1 "><p id="p66881467"><a name="p66881467"></a><a name="p66881467"></a>Code</p>
</td>
<td class="cellrowborder" valign="top" width="75.75%" headers="mcps1.2.3.1.2 "><p id="p48689731"><a name="p48689731"></a><a name="p48689731"></a>A string that uniquely identifies an error. For details about error codes, see <a href="error-codes.md#table30733758">Table 1</a>.</p>
</td>
</tr>
<tr id="row51554115"><td class="cellrowborder" valign="top" width="24.25%" headers="mcps1.2.3.1.1 "><p id="p15133796"><a name="p15133796"></a><a name="p15133796"></a>Message</p>
</td>
<td class="cellrowborder" valign="top" width="75.75%" headers="mcps1.2.3.1.2 "><p id="p17877965"><a name="p17877965"></a><a name="p17877965"></a>Error details in the XML format. For details about error codes, see <a href="error-codes.md#table30733758">Table 1</a>.</p>
</td>
</tr>
<tr id="row38829095"><td class="cellrowborder" valign="top" width="24.25%" headers="mcps1.2.3.1.1 "><p id="p58149018"><a name="p58149018"></a><a name="p58149018"></a>RequestId</p>
</td>
<td class="cellrowborder" valign="top" width="75.75%" headers="mcps1.2.3.1.2 "><p id="p12449997"><a name="p12449997"></a><a name="p12449997"></a>ID of the request whose error response is returned. The ID is used for locating internal errors.</p>
</td>
</tr>
<tr id="row44941110"><td class="cellrowborder" valign="top" width="24.25%" headers="mcps1.2.3.1.1 "><p id="p16351276"><a name="p16351276"></a><a name="p16351276"></a>HostId</p>
</td>
<td class="cellrowborder" valign="top" width="75.75%" headers="mcps1.2.3.1.2 "><p id="p49385016"><a name="p49385016"></a><a name="p49385016"></a>ID of the server that returns an error response.</p>
</td>
</tr>
<tr id="row41811960"><td class="cellrowborder" valign="top" width="24.25%" headers="mcps1.2.3.1.1 "><p id="p31325629"><a name="p31325629"></a><a name="p31325629"></a>Resource</p>
</td>
<td class="cellrowborder" valign="top" width="75.75%" headers="mcps1.2.3.1.2 "><p id="p54348043"><a name="p54348043"></a><a name="p54348043"></a>The requested resource such as a bucket or object.</p>
</td>
</tr>
</tbody>
</table>

>![](/images/icon-note.gif) **NOTE:**   
>Many error responses contain additional structured data, which can be easily read and understood during error diagnosis.  

