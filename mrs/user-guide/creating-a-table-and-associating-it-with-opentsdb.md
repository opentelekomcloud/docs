# Creating a Table and Associating It with OpenTSDB<a name="EN-US_TOPIC_0221415069"></a>

## Function<a name="section14297175215515"></a>

MRS Spark can be used to access the data source of OpenTSDB, create association tables in the Spark, and query and insert the OpenTSDB data.

Use the  **CREATE TABLE**  command to create a table and associate it with an existing metric in OpenTSDB.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>If no metric exists in OpenTSDB, an error will be reported when the corresponding table is queried.  

## Syntax<a name="section7314752195113"></a>

```
CREATE TABLE [IF NOT EXISTS] OPENTSDB_TABLE_NAME   USING OPENTSDB OPTIONS (
'metric' = 'METRIC_NAME',
'tags' = 'TAG1,TAG2'
);
```

## Keyword<a name="section1432961213524"></a>

<a name="table103551812185212"></a>
<table><thead align="left"><tr id="row1442312125528"><th class="cellrowborder" valign="top" width="30%" id="mcps1.1.3.1.1"><p id="p194231112205210"><a name="p194231112205210"></a><a name="p194231112205210"></a><strong id="b19595246174417"><a name="b19595246174417"></a><a name="b19595246174417"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="70%" id="mcps1.1.3.1.2"><p id="p54231712175216"><a name="p54231712175216"></a><a name="p54231712175216"></a><strong id="b154648154414"><a name="b154648154414"></a><a name="b154648154414"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1842411285212"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p12424212145211"><a name="p12424212145211"></a><a name="p12424212145211"></a>metric</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p74241012185219"><a name="p74241012185219"></a><a name="p74241012185219"></a>Name of the metric in OpenTSDB corresponding to the table to be created.</p>
</td>
</tr>
<tr id="row16424612185210"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p16424612135220"><a name="p16424612135220"></a><a name="p16424612135220"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p19424161275219"><a name="p19424161275219"></a><a name="p19424161275219"></a>Tag corresponding to the metric. The tags are used for classification, filtering, and quick retrieval. You can set 1 to 8 tags, which are separated by commas (,). The parameter value includes values of all tagks in the corresponding metric.</p>
</td>
</tr>
</tbody>
</table>

## Precautions<a name="section15363201265210"></a>

When creating a table, you do not need to specify the  **timestamp**  and  **value**  fields. The system automatically builds the following fields based on the specified tags. The fields  **TAG1**  and  **TAG2**  are specified by tags.

-   TAG1 String
-   TAG2 String
-   timestamp Timestamp
-   value double

## Example<a name="section11370151213522"></a>

Create table  **opentsdb\_table**  table and associate it with metric  **city.temp**  of the OpenTSDB component.

```
CREATE table opentsdb_table using opentsdb OPTIONS ('metric'='city.temp',  'tags'='city,location');
```

