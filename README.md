# TSDIT_CHATBOT

## Introduction

Nowadays, Chatbots have become an indispensable tool for customer service and query resolution. These intelligence systems artificial have stood out for their ability to interact naturally and fluid with users, offering complete and precise responses. Likewise, in the educational context, Chatbots can also play a role. important role in improving the student experience. For example, can be used to provide academic assistance, answer questions about the study plan or administrative processes. Therefore, this project proposes the implementation of a Chatbot through the WhatsApp instant messaging service, whose purpose is to solve the concerns that students may have about the existing procedures for the curricular project of Technology in Data Systematization and Engineering in Telematics.

The design and deployment of the Chatbot will be carried out with a distributed approach, scalable and efficient, ensuring its ability to handle an increase gradual increase in users. To achieve this purpose, the technologies are defined necessary and the Kanban methodology that is precise to meet the objectives established.

It is important for the curricular project, within the context of assistance administrative, have a tool that supports the management of procedures that will benefit both students and administrators, for quick resolution and reliable of the concerns that may arise

## STATE OF ART

4.1. REFERENTIAL FRAMEWORK

The existing knowledge in the literature about Chatbots in the sector Education is very diversified and mostly aims to improve learning of student. It is evident that the technological mediation between the student and the university has improved communication through the use of emerging technologies, student preferences are increasingly demanding, not only in their training process, but in their way of communicating. Comm100 is a global provider of omnichannel digital engagement software. customer service for educational, government and commercial organizations.

Comm100 is a global provider of omnichannel digital engagement software. customer service for educational, government and commercial organizations. Comm100 announced the results of a new survey on April 11, 2023 conducted to North American higher education students about their communication preferences during the registration and admission processes. A Key survey finding revealed that digital communication with schools is the most important support factor for future students, these The results emphasize once again the need for admissions adopt digital channels to meet support expectations of the students. The survey revealed the overwhelming openness of futures students to use Chatbots, with 95% of students at least somewhat open to receive support from a Chatbot [2].

With respect to this study, the potential of Chatbots in a only process that is admissions, however, extending the scope of a Chatbot beyond a process in the student is a challenge, but the literature has revealed some success stories. Authors Trung Thanh Nguyen and Anh Duc Le designed and implemented a Chatbot in the office admissions from the National University of Economics in Vietnam which was integrated into the university's Facebook Fanpage resulting in availability of responses in real time 24 hours a day with effective of 90.29% in a sample of 50,000 questions.

To achieve this result, the authors implemented a series of modeling models. deep learning natively integrated into the Rasa Framework [3] which is a powerful set of libraries in the Python programming language specialized in conversational AI. While it is true that the Rasa Framework is a great open source tool your learning curve can be a challenge, in addition to its integration with external systems such as APIs and others services has a certain complexity that is not convenient in an environment of production.

A group of researchers from the Institute of Engineering and Technology made a Complete analysis of the way Chatbots are currently developed extracting the best attributes, qualities, patterns, functional characteristics and quality when building a Chatbots that can achieve high rates of customer satisfaction.

The research is based mainly on surveys and what was found In the literature review, a series of aspects are defined in the research to consider in the design and development of a Chatbot, Initially the article suggests that the developer must have knowledge of markup language AI, Pattern Matching, Chat Script, Parsing, Databases and Strings Markov.

The article also proposes that the main reference point for constructing a Chatbot can be started from the ISO 9126-1 Quality Model which emphasizes six known key features such as functionality, reliability, ease of use, efficiency, ease of maintenance and portability that are based on the capacity to meet anticipated and unforeseen needs [4].

It was also found that there are seven elements that contribute to the design and development of the Chatbot increasingly similar to a human agent these elements correspond to technical functionalities, efficiency, effectiveness, humanistic, ethics, technical satisfaction and accessibility. This research provides as a theoretical and architectural reference in the construction of the assistant intelligent academic.

Simon Prananta Barus and Evalien Surijati implemented a Chatbot in the University of Matana in Indonesia in the face of the challenges brought by the pandemic, this Chatbot basically focused on frequently asked questions (FAQs) of the library in order to guarantee online services 24/7. The development of Chatbot was made in a minimalist way through the Dialogflow platform from Google that makes it easy to design and integrate Chatbot into other applications, This platform runs in the cloud and allows the creation of models of Natural Language Understanding (NLU) which is the basis for developing Chatbot [5].

Likewise, the technical complexity of this implementation was mainly due to in the design of the NLP model of the Chatbot where the design of a conversation where agents, intentions, entities, contexts, events, compliance and integration for the development of a model suitable. Dialogflow beyond a tool is a cloud service classified as a SaaS-type solution, although it is true that it can simplify and make sufficient abstractions in the development must be considered and analyzed its rate and costs of use.

So far the analyzes carried out show some technical and operational aspects. quality that is worth taking into account, but the way to encompass the problem remains a challenge. A research carried out at the Inter-American School of Library Science at the University of Antioquia in Colombia proposes a framework structured methodological based on Design Thinking for the design of virtual assistants (Chatbots). This framework is made up of the following stages: empathize, define, ideate, prototype and evaluate, which in turn include a series of techniques and methodological instruments used with a focus qualitative, exploratory and descriptive scope which favored the recognition of the actors involved in the virtual education processes, these actors were essential to generate a state of empathy in the team research [6]. This research was strongly supported by surveys where it is evident that among the students' preferences are: Web and mobile interoperability (via WhatsApp), using phrases short and simple, without technicalities, Hybrid (with default options, but with the possibility of asking) Textual communication based on FAQ (questions frequent).

Conversational artificial intelligence has had an incremental boom since At the end of 2022, after the arrival of chatGTP, it was evident that this application I reached 100 million monthly active users in just 2 months something that it took Instagram two and a half years, setting a record like the fastest growing application in history [7].

The core of an application of this magnitude works through a model of large language (LLM) which is a type of model based on neural networks which is trained on massive amounts of text data to understand and generate human language, chatGTP 3.5 LLM has 175 billion parameters spread over 96 layers in the neural network which makes it one of the largest deep learning models ever created [8].

ChatGTP is currently the greatest exponent of Chatbot technologies to study Its architecture and integration modes are novel and can provide knowledge cutting-edge research.

