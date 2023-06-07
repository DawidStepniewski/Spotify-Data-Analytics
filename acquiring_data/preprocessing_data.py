import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
from acquiring_data import spotify_user_data


def preprocess_data():
    scope = ("playlist-read-private", "user-library-read", "user-top-read")
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    user_tracks_df = pd.read_pickle('user_tracks_df.pkl')
    user_tracks_df.to_excel('C:/Users/Dawid Stępniewski/PycharmProjects/Spotify-Data-Analytics/Data/Processed '
                            'Data/user_tracks_data.xlsx', index=False)

    track_artists = pd.read_pickle('track_artists.pkl')
    track_artists.to_excel(
        'C:/Users/Dawid Stępniewski/PycharmProjects/Spotify-Data-Analytics/Data/Processed Data/track_artists_data.xlsx',
        index=False)

    tracks_audio_features = pd.read_pickle('audio_features.pkl')
    tracks_audio_features.to_excel(
        'C:/Users/Dawid Stępniewski/PycharmProjects/Spotify-Data-Analytics/Data/Processed Data/audio_features_data.xlsx',
        index=False)

    user_stats_df = pd.read_pickle('user_stats_df.pkl')
    user_stats_df.to_excel(
        'C:/Users/Dawid Stępniewski/PycharmProjects/Spotify-Data-Analytics/Data/Processed Data/user_stats_data.xlsx',
        index=False)

    audio_features_with_popularity = tracks_audio_features.merge(user_tracks_df[['track_id', 'popularity']],
                                                                 on='track_id', how='inner')
    audio_features_with_popularity.to_excel(
        'C:/Users/Dawid Stępniewski/PycharmProjects/Spotify-Data-Analytics/Data/Processed Data/features_with_popularity.xlsx',
        index=False)

    # user_tracks_df = spotify_user_data.get_tracks(sp)
    # user_tracks_df.to_pickle('user_tracks_df.pkl')
    #
    # track_artists = spotify_user_data.get_artist(sp, user_tracks_df)
    # track_artists.to_pickle('track_artists.pkl')
    #
    # tracks_audio_features = spotify_user_data.get_audio_features(sp, user_tracks_df)
    # tracks_audio_features.to_pickle('audio_features.pkl')

    # user_stats_df = user_tracks_df.merge(tracks_audio_features, how='left', on='track_id')
    # user_stats_df = user_stats_df.merge(track_artists.drop_duplicates(subset=['artist_id', 'artist_name']),
    #                                     on=['artist_id', 'artist_name'])
    # user_stats_df = user_stats_df[user_stats_df['genres'].map(lambda d: len(d)) > 0]  # Remove empty rows with
    # # empty genre
    # user_stats_df.to_pickle('user_stats_df.pkl')
    #
    # tracks_audio_features['duration_s'] = tracks_audio_features['duration_ms'].apply(lambda x: x / 1000)
    # tracks_audio_features = tracks_audio_features.drop('duration_ms', axis=1)
    # tracks_audio_features.to_pickle('audio_features.pkl')