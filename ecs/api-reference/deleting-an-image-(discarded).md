# Deleting an Image \(Discarded\)<a name="EN-US_TOPIC_0065817699"></a>

## Function<a name="en-us_topic_0057973130_section46534580"></a>

This API is used to delete a specified image. The image cannot be restored after being deleted.

## Constraints<a name="en-us_topic_0057973130_section11204655"></a>

-   This API will be discarded. You are advised to use the IMS API "Deleting an Image \(Native OpenStack API\)".

## URI<a name="en-us_topic_0057973130_section16158042"></a>

DELETE /v2/\{project\_id\}/images/\{image\_id\}

DELETE /v2.1/\{project\_id\}/images/\{image\_id\}

[Table 1](#en-us_topic_0057973130_en-us_topic_0020212650_table62669527)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="en-us_topic_0057973130_en-us_topic_0020212650_table62669527"></a>
<table><thead align="left"><tr id="en-us_topic_0057973130_en-us_topic_0020212650_row33894570"><th class="cellrowborder" valign="top" width="20.74%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.05%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="60.209999999999994%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973130_en-us_topic_0020212650_row8419032"><td class="cellrowborder" valign="top" width="20.74%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973130_en-us_topic_0020212650_p10852974"><a name="en-us_topic_0057973130_en-us_topic_0020212650_p10852974"></a><a name="en-us_topic_0057973130_en-us_topic_0020212650_p10852974"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973130_en-us_topic_0020212650_p6675738"><a name="en-us_topic_0057973130_en-us_topic_0020212650_p6675738"></a><a name="en-us_topic_0057973130_en-us_topic_0020212650_p6675738"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="60.209999999999994%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0057973130_row132721948105411"><td class="cellrowborder" valign="top" width="20.74%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973130_p11272124885417"><a name="en-us_topic_0057973130_p11272124885417"></a><a name="en-us_topic_0057973130_p11272124885417"></a>image_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973130_p11272104895417"><a name="en-us_topic_0057973130_p11272104895417"></a><a name="en-us_topic_0057973130_p11272104895417"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="60.209999999999994%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973130_p11272948145412"><a name="en-us_topic_0057973130_p11272948145412"></a><a name="en-us_topic_0057973130_p11272948145412"></a>Specifies the image ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0057973130_section35161875"></a>

None

## Response<a name="en-us_topic_0057973130_section48021419"></a>

None

## Example Request<a name="en-us_topic_0057973130_section29539590"></a>

```
DELETE https://{endpoint}/v2/9c53a566cb3443ab910cf0daebca90c4/images/6cad483b-e281-4985-a345-7afef1f3c5b7
DELETE https://{endpoint}/v2.1/9c53a566cb3443ab910cf0daebca90c4/images/6cad483b-e281-4985-a345-7afef1f3c5b7
```

## Example Response<a name="section5751181218241"></a>

None

## Returned Values<a name="en-us_topic_0057973130_section3564114017426"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

