# Querying the Metadata of a Specified Image \(Discarded\)<a name="EN-US_TOPIC_0065817698"></a>

## Function<a name="en-us_topic_0057973119_section36530619"></a>

This API is used to query the metadata of the specified image.

## Constraints<a name="en-us_topic_0057973119_section6190138"></a>

-   This API will be discarded. You are advised to use the IMS API "Querying Images".

## URI<a name="en-us_topic_0057973119_section60340116"></a>

GET /v2/\{project\_id\}/images/\{image\_id\}/metadata

GET /v2.1/\{project\_id\}/images/\{image\_id\}/metadata

[Table 1](#en-us_topic_0057973119_en-us_topic_0020212650_table62669527)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="en-us_topic_0057973119_en-us_topic_0020212650_table62669527"></a>
<table><thead align="left"><tr id="en-us_topic_0057973119_en-us_topic_0020212650_row33894570"><th class="cellrowborder" valign="top" width="20.74%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.05%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="60.209999999999994%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973119_en-us_topic_0020212650_row8419032"><td class="cellrowborder" valign="top" width="20.74%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973119_en-us_topic_0020212650_p10852974"><a name="en-us_topic_0057973119_en-us_topic_0020212650_p10852974"></a><a name="en-us_topic_0057973119_en-us_topic_0020212650_p10852974"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973119_en-us_topic_0020212650_p6675738"><a name="en-us_topic_0057973119_en-us_topic_0020212650_p6675738"></a><a name="en-us_topic_0057973119_en-us_topic_0020212650_p6675738"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="60.209999999999994%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0057973119_row132721948105411"><td class="cellrowborder" valign="top" width="20.74%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973119_p11272124885417"><a name="en-us_topic_0057973119_p11272124885417"></a><a name="en-us_topic_0057973119_p11272124885417"></a>image_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973119_p11272104895417"><a name="en-us_topic_0057973119_p11272104895417"></a><a name="en-us_topic_0057973119_p11272104895417"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="60.209999999999994%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973119_p11272948145412"><a name="en-us_topic_0057973119_p11272948145412"></a><a name="en-us_topic_0057973119_p11272948145412"></a>Specifies the image ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0057973119_section31639158"></a>

None

## Response<a name="en-us_topic_0057973119_section16316966"></a>

[Table 2](#en-us_topic_0057973119_table16931040)  describes the response parameters.

**Table  2**  Response parameter

<a name="en-us_topic_0057973119_table16931040"></a>
<table><thead align="left"><tr id="en-us_topic_0057973119_row9442355"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.4.1.1"><p id="en-us_topic_0057973119_p26633311"><a name="en-us_topic_0057973119_p26633311"></a><a name="en-us_topic_0057973119_p26633311"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.2"><p id="en-us_topic_0057973119_p9814616"><a name="en-us_topic_0057973119_p9814616"></a><a name="en-us_topic_0057973119_p9814616"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="en-us_topic_0057973119_p36298703"><a name="en-us_topic_0057973119_p36298703"></a><a name="en-us_topic_0057973119_p36298703"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973119_row54513821"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973119_p53543384"><a name="en-us_topic_0057973119_p53543384"></a><a name="en-us_topic_0057973119_p53543384"></a>User customization</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973119_p42046823"><a name="en-us_topic_0057973119_p42046823"></a><a name="en-us_topic_0057973119_p42046823"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973119_p51776931"><a name="en-us_topic_0057973119_p51776931"></a><a name="en-us_topic_0057973119_p51776931"></a>Specifies the key pair of the metadata.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="en-us_topic_0057973119_section12634966"></a>

```
GET https://{endpoint}/v2/9c53a566cb3443ab910cf0daebca90c4/images/17a1890b-0fa4-485e-8505-14e294017988/metadata
GET https://{endpoint}/v2.1/9c53a566cb3443ab910cf0daebca90c4/images/17a1890b-0fa4-485e-8505-14e294017988/metadata
```

## Example Response<a name="section78953122313"></a>

```
{
    "metadata": {
        "__os_version": "Suse Linux Enterprise 12.2 64bit",
        "__image_source_type": "uds",
        "__imagetype": "gold",
        "__os_bit": "64",
        "__os_type": "Suse",
        "__isregistered": "true",
        "__image_location": "192.168.80.11:5080:pcsimsbeta:suse12.2-addx710-05-11",
        "virtual_env_type": "Ironic",
        "__platform": "Suse",
        "__support_o3s": "true"
    }
}
```

## Returned Values<a name="en-us_topic_0057973119_section41491842"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

