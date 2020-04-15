# Introduction<a name="EN-US_TOPIC_0125376049"></a>

## Process<a name="s3cb6ba5f802b4f02b479d1c332adac42"></a>

The process for migrating user data with Loader is as follows:

1.  Access the Loader page of the Hue WebUI.
2.  Manage Loader links.
3.  Create a job and select a data source link and a link for saving data.
4.  Run the job to complete data migration.

## Loader Page<a name="s49ec1e4eeb254b4d97c98caf69fa110f"></a>

The Loader page is a graphical data migration management tool based on the open source Sqoop WebUI and is hosted on the Hue WebUI. Perform the following operations to access the Loader page:

1.  Access the Hue WebUI. For details, see  [Accessing the UI of the Open Source Component](accessing-the-ui-of-the-open-source-component.md).
2.  Choose  **Data Browsers**  \>  **Sqoop**.

    The job management tab page is displayed by default on the Loader page.


## Loader Link<a name="sd7b4f674f84f46f385a7a72b8c2c3962"></a>

Loader links save data location information. Loader uses links to access data or save data to the specified location. Perform the following operations to access the Loader link management page:

1.  Access the Loader page.
2.  Click  **Manage links**.

    The Loader link management page is displayed.

    You can click **Manage jobs**  to return to the job management page.

3.  Click  **New link**  to go to the configuration page and set parameters to create a Loader link.

## Loader Job<a name="s08da4ea795d248f4ba93e0d259d4abe5"></a>

Loader jobs are used to manage data migration tasks. Each job consists of a source data link and a destination data link. A job reads data from the source link and saves data to the destination link to complete a data migration task.

