# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

--- MusicVibeFinder 1.0

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

--- This recommender suggests songs from a small catalog. It tries to match a user's genre, mood, energy, and tempo. It is for classroom exploration, not real users.

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

--- Each song uses genre, mood, energy, and tempo. The user gives a favorite genre, favorite mood, target energy, and target tempo.The model adds points for exact genre and mood matches. It also adds more points when the song energy and tempo are close to the user's target. I changed the starter logic so energy matters more and tempo is now part of the score.

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

--- The catalog has 18 songs. It includes pop, lofi, rock, ambient, jazz, classical, hip-hop, and more. It also includes moods like happy, focused, intense, calm, and moody. The dataset is small, so some genres only appear once. It does not fully cover all musical tastes.

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

--- It works well when the user wants a clear vibe. It does a good job for users who want happy pop, calm lofi, or intense rock. It also gives simple and easy-to-read reasons for each choice.

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

--- It has a few limits because its does not use features like acousticness, valence, and danceability. And it may also overemphasize energy and exact matches which may favor certain user profiles and may prove to be a disadvantage to certain user profiles. And since the catalog is small and some genres appear only once, the model can easily miss reasonable matches.

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

--- I tested High-Energy Pop, Chill Lofi, Deep Intense Rock, Conflicted Energy vs Mood, Alias Mismatch, and Boundary Case Zero Energy. I compared the top songs for each profile. I looked for songs that matched the profile in a way that made sense. I was surprised that Gym Hero kept showing up for several profiles. That happened because energy and tempo had a strong effect on the score.

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

--- I would add more songs to the catalog. I would use more features like acousticness and valence in the score. I would also improve diversity so the top results do not feel too similar.

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

--- My biggest learning moment was seeing how a simple score can still shape the whole experience. AI tools helped me move faster and test ideas, but I still had to double-check the scoring math and the final rankings. I was surprised that a few simple rules could still feel like real recommendations when the top songs matched the user's vibe. If I kept going, I would add more song features, improve diversity, and make the results less dependent on exact labels.
