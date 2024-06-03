def solution(genres, plays):
    from collections import defaultdict
    
    # 1. 각 장르별 총 재생 횟수 계산
    genre_play_counts = defaultdict(int)
    for genre, play in zip(genres, plays):
        genre_play_counts[genre] += play
    
    # 2. 장르별로 노래들을 재생 횟수와 고유 번호를 기준으로 정렬
    genre_to_songs = defaultdict(list)
    for i, (genre, play) in enumerate(zip(genres, plays)):
        genre_to_songs[genre].append((play, i))
    
    for genre in genre_to_songs:
        genre_to_songs[genre].sort(key=lambda x: (-x[0], x[1]))
    
    # 3. 장르별로 상위 두 곡씩을 선택하여 결과 리스트에 추가
    sorted_genres = sorted(genre_play_counts.keys(), key=lambda x: genre_play_counts[x], reverse=True)
    
    best_music = []
    for genre in sorted_genres:
        best_music.extend([song[1] for song in genre_to_songs[genre][:2]])
    
    return best_music