### 4.2. THEORETICAL FRAMEWORK

4.2.1. Chatbots.

A chatbot is a software designed to simulate conversations with human users,
usually through messaging applications, such as

Facebook Messenger, WhatsApp or Telegram. A chatbot usually employs natural language processing (NLP) algorithms to interpret user messages and provide automated responses. The purpose of a chatbot is to benefit from automating a wide range of tasks ranging from customer service and sales to entertainment and personal assistance. They can help organizations automate routine tasks, reduce response times and improve customer satisfaction.

A chatbot can be rule-based or artificial intelligence-based. A rule-based chatbot follows a predefined set of rules and can only respond to specific keywords or phrases. An AI-based chatbot, on the other hand, employs machine learning algorithms to learn from previous interactions and improve its responses over time. An AI-based chatbot can also understand natural language inputs, making it more flexible and adaptable than a rule-based chatbot.

The ideal of a chatbot is to ensure a seamless, human-like user experience. Chatbots are currently the most popular because they can handle a variety of inputs, understand context, and provide relevant and helpful responses. Despite the challenges, chatbots have become increasingly popular in recent years, and many organizations are adopting them to improve their customer service and communication channels.

4.2.2. How a chatbot works.

To create chatbots, which replicate natural language conversations with users through messaging apps, websites, mobile apps, and phones, AI software is typically used. This application is essential as knowledge is pre-stored, allowing for self-learning and restoration of knowledge through human or online resources. As the application of the system takes the form of a Chatbot, it responds to user requests using the question-answer protocol [9].

4.2.3. Technological advancements and related trends.

• Conversational AI. 

Conversational AI makes it possible to understand human language and respond accordingly. In other words, conversational AI allows a Chatbot to respond to you naturally. 
 
It uses voice recognition and machine learning to understand what people are saying, how they are feeling, what the context of the conversation is, and how they can respond appropriately. Furthermore, it supports many communication channels (including voice, text, and video) and is context-aware, allowing it to understand complex requests involving multiple inputs/outputs. The critical difference between Chatbots and Conversational AI is that the former is a computer program, while the latter is a type of technology. [10]

• Multimodal inputs.

Multimodal AI is in the field of natural language dialogue systems. Multimodal models can use visual and linguistic cues to generate more human-like conversational responses. For example, a chatbot that understands the visual context of the conversation can generate more appropriate responses that consider not only the text of the conversation but also the images or videos that are shared. [11] Many chatbot platforms now support multimodal inputs as a standard feature. Multimodal chatbots are especially useful for complex interactions where multiple types of inputs are required, such as making a hotel reservation where the user may want to see photos of the rooms, ask questions about amenities, and check availability by voice or text.

Integration with other technologies.

Chatbots are being integrated with other technologies, such as machine learning, IoT, and AR/VR, to provide more complete solutions. For example, Chatbots can be integrated with machine learning algorithms to provide predictive analytics and personalized recommendations. Integration can also be defined as the problem of integrating conversational capabilities into existing software systems. Doing so may require developing a conversational agent that starts with the data, application logic, or graphical UI of the system to support natural language conversations leveraging artificial intelligence (AI) or more traditional software engineering approaches.[12]

•Ethics, privacy, and security. Chatbots are increasingly popular artificial communication systems and not all of their security questions are clearly resolved. People use Chatbots for shopping assistance, banking communication, food delivery, healthcare, automobiles, and many other actions. However, it brings an additional security risk and creates serious security challenges that need to be managed.

Modern Chatbots are no longer rule-based models, but rather employ modern natural language and machine learning techniques. Such techniques learn from a conversation, which may contain personal information [13] that must be treated appropriately, for which ethical and data handling policy rules are provided. Many Chatbots operate on a social/messaging platform, which has its terms and conditions regarding data handling.

•Evaluating the performance of Chatbot systems. Chatbots are generally designed to serve specific purposes. 

For example, customer service Chatbots are designed specifically to meet the needs of customers seeking help, while conversational Chatbots are designed to have interactive communications with users. These Chatbots are designed and built based on the domain in which they will operate. Chatbots tend to fail when presented with situations and inputs that they are not familiar with. This may include ambiguous

statements, grammatically incorrect phrases, and statements outside the bot's
operational domain. [14]

Chatbot performance is often measured by its similarity to that of a human. Therefore, it is imperative that Chatbots operate and interact in a desirable manner. Organizations must rigorously test and verify their Chatbot before releasing it to production.

Current Chatbot testing approaches either monitor the Chatbot output to assess performance or study the internal functionality of the Chatbot and the various algorithms involved.

4.2.4. Rule-based Chatbots.

Rule-based Chatbots rely on a list of simple, predefined queries and possible resulting responses. It does not need any machine learning approach and language processing is not mandatory. They are intended for simple queries and may fail in more complicated questions as they cannot produce their own answers.

(Jagdish Singh 2019) Proposed a rule-based Chatbot for students at Asia Pacific University (APU) to answer their queries from their administrative offices. The designed Chatbot allows end users to view information and interact with the Chatbot regarding their queries. The developed system was compatible with the bot's Facebook application page to access via a laptop or computing devices. [15]

4.2.5. Hybrid Chatbots. 

A Hybrid Chatbot is a combination of rule-based and AI-powered Chatbots. They use pre-programmed rules to handle simple tasks and machine learning algorithms to handle more complex tasks. This allows the chatbot to provide the best of both worlds: consistent responses for simple tasks and personalized responses for complex tasks, providing an improved user experience that seamlessly blends automation with human assistance. [16]

4.2.6. Transactional Chatbots.

A transactional chatbot acts as an agent and interacts with external systems to carry out a specific action. Thus, a transactional chatbot differs from the more common bots, also called informative or conversational chatbots, in that its objective is to automate a transaction and simplify the user experience by providing a suitable and fast channel for a specific objective. It is optimized to execute a certain number of specialized processes that eliminate the need to speak with an expert or to use more complex interfaces such as mobile applications or websites.

Transactional chatbots can be implemented in various sectors, such as banking, insurance or e-commerce. In the financial sector, for example, they can automate simple tasks that would otherwise be carried out by a banker over the phone, such as verifying your identity, blocking a stolen credit card, informing you of the hours of nearby offices or confirming an issued transfer. [17]

