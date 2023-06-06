import pandas as pd


def get_tracks(sp) -> pd.DataFrame():
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


def get_artist(sp, user_tracks_df: pd.DataFrame()) -> pd.DataFrame():
    genres = []
    artist_name = []

    for artist in user_tracks_df['artist_id']:
        try:
            genres.append(sp.artist(artist).get('genres'))
            artist_name.append(sp.artist(artist).get('name'))
        except Exception as e:
            print(e)

    df = pd.DataFrame()
    df['genres'] = genres
    df['artist_name'] = artist_name
    df['artist_id'] = user_tracks_df['artist_id']

    return df


def get_audio_features(sp, user_tracks_df: pd.DataFrame()) -> pd.DataFrame():
    danceability = []
    energy = []
    loudness = []
    speechiness = []
    acousticness = []
    instrumentalness = []
    liveness = []
    valence = []
    tempo = []
    duration_ms = []
    mode = []
    time_signature = []

    for track in user_tracks_df['track_id']:
        try:
            danceability.append(sp.audio_features(track)[0].get('danceability'))
            energy.append(sp.audio_features(track)[0].get('energy'))
            loudness.append(sp.audio_features(track)[0].get('loudness'))
            speechiness.append(sp.audio_features(track)[0].get('speechiness'))
            acousticness.append(sp.audio_features(track)[0].get('acousticness'))
            instrumentalness.append(sp.audio_features(track)[0].get('instrumentalness'))
            liveness.append(sp.audio_features(track)[0].get('liveness'))
            valence.append(sp.audio_features(track)[0].get('valence'))
            tempo.append(sp.audio_features(track)[0].get('tempo'))
            duration_ms.append(sp.audio_features(track)[0].get('duration_ms'))
            mode.append(sp.audio_features(track)[0].get('mode'))
            time_signature.append(sp.audio_features(track)[0].get('time_signature'))

        except Exception as e:
            print(e)

    df = pd.DataFrame()
    df['track_id'] = user_tracks_df['track_id']
    df['danceability'] = danceability
    df['energy'] = energy
    df['loudness'] = loudness
    df['speechiness'] = speechiness
    df['acousticness'] = acousticness
    df['instrumentalness'] = instrumentalness
    df['liveness'] = liveness
    df['valance'] = valence
    df['tempo'] = tempo
    df['duration_ms'] = duration_ms
    df['mode'] = mode
    df['time_signature'] = time_signature

    return df
