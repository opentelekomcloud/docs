# Creating a Snapshot<a name="dws_02_0026"></a>

## Function<a name="sca64f36627a3417bbeb0c43855a40ce7"></a>

This API is used to create snapshots for a specified cluster.

## URI<a name="s79bb432d7cfa4d6ba3fe910602033e78"></a>

-   URI format

    POST /v1.0/\{project\_id\}/snapshots

-   Parameter description

    **Table  1**  URI parameter description

    <a name="t877e0dac894f448f87cc0782da0ae4a4"></a>
    <table><thead align="left"><tr id="r91eb15e2eb394521bdd6a7d42d36b68c"><th class="cellrowborder" valign="top" width="21.43%" id="mcps1.2.5.1.1"><p id="af98c37784bf6478b8638e51591fdbaa2"><a name="af98c37784bf6478b8638e51591fdbaa2"></a><a name="af98c37784bf6478b8638e51591fdbaa2"></a><strong id="b84235270617228"><a name="b84235270617228"></a><a name="b84235270617228"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="29.59%" id="mcps1.2.5.1.2"><p id="a5332e63e3c1348f4893ed5a46e9054ad"><a name="a5332e63e3c1348f4893ed5a46e9054ad"></a><a name="a5332e63e3c1348f4893ed5a46e9054ad"></a><strong id="b6167984116271"><a name="b6167984116271"></a><a name="b6167984116271"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.37%" id="mcps1.2.5.1.3"><p id="a76fb4bdd350545839ea670ef978f82b9"><a name="a76fb4bdd350545839ea670ef978f82b9"></a><a name="a76fb4bdd350545839ea670ef978f82b9"></a><strong id="b84235270617235"><a name="b84235270617235"></a><a name="b84235270617235"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="30.61%" id="mcps1.2.5.1.4"><p id="a36d2b446e91f40669768b2b4b1af1b2c"><a name="a36d2b446e91f40669768b2b4b1af1b2c"></a><a name="a36d2b446e91f40669768b2b4b1af1b2c"></a><strong id="b842352706172443"><a name="b842352706172443"></a><a name="b842352706172443"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r17094096c94e41c08fb927c01b191b6c"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.2.5.1.1 "><p id="a843feba0476744298eb5f8e2b1f975bd"><a name="a843feba0476744298eb5f8e2b1f975bd"></a><a name="a843feba0476744298eb5f8e2b1f975bd"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.59%" headers="mcps1.2.5.1.2 "><p id="ab8f64bdd2c7444e28c7a415c2331b54b"><a name="ab8f64bdd2c7444e28c7a415c2331b54b"></a><a name="ab8f64bdd2c7444e28c7a415c2331b54b"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.5.1.3 "><p id="ac4291dc3fa3c46f3852e35622bab1bb5"><a name="ac4291dc3fa3c46f3852e35622bab1bb5"></a><a name="ac4291dc3fa3c46f3852e35622bab1bb5"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.61%" headers="mcps1.2.5.1.4 "><p id="p14202648155510"><a name="p14202648155510"></a><a name="p14202648155510"></a>Project ID. For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="s21224531b3af41768965da75256b6574"></a>

-   Sample request

    ```
    POST /v1.0/89cd04f168b84af6be287f71730fdb4b/snapshots
    {
        "snapshot": {
           "name": "snapshot-3",
           "cluster_id": "44b277eb-39be-4921-be31-3d61b43651d7",
           "description": "Snapshot-3 description"
         }
    }
    ```


