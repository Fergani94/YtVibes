import json
import ast
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import  KeywordsOptions, SentimentOptions, EmotionOptions,Features
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

#Receive a comment as an arg, goes into Watson NLU and bring to us the overall sentiment of the comments
def getScore(comment):
    authenticator = IAMAuthenticator('YOUR API KEY')
    service = NaturalLanguageUnderstandingV1(
        version='2018-03-16',
        authenticator=authenticator)
    service.set_service_url('https://gateway.watsonplatform.net/natural-language-understanding/api')

    response = service.analyze(
        text=comment,
        features=Features(sentiment=SentimentOptions(),
                          keywords=KeywordsOptions(),emotion=EmotionOptions())).get_result()
    result = ast.literal_eval(json.dumps(response))
    final = result["sentiment"]["document"]["score"]*100
    return final