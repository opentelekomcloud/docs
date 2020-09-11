# Querying All API Versions<a name="en-us_topic_0168602247"></a>

## Function<a name="s0466135c97cb4142aa7983923c915d8c"></a>

This API is used to query all API versions supported by CTS.

## URI<a name="s04b7f4492f314198a774428f35becda2"></a>

GET /

## Request<a name="s84cceca358f247f69eb175807e7c2b50"></a>

None

## Response<a name="s4d7d5e00cc9b4d6f976ccc3966242889"></a>

-   Parameter description

    **Table  1**  Parameters in the response

    <a name="tdf4d7268413c469c8221c4c5926fe87b"></a>
    <table><thead align="left"><tr id="rb45363afc3d24211ae09d1b4af288a9e"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.1"><p id="af9d1be9b0c1645e283baee0922d5fbbb"><a name="af9d1be9b0c1645e283baee0922d5fbbb"></a><a name="af9d1be9b0c1645e283baee0922d5fbbb"></a><strong id="b842352706115119"><a name="b842352706115119"></a><a name="b842352706115119"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18%" id="mcps1.2.5.1.2"><p id="en-us_topic_0133095426_p543845610355"><a name="en-us_topic_0133095426_p543845610355"></a><a name="en-us_topic_0133095426_p543845610355"></a><strong id="b842352706115121"><a name="b842352706115121"></a><a name="b842352706115121"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.3"><p id="a7823bd85d602486b879247d4b661d7f4"><a name="a7823bd85d602486b879247d4b661d7f4"></a><a name="a7823bd85d602486b879247d4b661d7f4"></a><strong id="b842352706115123"><a name="b842352706115123"></a><a name="b842352706115123"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.2.5.1.4"><p id="en-us_topic_0133095426_p244212561357"><a name="en-us_topic_0133095426_p244212561357"></a><a name="en-us_topic_0133095426_p244212561357"></a><strong id="b842352706115259"><a name="b842352706115259"></a><a name="b842352706115259"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r0ee0073f6e834f00bc77358f6f8635f5"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="a017cdab0a98d4851a49f5135cbad69d4"><a name="a017cdab0a98d4851a49f5135cbad69d4"></a><a name="a017cdab0a98d4851a49f5135cbad69d4"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.2 "><p id="acf0769f0413e439a8a183199f0d16ee2"><a name="acf0769f0413e439a8a183199f0d16ee2"></a><a name="acf0769f0413e439a8a183199f0d16ee2"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0133095426_p444855610353"><a name="en-us_topic_0133095426_p444855610353"></a><a name="en-us_topic_0133095426_p444855610353"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0133095426_p344911569354"><a name="en-us_topic_0133095426_p344911569354"></a><a name="en-us_topic_0133095426_p344911569354"></a>Specifies the list of all API versions.</p>
    </td>
    </tr>
    <tr id="rd47d209edd3149f699432eab07df3f16"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="ac4b145b2e58942c68d8499e88414cd81"><a name="ac4b145b2e58942c68d8499e88414cd81"></a><a name="ac4b145b2e58942c68d8499e88414cd81"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.2 "><p id="aaa9adc4b7c9145baabc697348da646ad"><a name="aaa9adc4b7c9145baabc697348da646ad"></a><a name="aaa9adc4b7c9145baabc697348da646ad"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="afae482155c0f41eab8beac94febc051f"><a name="afae482155c0f41eab8beac94febc051f"></a><a name="afae482155c0f41eab8beac94febc051f"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0133095426_p045585620357"><a name="en-us_topic_0133095426_p045585620357"></a><a name="en-us_topic_0133095426_p045585620357"></a>Specifies the version ID (version number), for example, v1.</p>
    </td>
    </tr>
    <tr id="r3bc50bee8f97476eb366ad2cda969e5b"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="a16441b8ffb7f4804b29d4766778d611f"><a name="a16441b8ffb7f4804b29d4766778d611f"></a><a name="a16441b8ffb7f4804b29d4766778d611f"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.2 "><p id="aa042642075e24ae2948962aa8b28bd44"><a name="aa042642075e24ae2948962aa8b28bd44"></a><a name="aa042642075e24ae2948962aa8b28bd44"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0133095426_p346325618353"><a name="en-us_topic_0133095426_p346325618353"></a><a name="en-us_topic_0133095426_p346325618353"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0133095426_p746525619351"><a name="en-us_topic_0133095426_p746525619351"></a><a name="en-us_topic_0133095426_p746525619351"></a>Specifies the API URL.</p>
    </td>
    </tr>
    <tr id="row7534410111710"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p16283354130"><a name="p16283354130"></a><a name="p16283354130"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.2 "><p id="p139117297139"><a name="p139117297139"></a><a name="p139117297139"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p13242332181317"><a name="p13242332181317"></a><a name="p13242332181317"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p2269104581219"><a name="p2269104581219"></a><a name="p2269104581219"></a>Specifies the reference address of the current API version.</p>
    </td>
    </tr>
    <tr id="row1811287181710"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p2139956101218"><a name="p2139956101218"></a><a name="p2139956101218"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.2 "><p id="p1994102917139"><a name="p1994102917139"></a><a name="p1994102917139"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p824653211138"><a name="p824653211138"></a><a name="p824653211138"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p513917563125"><a name="p513917563125"></a><a name="p513917563125"></a>Specifies the relationship between the current API version and the referenced address.</p>
    </td>
    </tr>
    <tr id="rbefb89827eb64c9fb76fa47e3518c25b"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="a197887174b37427aad0aa150e112bb4b"><a name="a197887174b37427aad0aa150e112bb4b"></a><a name="a197887174b37427aad0aa150e112bb4b"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0133095426_p164706561359"><a name="en-us_topic_0133095426_p164706561359"></a><a name="en-us_topic_0133095426_p164706561359"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="a49d2c8dda562477299d3a087fabf6226"><a name="a49d2c8dda562477299d3a087fabf6226"></a><a name="a49d2c8dda562477299d3a087fabf6226"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="afddf4ef447a0492e81251f2729d202ba"><a name="afddf4ef447a0492e81251f2729d202ba"></a><a name="afddf4ef447a0492e81251f2729d202ba"></a>If the APIs of this version support microversions, set this parameter to the supported maximum microversion. If the microversion is not supported, leave this parameter empty.</p>
    </td>
    </tr>
    <tr id="rd0382ea7e2f34bbba313199943f81b84"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0133095426_p647516561358"><a name="en-us_topic_0133095426_p647516561358"></a><a name="en-us_topic_0133095426_p647516561358"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0133095426_p447812565352"><a name="en-us_topic_0133095426_p447812565352"></a><a name="en-us_topic_0133095426_p447812565352"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="ac470d0351b0f417cb9cffaf0e28cd2d8"><a name="ac470d0351b0f417cb9cffaf0e28cd2d8"></a><a name="ac470d0351b0f417cb9cffaf0e28cd2d8"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="a3a9174449f8a4c4dabee175ef0b37b72"><a name="a3a9174449f8a4c4dabee175ef0b37b72"></a><a name="a3a9174449f8a4c4dabee175ef0b37b72"></a>Specifies the version status. The options are as follows:</p>
    <p id="a148dcf9e966342c6a2c2d53bbac49302"><a name="a148dcf9e966342c6a2c2d53bbac49302"></a><a name="a148dcf9e966342c6a2c2d53bbac49302"></a><strong id="b842352706192132"><a name="b842352706192132"></a><a name="b842352706192132"></a>CURRENT</strong>: indicates that the version is the primary version.</p>
    <p id="a5aac1a3bc7ed443ba67d3e5f4ef29988"><a name="a5aac1a3bc7ed443ba67d3e5f4ef29988"></a><a name="a5aac1a3bc7ed443ba67d3e5f4ef29988"></a><strong id="b842352706192150"><a name="b842352706192150"></a><a name="b842352706192150"></a>SUPPORTED</strong>: indicates that the version is an old version, but it is still supported.</p>
    <p id="a991e9ae8d16945a3adc86afb88dc1506"><a name="a991e9ae8d16945a3adc86afb88dc1506"></a><a name="a991e9ae8d16945a3adc86afb88dc1506"></a><strong id="b84235270619220"><a name="b84235270619220"></a><a name="b84235270619220"></a>DEPRECATED</strong>: indicates that the version is a deprecated version, which may be deleted later.</p>
    </td>
    </tr>
    <tr id="r3c318a216dc0482fa1dcac024fbc8bad"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="ab707aa5fa1ef4643b3075fa7353ead56"><a name="ab707aa5fa1ef4643b3075fa7353ead56"></a><a name="ab707aa5fa1ef4643b3075fa7353ead56"></a>updated</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.2 "><p id="a12638c03d03b43048ab2cb123ec124fe"><a name="a12638c03d03b43048ab2cb123ec124fe"></a><a name="a12638c03d03b43048ab2cb123ec124fe"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="a79d47501d5a944f48081dcd67c7cb965"><a name="a79d47501d5a944f48081dcd67c7cb965"></a><a name="a79d47501d5a944f48081dcd67c7cb965"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="a36c320ed10984a5ebbcd1d90837c783a"><a name="a36c320ed10984a5ebbcd1d90837c783a"></a><a name="a36c320ed10984a5ebbcd1d90837c783a"></a>Specifies the version release time, which must be the UTC time. For example, the release time of v1 is 2014-06-28T12:20:21Z.</p>
    </td>
    </tr>
    <tr id="r21e88a93e3be48adb4a7c5ca9946016e"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="abc5e00a197f74a12acb4c32212df9941"><a name="abc5e00a197f74a12acb4c32212df9941"></a><a name="abc5e00a197f74a12acb4c32212df9941"></a>min_version</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0133095426_p14966566355"><a name="en-us_topic_0133095426_p14966566355"></a><a name="en-us_topic_0133095426_p14966566355"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="aa592cf71536548969efa4aaf4bf26d89"><a name="aa592cf71536548969efa4aaf4bf26d89"></a><a name="aa592cf71536548969efa4aaf4bf26d89"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0133095426_p205014565351"><a name="en-us_topic_0133095426_p205014565351"></a><a name="en-us_topic_0133095426_p205014565351"></a>If the APIs of this version support microversions, set this parameter to the supported minimum microversion. If the microversion is not supported, leave this field empty.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
      "version": [
        {
          "id": "v1.0",
          "links": [
            {
              "href": "https://x.x.x.x/v1.0/",
              "rel": "self"
            }
          ],
          "min_version": "",
          "status": "CURRENT",
          "updated": "2018-09-30T00:00:00Z",
          "version": ""
        }
       {
          "id": "v2.0",
          "links": [
            {
              "href": "https://x.x.x.x/v2.0/",
              "rel": "self"
            }
          ],
          "min_version": "",
          "status": "SUPPORTED",
          "updated": "2018-09-30T00:00:00Z",
          "version": ""
        }
      ]
    }
    ```


## Returned Value<a name="sa0e69c95829e4ac2954f1b2a8545ccf7"></a>

-   Normal

    200

-   Abnormal

    **Table  2**  Return code for failed requests

    <a name="en-us_topic_0133095426_table46793998"></a>
    <table><thead align="left"><tr id="en-us_topic_0133095426_row65573909"><th class="cellrowborder" valign="top" width="61.839999999999996%" id="mcps1.2.3.1.1"><p id="en-us_topic_0133095426_p9886408"><a name="en-us_topic_0133095426_p9886408"></a><a name="en-us_topic_0133095426_p9886408"></a><strong id="b842352706112815"><a name="b842352706112815"></a><a name="b842352706112815"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="38.16%" id="mcps1.2.3.1.2"><p id="en-us_topic_0133095426_p62601592"><a name="en-us_topic_0133095426_p62601592"></a><a name="en-us_topic_0133095426_p62601592"></a><strong id="b972162650"><a name="b972162650"></a><a name="b972162650"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0133095426_row37564172"><td class="cellrowborder" valign="top" width="61.839999999999996%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0133095426_p22799085"><a name="en-us_topic_0133095426_p22799085"></a><a name="en-us_topic_0133095426_p22799085"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.16%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0133095426_p44643603"><a name="en-us_topic_0133095426_p44643603"></a><a name="en-us_topic_0133095426_p44643603"></a>Request error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0133095426_row66248115"><td class="cellrowborder" valign="top" width="61.839999999999996%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0133095426_p64497130"><a name="en-us_topic_0133095426_p64497130"></a><a name="en-us_topic_0133095426_p64497130"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.16%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0133095426_p42202994"><a name="en-us_topic_0133095426_p42202994"></a><a name="en-us_topic_0133095426_p42202994"></a>The authentication information is not provided or is incorrect.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0133095426_row44282627"><td class="cellrowborder" valign="top" width="61.839999999999996%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0133095426_p30123063"><a name="en-us_topic_0133095426_p30123063"></a><a name="en-us_topic_0133095426_p30123063"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.16%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0133095426_p15114764"><a name="en-us_topic_0133095426_p15114764"></a><a name="en-us_topic_0133095426_p15114764"></a>The request was forbidden.</p>
    </td>
    </tr>
    <tr id="row097836141618"><td class="cellrowborder" valign="top" width="61.839999999999996%" headers="mcps1.2.3.1.1 "><p id="p6738773164846"><a name="p6738773164846"></a><a name="p6738773164846"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.16%" headers="mcps1.2.3.1.2 "><p id="p8969753164846"><a name="p8969753164846"></a><a name="p8969753164846"></a>The server failed to find the requested resource.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0133095426_row1815156"><td class="cellrowborder" valign="top" width="61.839999999999996%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0133095426_p12809933"><a name="en-us_topic_0133095426_p12809933"></a><a name="en-us_topic_0133095426_p12809933"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.16%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0133095426_p10309404"><a name="en-us_topic_0133095426_p10309404"></a><a name="en-us_topic_0133095426_p10309404"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0133095426_row25675773"><td class="cellrowborder" valign="top" width="61.839999999999996%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0133095426_p66471715"><a name="en-us_topic_0133095426_p66471715"></a><a name="en-us_topic_0133095426_p66471715"></a>429 Too Many Requests</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.16%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0133095426_p5281111"><a name="en-us_topic_0133095426_p5281111"></a><a name="en-us_topic_0133095426_p5281111"></a>The number requests exceeded the upper limit.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0133095426_row47530006"><td class="cellrowborder" valign="top" width="61.839999999999996%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0133095426_p24725298"><a name="en-us_topic_0133095426_p24725298"></a><a name="en-us_topic_0133095426_p24725298"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.16%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0133095426_p39567352"><a name="en-us_topic_0133095426_p39567352"></a><a name="en-us_topic_0133095426_p39567352"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0133095426_row20561848"><td class="cellrowborder" valign="top" width="61.839999999999996%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0133095426_p54897010"><a name="en-us_topic_0133095426_p54897010"></a><a name="en-us_topic_0133095426_p54897010"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.16%" headers="mcps1.2.3.1.2 "><p id="ae8051cac98af4c3a813d03ca7a40dc7c"><a name="ae8051cac98af4c3a813d03ca7a40dc7c"></a><a name="ae8051cac98af4c3a813d03ca7a40dc7c"></a>The service is currently unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