-   Parameter description

    **Table  2**  Request parameter description

    <a name="te0498183a8d548b18ee84355358fa428"></a>
    <table><thead align="left"><tr id="r3316ed90298844498b050212dc42697e"><th class="cellrowborder" valign="top" width="19.39%" id="mcps1.2.5.1.1"><p id="af4974efcb8a2461283025ad83d1f368c"><a name="af4974efcb8a2461283025ad83d1f368c"></a><a name="af4974efcb8a2461283025ad83d1f368c"></a><strong id="b2100984300"><a name="b2100984300"></a><a name="b2100984300"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.43%" id="mcps1.2.5.1.2"><p id="a9391ebe7e476442d888f9616c6bbc4f2"><a name="a9391ebe7e476442d888f9616c6bbc4f2"></a><a name="a9391ebe7e476442d888f9616c6bbc4f2"></a><strong id="b781889678"><a name="b781889678"></a><a name="b781889678"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23.47%" id="mcps1.2.5.1.3"><p id="ab485b8c919cd4cd9b4181f997ffbe7aa"><a name="ab485b8c919cd4cd9b4181f997ffbe7aa"></a><a name="ab485b8c919cd4cd9b4181f997ffbe7aa"></a><strong id="b2070782583"><a name="b2070782583"></a><a name="b2070782583"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="35.709999999999994%" id="mcps1.2.5.1.4"><p id="a91eb8ef942f9471393f7f5ef2490cfdc"><a name="a91eb8ef942f9471393f7f5ef2490cfdc"></a><a name="a91eb8ef942f9471393f7f5ef2490cfdc"></a><strong id="b1884913126"><a name="b1884913126"></a><a name="b1884913126"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r8f20dcf2fb324a04a84318495ec2cd34"><td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.2.5.1.1 "><p id="aa6cd5074e4834ec1bc90f073c0c3b72d"><a name="aa6cd5074e4834ec1bc90f073c0c3b72d"></a><a name="aa6cd5074e4834ec1bc90f073c0c3b72d"></a>snapshot</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.2.5.1.2 "><p id="a74e20aa1255b420aa615fc68846712e7"><a name="a74e20aa1255b420aa615fc68846712e7"></a><a name="a74e20aa1255b420aa615fc68846712e7"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.47%" headers="mcps1.2.5.1.3 "><p id="ab14b184fdeb1452882bcb7b8cc6c29dc"><a name="ab14b184fdeb1452882bcb7b8cc6c29dc"></a><a name="ab14b184fdeb1452882bcb7b8cc6c29dc"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.709999999999994%" headers="mcps1.2.5.1.4 "><p id="aa65bd0e9e4ba485b9b8dfd1c1398aa16"><a name="aa65bd0e9e4ba485b9b8dfd1c1398aa16"></a><a name="aa65bd0e9e4ba485b9b8dfd1c1398aa16"></a>Snapshot object</p>
    </td>
    </tr>
    <tr id="r50b8f38bad4f486fa20079d5f77c9f5a"><td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.2.5.1.1 "><p id="abc3b956da9374a9dbced73fc0ee6266b"><a name="abc3b956da9374a9dbced73fc0ee6266b"></a><a name="abc3b956da9374a9dbced73fc0ee6266b"></a>cluster_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.2.5.1.2 "><p id="a144e6678f7564a9a8099cbe25f6247b0"><a name="a144e6678f7564a9a8099cbe25f6247b0"></a><a name="a144e6678f7564a9a8099cbe25f6247b0"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.47%" headers="mcps1.2.5.1.3 "><p id="a05a9783d162c48b09d9ce4090b0b11fa"><a name="a05a9783d162c48b09d9ce4090b0b11fa"></a><a name="a05a9783d162c48b09d9ce4090b0b11fa"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.709999999999994%" headers="mcps1.2.5.1.4 "><p id="a61ba158db3004568919c03eb6ee1611c"><a name="a61ba158db3004568919c03eb6ee1611c"></a><a name="a61ba158db3004568919c03eb6ee1611c"></a>ID of the cluster for which you want to create a snapshot</p>
    </td>
    </tr>
    <tr id="r6f380676c5cc4d93ba5020ed27fc7f20"><td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.2.5.1.1 "><p id="a6d07c0acbb8a4d069847b117e1cd1058"><a name="a6d07c0acbb8a4d069847b117e1cd1058"></a><a name="a6d07c0acbb8a4d069847b117e1cd1058"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.2.5.1.2 "><p id="a997eab9b86fb4188bbf1bc7a5e5b85be"><a name="a997eab9b86fb4188bbf1bc7a5e5b85be"></a><a name="a997eab9b86fb4188bbf1bc7a5e5b85be"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.47%" headers="mcps1.2.5.1.3 "><p id="a0f2e6c775ca44ff489c1f75c87ec005a"><a name="a0f2e6c775ca44ff489c1f75c87ec005a"></a><a name="a0f2e6c775ca44ff489c1f75c87ec005a"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.709999999999994%" headers="mcps1.2.5.1.4 "><p id="a8834ba35308f45098c2ca03ff4574a8b"><a name="a8834ba35308f45098c2ca03ff4574a8b"></a><a name="a8834ba35308f45098c2ca03ff4574a8b"></a>Snapshot name, which must be unique and start with a letter. It consists of 4 to 64 characters, which are case-insensitive and contain letters, digits, hyphens (-), and underscores (_) only.</p>
    </td>
    </tr>
    <tr id="r2e28b29d8f63419ba5032a31fd022b3e"><td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.2.5.1.1 "><p id="aa903c270161d46acac2b24a7a2446016"><a name="aa903c270161d46acac2b24a7a2446016"></a><a name="aa903c270161d46acac2b24a7a2446016"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.2.5.1.2 "><p id="aa1921961171a4bef8f45fe98ff592580"><a name="aa1921961171a4bef8f45fe98ff592580"></a><a name="aa1921961171a4bef8f45fe98ff592580"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.47%" headers="mcps1.2.5.1.3 "><p id="a0876ad8f680b4e469d03b5c586c3e070"><a name="a0876ad8f680b4e469d03b5c586c3e070"></a><a name="a0876ad8f680b4e469d03b5c586c3e070"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.709999999999994%" headers="mcps1.2.5.1.4 "><p id="a6d943823e61d4ae0ab542cf6f54c3e2b"><a name="a6d943823e61d4ae0ab542cf6f54c3e2b"></a><a name="a6d943823e61d4ae0ab542cf6f54c3e2b"></a>Snapshot description. If no value is specified, the description is empty.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Response<a name="s74ab9ad56efb4dddbd3dd843c2374513"></a>

