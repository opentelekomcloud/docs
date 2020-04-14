# Creating an IAM Agency<a name="dis_01_0605"></a>

## Introduction<a name="section15746595104641"></a>

If you choose to dump data from DIS to OBS, create an IAM agency that grants DIS permissions to access OBS.

## Creating an IAM Agency<a name="section25838076111910"></a>

1.  Log in to the management console.
2.  Click  **Service List**. Under  **Management & Deployment**, select  **Identify and Access Management**.
3.  Select  **Agencies**  in the navigation tree pane, and click  **Create Agency**.

    **Figure  1**  Creating an IAM agency<a name="fig165014586333"></a>  
    ![](figures/creating-an-iam-agency.jpg "creating-an-iam-agency")

4.  Configure agency parameters and click  **OK**. 

    **Figure  2**  Configuring agency parameters<a name="fig1498012571344"></a>  
    ![](figures/configuring-agency-parameters.jpg "configuring-agency-parameters")

    **Table  1**  Agency parameter description

    <a name="table66133055111910"></a>
    <table><thead align="left"><tr id="row32490906111910"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.3.1.1"><p id="p14517702111910"><a name="p14517702111910"></a><a name="p14517702111910"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="70%" id="mcps1.2.3.1.2"><p id="p35083239111910"><a name="p35083239111910"></a><a name="p35083239111910"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row23170149111910"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p64842791111910"><a name="p64842791111910"></a><a name="p64842791111910"></a>Agency Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p17774742111910"><a name="p17774742111910"></a><a name="p17774742111910"></a>Name of the agency to be created. The value of this parameter is 1 to 64 characters long and cannot be left unspecified.</p>
    </td>
    </tr>
    <tr id="row25754953111910"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p5776486111910"><a name="p5776486111910"></a><a name="p5776486111910"></a>Agency Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p65242211111910"><a name="p65242211111910"></a><a name="p65242211111910"></a>Type of the agency to be created. This parameter must be set to <strong id="b147241335189"><a name="b147241335189"></a><a name="b147241335189"></a>Cloud service</strong>.</p>
    </td>
    </tr>
    <tr id="row50308989111910"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p48496302111910"><a name="p48496302111910"></a><a name="p48496302111910"></a>Cloud Service</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p35886355111910"><a name="p35886355111910"></a><a name="p35886355111910"></a>Click <strong id="b10448144191416"><a name="b10448144191416"></a><a name="b10448144191416"></a>Select</strong> next to <strong id="b194031287144"><a name="b194031287144"></a><a name="b194031287144"></a>Cloud Service</strong>. In the <strong id="b1195624117142"><a name="b1195624117142"></a><a name="b1195624117142"></a>Select Cloud Service</strong> dialog box, select <strong id="b17685194915144"><a name="b17685194915144"></a><a name="b17685194915144"></a>DIS</strong> and click <strong id="b13767105151419"><a name="b13767105151419"></a><a name="b13767105151419"></a>OK</strong>.</p>
    </td>
    </tr>
    <tr id="row54541740111910"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p55804859111910"><a name="p55804859111910"></a><a name="p55804859111910"></a>Validity Period</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p23899763111910"><a name="p23899763111910"></a><a name="p23899763111910"></a>Select <strong id="b113861320101513"><a name="b113861320101513"></a><a name="b113861320101513"></a>Permanent</strong>.</p>
    <div class="note" id="note47354677104651"><a name="note47354677104651"></a><a name="note47354677104651"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p23538910104651"><a name="p23538910104651"></a><a name="p23538910104651"></a>Currently, this parameter must be set to <strong id="b133691353153"><a name="b133691353153"></a><a name="b133691353153"></a>Permanent</strong>. Using another value may result in authorization failures.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row13771277111910"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p41731668111910"><a name="p41731668111910"></a><a name="p41731668111910"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p24821976111910"><a name="p24821976111910"></a><a name="p24821976111910"></a>Agency description. The entered description cannot exceed 255 characters.</p>
    </td>
    </tr>
    <tr id="row22071196111910"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p238213123015"><a name="p238213123015"></a><a name="p238213123015"></a>Permissions</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p9543077171349"><a name="p9543077171349"></a><a name="p9543077171349"></a>If <strong id="b1547196153414"><a name="b1547196153414"></a><a name="b1547196153414"></a>Dump Destination</strong> is <strong id="b119971512143416"><a name="b119971512143416"></a><a name="b119971512143416"></a>OBS</strong>, policy settings are as follows: <span id="text13276113293412"><a name="text13276113293412"></a><a name="text13276113293412"></a>Region: Global service
    Project: OBS
    Policy: Tenant Administrator</span></p>
    <p id="p46724365101249"><a name="p46724365101249"></a><a name="p46724365101249"></a>To modify agency policies, click <strong id="b5521810203614"><a name="b5521810203614"></a><a name="b5521810203614"></a>Modify</strong> in the <strong id="b37780128367"><a name="b37780128367"></a><a name="b37780128367"></a>Operation</strong> column. In the <strong id="b1322185853711"><a name="b1322185853711"></a><a name="b1322185853711"></a>Available Policies</strong> area, select your required policy and click <strong id="b4977111643810"><a name="b4977111643810"></a><a name="b4977111643810"></a>OK</strong>.</p>
    <div class="note" id="note58012428112512"><a name="note58012428112512"></a><a name="note58012428112512"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p65485460112517"><a name="p65485460112517"></a><a name="p65485460112517"></a>After an agency is created, its policies cannot be modified.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>


