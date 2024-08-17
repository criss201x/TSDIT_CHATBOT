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


4.2. THEORETICAL FRAMEWORK

4.2.1. Chatbots.

A chatbot is a software designed to simulate conversations with human users,
usually through messaging applications, such as

Facebook Messenger, WhatsApp or Telegram. A chatbot usually
employs natural language processing (NLP) algorithms to interpret
user messages and provide automated responses. The purpose of a chatbot is to
benefit from automating a wide range of tasks ranging from customer
service and sales to entertainment and personal assistance. They can help
organizations automate routine tasks, reduce response times and improve
customer satisfaction.

A chatbot can be rule-based or artificial intelligence-based. A
rule-based chatbot follows a predefined set of rules and can only
respond to specific keywords or phrases. An AI-based chatbot, on the other hand, employs machine
learning algorithms to learn from previous interactions and improve its responses
over time. An AI-based chatbot can also understand natural language inputs, making it more flexible and adaptable than a rule-based chatbot.

The ideal of a chatbot is to ensure a seamless, human-like user experience. Chatbots are currently the most popular because they can handle a variety of inputs, understand context, and provide relevant and helpful responses. Despite the challenges, chatbots have become increasingly popular in recent years, and many organizations are adopting them to improve their customer service and communication channels.

4.2.2. How a chatbot works.

To create chatbots, which replicate natural language conversations with users through messaging apps, websites, mobile apps, and phones, AI software is typically used. This application is essential as knowledge is pre-stored, allowing for self-learning and restoration of knowledge through human or online resources. As the application of the system takes the form of a
Chatbot, it responds to user requests using the question-answer
protocol [9].

4.2.3. Technological advancements and related trends.
•
Conversational AI.
Conversational AI makes it possible to understand human language and respond
accordingly. In other words, conversational AI allows a Chatbot to
respond to you naturally.
It uses voice recognition and machine learning to understand
what people are saying, how they are feeling, what the context of the
conversation is, and how they can respond appropriately. Furthermore, it supports
many communication channels (including voice, text, and video) and is context-aware, allowing it to understand complex requests
involving multiple inputs/outputs. The critical difference between Chatbots and
Conversational AI is that the former is a computer program,
while the latter is a type of technology. [10]
•
Multimodal inputs.
Multimodal AI is in the field of natural language dialogue systems. Multimodal models can use visual and linguistic cues to generate more human-like conversational responses. For example, a chatbot that understands the visual context of the conversation can generate more appropriate responses that consider not only the text of the conversation but also the images or videos that are shared. [11] Many chatbot platforms now support multimodal inputs as a standard feature. Multimodal chatbots are especially useful for complex interactions where multiple types of inputs are required, such as making a hotel reservation where the user may want to see photos of the rooms, ask questions about amenities, and check availability by voice or text.

Integration with other technologies.
Chatbots are being integrated with other technologies, such as machine learning,
IoT, and AR/VR, to provide more complete solutions. For example,
Chatbots can be integrated with machine learning algorithms to
provide predictive analytics and personalized recommendations.
Integration can also be defined as the problem of integrating
conversational capabilities into existing software systems. Doing so
may require developing a conversational agent that starts with the
data, application logic, or graphical UI of the system to support
natural language conversations leveraging artificial intelligence (AI)
or more traditional software engineering approaches.[12]
•
Ethics, privacy, and security.
Chatbots are increasingly popular artificial communication systems
and not all of their security questions are clearly resolved.
People use Chatbots for shopping assistance, banking communication,
food delivery, healthcare, automobiles, and many other actions.
However, it brings an additional security risk and creates serious security challenges that need to be managed.

Modern Chatbots are no longer rule-based models, but rather
employ modern natural language and machine learning techniques.
Such techniques learn from a conversation, which may contain
personal information [13] that must be treated appropriately, for which ethical and data handling policy rules are provided.
Many Chatbots operate on a social/messaging platform, which has
its terms and conditions regarding data handling.
•
Evaluating the performance of Chatbot systems.
Chatbots are generally designed to serve specific purposes.
For example, customer service Chatbots are designed
specifically to meet the needs of customers seeking help, while conversational Chatbots are designed to have
interactive communications with users. These Chatbots are designed
and built based on the domain in which they will operate.
Chatbots tend to fail when presented with situations and inputs that they are not familiar with. This may include ambiguous

statements, grammatically incorrect phrases, and statements outside the bot's
operational domain. [14]
Chatbot performance is often measured by its similarity to that of a
human. Therefore, it is imperative that Chatbots operate and interact in a
desirable manner. Organizations must rigorously test and verify their Chatbot
before releasing it to production.
Current Chatbot testing approaches either monitor the Chatbot output
to assess performance or study the internal functionality of the Chatbot and the
various algorithms involved.
4.2.4. Rule-based Chatbots.
Rule-based Chatbots rely on a list of simple,
predefined queries and possible resulting responses. It does not need any machine
learning approach and language processing is not mandatory.
They are intended for simple queries and may fail in more complicated questions as they cannot produce their own answers.
(Jagdish Singh 2019) Proposed a rule-based Chatbot for students at Asia Pacific University (APU) to answer their queries from their administrative offices. The designed Chatbot allows end users to view information and interact with the Chatbot regarding their queries. The developed system was compatible with the bot's Facebook application page to access via a laptop or computing devices. [15]
4.2.5. Hybrid Chatbots.
A Hybrid Chatbot is a combination of rule-based and AI-powered Chatbots. They use pre-programmed rules to handle simple tasks and machine learning algorithms to handle more complex tasks.
This allows the chatbot to provide the best of both worlds: consistent responses for simple tasks and personalized responses for complex tasks, providing an improved user experience that seamlessly blends automation with human assistance. [16]

