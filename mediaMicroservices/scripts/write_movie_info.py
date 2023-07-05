import aiohttp
import asyncio
import sys
import json
import argparse

async def upload_cast_info(session, addr, cast):
  async with session.post(f"{addr}/wrk2-api/cast-info/write", json=cast) as resp:
    return await resp.text()

async def upload_plot(session, addr, plot):
  async with session.post(f"{addr}/wrk2-api/plot/write", json=plot) as resp:
    return await resp.text()

async def upload_movie_info(session, addr, movie):
  async with session.post(f"{addr}/wrk2-api/movie-info/write", json=movie) as resp:
    return await resp.text()

async def register_movie(session, addr, movie):
  params = {
    "title": movie["title"],
    "movie_id": movie["movie_id"]
  }
  async with session.post(f"{addr}/wrk2-api/movie/register", data=params) as resp:
    return await resp.text()

async def write_cast_info(addr, raw_casts):
  idx = 0
  tasks = []
  conn = aiohttp.TCPConnector(limit=200)
  async with aiohttp.ClientSession(connector=conn) as session:
    for raw_cast in raw_casts:
      try:
        cast = {
            "cast_info_id": raw_cast["id"],
            "name": raw_cast["name"],
            "gender": raw_cast["gender"] == 2,
            "intro": raw_cast["biography"],
        }
        task = asyncio.ensure_future(upload_cast_info(session, addr, cast))
        tasks.append(task)
        idx += 1
      except:
        print("Warning: cast info missing!")
      if idx % 200 == 0:
        resps = await asyncio.gather(*tasks)
        print(idx, "casts finished")
    resps = await asyncio.gather(*tasks)
    print(idx, "casts finished")

async def write_movie_info(addr, raw_movies):
  idx = 0
  tasks = []
  conn = aiohttp.TCPConnector(limit=200)
  async with aiohttp.ClientSession(connector=conn) as session:
    for raw_movie in raw_movies:
      casts = []
      for raw_cast in raw_movie["cast"]:
        try:
          cast = {
              "cast_id": raw_cast["cast_id"],
              "character": raw_cast["character"],
              "cast_info_id": raw_cast["id"],
          }
          casts.append(cast)
        except:
          print("Warning: cast info missing!")
      movie = {
          "movie_id": str(raw_movie["id"]),
          "title": raw_movie["title"],
          "plot_id": raw_movie["id"],
          "casts": casts,
          "thumbnail_ids": [raw_movie["poster_path"]],
          "photo_ids": [],
          "video_ids": [],
          "avg_rating": raw_movie["vote_average"],
          "num_rating": raw_movie["vote_count"],
      }
      task = asyncio.ensure_future(upload_movie_info(session, addr, movie))
      tasks.append(task)
      plot = {"plot_id": raw_movie["id"], "plot": raw_movie["overview"]}
      task = asyncio.ensure_future(upload_plot(session, addr, plot))
      tasks.append(task)
      task = asyncio.ensure_future(register_movie(session, addr, movie))
      tasks.append(task)
      idx += 1
      if idx % 200 == 0:
        resps = await asyncio.gather(*tasks)
        print(idx, "movies finished")
    resps = await asyncio.gather(*tasks)
    print(idx, "movies finished")

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("-c", "--cast", action="store", dest="cast_filename",
    type=str, default="../datasets/tmdb/casts.json")
  parser.add_argument("-m", "--movie", action="store", dest="movie_filename",
    type=str, default="../datasets/tmdb/movies.json")
  args = parser.parse_args()

  with open(args.cast_filename, 'r') as cast_file:
    raw_casts = json.load(cast_file)
  addr = "http://127.0.0.1:8080"
  loop = asyncio.get_event_loop()
  future = asyncio.ensure_future(write_cast_info(addr, raw_casts))
  loop.run_until_complete(future)

  with open(args.movie_filename, 'r') as movie_file:
    raw_movies = json.load(movie_file)
    addr = "http://127.0.0.1:8080"
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(write_movie_info(addr, raw_movies))
    loop.run_until_complete(future)