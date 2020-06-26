# Querying a Specified API Version Information \(Compatible with OpenStack\)<a name="en-us_topic_0057306832"></a>

## Function<a name="se8a5fdb5b69140fd9a6a162a2c946544"></a>

This API is used to query the specified API version.

-   Learn how to  [authorize and authenticate](authentication.md)  this API before using it.
-   Before calling this API, obtain the required  [region and endpoint](https://docs.otc.t-systems.com/en-us/endpoint/index.html).

## URI<a name="s8712952f689e42849bfa7025a8e9c26f"></a>

-   URI format

    PATH: /v1.0

    Method: GET


## Request<a name="sf8445598dc1d4accb1009f668e3f1ecf"></a>

None

## Response<a name="s3f86068037d34985978d5319f962aed1"></a>

-   Normal response

    **Table  1**  Parameter description

    <a name="ta171724895be4537bbe91c6b330ae5ce"></a>
    <table><thead align="left"><tr id="rbedc4fe052c146af934330775aaeba39"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="a42f6eedd33674c2f816859311dff9977"><a name="a42f6eedd33674c2f816859311dff9977"></a><a name="a42f6eedd33674c2f816859311dff9977"></a><strong id="en-us_topic_0032347779_b842352706102328"><a name="en-us_topic_0032347779_b842352706102328"></a><a name="en-us_topic_0032347779_b842352706102328"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="a6afd7a78742d44cf9ae4b267ee6d1684"><a name="a6afd7a78742d44cf9ae4b267ee6d1684"></a><a name="a6afd7a78742d44cf9ae4b267ee6d1684"></a><strong id="en-us_topic_0032347779_b842352706164541"><a name="en-us_topic_0032347779_b842352706164541"></a><a name="en-us_topic_0032347779_b842352706164541"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="a627b20f6558b481cb956f1e9e4066183"><a name="a627b20f6558b481cb956f1e9e4066183"></a><a name="a627b20f6558b481cb956f1e9e4066183"></a><strong id="en-us_topic_0032347779_b842352706163417"><a name="en-us_topic_0032347779_b842352706163417"></a><a name="en-us_topic_0032347779_b842352706163417"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r88496f9018374c7b9e90193348520374"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="a7fdf81619fa246bdbe4a368c7742111d"><a name="a7fdf81619fa246bdbe4a368c7742111d"></a><a name="a7fdf81619fa246bdbe4a368c7742111d"></a>versions</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="a9a9492e05cb648e885d1e747a339d04d"><a name="a9a9492e05cb648e885d1e747a339d04d"></a><a name="a9a9492e05cb648e885d1e747a339d04d"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="a92bad74081154ce6a5337bf766dea530"><a name="a92bad74081154ce6a5337bf766dea530"></a><a name="a92bad74081154ce6a5337bf766dea530"></a>Indicates the list of detailed API version information.</p>
    <p id="p5766192462116"><a name="p5766192462116"></a><a name="p5766192462116"></a>For details, see <a href="#t5963fff962ed43abb7a3e7d46742f177">Table 2</a>.</p>
    </td>
    </tr>
    <tr id="row6705357611756"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p6023687711820"><a name="p6023687711820"></a><a name="p6023687711820"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p5356304153"><a name="p5356304153"></a><a name="p5356304153"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1005360411820"><a name="p1005360411820"></a><a name="p1005360411820"></a>Indicates the list of detailed API version information.</p>
    <p id="p1815410320219"><a name="p1815410320219"></a><a name="p1815410320219"></a>For details, see <a href="#t5963fff962ed43abb7a3e7d46742f177">Table 2</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  versions field data structure description

    <a name="t5963fff962ed43abb7a3e7d46742f177"></a>
    <table><thead align="left"><tr id="re7b458966c154793973d30e4f9484d30"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="aa8a0ea4f858b4e93b0511a227f423769"><a name="aa8a0ea4f858b4e93b0511a227f423769"></a><a name="aa8a0ea4f858b4e93b0511a227f423769"></a><strong id="b24080716"><a name="b24080716"></a><a name="b24080716"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="ae9525ddc0df7401790c8aa3639214182"><a name="ae9525ddc0df7401790c8aa3639214182"></a><a name="ae9525ddc0df7401790c8aa3639214182"></a><strong id="b1008201159"><a name="b1008201159"></a><a name="b1008201159"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="ae06052e3e2b844cca0f51e47f6d620eb"><a name="ae06052e3e2b844cca0f51e47f6d620eb"></a><a name="ae06052e3e2b844cca0f51e47f6d620eb"></a><strong id="b1206444668"><a name="b1206444668"></a><a name="b1206444668"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r94d24e2978694f5dab231414b5052e31"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="a0fa0e6898d284b19846167535fd33e7c"><a name="a0fa0e6898d284b19846167535fd33e7c"></a><a name="a0fa0e6898d284b19846167535fd33e7c"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="a685d2a430e0940c4859474efe2cd23f1"><a name="a685d2a430e0940c4859474efe2cd23f1"></a><a name="a685d2a430e0940c4859474efe2cd23f1"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="a605f505929f7413eab02a91f8967a2e0"><a name="a605f505929f7413eab02a91f8967a2e0"></a><a name="a605f505929f7413eab02a91f8967a2e0"></a>Indicates the API version.</p>
    </td>
    </tr>
    <tr id="row2126108012754"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p16997501285"><a name="p16997501285"></a><a name="p16997501285"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p34620521285"><a name="p34620521285"></a><a name="p34620521285"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p408083281285"><a name="p408083281285"></a><a name="p408083281285"></a>Indicates the API link information.</p>
    <p id="p5314441142117"><a name="p5314441142117"></a><a name="p5314441142117"></a>For details, see <a href="#t39ce8ee145d0420f9b392b8b6897bd15">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="rcd2f361a04d948c5bb73954c6d819774"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="a62c7a1a0e07d4b63b5dd4aae7d190569"><a name="a62c7a1a0e07d4b63b5dd4aae7d190569"></a><a name="a62c7a1a0e07d4b63b5dd4aae7d190569"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="aa8a04dbf0d5d475da26785a1edd0dbf0"><a name="aa8a04dbf0d5d475da26785a1edd0dbf0"></a><a name="aa8a04dbf0d5d475da26785a1edd0dbf0"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="a45f8228ed2054117a2d286fde0d805ce"><a name="a45f8228ed2054117a2d286fde0d805ce"></a><a name="a45f8228ed2054117a2d286fde0d805ce"></a>Indicates the version status.</p>
    </td>
    </tr>
    <tr id="rfbbdb750c08d4b5ca5c305b1cebe308e"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="acb3944d5001d481d9f231aecbdd78616"><a name="acb3944d5001d481d9f231aecbdd78616"></a><a name="acb3944d5001d481d9f231aecbdd78616"></a>updated</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="ae2f32c984c5a4589a151fe2ed0e97b6c"><a name="ae2f32c984c5a4589a151fe2ed0e97b6c"></a><a name="ae2f32c984c5a4589a151fe2ed0e97b6c"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="aaa9a5d99f9e34b0592c5d1dc91350299"><a name="aaa9a5d99f9e34b0592c5d1dc91350299"></a><a name="aaa9a5d99f9e34b0592c5d1dc91350299"></a>Indicates the version update time.</p>
    <p id="a67f4ade5f67b4b00bca133cc7b9d6aa2"><a name="a67f4ade5f67b4b00bca133cc7b9d6aa2"></a><a name="a67f4ade5f67b4b00bca133cc7b9d6aa2"></a>The format is yyyy-mm-dd Thh:mm:ssZ.</p>
    <p id="a36d1013820b94694a2498bb899e76fb7"><a name="a36d1013820b94694a2498bb899e76fb7"></a><a name="a36d1013820b94694a2498bb899e76fb7"></a><strong id="b842352706104536"><a name="b842352706104536"></a><a name="b842352706104536"></a>T</strong> is the separator between the calendar and the hourly notation of time. <strong id="b842352706161738"><a name="b842352706161738"></a><a name="b842352706161738"></a>Z</strong> indicates the UTC.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  links field data structure description

    <a name="t39ce8ee145d0420f9b392b8b6897bd15"></a>
    <table><thead align="left"><tr id="re0d5492ee4c74e7baf0d6835fdb85f6d"><th class="cellrowborder" valign="top" width="26.529999999999998%" id="mcps1.2.4.1.1"><p id="a0d47c1e2eda942fd915f14fe2a95a7fa"><a name="a0d47c1e2eda942fd915f14fe2a95a7fa"></a><a name="a0d47c1e2eda942fd915f14fe2a95a7fa"></a><strong id="b1640135724"><a name="b1640135724"></a><a name="b1640135724"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.800000000000004%" id="mcps1.2.4.1.2"><p id="a644502e4b2514d1c85c0f93b9ac7f289"><a name="a644502e4b2514d1c85c0f93b9ac7f289"></a><a name="a644502e4b2514d1c85c0f93b9ac7f289"></a><strong id="b2021585003"><a name="b2021585003"></a><a name="b2021585003"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.67%" id="mcps1.2.4.1.3"><p id="ae7079a1e380a40afba5a6a5de69eda3a"><a name="ae7079a1e380a40afba5a6a5de69eda3a"></a><a name="ae7079a1e380a40afba5a6a5de69eda3a"></a><strong id="b1000583669"><a name="b1000583669"></a><a name="b1000583669"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r5bc2727ac5744a8e976ee1b2dd7f0b9a"><td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.1 "><p id="a8229f25d830a4e0580e409909894a80b"><a name="a8229f25d830a4e0580e409909894a80b"></a><a name="a8229f25d830a4e0580e409909894a80b"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.2 "><p id="a3f4057e3fea64c19806b893971fcd556"><a name="a3f4057e3fea64c19806b893971fcd556"></a><a name="a3f4057e3fea64c19806b893971fcd556"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.67%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0032347779_p619568715440"><a name="en-us_topic_0032347779_p619568715440"></a><a name="en-us_topic_0032347779_p619568715440"></a>Indicates the API URL and the value is <strong id="b84235270618633"><a name="b84235270618633"></a><a name="b84235270618633"></a>""</strong>.</p>
    </td>
    </tr>
    <tr id="rd4ec13ef5bf046e2891351e0a8e8e7c0"><td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.1 "><p id="abeff09729c074f3f891587452b023b80"><a name="abeff09729c074f3f891587452b023b80"></a><a name="abeff09729c074f3f891587452b023b80"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.2 "><p id="ae412b819da8948cbad262b653caf8f32"><a name="ae412b819da8948cbad262b653caf8f32"></a><a name="ae412b819da8948cbad262b653caf8f32"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.67%" headers="mcps1.2.4.1.3 "><p id="aadccb003a11348fdbbe3243d439df7db"><a name="aadccb003a11348fdbbe3243d439df7db"></a><a name="aadccb003a11348fdbbe3243d439df7db"></a>Its value is <strong id="b84235270616818"><a name="b84235270616818"></a><a name="b84235270616818"></a>self</strong>, indicating that <strong id="b84235270616856"><a name="b84235270616856"></a><a name="b84235270616856"></a>href</strong> is a local link.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example normal response

    ```
    {
    	"version": {
    		"id": "v1.0",
    		"links": [{
    			"href": "",
    			"rel": "self"
    		}],
    		"status": "CURRENT",
    		"updated": "2017-03-23T17:34:02Z"
    	},
    	"versions": {
    		"id": "v1.0",
    		"links": [{
    			"href": "",
    			"rel": "self"
    		}],
    		"status": "CURRENT",
    		"updated": "2017-03-23T17:34:02Z"
    	}
    }
    ```

-   Abnormal response

    For details, see  [Abnormal Request Results](abnormal-request-results.md).


## Status Code<a name="section4778540915440"></a>

For details, see  [Status Codes](status-codes.md).

## Error Code<a name="section946032144017"></a>

For details, see  [Error Codes](error-codes.md).

