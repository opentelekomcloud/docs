# Querying Service Details<a name="en-us_topic_0067148045"></a>

## Function Description<a name="s1fea94fc86654d20a4264b290de6701b"></a>

This interface is used to query service details.

## URI<a name="sd0c6621b74af445d8e95f2e8c5061c96"></a>

-   URI format

    GET /v3/services/\{service\_id\}


-   URI parameter description

    <a name="ta5ea92914f7e42ff96cb722ca62bbbc9"></a>
    <table><thead align="left"><tr id="r4b24ae277ca941128fbc303aeaf8326a"><th class="cellrowborder" valign="top" width="20.75%" id="mcps1.1.5.1.1"><p id="af8e60b99318f4a20b2d78b90100c964d"><a name="af8e60b99318f4a20b2d78b90100c964d"></a><a name="af8e60b99318f4a20b2d78b90100c964d"></a><strong id="a173ae121cc9e48328ca613e72f2a1504"><a name="a173ae121cc9e48328ca613e72f2a1504"></a><a name="a173ae121cc9e48328ca613e72f2a1504"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.099999999999998%" id="mcps1.1.5.1.2"><p id="a3e2b7330b740417881fc8195c5dc3d24"><a name="a3e2b7330b740417881fc8195c5dc3d24"></a><a name="a3e2b7330b740417881fc8195c5dc3d24"></a><strong id="ac429376f11ae472b87ff4be326afb9d8_1"><a name="ac429376f11ae472b87ff4be326afb9d8_1"></a><a name="ac429376f11ae472b87ff4be326afb9d8_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.63%" id="mcps1.1.5.1.3"><p id="a181496d4ddc847339375b4f23dfc9987"><a name="a181496d4ddc847339375b4f23dfc9987"></a><a name="a181496d4ddc847339375b4f23dfc9987"></a><strong id="b842352706143526_1"><a name="b842352706143526_1"></a><a name="b842352706143526_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="42.52%" id="mcps1.1.5.1.4"><p id="a5e29560192784650a29a305b9bad99e5"><a name="a5e29560192784650a29a305b9bad99e5"></a><a name="a5e29560192784650a29a305b9bad99e5"></a><strong id="b20601766145329"><a name="b20601766145329"></a><a name="b20601766145329"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r6af57967c5d04d67b0035d0ca833ad57"><td class="cellrowborder" valign="top" width="20.75%" headers="mcps1.1.5.1.1 "><p id="a50c523360f4d4908b875d10a28623c70"><a name="a50c523360f4d4908b875d10a28623c70"></a><a name="a50c523360f4d4908b875d10a28623c70"></a>service_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.099999999999998%" headers="mcps1.1.5.1.2 "><p id="ac24e8e998166421f94f7530c61d06715"><a name="ac24e8e998166421f94f7530c61d06715"></a><a name="ac24e8e998166421f94f7530c61d06715"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.63%" headers="mcps1.1.5.1.3 "><p id="a87c50dfba8bc4d549c30e53012306af5"><a name="a87c50dfba8bc4d549c30e53012306af5"></a><a name="a87c50dfba8bc4d549c30e53012306af5"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.52%" headers="mcps1.1.5.1.4 "><p id="a5e8ec1f1ea9349f8a0219d77303769ef"><a name="a5e8ec1f1ea9349f8a0219d77303769ef"></a><a name="a5e8ec1f1ea9349f8a0219d77303769ef"></a>Service ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## **Request**<a name="sc6a67a265e0c4e6c85c6dddbfffeec05"></a>

