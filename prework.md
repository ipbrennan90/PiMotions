# Part 0: Prework
## Introduction

This prework should only take you 10 - 15 minutes to complete.
We are going to download necessary tools, and make sure we have a resin account ready to go.

## Prework Steps
- Create a GitHub account (if you need to)
- Generate an SSH key     (if you need to)
- Create a resin.io account
- Download tools

### 1. Create a GitHub account

You will need GitHub account to complete this workshop.
If you do not have a GitHub account, sign up for one [here](https://github.com/join) page.

### 2. Generate an SSH key if you do not have one

If you are unfamiliar with SSH keys, here's a [walkthrough of the following steps](https://git-scm.com/book/en/v2/Git-on-the-Server-Generating-Your-SSH-Public-Key).

We need public-key authentication for this tutorial so we can push code to our Pis.
If you do not have an SSH key or you just created a new GitHub account in Step 1 above, you should do the following:
- [Generate an SSH key](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/)
- [Add it to your account](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/).

You can check to see if you have an existing SSH key by running `ls -al ~/.ssh` in your terminal. This will list the files in your .ssh directory. Look for a file that looks like `id_dsa.pub`, `id_ecdsa.pub`, `id_ed25519.pub`, or `id_rsa.pub`. If you see one, congratulations! You have an public SSH key. Make sure to [add it to your GitHub account ](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/).

If you don't see a key, [generate an SSH key](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/) and [add it to your GitHub account ](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/).

### 3. Create a resin.io account

To make deploying code on our Pi easy, we're going to use a service called [resin.io](https://resin.io/). To learn more about resin.io, [click here](https://docs.resin.io/understanding/understanding-code-deployment/).

1. Sign up for an account at [resin.io](https://resin.io/).
Ideally, use your GitHub account for authentication. This will make the next step very easy.

2. Add your SSH keys to resin.io.
Navigate to the ["Preferences" page in the resin.io dashboard](https://dashboard.resin.io/preferences/sshkeys) to add your SSH keys. Either select "Import from GitHub" (if you authenticated with GitHub), or enter your public SSH key manually. If you are entering your key manually, use `cat ~/.ssh/id_rsa.pub` in the terminal to get an easy to copy version. Make sure you copy the whole thing, including `ssh-rsa`.

### 4. Download Docker and Etcher

1. Download [Docker](https://www.docker.com/community-edition)
2. Download [Etcher](https://etcher.io/)
