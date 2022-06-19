<h1>notification-gateway-lite</h1>

# 简介

notification-gateway-lite 是一个非常轻量的通知网关，可以聚合各种推送渠道，使用 Serverless 部署，几乎零成本运行。

> ## 更新
> - v0.1.5
>   - 修复 PushDeer 支持
> - v0.1.4
>   - 新增 debug 模式，详见 [环境变量](docs/Env.md) 
> - v0.1.3
>   - 支持同时推送到多个渠道，见 [接口文档](docs/Api.md/#multi-channel)
> - v0.1.2
>   - 支持 `POST` 等更多接口，详见 [接口文档](docs/Api.md)
>   - 新增 [在线版接口文档](https://service-epwdrzxg-1255787947.gz.apigw.tencentcs.com/release/docs)

# 特性

- 等同于免费、开源、可自建的 [新版Server酱](https://sct.ftqq.com/)，没有任何限制，痛快推送
- 支持各种常见的推送渠道，如Bark、企业微信等
- 支持部署成腾讯云Serverless，几乎零成本运行
- 解决因为群晖DSM奇怪的webhook设置方式而无法接入一些推送渠道的问题

## 目前支持的通知方式

- [Bark](https://github.com/Finb/Bark)
- [企业微信应用消息](https://developer.work.weixin.qq.com/document/path/90236)
- [企业微信机器人webhook](https://developer.work.weixin.qq.com/document/path/91770)
- [PushDeer](http://pushdeer.com)
- [Pushover](https://pushover.net/api) [未测试]

### 可能会支持的推送方式
- [ ] 钉钉
- [ ] Chanify
- [ ] ...

> 如果有需要的通知方式，请提交 [issue](https://github.com/LeslieLeung/notification-gateway-lite/issues/new?assignees=LeslieLeung&labels=enhancement&template=feature_request.md&title=)


# 部署方式

- [腾讯云Serverless](docs/deploy/TencentcloudServerless.md)
- [阿里云Serverless](docs/deploy/AliyunServerless.md)
- [华为云Serverless（WIP)](docs/deploy/HuaweicloudServerless.md)
- [Docker](docs/deploy/Docker.md) （支持 `arm64`、`amd64`架构）

# 接口文档

见 [在线版接口文档](https://service-epwdrzxg-1255787947.gz.apigw.tencentcs.com/release/docs) 或 [接口文档](docs/Api.md)

# 示例应用

- [使用 notification-gateway-lite 接收群晖DSM推送](docs/example/DSM.md)

# 微信交流群
![](http://img.ameow.xyz/202206180147750.jpg)