# Creating an Image Repository<a name="cce_01_0208"></a>

An image repository is used to store, deploy, and manage Docker images.

## Prerequisites<a name="section148833143811"></a>

An organization has been created. For more information, see  [Creating an Organization](creating-an-organization.md).

## Procedure<a name="section10802936913"></a>

1.  Log in to the CCE console. In the navigation pane, choose  ****Image Repository****. Click  ****Create Repository****.
2.  Configure the parameters for creating an image repository, as listed in  [Table 1](#tba5add70c0e34273a45ccec18464dd51). The parameters marked with an asterisk \(\*\) are mandatory.

    **Table  1**  Parameters for creating an image repository

    <a name="tba5add70c0e34273a45ccec18464dd51"></a>
    <table><thead align="left"><tr id="en-us_topic_0075419264_row1884320375"><th class="cellrowborder" valign="top" width="33%" id="mcps1.2.3.1.1"><p id="en-us_topic_0075419264_p168410201713"><a name="en-us_topic_0075419264_p168410201713"></a><a name="en-us_topic_0075419264_p168410201713"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="67%" id="mcps1.2.3.1.2"><p id="en-us_topic_0075419264_p88417201574"><a name="en-us_topic_0075419264_p88417201574"></a><a name="en-us_topic_0075419264_p88417201574"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r65d23dd69a084209be460dc0a87416cc"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0075419264_p1784420273"><a name="en-us_topic_0075419264_p1784420273"></a><a name="en-us_topic_0075419264_p1784420273"></a>* Repository Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.3.1.2 "><a name="ol834202232811"></a><a name="ol834202232811"></a><ol id="ol834202232811"><li>Select an existing organization for the image repository you want to create.</li><li>Enter an image repository name.<p id="p191388449458"><a name="p191388449458"></a><a name="p191388449458"></a>In an image repository, an image is presented in the same way as an official image in the Docker Hub. Therefore, <strong id="b17135141310290"><a name="b17135141310290"></a><a name="b17135141310290"></a>Repository Name</strong> specified here is also the image name. One image repository corresponds to one image. An image repository may include different versions of an image.</p>
    </li></ol>
    </td>
    </tr>
    <tr id="r98d46458c1a648f6b44ba9f673669a71"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0075419264_p98417201871"><a name="en-us_topic_0075419264_p98417201871"></a><a name="en-us_topic_0075419264_p98417201871"></a>* Sharing Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0075419264_p08432012718"><a name="en-us_topic_0075419264_p08432012718"></a><a name="en-us_topic_0075419264_p08432012718"></a>Container image repository type. The default type is <strong id="b14453253225"><a name="b14453253225"></a><a name="b14453253225"></a>Public</strong>.</p>
    <a name="en-us_topic_0075419264_ul68422012719"></a><a name="en-us_topic_0075419264_ul68422012719"></a><ul id="en-us_topic_0075419264_ul68422012719"><li>Public: available to all accounts and users.</li><li>Private: available only to the current account and associated users.</li></ul>
    </td>
    </tr>
    <tr id="r24703398020a4c678388df987240d83c"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0075419264_p178516201178"><a name="en-us_topic_0075419264_p178516201178"></a><a name="en-us_topic_0075419264_p178516201178"></a>* Category</p>
    </td>
    <td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0075419264_p28542016712"><a name="en-us_topic_0075419264_p28542016712"></a><a name="en-us_topic_0075419264_p28542016712"></a>Select a repository category.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0075419264_row1985220173"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0075419264_p38518201671"><a name="en-us_topic_0075419264_p38518201671"></a><a name="en-us_topic_0075419264_p38518201671"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0075419264_p985112016715"><a name="en-us_topic_0075419264_p985112016715"></a><a name="en-us_topic_0075419264_p985112016715"></a>Brief description of the image repository.</p>
    </td>
    </tr>
    </tbody>
    </table>

3.  Click  **Create**.

