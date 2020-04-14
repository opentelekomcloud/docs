# Querying the List of Event Log Files<a name="EN-US_TOPIC_0193631180"></a>

## Function Description<a name="section32792555"></a>

This API is used to query the list of event log files.

## URI<a name="section26697540"></a>

-   URI format

    GET  /v1/\{project\_id\}/waf/event/dump?offset=\{offset\}&limit=\{limit\}

-   Parameter description

    **Table  1**  Path parameters

    <a name="table9786546"></a>
    <table><thead align="left"><tr id="row45293161"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p44867418"><a name="p44867418"></a><a name="p44867418"></a><strong id="b8938194854910"><a name="b8938194854910"></a><a name="b8938194854910"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.2"><p id="p10382207"><a name="p10382207"></a><a name="p10382207"></a><strong id="b19189950184911"><a name="b19189950184911"></a><a name="b19189950184911"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.3"><p id="p35652416"><a name="p35652416"></a><a name="p35652416"></a><strong id="b126918515499"><a name="b126918515499"></a><a name="b126918515499"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.5.1.4"><p id="p2164615"><a name="p2164615"></a><a name="p2164615"></a><strong id="b6172165394911"><a name="b6172165394911"></a><a name="b6172165394911"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row41116089"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p42068928"><a name="p42068928"></a><a name="p42068928"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p52140036"><a name="p52140036"></a><a name="p52140036"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p62593388"><a name="p62593388"></a><a name="p62593388"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p36899681"><a name="p36899681"></a><a name="p36899681"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row30072732"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p19972195"><a name="p19972195"></a><a name="p19972195"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p7135119"><a name="p7135119"></a><a name="p7135119"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p41073800"><a name="p41073800"></a><a name="p41073800"></a>Long</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p21617533"><a name="p21617533"></a><a name="p21617533"></a>Specifies the number of returned pages. Its value ranges from <strong id="b62414315508"><a name="b62414315508"></a><a name="b62414315508"></a>0</strong> to <strong id="b324113315501"><a name="b324113315501"></a><a name="b324113315501"></a>65535</strong>. The default value is <strong id="b182411320504"><a name="b182411320504"></a><a name="b182411320504"></a>0</strong>.</p>
    </td>
    </tr>
    <tr id="row12247267"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p52504570"><a name="p52504570"></a><a name="p52504570"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p25011769"><a name="p25011769"></a><a name="p25011769"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p12687433"><a name="p12687433"></a><a name="p12687433"></a>Long</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p25357967"><a name="p25357967"></a><a name="p25357967"></a>Specifies the maximum number of records displayed on each page. Its value ranges from <strong id="b152329814504"><a name="b152329814504"></a><a name="b152329814504"></a>0</strong> to <strong id="b023914820508"><a name="b023914820508"></a><a name="b023914820508"></a>50</strong>. The default value is <strong id="b62395817507"><a name="b62395817507"></a><a name="b62395817507"></a>10</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section38951274"></a>

Request parameters

None

## Response<a name="section15017149"></a>

Response parameters

**Table  2**  Parameter description

<a name="table15472974"></a>
<table><thead align="left"><tr id="row56736167"><th class="cellrowborder" valign="top" width="30.316968303169677%" id="mcps1.2.4.1.1"><p id="p32226778"><a name="p32226778"></a><a name="p32226778"></a><strong id="b959141617504"><a name="b959141617504"></a><a name="b959141617504"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="29.88701129887011%" id="mcps1.2.4.1.2"><p id="p60232263"><a name="p60232263"></a><a name="p60232263"></a><strong id="b1118551765017"><a name="b1118551765017"></a><a name="b1118551765017"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.4.1.3"><p id="p46975124"><a name="p46975124"></a><a name="p46975124"></a><strong id="b1212971885018"><a name="b1212971885018"></a><a name="b1212971885018"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row20122934"><td class="cellrowborder" valign="top" width="30.316968303169677%" headers="mcps1.2.4.1.1 "><p id="p19344951"><a name="p19344951"></a><a name="p19344951"></a>total</p>
</td>
<td class="cellrowborder" valign="top" width="29.88701129887011%" headers="mcps1.2.4.1.2 "><p id="p23437164"><a name="p23437164"></a><a name="p23437164"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p19362109"><a name="p19362109"></a><a name="p19362109"></a>Specifies the total number of log files.</p>
</td>
</tr>
<tr id="row40041260"><td class="cellrowborder" valign="top" width="30.316968303169677%" headers="mcps1.2.4.1.1 "><p id="p22116660"><a name="p22116660"></a><a name="p22116660"></a>items</p>
</td>
<td class="cellrowborder" valign="top" width="29.88701129887011%" headers="mcps1.2.4.1.2 "><p id="p46619020"><a name="p46619020"></a><a name="p46619020"></a><a href="#table16394183011019">Table 3</a></p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p1603648"><a name="p1603648"></a><a name="p1603648"></a>Specifies the log file objects.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **items**

