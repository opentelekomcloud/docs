# Storage Classes Overview<a name="en-us_topic_0050937852"></a>

OBS supports tiered storage classes at the bucket level and object level.

OBS provides the following storage classes: Standard, Warm, and Cold.

Different storage classes meet different requirements for storage performance and costs.

-   The Standard storage class features low access latency and high throughput. It is therefore suitable for storing a massive number of hot files \(frequently accessed every month\) or small files \(less than 1 MB\). The application scenarios include big data analytics, mobile apps, hot videos, and social apps.
-   The Warm storage class is ideal for storing data that is semi-frequently accessed \(less than 12 times a year\), with requirements for quick response. The application scenarios include file synchronization, file sharing, and enterprise backup. It provides the same durability, access latency, and throughput as the Standard storage class but at a lower cost. However, the Warm storage class has lower availability than the Standard storage class.
-   The Cold storage class is suitable for archiving data that is rarely-accessed \(averagely once a year\). The application scenarios include data archiving and long-term data backups. The Cold storage class is secure, durable, and inexpensive, and can be used to replace tape libraries. However, it may take hours to restore data from the Archive storage class.

## Bucket Storage Classes vs. Object Storage Classes<a name="section510051131514"></a>

When an object is uploaded, it inherits the storage class of the bucket by default. You can change the default storage class when you upload the object.

Changing the storage class of a bucket does not change the storage classes of existing objects in the bucket, but newly uploaded objects inherit the new storage class by default.

## Comparison of Storage Classes<a name="section64461132193015"></a>

<a name="table1410941163116"></a>
<table><thead align="left"><tr id="row1410174113319"><th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.1"><p id="p1110194153116"><a name="p1110194153116"></a><a name="p1110194153116"></a>Compared Item</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.2"><p id="p51064110319"><a name="p51064110319"></a><a name="p51064110319"></a>Standard</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.3"><p id="p1521511382333"><a name="p1521511382333"></a><a name="p1521511382333"></a>Warm</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.4"><p id="p51226614339"><a name="p51226614339"></a><a name="p51226614339"></a>Cold</p>
</th>
</tr>
</thead>
<tbody><tr id="row103188419355"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p131810412351"><a name="p131810412351"></a><a name="p131810412351"></a>Feature</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="p2031818473511"><a name="p2031818473511"></a><a name="p2031818473511"></a>Top-notch performance, highly reliable and available </p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.3 "><p id="p83181416352"><a name="p83181416352"></a><a name="p83181416352"></a>Reliable, inexpensive, and real-time storage access</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.4 "><p id="p19318134103517"><a name="p19318134103517"></a><a name="p19318134103517"></a>Long-term storage for archived data at a very low cost</p>
</td>
</tr>
<tr id="row265162715348"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p46642711342"><a name="p46642711342"></a><a name="p46642711342"></a>Application scenarios</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="p466627123418"><a name="p466627123418"></a><a name="p466627123418"></a>Cloud application, data sharing, content sharing, and hot data storage</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.3 "><p id="p06613277349"><a name="p06613277349"></a><a name="p06613277349"></a>Web disk applications, enterprise backup, active archiving, and data monitoring</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.4 "><p id="p186612743416"><a name="p186612743416"></a><a name="p186612743416"></a>Archive, medical image storage, video material storage, and replacement of tape libraries</p>
</td>
</tr>
<tr id="row565445793616"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p136541857183616"><a name="p136541857183616"></a><a name="p136541857183616"></a>Minimum storage duration</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="p18654105712362"><a name="p18654105712362"></a><a name="p18654105712362"></a>Not required</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.3 "><p id="p12654145712368"><a name="p12654145712368"></a><a name="p12654145712368"></a>30 days</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.4 "><p id="p10654165783617"><a name="p10654165783617"></a><a name="p10654165783617"></a>90 days</p>
</td>
</tr>
</tbody>
</table>

