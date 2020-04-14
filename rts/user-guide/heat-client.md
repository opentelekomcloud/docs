# Heat Client<a name="EN-US_TOPIC_0076468633"></a>

## Overview<a name="section115632153502"></a>

The Heat client is a subproject of OpenStack Client, functioning as a command line client targeted for Heat. You can use this client to access cloud services by running commands.

RTS supports Heat 1.5.1.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>To use the Heat client, you need to install and configure OpenStack Client first. For details, see  [Installing OpenStack Client](#section9738343155012)  and  [Configuration](#section33343719617).  

## Installing OpenStack Client<a name="section9738343155012"></a>

To install OpenStack Client, you need to install and run the python-openstackclient plug-in and ensure that the plug-in is running properly.

OpenStack Client can be used on all OSs as long as python-openstackclient is running properly. Operation methods vary depending on the OS you use. The 64-bit Ubuntu 16.04 OS is recommended. This section describes how to install and configure OpenStack Client by using the 64-bit Ubuntu 16.04 OS as an example.

To install OpenStack Client, perform the following operations as user  **root**: 

1.  Run the following commands to update the OS:

    **apt-get update**

    **apt-get upgrade**

2.  Install Python.

    Install Python and pip based on the type of the OS. Python 2.7 is supported.

    Ubuntu 16.04 includes Python 2.7. If Python is not installed, perform the following steps to install it:

    Run the following command to install Python:

    **apt-get install python**

    Run the following command to install Setuptools:

    **apt-get install python-setuptools**

    Run the following command to install pip:

    **apt-get install python-pip**

    If Ubuntu supports Setuptools and pip of earlier versions, you can install them offline.

    Run the following command to install Dev:

    **apt-get install python-dev**

3.  Install python-openstackclient and its dependent components.

    The following python-openstackclient versions are supported by default:

    -   python-openstackclient: 3.2.1
    -   python-novaclient: 6.0.2
    -   python-glanceclient: 2.5.0
    -   python-keystoneclient: 3.5.1
    -   python-neutronclient: 6.0.1
    -   python-cinderclient: 1.9.0
    -   python-heatclient: 1.5.1
    -   python-designateclient: 2.3.0
    -   openstacksdk: 0.9.5
    -   cliff: 2.2.0
    -   os-client-config: 1.21.1
    -   osc-lib: 1.1.0

    Run the following command to install python-openstackclient using pip:

    **pip install python-openstackclient==3.2.1**

    After the installation is complete, run the following command to verify the installation:

    **openstack -h**

    Check whether help information is displayed. The installation is successful if help information is displayed.

    Other components can be installed in sequence using the same command.


## Configuration<a name="section33343719617"></a>

You can configure OpenStack Client either as user  **root**  or as a common user.

1.  Switch to the directory where OpenStack Client is installed and create an environment variable file, for example,  **novarc**.
2.  Use a text editor to edit the environment variable file and enter the username, password, region, IAM IP address, and port number.

    The following is an example:

    ```
    export OS_USERNAME="user_name" 
    export OS_USER_DOMAIN_NAME=user_domain_name 
    export OS_PASSWORD=******* 
    export TENANT_ID=********
    
    # Only change these for a different region
    export OS_TENANT_NAME=az1 
    export OS_PROJECT_NAME=az1 
    export OS_AUTH_URL=https://iam.az1.domainname.com:443/v3
    
    # No changes needed beyond this point
    export NOVA_ENDPOINT_TYPE=publicURL 
    export OS_ENDPOINT_TYPE=publicURL 
    export CINDER_ENDPOINT_TYPE=publicURL 
    export OS_VOLUME_API_VERSION=2 
    export OS_IDENTITY_API_VERSION=3 
    export OS_IMAGE_API_VERSION=2
    ```

    Environment variables to be configured include the username, password, IAM URL, and port number.  [Table 1](#table1638643151819)  describes the required environment variables.

    **Table  1**  Environment variables

    <a name="table1638643151819"></a>
    <table><thead align="left"><tr id="row1141174317185"><th class="cellrowborder" valign="top" width="38%" id="mcps1.2.3.1.1"><p id="p64118439186"><a name="p64118439186"></a><a name="p64118439186"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="62%" id="mcps1.2.3.1.2"><p id="p34119438187"><a name="p34119438187"></a><a name="p34119438187"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row154116432188"><td class="cellrowborder" valign="top" width="38%" headers="mcps1.2.3.1.1 "><p id="p1137106131916"><a name="p1137106131916"></a><a name="p1137106131916"></a>OS_USERNAME</p>
    </td>
    <td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.3.1.2 "><p id="p2137146101913"><a name="p2137146101913"></a><a name="p2137146101913"></a>Specifies the username for logging in to the management console.</p>
    </td>
    </tr>
    <tr id="row15418438183"><td class="cellrowborder" valign="top" width="38%" headers="mcps1.2.3.1.1 "><p id="p63561321151917"><a name="p63561321151917"></a><a name="p63561321151917"></a>OS_USER_DOMAIN_NAME</p>
    </td>
    <td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.3.1.2 "><p id="p6356162110192"><a name="p6356162110192"></a><a name="p6356162110192"></a>Specifies the enterprise account for logging in to the management console.</p>
    </td>
    </tr>
    <tr id="row1141174331813"><td class="cellrowborder" valign="top" width="38%" headers="mcps1.2.3.1.1 "><p id="p140712389224"><a name="p140712389224"></a><a name="p140712389224"></a>OS_PASSWORD</p>
    </td>
    <td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.3.1.2 "><p id="p1640793816221"><a name="p1640793816221"></a><a name="p1640793816221"></a>Specifies the password for logging in to the management console.</p>
    </td>
    </tr>
    <tr id="row1741943161810"><td class="cellrowborder" valign="top" width="38%" headers="mcps1.2.3.1.1 "><p id="p9411143181816"><a name="p9411143181816"></a><a name="p9411143181816"></a>TENANT_ID</p>
    </td>
    <td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.3.1.2 "><p id="p194144316189"><a name="p194144316189"></a><a name="p194144316189"></a>Specifies the project ID provided in the project list on the <strong id="b4765622512162"><a name="b4765622512162"></a><a name="b4765622512162"></a>My Credentials</strong> page.</p>
    </td>
    </tr>
    <tr id="row134144311181"><td class="cellrowborder" valign="top" width="38%" headers="mcps1.2.3.1.1 "><p id="p174114435189"><a name="p174114435189"></a><a name="p174114435189"></a>OS_TENANT_NAME</p>
    </td>
    <td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.3.1.2 "><p id="p7498035102313"><a name="p7498035102313"></a><a name="p7498035102313"></a>Specifies the project name provided in the project list on the <strong id="b138901501974"><a name="b138901501974"></a><a name="b138901501974"></a>My Credentials</strong> page.</p>
    </td>
    </tr>
    <tr id="row4411643181815"><td class="cellrowborder" valign="top" width="38%" headers="mcps1.2.3.1.1 "><p id="p9418439182"><a name="p9418439182"></a><a name="p9418439182"></a>OS_PROJECT_NAME</p>
    </td>
    <td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.3.1.2 "><p id="p89055415231"><a name="p89055415231"></a><a name="p89055415231"></a>The value is the same as the <strong id="b84235270617815"><a name="b84235270617815"></a><a name="b84235270617815"></a>OS_TENANT_NAME</strong> value.</p>
    </td>
    </tr>
    <tr id="row87341316192313"><td class="cellrowborder" valign="top" width="38%" headers="mcps1.2.3.1.1 "><p id="p137351016112318"><a name="p137351016112318"></a><a name="p137351016112318"></a>OS_AUTH_URL</p>
    </td>
    <td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.3.1.2 "><p id="p437114719239"><a name="p437114719239"></a><a name="p437114719239"></a>The parameter value is in the format of <strong id="b1265612520501"><a name="b1265612520501"></a><a name="b1265612520501"></a>https://</strong><em id="i70523994917849"><a name="i70523994917849"></a><a name="i70523994917849"></a>IAM URL</em>:<em id="i30169679717849"><a name="i30169679717849"></a><a name="i30169679717849"></a>Port number</em>/<em id="i133883547417849"><a name="i133883547417849"></a><a name="i133883547417849"></a>API version</em>, for example, <strong id="b33554595011"><a name="b33554595011"></a><a name="b33554595011"></a>https://iam.</strong><em id="i208568455817849"><a name="i208568455817849"></a><a name="i208568455817849"></a>example</em><strong id="b1626594845014"><a name="b1626594845014"></a><a name="b1626594845014"></a>.com:443/v3</strong>.</p>
    <a name="ul43716471232"></a><a name="ul43716471232"></a><ul id="ul43716471232"><li><em id="i1187224403819"><a name="i1187224403819"></a><a name="i1187224403819"></a>IAM URL</em>: Obtain the value from <a href="https://docs.otc.t-systems.com/en-us/endpoint/index.html" target="_blank" rel="noopener noreferrer">Regions and Endpoints</a>.</li><li><strong id="b18774166192611"><a name="b18774166192611"></a><a name="b18774166192611"></a>Port number</strong>: 443</li><li><strong id="b36431159112518"><a name="b36431159112518"></a><a name="b36431159112518"></a>API version</strong>: v3</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

3.  Run the following command to set environment variables:

    **source novarc**


The Heat client becomes available after OpenStackClient is installed and configured. For more information, see  [Creating Resources Using a Template \(Using the Heat Client\)](creating-resources-using-a-template-(using-the-heat-client).md).

