> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 用户管理

> 管理用户和权限以访问 Bright Data

# 用户访问类型

Bright Data 提供 3 种主要的用户类型，每种类型对应一个不同的访问渠道：

1. 控制面板用户
2. 使用 API 密钥的 API 用户
3. Proxy Manager 用户

这 3 种不同的访问方式负责在使用任何 Bright Data 服务之前进行身份验证。

它们会分别显示在控制面板“账户设置”中的三个用户与 API 密钥表格中。

## 控制面板用户

控制面板用户可以访问 Bright Data 控制面板，并根据创建用户时分配的权限访问其他服务。

<Note>
  注册 Bright Data 的用户为账户管理员，默认具有管理员权限。
</Note>

### 权限与允许的操作

| 权限         | 操作                                                                                                                                          |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Admin      | 完整账户控制：创建和删除账户、添加/删除/编辑用户、添加/删除/编辑财务和支付方式、添加/删除/编辑 API 密钥、添加/删除/编辑 Proxy Manager 用户、设置 Zone 和用户限制、添加/删除/编辑 Bright Data 服务、使用 Bright Data 服务 |
| Finance    | 添加/删除/编辑财务和支付方式                                                                                                                             |
| Ops        | 添加/删除/编辑 Bright Data 服务                                                                                                                     |
| User       | 使用 Bright Data 服务                                                                                                                           |
| Limit      | 编辑账户限制                                                                                                                                      |
| User limit | 编辑用户使用限制                                                                                                                                    |

## API 密钥

每个控制面板用户都可以拥有一个分配给他的 API 密钥。第一个 API 密钥会自动为创建账户的用户生成。具有管理员权限的用户无法以明文形式查看自己的 API 密钥。

## Proxy Manager 用户

Proxy Manager 用户只能访问 Proxy Manager。可访问的端口权限需要在 Proxy Manager 控制台中设置。此功能仅适用于使用 Proxy Manager 的用户。
