#Petar Ralevski 
import json
from datetime import datetime

def filter_reviews_by_rating(reviews, minimum_rating):
    filtered_reviews = []
    for review in reviews:
        if int(review["rating"]) >= int(minimum_rating):
            filtered_reviews.append(review)
    return filtered_reviews

def order_reviews_by_rating(order, reviews):
    if order == "Highest first":
        reviews.sort(key=lambda r : r["rating"], reverse=True)
    elif order == "Lowest first":
        reviews.sort(key=lambda r : r["rating"], reverse=False)
    return reviews    

def prioritize_reviews(reviews, args):
    reviews_with_text = []
    reviews_without_text = []
    order_by_rating = args["orderByRating"]
    minimum_rating = args["minimumRating"]
    
    for review in reviews:
        if review["reviewText"] != "":
            reviews_with_text.append(review)
        else:
            reviews_without_text.append(review)  
    
    reviews_with_text = order_reviews_by_rating(order_by_rating, reviews_with_text)
    reviews_without_text = order_reviews_by_rating(order_by_rating, reviews_without_text)

    if minimum_rating: 
        reviews_without_text = filter_reviews_by_rating(reviews_without_text, minimum_rating)   
        reviews_with_text = filter_reviews_by_rating(reviews_with_text, minimum_rating) 
        
    prioritized_reviews = reviews_with_text + reviews_without_text
    return prioritized_reviews

def sort_and_filter_reviews(data, args):
    order_by_rating = args["orderByRating"]
    minimum_rating = args["minimumRating"]
    prioritize_by_text = args["prioritizeByText"]
    order_by_date = args["orderByDate"]
    
    data = order_reviews_by_rating(order_by_rating, data)

    if minimum_rating:
        data = filter_reviews_by_rating(data, minimum_rating)

    if prioritize_by_text == "Yes":
        data = prioritize_reviews(data, args)
        
    if order_by_date == "Newest First":
        data = sorted(data, key=lambda x: datetime.strptime(x['reviewCreatedOnDate'], '%Y-%m-%dT%H:%M:%S%z'))
    elif order_by_date == "Oldest First":
        data = sorted(data, key=lambda x: datetime.strptime(x['reviewCreatedOnDate'], '%Y-%m-%dT%H:%M:%S%z'), reverse=True)
    
    return data


def readJson(location):
    with open(location, 'r') as myfile:
        data = json.load(myfile)
    return data