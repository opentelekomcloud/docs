# Inserting Data to the OpenTSDB Table<a name="EN-US_TOPIC_0221415070"></a>

## Function<a name="section2167437125214"></a>

Run the  **INSERT INTO**  statement to insert the data in the table to the associated  **OpenTSDB metric**.

## Syntax<a name="section41681537155216"></a>

```
INSERT INTO TABLE_NAME SELECT * FROM SRC_TABLE;
INSERT INTO TABLE_NAME VALUES(XXX);
```

## Keyword<a name="section5170183716527"></a>

<a name="table1817193710524"></a>
<table><thead align="left"><tr id="row42382375527"><th class="cellrowborder" valign="top" width="30%" id="mcps1.1.3.1.1"><p id="p1423823745220"><a name="p1423823745220"></a><a name="p1423823745220"></a><strong id="b14104163514303"><a name="b14104163514303"></a><a name="b14104163514303"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="70%" id="mcps1.1.3.1.2"><p id="p18239537115218"><a name="p18239537115218"></a><a name="p18239537115218"></a><strong id="b63453653012"><a name="b63453653012"></a><a name="b63453653012"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row323913745210"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p15239133735214"><a name="p15239133735214"></a><a name="p15239133735214"></a>TABLE_NAME</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p1523993745219"><a name="p1523993745219"></a><a name="p1523993745219"></a>Name of the associated OpenTSDB table.</p>
</td>
</tr>
<tr id="row2239837105215"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p11239153785212"><a name="p11239153785212"></a><a name="p11239153785212"></a>SRC_TABLE</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p7239103765217"><a name="p7239103765217"></a><a name="p7239103765217"></a>Name of the table from which data is obtained. This parameter can be set to a name of a common table.</p>
</td>
</tr>
</tbody>
</table>

## Precautions<a name="section13175153785212"></a>

-   The inserted data cannot be  **null**. If the inserted data is the same as the original data or only the  **value**  is different, the inserted data overwrites the original data.
-   **INSERT OVERWRITE**  is not supported.
-   You are advised not to concurrently insert data into a table. If you concurrently insert data into a table, there is a possibility that conflicts occur, leading to failed data insertion.
-   The  **TIMESTAMP**  format supports only yyyy-MM-dd hh:mm:ss.

## Example<a name="section7179937145212"></a>

Insert data into table  **opentsdb\_table**.

```
insert into opentsdb_table values('shenzhen','futian','2018-05-03 00:00:00',21);
```

