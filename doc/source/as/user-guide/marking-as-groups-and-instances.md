# Marking AS Groups and Instances<a name="EN-US_TOPIC_0067025419"></a>

If you have many resources of the same type, you can use a tag to manage resources flexibly. You can identify specified resources quickly using the tags allocated to them.

Using a tag, you can assign custom data to each AS group. You can organize and manage AS groups, for example, classify AS group resources by usage, owner, or environment.

Each tag contains a key and a value. You can specify the key and value for each tag. A key can be a category associated with certain values, such as usage, owner, and environment.

For example, if you want to distinguish the test environment and production environment, you can allocate a tag with the key  **environment**  to each AS group. For the test environment, the key value is  **test**  and for the production environment, the key value is  **production**. You are advised to use one or more groups of consistent tags to manage your AS group resources.

After you allocate a tag to an AS group, the system will automatically add the tag to the instances automatically created in the AS group. If you add a tag to an AS group or modify the tag, the new tag will be added to the ECSs automatically created in the AS group. Creating, deleting, or modifying the tag of an AS group will have no impact on the ECSs in the AS group.

## Restrictions of Using Tags<a name="section7355112104225"></a>

You must observe the following rules when using tags:

-   Each AS group can have a maximum of 10 tags added to it.
-   Each tag contains a key and a value.
-   You can set the tag value to an empty character string.
-   If you delete an AS group, all tags of it will also be deleted.

## Adding a Tag to an AS Group<a name="section12477432195230"></a>

1.  Log in to the management console.
2.  Click  ![](figures/d00356819-云计算开发部-公有云_iaas-image-f1cac6ef-c4f7-462b-a7f1-85e988937e64-3.png)  in the upper left corner to select a region and a project.
3.  Under  **Computing**, click  **Auto Scaling**. In the navigation pane on the left, choose  **Instance Scaling**.
4.  Click the AS group name. On the  **Basic Information**  page, click the  **Tags**  tab and then click  **Add Tag**.
5.  Set the parameters listed in  [Table 1](#table1794599823119).

    **Table  1**  Tag naming rules

    <a name="table1794599823119"></a>
    <table><thead align="left"><tr id="row2997812223119"><th class="cellrowborder" valign="top" width="18.54%" id="mcps1.2.4.1.1"><p id="p4367076523119"><a name="p4367076523119"></a><a name="p4367076523119"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.39%" id="mcps1.2.4.1.2"><p id="p4767111023119"><a name="p4767111023119"></a><a name="p4767111023119"></a>Requirement</p>
    </th>
    <th class="cellrowborder" valign="top" width="28.07%" id="mcps1.2.4.1.3"><p id="p3615470723119"><a name="p3615470723119"></a><a name="p3615470723119"></a>Example Value</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5695691323119"><td class="cellrowborder" valign="top" width="18.54%" headers="mcps1.2.4.1.1 "><p id="p5010724023119"><a name="p5010724023119"></a><a name="p5010724023119"></a>Tag Key</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.39%" headers="mcps1.2.4.1.2 "><a name="ul2321196023222"></a><a name="ul2321196023222"></a><ul id="ul2321196023222"><li>The value cannot be empty.</li><li>An AS group has a unique key.</li><li>A key can contain a maximum of 36 characters, including only digits, letters, hyphens (-), and underscores (_).</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="28.07%" headers="mcps1.2.4.1.3 "><p id="p5438834323119"><a name="p5438834323119"></a><a name="p5438834323119"></a>Organization</p>
    </td>
    </tr>
    <tr id="row1973304523119"><td class="cellrowborder" valign="top" width="18.54%" headers="mcps1.2.4.1.1 "><p id="p5487280123119"><a name="p5487280123119"></a><a name="p5487280123119"></a>Tag Value</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.39%" headers="mcps1.2.4.1.2 "><a name="ul6706750105539"></a><a name="ul6706750105539"></a><ul id="ul6706750105539"><li>The value can be an empty character string.</li><li>A key can have only one value.</li><li>A tag value can contain a maximum of 43 characters, including only digits, letters, hyphens (-), and underscores (_).</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="28.07%" headers="mcps1.2.4.1.3 "><p id="p4850087723119"><a name="p4850087723119"></a><a name="p4850087723119"></a>Apache</p>
    </td>
    </tr>
    </tbody>
    </table>

6.  Click  **OK**.

## Modifying or Deleting Tags of an AS Group<a name="section8057725103917"></a>

1.  Log in to the management console.
2.  Click  ![](figures/d00356819-云计算开发部-公有云_iaas-image-f1cac6ef-c4f7-462b-a7f1-85e988937e64-4.png)  in the upper left corner to select a region and a project.
3.  Under  **Computing**, click  **Auto Scaling**. In the navigation pane on the left, choose  **Instance Scaling**. Then click the  **AS Groups**  tab.
4.  Click the AS group name. On the  **Basic Information**  page, click the  **Tags**  tab.
5.  Locate the row that contains the tag and click  **Edit**  or  **Delete**  in the  **Operation**  column.

    After clicking  **Edit**, configure required parameters. For details, see  [Table 1](#table1794599823119).

    After you click  **Delete**, the added tag will be deleted.


