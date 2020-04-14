# Getting Started with Elasticsearch<a name="css_01_0007"></a>

For details about the concept, advantages, functions, and application scenarios of CSS, see  [Overview](overview.md).

This section provides a simple example. For details, see  [Scenario Description](#section15177859183319). You can use the Elasticsearch search engine of CSS to search for data based on the scenario example. The basic operation process is as follows:

-   [Step 1: Create a Cluster](#section96881833619)
-   [Step 2: Import Data](#section398512163445)
-   [Step 3: Search for Data](#section167624221443)
-   [Step 4: Delete the Cluster](#section75027114374)

## Scenario Description<a name="section15177859183319"></a>

A women's clothing brand does business on an e-commerce website. It uses traditional databases to provide a commodity search function for users. However, with an increase in users and business, it suffers from the slow response and low accuracy of the traditional databases. To improve user experience and avoid user loss, the e-commerce website adopts Elasticsearch to provide the commodity search function for users. This solves the issues caused by traditional databases and increases user quantity.

This section describes how to use Elasticsearch to provide the search function for users.

Assume that the e-commerce website provides the following data:

```
{
"products":[
{"productName":"Latest art shirts for women in 2017 autumn","size":"L"}
{"productName":"Latest art shirts for women in 2017 autumn","size":"M"}
{"productName":"Latest art shirts for women in 2017 autumn","size":"S"}
{"productName":"Latest jeans for women in spring 2018","size":"M"}
{"productName":"Latest jeans for women in spring 2018","size":"S"}
{"productName":"Latest casual pants for women in spring 2017","size":"L"}
{"productName":"Latest casual pants for women in spring 2017","size":"S"}
]
}
```

## Step 1: Create a Cluster<a name="section96881833619"></a>

Before searching for data, create a cluster using Elasticsearch as the search engine. In this example, suppose that you create a cluster named  **Es-xfx**. This cluster is used only for getting started with Elasticsearch. For this cluster, you are advised to select  **css.medium.8**  for  **Node Specifications**,  **Common I/O**  for  **Node Storage Type**, and  **40 GB**  for  **Node Storage Capacity**. For details, see  [Creating a Cluster](creating-a-cluster.md).

After a cluster is created, switch to the cluster list to view the created cluster. If the  **Status**  of the cluster is  **Available**, the cluster is created successfully. See  [Figure 1](#fig65748551484).

**Figure  1**  Creating a cluster<a name="fig65748551484"></a>  
![](figures/creating-a-cluster.png "creating-a-cluster")

## Step 2: Import Data<a name="section398512163445"></a>

CSS supports importing data to Elasticsearch using Logstash, Kibana, or APIs. Kibana lets you visualize your Elasticsearch data. The following procedure illustrates how to import data to Elasticsearch using Kibana.

1.  On the  **Clusters**  page of the CSS management console, locate the row where the target cluster resides and click  **Kibana**  in the  **Operation**  column.
2.  In the left navigation pane of Kibana, click  **Dev Tools**. Click  **Get to work**  to switch to the  **Console**  page. See  [Figure 2](#fig221172817246).

    Enter the code as required in the left pane and view the result in the right pane.

    **Figure  2**  Console page<a name="fig221172817246"></a>  
    ![](figures/console-page.png "console-page")

3.  On the  **Console**  page, run the following command to create index named  **my\_store**:

    ```
    PUT /my_store
    {
      "settings": {
        "number_of_shards": 1
      },
      "mappings": {
        "products": {
          "properties": {
            "productName": {
              "type": "text"
              },
            "size": {
              "type": "keyword"
            }
          }
        }
      }
    }
    ```

    The command output is similar to below.

    ```
    {
      "acknowledged": true,
      "shards_acknowledged": true,
      "index": "my_store"
    }
    ```

4.  On the  **Console**  page, run the following command to import data to index named  **my\_store**:

    ```
    POST /my_store/products/_bulk
    {"index":{}}
    {"productName":"Latest art shirts for women in 2017 autumn","size":"L"}
    {"index":{}}
    {"productName":"Latest art shirts for women in 2017 autumn","size":"M"}
    {"index":{}}
    {"productName":"Latest art shirts for women in 2017 autumn","size":"S"}
    {"index":{}}
    {"productName":"Latest jeans for women in spring 2018","size":"M"}
    {"index":{}}
    {"productName":"Latest jeans for women in spring 2018","size":"S"}
    {"index":{}}
    {"productName":"Latest casual pants for women in spring 2017","size":"L"}
    {"index":{}}
    {"productName":"Latest casual pants for women in spring 2017","size":"S"}
    
    ```

    If the value of the  **errors**  field in the command output is  **false**, the data is imported successfully.


## Step 3: Search for Data<a name="section167624221443"></a>

-   **Full-text search**

    If you access the e-commerce website and want to search for commodities whose names include "spring jeans", enter "spring jeans" to begin your search. The following text provides the command to be executed on Kibana and the command output.

    Command to be executed on Kibana:

    ```
    GET /my_store/products/_search
    {
      "query": {"match": {
        "productName": "spring jeans"
      }}
    }
    ```

    The command output is similar to below.

    ```
    {
      "took": 80,
      "timed_out": false,
      "_shards": {
        "total": 1,
        "successful": 1,
        "skipped": 0,
        "failed": 0
      },
      "hits": {
        "total": 4,
        "max_score": 1.8069603,
        "hits": [
          {
            "_index": "my_store",
            "_type": "products",
            "_id": "yTG1QWUBRuneTTG2KJSq",
            "_score": 1.8069603,
            "_source": {
              "productName": "Latest jeans for women in spring 2018",
              "size": "M"
            }
          },
          {
            "_index": "my_store",
            "_type": "products",
            "_id": "yjG1QWUBRuneTTG2KJSq",
            "_score": 1.8069603,
            "_source": {
              "productName": "Latest jeans for women in spring 2018",
              "size": "S"
            }
          },
          {
            "_index": "my_store",
            "_type": "products",
            "_id": "yzG1QWUBRuneTTG2KJSq",
            "_score": 0.56677663,
            "_source": {
              "productName": "Latest casual pants for women in spring 2017",
              "size": "L"
            }
          },
          {
            "_index": "my_store",
            "_type": "products",
            "_id": "zDG1QWUBRuneTTG2KJSq",
            "_score": 0.56677663,
            "_source": {
              "productName": "Latest casual pants for women in spring 2017",
              "size": "S"
            }
          }
        ]
      }
    }
    ```

    -   Elasticsearch supports full-text search. The preceding command searches for the information about all commodities whose names include "spring" or "jeans".
    -   Unlike traditional databases, Elasticsearch can return results in milliseconds by using inverted indices.
    -   Elasticsearch supports sorting by score. In the command output, information about the first two commodities contains both  and "jeans", while that about the last two commodities contains only "spring". Therefore, the first two commodities rank prior to the last two due to high keyword match.


-   **Aggregation result display**

    The e-commerce website provides the function of displaying aggregation results. For example, it classifies commodities corresponding to "spring" based on the size so that you can collect the number of commodities of different sizes. The following provides the command to be executed on Kibana and the command output.

    Command to be executed on Kibana:

    ```
    GET /my_store/products/_search
    {
    "query": {
    "match": { "productName": "spring" }
    },
    "size": 0,
    "aggs": {
    "sizes": {
    "terms": { "field": "size" }
    }
    }
    }
    ```

    The command output is similar to below.

    ```
    {
      "took": 66,
      "timed_out": false,
      "_shards": {
        "total": 1,
        "successful": 1,
        "skipped": 0,
        "failed": 0
      },
      "hits": {
        "total": 4,
        "max_score": 0,
        "hits": []
      },
      "aggregations": {
        "sizes": {
          "doc_count_error_upper_bound": 0,
          "sum_other_doc_count": 0,
          "buckets": [
            {
              "key": "S",
              "doc_count": 2
            },
            {
              "key": "L",
              "doc_count": 1
            },
            {
              "key": "M",
              "doc_count": 1
            }
          ]
        }
      }
    }
    ```


## Step 4: Delete the Cluster<a name="section75027114374"></a>

Once you understand the process and method of using Elasticsearch, you can perform the following steps to delete the sample cluster and sample data to avoid resource waste.

After a cluster is deleted, its data cannot be recovered. Exercise caution when deleting a cluster.

1.  Log in to the CSS management console. In the left navigation pane, click  **Clusters**  to switch to the  **Clusters**  page.
2.  Locate the row where the  **Es-xfx**  cluster resides and click  **More \> Delete**  in the  **Operation**  column. 
3.  In the displayed dialog box, click  **Yes**.

