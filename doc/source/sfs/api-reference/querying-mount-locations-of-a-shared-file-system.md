# Querying Mount Locations of a Shared File System<a name="sfs_02_0025"></a>

## Function<a name="sc9565b85d20d4b76ac01cc09ae82ef6c"></a>

This API is used to query mount locations of a shared file system.

>![](/images/icon-note.gif) **NOTE:**   
>This API exists only when  **X-Openstack-Manila-Api-Version**  in the request header is greater than or equal to 2.9. The following is an example request sent by the  **curl**  command: curl -k -i -X GET https://192.168.196.47:8786/v2/13c7ff9a479c4e3599f4331d9e4a1835/shares/2a8c5470-d5d9-4fe1-b9fc-66a15a162e41/export\_locations  **-H "X-Openstack-Manila-Api-Version: 2.9"**  -H "X-Auth-Token: $token" -H "Accept: application/json"  

## URI<a name="scc4137b0ecc84a588627ed0283ef7582"></a>

-   GET /v2/\{project\_id\}/shares/\{share\_id\}/export\_locations
-   Parameter description

    <a name="tf151ace29f074f82b3db38c9d021a642"></a>
    <table><thead align="left"><tr id="r119e607827044610a1ce4f0e30f79e28"><th class="cellrowborder" valign="top" width="16.458354164583543%" id="mcps1.1.5.1.1"><p id="p17124101410431"><a name="p17124101410431"></a><a name="p17124101410431"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.408659134086594%" id="mcps1.1.5.1.2"><p id="p1612415146430"><a name="p1612415146430"></a><a name="p1612415146430"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.217978202179786%" id="mcps1.1.5.1.3"><p id="p312416148432"><a name="p312416148432"></a><a name="p312416148432"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="49.91500849915009%" id="mcps1.1.5.1.4"><p id="p3124181464318"><a name="p3124181464318"></a><a name="p3124181464318"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r5964eb14ebcf469da767c010cdbd35a1"><td class="cellrowborder" valign="top" width="16.458354164583543%" headers="mcps1.1.5.1.1 "><p id="acbabbd1114a74dde86b229e2d01592b7"><a name="acbabbd1114a74dde86b229e2d01592b7"></a><a name="acbabbd1114a74dde86b229e2d01592b7"></a>share_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.408659134086594%" headers="mcps1.1.5.1.2 "><p id="a28198f20e7214cfe8023b5ad067a5441"><a name="a28198f20e7214cfe8023b5ad067a5441"></a><a name="a28198f20e7214cfe8023b5ad067a5441"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.217978202179786%" headers="mcps1.1.5.1.3 "><p id="a04f245dda8dc4853b2b6a28c1ad280df"><a name="a04f245dda8dc4853b2b6a28c1ad280df"></a><a name="a04f245dda8dc4853b2b6a28c1ad280df"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.91500849915009%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0072841107_p24130518147"><a name="en-us_topic_0072841107_p24130518147"></a><a name="en-us_topic_0072841107_p24130518147"></a>Specifies the UUID of the shared file system.</p>
    </td>
    </tr>
    <tr id="r11bf0d0d2f5f4e7ca8d34f6c8449aebc"><td class="cellrowborder" valign="top" width="16.458354164583543%" headers="mcps1.1.5.1.1 "><p id="a7431bfa97a9c4c97925e447350878455"><a name="a7431bfa97a9c4c97925e447350878455"></a><a name="a7431bfa97a9c4c97925e447350878455"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.408659134086594%" headers="mcps1.1.5.1.2 "><p id="a51117b683e214b7387f9b9c323c3abbf"><a name="a51117b683e214b7387f9b9c323c3abbf"></a><a name="a51117b683e214b7387f9b9c323c3abbf"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.217978202179786%" headers="mcps1.1.5.1.3 "><p id="a5e09b054a39446f0a7813f37d73fc4bb"><a name="a5e09b054a39446f0a7813f37d73fc4bb"></a><a name="a5e09b054a39446f0a7813f37d73fc4bb"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.91500849915009%" headers="mcps1.1.5.1.4 "><p id="a09f81380795242328f7b3934b675d964"><a name="a09f81380795242328f7b3934b675d964"></a><a name="a09f81380795242328f7b3934b675d964"></a>Specifies the project ID of the operator.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="se53eee3721d54dba9584e7c60eb9cfd4"></a>

-   Parameter description

    None

-   Example request

    None


## Response<a name="sb0a4e7e02465467186f4eac387306edd"></a>

