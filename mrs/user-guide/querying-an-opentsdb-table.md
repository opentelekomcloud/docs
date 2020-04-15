# Querying an OpenTSDB Table<a name="EN-US_TOPIC_0221415071"></a>

This  **SELECT**  command is used to query data in an OpenTSDB table.

## Syntax<a name="section6313185812529"></a>

```
SELECT * FROM table_name WHERE tagk=tagv LIMIT number;
```

## Keyword<a name="section1931315582526"></a>

<a name="table1817193710524"></a>
<table><thead align="left"><tr id="row42382375527"><th class="cellrowborder" valign="top" width="30%" id="mcps1.1.3.1.1"><p id="p1423823745220"><a name="p1423823745220"></a><a name="p1423823745220"></a><strong id="b1684104918132"><a name="b1684104918132"></a><a name="b1684104918132"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="70%" id="mcps1.1.3.1.2"><p id="p18239537115218"><a name="p18239537115218"></a><a name="p18239537115218"></a><strong id="b1386615503130"><a name="b1386615503130"></a><a name="b1386615503130"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row323913745210"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p4512182532414"><a name="p4512182532414"></a><a name="p4512182532414"></a>LIMIT</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p1523993745219"><a name="p1523993745219"></a><a name="p1523993745219"></a>Used to limit the query results.</p>
</td>
</tr>
<tr id="row2239837105215"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p96329379241"><a name="p96329379241"></a><a name="p96329379241"></a>number</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p7239103765217"><a name="p7239103765217"></a><a name="p7239103765217"></a>Only the INT type is supported.</p>
</td>
</tr>
</tbody>
</table>

## Precautions<a name="section1331415589523"></a>

-   The to-be-queried table must exist. Otherwise, an error is reported.
-   The value of  **tagv**  must exist. Otherwise, an error occurs.

## Example<a name="section1231515865218"></a>

Query data in the  **opentsdb\_table**  table.

```
SELECT * FROM opentsdb_table LIMIT 100;
SELECT * FROM opentsdb_table WHERE city='shenzhen';
```

