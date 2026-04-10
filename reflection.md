# Reflection

## Profiles Tested

I tested these user profiles:
- High-Energy Pop
- Chill Lofi
- Deep Intense Rock
- Conflicted Energy vs Mood
- Alias Mismatch
- Boundary Case Zero Energy

## What Surprised Me

The thing that shocked me was that Gym Hero kept appearing even though the user never requested any rock music or intense songs. This meant that the tempo and energy were playing significant roles in the ranking process, hence enabling the song to rank highly despite not being rock music.

## Profile Comparisons
High-Energy Pop vs Chill Lofi: since the two profiles differ from each other, the best songs according to them will also be different. The former will retain its Sunrise City due to matching pop, happiness, high energy level, and tempo, whereas the latter will get closer to Focus Flow by matching lo-fi and being focused. This is an expected result because the recommendation system starts with genre and mood identification, then picks songs with similar energy and tempo.

High-Energy Pop vs Deep Intense Rock: even with such opposite needs like happy pop music for one and intense rock music for another, both profiles may end up having the same song recommended to them. In the case described above, it would be Gym Hero due to its high energy level and similar tempo for the two profiles despite differing genres. This explains how some songs remain the same recommendation regardless of users' tastes.

Chill Lofi vs Alias Mismatch: both of these profiles got similar song suggestions. The reason for that is that the scorer takes into account favorite genres, favorite moods, and target energy but not additional alias information. Therefore, the apparent mismatch between these profiles does not affect song scoring at all. Thus, we know now that additional field values do not influence recommendations at all.

Conflicted Energy vs Mood vs Boundary Case Zero Energy: both of these profiles managed to pull songs mostly based on their energy and tempo rather than mood. For instance, such songs as "Gym Hero" and "Dawn Cathedral" get recommended because they are suitable due to energy and tempo even though they do not represent the mood of those profiles. It seems that due to very high energy coefficient, the model manages to neglect the mood part.

## What I Learned

This recommendor does not act in accordance with a deeper knowledge of the user’s taste preferences. Mostly because of the fact that it compares energy with labels; thus, a song such as “Gym Hero” will get recommended for listening in case a user requests something along the lines of Happy Pop and is in a rather energetic mood.