4.2.6. Transactional Chatbots.

A transactional chatbot acts as an agent and interacts with external
systems to carry out a specific action. Thus, a transactional
chatbot differs from the more common bots, also called informative or
conversational chatbots, in that its objective is to
automate a transaction and simplify the user experience
by providing a suitable and fast channel for a specific objective. It is
optimized to execute a certain number of specialized processes
that eliminate the need to speak with an expert or to use more complex interfaces
such as mobile applications or websites.

Transactional chatbots can be implemented in various sectors,
such as banking, insurance or e-commerce. In the financial sector, for example,
they can automate simple tasks that would otherwise be carried out by a
banker over the phone, such as verifying your identity, blocking a stolen credit
card, informing you of the hours of nearby offices or confirming an issued
transfer. [17]
4.2.7. Self-learning Chatbot.
A self-learning Chatbot understands what the user wants and consequently saves the users effort to complete a daily task by communicating with the second Chatbot on behalf of the user. It tries to overcome the lack of knowledge of the user's preferences and requirements in making decisions on behalf of the user.
Both the server and the chatbot interact with each other and work as if it were a normal conversation and the resulting output is returned to the user. This leads to reduced to sometimes zero input from the user while adapting the user's preferences and tastes. User preferences play a vital role in the conversation. The more the user interacts with the system, the more it trains the system to understand the user's preferences.
Automating the communication of a Chatbot in such a way that it communicates on behalf of human preferences considering the preferences is what has been proven as a system. By

self-learning, the system adapts and takes into account all the user's
preferences and learns more and more about the user over time. [18]
4.2.8. Natural Language Processing.
Natural language processing (NLP) is a field of computer science,
artificial intelligence, and computational linguistics that deals with the
interactions between computers and human (natural) languages. It
focuses on how to program computers to process and analyze large
amounts of natural language data.
Natural language processing (NLP) is experiencing rapid
growth as its theories and methods are increasingly implemented
in a wide range of different fields. In the humanities, work
on corpora is gaining increasing prominence. Within industry,
people need NLP for market analysis, web software development, to name a few examples. For this reason, it is important
for many people to have some working knowledge of NLP. [19]
The relationship between Chatbots and NLP lies in the fact that Chatbots have
become an increasingly popular means of customer service and support for
businesses. By using Chatbots, businesses can automate
customer interactions, provide 24/7 support, and reduce the workload of human customer
service representatives. However, for Chatbots to be effective, they must
be able to understand and respond to users' natural language input, which
requires sophisticated NLP algorithms.
4.2.9. Python programming language.
It is a multiplatform programming language, very popular in the industry.
Being a dynamic language, it allows testing portions of code as they are
generated, optimizing the programming and debugging time of the written code. Created by Guido van Rossum in 1989. This
language is considered simple and easy to learn, granting the programmer virtues such as automatic memory management, simple reading or writing operations. In which it differs from other programming languages

programming. Another advantage is its flexibility, since
it stores a large amount of data of various types without having to declare each
type of data, it is an ordered, readable, and portable language. [20]
4.2.10. Microservice-API.
The microservices architectural style is an approach to develop a
single application as a set of small services, each
running in its own process and communicating with lightweight mechanisms,
often an HTTP resource API. These services are based on
business capabilities and are implemented independently by
fully automated deployment machinery. There is a minimum
indispensable centralized management of these services, which can be
written in different programming languages ​​and use different
data storage technologies. [21]
4.2.11. Cloud infrastructure.
Cloud infrastructure is based on virtualization to separate
resources from physical hardware and group them into clouds. Automation software and management tools distribute these resources and
prepare new environments so that users can access the elements they
need at any time. This allows for greater flexibility and scalability in managing computing
resources. Hardware, virtualization, storage, and network components work
together to provide a complete cloud computing solution.

Cloud infrastructure can refer to both an entire cloud computing system and the individual technologies that compose it.

•
Elements of cloud infrastructure.

o Hardware
Cloud infrastructure requires physical hardware to operate, which can include a network of hardware systems
distributed across different geographic locations. This network can

include network equipment such as switches, routers, firewalls, and load balancers, as well as storage arrays, backup devices, and servers.

