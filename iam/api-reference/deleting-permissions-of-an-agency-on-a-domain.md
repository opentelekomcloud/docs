# Deleting Permissions of an Agency on a Domain<a name="en-us_topic_0079467622"></a>

## Function Description<a name="s6f06ea3136194d5980c38c9e94e76e43"></a>

This interface is used to delete permissions of an agency on a domain.

## URI<a name="sde73940d763d4ed4b4d1566baadf9d85"></a>

-   URI format

    DELETE /v3.0/OS-AGENCY/domains/\{domain\_id\}/agencies/\{agency\_id\}/roles/\{role\_id\}


-   URI parameter description

    <a name="t277db3937ec44018ae523cc5da8818d8"></a>
    <table><thead align="left"><tr id="rb4e7210075f145ac84669dc503689294"><th class="cellrowborder" valign="top" width="18.360000000000003%" id="mcps1.1.5.1.1"><p id="ad371ce458f1244ea8c7458487dc8af55"><a name="ad371ce458f1244ea8c7458487dc8af55"></a><a name="ad371ce458f1244ea8c7458487dc8af55"></a><strong id="a173ae121cc9e48328ca613e72f2a1504"><a name="a173ae121cc9e48328ca613e72f2a1504"></a><a name="a173ae121cc9e48328ca613e72f2a1504"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.48%" id="mcps1.1.5.1.2"><p id="aa463e4b491154da0b1dc5f62f8608ccf"><a name="aa463e4b491154da0b1dc5f62f8608ccf"></a><a name="aa463e4b491154da0b1dc5f62f8608ccf"></a><strong id="b842352706161940"><a name="b842352706161940"></a><a name="b842352706161940"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.86%" id="mcps1.1.5.1.3"><p id="a2ac8ad8d4ac94d91a5b44e16e110491e"><a name="a2ac8ad8d4ac94d91a5b44e16e110491e"></a><a name="a2ac8ad8d4ac94d91a5b44e16e110491e"></a><strong id="b842352706143526"><a name="b842352706143526"></a><a name="b842352706143526"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.3%" id="mcps1.1.5.1.4"><p id="a1c9e46cc774349958fb38337961ce374"><a name="a1c9e46cc774349958fb38337961ce374"></a><a name="a1c9e46cc774349958fb38337961ce374"></a><strong id="b20601766145329"><a name="b20601766145329"></a><a name="b20601766145329"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="rec49bc11993744319f9a4ad52b184cf5"><td class="cellrowborder" valign="top" width="18.360000000000003%" headers="mcps1.1.5.1.1 "><p id="aa05127e1e7bc44de8c35c1b0e0682bfe"><a name="aa05127e1e7bc44de8c35c1b0e0682bfe"></a><a name="aa05127e1e7bc44de8c35c1b0e0682bfe"></a>domain_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.5.1.2 "><p id="ad93d14c9f4024916b03099716217cf93"><a name="ad93d14c9f4024916b03099716217cf93"></a><a name="ad93d14c9f4024916b03099716217cf93"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.1.5.1.3 "><p id="a368b531a10f341fab3642f36a78e5d59"><a name="a368b531a10f341fab3642f36a78e5d59"></a><a name="a368b531a10f341fab3642f36a78e5d59"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.3%" headers="mcps1.1.5.1.4 "><p id="abf4c3ff71b7d4097a42ad181082acf68"><a name="abf4c3ff71b7d4097a42ad181082acf68"></a><a name="abf4c3ff71b7d4097a42ad181082acf68"></a>ID of the current domain.</p>
    </td>
    </tr>
    <tr id="rf8fbe4fd025142daadab1f5f2592fdbc"><td class="cellrowborder" valign="top" width="18.360000000000003%" headers="mcps1.1.5.1.1 "><p id="a3017b564242c447aa5a7f5f49aba1b8d"><a name="a3017b564242c447aa5a7f5f49aba1b8d"></a><a name="a3017b564242c447aa5a7f5f49aba1b8d"></a>agency_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.5.1.2 "><p id="aec63f5510722406480484e1015bfbe2e"><a name="aec63f5510722406480484e1015bfbe2e"></a><a name="aec63f5510722406480484e1015bfbe2e"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.1.5.1.3 "><p id="ac0e14d37c0cd470f8200076785f8d39e"><a name="ac0e14d37c0cd470f8200076785f8d39e"></a><a name="ac0e14d37c0cd470f8200076785f8d39e"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.3%" headers="mcps1.1.5.1.4 "><p id="a64096589e0dc4ca0b740ecf464431b6a"><a name="a64096589e0dc4ca0b740ecf464431b6a"></a><a name="a64096589e0dc4ca0b740ecf464431b6a"></a>ID of an agency.</p>
    </td>
    </tr>
    <tr id="r1bbd85e74bc24ef98727452e474dc208"><td class="cellrowborder" valign="top" width="18.360000000000003%" headers="mcps1.1.5.1.1 "><p id="af9bd81b465a54565b6ded7b7b84899e6"><a name="af9bd81b465a54565b6ded7b7b84899e6"></a><a name="af9bd81b465a54565b6ded7b7b84899e6"></a>role_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.5.1.2 "><p id="a8c27c166011e4696a65e46daaac74f58"><a name="a8c27c166011e4696a65e46daaac74f58"></a><a name="a8c27c166011e4696a65e46daaac74f58"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.1.5.1.3 "><p id="a56a5abedea034ac8b9ede5b938c784df"><a name="a56a5abedea034ac8b9ede5b938c784df"></a><a name="a56a5abedea034ac8b9ede5b938c784df"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.3%" headers="mcps1.1.5.1.4 "><p id="abf1501bee8d4416e8d987e5c121c434a"><a name="abf1501bee8d4416e8d987e5c121c434a"></a><a name="abf1501bee8d4416e8d987e5c121c434a"></a>ID of a role.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="s7c597b2b51204de7923233e29aeb797b"></a>

