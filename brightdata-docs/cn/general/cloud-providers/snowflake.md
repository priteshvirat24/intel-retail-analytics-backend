> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Snowflake 数据交付配置指南

<Note>
  Snowflake 配置可用于“数据集”交付，但不支持数据收集器（如网页抓取工具）。
</Note>

## 立即开始

为了确保数据集能够高效传输至您的 Snowflake 环境，我们特地提供了详细的分步设置指南。 请按照以下步骤操作：

<Steps>
  <Step title="选择或创建数据库">
    首先，确定是使用现有数据库还是创建新的数据库。 如果选择创建新的数据库，请使用以下命令：

    ```sql theme={null}
    CREATE DATABASE <database>;
    ```

    <Tip>
      请记得将 `<database>` 替换为您希望使用的数据库名称。
    </Tip>
  </Step>

  <Step title="选择或创建架构">
    确定是使用现有架构还是创建新的架构。 默认情况下，所有数据库都包含一个名为 PUBLIC 的架构。 如果希望使用其他架构，请使用以下命令：

    ```sql theme={null}
    CREATE SCHEMA <schema>;
    ```

    <Tip>
      请将 `<schema>` 替换为您自己的架构名称。
    </Tip>
  </Step>

  <Step title="选择或创建仓库">
    选择使用现有仓库还是创建新的仓库。 创建新的仓库时，请参考 Snowflake 针对数据加载场景的仓库配置建议。要创建仓库，请使用以下命令：

    ```sql theme={null}
    CREATE WAREHOUSE <warehouse>;
    ```

    <Tip>
      请将 `<warehouse>` 替换为您希望使用的仓库名称。
    </Tip>
  </Step>

  <Step title="选择或创建内部命名暂存区">
    接下来，选择使用现有内部命名暂存区还是创建新的暂存区。 要创建新的暂存区，请使用以下命令：

    ```sql theme={null}
    CREATE STAGE <stage>;
    ```

    <Tip>
      请记得将 `<stage>` 替换为您希望使用的暂存区名称。
    </Tip>
  </Step>

  <Step title="创建角色">
    您需要创建一个具有所选暂存区写入权限的角色。要创建角色，请使用以下命令：

    ```sql theme={null}
    CREATE ROLE <role_name>;
    ```

    <Tip>请将 `<role_name>` 替换为您选择的角色名称。</Tip>
  </Step>

  <Step title="为角色授予仓库权限">
    接下来，请使用以下命令，为新角色授予所选仓库的必要操作权限：

    ```sql theme={null}
    GRANT OPERATE ON WAREHOUSE <warehouse> TO ROLE <role_name>;
    ```

    <Tip>
      请记得将 `<warehouse>` 和 `<role_name>` 分别替换为具体仓库名称和角色名称。
    </Tip>
  </Step>

  <Step title="为角色启用暂存区写入权限">
    要为角色启用暂存区写入权限，请使用以下命令：

    ```sql theme={null}
    GRANT WRITE ON STAGE <stage> TO ROLE <role_name>;
    ```

    <Tip>
      同样，请将 `<stage>` 和 `<role_name>` 替换为您选择的暂存区名称和角色名称。
    </Tip>
  </Step>

  <Step title="创建 BrightData 用户">
    接下来，创建 BrightData 新用户，用于直接向 Snowflake 上传数据。 请使用以下命令：

    ```sql theme={null}
    create user <user_name>
    PASSWORD = '<password>'
    LOGIN_NAME = <login>
    MUST_CHANGE_PASSWORD = FALSE
    DISABLED = FALSE
    COMMENT = 'user for BrightData to upload data directly into Snowflake'
    ```

    <Tip>
      请将 `<user_name>`、`<password>` 和 `<login>` 分别替换为您选择的用户名、密码和登录名。
    </Tip>
  </Step>

  <Step title="为新用户授予角色权限">
    最后，为新用户授予您创建的角色权限：

    ```sql theme={null}
    GRANT ROLE <role_name> TO USER <user_name>;
    ```

    <Tip>
      请将 `<role_name>` 和 `<user_name>` 替换为您的角色名称和用户名称。
    </Tip>
  </Step>

  <Step title="建立 IP 白名单">
    如果您的 Snowflake 账户启用了网络策略，需要将以下 IP 加入白名单：

    ```sql theme={null}
    ALTER NETWORK POLICY <policy_name>

    SET ALLOWED_IP_LIST=(
        <existing_allowlisted_ips>,
        '35.169.71.210',
        '34.233.211.38',
        '44.194.183.74',
        '54.243.177.151'
    );
    ```

    <Tip>
      请将 `<policy_name>` 替换为您的网络策略名称。  \
      请将 `<existing_whiltelisted_ips>` 替换为当前已列入白名单的 IP 列表。
    </Tip>

    大功告成！您已完成 Snowflake 环境的配置，可以接收来自我们平台的数据了。

    如遇任何问题或需要进一步帮助，请联系我们的支持团队。

    如需了解更多关于数据加载性能和仓库大小注意事项的信息，[请点击此处](https://docs.snowflake.com/en/user-guide/warehouses-overview#impact-on-data-loading)。
  </Step>
</Steps>
