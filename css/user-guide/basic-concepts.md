# Basic Concepts<a name="css_04_0003"></a>

For details about Elasticsearch concepts, visit the following website:

[https://www.elastic.co/guide/en/elasticsearch/reference/6.2/\_basic\_concepts.html](https://www.elastic.co/guide/en/elasticsearch/reference/6.2/_basic_concepts.html)

## Cluster<a name="en-us_topic_0103614115_section1830421944212"></a>

CSS provides functions on a per cluster basis. A cluster represents an independent search service that consists of multiple nodes.

## Index<a name="en-us_topic_0103614115_section19166022134218"></a>

Index, similar to "Database" in the relational database \(RDB\), stores Elasticsearch data. It refers to a logical space that consists of one or more shards.

**Table  1**  Mapping between Elasticsearch and RDB

<a name="en-us_topic_0103614115_table748644118216"></a>
<table><tbody><tr id="en-us_topic_0103614115_row1448718416214"><th class="firstcol" valign="top" width="19%" id="mcps1.2.7.1.1"><p id="en-us_topic_0103614115_p84877416219"><a name="en-us_topic_0103614115_p84877416219"></a><a name="en-us_topic_0103614115_p84877416219"></a>Elasticsearch</p>
</th>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0103614115_p2048764117216"><a name="en-us_topic_0103614115_p2048764117216"></a><a name="en-us_topic_0103614115_p2048764117216"></a>Index</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0103614115_p15487184192119"><a name="en-us_topic_0103614115_p15487184192119"></a><a name="en-us_topic_0103614115_p15487184192119"></a>Document Type</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0103614115_p6487184115215"><a name="en-us_topic_0103614115_p6487184115215"></a><a name="en-us_topic_0103614115_p6487184115215"></a>Document</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0103614115_p1948719411216"><a name="en-us_topic_0103614115_p1948719411216"></a><a name="en-us_topic_0103614115_p1948719411216"></a>Field</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0103614115_p5180916821"><a name="en-us_topic_0103614115_p5180916821"></a><a name="en-us_topic_0103614115_p5180916821"></a>Mapping</p>
</td>
</tr>
<tr id="en-us_topic_0103614115_row109591755537"><th class="firstcol" valign="top" width="19%" id="mcps1.2.7.2.1"><p id="en-us_topic_0103614115_p7874502418"><a name="en-us_topic_0103614115_p7874502418"></a><a name="en-us_topic_0103614115_p7874502418"></a>RDB</p>
</th>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.7.2.1 "><p id="en-us_topic_0103614115_p108747011416"><a name="en-us_topic_0103614115_p108747011416"></a><a name="en-us_topic_0103614115_p108747011416"></a>Database</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.7.2.1 "><p id="en-us_topic_0103614115_p198746014410"><a name="en-us_topic_0103614115_p198746014410"></a><a name="en-us_topic_0103614115_p198746014410"></a>Table</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.7.2.1 "><p id="en-us_topic_0103614115_p128741601746"><a name="en-us_topic_0103614115_p128741601746"></a><a name="en-us_topic_0103614115_p128741601746"></a>Row</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.2.1 "><p id="en-us_topic_0103614115_p11874120441"><a name="en-us_topic_0103614115_p11874120441"></a><a name="en-us_topic_0103614115_p11874120441"></a>Column</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.7.2.1 "><p id="en-us_topic_0103614115_p0874401749"><a name="en-us_topic_0103614115_p0874401749"></a><a name="en-us_topic_0103614115_p0874401749"></a>Schema</p>
</td>
</tr>
</tbody>
</table>

## Shard<a name="en-us_topic_0103614115_section78422819503"></a>

An index can potentially store a large amount of data that can exceed the hardware limits of a single node. To solve this problem, Elasticsearch provides the ability to subdivide your index into multiple pieces called shards. When you create an index, you can simply define the number of shards that you want. Each shard is in itself a fully-functional and independent "index" that can be hosted on any node in the cluster.

You need to specify the number of shards before creating an index and cannot change the number after the index is successfully created.

## Replica<a name="en-us_topic_0103614115_section1728813145500"></a>

A replica is a copy of the actual storage index in a shard. It can be understood as a backup of the shard. Replicas help prevent single point of failures \(SPOFs\). You can increase or decrease the number of replicas based on your service requirements.

## Document<a name="en-us_topic_0103614115_section95801224500"></a>

An entity for Elasticsearch storage. Equivalent to the row in the RDB, the document is the basic unit that can be indexed.

## Document Type<a name="en-us_topic_0103614115_section05836341509"></a>

Similar to the table in the RDB, the document type is used to distinguish between different data. One index can contain multiple document types. A document actually must be indexed to a document type inside an index.

## Mapping<a name="en-us_topic_0103614115_section6795201915110"></a>

A mapping is used to restrict the type of a field and can be automatically created based on data. It is similar to the schema in the database.

## Field<a name="en-us_topic_0103614115_section155732145251"></a>

Minimum unit of a document. The field is similar to the column in the database.

