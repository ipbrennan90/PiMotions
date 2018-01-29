FROM resin/%%RESIN_MACHINE_NAME%%-python:latest
RUN apt-get update && apt-get install -y wget && rm -rf /var/lib/apt/lists/*
# Install node
RUN curl -sL https://deb.nodesource.com/setup_9.x | sudo -E bash - && sudo apt install nodejs
# Install Yarn
RUN curl -o- -L https://yarnpkg.com/install.sh | bash 
# Install Pipenv
RUN pip install pipenv
COPY ./static/yarn.lock /static/yarn.lock
COPY ./static/package.json /static/package.json
COPY ./static/webpack.config.js /static/webpack.config.js
COPY ./static/.babelrc /static/.babelrc
WORKDIR /static
RUN $HOME/.yarn/bin/yarn install
COPY ./static/index.html /static/index.html
COPY ./static/js /static/js
COPY ./justin_smells.jpeg /justin_smells.jpeg
RUN $HOME/.yarn/bin/yarn build
COPY ./server/Pipfile /server/Pipfile
COPY ./server/Pipfile.lock /server/Pipfile.lock
WORKDIR /server
RUN pipenv install --system
COPY ./server/server.py /server/server.py
CMD ["python", "server.py"]

