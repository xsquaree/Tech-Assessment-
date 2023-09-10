Summary on designing/deploying this using cloud services 

1. Extraction:
We can consider extraction of JSON data using a Python script deployed on EC2 instances. These instances are responsible for pulling data from the specified JSON link. The frequency of this extraction process can be configured in AWS Lambda based on the desired data update frequency. The use of AwS Lambda allows automation and efficiency which makes data extraction easier. Data from Zomato are updated and increasing every day, hence I feel that it is important to automate the extraction process every single day. 
2. Transformation:
AWS Docker containers are then used to do data transformation. Each microservice in these containers is in charge of cleaning and ensuring the correct data format. The use of container is because it is decentralized which increases adaptability, making it simpler to incorporate changes and carry out effective unit testing. Hence, it is easier to maintain in a long run and tested independently. 
3. Load:
After the data has been transformed and cleaned, it is loaded into a scalable data warehouse, Amazon RDS (Relational Database Service). 

The architecture diagram here showings the flow of the solutions and the infrastructure component: 



![architecture_diagram](https://github.com/xsquaree/Tech-Assessment-/assets/35002684/d8ef17ae-0918-4427-af85-0e039ae4efcd)

 

Some considerations to include would be: 
1.	Error handling in the microservices 
2.	AWS is using pay-as-you-go approach, hence we can stop their web services when we do not need to use it 