-   Sample response

    ```
    STATUS CODE 200
    {
        "snapshot": {
            "id": "2a4d0f86-67cd-408a-8b66-017454fb7793"
        }
    }
    ```

-   Parameter description

    **Table  3**  Response parameter description

    <a name="tfecb235e184446e6aa31978fd84e85b1"></a>
    <table><thead align="left"><tr id="rdc5eb16b88304fc0a963686eaa2c59f7"><th class="cellrowborder" valign="top" width="18.36816318368163%" id="mcps1.2.5.1.1"><p id="ab8381a5a7de3429eae536e912ede30b4"><a name="ab8381a5a7de3429eae536e912ede30b4"></a><a name="ab8381a5a7de3429eae536e912ede30b4"></a><strong id="b921485034"><a name="b921485034"></a><a name="b921485034"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.447755224477554%" id="mcps1.2.5.1.2"><p id="a988f3372360a41f1a76a7c546788b5bf"><a name="a988f3372360a41f1a76a7c546788b5bf"></a><a name="a988f3372360a41f1a76a7c546788b5bf"></a><strong id="b879575268"><a name="b879575268"></a><a name="b879575268"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15.308469153084694%" id="mcps1.2.5.1.3"><p id="a800f707ea50b43bd8263c4fd32a8a8ba"><a name="a800f707ea50b43bd8263c4fd32a8a8ba"></a><a name="a800f707ea50b43bd8263c4fd32a8a8ba"></a><strong id="b1513553480"><a name="b1513553480"></a><a name="b1513553480"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43.87561243875613%" id="mcps1.2.5.1.4"><p id="a366b83bf32f646469515eb2e80d88f62"><a name="a366b83bf32f646469515eb2e80d88f62"></a><a name="a366b83bf32f646469515eb2e80d88f62"></a><strong id="b590978399"><a name="b590978399"></a><a name="b590978399"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r7aec5e9f707b4aecb31afac0631ad0e8"><td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.1 "><p id="af1268864da1a4f7f8dbe4b0676e0aab7"><a name="af1268864da1a4f7f8dbe4b0676e0aab7"></a><a name="af1268864da1a4f7f8dbe4b0676e0aab7"></a>snapshot</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.447755224477554%" headers="mcps1.2.5.1.2 "><p id="ada5d179e8ecf4d7f9eb02185177b33db"><a name="ada5d179e8ecf4d7f9eb02185177b33db"></a><a name="ada5d179e8ecf4d7f9eb02185177b33db"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.3 "><p id="a8c3a138112194288bd7f74fcb8cef768"><a name="a8c3a138112194288bd7f74fcb8cef768"></a><a name="a8c3a138112194288bd7f74fcb8cef768"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.87561243875613%" headers="mcps1.2.5.1.4 "><p id="a14f353402a624aa8932d3187d2f04960"><a name="a14f353402a624aa8932d3187d2f04960"></a><a name="a14f353402a624aa8932d3187d2f04960"></a>Snapshot object</p>
    </td>
    </tr>
    <tr id="rfa8576ca9bd54758b94e9216b7fd5963"><td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.1 "><p id="a0735ace9c1314d629d943fd4bdf51243"><a name="a0735ace9c1314d629d943fd4bdf51243"></a><a name="a0735ace9c1314d629d943fd4bdf51243"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.447755224477554%" headers="mcps1.2.5.1.2 "><p id="aa999f9d7f69f46b2a54b51367d931594"><a name="aa999f9d7f69f46b2a54b51367d931594"></a><a name="aa999f9d7f69f46b2a54b51367d931594"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.3 "><p id="a95923db2cb6d40ec9bdbb69e53c0781f"><a name="a95923db2cb6d40ec9bdbb69e53c0781f"></a><a name="a95923db2cb6d40ec9bdbb69e53c0781f"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.87561243875613%" headers="mcps1.2.5.1.4 "><p id="a19d83838bedc4635a1d34a68074109ba"><a name="a19d83838bedc4635a1d34a68074109ba"></a><a name="a19d83838bedc4635a1d34a68074109ba"></a>Snapshot ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Returned Values<a name="s763e6683944443b1a55793807c544818"></a>

