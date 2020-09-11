# Querying the Snapshot List<a name="dws_02_0024"></a>

## Function<a name="s3c15d46d4772415a849078534fba2ebe"></a>

This API is used to query the snapshot list.

## URI<a name="s7c03edfa8db3493eace6432e450328c6"></a>

-   URI format

    ```
    GET /v1.0/{project_id}/snapshots
    ```


-   Parameter description

    **Table  1**  URI parameter description

    <a name="t6ad12ac6cf434e8a8e85229b928d8ac0"></a>
    <table><thead align="left"><tr id="r00b86904f21a4f08b3a54beb036bd02b"><th class="cellrowborder" valign="top" width="22.45%" id="mcps1.2.5.1.1"><p id="a913c773bc62944e2917dfb70480f973d"><a name="a913c773bc62944e2917dfb70480f973d"></a><a name="a913c773bc62944e2917dfb70480f973d"></a><strong id="b84235270617228"><a name="b84235270617228"></a><a name="b84235270617228"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.55%" id="mcps1.2.5.1.2"><p id="ad7199863e6794e4f9604ba3f4eab5440"><a name="ad7199863e6794e4f9604ba3f4eab5440"></a><a name="ad7199863e6794e4f9604ba3f4eab5440"></a><strong id="b6167984116271"><a name="b6167984116271"></a><a name="b6167984116271"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.39%" id="mcps1.2.5.1.3"><p id="acd9bdd04bba04f599b7ade60e0c1173a"><a name="acd9bdd04bba04f599b7ade60e0c1173a"></a><a name="acd9bdd04bba04f599b7ade60e0c1173a"></a><strong id="b84235270617235"><a name="b84235270617235"></a><a name="b84235270617235"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="30.61%" id="mcps1.2.5.1.4"><p id="a663391723c604862bfc83d8eab00e99f"><a name="a663391723c604862bfc83d8eab00e99f"></a><a name="a663391723c604862bfc83d8eab00e99f"></a><strong id="b842352706172443"><a name="b842352706172443"></a><a name="b842352706172443"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r2d1b53aa3bbf44be85dfee3ef56a15a2"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.5.1.1 "><p id="a7e1a661d535e4d5a83a12c69a261e0af"><a name="a7e1a661d535e4d5a83a12c69a261e0af"></a><a name="a7e1a661d535e4d5a83a12c69a261e0af"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.55%" headers="mcps1.2.5.1.2 "><p id="aee547991fe474196b2b812de80eb5387"><a name="aee547991fe474196b2b812de80eb5387"></a><a name="aee547991fe474196b2b812de80eb5387"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.2.5.1.3 "><p id="a690e0609695c489198262b294054a104"><a name="a690e0609695c489198262b294054a104"></a><a name="a690e0609695c489198262b294054a104"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.61%" headers="mcps1.2.5.1.4 "><p id="p19606155735515"><a name="p19606155735515"></a><a name="p19606155735515"></a>Project ID. For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="s4fc5d63bd89e49e6816c196c6318c4da"></a>

Sample request

```
GET /v1.0/89cd04f168b84af6be287f71730fdb4b/snapshots
```

## Response<a name="sda34999659764d20a25a5713e3a41c25"></a>

-   Sample response

    ```
    STATUS CODE 200
    {
        "snapshots": [
            {
                "id": "2a4d0f86-67cd-408a-8b66-017454fb7793",
                "name": "snapshot-1",
                "description": "",
                "started": "2016-08-23T03:59:23Z",
                "finished": "2016-08-23T04:01:40Z", 
                "size": 500,
                "status": "AVAILABLE",
                "type": "MANUAL",
                "cluster_id": "4f87d3c4-9e33-482f-b962-e23b30d1a18c"
            },
            {
                "id": "4af11460-06ec-48a4-b3ad-0e3bbdcd8ab1",
                "name": "snapshot-2",
                "description": "",
                "started": "2016-08-23T18:20:00Z",
                "finished": "2016-08-23T18:22:12Z",
                "size": 500,
                "status": "AVAILABLE",
                "type": "MANUAL",
                "cluster_id": "4f87d3c4-9e33-482f-b962-e23b30d1a18c"
            }
        ]
    }
    ```

