import json
import ast


def read_json_data(path):
    with open(path) as f:
        data = json.load(f)
        f.close()
        return data


def create_data_dicts(json_data):
    dicts = []
    for item in json_data:
        entry = {}
        entry['name'] = item['title']
        entry['text'] = item['summary']
        entry['url'] = ast.literal_eval(item['link'])[1]['href']
        dicts.append(entry)
    return dicts


def extract_info_from_predictions(answers):
    results = []
    predictions = answers['answers']
    for pred in predictions:
        res = {}
        res['answer'] = pred['answer']
        res['score'] = pred['score']
        res['context'] = pred['context']
        res['paper'] = pred['meta']
        results.append(res)
    return results
