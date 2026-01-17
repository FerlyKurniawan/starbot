from bs4 import BeautifulSoup
import httpx
import json
import re
from logs import logger


class Drakor:
    BASE_URL = "https://dramaqu.ad"

    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0"}

    async def get_ongoing(self, limit=10, page=1):
        url = f"{self.BASE_URL}/category/ongoing-drama/page/{page}/"
        result = []

        try:
            async with httpx.AsyncClient(follow_redirects=True) as client:
                res = await client.get(url, headers=self.headers, timeout=10)
        except Exception as e:
            logger.error(f"[ONGOING] Gagal ambil halaman: {e}")
            return []

        if res.status_code != 200:
            logger.warning(f"[ONGOING] Status code {res.status_code}")
            return []

        soup = BeautifulSoup(res.text, "html.parser")
        items = soup.select("article.movie-preview")

        for item in items[:limit]:
            a_tag = item.select_one(".movie-poster a")
            if not a_tag:
                continue

            link = a_tag.get("href")
            img = a_tag.find("img")
            title = img.get("alt", "No Title") if img else "No Title"
            thumb = img.get("src") if img else None

            detail = await self.get_detail(link)

            result.append({
                "title": title,
                "url": link,
                "thumbnail": thumb,
                "deskripsi": detail.get("deskripsi"),
                "genre": detail.get("genre"),
                "episodes": detail.get("episodes"),
                "latest_episode": detail.get("latest_episode"),
                "total_episodes": detail.get("total_episodes"),
                "release": detail.get("release"),
                "director": detail.get("director"),
                "stars": detail.get("stars"),
                "rating": detail.get("rating"),
                "total_vote": detail.get("total_vote"),
            })

        logger.info(f"✅ Berhasil ambil {len(result)} drama ongoing (page {page})")
        return result

    async def get_detail(self, url: str) -> dict:
        try:
            async with httpx.AsyncClient(follow_redirects=True) as client:
                res = await client.get(url, headers=self.headers, timeout=10)
        except Exception as e:
            logger.error(f"[DETAIL] Gagal ambil {url}: {e}")
            return self._empty_detail()

        if res.status_code != 200:
            logger.warning(f"[DETAIL] Status {res.status_code} untuk {url}")
            return self._empty_detail()

        soup = BeautifulSoup(res.text, "html.parser")

        # --- JSON-LD ---
        json_ld = soup.find("script", type="application/ld+json")
        data_json = {}
        if json_ld:
            try:
                data_json = json.loads(json_ld.string)
            except Exception as e:
                logger.warning(f"[DETAIL] Gagal parse JSON-LD {url}: {e}")

        # --- Title & Poster ---
        title = soup.select_one(".info-right .title span")
        title = title.get_text(strip=True) if title else data_json.get("name", "Unknown")

        poster = soup.select_one(".info-left .poster img")
        poster = poster["src"] if poster else data_json.get("image")

        # --- Deskripsi ---
        deskripsi = (
            data_json.get("description")
            or (soup.select_one(".excerpt.more") or soup.select_one(".movie-excerpt p"))
        )
        if hasattr(deskripsi, "get_text"):
            deskripsi = deskripsi.get_text(" ", strip=True)
        if not deskripsi:
            deskripsi = "No description available"

        # --- Genre ---
        genres = []
        for a in soup.select(".categories a"):
            genres.append(a.get_text(strip=True))
        if not genres and data_json.get("genre"):
            genres = data_json.get("genre") if isinstance(data_json.get("genre"), list) else [data_json.get("genre")]

        # --- Director ---
        director = "Unknown"
        director_el = soup.select_one(".director a")
        if director_el:
            director = director_el.get_text(strip=True)
        elif "director" in data_json:
            if isinstance(data_json["director"], dict):
                director = data_json["director"].get("name", "Unknown")

        # --- Stars ---
        stars = [a.get_text(strip=True) for a in soup.select(".actor a")]
        if not stars and "actor" in data_json:
            stars = [a.get("name") for a in data_json.get("actor", []) if a.get("name")]

        # --- Rating ---
        rating = soup.select_one(".site-vote .average")
        rating = rating.get_text(strip=True) if rating else data_json.get("aggregateRating", {}).get("ratingValue", "N/A")

        total_vote = soup.select_one(".details .total")
        total_vote = total_vote.get_text(strip=True) if total_vote else "0"

        # --- Episode list ---
        episodes = []
        for a in soup.select(".episodelist li a"):
            episodes.append({
                "title": a.get_text(strip=True),
                "url": a.get("href", "")
            })

        # --- Latest & Total Episodes ---
        latest_episode = "Unknown"
        if episodes:
            latest_episode = episodes[0]["title"]

        total_episodes = "Unknown"
        if episodes:
            total_episodes = str(len(episodes))
        else:
            ep_text = soup.find(string=lambda t: t and "Episode" in t)
            if ep_text:
                match = re.search(r"(\d+)", ep_text)
                if match:
                    total_episodes = match.group(1)

        # --- Release ---
        release = "Unknown"
        release_el = soup.select_one(".movie-release")
        if release_el:
            release = release_el.get_text(strip=True)
        elif "datePublished" in data_json:
            release = data_json.get("datePublished", "Unknown")

        return {
            "title": title,
            "poster": poster,
            "latest_episode": latest_episode,
            "deskripsi": deskripsi,
            "genre": genres or ["Unknown"],
            "episodes": episodes,
            "total_episodes": total_episodes,
            "release": release,   # ✅ fix disini
            "director": director,
            "stars": stars,
            "rating": rating,
            "total_vote": total_vote,
        }

    def _empty_detail(self) -> dict:
        return {
            "title": "Unknown",
            "poster": None,
            "latest_episode": "Unknown",
            "deskripsi": "Gagal mengambil",
            "genre": [],
            "episodes": [],
            "total_episodes": "Unknown",
            "release": "Unknown",
            "director": "Unknown",
            "stars": [],
            "rating": "N/A",
            "total_vote": "0",
        }


drakor = Drakor()