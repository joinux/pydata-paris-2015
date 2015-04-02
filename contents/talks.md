---
title: Talks details
author: sfermigier
template: text.html
---

<style>
blockquote p {
	font-style: italic;
	color: #555;
}
</style>

# All the talks and speakers at a glance

(See also the [Detailed Schedule](/schedule.html).)


## Keynotes


**Gaël Varoquaux** (INRIA): “scikit-learn for easy machine learning: the vision, the tools and its development”

> **Bio**: Gaël Varoquaux is an INRIA faculty researcher working on computational science for brain imaging in the Neurospin brain research institute (Paris, France). His research focuses on modeling and mining brain activity in relation to cognition. Years before the NSA, he was hoping to make bleeding-edge data processing available across new fields, and he has been working on a mastermind plan building easy-to-use open-source software in Python. He is a core developer of scikit-learn, joblib, and Mayavi, a nominated member of the PSF, and often teaches scientific computing with Python using <http://scipy-lectures.github.com/>.


**Francesc Alted** (UberResearch GmbH), “New Trends In Storing And Analyzing Large Data Silos With Python”.

> **Bio**: Teacher, developer and consultant in a wide variety of business applications. Particularly interested in the field of very large databases, with special emphasis in squeezing the last drop of performance out of computer as whole, i.e. not only the CPU, but the memory and I/O subsystems.


## Track 1 (morning): A gentle introduction to PyData technologies


**Alexandre Gramfort** (Telecom ParisTech): “Linear predictions with scikit-learn: simple and efficient”

> **Abstract**: Scikit-Learn offers numerous state-of-the-art models for prediction (regression and classification). Linear models (e.g. Ridge, Logistic Regression) are the simplest of these models. They have pratical benefits such as interpretability and limited computation time while offering the best performance for some applications. This talk will cover the basics of these models with examples and demonstrate how they can scale to datasets that do not fit in memory or how they can incorporate simple polynomial non-linearities.

> **Bio**: Alexandre Gramfort is Assistant Professor at Telecom Paristech in the signal and image processing department. His field of expertise is signal and image processing, statistical machine learning, software engineering and scientific computing applied primarily to neuroscience data. He has been a core developer of Scikit-Learn since 2010.


**Emmanuelle Gouillart** (CNRS): “Introduction to scikit-image”

> **Abstract**: scikit-image is a general-purpose image processing module for the Python programming language. It is designed to interact efficiently with other popular scientific Python libraries, such as NumPy and SciPy. In particular, scikit-image leverages the powerful data array container of NumPy, that can store images of various dimensions (2-D, 2D RGB, 3D, 4D...).

> **Bio**:  I'm a researcher in physics, working in the joint unit between the French institute CNRS and the company Saint-Gobain. I'm a member of the core development team of scikit-image, and I've been focussing in particular on implementing segmentation and denoising algorithms. I'm also a member of the PSF.


**Gilles Louppe** (CERN): “Tree models with scikit-learn: great learners with little assumptions”

> **Abstract**: This talk gives an introduction to tree-based methods, both from a theoretical and practical point of view. It covers decision trees, random forests and boosting estimators, along with concrete examples based on Scikit-Learn about how they work, when they work and why they work. 

> **Bio**: Core contributor of Scikit-Learn, Researcher in machine learning, currently at CERN (Switzerland).


**Joris Van Den Bossche** (Ghent University): “Introduction to Pandas”

> **Abstract**: Pandas is becoming the fundamental library for manipulating and analyzing structured data, providing high-performance, easy-to-use data structures and data analysis tools. This talk will give a basic introduction to pandas, explaining the key concepts and defining features.

> **Bio**: I am a PhD student at Ghent University (Department of Mathematical Modelling, Statistics and Bio-informatics) working on mobile air quality monitoring in collaboration with VITO (Flemish Institute for Technological Research). I am also a contributor to pandas, and since a year a member of the core development team.


## Track 2 (morning): PyData in the real world

**Ian Ozsvald** (Mor Consulting): “Cleaning Confused Collections of Characters”

