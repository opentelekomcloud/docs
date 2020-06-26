# Obtaining the Parameter Template of a Specified DB Instance<a name="rds_09_0306"></a>

## Function<a name="section8137930122719"></a>

This API is used to obtain information about the parameter template of a specified DB instance.

-   Learn how to  [authorize and authenticate](authentication.md)  this API before using it.
-   Before calling this API, obtain the required  [region and endpoint](https://docs.otc.t-systems.com/en-us/endpoint/index.html).

## Constraints<a name="section1270314533467"></a>

-   The following DB engines are supported: MySQL, PostgreSQL, and Microsoft SQL Server.
-   For Microsoft SQL Server, only the following editions are supported: Microsoft SQL Server 2014 SE, 2016 SE, and 2016 EE.

## URI<a name="section1013703014278"></a>

-   URI format

    GET https://\{_Endpoint_\}/v3/\{project\_id\}/instances/\{instance\_id\}/configurations

-   Example

    https://rds.eu-de.otc.t-systems.com/v3/0483b6b16e954cb88930a360d2c4e663/instances/dsfae23fsfdsae3435in01/configurations

-   Parameter description

    **Table  1**  Parameter description

    <a name="table11137330152717"></a>
    <table><thead align="left"><tr id="row6355630152713"><th class="cellrowborder" valign="top" width="21.14%" id="mcps1.2.4.1.1"><p id="p17355143011279"><a name="p17355143011279"></a><a name="p17355143011279"></a><strong id="b84235270691445"><a name="b84235270691445"></a><a name="b84235270691445"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="29.23%" id="mcps1.2.4.1.2"><p id="p435563012275"><a name="p435563012275"></a><a name="p435563012275"></a><strong id="b12588133410016"><a name="b12588133410016"></a><a name="b12588133410016"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="49.63%" id="mcps1.2.4.1.3"><p id="p635513013278"><a name="p635513013278"></a><a name="p635513013278"></a><strong id="b842352706163417"><a name="b842352706163417"></a><a name="b842352706163417"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1235520308278"><td class="cellrowborder" valign="top" width="21.14%" headers="mcps1.2.4.1.1 "><p id="p0355130202712"><a name="p0355130202712"></a><a name="p0355130202712"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.23%" headers="mcps1.2.4.1.2 "><p id="p1735511302279"><a name="p1735511302279"></a><a name="p1735511302279"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.63%" headers="mcps1.2.4.1.3 "><p id="p5355183014275"><a name="p5355183014275"></a><a name="p5355183014275"></a>Specifies the project ID of a tenant in a region.</p>
    <p id="p10290162519612"><a name="p10290162519612"></a><a name="p10290162519612"></a>For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row335573052719"><td class="cellrowborder" valign="top" width="21.14%" headers="mcps1.2.4.1.1 "><p id="p143551530112714"><a name="p143551530112714"></a><a name="p143551530112714"></a>instance_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.23%" headers="mcps1.2.4.1.2 "><p id="p163551830202719"><a name="p163551830202719"></a><a name="p163551830202719"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.63%" headers="mcps1.2.4.1.3 "><p id="p735515304272"><a name="p735515304272"></a><a name="p735515304272"></a>Specifies the DB instance ID compliant with the UUID format.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section20152163016277"></a>

None

## Response<a name="section14152103042715"></a>

-   Normal response

    **Table  2**  Parameter description

    <a name="table71681830152719"></a>
    <table><thead align="left"><tr id="row133554304277"><th class="cellrowborder" valign="top" width="23.01%" id="mcps1.2.4.1.1"><p id="p1235583052717"><a name="p1235583052717"></a><a name="p1235583052717"></a><strong id="b1402756775"><a name="b1402756775"></a><a name="b1402756775"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23.3%" id="mcps1.2.4.1.2"><p id="p1735523017272"><a name="p1735523017272"></a><a name="p1735523017272"></a><strong id="b842352706164541"><a name="b842352706164541"></a><a name="b842352706164541"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.690000000000005%" id="mcps1.2.4.1.3"><p id="p193551030132710"><a name="p193551030132710"></a><a name="p193551030132710"></a><strong id="b1393831383"><a name="b1393831383"></a><a name="b1393831383"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row735515304278"><td class="cellrowborder" valign="top" width="23.01%" headers="mcps1.2.4.1.1 "><p id="p1535518301272"><a name="p1535518301272"></a><a name="p1535518301272"></a>datastore_version_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.3%" headers="mcps1.2.4.1.2 "><p id="p1535511303279"><a name="p1535511303279"></a><a name="p1535511303279"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.690000000000005%" headers="mcps1.2.4.1.3 "><p id="p1835516301278"><a name="p1835516301278"></a><a name="p1835516301278"></a>Indicates the database version name.</p>
    </td>
    </tr>
    <tr id="row123556307271"><td class="cellrowborder" valign="top" width="23.01%" headers="mcps1.2.4.1.1 "><p id="p113551630112710"><a name="p113551630112710"></a><a name="p113551630112710"></a>datastore_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.3%" headers="mcps1.2.4.1.2 "><p id="p2035583016274"><a name="p2035583016274"></a><a name="p2035583016274"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.690000000000005%" headers="mcps1.2.4.1.3 "><p id="p1435553062714"><a name="p1435553062714"></a><a name="p1435553062714"></a>Indicates the database name.</p>
    </td>
    </tr>
    <tr id="row163551230122718"><td class="cellrowborder" valign="top" width="23.01%" headers="mcps1.2.4.1.1 "><p id="p133555309277"><a name="p133555309277"></a><a name="p133555309277"></a>created</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.3%" headers="mcps1.2.4.1.2 "><p id="p14355143016275"><a name="p14355143016275"></a><a name="p14355143016275"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.690000000000005%" headers="mcps1.2.4.1.3 "><p id="p20355830172718"><a name="p20355830172718"></a><a name="p20355830172718"></a>Indicates the creation time in the following format: yyyy-MM-ddTHH:mm:ssZ.</p>
    <p id="p15355193018279"><a name="p15355193018279"></a><a name="p15355193018279"></a><strong id="b96298341406"><a name="b96298341406"></a><a name="b96298341406"></a>T</strong> is the separator between the calendar and the hourly notation of time. <strong id="b662919348013"><a name="b662919348013"></a><a name="b662919348013"></a>Z</strong> indicates the time zone offset.</p>
    </td>
    </tr>
    <tr id="row17355123011278"><td class="cellrowborder" valign="top" width="23.01%" headers="mcps1.2.4.1.1 "><p id="p11355123016277"><a name="p11355123016277"></a><a name="p11355123016277"></a>updated</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.3%" headers="mcps1.2.4.1.2 "><p id="p1355183013273"><a name="p1355183013273"></a><a name="p1355183013273"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.690000000000005%" headers="mcps1.2.4.1.3 "><p id="p15355133016272"><a name="p15355133016272"></a><a name="p15355133016272"></a>Indicates the update time in the following format: yyyy-MM-ddTHH:mm:ssZ.</p>
    <p id="p53551930182720"><a name="p53551930182720"></a><a name="p53551930182720"></a><strong id="b10636153418013"><a name="b10636153418013"></a><a name="b10636153418013"></a>T</strong> is the separator between the calendar and the hourly notation of time. <strong id="b15636103419017"><a name="b15636103419017"></a><a name="b15636103419017"></a>Z</strong> indicates the time zone offset.</p>
    </td>
    </tr>
    <tr id="row2355730152716"><td class="cellrowborder" valign="top" width="23.01%" headers="mcps1.2.4.1.1 "><p id="p8355133002719"><a name="p8355133002719"></a><a name="p8355133002719"></a>configuration_parameters</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.3%" headers="mcps1.2.4.1.2 "><p id="p135518306279"><a name="p135518306279"></a><a name="p135518306279"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.690000000000005%" headers="mcps1.2.4.1.3 "><p id="p435512305278"><a name="p435512305278"></a><a name="p435512305278"></a>Indicates the parameters defined by users based on the default parameter templates.</p>
    <p id="p425083010377"><a name="p425083010377"></a><a name="p425083010377"></a>For details, see <a href="#table19183193052719">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  configuration\_parameters field data structure description

    <a name="table19183193052719"></a>
    <table><thead align="left"><tr id="row13355163082719"><th class="cellrowborder" valign="top" width="23.18%" id="mcps1.2.4.1.1"><p id="p1635513305278"><a name="p1635513305278"></a><a name="p1635513305278"></a><strong id="b1578335060"><a name="b1578335060"></a><a name="b1578335060"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.95%" id="mcps1.2.4.1.2"><p id="p635593015275"><a name="p635593015275"></a><a name="p635593015275"></a><strong id="b562952166"><a name="b562952166"></a><a name="b562952166"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.87%" id="mcps1.2.4.1.3"><p id="p13551230172713"><a name="p13551230172713"></a><a name="p13551230172713"></a><strong id="b881355960"><a name="b881355960"></a><a name="b881355960"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row13355530172712"><td class="cellrowborder" valign="top" width="23.18%" headers="mcps1.2.4.1.1 "><p id="p14355123062711"><a name="p14355123062711"></a><a name="p14355123062711"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.95%" headers="mcps1.2.4.1.2 "><p id="p16355123016276"><a name="p16355123016276"></a><a name="p16355123016276"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.87%" headers="mcps1.2.4.1.3 "><p id="p73553306270"><a name="p73553306270"></a><a name="p73553306270"></a>Indicates the parameter name.</p>
    </td>
    </tr>
    <tr id="row135573012271"><td class="cellrowborder" valign="top" width="23.18%" headers="mcps1.2.4.1.1 "><p id="p11355133018273"><a name="p11355133018273"></a><a name="p11355133018273"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.95%" headers="mcps1.2.4.1.2 "><p id="p13355030112715"><a name="p13355030112715"></a><a name="p13355030112715"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.87%" headers="mcps1.2.4.1.3 "><p id="p1135553014273"><a name="p1135553014273"></a><a name="p1135553014273"></a>Indicates the parameter value.</p>
    </td>
    </tr>
    <tr id="row8355203012713"><td class="cellrowborder" valign="top" width="23.18%" headers="mcps1.2.4.1.1 "><p id="p1335583012277"><a name="p1335583012277"></a><a name="p1335583012277"></a>restart_required</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.95%" headers="mcps1.2.4.1.2 "><p id="p103554302274"><a name="p103554302274"></a><a name="p103554302274"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.87%" headers="mcps1.2.4.1.3 "><p id="p335516303270"><a name="p335516303270"></a><a name="p335516303270"></a>Indicates whether a reboot is required.</p>
    <a name="ul1035593019278"></a><a name="ul1035593019278"></a><ul id="ul1035593019278"><li><strong id="b842352706214352_1"><a name="b842352706214352_1"></a><a name="b842352706214352_1"></a>false</strong>: A reboot is not required.</li><li><strong id="b84235270621449_1"><a name="b84235270621449_1"></a><a name="b84235270621449_1"></a>true</strong>: A reboot is required.</li></ul>
    </td>
    </tr>
    <tr id="row237116301277"><td class="cellrowborder" valign="top" width="23.18%" headers="mcps1.2.4.1.1 "><p id="p4371133042719"><a name="p4371133042719"></a><a name="p4371133042719"></a>readonly</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.95%" headers="mcps1.2.4.1.2 "><p id="p73719303277"><a name="p73719303277"></a><a name="p73719303277"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.87%" headers="mcps1.2.4.1.3 "><p id="p1637110308275"><a name="p1637110308275"></a><a name="p1637110308275"></a>Indicates whether the parameter is read-only.</p>
    <a name="ul8371730172718"></a><a name="ul8371730172718"></a><ul id="ul8371730172718"><li><strong id="b1465513757"><a name="b1465513757"></a><a name="b1465513757"></a>false</strong>: The parameter is not read-only.</li><li><strong id="b88350933"><a name="b88350933"></a><a name="b88350933"></a>true</strong>: The parameter is read-only.</li></ul>
    </td>
    </tr>
    <tr id="row93711530122714"><td class="cellrowborder" valign="top" width="23.18%" headers="mcps1.2.4.1.1 "><p id="p537163015278"><a name="p537163015278"></a><a name="p537163015278"></a>value_range</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.95%" headers="mcps1.2.4.1.2 "><p id="p1837112307275"><a name="p1837112307275"></a><a name="p1837112307275"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.87%" headers="mcps1.2.4.1.3 "><p id="p4371103013276"><a name="p4371103013276"></a><a name="p4371103013276"></a>Indicates the parameter value range. If the type is Integer, the value is <strong id="b9300328153312"><a name="b9300328153312"></a><a name="b9300328153312"></a>0</strong> or <strong id="b523003053313"><a name="b523003053313"></a><a name="b523003053313"></a>1</strong>. If the type is Boolean, the value is <strong id="b76791938103315"><a name="b76791938103315"></a><a name="b76791938103315"></a>true</strong> or <strong id="b850694112333"><a name="b850694112333"></a><a name="b850694112333"></a>false</strong>.</p>
    </td>
    </tr>
    <tr id="row1437143042719"><td class="cellrowborder" valign="top" width="23.18%" headers="mcps1.2.4.1.1 "><p id="p5371173042710"><a name="p5371173042710"></a><a name="p5371173042710"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.95%" headers="mcps1.2.4.1.2 "><p id="p143711730172715"><a name="p143711730172715"></a><a name="p143711730172715"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.87%" headers="mcps1.2.4.1.3 "><p id="p18371930192720"><a name="p18371930192720"></a><a name="p18371930192720"></a>Indicates the parameter type, which can be <strong id="b317172548174558"><a name="b317172548174558"></a><a name="b317172548174558"></a>integer</strong>, <strong id="b842352706174612"><a name="b842352706174612"></a><a name="b842352706174612"></a>string</strong>, <strong id="b842352706174617"><a name="b842352706174617"></a><a name="b842352706174617"></a>boolean</strong>, <strong id="b842352706171731"><a name="b842352706171731"></a><a name="b842352706171731"></a>list</strong>, or <strong id="b842352706171734"><a name="b842352706171734"></a><a name="b842352706171734"></a>float</strong>.</p>
    </td>
    </tr>
    <tr id="row103711330162711"><td class="cellrowborder" valign="top" width="23.18%" headers="mcps1.2.4.1.1 "><p id="p17371143022711"><a name="p17371143022711"></a><a name="p17371143022711"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.95%" headers="mcps1.2.4.1.2 "><p id="p1537123019272"><a name="p1537123019272"></a><a name="p1537123019272"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.87%" headers="mcps1.2.4.1.3 "><p id="p8371123082715"><a name="p8371123082715"></a><a name="p8371123082715"></a>Indicates the parameter description.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example normal response

    ```
    {
    	"datastore_version_name": "5.7",
    	"datastore_name": "mysql",
    	"created": "2018-10-11 11:40:44",
    	"updated": "2018-10-11 11:40:44",
    	"configuration_parameters": [{
    		"name": "auto_increment_increment",
    		"value": "1",
    		"restart_required": false,
    		"readonly": false,
    		"value_range": "1-65535",
    		"type": "integer",
    		"description": auto_increment_increment and auto_increment_offset are used for master-to-master replication and to control the operations of the AUTO_INCREMENT column.
    	}]
    }
    ```

-   Abnormal Response

    For details, see  [Abnormal Request Results](abnormal-request-results.md).


## Status Code<a name="section4778540915440"></a>

For details, see  [Status Codes](status-codes.md).

## Error Code<a name="section946032144017"></a>

For details, see  [Error Codes](error-codes.md).

