import json
import webbrowser
import os

score_file_path = "./pred.json"
annotate_file_path = "./annotate.txt"
score_file_pointer = open(score_file_path, "r", encoding="utf-8")
annotate_file_pointer = open(annotate_file_path, "w", encoding="utf-8")

score_data = json.load(score_file_pointer)

low_score_threshold = 0.2
middle_score_threshold = 0.7

low = 0
mid = 0
high = 0
# print(score_data)
for img_name, pred_res in score_data.items():
    # print(pred_res['text'])
    text = pred_res['text']
    score = pred_res['score']

    min_score = min(score)
    max_score = max(score)
    mean_score = sum(score) / len(score)

    if mean_score >= middle_score_threshold:
        high += 1
    elif mean_score >= low_score_threshold:
        mid += 1
    else:
        low += 1
    annotate_file_pointer.write(f"{img_name}\t{text}\n")

print(high, mid, low)
score_file_pointer.close()
annotate_file_pointer.close()

# html_filename = 'file:///' + os.getcwd() + "/" + "./anotation_latest.html"
# webbrowser.open_new_tab(html_filename)
