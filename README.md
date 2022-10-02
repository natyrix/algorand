# Algorand


***

End-to-End Web3 dApps: certificate generation, distribution, and value transfer with Algorand NFTs and smart contracts

**Table of Contents**
- [Algorand](#Algorand)
  - [Overview](#overview)
  - [About](#about)
  - [Project Structure](#project-structure)
    - [.github](#.github)
    - [notebooks](#notebooks)
    - [scripts](#scripts)
    - [tests](#tests)
    - [root folder](#root-folder)
  - [Installation guide](#Installation-guide)

***

## Overview

End-to-end Web3 dapps on the Algorand Blockchain that will help 10 Academy generate and distribute Non-Fungible Tokens (NFTs) as certificates that will represent the successful completion of a weekly challenge to trainees, and allow trainees with NFTs to interact with a smart contract to perform pre-defined actions.  


## About


In this project, the client is 10 Academy; the client would like to solve the challenge of ensuring that certificates are available to all trainees in a secure way, and (if possible) that certificate holders can benefit from smart contract actions now and in the future.  At present, certificates are distributed as simple PDF files, without the ability to verify their authenticity nor can 10 Academy undertake smart actions with the trainees/their contracts.

## Why Algorand

![Alt text](alg.jpeg?raw=true "Why Algorand")


## Project Structure
The repository has a number of files including python scripts, jupyter notebooks, raw and cleaned data, and text files. Here is their structure with a brief explanation.


### .github
- a configuration file for github actions and workflow


### notebooks
- `playground.ipynb`: a jupyter notebook holding different interaction with Algorand API using python sdk


***
# Algorand Explorer
![Alt text](explorer_img_1.png?raw=true "Tech stack")

***

### root folder
- `requirements.txt`: a text file lsiting the projet's dependancies
- `.gitignore`: a text file listing files and folders to be ignored
- `README.md`: Markdown text with a brief explanation of the project and the repository structure.
- `.teal`: Compiled teal files of a smart contract written using pyteal.


***
# Algorand Assets Explorer
![Alt text](explorer_img_3.png?raw=true "Tech stack")

***

### scripts
- `helpers.py`: helper functions for the smart contract
- `contracts.py`: smart contract for splitting funds transaction


## Installation guide
Django Server
```
git clone https://github.com/natyrix/algorand
cd algorand
pip install -r requirements.txt 
python manage.py migrate
python manage.py runserver
```
React Frontend
```
git clone https://github.com/natyrix/algorand
cd algorand_front_end
npm install
npm start
```

***

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]


[contributors-shield]: https://img.shields.io/github/contributors/natyrix/algorand.svg?style=for-the-badge
[contributors-url]: https://github.com/natyrix/algorand/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/natyrix/algorand.svg?style=for-the-badge
[forks-url]: https://github.com/natyrix/algorand/network/members
[stars-shield]: https://img.shields.io/github/stars/natyrix/algorand.svg?style=for-the-badge
[stars-url]: https://github.com/natyrix/algorand/stargazers
[issues-shield]: https://img.shields.io/github/issues/natyrix/algorand.svg?style=for-the-badge
[issues-url]: https://github.com/natyrix/algorand/issues