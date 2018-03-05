| Table Of Contents                   |
| ------------------------------------|
| [Introduction](README.md)           |
| Part 0: Prework                     |
| [Part 1: Pi and Web App](part1.md)  |
| [Part 2: Motion Detection](part2.md)|

# Part 0: Prework
## Introduction

This prework should only take you 10 - 15 minutes to complete.
We are going to download necessary tools, and make sure we have a resin.io account ready to go.

## Prework Steps
- Download tools
- Create a GitHub account (if you need to)
- Generate an SSH key     (if you need to)
- Create a resin.io account

### Follow the instructions based on your operating system:

Click to expand:

<details><summary>For Windows Users</summary>
<p>

### 1. Download Git for Windows
If you're on Windows, download Git for Windows [here](https://gitforwindows.org).
Click through the installation steps. You don't need to change any of the default options.

Open Git Bash if it does not open automatically. (Search for it in the Start Menu).

### 2. Download additional tools
1. Download [Docker](https://www.docker.com/community-edition)

Docker may ask you to restart your computer or "Allow the application to make changes".

2. Download [Etcher](https://etcher.io/)

3. Download [NodeJS](https://nodejs.org/en/)

Download the option recommended for most users.

### 3. Create a GitHub account (if you need to)

You will need GitHub account to complete this workshop.
If you do not have a GitHub account, [sign up for one here](https://github.com/join).

Select "Unlimited Public Repositories" (the free tier), and then proceed through the signup.
Verify your email.

### 4. Generate an SSH key (if you need to)

We need public-key authentication for this tutorial so we can push code to our Pis.

- You can check to see if you have an existing SSH key by running `ls -al ~/.ssh` in your Git Bash terminal. This will list the files in your .ssh directory. Look for a file that looks like `id_rsa.pub`. If you see one, congratulations! You have an public SSH key.

- If you do not have an SSH key or you just created a new GitHub account in Step 1 above, you should create one by running `ssh-keygen` in your terminal.

**To add your SSH key to your GitHub account:**
- Run `clip < ~/.ssh/id_rsa.pub` in your terminal to copy it.
- Go to your GitHub account, click on your profile avatar in the upper right-hand corner, select "Settings", and then click on "SSH and GPG Keys".
- Click "New SSH Key" and then paste what you copied from the terminal into the text box. Click "Add SSH Key".

**Helpful Links**

If you are unfamiliar with SSH keys, here's a more detailed [walkthrough](https://git-scm.com/book/en/v2/Git-on-the-Server-Generating-Your-SSH-Public-Key).

If you're having trouble, here are step-by-step instructions from GitHub:
- [Generate an SSH key](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/)
- [Add it to your account](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/).

### 5. Create a resin.io account

To make deploying code on our Pi easy, we're going to use a service called [resin.io](https://resin.io/). To learn more about resin.io, [click here](https://docs.resin.io/understanding/understanding-code-deployment/).

1. Sign up for an account at [resin.io](https://resin.io/).
Ideally, use your GitHub account for authentication. This will make the next step very easy.

2. Add your SSH keys to resin.io.
Navigate to the ["Preferences" page in the resin.io dashboard](https://dashboard.resin.io/preferences/sshkeys) to add your SSH keys. Either select "Import from GitHub" (if you authenticated with GitHub), or enter your public SSH key manually. If you are entering your key manually, you can paste the key you copied in the earlier step, or use `cat ~/.ssh/id_rsa.pub` in the terminal to print the key to the screen. Make sure you copy the whole thing, including `ssh-rsa`.

[I'm done with the prework. Take me to Part 1!](part1.md)
</p>
</details>


<details><summary>For OS X/Linux users</summary>
<p>

### 1. Download tools

1. Download [Docker](https://www.docker.com/community-edition)

2. Download [Etcher](https://etcher.io/)

3. Check to make sure NodeJS is downloaded by running `node -v`
If NodeJS is not installed, install it with a package manager, or [download it here](https://nodejs.org/en/)

### 2. Create a GitHub account (if you need to)

You will need GitHub account to complete this workshop.
If you do not have a GitHub account, [sign up for one here](https://github.com/join).

Select "Unlimited Public Repositories" (the free tier), and then proceed through the signup.
Verify your email.

### 3. Generate an SSH key (if you need to)

We need public-key authentication for this tutorial so we can push code to our Pis.

- You can check to see if you have an existing SSH key by running `ls -al ~/.ssh` in your terminal. This will list the files in your .ssh directory. Look for a file that looks like `id_rsa.pub`. If you see one, congratulations! You have an public SSH key.

- If you do not have an SSH key or you just created a new GitHub account in Step 1 above, you should create one by running `ssh-keygen` in your terminal.

**To add your SSH key to your GitHub account:**
- Copy your SSH key by running `cat ~/.ssh/id_rsa.pub` in the terminal.
- Copy the output. Make sure you copy the entire output, including `ssh-rsa`.
- Go to your GitHub account, click on your profile avatar in the upper right-hand corner, select "Settings", and then click on "SSH and GPG Keys".
- Click "New SSH Key" and then paste what you copied from the terminal into the text box. Click "Add SSH Key".

**Helpful Links**

If you are unfamiliar with SSH keys, here's a more detailed [walkthrough](https://git-scm.com/book/en/v2/Git-on-the-Server-Generating-Your-SSH-Public-Key).

If you're having trouble, here are step-by-step instructions from GitHub:
- [Generate an SSH key](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/)
- [Add it to your account](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/).

### 4. Create a resin.io account

To make deploying code on our Pi easy, we're going to use a service called [resin.io](https://resin.io/). To learn more about resin.io, [click here](https://docs.resin.io/understanding/understanding-code-deployment/).

1. Sign up for an account at [resin.io](https://resin.io/).
Ideally, use your GitHub account for authentication. This will make the next step very easy.

2. Add your SSH keys to resin.io.
Navigate to the ["Preferences" page in the resin.io dashboard](https://dashboard.resin.io/preferences/sshkeys) to add your SSH keys. Either select "Import from GitHub" (if you authenticated with GitHub), or enter your public SSH key manually. If you are entering your key manually, you can paste the key you copied in the earlier step, or use `cat ~/.ssh/id_rsa.pub` in the terminal to print the key to the screen. Make sure you copy the whole thing, including `ssh-rsa`.

[I'm done with the prework. Take me to Part 1!](part1.md)

</p>
</details>
