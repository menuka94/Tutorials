let webpack = require('webpack');
let path = require('path');

module.exports = {
    entry: './js/main.js',
    output: {
        path: path.resolve(__dirname, 'public/js'),
        filename: 'bundle.js',
        publicPath: './public'
    },
    plugins: [],
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                loader: 'babel-loader'
            }
        ]
    },
    node: {
        fs: 'empty'
    },
    resolve: {
        alias: {
            'handlebars': 'handlebars'
        }
    },
    resolveLoader: {
        alias: {
            'hbs': 'handlebars-loader'
        }
    }
};

if(process.env.NODE_ENV === 'production') {
    module.exports.plugins.push(
        new webpack.LoaderOptionsPlugin({
            minimize: true,
            sourceMap: true
        })
    );

    module.exports.plugins.push(
        new webpack.DefinePlugin({
            'process.env': {
                NODE_ENV: 'production'
            }
        })
    );
}