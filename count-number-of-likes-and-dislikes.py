# Write a function to count the  number of likes and dislikes for a post

def count_votes(votes):

    likes = votes.count('like')
    dislike = votes.count('dislike')

    return {'likes': likes, 'dislikes': dislike}

votes = ['like', 'dislike', 'like', 'like']
print(count_votes(votes))