import sys


def score_cruncher():
    '''
    takes the scores from argv,
    converts them to ints and gives acoording values
    '''
    print('=== PLayer Score Analytics ===')
    if len(sys.argv) == 1:
        print(
                'No Scores Provided! ',
                'Usage: python3 ft_score_analytics.py <score1> <score2> ...'
            )
        return
    scores = []
    for score in sys.argv:
        try:
            score_int = int(score)
            scores.append(score_int)
        except Exception:
            continue
    print(f'Scores Processed: {scores}')
    print(f'Total Players: {len(scores)}')
    print(f'Total Scores: {sum(scores)}')
    print(f'Average Score: {sum(scores) / len(scores)}')
    print(f'High Score: {max(scores)}')
    print(f'Low Score: {min(scores)}')
    print(f'Score range: {max(scores) - min(scores)}')


if __name__ == '__main__':
    score_cruncher()