-   Request header parameter description

    <a name="tc0fa7c1a50904b1f89d17044cd5c7a69"></a>
    <table><thead align="left"><tr id="r5c7ba6eda36a4b26892f6d4780a4b508"><th class="cellrowborder" valign="top" width="19.36%" id="mcps1.1.5.1.1"><p id="ad460645e55244613b94da7e13ec04d03"><a name="ad460645e55244613b94da7e13ec04d03"></a><a name="ad460645e55244613b94da7e13ec04d03"></a><strong id="b60153559144451"><a name="b60153559144451"></a><a name="b60153559144451"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.26%" id="mcps1.1.5.1.2"><p id="a6e13910b05c24dd2bea36eff98ef7839"><a name="a6e13910b05c24dd2bea36eff98ef7839"></a><a name="a6e13910b05c24dd2bea36eff98ef7839"></a><strong id="b219683757"><a name="b219683757"></a><a name="b219683757"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.93%" id="mcps1.1.5.1.3"><p id="afa6d24c1310e471795557934ef86fe8e"><a name="afa6d24c1310e471795557934ef86fe8e"></a><a name="afa6d24c1310e471795557934ef86fe8e"></a><strong id="b2074908248"><a name="b2074908248"></a><a name="b2074908248"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.45%" id="mcps1.1.5.1.4"><p id="a41880dbeb61d48aa88c6e6908721f525"><a name="a41880dbeb61d48aa88c6e6908721f525"></a><a name="a41880dbeb61d48aa88c6e6908721f525"></a><strong id="b1864068881"><a name="b1864068881"></a><a name="b1864068881"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r9d91939c095344fe8e42ab6cfc3db6c1"><td class="cellrowborder" valign="top" width="19.36%" headers="mcps1.1.5.1.1 "><p id="a381351d3e33f4051b3f3cf5533cdcdbc"><a name="a381351d3e33f4051b3f3cf5533cdcdbc"></a><a name="a381351d3e33f4051b3f3cf5533cdcdbc"></a>Content-Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.26%" headers="mcps1.1.5.1.2 "><p id="a0be7cea5e82549eb8e7c0f934aa5e988"><a name="a0be7cea5e82549eb8e7c0f934aa5e988"></a><a name="a0be7cea5e82549eb8e7c0f934aa5e988"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.93%" headers="mcps1.1.5.1.3 "><p id="a4f0b0fa7ffb14c368580ad35ea5eb785"><a name="a4f0b0fa7ffb14c368580ad35ea5eb785"></a><a name="a4f0b0fa7ffb14c368580ad35ea5eb785"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.45%" headers="mcps1.1.5.1.4 "><p id="ad5ceecf431b34d40ba3dc9df81ec800c"><a name="ad5ceecf431b34d40ba3dc9df81ec800c"></a><a name="ad5ceecf431b34d40ba3dc9df81ec800c"></a>Fill <strong id="b842352706161331"><a name="b842352706161331"></a><a name="b842352706161331"></a>application/json;charset=utf8</strong> in this field.</p>
    </td>
    </tr>
    <tr id="ra0471ded40a146fd952f8037548cf080"><td class="cellrowborder" valign="top" width="19.36%" headers="mcps1.1.5.1.1 "><p id="a3295a62ea2304089b03307c76e466c6f"><a name="a3295a62ea2304089b03307c76e466c6f"></a><a name="a3295a62ea2304089b03307c76e466c6f"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.26%" headers="mcps1.1.5.1.2 "><p id="a3d71cbe3689240fba41d597cc7f85e6d"><a name="a3d71cbe3689240fba41d597cc7f85e6d"></a><a name="a3d71cbe3689240fba41d597cc7f85e6d"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.93%" headers="mcps1.1.5.1.3 "><p id="a9648d928937441a581b1923660597eb6"><a name="a9648d928937441a581b1923660597eb6"></a><a name="a9648d928937441a581b1923660597eb6"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.45%" headers="mcps1.1.5.1.4 "><p id="a1602030331024f6d9061c82cfaca200a"><a name="a1602030331024f6d9061c82cfaca200a"></a><a name="a1602030331024f6d9061c82cfaca200a"></a>Authenticated token with the <strong id="b750798910387"><a name="b750798910387"></a><a name="b750798910387"></a>Security Administrator</strong> permission.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Sample request

    ```
    curl -i -k -H "X-Auth-Token:$token" -H 'Content-Type:application/json;charset=utf8' -X DELETE https://sample.domain.com/v3.0/OS-AGENCY/domains/b32d99a7778d4fd9aa5bc616c3dc4e5f/agencies/37f90258b820472bbc8a0f4f0bfd720d/roles/0f3a2d418ed747fa8be46e92757be9ff
    ```


