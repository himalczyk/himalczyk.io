import os

from dotenv import load_dotenv

load_dotenv()
YT_API_KEY = os.getenv("YT_API_KEY")
YT_BASE_URL = "https://www.youtube.com/embed/"

RP_BASE_URL = "https://realpython.com"
RP_PODCAST_BASE_URL = "https://realpython.com/podcasts/rpp/"


YOUTUBE_CHANNELS = [
    "UC8butISFwT-Wl7EV0hUK0BQ",
    "UCVhQ2NnY5Rskt6UjCUkJ_DA",
    "UCZgt6AzoyjslHTC9dz0UoTw",
    "UCCezIgC97PvUuR4_gbFUs5g",
    "UCUyeluBRhGPCW4rPe_UvBZQ",
    "UCsrVDPJBYeXItETFHG0qzyw",
    "UC1Zfv1Zrp1q5lKgBomzOyCA",
    "UCd3dNckv1Za2coSaHGHl5aA",
]


YT_VIDEOS_API_LIMIT_REACHED = [
    {
        "url": "https://www.youtube.com/embed/PYuTzLswn_Y",
        "youtube_url": "https://www.youtube.com/watch?v=PYuTzLswn_Y",
        "title": "Python Tutorial: Securely Manage Passwords and API Keys with DotEnv",
        "description": "In this Python Programming video, we will be learning how to properly manage sensitive information...",
        "channel_name": "Corey Schafer",
        "channel_url": "https://www.youtube.com/@coreyms",
        "thumbnail": "https://i.ytimg.com/vi/PYuTzLswn_Y/hqdefault.jpg",
    },
    {
        "url": "https://www.youtube.com/embed/CvQ7e6yUtnw",
        "youtube_url": "https://www.youtube.com/watch?v=CvQ7e6yUtnw",
        "title": "This Is Why Python Data Classes Are Awesome",
        "description": "Data classes in Python are really powerful and not just for representing structured data...",
        "channel_name": "ArjanCodes",
        "channel_url": "https://www.youtube.com/@ArjanCodes",
        "thumbnail": "https://i.ytimg.com/vi/CvQ7e6yUtnw/hqdefault.jpg",
    },
    {
        "url": "https://www.youtube.com/embed/rfscVS0vtbw",
        "youtube_url": "https://youtube.com/watch?v=rfscVS0vtbw",
        "title": "Python for Beginners - Full Course",
        "description": "Learn Python programming with this comprehensive course from freeCodeCamp...",
        "channel_name": "freeCodeCamp.org",
        "channel_url": "https://www.youtube.com/@freecodecamp",
        "thumbnail": "https://i.ytimg.com/vi/rfscVS0vtbw/hqdefault.jpg",
    },
    {
        "url": "https://www.youtube.com/embed/TlHvYWVUZyc",
        "youtube_url": "https://www.youtube.com/watch?v=TlHvYWVUZyc",
        "title": "Kubernetes Explained in 6 Minutes | k8s Architecture",
        "description": "Learn about the architecture of Kubernetes and how it works...",
        "channel_name": "ByteByteGo",
        "channel_url": "https://www.youtube.com/@ByteByteGo",
        "thumbnail": "https://i.ytimg.com/vi/TlHvYWVUZyc/hqdefault.jpg",
    },
    {
        "url": "https://www.youtube.com/embed/Dl-BdxNRUqs",
        "youtube_url": "https://www.youtube.com/watch?v=Dl-BdxNRUqs",
        "title": "What does larger scale software development look like?",
        "description": "What does larger scale software development look like?...",
        "channel_name": "Web Dev Cody",
        "channel_url": "https://www.youtube.com/@WebDevCody",
        "thumbnail": "https://i.ytimg.com/vi/Dl-BdxNRUqs/hqdefault.jpg",
    },
    {
        "url": "https://www.youtube.com/embed/0XKYMt5mGpQ",
        "youtube_url": "https://www.youtube.com/watch?v=0XKYMt5mGpQ",
        "title": "Vim Is The Perfect IDE",
        "description": "Learn why Vim can be the perfect IDE for your development workflow...",
        "channel_name": "ThePrimeagen",
        "channel_url": "https://www.youtube.com/@ThePrimeagen",
        "thumbnail": "https://i.ytimg.com/vi/0XKYMt5mGpQ/hqdefault.jpg",
    },
    {
        "url": "https://www.youtube.com/embed/u-O59jWbKZE",
        "youtube_url": "https://www.youtube.com/watch?v=u-O59jWbKZE",
        "title": "curiosity",
        "description": "Be curios, explore, create, learn, develop and be nice...",
        "channel_name": "TJ DeVries",
        "channel_url": "https://www.youtube.com/@teej_dv",
        "thumbnail": "https://i.ytimg.com/vi/u-O59jWbKZE/hqdefault.jpg",
    },
    {
        "url": "https://www.youtube.com/embed/VVb65xABTWw",
        "youtube_url": "https://www.youtube.com/watch?v=VVb65xABTWw",
        "title": "Why does everyone hate Go?",
        "description": "It seems every language goes through this - PHP, JavaScript, Ruby - everything. ...",
        "channel_name": "Melkey",
        "channel_url": "https://www.youtube.com/@MelkeyDev",
        "thumbnail": "https://i.ytimg.com/vi/VVb65xABTWw/hqdefault.jpg",
    },
]
