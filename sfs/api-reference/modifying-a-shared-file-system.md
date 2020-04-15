# Modifying a Shared File System<a name="sfs_02_0026"></a>

## Function<a name="sa1160ada045246fdb31ec5a05b1da577"></a>

This API is used to modify the name and description of a shared file system.

## URI<a name="s0a5d778b389745598323cc30c04bdba3"></a>

-   PUT /v2/\{project\_id\}/shares/\{share\_id\}
-   Parameter description

    <a name="t8ac8686a00034bd98c93fe494e6edf07"></a>
    <table><thead align="left"><tr id="r802ae08e97b84627b2d4a97cbbfe58e8"><th class="cellrowborder" valign="top" width="17.29%" id="mcps1.1.5.1.1"><p id="p17124101410431"><a name="p17124101410431"></a><a name="p17124101410431"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.229999999999999%" id="mcps1.1.5.1.2"><p id="p1612415146430"><a name="p1612415146430"></a><a name="p1612415146430"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.17%" id="mcps1.1.5.1.3"><p id="p312416148432"><a name="p312416148432"></a><a name="p312416148432"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="48.309999999999995%" id="mcps1.1.5.1.4"><p id="p3124181464318"><a name="p3124181464318"></a><a name="p3124181464318"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="rda99634f23094e6083f1fd5a924f3268"><td class="cellrowborder" valign="top" width="17.29%" headers="mcps1.1.5.1.1 "><p id="ab88f7ee0ba7349ea8448dc55accd67e9"><a name="ab88f7ee0ba7349ea8448dc55accd67e9"></a><a name="ab88f7ee0ba7349ea8448dc55accd67e9"></a>share_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.1.5.1.2 "><p id="a65a88190b0614c4f96320d053a2dd5e2"><a name="a65a88190b0614c4f96320d053a2dd5e2"></a><a name="a65a88190b0614c4f96320d053a2dd5e2"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.17%" headers="mcps1.1.5.1.3 "><p id="a70f1dbb49a404dbe95f5e93125d07404"><a name="a70f1dbb49a404dbe95f5e93125d07404"></a><a name="a70f1dbb49a404dbe95f5e93125d07404"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.309999999999995%" headers="mcps1.1.5.1.4 "><p id="a4626fde818c640fdb588ee2877762ea9"><a name="a4626fde818c640fdb588ee2877762ea9"></a><a name="a4626fde818c640fdb588ee2877762ea9"></a>Specifies the UUID of the shared file system.</p>
    </td>
    </tr>
    <tr id="rcab3351d8c5b4d4f8395aa538166bdbd"><td class="cellrowborder" valign="top" width="17.29%" headers="mcps1.1.5.1.1 "><p id="af220083f955243028b4b4333561e6ebe"><a name="af220083f955243028b4b4333561e6ebe"></a><a name="af220083f955243028b4b4333561e6ebe"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.1.5.1.2 "><p id="a06a1e099332f4c39a7015d80616cd819"><a name="a06a1e099332f4c39a7015d80616cd819"></a><a name="a06a1e099332f4c39a7015d80616cd819"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.17%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0064390795_p220903181347"><a name="en-us_topic_0064390795_p220903181347"></a><a name="en-us_topic_0064390795_p220903181347"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.309999999999995%" headers="mcps1.1.5.1.4 "><p id="adc9f3a14f69f4632ac569830b59123b9"><a name="adc9f3a14f69f4632ac569830b59123b9"></a><a name="adc9f3a14f69f4632ac569830b59123b9"></a>Specifies the project ID of the operator.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="sf9a4b455b8dd467e91189aecc126dcc1"></a>

