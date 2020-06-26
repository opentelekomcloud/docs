# Querying Endpoint Details<a name="en-us_topic_0067148046"></a>

## Function Description<a name="s81394c6441e2433aa089b83d9ae901bb"></a>

This interface is used to query endpoint details.

## URI<a name="s7f773a8bf34349f5bf81d0c7af9a440d"></a>

-   URI format

    GET /v3/endpoints/\{endpoint\_id\}


-   URI parameter description

    <a name="t3b91158605e2483f8ec0f7e76612766e"></a>
    <table><thead align="left"><tr id="r7c9a4d7646cc40838d1c27ac6a0771ed"><th class="cellrowborder" valign="top" width="20.747925207479252%" id="mcps1.1.5.1.1"><p id="a870dd0e09c234313a6279943760cd249"><a name="a870dd0e09c234313a6279943760cd249"></a><a name="a870dd0e09c234313a6279943760cd249"></a><strong id="a173ae121cc9e48328ca613e72f2a1504"><a name="a173ae121cc9e48328ca613e72f2a1504"></a><a name="a173ae121cc9e48328ca613e72f2a1504"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.428057194280573%" id="mcps1.1.5.1.2"><p id="a3fa42d29543146eda8cc5294eee7152c"><a name="a3fa42d29543146eda8cc5294eee7152c"></a><a name="a3fa42d29543146eda8cc5294eee7152c"></a><strong id="ac429376f11ae472b87ff4be326afb9d8"><a name="ac429376f11ae472b87ff4be326afb9d8"></a><a name="ac429376f11ae472b87ff4be326afb9d8"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.41785821417858%" id="mcps1.1.5.1.3"><p id="a8747c43669bb409782410e7aafd0e8d9"><a name="a8747c43669bb409782410e7aafd0e8d9"></a><a name="a8747c43669bb409782410e7aafd0e8d9"></a><strong id="b842352706143526_1"><a name="b842352706143526_1"></a><a name="b842352706143526_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="38.406159384061596%" id="mcps1.1.5.1.4"><p id="a7f591587c22c4b1ebc7dedb7d0d2a0d6"><a name="a7f591587c22c4b1ebc7dedb7d0d2a0d6"></a><a name="a7f591587c22c4b1ebc7dedb7d0d2a0d6"></a><strong id="b20601766145329"><a name="b20601766145329"></a><a name="b20601766145329"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r9f23e5d0e8de4d70bb3200d16e4f2789"><td class="cellrowborder" valign="top" width="20.747925207479252%" headers="mcps1.1.5.1.1 "><p id="a8b74590de667463195f36260f5b8baf9"><a name="a8b74590de667463195f36260f5b8baf9"></a><a name="a8b74590de667463195f36260f5b8baf9"></a>endpoint_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.428057194280573%" headers="mcps1.1.5.1.2 "><p id="a2e615c570a484ad3bd1572d579904e5e"><a name="a2e615c570a484ad3bd1572d579904e5e"></a><a name="a2e615c570a484ad3bd1572d579904e5e"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.41785821417858%" headers="mcps1.1.5.1.3 "><p id="a2b5c563d5b934e40979aac7a0904045c"><a name="a2b5c563d5b934e40979aac7a0904045c"></a><a name="a2b5c563d5b934e40979aac7a0904045c"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.406159384061596%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0031136110_p529112711147"><a name="en-us_topic_0031136110_p529112711147"></a><a name="en-us_topic_0031136110_p529112711147"></a>Endpoint ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## **Request**<a name="sf86f3f4f84a8493e84f564c16c53eaf3"></a>

