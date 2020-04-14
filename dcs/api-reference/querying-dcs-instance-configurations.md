# Querying DCS Instance Configurations<a name="EN-US_TOPIC_0237964362"></a>

## Function<a name="section29587109"></a>

This API is used to query the configuration parameters of a DCS instance.

## URI<a name="section64957389"></a>

-   URI format:

    GET /v1.0/\{project\_id\}/instances/\{instance\_id\}/configs

-   Parameter description:

    [Table 3-4](#table42828888)  describes the parameters of this API.


**Table  1**  Parameter description

<a name="table42828888"></a>
<table><thead align="left"><tr id="row44871090"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p10679711"><a name="p10679711"></a><a name="p10679711"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p59750252"><a name="p59750252"></a><a name="p59750252"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p7932225"><a name="p7932225"></a><a name="p7932225"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p38530503"><a name="p38530503"></a><a name="p38530503"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row33963045"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p66652164"><a name="p66652164"></a><a name="p66652164"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p30116236"><a name="p30116236"></a><a name="p30116236"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p23496036"><a name="p23496036"></a><a name="p23496036"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p24130740"><a name="p24130740"></a><a name="p24130740"></a>Project ID.</p>
</td>
</tr>
<tr id="row15850073"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p8787537"><a name="p8787537"></a><a name="p8787537"></a>instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p40701910"><a name="p40701910"></a><a name="p40701910"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p8520399"><a name="p8520399"></a><a name="p8520399"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p19063717"><a name="p19063717"></a><a name="p19063717"></a>DCS instance ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section47745595"></a>

None.

## Response<a name="section27057175"></a>

-   Status code:

    If status code "200 OK" is returned, this request is fulfilled. For description of other status codes, see  [API Usage Guidelines](api-usage-guidelines.md).

-   Response parameter:

    [Table 3-5](#table7950717)  describes response parameters.


**Table  2**  Parameter description

<a name="table7950717"></a>
<table><thead align="left"><tr id="row28998002"><th class="cellrowborder" valign="top" width="26%" id="mcps1.2.4.1.1"><p id="p27965"><a name="p27965"></a><a name="p27965"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="26%" id="mcps1.2.4.1.2"><p id="p2265180"><a name="p2265180"></a><a name="p2265180"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="48%" id="mcps1.2.4.1.3"><p id="p49261880"><a name="p49261880"></a><a name="p49261880"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row30789304"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.1 "><p id="p10905668"><a name="p10905668"></a><a name="p10905668"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="p10943941"><a name="p10943941"></a><a name="p10943941"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.4.1.3 "><p id="p14044067"><a name="p14044067"></a><a name="p14044067"></a>Current status of a DCS instance.</p>
</td>
</tr>
<tr id="row59287744"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.1 "><p id="p37577972"><a name="p37577972"></a><a name="p37577972"></a>instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="p23916855"><a name="p23916855"></a><a name="p23916855"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.4.1.3 "><p id="p58217140"><a name="p58217140"></a><a name="p58217140"></a>DCS instance ID.</p>
</td>
</tr>
<tr id="row54192215"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.1 "><p id="p27493275"><a name="p27493275"></a><a name="p27493275"></a>redis_config</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="p12362796"><a name="p12362796"></a><a name="p12362796"></a>Array.</p>
<p id="p44156300"><a name="p44156300"></a><a name="p44156300"></a>For details, see <a href="#table53580277">Table 3</a>.</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.4.1.3 "><p id="p44797266"><a name="p44797266"></a><a name="p44797266"></a>Array of configurations items of the DCS instance.</p>
</td>
</tr>
<tr id="row522217"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.1 "><p id="p42299649"><a name="p42299649"></a><a name="p42299649"></a>config_status</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="p3719529"><a name="p3719529"></a><a name="p3719529"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.4.1.3 "><p id="p32846409"><a name="p32846409"></a><a name="p32846409"></a>DCS instance status that is being modified or has been modified.</p>
<p id="p27182230"><a name="p27182230"></a><a name="p27182230"></a>Options:</p>
<a name="ul43313482"></a><a name="ul43313482"></a><ul id="ul43313482"><li>UPDATING</li><li>FAILURE</li><li>SUCCESS</li></ul>
</td>
</tr>
<tr id="row40828621"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.1 "><p id="p18784032"><a name="p18784032"></a><a name="p18784032"></a>config_time</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="p45111603"><a name="p45111603"></a><a name="p45111603"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.4.1.3 "><p id="p30161198"><a name="p30161198"></a><a name="p30161198"></a>Time at which the DCS instance is manipulated.</p>
<p id="p3015330"><a name="p3015330"></a><a name="p3015330"></a>For example, 2017-03-31<strong id="b27137978"><a name="b27137978"></a><a name="b27137978"></a>T</strong>12:24:46.297<strong id="b42915214"><a name="b42915214"></a><a name="b42915214"></a>Z</strong>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Parameter description of the redis\_config array

<a name="table53580277"></a>
<table><thead align="left"><tr id="row62740391"><th class="cellrowborder" valign="top" width="24.240000000000002%" id="mcps1.2.4.1.1"><p id="p48806929"><a name="p48806929"></a><a name="p48806929"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="15.15%" id="mcps1.2.4.1.2"><p id="p61047167"><a name="p61047167"></a><a name="p61047167"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="60.61%" id="mcps1.2.4.1.3"><p id="p45873498"><a name="p45873498"></a><a name="p45873498"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row24765833"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.1 "><p id="p59875445"><a name="p59875445"></a><a name="p59875445"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="15.15%" headers="mcps1.2.4.1.2 "><p id="p18072837"><a name="p18072837"></a><a name="p18072837"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.61%" headers="mcps1.2.4.1.3 "><p id="p54613665"><a name="p54613665"></a><a name="p54613665"></a>Parameter description</p>
</td>
</tr>
<tr id="row21760944"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.1 "><p id="p17806026"><a name="p17806026"></a><a name="p17806026"></a>param_id</p>
</td>
<td class="cellrowborder" valign="top" width="15.15%" headers="mcps1.2.4.1.2 "><p id="p33002021"><a name="p33002021"></a><a name="p33002021"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="60.61%" headers="mcps1.2.4.1.3 "><p id="p55918057"><a name="p55918057"></a><a name="p55918057"></a>Parameter ID.</p>
<p id="p33500465"><a name="p33500465"></a><a name="p33500465"></a>For the possible values, see the <strong id="b33068732"><a name="b33068732"></a><a name="b33068732"></a>Parameter ID</strong> column in <a href="#table41014082">Table 3-7</a>.</p>
</td>
</tr>
<tr id="row61321673"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.1 "><p id="p999606"><a name="p999606"></a><a name="p999606"></a>param_name</p>
</td>
<td class="cellrowborder" valign="top" width="15.15%" headers="mcps1.2.4.1.2 "><p id="p13859243"><a name="p13859243"></a><a name="p13859243"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.61%" headers="mcps1.2.4.1.3 "><p id="p48856913"><a name="p48856913"></a><a name="p48856913"></a>Parameter name.</p>
<p id="p37059038"><a name="p37059038"></a><a name="p37059038"></a>For the possible values, see the <strong id="b65095887"><a name="b65095887"></a><a name="b65095887"></a>Parameter Name</strong> column in <a href="#table41014082">Table 3-7</a>.</p>
</td>
</tr>
<tr id="row38275534"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.1 "><p id="p13310582"><a name="p13310582"></a><a name="p13310582"></a>param_value</p>
</td>
<td class="cellrowborder" valign="top" width="15.15%" headers="mcps1.2.4.1.2 "><p id="p4415342"><a name="p4415342"></a><a name="p4415342"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.61%" headers="mcps1.2.4.1.3 "><p id="p22098398"><a name="p22098398"></a><a name="p22098398"></a>Parameter value.</p>
</td>
</tr>
<tr id="row64667859"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.1 "><p id="p3605227"><a name="p3605227"></a><a name="p3605227"></a>default_value</p>
</td>
<td class="cellrowborder" valign="top" width="15.15%" headers="mcps1.2.4.1.2 "><p id="p23587984"><a name="p23587984"></a><a name="p23587984"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.61%" headers="mcps1.2.4.1.3 "><p id="p31578537"><a name="p31578537"></a><a name="p31578537"></a>Default value.</p>
<p id="p15771381"><a name="p15771381"></a><a name="p15771381"></a>For the possible values, see the <strong id="b7724703"><a name="b7724703"></a><a name="b7724703"></a>Default Value</strong> column in <a href="#table41014082">Table 3-7</a>.</p>
</td>
</tr>
<tr id="row21721177"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.1 "><p id="p14584895"><a name="p14584895"></a><a name="p14584895"></a>value_type</p>
</td>
<td class="cellrowborder" valign="top" width="15.15%" headers="mcps1.2.4.1.2 "><p id="p40525883"><a name="p40525883"></a><a name="p40525883"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.61%" headers="mcps1.2.4.1.3 "><p id="p61371058"><a name="p61371058"></a><a name="p61371058"></a>Value type.</p>
<p id="p15468616"><a name="p15468616"></a><a name="p15468616"></a>For the possible values, see the <strong id="b4999822"><a name="b4999822"></a><a name="b4999822"></a>Value Type</strong> column in <a href="#table41014082">Table 3-7</a>.</p>
</td>
</tr>
<tr id="row2332471"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.1 "><p id="p54712468"><a name="p54712468"></a><a name="p54712468"></a>value_range</p>
</td>
<td class="cellrowborder" valign="top" width="15.15%" headers="mcps1.2.4.1.2 "><p id="p2524942"><a name="p2524942"></a><a name="p2524942"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.61%" headers="mcps1.2.4.1.3 "><p id="p3193740"><a name="p3193740"></a><a name="p3193740"></a>Value range.</p>
<p id="p28743664"><a name="p28743664"></a><a name="p28743664"></a>For the possible values, see the <strong id="b57366391"><a name="b57366391"></a><a name="b57366391"></a>Value Range</strong> column in <a href="#table41014082">Table 3-7</a>.</p>
</td>
</tr>
</tbody>
</table>

[Table 3-7](#table41014082)  describes the configuration parameters of a DCS instance.

**Table  4**  Configuration parameters of a DCS instance

<a name="table41014082"></a>
<table><thead align="left"><tr id="row7571935"><th class="cellrowborder" valign="top" width="9.37906209379062%" id="mcps1.2.7.1.1"><p id="p9347022"><a name="p9347022"></a><a name="p9347022"></a>Parameter ID</p>
</th>
<th class="cellrowborder" valign="top" width="14.578542145785423%" id="mcps1.2.7.1.2"><p id="p18911313"><a name="p18911313"></a><a name="p18911313"></a>Parameter Name</p>
</th>
<th class="cellrowborder" valign="top" width="12.4987501249875%" id="mcps1.2.7.1.3"><p id="p55421393"><a name="p55421393"></a><a name="p55421393"></a>Value Type</p>
</th>
<th class="cellrowborder" valign="top" width="31.246875312468752%" id="mcps1.2.7.1.4"><p id="p59947829"><a name="p59947829"></a><a name="p59947829"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="21.87781221877812%" id="mcps1.2.7.1.5"><p id="p23935974"><a name="p23935974"></a><a name="p23935974"></a>Value Range</p>
</th>
<th class="cellrowborder" valign="top" width="10.418958104189581%" id="mcps1.2.7.1.6"><p id="p59765707"><a name="p59765707"></a><a name="p59765707"></a>Default Value</p>
</th>
</tr>
</thead>
<tbody><tr id="row9184076"><td class="cellrowborder" valign="top" width="9.37906209379062%" headers="mcps1.2.7.1.1 "><p id="p5712723"><a name="p5712723"></a><a name="p5712723"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="14.578542145785423%" headers="mcps1.2.7.1.2 "><p id="p60077381"><a name="p60077381"></a><a name="p60077381"></a>timeout</p>
</td>
<td class="cellrowborder" valign="top" width="12.4987501249875%" headers="mcps1.2.7.1.3 "><p id="p34429708"><a name="p34429708"></a><a name="p34429708"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="31.246875312468752%" headers="mcps1.2.7.1.4 "><p id="p37342992"><a name="p37342992"></a><a name="p37342992"></a>Connection between the client and server (DCS instance) will be closed if the client is idle for the timeout period (measured in seconds). A timeout period of 0 seconds indicates that the timeout function is disabled.</p>
</td>
<td class="cellrowborder" valign="top" width="21.87781221877812%" headers="mcps1.2.7.1.5 "><p id="p4883512"><a name="p4883512"></a><a name="p4883512"></a>0 to 7200 seconds</p>
</td>
<td class="cellrowborder" valign="top" width="10.418958104189581%" headers="mcps1.2.7.1.6 "><p id="p60020205"><a name="p60020205"></a><a name="p60020205"></a>0</p>
</td>
</tr>
<tr id="row3310935"><td class="cellrowborder" valign="top" width="9.37906209379062%" headers="mcps1.2.7.1.1 "><p id="p66859210"><a name="p66859210"></a><a name="p66859210"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="14.578542145785423%" headers="mcps1.2.7.1.2 "><p id="p46886909"><a name="p46886909"></a><a name="p46886909"></a>maxmemory-policy</p>
</td>
<td class="cellrowborder" valign="top" width="12.4987501249875%" headers="mcps1.2.7.1.3 "><p id="p39743256"><a name="p39743256"></a><a name="p39743256"></a>Enum</p>
</td>
<td class="cellrowborder" valign="top" width="31.246875312468752%" headers="mcps1.2.7.1.4 "><p id="p65087172"><a name="p65087172"></a><a name="p65087172"></a>How Redis will select what to remove when maxmemory is reached.</p>
<p id="p48913640"><a name="p48913640"></a><a name="p48913640"></a>For more information about this parameter, see <a href="https://redis.io/topics/lru-cache" target="_blank" rel="noopener noreferrer">https://redis.io/topics/lru-cache</a>.</p>
</td>
<td class="cellrowborder" valign="top" width="21.87781221877812%" headers="mcps1.2.7.1.5 "><p id="p23236845"><a name="p23236845"></a><a name="p23236845"></a>volatile-lru</p>
<p id="p7805019"><a name="p7805019"></a><a name="p7805019"></a>allkeys-lru</p>
<p id="p3136315"><a name="p3136315"></a><a name="p3136315"></a>volatile-random</p>
<p id="p28226836"><a name="p28226836"></a><a name="p28226836"></a>allkeys-random</p>
<p id="p52714937"><a name="p52714937"></a><a name="p52714937"></a>volatile-ttl</p>
<p id="p4672385"><a name="p4672385"></a><a name="p4672385"></a>noeviction</p>
</td>
<td class="cellrowborder" valign="top" width="10.418958104189581%" headers="mcps1.2.7.1.6 "><p id="p42918923"><a name="p42918923"></a><a name="p42918923"></a>noeviction</p>
</td>
</tr>
<tr id="row50725990"><td class="cellrowborder" valign="top" width="9.37906209379062%" headers="mcps1.2.7.1.1 "><p id="p15164517"><a name="p15164517"></a><a name="p15164517"></a>3</p>
</td>
<td class="cellrowborder" valign="top" width="14.578542145785423%" headers="mcps1.2.7.1.2 "><p id="p20366389"><a name="p20366389"></a><a name="p20366389"></a>hash-max-ziplist-entries</p>
</td>
<td class="cellrowborder" valign="top" width="12.4987501249875%" headers="mcps1.2.7.1.3 "><p id="p39064830"><a name="p39064830"></a><a name="p39064830"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="31.246875312468752%" headers="mcps1.2.7.1.4 "><p id="p10134631"><a name="p10134631"></a><a name="p10134631"></a>When the number of entries in hashes is less than the value of this parameter, hashes are encoded using a memory efficient data structure.</p>
</td>
<td class="cellrowborder" valign="top" width="21.87781221877812%" headers="mcps1.2.7.1.5 "><p id="p15598744"><a name="p15598744"></a><a name="p15598744"></a>1 to 10000</p>
</td>
<td class="cellrowborder" valign="top" width="10.418958104189581%" headers="mcps1.2.7.1.6 "><p id="p55538746"><a name="p55538746"></a><a name="p55538746"></a>512</p>
</td>
</tr>
<tr id="row30086668"><td class="cellrowborder" valign="top" width="9.37906209379062%" headers="mcps1.2.7.1.1 "><p id="p21101082"><a name="p21101082"></a><a name="p21101082"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="14.578542145785423%" headers="mcps1.2.7.1.2 "><p id="p31466092"><a name="p31466092"></a><a name="p31466092"></a>hash-max-ziplist-value</p>
</td>
<td class="cellrowborder" valign="top" width="12.4987501249875%" headers="mcps1.2.7.1.3 "><p id="p65725547"><a name="p65725547"></a><a name="p65725547"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="31.246875312468752%" headers="mcps1.2.7.1.4 "><p id="p22169086"><a name="p22169086"></a><a name="p22169086"></a>When the biggest entry in hashes does not exceed the length threshold indicated by this parameter, hashes are encoded using a memory efficient data structure.</p>
</td>
<td class="cellrowborder" valign="top" width="21.87781221877812%" headers="mcps1.2.7.1.5 "><p id="p50865550"><a name="p50865550"></a><a name="p50865550"></a>1 to 10000</p>
</td>
<td class="cellrowborder" valign="top" width="10.418958104189581%" headers="mcps1.2.7.1.6 "><p id="p26468866"><a name="p26468866"></a><a name="p26468866"></a>64</p>
</td>
</tr>
<tr id="row36893205"><td class="cellrowborder" valign="top" width="9.37906209379062%" headers="mcps1.2.7.1.1 "><p id="p35559643"><a name="p35559643"></a><a name="p35559643"></a>5</p>
</td>
<td class="cellrowborder" valign="top" width="14.578542145785423%" headers="mcps1.2.7.1.2 "><p id="p61758841"><a name="p61758841"></a><a name="p61758841"></a>list-max-ziplist-entries</p>
</td>
<td class="cellrowborder" valign="top" width="12.4987501249875%" headers="mcps1.2.7.1.3 "><p id="p36410264"><a name="p36410264"></a><a name="p36410264"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="31.246875312468752%" headers="mcps1.2.7.1.4 "><p id="p63550304"><a name="p63550304"></a><a name="p63550304"></a>When the number of entries in lists is less than the value of this parameter, lists are encoded using a memory efficient data structure.</p>
</td>
<td class="cellrowborder" valign="top" width="21.87781221877812%" headers="mcps1.2.7.1.5 "><p id="p47300984"><a name="p47300984"></a><a name="p47300984"></a>1 to 10000</p>
</td>
<td class="cellrowborder" valign="top" width="10.418958104189581%" headers="mcps1.2.7.1.6 "><p id="p6174472"><a name="p6174472"></a><a name="p6174472"></a>512</p>
</td>
</tr>
<tr id="row55570253"><td class="cellrowborder" valign="top" width="9.37906209379062%" headers="mcps1.2.7.1.1 "><p id="p4896645"><a name="p4896645"></a><a name="p4896645"></a>6</p>
</td>
<td class="cellrowborder" valign="top" width="14.578542145785423%" headers="mcps1.2.7.1.2 "><p id="p61083978"><a name="p61083978"></a><a name="p61083978"></a>list-max-ziplist-value</p>
</td>
<td class="cellrowborder" valign="top" width="12.4987501249875%" headers="mcps1.2.7.1.3 "><p id="p48855171"><a name="p48855171"></a><a name="p48855171"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="31.246875312468752%" headers="mcps1.2.7.1.4 "><p id="p64954777"><a name="p64954777"></a><a name="p64954777"></a>When the biggest entry in lists does not exceed the length threshold indicated by this parameter, lists are encoded using a memory efficient data structure.</p>
</td>
<td class="cellrowborder" valign="top" width="21.87781221877812%" headers="mcps1.2.7.1.5 "><p id="p26845555"><a name="p26845555"></a><a name="p26845555"></a>1 to 10000</p>
</td>
<td class="cellrowborder" valign="top" width="10.418958104189581%" headers="mcps1.2.7.1.6 "><p id="p27006329"><a name="p27006329"></a><a name="p27006329"></a>64</p>
</td>
</tr>
<tr id="row41730377"><td class="cellrowborder" valign="top" width="9.37906209379062%" headers="mcps1.2.7.1.1 "><p id="p24717373"><a name="p24717373"></a><a name="p24717373"></a>7</p>
</td>
<td class="cellrowborder" valign="top" width="14.578542145785423%" headers="mcps1.2.7.1.2 "><p id="p55950226"><a name="p55950226"></a><a name="p55950226"></a>set-max-intset-entries</p>
</td>
<td class="cellrowborder" valign="top" width="12.4987501249875%" headers="mcps1.2.7.1.3 "><p id="p35674480"><a name="p35674480"></a><a name="p35674480"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="31.246875312468752%" headers="mcps1.2.7.1.4 "><p id="p3951742"><a name="p3951742"></a><a name="p3951742"></a>When a set is composed entirely of strings that happen to be integers in radix 10 in the range of 64 bit signed integers, sets are encoded using a memory efficient data structure.</p>
</td>
<td class="cellrowborder" valign="top" width="21.87781221877812%" headers="mcps1.2.7.1.5 "><p id="p51655652"><a name="p51655652"></a><a name="p51655652"></a>1 to 10000</p>
</td>
<td class="cellrowborder" valign="top" width="10.418958104189581%" headers="mcps1.2.7.1.6 "><p id="p23358283"><a name="p23358283"></a><a name="p23358283"></a>512</p>
</td>
</tr>
<tr id="row8897958"><td class="cellrowborder" valign="top" width="9.37906209379062%" headers="mcps1.2.7.1.1 "><p id="p49646001"><a name="p49646001"></a><a name="p49646001"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="14.578542145785423%" headers="mcps1.2.7.1.2 "><p id="p61903120"><a name="p61903120"></a><a name="p61903120"></a>zset-max-ziplist-entries</p>
</td>
<td class="cellrowborder" valign="top" width="12.4987501249875%" headers="mcps1.2.7.1.3 "><p id="p48096812"><a name="p48096812"></a><a name="p48096812"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="31.246875312468752%" headers="mcps1.2.7.1.4 "><p id="p3527660"><a name="p3527660"></a><a name="p3527660"></a>When the number of entries in sorted sets is less than the value of this parameter, sorted sets are encoded using a memory efficient data structure.</p>
</td>
<td class="cellrowborder" valign="top" width="21.87781221877812%" headers="mcps1.2.7.1.5 "><p id="p17305016"><a name="p17305016"></a><a name="p17305016"></a>1 to 10000</p>
</td>
<td class="cellrowborder" valign="top" width="10.418958104189581%" headers="mcps1.2.7.1.6 "><p id="p59529081"><a name="p59529081"></a><a name="p59529081"></a>128</p>
</td>
</tr>
<tr id="row65999689"><td class="cellrowborder" valign="top" width="9.37906209379062%" headers="mcps1.2.7.1.1 "><p id="p44374612"><a name="p44374612"></a><a name="p44374612"></a>9</p>
</td>
<td class="cellrowborder" valign="top" width="14.578542145785423%" headers="mcps1.2.7.1.2 "><p id="p37573832"><a name="p37573832"></a><a name="p37573832"></a>zset-max-ziplist-value</p>
</td>
<td class="cellrowborder" valign="top" width="12.4987501249875%" headers="mcps1.2.7.1.3 "><p id="p23581515"><a name="p23581515"></a><a name="p23581515"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="31.246875312468752%" headers="mcps1.2.7.1.4 "><p id="p31054600"><a name="p31054600"></a><a name="p31054600"></a>When the biggest entry in sorted sets does not exceed the length threshold indicated by this parameter, sorted sets are encoded using a memory efficient data structure.</p>
</td>
<td class="cellrowborder" valign="top" width="21.87781221877812%" headers="mcps1.2.7.1.5 "><p id="p32394661"><a name="p32394661"></a><a name="p32394661"></a>1 to 10000</p>
</td>
<td class="cellrowborder" valign="top" width="10.418958104189581%" headers="mcps1.2.7.1.6 "><p id="p6721866"><a name="p6721866"></a><a name="p6721866"></a>64</p>
</td>
</tr>
<tr id="row60496800"><td class="cellrowborder" valign="top" width="9.37906209379062%" headers="mcps1.2.7.1.1 "><p id="p1293733"><a name="p1293733"></a><a name="p1293733"></a>10</p>
</td>
<td class="cellrowborder" valign="top" width="14.578542145785423%" headers="mcps1.2.7.1.2 "><p id="p37683526"><a name="p37683526"></a><a name="p37683526"></a>latency-monitor-threshold</p>
</td>
<td class="cellrowborder" valign="top" width="12.4987501249875%" headers="mcps1.2.7.1.3 "><p id="p32466797"><a name="p32466797"></a><a name="p32466797"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="31.246875312468752%" headers="mcps1.2.7.1.4 "><p id="p12564863"><a name="p12564863"></a><a name="p12564863"></a>Only events that run in more time than the configured latency-monitor-threshold will be logged as latency spikes.</p>
<a name="ul45974909"></a><a name="ul45974909"></a><ul id="ul45974909"><li>If the latency-monitor-threshold is set to 0, latency monitoring is disabled.</li><li>If the latency-monitor-threshold is set to a value greater than 0, all events blocking the server for a time equal to or greater than the configured latency-monitor-threshold will be logged.</li></ul>
<p id="p28385674"><a name="p28385674"></a><a name="p28385674"></a>By running the LATENCY command, you can perform operations related to latency monitoring, such as enabling latency monitoring, reporting the latest latency events logged, and obtaining statistical data.</p>
<p id="p54144478"><a name="p54144478"></a><a name="p54144478"></a>For more information about the latency-monitor-threshold, visit <a href="https://redis.io/topics/latency-monitor" target="_blank" rel="noopener noreferrer">https://redis.io/topics/latency-monitor</a>.</p>
</td>
<td class="cellrowborder" valign="top" width="21.87781221877812%" headers="mcps1.2.7.1.5 "><p id="p11312807"><a name="p11312807"></a><a name="p11312807"></a>0 to 86400000 ms</p>
</td>
<td class="cellrowborder" valign="top" width="10.418958104189581%" headers="mcps1.2.7.1.6 "><p id="p43922160"><a name="p43922160"></a><a name="p43922160"></a>0</p>
</td>
</tr>
<tr id="row59755124"><td class="cellrowborder" valign="top" width="9.37906209379062%" headers="mcps1.2.7.1.1 "><p id="p8326855"><a name="p8326855"></a><a name="p8326855"></a>12</p>
</td>
<td class="cellrowborder" valign="top" width="14.578542145785423%" headers="mcps1.2.7.1.2 "><p id="p3386626"><a name="p3386626"></a><a name="p3386626"></a>reserved-memory</p>
</td>
<td class="cellrowborder" valign="top" width="12.4987501249875%" headers="mcps1.2.7.1.3 "><p id="p5881294"><a name="p5881294"></a><a name="p5881294"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="31.246875312468752%" headers="mcps1.2.7.1.4 "><p id="p6622802"><a name="p6622802"></a><a name="p6622802"></a>The number of megabytes reserved for the backend to perform internal processing such as persistence and master/standby replication.</p>
<p id="p59605225"><a name="p59605225"></a><a name="p59605225"></a>This parameter is configurable only for master/standby instances.</p>
</td>
<td class="cellrowborder" valign="top" width="21.87781221877812%" headers="mcps1.2.7.1.5 "><p id="p63293941"><a name="p63293941"></a><a name="p63293941"></a>0% to 50% of maximum memory space initially available to the instance and below the current free memory space</p>
<p id="p32774565"><a name="p32774565"></a><a name="p32774565"></a>NOTE: For more information about maximum available memory of each instance type, see <em id="i26535630"><a name="i26535630"></a><a name="i26535630"></a>Distributed Cache Service User Guide 0X.</em></p>
</td>
<td class="cellrowborder" valign="top" width="10.418958104189581%" headers="mcps1.2.7.1.6 "><p id="p1902427"><a name="p1902427"></a><a name="p1902427"></a>0</p>
</td>
</tr>
<tr id="row17121849"><td class="cellrowborder" valign="top" width="9.37906209379062%" headers="mcps1.2.7.1.1 "><p id="p44692528"><a name="p44692528"></a><a name="p44692528"></a>13</p>
</td>
<td class="cellrowborder" valign="top" width="14.578542145785423%" headers="mcps1.2.7.1.2 "><p id="p63325007"><a name="p63325007"></a><a name="p63325007"></a>notify-keyspace-events</p>
</td>
<td class="cellrowborder" valign="top" width="12.4987501249875%" headers="mcps1.2.7.1.3 "><p id="p29051967"><a name="p29051967"></a><a name="p29051967"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="31.246875312468752%" headers="mcps1.2.7.1.4 "><p id="p4399144"><a name="p4399144"></a><a name="p4399144"></a>Keyspace event notification. If this parameter is configured, the Redis Sub/Pub feature will allow clients to receive an event when a Redis data set is modified.</p>
</td>
<td class="cellrowborder" valign="top" width="21.87781221877812%" headers="mcps1.2.7.1.5 "><p id="p20786353"><a name="p20786353"></a><a name="p20786353"></a>If the parameter value is an empty character string or null, the default value <strong id="b52859449"><a name="b52859449"></a><a name="b52859449"></a>Ex</strong> is used.</p>
<p id="p5972994"><a name="p5972994"></a><a name="p5972994"></a>You can set the value to a combination of any of the following characters, with each character identifying a class of keyspace events for which Redis will send notifications.</p>
<p id="p53756949"><a name="p53756949"></a><a name="p53756949"></a>K: Keyspace events, published with the __keyspace@__ prefix</p>
<p id="p14050500"><a name="p14050500"></a><a name="p14050500"></a>E: Keyevent events, published with __keyevent@__ prefix</p>
<p id="p59345638"><a name="p59345638"></a><a name="p59345638"></a>g: Generic commands (non-type specific) such as DEL, EXPIRE, and RENAME</p>
<p id="p64348702"><a name="p64348702"></a><a name="p64348702"></a>$: String commands</p>
<p id="p42267412"><a name="p42267412"></a><a name="p42267412"></a>l: List commands</p>
<p id="p44862393"><a name="p44862393"></a><a name="p44862393"></a>s: Set commands</p>
<p id="p1108358"><a name="p1108358"></a><a name="p1108358"></a>h: Hash commands</p>
<p id="p9975229"><a name="p9975229"></a><a name="p9975229"></a>z: Sorted set commands</p>
<p id="p22668197"><a name="p22668197"></a><a name="p22668197"></a>x: Expired events (events generated every time a key expires)</p>
<p id="p2687184"><a name="p2687184"></a><a name="p2687184"></a>e: Evicted events (events generated when a key is evicted for maxmemory)</p>
<p id="p24184664"><a name="p24184664"></a><a name="p24184664"></a>A: Alias for "g$lshzxe", so that the "AKE" string means all the events.</p>
<p id="p16335389"><a name="p16335389"></a><a name="p16335389"></a>Note that the parameter value must contain either K or E.</p>
</td>
<td class="cellrowborder" valign="top" width="10.418958104189581%" headers="mcps1.2.7.1.6 "><p id="p48098122"><a name="p48098122"></a><a name="p48098122"></a>Ex</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>Description of the  **notify-keyspace-events**  parameter:  
>-   The parameter value must contain either K or E.  
>-   A is an alias for "g$lshzxe"and cannot be used together with any of the characters "g$lshzxe".  
>-   For example, the value Kl means that Redis will notify Pub/Sub clients about keyspace events and list commands. The value AKE means Redis will notify Pub/Sub clients about all events.  

-   Example response:

    ```
    { 
     "status": "RUNNING", 
     "instance_id": "c08fdc6e-5c25-4185-ab57-c0a5529b727f", 
     "redis_config": [ 
            { 
                "description": "How Redis will select what to remove when maxmemory is reached, You can select among five behaviors: volatile-lru : remove the key with an expire set using an LRU algorithm allkeys-lru : remove any key according to the LRU algorithm volatile-random: remove a random key with an expire set allkeys-random: remove a random key, any key volatile-ttl : remove the key with the nearest expire time (minor TTL) noeviction : don't expire at all, just return an error on write operations", 
                "param_id": 2, 
                "param_name": "maxmemory-policy", 
                "param_value": "noeviction", 
                "default_value": "noeviction", 
                "value_type": "Enum", 
                "value_range": "volatile-lru,allkeys-lru,volatile-random,allkeys-random,volatile-ttl,noeviction" 
            }, 
            { 
                "description": "Hashes are encoded using a memory efficient data structure when they have a small number of entries", 
                "param_id": 3, 
                "param_name": "hash-max-ziplist-entries", 
             "param_value": "512", 
                "default_value": "512", 
                "value_type": "Interger", 
                "value_range": "1-10000" 
            }, 
            { 
                "description": "Hashes are encoded using a memory efficient data structure when the biggest entry does not exceed a given threshold", 
                "param_id": 4, 
                "param_name": "hash-max-ziplist-value", 
                "param_value": "64", 
                "default_value": "64", 
                "value_type": "Interger", 
                "value_range": "1-10000" 
            }, 
            { 
                "description": "Lists are encoded using a memory efficient data structure when they have a small number of entries", 
                "param_id": 5, 
                "param_name": "list-max-ziplist-entries", 
                "param_value": "512", 
                "default_value": "512", 
                "value_type": "Interger", 
                "value_range": "1-10000" 
            }, 
            { 
                "description": "Lists are encoded using a memory efficient data structure when the biggest entry does not exceed a given threshold", 
                "param_id": 6, 
                "param_name": "list-max-ziplist-value", 
                "param_value": "64", 
                "default_value": "64", 
                "value_type": "Interger", 
                "value_range": "1-10000" 
            }, 
            { 
                "description": "When a set is composed of just strings that happen to be integers in radix 10 in the range of 64 bit signed integers.", 
                "param_id": 7, 
                "param_name": "set-max-intset-entries", 
                "param_value": "512", 
                "default_value": "512", 
                "value_type": "Interger", 
                "value_range": "1-10000" 
            }, 
            { 
                "description": "Sorted sets are encoded using a memory efficient data structure when they have a small number of entries", 
                "param_id": 8, 
                "param_name": "zset-max-ziplist-entries", 
                "param_value": "128", 
                "default_value": "128", 
                "value_type": "Interger", 
                "value_range": "1-10000" 
            }, 
            { 
                "description": "Sorted sets are encoded using a memory efficient data structure when the biggest entry does not exceed a given threshold", 
                "param_id": 9, 
                "param_name": "zset-max-ziplist-value", 
                "param_value": "64", 
                "default_value": "64", 
                "value_type": "Interger", 
                "value_range": "1-10000" 
            }, 
            { 
                "description": "Close the connection after a client is idle for N seconds (0 to disable)", 
                "param_id": 1, 
                "param_name": "timeout", 
                "param_value": "0", 
                "default_value": "0", 
                "value_type": "Interger", 
                "value_range": "0-7200" 
            }, 
            { 
                "description": "Only events that run in more time than the configured latency-monitor-threshold will be logged as latency spikes. If latency-monitor-threshold is set to 0, latency monitoring is disabled. If latency-monitor-threshold is set to a value greater than 0, all events blocking the server for a time equal to or greater than the configured latency-monitor-threshold will be logged.", 
                "param_id": 10, 
                "param_name": "latency-monitor-threshold", 
                "param_value": "0", 
                "default_value": "0", 
                "value_type": "Interger", 
                "value_range": "0-86400000" 
            }, 
            { 
                "description": "The total memory, in bytes, reserved for non-data usage.", 
                "param_id": 12, 
                "param_name": "reserved-memory", 
                "param_value": "0", 
                "default_value": "0", 
                "value_type": "Interger", 
                "value_range": "0-6553" 
            }, 
            { 
                "description": "Redis can notify Pub or Sub clients about events happening in the key space", 
                "param_id": 13, 
                "param_name": "notify-keyspace-events", 
                "param_value": null, 
             "default_value": null, 
                "value_type": "regular", 
                "value_range": "([KE]+([A]|[g$lshzxe]+)){0,11}" 
            } 
     ], 
     "config_status": "SUCCESS", 
     "config_time": "" 
    }
    ```