4.2.7. Self-learning Chatbot.

A self-learning Chatbot understands what the user wants and consequently saves the users effort to complete a daily task by communicating with the second Chatbot on behalf of the user. It tries to overcome the lack of knowledge of the user's preferences and requirements in making decisions on behalf of the user.
Both the server and the chatbot interact with each other and work as if it were a normal conversation and the resulting output is returned to the user. This leads to reduced to sometimes zero input from the user while adapting the user's preferences and tastes. User preferences play a vital role in the conversation. The more the user interacts with the system, the more it trains the system to understand the user's preferences. Automating the communication of a Chatbot in such a way that it communicates on behalf of human preferences considering the preferences is what has been proven as a system. By

self-learning, the system adapts and takes into account all the user's preferences and learns more and more about the user over time. [18]

4.2.8. Natural Language Processing.

Natural language processing (NLP) is a field of computer science, artificial intelligence, and computational linguistics that deals with the interactions between computers and human (natural) languages. It focuses on how to program computers to process and analyze large amounts of natural language data.

Natural language processing (NLP) is experiencing rapid growth as its theories and methods are increasingly implemented in a wide range of different fields. In the humanities, work on corpora is gaining increasing prominence. Within industry, people need NLP for market analysis, web software development, to name a few examples. For this reason, it is important for many people to have some working knowledge of NLP. [19]

The relationship between Chatbots and NLP lies in the fact that Chatbots have become an increasingly popular means of customer service and support for businesses. By using Chatbots, businesses can automate customer interactions, provide 24/7 support, and reduce the workload of human customer service representatives. However, for Chatbots to be effective, they must be able to understand and respond to users' natural language input, which requires sophisticated NLP algorithms.

**4.2.9. Python programming language.**

It is a multiplatform programming language, very popular in the industry. Being a dynamic language, it allows testing portions of code as they are generated, optimizing the programming and debugging time of the written code. Created by Guido van Rossum in 1989. This language is considered simple and easy to learn, granting the programmer virtues such as automatic memory management, simple reading or writing operations. In which it differs from other programming languages

programming. Another advantage is its flexibility, since it stores a large amount of data of various types without having to declare each type of data, it is an ordered, readable, and portable language. [20]

**4.2.10. Microservice-API.**

The microservices architectural style is an approach to develop a single application as a set of small services, each running in its own process and communicating with lightweight mechanisms, often an HTTP resource API. These services are based on business capabilities and are implemented independently by fully automated deployment machinery. There is a minimum indispensable centralized management of these services, which can be written in different programming languages ​​and use different data storage technologies. [21]

**4.2.11. Cloud infrastructure.**

Cloud infrastructure is based on virtualization to separate resources from physical hardware and group them into clouds. Automation software and management tools distribute these resources and prepare new environments so that users can access the elements they need at any time. This allows for greater flexibility and scalability in managing computing resources. Hardware, virtualization, storage, and network components work together to provide a complete cloud computing solution.

Cloud infrastructure can refer to both an entire cloud computing system and the individual technologies that compose it.

• Elements of cloud infrastructure. Hardware Cloud infrastructure requires physical hardware to operate, which can include a network of hardware systems distributed across different geographic locations. This network can include network equipment such as switches, routers, firewalls, and load balancers, as well as storage arrays, backup devices, and servers. o Virtualization Virtualization is a technology that separates IT functions and services from the physical hardware system. A hypervisor, a specialized software, controls the physical hardware and abstracts the machine's resources, such as memory, computing power, and storage. Once virtual resources are assigned to centralized pools, they are considered clouds. 

Virtualization is essential for creating and managing cloud infrastructure, as it allows for the creation of virtual environments from a single set of physical resources, allowing for greater efficiency and scalability. o Storage Storage management in cloud infrastructure is essential to ensure data integrity and availability. Data is stored on storage arrays and is regularly backed up to protect against failure or loss of information. With virtualization, storage is abstracted from the hard are and offered to users in the cloud as a shared resource. 

This allows for greater flexibility in managing storage resources, as drives can be added or removed as needed and respond to changes without having to add separate storage servers. o Network Cloud infrastructure includes a physical network made up of cables, switches, routers, and other equipment, which is used to create virtual networks. The traditional cloud network setup consists of multiple subnetworks with different levels of control, and virtual local area networks (VLANs) can be created and static or dynamic addresses assigned to network resources. Users can access cloud resources through a network, either the Internet or an Intranet, allowing them to access cloud applications or services remotely. The network also allows users to interconnect multiple clouds, giving them the flexibility to choose different cloud providers or integrate their own private and public cloud solutions. Cloud infrastructure consists of the same basic elements, whether it is a public, private, or hybrid cloud. To work with any type of Cloud Computing, a cloud infrastructure is required, which can be created by yourself or using a public cloud through a cloud service provider.

•Comparison between infrastructure and cloud architecture:

Cloud architecture refers to the way different technologies are combined to create cloud computing environments, while infrastructure is the set of tools needed to design the cloud. Architecture is like a technical blueprint that indicates how cloud elements such as hardware, virtual resources, networks, operating systems, etc. should be connected. [22]

***4.2.12. Types of Cloud Computing as a Service. [23]***

*** IAAS***

Infrastructure as a Service (IaaS) is a cloud service model in which a third-party service provider offers IT infrastructure such as storage, servers, and virtualization to users who pay for their consumption. The provider manages the resources, and the user is responsible for operating systems, data, applications, and runtimes. IaaS offers flexibility to acquire and adapt the necessary elements and is an affordable option since it does not generate maintenance costs.

Some disadvantages of IaaS are possible security problems of the provider, service reliability, and multi-tenant systems where the provider must share infrastructure resources with several customers. Some public cloud providers that offer IaaS may include AWS, Microsoft Azure, and Google Cloud.

***PAAS***
Platform as a Service (PaaS) is a type of cloud service model used to provide users with an online application development and running environment. In the PaaS model, the cloud service provider hosts the platform and software on its infrastructure, allowing users to develop and run applications without having to worry about managing the infrastructure.

