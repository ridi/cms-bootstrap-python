const path = require('path');

const OUTPUT_PATH = path.resolve(__dirname, '..', 'static', 'dist');
const SRC_PATH = path.resolve(__dirname, 'src');

module.exports = {
  devtool: 'cheap-source-map',
  entry: {
    menu: path.resolve(SRC_PATH, 'menu'),
  },
  output: {
    path: OUTPUT_PATH,
    filename: '[name].js',
  },
  resolve: {
    modules: ['node_modules'],
    extensions: ['.js', '.jsx'],
    symlinks: false,
  },
  module: {
    rules: [
      {
        enforce: 'pre',
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        loader: 'eslint-loader',
      },
      {
        test: /\.(js|jsx)$/,
        loader: 'babel-loader',
        include: SRC_PATH,
      },
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader'],
      },
    ],
  },
};
