def solution(genres, plays):
    answer = []
    album = {}
    for index, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in album:
            album[genre] = [play, []]
        else:
            album[genre][0] += play
        album[genre][1].append((index, play))

    album = sorted(album.items(), key=lambda x: x[1], reverse=True)
    
    for _, rank in album:
        rank = sorted(rank[1], key=lambda x: (-x[1], x[0])) 
        answer += [index[0] for index in rank[:2]]
        
    return answer