o Virtualization
Virtualization is a technology that separates IT functions and services from the physical hardware system. A hypervisor, a specialized software, controls the physical hardware and abstracts the machine's
resources, such as memory, computing power, and storage. Once virtual resources are assigned to
centralized pools, they are considered clouds.
Virtualization is essential for creating and managing cloud
infrastructure, as it allows for the creation of virtual environments
from a single set of physical resources, allowing for greater efficiency and scalability.
o Storage
Storage management in cloud infrastructure is
essential to ensure data integrity and availability.
Data is stored on storage arrays and is
regularly backed up to protect against failure or loss of information.
With virtualization, storage is abstracted from the hardware
and offered to users in the cloud as a shared resource.
This allows for greater flexibility in managing storage
resources, as drives can be added or removed as needed and respond to changes
without having to add separate storage servers.
o Network
Cloud infrastructure includes a physical network made up of
cables, switches, routers, and other equipment, which is used
to create virtual networks. The traditional cloud network setup
consists of multiple subnetworks with different levels of
control, and virtual local area networks (VLANs) can be created and
static or dynamic addresses assigned to network resources.
Users can access cloud resources through
a network, either the Internet or an Intranet, allowing them to access
cloud applications or services remotely. The network
also allows users to interconnect multiple clouds, giving them the
flexibility to choose different cloud providers or
integrate their own private and public cloud solutions.
Cloud infrastructure consists of the same basic elements,
whether it is a public, private, or hybrid cloud. To
work with any type of Cloud Computing, a cloud infrastructure is required, which can be created by yourself or
using a public cloud through a cloud service provider.

•
Comparison between infrastructure and cloud architecture:
Cloud architecture refers to the way different technologies are combined to create cloud computing environments, while infrastructure is the set of tools needed to design the cloud. Architecture is like a technical blueprint that indicates how cloud elements such as hardware, virtual resources, networks, operating systems, etc. should be connected. [22]
4.2.12. Types of Cloud Computing as a Service. [23]
•
IAAS
Infrastructure as a Service (IaaS) is a cloud service model in which a third-party service provider offers IT infrastructure such as storage, servers, and virtualization to users who pay for their consumption. The provider manages the resources, and the user is responsible for operating systems, data, applications, and runtimes. IaaS
offers flexibility to acquire and adapt the necessary elements and is an
affordable option since it does not generate maintenance costs.

Some disadvantages of IaaS are possible security problems of the
provider, service reliability, and multi-tenant systems where the
provider must share infrastructure resources with several
customers. Some public cloud providers that offer IaaS may include
AWS, Microsoft Azure, and Google Cloud.
•
PAAS
Platform as a Service (PaaS) is a type of cloud service model used to
provide users with an online application development and
running environment. In the PaaS model, the cloud service provider
hosts the platform and software on its infrastructure, allowing users to develop and
run applications without having to worry about managing the infrastructure.
PaaS is an especially useful solution for developers and programmers, as it provides them with a complete environment to write and manage applications, and allows them to focus on developing the application itself, rather than having to worry about maintaining and managing the infrastructure. In addition, PaaS offers the ability to customize and design their web-based applications using built-in software elements. Examples of PaaS include AWS Elastic Beanstalk, Heroku, and Red Hat OpenShift.
4.2.13. Digital transformation. [24]
Digital transformation refers to the process of incorporating digital technologies into all areas of an organization to change the way value is delivered to customers. Digital transformation involves cultural and operational changes, and can include building digital solutions, moving to cloud computing, and adopting smart sensors to reduce operating costs. The goal is to better adapt to changing customer needs and improve efficiency in the organization.
Digital transformation is important for organizations because it allows them to
stay competitive in an ever-changing technological environment. Digital
transformation initiatives can improve productivity, customer
experience, and reduce operational costs. Emerging technologies, such as artificial
intelligence and cloud services, can save time and improve efficiency in business
processes. Digital transformation can significantly reduce operational
costs by eliminating or replacing specific workflows, reducing spending on
expensive infrastructure and equipment, and automating tasks with technologies such as
smart sensors and machine learning.
Digital transformation goes beyond digitizing processes and workflows. It refers to the integration of digital technologies to
fundamentally change the way products or services are delivered, customers are interacted with, and business
processes are operated.
Digital transformation involves profound cultural and operational changes,
such as reorganizing teams and adopting new ways of working, to adapt to changing market and customer needs. Digital transformation is about using technology to reinvent
the business and create new growth opportunities.

•
Digital transformation and Chatbot [25]:
As mentioned, digital transformation is a complex process that
involves a re-evaluation and reorganization of business processes
to make the most of emerging technologies. In this context,
Chatbots have emerged as a key tool to assist in the
digital transformation process of organizations.
The main way Chatbots help in the digital
transformation process of an organization is by automating
tasks and processes. Chatbots can be integrated into different business
systems and applications to provide quick and accurate answers to
frequently asked questions and perform repetitive tasks, thereby
reducing the workload on employees and allowing a focus on more strategic
tasks.

In addition, Chatbots can significantly improve the customer experience by providing instant and personalized customer support. Customers can interact with a Chatbot at any time of the day and get accurate and fast answers to their questions.

Another benefit of Chatbots is data collection. Chatbots can track and analyze customer interactions, allowing organizations to better understand customer needs and preferences and
continuously improve their services and products. Additionally, chatbots
can be integrated with data analytics and machine learning tools to identify
patterns and trends in the data collected, which can help in business decision-making.
