# Failed to Pull an Image<a name="cce_faq_00015"></a>

If the  workload  details page displays an event indicating that image pulling fails, perform the following operations to locate the fault:

## Fault Locating<a name="en-us_topic_0242566251_section43315267479"></a>

-   [Check Item 1: Checking Whether imagePullSecret Is Specified When You Use kubectl to Create a Workload](#en-us_topic_0242566251_section629791052512)
-   [Check Item 2: Checking Whether the Image Address Is Correct When a Third-Party Image Is Used](#en-us_topic_0242566251_section819316261313)
-   [Check Item 3: Checking Whether an Incorrect Key Is Used or the Key Expires When a Third-Party Image Is Used](#en-us_topic_0242566251_section9312113135616)
-   [Check Item 4: Checking Whether Disk Space Is Insufficient](#en-us_topic_0242566251_section165209286116)

## Check Item 1: Checking Whether  **imagePullSecret**  Is Specified When You Use kubectl to Create a Workload<a name="en-us_topic_0242566251_section629791052512"></a>

For example, when creating a deployment named  **nginx**, check whether the YAML file contains the  **imagePullSecrets**  parameter, which indicates the secret name during image pulling.

-   To pull an image from SWR, set the  **imagePullSecrets**  parameter to  **default-secret**.
-   To pull an image from a third-party image repository, set the  **imagePullSecrets**  parameter to the created secret name.

The example shows the situation when you fail to pull an image when  **imagePullSecret**  is not configured in your YAML file.

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
        imagePullPolicy: Always
        name: nginx
      imagePullSecrets:
      - name: default-secret
```

**Solution**

When pulling an image from a third-party image repository, set  **imagePullSecrets**  to the created secret name.

## Check Item 2: Checking Whether the Image Address Is Correct When a Third-Party Image Is Used<a name="en-us_topic_0242566251_section819316261313"></a>

CCE can create workloads using images pulled from a third-party image repository in addition to SWR and Docker Hub.

Enter the third-party image address according to requirements. The format must be  **ip:port/path/name:version**  or  **name:version**. If no tag is specified,  **latest**  is used by default.

-   For a private repository, enter an image address in the format of  **ip:port/path/name:version**.
-   For an open-source Docker repository, enter an image address in the format of  **name:version**. For example,  **nginx:latest**.

The following information is displayed when you fail to pull an image due to incorrect image address provided.

```
Failed to pull image "nginx:v1.1": rpc error:code = Unknown desc=Error response from daemon: manifest for nginx:v1.1 not found
```

**Solution**

You can either edit your YAML file to modify the image address or log in to the CCE console to replace the image on the  **Upgrade**  tag page of the workload details page.

## Check Item 3: Checking Whether an Incorrect Key Is Used or the Key Expires When a Third-Party Image Is Used<a name="en-us_topic_0242566251_section9312113135616"></a>

CCE allows you to create workloads using images pulled from a third-party image repository in addition to SWR or Docker Hub.

**Solution**

Generally, a third-party image repository can be accessed only after authentication. CCE uses the secret authentication mode to obtain images. Therefore, you need to create a secret for an image repository before pulling images from the repository.

If the secret is incorrect or expires, images will fail to be pulled.

## Check Item 4: Checking Whether Disk Space Is Insufficient<a name="en-us_topic_0242566251_section165209286116"></a>

After a node is created in a cluster of v1.7.3-r7 or a later version, a 100 GB data disk dedicated for Docker is bound to the node. If the data disk space is insufficient, image fails to be pulled.

If the following information is contained in the Kubernetes event, the disk space on the node for storing images is full. You need to delete images or expand the disk capacity.

You can run  **lvs**  to check the disk space on the node for storing images.

![](figures/lvs.jpg)

You can run the following command to delete an image:

```
docker rmi –f {Image ID}
```

Perform the following steps to expend the disk capacity:

1.  Expand the capacity of the Docker disk on the EVS console.
2.  Log in to the target node.
3.  Run the following commands on the node to add the new disk capacity to the Docker disk:

    ```
    pvresize /dev/vdb
    lvextend -l+100%FREE -n vgpaas/thinpool
    ```