PaaS is an especially useful solution for developers and programmers, as it provides them with a complete environment to write and manage applications, and allows them to focus on developing the application itself, rather than having to worry about maintaining and managing the infrastructure. In addition, PaaS offers the ability to customize and design their web-based applications using built-in software elements. Examples of PaaS include AWS Elastic Beanstalk, Heroku, and Red Hat OpenShift.

***4.2.13. Digital transformation.***

Digital transformation refers to the process of incorporating digital technologies into all areas of an organization to change the way value is delivered to customers. Digital transformation involves cultural and operational changes, and can include building digital solutions, moving to cloud computing, and adopting smart sensors to reduce operating costs. The goal is to better adapt to changing customer needs and improve efficiency in the organization. Digital transformation is important for organizations because it allows them to stay competitive in an ever-changing technological environment. 

Digital transformation initiatives can improve productivity, customer experience, and reduce operational costs. Emerging technologies, such as artificial intelligence and cloud services, can save time and improve efficiency in business processes. Digital transformation can significantly reduce operational costs by eliminating or replacing specific workflows, reducing spending on expensive infrastructure and equipment, and automating tasks with technologies such as smart sensors and machine learning. Digital transformation goes beyond digitizing processes and workflows. It refers to the integration of digital technologies to fundamentally change the way products or services are delivered, customers are interacted with, and business processes are operated. Digital transformation involves profound cultural and operational changes, such as reorganizing teams and adopting new ways of working, to adapt to changing market and customer needs. Digital transformation is about using technology to reinvent the business and create new growth opportunities.

***Digital transformation and Chatbot:***

As mentioned, digital transformation is a complex process that involves a re-evaluation and reorganization of business processes to make the most of emerging technologies. In this context, Chatbots have emerged as a key tool to assist in the digital transformation process of organizations. The main way Chatbots help in the digital transformation process of an organization is by automating tasks and processes. Chatbots can be integrated into different business systems and applications to provide quick and accurate answers to frequently asked questions and perform repetitive tasks, thereby reducing the workload on employees and allowing a focus on more strategic tasks.

In addition, Chatbots can significantly improve the customer experience by providing instant and personalized customer support. Customers can interact with a Chatbot at any time of the day and get accurate and fast answers to their questions.

Another benefit of Chatbots is data collection. Chatbots can track and analyze customer interactions, allowing organizations to better understand customer needs and preferences and continuously improve their services and products. Additionally, chatbots can be integrated with data analytics and machine learning tools to identify patterns and trends in the data collected, which can help in business decision-making.

TECHNOLOGICAL SOLUTION

The technological solution aims to automate the management of frequently asked questions and their corresponding answers within the curricular project of Data Systematization Technology and Telematics Engineering. This will be achieved through the integration of a Chatbot into the WhatsApp instant messaging platform. The main goal is to alleviate the workload of the project's administrative staff, optimizing student service processes and offering efficient responses in real time.

To achieve this result, a series of specific objectives were established that define each procedure or component of the Chatbot implementation. The technological solution is detailed below by specific objective.

• Initially, an analysis must be carried out, where the scope of the processes that the Chatbot will cover will be explored and delimited through the automation of responses. This analysis must be aligned and documented according to the methodological flow used in the development of the project, as well as the research of the technologies that meet the requirements and allow the implementation.

• Design and develop the software components necessary to integrate the Chatbot into the WhatsApp instant messaging service. This solution will be implemented in a microservices architecture exposed in APIs made in the Python programming language, which must have libraries specialized in artificial intelligence techniques.

• Design and implement a data architecture that can store 

conversations and the Core of the response processing engine in an efficient manner, considering that the response processing engine will work adequately in a relational database such as PostgreSQL, on the other hand, considering the excess of write and read operations such as conversations, a non-relational approach such as Mongodb can be opted.

• Train the response processing model using as an input source a catalog of rules defined from an analysis of the requirements survey. This input source must have a specific format that can be synchronized with the semantic and syntactical patterns of the natural language processing (NLP) technique used.

• Deploying the Chatbot along with its components in a pre-production environment will be done through a cloud infrastructure provider that offers the benefits of an infrastructure as a service (IAAS) or platform as a service (PAAS) which make an abstraction of underlying network infrastructure configurations, such as provisioning or virtualization, thus allowing greater emphasis on the project objectives.

• When selecting the cloud infrastructure provider, the costs and the catalog of services offered by layer (TIER) will be taken into account. Many cloud providers offer a free TIER which has limitations regarding services and storage, however, for this prototype it is likely that an initial investment must be made.

• In the functional testing phase, the Chatbot will be evaluated in a scenario of questions with different conversational flows. In case there are corrections and improvements, the project will have a continuous integration and continuous deployment flow (CI/CD).
It is important to highlight that this series of objectives will be carried out in a structured manner according to an agile methodology.


7.1. TECHNOLOGIES FOR THE DEVELOPMENT OF THE PROJECT

Below are the technologies that were used in the development of the project:

• RASA: Rasa is an open source platform for the development of Chatbots and virtual assistants powered by conversational artificial intelligence. As elements to highlight, Rasa offers an intuitive user interface that facilitates the creation of the Chatbot, can be scaled to support large volumes in conversations, and makes use of machine learning models that ensure that the Chatbot can understand and respond to natural language accurately. [28] 

• Python Virtual Environments: A Python virtual environment (venv) is a directory that contains a stand-alone installation of Python, along with the libraries and dependencies that a specific project needs. It is like having a separate copy of Python for the development of the Chatbot. 

The benefits of using Virtual Environments for developing the Chatbot are that it has its own set of dependencies, which avoids conflicts between other different projects, it guarantees operation in any environment with the correct Python configuration and libraries, which facilitates project management. [29]

• Twilio: It is a platform that provides communication tools so that phone call functionalities, text messages (SMS), chat, email and other forms of communication can be incorporated into applications and websites. Twilio acts as an intermediary between any application and cellular telephone networks and messaging service providers.

This is a de facto tool that is suggested by Rasa for handling communications with WhatsApp, the Twilio platform offers an integration with the WhatsApp Business API, which allows you to take advantage of its advantages to improve communication, which is a fundamental part of Chatbot development. [30]

