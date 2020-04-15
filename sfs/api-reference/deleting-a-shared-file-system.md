# Deleting a Shared File System<a name="sfs_02_0027"></a>

## Function<a name="s756a340c47e0467f98ab7c716a729342"></a>

This API is used to delete a shared file system.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>This API is an asynchronous API. If the returned status code is  **202**, the API request is successfully delivered and received. Later, you can query the shared file system by referring to  [Querying Details About a Shared File System](querying-details-about-a-shared-file-system.md)  to identify whether the deletion is complete and successful.  

## URI<a name="s6574f11230c74ddaa20136feed374db1"></a>

-   DELETE /v2/\{project\_id\}/shares/\{share\_id\}
-   Parameter description

    <a name="t1456ab35816344b8a76e36c773441dff"></a>
    <table><thead align="left"><tr id="r753a0263858a4c31a49be8a5ec591070"><th class="cellrowborder" valign="top" width="17.62%" id="mcps1.1.5.1.1"><p id="p17124101410431"><a name="p17124101410431"></a><a name="p17124101410431"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.62%" id="mcps1.1.5.1.2"><p id="p1612415146430"><a name="p1612415146430"></a><a name="p1612415146430"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.88%" id="mcps1.1.5.1.3"><p id="p312416148432"><a name="p312416148432"></a><a name="p312416148432"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="47.88%" id="mcps1.1.5.1.4"><p id="p3124181464318"><a name="p3124181464318"></a><a name="p3124181464318"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="rdc75ac94fac44a67a0ec925cb48bb63f"><td class="cellrowborder" valign="top" width="17.62%" headers="mcps1.1.5.1.1 "><p id="a0742d2efba12435e91866628388ffcec"><a name="a0742d2efba12435e91866628388ffcec"></a><a name="a0742d2efba12435e91866628388ffcec"></a>share_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.62%" headers="mcps1.1.5.1.2 "><p id="a4c0a9dd339964ad3adfcbff066294968"><a name="a4c0a9dd339964ad3adfcbff066294968"></a><a name="a4c0a9dd339964ad3adfcbff066294968"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.88%" headers="mcps1.1.5.1.3 "><p id="a8af9c62e72624886b917ce668a7437f4"><a name="a8af9c62e72624886b917ce668a7437f4"></a><a name="a8af9c62e72624886b917ce668a7437f4"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.88%" headers="mcps1.1.5.1.4 "><p id="a238f3a91d5014043836c8907e47dce2f"><a name="a238f3a91d5014043836c8907e47dce2f"></a><a name="a238f3a91d5014043836c8907e47dce2f"></a>Specifies the UUID of the shared file system.</p>
    </td>
    </tr>
    <tr id="r069cb350c1b547adb6d40dadcddddfcb"><td class="cellrowborder" valign="top" width="17.62%" headers="mcps1.1.5.1.1 "><p id="ab20f7ae58a56489ea61c3e68d662ca37"><a name="ab20f7ae58a56489ea61c3e68d662ca37"></a><a name="ab20f7ae58a56489ea61c3e68d662ca37"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.62%" headers="mcps1.1.5.1.2 "><p id="a6e22414afbe04ff79f3165c0249b43c2"><a name="a6e22414afbe04ff79f3165c0249b43c2"></a><a name="a6e22414afbe04ff79f3165c0249b43c2"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.88%" headers="mcps1.1.5.1.3 "><p id="ac6fa3b3eee82486c975a26a1df39dc4e"><a name="ac6fa3b3eee82486c975a26a1df39dc4e"></a><a name="ac6fa3b3eee82486c975a26a1df39dc4e"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.88%" headers="mcps1.1.5.1.4 "><p id="a4aa4e6fe53a941cd886a5f622400d338"><a name="a4aa4e6fe53a941cd886a5f622400d338"></a><a name="a4aa4e6fe53a941cd886a5f622400d338"></a>Specifies the project ID of the operator.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="sa79c834e019e4d1b9e7e6ddcec17f188"></a>

