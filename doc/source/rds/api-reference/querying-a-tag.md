# Querying a Tag<a name="rds_01_0007"></a>

## Function<a name="sea993a330c974061b405ca4661f93d6d"></a>

This API is used to query the tag associated with a DB instance.

## URI<a name="s9e54b8684a4040539a9725802741a783"></a>

-   URI format

    PATH: /v1/\{project\_id\}/rds/\{instanceId\}/tags

    Method: GET

-   Parameter description

    **Table  1**  Parameter description

    <a name="en-us_topic_0091754392_table58427690"></a>
    <table><thead align="left"><tr id="en-us_topic_0091754392_row1482002"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.1"><p id="en-us_topic_0091754392_p52933326"><a name="en-us_topic_0091754392_p52933326"></a><a name="en-us_topic_0091754392_p52933326"></a><strong id="en-us_topic_0091754392_b84235270691445"><a name="en-us_topic_0091754392_b84235270691445"></a><a name="en-us_topic_0091754392_b84235270691445"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="en-us_topic_0091754392_p59740974"><a name="en-us_topic_0091754392_p59740974"></a><a name="en-us_topic_0091754392_p59740974"></a><strong id="en-us_topic_0091754392_b842352706102346"><a name="en-us_topic_0091754392_b842352706102346"></a><a name="en-us_topic_0091754392_b842352706102346"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="54%" id="mcps1.2.4.1.3"><p id="en-us_topic_0091754392_p7180698"><a name="en-us_topic_0091754392_p7180698"></a><a name="en-us_topic_0091754392_p7180698"></a><strong id="en-us_topic_0091754392_b842352706163417"><a name="en-us_topic_0091754392_b842352706163417"></a><a name="en-us_topic_0091754392_b842352706163417"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0091754392_row44765691"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0091754392_p2142393"><a name="en-us_topic_0091754392_p2142393"></a><a name="en-us_topic_0091754392_p2142393"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0091754392_p39316155"><a name="en-us_topic_0091754392_p39316155"></a><a name="en-us_topic_0091754392_p39316155"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0091754392_p30492010"><a name="en-us_topic_0091754392_p30492010"></a><a name="en-us_topic_0091754392_p30492010"></a>Specifies the project ID of a tenant in a region.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0091754392_row5992637"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0091754392_p15641626"><a name="en-us_topic_0091754392_p15641626"></a><a name="en-us_topic_0091754392_p15641626"></a>instanceId</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0091754392_p59012183"><a name="en-us_topic_0091754392_p59012183"></a><a name="en-us_topic_0091754392_p59012183"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="p7417132564016"><a name="p7417132564016"></a><a name="p7417132564016"></a>Specifies the primary node ID of the DB instance.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Restrictions

    Standby DB instances do not support tag queries.


## Request<a name="s299517745d844e4c9b94a601e0b8c6d4"></a>

None

