> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 账单

<Info>
  我们网站上公布的所有价格均以美元计价
</Info>

<AccordionGroup>
  <Accordion title="Bright Data 的账单如何运作？">
    **最低月度承诺** - 只要您的账户处于“活动”状态，您就需要承诺在每个月月初支付一笔最低金额。该最低承诺将设置您的基本使用限制：一旦您的使用量超过最低承诺金额，您将需要添加额外资金才能继续使用我们的服务。

    <Note>
      了解更多信息，请访问我们的[定价页面](https://www.bright.cn/pricing)。
    </Note>
  </Accordion>

  <Accordion title="如何重新验证我的账户以解决账单问题？">
    如果您的账户被屏蔽，您将立即收到一封电子邮件，解释如何解决问题。请联系您的专属客户经理或 Bright Data 的合规团队：[compliance@brightdata.com](mailto:compliance@brightdata.com)。要恢复您被屏蔽的账户，您需要提供以下信息：

    <Tabs>
      <Tab title="注册公司">
        * 公司注册表格
        * 被标记的付款方式的照片
      </Tab>

      <Tab title="非注册公司">
        * 照片身份证明、驾驶执照或护照
        * 被标记的付款方式的照片
      </Tab>
    </Tabs>
  </Accordion>

  <Accordion title="如果我只使用数据中心 IP，Bright Data 的账单周期如何运作？">
    当客户仅使用数据中心 IP 时，我们会按日计算他们的成本。我们从您账户中的当前余额中减去每日成本，显示可供使用的剩余余额。成本是根据所使用的 IP 类型（共享与专用）以及使用的带宽/GB 进行计算的。我们还会计算添加功能（如独占时间或专用域/主机）的任何额外成本。\
    您将在每月的 1 号收到上述成本的账单。您账户中剩余的余额将反映可供将来使用的金额。
  </Accordion>

  <Accordion title="Bright Data 的账单周期如何运作？">
    Bright Data 的账单周期从每月的 1 号开始。这意味着只要您的账户状态处于活动状态，您每月账户承诺的费用将在每月的 1 号自动计费。
  </Accordion>

  <Accordion title="如果我在账单周期中途（月中）加入 Bright Data，会发生什么？">
    如果您在月中加入 Bright Data，您的第一次最低账户承诺付款将在您加入当天收取，并且使用量将仅追溯应用于当月您的账户处于活动状态的天数。

    **示例**：您于 6 月 25 日加入 Bright Data 住宅网络，您的价格计划有 \$500 的最低月度承诺，您支付了您的第一笔款项 \$500。

    7 月 1 日会发生什么？

    * 我们的系统将看到您的账户在 6 月份只活动了 6 天，占当月的 20%，因此最低月度承诺的相对部分将是 \$100。除非您的使用成本高于此金额，否则 \$100 将是您 6 月份的成本。
    * 我们将向您发送发票，并从您的余额中扣除 \$100 作为 6 月份的费用，您的余额剩余 \$400。
    * 由于在每月的 1 号您的余额需要符合您的最低月度承诺，我们现在将从您的信用卡中收取 \$100，以便将其补足至 \$500，以符合您 7 月份的最低月度承诺。
  </Accordion>

  <Accordion title="我会收到发票吗？">
    是的。您将在该月的第三个以色列工作日收到发票。发票将提供您上个月的使用详情。它将细分您的使用量与您的最低账户承诺（以及，如果适用，当月添加的任何额外资金）之间的关系。
  </Accordion>

  <Accordion title="我的账单周期使用的是哪个时区？">
    所有账单计算均根据我们仪表板的时区 UTC+0 进行。这会对您的账单产生什么影响？您可以选择启用和禁用您的区域 (Zone)。启用/禁用的时间将以 UTC 时间为准，因此每日费用将相应地应用。
  </Accordion>

  <Accordion title="我不会每天使用 Bright Data，而是按项目使用。我仍然需要支付全部最低月度承诺吗？">
    ### 代理服务计费

    代理服务要么按代理数量（IP 地址）预付，要么按使用量预付。

    | 网络类型                         | 代理类型                       | 付款类型                                                     | 备注                           |
    | ---------------------------- | -------------------------- | -------------------------------------------------------- | ---------------------------- |
    | 数据中心 (Datacenter)            | 共享池 (Shared pool)          | 按 GB 计费 (per GB)                                         | 无使用量：无付款。                    |
    | 数据中心 (Datacenter)            | 共享无限 (Shared unlimited)    | 按 IP 预付 (Prepaid per IP)                                 | 默认每月恢复                       |
    | 数据中心 (Datacenter)            | 专用无限 (Dedicated unlimited) | 按 IP 预付 (Prepaid per IP)                                 | 默认每月恢复                       |
    | ISP                          | 共享池 (Shared pool)          | 按 GB 计费 (per GB)                                         | 无使用量：无付款。                    |
    | ISP                          | 共享无限 (Shared unlimited)    | 按 IP 预付 (Prepaid per IP)                                 | 默认每月恢复                       |
    | ISP                          | 专用无限 (Dedicated unlimited) | 按 IP 预付 (Prepaid per IP)                                 | 默认每月恢复                       |
    | 住宅共享 (Residential shared)    | 全部: IPv4,IPv4+IPv6, IPv6   | 按 GB 计费 (per GB)                                         | 无使用量，无付款                     |
    | 住宅专用 (Residential dedicated) | 专用 `gIP`s                  | 每 `gIP` 固定收费 + 按 GB 计费 (Fixed charge per `gIP` + per GB) | `gIP` 费用默认每月恢复，在 1 号计费，按比例计算 |

    ### 非代理服务

    在您不使用我们服务的期间，您可以关闭您的区域 (Zone)。服务费用将仅适用于服务处于活动状态的当月相对部分。所有账单计算均根据我们仪表板的时区 UTC+0 进行。这会对您的账单产生什么影响？您可以选择启用和禁用您的区域 (Zone)。启用/禁用的时间将以 UTC 时间为准，因此每日费用将相应地应用。
  </Accordion>

  <Accordion title="如果我发起拒付争议，会发生什么？">
    如果您发起信用卡拒付或银行争议，且理由不合理，Bright Data 将收取每笔 \$150 的手续费。
  </Accordion>

  <Accordion title="为什么我的账户因账单问题被屏蔽？">
    账户因以下原因之一而被屏蔽：

    * 付款方式与个人详情之间存在差异
    * 用户登录的国家/地区与其信用卡所在国家/地区不同
    * 尝试处理被拒绝的付款次数过多
    * 未能使用 3D Secure 验证信用卡付款
  </Accordion>

  <Accordion title="如何将用户添加到发票接收人列表？">
    要将电子邮件地址添加到发票接收人列表，请遵循以下指南

    <Steps>
      <Step title="点击控制面板侧边栏上的“账单”按钮" />

      <Step title="向下滚动页面" />

      <Step title="在“发票接收人”屏幕中，点击“+ 添加新接收人”按钮">
        <Frame>
          <img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/account/management/invoice_recipients_1.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=8f85b9e6a3f8f35cf7b94d3d19f4c5f3" alt="invoice_recipients_1.png" width="1832" height="971" data-path="images/general/account/management/invoice_recipients_1.png" />
        </Frame>
      </Step>

      <Step title="添加姓名和电子邮件地址">
        <Frame>
          <img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/account/management/invoice_recipients_2.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=775e999a7c53ac894194f1d5d553a181" alt="invoice_recipients_2.png" width="1832" height="971" data-path="images/general/account/management/invoice_recipients_2.png" />
        </Frame>
      </Step>

      <Step title="点击“添加”按钮">
        <Frame>
          <img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/account/management/invoice_recipients_3.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=c4926f87348eb17c07129c979da4da65" alt="invoice_recipients_3.png" width="1832" height="971" data-path="images/general/account/management/invoice_recipients_3.png" />
        </Frame>
      </Step>
    </Steps>
  </Accordion>

  <Accordion title="如果我的账户并非整个月都处于“活动”状态，会发生什么？">
    如果您的余额中在非活动月份仍有剩余资金，您不会失去余额，但会在下个月的 1 号被收取费用以将该余额补足至最低月度承诺。

    <Frame>
      <img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/account/management/suspend-account.gif?s=1f7aa443b673927577f8f6644e77c820" alt="suspend-account.gif" width="1636" height="930" data-path="images/general/account/management/suspend-account.gif" />
    </Frame>
  </Accordion>

  <Accordion title="如何防止我的账户被暂停？">
    为确保您的账户永不被暂停，我们强烈建议您使用我们的自动充值选项。可以在您账户的“账单”部分激活它，并确保不间断的服务。当您的可用余额低于总账户余额的 85% 时，自动充值开始生效。设置的金额完全由您决定，可以是任何面额。

    <Frame>
      <img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/account/management/billing.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=9aa42b4c5724f04ccc0cbfa706325f39" alt="billing.png" width="1636" height="908" data-path="images/general/account/management/billing.png" />

      <img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/account/management/payment-settings.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=77d833a82d9a4bf4e960141a59edb3a0" alt="payment-settings.png" width="1636" height="906" data-path="images/general/account/management/payment-settings.png" />

      <img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/account/management/confirm.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=352ac14a0c59372dc95d1fae3d6c4cb9" alt="confirm.png" width="1636" height="930" data-path="images/general/account/management/confirm.png" />
    </Frame>
  </Accordion>

  <Accordion title="首次存款匹配优惠如何运作？">
    当您首次向账户存款时，我们将以一美元对一美元的方式进行匹配。
  </Accordion>

  <Accordion title="我可以获得的最大奖金是多少？">
    我们将匹配您的存款，最高限额为 \$500。例如，如果您存款 \$500，您将获得额外的 \$500 促销积分。如果您存款 \$600，您仍将获得最高 \$500 的积分。
  </Accordion>

  <Accordion title="使用奖金积分有时间限制吗？">
    是的。匹配的促销积分必须在添加到您账户之日起 90 天内使用。
  </Accordion>

  <Accordion title="保持奖金积分有效有哪些要求？">
    是的。为了保持奖金，您必须每月至少使用 \$5 的账户。如果您的使用量低于此金额，剩余的奖金积分可能会被没收。
  </Accordion>
</AccordionGroup>
