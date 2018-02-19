const webpack = require('webpack');
const Dotenv = require('dotenv-webpack');
const ExtractTextPlugin = require('extract-text-webpack-plugin');

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
                test: /\.jsx?$/,
                loader: 'babel-loader',
                exclude: /node_modules/,
            },
            {
                test: /\.css$/,
                loader: ExtractTextPlugin.extract('css-loader')
            }
        ],  
    },
    plugins: [
        new Dotenv({
            path: './.env', // Path to .env file (this is the default) 
        }),
        new ExtractTextPlugin('style.css')
    ],
    watch: true,
    watchOptions: {
        poll: 1000
    }
}


module.exports = config;