-   Parameter description

    <a name="t6b565351353d435e92d72b89912dd4df"></a>
    <table><thead align="left"><tr id="rb531a383fac5406fbdfd2a152560a594"><th class="cellrowborder" valign="top" width="26.950000000000003%" id="mcps1.1.4.1.1"><p id="p2358181315814"><a name="p2358181315814"></a><a name="p2358181315814"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.52%" id="mcps1.1.4.1.2"><p id="p12358913185815"><a name="p12358913185815"></a><a name="p12358913185815"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="52.53%" id="mcps1.1.4.1.3"><p id="p1137381314587"><a name="p1137381314587"></a><a name="p1137381314587"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r8ce8b00eacc747dd897a5834b2232c7a"><td class="cellrowborder" valign="top" width="26.950000000000003%" headers="mcps1.1.4.1.1 "><p id="a213419b985944d4bbc5f357b7b12aa85"><a name="a213419b985944d4bbc5f357b7b12aa85"></a><a name="a213419b985944d4bbc5f357b7b12aa85"></a>export_locations</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.52%" headers="mcps1.1.4.1.2 "><p id="a35ae2871e368471ab08d91e001f5f0a5"><a name="a35ae2871e368471ab08d91e001f5f0a5"></a><a name="a35ae2871e368471ab08d91e001f5f0a5"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.53%" headers="mcps1.1.4.1.3 "><p id="a7acade7e66b648be8946da108d4aab51"><a name="a7acade7e66b648be8946da108d4aab51"></a><a name="a7acade7e66b648be8946da108d4aab51"></a>Specifies the list of export locations.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Description of field  **export\_location**

    <a name="t466f2739b20d4f53abe4ad046e03f479"></a>
    <table><thead align="left"><tr id="r9f7fb68dbec848f3b74afe863b4622cb"><th class="cellrowborder" valign="top" width="18.84%" id="mcps1.1.4.1.1"><p id="p78741117115813"><a name="p78741117115813"></a><a name="p78741117115813"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.97%" id="mcps1.1.4.1.2"><p id="p887416172586"><a name="p887416172586"></a><a name="p887416172586"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="58.19%" id="mcps1.1.4.1.3"><p id="p987451775819"><a name="p987451775819"></a><a name="p987451775819"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r11e5443fcf8747a7a036b22104d1b976"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="a4f5fb4c4a6374b85b7fc9a98b0cc2127"><a name="a4f5fb4c4a6374b85b7fc9a98b0cc2127"></a><a name="a4f5fb4c4a6374b85b7fc9a98b0cc2127"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="a071408cb91ef44869f3954fec7b0c3f5"><a name="a071408cb91ef44869f3954fec7b0c3f5"></a><a name="a071408cb91ef44869f3954fec7b0c3f5"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="a7597ba3a14404ccc9bd6ef8939fd7a71"><a name="a7597ba3a14404ccc9bd6ef8939fd7a71"></a><a name="a7597ba3a14404ccc9bd6ef8939fd7a71"></a>Specifies the UUID of the mount location of the shared file system.</p>
    </td>
    </tr>
    <tr id="r2b5ad9e6bd29487aa4f1d0f6048c4d20"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="a30c02f6624ff48d780fd9b9aad8bee2b"><a name="a30c02f6624ff48d780fd9b9aad8bee2b"></a><a name="a30c02f6624ff48d780fd9b9aad8bee2b"></a>share_instance_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="a007fb95a7a0844fe94a4f8a1bb5c5718"><a name="a007fb95a7a0844fe94a4f8a1bb5c5718"></a><a name="a007fb95a7a0844fe94a4f8a1bb5c5718"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="ac7227f13ccd94bff9fd4b5c734d52c0a"><a name="ac7227f13ccd94bff9fd4b5c734d52c0a"></a><a name="ac7227f13ccd94bff9fd4b5c734d52c0a"></a>Specifies the UUID of the shared file system instance.</p>
    </td>
    </tr>
    <tr id="r3c308ab16a0942109d9947bd91b1cc6f"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="aff714311b21f4ecea647be7b2e32a190"><a name="aff714311b21f4ecea647be7b2e32a190"></a><a name="aff714311b21f4ecea647be7b2e32a190"></a>path</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="a6eab24e4204c4b2f80662bbbca377e64"><a name="a6eab24e4204c4b2f80662bbbca377e64"></a><a name="a6eab24e4204c4b2f80662bbbca377e64"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="af1fc35bd3f1d4fffb728ee033e406d6c"><a name="af1fc35bd3f1d4fffb728ee033e406d6c"></a><a name="af1fc35bd3f1d4fffb728ee033e406d6c"></a>Specifies the path to which the shared file system will be mounted.</p>
    </td>
    </tr>
    <tr id="re452c38520a64d59acec09b4cfeab24e"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="a9fc48bfdc4b34061a6566cde9c95216f"><a name="a9fc48bfdc4b34061a6566cde9c95216f"></a><a name="a9fc48bfdc4b34061a6566cde9c95216f"></a>is_admin_only</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="a536e6c077a2d493695ce7570427e6a07"><a name="a536e6c077a2d493695ce7570427e6a07"></a><a name="a536e6c077a2d493695ce7570427e6a07"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="a49c9c5cd7ed847ed8ec4944cc9ebfd8c"><a name="a49c9c5cd7ed847ed8ec4944cc9ebfd8c"></a><a name="a49c9c5cd7ed847ed8ec4944cc9ebfd8c"></a>Specifies whether the shared file system is only visible to administrators and its owner. Possible values are <strong id="b84235270611834"><a name="b84235270611834"></a><a name="b84235270611834"></a>true</strong> (only visible to administrators and its owner) and <strong id="b84235270611829"><a name="b84235270611829"></a><a name="b84235270611829"></a>false</strong> (visible to all users).</p>
    </td>
    </tr>
    <tr id="r4b61598e77a44112b694ccb715a692c4"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="abe315f4b0405410aaaa5a857c979b2f2"><a name="abe315f4b0405410aaaa5a857c979b2f2"></a><a name="abe315f4b0405410aaaa5a857c979b2f2"></a>preferred</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="aca0819a377ef4c24a8a4142aebabf123"><a name="aca0819a377ef4c24a8a4142aebabf123"></a><a name="aca0819a377ef4c24a8a4142aebabf123"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="a302833daed9744f3bc813db9a8db1154"><a name="a302833daed9744f3bc813db9a8db1154"></a><a name="a302833daed9744f3bc813db9a8db1154"></a>Identifies which mount locations are most efficient and are used preferentially when multiple mount locations exist.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    NFS share:

    ```
    {
      "export_locations": [
        {
          "path": "sfs-nas1.dong.com:/share-236b936a",
          "id": "b03d2aac-aeed-409a-af07-5d1b9024241c",
          "preferred": false
        }
      ]
    }
    ```

    CIFS share:

    ```
    {
      "export_locations": [
        {
          "path": "\\\\sfs-nas1.dong.com\\share-4e76e627",
          "id": "85eb5849-1a89-43ae-99ac-2e781514a228",
          "preferred": false
        }
      ]
    }
    ```