## Response<a name="s2efeb64f5f17479ea6c3fdef5593e8fb"></a>

-   Sample response \(request failed\)

    ```
    {
       "error" : {
           "message" : "Could not find role: 0f3a2d418ed747fa8be46e92757be9ddff",
           "code" : 404,
           "title" : "Not Found"
         }
    }
    ```


## **Status Codes**<a name="s52a4cdf70d764312a274df0668ad16ed"></a>

<a name="t753d29820c3540d1875d3053d76c7761"></a>
<table><thead align="left"><tr id="rb216d4f58d924585aafa54d9f3553979"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="ac6ea5ba6898e4abf82dba0bcaad485e1"><a name="ac6ea5ba6898e4abf82dba0bcaad485e1"></a><a name="ac6ea5ba6898e4abf82dba0bcaad485e1"></a><strong id="b43497138144451"><a name="b43497138144451"></a><a name="b43497138144451"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="a27c63c2f8ed44e078a958278afca10e9"><a name="a27c63c2f8ed44e078a958278afca10e9"></a><a name="a27c63c2f8ed44e078a958278afca10e9"></a><strong id="b394921908"><a name="b394921908"></a><a name="b394921908"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r3deb47eb460f4bc187d2d8dad503c9ee"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a88cdd4bd37104bea9011f934aa8198fe"><a name="a88cdd4bd37104bea9011f934aa8198fe"></a><a name="a88cdd4bd37104bea9011f934aa8198fe"></a>204</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a09e586f6495549379e030d8a67f1b10d"><a name="a09e586f6495549379e030d8a67f1b10d"></a><a name="a09e586f6495549379e030d8a67f1b10d"></a>The request is successful.</p>
</td>
</tr>
<tr id="rca43722291a5474f94edc848c4b5b82e"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="ac6d9bade3f2a4bb48da870d9b00c29be"><a name="ac6d9bade3f2a4bb48da870d9b00c29be"></a><a name="ac6d9bade3f2a4bb48da870d9b00c29be"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a9784d8d7b0c847f499be0cc720d8bd85"><a name="a9784d8d7b0c847f499be0cc720d8bd85"></a><a name="a9784d8d7b0c847f499be0cc720d8bd85"></a>You must enter a username and password to access the requested page.</p>
</td>
</tr>
<tr id="r0c7454cf24b948779d051733b586207c"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a7e5d8761d5424ba7baf7e5909e84a741"><a name="a7e5d8761d5424ba7baf7e5909e84a741"></a><a name="a7e5d8761d5424ba7baf7e5909e84a741"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a7a4e7387b62a4287af199c5982a96e75"><a name="a7a4e7387b62a4287af199c5982a96e75"></a><a name="a7a4e7387b62a4287af199c5982a96e75"></a>You are forbidden to access the requested page.</p>
</td>
</tr>
<tr id="r2ea8b8c32c53479f90c5b002ca7049cb"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="ae1a980fa5bb94fe5aca5c22890fc5402"><a name="ae1a980fa5bb94fe5aca5c22890fc5402"></a><a name="ae1a980fa5bb94fe5aca5c22890fc5402"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a12695efccfa848ed8418e32abd45bd1c"><a name="a12695efccfa848ed8418e32abd45bd1c"></a><a name="a12695efccfa848ed8418e32abd45bd1c"></a>The server could not find the requested page.</p>
</td>
</tr>
<tr id="r8734af361e7c4823be67924868676c22"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a7786f144832e457c9819e26de4a4c791"><a name="a7786f144832e457c9819e26de4a4c791"></a><a name="a7786f144832e457c9819e26de4a4c791"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="afdafb2c6d31b41d8a27d33b897e5569d"><a name="afdafb2c6d31b41d8a27d33b897e5569d"></a><a name="afdafb2c6d31b41d8a27d33b897e5569d"></a>Failed to complete the request because of an internal service error.</p>
</td>
</tr>
</tbody>
</table>