## Normal Response<a name="s368fe6de564946c2b526b9ef768efc16"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="tdf9bc68cc7aa4f6c91fa3f68db98f402"></a>
    <table><thead align="left"><tr id="rff0956339a58457fb90f872efb864b95"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="ae882aa35f1de435b9a580a075747ee71"><a name="ae882aa35f1de435b9a580a075747ee71"></a><a name="ae882aa35f1de435b9a580a075747ee71"></a><strong id="b868697366"><a name="b868697366"></a><a name="b868697366"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="a5771f9cf14ab47ebb4c8d3df3c5f217f"><a name="a5771f9cf14ab47ebb4c8d3df3c5f217f"></a><a name="a5771f9cf14ab47ebb4c8d3df3c5f217f"></a><strong id="en-us_topic_0091754392_b842352706164541"><a name="en-us_topic_0091754392_b842352706164541"></a><a name="en-us_topic_0091754392_b842352706164541"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="aad9efbdf9d0d43518c9594a21edee6c7"><a name="aad9efbdf9d0d43518c9594a21edee6c7"></a><a name="aad9efbdf9d0d43518c9594a21edee6c7"></a><strong id="b498706646"><a name="b498706646"></a><a name="b498706646"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="rdaedaaefc6ed46c3b614884798b54f88"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="ad45f5d9336664a4aad87f123b63f53ff"><a name="ad45f5d9336664a4aad87f123b63f53ff"></a><a name="ad45f5d9336664a4aad87f123b63f53ff"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="a4be451d811c44684b59ce41ae7330957"><a name="a4be451d811c44684b59ce41ae7330957"></a><a name="a4be451d811c44684b59ce41ae7330957"></a>List data structure. For details, see <a href="#t8538b53f8f2141978a5bf8ef5606bf24">Table 3</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="a5ebc1c8bc38a441d81ab753dc2ad7db3"><a name="a5ebc1c8bc38a441d81ab753dc2ad7db3"></a><a name="a5ebc1c8bc38a441d81ab753dc2ad7db3"></a>Specifies the tag information.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  tags field data structure description

    <a name="t8538b53f8f2141978a5bf8ef5606bf24"></a>
    <table><thead align="left"><tr id="rb6cfe419b44646bd8577bc3ed47eb5b3"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="a26202a3b1c294a109b26ad197fee22a9"><a name="a26202a3b1c294a109b26ad197fee22a9"></a><a name="a26202a3b1c294a109b26ad197fee22a9"></a><strong id="b14472580"><a name="b14472580"></a><a name="b14472580"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="a2802be9864364665bbb2ab2e74a6d0b9"><a name="a2802be9864364665bbb2ab2e74a6d0b9"></a><a name="a2802be9864364665bbb2ab2e74a6d0b9"></a><strong id="b1203370500"><a name="b1203370500"></a><a name="b1203370500"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="afc20aa691ea441059d7a6fa3d7c2b242"><a name="afc20aa691ea441059d7a6fa3d7c2b242"></a><a name="afc20aa691ea441059d7a6fa3d7c2b242"></a><strong id="b1617532541"><a name="b1617532541"></a><a name="b1617532541"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r7aaef0b8085c44e184efd6a0cc1fc6fc"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="a0eac6dd9eec4493e81e7df32833ca631"><a name="a0eac6dd9eec4493e81e7df32833ca631"></a><a name="a0eac6dd9eec4493e81e7df32833ca631"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="a7463599bd8ce4e089b24dc6c0e87d20b"><a name="a7463599bd8ce4e089b24dc6c0e87d20b"></a><a name="a7463599bd8ce4e089b24dc6c0e87d20b"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="ab3ccadae35c840d4a43d7796f3a572cb"><a name="ab3ccadae35c840d4a43d7796f3a572cb"></a><a name="ab3ccadae35c840d4a43d7796f3a572cb"></a>Specifies the tag key.</p>
    <p id="en-us_topic_0091754392_p223453410469"><a name="en-us_topic_0091754392_p223453410469"></a><a name="en-us_topic_0091754392_p223453410469"></a>Its value cannot be empty and must be 1 to 36 Unicode characters in length. It cannot contain nonprintable ASCII characters (0–31) and the following special characters: *&lt;&gt;\=</p>
    </td>
    </tr>
    <tr id="r621a8e5a0a674e0b8e1e564d324888cf"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0091754392_p637211162517"><a name="en-us_topic_0091754392_p637211162517"></a><a name="en-us_topic_0091754392_p637211162517"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="ad653997cd2c8467ebf471c9e430f2ab1"><a name="ad653997cd2c8467ebf471c9e430f2ab1"></a><a name="ad653997cd2c8467ebf471c9e430f2ab1"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="a4be7f42db44c4067833d133e404835f5"><a name="a4be7f42db44c4067833d133e404835f5"></a><a name="a4be7f42db44c4067833d133e404835f5"></a>Specifies the tag value.</p>
    <p id="ad36f13f908504e398a5c843de3beb064"><a name="ad36f13f908504e398a5c843de3beb064"></a><a name="ad36f13f908504e398a5c843de3beb064"></a>Its value can be empty or 1 to 43 Unicode characters in length. It cannot contain nonprintable ASCII characters (0–31) and the following special characters: *&lt;&gt;\=</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Response example

    ```
    {
           "tags": [
            {
                "key": "key1",
                "value": "value1"
            },
            {
                "key": "key2",
                "value": "value3"
            }
        ]
    }
    ```


## Abnormal Response<a name="sefb698423812481abfe93407238a2012"></a>

For details, see  [Abnormal Request Results](abnormal-request-results.md).

