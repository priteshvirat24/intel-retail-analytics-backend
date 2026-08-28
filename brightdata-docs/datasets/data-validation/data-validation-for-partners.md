> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Data validation for partners

> How Bright Data's data staging and validation process works across 250+ domains for partners: error handling, approval workflows and quality checks.

## Overview

We are introducing a new data staging process, enabling both developers and owners to verify and approve datasets before delivery.

The system will facilitate error handling, validation checks, and customization, ensuring accuracy and reliability.

It will help everyone save time, reduce the number of open tickets, and keep the needed level of quality to maintain the level of quality we want.

<img src="https://mintcdn.com/brightdata/0sd4eqxAli7ENzfc/images/datasets/data-validation/data-validation-for-partners/flowchart.png?fit=max&auto=format&n=0sd4eqxAli7ENzfc&q=85&s=ca4afc5308c479971452383206142d7b" alt="flowchart.png" width="1600" height="651" data-path="images/datasets/data-validation/data-validation-for-partners/flowchart.png" />

## How does it work?

Once the dataset snapshot is ready, we run its validation tests.

<Tabs>
  <Tab title="✅ If all the validation tests are okay">
    The customer will get the dataset snapshot with an indication on the CP that all test was passed.
  </Tab>

  <Tab title="❌ If all/some of the validation tests fail">
    The partner will review the issues and will choose:

    1. To fix the failed tests
    2. To deliver the snapshot as it is to the customer (**with an explanation of why this test failed but still override**).

    The customer can then decide (per fail test or as a batch):

    1. If he is willing to accept it as it is
    2. Accept it as it is only for this specific snapshot
    3. Reject it and return it to the partner to fix what needs to be fixed
  </Tab>
</Tabs>

Once the customer approves, the snapshot goes to the delivery phase.

## The validation tests

<AccordionGroup>
  <Accordion title="Uniqueness">
    Ensures a minimum percentage of unique values in the dataset.
  </Accordion>

  <Accordion title="Filling Rate">
    Mandates a minimum percentage for filled values.
  </Accordion>

  <Accordion title="Persistence Validation">
    Makes a field mandatory once filled; triggers an error if left empty afterward.
  </Accordion>

  <Accordion title="Data Stability">
    The value number must not change by more than X amount compared to previous values.
  </Accordion>

  <Accordion title="Type Verification">
    Checks each entry's data type against its field type (e.g., string, number, date) to ensure integrity and flag mismatches for correction before processing.
  </Accordion>

  <Accordion title="Schema and Field Custom Validation">
    Establish a custom rule to validate if the specific field exists and the field value is valid, such as requiring the size string to be 'S', 'M', or 'L'; any other value is considered an error.
  </Accordion>

  <Accordion title="Minimum Records Threshold">
    Requires a minimum of X records for the initial dataset (in specific URL should per the minimum of X records from the total URL inputs)
  </Accordion>

  <Accordion title="Data Size Fluctuation Threshold">
    Validates fluctuations within a +/- X% range.
  </Accordion>
</AccordionGroup>

## **Main components and functionality**

<Frame caption="When clicking on the specific snapshot to review it">
  <img src="https://mintcdn.com/brightdata/0sd4eqxAli7ENzfc/images/datasets/data-validation/data-validation-for-partners/snapshots.png?fit=max&auto=format&n=0sd4eqxAli7ENzfc&q=85&s=044b29ea52c54f33f6abb035d18671d2" alt="snapshots.png" width="1093" height="398" data-path="images/datasets/data-validation/data-validation-for-partners/snapshots.png" />
</Frame>

