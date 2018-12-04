school = [{'school_class': '1a', 'scores': [5,5,5,4,3]}, {'school_class': '1b', 'scores': [5,4,5,5,4,5]}, 
		  {'school_class': '2a1', 'scores': [4,3,4,5,4,4,5,4]}, {'school_class': '2b', 'scores': [5,5,5,5,3,2,4,5,2,3]}]
import scipy

school_mean = scipy.mean([scipy.mean(item['scores']) for item in school])
print('School average grade point = %s' % round(school_mean, 2))


classes = [scipy.mean(item['scores']) for item in school]
for cls in classes:
    print(round(cls,2))
# А как сделать, чтобы он каждому значению класс подставлял?