-   Request header parameter description

    <a name="tab13448d4b644cd482b72e023e311a4c"></a>
    <table><thead align="left"><tr id="r9cc8c45e565f499a85068ccf812c4906"><th class="cellrowborder" valign="top" width="20.49%" id="mcps1.1.5.1.1"><p id="en-us_topic_0031136110_p289771511147"><a name="en-us_topic_0031136110_p289771511147"></a><a name="en-us_topic_0031136110_p289771511147"></a><strong id="b37426530113629"><a name="b37426530113629"></a><a name="b37426530113629"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.689999999999998%" id="mcps1.1.5.1.2"><p id="aa8a52be628254fb799e7d667253339cf"><a name="aa8a52be628254fb799e7d667253339cf"></a><a name="aa8a52be628254fb799e7d667253339cf"></a><strong id="b749622252"><a name="b749622252"></a><a name="b749622252"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.279999999999998%" id="mcps1.1.5.1.3"><p id="a8de3dfc3143a4304a1273fade5a53dae"><a name="a8de3dfc3143a4304a1273fade5a53dae"></a><a name="a8de3dfc3143a4304a1273fade5a53dae"></a><strong id="b842352706143526_3"><a name="b842352706143526_3"></a><a name="b842352706143526_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="38.54%" id="mcps1.1.5.1.4"><p id="a51fedaacfb0744a39c0e39893bf93f94"><a name="a51fedaacfb0744a39c0e39893bf93f94"></a><a name="a51fedaacfb0744a39c0e39893bf93f94"></a><strong id="b14438018113629"><a name="b14438018113629"></a><a name="b14438018113629"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r439e4c7cd1bc47f5a75d1632d4b0d739"><td class="cellrowborder" valign="top" width="20.49%" headers="mcps1.1.5.1.1 "><p id="a0131df71ca694a6ca73f9ad3a3a794a9"><a name="a0131df71ca694a6ca73f9ad3a3a794a9"></a><a name="a0131df71ca694a6ca73f9ad3a3a794a9"></a>Content-Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.689999999999998%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0031136110_p746938611147"><a name="en-us_topic_0031136110_p746938611147"></a><a name="en-us_topic_0031136110_p746938611147"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.279999999999998%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0031136110_p104050011147"><a name="en-us_topic_0031136110_p104050011147"></a><a name="en-us_topic_0031136110_p104050011147"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.54%" headers="mcps1.1.5.1.4 "><p id="a15c772f0a23d4d52b8f64d1377e3410a"><a name="a15c772f0a23d4d52b8f64d1377e3410a"></a><a name="a15c772f0a23d4d52b8f64d1377e3410a"></a>Fill <strong id="b842352706161331"><a name="b842352706161331"></a><a name="b842352706161331"></a>application/json;charset=utf8</strong> in this field.</p>
    </td>
    </tr>
    <tr id="r80e6b051a95142239d52ef85b3b9e59c"><td class="cellrowborder" valign="top" width="20.49%" headers="mcps1.1.5.1.1 "><p id="a88f9db0a7b6c4b4690378ccf5a787f60"><a name="a88f9db0a7b6c4b4690378ccf5a787f60"></a><a name="a88f9db0a7b6c4b4690378ccf5a787f60"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.689999999999998%" headers="mcps1.1.5.1.2 "><p id="ad6cfd0f57eb643a0afb40a639b4a8515"><a name="ad6cfd0f57eb643a0afb40a639b4a8515"></a><a name="ad6cfd0f57eb643a0afb40a639b4a8515"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.279999999999998%" headers="mcps1.1.5.1.3 "><p id="ac4cc17eda4bf4dd4aa34a5449be8f04e"><a name="ac4cc17eda4bf4dd4aa34a5449be8f04e"></a><a name="ac4cc17eda4bf4dd4aa34a5449be8f04e"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.54%" headers="mcps1.1.5.1.4 "><p id="a259cd575002145db850a7dcaf1cbe007"><a name="a259cd575002145db850a7dcaf1cbe007"></a><a name="a259cd575002145db850a7dcaf1cbe007"></a>Authenticated token.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Sample request

    ```
    curl -i -k -H 'Accept:application/json' -H 'Content-Type:application/json;charset=utf8' -H "X-Auth-Token:$token" -X GET https://172.30.48.86:31943/v3/endpoints/62ea3602f8ee42b1825956473f5295a8
    ```


## **Response**<a name="s6e8a35fa777c4de29b376bef459aba1d"></a>

Sample response \(successful request\)

```
{
    "endpoint": {
        "region_id": "region_id",
        "links": {
            "self": "10.10.10.10/v3/endpoints/62ea3602f8ee42b1825956473f5295a8"
        },
        "url": "https://172.30.49.68:7443/v2/",
        "region": "region_name",
        "enabled": true,
        "interface": "public",
        "service_id": "5a4ed456d228428c800ed2b67b4363a7",
        "id": "62ea3602f8ee42b1825956473f5295a8"
    }
}
```

## **Status Codes**<a name="s161ee4f22c7a4e5f928bf049a4425742"></a>

