# Modifying the Default Configuration Data<a name="EN-US_TOPIC_0221415072"></a>

By default, connect the local TSD process of the node where the Spark executor resides with OpenTSDB. In MRS, use the default configuration.

**Table  1**  OpenTSDB data source configuration

<a name="table13240911145315"></a>
<table><tbody><tr id="row33121811195313"><td class="cellrowborder" valign="top" width="39.53%"><p id="p33121119534"><a name="p33121119534"></a><a name="p33121119534"></a>Item</p>
</td>
<td class="cellrowborder" valign="top" width="32.25%"><p id="p33131911135319"><a name="p33131911135319"></a><a name="p33131911135319"></a>Description</p>
</td>
<td class="cellrowborder" valign="top" width="28.22%"><p id="p143131911105315"><a name="p143131911105315"></a><a name="p143131911105315"></a>Example Value</p>
</td>
</tr>
<tr id="row9313171145320"><td class="cellrowborder" valign="top" width="39.53%"><p id="p183132011145313"><a name="p183132011145313"></a><a name="p183132011145313"></a>spark.sql.datasource.opentsdb.host</p>
</td>
<td class="cellrowborder" valign="top" width="32.25%"><p id="p2313161111538"><a name="p2313161111538"></a><a name="p2313161111538"></a>IP address of the connected TSD process.</p>
</td>
<td class="cellrowborder" valign="top" width="28.22%"><p id="p3313811165314"><a name="p3313811165314"></a><a name="p3313811165314"></a>Null (default value)</p>
<p id="p613845811342"><a name="p613845811342"></a><a name="p613845811342"></a><strong id="b8477111810537"><a name="b8477111810537"></a><a name="b8477111810537"></a>xx.xx.xx.xx</strong> indicates the IP address. Separate multiple IP addresses with commas (,).</p>
</td>
</tr>
<tr id="row93131311145311"><td class="cellrowborder" valign="top" width="39.53%"><p id="p13313111155314"><a name="p13313111155314"></a><a name="p13313111155314"></a>spark.sql.datasource.opentsdb.port</p>
</td>
<td class="cellrowborder" valign="top" width="32.25%"><p id="p153131911155317"><a name="p153131911155317"></a><a name="p153131911155317"></a>Port number of the TSD process.</p>
</td>
<td class="cellrowborder" valign="top" width="28.22%"><p id="p63131611105311"><a name="p63131611105311"></a><a name="p63131611105311"></a>4242 (default value)</p>
</td>
</tr>
<tr id="row0313191155314"><td class="cellrowborder" valign="top" width="39.53%"><p id="p93131511105317"><a name="p93131511105317"></a><a name="p93131511105317"></a>spark.sql.datasource.opentsdb.randomSeed</p>
</td>
<td class="cellrowborder" valign="top" width="32.25%"><p id="p531341114537"><a name="p531341114537"></a><a name="p531341114537"></a>Whether to use the random seed when the <strong id="b4347145132020"><a name="b4347145132020"></a><a name="b4347145132020"></a>spark.sql.datasource.opentsdb.host</strong> is configured with multiple addresses. If this parameter is set to <strong id="b472711305542"><a name="b472711305542"></a><a name="b472711305542"></a>false</strong>, all executors on the same node are connected to the same host. In this way, <strong id="b9913544185419"><a name="b9913544185419"></a><a name="b9913544185419"></a>spark.blacklist.enabled=true</strong> can be used to implement task fault tolerance.</p>
</td>
<td class="cellrowborder" valign="top" width="28.22%"><p id="p1131371113534"><a name="p1131371113534"></a><a name="p1131371113534"></a>false by default</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section17239141145318"></a>

Run the  **set**  statement in  **spark-sql**  and  **spark-beeline**, and then run other SQL statements.

```
set spark.sql.datasource.opentsdb.host = 192.168.2.143,192.168.2.158;
SELECT * FROM opentsdb_table ;
```

