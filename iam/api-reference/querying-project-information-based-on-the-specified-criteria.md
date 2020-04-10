# Querying Project Information Based on the Specified Criteria<a name="en-us_topic_0057845625"></a>

## Function Description<a name="s380dc90cda6c4acba39c06b7dd2ce1e9"></a>

This interface is used to query project information based on the specified criteria.

## URI<a name="sf615d5ea5cc44edf8d9960f0bc981e97"></a>

-   URI format

    GET /v3/projects\{?domain\_id,name,enabled,parent\_id,is\_domain,page,per\_page\}


-   URI parameter description

    <a name="en-us_topic_0026585113_table47336128"></a>
    <table><thead align="left"><tr id="en-us_topic_0026585113_row49554687"><th class="cellrowborder" valign="top" width="18.421842184218423%" id="mcps1.1.5.1.1"><p id="en-us_topic_0026585113_p54506685"><a name="en-us_topic_0026585113_p54506685"></a><a name="en-us_topic_0026585113_p54506685"></a><strong id="b62544519112125"><a name="b62544519112125"></a><a name="b62544519112125"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.79187918791879%" id="mcps1.1.5.1.2"><p id="en-us_topic_0026585113_p52965331"><a name="en-us_topic_0026585113_p52965331"></a><a name="en-us_topic_0026585113_p52965331"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_1"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_1"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.021902190219024%" id="mcps1.1.5.1.3"><p id="en-us_topic_0026585113_p62333418"><a name="en-us_topic_0026585113_p62333418"></a><a name="en-us_topic_0026585113_p62333418"></a><strong id="ac567ba5e1a47441987e0c88f4078942e_1"><a name="ac567ba5e1a47441987e0c88f4078942e_1"></a><a name="ac567ba5e1a47441987e0c88f4078942e_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43.76437643764376%" id="mcps1.1.5.1.4"><p id="en-us_topic_0026585113_p15842089"><a name="en-us_topic_0026585113_p15842089"></a><a name="en-us_topic_0026585113_p15842089"></a><strong id="a474b3e785d7d4684a0c90106e51e3ba6"><a name="a474b3e785d7d4684a0c90106e51e3ba6"></a><a name="a474b3e785d7d4684a0c90106e51e3ba6"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0026585113_row8140857"><td class="cellrowborder" valign="top" width="18.421842184218423%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0026585113_p55429698"><a name="en-us_topic_0026585113_p55429698"></a><a name="en-us_topic_0026585113_p55429698"></a>domain_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.79187918791879%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0026585113_p60620523"><a name="en-us_topic_0026585113_p60620523"></a><a name="en-us_topic_0026585113_p60620523"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.021902190219024%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0026585113_p11315292"><a name="en-us_topic_0026585113_p11315292"></a><a name="en-us_topic_0026585113_p11315292"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.76437643764376%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0026585113_p44123454"><a name="en-us_topic_0026585113_p44123454"></a><a name="en-us_topic_0026585113_p44123454"></a>ID of an enterprise account to which a user belongs.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0026585113_row61566768"><td class="cellrowborder" valign="top" width="18.421842184218423%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0026585113_p20852350"><a name="en-us_topic_0026585113_p20852350"></a><a name="en-us_topic_0026585113_p20852350"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.79187918791879%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0026585113_p11318800"><a name="en-us_topic_0026585113_p11318800"></a><a name="en-us_topic_0026585113_p11318800"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.021902190219024%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0026585113_p44407631"><a name="en-us_topic_0026585113_p44407631"></a><a name="en-us_topic_0026585113_p44407631"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.76437643764376%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0026585113_p40248354"><a name="en-us_topic_0026585113_p40248354"></a><a name="en-us_topic_0026585113_p40248354"></a>Project name.</p>
    </td>
    </tr>
    <tr id="row7299172943813"><td class="cellrowborder" valign="top" width="18.421842184218423%" headers="mcps1.1.5.1.1 "><p id="p14121195319395"><a name="p14121195319395"></a><a name="p14121195319395"></a>parent_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.79187918791879%" headers="mcps1.1.5.1.2 "><p id="p71215530394"><a name="p71215530394"></a><a name="p71215530394"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.021902190219024%" headers="mcps1.1.5.1.3 "><p id="p4121185320399"><a name="p4121185320399"></a><a name="p4121185320399"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.76437643764376%" headers="mcps1.1.5.1.4 "><p id="p171211453143913"><a name="p171211453143913"></a><a name="p171211453143913"></a>Parent project ID of a project.</p>
    </td>
    </tr>
    <tr id="row111461543103820"><td class="cellrowborder" valign="top" width="18.421842184218423%" headers="mcps1.1.5.1.1 "><p id="p913943183913"><a name="p913943183913"></a><a name="p913943183913"></a>enabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.79187918791879%" headers="mcps1.1.5.1.2 "><p id="p813983143913"><a name="p813983143913"></a><a name="p813983143913"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.021902190219024%" headers="mcps1.1.5.1.3 "><p id="p613918315398"><a name="p613918315398"></a><a name="p613918315398"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.76437643764376%" headers="mcps1.1.5.1.4 "><p id="p181391532398"><a name="p181391532398"></a><a name="p181391532398"></a>Whether a project is available.</p>
    </td>
    </tr>
    <tr id="row793683814389"><td class="cellrowborder" valign="top" width="18.421842184218423%" headers="mcps1.1.5.1.1 "><p id="p1213920333917"><a name="p1213920333917"></a><a name="p1213920333917"></a>is_domain</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.79187918791879%" headers="mcps1.1.5.1.2 "><p id="p1013914313919"><a name="p1013914313919"></a><a name="p1013914313919"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.021902190219024%" headers="mcps1.1.5.1.3 "><p id="p181391537399"><a name="p181391537399"></a><a name="p181391537399"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.76437643764376%" headers="mcps1.1.5.1.4 "><p id="p12139183153915"><a name="p12139183153915"></a><a name="p12139183153915"></a>Is domain or not.</p>
    </td>
    </tr>
    <tr id="row3301961143855"><td class="cellrowborder" valign="top" width="18.421842184218423%" headers="mcps1.1.5.1.1 "><p id="p5159279014395"><a name="p5159279014395"></a><a name="p5159279014395"></a>page</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.79187918791879%" headers="mcps1.1.5.1.2 "><p id="p1826646714395"><a name="p1826646714395"></a><a name="p1826646714395"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.021902190219024%" headers="mcps1.1.5.1.3 "><p id="p318887714395"><a name="p318887714395"></a><a name="p318887714395"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.76437643764376%" headers="mcps1.1.5.1.4 "><p id="p5697247514395"><a name="p5697247514395"></a><a name="p5697247514395"></a>The page to be queried. The minimum value is <strong id="b1810282377163149"><a name="b1810282377163149"></a><a name="b1810282377163149"></a>1</strong>.</p>
    </td>
    </tr>
    <tr id="row791068914390"><td class="cellrowborder" valign="top" width="18.421842184218423%" headers="mcps1.1.5.1.1 "><p id="p5965671114395"><a name="p5965671114395"></a><a name="p5965671114395"></a>per_page</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.79187918791879%" headers="mcps1.1.5.1.2 "><p id="p35544014395"><a name="p35544014395"></a><a name="p35544014395"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.021902190219024%" headers="mcps1.1.5.1.3 "><p id="p2879064914395"><a name="p2879064914395"></a><a name="p2879064914395"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.76437643764376%" headers="mcps1.1.5.1.4 "><p id="p62859960163424"><a name="p62859960163424"></a><a name="p62859960163424"></a>Number of data records on each page.</p>
    <p id="p5034119414395"><a name="p5034119414395"></a><a name="p5034119414395"></a>Value range: [1,5000]</p>
    </td>
    </tr>
    </tbody>
    </table>

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >When querying required information by page, ensure that the query parameters  **page**  and  **per\_page**  both exist.  


