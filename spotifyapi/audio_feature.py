""" This module provides the audio feature object """


class AudioFeature:
    def __init__(self, data):
        self._duration_ms = data['duration_ms']
        self._key = data['key']
        self._mode = data['mode']
        self._time_signature = data['time_signature']
        self._acousticness = data['acousticness']
        self._danceability = data['danceability']
        self._energy = data['energy']
        self._instrumentalness = data['instrumentalness']
        self._liveness = data['liveness']
        self._loudness = data['loudness']
        self._speechiness = data['speechiness']
        self._valence = data['valence']
        self._tempo = data['tempo']

    @property
    def duration_ms(self):
        """ The duration of the track in milliseconds. """
        return self._duration_ms

    @property
    def key(self):
        """
        The estimated overall key of the track. Integers map to pitches using standard Pitch Class notation.
        E.g. 0 = C, 1 = C♯/D♭, 2 = D, and so on. If no key was detected, the value is -1.
        """
        return self._key

    @property
    def mode(self):
        """
        Mode indicates the modality (major or minor) of a track, the type of scale from which its melodic content is
        derived. Major is represented by 1 and minor is 0.
        """
        return self._mode

    @property
    def time_signature(self):
        """
        An estimated overall time signature of a track. The time signature (meter) is a notational convention to specify
        how many beats are in each bar (or measure).
        """
        return self._time_signature

    @property
    def acousticness(self):
        """
        A confidence measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence the track
        is acoustic.
        """
        return self._acousticness

    @property
    def danceability(self):
        """
        Danceability describes how suitable a track is for dancing based on a combination of musical elements including
        tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is
        most danceable.
        """
        return self._danceability

    @property
    def energy(self):
        """
        Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically,
        energetic tracks feel fast, loud, and noisy. For example, death metal has high energy, while a Bach prelude
        scores low on the scale. Perceptual features contributing to this attribute include dynamic range, perceived
        loudness, timbre, onset rate, and general entropy.
        """
        return self._energy

    @property
    def instrumentalness(self):
        """
        Predicts whether a track contains no vocals. “Ooh” and “aah” sounds are treated as instrumental in this context.
        Rap or spoken word tracks are clearly “vocal”. The closer the instrumentalness value is to 1.0, the greater
        likelihood the track contains no vocal content. Values above 0.5 are intended to represent instrumental tracks,
        but confidence is higher as the value approaches 1.0.
        """
        return self._instrumentalness

    @property
    def liveness(self):
        """
        Detects the presence of an audience in the recording. Higher liveness values represent an increased probability
        that the track was performed live. A value above 0.8 provides strong likelihood that the track is live.
        """
        return self._liveness

    @property
    def loudness(self):
        """
        The overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track and are
        useful for comparing relative loudness of tracks. Loudness is the quality of a sound that is the primary
        psychological correlate of physical strength (amplitude). Values typical range between -60 and 0 db.
        """
        return self._loudness

    @property
    def speechiness(self):
        """
        Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the recording
        (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value. Values above 0.66 describe tracks
        that are probably made entirely of spoken words. Values between 0.33 and 0.66 describe tracks that may contain
        both music and speech, either in sections or layered, including such cases as rap music. Values below 0.33 most
        likely represent music and other non-speech-like tracks.
        """
        return self._speechiness

    @property
    def valence(self):
        """
        A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence
        sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative
        (e.g. sad, depressed, angry).
        """
        return self._valence

    @property
    def tempo(self):
        """
        The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or
        pace of a given piece and derives directly from the average beat duration.
        """
        return self._tempo
