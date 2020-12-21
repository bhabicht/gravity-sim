# Exercise B - FSWT
## 1. Unified Modeling Language
I created the following 3 UML diagrams to enable a better understanding of the  
code.
1.  First I created a relatively simple class diagram which shows the 3 classes  
Massiveobject, Planet and Rocket. Planet and Rocket inherit from the base class  
Massiveobject as you can see in the figure:  
![Class diagram](/documentation/UML/InheritanceClassDiagramUML.png)  

2.  Then as a second UML diagram I created a use case diagram to show what you  
can do with my program. First you can create a planet system, then you can use  
this system and calculate the trajectories that are given by the physical laws  
of motion and finally you can plot the resulting trajectory with a 3D plotting  
tool:  
![Use case diagram](/documentation/UML/UseCaseDiagram.png)  

3.  And last but not least I created a dependency graph to show which files use  
which imports. And you can see that my 3 domains are nicely seperated:  
![Dependency graph diagram](/documentation/UML/DependencyGraphUML.png)  
## 2. Domain Driven Design
I could identify 3 different domains for my project.  
The most important part of my project is the calculation of the trajectories.  
Thus I defined **Trajectory Calculation** to be my core domain.  
Next I could also identify a supporting domain: The **Planet system creation**  
domain. It is supporting and not a core domain because it is necessary for this  
project and also specific for this project but it is not the interesting part.  
Then there is also a generic domain **3D Plotting** which is not at all  
specific for my project. This domain is very general and applicable to a lot of  
projects. Please look at the following figure:  
![Relationship Diagram](/documentation/DDD/RelationshipDiagram.png)  
As you can see the data flows from the top to the bottom. It starts with the  
planet system generation. Details of the planet system are then needed for the  
trajectory calculation. And finally the data of the trajectory is fed into the  
plotting module.

## 3. Metrics
I looked at a few tools to calculate metrics but finally I settled with codacy  
because I like the website a lot, it is easy to use, and focuses on the  
relevant stuff. I used github actions to upload the coverage data automatically  
to the website.  
Here are some metrics that are calculated:
-   **Issues**  
"Number of lines of code with issues divided by all lines of code"  

-   **Complexity**  
"Number of complex lines of code divided by all lines of code"  

-   **Duplication**  
"% of files with duplication"  

-   **Test Coverage**  
"% of lines of code tested"  

The test coverage report ist automatically uploaded to codacy using  Github  
Actions. And I also added a badge to my readme to directly acces the website.  
Or [click here](https://app.codacy.com/gh/bhabicht/gravity-sim/dashboard) to access the website. This tool helped me to spot my weaknesses  
and thus it made me a better programmer.

## 4. Clean Code Development
i need to show 5 points in my code and create a ten point cheat sheet.

## 5. Build Management
I decided to use the handy build managment tool [doit](https://pydoit.org/). I used this tool to automate  
tasks that need to be done frequent but take some time to type in manually.  
Therefore I used a [dodo.py](https://github.com/bhabicht/gravity-sim/blob/main/dodo.py) file to define the tasks that I wanted to automate:  

-   **coverage**  
With this task I can automatically generate a coverage.xml file that is needed  
to upload the test coverage data to codacy.

-   **ut**  
Here I execute all unit tests.

-   **lint**  
Use flake8 to link every line of code.

-   **html**  
Create a html version of the documentation using pdoc. You can see the  
generated file [here](https://github.com/bhabicht/gravity-sim/blob/main/documentation/code/index.html).

-   **dependency**:  
Use pydeps to create a dependency graph.

## 6. Unit Tests
The unit tests can be found in this [folder](https://github.com/bhabicht/gravity-sim/tree/main/tests).  
Right now (20.10.2020) the test coverage is 72%. I used the standard python  
library unittest to do the tests. I included running all tests in my build  
management und also for CI/CD with Github Actions. This was the first time  
for me that I wrote tests. I realized they are very useful to ensure that your   
code is working as intended and gives you much more confidence when refactoring  
your code.

## 7. Continuous Delivery
"Continuous Delivery is about keeping your application in a state where it is  
always able to deploy into production" (Martin Fowler).  
To ensure that my application is in a state where it is always able to deploy  
into production I used the tool Github Actions.
My pipeline as a .yml can be found [here](https://github.com/bhabicht/gravity-sim/blob/main/.github/workflows/test-lint-code.yml).  
The pipeline is as follows:
1.  Print the current python version to ensure that 3.6 is used
2.  Upgrade pip and install the dependencies from [requirements.txt](https://github.com/bhabicht/gravity-sim/blob/main/requirements.txt)
3.  Run all test, generate coverage.xml, upload report to codacy
4.  Lint the code with flake8 to ensure PEP8
## 8. IDE
I used VSCodium as my IDE because it is very lightweight (and fast!), yet it has a lot of  
useful functionality. For example it integrates linter tools like flake8 and  
mypy and pylint. Also it can run all my tests automatically and has really nice  
git integration (the diffs are really useful). Also useful was that I could  
specify which virtual environment it should use.
My favourite keyboard shortcuts are:
-   Ctrl + Shift + P to open the search
-   Shift + Alt + F to reformat code
-   F2 to rename files
## 9. DSL
## 10. Functional Programming