-   Parameter description

    **Table  2**  Response parameter description

    <a name="t4e4e5792bd6a4cdca26100da819b222d"></a>
    <table><thead align="left"><tr id="r48bdcd5b89f64e47a8c185b2ee934391"><th class="cellrowborder" valign="top" width="18.36816318368163%" id="mcps1.2.5.1.1"><p id="adb9c65faaff34c03802de977783b0159"><a name="adb9c65faaff34c03802de977783b0159"></a><a name="adb9c65faaff34c03802de977783b0159"></a><strong id="b1915479762"><a name="b1915479762"></a><a name="b1915479762"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.447755224477554%" id="mcps1.2.5.1.2"><p id="ad26fa0e87c73477a9341198a5137ca15"><a name="ad26fa0e87c73477a9341198a5137ca15"></a><a name="ad26fa0e87c73477a9341198a5137ca15"></a><strong id="b1155340281"><a name="b1155340281"></a><a name="b1155340281"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15.308469153084694%" id="mcps1.2.5.1.3"><p id="a92bf88d686ae4e339e8f11042154b7d5"><a name="a92bf88d686ae4e339e8f11042154b7d5"></a><a name="a92bf88d686ae4e339e8f11042154b7d5"></a><strong id="b638071014"><a name="b638071014"></a><a name="b638071014"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43.87561243875613%" id="mcps1.2.5.1.4"><p id="a8371dcb22555452ab82c3c4a0f833145"><a name="a8371dcb22555452ab82c3c4a0f833145"></a><a name="a8371dcb22555452ab82c3c4a0f833145"></a><strong id="b1605521174"><a name="b1605521174"></a><a name="b1605521174"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="ra7b7c5a56389499fbe4294793996a675"><td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.1 "><p id="aac890d13d3634134ae15be764fe74f85"><a name="aac890d13d3634134ae15be764fe74f85"></a><a name="aac890d13d3634134ae15be764fe74f85"></a>snapshots</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.447755224477554%" headers="mcps1.2.5.1.2 "><p id="a870f251e989c4028bb04ee03d02c18fc"><a name="a870f251e989c4028bb04ee03d02c18fc"></a><a name="a870f251e989c4028bb04ee03d02c18fc"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.3 "><p id="a9306e694532c4d0bae38509b6b77200e"><a name="a9306e694532c4d0bae38509b6b77200e"></a><a name="a9306e694532c4d0bae38509b6b77200e"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.87561243875613%" headers="mcps1.2.5.1.4 "><p id="aa53ac37474cb4a7cbef79d9d25dd1692"><a name="aa53ac37474cb4a7cbef79d9d25dd1692"></a><a name="aa53ac37474cb4a7cbef79d9d25dd1692"></a>List of snapshot objects</p>
    </td>
    </tr>
    <tr id="r90518fb4a58a4281b99918913e6cadd5"><td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.1 "><p id="a142a1af6b84545e29ef88ab0807c03ee"><a name="a142a1af6b84545e29ef88ab0807c03ee"></a><a name="a142a1af6b84545e29ef88ab0807c03ee"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.447755224477554%" headers="mcps1.2.5.1.2 "><p id="a65cbf3ee381349a380595edf34204d43"><a name="a65cbf3ee381349a380595edf34204d43"></a><a name="a65cbf3ee381349a380595edf34204d43"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.3 "><p id="a43b394ba54b54d99910ec79793fcb1a4"><a name="a43b394ba54b54d99910ec79793fcb1a4"></a><a name="a43b394ba54b54d99910ec79793fcb1a4"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.87561243875613%" headers="mcps1.2.5.1.4 "><p id="ad7b71b54fb934101a3b4bebcb88a968c"><a name="ad7b71b54fb934101a3b4bebcb88a968c"></a><a name="ad7b71b54fb934101a3b4bebcb88a968c"></a>Snapshot name</p>
    </td>
    </tr>
    <tr id="rb641ef1b2ab64b2e9abb16c9bbc08849"><td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.1 "><p id="a60c60c8dc2a54ac38de94ff12b7110b8"><a name="a60c60c8dc2a54ac38de94ff12b7110b8"></a><a name="a60c60c8dc2a54ac38de94ff12b7110b8"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.447755224477554%" headers="mcps1.2.5.1.2 "><p id="a51f1560043624e82b20d7a78746a269a"><a name="a51f1560043624e82b20d7a78746a269a"></a><a name="a51f1560043624e82b20d7a78746a269a"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.3 "><p id="a3d404a967e364021bfb217e339684691"><a name="a3d404a967e364021bfb217e339684691"></a><a name="a3d404a967e364021bfb217e339684691"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.87561243875613%" headers="mcps1.2.5.1.4 "><p id="a492703488865469db56110505fcf865e"><a name="a492703488865469db56110505fcf865e"></a><a name="a492703488865469db56110505fcf865e"></a>Snapshot ID</p>
    </td>
    </tr>
    <tr id="r819d5b462b374f7c9a9506ce37b5a7f6"><td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.1 "><p id="adf94410824874328aec0b53215b6848f"><a name="adf94410824874328aec0b53215b6848f"></a><a name="adf94410824874328aec0b53215b6848f"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.447755224477554%" headers="mcps1.2.5.1.2 "><p id="ac1ec37842f5c44c8867bfd30749f34c8"><a name="ac1ec37842f5c44c8867bfd30749f34c8"></a><a name="ac1ec37842f5c44c8867bfd30749f34c8"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.3 "><p id="aa10f59ab006c464f95d8175851c478a1"><a name="aa10f59ab006c464f95d8175851c478a1"></a><a name="aa10f59ab006c464f95d8175851c478a1"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.87561243875613%" headers="mcps1.2.5.1.4 "><p id="afb4967b27d834f85bc4bc3cdba82cb22"><a name="afb4967b27d834f85bc4bc3cdba82cb22"></a><a name="afb4967b27d834f85bc4bc3cdba82cb22"></a>Snapshot description</p>
    </td>
    </tr>
    <tr id="r04142f063491444190e45627108c69f1"><td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.1 "><p id="a951739ee0dcb4e2ba4c0d1c02a46f378"><a name="a951739ee0dcb4e2ba4c0d1c02a46f378"></a><a name="a951739ee0dcb4e2ba4c0d1c02a46f378"></a>started</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.447755224477554%" headers="mcps1.2.5.1.2 "><p id="ae04a380f25cb4b8e9f7386c60e635832"><a name="ae04a380f25cb4b8e9f7386c60e635832"></a><a name="ae04a380f25cb4b8e9f7386c60e635832"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.3 "><p id="a1433dd02bdfe4aaebb35bc49f34b3c05"><a name="a1433dd02bdfe4aaebb35bc49f34b3c05"></a><a name="a1433dd02bdfe4aaebb35bc49f34b3c05"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.87561243875613%" headers="mcps1.2.5.1.4 "><p id="ad7713940539840af873a13868a2f4378"><a name="ad7713940539840af873a13868a2f4378"></a><a name="ad7713940539840af873a13868a2f4378"></a>Time when a snapshot is being created. The format is <strong id="b842352706102625"><a name="b842352706102625"></a><a name="b842352706102625"></a>ISO8601: YYYY-MM-DDThh:mm:ssZ</strong>.</p>
    </td>
    </tr>
    <tr id="r0f7fea336b1346e0a26f2c024d21cc14"><td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.1 "><p id="abd43045543a8469db44d4965bd66bd2f"><a name="abd43045543a8469db44d4965bd66bd2f"></a><a name="abd43045543a8469db44d4965bd66bd2f"></a>finished</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.447755224477554%" headers="mcps1.2.5.1.2 "><p id="a4f76f51c34964a3680d2310d28a99b67"><a name="a4f76f51c34964a3680d2310d28a99b67"></a><a name="a4f76f51c34964a3680d2310d28a99b67"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.3 "><p id="a869110ec4f1b4f839a6bd4febc3a741f"><a name="a869110ec4f1b4f839a6bd4febc3a741f"></a><a name="a869110ec4f1b4f839a6bd4febc3a741f"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.87561243875613%" headers="mcps1.2.5.1.4 "><p id="a54ca38496db44682873d87a0f3118dbf"><a name="a54ca38496db44682873d87a0f3118dbf"></a><a name="a54ca38496db44682873d87a0f3118dbf"></a>Time when a snapshot has been created. The format is <strong id="b893555913"><a name="b893555913"></a><a name="b893555913"></a>ISO8601: YYYY-MM-DDThh:mm:ssZ</strong>.</p>
    </td>
    </tr>
    <tr id="r94be4f65f29047b0b85982dfe30554ba"><td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.1 "><p id="a1cad902e525f41538bca453c77ee56fd"><a name="a1cad902e525f41538bca453c77ee56fd"></a><a name="a1cad902e525f41538bca453c77ee56fd"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.447755224477554%" headers="mcps1.2.5.1.2 "><p id="a8a69f4abb0de49f78e9bf4d96d8a5159"><a name="a8a69f4abb0de49f78e9bf4d96d8a5159"></a><a name="a8a69f4abb0de49f78e9bf4d96d8a5159"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.3 "><p id="a729d13c927674865b84ddc653847e85a"><a name="a729d13c927674865b84ddc653847e85a"></a><a name="a729d13c927674865b84ddc653847e85a"></a>Double</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.87561243875613%" headers="mcps1.2.5.1.4 "><p id="abacc0f6e4fb64c6f9d55788c992310f6"><a name="abacc0f6e4fb64c6f9d55788c992310f6"></a><a name="abacc0f6e4fb64c6f9d55788c992310f6"></a>Snapshot size, expressed in GB.</p>
    </td>
    </tr>
    <tr id="r5ce50e8267f84d1481e923bc9470ed4d"><td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.1 "><p id="a02257cd410e4470d914afbb6e33b52e3"><a name="a02257cd410e4470d914afbb6e33b52e3"></a><a name="a02257cd410e4470d914afbb6e33b52e3"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.447755224477554%" headers="mcps1.2.5.1.2 "><p id="a6b4257e842954bbcb6de03d87c6bae33"><a name="a6b4257e842954bbcb6de03d87c6bae33"></a><a name="a6b4257e842954bbcb6de03d87c6bae33"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.3 "><p id="a93459c5932544c2092caf41855250360"><a name="a93459c5932544c2092caf41855250360"></a><a name="a93459c5932544c2092caf41855250360"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.87561243875613%" headers="mcps1.2.5.1.4 "><p id="ac24f77a2438643488dce30d87f6bfce3"><a name="ac24f77a2438643488dce30d87f6bfce3"></a><a name="ac24f77a2438643488dce30d87f6bfce3"></a>Snapshot status, which can be one of the following:</p>
    <a name="u7009614c436649a7b8675da64d7a3e0d"></a><a name="u7009614c436649a7b8675da64d7a3e0d"></a><ul id="u7009614c436649a7b8675da64d7a3e0d"><li><strong id="b842352706152546"><a name="b842352706152546"></a><a name="b842352706152546"></a>CREATING</strong></li><li><strong id="b335382630162424"><a name="b335382630162424"></a><a name="b335382630162424"></a>AVAILABLE</strong></li><li><strong id="b842352706162411"><a name="b842352706162411"></a><a name="b842352706162411"></a>UNAVAILABLE</strong></li></ul>
    </td>
    </tr>
    <tr id="rf9a33ba2a8b54e8ab4250642e6498d98"><td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.1 "><p id="a7fe72546037c4c02bc0dfc5f3e5e9673"><a name="a7fe72546037c4c02bc0dfc5f3e5e9673"></a><a name="a7fe72546037c4c02bc0dfc5f3e5e9673"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.447755224477554%" headers="mcps1.2.5.1.2 "><p id="a8cdbd10ea08b40f5966814b368dc5d91"><a name="a8cdbd10ea08b40f5966814b368dc5d91"></a><a name="a8cdbd10ea08b40f5966814b368dc5d91"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.3 "><p id="a31d24d1b49894ee790bf86e34f6a4ddf"><a name="a31d24d1b49894ee790bf86e34f6a4ddf"></a><a name="a31d24d1b49894ee790bf86e34f6a4ddf"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.87561243875613%" headers="mcps1.2.5.1.4 "><p id="a6cf7db9741cf4d10a2f3e0882c7a2b85"><a name="a6cf7db9741cf4d10a2f3e0882c7a2b85"></a><a name="a6cf7db9741cf4d10a2f3e0882c7a2b85"></a>Snapshot creation type. Currently, only <strong id="b842352706103021"><a name="b842352706103021"></a><a name="b842352706103021"></a>MANUAL</strong> is supported.</p>
    </td>
    </tr>
    <tr id="re798bf4f4951497abb484a67840f4ffe"><td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.1 "><p id="a078c39f5fde146db818756f5e835f1c0"><a name="a078c39f5fde146db818756f5e835f1c0"></a><a name="a078c39f5fde146db818756f5e835f1c0"></a>cluster_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.447755224477554%" headers="mcps1.2.5.1.2 "><p id="ab4b3c96de8a44fd4bfda84a743b890f3"><a name="ab4b3c96de8a44fd4bfda84a743b890f3"></a><a name="ab4b3c96de8a44fd4bfda84a743b890f3"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.3 "><p id="a42759dc8291340d292d8768dcef8135e"><a name="a42759dc8291340d292d8768dcef8135e"></a><a name="a42759dc8291340d292d8768dcef8135e"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.87561243875613%" headers="mcps1.2.5.1.4 "><p id="a8b843a420281400e894518ae3a9e7afc"><a name="a8b843a420281400e894518ae3a9e7afc"></a><a name="a8b843a420281400e894518ae3a9e7afc"></a>ID of the cluster for which a snapshot is created</p>
    </td>
    </tr>
    </tbody>
    </table>