<a name="en-us_topic_0031136110_table25927028"></a>
<table><thead align="left"><tr id="en-us_topic_0031136110_row10578662"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0031136110_p51565323"><a name="en-us_topic_0031136110_p51565323"></a><a name="en-us_topic_0031136110_p51565323"></a><strong id="b37151362163018"><a name="b37151362163018"></a><a name="b37151362163018"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0031136110_p16041657"><a name="en-us_topic_0031136110_p16041657"></a><a name="en-us_topic_0031136110_p16041657"></a><strong id="b38470707163018"><a name="b38470707163018"></a><a name="b38470707163018"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0031136110_row24305815"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0031136110_p22613965"><a name="en-us_topic_0031136110_p22613965"></a><a name="en-us_topic_0031136110_p22613965"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0031136110_p19791876"><a name="en-us_topic_0031136110_p19791876"></a><a name="en-us_topic_0031136110_p19791876"></a>The request is successful.</p>
</td>
</tr>
<tr id="en-us_topic_0031136110_row43909159"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0031136110_p66980994"><a name="en-us_topic_0031136110_p66980994"></a><a name="en-us_topic_0031136110_p66980994"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0031136110_p56751409"><a name="en-us_topic_0031136110_p56751409"></a><a name="en-us_topic_0031136110_p56751409"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="re5868592b58a49148d1e374ab0ee4186"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a67da088f332e48ca9c70f3ba30897dde"><a name="a67da088f332e48ca9c70f3ba30897dde"></a><a name="a67da088f332e48ca9c70f3ba30897dde"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a0525ff08629b4648808d6e876aaf9c5f"><a name="a0525ff08629b4648808d6e876aaf9c5f"></a><a name="a0525ff08629b4648808d6e876aaf9c5f"></a>You must enter a username and password to access the requested page.</p>
</td>
</tr>
<tr id="en-us_topic_0031136110_row41000636"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0031136110_p32717189"><a name="en-us_topic_0031136110_p32717189"></a><a name="en-us_topic_0031136110_p32717189"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a98f74bf5eda646c6a5973dfa742126c4"><a name="a98f74bf5eda646c6a5973dfa742126c4"></a><a name="a98f74bf5eda646c6a5973dfa742126c4"></a>You are forbidden to access the requested page.</p>
</td>
</tr>
<tr id="r40e82c2469d34bf089fe9bfb0fa81526"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a8be4e075b25144a38cbe0ff05c2b2f15"><a name="a8be4e075b25144a38cbe0ff05c2b2f15"></a><a name="a8be4e075b25144a38cbe0ff05c2b2f15"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a5147e7c96ca94cb882828f2c4a33c1dc"><a name="a5147e7c96ca94cb882828f2c4a33c1dc"></a><a name="a5147e7c96ca94cb882828f2c4a33c1dc"></a>The server could not find the requested page.</p>
</td>
</tr>
<tr id="r6ae77ec5e12645e0a53aa0f3be73d1a9"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a61cb90ae8ac1482f83a82028556bbee5"><a name="a61cb90ae8ac1482f83a82028556bbee5"></a><a name="a61cb90ae8ac1482f83a82028556bbee5"></a>405</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a41bd1c94c1ba4153b7346917bc58b6b3"><a name="a41bd1c94c1ba4153b7346917bc58b6b3"></a><a name="a41bd1c94c1ba4153b7346917bc58b6b3"></a>You are not allowed to use the method specified in the request.</p>
</td>
</tr>
<tr id="rbea4e490c384410e8d1210ca41179e16"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a9eaf1c04680e4901822818bfe53ee0fc"><a name="a9eaf1c04680e4901822818bfe53ee0fc"></a><a name="a9eaf1c04680e4901822818bfe53ee0fc"></a>413</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a5e2acac6d93f406caa8cb7f89f4b0e4d"><a name="a5e2acac6d93f406caa8cb7f89f4b0e4d"></a><a name="a5e2acac6d93f406caa8cb7f89f4b0e4d"></a>The request entity is too large.</p>
</td>
</tr>
<tr id="r3b34616283144b19899b01b4552b799c"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a898bb41bdd874b25b452c9fd609e5bc0"><a name="a898bb41bdd874b25b452c9fd609e5bc0"></a><a name="a898bb41bdd874b25b452c9fd609e5bc0"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="ad43eae2906e84b6fb48fb6c11746dfab"><a name="ad43eae2906e84b6fb48fb6c11746dfab"></a><a name="ad43eae2906e84b6fb48fb6c11746dfab"></a>Failed to complete the request because of an internal service error.</p>
</td>
</tr>
<tr id="r73ae10963ce24ea09cafcfec5f21c2ab"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a3f2f513363a24dcb87462518dff622e7"><a name="a3f2f513363a24dcb87462518dff622e7"></a><a name="a3f2f513363a24dcb87462518dff622e7"></a>503</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a642a35bd05f24df68588a7f13c7cb3b7"><a name="a642a35bd05f24df68588a7f13c7cb3b7"></a><a name="a642a35bd05f24df68588a7f13c7cb3b7"></a>Failed to complete the request because the service is unavailable.</p>
</td>
</tr>
</tbody>
</table>

