> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 区域带宽统计

> 获取区域的带宽统计信息

<Tip>
  将您的 API key 粘贴到授权字段中。要获取 API key，请[创建账号](https://www.bright.cn/?hs_signup=1\&utm_source=docs\&utm_campaign=playground)，并查看[如何生成新的 API key？](/cn/api-reference/authentication#如何生成新的-api-key？)
</Tip>


## OpenAPI

````yaml cn-openapi GET /zone/bw
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
  /zone/bw:
    get:
      description: 获取区域的带宽统计信息
      parameters:
        - in: query
          name: zone
          description: 区域名称
          required: true
          schema:
            type: string
          example: resi-zone-1
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
                  'ID:':
                    customer_id: customer_id
                    from: '2022-10-01T00:00:00.000Z'
                    to: '2022-11-23T00:00:00.000Z'
                    data:
                      static:
                        bw_sum:
                          - 0
                          - 745
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 6960
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                        bw_dn:
                          - 0
                          - 525
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 5990
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                        bw_up:
                          - 0
                          - 220
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 970
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                        http_direct_req:
                          - 0
                          - 1
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                        bw_sum_dc:
                          - 0
                          - 745
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 6960
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                        bw_api:
                          - 0
                          - 745
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 6960
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                        https_direct_req:
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 1
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                    last_value_ts: '2022-11-19T19:08:51.546Z'
                    last_update_ts: '2022-11-22T11:35:32.122Z'
                    sums:
                      static:
                        back_m1:
                          bw_sum: 745
                          bw_dn: 525
                          bw_up: 220
                          http_direct_req: 1
                          bw_sum_dc: 745
                          bw_api: 745
                          https_direct_req: 0
                        back_m0:
                          bw_sum: 6960
                          bw_dn: 5990
                          bw_up: 970
                          http_direct_req: 0
                          bw_sum_dc: 6960
                          bw_api: 6960
                          https_direct_req: 1
                        back_d2:
                          bw_sum: 0
                          bw_dn: 0
                          bw_up: 0
                          http_direct_req: 0
                          bw_sum_dc: 0
                          bw_api: 0
                          https_direct_req: 0
                        back_d1:
                          bw_sum: 0
                          bw_dn: 0
                          bw_up: 0
                          http_direct_req: 0
                          bw_sum_dc: 0
                          bw_api: 0
                          https_direct_req: 0
                        back_d0:
                          bw_sum: 0
                          bw_dn: 0
                          bw_up: 0
                          http_direct_req: 0
                          bw_sum_dc: 0
                          bw_api: 0
                          https_direct_req: 0
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