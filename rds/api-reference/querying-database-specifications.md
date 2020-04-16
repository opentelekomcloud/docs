# Querying Database Specifications<a name="rds_06_0002"></a>

## Function<a name="section4850156117316"></a>

This API is used to query the database specifications of a specified DB engine version.

-   Learn how to  [authorize and authenticate](authentication.md)  this API before using it.
-   Before calling this API, obtain the required  [region and endpoint](https://docs.otc.t-systems.com/en-us/endpoint/index.html).

## URI<a name="section28961517113719"></a>

-   URI format

    GET https://\{_Endpoint_\}/v3/\{project\_id\}/flavors/\{database\_name\}?version\_name=\{version\_name\}

-   Example

    https://rds.eu-de.otc.t-systems.com/v3/0483b6b16e954cb88930a360d2c4e663/flavors/mysql?version\_name=5.7


-   Parameter description

    **Table  1**  Parameter description

    <a name="table4657088"></a>
    <table><thead align="left"><tr id="row60083059"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.1"><p id="p34889605"><a name="p34889605"></a><a name="p34889605"></a><strong id="b1836614023310"><a name="b1836614023310"></a><a name="b1836614023310"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="24%" id="mcps1.2.4.1.2"><p id="p7485743"><a name="p7485743"></a><a name="p7485743"></a><strong id="b1273274016330"><a name="b1273274016330"></a><a name="b1273274016330"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="55.00000000000001%" id="mcps1.2.4.1.3"><p id="p2365466"><a name="p2365466"></a><a name="p2365466"></a><strong id="b491164163315"><a name="b491164163315"></a><a name="b491164163315"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row57385070"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p17679057"><a name="p17679057"></a><a name="p17679057"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.2 "><p id="p22717550"><a name="p22717550"></a><a name="p22717550"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p28182251"><a name="p28182251"></a><a name="p28182251"></a>Specifies the project ID of a tenant in a region.</p>
    <p id="p181691757183820"><a name="p181691757183820"></a><a name="p181691757183820"></a>For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row2864326155157"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p41557789155220"><a name="p41557789155220"></a><a name="p41557789155220"></a>database_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.2 "><p id="p10737742155220"><a name="p10737742155220"></a><a name="p10737742155220"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p64450739155220"><a name="p64450739155220"></a><a name="p64450739155220"></a>Specifies the DB engine name. Its value can be any of the following and is case-insensitive:</p>
    <a name="ul924933143511"></a><a name="ul924933143511"></a><ul id="ul924933143511"><li>MySQL</li><li>PostgreSQL</li><li>SQLServer</li></ul>
    </td>
    </tr>
    <tr id="row4161445171"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p516110417170"><a name="p516110417170"></a><a name="p516110417170"></a>version_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.2 "><p id="p116114111716"><a name="p116114111716"></a><a name="p116114111716"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p31610414179"><a name="p31610414179"></a><a name="p31610414179"></a>Specifies the database version. For details about how to obtain the database version, see section <a href="querying-version-information-about-a-db-engine.md">Querying Version Information About a DB Engine</a>. </p>
    </td>
    </tr>
    <tr id="row115971435205310"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p1959723516537"><a name="p1959723516537"></a><a name="p1959723516537"></a>spec_code</p>
    </td>
    <td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.2 "><p id="p105971935105319"><a name="p105971935105319"></a><a name="p105971935105319"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p10597235155311"><a name="p10597235155311"></a><a name="p10597235155311"></a>Specifies the specification code.</p>
    <p id="p86678172112"><a name="p86678172112"></a><a name="p86678172112"></a>The format of the specification code is: {<em id="i126668122115"><a name="i126668122115"></a><a name="i126668122115"></a>spec code</em>}{<em id="i196617832114"><a name="i196617832114"></a><a name="i196617832114"></a>instance mode</em>}.</p>
    <a name="ul24442061515"></a><a name="ul24442061515"></a><ul id="ul24442061515"><li><em id="i35334240217"><a name="i35334240217"></a><a name="i35334240217"></a>spec code</em> can be obtained from <a href="db-instance-specifications.md#ted9b9d433c8a4c52884e199e17f94479">Table 1</a>.</li><li><em id="i9410114261817"><a name="i9410114261817"></a><a name="i9410114261817"></a>instance mode</em> can be any of the following:<a name="ul07451328162117"></a><a name="ul07451328162117"></a><ul id="ul07451328162117"><li>For single DB instances, the value is <strong id="b105131586157"><a name="b105131586157"></a><a name="b105131586157"></a>null</strong>. Example spe_code: rds.mysql.s1.xlarge</li><li>For primary/standby DB instances, the value is <span class="parmvalue" id="parmvalue05973377819"><a name="parmvalue05973377819"></a><a name="parmvalue05973377819"></a><b>.ha</b></span>. Example spe_code: rds.mysql.s1.xlarge.ha</li><li>For read replicas, the value is <span class="parmvalue" id="parmvalue17579173418816"><a name="parmvalue17579173418816"></a><a name="parmvalue17579173418816"></a><b>.rr</b></span>. Example spe_code: rds.mysql.s1.xlarge.rr</li></ul>
    </li></ul>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section36474591"></a>

None

## Response<a name="section59835867"></a>

-   Normal response

    **Table  2**  Parameter description

    <a name="table29752153"></a>
    <table><thead align="left"><tr id="row62070345"><th class="cellrowborder" valign="top" width="16.6%" id="mcps1.2.4.1.1"><p id="p61642077"><a name="p61642077"></a><a name="p61642077"></a><strong id="b12952446193514"><a name="b12952446193514"></a><a name="b12952446193514"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.07%" id="mcps1.2.4.1.2"><p id="p26952341"><a name="p26952341"></a><a name="p26952341"></a><strong id="b1660114793511"><a name="b1660114793511"></a><a name="b1660114793511"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33%" id="mcps1.2.4.1.3"><p id="p35656026"><a name="p35656026"></a><a name="p35656026"></a><strong id="b8477174833518"><a name="b8477174833518"></a><a name="b8477174833518"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2456979"><td class="cellrowborder" valign="top" width="16.6%" headers="mcps1.2.4.1.1 "><p id="p64797609"><a name="p64797609"></a><a name="p64797609"></a>flavors</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.07%" headers="mcps1.2.4.1.2 "><p id="p158510360232"><a name="p158510360232"></a><a name="p158510360232"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p22140377"><a name="p22140377"></a><a name="p22140377"></a>Indicates the DB instance specifications information list.</p>
    <p id="p16922658102215"><a name="p16922658102215"></a><a name="p16922658102215"></a>For details, see <a href="#table66531170">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  flavors field data structure description

    <a name="table66531170"></a>
    <table><thead align="left"><tr id="row12984378"><th class="cellrowborder" valign="top" width="17.419999999999998%" id="mcps1.2.4.1.1"><p id="p45101667"><a name="p45101667"></a><a name="p45101667"></a><strong id="b186891113615"><a name="b186891113615"></a><a name="b186891113615"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="13.34%" id="mcps1.2.4.1.2"><p id="p29356372"><a name="p29356372"></a><a name="p29356372"></a><strong id="b14880101113614"><a name="b14880101113614"></a><a name="b14880101113614"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="69.24%" id="mcps1.2.4.1.3"><p id="p29055926"><a name="p29055926"></a><a name="p29055926"></a><strong id="b536521263611"><a name="b536521263611"></a><a name="b536521263611"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4719792"><td class="cellrowborder" valign="top" width="17.419999999999998%" headers="mcps1.2.4.1.1 "><p id="p95609428242"><a name="p95609428242"></a><a name="p95609428242"></a>vcpus</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.34%" headers="mcps1.2.4.1.2 "><p id="p29373839"><a name="p29373839"></a><a name="p29373839"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="69.24%" headers="mcps1.2.4.1.3 "><p id="p30470722"><a name="p30470722"></a><a name="p30470722"></a>Indicates the CPU size. For example, the value <strong id="b1311053793611"><a name="b1311053793611"></a><a name="b1311053793611"></a>1</strong> indicates 1 vCPU.</p>
    </td>
    </tr>
    <tr id="row5801050"><td class="cellrowborder" valign="top" width="17.419999999999998%" headers="mcps1.2.4.1.1 "><p id="p32321902251"><a name="p32321902251"></a><a name="p32321902251"></a>ram</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.34%" headers="mcps1.2.4.1.2 "><p id="p9967070"><a name="p9967070"></a><a name="p9967070"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="69.24%" headers="mcps1.2.4.1.3 "><p id="p175975912613"><a name="p175975912613"></a><a name="p175975912613"></a>Indicates the memory size in GB.</p>
    </td>
    </tr>
    <tr id="row18237015"><td class="cellrowborder" valign="top" width="17.419999999999998%" headers="mcps1.2.4.1.1 "><p id="p803253"><a name="p803253"></a><a name="p803253"></a>spec_code</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.34%" headers="mcps1.2.4.1.2 "><p id="p65063572"><a name="p65063572"></a><a name="p65063572"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="69.24%" headers="mcps1.2.4.1.3 "><p id="p14244105293416"><a name="p14244105293416"></a><a name="p14244105293416"></a>Indicates the resource specification code. Use <strong id="b108281149135817"><a name="b108281149135817"></a><a name="b108281149135817"></a>rds.mysql.m1.xlarge.rr</strong> as an example.</p>
    <a name="ul12216011105918"></a><a name="ul12216011105918"></a><ul id="ul12216011105918"><li><span class="parmvalue" id="parmvalue136353217115"><a name="parmvalue136353217115"></a><a name="parmvalue136353217115"></a><b>rds</b></span>: indicates the RDS product.</li><li><span class="parmvalue" id="parmvalue0715115813017"><a name="parmvalue0715115813017"></a><a name="parmvalue0715115813017"></a><b>mysql</b></span>: indicates the DB engine.</li><li><span class="parmvalue" id="parmvalue7179568013"><a name="parmvalue7179568013"></a><a name="parmvalue7179568013"></a><b>m1.xlarge</b></span>: indicates the high memory performance specifications.</li><li><span class="parmvalue" id="parmvalue138931811171118"><a name="parmvalue138931811171118"></a><a name="parmvalue138931811171118"></a><b>rr</b></span>: indicates the read replica (<span class="parmvalue" id="parmvalue48932111115"><a name="parmvalue48932111115"></a><a name="parmvalue48932111115"></a><b>.ha</b></span> indicates primary/standby DB instances).</li></ul>
    </td>
    </tr>
    <tr id="row821651732516"><td class="cellrowborder" valign="top" width="17.419999999999998%" headers="mcps1.2.4.1.1 "><p id="p12168175255"><a name="p12168175255"></a><a name="p12168175255"></a>instance_mode</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.34%" headers="mcps1.2.4.1.2 "><p id="p621615176251"><a name="p621615176251"></a><a name="p621615176251"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="69.24%" headers="mcps1.2.4.1.3 "><p id="p227871816573"><a name="p227871816573"></a><a name="p227871816573"></a>Indicates the DB instance type. Its value can be any of the following:</p>
    <a name="ul1328613207570"></a><a name="ul1328613207570"></a><ul id="ul1328613207570"><li><strong id="b94633131255"><a name="b94633131255"></a><a name="b94633131255"></a>ha</strong>: indicates primary/standby DB instances.</li><li><strong id="b72493481257"><a name="b72493481257"></a><a name="b72493481257"></a>replica</strong>: indicates read replicas.</li><li><strong id="b1497352268"><a name="b1497352268"></a><a name="b1497352268"></a>single</strong>: indicates single DB instances.</li></ul>
    </td>
    </tr>
    <tr id="row13887256172319"><td class="cellrowborder" valign="top" width="17.419999999999998%" headers="mcps1.2.4.1.1 "><p id="p722175112411"><a name="p722175112411"></a><a name="p722175112411"></a>az_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.34%" headers="mcps1.2.4.1.2 "><p id="p12213514242"><a name="p12213514242"></a><a name="p12213514242"></a>Map&lt;String, String&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="69.24%" headers="mcps1.2.4.1.3 "><p id="p172295182411"><a name="p172295182411"></a><a name="p172295182411"></a>Indicates the status of the AZ to which the DB instance specifications belong. Its value can be any of the following:</p>
    <a name="ul192219516243"></a><a name="ul192219516243"></a><ul id="ul192219516243"><li><strong id="b748045614206"><a name="b748045614206"></a><a name="b748045614206"></a>normal</strong>: indicates that the AZ is on sale.</li><li><strong id="b20762105382319"><a name="b20762105382319"></a><a name="b20762105382319"></a>unsupported</strong>: indicates that the DB instance specifications are not supported by the AZ.</li><li><strong id="b842352706154546"><a name="b842352706154546"></a><a name="b842352706154546"></a>sellout</strong>: indicates that the DB instance specifications are sold out.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Example normal response

    ```
    {
    	"flavors": [{
    		"vcpus": "1",
    		"ram": 2,
    		"spec_code": "rds.mysql.c2.medium.ha",
    		"instance_mode": "ha",
    		"az_status": {
    			"az1": "normal",
    			"az2": "normal"
    		}
    	}, {
    		"vcpus": "1",
    		"ram": 2,
    		"spec_code": "rds.mysql.c2.medium.rr",
    		"instance_mode": "replica",
    		"az_status": {
    			"az1": "normal",
    			"az2": "normal"
    		}
    	}]
    }
    ```

-   Abnormal response

    For details, see  [Abnormal Request Results](abnormal-request-results.md).


## Status Code<a name="section4778540915440"></a>

For details, see  [Status Codes](status-codes.md).

## Error Code<a name="section946032144017"></a>

For details, see  [Error Codes](error-codes.md).

