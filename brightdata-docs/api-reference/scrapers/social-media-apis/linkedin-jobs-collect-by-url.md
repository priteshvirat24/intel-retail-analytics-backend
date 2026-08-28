> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Collect LinkedIn jobs by URL

> Collect structured LinkedIn job posting data by URL using the Bright Data Web Scraper API with dataset ID gd_lpfll7v5hcqtkxl6l for job details and metadata.

## Query Parameters

<ParamField query="dataset_id" type="string" default="gd_lpfll7v5hcqtkxl6l" required>
  The dataset ID used for this request.

  <Warning>
    Must be set to `gd_lpfll7v5hcqtkxl6l` to collect **Jobs by URL** data.
  </Warning>
</ParamField>

<ParamField query="notify" type="boolean" default={false}>
  Whether to send notifications when the request is completed.
</ParamField>

<ParamField query="include_errors" type="boolean" default={true}>
  Whether to include errors in the response.
</ParamField>

## Request Body

<ParamField body="input" type="object[]" required>
  An array of input objects.

  <Expandable title="properties">
    <ParamField body="url" type="string" required>
      The URL of the LinkedIn job listing to collect.
    </ParamField>
  </Expandable>

  #### Example

  ```json theme={null}
  {
    "input":[
      {"url":"https://www.linkedin.com/jobs/view/software-engineer-at-epic-3986111804?_l=en"},
      {"url":"https://www.linkedin.com/jobs/view/software-engineer-at-pave-4310512612/"}
    ]
  }
  ```
</ParamField>

