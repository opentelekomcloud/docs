# Overview<a name="EN-US_TOPIC_0092499768"></a>

## Scenarios<a name="section1577285115210"></a>

A tag identifies an ECS. Adding tags to an ECS facilitates ECS identification and management.

You can add a tag to an ECS during the ECS creation or after the ECS creation \(**Tags**  tab on the page providing details about the ECS\). Up to 10 tags can be added to an ECS.

>![](/images/icon-note.gif) **NOTE:**   
>Tags added during ECS creation will also be added to the created EIP and EVS disks \(including the system disk and data disks\) of the ECS. If the ECS uses an existing EIP, the tags will not be added to the EIP.  
>After creating the ECS, you can view the tags on the pages providing details about the ECS, EIP, and EVS disks.  

## Basics of Tags<a name="section1855512613159"></a>

Tags are used to identify cloud resources. When you have many cloud resources of the same type, you can use tags to classify cloud resources by dimension \(for example, use, owner, or environment\).

**Figure  1**  Example tags<a name="en-us_topic_0157874334_fig81911042564"></a>  
![](figures/example-tags.png "example-tags")

[Figure 1](#en-us_topic_0157874334_fig81911042564)  shows how tags work. In this example, you assign two tags to each cloud resource. Each tag contains a key and a value that you define. The key of one tag is  **Owner**, and the key of another tag is  **Use**. Each tag has a value.

You can quickly search for and filter specific cloud resources based on the tags added to them. For example, you can define a set of tags for cloud resources in an account to track the owner and usage of each cloud resource, making resource management easier.

## Tag Naming Rules<a name="section992912468317"></a>

-   Each tag consists of a key-value pair.
-   Each ECS supports adding up to 10 tags.
-   For each resource, a tag key must be unique and can have only one tag value.
-   A tag consists of a tag key and a tag value.  [Table 1](#table197401426182516)  lists the tag key and value requirements.

    **Table  1**  Tag key and value requirements

    <a name="table197401426182516"></a>
    <table><thead align="left"><tr id="row374112610252"><th class="cellrowborder" valign="top" width="18.54%" id="mcps1.2.4.1.1"><p id="p674122692511"><a name="p674122692511"></a><a name="p674122692511"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.769999999999996%" id="mcps1.2.4.1.2"><p id="p47412026172519"><a name="p47412026172519"></a><a name="p47412026172519"></a>Requirement</p>
    </th>
    <th class="cellrowborder" valign="top" width="24.69%" id="mcps1.2.4.1.3"><p id="p074152682511"><a name="p074152682511"></a><a name="p074152682511"></a>Example Value</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row77477265250"><td class="cellrowborder" valign="top" width="18.54%" headers="mcps1.2.4.1.1 "><p id="p37471326142512"><a name="p37471326142512"></a><a name="p37471326142512"></a>Key</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.769999999999996%" headers="mcps1.2.4.1.2 "><a name="ul207505264257"></a><a name="ul207505264257"></a><ul id="ul207505264257"><li>Cannot be left blank.</li><li>The key value must be unique for an ECS.</li><li>Can contain a maximum of 36 characters.</li><li>Can only consist of digits, letters, hyphens (-), and underscores (_).</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="24.69%" headers="mcps1.2.4.1.3 "><p id="p157536266259"><a name="p157536266259"></a><a name="p157536266259"></a>Organization</p>
    </td>
    </tr>
    <tr id="row4754926182519"><td class="cellrowborder" valign="top" width="18.54%" headers="mcps1.2.4.1.1 "><p id="p37542260253"><a name="p37542260253"></a><a name="p37542260253"></a>Value</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.769999999999996%" headers="mcps1.2.4.1.2 "><a name="ul107561326102518"></a><a name="ul107561326102518"></a><ul id="ul107561326102518"><li>Can contain a maximum of 43 characters.</li><li>Can only consist of digits, letters, hyphens (-), and underscores (_).</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="24.69%" headers="mcps1.2.4.1.3 "><p id="p47581826192520"><a name="p47581826192520"></a><a name="p47581826192520"></a>Apache</p>
    </td>
    </tr>
    </tbody>
    </table>