• Mongo DB: Mongo DB is an open source, document-oriented NoSQL database written in C++. Unlike traditional relational databases that store information in tables with structured rows and columns, Mongo DB uses a flexible document model based on JSON (JavaScript Object Notation).
In the development of the Chatbot it is ideal for storing dynamic and constantly changing data such as the conversational flow and the history record of conversations by storing them in JSON format. Due to its flexibility and scalability it allows fluid analysis and integration with Frameworks such as Rasa in the development and analysis of conversations. [31] 

•Postgres: PostgreSQL is an open source, robust and scalable relational database management system (RDBMS), ideal for storing business rules and knowledge bases for the Chatbot. It allows you to organize information in tables with well-defined relationships, guarantees the accuracy and consistency of the information through validation rules and restrictions. It provides high performance for reading and writing data, allowing fast and efficient access to business rules and the knowledge base. [32] •Docker: It is an open source platform that facilitates the development, execution and deployment of applications, such as the Chatbot, through the use of containers.

When developing the Chatbot, Docker provides an isolated environment where the application can be developed and tested, along with all the necessary dependencies and configurations. You can ensure that the Chatbot works in various environments, making it easy to integrate and deploy on the WhatsApp messaging platform. [33]

• BERT: (Bidirectional Encoder Representations from), is a machine learning technique used to train natural language models (NLP). BERT is based on the Transformer architecture, which allows for bidirectional text processing, that is, taking into account the full context of a sentence.
In order to improve the accuracy of the Chatbot, this AI model will be used to train the Chatbot. [34] 

• DIETClassifier: (Dual Intent and Entity Transformer), is a multi-task natural language processing (NLP) model developed by Rasa NLU. Its main function lies in the classification of intents and the extraction of entities in dialog applications. This model is especially useful for empowering the Chatbot, allowing it to understand and respond naturally to user queries. Intent classification is crucial for identifying the purpose or goal of a user statement. [35]

• Django: It is a free and open source web development framework based on Python, which provides a predefined structure and tools to build web applications faster and more efficiently. In the development of the Chatbot, based on Django and REST Framework, it is a versatile tool, it provides flexibility to support the rules and allows the Chatbot to be adapted to different needs and scenarios. [36]

• Ngrok: It is a tool that allows a local server to be exposed to the Internet in a secure and temporary way. It works by creating a proxy server in the cloud, creates a secure tunnel between the computer and the server, then provides a unique URL that can be used to access a local server from any web browser or application.

In the development of the Chatbot, this tool will be used to expose the Chatbot's messaging server to the Internet for the testing phase. [37]

• AWS: Amazon Web Services, it is considered the most complete and used cloud platform in the world; Instead of having physical servers to store data and run applications, these resources can be rented. AWS offers a large number of comprehensive services ranging from basic infrastructure to emerging technologies such as AI and machine learning, which is precisely what this project is about. AWS is a tool that will facilitate the pre-production deployment of the Chatbot, since the application will be packaged in a Docker container and AWS has this service. [38]

In project management, the Kanban methodology has emerged as a tool that offers a complete and effective perspective for the successful development and execution of projects. By providing a transparent and detailed view of the work process, Kanban is presented as a valuable solution for managing tasks, optimizing time and achieving goals efficiently.

The Kanban methodology is a project management tool and is a great option for project development. This methodology offers a transparent way to manage tasks and visualize the process of carrying them out. This methodology helps prioritize tasks and manage time efficiently.
 
The first step in implementing the Kanban methodology is to define the  project workflow. To do this, a board must be created that is accessible by all team members. Each column on the board must correspond to a specific state of the task flow, from start to finish. It is important that the board has as many columns as the states that a task goes through,

so that you can know the status of each activity.

One of the peculiarities of the Kanban board is that it is continuous, unlike Scrum. As you move forward, new tasks accumulate in the initial section, and in regular meetings they are prioritized and placed in the section that is deemed appropriate. This board can be specific for a specific project or generic, depending on the needs of the team.

The second step to implement the Kanban methodology is to visualize the phases of the production cycle. To do this, the work is divided into different parts, which speeds up the production process. Each of these parts is written on a post-it and stuck on the board, in the corresponding phase. These post-its contain the basic information so that the team quickly knows the total workload that it entails. In addition, photos can be used to assign responsibilities, as well as cards with different shapes to put observations or indicate blockages.

The goal of the visualization is to make as clear as possible the work to be done, the tasks assigned to each team member, the priorities and the assigned goal. This helps students to have a clear idea of ​​what is expected of them and to prioritize tasks based on importance and urgency.

Finally, the third step to implement the Kanban methodology in the project is to apply the motto "Stop Starting, Start Finishing." This means that work that is in progress is prioritized instead of starting new tasks. Instead of jumping from one task to another, the focus should be on finishing tasks that are already in progress before moving on to new tasks. This helps to avoid overwork and the accumulation of pending tasks. 

The Kanban methodology turns out to be an effective tool to manage degree projects efficiently and transparently. This methodology can be applied to prioritize tasks, visualize the production process, and avoid
overwork. 

With proper implementation, the Kanban methodology can help successfully complete the project that has been planned.[39] Workflow for project development with the Kanban methodology

7.2.2. Workflow for project development using the Kanban methodology

Phase 1: Planning

• Proposed solution: Define the Chatbot solution to be developed, including its objectives and components. Chatbot requirements: Specify the functionalities and features of the Chatbot, including the scope. Processes to be covered: Identify the processes or procedures that will be automated with the Chatbot. Conversational flow: Design the Chatbot conversation flow.

### Phase 2: Design

• Application architecture: Define the Chatbot system architecture, including the different components and their interconnection. Process modeling: Document the processes or procedures that will be automated with the Chatbot.

Phase 3: Development

### Phase I: Development of the Chatbot Core o Development environment: 

Set up the development environment for the Chatbot. o NLP model training: Train the Chatbot's artificial intelligence model to understand natural language. o Input/output protocols: Select and implement the data input and output protocols for the Chatbot.

### Phase II: Development of WhatsApp integration middleware

Communication protocol and channel: Select and implement the communication protocol for WhatsApp integration. o Conversation rules management system: Design and develop an application for managing conversation rules. o Conversation databases: Design and develop the databases to store the Chatbot conversations and the neural network training data. o Data Neural Network Training: Define information processing with model training