<ResponseExample>
  ```json 200 theme={null}
  [
    {
      "url": "https://www.linkedin.com/jobs/view/pharmacy-technician-at-walmart-4385163817?_l=en",
      "job_posting_id": "4385163817",
      "job_title": "Pharmacy Technician",
      "company_name": "Walmart",
      "company_id": "2646",
      "job_location": "Fayetteville, NC",
      "job_summary": "Hourly Wage: $16 - $29 per/hour The actual hourly rate will equal or exceed the required minimum wage applicable to the job location. Additional Compensation Includes Annual Or Quarterly Performance Incentives. Additional compensation in the form of premiums may be paid in amounts ranging from $0.35 per hour to $3.00 per hour in specific circumstances. Premiums may be based on schedule, facility, season, or specific work performed. Multiple premiums may apply if applicable criteria are met. Employment Type: Part-Time Available shifts: Mid-Shift, Closing Location Walmart Supercenter #3595 7701 S RAEFORD RD, FAYETTEVILLE, NC, 28304, US Job Overview Pharmacy associates focus on the needs of our customers as they entrust us with their prescriptions and health needs. They are responsible for inputting and processing prescriptions, supporting patients with product information, and providing customer service in our store pharmacies. Benefits & perks At Walmart, we offer competitive pay as well as performance-based incentive awards and other great benefits for a happier mind, body, and wallet. Health benefits include medical, vision and dental coverage. Financial benefits include 401(k), stock purchase and company-paid life insurance. Paid time off benefits include parental leave, family care leave, bereavement, jury duty, and voting. Other benefits include short-term and long-term disability, company discounts, Military Leave Pay, adoption and surrogacy expense reimbursement, and more. You will also receive PTO and/or PPTO that can be used for vacation, sick leave, holidays, or other purposes. The amount you receive depends on your job classification and length of employment. It will meet or exceed the requirements of paid sick leave laws, where applicable. For information about PTO, see Smart Guide page Live Better U is a Walmart-paid education benefit program for full-time and part-time associates in Walmart and Sam's Club facilities. Programs range from high school completion to bachelor's degrees, including English Language Learning and short-form certificates. Tuition, books, and fees are completely paid for by Walmart. Eligibility requirements apply to some benefits and may depend on your job classification and length of employment. Benefits are subject to change and may be subject to a specific plan or program terms. For information about benefits and eligibility, see One.Walmart.com. Walmart is committed to maintaining a drug-free workplace and has a no tolerance policy regarding the use of illegal drugs and alcohol on the job. This policy applies to all employees and aims to create a safe and productive work environment. Show more Show less",
      "job_seniority_level": "Entry level",
      "job_function": "Health Care Provider",
      "job_employment_type": "Part-time",
      "job_industries": "Retail",
      "job_base_pay_range": "$16.00/hr - $29.00/hr",
      "company_url": "https://www.linkedin.com/company/walmart?trk=public_jobs_topcard-org-name",
      "job_posted_time": "4 days ago",
      "job_num_applicants": 25,
      "discovery_input": {
        "experience_level": null,
        "job_type": null,
        "remote": null,
        "selective_search": null,
        "time_range": null
      },
      "apply_link": null,
      "country_code": "US",
      "title_id": "1062",
      "company_logo": "https://media.licdn.com/dms/image/v2/D560BAQHZkPdlecGssw/company-logo_100_100/company-logo_100_100/0/1736779000209/walmart_logo?e=2147483647&v=beta&t=tWcWIFSyHtICTzTLIPiYeKCp21XucI-HWijZdWwYR-A",
      "job_posted_date": "2026-03-13T09:48:59.171Z",
      "job_poster": {
        "name": null,
        "title": null,
        "url": null
      },
      "application_availability": true,
      "job_description_formatted": "<section class=\"show-more-less-html\" data-max-lines=\"5\">\n        <div class=\"show-more-less-html__markup show-more-less-html__markup--clamp-after-5\n            relative overflow-hidden\">\n          Hourly Wage: <strong>$16 - $29 per/hour<br><br></strong><ul><li>The actual hourly rate will equal or exceed the required minimum wage applicable to the job location.<br><br></li></ul><strong>Additional Compensation Includes Annual Or Quarterly Performance Incentives.<br><br></strong>Additional compensation in the form of premiums may be paid in amounts ranging from $0.35 per hour to $3.00 per hour in specific circumstances. Premiums may be based on schedule, facility, season, or specific work performed. Multiple premiums may apply if applicable criteria are met.<br><br>Employment Type: <strong>Part-Time<br><br></strong>Available shifts: <strong>Mid-Shift, Closing<br><br></strong>Location<br><br><strong>Walmart Supercenter #3595<br><br></strong>7701 S RAEFORD RD, FAYETTEVILLE, NC, 28304, US<br><br><strong>Job Overview<br><br></strong>Pharmacy associates focus on the needs of our customers as they entrust us with their prescriptions and health needs. They are responsible for inputting and processing prescriptions, supporting patients with product information, and providing customer service in our store pharmacies.<br><br>Benefits &amp; perks<br><br>At Walmart, we offer competitive pay as well as performance-based incentive awards and other great benefits for a happier mind, body, and wallet. Health benefits include medical, vision and dental coverage. Financial benefits include 401(k), stock purchase and company-paid life insurance. Paid time off benefits include parental leave, family care leave, bereavement, jury duty, and voting. Other benefits include short-term and long-term disability, company discounts, Military Leave Pay, adoption and surrogacy expense reimbursement, and more.<br><br>You will also receive PTO and/or PPTO that can be used for vacation, sick leave, holidays, or other purposes. The amount you receive depends on your job classification and length of employment. It will meet or exceed the requirements of paid sick leave laws, where applicable. For information about PTO, see Smart Guide page<br><br>Live Better U is a Walmart-paid education benefit program for full-time and part-time associates in Walmart and Sam&apos;s Club facilities. Programs range from high school completion to bachelor&apos;s degrees, including English Language Learning and short-form certificates. Tuition, books, and fees are completely paid for by Walmart.<br><br>Eligibility requirements apply to some benefits and may depend on your job classification and length of employment. Benefits are subject to change and may be subject to a specific plan or program terms. For information about benefits and eligibility, see One.Walmart.com.<br><br>Walmart is committed to maintaining a drug-free workplace and has a no tolerance policy regarding the use of illegal drugs and alcohol on the job. This policy applies to all employees and aims to create a safe and productive work environment.\n        </div>\n\n        \n\n    \n    \n    \n\n    <button class=\"show-more-less-html__button show-more-less-button\n        show-more-less-html__button--more\n        ml-0.5\" data-tracking-control-name=\"public_jobs_show-more-html-btn\" aria-label=\"Show more\" aria-expanded=\"false\">\n<!---->\n        \n            Show more\n          \n\n          <icon class=\"show-more-less-html__button-icon show-more-less-button-icon\" data-delayed-url=\"https://static.licdn.com/aero-v1/sc/h/cyolgscd0imw2ldqppkrb84vo\"></icon>\n    </button>\n  \n\n        \n\n    \n    \n    \n\n    <button class=\"show-more-less-html__button show-more-less-button\n        show-more-less-html__button--less\n        ml-0.5\" data-tracking-control-name=\"public_jobs_show-less-html-btn\" aria-label=\"Show less\" aria-expanded=\"true\">\n<!---->\n        \n            Show less\n          \n\n          <icon class=\"show-more-less-html__button-icon show-more-less-button-icon\" data-delayed-url=\"https://static.licdn.com/aero-v1/sc/h/4chtt12k98xwnba1nimld2oyg\"></icon>\n    </button>\n  \n<!---->    </section>",
      "base_salary": {
        "currency": "$",
        "max_amount": 29,
        "min_amount": 16,
        "payment_period": "hr"
      },
      "salary_standards": "This range is provided by Walmart. Your actual pay will be based on your skills and experience — talk with your recruiter to learn more.",
      "is_easy_apply": false
    }
  ]
  ```
