# Using a Third-Party Image<a name="cce_01_0009"></a>

CCE allows you to create workloads using images pulled from  third-party image repositories.

Generally, you are required to pass authentication using your account and password before accessing a third-party image repository. The secret authentication is used for pulling images from a CCE container. Therefore, you must create a secret for accessing the image repository before pulling images.

## Prerequisites<a name="section14876601632"></a>

The node where the workload is running is accessible from public networks. Public network access can be achieved either through a  [node access \(NodePort\)](nodeport.md)  service.

## Using the Console<a name="section0402183334411"></a>

1.  <a name="li16481144064414"></a>Create a secret for accessing a third-party image repository.

    In the navigation pane, choose  **Configuration Center**  \>  **Secret**, and click  **Create Secret**.  **Type**  must be set to  **kubernetes.io/dockerconfigjson**. For details, see  [Creating a Secret](creating-a-secret.md).

    Enter the user name and password used to access the third-party image repository.

2.  Create a workload. For details, see  [Creating a Deployment](creating-a-deployment.md)  or  [Creating a StatefulSet](creating-a-statefulset.md). If the workload will be created from a third-party image, set the image parameters as follows:
    1.  Set  **Secret Authentication**  to  **Yes**.
    2.  Select the secret created in step  [1](#li16481144064414).
    3.  Enter the image address.

3.  Click  **OK**.

## Using CLI<a name="section18217101117197"></a>

1.  Configure kubectl. For details, see  [Connecting to a Kubernetes Cluster Using kubectl](connecting-to-a-kubernetes-cluster-using-kubectl.md).
2.  Log in to the ECS on which the kubectl commands have been configured.
3.  Create a secret of the dockercfg type using kubectl.

    ```
    kubectl create secret docker-registry myregistrykey --docker-server=DOCKER_REGISTRY_SERVER --docker-username=DOCKER_USER --docker-password=DOCKER_PASSWORD --docker-email=DOCKER_EMAIL
    ```

    In the preceding commands,  **myregistrykey**  indicates the secret name, and other parameters are described as follows:

    -   **DOCKER\_REGISTRY\_SERVER**: address of a third-party image repository, for example,  **www.3rdregistry.com**  or  **10.10.10.10:443**
    -   **DOCKER\_USER**: account used for logging in to a third-party image repository
    -   **DOCKER\_PASSWORD**: password used for logging in to a third-party image repository
    -   **DOCKER\_EMAIL**: email of a third-party image repository

4.  Use a third-party image to create a workload.

    A dockecfg secret is used for authentication when you obtain a private image. The following is an example of using the myregistrykey for authentication.

    ```
    apiVersion: v1
    kind: Pod
    metadata:
      name: foo
      namespace: default
    spec:
      containers:
        - name: foo
          image: www.3rdregistry.com/janedoe/awesomeapp:v1
      imagePullSecrets:
        - name: myregistrykey              #Use the created key.
    ```


