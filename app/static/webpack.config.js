const webpack = require('webpack');
const Dotenv = require('dotenv-webpack');

const config = {
    entry: __dirname + '/js/index.jsx',
    output: {
        path: __dirname + '/dist',
        filename: 'bundle.js',

    },
    resolve: {
        extensions: [ '.js', '.jsx', '.css']
    },
    module: {
        rules: [
            {
                test: /\.jsx?/,
                exclude: /node_modules/,
                use: 'babel-loader'
            }
        ]
    },
    plugins: [
        new Dotenv({
            path: './.env', // Path to .env file (this is the default) 
        })
    ],
    watch: true,
    watchOptions: {
        poll: 1000
    }
}


module.exports = config;

