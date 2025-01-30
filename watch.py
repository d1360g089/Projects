import re

def main():
    html_input = input("HTML: ")
    print(parse(html_input))

def parse(ip):
    iframe_pattern = r'<iframe[^>]*\bsrc="([^"]+)"'
    iframe = re.search(iframe_pattern, ip)
    if iframe:
        yt_url = iframe.group(1)

        video_id = re.search(r"https?:\/\/(www\.)?youtube\.com\/embed\/([\w]+)", yt_url)

    if video_id:
        video_id = video_id.group(2)
        return f"https://youtu.be/{video_id}"
if __name__ == "__main__":
    main()