## Status Codes<a name="sd08ba73f065d437f92fca14d30df0b4e"></a>

-   Normal

    200

-   Abnormal

    <a name="t63883f904bd64a27a863345d914aec64"></a>
    <table><thead align="left"><tr id="redad891a904243d3ab39279798e6da21"><th class="cellrowborder" valign="top" width="43.43%" id="mcps1.1.3.1.1"><p id="a0a2b36124ef44791a32863743d9e29e2"><a name="a0a2b36124ef44791a32863743d9e29e2"></a><a name="a0a2b36124ef44791a32863743d9e29e2"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.57%" id="mcps1.1.3.1.2"><p id="en-us_topic_0072841107_p263515418147"><a name="en-us_topic_0072841107_p263515418147"></a><a name="en-us_topic_0072841107_p263515418147"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="re40bdaee0f184486b5f31a815a24e576"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="a083e91c0b8df43e08cfeb79a62923bd6"><a name="a083e91c0b8df43e08cfeb79a62923bd6"></a><a name="a083e91c0b8df43e08cfeb79a62923bd6"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0072841107_p125346718147"><a name="en-us_topic_0072841107_p125346718147"></a><a name="en-us_topic_0072841107_p125346718147"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="rb216fb9efde0473e8d19ca51969c7f15"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="aa63843b552c64a66b3317630274fb22b"><a name="aa63843b552c64a66b3317630274fb22b"></a><a name="aa63843b552c64a66b3317630274fb22b"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="a38c0ce5304ae40339dc6731e7738e2a7"><a name="a38c0ce5304ae40339dc6731e7738e2a7"></a><a name="a38c0ce5304ae40339dc6731e7738e2a7"></a>You must enter a username and the password to access the requested page.</p>
    </td>
    </tr>
    <tr id="raf230c82811e4e0fb90ce019a3fb807e"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0072841107_p246117518147"><a name="en-us_topic_0072841107_p246117518147"></a><a name="en-us_topic_0072841107_p246117518147"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="a7350ca43fcb14bd296228ba24e384bf5"><a name="a7350ca43fcb14bd296228ba24e384bf5"></a><a name="a7350ca43fcb14bd296228ba24e384bf5"></a>Access to the requested page is forbidden.</p>
    </td>
    </tr>
    <tr id="rb84ca596a41549509528f877bb6215d3"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="ad7d9aed838c64b48b63a9fd77fa6d9f0"><a name="ad7d9aed838c64b48b63a9fd77fa6d9f0"></a><a name="ad7d9aed838c64b48b63a9fd77fa6d9f0"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="a8bc00eafeaa0448d89a7dd26177f79f6"><a name="a8bc00eafeaa0448d89a7dd26177f79f6"></a><a name="a8bc00eafeaa0448d89a7dd26177f79f6"></a>The requested page was not found.</p>
    </td>
    </tr>
    </tbody>
    </table>


