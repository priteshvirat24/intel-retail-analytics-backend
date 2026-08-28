> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 所有区域的带宽统计

> 获取您所有区域的带宽统计

<Tip>
  将您的 API key 粘贴到授权字段中。要获取 API key，请[创建账号](https://www.bright.cn/?hs_signup=1\&utm_source=docs\&utm_campaign=playground)，并查看[如何生成新的 API key？](/cn/api-reference/authentication#如何生成新的-api-key？)
</Tip>

<Note>示例响应已隐藏</Note>


## OpenAPI

````yaml cn-openapi GET /customer/bw
openapi: 3.0.1
info:
  title: Bright Data API
  description: 将 Bright Data API 集成到您的流程中，以实现高端的爬取精度
  version: 1.0.0
servers:
  - url: https://api.brightdata.com
security:
  - bearerAuth: []
paths:
  /customer/bw:
    get:
      description: 获取所有区域的带宽统计信息
      parameters:
        - in: query
          name: from
          description: 开始时间
          required: false
          schema:
            type: string
          example: '2018-07-01T00:00:00'
        - in: query
          name: to
          description: 结束时间
          required: false
          schema:
            type: string
          example: '2018-07-02T00:00:00'
      responses:
        '200':
          description: 成功
          content:
            application/json:
              schema:
                type: object
                example:
                  ID:
                    customer_id: CUST_ID
                    from: '2022-10-01T00:00:00.000Z'
                    to: '2022-11-24T00:00:00.000Z'
                    data:
                      data_center: {}
                      isp: {}
                      residential: {}
                      mobile: {}
                      unlocker: {}
                      v__ub_browser: {}
                      serp: {}
                      dc_elastic: {}
                      isp1: {}
                      test_zone: {}
                      test_zone2: {}
                      japan: {}
                      zone1_res_ex: {}
                      zone5_isp: {}
                      zone1: {}
                      zone2: {}
                      zum_rails_res_canada: {}
                      zone3: {}
                      elastic_log_test: {}
                      google_async: {}
                      last_value_ts: '2022-11-23T13:41:20.099Z'
                      last_update_ts: '2022-11-23T14:05:55.108Z'
                      sums: {}
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      description: >-
        在 Authorization 头中使用您的 Bright Data API Key 作为 Bearer token。


        **认证方法:**

        1. 从 Bright Data 账户设置获取您的 API Key:
        https://brightdata.com/cp/setting/users

        2. 在请求的 Authorization 头中包含 API Key

        3. 格式: `Authorization: Bearer YOUR_API_KEY`


        **示例:**

        ```

        Authorization: Bearer
        b5648e1096c6442f60a6c4bbbe73f8d2234d3d8324554bd6a7ec8f3f251f07df

        ```


        了解如何获取 Bright Data API Key:
        https://docs.brightdata.com/cn/api-reference/authentication#如何生成新的-api-key？
      bearerFormat: API Key

````