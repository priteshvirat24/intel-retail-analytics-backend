> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Webhook 通知

<table>
  <thead>
    <tr>
      <th>类别</th>
      <th>主题</th>
      <th>产品</th>
      <th>正文</th>
      <th>事件代码</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>账单</td>
      <td>因资金不足导致账户暂停</td>
      <td>不适用</td>
      <td>您的 Bright Data 账户因资金不足已被暂停。</td>
      <td>1000 - Insufficient funds</td>
    </tr>

    <tr>
      <td>账单</td>
      <td>余额不足</td>
      <td>不适用</td>
      <td>您的账户余额为 \$\X，已接近限额。请充值您的账户以避免账户暂停。</td>
      <td>1001 - Low balance</td>
    </tr>

    <tr>
      <td>账单</td>
      <td>自动充值失败</td>
      <td>不适用</td>
      <td>您的支付方式被拒绝，我们无法使用自动充值功能向您的账户添加资金。请重试或使用其他支付方式。</td>
      <td>1002 - Auto recharge failed</td>
    </tr>

    <tr>
      <td>合规性</td>
      <td>因违反 TOS 导致账户禁用</td>
      <td>不适用</td>
      <td>我们检测到您的账户违反了我们的 TOS（服务条款）。请联系我们的合规团队获取更多信息：[compliance@brightdata.com](mailto:compliance@brightdata.com)</td>
      <td>2000 - Account disabled</td>
    </tr>

    <tr>
      <td>合规性</td>
      <td>因验证失败导致账户暂停</td>
      <td>不适用</td>
      <td>您的账户因无法通过验证已被暂停。请联系您的客户经理以获取更多信息邮件。</td>
      <td>2001 - Account suspension due to validation fail</td>
    </tr>

    <tr>
      <td>合规性</td>
      <td>新的禁用 IP</td>
      <td>不适用</td>
      <td>我们检测到来自可疑 IP 地址的请求正在通过您的区域运行。我们已将这些 IP 地址添加到您的禁用列表。</td>
      <td>2002 - Denylisted IPs</td>
    </tr>

    <tr>
      <td>网络健康</td>
      <td>Web Unlocker API 服务中断开始</td>
      <td>Web Unlocker API</td>
      <td>Web Unlocker API 目前在您的目标域上的成功率较低。</td>
      <td>4000 - Web Unlocker API service disruption start</td>
    </tr>

    <tr>
      <td>网络健康</td>
      <td>Web Unlocker API 服务中断结束</td>
      <td>Web Unlocker API</td>
      <td>我们已解决此问题，Web Unlocker API 现在在您的目标域上表现出高成功率。</td>
      <td>4001 - Web Unlocker API service disruption end</td>
    </tr>

    <tr>
      <td>网络健康</td>
      <td>服务中断开始</td>
      <td>网络</td>
      <td>我们的网络已宕机。我们正在努力修复，一旦恢复，我们会立即通知您。</td>
      <td>4002 - Outage start</td>
    </tr>

    <tr>
      <td>网络健康</td>
      <td>服务中断结束</td>
      <td>网络</td>
      <td>我们已修复此问题，插入网络网络已恢复运行。</td>
      <td>4003 - Outage end</td>
    </tr>

    <tr>
      <td>维护</td>
      <td>计划的 IP 替换</td>
      <td>DC/ISP</td>
      <td>我们计划在插入日期和时间更改我们的 DC 和 ISP 网络中的 IP 范围 添加受影响列表的链接（与电子邮件中相同）</td>
      <td>5000 - Future IP replacement</td>
    </tr>

    <tr>
      <td>维护</td>
      <td>IP 替换完成</td>
      <td>DC/ISP</td>
      <td>IP 替换已完成。添加受影响列表的链接（与电子邮件中相同）</td>
      <td>5001 - IP replacement completed</td>
    </tr>

    <tr>
      <td>维护</td>
      <td>Gips 已释放</td>
      <td>Residential/Mobile</td>
      <td>以下 gips 已从您的区域释放 添加受影响列表的链接</td>
      <td>5004 - gips released</td>
    </tr>

    <tr>
      <td>维护</td>
      <td>Gips 已替换</td>
      <td>Residential/Mobile</td>
      <td>以下 gips 已从您的区域释放并替换为新的 gips 添加受影响列表的链接</td>
      <td>5005 - gips were changed</td>
    </tr>

    <tr>
      <td>维护</td>
      <td>计划的维护</td>
      <td>任何</td>
      <td>我们正在对 XYZ 进行维护，计划于插入日期和时间进行。</td>
      <td>5002 - Future maintenance</td>
    </tr>

    <tr>
      <td>维护</td>
      <td>维护完成</td>
      <td>任何</td>
      <td>对 XYZ 的维护已完成。</td>
      <td>5003 - Maintenance completed</td>
    </tr>

    <tr>
      <td>测试</td>
      <td>测试通知</td>
      <td>不适用</td>
      <td>此通知是从您的控制面板发送的，用于测试您的 Webhook URL。如果您能看到此消息，则表示它运行正常。</td>
      <td>9000 - Test notification</td>
    </tr>
  </tbody>
</table>
