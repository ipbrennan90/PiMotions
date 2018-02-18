FROM python:3

# Install Node
RUN apt-get update && apt-get -y install sudo &&  apt-get install -y wget && rm -rf /var/lib/apt/lists/* && curl -sL https://deb.nodesource.com/setup_9.x | sudo -E bash - && sudo apt install nodejs

# Install Yarn
RUN curl -o- -L https://yarnpkg.com/install.sh | bash 

# Copy Application
COPY ./static/yarn.lock /static/yarn.lock
COPY ./static/package.json /static/package.json
COPY ./static/webpack.config.js /static/webpack.config.js
COPY ./static/.babelrc /static/.babelrc
WORKDIR /static

# Install Dependencies
RUN $HOME/.yarn/bin/yarn install
COPY ./static/index.html /static/index.html
COPY ./static/js /static/js

# Build Static
RUN $HOME/.yarn/bin/yarn watch

# Copy Flask Server Requirements File
COPY ./server/requirements.txt /server/requirements.txt
WORKDIR /server
ENV READTHEDOCS True

#Install Flask Server Dependencies
RUN pip install -r ./requirements.txt

# Copying this separately after dependencies are installed since
# this will be the most changed file and should not tell docker to re-install dependencies upon changes
COPY ./server/server.py /server/server.py

# Command to run upon successful docker install
CMD ["python", "server.py"]

