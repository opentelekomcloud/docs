# Endpoints and Domain Names<a name="obs_03_0152"></a>

**Endpoint:**  OBS provides an endpoint for each region. An endpoint is a domain name to access OBS in a region and is used to process access requests of that region. For details about regions and endpoints, see  [Regions and Endpoints](https://docs.otc.t-systems.com/en-us/endpoint/index.html).

**Bucket domain name**: Each bucket in OBS has a domain name. A domain name is the Internet address of a bucket and can be used to access the bucket over the Internet. It is applicable to cloud application development and data sharing scenarios.

An OBS bucket domain name is in the format  **_BucketName.Endpoint_**, where  **BucketName**  indicates the name of the bucket, and  **Endpoint**  indicates the domain name of the region where the bucket is located.

[Table 1](#table94332031121816)  lists the bucket domain name and other domain names in OBS, including their formats and protocols.

**Table  1**  OBS domain names

<a name="table94332031121816"></a>
<table><thead align="left"><tr id="row154336315183"><th class="cellrowborder" valign="top" width="11.940000000000001%" id="mcps1.2.5.1.1"><p id="p1443393181818"><a name="p1443393181818"></a><a name="p1443393181818"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="39.489999999999995%" id="mcps1.2.5.1.2"><p id="p1643412316188"><a name="p1643412316188"></a><a name="p1643412316188"></a>Structure</p>
</th>
<th class="cellrowborder" valign="top" width="40.56%" id="mcps1.2.5.1.3"><p id="p2434831101818"><a name="p2434831101818"></a><a name="p2434831101818"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="8.01%" id="mcps1.2.5.1.4"><p id="p153466530208"><a name="p153466530208"></a><a name="p153466530208"></a>Protocol</p>
</th>
</tr>
</thead>
<tbody><tr id="row343414317188"><td class="cellrowborder" valign="top" width="11.940000000000001%" headers="mcps1.2.5.1.1 "><p id="p743463191818"><a name="p743463191818"></a><a name="p743463191818"></a>Regional domain name</p>
</td>
<td class="cellrowborder" valign="top" width="39.489999999999995%" headers="mcps1.2.5.1.2 "><p id="p143411310182"><a name="p143411310182"></a><a name="p143411310182"></a><strong id="b166673318532"><a name="b166673318532"></a><a name="b166673318532"></a>Endpoint</strong></p>
</td>
<td class="cellrowborder" valign="top" width="40.56%" headers="mcps1.2.5.1.3 "><p id="p115115654012"><a name="p115115654012"></a><a name="p115115654012"></a>Each region has an endpoint, which is the domain name of the region.</p>
<p id="p061553143519"><a name="p061553143519"></a><a name="p061553143519"></a>For regions and endpoints, see <a href="https://docs.otc.t-systems.com/en-us/endpoint/index.html" target="_blank" rel="noopener noreferrer">Regions and Endpoints</a>.</p>
</td>
<td class="cellrowborder" valign="top" width="8.01%" headers="mcps1.2.5.1.4 "><p id="p579925213555"><a name="p579925213555"></a><a name="p579925213555"></a>HTTPS</p>
<p id="p103465535203"><a name="p103465535203"></a><a name="p103465535203"></a>HTTP</p>
</td>
</tr>
<tr id="row94341931171819"><td class="cellrowborder" valign="top" width="11.940000000000001%" headers="mcps1.2.5.1.1 "><p id="p1343443111810"><a name="p1343443111810"></a><a name="p1343443111810"></a>Bucket domain name</p>
</td>
<td class="cellrowborder" valign="top" width="39.489999999999995%" headers="mcps1.2.5.1.2 "><p id="p6434131131813"><a name="p6434131131813"></a><a name="p6434131131813"></a><strong id="b129431695318"><a name="b129431695318"></a><a name="b129431695318"></a>BucketName.Endpoint</strong></p>
</td>
<td class="cellrowborder" valign="top" width="40.56%" headers="mcps1.2.5.1.3 "><p id="p5434331191817"><a name="p5434331191817"></a><a name="p5434331191817"></a>After a bucket is created, you can use the domain name to access the bucket. You can compose the domain name according to the structure of bucket domain names, or you can obtain it from basic information of the bucket on OBS Console, OBS Browser.</p>
</td>
<td class="cellrowborder" valign="top" width="8.01%" headers="mcps1.2.5.1.4 "><p id="p166078569551"><a name="p166078569551"></a><a name="p166078569551"></a>HTTPS</p>
<p id="p134675352019"><a name="p134675352019"></a><a name="p134675352019"></a>HTTP</p>
</td>
</tr>
<tr id="row9434153141812"><td class="cellrowborder" valign="top" width="11.940000000000001%" headers="mcps1.2.5.1.1 "><p id="p9434133113188"><a name="p9434133113188"></a><a name="p9434133113188"></a>Object domain name</p>
</td>
<td class="cellrowborder" valign="top" width="39.489999999999995%" headers="mcps1.2.5.1.2 "><p id="p443473113188"><a name="p443473113188"></a><a name="p443473113188"></a><strong id="b11401337205418"><a name="b11401337205418"></a><a name="b11401337205418"></a>BucketName.Endpoint/ObjectName</strong></p>
</td>
<td class="cellrowborder" valign="top" width="40.56%" headers="mcps1.2.5.1.3 "><p id="p1443403115186"><a name="p1443403115186"></a><a name="p1443403115186"></a>After an object is uploaded to a bucket, you can use the object domain name to access the object. You can compose the domain name according to the structure of object domain names, or you can obtain it from the object details on OBS Console, OBS Browser. Alternatively, you can call the GetObjectUrl API through the SDK to obtain the object domain name.</p>
</td>
<td class="cellrowborder" valign="top" width="8.01%" headers="mcps1.2.5.1.4 "><p id="p132801859105519"><a name="p132801859105519"></a><a name="p132801859105519"></a>HTTPS</p>
<p id="p13462053122016"><a name="p13462053122016"></a><a name="p13462053122016"></a>HTTP</p>
</td>
</tr>
<tr id="row1434193171811"><td class="cellrowborder" valign="top" width="11.940000000000001%" headers="mcps1.2.5.1.1 "><p id="p4434113141820"><a name="p4434113141820"></a><a name="p4434113141820"></a>Static website domain name</p>
</td>
<td class="cellrowborder" valign="top" width="39.489999999999995%" headers="mcps1.2.5.1.2 "><p id="p13434631111815"><a name="p13434631111815"></a><a name="p13434631111815"></a><strong id="b1514554345410"><a name="b1514554345410"></a><a name="b1514554345410"></a>BucketName.obs-website.Enpoint</strong></p>
</td>
<td class="cellrowborder" valign="top" width="40.56%" headers="mcps1.2.5.1.3 "><p id="p443423181814"><a name="p443423181814"></a><a name="p443423181814"></a>Static website domain name is a bucket domain name when the bucket is configured to host a static website.</p>
</td>
<td class="cellrowborder" valign="top" width="8.01%" headers="mcps1.2.5.1.4 "><p id="p1019528565"><a name="p1019528565"></a><a name="p1019528565"></a>HTTPS</p>
<p id="p10346155302015"><a name="p10346155302015"></a><a name="p10346155302015"></a>HTTP</p>
</td>
</tr>
</tbody>
</table>