## Returned Values<a name="s1036822a067a466da1109ae1ebb7de32"></a>

-   Normal

    200

-   Abnormal 

    **Table  3**  Returned value description

    <a name="t879ea391669b4d52b678ff171ed7d1b1"></a>
    <table><thead align="left"><tr id="re71b248e12ce49329996e8af4dd95642"><th class="cellrowborder" valign="top" width="38.379999999999995%" id="mcps1.2.3.1.1"><p id="a4156601fe0f141eaa9b97762af3a288b"><a name="a4156601fe0f141eaa9b97762af3a288b"></a><a name="a4156601fe0f141eaa9b97762af3a288b"></a><strong id="b84235270610317"><a name="b84235270610317"></a><a name="b84235270610317"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="61.62%" id="mcps1.2.3.1.2"><p id="ad5387a5717d84531a4f5343626e75e52"><a name="ad5387a5717d84531a4f5343626e75e52"></a><a name="ad5387a5717d84531a4f5343626e75e52"></a><strong id="b983014398"><a name="b983014398"></a><a name="b983014398"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r0b01a81f6d134f9db1028228e30c088a"><td class="cellrowborder" valign="top" width="38.379999999999995%" headers="mcps1.2.3.1.1 "><p id="a29053c2412564c96935dd4730de1d3fd"><a name="a29053c2412564c96935dd4730de1d3fd"></a><a name="a29053c2412564c96935dd4730de1d3fd"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.3.1.2 "><p id="ae343f1f3bc474dc9afa8d7d6e5d16930"><a name="ae343f1f3bc474dc9afa8d7d6e5d16930"></a><a name="ae343f1f3bc474dc9afa8d7d6e5d16930"></a>Request error.</p>
    </td>
    </tr>
    <tr id="r7bf3694410fa4b2492610b703f474d08"><td class="cellrowborder" valign="top" width="38.379999999999995%" headers="mcps1.2.3.1.1 "><p id="abbfa6aea23294afc934cb1b1618a9798"><a name="abbfa6aea23294afc934cb1b1618a9798"></a><a name="abbfa6aea23294afc934cb1b1618a9798"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.3.1.2 "><p id="a1af077fdec744dd78088302cecac3173"><a name="a1af077fdec744dd78088302cecac3173"></a><a name="a1af077fdec744dd78088302cecac3173"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="r8f6c8fea208445639655574369ff8a50"><td class="cellrowborder" valign="top" width="38.379999999999995%" headers="mcps1.2.3.1.1 "><p id="a20afad770b894fc0a332cf6823ab3233"><a name="a20afad770b894fc0a332cf6823ab3233"></a><a name="a20afad770b894fc0a332cf6823ab3233"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.3.1.2 "><p id="a5ef6134ecc864c28868c0d7206ea24d2"><a name="a5ef6134ecc864c28868c0d7206ea24d2"></a><a name="a5ef6134ecc864c28868c0d7206ea24d2"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="rdd4471769a284ab8a11ccdaddcce41b8"><td class="cellrowborder" valign="top" width="38.379999999999995%" headers="mcps1.2.3.1.1 "><p id="a7fafc5acc38a429899d59784e05b3fcf"><a name="a7fafc5acc38a429899d59784e05b3fcf"></a><a name="a7fafc5acc38a429899d59784e05b3fcf"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.3.1.2 "><p id="a63da58081cdd439389a2af77bb49c445"><a name="a63da58081cdd439389a2af77bb49c445"></a><a name="a63da58081cdd439389a2af77bb49c445"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="reec1c8fe7e344dc3bdbd808c51e9e2ba"><td class="cellrowborder" valign="top" width="38.379999999999995%" headers="mcps1.2.3.1.1 "><p id="a105f246de0e64b6f91a2f2c7999e3fd7"><a name="a105f246de0e64b6f91a2f2c7999e3fd7"></a><a name="a105f246de0e64b6f91a2f2c7999e3fd7"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.3.1.2 "><p id="a19be07e80603486f84a6de57873a173d"><a name="a19be07e80603486f84a6de57873a173d"></a><a name="a19be07e80603486f84a6de57873a173d"></a>Internal service error.</p>
    </td>
    </tr>
    <tr id="r63e38845fce74281b2b7e358303b6131"><td class="cellrowborder" valign="top" width="38.379999999999995%" headers="mcps1.2.3.1.1 "><p id="a45c47ef3f60c40f885bac907d7fb266f"><a name="a45c47ef3f60c40f885bac907d7fb266f"></a><a name="a45c47ef3f60c40f885bac907d7fb266f"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.3.1.2 "><p id="a246d6f8bc9da46e8ac1e2e42bbf3ef0d"><a name="a246d6f8bc9da46e8ac1e2e42bbf3ef0d"></a><a name="a246d6f8bc9da46e8ac1e2e42bbf3ef0d"></a>The service is unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


