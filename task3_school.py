school = [{'school_class': '1a', 'scores': [5, 5, 5, 4, 3]},
          {'school_class': '1b', 'scores': [5, 4, 5, 5, 4, 5]},
          {'school_class': '2a1', 'scores': [4, 3, 4, 5, 4, 4, 5, 4]},
          {'school_class': '2b', 'scores': [5, 5, 5, 5, 3, 2, 4, 5, 2, 3]}
          ]


def count_marks(marks_list):

    classes = dict()
    total_av_scores = list()

    for school_class in marks_list:
        cls_avg_score = sum(school_class["scores"])/len(school_class["scores"])
        classes[school_class["school_class"]] = cls_avg_score
        total_av_scores.append(cls_avg_score)

    return classes, sum(total_av_scores)/len(total_av_scores)


def main():

    classes, total_av_scores = count_marks(school)

    for school_class in classes.items():
        print(f"В классе {school_class[0]} средний балл {school_class[1]:.2f}")

    print(f"Средний балл по школе {total_av_scores:.2f}")


if __name__ == '__main__':
    main()