> **Abstract**: Success in data science projects depends upon clean input data. Text data is often badly encoded, lacks data types and is inconsistent. Aimed at the intermediate Pythonista I'll talk about the time saving tools I use in ModelInsight to clean and normalise my data so you can easily work on new projects.

> **Bio**: As a contract data scientist working at a high strategic level, my role is to uncover potential revenue streams that can be exploited in clients’ large data sets. This work also includes scaling existing systems and strategic design for new systems.


**Chloe-Agathe Azencott** (Mines ParisTech): “Reaching your DREAMs with Python”

> **Abstract**: DREAM challenges (http://dreamchallenges.org/) gather participants from a wide community of researchers to analyze data provided to help solve fundamental, cutting­edge questions about systems biology and translational medicine.

> I will show how Python and scikit­learn can be used to process data, try out standard machine learning techniques, and develop ad hoc solutions to address such challenges. This talk will be illustrated by the example of two challenges in which I took part, both times in teams that placed second. The first of these challenges was in toxicogenetics (https://www.synapse.org/#!Synapse:syn1734172), aiming at predicting the toxicity of a chemical on a cell line. The second (https://www.synapse.org/#!Synapse:syn1761567) was aimed at predicting the response of patients to rhematoid arthritis treatment.

> **Bio**: Chloé Agathe Azencott is a junior research faculty at Mines ParisTech (Paris, France). She belongs to the Centre for Computational Biology, a joint research group between Mines ParisTech, Institut Curie and INSERM focusing on bioinformatics for cancer research. She holds a PhD in computer science from University of California, Irvine (USA), which she obtained in 2010. From 2011 to 2013 she was a postdoctoral fellow in the Machine Learning for Computational Biology research group of the Max Planck Institutes for Developmental Biology and Intelligent Systems in Tuebingen (Germany). Her research interests revolve around developing machine learning approaches for therapeutic research. This ranges from chemoinformatics methods for drug discovery to the analysis of large­scale, heterogeneous, whole­genome data for precision medicine. And she has now been programming in Python for 10 years.

> For more details see <http://cazencott.info/>


**Camilla Montonen**: “Rush Hour Dynamics: Simulating and visualising commuter flow through the London Underground using graphtool and bokeh”

> **Abstract**: Every year the London Tube transports about 1.3 billion commuters. With multiple intersecting lines, the daily functioning of the London Tube network poses many interesting questions: What effects do severe delays on the Piccadilly Line have on passengers taking the Northern Line? What is the shortest path from station x to station y? How does overcrowding on one station affect its neighbouring stations? These are but a few examples of the many questions one can start to investigate using two Python libraries: graph­tool for manipulating and analysing graphs and bokeh for visualizing and streaming “live” data from simulations.
> In this talk, I will briefly show how one can transform structures such as the London Underground map into programmatic objects that can be analysed and manipulated using Python. Furthermore, I will show examples of simulations based on the publicly available data from Transport for London and illustrate how simulations can be used to glean insight on the large scale behaviour of a complex system. Last but not least, I hope to illustrate how the bokeh server can be leveraged to create “real­time” visualizations of simulations.

> **Bio**: Noora Camilla Montonen first started using Python for scientific computing when she was completing her MSc in Informatics at the University of Edinburgh. She currently works as a Junior Software Engineer in Test at a London financial software company. Although by day she works with Java, by night she is a secret Pythonista. She would like thank Pyladies London and Women in
Data London for showing her how amazing Python can be.


**Data scientists from AXA Data Innovation Lab** (Axa): “Whitening the blackbox : why and how to explain machine learning predictions”

> **Abstract**: Unfortunately, the predictive models that are most powerful are usually the least interpretable. However in some cases, for example fraud detection, end users need an understandable explanation of a particular prediction, at observation level, and not only at population level (e.g. : features importance).
> During this talk we will present different approaches to tackle this issue, both for random forests and gradient boosting trees. We will also demonstrate an implementation based on scikit-learn.


#### Track 3 (afternoon): High Performance PyData

**Niels Zeilemaker** (GoDataDriven): "Embarrassingly parallel database calls with Python"

> **Abstract**: Have you ever squeezed you SQL queries to the last millisecond, but still found yourself with not enough speed in your data­driven Python applications? Then this talk is for you. We'll look at how to shard your data, which design changes should happen and how to use the Python threading module to bring in the data as quickly as possible by making parallel
database calls.

> Expected audience: Python developers building real­time applications needing increase their response time.


**Serge Guelton and Pierrick Brunet** (Namek): “Pythran: Static Compilation of Parallel Scientific Kernels”

> **Abstract**: As the use of Python coupled to Numpy/SciPy for numerical computation increases, many tools to optimize performance have emerged. Indeed, this duo has relatively poor performance when compared to scientific codes written in legacy languages like C or Fortran. Cython, Numba, numexpr and parakeet belongs to this new compiler ecosystem. And so does Pythran, a Python to C++11 translator for scientific Python.

> Pythran uses a static compilation approach a la Cython, but with full backward compatibility with Python. It does not only turns Python code into C++ code, it also performs Python/Numpy specific optimizations, generates calls to a parallel, vectorized runtime and makes it possible to write OpenMP annotation in the original Python code. It supports a large range of Numpy functions and can combine them in efficient ways: it can optimize high­level modern Python/Numpy codes and not only Fortran­ with­ a­ Python­ flavor ones.

> This talk presents the existing compilation approach and optimization opportunities for numerical Python, their strengths and weaknesses, then focus on the specificities of the Pythran compiler.


**Antoine Pitrou** (Continuum Analytics): “Numba, a JIT compiler for fast numerical code”

> **Abstract**: This talk will be a general introduction to Numba. Numba is a just­-in-­time Python compiler that allows you to speed up numerical algorithms for which fast linear algebra (i.e. Numpy array operations) is not enough. It has backends for the CPU and for CUDA GPUs.

> Expected audience: Python programmers / scientists who have an interest in speeding up numerical routines. Also, people who are curious about attempts at high-­performance Python.

> **Bio**: Antoine Pitrou is a senior software engineer.  A Python core developer since 2008, he works at Continuum Analytics on Numba.


**Kirill Smelkov** (Nexedi): “Out-of-core NumPy arrays without changing your code with wendelin-core”

> **Abstract**: This talk introduces a new implementation of NumPy arrays that provides support for out­of­core data analysis without changing code, without breaking APIs and without losing the performance advantage provided by FORTRAN libraries or just­in­time compilers. wendelin­core acts transparently as distributed shared virtual memory manager for binary data handled by python interpreters deployed on a cluster. Thanks to wendelin­ core, each python interpreter can access elementary ndarray structures of virtually 2 exabytes in a single memory block, whatever the amount of RAM available on each node. With wendelin­core, a cluster of inexpensive PCs can thus act as a teramory server at much lower cost. A cluster of tera­-memory servers can act as an examemory machine.

> In addition to bringing true BIg Data support to NumPy libraries, wendelin­core also provides native persistency of ndarrays thanks to its integration with NEO database. NEO together with wendelin­core can shard and store ndarrays on a redundant array of inexpensive computers and provide native support for python exception handling, thus enforcing a rollback of any change made to data in case of bug or error during a calculation.

> The talk will focus on the technical aspects of wendelin­-core. It will explain the technical approach that has been used for the first implementation: what has been achieved, what is still weak, what can be improved. It will explain how to hook wendelin­-core to a persistency layer. It will then present the technical roadmap and suggest how to integrate wendelin­core to other persistency layers or to other data structures.


#### Track 4 (afternoon): Industrial and business case studies

**Jean-Paul Smets and Sébastien Robin** (Nexedi): “Industrial Monitoring with the Wendelin Big Data platform”

> **Abstract**: This talk presents the Wendelin Big Data "Full Stack" and introduces a first success story related to the collection of vibration data in wind turbines and the analysis of vibrations.

> Wendelin (<http://wendelin.io/>) combines automated cluster deployment, distributed data persistency for NumPy arrays, parallel data processing, fluentd compliant data ingestion interface and JIO compliant javascript interface. It is an all­in­one open source solution that provides a 100% native python alternative to hybrid solutions based on Spark.

> The talk is derived from the presentation made at MariaDB community event (<https://mariadb.org/en/community-events/>). The presentation of Wendelin Full Stack will be shorter than in Santa Clara in order to provide enough time to present the first implementation for Wind Turbines. We will show in particular which parts of data analysis are handled on server side with pydata libraries, which parts of data analysis are handled on browser side in javascript and how both can be integrated to minimize implementation costs.

> The talk concludes on Wendelin platform roadmap.


**Jean Maynier** (Kpler): "Python, SQLalchemy and Scrapy for real-time data processing at Kpler”

> **Bio**: I lead the engineering and operational activities of Kpler (formerly eCO2market).

> Founded in Paris in 2009, Kpler is an intelligence company providing transparency solutions in energy markets. We develop proprietary technologies that systematically aggregate data from hundreds of sources, ranging from logistics and commercial, to governmental and shipping databases. By connecting the dots across fragmented information landscapes, we are able to deliver our clients with unique real-time market coverage.


**Fabien Mangeant et Vincent Feuillard** (Airbus): "scikit-learn for predictive maintenance at Airbus"



**Julien Sananikone** (PriceMinister), **Benjamin Guinebertière** (Microsoft), **Samuel Charron** (Data Publica), **Thomas Cabrol** (Dataiku): “Industrial uses of scikit-learn” (business roundtable)

> **Bio**: Julien Sananikone is Project manager at PriceMinister. 

> Benjamin Guinebertière is technical evangelist at Microsoft. Benjamin works with startups and companies of different sizes to help them technically adopt Microsoft Azure cloud, should they use Big Data, Machine Learning or other technologies. He also speaks at conferences, writes (blogs, …) and takes feedback.


> Combining a strong background in webmining and big data technologies
with a deep interest in machine learning, Samuel Charron has earned
the title of Big Data Sergeant at Data Publica, where he alternates
between contributions to the development of the infrastructure of the
C-Radar product and stints of rapid prototyping with Python data
science libs (such as pandas, sklearn).
In particular, he works on NLP related problems using unstructured
web-scraped data to enrich corporate information.


> Thomas is Dataiku’s Chief Data Scientist. Thomas started his career in data mining for large retail and telecommunications companies. Then he lead the data mining team and geo-marketing initiatives at Apple Europe. He was lead data scientist at qunb, a data visualization startup. He spent most of his career deriving value from large datasets using cutting-edge innovations. He is fluent in all the data scientists linguas: R, Python, SAS...


**Clément Jambou** (Lyft): “Using Python and Data science to tackle real-time transportation problems at Lyft"”

> **Abstract**: I'm interested in giving a talk for this conference as I believe many students with the same background as mine would be interested in hearing about how Data Science is a crucial tool in building a successful startup and its influence on taking decision every day. As part of my work I use python and scientific librairies ( pandas, scikit­learn) on a daily basis as it is used both on our backend services as well as for Data analysis. We tackle complex problems such as Dynamic Pricing depending on local demand an supply, dispatching Drivers efficiently, Matching multiple passenger routes together for or real time ride­sharing product Lyft Line, real­time ETAs and traffic estimation...
> The fact that a lot of or analyses use geolocation data adds a specific component to it that leads to complex problems. Optimization is crucial as it is beneficial for everyone in our Marketplace: Passenger can get lower prices and better service, Drivers spend more time with someone in their car and have higher earnings...

> **Bio**: I followed the classical French Engineering path by spending 2 years in "Preparatory Classes" with major in Mathematics and Computer Science at Lycee Hoche in Versailles. I then join ISAE­Supaero where I was able to discover the field of Machine Learning and learn more about its growing impact on our society. I interned with Lyft in the summer of 2013 in San Francisco, which comforted me in my choice of becoming a Data Scientist. I then finished my degree from Supaero by doing a Masters in AI and Machine Learning at the Imperial College in London before going back to Lyft. I have always have a passion for Mathematics ( since High school) and my job gives me an opportunity to apply Math to solve concrete problems. I am particularly interested in Deep Learning, and problems that use a large amount of Data, therefore I use Pandas, Theano, Pylearn2 and Scikit­learn in a daily based for my job.

