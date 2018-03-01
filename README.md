# Welcome!
## Introduction

We're excited that you are joining us to dive into the wonders of the [Raspberry Pi Zero W](https://www.raspberrypi.org/products/raspberry-pi-zero-w/) today. As you may know, a Raspberry Pi is a tiny, affordable computer we can use to build all kinds of things. A Pi Zero W, the Pi we will work with today, is the smallest Pi.

In this tutorial, we're going to build a web application that can take a picture using our Pi with the click of a button.

## Overview
We're going to cover a lot of ground in this tutorial, even if our final product seems simple!

By the end, you should know:
1. How to program your Pi
1. How to communicate with your Pi from a web application
1. How to extend the application we build together, if you want to. :tada:

**Important:**
If you're proceeding to the tutorial, we assume you have a GitHub account. If you do not have a GitHub account, sign up for one [here](https://github.com/join) page.
If you're creating a new GitHub account, you'll also need to [generate an SSH key](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/) and [add it to your account](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/).

Since we need public-key authentication for this tutorial so we can push code to our Pis, if you do not have an SSH key, you should [generate one](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/).

## Tutorial Steps
- Fork and clone this repo to your own machine.
- Get the application running locally
- Set up a resin.io account and learn about what resin.io can do.
- Configure your Pi with a Resin image.
- Get the application talking to the Pi!

Since this tutorial is focused on working with a Pi, we've written the code for the web application for you. That way you don't have to fixate on debugging code when you want to learn about a Pi. If you want more of a challenge, you are welcome to modify or extend the existing code in any way you'd like.

### 1. Fork, clone
[Detailed steps here if you need them!](https://help.github.com/articles/fork-a-repo/)

1. Fork the repo to your own account.
2. Clone: `git@github.com:your-username/PiMotions.git`
3. Navigate into the directory: `cd PiMotions`
4. Rename the `.env.example` file to `.env`

### 2. Download some tools

1. Download [Docker](https://www.docker.com/community-edition)
2. Download [Etcher](https://etcher.io/)

### 3. Set up and configure your resin.io application

To make deploying code on our Pi easy, we're going to use a service called [resin.io](https://resin.io/).
To learn more about resin.io, [click here](https://docs.resin.io/understanding/understanding-code-deployment/).

1. Sign up for an account at [resin.io](https://resin.io/). Ideally, use your GitHub account for authentication.

2. You'll see a prompt to create a new application.
    1. Set Device Type to "Raspberry Pi (v1 or Zero)"
    1. Give your application a name!
    1. Click "Create New Application"

3. Click "Add device" to configure a resinOS image specifically for your application. Choose the recommend resinOS version, then toggle on "Development" under "Select Edition" and "Wifi + Ethernet" under "Network Connection".
4. Enter the WiFi SSID and passphrase, and then click "Download".

While the resinOS image is downloading, do the following:

5. Navigate to the ["Preferences" page in the resin.io dashboard](https://dashboard.resin.io/preferences/sshkeys) to add your SSH keys. Either select "Import from GitHub" (if you authenticated with GitHub), or enter your public SSH key manually. If you are entering your key manually, use `cat ~/.ssh/id_rsa.pub` in the terminal to get an easy to copy version. Make sure you copy the whole thing, including `ssh-rsa`.

You can read more about finding your SSH key or generating a new one [here](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/). 
You can check to see if you have an existing SSH key by [following the steps here](https://help.github.com/articles/checking-for-existing-ssh-keys/).

6. From your resin.io dashboard, set device configuration variables by clicking on "Fleet Configuration". Add the following two device config variables:
- NAME: `RESIN_HOST_CONFIG_gpu_mem` VALUE: `128`
- NAME: `RESIN_HOST_CONFIG_start_x` VALUE: `1`

These variables make sure that the camera works on the Pi.

7. If you aren't already there, navigate in your terminal to your project directory (`cd PiMotions`). Add a resin.io remote repo by copying the `git remote add` command in the top right of your dashboard. 

### 4. Make a bootable SD card

Once the resinOS image has downloaded and we've completed our configuration steps, we'll use Etcher to flash the image onto our SD card. (You may be asked to grant admin permissions to Etcher.)

1. Open Etcher.
2. Insert your SD card into your computer.
3. Using Etcher, click "Select Image" and find the image you downloaded in step 3 above.
4. Click "Flash!"

Once Etcher finishes creating the bootable SD card, it will eject it for you.
While you're waiting for Etcher to finish, you can move on to step 6. (Step 5 requires the SD card).

### 5. Set up your Pi

1. Insert the SD card into your Pi.
2. Plug your Pi into your computer or a power source using a micro USB cable. (We need power!)
3. It make take a few minutes, but your Pi should appear on your [resin.io dashboard](https://dashboard.resin.io/apps).

### 6. Deploy code to your Pi

1. From your project directory, run `git push resin master`

This is going to deploy the code in the `server/` directory to our Pi.
If you're curious, you can look at the `Dockerfile.template` file to see the commands that are run.

Note: this may ask you to add this host to your list of allowed hosts. Type 'yes'.

When you see a unicorn appear in your terminal, your push was successful!

It may take a few minutes.

### 7. Get the app running locally

1. `cd app/static`
2. Run `npm run docker-build`

This will build a Docker image based on our Dockerfile and start our containers. Your app will now be running, so you can navigate to `localhost:80` in your browser to check it out.

Note: We don't need to build the Docker image every time we want to start our app. If you want to start the app without rebuilding the image, you can run `npm run start`, which runs `docker-compose up` for us.

3. Navigate to `localhost:80` in your browser. You should see the app running there.

4. Click on "Webcam" under "Image Source" and then click "Take a Picture".

### 8. Get the web app and the Pi talking to each other

Now we have an web app running locally that can take a picture using our computer's webcam.
The next step is to get the web app and the Pi talking to each other, so we can use the Pi's camera to take a picture.

Right now, the "R Pi" button under "Image Source" doesn't do anything. We're about to fix that.

1. Enable a public url for your device. Go into `Actions` on your resin.io device dashboard and click 'Enable All Public Device URLs'.
Copy the public url and paste it into `app/static/.env` as the value for `RASPI_URL`.

```
RASPI_URL=<your public url here>
```
2. Navigate to `localhost:80` in your browser. Click on "R Pi" under "Image Source", and then click "Take Picture".

:tada::tada::tada:

Your web app is now set up to take pictures using your computer's webcam and using your Pi.

**In the next stage, we'll write code to detect motion using the picamera.**
