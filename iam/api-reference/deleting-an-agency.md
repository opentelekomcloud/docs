# Deleting an Agency<a name="en-us_topic_0079467625"></a>

## Function Description<a name="sb6596dc8b5f44731a92c8b950ee95e38"></a>

This interface is used to delete an agency.

## URI<a name="se12ea354d7df4a2f89999cc32c337dd7"></a>

-   URI format

    DELETE /v3.0/OS-AGENCY/agencies/\{agency\_id\}


-   URI parameter description

    <a name="t9160453da6c646bab98ddb409718d030"></a>
    <table><thead align="left"><tr id="r0790258fcb724e31999bd0c4f0f7cd8e"><th class="cellrowborder" valign="top" width="18.360000000000003%" id="mcps1.1.5.1.1"><p id="a8b4497ec357e417eae3508dcc05bfdda"><a name="a8b4497ec357e417eae3508dcc05bfdda"></a><a name="a8b4497ec357e417eae3508dcc05bfdda"></a><strong id="en-us_topic_0026586105_b842352706143612"><a name="en-us_topic_0026586105_b842352706143612"></a><a name="en-us_topic_0026586105_b842352706143612"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.48%" id="mcps1.1.5.1.2"><p id="a27e14d6572df4c69a0f4d68b18602437"><a name="a27e14d6572df4c69a0f4d68b18602437"></a><a name="a27e14d6572df4c69a0f4d68b18602437"></a><strong id="b842352706161940"><a name="b842352706161940"></a><a name="b842352706161940"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.86%" id="mcps1.1.5.1.3"><p id="aa372e51be903421da30b54b77c6ce29c"><a name="aa372e51be903421da30b54b77c6ce29c"></a><a name="aa372e51be903421da30b54b77c6ce29c"></a><strong id="b842352706143526"><a name="b842352706143526"></a><a name="b842352706143526"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.3%" id="mcps1.1.5.1.4"><p id="aed93ee8738a643fdaae6aed295844ab2"><a name="aed93ee8738a643fdaae6aed295844ab2"></a><a name="aed93ee8738a643fdaae6aed295844ab2"></a><strong id="b20601766145329"><a name="b20601766145329"></a><a name="b20601766145329"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r3438217c55c7410fa66f7d1dc61d35d7"><td class="cellrowborder" valign="top" width="18.360000000000003%" headers="mcps1.1.5.1.1 "><p id="a1a21bcca29fe4ef1b7b752484f32330e"><a name="a1a21bcca29fe4ef1b7b752484f32330e"></a><a name="a1a21bcca29fe4ef1b7b752484f32330e"></a>agency_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.5.1.2 "><p id="af4b82dfe9d5b411bab7fc415e602ed72"><a name="af4b82dfe9d5b411bab7fc415e602ed72"></a><a name="af4b82dfe9d5b411bab7fc415e602ed72"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.1.5.1.3 "><p id="a2912d1342d76422e839f3d24b6dc912d"><a name="a2912d1342d76422e839f3d24b6dc912d"></a><a name="a2912d1342d76422e839f3d24b6dc912d"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.3%" headers="mcps1.1.5.1.4 "><p id="afc3d3b18f93c4b2997ef7cefda5e5a8a"><a name="afc3d3b18f93c4b2997ef7cefda5e5a8a"></a><a name="afc3d3b18f93c4b2997ef7cefda5e5a8a"></a>ID of an agency.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="s6b7ffda07dd44957b5fb7f306b13a924"></a>

