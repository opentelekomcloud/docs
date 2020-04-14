# Creating a Cluster<a name="css_03_0019"></a>

## Function<a name="section5535191365611"></a>

This API is used to create a cluster.

## URI<a name="section3535913135615"></a>

```
POST /v1.0/{project_id}/clusters
```

**Table  1**  Parameter description

<a name="table155351113195611"></a>
<table><thead align="left"><tr id="row311410148566"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.1"><p id="p1911411455617"><a name="p1911411455617"></a><a name="p1911411455617"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.2.5.1.2"><p id="p811414147563"><a name="p811414147563"></a><a name="p811414147563"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="p211416149565"><a name="p211416149565"></a><a name="p211416149565"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="46%" id="mcps1.2.5.1.4"><p id="p12114914175616"><a name="p12114914175616"></a><a name="p12114914175616"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row011401445615"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p13114114115610"><a name="p13114114115610"></a><a name="p13114114115610"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.2 "><p id="p131141614105611"><a name="p131141614105611"></a><a name="p131141614105611"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p211481414566"><a name="p211481414566"></a><a name="p211481414566"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p8114151414568"><a name="p8114151414568"></a><a name="p8114151414568"></a>Project ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section3535201311569"></a>

[Table 2](#table1839843619476)  describes the request parameters.

**Table  2**  Parameter description

<a name="table1839843619476"></a>
<table><thead align="left"><tr id="row144081836154714"><th class="cellrowborder" valign="top" width="21.21212121212121%" id="mcps1.2.5.1.1"><p id="p1440963624719"><a name="p1440963624719"></a><a name="p1440963624719"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.171717171717173%" id="mcps1.2.5.1.2"><p id="p1141311365470"><a name="p1141311365470"></a><a name="p1141311365470"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.333333333333334%" id="mcps1.2.5.1.3"><p id="p13414193614478"><a name="p13414193614478"></a><a name="p13414193614478"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="47.28282828282829%" id="mcps1.2.5.1.4"><p id="p104181436174710"><a name="p104181436174710"></a><a name="p104181436174710"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row16421936164713"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.5.1.1 "><p id="p042443610476"><a name="p042443610476"></a><a name="p042443610476"></a>cluster</p>
</td>
<td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.2 "><p id="p1142863618470"><a name="p1142863618470"></a><a name="p1142863618470"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.333333333333334%" headers="mcps1.2.5.1.3 "><p id="p743111368475"><a name="p743111368475"></a><a name="p743111368475"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="47.28282828282829%" headers="mcps1.2.5.1.4 "><p id="p11434436174715"><a name="p11434436174715"></a><a name="p11434436174715"></a>Cluster object. For details about related parameters, see <a href="#table1535613145617">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **cluster**  field description

<a name="table1535613145617"></a>
<table><thead align="left"><tr id="row21141114115612"><th class="cellrowborder" valign="top" width="17.313131313131315%" id="mcps1.2.5.1.1"><p id="p1411411416567"><a name="p1411411416567"></a><a name="p1411411416567"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18.31313131313131%" id="mcps1.2.5.1.2"><p id="p1311471415563"><a name="p1311471415563"></a><a name="p1311471415563"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="18.535353535353536%" id="mcps1.2.5.1.3"><p id="p511491418566"><a name="p511491418566"></a><a name="p511491418566"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="45.83838383838384%" id="mcps1.2.5.1.4"><p id="p4114714155614"><a name="p4114714155614"></a><a name="p4114714155614"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row101143141560"><td class="cellrowborder" valign="top" width="17.313131313131315%" headers="mcps1.2.5.1.1 "><p id="p12114181411565"><a name="p12114181411565"></a><a name="p12114181411565"></a>instance</p>
</td>
<td class="cellrowborder" valign="top" width="18.31313131313131%" headers="mcps1.2.5.1.2 "><p id="p12114131425613"><a name="p12114131425613"></a><a name="p12114131425613"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.535353535353536%" headers="mcps1.2.5.1.3 "><p id="p311441411563"><a name="p311441411563"></a><a name="p311441411563"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="45.83838383838384%" headers="mcps1.2.5.1.4 "><p id="p4114171475610"><a name="p4114171475610"></a><a name="p4114171475610"></a>Instance object. For details about related parameters, see <a href="#table1656713138562">Table 4</a>.</p>
</td>
</tr>
<tr id="row0288165613411"><td class="cellrowborder" valign="top" width="17.313131313131315%" headers="mcps1.2.5.1.1 "><p id="p519571284210"><a name="p519571284210"></a><a name="p519571284210"></a>datastore</p>
</td>
<td class="cellrowborder" valign="top" width="18.31313131313131%" headers="mcps1.2.5.1.2 "><p id="p0195181211421"><a name="p0195181211421"></a><a name="p0195181211421"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.535353535353536%" headers="mcps1.2.5.1.3 "><p id="p1719515127429"><a name="p1719515127429"></a><a name="p1719515127429"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="45.83838383838384%" headers="mcps1.2.5.1.4 "><p id="p18195201210421"><a name="p18195201210421"></a><a name="p18195201210421"></a>Type of the data search engine. For details about related parameters, see <a href="#table1121072510499">Table 7</a>.</p>
</td>
</tr>
<tr id="row1911451410564"><td class="cellrowborder" valign="top" width="17.313131313131315%" headers="mcps1.2.5.1.1 "><p id="p311421412568"><a name="p311421412568"></a><a name="p311421412568"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="18.31313131313131%" headers="mcps1.2.5.1.2 "><p id="p13114101410568"><a name="p13114101410568"></a><a name="p13114101410568"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.535353535353536%" headers="mcps1.2.5.1.3 "><p id="p211416149564"><a name="p211416149564"></a><a name="p211416149564"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.83838383838384%" headers="mcps1.2.5.1.4 "><p id="p101141514135615"><a name="p101141514135615"></a><a name="p101141514135615"></a>Cluster name. It contains 4 to 32 characters. Only letters, digits, hyphens (-), and underscores (_) are allowed. The value must start with a letter.</p>
</td>
</tr>
<tr id="row163153654912"><td class="cellrowborder" valign="top" width="17.313131313131315%" headers="mcps1.2.5.1.1 "><p id="p2316163499"><a name="p2316163499"></a><a name="p2316163499"></a>instanceNum</p>
</td>
<td class="cellrowborder" valign="top" width="18.31313131313131%" headers="mcps1.2.5.1.2 "><p id="p1931606104919"><a name="p1931606104919"></a><a name="p1931606104919"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.535353535353536%" headers="mcps1.2.5.1.3 "><p id="p15316156154916"><a name="p15316156154916"></a><a name="p15316156154916"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="45.83838383838384%" headers="mcps1.2.5.1.4 "><p id="p1131636164912"><a name="p1131636164912"></a><a name="p1131636164912"></a>Number of cluster instances. The value range is 1 to 32.</p>
</td>
</tr>
<tr id="row1391892313405"><td class="cellrowborder" valign="top" width="17.313131313131315%" headers="mcps1.2.5.1.1 "><p id="p8918132324017"><a name="p8918132324017"></a><a name="p8918132324017"></a>diskEncryption</p>
</td>
<td class="cellrowborder" valign="top" width="18.31313131313131%" headers="mcps1.2.5.1.2 "><p id="p3918192334014"><a name="p3918192334014"></a><a name="p3918192334014"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.535353535353536%" headers="mcps1.2.5.1.3 "><p id="p1991832310403"><a name="p1991832310403"></a><a name="p1991832310403"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="45.83838383838384%" headers="mcps1.2.5.1.4 "><p id="p1919523194019"><a name="p1919523194019"></a><a name="p1919523194019"></a>Whether disks are encrypted. For details about related parameters, see <a href="#table18671184912468">Table 8</a>.</p>
</td>
</tr>
<tr id="row1532416411127"><td class="cellrowborder" valign="top" width="17.313131313131315%" headers="mcps1.2.5.1.1 "><p id="p1834019412129"><a name="p1834019412129"></a><a name="p1834019412129"></a>httpsEnable</p>
</td>
<td class="cellrowborder" valign="top" width="18.31313131313131%" headers="mcps1.2.5.1.2 "><p id="p1034024171218"><a name="p1034024171218"></a><a name="p1034024171218"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.535353535353536%" headers="mcps1.2.5.1.3 "><p id="p13340174115126"><a name="p13340174115126"></a><a name="p13340174115126"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.83838383838384%" headers="mcps1.2.5.1.4 "><p id="p434054111210"><a name="p434054111210"></a><a name="p434054111210"></a>Whether communication encryption is performed on the cluster. Available values include <strong id="b3595124913285"><a name="b3595124913285"></a><a name="b3595124913285"></a>true</strong> and <strong id="b1960114516289"><a name="b1960114516289"></a><a name="b1960114516289"></a>false</strong>. By default, communication encryption is enabled.</p>
<a name="ul1620016015114"></a><a name="ul1620016015114"></a><ul id="ul1620016015114"><li>Value <strong id="b67881516192918"><a name="b67881516192918"></a><a name="b67881516192918"></a>true</strong> indicates that communication encryption is performed on the cluster.</li><li>Value <strong id="b740663482913"><a name="b740663482913"></a><a name="b740663482913"></a>false</strong> indicates that communication encryption is not performed on the cluster.</li></ul>
</td>
</tr>
</tbody>
</table>

**Table  4** **instance**  field description

<a name="table1656713138562"></a>
<table><thead align="left"><tr id="row311410146564"><th class="cellrowborder" valign="top" width="15.841584158415841%" id="mcps1.2.5.1.1"><p id="p13114121413566"><a name="p13114121413566"></a><a name="p13114121413566"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13.861386138613863%" id="mcps1.2.5.1.2"><p id="p6114161410569"><a name="p6114161410569"></a><a name="p6114161410569"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="12.871287128712872%" id="mcps1.2.5.1.3"><p id="p12114171435615"><a name="p12114171435615"></a><a name="p12114171435615"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="57.42574257425742%" id="mcps1.2.5.1.4"><p id="p11114314145619"><a name="p11114314145619"></a><a name="p11114314145619"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row2114314115613"><td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.1 "><p id="p111431445615"><a name="p111431445615"></a><a name="p111431445615"></a>flavorRef</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.2 "><p id="p1911421455618"><a name="p1911421455618"></a><a name="p1911421455618"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.5.1.3 "><p id="p11145146569"><a name="p11145146569"></a><a name="p11145146569"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.42574257425742%" headers="mcps1.2.5.1.4 "><p id="p111145146568"><a name="p111145146568"></a><a name="p111145146568"></a>Instance flavor name. For example:</p>
<a name="ul55698341357"></a><a name="ul55698341357"></a><ul id="ul55698341357"><li>Value range of flavor <strong id="b54801110164"><a name="b54801110164"></a><a name="b54801110164"></a>css.medium.8</strong>: 40 GB to 640 GB</li><li>Value range of flavor <strong id="b2028019193505"><a name="b2028019193505"></a><a name="b2028019193505"></a>css.large.8</strong>: 40 GB to 1,280 GB</li><li>Value range of flavor <strong id="b131001025135013"><a name="b131001025135013"></a><a name="b131001025135013"></a>css.xlarge.8</strong>: 40 GB to 2,560 GB</li><li>Value range of flavor <strong id="b18766102895012"><a name="b18766102895012"></a><a name="b18766102895012"></a>css.2xlarge.8</strong>: 80 GB to 5,120 GB</li><li>Value range of flavor <strong id="b18539173112509"><a name="b18539173112509"></a><a name="b18539173112509"></a>css.4xlarge.8</strong>: 160 GB to 10,240 GB</li></ul>
<a name="ul148819369529"></a><a name="ul148819369529"></a>
</td>
</tr>
<tr id="row14114514205612"><td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.1 "><p id="p6114314175617"><a name="p6114314175617"></a><a name="p6114314175617"></a>volume</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.2 "><p id="p411491485612"><a name="p411491485612"></a><a name="p411491485612"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.5.1.3 "><p id="p16114514195615"><a name="p16114514195615"></a><a name="p16114514195615"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="57.42574257425742%" headers="mcps1.2.5.1.4 "><p id="p1011491417565"><a name="p1011491417565"></a><a name="p1011491417565"></a>Information about the volume. For details about related parameters, see <a href="#table11567131335613">Table 5</a>.</p>
</td>
</tr>
<tr id="row211481410562"><td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.1 "><p id="p17114171445618"><a name="p17114171445618"></a><a name="p17114171445618"></a>nics</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.2 "><p id="p111144141567"><a name="p111144141567"></a><a name="p111144141567"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.5.1.3 "><p id="p131146145562"><a name="p131146145562"></a><a name="p131146145562"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="57.42574257425742%" headers="mcps1.2.5.1.4 "><p id="p19114171413565"><a name="p19114171413565"></a><a name="p19114171413565"></a>Subnet information. For details about related parameters, see <a href="#table1959831319562">Table 6</a>.</p>
</td>
</tr>
<tr id="row1471028164115"><td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.1 "><p id="p1641339204112"><a name="p1641339204112"></a><a name="p1641339204112"></a>availability_zone</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.2 "><p id="p17641239194115"><a name="p17641239194115"></a><a name="p17641239194115"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.5.1.3 "><p id="p5641339154116"><a name="p5641339154116"></a><a name="p5641339154116"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.42574257425742%" headers="mcps1.2.5.1.4 "><p id="p1464133919412"><a name="p1464133919412"></a><a name="p1464133919412"></a>Availability zone (AZ).</p>
</td>
</tr>
</tbody>
</table>

**Table  5** **volume**  field description

<a name="table11567131335613"></a>
<table><thead align="left"><tr id="row4114101435619"><th class="cellrowborder" valign="top" width="15.559999999999999%" id="mcps1.2.5.1.1"><p id="p1511401416567"><a name="p1511401416567"></a><a name="p1511401416567"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.44%" id="mcps1.2.5.1.2"><p id="p311471413563"><a name="p311471413563"></a><a name="p311471413563"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="12.32%" id="mcps1.2.5.1.3"><p id="p16114151416564"><a name="p16114151416564"></a><a name="p16114151416564"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="57.68%" id="mcps1.2.5.1.4"><p id="p411414143564"><a name="p411414143564"></a><a name="p411414143564"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row12114314195613"><td class="cellrowborder" valign="top" width="15.559999999999999%" headers="mcps1.2.5.1.1 "><p id="p1211414145563"><a name="p1211414145563"></a><a name="p1211414145563"></a>volume_type</p>
</td>
<td class="cellrowborder" valign="top" width="14.44%" headers="mcps1.2.5.1.2 "><p id="p11114121465615"><a name="p11114121465615"></a><a name="p11114121465615"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="12.32%" headers="mcps1.2.5.1.3 "><p id="p41141114125611"><a name="p41141114125611"></a><a name="p41141114125611"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.68%" headers="mcps1.2.5.1.4 "><p id="p20114171445614"><a name="p20114171445614"></a><a name="p20114171445614"></a><strong id="b17991829111015"><a name="b17991829111015"></a><a name="b17991829111015"></a>COMMON</strong>: Common I/O. The SATA disk is used.</p>
<p id="p411471465616"><a name="p411471465616"></a><a name="p411471465616"></a><strong id="b2911428131120"><a name="b2911428131120"></a><a name="b2911428131120"></a>HIGH</strong>: High I/O. The SAS disk is used.</p>
<p id="p1311431405610"><a name="p1311431405610"></a><a name="p1311431405610"></a><strong id="b49772406111"><a name="b49772406111"></a><a name="b49772406111"></a>ULTRAHIGH</strong>: Ultra-high I/O. The solid-state drive (SSD) is used.</p>
</td>
</tr>
<tr id="row71141114145614"><td class="cellrowborder" valign="top" width="15.559999999999999%" headers="mcps1.2.5.1.1 "><p id="p1411401413563"><a name="p1411401413563"></a><a name="p1411401413563"></a>size</p>
</td>
<td class="cellrowborder" valign="top" width="14.44%" headers="mcps1.2.5.1.2 "><p id="p21147147566"><a name="p21147147566"></a><a name="p21147147566"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="12.32%" headers="mcps1.2.5.1.3 "><p id="p71149143562"><a name="p71149143562"></a><a name="p71149143562"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="57.68%" headers="mcps1.2.5.1.4 "><p id="p8114161418569"><a name="p8114161418569"></a><a name="p8114161418569"></a>Volume size, which must be a multiple of 4 and 10.</p>
</td>
</tr>
</tbody>
</table>

**Table  6** **nics**  field description

<a name="table1959831319562"></a>
<table><thead align="left"><tr id="row411461445618"><th class="cellrowborder" valign="top" width="15.049999999999999%" id="mcps1.2.5.1.1"><p id="p9114101414569"><a name="p9114101414569"></a><a name="p9114101414569"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15.45%" id="mcps1.2.5.1.2"><p id="p011461445616"><a name="p011461445616"></a><a name="p011461445616"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="12.120000000000001%" id="mcps1.2.5.1.3"><p id="p13114131415619"><a name="p13114131415619"></a><a name="p13114131415619"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="57.379999999999995%" id="mcps1.2.5.1.4"><p id="p911491435613"><a name="p911491435613"></a><a name="p911491435613"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row96965570369"><td class="cellrowborder" valign="top" width="15.049999999999999%" headers="mcps1.2.5.1.1 "><p id="p240011597368"><a name="p240011597368"></a><a name="p240011597368"></a>vpcId</p>
</td>
<td class="cellrowborder" valign="top" width="15.45%" headers="mcps1.2.5.1.2 "><p id="p54003593363"><a name="p54003593363"></a><a name="p54003593363"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="12.120000000000001%" headers="mcps1.2.5.1.3 "><p id="p3400165910366"><a name="p3400165910366"></a><a name="p3400165910366"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.379999999999995%" headers="mcps1.2.5.1.4 "><p id="p7415135911368"><a name="p7415135911368"></a><a name="p7415135911368"></a>VPC ID, which is used for configuring cluster network.</p>
</td>
</tr>
<tr id="row311410149566"><td class="cellrowborder" valign="top" width="15.049999999999999%" headers="mcps1.2.5.1.1 "><p id="p1114141419563"><a name="p1114141419563"></a><a name="p1114141419563"></a>netId</p>
</td>
<td class="cellrowborder" valign="top" width="15.45%" headers="mcps1.2.5.1.2 "><p id="p10114191411569"><a name="p10114191411569"></a><a name="p10114191411569"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="12.120000000000001%" headers="mcps1.2.5.1.3 "><p id="p16114214165616"><a name="p16114214165616"></a><a name="p16114214165616"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.379999999999995%" headers="mcps1.2.5.1.4 "><p id="p4114101445616"><a name="p4114101445616"></a><a name="p4114101445616"></a>Subnet ID. All instances in a cluster must have the same subnets and security groups.</p>
</td>
</tr>
<tr id="row1114614195611"><td class="cellrowborder" valign="top" width="15.049999999999999%" headers="mcps1.2.5.1.1 "><p id="p611471410563"><a name="p611471410563"></a><a name="p611471410563"></a>securityGroupId</p>
</td>
<td class="cellrowborder" valign="top" width="15.45%" headers="mcps1.2.5.1.2 "><p id="p611410141567"><a name="p611410141567"></a><a name="p611410141567"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="12.120000000000001%" headers="mcps1.2.5.1.3 "><p id="p7114181418567"><a name="p7114181418567"></a><a name="p7114181418567"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.379999999999995%" headers="mcps1.2.5.1.4 "><p id="p3114914195618"><a name="p3114914195618"></a><a name="p3114914195618"></a>Security group ID. All instances in a cluster must have the same subnets and security groups.</p>
</td>
</tr>
</tbody>
</table>

**Table  7** **datastore**  field description

<a name="table1121072510499"></a>
<table><thead align="left"><tr id="row9210132514499"><th class="cellrowborder" valign="top" width="14.85%" id="mcps1.2.5.1.1"><p id="p257003611426"><a name="p257003611426"></a><a name="p257003611426"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15.659999999999998%" id="mcps1.2.5.1.2"><p id="p1057073612420"><a name="p1057073612420"></a><a name="p1057073612420"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="12.32%" id="mcps1.2.5.1.3"><p id="p1457083654210"><a name="p1457083654210"></a><a name="p1457083654210"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="57.17%" id="mcps1.2.5.1.4"><p id="p1757018361424"><a name="p1757018361424"></a><a name="p1757018361424"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1121052512495"><td class="cellrowborder" valign="top" width="14.85%" headers="mcps1.2.5.1.1 "><p id="p6570143664211"><a name="p6570143664211"></a><a name="p6570143664211"></a>version</p>
</td>
<td class="cellrowborder" valign="top" width="15.659999999999998%" headers="mcps1.2.5.1.2 "><p id="p3570153613422"><a name="p3570153613422"></a><a name="p3570153613422"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="12.32%" headers="mcps1.2.5.1.3 "><p id="p18570636184216"><a name="p18570636184216"></a><a name="p18570636184216"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.17%" headers="mcps1.2.5.1.4 "><p id="p8570193615422"><a name="p8570193615422"></a><a name="p8570193615422"></a>Engine version. The default value is 6.2.3.</p>
</td>
</tr>
<tr id="row134267612250"><td class="cellrowborder" valign="top" width="14.85%" headers="mcps1.2.5.1.1 "><p id="p174261868256"><a name="p174261868256"></a><a name="p174261868256"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="15.659999999999998%" headers="mcps1.2.5.1.2 "><p id="p34272615255"><a name="p34272615255"></a><a name="p34272615255"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.32%" headers="mcps1.2.5.1.3 "><p id="p24274612517"><a name="p24274612517"></a><a name="p24274612517"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.17%" headers="mcps1.2.5.1.4 "><p id="p194276622512"><a name="p194276622512"></a><a name="p194276622512"></a>Engine type. The default value is <strong id="b53898421169"><a name="b53898421169"></a><a name="b53898421169"></a>elasticsearch</strong>. Currently, the value can only be <strong id="b9606194511169"><a name="b9606194511169"></a><a name="b9606194511169"></a>elasticsearch</strong>.</p>
</td>
</tr>
</tbody>
</table>

**Table  8** **diskEncryption**  field description

<a name="table18671184912468"></a>
<table><thead align="left"><tr id="row14688114919464"><th class="cellrowborder" valign="top" width="16.94%" id="mcps1.2.5.1.1"><p id="p76929493462"><a name="p76929493462"></a><a name="p76929493462"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13.640000000000002%" id="mcps1.2.5.1.2"><p id="p4695174911463"><a name="p4695174911463"></a><a name="p4695174911463"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="12.930000000000003%" id="mcps1.2.5.1.3"><p id="p47005496467"><a name="p47005496467"></a><a name="p47005496467"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="56.49000000000001%" id="mcps1.2.5.1.4"><p id="p167021949164619"><a name="p167021949164619"></a><a name="p167021949164619"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row87056492467"><td class="cellrowborder" valign="top" width="16.94%" headers="mcps1.2.5.1.1 "><p id="p8708114914466"><a name="p8708114914466"></a><a name="p8708114914466"></a>systemEncrypted</p>
</td>
<td class="cellrowborder" valign="top" width="13.640000000000002%" headers="mcps1.2.5.1.2 "><p id="p1871144924611"><a name="p1871144924611"></a><a name="p1871144924611"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="12.930000000000003%" headers="mcps1.2.5.1.3 "><p id="p971424919464"><a name="p971424919464"></a><a name="p971424919464"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.49000000000001%" headers="mcps1.2.5.1.4 "><p id="p1071724934610"><a name="p1071724934610"></a><a name="p1071724934610"></a>Value <strong id="b10809148152220"><a name="b10809148152220"></a><a name="b10809148152220"></a>1</strong> indicates encryption is performed, and value <strong id="b1041715111236"><a name="b1041715111236"></a><a name="b1041715111236"></a>0</strong> indicates encryption is not performed.</p>
</td>
</tr>
<tr id="row1872054954614"><td class="cellrowborder" valign="top" width="16.94%" headers="mcps1.2.5.1.1 "><p id="p372314911466"><a name="p372314911466"></a><a name="p372314911466"></a>systemCmkid</p>
</td>
<td class="cellrowborder" valign="top" width="13.640000000000002%" headers="mcps1.2.5.1.2 "><p id="p772615498467"><a name="p772615498467"></a><a name="p772615498467"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="12.930000000000003%" headers="mcps1.2.5.1.3 "><p id="p9727749184619"><a name="p9727749184619"></a><a name="p9727749184619"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.49000000000001%" headers="mcps1.2.5.1.4 "><p id="p155270534461"><a name="p155270534461"></a><a name="p155270534461"></a>Key ID.</p>
<a name="ul9357152215468"></a><a name="ul9357152215468"></a><ul id="ul9357152215468"><li>The Default Master Keys cannot be used to create grants. Specifically, you cannot use Default Master Keys whose aliases end with <span class="parmvalue" id="parmvalue2967115854615"><a name="parmvalue2967115854615"></a><a name="parmvalue2967115854615"></a><b>/default</b></span> in KMS to create clusters.</li><li>After a cluster is created, do not delete the key used by the cluster. Otherwise, the cluster will become unavailable.</li></ul>
</td>
</tr>
</tbody>
</table>

## Response<a name="section1261411310560"></a>

[Table 9](#table1088918316183)  describes the response parameters.

**Table  9**  Parameter description

<a name="table1088918316183"></a>
<table><thead align="left"><tr id="row3889130189"><th class="cellrowborder" valign="top" width="24.5024502450245%" id="mcps1.2.4.1.1"><p id="p1214201516183"><a name="p1214201516183"></a><a name="p1214201516183"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="27.872787278727873%" id="mcps1.2.4.1.2"><p id="p148892310183"><a name="p148892310183"></a><a name="p148892310183"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="47.624762476247625%" id="mcps1.2.4.1.3"><p id="p988917381817"><a name="p988917381817"></a><a name="p988917381817"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1889183201813"><td class="cellrowborder" valign="top" width="24.5024502450245%" headers="mcps1.2.4.1.1 "><p id="p8889931181"><a name="p8889931181"></a><a name="p8889931181"></a>cluster</p>
</td>
<td class="cellrowborder" valign="top" width="27.872787278727873%" headers="mcps1.2.4.1.2 "><p id="p1388913181817"><a name="p1388913181817"></a><a name="p1388913181817"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="47.624762476247625%" headers="mcps1.2.4.1.3 "><p id="p3889123181818"><a name="p3889123181818"></a><a name="p3889123181818"></a>Cluster object. For details, see <a href="#table2614813135615">Table 10</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  10** **cluster**  field description

<a name="table2614813135615"></a>
<table><thead align="left"><tr id="row1611419143569"><th class="cellrowborder" valign="top" width="24.412441244124413%" id="mcps1.2.4.1.1"><p id="p10114141412569"><a name="p10114141412569"></a><a name="p10114141412569"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="28.782878287828783%" id="mcps1.2.4.1.2"><p id="p111141014195619"><a name="p111141014195619"></a><a name="p111141014195619"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="46.804680468046804%" id="mcps1.2.4.1.3"><p id="p3114151415563"><a name="p3114151415563"></a><a name="p3114151415563"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1511418148568"><td class="cellrowborder" valign="top" width="24.412441244124413%" headers="mcps1.2.4.1.1 "><p id="p1111451415613"><a name="p1111451415613"></a><a name="p1111451415613"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="28.782878287828783%" headers="mcps1.2.4.1.2 "><p id="p3114314145616"><a name="p3114314145616"></a><a name="p3114314145616"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.804680468046804%" headers="mcps1.2.4.1.3 "><p id="p4114171419566"><a name="p4114171419566"></a><a name="p4114171419566"></a>Cluster ID</p>
</td>
</tr>
<tr id="row2114181411562"><td class="cellrowborder" valign="top" width="24.412441244124413%" headers="mcps1.2.4.1.1 "><p id="p511411418561"><a name="p511411418561"></a><a name="p511411418561"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="28.782878287828783%" headers="mcps1.2.4.1.2 "><p id="p1211411416562"><a name="p1211411416562"></a><a name="p1211411416562"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.804680468046804%" headers="mcps1.2.4.1.3 "><p id="p81141114125615"><a name="p81141114125615"></a><a name="p81141114125615"></a>Cluster name</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="section153121221152"></a>

Example request

```
POST /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters
{ 
    "cluster": { 
        "name": "ES-Test",
        "instanceNum": 4,
           "instance": { 
               "flavorRef": "css.large.8", 
                  "volume": { 
                         "volume_type": "COMMON", 
                         "size": 100
                  }, 
                  "nics": { 
                         "vpcId": "fccd753c-91c3-40e2-852f-5ddf76d1a1b2",
                         "netId": "af1c65ae-c494-4e24-acd8-81d6b355c9f1", 
                         "securityGroupId": "7e3fed21-1a44-4101-ab29-34e57124f614" 
                  }
           },
           "httpsEnable": "false",
           "diskEncryption" : {
		"systemEncrypted" : "1",
		"systemCmkid" : "42546bb1-8025-4ad1-868f-600729c341ae"
	    }
    } 
}
```

Example response

```
{
  "cluster": {
    "id": "ef683016-871e-48bc-bf93-74a29d60d214",
    "name": "ES-Test"
  }
}
```

## Status Code<a name="section87962546391"></a>

[Table 11](#table209491933101317)  describes the status code.

**Table  11**  Status code

<a name="table209491933101317"></a>
<table><thead align="left"><tr id="row194918333132"><th class="cellrowborder" valign="top" width="26.162616261626166%" id="mcps1.2.4.1.1"><p id="p6531343171310"><a name="p6531343171310"></a><a name="p6531343171310"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="28.522852285228524%" id="mcps1.2.4.1.2"><p id="p16534124318132"><a name="p16534124318132"></a><a name="p16534124318132"></a>Code</p>
</th>
<th class="cellrowborder" valign="top" width="45.314531453145314%" id="mcps1.2.4.1.3"><p id="p1453710437131"><a name="p1453710437131"></a><a name="p1453710437131"></a>Status Code Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row11949333171318"><td class="cellrowborder" valign="top" width="26.162616261626166%" headers="mcps1.2.4.1.1 "><p id="p1354264331315"><a name="p1354264331315"></a><a name="p1354264331315"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="28.522852285228524%" headers="mcps1.2.4.1.2 "><p id="p175442043151310"><a name="p175442043151310"></a><a name="p175442043151310"></a>BadRequest</p>
</td>
<td class="cellrowborder" valign="top" width="45.314531453145314%" headers="mcps1.2.4.1.3 "><p id="p10547843141317"><a name="p10547843141317"></a><a name="p10547843141317"></a>Invalid request.</p>
<p id="p1954810435138"><a name="p1954810435138"></a><a name="p1954810435138"></a>The client should not repeat the request without modifications.</p>
</td>
</tr>
<tr id="row15949153314139"><td class="cellrowborder" valign="top" width="26.162616261626166%" headers="mcps1.2.4.1.1 "><p id="p17551134391315"><a name="p17551134391315"></a><a name="p17551134391315"></a>409</p>
</td>
<td class="cellrowborder" valign="top" width="28.522852285228524%" headers="mcps1.2.4.1.2 "><p id="p75541043121319"><a name="p75541043121319"></a><a name="p75541043121319"></a>Conflict</p>
</td>
<td class="cellrowborder" valign="top" width="45.314531453145314%" headers="mcps1.2.4.1.3 "><p id="p3555843131312"><a name="p3555843131312"></a><a name="p3555843131312"></a>The request could not be processed due to a conflict.</p>
<p id="p75561143171311"><a name="p75561143171311"></a><a name="p75561143171311"></a>This status code indicates that the resource that the client attempts to create already exits, or the request fails to be processed because of the update of the conflict request.</p>
</td>
</tr>
<tr id="row129491333137"><td class="cellrowborder" valign="top" width="26.162616261626166%" headers="mcps1.2.4.1.1 "><p id="p13559943141313"><a name="p13559943141313"></a><a name="p13559943141313"></a>412</p>
</td>
<td class="cellrowborder" valign="top" width="28.522852285228524%" headers="mcps1.2.4.1.2 "><p id="p9562743101314"><a name="p9562743101314"></a><a name="p9562743101314"></a>Precondition Failed</p>
</td>
<td class="cellrowborder" valign="top" width="45.314531453145314%" headers="mcps1.2.4.1.3 "><p id="p16565204314137"><a name="p16565204314137"></a><a name="p16565204314137"></a>The server does not meet one of the preconditions that the requester puts on the request.</p>
</td>
</tr>
<tr id="row09491533111315"><td class="cellrowborder" valign="top" width="26.162616261626166%" headers="mcps1.2.4.1.1 "><p id="p1656994351310"><a name="p1656994351310"></a><a name="p1656994351310"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="28.522852285228524%" headers="mcps1.2.4.1.2 "><p id="p4573443111317"><a name="p4573443111317"></a><a name="p4573443111317"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="45.314531453145314%" headers="mcps1.2.4.1.3 "><p id="p1057744317139"><a name="p1057744317139"></a><a name="p1057744317139"></a>The request is processed successfully.</p>
</td>
</tr>
</tbody>
</table>

