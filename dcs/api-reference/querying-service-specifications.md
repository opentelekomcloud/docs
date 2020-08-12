# Querying Service Specifications<a name="dcs-api-0312040"></a>

## Function<a name="section164151825713"></a>

This API is used to query the product ID \(parameter  **product\_id**\) which indicates the specifications of the DCS service you created. 

## URI<a name="section16452102542018"></a>

GET /v1.0/products

## Request<a name="section6514194713209"></a>

**Request parameters**

None.

**Example request**

None.

## Response<a name="section11526162120234"></a>

**Response parameters**

[Table 1](#table18437193323916)  describes the response parameters.

**Table  1**  Parameter description

<a name="table18437193323916"></a>
<table><thead align="left"><tr id="row184378330394"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p943663310393"><a name="p943663310393"></a><a name="p943663310393"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p543683363919"><a name="p543683363919"></a><a name="p543683363919"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p184371733193920"><a name="p184371733193920"></a><a name="p184371733193920"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row14378335398"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1643712333399"><a name="p1643712333399"></a><a name="p1643712333399"></a>products</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p4437193343911"><a name="p4437193343911"></a><a name="p4437193343911"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1843773353916"><a name="p1843773353916"></a><a name="p1843773353916"></a>List of specifications of the DCS service to which you can subscribe.</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  products parameter description

<a name="table18238145151512"></a>
<table><thead align="left"><tr id="row8238951171516"><th class="cellrowborder" valign="top" width="23.330000000000002%" id="mcps1.2.4.1.1"><p id="p723895120156"><a name="p723895120156"></a><a name="p723895120156"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.669999999999998%" id="mcps1.2.4.1.2"><p id="p1238951131512"><a name="p1238951131512"></a><a name="p1238951131512"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="60%" id="mcps1.2.4.1.3"><p id="p22385511154"><a name="p22385511154"></a><a name="p22385511154"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row389654918549"><td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.1 "><p id="p62384514152"><a name="p62384514152"></a><a name="p62384514152"></a>product_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.2.4.1.2 "><p id="p7238105116152"><a name="p7238105116152"></a><a name="p7238105116152"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p2238151191518"><a name="p2238151191518"></a><a name="p2238151191518"></a>Product ID used to differentiate DCS specifications.</p>
</td>
</tr>
<tr id="row20491126105513"><td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.1 "><p id="p323975119159"><a name="p323975119159"></a><a name="p323975119159"></a>spec_code</p>
</td>
<td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.2.4.1.2 "><p id="p132391951151516"><a name="p132391951151516"></a><a name="p132391951151516"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p546716557277"><a name="p546716557277"></a><a name="p546716557277"></a>DCS instance specification code.</p>
<a name="ul181289335104"></a><a name="ul181289335104"></a><ul id="ul181289335104"><li><strong id="b6471192914419"><a name="b6471192914419"></a><a name="b6471192914419"></a>dcs.single_node</strong></li><li><strong id="b17521051861"><a name="b17521051861"></a><a name="b17521051861"></a>dcs.master_standby</strong></li><li><strong id="b3404123613412"><a name="b3404123613412"></a><a name="b3404123613412"></a>dcs.cluster</strong></li></ul>
</td>
</tr>
<tr id="row163113595519"><td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.1 "><p id="p198111983417"><a name="p198111983417"></a><a name="p198111983417"></a>cache_mode</p>
</td>
<td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.2.4.1.2 "><p id="p7981161915341"><a name="p7981161915341"></a><a name="p7981161915341"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p9981161933414"><a name="p9981161933414"></a><a name="p9981161933414"></a>DCS instance type. Options:</p>
<a name="ul710514217427"></a><a name="ul710514217427"></a><ul id="ul710514217427"><li><strong id="b380093713710"><a name="b380093713710"></a><a name="b380093713710"></a>single</strong>: single-node</li><li><strong id="b33395398720"><a name="b33395398720"></a><a name="b33395398720"></a>ha</strong>: master/standby</li><li><strong id="b71446401576"><a name="b71446401576"></a><a name="b71446401576"></a>cluster</strong>: Redis Cluster</li></ul>
</td>
</tr>
<tr id="row1099540155611"><td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.1 "><p id="p1598151983414"><a name="p1598151983414"></a><a name="p1598151983414"></a>product_type</p>
</td>
<td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.2.4.1.2 "><p id="p119811190343"><a name="p119811190343"></a><a name="p119811190343"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p1898112198347"><a name="p1898112198347"></a><a name="p1898112198347"></a>Edition of DCS for Redis.</p>
</td>
</tr>
<tr id="row1458210115619"><td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.1 "><p id="p19981181973410"><a name="p19981181973410"></a><a name="p19981181973410"></a>cpu_type</p>
</td>
<td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.2.4.1.2 "><p id="p49811719103414"><a name="p49811719103414"></a><a name="p49811719103414"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p109817194340"><a name="p109817194340"></a><a name="p109817194340"></a>CPU architecture.</p>
</td>
</tr>
<tr id="row747092905615"><td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.1 "><p id="p924775611344"><a name="p924775611344"></a><a name="p924775611344"></a>storage_type</p>
</td>
<td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.2.4.1.2 "><p id="p10247256193411"><a name="p10247256193411"></a><a name="p10247256193411"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p1024735612348"><a name="p1024735612348"></a><a name="p1024735612348"></a>Storage type.</p>
</td>
</tr>
<tr id="row3719113919263"><td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.1 "><p id="p147201739172613"><a name="p147201739172613"></a><a name="p147201739172613"></a>details</p>
</td>
<td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.2.4.1.2 "><p id="p1720113918263"><a name="p1720113918263"></a><a name="p1720113918263"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p272023912260"><a name="p272023912260"></a><a name="p272023912260"></a>Details of the specifications. <a href="#table830249172716">Table 3</a> describes the parameters in this array.</p>
</td>
</tr>
<tr id="row16887753113017"><td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.1 "><p id="p588718535303"><a name="p588718535303"></a><a name="p588718535303"></a>engine</p>
</td>
<td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.2.4.1.2 "><p id="p2887135363012"><a name="p2887135363012"></a><a name="p2887135363012"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p208889533306"><a name="p208889533306"></a><a name="p208889533306"></a>Cache engine.</p>
</td>
</tr>
<tr id="row859165010568"><td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.1 "><p id="p1524714568340"><a name="p1524714568340"></a><a name="p1524714568340"></a>engine_versions</p>
</td>
<td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.2.4.1.2 "><p id="p1524720567349"><a name="p1524720567349"></a><a name="p1524720567349"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p3247155613420"><a name="p3247155613420"></a><a name="p3247155613420"></a>Cache engine version.</p>
</td>
</tr>
<tr id="row35312151710"><td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.1 "><p id="p17239195171517"><a name="p17239195171517"></a><a name="p17239195171517"></a>spec_details</p>
</td>
<td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.2.4.1.2 "><p id="p1923915117155"><a name="p1923915117155"></a><a name="p1923915117155"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p217316221173"><a name="p217316221173"></a><a name="p217316221173"></a>DCS specifications. The value subjects to the returned specifications.</p>
</td>
</tr>
<tr id="row1825012201673"><td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.1 "><p id="p945220933816"><a name="p945220933816"></a><a name="p945220933816"></a>spec_details2</p>
</td>
<td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.2.4.1.2 "><p id="p94527923814"><a name="p94527923814"></a><a name="p94527923814"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p174523923819"><a name="p174523923819"></a><a name="p174523923819"></a>Detailed DCS specifications, including the maximum number of connections and maximum memory size.</p>
</td>
</tr>
<tr id="row272131212317"><td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.1 "><p id="p323975111510"><a name="p323975111510"></a><a name="p323975111510"></a>charging_type</p>
</td>
<td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.2.4.1.2 "><p id="p523995151511"><a name="p523995151511"></a><a name="p523995151511"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p7327171013210"><a name="p7327171013210"></a><a name="p7327171013210"></a>Billing mode. Value: <strong id="b12306352165"><a name="b12306352165"></a><a name="b12306352165"></a>Hourly</strong>.</p>
</td>
</tr>
<tr id="row1223815161515"><td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.1 "><p id="p0181153116713"><a name="p0181153116713"></a><a name="p0181153116713"></a>price</p>
</td>
<td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.2.4.1.2 "><p id="p81811311975"><a name="p81811311975"></a><a name="p81811311975"></a>doubule</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p018110312712"><a name="p018110312712"></a><a name="p018110312712"></a>Price of the DCS service to which you can subscribe. (This parameter has been abandoned.)</p>
</td>
</tr>
<tr id="row122398512158"><td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.1 "><p id="p71813311718"><a name="p71813311718"></a><a name="p71813311718"></a>currency</p>
</td>
<td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.2.4.1.2 "><p id="p818213314719"><a name="p818213314719"></a><a name="p818213314719"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p12182331877"><a name="p12182331877"></a><a name="p12182331877"></a>Currency.</p>
</td>
</tr>
<tr id="row49808195344"><td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.1 "><p id="p1858424318014"><a name="p1858424318014"></a><a name="p1858424318014"></a>prod_type</p>
</td>
<td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.2.4.1.2 "><p id="p12584144316012"><a name="p12584144316012"></a><a name="p12584144316012"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p1234224715319"><a name="p1234224715319"></a><a name="p1234224715319"></a>Product type.</p>
<p id="p723634511240"><a name="p723634511240"></a><a name="p723634511240"></a>Options: <strong id="b19994144711310"><a name="b19994144711310"></a><a name="b19994144711310"></a>instance</strong> and <strong id="b64912501311"><a name="b64912501311"></a><a name="b64912501311"></a>obs_space</strong>.</p>
</td>
</tr>
<tr id="row4981519103410"><td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.1 "><p id="p328196163612"><a name="p328196163612"></a><a name="p328196163612"></a>cloud_service_type_code</p>
</td>
<td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.2.4.1.2 "><p id="p82801867362"><a name="p82801867362"></a><a name="p82801867362"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p12278864360"><a name="p12278864360"></a><a name="p12278864360"></a>Cloud service type code.</p>
</td>
</tr>
<tr id="row16981719143412"><td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.1 "><p id="p1323514115365"><a name="p1323514115365"></a><a name="p1323514115365"></a>cloud_resource_type_code</p>
</td>
<td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.2.4.1.2 "><p id="p152351411163611"><a name="p152351411163611"></a><a name="p152351411163611"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p1023511133614"><a name="p1023511133614"></a><a name="p1023511133614"></a>Cloud resource type code.</p>
</td>
</tr>
<tr id="row142461756103416"><td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.1 "><p id="p1473512163111"><a name="p1473512163111"></a><a name="p1473512163111"></a>flavors</p>
</td>
<td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.2.4.1.2 "><p id="p173112153111"><a name="p173112153111"></a><a name="p173112153111"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p127301213118"><a name="p127301213118"></a><a name="p127301213118"></a>AZs with available resources. <a href="#table1979512328317">Table 4</a> describes the parameters in this array.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  details parameter description

<a name="table830249172716"></a>
<table><thead align="left"><tr id="row193113491271"><th class="cellrowborder" valign="top" width="23.392339233923394%" id="mcps1.2.4.1.1"><p id="p552710118284"><a name="p552710118284"></a><a name="p552710118284"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.65166516651665%" id="mcps1.2.4.1.2"><p id="p1852741102813"><a name="p1852741102813"></a><a name="p1852741102813"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="59.95599559955996%" id="mcps1.2.4.1.3"><p id="p452719113284"><a name="p452719113284"></a><a name="p452719113284"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row832949192715"><td class="cellrowborder" valign="top" width="23.392339233923394%" headers="mcps1.2.4.1.1 "><p id="p183284919278"><a name="p183284919278"></a><a name="p183284919278"></a>capacity</p>
</td>
<td class="cellrowborder" valign="top" width="16.65166516651665%" headers="mcps1.2.4.1.2 "><p id="p1132204913271"><a name="p1132204913271"></a><a name="p1132204913271"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.95599559955996%" headers="mcps1.2.4.1.3 "><p id="p183217499276"><a name="p183217499276"></a><a name="p183217499276"></a>Specification (total memory) of the DCS instance.</p>
</td>
</tr>
<tr id="row632749192720"><td class="cellrowborder" valign="top" width="23.392339233923394%" headers="mcps1.2.4.1.1 "><p id="p2321049152718"><a name="p2321049152718"></a><a name="p2321049152718"></a>max_bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="16.65166516651665%" headers="mcps1.2.4.1.2 "><p id="p183224913273"><a name="p183224913273"></a><a name="p183224913273"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.95599559955996%" headers="mcps1.2.4.1.3 "><p id="p1632184918277"><a name="p1632184918277"></a><a name="p1632184918277"></a>Maximum bandwidth supported by the specification.</p>
</td>
</tr>
<tr id="row232114922711"><td class="cellrowborder" valign="top" width="23.392339233923394%" headers="mcps1.2.4.1.1 "><p id="p7321249162716"><a name="p7321249162716"></a><a name="p7321249162716"></a>max_clients</p>
</td>
<td class="cellrowborder" valign="top" width="16.65166516651665%" headers="mcps1.2.4.1.2 "><p id="p232114912273"><a name="p232114912273"></a><a name="p232114912273"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.95599559955996%" headers="mcps1.2.4.1.3 "><p id="p1932149142714"><a name="p1932149142714"></a><a name="p1932149142714"></a>Maximum number of clients supported by the specification, which is usually equal to the maximum number of connections.</p>
</td>
</tr>
<tr id="row1032194912278"><td class="cellrowborder" valign="top" width="23.392339233923394%" headers="mcps1.2.4.1.1 "><p id="p8321749172712"><a name="p8321749172712"></a><a name="p8321749172712"></a>max_connections</p>
</td>
<td class="cellrowborder" valign="top" width="16.65166516651665%" headers="mcps1.2.4.1.2 "><p id="p17321549112710"><a name="p17321549112710"></a><a name="p17321549112710"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.95599559955996%" headers="mcps1.2.4.1.3 "><p id="p532749152716"><a name="p532749152716"></a><a name="p532749152716"></a>Maximum number of connections supported by the specification.</p>
</td>
</tr>
<tr id="row2032114918277"><td class="cellrowborder" valign="top" width="23.392339233923394%" headers="mcps1.2.4.1.1 "><p id="p13327493271"><a name="p13327493271"></a><a name="p13327493271"></a>max_in_bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="16.65166516651665%" headers="mcps1.2.4.1.2 "><p id="p1232749152717"><a name="p1232749152717"></a><a name="p1232749152717"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.95599559955996%" headers="mcps1.2.4.1.3 "><p id="p7331349112717"><a name="p7331349112717"></a><a name="p7331349112717"></a>Maximum inbound bandwidth supported by the specification, which is usually equal to the maximum bandwidth.</p>
</td>
</tr>
<tr id="row1933194912719"><td class="cellrowborder" valign="top" width="23.392339233923394%" headers="mcps1.2.4.1.1 "><p id="p133318498272"><a name="p133318498272"></a><a name="p133318498272"></a>max_memory</p>
</td>
<td class="cellrowborder" valign="top" width="16.65166516651665%" headers="mcps1.2.4.1.2 "><p id="p8336491274"><a name="p8336491274"></a><a name="p8336491274"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.95599559955996%" headers="mcps1.2.4.1.3 "><p id="p1433124972718"><a name="p1433124972718"></a><a name="p1433124972718"></a>Maximum available memory.</p>
</td>
</tr>
<tr id="row3391144205314"><td class="cellrowborder" valign="top" width="23.392339233923394%" headers="mcps1.2.4.1.1 "><p id="p173921443533"><a name="p173921443533"></a><a name="p173921443533"></a>tenant_ip_count</p>
</td>
<td class="cellrowborder" valign="top" width="16.65166516651665%" headers="mcps1.2.4.1.2 "><p id="p9392124425311"><a name="p9392124425311"></a><a name="p9392124425311"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.95599559955996%" headers="mcps1.2.4.1.3 "><p id="p17392104485318"><a name="p17392104485318"></a><a name="p17392104485318"></a>Number of tenant IP addresses corresponding to the specifications.</p>
</td>
</tr>
<tr id="row103921244175315"><td class="cellrowborder" valign="top" width="23.392339233923394%" headers="mcps1.2.4.1.1 "><p id="p1039214475315"><a name="p1039214475315"></a><a name="p1039214475315"></a>sharding_num</p>
</td>
<td class="cellrowborder" valign="top" width="16.65166516651665%" headers="mcps1.2.4.1.2 "><p id="p83931344145320"><a name="p83931344145320"></a><a name="p83931344145320"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.95599559955996%" headers="mcps1.2.4.1.3 "><p id="p639324410537"><a name="p639324410537"></a><a name="p639324410537"></a>Number of shards supported by the specifications.</p>
</td>
</tr>
<tr id="row1139314495311"><td class="cellrowborder" valign="top" width="23.392339233923394%" headers="mcps1.2.4.1.1 "><p id="p17393144485319"><a name="p17393144485319"></a><a name="p17393144485319"></a>proxy_num</p>
</td>
<td class="cellrowborder" valign="top" width="16.65166516651665%" headers="mcps1.2.4.1.2 "><p id="p1739312440539"><a name="p1739312440539"></a><a name="p1739312440539"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.95599559955996%" headers="mcps1.2.4.1.3 "><p id="p239394417532"><a name="p239394417532"></a><a name="p239394417532"></a>Number of proxies supported by Proxy Cluster instances of the specified specifications. If the instance is not a Proxy Cluster instance, the value of this parameter is <strong id="b685903718444"><a name="b685903718444"></a><a name="b685903718444"></a>0</strong>.</p>
</td>
</tr>
<tr id="row137791713125416"><td class="cellrowborder" valign="top" width="23.392339233923394%" headers="mcps1.2.4.1.1 "><p id="p777981315541"><a name="p777981315541"></a><a name="p777981315541"></a>db_number</p>
</td>
<td class="cellrowborder" valign="top" width="16.65166516651665%" headers="mcps1.2.4.1.2 "><p id="p077991375415"><a name="p077991375415"></a><a name="p077991375415"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.95599559955996%" headers="mcps1.2.4.1.3 "><p id="p577931317541"><a name="p577931317541"></a><a name="p577931317541"></a>Number of DBs of the specifications.</p>
</td>
</tr>
</tbody>
</table>

**Table  4**  flavors parameter description

<a name="table1979512328317"></a>
<table><thead align="left"><tr id="row1879611326319"><th class="cellrowborder" valign="top" width="23.292329232923294%" id="mcps1.2.4.1.1"><p id="p1179619321315"><a name="p1179619321315"></a><a name="p1179619321315"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.761676167616763%" id="mcps1.2.4.1.2"><p id="p7796143273112"><a name="p7796143273112"></a><a name="p7796143273112"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="59.94599459945995%" id="mcps1.2.4.1.3"><p id="p17966325311"><a name="p17966325311"></a><a name="p17966325311"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row279616329313"><td class="cellrowborder" valign="top" width="23.292329232923294%" headers="mcps1.2.4.1.1 "><p id="p11796432123117"><a name="p11796432123117"></a><a name="p11796432123117"></a>capacity</p>
</td>
<td class="cellrowborder" valign="top" width="16.761676167616763%" headers="mcps1.2.4.1.2 "><p id="p1779643210313"><a name="p1779643210313"></a><a name="p1779643210313"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.94599459945995%" headers="mcps1.2.4.1.3 "><p id="p499239145"><a name="p499239145"></a><a name="p499239145"></a>Specification (total memory) of the DCS instance.</p>
</td>
</tr>
<tr id="row8796173215312"><td class="cellrowborder" valign="top" width="23.292329232923294%" headers="mcps1.2.4.1.1 "><p id="p1079610325315"><a name="p1079610325315"></a><a name="p1079610325315"></a>unit</p>
</td>
<td class="cellrowborder" valign="top" width="16.761676167616763%" headers="mcps1.2.4.1.2 "><p id="p779603243111"><a name="p779603243111"></a><a name="p779603243111"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.94599459945995%" headers="mcps1.2.4.1.3 "><p id="p479619326314"><a name="p479619326314"></a><a name="p479619326314"></a>Memory unit.</p>
</td>
</tr>
<tr id="row167967329318"><td class="cellrowborder" valign="top" width="23.292329232923294%" headers="mcps1.2.4.1.1 "><p id="p1679618326317"><a name="p1679618326317"></a><a name="p1679618326317"></a>available_zones</p>
</td>
<td class="cellrowborder" valign="top" width="16.761676167616763%" headers="mcps1.2.4.1.2 "><p id="p1679753215316"><a name="p1679753215316"></a><a name="p1679753215316"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="59.94599459945995%" headers="mcps1.2.4.1.3 "><p id="p1579733233116"><a name="p1579733233116"></a><a name="p1579733233116"></a>AZ ID.</p>
</td>
</tr>
</tbody>
</table>

**Example response**

```
{
    "products": [
       {
            "details": {
                "capacity": 64,
                "max_memory": 64,
                "max_connections": 20000,
                "max_clients": 80000,
                "max_bandwidth": 2000,
                "max_in_bandwidth": 600,
                "proc_num": 8
            },
            "engine": "redis",
            "price": 0.04,
            "currency": "1",
            "flavors": [
                {
                    "capacity": "64",
                    "unit": "GB",
                    "available_zones": [
                        "ae04cf9d61544df3806a3feeb401b204",
                        "882f6e449e3245dbb8c1c0fafa494c89"
                    ]
                },
                {
                    "capacity": "128",
                    "unit": "GB",
                    "available_zones": [
                        "ae04cf9d61544df3806a3feeb401b204",
                        "882f6e449e3245dbb8c1c0fafa494c89"
                    ]
                },
                {
                    "capacity": "256",
                    "unit": "GB",
                    "available_zones": [
                        "ae04cf9d61544df3806a3feeb401b204",
                        "882f6e449e3245dbb8c1c0fafa494c89"
                    ]
                }
            ],
            "product_id": "00301-30112-0--0",
            "spec_code": "dcs.cluster",
            "cache_mode": "cluster",
            "product_type": "generic",
            "cpu_type": "x86_64",
            "storage_type": "DRAM",
            "engine_versions": "3.0",
            "spec_details": "[{\"mem\":\"64,128,256\"}]",
            "spec_details2": "[{\"capacity\": 64,\"max_memory\": 64,\"max_connections\": 20000,\"max_clients\":80000,\"max_bandwidth\": 2000,\"max_in_bandwidth\": 600,\"proc_num\":8},{\"capacity\": 128,\"max_memory\": 128,\"max_connections\": 20000,\"max_clients\":160000,\"max_bandwidth\": 2000,\"max_in_bandwidth\": 600,\"proc_num\":16},{\"capacity\": 256,\"max_memory\": 256,\"max_connections\": 20000,\"max_clients\":160000,\"max_bandwidth\": 2000,\"max_in_bandwidth\": 600,\"proc_num\":32},{\"capacity\": 512,\"max_memory\": 512,\"max_connections\": 20000,\"max_clients\":160000,\"max_bandwidth\": 2000,\"max_in_bandwidth\": 600,\"proc_num\":64},{\"capacity\": 1024,\"max_memory\": 1024,\"max_connections\": 20000,\"max_clients\":160000,\"max_bandwidth\": 2000,\"max_in_bandwidth\": 600,\"proc_num\":128}]",
            "charging_type": "Hourly",
            "prod_type": "instance",
            "cloud_service_type_code": "XXXX",
            "cloud_resource_type_code": "XXXX"
        },
}
```

## Status Code<a name="section108740485137"></a>

[Table 5](#table11875348101316)  describes the status code of successful operations. For details about other status codes, see  [Table 1](status-codes.md#table5210141351517).

**Table  5**  Status code

<a name="table11875348101316"></a>
<table><thead align="left"><tr id="row187524831319"><th class="cellrowborder" valign="top" width="15.98%" id="mcps1.2.3.1.1"><p id="p138751048141314"><a name="p138751048141314"></a><a name="p138751048141314"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="84.02%" id="mcps1.2.3.1.2"><p id="p087514488136"><a name="p087514488136"></a><a name="p087514488136"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row48751148101320"><td class="cellrowborder" valign="top" width="15.98%" headers="mcps1.2.3.1.1 "><p id="p48755482133"><a name="p48755482133"></a><a name="p48755482133"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="84.02%" headers="mcps1.2.3.1.2 "><p id="p5875194821319"><a name="p5875194821319"></a><a name="p5875194821319"></a>Service specifications queried successfully.</p>
</td>
</tr>
</tbody>
</table>