-   Request header parameter description

    <a name="tf116769063204d7596eaaa9fd057926d"></a>
    <table><thead align="left"><tr id="r8e25bcd7ed0d474cb19289b1da801b23"><th class="cellrowborder" valign="top" width="19.36%" id="mcps1.1.5.1.1"><p id="aa20bfca9bf01411ba9cf7ea09be73cba"><a name="aa20bfca9bf01411ba9cf7ea09be73cba"></a><a name="aa20bfca9bf01411ba9cf7ea09be73cba"></a><strong id="b775932645"><a name="b775932645"></a><a name="b775932645"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.73%" id="mcps1.1.5.1.2"><p id="aa8f2b48d9a0a411098dd2e918ed50bc7"><a name="aa8f2b48d9a0a411098dd2e918ed50bc7"></a><a name="aa8f2b48d9a0a411098dd2e918ed50bc7"></a><strong id="b84235270616358"><a name="b84235270616358"></a><a name="b84235270616358"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.46%" id="mcps1.1.5.1.3"><p id="ad81c2db9fab54416942d17d4054153fa"><a name="ad81c2db9fab54416942d17d4054153fa"></a><a name="ad81c2db9fab54416942d17d4054153fa"></a><strong id="b1283822302"><a name="b1283822302"></a><a name="b1283822302"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.45%" id="mcps1.1.5.1.4"><p id="ade539319fe5544b884685f354ea18b1f"><a name="ade539319fe5544b884685f354ea18b1f"></a><a name="ade539319fe5544b884685f354ea18b1f"></a><strong id="b2036566434"><a name="b2036566434"></a><a name="b2036566434"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r1bc4074380ce4caa98258b006d937e2f"><td class="cellrowborder" valign="top" width="19.36%" headers="mcps1.1.5.1.1 "><p id="a1a0a073e17de4254a5904d17faaf54b7"><a name="a1a0a073e17de4254a5904d17faaf54b7"></a><a name="a1a0a073e17de4254a5904d17faaf54b7"></a>Content-Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.1.5.1.2 "><p id="a81855a86cedb4c1bbdcb03de8c7ef87d"><a name="a81855a86cedb4c1bbdcb03de8c7ef87d"></a><a name="a81855a86cedb4c1bbdcb03de8c7ef87d"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.46%" headers="mcps1.1.5.1.3 "><p id="af506635a79744dcb85881210222edcc4"><a name="af506635a79744dcb85881210222edcc4"></a><a name="af506635a79744dcb85881210222edcc4"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.45%" headers="mcps1.1.5.1.4 "><p id="a6f7c37f5f0704523b61136a4d1e72a7b"><a name="a6f7c37f5f0704523b61136a4d1e72a7b"></a><a name="a6f7c37f5f0704523b61136a4d1e72a7b"></a>Fill <strong id="b842352706161331"><a name="b842352706161331"></a><a name="b842352706161331"></a>application/json;charset=utf8</strong> in this field.</p>
    </td>
    </tr>
    <tr id="r8022c5e431104b75841d73f8bf0d83b5"><td class="cellrowborder" valign="top" width="19.36%" headers="mcps1.1.5.1.1 "><p id="a96f588d7ea674791961c78d8b7469fe5"><a name="a96f588d7ea674791961c78d8b7469fe5"></a><a name="a96f588d7ea674791961c78d8b7469fe5"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.1.5.1.2 "><p id="ae1c8f8b729084269b159f1d491513b17"><a name="ae1c8f8b729084269b159f1d491513b17"></a><a name="ae1c8f8b729084269b159f1d491513b17"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.46%" headers="mcps1.1.5.1.3 "><p id="ab6dd06b9fe6c43a8bda64189dc5aeb29"><a name="ab6dd06b9fe6c43a8bda64189dc5aeb29"></a><a name="ab6dd06b9fe6c43a8bda64189dc5aeb29"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.45%" headers="mcps1.1.5.1.4 "><p id="a6f8a4cec8b1e4540ba921ba50f5ba3a3"><a name="a6f8a4cec8b1e4540ba921ba50f5ba3a3"></a><a name="a6f8a4cec8b1e4540ba921ba50f5ba3a3"></a>Authenticated token with the <strong id="b750798910387"><a name="b750798910387"></a><a name="b750798910387"></a>Security Administrator</strong> permission.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Sample request

    ```
    curl -i -k -H "X-Auth-Token:$token" -H 'Content-Type:application/json;charset=utf8' -X DELETE https://sample.domain.com/v3.0/OS-AGENCY/agencies/2809756f748a46e2b92d58d309f67291
    ```


