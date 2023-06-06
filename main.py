import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import pandas as pd
import spotify_user_access

if __name__ == "__main__":
    # client_credentials_manager = SpotifyClientCredentials(client_id='SPOTIPY_CLIENT_ID', client_secret='SPOTIPY_CLIENT_SECRET')
    # sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    def main():
        scope = ("playlist-read-private", "user-library-read", "user-top-read")
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

        user_tracks_df = spotify_user_access.get_tracks(sp)
        tracks_audio_features = spotify_user_access.get_audio_features(sp, user_tracks_df)

    main()
