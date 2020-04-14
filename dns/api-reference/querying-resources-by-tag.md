# Querying Resources by Tag<a name="dns_api_67006"></a>

## Function<a name="scc94830eea9a47fa9c81380d5748b11b"></a>

Query DNS resources by tag.

Resources are sorted by creation time in descending order.

## URI<a name="sbb832340100d47c5b826259ab61954a9"></a>

POST /v2/\{project\_id\}/\{resource\_type\}/resource\_instances/action

For details, see  [Table 1](#ta232abacc5c94e828ce60c58a8982bee).

**Table  1**  Parameters in the URI

<a name="ta232abacc5c94e828ce60c58a8982bee"></a>
<table><thead align="left"><tr id="r4414011e2d0f47f99d4a85508602edc6"><th class="cellrowborder" valign="top" width="22.64%" id="mcps1.2.5.1.1"><p id="a27f14d476f204411830ab21a16fd20d8"><a name="a27f14d476f204411830ab21a16fd20d8"></a><a name="a27f14d476f204411830ab21a16fd20d8"></a><strong>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.37%" id="mcps1.2.5.1.2"><p id="a6687030089db4cd887e398798fd31df4"><a name="a6687030089db4cd887e398798fd31df4"></a><a name="a6687030089db4cd887e398798fd31df4"></a><strong>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.349999999999998%" id="mcps1.2.5.1.3"><p id="aa7d84d0067f6473bb09dd153ef5125f9"><a name="aa7d84d0067f6473bb09dd153ef5125f9"></a><a name="aa7d84d0067f6473bb09dd153ef5125f9"></a><strong>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="42.64%" id="mcps1.2.5.1.4"><p id="a4b5b9c81830d44c0ad4c491efc147701"><a name="a4b5b9c81830d44c0ad4c491efc147701"></a><a name="a4b5b9c81830d44c0ad4c491efc147701"></a><strong>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r87f3b0e3d5e34645a6a72c8295a60dd1"><td class="cellrowborder" valign="top" width="22.64%" headers="mcps1.2.5.1.1 "><p id="a02bd4a996c2247aaaf70785d641ea99b"><a name="a02bd4a996c2247aaaf70785d641ea99b"></a><a name="a02bd4a996c2247aaaf70785d641ea99b"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.37%" headers="mcps1.2.5.1.2 "><p id="a36e39cee57d342b494172182623f150f"><a name="a36e39cee57d342b494172182623f150f"></a><a name="a36e39cee57d342b494172182623f150f"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.5.1.3 "><p id="a5f56142551544aff8f99a8519c45e8c5"><a name="a5f56142551544aff8f99a8519c45e8c5"></a><a name="a5f56142551544aff8f99a8519c45e8c5"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.64%" headers="mcps1.2.5.1.4 "><p id="af2be59fc13474cdbb11ea3ce65ad1dfa"><a name="af2be59fc13474cdbb11ea3ce65ad1dfa"></a><a name="af2be59fc13474cdbb11ea3ce65ad1dfa"></a>Project ID. You can obtain it in <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
</td>
</tr>
<tr id="rf27add3e7a944b14819763911f5fde7c"><td class="cellrowborder" valign="top" width="22.64%" headers="mcps1.2.5.1.1 "><p id="a05d15e734e994570a07d9814f4d5d594"><a name="a05d15e734e994570a07d9814f4d5d594"></a><a name="a05d15e734e994570a07d9814f4d5d594"></a>resource_type</p>
</td>
<td class="cellrowborder" valign="top" width="17.37%" headers="mcps1.2.5.1.2 "><p id="a64a15d111ae74078a66bf54abcf4c9ff"><a name="a64a15d111ae74078a66bf54abcf4c9ff"></a><a name="a64a15d111ae74078a66bf54abcf4c9ff"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.5.1.3 "><p id="af8f958157b664e299ef1e1afcf441a9c"><a name="af8f958157b664e299ef1e1afcf441a9c"></a><a name="af8f958157b664e299ef1e1afcf441a9c"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.64%" headers="mcps1.2.5.1.4 "><p id="a61960b908f644177b46c8ddc6c95c941"><a name="a61960b908f644177b46c8ddc6c95c941"></a><a name="a61960b908f644177b46c8ddc6c95c941"></a>Resource type, which can be <strong>DNS-public_zone</strong>, <strong>DNS-private_zone</strong>, <strong>DNS-public_recordset</strong>, <strong>DNS-private_recordset</strong>, or <strong>DNS-ptr_record</strong></p>
</td>
</tr>
</tbody>
</table>

## Request<a name="s1f778fe858bc44ffbb2aa37ffaa1e116"></a>

-   Parameter description

    **Table  2**  Parameters in the request

    <a name="tb06f4f4b35c94f68b3bca7c2155e0126"></a>
    <table><thead align="left"><tr id="r870f3c315b9048009d9896b5ea970423"><th class="cellrowborder" valign="top" width="19.8%" id="mcps1.2.5.1.1"><p id="a9be1225ebd6445aaa71d7de2258c3744"><a name="a9be1225ebd6445aaa71d7de2258c3744"></a><a name="a9be1225ebd6445aaa71d7de2258c3744"></a><strong>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="13.5%" id="mcps1.2.5.1.2"><p id="af809a931c8c64f2ab0c1481b0c0ae061"><a name="af809a931c8c64f2ab0c1481b0c0ae061"></a><a name="af809a931c8c64f2ab0c1481b0c0ae061"></a><strong>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.8%" id="mcps1.2.5.1.3"><p id="a2dbf8296ade74459b85d45db216c4290"><a name="a2dbf8296ade74459b85d45db216c4290"></a><a name="a2dbf8296ade74459b85d45db216c4290"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="48.9%" id="mcps1.2.5.1.4"><p id="acf61e6cae8b64132874080f05a52d7ef"><a name="acf61e6cae8b64132874080f05a52d7ef"></a><a name="acf61e6cae8b64132874080f05a52d7ef"></a><strong>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r5cf51c052eac4be485c8ca05721c7a1a"><td class="cellrowborder" valign="top" width="19.8%" headers="mcps1.2.5.1.1 "><p id="a474dc55159124b3e9c370011fa217463"><a name="a474dc55159124b3e9c370011fa217463"></a><a name="a474dc55159124b3e9c370011fa217463"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.5%" headers="mcps1.2.5.1.2 "><p id="af717102a783f455bb2308a292537fcae"><a name="af717102a783f455bb2308a292537fcae"></a><a name="af717102a783f455bb2308a292537fcae"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.8%" headers="mcps1.2.5.1.3 "><p id="p196721612141417"><a name="p196721612141417"></a><a name="p196721612141417"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.9%" headers="mcps1.2.5.1.4 "><p id="a3ffd26e94c7945a58a31cdda3fd6fb99"><a name="a3ffd26e94c7945a58a31cdda3fd6fb99"></a><a name="a3ffd26e94c7945a58a31cdda3fd6fb99"></a>Includes specified tags. For details, see <a href="#tb2c210e5c1f44fad9eaeb485e2da1424">Table 3</a>.</p>
    <p id="aa761ae649fd444f2a93cb44a0a9ade9b"><a name="aa761ae649fd444f2a93cb44a0a9ade9b"></a><a name="aa761ae649fd444f2a93cb44a0a9ade9b"></a>The structure body is mandatory. A maximum of 10 tag keys are allowed in each query operation. The tag key cannot be left blank or set to the empty string. One tag key can have up to 10 tag values. Each tag key must be unique, and the tag values of one key must also be unique.</p>
    </td>
    </tr>
    <tr id="r99a6a134768b4fe0a9a39f5937d5d3b5"><td class="cellrowborder" valign="top" width="19.8%" headers="mcps1.2.5.1.1 "><p id="a35bc80ef6a00468abb7cf4f22933ff64"><a name="a35bc80ef6a00468abb7cf4f22933ff64"></a><a name="a35bc80ef6a00468abb7cf4f22933ff64"></a>tags_any</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.5%" headers="mcps1.2.5.1.2 "><p id="ab5ab6ef6efef4386a4afb899282d3092"><a name="ab5ab6ef6efef4386a4afb899282d3092"></a><a name="ab5ab6ef6efef4386a4afb899282d3092"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.8%" headers="mcps1.2.5.1.3 "><p id="p816310154149"><a name="p816310154149"></a><a name="p816310154149"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.9%" headers="mcps1.2.5.1.4 "><p id="a26c27c508b6448ff8eb40cb4c639020c"><a name="a26c27c508b6448ff8eb40cb4c639020c"></a><a name="a26c27c508b6448ff8eb40cb4c639020c"></a>Includes any of the specified tags. For details, see <a href="#tb2c210e5c1f44fad9eaeb485e2da1424">Table 3</a>.</p>
    <p id="ab8a16d2d15ac44409e5cef21c0beb7a1"><a name="ab8a16d2d15ac44409e5cef21c0beb7a1"></a><a name="ab8a16d2d15ac44409e5cef21c0beb7a1"></a>The structure body is mandatory. A maximum of 10 tag keys are allowed in each query operation. The tag key cannot be left blank or set to the empty string. One tag key can have up to 10 tag values. Each tag key must be unique, and the tag values of one key must also be unique.</p>
    </td>
    </tr>
    <tr id="r312274f5bc614453b9f0182d8c1b8f31"><td class="cellrowborder" valign="top" width="19.8%" headers="mcps1.2.5.1.1 "><p id="a2badc302985c4a07a39675214a576f03"><a name="a2badc302985c4a07a39675214a576f03"></a><a name="a2badc302985c4a07a39675214a576f03"></a>not_tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.5%" headers="mcps1.2.5.1.2 "><p id="ae7560f3d42a241fe87b9268730d86d98"><a name="ae7560f3d42a241fe87b9268730d86d98"></a><a name="ae7560f3d42a241fe87b9268730d86d98"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.8%" headers="mcps1.2.5.1.3 "><p id="a77db840a97da4e81a507b151141b1936"><a name="a77db840a97da4e81a507b151141b1936"></a><a name="a77db840a97da4e81a507b151141b1936"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.9%" headers="mcps1.2.5.1.4 "><p id="ac3ecce5080bd46b791eb9ea33219f13c"><a name="ac3ecce5080bd46b791eb9ea33219f13c"></a><a name="ac3ecce5080bd46b791eb9ea33219f13c"></a>Excludes specified tags. For details, see <a href="#tb2c210e5c1f44fad9eaeb485e2da1424">Table 3</a>.</p>
    <p id="p1486152918114"><a name="p1486152918114"></a><a name="p1486152918114"></a>The structure body is mandatory. A maximum of 10 tag keys are allowed in each query operation. The tag key cannot be left blank or set to the empty string. One tag key can have up to 10 tag values. Each tag key must be unique, and the tag values of one key must also be unique.</p>
    </td>
    </tr>
    <tr id="rcb4c18c8024344d48deadb3c1ceea94b"><td class="cellrowborder" valign="top" width="19.8%" headers="mcps1.2.5.1.1 "><p id="adfaaffce4eae4829a5f32a14eebe4176"><a name="adfaaffce4eae4829a5f32a14eebe4176"></a><a name="adfaaffce4eae4829a5f32a14eebe4176"></a>not_tags_any</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.5%" headers="mcps1.2.5.1.2 "><p id="a4b071b97ef9742fab53e7e392b3bf2bc"><a name="a4b071b97ef9742fab53e7e392b3bf2bc"></a><a name="a4b071b97ef9742fab53e7e392b3bf2bc"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.8%" headers="mcps1.2.5.1.3 "><p id="p0311732161411"><a name="p0311732161411"></a><a name="p0311732161411"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.9%" headers="mcps1.2.5.1.4 "><p id="ac4670404f0884590b2c25f855c7949a7"><a name="ac4670404f0884590b2c25f855c7949a7"></a><a name="ac4670404f0884590b2c25f855c7949a7"></a>Excludes any of the specified tags. For details, see <a href="#tb2c210e5c1f44fad9eaeb485e2da1424">Table 3</a>.</p>
    <p id="p146827567125"><a name="p146827567125"></a><a name="p146827567125"></a>The structure body is mandatory. A maximum of 10 tag keys are allowed in each query operation. The tag key cannot be left blank or set to the empty string. One tag key can have up to 10 tag values. Each tag key must be unique, and the tag values of one key must also be unique.</p>
    </td>
    </tr>
    <tr id="rf2bfc3c71b6b4c82a44ea2a48d974822"><td class="cellrowborder" valign="top" width="19.8%" headers="mcps1.2.5.1.1 "><p id="aea1a32690372433c97dc2a6d7a4cc1a3"><a name="aea1a32690372433c97dc2a6d7a4cc1a3"></a><a name="aea1a32690372433c97dc2a6d7a4cc1a3"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.5%" headers="mcps1.2.5.1.2 "><p id="a1de307db033e47e5831bb8e73262f1c9"><a name="a1de307db033e47e5831bb8e73262f1c9"></a><a name="a1de307db033e47e5831bb8e73262f1c9"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.8%" headers="mcps1.2.5.1.3 "><p id="a223ade7619e34423a6096e2315ce79c1"><a name="a223ade7619e34423a6096e2315ce79c1"></a><a name="a223ade7619e34423a6096e2315ce79c1"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.9%" headers="mcps1.2.5.1.4 "><p id="p230120311413"><a name="p230120311413"></a><a name="p230120311413"></a>Number of resources on each page</p>
    <p id="p147131447514"><a name="p147131447514"></a><a name="p147131447514"></a>The value range is 1–1000.</p>
    <a name="ul32433360317"></a><a name="ul32433360317"></a><ul id="ul32433360317"><li>If the value of <strong id="b84235270692122"><a name="b84235270692122"></a><a name="b84235270692122"></a>action</strong> is set to <strong id="b84235270692134"><a name="b84235270692134"></a><a name="b84235270692134"></a>filter</strong>, the default value is <strong id="b19626194614914"><a name="b19626194614914"></a><a name="b19626194614914"></a>1000</strong>.</li><li>If <strong id="b842352706152943"><a name="b842352706152943"></a><a name="b842352706152943"></a>action</strong> is set to <strong id="b842352706152951"><a name="b842352706152951"></a><a name="b842352706152951"></a>count</strong>, this parameter does not take effect.</li></ul>
    </td>
    </tr>
    <tr id="r09054f0ce9c8438698d0b7928d5977a1"><td class="cellrowborder" valign="top" width="19.8%" headers="mcps1.2.5.1.1 "><p id="acfe40660f4704831845244f5d21e1e3d"><a name="acfe40660f4704831845244f5d21e1e3d"></a><a name="acfe40660f4704831845244f5d21e1e3d"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.5%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0123490185_p765135818031"><a name="en-us_topic_0123490185_p765135818031"></a><a name="en-us_topic_0123490185_p765135818031"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.8%" headers="mcps1.2.5.1.3 "><p id="aa94f9be6b0034b5b8df645c4a99c0970"><a name="aa94f9be6b0034b5b8df645c4a99c0970"></a><a name="aa94f9be6b0034b5b8df645c4a99c0970"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.9%" headers="mcps1.2.5.1.4 "><p id="p35951433204916"><a name="p35951433204916"></a><a name="p35951433204916"></a>Start offset of pagination query. The query will start from the next resource of the offset value.</p>
    <p id="p18898143914915"><a name="p18898143914915"></a><a name="p18898143914915"></a>Value range: 0–2147483647</p>
    <p id="p13209172234718"><a name="p13209172234718"></a><a name="p13209172234718"></a>The default value is 0.</p>
    <a name="ul7272852175312"></a><a name="ul7272852175312"></a><ul id="ul7272852175312"><li>You do not need to specify this parameter when querying resources on the first page.</li><li>When you query resources on subsequent pages, set the value of <strong id="b842352706101324"><a name="b842352706101324"></a><a name="b842352706101324"></a>offset</strong> to the location returned in the response body for the previous query.</li><li>If <strong id="b84235270692726"><a name="b84235270692726"></a><a name="b84235270692726"></a>action</strong> is set to <strong id="b84235270692731"><a name="b84235270692731"></a><a name="b84235270692731"></a>filter</strong>, this parameter takes effect. Its value can be 0 (default) or a positive integer.</li><li>If <strong id="b443215778"><a name="b443215778"></a><a name="b443215778"></a>action</strong> is set to <strong id="b1792365062"><a name="b1792365062"></a><a name="b1792365062"></a>count</strong>, this parameter does not take effect.</li></ul>
    </td>
    </tr>
    <tr id="r419264becf14466cabd9b38178560e63"><td class="cellrowborder" valign="top" width="19.8%" headers="mcps1.2.5.1.1 "><p id="a97d276945fbd43bdb98d2f7f17e54a33"><a name="a97d276945fbd43bdb98d2f7f17e54a33"></a><a name="a97d276945fbd43bdb98d2f7f17e54a33"></a>action</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.5%" headers="mcps1.2.5.1.2 "><p id="a84511b82712044bca5f56780d91970ff"><a name="a84511b82712044bca5f56780d91970ff"></a><a name="a84511b82712044bca5f56780d91970ff"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.8%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0123490185_p119142418031"><a name="en-us_topic_0123490185_p119142418031"></a><a name="en-us_topic_0123490185_p119142418031"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.9%" headers="mcps1.2.5.1.4 "><p id="aad7e6106827a43a1858dafe53b83e22d"><a name="aad7e6106827a43a1858dafe53b83e22d"></a><a name="aad7e6106827a43a1858dafe53b83e22d"></a>Operation to be performed</p>
    <p id="a2b9a1fecc8b14740bd6a0220d62500c8"><a name="a2b9a1fecc8b14740bd6a0220d62500c8"></a><a name="a2b9a1fecc8b14740bd6a0220d62500c8"></a>The value can be:</p>
    <a name="ul1240981910525"></a><a name="ul1240981910525"></a><ul id="ul1240981910525"><li><strong id="b842352706103947"><a name="b842352706103947"></a><a name="b842352706103947"></a>filter</strong>: queries resources in pages by filter condition.</li><li><strong id="b842352706104030"><a name="b842352706104030"></a><a name="b842352706104030"></a>count</strong>: queries the total number of resources.</li></ul>
    </td>
    </tr>
    <tr id="rd44a180697704df2a49a4d373c3078e2"><td class="cellrowborder" valign="top" width="19.8%" headers="mcps1.2.5.1.1 "><p id="a7f8cb0b76cb54a3385cb12f2a06491ba"><a name="a7f8cb0b76cb54a3385cb12f2a06491ba"></a><a name="a7f8cb0b76cb54a3385cb12f2a06491ba"></a>matches</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.5%" headers="mcps1.2.5.1.2 "><p id="a3750d26fc2b6422d99b537ae889d4b17"><a name="a3750d26fc2b6422d99b537ae889d4b17"></a><a name="a3750d26fc2b6422d99b537ae889d4b17"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.8%" headers="mcps1.2.5.1.3 "><p id="p168091539101416"><a name="p168091539101416"></a><a name="p168091539101416"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.9%" headers="mcps1.2.5.1.4 "><p id="abe290bcf898740e2ad76c48d098c6cb8"><a name="abe290bcf898740e2ad76c48d098c6cb8"></a><a name="abe290bcf898740e2ad76c48d098c6cb8"></a>Field to be matched. For details, see <a href="#tddefa9c37bda4fab97a689a2dcf0ac0e">Table 4</a>.</p>
    <p id="a7c20b93547bb4bc29f22d3c79a4d0710"><a name="a7c20b93547bb4bc29f22d3c79a4d0710"></a><a name="a7c20b93547bb4bc29f22d3c79a4d0710"></a>This parameter specifies the key-value pair to be matched in the query.</p>
    <p id="a3760f1bfd4e44db88d21728a4357e51e"><a name="a3760f1bfd4e44db88d21728a4357e51e"></a><a name="a3760f1bfd4e44db88d21728a4357e51e"></a>If <strong id="b84235270610160"><a name="b84235270610160"></a><a name="b84235270610160"></a>value</strong> is left blank, an exact match is performed. Otherwise, a fuzzy match is performed.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Parameters in the  **tags**  field

    <a name="tb2c210e5c1f44fad9eaeb485e2da1424"></a>
    <table><thead align="left"><tr id="r75bc9d909ae3472a9c7a3f44d4b7f8f8"><th class="cellrowborder" valign="top" width="19.54%" id="mcps1.2.5.1.1"><p id="ad966754362394a4ca7e94700a01114e9"><a name="ad966754362394a4ca7e94700a01114e9"></a><a name="ad966754362394a4ca7e94700a01114e9"></a><strong>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15.590000000000002%" id="mcps1.2.5.1.2"><p id="afbb54878c81348ab812caa43db1ad751"><a name="afbb54878c81348ab812caa43db1ad751"></a><a name="afbb54878c81348ab812caa43db1ad751"></a><strong>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.9%" id="mcps1.2.5.1.3"><p id="a34d95cfd430f4172b8e5252a83616aab"><a name="a34d95cfd430f4172b8e5252a83616aab"></a><a name="a34d95cfd430f4172b8e5252a83616aab"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="45.97%" id="mcps1.2.5.1.4"><p id="a61526b5c1b1243e9923524b8c4060e92"><a name="a61526b5c1b1243e9923524b8c4060e92"></a><a name="a61526b5c1b1243e9923524b8c4060e92"></a><strong>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="raa8d7d3e734e4b939b7224d3497582f0"><td class="cellrowborder" valign="top" width="19.54%" headers="mcps1.2.5.1.1 "><p id="a296adc25efe24b5ca1a179ceda99bca4"><a name="a296adc25efe24b5ca1a179ceda99bca4"></a><a name="a296adc25efe24b5ca1a179ceda99bca4"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.590000000000002%" headers="mcps1.2.5.1.2 "><p id="a30ae6511738a4ca3abd8fe5137773aba"><a name="a30ae6511738a4ca3abd8fe5137773aba"></a><a name="a30ae6511738a4ca3abd8fe5137773aba"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.9%" headers="mcps1.2.5.1.3 "><p id="aec1d4df913254d11937a55779eb2b3fe"><a name="aec1d4df913254d11937a55779eb2b3fe"></a><a name="aec1d4df913254d11937a55779eb2b3fe"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.97%" headers="mcps1.2.5.1.4 "><p id="a9fc8983744854c459f9d89f0fb75ba76"><a name="a9fc8983744854c459f9d89f0fb75ba76"></a><a name="a9fc8983744854c459f9d89f0fb75ba76"></a>Tag key. A key contains 127 Unicode characters and cannot be blank. (This parameter is not verified in the search process.)</p>
    </td>
    </tr>
    <tr id="r8ad1636f73434dda92c87d3693fef1c5"><td class="cellrowborder" valign="top" width="19.54%" headers="mcps1.2.5.1.1 "><p id="aae08144e8a3342a48e279cd4f4137be7"><a name="aae08144e8a3342a48e279cd4f4137be7"></a><a name="aae08144e8a3342a48e279cd4f4137be7"></a>values</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.590000000000002%" headers="mcps1.2.5.1.2 "><p id="ac9fa5e936d0c4535b20ee342ea0ac906"><a name="ac9fa5e936d0c4535b20ee342ea0ac906"></a><a name="ac9fa5e936d0c4535b20ee342ea0ac906"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.9%" headers="mcps1.2.5.1.3 "><p id="p188882535148"><a name="p188882535148"></a><a name="p188882535148"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.97%" headers="mcps1.2.5.1.4 "><p id="a42c53b30ce50457e999e286d86a7268b"><a name="a42c53b30ce50457e999e286d86a7268b"></a><a name="a42c53b30ce50457e999e286d86a7268b"></a>Values of the tag.</p>
    <p id="ad36b2b1a449f4f66a898a59c9ea4ca9a"><a name="ad36b2b1a449f4f66a898a59c9ea4ca9a"></a><a name="ad36b2b1a449f4f66a898a59c9ea4ca9a"></a>A value contains a maximum of 255 Unicode characters.</p>
    <p id="ac2f20f96c50245928e2a48e29bff1b18"><a name="ac2f20f96c50245928e2a48e29bff1b18"></a><a name="ac2f20f96c50245928e2a48e29bff1b18"></a>The asterisk (*) is a reserved character.</p>
    <p id="ae001ea87f71c45918b92a6b18937abf2"><a name="ae001ea87f71c45918b92a6b18937abf2"></a><a name="ae001ea87f71c45918b92a6b18937abf2"></a>If the value starts with an asterisk (*), the string following the asterisk is fuzzy matched.</p>
    <p id="ab4462955b3ee4cfd98e9a32c55b42432"><a name="ab4462955b3ee4cfd98e9a32c55b42432"></a><a name="ab4462955b3ee4cfd98e9a32c55b42432"></a>If this parameter is not specified, any value is matched. The values are in OR relationship.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  Parameters in the  **matches**  field

    <a name="tddefa9c37bda4fab97a689a2dcf0ac0e"></a>
    <table><thead align="left"><tr id="r7077b0e28dbe4174a5cc6473e28bcfb2"><th class="cellrowborder" valign="top" width="19.73%" id="mcps1.2.5.1.1"><p id="en-us_topic_0123490185_p2130318031"><a name="en-us_topic_0123490185_p2130318031"></a><a name="en-us_topic_0123490185_p2130318031"></a><strong>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15.4%" id="mcps1.2.5.1.2"><p id="en-us_topic_0123490185_p172557318031"><a name="en-us_topic_0123490185_p172557318031"></a><a name="en-us_topic_0123490185_p172557318031"></a><strong>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.9%" id="mcps1.2.5.1.3"><p id="en-us_topic_0123490185_p555372818031"><a name="en-us_topic_0123490185_p555372818031"></a><a name="en-us_topic_0123490185_p555372818031"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="45.97%" id="mcps1.2.5.1.4"><p id="a672c489165984b23b4ac7ff110d2f8d0"><a name="a672c489165984b23b4ac7ff110d2f8d0"></a><a name="a672c489165984b23b4ac7ff110d2f8d0"></a><strong>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r2f58632024304bcab1f6545bca0f6571"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="a1e5aa42a1ac9460791ffca2df385599c"><a name="a1e5aa42a1ac9460791ffca2df385599c"></a><a name="a1e5aa42a1ac9460791ffca2df385599c"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.4%" headers="mcps1.2.5.1.2 "><p id="a96219506a0114ef3b5f6e09afd519e2e"><a name="a96219506a0114ef3b5f6e09afd519e2e"></a><a name="a96219506a0114ef3b5f6e09afd519e2e"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.9%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0123490185_p735269618031"><a name="en-us_topic_0123490185_p735269618031"></a><a name="en-us_topic_0123490185_p735269618031"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.97%" headers="mcps1.2.5.1.4 "><p id="ac55706719e7d4b36bcd2b64fb641e8ad"><a name="ac55706719e7d4b36bcd2b64fb641e8ad"></a><a name="ac55706719e7d4b36bcd2b64fb641e8ad"></a>Key to be matched. Currently, it can only be <strong id="b842352706191718"><a name="b842352706191718"></a><a name="b842352706191718"></a>resource_name</strong>.</p>
    </td>
    </tr>
    <tr id="rd2297e30a76f4f9db7d25d69c4a6f284"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="a955ce5b872f54445a8cfb91d31e3e515"><a name="a955ce5b872f54445a8cfb91d31e3e515"></a><a name="a955ce5b872f54445a8cfb91d31e3e515"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.4%" headers="mcps1.2.5.1.2 "><p id="aa41ce3d226664d388cdbff6371aa0873"><a name="aa41ce3d226664d388cdbff6371aa0873"></a><a name="aa41ce3d226664d388cdbff6371aa0873"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.9%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0123490185_p350303918031"><a name="en-us_topic_0123490185_p350303918031"></a><a name="en-us_topic_0123490185_p350303918031"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.97%" headers="mcps1.2.5.1.4 "><p id="ad834a2ed8a664de4bce813d49cc4213b"><a name="ad834a2ed8a664de4bce813d49cc4213b"></a><a name="ad834a2ed8a664de4bce813d49cc4213b"></a>Value to be matched. It contains a maximum of 255 Unicode characters and cannot contain underscores (_) and percent sign (%).</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    Query DNS resources by tag.

    ```
    POST https://{DNS_Endpoint}/v2/{project_id}/DNS-private_zone/resource_instances/action
    ```

    The following is a request example when  **action**  is set to  **filter**:

    ```
    {
        "offset": "100", 
        "limit": "100", 
        "action": "filter", 
        "matches": [
            {
                "key": "resource_name", 
                "value": "resource1"
            }
        ], 
        "not_tags": [
            {
                "key": "key1", 
                "values": [
                    "*value1", 
                    "value2"
                ]
            }
        ], 
        "tags": [
            {
                "key": "key1", 
                "values": [
                    "*value1", 
                    "value2"
                ]
            }
        ], 
        "tags_any": [
            {
                "key": "key1", 
                "values": [
                    "value1", 
                    "value2"
                ]
            }
        ], 
        "not_tags_any": [
            {
                "key": "key1", 
                "values": [
                    "value1", 
                    "value2"
                ]
            }
        ]
    }
    ```

    The following is a request example when  **action**  is set to  **count**:

    ```
    {
        "action": "count", 
        "not_tags": [
            {
                "key": "key1", 
                "values": [
                    "value1", 
                    "*value2"
                ]
            }
        ], 
        "tags": [
            {
                "key": "key1", 
                "values": [
                    "value1", 
                    "value2"
                ]
            }, 
            {
                "key": "key2", 
                "values": [
                    "value1", 
                    "value2"
                ]
            }
        ], 
        "tags_any": [
            {
                "key": "key1", 
                "values": [
                    "value1", 
                    "value2"
                ]
            }
        ], 
        "not_tags_any": [
            {
                "key": "key1", 
                "values": [
                    "value1", 
                    "value2"
                ]
            }
        ], 
        "matches": [
            {
                "key": "resource_name", 
                "value": "resource1"
            }
        ]
    }
    ```


## Response<a name="sa5067885f5544ce5bae155c4813b5010"></a>

-   Parameter description

    **Table  5**  Parameters in the response

    <a name="t93ffcfa8fbbe4abcb969defd2a74fa2d"></a>
    <table><thead align="left"><tr id="ra25a22e127e6425fb02bdcc4c86e44f6"><th class="cellrowborder" valign="top" width="22.81%" id="mcps1.2.4.1.1"><p id="a296f7700dac14acb913c0d4cfc4c1242"><a name="a296f7700dac14acb913c0d4cfc4c1242"></a><a name="a296f7700dac14acb913c0d4cfc4c1242"></a><strong>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="26.75%" id="mcps1.2.4.1.2"><p id="adc79b60087ab4c80b586816493181550"><a name="adc79b60087ab4c80b586816493181550"></a><a name="adc79b60087ab4c80b586816493181550"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.44%" id="mcps1.2.4.1.3"><p id="a144302e9d47446eeaeab02331e0902e2"><a name="a144302e9d47446eeaeab02331e0902e2"></a><a name="a144302e9d47446eeaeab02331e0902e2"></a><strong>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r1112394dde664478bbbffb5e3f601aeb"><td class="cellrowborder" valign="top" width="22.81%" headers="mcps1.2.4.1.1 "><p id="acc27bc81988d493e8b21ae8ca69371a0"><a name="acc27bc81988d493e8b21ae8ca69371a0"></a><a name="acc27bc81988d493e8b21ae8ca69371a0"></a>resources</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.75%" headers="mcps1.2.4.1.2 "><p id="a0d48338359754182b83c7d83a8a3fcd3"><a name="a0d48338359754182b83c7d83a8a3fcd3"></a><a name="a0d48338359754182b83c7d83a8a3fcd3"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.44%" headers="mcps1.2.4.1.3 "><p id="a31b758a590b24f38a1b6ff57be47f7a1"><a name="a31b758a590b24f38a1b6ff57be47f7a1"></a><a name="a31b758a590b24f38a1b6ff57be47f7a1"></a>Resource list For details, see <a href="#t3e476a1cfb8049779a2717fcc171190c">Table 6</a>.</p>
    </td>
    </tr>
    <tr id="r13fafef109aa4ca3a77f5674457dc84e"><td class="cellrowborder" valign="top" width="22.81%" headers="mcps1.2.4.1.1 "><p id="a220b5c3ec6204c5ab0155e0dbdec40e6"><a name="a220b5c3ec6204c5ab0155e0dbdec40e6"></a><a name="a220b5c3ec6204c5ab0155e0dbdec40e6"></a>total_count</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.75%" headers="mcps1.2.4.1.2 "><p id="aea14055203614399a52ae2ffb18f014c"><a name="aea14055203614399a52ae2ffb18f014c"></a><a name="aea14055203614399a52ae2ffb18f014c"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.44%" headers="mcps1.2.4.1.3 "><p id="a49379e7d97b24743bd03df577f6cead4"><a name="a49379e7d97b24743bd03df577f6cead4"></a><a name="a49379e7d97b24743bd03df577f6cead4"></a>Number of resources that meet the filter criteria. The number is irrelevant to <strong id="b15991112751210"><a name="b15991112751210"></a><a name="b15991112751210"></a>limit</strong> or <strong id="b29913270124"><a name="b29913270124"></a><a name="b29913270124"></a>offset</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6**  Parameters in the  **resources**  field

    <a name="t3e476a1cfb8049779a2717fcc171190c"></a>
    <table><thead align="left"><tr id="rd120153f066f40ef8ef08f1152872177"><th class="cellrowborder" valign="top" width="23.189999999999998%" id="mcps1.2.4.1.1"><p id="en-us_topic_0123490185_p17211504363"><a name="en-us_topic_0123490185_p17211504363"></a><a name="en-us_topic_0123490185_p17211504363"></a><strong>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="26.38%" id="mcps1.2.4.1.2"><p id="en-us_topic_0123490185_p17216704366"><a name="en-us_topic_0123490185_p17216704366"></a><a name="en-us_topic_0123490185_p17216704366"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.43%" id="mcps1.2.4.1.3"><p id="a9e960e5aa1c54db3805d766f0274b42e"><a name="a9e960e5aa1c54db3805d766f0274b42e"></a><a name="a9e960e5aa1c54db3805d766f0274b42e"></a><strong>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="rd5c5239182a04cbf90ff620d5bac4e95"><td class="cellrowborder" valign="top" width="23.189999999999998%" headers="mcps1.2.4.1.1 "><p id="aee8c1fb529ec460cacb6ed4cae20c4ea"><a name="aee8c1fb529ec460cacb6ed4cae20c4ea"></a><a name="aee8c1fb529ec460cacb6ed4cae20c4ea"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.38%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0123490185_p1232603365"><a name="en-us_topic_0123490185_p1232603365"></a><a name="en-us_topic_0123490185_p1232603365"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.43%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0123490185_p172367023619"><a name="en-us_topic_0123490185_p172367023619"></a><a name="en-us_topic_0123490185_p172367023619"></a>Resource ID</p>
    </td>
    </tr>
    <tr id="r9cb6270a18704fc8b5da917c9e9c8451"><td class="cellrowborder" valign="top" width="23.189999999999998%" headers="mcps1.2.4.1.1 "><p id="ae83fa7e9bc4f40f4b28d14d2fc779af7"><a name="ae83fa7e9bc4f40f4b28d14d2fc779af7"></a><a name="ae83fa7e9bc4f40f4b28d14d2fc779af7"></a>resource_detail</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.38%" headers="mcps1.2.4.1.2 "><p id="af84e030d49a3448fa1c13ac1ce325679"><a name="af84e030d49a3448fa1c13ac1ce325679"></a><a name="af84e030d49a3448fa1c13ac1ce325679"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.43%" headers="mcps1.2.4.1.3 "><p id="a32fec0e09c2247a0aa6e5754144b3920"><a name="a32fec0e09c2247a0aa6e5754144b3920"></a><a name="a32fec0e09c2247a0aa6e5754144b3920"></a>Resource details. This field is reserved for subsequent extension, and its value defaults to an empty string.</p>
    </td>
    </tr>
    <tr id="ra651330f319f4b55add1adc003cab0c5"><td class="cellrowborder" valign="top" width="23.189999999999998%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0123490185_p325210033618"><a name="en-us_topic_0123490185_p325210033618"></a><a name="en-us_topic_0123490185_p325210033618"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.38%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0123490185_p62596018369"><a name="en-us_topic_0123490185_p62596018369"></a><a name="en-us_topic_0123490185_p62596018369"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.43%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0123490185_p22617043616"><a name="en-us_topic_0123490185_p22617043616"></a><a name="en-us_topic_0123490185_p22617043616"></a>List of queried tags. If no tag is matched, an empty array is returned. For details, see <a href="data-structure.md#table19530794112436">Table 2</a>.</p>
    </td>
    </tr>
    <tr id="r24cb9cf0de95421199a90debd0f8973c"><td class="cellrowborder" valign="top" width="23.189999999999998%" headers="mcps1.2.4.1.1 "><p id="a2bc79a175c4842caab31f944c0a3dcd9"><a name="a2bc79a175c4842caab31f944c0a3dcd9"></a><a name="a2bc79a175c4842caab31f944c0a3dcd9"></a>resource_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.38%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0123490185_p827019012366"><a name="en-us_topic_0123490185_p827019012366"></a><a name="en-us_topic_0123490185_p827019012366"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.43%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0123490185_p527500133615"><a name="en-us_topic_0123490185_p527500133615"></a><a name="en-us_topic_0123490185_p527500133615"></a>Resource name. If no resource name is matched, the value is left blank.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    The following is a request example when  **action**  is set to  **filter**:

    ```
    {
        "resources": [
            {
                "resource_detail": null, 
                "resource_id": "cdfs_cefs_wesas_12_dsad", 
                "resource_name": "resouece1", 
                "tags": [
                    {
                        "key": "key1", 
                        "value": "value1"
                    }, 
                    {
                        "key": "key2", 
                        "value": "value1"
                    }
                ]
            }
        ], 
        "total_count": 1000
    }
    ```

    The following is a request example when  **action**  is set to  **count**:

    ```
    {
        "total_count": 1000
    }
    ```


## Returned Value<a name="section9249181042119"></a>

If the API call returns a code of 2_xx_, for example, 200, 202, or 204, the request is successful.

For details, see  [Status Code](status-code.md).