<AccordionGroup>
  <Accordion title="Dataset test view">
    There are three filter options (All results, Passed, Failed) for dataset test view

    <img src="https://mintcdn.com/brightdata/0sd4eqxAli7ENzfc/images/datasets/data-validation/data-validation-for-partners/dataset-view.png?fit=max&auto=format&n=0sd4eqxAli7ENzfc&q=85&s=90a920477cfd89cb75d487059ad43c35" alt="dataset-view.png" width="1135" height="659" data-path="images/datasets/data-validation/data-validation-for-partners/dataset-view.png" />
  </Accordion>

  <Accordion title="Reparse button">
    This will allow you to reparse the cached data

    <img src="https://mintcdn.com/brightdata/0sd4eqxAli7ENzfc/images/datasets/data-validation/data-validation-for-partners/reparse-button.png?fit=max&auto=format&n=0sd4eqxAli7ENzfc&q=85&s=fda2087b75569d42637cd438525cfa32" alt="reparse-button.png" width="965" height="422" data-path="images/datasets/data-validation/data-validation-for-partners/reparse-button.png" />
  </Accordion>

  <Accordion title="Ignore button">
    An option to override a test because the data seems healthy/or it makes sense that the specific dataset does not meet the threshold (note! In case of an override, you will need to write an explanation to the customer)

    <Frame>
      <img src="https://mintcdn.com/brightdata/0sd4eqxAli7ENzfc/images/datasets/data-validation/data-validation-for-partners/ignore-button.png?fit=max&auto=format&n=0sd4eqxAli7ENzfc&q=85&s=29b47e56f7600109932823441768a601" alt="ignore-button.png" width="683" height="326" data-path="images/datasets/data-validation/data-validation-for-partners/ignore-button.png" />

      <img src="https://mintcdn.com/brightdata/0sd4eqxAli7ENzfc/images/datasets/data-validation/data-validation-for-partners/undo-ignore.png?fit=max&auto=format&n=0sd4eqxAli7ENzfc&q=85&s=2f01caa2f98b7916d2764df5a890faf5" alt="undo-ignore.png" width="1052" height="248" data-path="images/datasets/data-validation/data-validation-for-partners/undo-ignore.png" />
    </Frame>

    <Frame>
      <img src="https://mintcdn.com/brightdata/0sd4eqxAli7ENzfc/images/datasets/data-validation/data-validation-for-partners/confirm-undo.png?fit=max&auto=format&n=0sd4eqxAli7ENzfc&q=85&s=74e92477a7aa2037955cda04616ac926" alt="confirm-undo.png" width="453" height="317" data-path="images/datasets/data-validation/data-validation-for-partners/confirm-undo.png" />
    </Frame>
  </Accordion>

  <Accordion title="“Show related records” and “View & Edit code”">
    In case the test failed, click on the “show related records” to see example of the records and then on “View\&Edit code” to get to the IDE and start fixing the issues

    <img src="https://mintcdn.com/brightdata/0sd4eqxAli7ENzfc/images/datasets/data-validation/data-validation-for-partners/view-edit-code.png?fit=max&auto=format&n=0sd4eqxAli7ENzfc&q=85&s=9db7adcadcb2d29133f0c142e5943101" alt="view-edit-code.png" width="683" height="326" data-path="images/datasets/data-validation/data-validation-for-partners/view-edit-code.png" />
  </Accordion>

  <Accordion title="What is the difference between Reparse or Recrawl?">
    Reparse:

    Reparse involves reprocessing the existing raw data that has already been collected.
    It applies the parsing logic, rules, or transformations to the data without fetching fresh data from the web.
    Reparse is useful when changes are needed in data structure, new fields are added to parsing logic, or existing data needs to be restructured or re-extracted.

    Recrawl:

    Recrawl involves revisiting the source website to collect new or updated data.
    It fetches fresh data directly from the source to reflect recent changes or additions on the website.
    Recrawling is useful when the content on the source website changes frequently, or when up-to-date data is critical for analysis or reporting.
  </Accordion>

  <Accordion title="Reparse or Recrawl buttons">
    Once you finish working on the needed fix, you’ll be able to Reparse or recrawl according to your needs

    <img src="https://mintcdn.com/brightdata/0sd4eqxAli7ENzfc/images/datasets/data-validation/data-validation-for-partners/reparse-recrawl.png?fit=max&auto=format&n=0sd4eqxAli7ENzfc&q=85&s=b3f60cf4974f61bd360a791e9ac040f6" alt="reparse-recrawl.png" width="940" height="459" data-path="images/datasets/data-validation/data-validation-for-partners/reparse-recrawl.png" />
  </Accordion>

  <Accordion title="Rerun test">
    This will allow you to run the validation tests again if needed

    <img src="https://mintcdn.com/brightdata/0sd4eqxAli7ENzfc/images/datasets/data-validation/data-validation-for-partners/rerun-tests.png?fit=max&auto=format&n=0sd4eqxAli7ENzfc&q=85&s=dbb307d62f28c47047908e220862e91f" alt="rerun-tests.png" width="1207" height="653" data-path="images/datasets/data-validation/data-validation-for-partners/rerun-tests.png" />
  </Accordion>

  <Accordion title="IDE button">
    This will allow you to redirect to the IDE in context in case you need to edit the collector and recrawl (e.g in case there are no records at all)

    <img src="https://mintcdn.com/brightdata/0sd4eqxAli7ENzfc/images/datasets/data-validation/data-validation-for-partners/ide-button.png?fit=max&auto=format&n=0sd4eqxAli7ENzfc&q=85&s=95f627d0351a37935dbb0d21360f71cb" alt="ide-button.png" width="1191" height="582" data-path="images/datasets/data-validation/data-validation-for-partners/ide-button.png" />
  </Accordion>

  <Accordion title="Deliver Dataset button">
    After reviewing the needed data and fixing/ignoring issues, you should click on this button and send the snapshot to the owner for review. The ignored tests should be equipped with a reasoning to explain why you chose to ignore the test

    <img src="https://mintcdn.com/brightdata/0sd4eqxAli7ENzfc/images/datasets/data-validation/data-validation-for-partners/deliver-dataset.png?fit=max&auto=format&n=0sd4eqxAli7ENzfc&q=85&s=037130d1c09c0600b90280ddf93ce02f" alt="deliver-dataset.png" width="693" height="219" data-path="images/datasets/data-validation/data-validation-for-partners/deliver-dataset.png" />
  </Accordion>

  <Accordion title="Rejected tests">
    In case not all rejected test was accepted by the owner, the issues will be sent back to you and will be marked with the “Rejected” label for additional fixes and re-sending to the owner for approval

    <img src="https://mintcdn.com/brightdata/0sd4eqxAli7ENzfc/images/datasets/data-validation/data-validation-for-partners/failed.png?fit=max&auto=format&n=0sd4eqxAli7ENzfc&q=85&s=d806269a35b2f0c99114d9bb6d7bc07e" alt="failed.png" width="1045" height="847" data-path="images/datasets/data-validation/data-validation-for-partners/failed.png" />
  </Accordion>
</AccordionGroup>

## Communications and notifications

Status changes and additional notifications will be presented to you as a megaphone on the CP.

## Tickets and bugs

Now, once we introduce the staging process, fixing a collector is not the end of the bug/issue

The process consists of two steps:

1. Fix the collector
2. Fix the snapshot

Hence, the bug processing workflow will be amended to align with the new 2-step process.
<Note>Tickets related to validation issues should not be allowed to be marked as “resolved” before the snapshot is delivered to the dataset owner!</Note>

## Changes to the flow:

We are removing the “Resolve” button from the option on the ticket
