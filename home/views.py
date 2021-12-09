from django.http import HttpResponse
from django.shortcuts import render
import datetime
import jwt
from TrustPayments.settings import ST_JWT_SECRET, ST_JWT_USER, ST_SITE_REFERENCE


def home(request):

    payload = {
        "payload": {
            "accounttypedescription": "ECOM",
            "baseamount": "1050",
            "currencyiso3a": "EUR",
            "sitereference": ST_SITE_REFERENCE,
            "requesttypedescriptions": ["THREEDQUERY", "AUTH"],
        },
        "iat": int(datetime.datetime.utcnow().timestamp()),
        "iss": ST_JWT_USER,
    }

    print("PAYLOAD:", payload)

    token = jwt.encode(
        payload=payload,
        key=ST_JWT_SECRET,
    )

    print("TOKEN:", token)

    return render(request, "index.html", context={"token": token})


def handle_submit(request):
    print("SUBMITTED:", request.POST)
    return HttpResponse(status=200)