### Phase 4: Functional Testing

• Functional testing: Perform unit tests to ensure consistency and fluidity in conversations.
• Training tests: Perform tests to evaluate the Chatbot's performance.

### Phase 5: Implementation

• Cloud Provider: Select a public cloud provider for Chatbot deployment.
• Service Deployment: Deploy Chatbot services and obtain corresponding domains.
• Technology Architecture: Define the technology architecture for Chatbot deployment. 
• Documentation: Build the Chatbot's technical and functional manual.

## 7.4. 

I. PROJECT DEVELOPMENT

Planning Phase.

a. Proposed solution.

The proposed technological solution for the Chatbot aims to automate the management of frequently asked questions and their corresponding answers within the curricular project of Data Systematization Technology and Telematics Engineering. This will be achieved through the integration of a Chatbot into the WhatsApp instant messaging platform. The solution is composed of the following components:

✓ Scope analysis: An analysis will be carried out to define the functions and requirements of the Chatbot, in addition to delimiting the scope of the processes that will be automated by the Chatbot. 
✓ Design and implementation of software components: The software components necessary to integrate the Chatbot into WhatsApp will be designed and developed. These components will be implemented in a microservices architecture exposed in APIS made in the Python programming language.
✓ Data architecture: A data architecture will be designed and implemented that can store conversations and the Core of the response processing engine efficiently. The response processing engine will work properly in a relational database such as PostgreSQL, but a non-relational database such as Mongodb can be chosen for conversations.
✓ Response processing model training: The response processing model will be trained using as an input source a catalog of rules defined from an analysis of the requirements gathering. This input source must have a specific format that can be synchronized with the semantic and syntactical patterns of the NLP technique used.
✓ Functional tests: The Chatbot will be evaluated in a scenario of questions with different users. In case there are corrections and improvements, a continuous integration and continuous deployment flow (CI/CD) will be used in accordance with DevOps best practices.
✓ Deployment in a pre-production environment: The Chatbot and its components will be deployed in an environment through a cloud infrastructure provider. A provider that offers the benefits of an infrastructure as a service (IAAS) or platform as a service (PAAS) will be used, which will allow the generation of network infrastructure configurations.

### b. Define functions and requirements of the Chatbot.

The main function of the Chatbot is to provide information and assistance to the user automatically, with content that is understandable in the university context. Within the requirements, it must be taken into account that the end users of the Chatbot will mainly be students, teachers and administrative staff.

The current scope of the Chatbot is limited to the internal procedures of the university, but it is contemplated that in the future it may be used by external personnel. Therefore, it is important to define the processes that will be 

covered in the Chatbot, taking into account the current needs of these users.

c. Processes that will be covered with the Chatbot.
The content that will be used in the Chatbot is important, so the procedures associated with Data Systematization Technology1 will be taken into account, which in turn are the same for telematics engineering:
Validation request Cancellation of subjects Request for NO renewal of registration Request for voluntary withdrawal Grade sheets Study certificates, programmatic content (Syllabus), good conduct Formats Projects and Preliminary Projects - Schedules Format for adding and canceling subjects Deepening mode Completion of subjects Saber T and T exam Graduation ceremony 


Application Architecture.

In the design phase, it is essential to structure the Chatbot architecture where each of its components must be identified and defined. The Rasa Open Source tool suite will be used for the creation, operation and training of the model. The components include Rasa SDK, Rasa Core and Rasa NLU. For the Tracker Store, Mongo DB will be implemented to save the flow and history of conversations, so the MongoTrackerStore file must be used. For the storage of training data and trained models, it will be done in the Filesystem. The main components in the architecture are:

•Natural language understanding (NLU) – NLU Pipeline, which is responsible for interpreting the user's intention from the natural language that he uses.

•Dialog management – ​​Dialogue Policies, which is responsible for maintaining a coherent conversational flow for the user.

Figure 10: Proposed Chatbot Prototype Architecture.
Based on: https://learning.rasa.com/conversational-ai-with-rasa/website-integration/

b. Process Modeling. 

In the planning phase in item c. Processes to be covered with the Chatbot, the processes to be implemented for the development of the Chatbot were defined, aligned with the statement of the problem, a joint interview of data systematization technology and telematics engineering is developed.

The objective of the interview is to document and analyze the process of managing procedures that are currently handled by coordination and thus be able to identify the areas of improvement for the attention of the same. This will help improve the efficiency and effectiveness of the process, as well as the experience of the end user who are the students. In general, the entire process is covered, from the reception of the application to the final response for the student, so the following scope is determined in the resolution of frequently asked questions about procedures:

• Guidance to students on the processes to follow to resolve their concerns.

• Provide updated information on the documentation required for each procedure. dates, requirements, and During the interview, the most relevant points to take into account in the development of the Chatbot were identified:

• It must be initially taken into account that the curricular project has grown, there are more students and the same people who attend to the requests. The scope is justified due to the number of requests. •As a consequence of the pandemic, students want an immediate response, however, the capacity is not sufficient since not only requests from the curricular project are attended to but also from other departments. 

• For the professional and administrative support assistant of the curricular project, the Chatbot proposal is interesting, according to what is published on the procedures page and taking this information as a base is important. Because students do not read, in the implementation of the Chatbot there should not be much text, that is, the questions and answers should be very clear and concise.

•The coordination sends communications to the students via email, for example, the schedules, but despite having the information in the email, the students do not read it, consequently, they cause loss of time for the professional and administrative support assistant, since information that the students already have must be repeated. The Chatbot would support the students to have faster access to the information.

• To update the Chatbot information, an administrator profile must be established, since modifications must be made annually, such as the dates of the preliminary project schedules, the financial values, and who and how could configure it. There would be a rules engine, the Chatbot that will be built is based on artificial intelligence techniques, the Framework that will be used makes sufficient abstractions so that anyone with basic programming knowledge can update the rules and their responses.

• Returning to the main scope of the Chatbot, such as the resolution of frequently asked questions, many students might think that they can do a complete procedure, such as canceling a subject. But this is a procedure that involves sending documentation and receiving a response to the process, it is a process that must be executed step by step. But for this type of process it is not covered by the Chatbot, however, the Chatbot will have the necessary information so that the student can ask all the possible questions regarding that process.

