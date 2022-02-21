# Observations:
- Since the dataset was of the sentiment analysis, first I have removed all the labels, and all the train, text and val sets were concatenated into one dataset to just make it a clean text dataset.
- The 'create_vocab' function is same as the one used in the 'sentiment_analysis_rnn' file for creating the vocabulary, except for the fact the it can now be used in two ways:
    - one for creating the words vocabulary for 'next_word_predictor' model
    - second one for creating the vocabulary for 'next_character_predictor' model which will store a mapping for each and every character used in the dataset. 
    
    All of this can be done by just adjusting the 'r' parameter.
- The 'divide' function will create our required dataset, which will contain the required number of words/characters, mapped as numbers, as the input (given by the parameter 'n'), and just one of them as output
- For character predicting task, with input length 100, there were about 3.5 lacs data in the training set, and the model was having a hard time learning them (was taking a huge time, with quite high error), so the training set was reduced to 1 lacs, which should work, because (hopefully) it has enough data to capture most of the sentence pattern.
- The model layers can be clearly seen. The accuracy is just around 53 percent, which is not that good. Adding more LSTM or Dense layers, or more neurons didn't bring about much change except for incresed training time.
- After testing the model, the next code will take custom input (of length 'n-1') from user, and give their predictions upto the number of characters the user wants the predictions for.

# Improvements:
- A better dataset may be more useful. The following are expected from a better dataset:

    - The dataset with punctuations might be useful for both the models, because in that case, the prediction can go on until a full-stop is encountered to return a meaningful sentence.

- An improvement in model may be to use more neurons in the embedding layer, and also to use conv1d and pooling layers.
- Using more specialised RNN or LSTM cells such as GRU may also be useful

# Drawbacks:
- The 53% accuracy clearly shows that the model is not that well trained.
- As can be seen from the custom input section that when given the input, it completed 'th' with 'the', then continued with 'struggled to the struggled.....'. 
  
  This clearly shows that the model could not hold long term dependencies, thus making grammatical errors, but it succesfully held short term dependencies, thus it didn't make any spelling mistake. 
- Again the 'th' could also have been completed as 'thought', instead of 'the' (that would have been more meaningful with 'feeling'). The dataset should reflect all of these possible outcomes, with their respective inputs to make help the model output more meaningful results.