-   Normal

    200

-   Abnormal 

    **Table  4**  Returned value description

    <a name="t1abefdff89ea4e27b3e5f7d7a5ec1fa9"></a>
    <table><thead align="left"><tr id="rd7dfd8d64b954a16a4a56cade6193a6c"><th class="cellrowborder" valign="top" width="46.46%" id="mcps1.2.3.1.1"><p id="a310555cdf51a47ec9666c91d4a5fe6f1"><a name="a310555cdf51a47ec9666c91d4a5fe6f1"></a><a name="a310555cdf51a47ec9666c91d4a5fe6f1"></a><strong id="b842352706104658"><a name="b842352706104658"></a><a name="b842352706104658"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.54%" id="mcps1.2.3.1.2"><p id="a5374003c95794b41b8e093fe8349c8b1"><a name="a5374003c95794b41b8e093fe8349c8b1"></a><a name="a5374003c95794b41b8e093fe8349c8b1"></a><strong id="b297757054"><a name="b297757054"></a><a name="b297757054"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r966aab4dd72c469d9f67a7a628c75279"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.2.3.1.1 "><p id="af4ae7e74b61a4c88a709a9634e381731"><a name="af4ae7e74b61a4c88a709a9634e381731"></a><a name="af4ae7e74b61a4c88a709a9634e381731"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.2.3.1.2 "><p id="a508dc5f7ae3145c1a0ab59c7a59175a6"><a name="a508dc5f7ae3145c1a0ab59c7a59175a6"></a><a name="a508dc5f7ae3145c1a0ab59c7a59175a6"></a>Request error.</p>
    </td>
    </tr>
    <tr id="r90009ad515fb4e789e9caee1a11fcf6b"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.2.3.1.1 "><p id="a78ec7d4b7eb442d4810eed0cad311e72"><a name="a78ec7d4b7eb442d4810eed0cad311e72"></a><a name="a78ec7d4b7eb442d4810eed0cad311e72"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.2.3.1.2 "><p id="ae8ab0533d27a42ec881a7a4edfa5acb4"><a name="ae8ab0533d27a42ec881a7a4edfa5acb4"></a><a name="ae8ab0533d27a42ec881a7a4edfa5acb4"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="rf1eeda5d71714397976d7bbd0c607077"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.2.3.1.1 "><p id="a113ccbee51324030ac46e1d94bebd5da"><a name="a113ccbee51324030ac46e1d94bebd5da"></a><a name="a113ccbee51324030ac46e1d94bebd5da"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.2.3.1.2 "><p id="a31f8f1d166774434a7d8567bd814dfdc"><a name="a31f8f1d166774434a7d8567bd814dfdc"></a><a name="a31f8f1d166774434a7d8567bd814dfdc"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="rdcbc82cf07414082bd244295a1c1be7b"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.2.3.1.1 "><p id="ad4429862c4874402b6d52f39df7cab3f"><a name="ad4429862c4874402b6d52f39df7cab3f"></a><a name="ad4429862c4874402b6d52f39df7cab3f"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.2.3.1.2 "><p id="a69dd1d22496a4112876ab4a55fae0837"><a name="a69dd1d22496a4112876ab4a55fae0837"></a><a name="a69dd1d22496a4112876ab4a55fae0837"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="rca892f0504d04aec843be64d6acc9741"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.2.3.1.1 "><p id="a4689343b3f2e43e292f664328e1aa0e1"><a name="a4689343b3f2e43e292f664328e1aa0e1"></a><a name="a4689343b3f2e43e292f664328e1aa0e1"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.2.3.1.2 "><p id="a65e553c1b6c246b69e513013846ed8f4"><a name="a65e553c1b6c246b69e513013846ed8f4"></a><a name="a65e553c1b6c246b69e513013846ed8f4"></a>Internal service error.</p>
    </td>
    </tr>
    <tr id="r9d1910b3d4eb45e08fd83c3103393a44"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.2.3.1.1 "><p id="aa0aafbeab1434aff99e14c59ed1d9048"><a name="aa0aafbeab1434aff99e14c59ed1d9048"></a><a name="aa0aafbeab1434aff99e14c59ed1d9048"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.2.3.1.2 "><p id="ae6f38fda718241b99a301927f3733f1b"><a name="ae6f38fda718241b99a301927f3733f1b"></a><a name="ae6f38fda718241b99a301927f3733f1b"></a>The service is unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