• The resolution of queries with extensive processes where documentation validations and the like must be done, is an administrative issue and could not be within the scope of the Chatbot, however, the objective is to handle all those frequently asked questions by providing the necessary guidelines so that the student can carry out the procedure. •Returning to the lack of reading of the students, they sometimes confuse the study certificates with the grade certificate, if a deposit must be made, for example, the students only focus on the price, but do not read that in addition to the deposit support, the email must be sent to the academic secretary but they do not do it. The response has to be punctual, it cannot be done with the totality of the processes because there are processes that are complex, for example, the process of the completed degrees.

• As a fundamental part for the Chatbot, and based on the previous points, a knowledge base of all these procedures must be created, identifying if there is any other process that requires some adjustment or some update. It should be one of the great milestones of the Chatbot, to configure the parameters and rules. To update these rules each semester, the administrator in charge at the beginning of the semester, each time the academic calendar is established, updates the rules from a simple, intuitive and easy-to-use user application. •The professional and administrative support assistant will share the templates of how emails are currently being answered, and use them as a basis for building the

responses to the procedures. The text of the responses should not be too extensive. Within the information gathering, the processes to be taken into account in the management of procedures in the Chatbot were identified:

• Receiving requests: 

o The student will initiate the interaction with the Chatbot through a text message or a query. o The Chatbot asks the student for the information necessary to carry out the procedure.

o The Chatbot identifies the type of procedure that the student is requesting. o The Chatbot validates the information provided by the student. If the question emphasizes a previously configured procedure, the Chatbot proceeds to give a response; if the information is incorrect, the Chatbot asks the student to correct the query.

• Guide:

o The Chatbot provides the student with instructions on how to carry out the procedure for which he or she asked. o The Chatbot can direct the student to additional resources, such as web pages or information documents. 

• Considerations:

o Develop the Chatbot prototype that includes the basic processes of procedures. o The Chatbot must be able to learn and adapt to the questions and requests of the students. o It is important to establish a management plan to keep the Chatbot updated and functional. o Evaluate the prototype to identify areas of improvement.

• Additional resources:

7.1. TECHNOLOGIES FOR PROJECT DEVELOPMENT

The technologies used in the development of the project are listed below:

• RASA: Rasa is an open-source platform for the development of chatbots and virtual assistants powered by conversational artificial intelligence.
Noteworthy elements include Rasa offering an intuitive user interface that facilitates chatbot creation, scalability to support large conversation volumes, and the use of machine learning models that ensure the chatbot can accurately understand and respond to natural language. [28]

• Python Virtual Environments: A Python virtual environment (venv) is a directory that contains a standalone installation of Python, along with the libraries and dependencies required by a specific project. It is like having a separate copy of Python for chatbot development. The benefits of using Virtual Environments for chatbot development include the fact that it has its own set of dependencies, which avoids conflicts between other projects. It guarantees operation in any environment with the correct Python configuration and libraries, which facilitates project management. [29]

• Twilio: This is a platform that provides communication tools so that phone calls, text messages (SMS), chat, email, and other forms of communication can be incorporated into applications and websites. Twilio acts as an intermediary between any application and cellular telephone networks and messaging service providers. This is a de facto tool suggested by Rasa for managing communications with WhatsApp. The Twilio platform offers integration with the WhatsApp Business API, allowing users to leverage its benefits to improve communication, which is a fundamental part of chatbot development. [30]

• Mongo DB: Mongo DB is an open-source, document-oriented NoSQL database written in C++. Unlike traditional relational databases that store information in tables with structured rows and columns, Mongo DB uses a flexible document model based on JSON (JavaScript Object Notation).
In chatbot development, it is ideal for storing dynamic and constantly changing data such as conversational flow and conversation history records by storing them in JSON format. Due to its flexibility and scalability, it allows for fluid analysis and integration with frameworks such as Rasa for conversation development and analysis. [31]

• Postgres: PostgreSQL is an open-source, robust, and scalable relational database management system (RDBMS), ideal for storing business rules and knowledge bases for chatbots. It allows you to organize information in tables with well-defined relationships, ensuring the accuracy and consistency of information through validation rules and restrictions. It provides high performance for reading and writing data, allowing for fast and efficient access to business rules and the knowledge base. [32]

• Docker: This is an open-source platform that facilitates the development, execution, and deployment of applications, such as the Chatbot, through the use of containers. When developing the Chatbot, Docker provides an isolated environment where you can develop and test the application, along with all the necessary dependencies and configurations. You can ensure that the Chatbot works in various environments, facilitating integration and deployment on the WhatsApp messaging platform. [33]

BERT: (Bidirectional Encoder Representations from) is a machine learning technique used to train natural language models (NLP). BERT is based on the Transformer architecture, which allows for bidirectional text processing, taking into account the full context of a sentence.
With the goal of improving chatbot accuracy, this AI model will be used for chatbot training. [34]

• DIETClassifier: (Dual Intent and Entity Transformer) is a multi-task natural language processing (NLP) model developed by Rasa NLU. Its main function is intent classification and entity extraction in dialog applications. This model is especially useful for enhancing chatbots, allowing them to understand and respond naturally to user queries. Intent classification is crucial for identifying the purpose or goal of a user's statement. [35]

Django: A free and open-source web development framework based on Python, it provides a predefined structure and tools for building web applications faster and more efficiently. In chatbot development, based on Django and the REST Framework, it is a versatile tool, providing flexibility in supporting rules and allowing the chatbot to be adapted to different needs and scenarios. [36]

• Ngrok: This tool allows a local server to be exposed to the Internet securely and temporarily. It works by creating a proxy server in the cloud, creating a secure tunnel between the computer and the server, and then providing a unique URL that can be used to access a local server from any web browser or application.

In chatbot development, this tool will be used to expose the chatbot's messaging server to the Internet for the testing phase. [37]

• AWS: Amazon Web Services, considered the most comprehensive and widely used cloud platform in the world; Instead of having physical servers to store data and run applications, these resources can be rented. AWS offers a wide range of comprehensive services, ranging from basic infrastructure to emerging technologies such as AI and machine learning, which is precisely what this project is concerned with. AWS is a tool that will facilitate the pre-production deployment of the Chatbot, as the application will be packaged in a Docker container, and AWS offers this service. [38]