-   Request header parameter description

    <a name="t97020ff6a99b4d02897c62dc32176b10"></a>
    <table><thead align="left"><tr id="r33f9811ab31441bcbb68da4318582ff7"><th class="cellrowborder" valign="top" width="20.49%" id="mcps1.1.5.1.1"><p id="a15b20b8a2b1a4846942c4381d69d0f1f"><a name="a15b20b8a2b1a4846942c4381d69d0f1f"></a><a name="a15b20b8a2b1a4846942c4381d69d0f1f"></a><strong id="b21588442152010"><a name="b21588442152010"></a><a name="b21588442152010"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.23%" id="mcps1.1.5.1.2"><p id="a0c341246324648c2a331a2f3b29728ce"><a name="a0c341246324648c2a331a2f3b29728ce"></a><a name="a0c341246324648c2a331a2f3b29728ce"></a><strong id="ac429376f11ae472b87ff4be326afb9d8_3"><a name="ac429376f11ae472b87ff4be326afb9d8_3"></a><a name="ac429376f11ae472b87ff4be326afb9d8_3"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.63%" id="mcps1.1.5.1.3"><p id="ae3c49c667f304a8ea41ef4821a55dd34"><a name="ae3c49c667f304a8ea41ef4821a55dd34"></a><a name="ae3c49c667f304a8ea41ef4821a55dd34"></a><strong id="b842352706143526_3"><a name="b842352706143526_3"></a><a name="b842352706143526_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="42.65%" id="mcps1.1.5.1.4"><p id="ac65744bcbe944be4891ed74be82742a6"><a name="ac65744bcbe944be4891ed74be82742a6"></a><a name="ac65744bcbe944be4891ed74be82742a6"></a><strong id="b4059516152010"><a name="b4059516152010"></a><a name="b4059516152010"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="rd59aad8dd3584169840a2a50ca0bc035"><td class="cellrowborder" valign="top" width="20.49%" headers="mcps1.1.5.1.1 "><p id="a5f8f06a2f0f141d1b14d88d3cec03e26"><a name="a5f8f06a2f0f141d1b14d88d3cec03e26"></a><a name="a5f8f06a2f0f141d1b14d88d3cec03e26"></a>Content-Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.23%" headers="mcps1.1.5.1.2 "><p id="a0c8ab11defdf4c8f817b21b21680e919"><a name="a0c8ab11defdf4c8f817b21b21680e919"></a><a name="a0c8ab11defdf4c8f817b21b21680e919"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.63%" headers="mcps1.1.5.1.3 "><p id="a222d884836b34d4b96111de13ad02311"><a name="a222d884836b34d4b96111de13ad02311"></a><a name="a222d884836b34d4b96111de13ad02311"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.65%" headers="mcps1.1.5.1.4 "><p id="af58e489f66734ee8bfea4223431362ec"><a name="af58e489f66734ee8bfea4223431362ec"></a><a name="af58e489f66734ee8bfea4223431362ec"></a>Fill <strong id="b842352706161331"><a name="b842352706161331"></a><a name="b842352706161331"></a>application/json;charset=utf8</strong> in this field.</p>
    </td>
    </tr>
    <tr id="red29555edeb84300a63e22cdf504909a"><td class="cellrowborder" valign="top" width="20.49%" headers="mcps1.1.5.1.1 "><p id="a41b44a08aca64e4382a1901f5c4d384d"><a name="a41b44a08aca64e4382a1901f5c4d384d"></a><a name="a41b44a08aca64e4382a1901f5c4d384d"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.23%" headers="mcps1.1.5.1.2 "><p id="a554d5f30caf14006ba608ee5e933804c"><a name="a554d5f30caf14006ba608ee5e933804c"></a><a name="a554d5f30caf14006ba608ee5e933804c"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.63%" headers="mcps1.1.5.1.3 "><p id="aa734bd6d2ee44712b9b1fba893b1ea79"><a name="aa734bd6d2ee44712b9b1fba893b1ea79"></a><a name="aa734bd6d2ee44712b9b1fba893b1ea79"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.65%" headers="mcps1.1.5.1.4 "><p id="a3598b3c82d4745f18c1f204cf8097e6d"><a name="a3598b3c82d4745f18c1f204cf8097e6d"></a><a name="a3598b3c82d4745f18c1f204cf8097e6d"></a>Authenticated token.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Sample request

    ```
    curl -i -k -H 'Accept:application/json' -H 'Content-Type:application/json;charset=utf8' -H "X-Auth-Token:$token" -X GET https://172.30.48.86:31943/v3/services/5a4ed456d228428c800ed2b67b4363a7
    ```


## **Response**<a name="s6166214bb04d407290d8691550229884"></a>

Sample response \(successful response\)

```
{
    "service": {
        "enabled": true,
        "type": "compute",
        "name": "nova",
        "links": {
            "self": "10.10.10.10/v3/services/5a4ed456d228428c800ed2b67b4363a7"
        },
        "id": "5a4ed456d228428c800ed2b67b4363a7"
    }
}
```

## **Status Codes**<a name="se70eb4ec1a7c43ec9858561956f0a7ba"></a>

<a name="en-us_topic_0035544336_table25927028"></a>
<table><thead align="left"><tr id="en-us_topic_0035544336_row10578662"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0035544336_p51565323"><a name="en-us_topic_0035544336_p51565323"></a><a name="en-us_topic_0035544336_p51565323"></a><strong id="b37151362163018"><a name="b37151362163018"></a><a name="b37151362163018"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0035544336_p16041657"><a name="en-us_topic_0035544336_p16041657"></a><a name="en-us_topic_0035544336_p16041657"></a><strong id="b38470707163018"><a name="b38470707163018"></a><a name="b38470707163018"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035544336_row24305815"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035544336_p22613965"><a name="en-us_topic_0035544336_p22613965"></a><a name="en-us_topic_0035544336_p22613965"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035544336_p19791876"><a name="en-us_topic_0035544336_p19791876"></a><a name="en-us_topic_0035544336_p19791876"></a>The request is successful.</p>
</td>
</tr>
<tr id="en-us_topic_0035544336_row43909159"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035544336_p66980994"><a name="en-us_topic_0035544336_p66980994"></a><a name="en-us_topic_0035544336_p66980994"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035544336_p56751409"><a name="en-us_topic_0035544336_p56751409"></a><a name="en-us_topic_0035544336_p56751409"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="rb99fbab78bc54ae4953661763b573830"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="aef55745ff0834933af36d690e2e339b8"><a name="aef55745ff0834933af36d690e2e339b8"></a><a name="aef55745ff0834933af36d690e2e339b8"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a480215738ced4bf5a8feafa2681db93b"><a name="a480215738ced4bf5a8feafa2681db93b"></a><a name="a480215738ced4bf5a8feafa2681db93b"></a>You must enter a username and password to access the requested page.</p>
</td>
</tr>
<tr id="en-us_topic_0035544336_row41000636"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035544336_p32717189"><a name="en-us_topic_0035544336_p32717189"></a><a name="en-us_topic_0035544336_p32717189"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="ae678037f26d640f5a985c943e2ffb92e"><a name="ae678037f26d640f5a985c943e2ffb92e"></a><a name="ae678037f26d640f5a985c943e2ffb92e"></a>You are forbidden to access the requested page.</p>
</td>
</tr>
<tr id="r1fd5c05b7b6b4c048f3f7b9ddbc755b0"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a5d7e2305922e4f9098442a900792dae1"><a name="a5d7e2305922e4f9098442a900792dae1"></a><a name="a5d7e2305922e4f9098442a900792dae1"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a9edf299d0513460caaac8a2a19b76e9a"><a name="a9edf299d0513460caaac8a2a19b76e9a"></a><a name="a9edf299d0513460caaac8a2a19b76e9a"></a>The server could not find the requested page.</p>
</td>
</tr>
<tr id="rbb5133f150fd42eebde8dd6e390ecbd5"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="ad1a2754016e44193a97043265cd611cf"><a name="ad1a2754016e44193a97043265cd611cf"></a><a name="ad1a2754016e44193a97043265cd611cf"></a>405</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a81837d461ef445259c5a6e9e1ce0e32a"><a name="a81837d461ef445259c5a6e9e1ce0e32a"></a><a name="a81837d461ef445259c5a6e9e1ce0e32a"></a>You are not allowed to use the method specified in the request.</p>
</td>
</tr>
<tr id="r2cecff297b1a412f956a312d3cd7acc9"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a1f617621d1bc4a9facb1c84d1946002b"><a name="a1f617621d1bc4a9facb1c84d1946002b"></a><a name="a1f617621d1bc4a9facb1c84d1946002b"></a>413</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="ac31ead3ee2db40eea8ae45b2779a09e9"><a name="ac31ead3ee2db40eea8ae45b2779a09e9"></a><a name="ac31ead3ee2db40eea8ae45b2779a09e9"></a>The request entity is too large.</p>
</td>
</tr>
<tr id="rd71e0e00759f4179a2dccaf345ba9f2f"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a1657c5ca5ebd4a2cbacbdb35fc9b7601"><a name="a1657c5ca5ebd4a2cbacbdb35fc9b7601"></a><a name="a1657c5ca5ebd4a2cbacbdb35fc9b7601"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a88b4b14048564e12942b8151dc791b99"><a name="a88b4b14048564e12942b8151dc791b99"></a><a name="a88b4b14048564e12942b8151dc791b99"></a>Failed to complete the request because of an internal service error.</p>
</td>
</tr>
<tr id="r5647e5fd26974514ac66cc3925f30601"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a16dfaa16ceac4a33a468c0ae158292fb"><a name="a16dfaa16ceac4a33a468c0ae158292fb"></a><a name="a16dfaa16ceac4a33a468c0ae158292fb"></a>503</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a5635c1924d9648a8be89b1e5dcf0a87b"><a name="a5635c1924d9648a8be89b1e5dcf0a87b"></a><a name="a5635c1924d9648a8be89b1e5dcf0a87b"></a>Failed to complete the request because the service is unavailable.</p>
</td>
</tr>
</tbody>
</table>