## **Request**<a name="sf15b8a66213e4cbebbe19daa3db9f159"></a>

-   Request header parameter description

    <a name="en-us_topic_0026585113_table19967814"></a>
    <table><thead align="left"><tr id="en-us_topic_0026585113_row62835574"><th class="cellrowborder" valign="top" width="18.23%" id="mcps1.1.5.1.1"><p id="en-us_topic_0026585113_p56516768"><a name="en-us_topic_0026585113_p56516768"></a><a name="en-us_topic_0026585113_p56516768"></a><strong id="a3d36e4824b214268bc27dd6cf0b3fdee"><a name="a3d36e4824b214268bc27dd6cf0b3fdee"></a><a name="a3d36e4824b214268bc27dd6cf0b3fdee"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.05%" id="mcps1.1.5.1.2"><p id="en-us_topic_0026585113_p14455523"><a name="en-us_topic_0026585113_p14455523"></a><a name="en-us_topic_0026585113_p14455523"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_3"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_3"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_3"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.15%" id="mcps1.1.5.1.3"><p id="en-us_topic_0026585113_p30046694"><a name="en-us_topic_0026585113_p30046694"></a><a name="en-us_topic_0026585113_p30046694"></a><strong id="ac567ba5e1a47441987e0c88f4078942e_3"><a name="ac567ba5e1a47441987e0c88f4078942e_3"></a><a name="ac567ba5e1a47441987e0c88f4078942e_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43.57%" id="mcps1.1.5.1.4"><p id="en-us_topic_0026585113_p17863121"><a name="en-us_topic_0026585113_p17863121"></a><a name="en-us_topic_0026585113_p17863121"></a><strong id="a78685c0019b64bedbbf38bdc95fd875d"><a name="a78685c0019b64bedbbf38bdc95fd875d"></a><a name="a78685c0019b64bedbbf38bdc95fd875d"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="rd830396628d84ea2a78249340dc8e6e5"><td class="cellrowborder" valign="top" width="18.23%" headers="mcps1.1.5.1.1 "><p id="ae69f4e1f183d4e6a82a447c6c51dd3bb"><a name="ae69f4e1f183d4e6a82a447c6c51dd3bb"></a><a name="ae69f4e1f183d4e6a82a447c6c51dd3bb"></a>Content-Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.1.5.1.2 "><p id="a46e7614fe7524390be4c0cfe6e146512"><a name="a46e7614fe7524390be4c0cfe6e146512"></a><a name="a46e7614fe7524390be4c0cfe6e146512"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.15%" headers="mcps1.1.5.1.3 "><p id="a9172a1617e4c423ca144149fbf806f52"><a name="a9172a1617e4c423ca144149fbf806f52"></a><a name="a9172a1617e4c423ca144149fbf806f52"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.57%" headers="mcps1.1.5.1.4 "><p id="a8a69e5f2739b4fcc996e01ae20ecbaf3"><a name="a8a69e5f2739b4fcc996e01ae20ecbaf3"></a><a name="a8a69e5f2739b4fcc996e01ae20ecbaf3"></a>Fill <strong id="b842352706161331"><a name="b842352706161331"></a><a name="b842352706161331"></a>application/json;charset=utf8</strong> in this field.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0026585113_row37626701"><td class="cellrowborder" valign="top" width="18.23%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0026585113_p27863937"><a name="en-us_topic_0026585113_p27863937"></a><a name="en-us_topic_0026585113_p27863937"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0026585113_p42386454"><a name="en-us_topic_0026585113_p42386454"></a><a name="en-us_topic_0026585113_p42386454"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.15%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0026585113_p10750772"><a name="en-us_topic_0026585113_p10750772"></a><a name="en-us_topic_0026585113_p10750772"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.57%" headers="mcps1.1.5.1.4 "><p id="p52774644194451"><a name="p52774644194451"></a><a name="p52774644194451"></a>Authenticated token of the target tenant.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Sample request

    ```
    curl -i -k -H 'Accept:application/json' -H 'Content-Type:application/json;charset=utf8' -X "X-Auth-Token:$token" -X GET https://10.145.93.56:31943/v3/projects?domain_id=5c9f5525d9d24c5bbf91e74d86772029&name=region_name
    ```


