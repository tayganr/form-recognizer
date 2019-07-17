# Form Recognizer with Azure Functions

**Pre-Requisites**  
* Visual Studio Code
* Python 3
* Azure Functions Extension for Visual Studio Code.

**Steps**  
1. Azure Portal > Create a Function App  
   * **Operating System:** Linux
   * **Hosting Plan:** Consumption
   * **Runtime Stack:** Python

2. Visual Studio Code > Create a New Virtual Envrionment (Python).
    * Open Visual Studio Code
    * Open the folder that you would like to work from
    * Terminal: ```virtualenv .``` (this will create a virtual environment)
    * Terminal: ```.\Scripts\activate``` (this will activate the virtual environment)

3. Press: Ctrl + SHIFT + P
4. Search "Create New Project", Select **"Azure Functions: Create New Project"**
5. Select the folder to deploy the Azure Function project to.
6. Select **Python** as the language for your Azure Function project.
7. Select **HTTP trigger** as the template for your projects function.
8. Provide the function a name (e.g. AnalyzeForm).
9. Select the **Function** authorization level.