-   Parameter description

    <a name="t97e007a9334f453bbd2613d1a3c0c93f"></a>
    <table><thead align="left"><tr id="r630be26f2eae4ada98d4105eddfbc192"><th class="cellrowborder" valign="top" width="17.401740174017398%" id="mcps1.1.5.1.1"><p id="p719013935913"><a name="p719013935913"></a><a name="p719013935913"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.46154615461546%" id="mcps1.1.5.1.2"><p id="p21901194598"><a name="p21901194598"></a><a name="p21901194598"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.98189818981898%" id="mcps1.1.5.1.3"><p id="p1320610935919"><a name="p1320610935919"></a><a name="p1320610935919"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="48.154815481548155%" id="mcps1.1.5.1.4"><p id="p32066955914"><a name="p32066955914"></a><a name="p32066955914"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="racc482aa497b43e8958d45bb96883a63"><td class="cellrowborder" valign="top" width="17.401740174017398%" headers="mcps1.1.5.1.1 "><p id="ae96323d4b6754d5c9117a2a1264df13f"><a name="ae96323d4b6754d5c9117a2a1264df13f"></a><a name="ae96323d4b6754d5c9117a2a1264df13f"></a>share</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.46154615461546%" headers="mcps1.1.5.1.2 "><p id="aee67c57c35e54ffcbcc0cd5d69db4057"><a name="aee67c57c35e54ffcbcc0cd5d69db4057"></a><a name="aee67c57c35e54ffcbcc0cd5d69db4057"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.98189818981898%" headers="mcps1.1.5.1.3 "><p id="a04d0c658e0bc480587b87bcaeb64201e"><a name="a04d0c658e0bc480587b87bcaeb64201e"></a><a name="a04d0c658e0bc480587b87bcaeb64201e"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.154815481548155%" headers="mcps1.1.5.1.4 "><p id="a7de878600fff4565b2fde3407f96f209"><a name="a7de878600fff4565b2fde3407f96f209"></a><a name="a7de878600fff4565b2fde3407f96f209"></a>Specifies the share object.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Description of the  **share**  field

    <a name="t202c3d1114554f98b1c065b64c82c77d"></a>
    <table><thead align="left"><tr id="r8d1ba0a9377244d88df0278563aaa4d8"><th class="cellrowborder" valign="top" width="17.731773177317734%" id="mcps1.1.5.1.1"><p id="p598761115595"><a name="p598761115595"></a><a name="p598761115595"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.101510151015102%" id="mcps1.1.5.1.2"><p id="p13987101115594"><a name="p13987101115594"></a><a name="p13987101115594"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.401940194019403%" id="mcps1.1.5.1.3"><p id="p19987141175912"><a name="p19987141175912"></a><a name="p19987141175912"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="47.76477647764777%" id="mcps1.1.5.1.4"><p id="p2098771165910"><a name="p2098771165910"></a><a name="p2098771165910"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r28040c369fef40b4a423be627213f5bd"><td class="cellrowborder" valign="top" width="17.731773177317734%" headers="mcps1.1.5.1.1 "><p id="a1822ac749a4f4efd83a846c62f1e4452"><a name="a1822ac749a4f4efd83a846c62f1e4452"></a><a name="a1822ac749a4f4efd83a846c62f1e4452"></a>display_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.101510151015102%" headers="mcps1.1.5.1.2 "><p id="a0b365c8140664fd8b72baa80d3bcd01c"><a name="a0b365c8140664fd8b72baa80d3bcd01c"></a><a name="a0b365c8140664fd8b72baa80d3bcd01c"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.401940194019403%" headers="mcps1.1.5.1.3 "><p id="a215adcd3228744c5b256bf4fd0d964bd"><a name="a215adcd3228744c5b256bf4fd0d964bd"></a><a name="a215adcd3228744c5b256bf4fd0d964bd"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.76477647764777%" headers="mcps1.1.5.1.4 "><p id="a856c857adbe9468b8e62c888918003c1"><a name="a856c857adbe9468b8e62c888918003c1"></a><a name="a856c857adbe9468b8e62c888918003c1"></a>Specifies the new name of the shared file system. The value consists of 0 to 255 characters.</p>
    </td>
    </tr>
    <tr id="r6143cc9af3944ecf82fa9cde09c04c4b"><td class="cellrowborder" valign="top" width="17.731773177317734%" headers="mcps1.1.5.1.1 "><p id="a4391493ee9ce4e73a508c1dcd839e8a4"><a name="a4391493ee9ce4e73a508c1dcd839e8a4"></a><a name="a4391493ee9ce4e73a508c1dcd839e8a4"></a>display_description</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.101510151015102%" headers="mcps1.1.5.1.2 "><p id="abb53e69780ba4b19a532b2018a7dad07"><a name="abb53e69780ba4b19a532b2018a7dad07"></a><a name="abb53e69780ba4b19a532b2018a7dad07"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.401940194019403%" headers="mcps1.1.5.1.3 "><p id="a4345f3d66443477b9946dcbfe1c7549f"><a name="a4345f3d66443477b9946dcbfe1c7549f"></a><a name="a4345f3d66443477b9946dcbfe1c7549f"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.76477647764777%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0064390795_p536254181347"><a name="en-us_topic_0064390795_p536254181347"></a><a name="en-us_topic_0064390795_p536254181347"></a>Describes the shared file system. The value contains 0 to 255 characters.</p>
    </td>
    </tr>
    <tr id="row8646436155211"><td class="cellrowborder" valign="top" width="17.731773177317734%" headers="mcps1.1.5.1.1 "><p id="p5646173613522"><a name="p5646173613522"></a><a name="p5646173613522"></a>is_public</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.101510151015102%" headers="mcps1.1.5.1.2 "><p id="p11646123615526"><a name="p11646123615526"></a><a name="p11646123615526"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.401940194019403%" headers="mcps1.1.5.1.3 "><p id="p12646153618524"><a name="p12646153618524"></a><a name="p12646153618524"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.76477647764777%" headers="mcps1.1.5.1.4 "><p id="a8ba58545b5ab4eebb1ded66c86c2212b"><a name="a8ba58545b5ab4eebb1ded66c86c2212b"></a><a name="a8ba58545b5ab4eebb1ded66c86c2212b"></a>(Supported by API v2.8 and later versions.) Specifies whether a file system can be publicly seen. If it is set to <strong id="b19718811101312"><a name="b19718811101312"></a><a name="b19718811101312"></a>true</strong>, the file system can be seen publicly. If it is set to <strong id="b77191411181317"><a name="b77191411181317"></a><a name="b77191411181317"></a>false</strong>, the file system can be seen privately. The default value is <strong id="b1872161181311"><a name="b1872161181311"></a><a name="b1872161181311"></a>false</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    {
        "share": {
            "display_name": "testshare",
            "display_description": "test"
        }
    }
    ```


## Response<a name="sbbc5e0545135406aae43b288bf052255"></a>

-   Parameter description

    <a name="tdf5852da1df842c4b1ef530355091025"></a>
    <table><thead align="left"><tr id="re0d7e71c0033415da7b0854802b4d7ec"><th class="cellrowborder" valign="top" width="20.7%" id="mcps1.1.4.1.1"><p id="p3627161513596"><a name="p3627161513596"></a><a name="p3627161513596"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.689999999999998%" id="mcps1.1.4.1.2"><p id="p962711514592"><a name="p962711514592"></a><a name="p962711514592"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.61000000000001%" id="mcps1.1.4.1.3"><p id="p2627141565920"><a name="p2627141565920"></a><a name="p2627141565920"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="rc2a0adc67f6444bb9b9fa538a274c843"><td class="cellrowborder" valign="top" width="20.7%" headers="mcps1.1.4.1.1 "><p id="a0e38f06710a84c9eb8c2d6d03fd85dd9"><a name="a0e38f06710a84c9eb8c2d6d03fd85dd9"></a><a name="a0e38f06710a84c9eb8c2d6d03fd85dd9"></a>share</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.689999999999998%" headers="mcps1.1.4.1.2 "><p id="aefbbc00c8a9c4653aec5744d6c29acc0"><a name="aefbbc00c8a9c4653aec5744d6c29acc0"></a><a name="aefbbc00c8a9c4653aec5744d6c29acc0"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.61000000000001%" headers="mcps1.1.4.1.3 "><p id="a42ad98408cfe46d8922b95d480a5c8b1"><a name="a42ad98408cfe46d8922b95d480a5c8b1"></a><a name="a42ad98408cfe46d8922b95d480a5c8b1"></a>Specifies the share object.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Description of the  **share**  field

    <a name="table0134127194218"></a>
    <table><thead align="left"><tr id="row713414754211"><th class="cellrowborder" valign="top" width="18.84%" id="mcps1.1.4.1.1"><p id="p1513418714426"><a name="p1513418714426"></a><a name="p1513418714426"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.97%" id="mcps1.1.4.1.2"><p id="p1913420714210"><a name="p1913420714210"></a><a name="p1913420714210"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="58.19%" id="mcps1.1.4.1.3"><p id="p61349719426"><a name="p61349719426"></a><a name="p61349719426"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row113437114217"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p28090732115456"><a name="en-us_topic_0064390794_p28090732115456"></a><a name="en-us_topic_0064390794_p28090732115456"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p60756818115456"><a name="en-us_topic_0064390794_p60756818115456"></a><a name="en-us_topic_0064390794_p60756818115456"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p53809467171857"><a name="en-us_topic_0064390794_p53809467171857"></a><a name="en-us_topic_0064390794_p53809467171857"></a>Specifies the links of shared file systems.</p>
    </td>
    </tr>
    <tr id="row71351376429"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p20630446115456"><a name="en-us_topic_0064390794_p20630446115456"></a><a name="en-us_topic_0064390794_p20630446115456"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p60453459115456"><a name="en-us_topic_0064390794_p60453459115456"></a><a name="en-us_topic_0064390794_p60453459115456"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p35525415171857"><a name="en-us_topic_0064390794_p35525415171857"></a><a name="en-us_topic_0064390794_p35525415171857"></a>Specifies the availability zone.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row5492535895012"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p1976898095012"><a name="en-us_topic_0064390794_p1976898095012"></a><a name="en-us_topic_0064390794_p1976898095012"></a>share_server_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p4995572295012"><a name="en-us_topic_0064390794_p4995572295012"></a><a name="en-us_topic_0064390794_p4995572295012"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p1988170695012"><a name="en-us_topic_0064390794_p1988170695012"></a><a name="en-us_topic_0064390794_p1988170695012"></a>Specifies the UUID for managing share services.</p>
    </td>
    </tr>
    <tr id="row513515716426"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p27750209115456"><a name="en-us_topic_0064390794_p27750209115456"></a><a name="en-us_topic_0064390794_p27750209115456"></a>share_network_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p33174447115456"><a name="en-us_topic_0064390794_p33174447115456"></a><a name="en-us_topic_0064390794_p33174447115456"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p59674002171857"><a name="en-us_topic_0064390794_p59674002171857"></a><a name="en-us_topic_0064390794_p59674002171857"></a>Specifies the UUID of the share network. This parameter is reserved, because share network management is not supported currently.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row39279891115440"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p39186779115456"><a name="en-us_topic_0064390794_p39186779115456"></a><a name="en-us_topic_0064390794_p39186779115456"></a>snapshot_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p20012545115456"><a name="en-us_topic_0064390794_p20012545115456"></a><a name="en-us_topic_0064390794_p20012545115456"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p17092907171857"><a name="en-us_topic_0064390794_p17092907171857"></a><a name="en-us_topic_0064390794_p17092907171857"></a>Specifies the UUID of the source snapshot that is used to create the shared file system. This parameter is reserved, because snapshots are not supported currently.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row5321904710035"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p1577556910035"><a name="en-us_topic_0064390794_p1577556910035"></a><a name="en-us_topic_0064390794_p1577556910035"></a>snapshot_support</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p2164239410035"><a name="en-us_topic_0064390794_p2164239410035"></a><a name="en-us_topic_0064390794_p2164239410035"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="p151357713425"><a name="p151357713425"></a><a name="p151357713425"></a>Specifies whether snapshots are supported. This parameter is reserved, because snapshots are not supported currently.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row66254026115429"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p66240344115456"><a name="en-us_topic_0064390794_p66240344115456"></a><a name="en-us_topic_0064390794_p66240344115456"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p63867663115456"><a name="en-us_topic_0064390794_p63867663115456"></a><a name="en-us_topic_0064390794_p63867663115456"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p45589478171857"><a name="en-us_topic_0064390794_p45589478171857"></a><a name="en-us_topic_0064390794_p45589478171857"></a>Specifies the UUID of the shared file system.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row25775244115437"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p57485250115456"><a name="en-us_topic_0064390794_p57485250115456"></a><a name="en-us_topic_0064390794_p57485250115456"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p25793701115456"><a name="en-us_topic_0064390794_p25793701115456"></a><a name="en-us_topic_0064390794_p25793701115456"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p42544068172855"><a name="en-us_topic_0064390794_p42544068172855"></a><a name="en-us_topic_0064390794_p42544068172855"></a>Specifies the size (GB) of the shared file system.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row2811743793851"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="p141361278423"><a name="p141361278423"></a><a name="p141361278423"></a>share_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="p191361718428"><a name="p191361718428"></a><a name="p191361718428"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="p913617713429"><a name="p913617713429"></a><a name="p913617713429"></a>(Supported by API versions from v2.31 to v2.42) Specifies the UUID of a consistency group. This parameter is reserved, because consistency groups are not supported currently.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row14146850115432"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p43647722115456"><a name="en-us_topic_0064390794_p43647722115456"></a><a name="en-us_topic_0064390794_p43647722115456"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p45804593115456"><a name="en-us_topic_0064390794_p45804593115456"></a><a name="en-us_topic_0064390794_p45804593115456"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p36017679171857"><a name="en-us_topic_0064390794_p36017679171857"></a><a name="en-us_topic_0064390794_p36017679171857"></a>Specifies the UUID of the project to which the shared file system belongs.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row27677209115427"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p30561506115456"><a name="en-us_topic_0064390794_p30561506115456"></a><a name="en-us_topic_0064390794_p30561506115456"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p59562882115456"><a name="en-us_topic_0064390794_p59562882115456"></a><a name="en-us_topic_0064390794_p59562882115456"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390792_p42083247173855"><a name="en-us_topic_0064390792_p42083247173855"></a><a name="en-us_topic_0064390792_p42083247173855"></a>Sets one or more metadata key and value pairs as a dictionary of strings. <strong id="b1139105052915"><a name="b1139105052915"></a><a name="b1139105052915"></a>share_used</strong> is the key, and the corresponding value is the used capacity of the shared file system in the unit of Bytes. </p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row21024096115415"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p23577146115456"><a name="en-us_topic_0064390794_p23577146115456"></a><a name="en-us_topic_0064390794_p23577146115456"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p30700686115456"><a name="en-us_topic_0064390794_p30700686115456"></a><a name="en-us_topic_0064390794_p30700686115456"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p9195044171857"><a name="en-us_topic_0064390794_p9195044171857"></a><a name="en-us_topic_0064390794_p9195044171857"></a>Specifies the status of the shared file system.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row665580195924"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="p81362717422"><a name="p81362717422"></a><a name="p81362717422"></a>task_state</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p5905231595924"><a name="en-us_topic_0064390794_p5905231595924"></a><a name="en-us_topic_0064390794_p5905231595924"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p1850821095924"><a name="en-us_topic_0064390794_p1850821095924"></a><a name="en-us_topic_0064390794_p1850821095924"></a>Specifies the data migration status. This parameter is reserved, because data migration is not supported currently.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row939599610316"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p2287823910316"><a name="en-us_topic_0064390794_p2287823910316"></a><a name="en-us_topic_0064390794_p2287823910316"></a>has_replicas</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p4870772510316"><a name="en-us_topic_0064390794_p4870772510316"></a><a name="en-us_topic_0064390794_p4870772510316"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p5301165710316"><a name="en-us_topic_0064390794_p5301165710316"></a><a name="en-us_topic_0064390794_p5301165710316"></a>(Supported by API versions from v2.11 to v2.42) Specifies whether any replication exists. This parameter is reserved, because replication is not supported currently.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row48841735810"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p1388510311817"><a name="en-us_topic_0064390794_p1388510311817"></a><a name="en-us_topic_0064390794_p1388510311817"></a>replication_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="p161371471421"><a name="p161371471421"></a><a name="p161371471421"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="p21373711424"><a name="p21373711424"></a><a name="p21373711424"></a>(Supported by API versions from v2.11 to v2.42) Specifies the replication type. This parameter is reserved, because replication is not supported currently.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row38372338115421"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p61202789115456"><a name="en-us_topic_0064390794_p61202789115456"></a><a name="en-us_topic_0064390794_p61202789115456"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p58478870115456"><a name="en-us_topic_0064390794_p58478870115456"></a><a name="en-us_topic_0064390794_p58478870115456"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p59409689171857"><a name="en-us_topic_0064390794_p59409689171857"></a><a name="en-us_topic_0064390794_p59409689171857"></a>Describes the shared file system.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row35274029115424"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p58169755115456"><a name="en-us_topic_0064390794_p58169755115456"></a><a name="en-us_topic_0064390794_p58169755115456"></a>host</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p14129699115456"><a name="en-us_topic_0064390794_p14129699115456"></a><a name="en-us_topic_0064390794_p14129699115456"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p24446366171857"><a name="en-us_topic_0064390794_p24446366171857"></a><a name="en-us_topic_0064390794_p24446366171857"></a>Specifies the name of the host. This field is visible only to the administrator.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row10855127115417"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p66003741115456"><a name="en-us_topic_0064390794_p66003741115456"></a><a name="en-us_topic_0064390794_p66003741115456"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p44702790115456"><a name="en-us_topic_0064390794_p44702790115456"></a><a name="en-us_topic_0064390794_p44702790115456"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p37552527171857"><a name="en-us_topic_0064390794_p37552527171857"></a><a name="en-us_topic_0064390794_p37552527171857"></a>Specifies the name of the shared file system.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row6259894411544"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p66214260115456"><a name="en-us_topic_0064390794_p66214260115456"></a><a name="en-us_topic_0064390794_p66214260115456"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p61754840115456"><a name="en-us_topic_0064390794_p61754840115456"></a><a name="en-us_topic_0064390794_p61754840115456"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p62484878171857"><a name="en-us_topic_0064390794_p62484878171857"></a><a name="en-us_topic_0064390794_p62484878171857"></a>Specifies the date and time stamp when the shared file system was created.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row2256685795641"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p1597610695641"><a name="en-us_topic_0064390794_p1597610695641"></a><a name="en-us_topic_0064390794_p1597610695641"></a>access_rules_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p6230051595641"><a name="en-us_topic_0064390794_p6230051595641"></a><a name="en-us_topic_0064390794_p6230051595641"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p1317697095641"><a name="en-us_topic_0064390794_p1317697095641"></a><a name="en-us_topic_0064390794_p1317697095641"></a>(Supported by API versions from v2.10 to v2.27.) Specifies the configuration status of the access rule. Possible values are <strong id="b476118150156"><a name="b476118150156"></a><a name="b476118150156"></a>active</strong> (effective), <strong id="b1878131561510"><a name="b1878131561510"></a><a name="b1878131561510"></a>error</strong> (configuration failed), and <strong id="b2783151521515"><a name="b2783151521515"></a><a name="b2783151521515"></a>syncing</strong> (configuration in progress).</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row66328432115411"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p11825073115456"><a name="en-us_topic_0064390794_p11825073115456"></a><a name="en-us_topic_0064390794_p11825073115456"></a>share_proto</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p18306875115456"><a name="en-us_topic_0064390794_p18306875115456"></a><a name="en-us_topic_0064390794_p18306875115456"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p51666373171857"><a name="en-us_topic_0064390794_p51666373171857"></a><a name="en-us_topic_0064390794_p51666373171857"></a>Specifies the protocol for sharing file systems.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row4389128911547"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p54695598115456"><a name="en-us_topic_0064390794_p54695598115456"></a><a name="en-us_topic_0064390794_p54695598115456"></a>volume_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p1158423115456"><a name="en-us_topic_0064390794_p1158423115456"></a><a name="en-us_topic_0064390794_p1158423115456"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p16713897171857"><a name="en-us_topic_0064390794_p16713897171857"></a><a name="en-us_topic_0064390794_p16713897171857"></a>Specifies the volume type. The definition of this parameter is the same as that of <strong id="b16209938113115"><a name="b16209938113115"></a><a name="b16209938113115"></a>share_type</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row1997612012118"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="p191382720428"><a name="p191382720428"></a><a name="p191382720428"></a>share_type_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p6682275212118"><a name="en-us_topic_0064390794_p6682275212118"></a><a name="en-us_topic_0064390794_p6682275212118"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p55872650172937"><a name="en-us_topic_0064390794_p55872650172937"></a><a name="en-us_topic_0064390794_p55872650172937"></a>Specifies the storage service type assigned for the shared file system, such as high-performance storage (composed of SSDs) and large-capacity storage (composed of SATA disks).</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row6380688295244"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="p171393784215"><a name="p171393784215"></a><a name="p171393784215"></a>share_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p2135204095244"><a name="en-us_topic_0064390794_p2135204095244"></a><a name="en-us_topic_0064390794_p2135204095244"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p5179364095244"><a name="en-us_topic_0064390794_p5179364095244"></a><a name="en-us_topic_0064390794_p5179364095244"></a>Specifies the UUID of the share type.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row1256499495932"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="p5139272427"><a name="p5139272427"></a><a name="p5139272427"></a>export_locations</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="p171391575425"><a name="p171391575425"></a><a name="p171391575425"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="p121391714216"><a name="p121391714216"></a><a name="p121391714216"></a>Lists the mount locations. Currently, only a single mount location is supported. This parameter exists only when <strong id="b1669635310317"><a name="b1669635310317"></a><a name="b1669635310317"></a>X-Openstack-Manila-Api-Version</strong> specified in the request header is smaller than <strong id="b1469719536319"><a name="b1469719536319"></a><a name="b1469719536319"></a>2.8</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row1105050495936"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="p01391744212"><a name="p01391744212"></a><a name="p01391744212"></a>export_location</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="p1213997204213"><a name="p1213997204213"></a><a name="p1213997204213"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="p01399713422"><a name="p01399713422"></a><a name="p01399713422"></a>Specifies the mount location. This parameter exists only when <strong id="b36655599317"><a name="b36655599317"></a><a name="b36655599317"></a>X-Openstack-Manila-Api-Version</strong> specified in the request header is smaller than <strong id="b19666105914313"><a name="b19666105914313"></a><a name="b19666105914313"></a>2.8</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row760346112115"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p1190063912115"><a name="en-us_topic_0064390794_p1190063912115"></a><a name="en-us_topic_0064390794_p1190063912115"></a>is_public</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p2442773012115"><a name="en-us_topic_0064390794_p2442773012115"></a><a name="en-us_topic_0064390794_p2442773012115"></a>Bool</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="p111398774211"><a name="p111398774211"></a><a name="p111398774211"></a>(Supported by API versions from v2.8 to v2.42). Specifies whether a file system can be publicly seen. If it is set to <strong id="b1783672333213"><a name="b1783672333213"></a><a name="b1783672333213"></a>true</strong>, the file system can be seen publicly. If it is set to <strong id="b138382237325"><a name="b138382237325"></a><a name="b138382237325"></a>false</strong>, the file system can be seen privately. The default value is <strong id="b583818239324"><a name="b583818239324"></a><a name="b583818239324"></a>false</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row138591369913"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="p121392744219"><a name="p121392744219"></a><a name="p121392744219"></a>source_share_group_snapshot_member_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p1486018614919"><a name="en-us_topic_0064390794_p1486018614919"></a><a name="en-us_topic_0064390794_p1486018614919"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="p1513912715422"><a name="p1513912715422"></a><a name="p1513912715422"></a>(Supported by API v2.31 and later versions.) Specifies the UUID of a consistency snapshot source. Currently, the consistency group is not supported. This field is reserved.</p>
    </td>
    </tr>
    <tr id="row14139187144219"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="p1314013713421"><a name="p1314013713421"></a><a name="p1314013713421"></a>revert_to_snapshot_support</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="p81409704220"><a name="p81409704220"></a><a name="p81409704220"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="p514057104218"><a name="p514057104218"></a><a name="p514057104218"></a>(Supported by API v2.27 and later versions.) Specifies whether reversion to snapshot is supported. Currently, snapshot is not supported. This field is reserved.</p>
    </td>
    </tr>
    <tr id="row514015764219"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="p914037164212"><a name="p914037164212"></a><a name="p914037164212"></a>create_share_from_snapshot_support</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="p183731148374"><a name="p183731148374"></a><a name="p183731148374"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="p31401575429"><a name="p31401575429"></a><a name="p31401575429"></a>(Supported by API v2.24 and later versions.) Specifies whether creating file systems from snapshot is supported. Currently, snapshot is not supported. This field is reserved.</p>
    </td>
    </tr>
    <tr id="row51401973428"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="p814012724211"><a name="p814012724211"></a><a name="p814012724211"></a>mount_snapshot_support</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="p1542014812379"><a name="p1542014812379"></a><a name="p1542014812379"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="p121409715427"><a name="p121409715427"></a><a name="p121409715427"></a>(Supported by API v2.32 and later versions.) Specifies whether snapshot mounting is supported. Currently, snapshot is not supported. This field is reserved.</p>
    </td>
    </tr>
    <tr id="row181401778427"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="p914011716422"><a name="p914011716422"></a><a name="p914011716422"></a>user_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="p314014724213"><a name="p314014724213"></a><a name="p314014724213"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="p61407734218"><a name="p61407734218"></a><a name="p61407734218"></a>(Supported by API v2.16 and later versions.) Specifies the user ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
      "share": {
        "status": "available",
        "share_type_name": "sla",
        "description": "test",
        "links": [
          {
            "href": "https://192.168.196.47:8796/v2/07412155bf474db9a2f697fd978593d7/shares/f26d867f-9876-433d-8db2-25d210f29309",
            "rel": "self"
          },
          {
            "href": "https://192.168.196.47:8796/07412155bf474db9a2f697fd978593d7/shares/f26d867f-9876-433d-8db2-25d210f29309",
            "rel": "bookmark"
          }
        ],
        "availability_zone": "az1.dc1",
        "share_network_id": null,
        "share_server_id": null,
        "share_group_id": null,
        "host": "DJ38@a4588256-3880-4136-b3c9-4c3aade8a84b#a4588256-3880-4136-b3c9-4c3aade8a84b",
        "revert_to_snapshot_support": null,
        "access_rules_status": "active",
        "snapshot_id": null,
        "create_share_from_snapshot_support": null,
        "is_public": true,
        "task_state": null,
        "snapshot_support": true,
        "id": "f26d867f-9876-433d-8db2-25d210f29309",
        "size": 1,
        "source_share_group_snapshot_member_id": null,
        "user_id": "daa3f8f8d7254465841da769298a76f6",
        "name": "manila share",
        "share_type": "8ae4e74e-83f4-4980-8ab8-e637f9294e0b",
        "has_replicas": false,
        "replication_type": null,
        "created_at": "2018-12-25T08:45:22.525899",
        "share_proto": "NFS",
        "volume_type": "sla",
        "mount_snapshot_support": null,
        "project_id": "07412155bf474db9a2f697fd978593d7",
        "metadata": {
          "share_key": "test",
          "share_used": "1",
        }
      }
    }
    ```


