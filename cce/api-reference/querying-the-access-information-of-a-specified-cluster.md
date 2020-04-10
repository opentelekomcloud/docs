# Querying the Access Information of a Specified Cluster<a name="cce_02_0347"></a>

## Function<a name="s6fbafdbe1fae41f0bcf8051f0b7e9bd7"></a>

This API is used to query the access information of a specified cluster.

## URI<a name="sc2f4026114044d50b09a65549f6107f3"></a>

GET /api/v3/projects/\{project\_id\}/clusters/\{cluster\_id\}/openapi

[Table 1](#tcb491e3c1e0f4805bc2a0f117c2e5291)  describes the parameters of the API.

**Table  1**  Parameter description

<a name="tcb491e3c1e0f4805bc2a0f117c2e5291"></a>
<table><thead align="left"><tr id="rb1f18e3e47264a689ce8837da9540243"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.1"><p id="a751f244cbf5b43bbae736c7fe4157a65"><a name="a751f244cbf5b43bbae736c7fe4157a65"></a><a name="a751f244cbf5b43bbae736c7fe4157a65"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.74%" id="mcps1.2.4.1.2"><p id="a8cd1c6a113cc42b5b1ed7195b0d632ea"><a name="a8cd1c6a113cc42b5b1ed7195b0d632ea"></a><a name="a8cd1c6a113cc42b5b1ed7195b0d632ea"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="60.260000000000005%" id="mcps1.2.4.1.3"><p id="a130c3125c9c54410a8213b4095e993a7"><a name="a130c3125c9c54410a8213b4095e993a7"></a><a name="a130c3125c9c54410a8213b4095e993a7"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="r233fdbfefc734b3f872982d4f6bbe5f0"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="a210d020408a14eaabab2b4f4411603f2"><a name="a210d020408a14eaabab2b4f4411603f2"></a><a name="a210d020408a14eaabab2b4f4411603f2"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0102499104_p814518580186"><a name="en-us_topic_0102499104_p814518580186"></a><a name="en-us_topic_0102499104_p814518580186"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="60.260000000000005%" headers="mcps1.2.4.1.3 "><p id="a11311534aa924643804a0f42eca7da84"><a name="a11311534aa924643804a0f42eca7da84"></a><a name="a11311534aa924643804a0f42eca7da84"></a>Project ID.</p>
</td>
</tr>
<tr id="rc13dcfbc5dc94afa9fa3c0533f438e88"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p614194762313"><a name="p614194762313"></a><a name="p614194762313"></a>cluster_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.4.1.2 "><p id="af22431c45a934fc3b3d29abe71edf037"><a name="af22431c45a934fc3b3d29abe71edf037"></a><a name="af22431c45a934fc3b3d29abe71edf037"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="60.260000000000005%" headers="mcps1.2.4.1.3 "><p id="ad84b46caf65641eaa6a2a0136244932d"><a name="ad84b46caf65641eaa6a2a0136244932d"></a><a name="ad84b46caf65641eaa6a2a0136244932d"></a>Cluster ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="s41fee4eb162746cdbed4f2b5779e9fdf"></a>

N/A

## Response<a name="s2ccf3fe413964af09c341dde26d1af0c"></a>

**Response parameters:**

[Table 2](#tab67b852d83a4de9b60d1595df71492e)  describes the response parameters.

**Table  2**  Response parameters

<a name="tab67b852d83a4de9b60d1595df71492e"></a>
<table><thead align="left"><tr id="rf1a4c381ee074a46b9ac346753818e82"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="a4b7b787bc55444b5bfd1eed9a48cb61a"><a name="a4b7b787bc55444b5bfd1eed9a48cb61a"></a><a name="a4b7b787bc55444b5bfd1eed9a48cb61a"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="27%" id="mcps1.2.4.1.2"><p id="a1da7a400d42949e485343e14a806b0c9"><a name="a1da7a400d42949e485343e14a806b0c9"></a><a name="a1da7a400d42949e485343e14a806b0c9"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="48%" id="mcps1.2.4.1.3"><p id="a5db7f899fce44bb3ab2b7417e6bb529b"><a name="a5db7f899fce44bb3ab2b7417e6bb529b"></a><a name="a5db7f899fce44bb3ab2b7417e6bb529b"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row5412154301117"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1541244331118"><a name="p1541244331118"></a><a name="p1541244331118"></a>metadata</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.2 "><p id="p17412134341111"><a name="p17412134341111"></a><a name="p17412134341111"></a>json</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.4.1.3 "><p id="p041274371111"><a name="p041274371111"></a><a name="p041274371111"></a>Metadata.</p>
</td>
</tr>
<tr id="red54b450669c43c0ae4c9675aeda9783"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a1a0d8544138a4c3b822e532cf1c6f81a"><a name="a1a0d8544138a4c3b822e532cf1c6f81a"></a><a name="a1a0d8544138a4c3b822e532cf1c6f81a"></a>spec</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.2 "><p id="af72d398703ac446f84a274d142bf3298"><a name="af72d398703ac446f84a274d142bf3298"></a><a name="af72d398703ac446f84a274d142bf3298"></a><a href="#ta3c0ec2411934d01ad2031e6ea7a7106">Table 3</a></p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0102499104_p173598507179"><a name="en-us_topic_0102499104_p173598507179"></a><a name="en-us_topic_0102499104_p173598507179"></a>-</p>
</td>
</tr>
<tr id="r951f151cb6a94522959fa721d7447c89"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a126dd3f6b78d4124bbb8ae293a96c730"><a name="a126dd3f6b78d4124bbb8ae293a96c730"></a><a name="a126dd3f6b78d4124bbb8ae293a96c730"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.2 "><p id="a7d23dbee2d6141b89197a1ea8eb6ec43"><a name="a7d23dbee2d6141b89197a1ea8eb6ec43"></a><a name="a7d23dbee2d6141b89197a1ea8eb6ec43"></a><a href="#t500749d17adf492d8e2535fe4933b586">Table 7</a></p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.4.1.3 "><p id="a25339ae7ec4f40078fd92aeaac7c383b"><a name="a25339ae7ec4f40078fd92aeaac7c383b"></a><a name="a25339ae7ec4f40078fd92aeaac7c383b"></a>Cluster endpoint.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Data structure of the spec field

<a name="ta3c0ec2411934d01ad2031e6ea7a7106"></a>
<table><thead align="left"><tr id="r0a5786e3462f4b9ebdc5ca420b02da9c"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="en-us_topic_0102499104_p208332952414"><a name="en-us_topic_0102499104_p208332952414"></a><a name="en-us_topic_0102499104_p208332952414"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="26%" id="mcps1.2.4.1.2"><p id="a91f3cd2aee7c45cb8b2451f756b44a8c"><a name="a91f3cd2aee7c45cb8b2451f756b44a8c"></a><a name="a91f3cd2aee7c45cb8b2451f756b44a8c"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49%" id="mcps1.2.4.1.3"><p id="en-us_topic_0102499104_p118491295245"><a name="en-us_topic_0102499104_p118491295245"></a><a name="en-us_topic_0102499104_p118491295245"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="r95ca90217b1a46ae9638055735cfe644"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1057110497368"><a name="p1057110497368"></a><a name="p1057110497368"></a>spec</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="ab6148cf65df3409e97e83b8a725dd60c"><a name="ab6148cf65df3409e97e83b8a725dd60c"></a><a name="ab6148cf65df3409e97e83b8a725dd60c"></a><a href="#table5860192685015">Table 4</a></p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0102499074_p10785112129"><a name="en-us_topic_0102499074_p10785112129"></a><a name="en-us_topic_0102499074_p10785112129"></a>Information about the elastic IP address.</p>
</td>
</tr>
</tbody>
</table>

**Table  4**  Data structure of the spec-spec field

<a name="table5860192685015"></a>
<table><thead align="left"><tr id="row19864142616509"><th class="cellrowborder" valign="top" width="24.89%" id="mcps1.2.4.1.1"><p id="p886582655017"><a name="p886582655017"></a><a name="p886582655017"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="26.11%" id="mcps1.2.4.1.2"><p id="p78661526135012"><a name="p78661526135012"></a><a name="p78661526135012"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49%" id="mcps1.2.4.1.3"><p id="p4867142612505"><a name="p4867142612505"></a><a name="p4867142612505"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row286912605010"><td class="cellrowborder" valign="top" width="24.89%" headers="mcps1.2.4.1.1 "><p id="p11870102655019"><a name="p11870102655019"></a><a name="p11870102655019"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="26.11%" headers="mcps1.2.4.1.2 "><p id="p188711926195018"><a name="p188711926195018"></a><a name="p188711926195018"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.4.1.3 "><p id="p98720266503"><a name="p98720266503"></a><a name="p98720266503"></a>ID of the elastic IP address.</p>
</td>
</tr>
<tr id="rd71807884d5b4addae4502c0e4976380"><td class="cellrowborder" valign="top" width="24.89%" headers="mcps1.2.4.1.1 "><p id="p99031531155110"><a name="p99031531155110"></a><a name="p99031531155110"></a>eip</p>
</td>
<td class="cellrowborder" valign="top" width="26.11%" headers="mcps1.2.4.1.2 "><p id="a98abb425f12e46919d8d4f2f34f219dc"><a name="a98abb425f12e46919d8d4f2f34f219dc"></a><a name="a98abb425f12e46919d8d4f2f34f219dc"></a><a href="#table423743115136">Table 5</a></p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.4.1.3 "><p id="a66f6d6cdbe2f4bc1b569069bf033d941"><a name="a66f6d6cdbe2f4bc1b569069bf033d941"></a><a name="a66f6d6cdbe2f4bc1b569069bf033d941"></a>Information about the elastic IP address.</p>
</td>
</tr>
<tr id="row4157172341013"><td class="cellrowborder" valign="top" width="24.89%" headers="mcps1.2.4.1.1 "><p id="p10157142316100"><a name="p10157142316100"></a><a name="p10157142316100"></a>IsDynamic</p>
</td>
<td class="cellrowborder" valign="top" width="26.11%" headers="mcps1.2.4.1.2 "><p id="p17157112311013"><a name="p17157112311013"></a><a name="p17157112311013"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.4.1.3 "><p id="p6157192315109"><a name="p6157192315109"></a><a name="p6157192315109"></a>Whether the elastic IP address is dynamic.</p>
</td>
</tr>
</tbody>
</table>

**Table  5**  Data structure of the eip field

<a name="table423743115136"></a>
<table><thead align="left"><tr id="row1524443116131"><th class="cellrowborder" valign="top" width="25.742574257425744%" id="mcps1.2.4.1.1"><p id="p1724614319136"><a name="p1724614319136"></a><a name="p1724614319136"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25.742574257425744%" id="mcps1.2.4.1.2"><p id="p10247431141313"><a name="p10247431141313"></a><a name="p10247431141313"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="48.51485148514851%" id="mcps1.2.4.1.3"><p id="p82491431101310"><a name="p82491431101310"></a><a name="p82491431101310"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1425153118130"><td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.4.1.1 "><p id="p3253103141310"><a name="p3253103141310"></a><a name="p3253103141310"></a>bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.4.1.2 "><p id="p14941513123816"><a name="p14941513123816"></a><a name="p14941513123816"></a><a href="#table163165523719">Table 6</a></p>
</td>
<td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.2.4.1.3 "><p id="p347694721310"><a name="p347694721310"></a><a name="p347694721310"></a>Specifies the bandwidth of the elastic IP address.</p>
</td>
</tr>
</tbody>
</table>

**Table  6**  Data structure of the bandwidth field

<a name="table163165523719"></a>
<table><thead align="left"><tr id="row1072175583718"><th class="cellrowborder" valign="top" width="25.742574257425744%" id="mcps1.2.4.1.1"><p id="p15739559374"><a name="p15739559374"></a><a name="p15739559374"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25.742574257425744%" id="mcps1.2.4.1.2"><p id="p1176355163715"><a name="p1176355163715"></a><a name="p1176355163715"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="48.51485148514851%" id="mcps1.2.4.1.3"><p id="p178755103720"><a name="p178755103720"></a><a name="p178755103720"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row380155511373"><td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.4.1.1 "><p id="p0831755153715"><a name="p0831755153715"></a><a name="p0831755153715"></a>size</p>
</td>
<td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.4.1.2 "><p id="p198417553371"><a name="p198417553371"></a><a name="p198417553371"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.2.4.1.3 "><p id="p3537184134311"><a name="p3537184134311"></a><a name="p3537184134311"></a>Specifies the bandwidth (Mbit/s).</p>
</td>
</tr>
<tr id="row586145514376"><td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.4.1.1 "><p id="p16600202813817"><a name="p16600202813817"></a><a name="p16600202813817"></a>sharetype</p>
</td>
<td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.4.1.2 "><p id="p11901855153716"><a name="p11901855153716"></a><a name="p11901855153716"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.2.4.1.3 "><p id="p10781737104310"><a name="p10781737104310"></a><a name="p10781737104310"></a>Specifies the bandwidth sharing type.</p>
<p id="p590185512376"><a name="p590185512376"></a><a name="p590185512376"></a>Enumerated values: <strong id="b1441015514311"><a name="b1441015514311"></a><a name="b1441015514311"></a>PER</strong> (indicates exclusive bandwidth) and <strong id="b1083935964315"><a name="b1083935964315"></a><a name="b1083935964315"></a>WHOLE</strong> (indicates sharing).</p>
</td>
</tr>
</tbody>
</table>

**Table  7**  Data structure of the status field

<a name="t500749d17adf492d8e2535fe4933b586"></a>
<table><thead align="left"><tr id="r35bb9041298042aea213c61c98130164"><th class="cellrowborder" valign="top" width="25.742574257425744%" id="mcps1.2.4.1.1"><p id="a3a4552f2f2f14345a506166c2bfdcd48"><a name="a3a4552f2f2f14345a506166c2bfdcd48"></a><a name="a3a4552f2f2f14345a506166c2bfdcd48"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25.742574257425744%" id="mcps1.2.4.1.2"><p id="a8540b1b2bd6f4d8ba70ee536a8c040b4"><a name="a8540b1b2bd6f4d8ba70ee536a8c040b4"></a><a name="a8540b1b2bd6f4d8ba70ee536a8c040b4"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="48.51485148514851%" id="mcps1.2.4.1.3"><p id="af212738c42704cf79be9111dc1e30df4"><a name="af212738c42704cf79be9111dc1e30df4"></a><a name="af212738c42704cf79be9111dc1e30df4"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="r0a94403170a244dd9462220cc9fb4dfa"><td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.4.1.1 "><p id="p10319138123815"><a name="p10319138123815"></a><a name="p10319138123815"></a>privateEndpoint</p>
</td>
<td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.4.1.2 "><p id="adf37e5e216064f3d98f4d043fe86a19d"><a name="adf37e5e216064f3d98f4d043fe86a19d"></a><a name="adf37e5e216064f3d98f4d043fe86a19d"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.2.4.1.3 "><p id="p954112165387"><a name="p954112165387"></a><a name="p954112165387"></a>Address for access within the VPC.</p>
</td>
</tr>
<tr id="rf1abd6a843de4df799d8ea0e9adec242"><td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.4.1.1 "><p id="p4319986389"><a name="p4319986389"></a><a name="p4319986389"></a>publicEndpoint</p>
</td>
<td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.4.1.2 "><p id="a334521d77dc74e94ac8204f91c2ad8c0"><a name="a334521d77dc74e94ac8204f91c2ad8c0"></a><a name="a334521d77dc74e94ac8204f91c2ad8c0"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.2.4.1.3 "><p id="p1654117168385"><a name="p1654117168385"></a><a name="p1654117168385"></a>Address for access outside the VPC.</p>
</td>
</tr>
</tbody>
</table>

**Example response:**

```
{
    "metadata": {},
    "spec": {
        "spec": {
            "id": "0ead681e-9f94-4599-8a21-e2a1950da121",
            "eip": {
                "bandwidth": {
                    "size": 5,
                    "sharetype": "PER"
                }
            },
            "IsDynamic": false
        }
    },
    "status": {
        "privateEndpoint": "https://192.168.0.189:5443",
        "publicEndpoint": "https://10.154.50.197:5443"
    }
}
```

## Status Code<a name="s131d783777b74801babd13f31325a701"></a>

[Table 8](#table5493720464)  describes the status code of the API.

**Table  8**  Status code

<a name="table5493720464"></a>
<table><thead align="left"><tr id="row75001284615"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p75021728465"><a name="p75021728465"></a><a name="p75021728465"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p35041625463"><a name="p35041625463"></a><a name="p35041625463"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row350519216468"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p19507152124619"><a name="p19507152124619"></a><a name="p19507152124619"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p1508152134613"><a name="p1508152134613"></a><a name="p1508152134613"></a>The progress of the specified job is successfully obtained.</p>
</td>
</tr>
</tbody>
</table>

For details about error status codes, see  [Status Code](status-code.md).

