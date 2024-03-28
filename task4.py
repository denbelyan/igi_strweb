def function_task4():
   """doc"""
   string = "So she was considering in her own mind, as well as she could, for the hot day made her feel very sleepy and stupid, whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her."
   words = [word.strip("," ".") for word in string.split()]

   even_len_words = [word for word in words if len(word)%2==0]
   print ("Words with an even number of letters:\n", even_len_words)

   a_started_words = [word for word in words if word.startswith('a') or word.startswith('A')]
   shortest_a_started_word = min (a_started_words , key = len)
   print ("The shortest word, started with 'a' is ", shortest_a_started_word)

   words_sorted_len = sorted (words, key = len , reverse = True)
   print("All words sorted by length in reverse order: \n" , words_sorted_len)