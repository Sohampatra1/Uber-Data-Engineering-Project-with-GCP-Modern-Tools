# Uber Data Analytics Project

This project aims to analyze the Uber dataset using various data engineering and analytics techniques. The project utilizes Google Cloud Platform (GCP) services and modern tools to process, transform, and visualize the data.

## Project Steps

1. **Create Bucket**: Create a storage bucket in GCP to store the project files.

2. **Create Instance**: Set up a GCP compute instance with the following specifications:
   - CPU: e2 standard 16
   - 8 core CPU
   - 64 GB RAM

3. **SSH Connection**: Establish an SSH connection to the GCP compute instance.

4. **Run Command**: Execute the commands provided in the `command.txt` file from the GitHub repository to install Python3 and the required libraries, including:
   - pandas
   - maze.ai
   - Google Cloud SDK

5. **Start Maze.ai Project**: Launch the Maze.ai project on port 6789 and access it through the external IP provided by the GCP instance.

6. **Update Firewall Rule**: Modify the firewall rule to allow access to the Maze.ai dashboard via the external IP and port.

7. **Create Data Loader Pipeline**: Set up a data loading pipeline to import the Uber dataset into the project.

8. **Create Data Transformer Pipeline**: Develop a data transformation pipeline using a generic template. Handle any errors or kernel overloads that may occur during the transformation process.

9. **Connect to DataExporter**: Connect the data transformation pipeline to the DataExporter module to export the transformed data to Google BigQuery.

10. **Configure io_config.yaml**: Access GCP, open API services, and create a new service account. Download the service account key in JSON format and copy the JSON data into the `io_config.yaml` file. This step ensures secure access to GCP services.

11. **Complete Data Loader Pipeline**: After completing the third pipeline, navigate to BigQuery and refresh the data to preview the connected data.

12. **Data Visualization**: Utilize Looker or Data Studio to create visualizations and analyze the Uber dataset.


## Hashnode Blog Post

Check out my detailed blog post on this project on [Hashnode](https://sohampatra.hashnode.dev/building-an-uber-data-engineering-project-with-gcp-and-modern-tools).



## Project Dependencies

- Python 3
- pandas
- maze.ai
- Google Cloud SDK
- Google Cloud BigQuery

## License

This project is licensed under the [MIT License](LICENSE).
