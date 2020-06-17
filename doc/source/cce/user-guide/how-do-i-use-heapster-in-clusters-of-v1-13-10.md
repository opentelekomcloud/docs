# How Do I Use heapster in Clusters of v1.13.10?<a name="cce_01_0235"></a>

After a cluster of v1.13.10 is created, you can use heapster only after rbac is enabled.

## Procedure<a name="section1735317421484"></a>

1.  Connect to the cluster on which you need to use heapster by following the instruction provided in  [Connecting to a Kubernetes Cluster Using kubectl](connecting-to-a-kubernetes-cluster-using-kubectl.md).
2.  Delete the existing heapster cluster role.

    **kubectl delete clusterrole system:heapster**

3.  Create a heapster cluster role.

    Copy the following file to a server on which kubectl is supported, and name the file to  **heapster-cluster-role.yaml**.

    ```
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      annotations:
        rbac.authorization.kubernetes.io/autoupdate: "true"
      labels:
        kubernetes.io/bootstrapping: rbac-defaults
      name: system:heapster
    rules:
    - apiGroups:
      - ""
      resources:
      - events
      - namespaces
      - nodes
      - pods
      - nodes/stats
      verbs:
      - create
      - get
      - list
      - watch
    - apiGroups:
      - extensions
      resources:
      - deployments
      verbs:
      - get
      - list
      - update
      - watch
    ```

    Run the following command to create a heapster cluster role.

    **kubectl create -f heapster-cluster-role.yaml**

4.  Create a heapster service account.

    Copy the following file to a server on which kubectl is supported, and name the file to  **heapster-serviceaccount.yaml**.

    ```
    apiVersion: v1
    kind: ServiceAccount
    metadata:
      name: heapster
      namespace: kube-system
    ```

    Run the following command to create a heapster service account.

    **kubectl create -f heapster-serviceaccount.yaml**

5.  Create a heapster cluster role binding.

    Copy the following file to a server on which kubectl is supported, and name the file to  **heapster-cluster-rolebinding.yaml**.

    ```
    kind: ClusterRoleBinding
    apiVersion: rbac.authorization.k8s.io/v1beta1
    metadata:
      name: heapster
    roleRef:
      apiGroup: rbac.authorization.k8s.io
      kind: ClusterRole
      name: system:heapster
    subjects:
    - kind: ServiceAccount
      name: heapster
      namespace: kube-system
    ```

    Run the following command to create a heapster cluster role binding.

    **kubectl create -f heapster-cluster-rolebinding.yaml**

6.  Re-create the heapster deployment.

    Copy the following file to a server on which kubectl is supported, and name the file to  **heapster-apiserver.yaml**.

    ```
    apiVersion: extensions/v1beta1
    kind: Deployment
    metadata:
      annotations:
        deployment.kubernetes.io/revision: "1"
      generation: 1
      labels:
        k8s-app: heapster
        module: apiserver
        version: v6
      name: heapster-apiserver
      namespace: kube-system
    spec:
      progressDeadlineSeconds: 2147483647
      replicas: 1
      revisionHistoryLimit: 2147483647
      selector:
        matchLabels:
          k8s-app: heapster
          module: apiserver
          version: v6
      strategy:
        rollingUpdate:
          maxSurge: 1
          maxUnavailable: 1
        type: RollingUpdate
      template:
        metadata:
          creationTimestamp: null
          labels:
            k8s-app: heapster
            module: apiserver
            version: v6
          name: heapster
        spec:
          containers:
          - command:
            - /heapster
            - --source=kubernetes.summary_api:''?useServiceAccount=true&kubeletPort=10250&kubeletHttps=true&insecure=true&auth=/srv/config
            - --api-server
            - --secure-port=6443
            image: k8s.gcr.io/heapster-amd64:v1.5.3
            imagePullPolicy: IfNotPresent
            name: heapster
            ports:
            - containerPort: 6443
              name: https
              protocol: TCP
            - containerPort: 8080
              name: http
              protocol: TCP
            resources: {}
            securityContext:
              runAsUser: 0
            terminationMessagePath: /dev/termination-log
            terminationMessagePolicy: File
            volumeMounts:
            - mountPath: /root/.kube
              name: config
            - mountPath: /srv/config
              name: heapster
              subPath: config
          dnsPolicy: ClusterFirst
          restartPolicy: Always
          schedulerName: default-scheduler
          securityContext: {}
          serviceAccount: heapster
          serviceAccountName: heapster
          terminationGracePeriodSeconds: 30
          volumes:
          - hostPath:
              path: /root/.kube
              type: ""
            name: config
          - configMap:
              defaultMode: 420
              items:
              - key: config
                path: config
              name: heapster
            name: heapster
    ```

    Run the following commands to re-create the heapster deployment.

    **kubectl delete -f heapster-apiserver.yaml**

    **kubectl create -f heapster-apiserver.yaml**

7.  Check whether heapster is enabled.

    **kubectl top nodes**

    heapster is enabled when statistics are displayed in the command output.


