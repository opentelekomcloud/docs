# Modifying the Access Information of a Specified Cluster<a name="cce_02_0346"></a>

## Function<a name="s6fbafdbe1fae41f0bcf8051f0b7e9bd7"></a>

This API is used to modify the access information of a specified cluster.

## URI<a name="sc2f4026114044d50b09a65549f6107f3"></a>

PUT /api/v3/projects/\{project\_id\}/clusters/\{cluster\_id\}/mastereip

[Table 1](#tcb491e3c1e0f4805bc2a0f117c2e5291)  describes the parameters of the API.

**Table  1**  Parameter description

<a name="tcb491e3c1e0f4805bc2a0f117c2e5291"></a>
<table><thead align="left"><tr id="rb1f18e3e47264a689ce8837da9540243"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.1"><p id="a751f244cbf5b43bbae736c7fe4157a65"><a name="a751f244cbf5b43bbae736c7fe4157a65"></a><a name="a751f244cbf5b43bbae736c7fe4157a65"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.24%" id="mcps1.2.4.1.2"><p id="a8cd1c6a113cc42b5b1ed7195b0d632ea"><a name="a8cd1c6a113cc42b5b1ed7195b0d632ea"></a><a name="a8cd1c6a113cc42b5b1ed7195b0d632ea"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="62.760000000000005%" id="mcps1.2.4.1.3"><p id="a130c3125c9c54410a8213b4095e993a7"><a name="a130c3125c9c54410a8213b4095e993a7"></a><a name="a130c3125c9c54410a8213b4095e993a7"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="r233fdbfefc734b3f872982d4f6bbe5f0"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="a210d020408a14eaabab2b4f4411603f2"><a name="a210d020408a14eaabab2b4f4411603f2"></a><a name="a210d020408a14eaabab2b4f4411603f2"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.24%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0102499104_p814518580186"><a name="en-us_topic_0102499104_p814518580186"></a><a name="en-us_topic_0102499104_p814518580186"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="62.760000000000005%" headers="mcps1.2.4.1.3 "><p id="a11311534aa924643804a0f42eca7da84"><a name="a11311534aa924643804a0f42eca7da84"></a><a name="a11311534aa924643804a0f42eca7da84"></a>Project ID.</p>
</td>
</tr>
<tr id="rc13dcfbc5dc94afa9fa3c0533f438e88"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p614194762313"><a name="p614194762313"></a><a name="p614194762313"></a>cluster_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.24%" headers="mcps1.2.4.1.2 "><p id="af22431c45a934fc3b3d29abe71edf037"><a name="af22431c45a934fc3b3d29abe71edf037"></a><a name="af22431c45a934fc3b3d29abe71edf037"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="62.760000000000005%" headers="mcps1.2.4.1.3 "><p id="ad84b46caf65641eaa6a2a0136244932d"><a name="ad84b46caf65641eaa6a2a0136244932d"></a><a name="ad84b46caf65641eaa6a2a0136244932d"></a>Cluster ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="s41fee4eb162746cdbed4f2b5779e9fdf"></a>

**Request parameters:**

[Table 2](#t97650ea1b00a431b9ba9075aafc7e494)  describes the request parameters.

**Table  2**  Parameter description

<a name="t97650ea1b00a431b9ba9075aafc7e494"></a>
<table><thead align="left"><tr id="r834c19a7a4b345b2b8a955d744cbb20c"><th class="cellrowborder" valign="top" width="20.202020202020204%" id="mcps1.2.5.1.1"><p id="en-us_topic_0102499074_p2030132"><a name="en-us_topic_0102499074_p2030132"></a><a name="en-us_topic_0102499074_p2030132"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.747474747474747%" id="mcps1.2.5.1.2"><p id="en-us_topic_0102499074_p30222992"><a name="en-us_topic_0102499074_p30222992"></a><a name="en-us_topic_0102499074_p30222992"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="21.797979797979796%" id="mcps1.2.5.1.3"><p id="en-us_topic_0102499074_p32143248"><a name="en-us_topic_0102499074_p32143248"></a><a name="en-us_topic_0102499074_p32143248"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="41.25252525252525%" id="mcps1.2.5.1.4"><p id="en-us_topic_0102499074_p53466268"><a name="en-us_topic_0102499074_p53466268"></a><a name="en-us_topic_0102499074_p53466268"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0102499074_row9619511127"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0102499074_p4785161212"><a name="en-us_topic_0102499074_p4785161212"></a><a name="en-us_topic_0102499074_p4785161212"></a>spec</p>
</td>
<td class="cellrowborder" valign="top" width="16.747474747474747%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0102499074_p97205171219"><a name="en-us_topic_0102499074_p97205171219"></a><a name="en-us_topic_0102499074_p97205171219"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.797979797979796%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0102499074_p67105119126"><a name="en-us_topic_0102499074_p67105119126"></a><a name="en-us_topic_0102499074_p67105119126"></a><a href="#t18f5d0505d9048cab59a8ecd4fa7138d">Table 3</a></p>
</td>
<td class="cellrowborder" valign="top" width="41.25252525252525%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0102499074_p10785112129"><a name="en-us_topic_0102499074_p10785112129"></a><a name="en-us_topic_0102499074_p10785112129"></a>-</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Data structure of the spec field

<a name="t18f5d0505d9048cab59a8ecd4fa7138d"></a>
<table><thead align="left"><tr id="r113f74eeb0da4e56bfcf3584e489d2c7"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.1"><p id="a5b5028a5cb07467b83f5dab81fe07f19"><a name="a5b5028a5cb07467b83f5dab81fe07f19"></a><a name="a5b5028a5cb07467b83f5dab81fe07f19"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.11%" id="mcps1.2.5.1.2"><p id="a23cedfd53bad4d57a6ca33bf335dfccb"><a name="a23cedfd53bad4d57a6ca33bf335dfccb"></a><a name="a23cedfd53bad4d57a6ca33bf335dfccb"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="13.889999999999999%" id="mcps1.2.5.1.3"><p id="ad2af0c8795624545820501099fc4ce30"><a name="ad2af0c8795624545820501099fc4ce30"></a><a name="ad2af0c8795624545820501099fc4ce30"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49%" id="mcps1.2.5.1.4"><p id="a7980ec18617e4c289eb4f3a1bcd82699"><a name="a7980ec18617e4c289eb4f3a1bcd82699"></a><a name="a7980ec18617e4c289eb4f3a1bcd82699"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row10434569144"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p143175631416"><a name="p143175631416"></a><a name="p143175631416"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.2.5.1.2 "><p id="p1619112174"><a name="p1619112174"></a><a name="p1619112174"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.889999999999999%" headers="mcps1.2.5.1.3 "><p id="aeefd5eaaf23042b28237905441e36728"><a name="aeefd5eaaf23042b28237905441e36728"></a><a name="aeefd5eaaf23042b28237905441e36728"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.5.1.4 "><p id="p6979056174910"><a name="p6979056174910"></a><a name="p6979056174910"></a>Whether to bind an elastic IP address to the cluster or unbind an elastic IP address from the cluster. The value is <strong id="b126925119524"><a name="b126925119524"></a><a name="b126925119524"></a>bind</strong> or <strong id="b1569291125213"><a name="b1569291125213"></a><a name="b1569291125213"></a>unbind</strong> (case insensitive).</p>
<div class="note" id="note1219018516273"><a name="note1219018516273"></a><a name="note1219018516273"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p79151358133419"><a name="p79151358133419"></a><a name="p79151358133419"></a><strong id="b1137652614523"><a name="b1137652614523"></a><a name="b1137652614523"></a>id</strong> needs to be configured only when <strong id="b1937613269521"><a name="b1937613269521"></a><a name="b1937613269521"></a>action</strong> is set to <strong id="b143768268523"><a name="b143768268523"></a><a name="b143768268523"></a>bind</strong>.</p>
</div></div>
</td>
</tr>
<tr id="row202921151201520"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p18292105141517"><a name="p18292105141517"></a><a name="p18292105141517"></a>spec</p>
</td>
<td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.2.5.1.2 "><p id="p119991001173"><a name="p119991001173"></a><a name="p119991001173"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.889999999999999%" headers="mcps1.2.5.1.3 "><p id="p11293195141517"><a name="p11293195141517"></a><a name="p11293195141517"></a><a href="#table985812714268">Table 4</a></p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.5.1.4 "><p id="p178443385523"><a name="p178443385523"></a><a name="p178443385523"></a>Information about the elastic IP address.</p>
</td>
</tr>
</tbody>
</table>

**Table  4**  Data structure of the spec-spec field

<a name="table985812714268"></a>
<table><thead align="left"><tr id="row186619714265"><th class="cellrowborder" valign="top" width="20.464646464646467%" id="mcps1.2.5.1.1"><p id="p148697782611"><a name="p148697782611"></a><a name="p148697782611"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.87878787878788%" id="mcps1.2.5.1.2"><p id="p16871779269"><a name="p16871779269"></a><a name="p16871779269"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="18.737373737373737%" id="mcps1.2.5.1.3"><p id="p108739762610"><a name="p108739762610"></a><a name="p108739762610"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="43.91919191919192%" id="mcps1.2.5.1.4"><p id="p148751718269"><a name="p148751718269"></a><a name="p148751718269"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row108781475261"><td class="cellrowborder" valign="top" width="20.464646464646467%" headers="mcps1.2.5.1.1 "><p id="p5880472261"><a name="p5880472261"></a><a name="p5880472261"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="16.87878787878788%" headers="mcps1.2.5.1.2 "><p id="p58836772619"><a name="p58836772619"></a><a name="p58836772619"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.737373737373737%" headers="mcps1.2.5.1.3 "><p id="p188711926195018"><a name="p188711926195018"></a><a name="p188711926195018"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.91919191919192%" headers="mcps1.2.5.1.4 "><p id="p98720266503"><a name="p98720266503"></a><a name="p98720266503"></a>ID of the elastic IP address.</p>
</td>
</tr>
</tbody>
</table>

**Example request:**

-   Binding an elastic IP address to the cluster

    ```
    {
        "spec": {
            "action": "bind",
            "spec": {
                "id": "0ef26920-3527-405d-a7b4-27106618c2d7"
            }
        }
    }
    ```

-   Unbinding an elastic IP address from the cluster

    ```
    {
        "spec": {
            "action": "unbind"
        }
    }
    ```


## Response<a name="s2ccf3fe413964af09c341dde26d1af0c"></a>

**Response parameters:**

[Table 5](#tab67b852d83a4de9b60d1595df71492e)  describes the response parameters.

**Table  5**  Response parameters

<a name="tab67b852d83a4de9b60d1595df71492e"></a>
<table><thead align="left"><tr id="rf1a4c381ee074a46b9ac346753818e82"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="a4b7b787bc55444b5bfd1eed9a48cb61a"><a name="a4b7b787bc55444b5bfd1eed9a48cb61a"></a><a name="a4b7b787bc55444b5bfd1eed9a48cb61a"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="27%" id="mcps1.2.4.1.2"><p id="a1da7a400d42949e485343e14a806b0c9"><a name="a1da7a400d42949e485343e14a806b0c9"></a><a name="a1da7a400d42949e485343e14a806b0c9"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="48%" id="mcps1.2.4.1.3"><p id="a5db7f899fce44bb3ab2b7417e6bb529b"><a name="a5db7f899fce44bb3ab2b7417e6bb529b"></a><a name="a5db7f899fce44bb3ab2b7417e6bb529b"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row10105155934713"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p8105259114716"><a name="p8105259114716"></a><a name="p8105259114716"></a>metadata</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.2 "><p id="p1610685924712"><a name="p1610685924712"></a><a name="p1610685924712"></a>json</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.4.1.3 "><p id="p041274371111"><a name="p041274371111"></a><a name="p041274371111"></a>Metadata.</p>
</td>
</tr>
<tr id="red54b450669c43c0ae4c9675aeda9783"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a1a0d8544138a4c3b822e532cf1c6f81a"><a name="a1a0d8544138a4c3b822e532cf1c6f81a"></a><a name="a1a0d8544138a4c3b822e532cf1c6f81a"></a>spec</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.2 "><p id="af72d398703ac446f84a274d142bf3298"><a name="af72d398703ac446f84a274d142bf3298"></a><a name="af72d398703ac446f84a274d142bf3298"></a><a href="#tce0b898226db4163888e3bf7c290b876">Table 6</a></p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.4.1.3 "><p id="p626620214539"><a name="p626620214539"></a><a name="p626620214539"></a>-</p>
</td>
</tr>
<tr id="r951f151cb6a94522959fa721d7447c89"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a126dd3f6b78d4124bbb8ae293a96c730"><a name="a126dd3f6b78d4124bbb8ae293a96c730"></a><a name="a126dd3f6b78d4124bbb8ae293a96c730"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.2 "><p id="a7d23dbee2d6141b89197a1ea8eb6ec43"><a name="a7d23dbee2d6141b89197a1ea8eb6ec43"></a><a name="a7d23dbee2d6141b89197a1ea8eb6ec43"></a><a href="#t500749d17adf492d8e2535fe4933b586">Table 7</a></p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.4.1.3 "><p id="p926672105312"><a name="p926672105312"></a><a name="p926672105312"></a>Cluster endpoint.</p>
</td>
</tr>
</tbody>
</table>

**Table  6**  Data structure of the spec field

<a name="tce0b898226db4163888e3bf7c290b876"></a>
<table><thead align="left"><tr id="r2274ed69c1084ab0ad89026dcdcfc6d7"><th class="cellrowborder" valign="top" width="25.252525252525253%" id="mcps1.2.4.1.1"><p id="a6569bcab86994e7798721184d7167c1c"><a name="a6569bcab86994e7798721184d7167c1c"></a><a name="a6569bcab86994e7798721184d7167c1c"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="26.262626262626267%" id="mcps1.2.4.1.2"><p id="ad28df63ddf014e05b59955a86d961da1"><a name="ad28df63ddf014e05b59955a86d961da1"></a><a name="ad28df63ddf014e05b59955a86d961da1"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="48.484848484848484%" id="mcps1.2.4.1.3"><p id="a61de14365fa04d9cb3c6ed951cfccddf"><a name="a61de14365fa04d9cb3c6ed951cfccddf"></a><a name="a61de14365fa04d9cb3c6ed951cfccddf"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row7795169186"><td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.2.4.1.1 "><p id="p4795186171818"><a name="p4795186171818"></a><a name="p4795186171818"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="26.262626262626267%" headers="mcps1.2.4.1.2 "><p id="p1979506191815"><a name="p1979506191815"></a><a name="p1979506191815"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.2.4.1.3 "><p id="p93847142547"><a name="p93847142547"></a><a name="p93847142547"></a>Whether an EIP is bound to or unbound from the cluster. The value is <strong id="b53846146543"><a name="b53846146543"></a><a name="b53846146543"></a>bind</strong> or <strong id="b538416148544"><a name="b538416148544"></a><a name="b538416148544"></a>unbind</strong> (case insensitive).</p>
</td>
</tr>
<tr id="row455974181813"><td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.2.4.1.1 "><p id="p35608418184"><a name="p35608418184"></a><a name="p35608418184"></a>spec</p>
</td>
<td class="cellrowborder" valign="top" width="26.262626262626267%" headers="mcps1.2.4.1.2 "><p id="p14560741161812"><a name="p14560741161812"></a><a name="p14560741161812"></a><a href="#table985812714268">Table 4</a></p>
</td>
<td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.2.4.1.3 "><p id="p153926148540"><a name="p153926148540"></a><a name="p153926148540"></a>Information about the elastic IP address.</p>
</td>
</tr>
<tr id="en-us_topic_0102499104_row6345613224"><td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.2.4.1.1 "><p id="p191446177538"><a name="p191446177538"></a><a name="p191446177538"></a>elasticIp</p>
</td>
<td class="cellrowborder" valign="top" width="26.262626262626267%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0102499104_p3305622213"><a name="en-us_topic_0102499104_p3305622213"></a><a name="en-us_topic_0102499104_p3305622213"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.2.4.1.3 "><p id="p2392161465416"><a name="p2392161465416"></a><a name="p2392161465416"></a>Elastic IP address.</p>
</td>
</tr>
</tbody>
</table>

**Table  7**  Data structure of the status field

<a name="t500749d17adf492d8e2535fe4933b586"></a>
<table><thead align="left"><tr id="r35bb9041298042aea213c61c98130164"><th class="cellrowborder" valign="top" width="25.534653465346537%" id="mcps1.2.4.1.1"><p id="a3a4552f2f2f14345a506166c2bfdcd48"><a name="a3a4552f2f2f14345a506166c2bfdcd48"></a><a name="a3a4552f2f2f14345a506166c2bfdcd48"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25.95049504950495%" id="mcps1.2.4.1.2"><p id="a8540b1b2bd6f4d8ba70ee536a8c040b4"><a name="a8540b1b2bd6f4d8ba70ee536a8c040b4"></a><a name="a8540b1b2bd6f4d8ba70ee536a8c040b4"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="48.51485148514851%" id="mcps1.2.4.1.3"><p id="af212738c42704cf79be9111dc1e30df4"><a name="af212738c42704cf79be9111dc1e30df4"></a><a name="af212738c42704cf79be9111dc1e30df4"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="r0a94403170a244dd9462220cc9fb4dfa"><td class="cellrowborder" valign="top" width="25.534653465346537%" headers="mcps1.2.4.1.1 "><p id="p974817451532"><a name="p974817451532"></a><a name="p974817451532"></a>privateEndpoint</p>
</td>
<td class="cellrowborder" valign="top" width="25.95049504950495%" headers="mcps1.2.4.1.2 "><p id="adf37e5e216064f3d98f4d043fe86a19d"><a name="adf37e5e216064f3d98f4d043fe86a19d"></a><a name="adf37e5e216064f3d98f4d043fe86a19d"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.2.4.1.3 "><p id="p1880132319549"><a name="p1880132319549"></a><a name="p1880132319549"></a>Address for access within the VPC.</p>
</td>
</tr>
<tr id="rf1abd6a843de4df799d8ea0e9adec242"><td class="cellrowborder" valign="top" width="25.534653465346537%" headers="mcps1.2.4.1.1 "><p id="p147501045145319"><a name="p147501045145319"></a><a name="p147501045145319"></a>publicEndpoint</p>
</td>
<td class="cellrowborder" valign="top" width="25.95049504950495%" headers="mcps1.2.4.1.2 "><p id="a334521d77dc74e94ac8204f91c2ad8c0"><a name="a334521d77dc74e94ac8204f91c2ad8c0"></a><a name="a334521d77dc74e94ac8204f91c2ad8c0"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.2.4.1.3 "><p id="p148042335415"><a name="p148042335415"></a><a name="p148042335415"></a>Address for access outside the VPC.</p>
</td>
</tr>
</tbody>
</table>

**Example response:**

```
{
    "metadata": {},
    "spec": {
        "action": "bind",
        "spec": {
            "id": "0ef26920-3527-405d-a7b4-27106618c2d7",
            "eip": {
                "bandwidth": {
                    "size": 5,
                    "sharetype": "PER"
                }
            },
            "IsDynamic": false
        },
        "elasticIp": "10.154.50.11"
    },
    "status": {
        "privateEndpoint": "https://172.16.0.86:5443",
        "publicEndpoint": "https://10.154.50.11:5443"
    }
}
```

## Status Code<a name="s131d783777b74801babd13f31325a701"></a>

[Table 8](#tcb712722097d4597ae95bec996421736)  describes the status code of the API.

**Table  8**  Status code

<a name="tcb712722097d4597ae95bec996421736"></a>
<table><thead align="left"><tr id="raf218ccbec3841adbe9262ff3f979710"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="afa25e006a9c04ff7825041a04acf9e22"><a name="afa25e006a9c04ff7825041a04acf9e22"></a><a name="afa25e006a9c04ff7825041a04acf9e22"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="a83fe41b159214ceebd01cb9a66051ee8"><a name="a83fe41b159214ceebd01cb9a66051ee8"></a><a name="a83fe41b159214ceebd01cb9a66051ee8"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="ra13d8dded02b42348ff854630a5c6116"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="a6f5f4c332d184590b6cbaa8cc8e593ba"><a name="a6f5f4c332d184590b6cbaa8cc8e593ba"></a><a name="a6f5f4c332d184590b6cbaa8cc8e593ba"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="a37a7d2c56f48453e90d930ff08fcaab1"><a name="a37a7d2c56f48453e90d930ff08fcaab1"></a><a name="a37a7d2c56f48453e90d930ff08fcaab1"></a>The progress of the specified job is successfully obtained.</p>
</td>
</tr>
</tbody>
</table>

For details about error status codes, see  [Status Code](status-code.md).

