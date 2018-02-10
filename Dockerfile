FROM python:3
RUN apt-get update && apt-get -y install sudo &&  apt-get install -y wget && rm -rf /var/lib/apt/lists/* && curl -sL https://deb.nodesource.com/setup_9.x | sudo -E bash - && sudo apt install nodejs


# Install Yarn
RUN curl -o- -L https://yarnpkg.com/install.sh | bash 
COPY ./static/yarn.lock /static/yarn.lock
COPY ./static/package.json /static/package.json
COPY ./static/webpack.config.js /static/webpack.config.js
COPY ./static/.babelrc /static/.babelrc
WORKDIR /static
RUN $HOME/.yarn/bin/yarn install
COPY ./static/index.html /static/index.html
COPY ./static/js /static/js
RUN $HOME/.yarn/bin/yarn build
COPY ./server/requirements.txt /server/requirements.txt
WORKDIR /server
ENV READTHEDOCS True
RUN pip install -r ./requirements.txt
COPY ./server/local_config.py /server/local_config.py
COPY ./server/server.py /server/server.py
CMD ["python", "server.py"]