## **Response**<a name="s50fc4d2354714f279e24d075fbc04a26"></a>

-   Response body parameter description

    <a name="t1266dd240c3649048c9f42af34a0686b"></a>
    <table><thead align="left"><tr id="rd8ac2cd80e4b47d684b61df4f3c570cf"><th class="cellrowborder" valign="top" width="20.49%" id="mcps1.1.5.1.1"><p id="ad167d1bf89ca443eac693ea562da12a3"><a name="ad167d1bf89ca443eac693ea562da12a3"></a><a name="ad167d1bf89ca443eac693ea562da12a3"></a><strong id="a91cc16ec42d849d3ada0fe573ea173e1"><a name="a91cc16ec42d849d3ada0fe573ea173e1"></a><a name="a91cc16ec42d849d3ada0fe573ea173e1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.48%" id="mcps1.1.5.1.2"><p id="aad08ea1f8c8e4a42a1a81112a74cb237"><a name="aad08ea1f8c8e4a42a1a81112a74cb237"></a><a name="aad08ea1f8c8e4a42a1a81112a74cb237"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_5"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_5"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_5"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.36%" id="mcps1.1.5.1.3"><p id="a9b5fafff0348408893dcc06fbe0b1186"><a name="a9b5fafff0348408893dcc06fbe0b1186"></a><a name="a9b5fafff0348408893dcc06fbe0b1186"></a><strong id="ac567ba5e1a47441987e0c88f4078942e_5"><a name="ac567ba5e1a47441987e0c88f4078942e_5"></a><a name="ac567ba5e1a47441987e0c88f4078942e_5"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43.669999999999995%" id="mcps1.1.5.1.4"><p id="ad002a0bf107a468884a5777e55f837f6"><a name="ad002a0bf107a468884a5777e55f837f6"></a><a name="ad002a0bf107a468884a5777e55f837f6"></a><strong id="ab7086946bd9240b5a77037d99ded7220"><a name="ab7086946bd9240b5a77037d99ded7220"></a><a name="ab7086946bd9240b5a77037d99ded7220"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="ref3b81e8e64e418c961ca1bce6f25280"><td class="cellrowborder" valign="top" width="20.49%" headers="mcps1.1.5.1.1 "><p id="abb2b4d81b907497da50ad4f12760f7dc"><a name="abb2b4d81b907497da50ad4f12760f7dc"></a><a name="abb2b4d81b907497da50ad4f12760f7dc"></a>projects</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.5.1.2 "><p id="a7e49a4eaca054e36ba774b0cdc492081"><a name="a7e49a4eaca054e36ba774b0cdc492081"></a><a name="a7e49a4eaca054e36ba774b0cdc492081"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.1.5.1.3 "><p id="af41e29e0e266400c900609efde3aaf39"><a name="af41e29e0e266400c900609efde3aaf39"></a><a name="af41e29e0e266400c900609efde3aaf39"></a>List</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.669999999999995%" headers="mcps1.1.5.1.4 "><p id="a8ded0409c6d948dc82f7f779a4cfa5b8"><a name="a8ded0409c6d948dc82f7f779a4cfa5b8"></a><a name="a8ded0409c6d948dc82f7f779a4cfa5b8"></a>List of projects.</p>
    </td>
    </tr>
    <tr id="row17979111841518"><td class="cellrowborder" valign="top" width="20.49%" headers="mcps1.1.5.1.1 "><p id="p34207706172552"><a name="p34207706172552"></a><a name="p34207706172552"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.5.1.2 "><p id="p19360826172552"><a name="p19360826172552"></a><a name="p19360826172552"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.1.5.1.3 "><p id="p24723091172552"><a name="p24723091172552"></a><a name="p24723091172552"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.669999999999995%" headers="mcps1.1.5.1.4 "><p id="p56413324172552"><a name="p56413324172552"></a><a name="p56413324172552"></a>Resource links of a project.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Description for the project format

    <a name="t3ef10d134105438f922a72ac36adbe13"></a>
    <table><thead align="left"><tr id="ra836795da3204436ad115c6d63f33cb3"><th class="cellrowborder" valign="top" width="20.61%" id="mcps1.1.5.1.1"><p id="a915f4fa2492a4fa3b5fc5b52cb975ed3"><a name="a915f4fa2492a4fa3b5fc5b52cb975ed3"></a><a name="a915f4fa2492a4fa3b5fc5b52cb975ed3"></a><strong id="a47d7f5d64c8b432b9b0986aae135c770"><a name="a47d7f5d64c8b432b9b0986aae135c770"></a><a name="a47d7f5d64c8b432b9b0986aae135c770"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.23%" id="mcps1.1.5.1.2"><p id="aeb29128c8bc6489593aaf12297635c52"><a name="aeb29128c8bc6489593aaf12297635c52"></a><a name="aeb29128c8bc6489593aaf12297635c52"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_7"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_7"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_7"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.86%" id="mcps1.1.5.1.3"><p id="a367df15999ce47aa8fa2550bb2d3df9a"><a name="a367df15999ce47aa8fa2550bb2d3df9a"></a><a name="a367df15999ce47aa8fa2550bb2d3df9a"></a><strong id="ac567ba5e1a47441987e0c88f4078942e_7"><a name="ac567ba5e1a47441987e0c88f4078942e_7"></a><a name="ac567ba5e1a47441987e0c88f4078942e_7"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43.3%" id="mcps1.1.5.1.4"><p id="a16a6b7e4145e4fbabf25e75163ec3f95"><a name="a16a6b7e4145e4fbabf25e75163ec3f95"></a><a name="a16a6b7e4145e4fbabf25e75163ec3f95"></a><strong id="ae8f3de030d304e9ca0154a467f37982a"><a name="ae8f3de030d304e9ca0154a467f37982a"></a><a name="ae8f3de030d304e9ca0154a467f37982a"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1630172942012"><td class="cellrowborder" valign="top" width="20.61%" headers="mcps1.1.5.1.1 "><p id="p6161946154521"><a name="p6161946154521"></a><a name="p6161946154521"></a>is_domain</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.23%" headers="mcps1.1.5.1.2 "><p id="p21721285154521"><a name="p21721285154521"></a><a name="p21721285154521"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.1.5.1.3 "><p id="p41042049154521"><a name="p41042049154521"></a><a name="p41042049154521"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.3%" headers="mcps1.1.5.1.4 "><p id="p305652154521"><a name="p305652154521"></a><a name="p305652154521"></a>Is domain or not.</p>
    </td>
    </tr>
    <tr id="r6aa1186cf8554a019ac2b2130cf5b8d2"><td class="cellrowborder" valign="top" width="20.61%" headers="mcps1.1.5.1.1 "><p id="a1441367937eb4233b8cda7012259c030"><a name="a1441367937eb4233b8cda7012259c030"></a><a name="a1441367937eb4233b8cda7012259c030"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.23%" headers="mcps1.1.5.1.2 "><p id="a69f17d6e57f544fb90861e9a8297a485"><a name="a69f17d6e57f544fb90861e9a8297a485"></a><a name="a69f17d6e57f544fb90861e9a8297a485"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.1.5.1.3 "><p id="a1a749c575c9b40049712221af5070e71"><a name="a1a749c575c9b40049712221af5070e71"></a><a name="a1a749c575c9b40049712221af5070e71"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.3%" headers="mcps1.1.5.1.4 "><p id="ace0495cc79a34a2690c98b2dc69b4768"><a name="ace0495cc79a34a2690c98b2dc69b4768"></a><a name="ace0495cc79a34a2690c98b2dc69b4768"></a>Project description.</p>
    </td>
    </tr>
    <tr id="row13801134313207"><td class="cellrowborder" valign="top" width="20.61%" headers="mcps1.1.5.1.1 "><p id="p1080120431207"><a name="p1080120431207"></a><a name="p1080120431207"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.23%" headers="mcps1.1.5.1.2 "><p id="p2705079812952"><a name="p2705079812952"></a><a name="p2705079812952"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.1.5.1.3 "><p id="p4363103412952"><a name="p4363103412952"></a><a name="p4363103412952"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.3%" headers="mcps1.1.5.1.4 "><p id="p4445286212952"><a name="p4445286212952"></a><a name="p4445286212952"></a>Resource links of a project.</p>
    </td>
    </tr>
    <tr id="rb2ba995189ec478eb5d1181d3bb7be1c"><td class="cellrowborder" valign="top" width="20.61%" headers="mcps1.1.5.1.1 "><p id="aa1005da54f2c4746ae99676d14ab012d"><a name="aa1005da54f2c4746ae99676d14ab012d"></a><a name="aa1005da54f2c4746ae99676d14ab012d"></a>enabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.23%" headers="mcps1.1.5.1.2 "><p id="a6d0540b177e34775b18c670cf5cd46bc"><a name="a6d0540b177e34775b18c670cf5cd46bc"></a><a name="a6d0540b177e34775b18c670cf5cd46bc"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.1.5.1.3 "><p id="a65f6a6fc5a364d868072c58eeab90325"><a name="a65f6a6fc5a364d868072c58eeab90325"></a><a name="a65f6a6fc5a364d868072c58eeab90325"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.3%" headers="mcps1.1.5.1.4 "><p id="ababe5d21d4764e209d225a4cea9b9fa2"><a name="ababe5d21d4764e209d225a4cea9b9fa2"></a><a name="ababe5d21d4764e209d225a4cea9b9fa2"></a>Whether a project is available.</p>
    </td>
    </tr>
    <tr id="r41522dc2bd8d475b8d2a16af17d5213b"><td class="cellrowborder" valign="top" width="20.61%" headers="mcps1.1.5.1.1 "><p id="a2501c5b12ff94e338c0930e6c321af90"><a name="a2501c5b12ff94e338c0930e6c321af90"></a><a name="a2501c5b12ff94e338c0930e6c321af90"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.23%" headers="mcps1.1.5.1.2 "><p id="af10224f581d946cb91a49683adf34271"><a name="af10224f581d946cb91a49683adf34271"></a><a name="af10224f581d946cb91a49683adf34271"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.1.5.1.3 "><p id="a0316e95fb756489a82f70ae562c523b4"><a name="a0316e95fb756489a82f70ae562c523b4"></a><a name="a0316e95fb756489a82f70ae562c523b4"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.3%" headers="mcps1.1.5.1.4 "><p id="af5ce8c5c520f468895f28d74f6eb4540"><a name="af5ce8c5c520f468895f28d74f6eb4540"></a><a name="af5ce8c5c520f468895f28d74f6eb4540"></a>Project ID.</p>
    </td>
    </tr>
    <tr id="row2537965212"><td class="cellrowborder" valign="top" width="20.61%" headers="mcps1.1.5.1.1 "><p id="p49220723154521"><a name="p49220723154521"></a><a name="p49220723154521"></a>parent_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.23%" headers="mcps1.1.5.1.2 "><p id="p64815690154521"><a name="p64815690154521"></a><a name="p64815690154521"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.1.5.1.3 "><p id="p65672473154521"><a name="p65672473154521"></a><a name="p65672473154521"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.3%" headers="mcps1.1.5.1.4 "><p id="p30787847154521"><a name="p30787847154521"></a><a name="p30787847154521"></a>Parent ID of the project.</p>
    </td>
    </tr>
    <tr id="r1208cbb1496440d89eb758b2cd80d578"><td class="cellrowborder" valign="top" width="20.61%" headers="mcps1.1.5.1.1 "><p id="a4504807eb899465fb0ce3ac82d7013dc"><a name="a4504807eb899465fb0ce3ac82d7013dc"></a><a name="a4504807eb899465fb0ce3ac82d7013dc"></a>domain_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.23%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0026585113_p386591205643"><a name="en-us_topic_0026585113_p386591205643"></a><a name="en-us_topic_0026585113_p386591205643"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.1.5.1.3 "><p id="a293aacc9b5354786a8b30a063a186b02"><a name="a293aacc9b5354786a8b30a063a186b02"></a><a name="a293aacc9b5354786a8b30a063a186b02"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.3%" headers="mcps1.1.5.1.4 "><p id="aa1138dcdd40340039e621e7abf0332e1"><a name="aa1138dcdd40340039e621e7abf0332e1"></a><a name="aa1138dcdd40340039e621e7abf0332e1"></a>ID of an enterprise account to which a project belongs.</p>
    </td>
    </tr>
    <tr id="rbe8775b4e77a4b08be093de05e7bcbf3"><td class="cellrowborder" valign="top" width="20.61%" headers="mcps1.1.5.1.1 "><p id="acc4c499e1b2f4bdd98e5c7acd4e8861b"><a name="acc4c499e1b2f4bdd98e5c7acd4e8861b"></a><a name="acc4c499e1b2f4bdd98e5c7acd4e8861b"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.23%" headers="mcps1.1.5.1.2 "><p id="a4bf5dfe715d342e0a883343cbcf8181a"><a name="a4bf5dfe715d342e0a883343cbcf8181a"></a><a name="a4bf5dfe715d342e0a883343cbcf8181a"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.1.5.1.3 "><p id="a8c424bac7d93444dbc647a1d5c5c21e4"><a name="a8c424bac7d93444dbc647a1d5c5c21e4"></a><a name="a8c424bac7d93444dbc647a1d5c5c21e4"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.3%" headers="mcps1.1.5.1.4 "><p id="afc48731c8a2e4c66a56ac245f7a1e34e"><a name="afc48731c8a2e4c66a56ac245f7a1e34e"></a><a name="afc48731c8a2e4c66a56ac245f7a1e34e"></a>Project name.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Sample response

    ```
    {
      "links": {
        "self": "www.example.com/v3/projects?domain_id=c9f5525d9d24c5bbf91e74d86772029&name=region_name",
        "previous": null,
        "next": null
      },
      "projects": [
        {
          "is_domain": false,
          "description": "",
          "links": {
            "self": "www.example.com/v3/projects/e86737682ab64b2490c48f08bcc41914"
          },
          "enabled": true,
          "id": "e86737682ab64b2490c48f08bcc41914",
          "parent_id": "c9f5525d9d24c5bbf91e74d86772029",
          "domain_id": "c9f5525d9d24c5bbf91e74d86772029",
          "name": "region_name"
        }
      ]
    }
    ```


