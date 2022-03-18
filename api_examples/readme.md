This folder contains some example API calls to show how we can use the Riot API to make calls which will provide us with the data we need to compile our dataset.

The match_history_example displays how we can obtain the last 10 games that a selected player has completed.
![Complete Data](./api_examples/match_history_example.png)

The champion_experience example displays how we can obtain the specified player's experience on the champion that they are playing.
![Complete Data](./api_examples/champion_experience.png)

The complete_data example displays how we can combine all of the previous examples together to pull all of the relevant data for building our dataset. It displays each player in the game, their win rate, their experience on the champion they are playing, and the win rate of the champion they are playing. Our model will use all of these features to predict which team is going to win prior to the game starting.
![Complete Data](./api_examples/complete_data.png)
