# HospitalManagementSystem

Hospital Management System is a Project in python created by Aisha Faheem (102579) a Master's Student at BHT studying Data Science.

## 1. Git/Github:

I used github for controlling variants and versions. Since this was fairly new for me, I did initially struggle with it but this was done to store, push code and even uml diagram variants.

![image](https://github.com/AishaFaheem/HospitalManagementSystem/assets/64909342/4964b90b-e028-4db4-8cbf-7dbc68d74609)
![image](https://github.com/AishaFaheem/HospitalManagementSystem/assets/64909342/ef36289e-c011-4867-a94c-4f10251d92a6)


## 2. UML Diagrams:

I created UML Diagrams using draw.io, manually.
   
### Use Case Diagram:
A Use Case Diagram provides a visual representation of the functionality offered by a system, depicting actors, their objectives, and any interactions or dependencies between those use cases. It offers a high-level overview of how users (actors) interact with the system to accomplish specific goals.

[Use Case Diagram](https://drive.google.com/file/d/1C8CwuUi2ikwfCBTvw4JreK1dGvGdz1bP/view?usp=sharing)

### Sequence Diagram:
In a Sequence Diagram, the interactions between various processes or components of a system are illustrated, showing the sequence in which these interactions occur. It visually depicts how processes communicate with each other over time, highlighting the order of execution and the exchange of messages.

[Sequence Diagram](https://drive.google.com/file/d/1yZeZiP1Gu3jgwc8QjmWHAnJmd7GfYQoG/view?usp=sharing)

### Class Diagram:
A Class Diagram presents the structure of a system by depicting its classes, along with their attributes, methods (or operations), and the relationships between objects. It offers a static view of the system's architecture, emphasizing the blueprint of its components and their associations.

[Class Diagram](https://drive.google.com/file/d/14xqMyPHplQVmKomeD5NCnVyrb5p4PGbl/view?usp=sharing)

### Activity Diagram:
An Activity Diagram illustrates the flow of control or data among different activities within a system. It demonstrates the sequence of actions or steps involved in a process, showcasing decision points, parallel activities, and the overall workflow. Activity diagrams provide insights into the behavior of the system, emphasizing process flow and logic.

[Activity Diagram](https://drive.google.com/file/d/1hzPOMeXhx_iHLX5nDVmyN57-fu2rObr7/view?usp=sharing)

## 3. Domain Driven Design:

I have made a [Context Diagram](https://drive.google.com/file/d/1xaLQFyUG9PUT4wXm8WZ89wdPQFA-CKCe/view?usp=sharing) for my project manually and also made an [Event Storming Diagram](https://www.mermaidchart.com/raw/e5abad4e-62e8-478c-8d51-6fbd40eebb18?theme=light&version=v0.1&format=svg) via Mermaid.

Adding up on that, the code exhibits elements of DDD, including bounded contexts, entities, value objects, repositories, and services, reflecting a domain-centric approach to hospital management system design.

### Bounded Context:

The HospitalApp class encapsulates core application logic, focusing on patient information management, prescription handling, and user interface initialization.

### Entities and Value Objects:

Patient information fields and prescription data are represented as attributes and encapsulated within the class, serving as entities and value objects, respectively.

### Aggregates:

While not explicitly defined, patient information and prescriptions could form aggregates, with the class orchestrating interactions between them.

### Repositories:

The Database class abstracts database operations, acting as a repository interface and decoupling the application from specific database implementations.

### Services:

Methods within HospitalApp serve as domain services, encapsulating business logic and facilitating interactions between entities, value objects, and repositories.

## 4. Metrics:

To check the metrics of my code, I made use of Codacy. The following are the metrics of my code:


Code Quality: <a href="https://app.codacy.com/gh/AishaFaheem/HospitalManagementSystem/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/1afac9a7ef1a464e927851cd1253d833"/></a>

-Issues: 
![1](https://github.com/AishaFaheem/HospitalManagementSystem/assets/64909342/8792f496-ff3c-4699-bf2d-c9236cc7e7a5)
![2](https://github.com/AishaFaheem/HospitalManagementSystem/assets/64909342/ed153d73-dc2d-4070-9abf-3f93f51c02fb)
![3](https://github.com/AishaFaheem/HospitalManagementSystem/assets/64909342/04879fda-abda-43ae-824f-4aadd8a85002)


-Complexity: 
!(https://github.com/AishaFaheem/HospitalManagementSystem/assets/64909342/f9d35cd4-97f3-4bba-8510-d34b8c487bca)

-Duplication: 

## 5. Clean Code Development:
   
## 6 & 7. Build Management and CI/CD:
## 8. Unit Tests:
## 9. IDE:
## 10. DSL:
## 11. Functional Programming:
