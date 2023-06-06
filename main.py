import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
from feature_importance import dataset_preparation

if __name__ == "__main__":
    def main():
        scope = ("playlist-read-private", "user-library-read", "user-top-read")
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

        # user_tracks_df = spotify_user_access.get_tracks(sp)
        # user_tracks_df.to_pickle('user_tracks_df.pkl')
        user_tracks_df = pd.read_pickle('user_tracks_df.pkl')

        # track_artists = spotify_user_access.get_artist(sp, user_tracks_df)
        # track_artists.to_pickle('track_artists.pkl')
        track_artists = pd.read_pickle('track_artists.pkl')

        # tracks_audio_features = spotify_user_access.get_audio_features(sp, user_tracks_df)
        # tracks_audio_features.to_pickle('audio_features.pkl')
        tracks_audio_features = pd.read_pickle('audio_features.pkl')

        # user_stats_df = user_tracks_df.merge(tracks_audio_features, how='left', on='track_id')
        # user_stats_df = user_stats_df.merge(track_artists.drop_duplicates(subset=['artist_id', 'artist_name']),
        #                                     on=['artist_id', 'artist_name'])
        # user_stats_df = user_stats_df[user_stats_df['genres'].map(lambda d: len(d)) > 0]  # Remove empty rows with
        # # empty genre
        # user_stats_df.to_pickle('user_stats_df.pkl')

        user_stats_df = pd.read_pickle('user_stats_df.pkl')

        # feature_corr.calculate_corr(tracks_audio_features.drop(['track_id'], axis=1))
        dataset_preparation.scale_dataframe(tracks_audio_features.drop(['track_id', 'mode', 'time_signature'], axis=1))

    main()
