from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.prompts.prompt import PromptTemplate

def getTemplate():
    prompt_que_ans = [
    {
        "question": "how long BTC payment takes to get confirmed or through?",
        "answer":
    """
    BTC payment takes 30-90 minutes to confirm.
    No worries, please wait. After the payment confirmation,
    you will receive an email instantly with login credentials.
    """
    },
    {
        "question": "Can you suggest me any movie or series?",
        "answer":
    """
    Please inform through @toucaninfobot using Telegram.
    """
    },
    {
        "question": "How long is the Nonstop trial?",
        "answer":
    """
    Trial for 24 hours and default 2 connections.
    """
    },
    {
        "question": "I have problem with the connections. What to do?",
        "answer":
    """
    Restart your service, device, and router,
    Check if your connection is stable
    check speed on the speed test
    try VPN or if you are using vpn try again without VPN.
    """
    },
    {
        "question": "do you guys have any French channels?",
        "answer":
    """
    Yes.
    """
    },
    {
        "question": "Is there any discount for the first month? Many other sites have it.?",
        "answer":
    """
    It is already such a low price for what you get, so there is no discount right now.
    """
    },
      {
        "question": "Suggest an app app for Firestick or Android TV?",
        "answer":
    """
    Type https://nsfiretv.com/xc into the Downloader app to install.
      Then open the app and choose URL 2 and put your ID and password you got on your email.
      if it doesn’t work then try the smarter app. Type nsfiretv.com/smt into the Downloader app to install. Then open the Smarters app and log in using xtream codes API info from our email. Please be sure to allow storage permissions after logging in.
    """
    },
    {
        "question": "Can I try this service few days more?",
        "answer":
    """
    No. The free trial is 24 hours in NONSTOP.
    """
    },
        {
        "question": "How do I make payment with visa or master card?",
        "answer":
    """
    Sorry, card payment is not available right now. Only crypto payment is accepted.
    """
    },
    {
        "question": "When card payment will be available?",
        "answer":
    """
    We have no estimated time for that, only crypto payment is available
    """
    },
    {
        "question": "Is our service is Chromecast supported ?",
        "answer":
    """
    We support Gen4.Chromecast is not the best option
    """
    },
    {
        "question": "Which apps do you recommend to use your service on iPhone?",
        "answer":
    """
    We recommend IPTV Smarters pro (https://www.iptvsmarters.com/#downloads),IPTVX
    GSE SMART IPTV, Cloud Stream IPTV player, MegaIPTV, Snappy etc.
    """
    },
    {
        "question": "I want to pay but don't know how?",
        "answer":
    """
    Where do you from ?
    """
    },
    {
        "question": "I am from US",
        "answer":
    """
    you can use CASHAPP.
    1- Search your phones app store for Cash App from Square, INC. Install it
    2- Open Cash App and create an account, enter your phone number or an email address
    3- Cash App will send you a secret code via text or email—enter it
    4- Enter your debit card info to link your bank account to Cash App
    5- Enter a $Cashtag— a unique username you’ll use to send and receive money
    6- Add your zip code
    7- Tap the Bank button in the lower left corner to open the Banking tab
    8- Tap the Add Cash button
    9- Enter the amount of cash you want to add to Cash App
    10- Tap the green Add button

    Buy and Send Bitcoin with Cash App
    1- Tap the Bank button at bottom left.
    2- You’ll see an option to add cash and cash out. Scroll down to the Bitcoin button and click it.
    3- You will see 3 options. Buy, Sell, and Send. Tap Buy button and enter amount needed to pay for your order. click on confirm after.
    4- Tap the Payments ‘$’ at bottom center of your Cash App to get to the Payments screen
    5- Tap the QR Scanner on the top left corner of the screen
    6- Hold your camera over the Lightning Invoice QR code(shown on website after checkout) to scan it
    7- Follow the prompts to confirm and pay the request
    ".
    """
    },
    {
        "question": "I am from CANADA",
        "answer":
    """
    Then you can use http://newton.co
    It is very easy and secure to use
    Newton payment steps:
    Create an account and add funds
    1. Go to newton.co and create an account.
    You can use Newton on iOS, Android, or on a web browser.
    2. Add fiat (CAD) via e-Transfer or wire transfer.
    2. On the right-hand side of the dashboard, navigate to the two arrows.
    3. Using the dropdown menu in the lower field, select BTC
    4. Enter the amount needed to pay for your order
    5. Select Review Trade.

    How to send payment on newton
    1. On the right-hand side of the dashboard, navigate to the upwards-facing arrow.
    2. Select ""Crypto to Wallet"".
    3. Copy and paste the BTC address you received after checkout.
    4. Enter the amount needed to pay for your order
    5. Select ‘Review Withdrawal’.
    6. Review your withdrawal details to ensure you're sending the correct amount and then select 'Withdraw Funds'.
    """
    },
        {
        "question": "How do I make payment if I cashapp or newton.co don't available?",
        "answer":
    """
    "1- Create a Coinbase account
    Download the Coinbase app and start the signup process. You will need a valid ID and may be asked for proof of address in order to transact, so be sure to have those ready. Verifying your ID may take longer than a few minutes, depending on where you live.

    2- Tap on the payment method box and connect a payment method. You can use a bank account, debit card or initiate a wire.

    3- Tap the ( + ) Buy on the Home tab.

    4- Search for Bitcoin by typing “Bitcoin” into the search bar. When you see Bitcoin appear in the results, tap it to open up the purchase screen.

    5- Enter your order amount. The app will automatically convert this into a Bitcoin amount.

    6- Tap “View Purchase” when ready. You will see the details of your purchase. Make sure everything is in order and confirm your purchase by clicking ""Buy Now"".

    7- Once the order processes, you'll be taken to the confirmation screen.

    8- Go back to home screen.

    9- Tap Send.

    10- Select the asset and amount to send

    11- Tap Next.

    12- Enter the bitcoin address you received from us, or scan the qr code. You will get this after you complete your order on our website.

    13- Review and confirm the transaction."

    """
    },
        {
        "question": "I want to renew my service, how can I do that?",
        "answer":
    """
    Go to this site https://www.nonstopiptv.com/product/iptv-renew/
    and choose your desired connection and duration of the package"

    """
    },
    {
        "question": "How many devices can I run simultaneously?",
        "answer":
    """
    It depends on how many they have been paid for as we don't
      sell one connection, only 2, 4, or 6. Y
      ou can use 100 devices but can only connect 2, 4, or 6
     devices at the same time, depending on what you pay for
    """
    },
    {
    "question": "Why sould I choose your service?",
    "answer":
    """
    Because no one has a customer service that comes close to ours.
    You can test our subscriptions and you will know the rest
    """
    },
    {
        "question": "I want to be a reseller. What to do?",
        "answer":
    """
    For first purchase the minimum is $450USD.
    Each credit costs $9USD. Only Bitcoin is accepted for resellers.
    1 Month 2 Connections - 1 credit
    1 Month 4 Connections - 2 credits
    1 Month 6 Connections - 3 credits
    3 Month 2 Connections - 3 credits
    3 Month 4 Connections - 5 credits
    3 Month 6 Connections - 7 credits
    6 Month 2 Connections - 5 credits
    6 Month 4 Connections - 6 credits
    6 Month 6 Connections - 10 credits
    12 Month 2 Connections - 8 credits
    12 Month 4 Connections - 12 credits
    12 Month 6 Connections - 15 credits"


    A reseller will get his own pannel, where he can add delete give trial to your customer from there
    extend there account from there

    Reseller Panel Info

    Panel: http://tigerfights.xyz/SBrrErmQ
    Username: 
    Pass: 
    DNS: http://nonstopip.tv:80

    Our support is 24/7 On Telegram
    https://t.me/NonStop_SupportBot

    https://www.nonstopiptv.com/?chat-open"


    If he is an old reseller and wants to but more credit then To buy more credits 
    In the future use https://www.nonstopiptv.com/product/credits/
    Password: NSReseller
    to add more credits.

    """
    },
    ]
    return prompt_que_ans


def getPrompt(template):
    example_prompt = PromptTemplate(input_variables=["question", "answer"], template="Question: {question}\n{answer}")
    prompt = FewShotPromptTemplate(
    examples=template,
    example_prompt=example_prompt,
    suffix="Question: {input}",
    input_variables=["input"])
    return prompt