## Response<a name="sbc04ebdb940349d9a2107d5041800789"></a>

-   Sample response \(request failed\)

    ```
    {
        "error": {
            "message": "Could not find agency: 2809756f748a46e2b92d58d309f67291",
            "code": 404,
            "title": "Not Found"
        }
    }
    ```


## **Status Codes**<a name="sdfa0d1f63be8432287f6ecc0fe4b91c5"></a>

<a name="tc7141067802c43ef881aa22220820fb7"></a>
<table><thead align="left"><tr id="ra753c762e52944509247ce977b72ae90"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="afcb83520d064464dabb3441e86ae7486"><a name="afcb83520d064464dabb3441e86ae7486"></a><a name="afcb83520d064464dabb3441e86ae7486"></a><strong id="b691157769"><a name="b691157769"></a><a name="b691157769"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="a38c9798d04d94fe0819e20aaaa6cc5ec"><a name="a38c9798d04d94fe0819e20aaaa6cc5ec"></a><a name="a38c9798d04d94fe0819e20aaaa6cc5ec"></a><strong id="b265942355"><a name="b265942355"></a><a name="b265942355"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r35129cb7e9e24827b7a08134ae4a3fc3"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="ab1c9a58498d14deb910e2679dc8884b0"><a name="ab1c9a58498d14deb910e2679dc8884b0"></a><a name="ab1c9a58498d14deb910e2679dc8884b0"></a>204</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="ac2a02d868a9a4f3489e5e18374329c3a"><a name="ac2a02d868a9a4f3489e5e18374329c3a"></a><a name="ac2a02d868a9a4f3489e5e18374329c3a"></a>The request is successful.</p>
</td>
</tr>
<tr id="rea238a1492f74494aba7c5bbfc11e13d"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a21d8c4bd30e042469ed07bee172d2858"><a name="a21d8c4bd30e042469ed07bee172d2858"></a><a name="a21d8c4bd30e042469ed07bee172d2858"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a34e556791e6f40ff8ac68110192a21f1"><a name="a34e556791e6f40ff8ac68110192a21f1"></a><a name="a34e556791e6f40ff8ac68110192a21f1"></a>You must enter a username and password to access the requested page.</p>
</td>
</tr>
<tr id="rb960e9f524b9467ea13bfef36fe20a86"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a5c605ca12e0b40be89ebe65ba66f49f4"><a name="a5c605ca12e0b40be89ebe65ba66f49f4"></a><a name="a5c605ca12e0b40be89ebe65ba66f49f4"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a43d3636287fc476a9e1de01fd9101d24"><a name="a43d3636287fc476a9e1de01fd9101d24"></a><a name="a43d3636287fc476a9e1de01fd9101d24"></a>You are forbidden to access the requested page.</p>
</td>
</tr>
<tr id="r200e6dc59b404ee3b10f0ee3c30a93a3"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="ae3268a5f33df48649e441d3c426f2a65"><a name="ae3268a5f33df48649e441d3c426f2a65"></a><a name="ae3268a5f33df48649e441d3c426f2a65"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="acbfcfb3f66b34dab8ee8f165b0946232"><a name="acbfcfb3f66b34dab8ee8f165b0946232"></a><a name="acbfcfb3f66b34dab8ee8f165b0946232"></a>The server could not find the requested page.</p>
</td>
</tr>
<tr id="r7bde0cda122243379e138695a0dc77c8"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="ab44cab09ac2c4f87b312aedb8fc7ca26"><a name="ab44cab09ac2c4f87b312aedb8fc7ca26"></a><a name="ab44cab09ac2c4f87b312aedb8fc7ca26"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a1c3f6fd876f8434c8b5c993667fbf707"><a name="a1c3f6fd876f8434c8b5c993667fbf707"></a><a name="a1c3f6fd876f8434c8b5c993667fbf707"></a>Failed to complete the request because of an internal service error.</p>
</td>
</tr>
</tbody>
</table>

