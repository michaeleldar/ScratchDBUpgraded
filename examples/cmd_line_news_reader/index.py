from urllib.request import urlopen


def curl(url):
    page = urlopen(url)
    data_bytes = page.read()
    return data_bytes.decode("utf-8")


print(
    "Welcome to the slow, bad, complicated and very ineffecient command line scratch news reader."
)
how_far = input("How far back do you want to read news from (max 20)? ")
is_european = input("Do you live in europe y/n (for date formatting)? ")
if is_european == "y":
    is_european = True
else:
    is_european = False

assert int(how_far) < 21


print("Newest news will be at the top, while oldest will be at the bottom.")
print("Loading...")

titles = []
urls = []
descs = []
times = []

percent_increase = round(100 / int(how_far))
last_percent = 0

for post in range(0, int(how_far)):
    titles.append(
        curl(f"https://scratchdbupgraded.applejuicepro.repl.co/v1/news/{post}/title")
    )
    print(f"{round((percent_increase / 4) + last_percent)}% loaded.")

    urls.append(
        curl(f"https://scratchdbupgraded.applejuicepro.repl.co/v1/news/{post}/url")
    )
    print(f"{round((((percent_increase) / 4) * 2) + last_percent)}% loaded.")

    descs.append(
        curl(
            f"https://scratchdbupgraded.applejuicepro.repl.co/v1/news/{post}/description"
        )
    )
    print(f"{round((((percent_increase) / 4) * 3) + last_percent)}% loaded.")

    times_ = curl(
        f"https://scratchdbupgraded.applejuicepro.repl.co/v1/news/{post}/timestamp"
    )
    times_formatted = times_.split("-")
    if is_european:
        times.append(
            f"{times_formatted[2][:2]}/{times_formatted[1]}/{times_formatted[0]}"
        )
    else:
        times.append(
            f"{times_formatted[1]}/{times_formatted[2][:2]}/{times_formatted[0]}"
        )

    print(f"{round(percent_increase + last_percent)}% loaded.")
    last_percent = percent_increase + last_percent

for x in range(0, len(titles)):
    title = titles[x]
    desc = descs[x]
    url = urls[x]
    time = times[x]

    print("")
    print(title)
    print(desc)
    print("For more, visit " + url)
    print("(" + time + ")")
