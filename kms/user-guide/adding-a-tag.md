# Adding a Tag<a name="kms_01_0024"></a>

## Scenario<a name="s4e4979ae5e714e439604cdc40578fe1b"></a>

Tags are used to identify CMKs. You can add tags to CMKs so that you can classify CMKs, trace them, and collect their usage status according to the tags.

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>KMS does not support adding tags to Default Master Keys.  

## Prerequisites<a name="s3585ec157e684e689b9e070e93702dad"></a>

You have obtained an account and its password for logging in to the management console.

## Procedure<a name="s6d6371deb6044a3f9c806fb74fb09a6a"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner of the management console and select a region or project.
3.  Choose  **Security**  \>  **Key Management Service**. The  **Key Management Service**  page is displayed.
4.  Click the alias of the desired CMK to view its details.
5.  Click  **Tags**  to go to the tag management page, as shown in  [Figure 1](#fig1450357173911).

    **Figure  1**  Managing tags<a name="fig1450357173911"></a>  
    ![](figures/managing-tags.png "managing-tags")

6.  Click  **Add Tag**. A dialog box is displayed, as shown in  [Figure 2](#f47525a668085476c84565afde13ffc58).

    **Figure  2**  Adding a tag<a name="f47525a668085476c84565afde13ffc58"></a>  
    ![](figures/adding-a-tag.png "adding-a-tag")

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If you want to delete a tag to be added when adding multiple tags, you can click  **Delete**  in the row where the tag to be added is located to delete the tag.  

7.  In the  **Add Tag**  dialog box, enter the tag key and tag value.  [Table 1](#teaf23b4b14f841aaaa772e07bee5a20a)  describes the parameters.

    **Table  1**  Tag parameters

    <a name="teaf23b4b14f841aaaa772e07bee5a20a"></a>
    <table><thead align="left"><tr id="rc58535a3fce549da9f246d184d70dfc2"><th class="cellrowborder" valign="top" width="11%" id="mcps1.2.5.1.1"><p id="en-us_topic_0100501397_p550325414277"><a name="en-us_topic_0100501397_p550325414277"></a><a name="en-us_topic_0100501397_p550325414277"></a><strong>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="38%" id="mcps1.2.5.1.2"><p id="a26102430a53a4a0bacd5d7069dec49e2"><a name="a26102430a53a4a0bacd5d7069dec49e2"></a><a name="a26102430a53a4a0bacd5d7069dec49e2"></a><strong id="b842352706193336"><a name="b842352706193336"></a><a name="b842352706193336"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33%" id="mcps1.2.5.1.3"><p id="en-us_topic_0100501397_p250305412717"><a name="en-us_topic_0100501397_p250305412717"></a><a name="en-us_topic_0100501397_p250305412717"></a><strong id="b84235270613118"><a name="b84235270613118"></a><a name="b84235270613118"></a>Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18%" id="mcps1.2.5.1.4"><p id="p19213146174417"><a name="p19213146174417"></a><a name="p19213146174417"></a><strong id="b84235270610336"><a name="b84235270610336"></a><a name="b84235270610336"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="rf52642a625d547d6a35b2cfc34d2f823"><td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.1 "><p id="a9b7c7a18d91f4681849538c75fd5e212"><a name="a9b7c7a18d91f4681849538c75fd5e212"></a><a name="a9b7c7a18d91f4681849538c75fd5e212"></a>Tag key</p>
    </td>
    <td class="cellrowborder" valign="top" width="38%" headers="mcps1.2.5.1.2 "><p id="p91159390107"><a name="p91159390107"></a><a name="p91159390107"></a>Name of a tag.</p>
    <p id="p1551003816441"><a name="p1551003816441"></a><a name="p1551003816441"></a>The same tag (including tag key and tag value) can be used for different CMKs. However, under the same CMK, one tag key can have only one tag value.</p>
    <p id="p16287540104220"><a name="p16287540104220"></a><a name="p16287540104220"></a>A maximum of 10 tags can be added for one CMK.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.5.1.3 "><a name="ul9766456111319"></a><a name="ul9766456111319"></a><ul id="ul9766456111319"><li>Mandatory.</li><li>Each tag key must be unique under the same CMK.</li><li>Contains a maximum of 36 characters.</li><li>Only digits, letters, underscores (_), and hyphens (-) are allowed.</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.4 "><p id="p0213186204416"><a name="p0213186204416"></a><a name="p0213186204416"></a>cost</p>
    </td>
    </tr>
    <tr id="re26efe410cb54792a9f962ce86c224c7"><td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.1 "><p id="a98b138a8e31d44b19b614550ddadf28b"><a name="a98b138a8e31d44b19b614550ddadf28b"></a><a name="a98b138a8e31d44b19b614550ddadf28b"></a>Tag value</p>
    </td>
    <td class="cellrowborder" valign="top" width="38%" headers="mcps1.2.5.1.2 "><p id="p1627581310114"><a name="p1627581310114"></a><a name="p1627581310114"></a>Value of the tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.5.1.3 "><a name="ul121271524141420"></a><a name="ul121271524141420"></a><ul id="ul121271524141420"><li>This parameter can be empty.</li><li>Can contain a maximum of 43 characters.</li><li>Only digits, letters, underscores (_), and hyphens (-) are allowed.</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.4 "><p id="p1021366194412"><a name="p1021366194412"></a><a name="p1021366194412"></a>100</p>
    </td>
    </tr>
    </tbody>
    </table>

8.  Click  **OK**  to complete.

