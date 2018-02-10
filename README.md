# Welcome!
## Introduction

We're excited that you are joining us to dive into the wonders of the [Raspberry Pi Zero W](https://www.raspberrypi.org/products/raspberry-pi-zero-w/) today. As you may know, a Raspberry Pi is a tiny, affordable computer we can use to build all kinds of things. A Pi Zero W, the Pi we will work with today, is one of the smaller Pis.

In this tutorial, we're going to build a web application that can take a picture using our Pi with the click of a button.

This tutorial is for people with a little experience with writing code, but no experience programming a Pi.
If you've never coded before, don't know how to push and pull code from GitHub, or need some more background, check out our [Setup 101](#) page.

## Overview
We're going to cover a lot of ground in this tutorial, even if our final product seems simple!
By the end, you should know:
1. How to program your Pi
1. How to communicate with your Pi from a web application
1. How to extend the application we build together, if you want to. :tada:

**Important:**
If you're proceeding to the tutorial, we assume you have a GitHub account, are able to clone a repo, can pull from a repo, and can push to a repo. If you do not have a GitHub account or are not sure how to do any or all of the above, check out our [Setup 101](#) page.

## Tutorial Steps
- [ ] 1. Fork and clone this repo to your own machine.
- [ ] 2. Get the application running locally (?)
- [ ] 3. Set up a Resin.io account and learn about what Resin.io can do.
- [ ] 4. Configure your Pi with a Resin image.
- [ ] 5. Get the application talking to the Pi!

Since this tutorial is focused on working with a Pi, we've written the code for the web application for you. That way you don't have to fixate on debugging code when you want to learn about a Pi! If you want more of a challenge, you are welcome to modify or extend the existing code in any way you'd like.

### 1. Fork, clone
[Detailed steps here if you need them!](https://help.github.com/articles/fork-a-repo/)

1. Fork the repo to your own account.
2. Clone: `git@github.com:your-username/take-my-picture.git`
3. Navigate into the directory: `cd take-my-picture`

### 2. Get the app running locally
1. `mv server/local_config.template.py server/local_config.py`
2. `docker build -t <your_container_name> .`
3. `docker run -d -p 80:80 <your_container_name>:latest`
4. navigate to `localhost:80` in your browser, you should see the app running there
TODO

### 3. Set up a Resin.io account and application

To make deploying code on our Pi easy, we're going to use a service called [Resin.io](https://resin.io/). Resin.io will make it easy for us to deploy our code on our Pis.

[More about Resin.io](https://docs.resin.io/understanding/understanding-code-deployment/)

1. Sign up an account at [Resin.io](https://resin.io/).

2. You'll see a prompt to create a new application.
    1. Set Device Type to "Raspberry Pi (v1 or Zero)"
    1. Give your application a name!
    1. Click "Create New Application"

### 4. Set up your Pi!
TODO: flash pi with resin image

### 5. Make the magic happen :tada:
TODO:
diagram explaining setup
clicking the button, taking a picture, walking through the code.