</ResponseExample>


## OpenAPI

````yaml api-reference/sdk-specs/linkedin-jobs-collect-by-url POST /datasets/v3/scrape
openapi: 3.0.0
info:
  title: Collect LinkedIn Jobs by URL
  version: 1.0.0
servers:
  - url: https://api.brightdata.com
security: []
paths:
  /datasets/v3/scrape:
    post:
      summary: Collect LinkedIn Jobs by URL
      description: >-
        Collect structured LinkedIn job posting data by URL using the Bright
        Data Web Scraper API with dataset ID gd_lpfll7v5hcqtkxl6l for job
        details and metadata.
      parameters:
        - in: query
          name: dataset_id
          required: true
          schema:
            type: string
            default: gd_lpfll7v5hcqtkxl6l
          description: Must be `gd_lpfll7v5hcqtkxl6l` for this dataset.
        - in: query
          name: notify
          required: false
          schema:
            type: boolean
            default: false
          description: Send notifications when the request is completed.
        - in: query
          name: include_errors
          required: false
          schema:
            type: boolean
            default: true
          description: Include errors in the response.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - input
              properties:
                input:
                  type: array
                  description: >-
                    Array of input objects. See `Request Body` below for the
                    supported fields.
                  items:
                    type: object
                    required:
                      - url
                    properties:
                      url:
                        type: string
                        example: https://www.linkedin.com/jobs/view/123456
      responses:
        '200':
          description: OK. See response example below the parameters.
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
      x-codeSamples:
        - lang: shell
          label: cURL
          source: |-
            curl --request POST \
              --url 'https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_lpfll7v5hcqtkxl6l&include_errors=true' \
              --header "Authorization: Bearer YOUR_API_KEY" \
              --header "Content-Type: application/json" \
              --data '{"input": [{"url": "https://www.linkedin.com/jobs/view/123456"}]}'
        - lang: python
          label: Python
          source: >-
            import requests


            url =
            "https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_lpfll7v5hcqtkxl6l&include_errors=true"

            headers = {
                "Authorization": "Bearer YOUR_API_KEY",
                "Content-Type": "application/json",
            }

            payload = {
                "input": [
                    {
                        "url": "https://www.linkedin.com/jobs/view/123456"
                    }
                ]
            }


            response = requests.post(url, headers=headers, json=payload)

            print(response.text)
        - lang: py
          label: Python SDK
          source: |-
            # Install: pip install brightdata-sdk
            from brightdata import BrightDataClient

            async with BrightDataClient(api_key="YOUR_API_KEY") as client:
                result = await client.scrape.linkedin.jobs(url="https://www.linkedin.com/jobs/view/123456")
                print(result.data)
        - lang: javascript
          label: JavaScript
          source: >-
            const response = await
            fetch("https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_lpfll7v5hcqtkxl6l&include_errors=true",
            {
              method: "POST",
              headers: {
                "Authorization": "Bearer YOUR_API_KEY",
                "Content-Type": "application/json",
              },
              body: JSON.stringify({
                "input": [
                    {
                        "url": "https://www.linkedin.com/jobs/view/123456"
                    }
                ]
            }),

            });


            const data = await response.text();

            console.log(data);
        - lang: js
          label: JavaScript SDK
          source: >-
            // Install: npm install @brightdata/sdk

            import { bdclient } from '@brightdata/sdk';


            const client = new bdclient({ apiKey: 'YOUR_API_KEY' });


            const result = await
            client.scrape.linkedin.collectJobs(['https://www.linkedin.com/jobs/view/123456']);

            console.log(result);


            await client.close();
        - lang: php
          label: PHP
          source: >-
            <?php

            $ch =
            curl_init("https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_lpfll7v5hcqtkxl6l&include_errors=true");

            curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");

            curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

            curl_setopt($ch, CURLOPT_HTTPHEADER, [
                "Authorization: Bearer YOUR_API_KEY",
                "Content-Type: application/json",
            ]);

            curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode([
                "input" => [
                    [
                        "url" => "https://www.linkedin.com/jobs/view/123456"
                    ]
                ]
            ]));


            $response = curl_exec($ch);

            curl_close($ch);

            echo $response;
        - lang: go
          label: Go
          source: "package main\n\nimport (\n\t\"bytes\"\n\t\"fmt\"\n\t\"io\"\n\t\"net/http\"\n)\n\nfunc main() {\n\tpayload := []byte(\"{\\\"input\\\": [{\\\"url\\\": \\\"https://www.linkedin.com/jobs/view/123456\\\"}]}\")\n\treq, _ := http.NewRequest(\"POST\", \"https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_lpfll7v5hcqtkxl6l&include_errors=true\", bytes.NewBuffer(payload))\n\treq.Header.Set(\"Authorization\", \"Bearer YOUR_API_KEY\")\n\treq.Header.Set(\"Content-Type\", \"application/json\")\n\n\tres, err := http.DefaultClient.Do(req)\n\tif err != nil { panic(err) }\n\tdefer res.Body.Close()\n\n\tbody, _ := io.ReadAll(res.Body)\n\tfmt.Println(string(body))\n}"
        - lang: java
          label: Java
          source: |-
            import java.net.URI;
            import java.net.http.HttpClient;
            import java.net.http.HttpRequest;
            import java.net.http.HttpResponse;

            public class Main {
                public static void main(String[] args) throws Exception {
                    String body = "{\"input\": [{\"url\": \"https://www.linkedin.com/jobs/view/123456\"}]}";
                    HttpRequest request = HttpRequest.newBuilder()
                        .uri(URI.create("https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_lpfll7v5hcqtkxl6l&include_errors=true"))
                        .header("Authorization", "Bearer YOUR_API_KEY")
                        .header("Content-Type", "application/json")
                        .method("POST", HttpRequest.BodyPublishers.ofString(body))
                        .build();

                    HttpResponse<String> response = HttpClient.newHttpClient()
                        .send(request, HttpResponse.BodyHandlers.ofString());
                    System.out.println(response.body());
                }
            }
        - lang: ruby
          label: Ruby
          source: >-
            require 'net/http'

            require 'json'

            require 'uri'


            uri =
            URI.parse("https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_lpfll7v5hcqtkxl6l&include_errors=true")

            request = Net::HTTP::Post.new(uri)

            request["Authorization"] = "Bearer YOUR_API_KEY"

            request["Content-Type"] = "application/json"

            request.body = {"input": [{"url":
            "https://www.linkedin.com/jobs/view/123456"}]}.to_json


            response = Net::HTTP.start(uri.hostname, uri.port, use_ssl: true) {
            |http| http.request(request) }

            puts response.body

````