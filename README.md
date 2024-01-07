# Social Network XML Parser and Visualizer

A GUI-based program for parsing and visualizing an XML file representing a social network of users. The project includes various operations such as parsing, error checking and fixing, conversion to JSON, minifying, compression, decompression, prettifying, graph visualization, graph analysis, post search, and undo/redo functionality.

## Table of Contents

- [Social Network XML Parser and Visualizer](#social-network-xml-parser-and-visualizer)
  - [Description](#description)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)

## Description

The project involves developing a GUI-based program to parse and visualize an XML file representing a social network of users. The input XML file contains information about users, such as their id, name, posts, and followers, with operations like parsing, error checking and fixing, conversion to JSON, minifying, compression, decompression, prettifying, graph visualization, graph analysis, post search, and undo/redo functionality.

## Features

- **Parsing:** Parse the XML file into a tree structure.
- **Check & Fix Errors:** Identify and fix various errors in the XML file.
- **XML To JSON:** Convert the XML file to JSON format.
- **Minifying:** Decrease the XML file size by removing whitespaces and indentation.
- **Compress:** Reduce the file size.
- **Decompress:** Restore the compressed XML file to its original form.
- **Prettify:** Format the file with proper indentation.
- **Show Graph:** Visualize the social network connections in a graph.
- **Graph Analysis:** Identify the most influential user, most active user, mutual followers, and provide recommendations to follow.
- **Post Search:** Search for posts containing a specific word.
- **Undo/Redo:** Undo or redo previous editing in the XML file.

## Installation

Clone the repository and install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

or Run the application and use the GUI to perform various operations on the social network XML file.
