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
                test: /\.jsx?$/,
                loader: 'babel-loader',
                exclude: /node_modules/,
            },
            {
                test: /\.css$/,
                loaders: [
                    'style-loader?sourceMap',
                    'css-loader?modules&importLoaders=1&localIdentName=[path]___[name]__[local]___[hash:base64:5]'
                ]
            }
        ],  
    },
    plugins: [
        new Dotenv({
            path: './.env', // Path to .env file (this is the default) 
        }),
    ],
    watch: true,
    watchOptions: {
        poll: 1000
    }
}


module.exports = config;

