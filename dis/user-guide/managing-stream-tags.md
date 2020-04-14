# Managing Stream Tags<a name="dis_01_0050"></a>

A tag is an identifier of a stream. Adding tags to streams can help you identify and manage your stream resources.

You can add a maximum of 10 tags to a stream when creating the stream or add them on the details page of the created stream.

A tag consists of a tag key and a tag value.  [Table 1](#en-us_topic_0110219762_table16316649132010)  describes the rules for naming the tag key and value.

**Table  1**  Naming rules for a tag key and value

<a name="en-us_topic_0110219762_table16316649132010"></a>
<table><thead align="left"><tr id="en-us_topic_0110219762_row63177491201"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="en-us_topic_0110219762_p231714491209"><a name="en-us_topic_0110219762_p231714491209"></a><a name="en-us_topic_0110219762_p231714491209"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="en-us_topic_0110219762_p163171849152013"><a name="en-us_topic_0110219762_p163171849152013"></a><a name="en-us_topic_0110219762_p163171849152013"></a>Rule</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="en-us_topic_0110219762_p11317249122016"><a name="en-us_topic_0110219762_p11317249122016"></a><a name="en-us_topic_0110219762_p11317249122016"></a>Example</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0110219762_row93171449162013"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0110219762_p931774942019"><a name="en-us_topic_0110219762_p931774942019"></a><a name="en-us_topic_0110219762_p931774942019"></a>Key</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0110219762_p5771249122112"><a name="en-us_topic_0110219762_p5771249122112"></a><a name="en-us_topic_0110219762_p5771249122112"></a>A tag key cannot be left blank.</p>
<p id="en-us_topic_0110219762_p26351751142112"><a name="en-us_topic_0110219762_p26351751142112"></a><a name="en-us_topic_0110219762_p26351751142112"></a>A tag key must be unique for a stream.</p>
<p id="en-us_topic_0110219762_p93113330223"><a name="en-us_topic_0110219762_p93113330223"></a><a name="en-us_topic_0110219762_p93113330223"></a>A tag key contains a maximum of 36 characters.</p>
<p id="p1225516520470"><a name="p1225516520470"></a><a name="p1225516520470"></a>A tag value cannot contain special characters =*&lt;&gt;\,|/ or start or end with a space.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0110219762_p2317144913209"><a name="en-us_topic_0110219762_p2317144913209"></a><a name="en-us_topic_0110219762_p2317144913209"></a>Organization</p>
</td>
</tr>
<tr id="en-us_topic_0110219762_row193176495203"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0110219762_p931714916209"><a name="en-us_topic_0110219762_p931714916209"></a><a name="en-us_topic_0110219762_p931714916209"></a>Tag value</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0110219762_p14986938142211"><a name="en-us_topic_0110219762_p14986938142211"></a><a name="en-us_topic_0110219762_p14986938142211"></a>A tag value contains a maximum of 43 characters.</p>
<p id="p1111264194711"><a name="p1111264194711"></a><a name="p1111264194711"></a>A tag value cannot contain special characters =*&lt;&gt;\,|/ or start or end with a space. This parameter can be left blank.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0110219762_p431704919201"><a name="en-us_topic_0110219762_p431704919201"></a><a name="en-us_topic_0110219762_p431704919201"></a>Apache</p>
</td>
</tr>
</tbody>
</table>

## Adding a Tag to a Stream<a name="section93865701015"></a>

You can add a tag to a stream on the  **Buy Stream**  page.

1.  Log in to the management console.
2.  Choose  **Enterprise Intelligence**  \>  **Data Ingestion Service**.
3.  On the DIS management console, click  **Buy Stream**.
4.  On the  **Advanced Settings**  tab page, select  **Configure**.

    Enter the key and value of a tag to be added.

    You can add a maximum of 10 tags to the stream and use intersections of tags to search for the target stream.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >You can also add tags to existing streams. For details, see  [Managing Tags](#section188067265123).  


## Searching for a Target Stream<a name="section9673161212119"></a>

You can search for a target stream by tag on the  **Stream Management**  page.

1.  Log in to the management console.
2.  Choose  **EI Enterprise Intelligent**  \>  **Data Ingestion Service**.
3.  In the navigation tree, choose  **Ingestion Management**  \>  **Stream Management**. In the upper right corner of the page, click  **Search by Tag**.
4.  Enter the tag key and value of the stream you are searching for.

    You can select a tag key or tag value from its drop-down list. When the tag key or tag value is exactly matched, the system can automatically locate the target stream. If you enter multiple tags, their intersections are used to search for the stream.

5.  Click  **Search**.

    The system searches for the target stream by tag key or value.


## Managing Tags<a name="section188067265123"></a>

You can add, delete, modify, and view tags on the  **Tags**  tab page of a stream.

1.  Log in to the management console.
2.  Choose  **EI Enterprise Intelligent**  \>  **Data Ingestion Service**.
3.  In the navigation tree, choose  **Ingestion Management**  \>  **Stream Management**. Click a stream to which the tags to be managed belong to.

    The stream details page is displayed.

4.  Click the  **Tags**  tab and add, deleted, modify, and view tags.
    -   View

        On the  **Tags**  tab page, you can view details about tags of the stream, including the number of tags and the key and value of each tag.

    -   Add

        Click  **Add Tag**  in the upper left corner. In the displayed  **Add Tag**  dialog box, enter the key and value of the tag to be added, and click  **OK**.

    -   Modify

        In the  **Operation**  column of a tag, click  **Edit**. In the displayed  **Edit Tag**  page, enter a new tag key and value and click  **OK**.

    -   Delete

        In the  **Operation**  column of the tag, click  **Delete**. After confirmation, click  **OK**  on the displayed  **Delete Tag**  page.