<a name="table16394183011019"></a>
<table><thead align="left"><tr id="row939613301015"><th class="cellrowborder" valign="top" width="30.936906309369068%" id="mcps1.2.4.1.1"><p id="p039873016013"><a name="p039873016013"></a><a name="p039873016013"></a><strong id="b1684465411526"><a name="b1684465411526"></a><a name="b1684465411526"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="28.727127287271276%" id="mcps1.2.4.1.2"><p id="p183997301406"><a name="p183997301406"></a><a name="p183997301406"></a><strong id="b752445610526"><a name="b752445610526"></a><a name="b752445610526"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="40.33596640335966%" id="mcps1.2.4.1.3"><p id="p839973013010"><a name="p839973013010"></a><a name="p839973013010"></a><strong id="b1648525735216"><a name="b1648525735216"></a><a name="b1648525735216"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row6254134620148"><td class="cellrowborder" valign="top" width="30.936906309369068%" headers="mcps1.2.4.1.1 "><p id="p15927154410145"><a name="p15927154410145"></a><a name="p15927154410145"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="28.727127287271276%" headers="mcps1.2.4.1.2 "><p id="p18929194417149"><a name="p18929194417149"></a><a name="p18929194417149"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40.33596640335966%" headers="mcps1.2.4.1.3 "><p id="p8930944171414"><a name="p8930944171414"></a><a name="p8930944171414"></a>Specifies the ID of a log file.</p>
</td>
</tr>
<tr id="row9253144691412"><td class="cellrowborder" valign="top" width="30.936906309369068%" headers="mcps1.2.4.1.1 "><p id="p1493184451410"><a name="p1493184451410"></a><a name="p1493184451410"></a>filename</p>
</td>
<td class="cellrowborder" valign="top" width="28.727127287271276%" headers="mcps1.2.4.1.2 "><p id="p17933114491410"><a name="p17933114491410"></a><a name="p17933114491410"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40.33596640335966%" headers="mcps1.2.4.1.3 "><p id="p15934444201410"><a name="p15934444201410"></a><a name="p15934444201410"></a>Specifies the name of a log file.</p>
</td>
</tr>
<tr id="row325324620149"><td class="cellrowborder" valign="top" width="30.936906309369068%" headers="mcps1.2.4.1.1 "><p id="p7481196132815"><a name="p7481196132815"></a><a name="p7481196132815"></a>total</p>
</td>
<td class="cellrowborder" valign="top" width="28.727127287271276%" headers="mcps1.2.4.1.2 "><p id="p1960181082811"><a name="p1960181082811"></a><a name="p1960181082811"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="40.33596640335966%" headers="mcps1.2.4.1.3 "><p id="p169381144191419"><a name="p169381144191419"></a><a name="p169381144191419"></a>Specifies the total number of events in a log file.</p>
</td>
</tr>
<tr id="row8253104617149"><td class="cellrowborder" valign="top" width="30.936906309369068%" headers="mcps1.2.4.1.1 "><p id="p139407442141"><a name="p139407442141"></a><a name="p139407442141"></a>url</p>
</td>
<td class="cellrowborder" valign="top" width="28.727127287271276%" headers="mcps1.2.4.1.2 "><p id="p1494224410148"><a name="p1494224410148"></a><a name="p1494224410148"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40.33596640335966%" headers="mcps1.2.4.1.3 "><p id="p1454465813112"><a name="p1454465813112"></a><a name="p1454465813112"></a>Specifies the URL to download a log file.</p>
</td>
</tr>
<tr id="row2025284612149"><td class="cellrowborder" valign="top" width="30.936906309369068%" headers="mcps1.2.4.1.1 "><p id="p17943164411414"><a name="p17943164411414"></a><a name="p17943164411414"></a>timestamp</p>
</td>
<td class="cellrowborder" valign="top" width="28.727127287271276%" headers="mcps1.2.4.1.2 "><p id="p169441144111414"><a name="p169441144111414"></a><a name="p169441144111414"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="40.33596640335966%" headers="mcps1.2.4.1.3 "><p id="p199461944101413"><a name="p199461944101413"></a><a name="p199461944101413"></a>Specifies the time when a log file is generated.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section1014014529435"></a>

**total**  with a value of  **2**  is used as an example.

Response example

```
{
  "total": 2,
  "items": [{
      "id": "3a9b5c0f96784ec8abd8ba61a98064ef",
      "filename": "WAF-eu-de-2019-01-15.csv",
      "total": "100",
      "url": "https://obs_server/obs-waf-log/WAF-eu-de-2019-01-15-xxxxxxxxxx.csv?AWSAccessKeyId=XXXXXXXXXXXX&Expires=1547632&Signature=nC7ipaGzLQs",
      "timestamp": 1499817600
    }, {
      "id": "44d887434169475794b2717438f7fa78",
      "filename": "WAF-eu-de-2019-01-14.csv",
      "total": "200",
      "url": "https://obs_server/obs-waf-log/WAF-eu-de-2019-01-14-xxxxxxxxxx.csv?AWSAccessKeyId=XXXXXXXXXXXX&Expires=1547632&Signature=nC7ipaGzLQs",
      "timestamp": 1499817601
    }
  ]
}
```

