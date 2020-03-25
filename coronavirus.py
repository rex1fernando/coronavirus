import twint

c = twint.Config()

c.Username = "HealthySCC"
c.Since = "2020-01-15"
c.Store_object = True
c.Hide_output = True
twint.run.Search(c)

for tweet in twint.output.tweets_list:
    if "coronavirus" in tweet.tweet: 
        print(tweet.datestamp) 
        print(tweet.tweet) 