## Status Codes<a name="s67ffd29ee1f5428aaada0d4eccf99f16"></a>

-   Normal

    200

-   Abnormal

    <a name="tb821a17345624de98659535802d83ebc"></a>
    <table><thead align="left"><tr id="r0b3f082adf4c41638a0f6aa012f896fb"><th class="cellrowborder" valign="top" width="43.43%" id="mcps1.1.3.1.1"><p id="acef9aac3848d42f48c037e52944cd12c"><a name="acef9aac3848d42f48c037e52944cd12c"></a><a name="acef9aac3848d42f48c037e52944cd12c"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.57%" id="mcps1.1.3.1.2"><p id="a97333bb202db4d7d88fabb2ae8efa4e8"><a name="a97333bb202db4d7d88fabb2ae8efa4e8"></a><a name="a97333bb202db4d7d88fabb2ae8efa4e8"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r51284b226b4c406b8451253ff9681642"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="ab9af9c126dbc4a0b878d5dd33939f5f4"><a name="ab9af9c126dbc4a0b878d5dd33939f5f4"></a><a name="ab9af9c126dbc4a0b878d5dd33939f5f4"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="ac1afd6b5b61140efbf78093a2e6488b2"><a name="ac1afd6b5b61140efbf78093a2e6488b2"></a><a name="ac1afd6b5b61140efbf78093a2e6488b2"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="r2cfeac6a11704a6ea6dfebf22996b869"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="a404e032a5877497aa63b4f1118eb4696"><a name="a404e032a5877497aa63b4f1118eb4696"></a><a name="a404e032a5877497aa63b4f1118eb4696"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="aabf0a4db7bd44655a244c2b6b3db4ad7"><a name="aabf0a4db7bd44655a244c2b6b3db4ad7"></a><a name="aabf0a4db7bd44655a244c2b6b3db4ad7"></a>You must enter a username and the password to access the requested page.</p>
    </td>
    </tr>
    <tr id="reaef80cf151a42e0818ab91f7277d1f8"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="a340ae945c78245be83f3852f901a9ea4"><a name="a340ae945c78245be83f3852f901a9ea4"></a><a name="a340ae945c78245be83f3852f901a9ea4"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="a7ba1fac3a81c44be88cd1860deab9048"><a name="a7ba1fac3a81c44be88cd1860deab9048"></a><a name="a7ba1fac3a81c44be88cd1860deab9048"></a>Access to the requested page is forbidden.</p>
    </td>
    </tr>
    <tr id="r15e60137c04b4ec18b7311cade346d6b"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="a26fb2966067d4e6797a1b91c416d6aab"><a name="a26fb2966067d4e6797a1b91c416d6aab"></a><a name="a26fb2966067d4e6797a1b91c416d6aab"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="ac3e6ea5688d04b3682ec2c6322f74bba"><a name="ac3e6ea5688d04b3682ec2c6322f74bba"></a><a name="ac3e6ea5688d04b3682ec2c6322f74bba"></a>The requested page was not found.</p>
    </td>
    </tr>
    <tr id="rbbc10ff2055b42d09b9f341d238cfc6e"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="a499d5172c5df4561a9ae04439daba950"><a name="a499d5172c5df4561a9ae04439daba950"></a><a name="a499d5172c5df4561a9ae04439daba950"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="a06060d1eccff4d1d8c4f1c9bb8c6c06d"><a name="a06060d1eccff4d1d8c4f1c9bb8c6c06d"></a><a name="a06060d1eccff4d1d8c4f1c9bb8c6c06d"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="rc279e646b0a5421aa94241a1b72a086b"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="aa5ade6189c1546e9b54517d21d8cce5b"><a name="aa5ade6189c1546e9b54517d21d8cce5b"></a><a name="aa5ade6189c1546e9b54517d21d8cce5b"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="abb881446875245d89a0c36b723ebca50"><a name="abb881446875245d89a0c36b723ebca50"></a><a name="abb881446875245d89a0c36b723ebca50"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="r389f9a080d1941a597bbfb353b5df07f"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="ac1b2432c743448689e3a3d5d9dbf3731"><a name="ac1b2432c743448689e3a3d5d9dbf3731"></a><a name="ac1b2432c743448689e3a3d5d9dbf3731"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="a16e480571afe4adda10ec2e577578ed1"><a name="a16e480571afe4adda10ec2e577578ed1"></a><a name="a16e480571afe4adda10ec2e577578ed1"></a>You must use the proxy server for authentication. Then the request can be processed.</p>
    </td>
    </tr>
    <tr id="r2c052733abb64ec6a14129064cc430ba"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="aab6873867794478db405d16535eb82c1"><a name="aab6873867794478db405d16535eb82c1"></a><a name="aab6873867794478db405d16535eb82c1"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="a751143c633b0409abe4a49dfb4336611"><a name="a751143c633b0409abe4a49dfb4336611"></a><a name="a751143c633b0409abe4a49dfb4336611"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="r8a557c631fe34673a316c0e35c43d11f"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="a11f78520ce454afa806b191726b05b98"><a name="a11f78520ce454afa806b191726b05b98"></a><a name="a11f78520ce454afa806b191726b05b98"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="a79c1005df3304652aa107ca4f8abae55"><a name="a79c1005df3304652aa107ca4f8abae55"></a><a name="a79c1005df3304652aa107ca4f8abae55"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="re0f1fec4130c4099a3cbcde0b1e3a80e"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="ae624ac724b1d4895b4b37568a291ea3b"><a name="ae624ac724b1d4895b4b37568a291ea3b"></a><a name="ae624ac724b1d4895b4b37568a291ea3b"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="adcdb68f97219406da5385dc244175657"><a name="adcdb68f97219406da5385dc244175657"></a><a name="adcdb68f97219406da5385dc244175657"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="r4577c64201a8441eadd7529a1a2e6acb"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="a3d868f6ce411447c9290a080cae1307b"><a name="a3d868f6ce411447c9290a080cae1307b"></a><a name="a3d868f6ce411447c9290a080cae1307b"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="a8c70145b16364158ba5fc1a2c1f70372"><a name="a8c70145b16364158ba5fc1a2c1f70372"></a><a name="a8c70145b16364158ba5fc1a2c1f70372"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="red727416b1d046418a0d8b444b167f95"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="a33226e68d6a642a38bcfc6e95d83b329"><a name="a33226e68d6a642a38bcfc6e95d83b329"></a><a name="a33226e68d6a642a38bcfc6e95d83b329"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="aaabf966a8b734b0193a3af072e306369"><a name="aaabf966a8b734b0193a3af072e306369"></a><a name="aaabf966a8b734b0193a3af072e306369"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="r6ddf83d4972c491597bc600bd18fd54f"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="a5ed1e91bf8d144e5b3f8bcb2e0c068e2"><a name="a5ed1e91bf8d144e5b3f8bcb2e0c068e2"></a><a name="a5ed1e91bf8d144e5b3f8bcb2e0c068e2"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="a773dff55471644a4b695f6114926b8ef"><a name="a773dff55471644a4b695f6114926b8ef"></a><a name="a773dff55471644a4b695f6114926b8ef"></a>Failed to complete the request because the service is unavailable.</p>
    </td>
    </tr>
    <tr id="r392c7cc8e7d94db1b351f16b7d5a1c04"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="a87c93879d70546c3a748b20464da55ac"><a name="a87c93879d70546c3a748b20464da55ac"></a><a name="a87c93879d70546c3a748b20464da55ac"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="a484ae04f3e674672963a238f5925e5c2"><a name="a484ae04f3e674672963a238f5925e5c2"></a><a name="a484ae04f3e674672963a238f5925e5c2"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


