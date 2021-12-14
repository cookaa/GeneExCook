# GeneExCook

A tool to Normalize genetic expression and study Gene Correlation
>TODO Live demo [_here_](https://www.youtube.com). <!-- If you have the project hosted somewhere, include the link here. -->

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
<!-- * [License](#license) -->


## General Information
<!-- - Provide general information about your project here.
- What problem does it (intend to) solve?
- What is the purpose of your project?
- Why did you undertake it? -->

### Introduction - the project's aim
	Genetic sequencing, storage, and processing has reached a point to allow for the study of specific gene expression and their relation with other genes. This project uses housekeeping genes (HK) to normalize the expression of samples before running a correlation analysis. In addition, provides a publicly available program through github to test correlation between different genes.

### Technologies
Python 3.6 was chosen for this project due to its versatility and number of packages to allow for the handling of numbers. Python has a large number of features perfect for biological computation. Some of the included packages include: seaborn, serveItUp, plotly, and sci-kit, sklearn. scipy, numpy, and pandas and streamlit 1.1.0. 



## Technologies Used
- Streamlit 1.1.0.
- Pandas 1.3.4.
- Seaborn 0.1.1.2.


## Features
List the ready features here:
- Normalization
- Heatmap
- Output CSV


## Screenshots
![Example screenshot](./img/screenshot.png)
<!-- If you have screenshots you'd like to share, include them here. -->


## Setup
<!-- What are the project requirements/dependencies? Where are they listed? A requirements.txt or a Pipfile.lock file perhaps? Where is it located?

Proceed to describe how to install / setup one's local environment / get started with the project. -->

To install required dependencies, use:
```
pip install ...
```
any needed dependencies 

## Usage
In order to run the program navigate to the home location of the program and simply use the terminal and run:
```
streamlit run genExCook.py
```
Data to be analyzed should be named testdata_1.csv. In future updates, I hope to flush out a file selection and parsing of other file types.

Then click on whatever tools you would like to use (Pearson, Spearman, Heatmap, Etc.)


<!-- ![Data Flowchart](./images/flowchart.jpg) -->


## Project Status
Project is: _in progress_


## Room for Improvement

Room for improvement:
- Allow for different HKG for Normalization
- Data flow
- Code cleanliness 

To do:
- Add File input
- Add exception handling


## Acknowledgements
- This project was inspired by my work studying RNF4 and sumoylation, and the work done by Oliver Bonham Carter in genExSt.
- This project was based on [genExSt](https://github.com/developmentAC/genExSt).
- Many thanks to Dr. Thu and Oliver Bonham-Carter for their countless help throughout this project.


## Contact
Created by [@cookaa](https://www.linkedin.com/in/biocook/) - feel free to contact me!

Feedback is appreciated, feel free to comment or create an issue and pull requests.


<!-- Optional -->
## MIT License -->
This project is open source and available under the MIT License.


