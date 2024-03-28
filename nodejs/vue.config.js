const path = require('path');
const Dotenv = require('dotenv-webpack');
const CompressionWebpackPlugin = require('compression-webpack-plugin')

// 웹팩 설정 파일
module.exports = {
  // 페이지 구성
  pages: {
    index: {
      // 페이지를 위한 진입점(entry)
      entry: 'src/main.js',
      // 페이지 제목
      title: '통합 API',
    },
  },
  // 프로덕션 소스 맵(disable)
  productionSourceMap: false,
  // 웹팩 구성
  configureWebpack: {
    // 개발자 도구 설정
    devtool: 'inline-source-map',
    plugins: [
      // dotenv 설정
      new Dotenv({
        path: '.support',
        silent: true
      }),
      // 압축 플러그인 설정
      new CompressionWebpackPlugin({
        filename: '[path].gz[query]',
        algorithm: 'gzip',
        test: new RegExp('\\.(' + productionGzipExtensions.join('|') + ')$'),
        minRatio: 0.8
      })
    ],
    // 출력 파일 설정
    output: {
      filename: 'js/[name].[hash:8].js',
      chunkFilename: 'js/[name].[hash:8].js',
      sourceMapFilename: "js/[name].[hash:8].js.map"
    },
  },
  // 개발 서버 설정
  devServer: {
    // 호스트 설정
    host: '0.0.0.0',
    // 공개 설정
    public: '0.0.0.0' + process.env.VUE_APP_OPEN_WEB_PORT,
    // 핫 모듈 교체 활성화
    hot: true,
    // 정적 자산 압축
    compress: true,
    // 파일 감시 설정
    watchOptions: {
      poll: false,
      ignored: /node_modules/
    },
    // 호스트 확인 비활성화
    disableHostCheck: true,
  },
  // Babel로 변환되어야 하는 종속성 설정
  transpileDependencies: [
    'vuetify',
    'vuetify-dialog',
  ],
};