-   Parameter description

    None

-   Example request

    None


## Response<a name="s973f9cf407084187b1462c24e6cfc559"></a>

-   Example response

    None


## Status Codes<a name="sb9645d68c18a41e199286add50b318d0"></a>

-   Normal

    202

-   Abnormal

    <a name="t605dedf2056942d7a3b5370b25f20953"></a>
    <table><thead align="left"><tr id="r1462f8482a0440799e925fe066aa655c"><th class="cellrowborder" valign="top" width="43.43%" id="mcps1.1.3.1.1"><p id="a241187a617084a2f8d29138b71c184d2"><a name="a241187a617084a2f8d29138b71c184d2"></a><a name="a241187a617084a2f8d29138b71c184d2"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.57%" id="mcps1.1.3.1.2"><p id="ab13d2981d9304e10bab22faf617a38b6"><a name="ab13d2981d9304e10bab22faf617a38b6"></a><a name="ab13d2981d9304e10bab22faf617a38b6"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r095526b0e6e146d9ac72e98f49b82bba"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="ae4188d1edfb14129908e073964c9e452"><a name="ae4188d1edfb14129908e073964c9e452"></a><a name="ae4188d1edfb14129908e073964c9e452"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="a5c4cecd2d76741f59bf80dc7672329dc"><a name="a5c4cecd2d76741f59bf80dc7672329dc"></a><a name="a5c4cecd2d76741f59bf80dc7672329dc"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="rad4c5f78b8b04bc2aeb77ac628ae2da7"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="a9db0a604367a4dd9bc88285b85a53576"><a name="a9db0a604367a4dd9bc88285b85a53576"></a><a name="a9db0a604367a4dd9bc88285b85a53576"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="a2969b237598f40e98b7ee768eb3115c8"><a name="a2969b237598f40e98b7ee768eb3115c8"></a><a name="a2969b237598f40e98b7ee768eb3115c8"></a>You must enter a username and the password to access the requested page.</p>
    </td>
    </tr>
    <tr id="r14bebf3708884b48a86824800722d2c1"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="a658cd49d9e264c40b43d2b8f93c3eb1e"><a name="a658cd49d9e264c40b43d2b8f93c3eb1e"></a><a name="a658cd49d9e264c40b43d2b8f93c3eb1e"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="ac691cb9769e444a1bdcd2732df22fc6b"><a name="ac691cb9769e444a1bdcd2732df22fc6b"></a><a name="ac691cb9769e444a1bdcd2732df22fc6b"></a>Access to the requested page is forbidden.</p>
    </td>
    </tr>
    <tr id="r84d245962a1e4a36b589db182ea984ae"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="aff824dd42ae84e47808704409603b477"><a name="aff824dd42ae84e47808704409603b477"></a><a name="aff824dd42ae84e47808704409603b477"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="a9b2fd1537d594c90b374b1bd1ea7a418"><a name="a9b2fd1537d594c90b374b1bd1ea7a418"></a><a name="a9b2fd1537d594c90b374b1bd1ea7a418"></a>The requested page was not found.</p>
    </td>
    </tr>
    <tr id="rcbd52c0054bf403e8dde1048b80a384d"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="a7227ffed0a1943f2b8e7a1d2a9727716"><a name="a7227ffed0a1943f2b8e7a1d2a9727716"></a><a name="a7227ffed0a1943f2b8e7a1d2a9727716"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="a3d578ec02d29435ba6b7c4ba24158cc3"><a name="a3d578ec02d29435ba6b7c4ba24158cc3"></a><a name="a3d578ec02d29435ba6b7c4ba24158cc3"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="r56237b74a916408ca08c817f83fba1b8"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="adc58e633872c40bcb52badb5a2375a34"><a name="adc58e633872c40bcb52badb5a2375a34"></a><a name="adc58e633872c40bcb52badb5a2375a34"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="a6fa1d3a05a974384bd0e33d2daccc6f5"><a name="a6fa1d3a05a974384bd0e33d2daccc6f5"></a><a name="a6fa1d3a05a974384bd0e33d2daccc6f5"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="r11951d13b9c44ff1bdeb70cd964a01c5"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="aef1597c21c8445fa9b2bda805a0a9416"><a name="aef1597c21c8445fa9b2bda805a0a9416"></a><a name="aef1597c21c8445fa9b2bda805a0a9416"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="afb43881a086a41b3b393c0415fc704e4"><a name="afb43881a086a41b3b393c0415fc704e4"></a><a name="afb43881a086a41b3b393c0415fc704e4"></a>You must use the proxy server for authentication. Then the request can be processed.</p>
    </td>
    </tr>
    <tr id="r5b7cd21b85fc41c98d9e5aae6951462f"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="a38c61b6bf49c41479c8b36db69401729"><a name="a38c61b6bf49c41479c8b36db69401729"></a><a name="a38c61b6bf49c41479c8b36db69401729"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="a717cddfa84374c4db0941e9b19e90f02"><a name="a717cddfa84374c4db0941e9b19e90f02"></a><a name="a717cddfa84374c4db0941e9b19e90f02"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="r0bb503bad28f4388a32d2c1a0890708e"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="a06405cdc3091435ba6f174d081325fd4"><a name="a06405cdc3091435ba6f174d081325fd4"></a><a name="a06405cdc3091435ba6f174d081325fd4"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="a41e7a6977184470aa76345fba1c1b020"><a name="a41e7a6977184470aa76345fba1c1b020"></a><a name="a41e7a6977184470aa76345fba1c1b020"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="r1b35e848f6d84fcea2aee7f278809c25"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="a78194ca36e6a4d3f9304ee7f893f3aa3"><a name="a78194ca36e6a4d3f9304ee7f893f3aa3"></a><a name="a78194ca36e6a4d3f9304ee7f893f3aa3"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="a58b5d62a0ad14b14a06f1d8f0ffec681"><a name="a58b5d62a0ad14b14a06f1d8f0ffec681"></a><a name="a58b5d62a0ad14b14a06f1d8f0ffec681"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="r9ec15dd64c364a7fb6a4b94330b75302"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="abf5a904cb0324141940020cd26895489"><a name="abf5a904cb0324141940020cd26895489"></a><a name="abf5a904cb0324141940020cd26895489"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="af76bba7454e445aca816e2b878d94153"><a name="af76bba7454e445aca816e2b878d94153"></a><a name="af76bba7454e445aca816e2b878d94153"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="rab376948bbad4bee941098ff4fb6d3f8"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="a412d522e7dde4b4e82df31bfa6b0e38f"><a name="a412d522e7dde4b4e82df31bfa6b0e38f"></a><a name="a412d522e7dde4b4e82df31bfa6b0e38f"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="a3640db6a500d4904b5b053cc220ad7c7"><a name="a3640db6a500d4904b5b053cc220ad7c7"></a><a name="a3640db6a500d4904b5b053cc220ad7c7"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="r4c6f4e7ce63740299814a5d893cf8451"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="a052d2ef826bd410fb1926c5a7c57df0d"><a name="a052d2ef826bd410fb1926c5a7c57df0d"></a><a name="a052d2ef826bd410fb1926c5a7c57df0d"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="a82aaa5ccd8c24e958791f059180e2ac8"><a name="a82aaa5ccd8c24e958791f059180e2ac8"></a><a name="a82aaa5ccd8c24e958791f059180e2ac8"></a>Failed to complete the request because the service is unavailable.</p>
    </td>
    </tr>
    <tr id="r60718a2e05064b0eb57841b9b1df91a8"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="ab6e292c2030b47f6b97633cd9c5d45aa"><a name="ab6e292c2030b47f6b97633cd9c5d45aa"></a><a name="ab6e292c2030b47f6b97633cd9c5d45aa"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="acfdef610ecf34be685c4579ec892f86e"><a name="acfdef610ecf34be685c4579ec892f86e"></a><a name="acfdef610ecf34be685c4579ec892f86e"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


