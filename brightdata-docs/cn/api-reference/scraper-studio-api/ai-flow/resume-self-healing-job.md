> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 恢复自我修复任务



## OpenAPI

````yaml api-reference/web-scraper-ide-rest-api POST /dca/collectors/{collector_id}/resume_automation_job
openapi: 3.1.0
info:
  title: Brightdata API
  description: API for interaction with datasets marketplace
  version: 1.0.0
servers:
  - url: https://api.brightdata.com
security:
  - bearerAuth: []
paths:
  /dca/collectors/{collector_id}/resume_automation_job:
    post:
      summary: Resume Self-Healing Job
      description: >-
        Approve or reject a Self-Healing job that is paused awaiting user input.
        Call this when [Get Self-Healing Job
        Progress](/api-reference/scraper-studio-api/ai-flow/self-healing-job-progress)
        returns `status: "pending_answer"` with `step: "user_approval"`. Send
        `{"message": true}` to approve the proposed diff and let the job resume,
        or `{"message": false}` to reject it. Add `"auto_save": true` to save
        the approved template automatically once the job completes successfully.
      parameters:
        - name: collector_id
          in: path
          description: >-
            Collector ID returned by the [Create Scraper
            Template](/api-reference/scraper-studio-api/ai-flow/create-scraper-template)
            API endpoint.
          required: true
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ResumeAutomationJobRequest'
      responses:
        '200':
          description: Self-Healing job resumed
components:
  schemas:
    ResumeAutomationJobRequest:
      type: object
      required:
        - message
      properties:
        message:
          type: boolean
          description: >-
            `true` approves the proposed diff and lets the Self-Healing job
            resume. `false` rejects the diff and ends the job.
          example: true
        auto_save:
          type: boolean
          description: >-
            Optional. When `true`, the approved template is saved automatically
            once the Self-Healing job completes successfully. The template is
            saved only if `message` is `true` (you approved the diff) and the
            job succeeds. Currently applies to successful jobs only. Defaults to
            `false`.
          example: true
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      description: >-
        Use your Bright Data API Key as a Bearer token in the Authorization
        header.


        **How to authenticate:**

        1. Obtain your API Key from the Bright Data account settings at
        https://brightdata.com/cp/setting/users

        2. Include the API Key in the Authorization header of your requests

        3. Format: `Authorization: Bearer YOUR_API_KEY`


        **Example:**

        ```

        Authorization: Bearer
        b5648e1096c6442f60a6c4bbbe73f8d2234d3d8324554bd6a7ec8f3f251f07df

        ```


        Learn how to get your Bright Data API key:
        https://docs.brightdata.com/api-reference/authentication
      bearerFormat: API Key

````