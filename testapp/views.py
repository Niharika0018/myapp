from django.shortcuts import render
import requests
from django.http import HttpResponse
import datetime

def my_fun(request):
    response = requests.get("https://s3.us-west-2.amazonaws.com/secure.notion-static.com/f78c140f-bbf0-46d8-9902-fa8af18a4b0d/channel-cost.json?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230228T053909Z&X-Amz-Expires=86400&X-Amz-Signature=f2052dbe872366c3b35036f7935321b66caf3aa324a1f64670bf9ac361541c75&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22channel-cost.json%22&x-id=GetObject")
    response_body = response.json()
    list_one = []
    list_two = []
    a = b = c = d = 0
    start_date = datetime.date(2022, 12, 20)
    end_date = datetime.date(2023, 12, 31)
    delta = datetime.timedelta(days=1)
    while start_date <= end_date:
        date = start_date.strftime("%Y-%m-%d")
        list_one.append(date)
        start_date = start_date + delta


    for start in list_one:
        for i in response_body:
            if i['date'].split()[0] == start and 'ivr' in i:
                a = a + i['ivr']
            s = f"{a * 0.15:.2f}"

            if i['date'].split()[0] == start and 'email' in i:
                b = b + i['email']
            s1 = f"{b * 0.13:.2f}"

            if i['date'].split()[0] == start and 'sms' in i:
                c = c + i['sms']
            s2 = f"{c * 0.12:.2f}"

            if i['date'].split()[0] == start and 'whatsapp' in i:
                d = d + i['whatsapp']
            s3 = f"{d * 0.51:.2f}"

        list_two.append({"sms": s2, "whatsapp": s3, "email":s1, "ivr": s, "date": start})

    context = {
        'list_two': list_two,
    }

    return render(request, 'testapp/testapp.html', context=context)