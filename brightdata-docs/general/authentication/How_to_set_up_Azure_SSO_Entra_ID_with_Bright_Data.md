> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Azure Entra ID SSO setup

> Step-by-step guide to configuring Azure Entra ID (formerly Azure Active Directory) SSO and SCIM provisioning with Bright Data in 6 steps.

* Prepare application

* Setup SSO

* Setup SCIM provisioning

## How to prepare the application

* Go to [https://entra.microsoft.com/](https://entra.microsoft.com/) and log in to your account.

* Create Enterprise application:

<img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/authentication/entra-sso/entra_1.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=0b6841796c55c9bc15a9ab79b3e3c2da" alt="Microsoft Entra admin center with the Create Enterprise application button" width="1827" height="928" data-path="images/general/authentication/entra-sso/entra_1.png" />

* Click “Create your own application”

* Enter name of your application

* Select “Integrate any other application you don't find in the gallery (Non-gallery)”

* Click “Create”

<img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/authentication/entra-sso/entra_2.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=c54195cfb5f04ee5783b13b680a0a3f3" alt="Entra Create your own application dialog with non-gallery option selected" width="1827" height="929" data-path="images/general/authentication/entra-sso/entra_2.png" />

## How to set up SSO

<Warning>
  **Enforced Entra SSO disables password-based login.**

  When Entra SSO is enforced for your organization, password-based login and password reset emails are disabled for all users on the account. Users must sign in via Microsoft Entra.

  * Entering an email address on the Bright Data login page automatically redirects the user to the Entra sign-in page.
  * After a successful Entra sign-in, the user is redirected back to Bright Data.
  * Password reset requests will **not** generate an email.
</Warning>

* Go to [https://brightdata.com](https://brightdata.com) and log in to your account.

* Choose Settings->Account settings->Passwords & authentication in left side menu and toggle Microsoft Entra ID (Azur AD) switch

<img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/authentication/entra-sso/entra_3.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=49122c8887f2864721e76cf3417eae6d" alt="Bright Data Passwords and authentication settings with the Microsoft Entra ID toggle" width="1727" height="919" data-path="images/general/authentication/entra-sso/entra_3.png" />

* From “App registrations” view select your application.

* Copy “Application (client) ID” to “Client ID”

* Copy “Directory (tenant) ID” to “OAuth2 issuer (tenant)”

* Go to “Add a certificate or secret”

<img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/authentication/entra-sso/entra_4.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=34bafc2f22a857fd03ddcffc43b9a6f3" alt="Entra App registrations overview showing Application client ID and Directory tenant ID" width="1824" height="930" data-path="images/general/authentication/entra-sso/entra_4.png" />

* At secrets screen click “New client secret”

* Fill Description

* Click “Add”

<img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/authentication/entra-sso/entra_5.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=6bda5e8c9185fe4c7a4a23a2ba8b2604" alt="Entra Add a client secret dialog with Description and Add button" width="1823" height="930" data-path="images/general/authentication/entra-sso/entra_5.png" />

* Once secret is created copy secret value to “Client secret”.

* Copy “Sign-in redirect URI” to be used at next step

<img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/authentication/entra-sso/entra_6.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=fac7a9990338572c0795e7deb2d9ac96" alt="Bright Data Entra ID dialog with Sign-in redirect URI to copy" width="1828" height="929" data-path="images/general/authentication/entra-sso/entra_6.png" />

* At “Authentication” screen click “Add platform” and select “Web”

<img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/authentication/entra-sso/entra_7.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=03d219b2b73488b1499be7d1a7903892" alt="Entra Authentication screen with Add platform dialog and Web option" width="1825" height="930" data-path="images/general/authentication/entra-sso/entra_7.png" />

* Paste previously copied “Sign-in redirect URI” to the “Redirect URIs” and save settings by clicking “Configure”:

<img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/authentication/entra-sso/entra_8.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=07b000914d880bbf2791e23f23a3bd51" alt="Entra Configure Web platform dialog with Sign-in redirect URI pasted in" width="1825" height="930" data-path="images/general/authentication/entra-sso/entra_8.png" />

* Activate EntraID integration at BrighData control panel and test login:

<img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/authentication/entra-sso/entra_9.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=16e434e6e3156dae471546f30aecb4c3" alt="Bright Data Entra ID integration activated and ready for test login" width="892" height="916" data-path="images/general/authentication/entra-sso/entra_9.png" />

## Setup SCIM provisioning

* Copy “Auth token” from SCIM section of BrightData EntraID settings:

<img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/authentication/entra-sso/entra_10.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=4649683170006ad94dd8aea0825fb30c" alt="Bright Data Entra ID SCIM section showing the Auth token to copy" width="671" height="878" data-path="images/general/authentication/entra-sso/entra_10.png" />

* Select your application from “Enterprise Applications” view and go to “Provisioning” settings:

<img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/authentication/entra-sso/entra_11.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=22303e8f6bc9b20e268377e8ed180c6e" alt="Entra Enterprise Applications view with Bright Data application selected" width="1559" height="930" data-path="images/general/authentication/entra-sso/entra_11.png" />

* Select “Provisioning” under “Manage” menu:

<img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/authentication/entra-sso/entra_12.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=51632271bbd37f64e274b5ae9e4786d5" alt="Entra Manage menu with Provisioning option highlighted" width="1557" height="931" data-path="images/general/authentication/entra-sso/entra_12.png" />

* Select “Automatic” Provisioning Mode

* Fill “Tenant URL” with [https://brightdata.com/users/auth/scim](https://brightdata.com/users/auth/scim) value

* Fill “Secret Token” with previously copied value from BrightData control panel settings

* Test Connection. You should see successful message in top right corner
  Save Settings

<img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/authentication/entra-sso/entra_13.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=f88b5c584438faf81a75cbf2a3b2aa95" alt="Entra Provisioning settings with Tenant URL and Secret Token fields filled in" width="1823" height="931" data-path="images/general/authentication/entra-sso/entra_13.png" />

* Return to “Overview” tab and click “Start provisioning”.

* You can test provisioning at “Provision on demand” page, but first assign your users to BrightData application at “Users and groups” page:

<img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/authentication/entra-sso/entra_14.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=3566b35a83bf0411537b82c099b04498" alt="Entra Users and groups page with users assigned to the Bright Data application" width="1825" height="930" data-path="images/general/authentication/entra-sso/entra_14.png" />

## Troubleshooting

<AccordionGroup>
  <Accordion title="What should a user do if they are not receiving a password reset email?">
    If your organization has enabled **enforced Entra SSO**, password reset emails are not sent, because password-based authentication is disabled on accounts with enforced SSO.

    To sign in:

    1. Go to the [Bright Data sign-in page](https://brightdata.com/cp).
    2. Enter the user's email address.
    3. The user will be automatically redirected to the Microsoft Entra sign-in page.
    4. After a successful Entra sign-in, the user is redirected back to Bright Data.

    If access issues persist, contact your organization's IT / Entra administrator. They manage the Entra SSO configuration on your company's side.
  </Accordion>

  <Accordion title="Why is a user redirected to a Microsoft login page they do not recognize?">
    This is expected behavior when Entra SSO is enforced. The Bright Data login page detects the email domain associated with your organization's Entra tenant and redirects the user to your configured Microsoft Entra sign-in page.
  </Accordion>
</AccordionGroup>
