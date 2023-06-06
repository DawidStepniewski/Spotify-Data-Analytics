import pandas as pd
import spotipy
from spotipy import SpotifyOAuth


def get_tracks(sp):
    current_user_top_tracks = sp.current_user_top_tracks(limit=50, time_range="long_term")

    track_id = []
    track_name = []
    artist_id = []
    artist_name = []
    explicit = []
    popularity = []
    release_date = []

    for track in current_user_top_tracks['items']:
        try:
            track_id.append(track['id'])
            track_name.append(track['name'])
            artist_id.append(track['artists'][0]['id'])
            artist_name.append(track['artists'][0]['name'])
            explicit.append(track['explicit'])
            release_date.append(track['album']['release_date'])
            popularity.append(track['popularity'])
        except Exception as e:
            print(e)

    df = pd.DataFrame()
    df['track_id'] = track_id
    df['track_name'] = track_name
    df['artist_id'] = artist_id
    df['artist_name'] = artist_name
    df['explicit'] = explicit
    df['release_date'] = release_date
    df['popularity'] = popularity

    return df


def get_audio_features(sp, user_tracks_df):
    audio_features = []
    for track in user_tracks_df['track_id']:
        try:
            audio_features.append(sp.audio_features(track)[0])
        except Exception as e:
            print(e)
    df = pd.DataFrame()
    df['audio_features'] = audio_features

    return df
