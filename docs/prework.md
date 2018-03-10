| Table Of Contents                   |
| ------------------------------------|
| [Introduction](../README.md)        |
| Part 0: Prework                     |
| [Part 1: Pi and Web App](part1.md)  |
| [Part 2: Motion Detection](part2.md)|

# Part 0: Prework
## Introduction

This prework should only take you 10 - 15 minutes to complete.

We are going to download the necessary tools, and make sure we have a resin.io account ready to go.

## Prework Steps
- Download tools
- Create a GitHub account (if you need to)
- Generate an SSH key     (if you need to)
- Create a resin.io account

### Follow the instructions based on your operating system:

Click to expand:

<details><summary>For Windows users</summary>
<p>

### 1. Download necessary tools

1. Download Git for Windows [here](https://gitforwindows.org).

Click through the installation steps. You don't need to change any of the default options.

Open Git Bash if it does not open automatically. (Search for it in the Start Menu, and then double-click to launch).

2. [Download Docker](https://store.docker.com/editions/community/docker-ce-desktop-windows)

Click the link above, and then click "Get Docker".
Docker may ask you to restart your computer or "Allow the application to make changes".
Docker may also ask for "privileged access".

If you have an older Windows version, you may need to install Docker Toolbox. Please follow [the install steps here](https://docs.docker.com/toolbox/toolbox_install_windows/).

3. [Download NodeJS](https://nodejs.org/en/)

Download the option recommended for most users.

4. (Optional) Download a text editor

If you don't already have a text editor downloaded, you'll want one for the workshop. We recommend [Atom](https://atom.io/) or [Sublime Text](https://www.sublimetext.com/). (Either will do).

### 3. Create a GitHub account (if needed)

You will need a GitHub account to complete this workshop.
If you do not have a GitHub account, [sign up for one here](https://github.com/join).

Select "Unlimited Public Repositories" (the free tier), and then proceed through the signup. You can skip most of the steps if you'd like.

**Make sure to verify your account!**
GitHub will send you an email after you sign up prompting you to verify your account. Make sure to click the verification link in the email.

### 4. Generate an SSH key and add it to GitHub (if needed)

We need public-key authentication for this tutorial so we can push code to our Raspberry Pis.

- You can check to see if you have an existing SSH key by running `ls -al ~/.ssh` in your Git Bash terminal. This will list the files in your .ssh directory. Look for a file that looks like `id_rsa.pub`. If you see one, congratulations! You have an public SSH key.

- If you do not have an SSH key or you just created a new GitHub account in Step 1 above, you should create one by running `ssh-keygen` in your terminal. `ssh-keygen` will return output similar to the following:
```
  Generating public/private rsa key pair.
  Enter file in which to save the key:
```
Press enter. You'll then see another prompt:  
```
Enter passphrase (empty for no passphrase):
```
You can press enter to proceed without a passphrase, or type in a passphrase and press enter. You'll see a final prompt:
```
Enter same passphrase again:
```
If you left the passphrase empty, press enter. If you entered a passphrase earlier, re-enter it here.

**To add your SSH key to your GitHub account:**
- Run `clip < ~/.ssh/id_rsa.pub` in your terminal to copy it.

(If the `clip` command isn't working, you can run `cat ~/.ssh/id_rsa.pub` instead, which will print your public key to the screen. Copy the key, making sure you copy the entire output, including `ssh-rsa`).

- Go to your GitHub account, click on your profile avatar in the upper right-hand corner, select "Settings", and then click on "SSH and GPG Keys".

- Click "New SSH Key" and then paste what you copied from the terminal into the text box. Add a title. The title can be anything that's a helpful identifier. An example would be something like "work laptop". Once you've decided on a title, click "Add SSH Key" to save the key.

**Helpful Links**

If you're having trouble, here are step-by-step instructions from GitHub:
- [Generate an SSH key](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/)
- [Add an SSH key to your GitHub account](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/).

### 5. Create a resin.io staging account

To make deploying code to our Pi easy, we're going to use a service called resin.io.

1. Sign up for an account at [dashboard.resinstaging.io](https://dashboard.resinstaging.io/).

Ideally, use your GitHub account for authentication. This will make the next step very easy.

2. Add your SSH keys to resin.io.

[Click here](https://dashboard.resinstaging.io/preferences/sshkeys) to add your SSH keys to the resin.io dashboard. Either select "Import from GitHub" (if you authenticated with GitHub), or enter your public SSH key manually. If you are entering your key manually, you can paste the key you copied in the earlier step, or use `cat ~/.ssh/id_rsa.pub` in the terminal to print the key to the screen. Make sure you copy the whole thing, including `ssh-rsa`.

**If you've finished this step, you're done with the prework!**

[Take me to Part 1!](part1.md)
</p>
</details>


<details><summary>For OS X/Linux users</summary>
<p>

### 1. Download tools

1. [Download Docker](https://www.docker.com/community-edition)

Click the link above, and then scroll down until you see "Download Docker Community Edition".
Download the right option for your computer, and then follow the installation process.

Note: Docker may ask you to restart your computer or "Allow the application to make changes".

2. [Download NodeJS](https://nodejs.org/en/)

Download the option recommended for most users.

3. (Optional) Download a text editor

If you don't already have a text editor downloaded, you'll want one for the workshop. We recommend [Atom](https://atom.io/) or [Sublime Text](https://www.sublimetext.com/). (Either will do).

### 2. Create a GitHub account (if needed)

You will need a GitHub account to complete this workshop.
If you do not have a GitHub account, [sign up for one here](https://github.com/join).

Select "Unlimited Public Repositories" (the free tier), and then proceed through the signup. You can skip most of the steps if you'd like.

**Make sure to verify your account!**
GitHub will send you an email after you sign up prompting you to verify your account. Make sure to click the verification link in the email.

### 3. Generate an SSH key and add it to GitHub (if needed)

We need public-key authentication for this tutorial so we can push code to our Raspberry Pis.

- You can check to see if you have an existing SSH key by running `ls -al ~/.ssh` in your terminal. This will list the files in your .ssh directory. Look for a file that looks like `id_rsa.pub`. If you see one, congratulations! You have an public SSH key.

- If you do not have an SSH key or you just created a new GitHub account in Step 1 above, you should create one by running `ssh-keygen` in your terminal. `ssh-keygen` will return output similar to the following:
```
  Generating public/private rsa key pair.
  Enter file in which to save the key:
```
Press enter. You'll then see another prompt:  
```
Enter passphrase (empty for no passphrase):
```
You can press enter to proceed without a passphrase, or type in a passphrase and press enter. You'll see a final prompt:
```
Enter same passphrase again:
```
If you left the passphrase empty, press enter. If you entered a passphrase earlier, re-enter it here.

**To add your SSH key to your GitHub account:**
- Run `cat ~/.ssh/id_rsa.pub` in your terminal, which will output the key to the terminal.
- Copy the output. Make sure you copy the entire output, including `ssh-rsa`.
- Go to your GitHub account, click on your profile avatar in the upper right-hand corner, select "Settings", and then click on "SSH and GPG Keys".
- Click "New SSH Key" and then paste what you copied from the terminal into the text box. Add a title. The title can be anything that's a helpful identifier. An example would be something like "work laptop". Once you've decided on a title, click "Add SSH Key" to save the key.

**Helpful Links**

If you're having trouble, here are step-by-step instructions from GitHub:
- [Generate an SSH key](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/)
- [Add an SSH key to your GitHub account](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/).

### 4. Create a resin.io staging account

To make deploying code to our Pi easy, we're going to use a service called resin.io.

1. Sign up for an account at [dashboard.resinstaging.io](https://dashboard.resinstaging.io/).

Ideally, use your GitHub account for authentication. This will make the next step very easy.

2. Add your SSH keys to resin.io.

Navigate to the ["Preferences" page in the resin.io dashboard](https://dashboard.resinstaging.io/preferences/sshkeys) to add your SSH keys. Either select "Import from GitHub" (if you authenticated with GitHub), or enter your public SSH key manually. If you are entering your key manually, you can paste the key you copied in the earlier step, or use `cat ~/.ssh/id_rsa.pub` in the terminal to print the key to the screen. Make sure you copy the whole thing, including `ssh-rsa`.

**If you've finished this step, you're done with the prework!**

[Take me to Part 1!](part1.md)

</p>
</details>
