# vue-components-demo

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).


用户 julytech
密码 jy20180929
邮箱 2065413046@qq.com
npm 推送地址  http://nexus.internal.julytech.cn/repository/npm-hosted/
npm 组地址 http://nexus.internal.julytech.cn/repository/npm-group/
package.json中

"publishConfig": {
    "registry": "http://nexus.internal.julytech.cn/repository/npm-hosted/"
},

npm login --registry=http://nexus.internal.julytech.cn/repository/npm-hosted/
输入上方用户信息登录
 
 https://github.com/cnpm/cnpm


#在package scripts 中添加
 "lib": "vue-cli-service build --target lib --name vue-components-demo --dest lib packages/index.js"

--target: 构建目标，默认为应用模式。这里修改为 lib 启用库模式。

--dest : 输出目录，默认 dist。这里我们改成 lib
--name : 修改为自己的
[entry]: 最后一个参数为入口文件，默认为 src/App.vue。这里我们指定编译 packages/ 组件库目录
执行
npm run lib

#推送
npm publish --registry=http://nexus.internal.julytech.cn/repository/npm-hosted/
#后续推送时需要修改版本 
在其他项目中  npm install  vue-components-demo --registry=http://nexus.internal.julytech.cn/repository/npm-group/

https://www.cnblogs.com/sq-blogs/p/12822328.html