## **Status Codes**<a name="s791625f7e91045a99dacb83eeaeab0ca"></a>

<a name="en-us_topic_0026585113_table8268111"></a>
<table><thead align="left"><tr id="en-us_topic_0026585113_row6757235"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0026585113_p10465156"><a name="en-us_topic_0026585113_p10465156"></a><a name="en-us_topic_0026585113_p10465156"></a><strong id="abf4071d983774024a2b3c35bebf32cfb"><a name="abf4071d983774024a2b3c35bebf32cfb"></a><a name="abf4071d983774024a2b3c35bebf32cfb"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0026585113_p42371273"><a name="en-us_topic_0026585113_p42371273"></a><a name="en-us_topic_0026585113_p42371273"></a><strong id="a131041de71c64cb4b154f48c1db4e31d"><a name="a131041de71c64cb4b154f48c1db4e31d"></a><a name="a131041de71c64cb4b154f48c1db4e31d"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="reb721646e2bd423dba003e9081c1d4da"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a2e8a8ee7a72c45d38d3b5b39c17806b6"><a name="a2e8a8ee7a72c45d38d3b5b39c17806b6"></a><a name="a2e8a8ee7a72c45d38d3b5b39c17806b6"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a5554a6af41f04ac0bfe75e541afdb6f7"><a name="a5554a6af41f04ac0bfe75e541afdb6f7"></a><a name="a5554a6af41f04ac0bfe75e541afdb6f7"></a>The request is successful.</p>
</td>
</tr>
<tr id="r94c2894d0685406eb347de138998e50d"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a7039248d16864cfdb145042196dd0a4d"><a name="a7039248d16864cfdb145042196dd0a4d"></a><a name="a7039248d16864cfdb145042196dd0a4d"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a228f52291c964a8cb61e9f4cfa8835b2"><a name="a228f52291c964a8cb61e9f4cfa8835b2"></a><a name="a228f52291c964a8cb61e9f4cfa8835b2"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="r82fdd253c453410ea60c395495e4fa6d"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a087911f0192d4b1683fb93e6ed500ef6"><a name="a087911f0192d4b1683fb93e6ed500ef6"></a><a name="a087911f0192d4b1683fb93e6ed500ef6"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a5d0da0ddd2de45ca9631c290a74f45cd"><a name="a5d0da0ddd2de45ca9631c290a74f45cd"></a><a name="a5d0da0ddd2de45ca9631c290a74f45cd"></a>You must enter a username and password to access the requested page.</p>
</td>
</tr>
<tr id="re70fedbf4a8648a181e8a88d0b6f7b34"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="ad629b774064a4284ad2377c059ed5631"><a name="ad629b774064a4284ad2377c059ed5631"></a><a name="ad629b774064a4284ad2377c059ed5631"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="aa87e9b92d9d743ad80f53fb31fca0748"><a name="aa87e9b92d9d743ad80f53fb31fca0748"></a><a name="aa87e9b92d9d743ad80f53fb31fca0748"></a>You are forbidden to access the requested page.</p>
</td>
</tr>
<tr id="r68339f474aee485fb565034249fd9965"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="acf8367d1dbd7416c97e8111d6d73da12"><a name="acf8367d1dbd7416c97e8111d6d73da12"></a><a name="acf8367d1dbd7416c97e8111d6d73da12"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a02f598d0b2ac43cf823fd56654688995"><a name="a02f598d0b2ac43cf823fd56654688995"></a><a name="a02f598d0b2ac43cf823fd56654688995"></a>The server could not find the requested page.</p>
</td>
</tr>
<tr id="rb43cf0f7e13e4339bdc3c2b940fa979e"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a887894ab473844529e048190c04a42c1"><a name="a887894ab473844529e048190c04a42c1"></a><a name="a887894ab473844529e048190c04a42c1"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a6524f6b7ad6b432a9b23621e0e3b0149"><a name="a6524f6b7ad6b432a9b23621e0e3b0149"></a><a name="a6524f6b7ad6b432a9b23621e0e3b0149"></a>Failed to complete the request because of an internal service error.</p>
</td>
</tr>
<tr id="r322cf83b8af244cd8799c052cd4eee43"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a46a4bb51a0d7448097fc34697403f919"><a name="a46a4bb51a0d7448097fc34697403f919"></a><a name="a46a4bb51a0d7448097fc34697403f919"></a>503</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a9e597e4f5b40449aa94be1f6935a031d"><a name="a9e597e4f5b40449aa94be1f6935a031d"></a><a name="a9e597e4f5b40449aa94be1f6935a031d"></a>Failed to complete the request because the service is unavailable.</p>
</td>
</tr>
</tbody>
</table>

