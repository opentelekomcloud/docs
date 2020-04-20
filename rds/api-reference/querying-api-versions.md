# Querying API Versions<a name="en-us_topic_0032347778"></a>

## Function<a name="section9793815440"></a>

This API is used to query the currently supported RDS API versions.

-   Learn how to  [authorize and authenticate](authentication.md)  this API before using it.
-   Before calling this API, obtain the required  [region and endpoint](https://docs.otc.t-systems.com/en-us/endpoint/index.html).

## URI<a name="section428804115440"></a>

-   URI format

    GET https://\{_Endpoint_\}/rds/

-   Example

    https://rds.eu-de.otc.t-systems.com/rds/

-   Parameter description

    None


## Request<a name="section2907369315440"></a>

None

## Response<a name="section5543006115440"></a>

-   Normal response

    **Table  1**  Parameter description

    <a name="table3575976715440"></a>
    <table><thead align="left"><tr id="row5028223115440"><th class="cellrowborder" valign="top" width="26.26262626262626%" id="mcps1.2.4.1.1"><p id="p4632888215440"><a name="p4632888215440"></a><a name="p4632888215440"></a><strong id="b842352706102328_3"><a name="b842352706102328_3"></a><a name="b842352706102328_3"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="40.40404040404041%" id="mcps1.2.4.1.2"><p id="p6165196615440"><a name="p6165196615440"></a><a name="p6165196615440"></a><strong id="b842352706164541_1"><a name="b842352706164541_1"></a><a name="b842352706164541_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p2775334615440"><a name="p2775334615440"></a><a name="p2775334615440"></a><strong id="b842352706163417_3"><a name="b842352706163417_3"></a><a name="b842352706163417_3"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3342858315440"><td class="cellrowborder" valign="top" width="26.26262626262626%" headers="mcps1.2.4.1.1 "><p id="p2336072515440"><a name="p2336072515440"></a><a name="p2336072515440"></a>versions</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.40404040404041%" headers="mcps1.2.4.1.2 "><p id="p49221130121216"><a name="p49221130121216"></a><a name="p49221130121216"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p476126915440"><a name="p476126915440"></a><a name="p476126915440"></a>Indicates the list of detailed API version information.</p>
    <p id="p877352874313"><a name="p877352874313"></a><a name="p877352874313"></a>For details, see <a href="#table37479565104653">Table 2</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  versions field data structure description

    <a name="table37479565104653"></a>
    <table><thead align="left"><tr id="row65790814104653"><th class="cellrowborder" valign="top" width="26.529999999999998%" id="mcps1.2.4.1.1"><p id="p27455703104653"><a name="p27455703104653"></a><a name="p27455703104653"></a><strong id="b842352706102328_5"><a name="b842352706102328_5"></a><a name="b842352706102328_5"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="40.23%" id="mcps1.2.4.1.2"><p id="p9319469104653"><a name="p9319469104653"></a><a name="p9319469104653"></a><strong id="b842352706164541_3"><a name="b842352706164541_3"></a><a name="b842352706164541_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.239999999999995%" id="mcps1.2.4.1.3"><p id="p16679495104653"><a name="p16679495104653"></a><a name="p16679495104653"></a><strong id="b842352706163417_5"><a name="b842352706163417_5"></a><a name="b842352706163417_5"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8861837104653"><td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p46720233104653"><a name="p46720233104653"></a><a name="p46720233104653"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.23%" headers="mcps1.2.4.1.2 "><p id="p26242496104653"><a name="p26242496104653"></a><a name="p26242496104653"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.239999999999995%" headers="mcps1.2.4.1.3 "><p id="p45267452104653"><a name="p45267452104653"></a><a name="p45267452104653"></a>Indicates the API version.</p>
    <a name="ul1725315498237"></a><a name="ul1725315498237"></a><ul id="ul1725315498237"><li><strong id="b192361814298"><a name="b192361814298"></a><a name="b192361814298"></a>v1</strong>: indicates the API v1 version.</li><li><strong id="b11223411142919"><a name="b11223411142919"></a><a name="b11223411142919"></a>v1.0</strong>: indicates the OpenStack trove API v1.0.</li><li><strong id="b172244408114"><a name="b172244408114"></a><a name="b172244408114"></a>v3</strong>: indicates the API v3 version.</li></ul>
    </td>
    </tr>
    <tr id="row1548795912115"><td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p26342211121111"><a name="p26342211121111"></a><a name="p26342211121111"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.23%" headers="mcps1.2.4.1.2 "><p id="p1329784718535"><a name="p1329784718535"></a><a name="p1329784718535"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.239999999999995%" headers="mcps1.2.4.1.3 "><p id="p31978734121111"><a name="p31978734121111"></a><a name="p31978734121111"></a>Indicates the API link information. The value is empty when the version is <strong id="b84235270615454"><a name="b84235270615454"></a><a name="b84235270615454"></a>v1</strong> or <strong id="b8551221142314"><a name="b8551221142314"></a><a name="b8551221142314"></a>v3</strong>.</p>
    <p id="p3549257124214"><a name="p3549257124214"></a><a name="p3549257124214"></a>For details, see <a href="#table630875915440">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="row4753892104653"><td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p49520946104653"><a name="p49520946104653"></a><a name="p49520946104653"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.23%" headers="mcps1.2.4.1.2 "><p id="p51773656104653"><a name="p51773656104653"></a><a name="p51773656104653"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.239999999999995%" headers="mcps1.2.4.1.3 "><p id="p32916607104653"><a name="p32916607104653"></a><a name="p32916607104653"></a>Indicates the version status.</p>
    <p id="p1880593015412"><a name="p1880593015412"></a><a name="p1880593015412"></a><strong id="b12381327195914"><a name="b12381327195914"></a><a name="b12381327195914"></a>CURRENT</strong>: indicates that the version is recommended.</p>
    <p id="p10804162614411"><a name="p10804162614411"></a><a name="p10804162614411"></a><strong id="b84235270619220"><a name="b84235270619220"></a><a name="b84235270619220"></a>DEPRECATED</strong>: indicates a deprecated version which may be deleted later.</p>
    </td>
    </tr>
    <tr id="row27814010104653"><td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p38342341104653"><a name="p38342341104653"></a><a name="p38342341104653"></a>updated</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.23%" headers="mcps1.2.4.1.2 "><p id="p18721892104653"><a name="p18721892104653"></a><a name="p18721892104653"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.239999999999995%" headers="mcps1.2.4.1.3 "><p id="p40078272104653"><a name="p40078272104653"></a><a name="p40078272104653"></a>Indicates the version update time.</p>
    <p id="p25160128104653"><a name="p25160128104653"></a><a name="p25160128104653"></a>The format is yyyy-mm-dd Thh:mm:ssZ.</p>
    <p id="p25114560104653"><a name="p25114560104653"></a><a name="p25114560104653"></a><strong id="b842352706104536"><a name="b842352706104536"></a><a name="b842352706104536"></a>T</strong> is the separator between the calendar and the hourly notation of time. <strong id="b842352706161738"><a name="b842352706161738"></a><a name="b842352706161738"></a>Z</strong> indicates the Coordinated Universal Time (UTC).</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  links field data structure description \(dedicated for OpenStack v1.0\)

    <a name="table630875915440"></a>
    <table><thead align="left"><tr id="row4191288815440"><th class="cellrowborder" valign="top" width="26.529999999999998%" id="mcps1.2.4.1.1"><p id="p3950073415440"><a name="p3950073415440"></a><a name="p3950073415440"></a><strong id="b842352706102328_7"><a name="b842352706102328_7"></a><a name="b842352706102328_7"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.800000000000004%" id="mcps1.2.4.1.2"><p id="p4544288515440"><a name="p4544288515440"></a><a name="p4544288515440"></a><strong id="b842352706164541_5"><a name="b842352706164541_5"></a><a name="b842352706164541_5"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.67%" id="mcps1.2.4.1.3"><p id="p5699506015440"><a name="p5699506015440"></a><a name="p5699506015440"></a><strong id="b842352706163417_7"><a name="b842352706163417_7"></a><a name="b842352706163417_7"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5319717215440"><td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p1400369315440"><a name="p1400369315440"></a><a name="p1400369315440"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.2 "><p id="p6055731815440"><a name="p6055731815440"></a><a name="p6055731815440"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.67%" headers="mcps1.2.4.1.3 "><p id="p619568715440"><a name="p619568715440"></a><a name="p619568715440"></a>Indicates the API URL and the value is <strong id="b84235270618633"><a name="b84235270618633"></a><a name="b84235270618633"></a>""</strong>.</p>
    </td>
    </tr>
    <tr id="row5576118615440"><td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p2036224315440"><a name="p2036224315440"></a><a name="p2036224315440"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.2 "><p id="p3872902515440"><a name="p3872902515440"></a><a name="p3872902515440"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.67%" headers="mcps1.2.4.1.3 "><p id="p5004333115440"><a name="p5004333115440"></a><a name="p5004333115440"></a>Its value is <strong id="b84235270616818"><a name="b84235270616818"></a><a name="b84235270616818"></a>self</strong>, indicating that <strong id="b84235270616856"><a name="b84235270616856"></a><a name="b84235270616856"></a>href</strong> is a local link.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example normal response

    ```
    {
    	"versions": [{
    		"id": "v1",
    		"links": [],
    		"status": "CURRENT",
    		"updated": "2017-02-07T17:34:02Z"
    	}, {
    		"id": "v1.0",
    		"links": [{
    			"href": "",
    			"rel": "self"
    		}],
    		"status": "CURRENT",
    		"updated": "2017-03-23T17:34:02Z"
    	}, {
    		"id": "v3",
    		"links": [],
    		"status": "CURRENT",
    		"updated": "2019-01-15T12:00:00Z"
    	}]
    }
    ```

-   Abnormal response

    For details, see  [Abnormal Request Results](abnormal-request-results.md).


## Status Code<a name="section4778540915440"></a>

For details, see  [Status Codes](status-codes.md).

## Error Code<a name="section946032144017"></a>

For details, see  [Error Codes](error-codes.md).

