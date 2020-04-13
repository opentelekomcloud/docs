# Storage Classes Overview<a name="obs_03_0012"></a>

OBS supports tiered storage classes at the bucket and object level.

OBS offers three storage classes: Standard, Warm, and Cold, comprehensively meeting customers' varying requirements on storage performance and costs.

Different storage classes meet different needs for storage performance and costs.

-   The Standard storage class features low access latency and high throughput. It is therefore applicable to storing massive hot files \(frequently access every month\) or small files \(less than 1 MB\). The application scenarios include Big Data analytics, mobile apps, hot videos, and storing of social images.
-   The Warm storage class is applicable to storing less frequently accessed data \(less than 12 times per year on average\) with fast access response. The application scenarios include file synchronization or sharing, and enterprise-level backup. It provides the same durability, access latency, and throughput as the Standard storage class but at a lower price. However, the Warm storage class has lower availability than the Standard one.
-   The Cold storage class is applicable to archiving rarely-accessed \(averagely once a year\) data. The application scenarios include data archiving and long-term data retention for backup. The Cold storage class is secure, durable, and inexpensive, which can replace tape libraries. However, it can take up to hours to restore data from the Cold storage class.

## Bucket Storage Classes vs. Object Storage Classes<a name="en-us_topic_0050937852_section510051131514"></a>

When an object is uploaded, it inherits the storage class of the bucket by default. You can change the default storage class for the object to be uploaded.

Changing the storage class of a bucket does not change the storage classes of existing objects in the bucket, but newly uploaded objects inherit the new storage class by default.

## Comparison of Storage Classes<a name="en-us_topic_0050937852_section64461132193015"></a>

<a name="en-us_topic_0050937852_table1410941163116"></a>
<table><thead align="left"><tr id="en-us_topic_0050937852_row1410174113319"><th class="cellrowborder" valign="top" width="18.61%" id="mcps1.1.5.1.1"><p id="en-us_topic_0050937852_p1110194153116"><a name="en-us_topic_0050937852_p1110194153116"></a><a name="en-us_topic_0050937852_p1110194153116"></a>Compared Item</p>
</th>
<th class="cellrowborder" valign="top" width="26.51%" id="mcps1.1.5.1.2"><p id="en-us_topic_0050937852_p51064110319"><a name="en-us_topic_0050937852_p51064110319"></a><a name="en-us_topic_0050937852_p51064110319"></a>Standard</p>
</th>
<th class="cellrowborder" valign="top" width="27.66%" id="mcps1.1.5.1.3"><p id="en-us_topic_0050937852_p1521511382333"><a name="en-us_topic_0050937852_p1521511382333"></a><a name="en-us_topic_0050937852_p1521511382333"></a>Warm</p>
</th>
<th class="cellrowborder" valign="top" width="27.22%" id="mcps1.1.5.1.4"><p id="en-us_topic_0050937852_p51226614339"><a name="en-us_topic_0050937852_p51226614339"></a><a name="en-us_topic_0050937852_p51226614339"></a>Cold</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0050937852_row103188419355"><td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0050937852_p131810412351"><a name="en-us_topic_0050937852_p131810412351"></a><a name="en-us_topic_0050937852_p131810412351"></a>Feature</p>
</td>
<td class="cellrowborder" valign="top" width="26.51%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0050937852_p2031818473511"><a name="en-us_topic_0050937852_p2031818473511"></a><a name="en-us_topic_0050937852_p2031818473511"></a>Top-notch performance, highly reliable and available </p>
</td>
<td class="cellrowborder" valign="top" width="27.66%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0050937852_p83181416352"><a name="en-us_topic_0050937852_p83181416352"></a><a name="en-us_topic_0050937852_p83181416352"></a>Reliable, inexpensive, and real-time storage access</p>
</td>
<td class="cellrowborder" valign="top" width="27.22%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0050937852_p19318134103517"><a name="en-us_topic_0050937852_p19318134103517"></a><a name="en-us_topic_0050937852_p19318134103517"></a>Long-term storage for archived data for very low cost</p>
</td>
</tr>
<tr id="en-us_topic_0050937852_row265162715348"><td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0050937852_p46642711342"><a name="en-us_topic_0050937852_p46642711342"></a><a name="en-us_topic_0050937852_p46642711342"></a>Application scenarios</p>
</td>
<td class="cellrowborder" valign="top" width="26.51%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0050937852_p466627123418"><a name="en-us_topic_0050937852_p466627123418"></a><a name="en-us_topic_0050937852_p466627123418"></a>Cloud application, data sharing, content sharing, and hot data storage</p>
</td>
<td class="cellrowborder" valign="top" width="27.66%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0050937852_p06613277349"><a name="en-us_topic_0050937852_p06613277349"></a><a name="en-us_topic_0050937852_p06613277349"></a>Web disk applications, enterprise backup, active archiving, and data monitoring</p>
</td>
<td class="cellrowborder" valign="top" width="27.22%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0050937852_p186612743416"><a name="en-us_topic_0050937852_p186612743416"></a><a name="en-us_topic_0050937852_p186612743416"></a>Archive, medical image storage, video material storage, and replacement of tape libraries</p>
</td>
</tr>
<tr id="en-us_topic_0050937852_row565445793616"><td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0050937852_p136541857183616"><a name="en-us_topic_0050937852_p136541857183616"></a><a name="en-us_topic_0050937852_p136541857183616"></a>Minimum storage duration</p>
</td>
<td class="cellrowborder" valign="top" width="26.51%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0050937852_p18654105712362"><a name="en-us_topic_0050937852_p18654105712362"></a><a name="en-us_topic_0050937852_p18654105712362"></a>Not required</p>
</td>
<td class="cellrowborder" valign="top" width="27.66%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0050937852_p12654145712368"><a name="en-us_topic_0050937852_p12654145712368"></a><a name="en-us_topic_0050937852_p12654145712368"></a>30 days</p>
</td>
<td class="cellrowborder" valign="top" width="27.22%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0050937852_p10654165783617"><a name="en-us_topic_0050937852_p10654165783617"></a><a name="en-us_topic_0050937852_p10654165783617"></a>90 days</p>
</td>
</tr>
</tbody>
</table>