7.2. DEVELOPMENT METHODOLOGY

7.2.1. Kanban
In project management, the Kanban methodology has emerged as a tool that offers a comprehensive and effective perspective for the successful development and execution of projects. By providing a transparent and detailed view of the work process, Kanban is a valuable solution for managing tasks, optimizing time, and efficiently achieving goals.

The Kanban methodology is a project management tool and is a great option for project development. This methodology offers a transparent way to manage tasks and visualize the completion process. This methodology helps prioritize tasks and manage time efficiently.
The first step in implementing the Kanban methodology is to define the project workflow. To do this, a board must be created that is accessible to all team members. Each column of the board must correspond to a specific state of the task flow, from start to finish. It's important that the board has as many columns as the status of each task, so you can see the status of each activity.

One of the unique features of the Kanban board is that it is continuous, unlike Scrum. As progress is made, new tasks accumulate in the initial section, and during regular meetings, they are prioritized and placed in the appropriate section. This board can be specific to a specific project or generic, depending on the team's needs.
The second step in implementing the Kanban methodology is to visualize the phases of the production cycle. To do this, work is divided into different parts, which streamlines the production process. Each of these parts is written on a Post-it note and stuck on the board at the corresponding phase. These Post-its contain basic information so the team can quickly understand the total workload. Additionally, photos can be used to assign responsibilities, as well as cards in different shapes to provide feedback or indicate blockers.

The goal of visualization is to provide maximum clarity on the work to be done, the tasks assigned to each team member, the priorities, and the assigned goal. This helps students have a clear idea of ​​what is expected of them and prioritize tasks based on importance and urgency. Finally, the third step in implementing the Kanban methodology in the project is to apply the motto "Stop Starting, Start Finishing." This means prioritizing work in progress rather than starting new tasks. Instead of jumping from one task to another, focus on completing tasks already in progress before moving on to new tasks. This helps avoid overwork and the accumulation of backlogs.

The Kanban methodology proves to be an effective tool for managing undergraduate projects efficiently and transparently. This methodology can be applied to prioritize tasks, visualize the production process, and avoid overwork. With proper implementation, the Kanban methodology can help successfully complete the proposed project.
[39]

7.2.2. Workflow for project development using the Kanban methodology
Phase 1: Planning

• Proposed solution: Define the chatbot solution to be developed, including its objectives and components.
• Chatbot requirements: Specify the chatbot's functionalities and features, including the scope.
• Processes to be covered: Identify the processes or procedures to be automated with the chatbot.
• Conversational flow: Design the chatbot's conversational flow


Phase 2: Design

• Application Architecture: Define the Chatbot's system architecture, including the different components and their interconnection.
• Process Modeling: Document the processes or procedures that will be automated with the Chatbot.

Phase 3: Development

• Phase I: Chatbot Core Development
- Development Environment: Configure the development environment for the Chatbot.
- NLP Model Training: Train the Chatbot's artificial intelligence model for natural language understanding.
- Input/Output Protocols: Select and implement the input and output protocols for the Chatbot.

• Phase II: WhatsApp Integration Middleware Development
- Communication Protocol and Channel: Select and implement the communication protocol for integration with WhatsApp.
- Conversation Rules Management System: Design and develop an application for managing conversation rules.
- Conversation Databases: Design and develop databases to store chatbot conversations and neural network training data.
- Neural Network Training Data: Define information processing for model training.

Phase 4: Functional Testing
• Functional Testing: Perform unit tests to ensure consistency and fluidity in conversations.
• Training Testing: Perform tests to evaluate chatbot performance.

Phase 5: Implementation
• Cloud Provider: Select a public cloud provider for chatbot deployment.
• Service Deployment: Deploy chatbot services and obtain corresponding domains.
• Technology Architecture: Define the technology architecture for chatbot deployment.
• Documentation: Create the chatbot's technical and functional manual.

7.4. PROJECT DEVELOPMENT
I. Planning Phase

a. Proposed Solution
The proposed technological solution for the Chatbot aims to automate the management of frequently asked questions and their corresponding responses within the Data Systematization Technology and Telematics Engineering curriculum project. This will be achieved through the integration of a Chatbot into the WhatsApp instant messaging platform. The solution consists of the following components:

✓ Scope analysis: A scope analysis will be conducted to define the Chatbot's functions and requirements, as well as to delimit the scope of the processes that will be automated by the Chatbot.

✓ Design and implementation of software components: The software components necessary to integrate the Chatbot into WhatsApp will be designed and developed. These components will be implemented in a microservices architecture exposed through APIs developed in the Python programming language.

✓ Data architecture: A data architecture will be designed and implemented to efficiently store conversations and the core of the response processing engine. The response processing engine will run adequately in a relational database such as PostgreSQL, but a non-relational database such as MongoDB can be used for conversations.

✓ Training of the response processing model: The response processing model will be trained using as input a catalog of rules defined from an analysis of the requirements survey. This input source must have a specific format that can be synchronized with the semantic and syntactic patterns of the NLP technique used.

✓ Functional testing: The chatbot will be evaluated in a question-based scenario with different users. If corrections and improvements are made, a continuous integration and continuous deployment (CI/CD) pipeline will be used, in accordance with DevOps best practices.

✓ Deployment in a pre-production environment: The chatbot and its components will be deployed in an environment through a cloud infrastructure provider. A provider that offers the benefits of infrastructure as a service (IAAS) or platform as a service (PAAS) will be used, allowing for the generation of network infrastructure configurations.

b. Define chatbot functions and requirements.

The chatbot's main function is to automatically provide information and assistance to the user, with content that is understandable in a university context. The requirements should take into account that the chatbot's end users will primarily be students, faculty, and administrative staff.

The current scope of the Chatbot is limited to internal university procedures, but it is anticipated that it may be used by external personnel in the future. Therefore, it is important to define the processes to be covered by the Chatbot, taking into account the current needs of these users.

c. Processes to be covered by the Chatbot.

The content to be used in the Chatbot is important, so the procedures associated with Data Systematization Technology1 will be taken into account, which are the same as those for telematics engineering:
