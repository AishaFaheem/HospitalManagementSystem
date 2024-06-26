# HospitalManagementSystem

Hospital Management System is a Project in python created by Aisha Faheem (102579) a Master's Student at BHT studying Data Science.

## 1. Git:

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


### Code Quality: <a href="https://app.codacy.com/gh/AishaFaheem/HospitalManagementSystem/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/1afac9a7ef1a464e927851cd1253d833"/></a>

### Issues: 
![1](https://github.com/AishaFaheem/HospitalManagementSystem/assets/64909342/8792f496-ff3c-4699-bf2d-c9236cc7e7a5)
![2](https://github.com/AishaFaheem/HospitalManagementSystem/assets/64909342/ed153d73-dc2d-4070-9abf-3f93f51c02fb)
![3](https://github.com/AishaFaheem/HospitalManagementSystem/assets/64909342/04879fda-abda-43ae-824f-4aadd8a85002)


### Complexity: 


![1](https://github.com/AishaFaheem/HospitalManagementSystem/assets/64909342/f9d35cd4-97f3-4bba-8510-d34b8c487bca)


### Duplication: 


![1](https://github.com/AishaFaheem/HospitalManagementSystem/assets/64909342/a5b056a1-e0b3-4bb6-b0e2-4fa1a8d11d28)


## 5. Clean Code Development:
To ensure my project is easy to understand, I used standard naming conventions with simple declarations like **create_patient_info_fields()** and **fetch_data()**.

I also made use of the **pylint** library to analyse the code for convention mistakes.


![1](https://github.com/AishaFaheem/HospitalManagementSystem/assets/64909342/c8fe6a93-3ed3-4849-a485-92675d2d5fae)



![2](https://github.com/AishaFaheem/HospitalManagementSystem/assets/64909342/f879bcb0-71af-44f6-ae3a-9d0e737a5e67)



- Here is the regex I used for naming conventions:
^[a-zA-Z_][a-zA-Z0-9_]*$
^: Start of the line
[a-zA-Z_]: Matches any uppercase letter, lowercase letter, or underscore (allows both camelCase and snake_case)
[a-zA-Z0-9_]*: Matches any alphanumeric character or underscore (allows digits after the first character)
$: End of the line

This regular expression ensures that:
- The name starts with a letter or underscore.
- Subsequent characters can be letters, digits, or underscores.
- The name can't start with a digit.
   
## 6 & 7. Advanced Build Management and CI/CD:
I used GitHub Actions in conjunction with Codacy for CI/CD pipeline integration.

Here is the link the yaml file for [Github Actions](https://github.com/AishaFaheem/HospitalManagementSystem/blob/main/.github/workflows/codacy-analysis.yml)

And here is a screenshot of the completed action


![1](https://github.com/AishaFaheem/HospitalManagementSystem/assets/64909342/9cb430e6-727d-4940-b850-9b3526d979a1)


## 8. Unit Tests:
Unit testing for my code is done in the unit_test.py file. The file tests adding and updating patient information. It also checks for invalid information entries.


## 9. IDE:
I opted for Visual Studio Code (VS Code) as my IDE for the Hospital Management System project due to:

### Familiarity: 
Having prior experience with VS Code, I felt comfortable and efficient using it.

### Cross-Platform Compatibility: 
VS Code works seamlessly across different operating systems, ensuring consistency in my development environment.

### Extensive Extensions: 
Its vast library of extensions tailored to various needs, from syntax highlighting to debugging, enhanced my productivity. Extensions like SonarLint which aided me in terms of clean Code Development, Gitpod and Sonarcube.

### Integrated Terminal: 
The integrated terminal eliminated the need to switch between applications, streamlining my workflow.

## 10. Functional Programming:
This code exhibits several aspects of functional programming:

1. Modularity: The code is divided into classes and methods, each responsible for a specific functionality. For example, the HospitalApp class handles GUI initialization, database operations, and button actions, while the Patient class initializes patient data attributes.

2. Pure Functions: Many methods in the HospitalApp class can be considered as pure functions as they rely only on their input arguments and do not modify any external state. For example, the create_patient_info_fields method takes frame as input and generates patient information fields within that frame without modifying any external state.

3. First-class Functions: Functions are treated as first-class citizens. For example, button commands are assigned functions (self.i_prescription, self.i_prescription_data, etc.), and these functions can be passed around as arguments and returned from other functions.

4. Higher-order Functions: The create_buttons method creates buttons dynamically by taking a list of button names and associated functions as input arguments. It then generates buttons with the specified text and command functions.

5. Immutable Data: The data attributes in the Patient class are defined using tk.StringVar(), making them immutable. This ensures that these variables cannot be modified directly, promoting safer data handling practices.

These functional programming aspects contribute to cleaner, more modular, and easier-to-understand code, enhancing readability, maintainability, and reusability.

## 11. Domain Specific Language:
In the project, I implemented Domain Specific Language (DSL) elements to enhance code readability and maintainability. Here's how I integrated DSL:

Clear Abstractions: I wrote the code with clear abstractions concepts like patients, prescriptions, and medical records.

Readable Method Naming: I used meaningful method names that reflect domain actions, making the code self-explanatory and easy to understand. For example, methods like fetch_data() and update_data() easily explain their respective functionalities.

Consistent Naming Conventions: I used consistent naming conventions throughout the code, ensuring clarity and predictability.


