# Performance Tuning<a name="EN-US_TOPIC_0221415093"></a>

## Memory Configuration<a name="section18215463818"></a>

Flink depends on in-memory computing. If memory is insufficient during computing, the Flink execution efficiency will be adversely affected. You can determine whether memory becomes a performance bottleneck by monitoring garbage collection \(GC\) and evaluating memory usage, and take performance optimization measures.

If full GC frequently occurs in the YARN container GC logs of monitoring node processes, optimize GC.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>GC configuration: Add the following parameters to the  **env.java.opts**  configuration item in the  **conf/flink-conf.yaml**  file on the client: "-Xloggc:<LOG\_DIR\>/gc.log -XX:+PrintGCDetails -XX:-OmitStackTraceInFastThrow -XX:+PrintGCTimeStamps -XX:+PrintGCDateStamps -XX:+UseGCLogFileRotation -XX:NumberOfGCLogFiles=20 -XX:GCLogFileSize=20M". GC logs are added by default.  

-   GC optimization

    To optimize GC, adjust the ratio of the old generation to the young generation. In the  **conf/flink-conf.yaml**  configuration file on the client, add the  **-XX:NewRatio**  parameter to the  **env.java.opts**  configuration item. For example,  **-XX:NewRatio=2**  indicates that the ratio of the old generation to the young generation 2:1, the new generation occupies 1/3 of the entire heap space, and the old generation occupies 2/3.


-   When developing Flink applications, optimize the data partitioning or grouping of DataStream.
    -   If partitioning causes data skew, partitioning needs to be optimized.
    -   Avoid unparallel operations, because some operations on DataStream, for example, WindowAll, cause parallelism failure.
    -   Do not use a string for  **keyBy**.


## Configuring DOP<a name="section044644113397"></a>

The degree of parallelism \(DOP\) indicates the number of tasks to be executed concurrently. It determines the number of data blocks after splitting. Adjust the DOP to maximize the number of tasks, the volume of data processed in each task, and the data processing capabilities the machines.

Query CPU and memory usage. If data and tasks are not evenly distributed among nodes, increase the DOP. Increasing the DOP makes full use of computing capabilities of machines in the cluster.

You can specify and adjust the DOP at one of the following levels \(the priorities of which are in descending order\) based on the actual memory, CPU, data, and application logic conditions.

-   Operator

    Invoke the  **setParallelism\(\)**  method to specify the DOP of an operator, data source, and data sink. Example:

    ```
    final StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
    DataStream<String> text = [...]
    DataStream<Tuple2<String, Integer>> wordCounts = text
        .flatMap(new LineSplitter())
        .keyBy(0)
        .timeWindow(Time.seconds(5))
        .sum(1).setParallelism(5);
    wordCounts.print();
    env.execute("Word Count Example");
    ```

-   Execution environment

    A Flink program runs in the execution environment. In the execution environment, a default DOP is defined for all executed operators, data sources, and data sinks.

    You can specify the default DOP by invoking the  **setParallelism\(\)**  method. Example:

    ```
    final StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
    env.setParallelism(3);
    DataStream<String> text = [...]
    DataStream<Tuple2<String, Integer>> wordCounts = [...]
    wordCounts.print();
    env.execute("Word Count Example");
    ```


-   Client

    You can specify the DOP when submitting jobs to Flink on the client. For a CLI client, you can specify the DOP using the  **-p**  parameter. Example:

    ```
    ./bin/flink run -p 10 ../examples/*WordCount-java*.jar
    ```

-   System

    At the system level, you can modify  **parallelism.default**  in the  **flink-conf.yaml**  file in the  **conf**  directory of the Flink client to specify the default DOP for all execution environments.


## Configuring Process Parameters<a name="section417431434014"></a>

In Flink on YARN mode, there are two processes: JobManager and TaskManager. JobManagers and TaskManagers shoulder major responsibilities during task scheduling and running.

Parameter configurations of JobManagers and TaskManagers significantly affect the execution performance of Flink applications. You can perform the following operations to optimize Flink cluster performance.

1.  Configure JobManager memory.

    JobManagers are responsible for task scheduling and message communications between the TaskManager and ResourceManager. JobManager memory needs to be added as tasks and the DOP increase.

    You can set proper JobManager memory based on the number of tasks.

    -   When running the  **yarn-session**  command, add the  **-jm MEM**  parameter to configure memory.
    -   When running the  **yarn-cluster**  command, add the  **-yjm MEM**  parameter to configure memory.

2.  Configure the number of TaskManagers.

    Each core of a TaskManager can process a task at the same time. Increasing the number of TaskManager has the same effect as increasing the DOP. Therefore, you can increase the number of TaskManagers to improve efficiency when there are sufficient resources.

    -   When running the  **yarn-session**  command, add the  **-n NUM**  parameter to configure the number of TaskManagers.
    -   When running the  **yarn-cluster**  command, add the  **-yn NUM**  parameter to configure the number of TaskManagers.

3.  Configure the number of TaskManager slots.

    Multiple cores of a TaskManager can process multiple tasks at the same time. This has the same effect as increasing the DOP. However, the number of cores and the memory must be balanced, because all cores share the memory of the TaskManager.

    -   When running the  **yarn-session**  command, add the  **-s NUM**  parameter to configure the number of slots.
    -   When running the  **yarn-cluster**  command, add the  **-ys NUM**  parameter to configure the number of slots.

4.  Configure TaskManager memory.

    The memory of a TaskManager is used for task execution and communications. A large-size task requires more resources. In this case, you can increase memory.

    -   When running the  **yarn-session**  command, add the  **-tm MEM**  parameter to configure memory.
    -   When running the  **yarn-cluster**  command, add the  **-ytm MEM**  parameter to configure memory.


## Partitioning Design Methods<a name="section15194150134117"></a>

A proper partitioning design can optimize task splitting. Ensure even partitioning during programming to prevent data skew in tasks. Otherwise, long-time execution of a task will delay the whole task.

Partitioning methods are as follows:

-   **Random partitioning**: Partitions elements randomly.

    ```
    dataStream.shuffle();
    ```

-   **Rebalancing \(Round-robin partitioning\)**: Partitions elements round-robin, creating equal load per partition. This is useful for performance optimization in the presence of data skew.

    ```
    dataStream.rebalance();
    ```

-   **Rescaling**: Partitions elements, round-robin, to a subset of downstream operations. This is useful if you want to have pipelines where you, for example, fan out from each parallel instance of a source to a subset of several mappers to distribute load but don't want the full rebalance that  **rebalance\(\)**  would incur.

    ```
    dataStream.rescale();
    ```

-   **Broadcasting**: Broadcasts elements to every partition.

    ```
    dataStream.broadcast();
    ```

-   **Custom partitioning**: Uses a user-defined Partitioner to select the target task for each element. Custom partitioning allows users to partition data based on a certain feature to optimize task execution.

    The following is an example:

    ```
    // Use fromElements to construct a simple Tuple2 flow.
    DataStream<Tuple2<String, Integer>> dataStream = env.fromElements(Tuple2.of("hello",1), Tuple2.of("test",2), Tuple2.of("world",100));
    // Define a key value used for partitioning. The return value is the partition to which the key belongs. The value plus 1 is the ID of the corresponding subtask.
    Partitioner<Tuple2<String, Integer>> strPartitioner = new Partitioner<Tuple2<String, Integer>>() {
        @Override
        public int partition(Tuple2<String, Integer> key, int numPartitions) {
            return (key.f0.length() + key.f1) % numPartitions;
        }
    };
    // Indicates the key value for partitioning using Tuple2.
    dataStream.partitionCustom(strPartitioner, new KeySelector<Tuple2<String, Integer>, Tuple2<String, Integer>>() {
        @Override
        public Tuple2<String, Integer> getKey(Tuple2<String, Integer> value) throws Exception {
            return value;
        }
    }).print();
    ```


## Configuring the Netty Network Communication<a name="section8464203654118"></a>

Flink communications depend on a Netty network. Netty network configuration is critical to Flink application execution, because the network performance determines data exchange speed and task execution efficiency.

The following parameters allow for advanced tuning in the  **conf/flink-conf.yaml**  configuration file on the client. The default values are sufficient. Exercise caution when changing the default values, preventing performance deterioration.

-   **taskmanager.network.netty.num-arenas**: Number of Netty arenas. The default value is the value of  **taskmanager.numberOfTaskSlots**.
-   **taskmanager.network.netty.server.numThreads**  and  **taskmanager.network.netty.client.numThreads**: Number of Netty server and client threads, respectively. The default values are the value of  **taskmanager.numberOfTaskSlots**.
-   **taskmanager.network.netty.client.connectTimeoutSec**: Netty client connection timeout. The default value is  **120s**.
-   **taskmanager.network.netty.sendReceiveBufferSize**: Netty send and receive buffer size. This defaults to the system buffer size \(**cat /proc/sys/net/ipv4/tcp\_\[rw\]mem**\) and is 4 MB in modern Linux.
-   **taskmanager.network.netty.transport**: Netty transport type, either  **nio**  or  **epoll**. The default value is  **nio**.

## Experience Summary<a name="section63680211423"></a>

**Avoiding Data Skew**

If data skew occurs \(certain data volume is extremely large\), the execution time of tasks is inconsistent even though no GC is performed.

-   Redefine the keys. Use keys of smaller granularity to optimize task sizes.
-   Modify the DOP.
-   Call the rebalance operation to balance data partitions.

**Setting Buffer Timeout**

-   During the execution of tasks, data is exchanged through network. You can configure the  **setBufferTimeout**  parameter to specify a buffer timeout interval for data exchanging among different servers. 
-   If  **setBufferTimeout**  is set to  **-1**, the refreshing operation is performed when the buffer is full, maximizing the throughput. If  **setBufferTimeout**  is set to  **0**, the refreshing operation is performed each time data is received, minimizing the delay. If  **setBufferTimeout**  is set to a value greater than  **0**, the refreshing operation is performed after the butter times out.

    The following is an example.

    ```
    env.setBufferTimeout(timeoutMillis);
    env.generateSequence(1,10).map(new MyMapper()).setBufferTimeout(timeoutMillis);
    ```


