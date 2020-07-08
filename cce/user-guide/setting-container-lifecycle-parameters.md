# Setting Container Lifecycle Parameters<a name="cce_01_0105"></a>

CCE provides  callback functions  for the lifecycle management of containerized workloads. For example, if you want a container to perform a certain operation before stopping, you can register a hook function.

CCE provides the following lifecycle callback functions:

-   **Start Command**: executed to start a container. For details, see  [Setting Container Startup Commands](setting-container-startup-commands.md).
-   **Post-Start**: executed immediately after a container is started. For details, see  [Post-Start Processing](#section15243544163715).
-   **Pre-Stop**: executed before a container is stopped. The pre-stop processing function helps you ensure that the services running in the instances can be completed in advance in the case of instance upgrade or deletion. For details, see  [Pre-Stop Processing](#section2334114473712).

## Commands and Parameters Used to Run a Container<a name="section913591582414"></a>

The Docker image has metadata that stores image information. If lifecycle commands and parameters are not set, CCE runs the default commands and parameters, that is, Docker native commands Entrypoint and CMD, provided during image creation. For details, see the description of  [Entrypoint](https://docs.docker.com/engine/reference/builder/#/entrypoint)  and  [CMD](https://docs.docker.com/engine/reference/builder/#/cmd).

If the commands and parameters used to run a container are set during workload creation, the default commands Entrypoint and CMD are overwritten during image building. The rules are as follows:

**Table  1**  Commands and parameters used to run a container

<a name="table4833929202611"></a>
<table><thead align="left"><tr id="row1683442952610"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.1"><p id="p17834192919269"><a name="p17834192919269"></a><a name="p17834192919269"></a>Image Entrypoint</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.2"><p id="p168345294268"><a name="p168345294268"></a><a name="p168345294268"></a>Image CMD</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.3"><p id="p283416297265"><a name="p283416297265"></a><a name="p283416297265"></a>Command to Run a Container</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.4"><p id="p583412914264"><a name="p583412914264"></a><a name="p583412914264"></a>Parameters to Run a Container</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.5"><p id="p198341629182620"><a name="p198341629182620"></a><a name="p198341629182620"></a>Command Executed</p>
</th>
</tr>
</thead>
<tbody><tr id="row283622962618"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.1 "><p id="p583642920263"><a name="p583642920263"></a><a name="p583642920263"></a>[touch]</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="p128361129162616"><a name="p128361129162616"></a><a name="p128361129162616"></a>[/root/test]</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.3 "><p id="p15836162952619"><a name="p15836162952619"></a><a name="p15836162952619"></a>Not set</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.4 "><p id="p18836529172618"><a name="p18836529172618"></a><a name="p18836529172618"></a>Not set</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p1836132922617"><a name="p1836132922617"></a><a name="p1836132922617"></a>[touch /root/test]</p>
</td>
</tr>
<tr id="row283662932612"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.1 "><p id="p3836229172615"><a name="p3836229172615"></a><a name="p3836229172615"></a>[touch]</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="p18836142932613"><a name="p18836142932613"></a><a name="p18836142932613"></a>[/root/test]</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.3 "><p id="p1183602917269"><a name="p1183602917269"></a><a name="p1183602917269"></a>[mkdir]</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.4 "><p id="p983642982611"><a name="p983642982611"></a><a name="p983642982611"></a>Not set</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p1183612293269"><a name="p1183612293269"></a><a name="p1183612293269"></a>[mkdir]</p>
</td>
</tr>
<tr id="row9836152912618"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.1 "><p id="p167981050113418"><a name="p167981050113418"></a><a name="p167981050113418"></a>[touch]</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="p17837142972617"><a name="p17837142972617"></a><a name="p17837142972617"></a>[/root/test]</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.3 "><p id="p168379292269"><a name="p168379292269"></a><a name="p168379292269"></a>Not set</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.4 "><p id="p1583702911260"><a name="p1583702911260"></a><a name="p1583702911260"></a>[/opt/test]</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p58371729182613"><a name="p58371729182613"></a><a name="p58371729182613"></a>[touch /opt/test]</p>
</td>
</tr>
<tr id="row16837172972617"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.1 "><p id="p138691301355"><a name="p138691301355"></a><a name="p138691301355"></a>[touch]</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="p208371129182610"><a name="p208371129182610"></a><a name="p208371129182610"></a>[/root/test]</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.3 "><p id="p1283715298267"><a name="p1283715298267"></a><a name="p1283715298267"></a>[mkdir]</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.4 "><p id="p544733220362"><a name="p544733220362"></a><a name="p544733220362"></a>[/opt/test]</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p20837112917262"><a name="p20837112917262"></a><a name="p20837112917262"></a>[mkdir /opt/test]</p>
</td>
</tr>
</tbody>
</table>

## Startup Commands<a name="section54912655316"></a>

By default, the default command during image start. To run a specific command or rewrite the default image value, you must perform specific settings: For details, see  [Setting Container Startup Commands](setting-container-startup-commands.md).

## Post-Start Processing<a name="section15243544163715"></a>

1.  Log in to the CCE console. When creating a workload, expand  **Lifecycle**.
2.  Set the post-start processing parameters, as listed in  [Table 2](#table823614643810).

    **Table  2**  Post-start processing parameters

    <a name="table823614643810"></a>
    <table><thead align="left"><tr id="row182422468384"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.3.1.1"><p id="p122437460382"><a name="p122437460382"></a><a name="p122437460382"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="77%" id="mcps1.2.3.1.2"><p id="p1924524616384"><a name="p1924524616384"></a><a name="p1924524616384"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row102472046183820"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p1248204618385"><a name="p1248204618385"></a><a name="p1248204618385"></a><span class="keyword" id="keyword20279474821744"><a name="keyword20279474821744"></a><a name="keyword20279474821744"></a>CLI</span></p>
    </td>
    <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p8249134611380"><a name="p8249134611380"></a><a name="p8249134611380"></a>Command to be executed in the container. The command format is <strong id="b842352706152442"><a name="b842352706152442"></a><a name="b842352706152442"></a>Command Args[1] Args[2]...</strong>. <strong id="b84235270615253"><a name="b84235270615253"></a><a name="b84235270615253"></a>Command</strong> is a system command or a user-defined executable program. If no path is specified, an executable program in the default path will be selected. If multiple commands need to be executed, write the commands into a script for execution.</p>
    <p id="p32497468380"><a name="p32497468380"></a><a name="p32497468380"></a>Example command:</p>
    <pre class="screen" id="screen15250164673811"><a name="screen15250164673811"></a><a name="screen15250164673811"></a>exec: 
      command: 
      - /install.sh 
      - install_agent</pre>
    <p id="p92541146123820"><a name="p92541146123820"></a><a name="p92541146123820"></a>Enter <strong id="b842352706152826"><a name="b842352706152826"></a><a name="b842352706152826"></a>/install install_agent</strong> in the script.</p>
    <p id="p202541746103810"><a name="p202541746103810"></a><a name="p202541746103810"></a>This command indicates that <strong id="b842352706152857"><a name="b842352706152857"></a><a name="b842352706152857"></a>install_agent</strong> will be executed after the container is created successfully.</p>
    </td>
    </tr>
    <tr id="row925519462389"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p1261104603816"><a name="p1261104603816"></a><a name="p1261104603816"></a>HTTP request</p>
    </td>
    <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p162625461389"><a name="p162625461389"></a><a name="p162625461389"></a>HTTP invocation request. The related parameters are described as follows:</p>
    <a name="ul426364613385"></a><a name="ul426364613385"></a><ul id="ul426364613385"><li>Path: (optional) request URL.</li><li>Port: (mandatory) request port.</li><li>Host address: (optional) IP address of the request. The default value is the IP address of the node where the container resides.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


## Pre-Stop Processing<a name="section2334114473712"></a>

1.  Log in to the CCE console. When creating a workload, expand  **Lifecycle**.
2.  Set pre-stop processing parameters, as shown in  [Table 2](#table823614643810).

    **Table  3**  Pre-stop processing parameters

    <a name="table1541840142714"></a>
    <table><thead align="left"><tr id="row18419601274"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.3.1.1"><p id="p12419130182714"><a name="p12419130182714"></a><a name="p12419130182714"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="77%" id="mcps1.2.3.1.2"><p id="p1441913013274"><a name="p1441913013274"></a><a name="p1441913013274"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row04201302279"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p6420110192718"><a name="p6420110192718"></a><a name="p6420110192718"></a><span class="keyword" id="keyword1072082910"><a name="keyword1072082910"></a><a name="keyword1072082910"></a>CLI</span></p>
    </td>
    <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p94204010271"><a name="p94204010271"></a><a name="p94204010271"></a>Command to be executed in the container. The command format is <strong id="b1994861274"><a name="b1994861274"></a><a name="b1994861274"></a>Command Args[1] Args[2]...</strong>. <strong id="b1451902335"><a name="b1451902335"></a><a name="b1451902335"></a>Command</strong> is a system command or a user-defined executable program. If no path is specified, an executable program in the default path will be selected. If multiple commands need to be executed, write the commands into a script for execution.</p>
    <p id="p94203082712"><a name="p94203082712"></a><a name="p94203082712"></a>Example command:</p>
    <pre class="screen" id="screen6420190132712"><a name="screen6420190132712"></a><a name="screen6420190132712"></a>exec: 
      command: 
      - /install.sh 
      - install_agent</pre>
    <p id="p742120182716"><a name="p742120182716"></a><a name="p742120182716"></a>Enter <strong id="b85783068"><a name="b85783068"></a><a name="b85783068"></a>/install install_agent</strong> in the script.</p>
    <p id="p44211003277"><a name="p44211003277"></a><a name="p44211003277"></a>This command indicates that <strong id="b1475454961"><a name="b1475454961"></a><a name="b1475454961"></a>install_agent</strong> will be executed after the container is created successfully.</p>
    </td>
    </tr>
    <tr id="row4421190152715"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p154216032719"><a name="p154216032719"></a><a name="p154216032719"></a>HTTP request</p>
    </td>
    <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p15421160122715"><a name="p15421160122715"></a><a name="p15421160122715"></a>HTTP invocation request. The related parameters are described as follows:</p>
    <a name="ul204215052713"></a><a name="ul204215052713"></a><ul id="ul204215052713"><li>Path: (optional) request URL.</li><li>Port: (mandatory) request port.</li><li>Host address: (optional) IP address of the request. The default value is the IP address of the node where the container resides.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


## Example YAML for Setting the Container Lifecycle<a name="section151181981167"></a>

This section uses Nginx as an example to describe how to set the container lifecycle.

**Prerequisites**

The ECS where the kubectl client runs has been connected to your cluster. For details, see  [Connecting to a Kubernetes Cluster Using kubectl](connecting-to-a-kubernetes-cluster-using-kubectl.md).

**Procedure**

1.  Log in to the ECS on which kubectl has been configured. For details, see  [Logging In to a Linux ECS](https://docs.otc.t-systems.com/en-us/usermanual/ecs/en-us_topic_0013771089.html).
2.  Create and edit the  **nginx-deployment.yaml**  file.  **nginx-deployment.yaml**  is an example file name, and you can change it as required.

    **vi nginx-deployment.yaml**

    In the following configuration file, the  **postStart**  command is defined to run the  **install.sh**  command in the  **/bin/bash**  directory.  **preStop**  is defined to run the  **uninstall.sh**  command.

    ```
    apiVersion: extensions/v1beta1
    kind: Deployment
    metadata:
      name: nginx
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: nginx
      strategy:
        type: RollingUpdate
      template:
        metadata:
          labels:
            app: nginx
        spec:
          containers:
          - image: nginx 
            command:
            - sleep 3600                        #Startup command
            imagePullPolicy: Always
            lifecycle:
              postStart:
                exec:
                  command:
                  - /bin/bash
                  - install.sh                  #Post-start command
              preStop:
                exec:
                  command:
                  - /bin/bash
                  - uninstall.sh                 #Pre-stop command
            name: nginx
          imagePullSecrets:
          - name: default-secret
    ```


